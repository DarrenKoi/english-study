from pipeline import requests_inbox

def test_pending_requests_lists_only_md(tmp_path):
    inbox = tmp_path / "requests" / "inbox"
    inbox.mkdir(parents=True)
    (inbox / "poetic.md").write_text("이 표현 시적으로", encoding="utf-8")
    (inbox / "notes.txt").write_text("ignore", encoding="utf-8")
    found = requests_inbox.pending_requests(tmp_path)
    assert [p.name for p in found] == ["poetic.md"]

def test_pending_requests_empty_when_no_inbox(tmp_path):
    assert requests_inbox.pending_requests(tmp_path) == []
