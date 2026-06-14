import json
from pipeline import tokenlog

SAMPLE = json.dumps({
    "type": "result", "subtype": "success",
    "total_cost_usd": 0.0421,
    "usage": {"input_tokens": 1200, "output_tokens": 3400,
              "cache_read_input_tokens": 800, "cache_creation_input_tokens": 0},
    "result": "done"
})

def test_parse_usage_extracts_fields():
    u = tokenlog.parse_usage(SAMPLE)
    assert u["input_tokens"] == 1200
    assert u["output_tokens"] == 3400
    assert u["cache_read_input_tokens"] == 800
    assert u["cost_usd"] == 0.0421

def test_parse_usage_defensive_on_garbage():
    u = tokenlog.parse_usage("not json")
    assert u["input_tokens"] == 0 and u["cost_usd"] == 0.0

def test_append_token_log_writes_jsonl(tmp_path):
    tokenlog.append_token_log(tmp_path, "2026-06-14",
                              {"input_tokens": 10, "output_tokens": 20,
                               "cache_read_input_tokens": 0, "cost_usd": 0.01},
                              items_processed=3)
    log = tmp_path / "state" / "token-log.jsonl"
    line = json.loads(log.read_text(encoding="utf-8").strip())
    assert line["date"] == "2026-06-14"
    assert line["output_tokens"] == 20
    assert line["items_processed"] == 3
