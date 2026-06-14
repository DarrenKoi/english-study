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
    (r / "docs").mkdir()
    (r / "docs" / "a.md").write_text("first", encoding="utf-8")
    (r / "README.md").write_text("readme", encoding="utf-8")
    _run(r, "add", "-A")
    _run(r, "commit", "-q", "-m", "c1")
    return r

def test_glob_to_regex_matches_nested():
    assert gitutil._glob_to_regex("docs/**/*.md").match("docs/x/y.md")
    assert gitutil._glob_to_regex("docs/**/*.md").match("docs/a.md")
    assert not gitutil._glob_to_regex("docs/**/*.md").match("src/a.md")
    assert gitutil._glob_to_regex("**/*.md").match("anything/here.md")

def test_head_sha_returns_40_hex(repo):
    sha = gitutil.head_sha(repo)
    assert len(sha) == 40

def test_changed_md_since_none_returns_all_matching(repo):
    files = gitutil.changed_md_files(repo, None, ["docs/**/*.md"])
    assert files == ["docs/a.md"]   # README.md 는 glob 밖

def test_changed_md_since_sha_returns_only_new(repo):
    old = gitutil.head_sha(repo)
    (repo / "docs" / "b.md").write_text("second", encoding="utf-8")
    _run(repo, "add", "-A")
    _run(repo, "commit", "-q", "-m", "c2")
    files = gitutil.changed_md_files(repo, old, ["docs/**/*.md"])
    assert files == ["docs/b.md"]
