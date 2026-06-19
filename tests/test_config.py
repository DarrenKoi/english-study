import json
from pipeline import config

def test_load_config_reads(tmp_path):
    cfg_file = tmp_path / "sources.json"
    cfg_file.write_text(json.dumps({"base_path": "~/Codes", "doc_dirs": ["docs"]}), encoding="utf-8")
    cfg = config.load_config(cfg_file)
    assert cfg["doc_dirs"] == ["docs"]
    assert cfg["base_path"] == "~/Codes"

def test_load_state_missing_returns_default(tmp_path):
    st = config.load_state(tmp_path / "nope.json")
    assert st == {"transcripts": {}, "docs_seen": {}, "last_run": None}

def test_load_state_old_file_gets_docs_seen_default(tmp_path):
    # 구버전 progress.json (docs_seen 없음) 도 매끄럽게 로드돼야 한다
    p = tmp_path / "progress.json"
    p.write_text(json.dumps({"transcripts": {"s.jsonl": 5}, "last_run": "2026-06-14"}),
                 encoding="utf-8")
    st = config.load_state(p)
    assert st["docs_seen"] == {}
    assert st["transcripts"]["s.jsonl"] == 5

def test_save_then_load_state_roundtrip(tmp_path):
    p = tmp_path / "progress.json"
    config.save_state({"transcripts": {}, "docs_seen": {"a/x.md": "k"}, "last_run": "2026-06-14"}, p)
    assert config.load_state(p)["docs_seen"]["a/x.md"] == "k"

def test_load_state_returns_independent_copies(tmp_path):
    a = config.load_state(tmp_path / "missing.json")
    a["docs_seen"]["x"] = "1"
    b = config.load_state(tmp_path / "missing2.json")
    assert b["docs_seen"] == {}   # 이전 호출의 변경이 새 호출로 새지 않아야 함

def test_load_state_fills_missing_keys(tmp_path):
    p = tmp_path / "partial.json"
    p.write_text('{"docs_seen": {"a/x.md": "k"}}', encoding="utf-8")
    st = config.load_state(p)
    assert st["docs_seen"] == {"a/x.md": "k"}
    assert st["transcripts"] == {}
    assert st["last_run"] is None
