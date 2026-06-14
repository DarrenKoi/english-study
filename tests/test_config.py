import json
from pipeline import config

def test_load_config_expands_and_reads(tmp_path):
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
