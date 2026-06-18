import subprocess
from pathlib import Path
import pytest
from pipeline import gitutil

def _run(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True,
                   capture_output=True, text=True)

@pytest.fixture
def repo(tmp_path):
    r = tmp_path / "proj"
    r.mkdir()
    _run(r, "init", "-q")
    _run(r, "config", "user.email", "t@t.t")
    _run(r, "config", "user.name", "t")
    (r / "README.md").write_text("readme", encoding="utf-8")
    _run(r, "add", "-A")
    _run(r, "commit", "-q", "-m", "c1")
    return r

def test_pull_is_silent_without_upstream(repo):
    # 업스트림이 없는 repo 에서도 pull 은 예외 없이 조용히 끝나야 한다(무인 실행 안전).
    gitutil.pull(repo)   # 예외가 나면 테스트 실패
