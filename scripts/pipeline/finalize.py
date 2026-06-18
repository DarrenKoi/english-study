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
    state["repos"].update(manifest.get("repos", {}))
    state["transcripts"].update(manifest.get("transcripts", {}))
    # 부분 소비된 repo 는 남은 파일을 queue 에 기록, 전부 소진된 repo(=repos 전진)는 queue 제거.
    state["repo_queue"].update(manifest.get("repo_queue", {}))
    for name in manifest.get("repos", {}):
        state["repo_queue"].pop(name, None)
    # 오늘 처리한 문서 원장: 성공(=finalize)했을 때만 승격해 같은 날 재실행 중복을 막는다.
    # 날짜가 바뀌면 리셋하므로 매일 첫 실행은 윈도 전체를 다시 훑는다.
    dt = state.get("docs_today") or {}
    prev = set(dt.get("keys", [])) if dt.get("date") == today else set()
    state["docs_today"] = {"date": today,
                           "keys": sorted(prev | set(manifest.get("docs", [])))}
    state["last_run"] = today
    config.save_state(state, root / "state" / "progress.json")

    # 처리된 spool 노트를 spool/done 으로 날짜 접두사 붙여 아카이브 (멱등성)
    done_dir = root / "spool" / "done"
    done_dir.mkdir(parents=True, exist_ok=True)
    for rel in manifest.get("spool", []):
        src = root / rel
        if src.exists():
            shutil.move(str(src), str(done_dir / f"{today}-{src.name}"))

    _git_commit_push(root, f"study: nightly digest {today}")
    return {"committed": True, "today": today}

if __name__ == "__main__":
    print(finalize())
