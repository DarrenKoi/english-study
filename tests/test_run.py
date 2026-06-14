import json
from pathlib import Path
from pipeline import run as runmod

def test_run_skips_llm_when_no_items(tmp_path, monkeypatch):
    calls = {"claude": 0, "finalize": 0}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 0, "deferred": 0,
                                                  "batch_path": "x", "today": "2026-06-14"})
    monkeypatch.setattr(runmod, "_invoke_claude", lambda *a, **k: calls.__setitem__("claude", 1) or "{}")
    monkeypatch.setattr(runmod, "finalize", lambda root, today=None: calls.__setitem__("finalize", 1))
    runmod.run(root=tmp_path)
    assert calls["claude"] == 0          # 아이템 0이면 LLM 호출 안 함
    assert calls["finalize"] == 0

def test_run_invokes_llm_and_logs_tokens(tmp_path, monkeypatch):
    (tmp_path / "state").mkdir()
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 2, "deferred": 1,
                                                  "batch_path": str(tmp_path / "b.md"),
                                                  "today": "2026-06-14"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda prompt, root: json.dumps(
                            {"usage": {"input_tokens": 5, "output_tokens": 7,
                                       "cache_read_input_tokens": 0},
                             "total_cost_usd": 0.02}))
    finalized = {}
    monkeypatch.setattr(runmod, "finalize",
                        lambda root, today=None: finalized.__setitem__("done", today))
    runmod.run(root=tmp_path)
    log = (tmp_path / "state" / "token-log.jsonl").read_text(encoding="utf-8").strip()
    assert json.loads(log)["output_tokens"] == 7
    assert finalized["done"] == "2026-06-14"
