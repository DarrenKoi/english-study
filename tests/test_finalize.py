import json
from pathlib import Path
from pipeline import finalize, config

def test_finalize_advances_state_and_moves_requests(tmp_path, monkeypatch):
    root = tmp_path
    (root / "state").mkdir()
    (root / "requests" / "inbox").mkdir(parents=True)
    (root / "requests" / "done").mkdir(parents=True)
    (root / "requests" / "inbox" / "poetic.md").write_text("시적", encoding="utf-8")

    config.save_state({"repos": {}, "transcripts": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "repos": {"proj": "newsha"},
        "transcripts": {"s.jsonl": 5},
        "requests": ["requests/inbox/poetic.md"],
        "deferred": 0,
    }), encoding="utf-8")

    # git 호출은 가짜로
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")

    st = config.load_state(root / "state" / "progress.json")
    assert st["repos"]["proj"] == "newsha"
    assert st["transcripts"]["s.jsonl"] == 5
    assert st["last_run"] == "2026-06-14"
    # 요청이 done 으로 이동
    assert not (root / "requests" / "inbox" / "poetic.md").exists()
    assert (root / "requests" / "done" / "2026-06-14-poetic.md").exists()


def test_finalize_sets_repo_queue_on_partial(tmp_path, monkeypatch):
    root = tmp_path
    (root / "state").mkdir()
    config.save_state({"repos": {}, "repo_queue": {}, "transcripts": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "repos": {}, "transcripts": {}, "requests": [],
        "repo_queue": {"proj": {"target": "head1", "remaining": ["docs/b.md"]}},
        "deferred": 1,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")
    st = config.load_state(root / "state" / "progress.json")
    assert st["repo_queue"]["proj"]["remaining"] == ["docs/b.md"]
    assert "proj" not in st["repos"]


def test_finalize_clears_queue_when_repo_drained(tmp_path, monkeypatch):
    root = tmp_path
    (root / "state").mkdir()
    config.save_state({"repos": {}, "transcripts": {}, "last_run": None,
                       "repo_queue": {"proj": {"target": "head1", "remaining": ["docs/b.md"]}}},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "repos": {"proj": "head1"}, "transcripts": {}, "requests": [],
        "repo_queue": {}, "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")
    st = config.load_state(root / "state" / "progress.json")
    assert st["repos"]["proj"] == "head1"
    assert "proj" not in st["repo_queue"]   # 소진된 repo 의 queue 는 제거
