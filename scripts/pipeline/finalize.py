import json
import shutil
import subprocess
from datetime import date
from pathlib import Path

from pipeline import config

def _git_commit_push(root: Path, msg: str) -> None:
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=False)
    subprocess.run(["git", "-C", str(root), "commit", "-m", msg], check=False)
    subprocess.run(["git", "-C", str(root), "push"], check=False)

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

    _git_commit_push(root, f"study: nightly digest {today}")
    return {"committed": True, "today": today}

if __name__ == "__main__":
    print(finalize())
