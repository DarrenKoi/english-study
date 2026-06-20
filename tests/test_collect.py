import json
import os
import time
from pathlib import Path

from pipeline import collect, finalize as finalize_mod


def _finalize(root, today, monkeypatch):
    """성공 시 진행 상태를 전진시키는 finalize 를 git 없이 돌린다(원장 승격 확인용)."""
    monkeypatch.setattr(finalize_mod, "_git_commit_push", lambda root, msg: None)
    finalize_mod.finalize(root=root, today=today)


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
    # docs 는 경로→키 매핑(SHA 추적은 사라졌다). 발견한 4개 문서가 모두 들어간다.
    assert set(m["docs"]) == {
        "projA/docs/fresh.md", "projB/service/sub/docs/deep.md",
        "projB/docs/notes.txt", "projC/shared_docs/shared.md"}


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


def test_rerun_without_finalize_recollects(tmp_path, monkeypatch):
    # finalize(=성공) 전에는 원장이 전진하지 않으므로, LLM 실패 후 같은 날 재실행은
    # 그 문서들을 다시 집어야 한다(처리되지 않은 문서가 유실되면 안 됨).
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _write(codes / "proj" / "docs" / "a.md", "First doc body.")
    _write(codes / "proj" / "docs" / "b.md", "Second doc body.")

    first = collect.collect(root=root, today="2026-06-18")
    assert first["item_count"] == 2
    # finalize 를 부르지 않음(LLM 실패 시뮬레이션)
    second = collect.collect(root=root, today="2026-06-18")
    assert second["item_count"] == 2          # 재수집됨 — 유실 없음
    assert "First doc body." in _batch(root)


def test_same_day_rerun_skips_after_successful_finalize(tmp_path, monkeypatch):
    # finalize 가 성공한 뒤의 같은 날 재실행은 이미 처리한 문서를 다시 넣지 않는다.
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _write(codes / "proj" / "docs" / "a.md", "First doc body.")
    _write(codes / "proj" / "docs" / "b.md", "Second doc body.")

    first = collect.collect(root=root, today="2026-06-18")
    assert first["item_count"] == 2
    _finalize(root, "2026-06-18", monkeypatch)

    second = collect.collect(root=root, today="2026-06-18")
    assert second["item_count"] == 0          # 처리 완료 문서 → 재수집 안 함
    assert "First doc body." not in _batch(root)


def test_same_day_rerun_picks_up_edited_doc(tmp_path, monkeypatch):
    # 내용이 바뀐 문서는 같은 날이라도 다시 수집한다(mtime/크기가 달라지므로).
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    doc = codes / "proj" / "docs" / "a.md"
    _write(doc, "Original body.")

    collect.collect(root=root, today="2026-06-18")
    _finalize(root, "2026-06-18", monkeypatch)
    _write(doc, "Edited body, now clearly different and longer.")   # 같은 날 수정
    again = collect.collect(root=root, today="2026-06-18")

    assert again["item_count"] == 1
    assert "Edited body, now clearly different and longer." in _batch(root)


def test_new_day_skips_unchanged_doc(tmp_path, monkeypatch):
    # 영구 원장이므로 날짜가 바뀌어도 내용이 그대로인 문서는 다시 처리하지 않는다.
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _write(codes / "proj" / "docs" / "a.md", "Body.")

    collect.collect(root=root, today="2026-06-18")
    _finalize(root, "2026-06-18", monkeypatch)
    next_day = collect.collect(root=root, today="2026-06-19")
    assert next_day["item_count"] == 0            # 변경 없는 문서 → 재수집 안 함


def test_new_day_picks_up_edited_doc(tmp_path, monkeypatch):
    # 날이 바뀌고 내용이 바뀐 문서는 다시 수집한다(키가 달라지므로).
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    doc = codes / "proj" / "docs" / "a.md"
    _write(doc, "Body.")

    collect.collect(root=root, today="2026-06-18")
    _finalize(root, "2026-06-18", monkeypatch)
    _write(doc, "Body, revised the next day with more content.")
    next_day = collect.collect(root=root, today="2026-06-19")
    assert next_day["item_count"] == 1            # 내용 변경 → 재수집


def _index(root: Path, body: str) -> None:
    (root / "notes").mkdir(parents=True, exist_ok=True)
    (root / "notes" / "index.md").write_text(body, encoding="utf-8")


def test_empty_day_backlog_pass_picks_aged_doc(tmp_path, monkeypatch):
    # 정상 윈도(7일) 밖, 백로그 윈도(14일) 안의 미처리 문서를 빈 날에 따라잡는다.
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _write(codes / "proj" / "docs" / "aged.md", "Aged backlog body.", age_days=10)

    result = collect.collect(root=root)
    assert result["mode"] == "backlog"
    assert result["item_count"] == 1
    assert "Aged backlog body." in _batch(root)
    assert set(_manifest(root)["docs"]) == {"proj/docs/aged.md"}


def test_empty_day_review_pass_when_no_backlog(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14, digest_max=7)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _index(root,
           "- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17\n"
           "- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20\n")

    result = collect.collect(root=root)
    assert result["mode"] == "review"
    assert result["item_count"] == 1            # 복습 단위 하나
    m = _manifest(root)
    assert m["reviewed"] == ["backstop", "blast radius"]
    assert "backstop" in _batch(root)


def test_empty_day_returns_empty_when_nothing(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)

    result = collect.collect(root=root)
    assert result["mode"] == "empty"
    assert result["item_count"] == 0


def test_review_pass_skips_already_reviewed(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _index(root,
           "- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17\n"
           "- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20\n")
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state" / "reviewed.json").write_text(
        json.dumps({"backstop": "2026-06-19"}), encoding="utf-8")

    result = collect.collect(root=root)
    assert result["mode"] == "review"
    assert _manifest(root)["reviewed"] == ["blast radius"]
