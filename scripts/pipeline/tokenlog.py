import json
from pathlib import Path

def parse_usage(claude_json: str) -> dict:
    try:
        obj = json.loads(claude_json)
    except (json.JSONDecodeError, TypeError):
        obj = {}
    u = obj.get("usage", {}) if isinstance(obj, dict) else {}
    return {
        "input_tokens": u.get("input_tokens", 0),
        "output_tokens": u.get("output_tokens", 0),
        "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
        "cost_usd": obj.get("total_cost_usd", 0.0) if isinstance(obj, dict) else 0.0,
    }

def append_token_log(root: Path, date: str, usage: dict, items_processed: int) -> None:
    log = Path(root) / "state" / "token-log.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    entry = {"date": date, **usage, "items_processed": items_processed}
    with log.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
