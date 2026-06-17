import json
import os
import time
from pathlib import Path

from pipeline import collect


def _write(path: Path, text: str, *, age_days: float = 0.0) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if age_days:
        t = time.time() - age_days * 86400
        os.utime(path, (t, t))


def _sources(root: Path, codes: Path, **extra) -> None:
    (root / "config").mkdir(parents=True, exist_ok=True)
    cfg = {
        "base_path": str(codes),
        "transcripts_dir": str(root / "tx"),
        "char_budget": 100000,
        "exclude_projects": ["english-study"],
    }
    cfg.update(extra)
    (root / "config" / "sources.json").write_text(json.dumps(cfg), encoding="utf-8")


def _no_transcripts(monkeypatch):
    monkeypatch.setattr(collect.transcripts, "new_messages", lambda d, off: ([], dict(off)))


def _no_git(monkeypatch):
    monkeypatch.setattr(collect.gitutil, "pull", lambda repo: None)


def _manifest(root):
    return json.loads(next((root / "state").glob("consumed-*.json")).read_text(encoding="utf-8"))


def _batch(root):
    return next((root / "state").glob("batch-*.md")).read_text(encoding="utf-8")


def test_collect_discovers_recent_docs_across_projects(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)

    # 최근(윈도 안) 문서들 — 프로젝트 루트 docs, 깊게 중첩된 docs, .txt, shared_docs
    _write(codes / "projA" / "docs" / "fresh.md", "Let's circle back to this.")
    _write(codes / "projB" / "service" / "sub" / "docs" / "deep.md", "A deeply nested doc.")
    _write(codes / "projB" / "docs" / "notes.txt", "Plain text note.")
    _write(codes / "projC" / "shared_docs" / "shared.md", "Shared across teams.")
    # 제외 대상들
    _write(codes / "projA" / "docs" / "stale.md", "Old news.", age_days=30)          # 윈도 밖
    _write(codes / "projA" / "src" / "code.md", "Not in a docs folder.")             # docs 폴더 아님
    _write(codes / "projA" / "docs" / "node_modules" / "junk.md", "vendored noise")  # 프룬 대상
    _write(codes / "projA" / "docs" / "readme.rst", "wrong extension")               # 확장자 밖
    _write(codes / "english-study" / "docs" / "self.md", "our own output")           # 제외 프로젝트

    result = collect.collect(root=root)
    batch = _batch(root)

    assert "Let's circle back to this." in batch
    assert "A deeply nested doc." in batch
    assert "Plain text note." in batch
    assert "Shared across teams." in batch
    # 제외된 것들은 배치에 없어야 한다
    for absent in ("Old news.", "Not in a docs folder.", "vendored noise",
                   "wrong extension", "our own output"):
        assert absent not in batch
    # provenance 는 repo:<project> <상대경로>
    assert "repo:projA docs/fresh.md" in batch
    assert "repo:projB service/sub/docs/deep.md" in batch

    assert result["item_count"] == 4
    m = _manifest(root)
    assert m["repos"] == {}            # 더 이상 SHA 를 전진시키지 않는다
    assert m["repo_queue"] == {}


def test_budget_prefers_newest_and_defers_rest(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    # 한 단위(~100자 블록)만 들어갈 작은 예산
    _sources(root, codes, char_budget=140)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)

    _write(codes / "proj" / "docs" / "older.md", "o" * 100, age_days=5)
    _write(codes / "proj" / "docs" / "newer.md", "n" * 100, age_days=1)

    result = collect.collect(root=root)
    batch = _batch(root)

    # 최신순 우선: 예산이 1개만 허용하면 newer 가 들어가고 older 는 미뤄진다
    assert "n" * 100 in batch
    assert "o" * 100 not in batch
    assert result["item_count"] == 1
    assert result["deferred"] == 1


def test_spool_notes_take_priority(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    (root / "spool").mkdir(parents=True, exist_ok=True)
    (root / "spool" / "q.md").write_text("affect vs effect 차이?", encoding="utf-8")
    _write(codes / "proj" / "docs" / "fresh.md", "Document body.")

    result = collect.collect(root=root)
    m = _manifest(root)

    assert m["spool"] == ["spool/q.md"]
    assert result["item_count"] == 2   # spool 노트 + 문서 1개
