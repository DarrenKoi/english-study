import json
from pathlib import Path
from pipeline import finalize, config, review

def test_finalize_advances_state_and_moves_requests(tmp_path, monkeypatch):
    root = tmp_path
    (root / "state").mkdir()
    (root / "spool").mkdir(parents=True)
    (root / "spool" / "poetic.md").write_text("시적", encoding="utf-8")

    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "transcripts": {"s.jsonl": 5},
        "spool": ["spool/poetic.md"],
        "docs": {"proj/docs/a.md": "proj/docs/a.md:111.0:42"},
        "deferred": 0,
    }), encoding="utf-8")

    # git 호출은 가짜로
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")

    st = config.load_state(root / "state" / "progress.json")
    assert st["transcripts"]["s.jsonl"] == 5
    assert st["last_run"] == "2026-06-14"
    # spool 노트가 날짜 접두사로 spool/done 으로 보관(아카이브)
    assert not (root / "spool" / "poetic.md").exists()
    assert (root / "spool" / "done" / "2026-06-14-poetic.md").exists()


def test_finalize_promotes_docs_to_persistent_ledger(tmp_path, monkeypatch):
    # 처리한 문서(경로→키)는 영구 원장 docs_seen 에 누적된다.
    root = tmp_path
    (root / "state").mkdir()
    config.save_state({"transcripts": {}, "last_run": None,
                       "docs_seen": {"proj/docs/old.md": "proj/docs/old.md:1.0:9"}},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "transcripts": {}, "spool": [],
        "docs": {"proj/docs/new.md": "proj/docs/new.md:2.0:5"},
        "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")
    st = config.load_state(root / "state" / "progress.json")
    assert st["docs_seen"]["proj/docs/old.md"] == "proj/docs/old.md:1.0:9"   # 기존 유지
    assert st["docs_seen"]["proj/docs/new.md"] == "proj/docs/new.md:2.0:5"   # 새로 승격


def test_finalize_archives_same_name_note_without_clobber(tmp_path, monkeypatch):
    # 같은 날 같은 이름 노트가 또 처리되면 기존 아카이브를 덮어쓰지 않는다.
    root = tmp_path
    (root / "state").mkdir()
    (root / "spool").mkdir(parents=True)
    (root / "spool" / "done").mkdir(parents=True)
    (root / "spool" / "done" / "2026-06-14-q.md").write_text("first", encoding="utf-8")
    (root / "spool" / "q.md").write_text("second", encoding="utf-8")
    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "transcripts": {}, "spool": ["spool/q.md"], "docs": {}, "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")
    done = root / "spool" / "done"
    assert (done / "2026-06-14-q.md").read_text(encoding="utf-8") == "first"   # 보존
    assert (done / "2026-06-14-q-2.md").read_text(encoding="utf-8") == "second"  # 새 이름


def test_prune_old_daily_removes_folders_past_retention(tmp_path):
    # today 기준 retention_days 보다 더 오래된 날짜 폴더만 지운다(경계는 보존).
    root = tmp_path
    daily = root / "daily"
    for d in ["2026-05-30", "2026-05-31", "2026-06-01", "2026-06-20", "2026-06-21"]:
        (daily / d).mkdir(parents=True)
        (daily / d / "digest.md").write_text("x", encoding="utf-8")
    (daily / "_templates").mkdir()   # 날짜가 아닌 폴더는 건드리지 않는다

    removed = finalize.prune_old_daily(root, today="2026-06-21", retention_days=20)

    assert set(removed) == {"2026-05-30", "2026-05-31"}      # cutoff=2026-06-01 미만만
    assert not (daily / "2026-05-30").exists()
    assert not (daily / "2026-05-31").exists()
    assert (daily / "2026-06-01").exists()                   # 정확히 20일 → 보존
    assert (daily / "2026-06-21").exists()
    assert (daily / "_templates").exists()                   # 비-날짜 폴더 보존


def test_prune_old_daily_noop_when_dir_missing(tmp_path):
    assert finalize.prune_old_daily(tmp_path, today="2026-06-21", retention_days=20) == []


def test_finalize_prunes_old_daily(tmp_path, monkeypatch):
    # finalize 가 오래된 daily 폴더를 정리한다(config 없으면 기본 20일).
    root = tmp_path
    (root / "state").mkdir()
    (root / "daily" / "2026-05-01").mkdir(parents=True)
    (root / "daily" / "2026-06-21").mkdir(parents=True)
    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-21.json").write_text(json.dumps({
        "transcripts": {}, "spool": [], "docs": {}, "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    out = finalize.finalize(root=root, today="2026-06-21")

    assert not (root / "daily" / "2026-05-01").exists()      # 51일 전 → 삭제
    assert (root / "daily" / "2026-06-21").exists()          # 오늘 → 보존
    assert out["pruned"] == ["2026-05-01"]


def test_finalize_advances_reviewed_ledger(tmp_path, monkeypatch):
    # 복습한 표현은 state/reviewed.json 에 today 로 누적된다(성공 시에만).
    root = tmp_path
    (root / "state").mkdir()
    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-21.json").write_text(json.dumps({
        "transcripts": {}, "spool": [], "docs": {},
        "reviewed": ["backstop", "blast radius"], "mode": "review", "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-21")

    data = review.load_reviewed(root)
    assert data == {"backstop": "2026-06-21", "blast radius": "2026-06-21"}
