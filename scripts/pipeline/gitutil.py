import subprocess
from pathlib import Path

def _git(repo: Path, *args: str) -> str:
    res = subprocess.run(["git", "-C", str(repo), *args],
                         capture_output=True, text=True, check=True)
    return res.stdout.strip()

def pull(repo: Path) -> None:
    # 무인 실행: 충돌·업스트림 없음 등은 조용히 건너뛴다(다음 실행에서 재시도)
    try:
        _git(repo, "pull", "--ff-only", "--quiet")
    except subprocess.CalledProcessError:
        pass
