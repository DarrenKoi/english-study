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

def test_run_skips_finalize_when_llm_fails(tmp_path, monkeypatch):
    called = {"finalize": 0, "tokenlog": 0}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 1, "deferred": 0,
                                                  "batch_path": "b", "today": "2026-06-14"})
    monkeypatch.setattr(runmod, "_invoke_claude", lambda prompt, root: "")  # 빈 출력 = 실패
    monkeypatch.setattr(runmod.tokenlog, "append_token_log",
                        lambda *a, **k: called.__setitem__("tokenlog", 1))
    monkeypatch.setattr(runmod, "finalize",
                        lambda root, today=None: called.__setitem__("finalize", 1))
    result = runmod.run(root=tmp_path)
    assert called["finalize"] == 0          # 상태 전진 안 함
    assert result["status"] == "llm_failed"

def test_run_empty_mode_skips_llm(tmp_path, monkeypatch):
    calls = {"claude": 0}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 0, "deferred": 0,
                                                  "batch_path": "x", "today": "2026-06-21",
                                                  "mode": "empty"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda *a, **k: calls.__setitem__("claude", 1) or "{}")
    result = runmod.run(root=tmp_path)
    assert calls["claude"] == 0
    assert result["status"] == "empty"


def test_run_uses_review_prompt_for_review_mode(tmp_path, monkeypatch):
    (tmp_path / "state").mkdir()
    (tmp_path / "prompts").mkdir()
    (tmp_path / "prompts" / "process.md").write_text("PROCESS-PROMPT", encoding="utf-8")
    (tmp_path / "prompts" / "review.md").write_text("REVIEW-PROMPT", encoding="utf-8")
    seen = {}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 1, "deferred": 0,
                                                  "batch_path": str(tmp_path / "b.md"),
                                                  "today": "2026-06-21", "mode": "review"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda prompt, root: seen.update(prompt=prompt) or json.dumps(
                            {"usage": {"input_tokens": 1, "output_tokens": 1,
                                       "cache_read_input_tokens": 0}, "total_cost_usd": 0.0}))
    monkeypatch.setattr(runmod, "finalize", lambda root, today=None: None)
    runmod.run(root=tmp_path)
    assert "REVIEW-PROMPT" in seen["prompt"]
    assert "PROCESS-PROMPT" not in seen["prompt"]
