import re
import subprocess
from pathlib import Path

def _git(repo: Path, *args: str) -> str:
    res = subprocess.run(["git", "-C", str(repo), *args],
                         capture_output=True, text=True, check=True)
    return res.stdout.strip()

def _glob_to_regex(glob: str) -> re.Pattern:
    # ** => 디렉터리 가로지름, * => 한 세그먼트 내. 순서대로 치환.
    g = glob.replace(".", r"\.")
    g = g.replace("**/", "\x00").replace("**", "\x01").replace("*", "[^/]*")
    g = g.replace("\x00", "(?:.*/)?").replace("\x01", ".*")
    return re.compile("^" + g + "$")

def _matches_any(path: str, globs: list[str]) -> bool:
    return any(_glob_to_regex(g).match(path) for g in globs)

def head_sha(repo: Path) -> str:
    return _git(repo, "rev-parse", "HEAD")

def pull(repo: Path) -> None:
    # 새벽 무인 실행: 충돌 시 조용히 건너뛴다(다음 실행에서 재시도)
    try:
        _git(repo, "pull", "--ff-only", "--quiet")
    except subprocess.CalledProcessError:
        pass

def changed_md_files(repo: Path, since_sha: str | None, globs: list[str]) -> list[str]:
    if since_sha is None:
        candidates = _git(repo, "ls-files").splitlines()
    else:
        candidates = _git(repo, "diff", "--name-only", "--diff-filter=ACMR",
                          f"{since_sha}", "HEAD").splitlines()
    out = [p for p in candidates
           if _matches_any(p, globs) and (repo / p).exists()]
    return sorted(out)
