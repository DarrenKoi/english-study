import json
from pipeline import config

def test_load_config_reads(tmp_path):
    cfg_file = tmp_path / "sources.json"
    cfg_file.write_text(json.dumps({"base_path": "~/Codes", "repos": []}), encoding="utf-8")
    cfg = config.load_config(cfg_file)
    assert cfg["repos"] == []
    assert cfg["base_path"] == "~/Codes"

def test_load_state_missing_returns_default(tmp_path):
    st = config.load_state(tmp_path / "nope.json")
    assert st == {"repos": {}, "transcripts": {}, "last_run": None}

def test_save_then_load_state_roundtrip(tmp_path):
    p = tmp_path / "progress.json"
    config.save_state({"repos": {"a": "sha"}, "transcripts": {}, "last_run": "2026-06-14"}, p)
    assert config.load_state(p)["repos"]["a"] == "sha"

def test_load_state_returns_independent_copies(tmp_path):
    a = config.load_state(tmp_path / "missing.json")
    a["repos"]["x"] = "1"
    b = config.load_state(tmp_path / "missing2.json")
    assert b["repos"] == {}   # 이전 호출의 변경이 새 호출로 새지 않아야 함

def test_load_state_fills_missing_keys(tmp_path):
    p = tmp_path / "partial.json"
    p.write_text('{"repos": {"a": "sha"}}', encoding="utf-8")
    st = config.load_state(p)
    assert st["repos"] == {"a": "sha"}
    assert st["transcripts"] == {}
    assert st["last_run"] is None
