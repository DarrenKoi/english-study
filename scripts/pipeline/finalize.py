import json
import shutil
import subprocess
from datetime import date, timedelta
from pathlib import Path

from pipeline import config, review

def _git_commit_push(root: Path, msg: str) -> None:
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=False)
    subprocess.run(["git", "-C", str(root), "commit", "-m", msg], check=False)
    subprocess.run(["git", "-C", str(root), "push"], check=False)

def prune_old_daily(root: Path, today: str, retention_days: int = 20) -> list[str]:
    """`daily/<YYYY-MM-DD>/` 중 today 보다 retention_days 넘게 오래된 폴더를 지운다.

    경계(정확히 retention_days 전)는 보존하고, 날짜로 못 읽는 폴더는 건드리지 않는다.
    지운 폴더 이름(날짜)을 정렬해 돌려준다.
    """
    daily = Path(root) / "daily"
    if not daily.is_dir():
        return []
    cutoff = date.fromisoformat(today) - timedelta(days=retention_days)
    removed: list[str] = []
    for child in sorted(daily.iterdir()):
        if not child.is_dir():
            continue
        try:
            folder_date = date.fromisoformat(child.name)
        except ValueError:
            continue
        if folder_date < cutoff:
            shutil.rmtree(child)
            removed.append(child.name)
    return removed

def finalize(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()

    manifest_path = root / "state" / f"consumed-{today}.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    state = config.load_state(root / "state" / "progress.json")
    state["transcripts"].update(manifest.get("transcripts", {}))
    # 처리한 문서 원장(경로→키): 성공(=finalize)했을 때만 승격한다. 내용이 바뀌지 않은
    # 문서는 다음 날 이후로도 다시 처리하지 않고, 파일이 바뀌면 키가 달라져 갱신된다.
    seen = state.get("docs_seen") or {}
    seen.update(manifest.get("docs", {}))
    state["docs_seen"] = seen
    state["last_run"] = today
    config.save_state(state, root / "state" / "progress.json")

    # 복습한 표현을 영구 ledger(reviewed.json)에 전진시킨다 — docs_seen 과 동일 규율.
    reviewed = manifest.get("reviewed") or []
    if reviewed:
        review.mark_reviewed(root, reviewed, today)

    # 처리된 spool 노트를 spool/done 으로 날짜 접두사 붙여 아카이브 (멱등성).
    # 같은 날 같은 이름의 노트가 또 오면 기존 아카이브를 덮어쓰지 않도록 -2,-3… 을 붙인다.
    done_dir = root / "spool" / "done"
    done_dir.mkdir(parents=True, exist_ok=True)
    for rel in manifest.get("spool", []):
        src = root / rel
        if not src.exists():
            continue
        dest = done_dir / f"{today}-{src.name}"
        n = 2
        while dest.exists():
            dest = done_dir / f"{today}-{src.stem}-{n}{src.suffix}"
            n += 1
        shutil.move(str(src), str(dest))

    # 오래된 daily 폴더 정리 (다시 안 볼 자료). config 없으면 기본 20일.
    try:
        cfg = config.load_config(root / "config" / "sources.json")
        retention = int(cfg.get("daily_retention_days", 20))
    except FileNotFoundError:
        retention = 20
    pruned = prune_old_daily(root, today, retention)

    _git_commit_push(root, f"study: nightly digest {today}")
    return {"committed": True, "today": today, "pruned": pruned}

if __name__ == "__main__":
    print(finalize())
