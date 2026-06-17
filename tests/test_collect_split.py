import json
from pathlib import Path

import pytest

from pipeline import collect


def _setup(root: Path, monkeypatch, *, files, head="head1", char_budget, queue=None):
    """repo 'proj' 를 가진 collect 환경을 만든다. git/transcript 는 가짜로 대체."""
    (root / "config").mkdir(parents=True, exist_ok=True)
    (root / "config" / "sources.json").write_text(json.dumps({
        "base_path": str(root / "codes"),
        "transcripts_dir": str(root / "tx"),
        "char_budget": char_budget,
        "repos": [{"name": "proj", "globs": ["docs/**/*.md"]}],
    }), encoding="utf-8")

    docs = root / "codes" / "proj" / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    for f in files:
        (root / "codes" / "proj" / f).parent.mkdir(parents=True, exist_ok=True)
        (root / "codes" / "proj" / f).write_text("x" * 100, encoding="utf-8")

    if queue is not None:
        (root / "state").mkdir(parents=True, exist_ok=True)
        from pipeline import config
        config.save_state({"repos": {}, "repo_queue": queue, "transcripts": {}, "last_run": None},
                          root / "state" / "progress.json")

    monkeypatch.setattr(collect.gitutil, "pull", lambda repo: None)
    monkeypatch.setattr(collect.gitutil, "head_sha", lambda repo: head)
    monkeypatch.setattr(collect.gitutil, "changed_md_files",
                        lambda repo, sha, globs: list(files))
    monkeypatch.setattr(collect.transcripts, "new_messages", lambda d, off: ([], dict(off)))


def _manifest(root):
    return json.loads(next((root / "state").glob("consumed-*.json")).read_text(encoding="utf-8"))


def test_partial_consumption_queues_remaining(tmp_path, monkeypatch):
    # 3개 파일(각 ~100자) 중 예산상 1개만 소비 → 나머지 2개는 repo_queue 로 기록
    _setup(tmp_path, monkeypatch, files=["docs/a.md", "docs/b.md", "docs/c.md"],
           head="head1", char_budget=150)
    result = collect.collect(root=tmp_path)
    m = _manifest(tmp_path)
    # 부분 소비 → SHA 전진 금지
    assert "proj" not in m["repos"]
    # 남은 파일은 queue 에 target=head 로 기록
    assert m["repo_queue"]["proj"]["target"] == "head1"
    assert m["repo_queue"]["proj"]["remaining"] == ["docs/b.md", "docs/c.md"]
    assert result["item_count"] == 1   # 파일 단위 1개만 소비


def test_continues_from_queue_without_rediff(tmp_path, monkeypatch):
    # 같은 head 의 queue 가 있으면 changed_md_files 를 무시하고 남은 파일을 이어서 소진한다
    for f in ("docs/b.md", "docs/c.md", "docs/z.md"):
        p = tmp_path / "codes" / "proj" / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("y" * 100, encoding="utf-8")
    (tmp_path / "config").mkdir(parents=True, exist_ok=True)
    (tmp_path / "config" / "sources.json").write_text(json.dumps({
        "base_path": str(tmp_path / "codes"),
        "transcripts_dir": str(tmp_path / "tx"),
        "char_budget": 100000,
        "repos": [{"name": "proj", "globs": ["docs/**/*.md"]}],
    }), encoding="utf-8")
    from pipeline import config
    (tmp_path / "state").mkdir(parents=True, exist_ok=True)
    config.save_state({"repos": {}, "last_run": None, "transcripts": {},
                       "repo_queue": {"proj": {"target": "head1",
                                               "remaining": ["docs/b.md", "docs/c.md"]}}},
                      tmp_path / "state" / "progress.json")
    monkeypatch.setattr(collect.gitutil, "pull", lambda repo: None)
    monkeypatch.setattr(collect.gitutil, "head_sha", lambda repo: "head1")
    # 만약 이게 호출되면 z.md 가 섞여 테스트가 깨진다 — queue 를 써야 함을 증명
    monkeypatch.setattr(collect.gitutil, "changed_md_files",
                        lambda repo, sha, globs: ["docs/z.md"])
    monkeypatch.setattr(collect.transcripts, "new_messages", lambda d, off: ([], dict(off)))

    result = collect.collect(root=tmp_path)
    m = _manifest(tmp_path)
    assert result["item_count"] == 2          # b.md + c.md, z.md 아님
    assert m["repos"]["proj"] == "head1"      # 전부 소진 → SHA 전진
    assert "proj" not in m["repo_queue"]
