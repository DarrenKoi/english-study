"""격리 e2e: 임시 미니레포에서 collect → (LLM 스텁) → finalize 전 체인을 실제로 돌린다.

실제 레포/깃/네트워크는 건드리지 않는다 — LLM(claude -p)과 git push 만 스텁한다.
이 세션에서 추가한 prune(오래된 daily 삭제) · 복습 큐 보존 · notes/index 죽은 링크
청소가 한 흐름 안에서 함께 올바로 동작하는지를 한 번에 검증한다.
"""
import json
import shutil
from pathlib import Path

from pipeline import run as runmod
from pipeline import finalize as finalmod
from pipeline import config

REPO = Path(__file__).resolve().parents[1]
TODAY = "2026-06-21"            # prune cutoff = 2026-06-01 (TODAY-20)


def _seed(root: Path) -> None:
    base = root / "codes"
    (base / "myproj" / "docs").mkdir(parents=True)
    (base / "myproj" / "docs" / "intro.md").write_text(
        "The pipeline collects English from notes and renders a daily digest. "
        "It runs unattended every night and pushes the result.\n", encoding="utf-8")

    tx = root / "transcripts" / "proj"
    tx.mkdir(parents=True)
    (tx / "s.jsonl").write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in [
        {"type": "user", "message": {"role": "user",
            "content": "이 구조 분리 규칙이 왜 중요한지 한 줄로 설명해줘"}},
        {"type": "assistant", "message": {"role": "assistant", "content": [
            {"type": "text", "text": "Dependencies point one way — toward the more generic layer."}]}},
    ]) + "\n", encoding="utf-8")

    (root / "config").mkdir()
    (root / "config" / "sources.json").write_text(json.dumps({
        "base_path": str(base), "transcripts_dir": str(tx),
        "char_budget": 8000, "digest_min": 5, "digest_max": 7,
        "doc_dirs": ["doc", "docs", "shared_docs"], "doc_exts": [".md", ".txt"],
        "recent_days": 7, "backlog_days": 14, "daily_retention_days": 20,
        "exclude_projects": [],
    }), encoding="utf-8")

    (root / "prompts").mkdir()
    for p in ("process.md", "review.md"):
        shutil.copy(REPO / "prompts" / p, root / "prompts" / p)

    (root / "spool").mkdir()
    (root / "spool" / "q1.txt").write_text("affect 와 effect 차이?", encoding="utf-8")

    notes = root / "notes"
    (notes / "by-register").mkdir(parents=True)
    (notes / "by-register" / "conversational.md").write_text(
        "- **beta** — 베타 설명.\n  - 예: This is a beta example sentence.\n", encoding="utf-8")
    (notes / "index.md").write_text("\n".join([
        "# 표현 인덱스", "",
        "- [alpha](daily/2026-04-01/new-expressions.md) — 2026-04-01",   # reviewed + dead → 제거
        "- [beta](daily/2026-04-02/new-expressions.md) — 2026-04-02",    # unreviewed + dead → 보존
        "- [gamma](daily/2026-06-20/new-expressions.md) — 2026-06-20",   # reviewed + live → 보존
    ]) + "\n", encoding="utf-8")

    (root / "daily" / "2026-05-01").mkdir(parents=True)      # 오래된 폴더 → prune 대상
    (root / "daily" / "2026-05-01" / "digest.md").write_text("old", encoding="utf-8")
    (root / "daily" / "2026-06-20").mkdir(parents=True)      # 최근 → 보존 + gamma 의 live 타깃
    (root / "daily" / "2026-06-20" / "new-expressions.md").write_text("g", encoding="utf-8")

    (root / "state").mkdir()
    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "reviewed.json").write_text(
        json.dumps({"alpha": "2026-04-20", "gamma": "2026-06-20"}), encoding="utf-8")


def test_e2e_full_pipeline_normal_mode(tmp_path, monkeypatch):
    root = tmp_path
    _seed(root)

    captured = {}
    git_calls = []

    def fake_claude(prompt, _root):
        captured["prompt"] = prompt
        day = Path(_root) / "daily" / TODAY
        day.mkdir(parents=True, exist_ok=True)
        (day / "digest.md").write_text("# e2e digest\n", encoding="utf-8")
        return json.dumps({"usage": {"input_tokens": 10, "output_tokens": 20,
                                     "cache_read_input_tokens": 0}, "total_cost_usd": 0.01})

    monkeypatch.setattr(runmod, "_invoke_claude", fake_claude)
    monkeypatch.setattr(finalmod, "_git_commit_push", lambda r, m: git_calls.append(m))
    # collect 가 실제 날짜 대신 TODAY 를 쓰도록 강제(결정적 prune cutoff).
    orig_collect = runmod.collect
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: orig_collect(root=root, today=TODAY))

    result = runmod.run(root=root)

    # 오케스트레이션
    assert result["status"] == "done"
    assert (root / "state" / f"batch-{TODAY}.md").exists()
    assert (root / "state" / "token-log.jsonl").exists()
    assert (root / "daily" / TODAY / "digest.md").exists()      # LLM(스텁)이 산출물 작성
    assert "표현 추출" in captured["prompt"]                     # normal 모드 = process.md 지침
    assert "복습 가공 지침" not in captured["prompt"]            # review.md 가 아님

    # finalize: 상태 전진
    st = config.load_state(root / "state" / "progress.json")
    assert st["last_run"] == TODAY
    assert st["transcripts"] and all(v >= 1 for v in st["transcripts"].values())

    # finalize: spool 아카이브
    assert (root / "spool" / "done" / f"{TODAY}-q1.txt").exists()
    assert not (root / "spool" / "q1.txt").exists()

    # finalize: 오래된 daily prune
    assert not (root / "daily" / "2026-05-01").exists()
    assert (root / "daily" / "2026-06-20").exists()

    # finalize: notes/index 죽은 링크 청소 (복습 끝난 것만; 미복습은 보존)
    idx = (root / "notes" / "index.md").read_text(encoding="utf-8")
    assert "alpha" not in idx          # reviewed + dead → 제거
    assert "beta" in idx               # unreviewed + dead → 보존(복습 큐 유지)
    assert "gamma" in idx              # reviewed + live → 보존
    assert "# 표현 인덱스" in idx       # 비-인덱스 줄 보존

    # commit&push 1회 (push 자체는 스텁)
    assert len(git_calls) == 1
