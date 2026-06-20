import json
from pathlib import Path

from pipeline import review


def _index(root: Path, body: str) -> None:
    (root / "notes").mkdir(parents=True, exist_ok=True)
    (root / "notes" / "index.md").write_text(body, encoding="utf-8")


SAMPLE = """# 표현 인덱스

- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20
- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17
- [anchor on (the first plausible idea)](daily/2026-06-18/new-expressions.md) — 2026-06-18
"""


def test_parse_index_extracts_expr_date_link(tmp_path):
    _index(tmp_path, SAMPLE)
    rows = review.parse_index(tmp_path)
    exprs = {r["expr"] for r in rows}
    assert exprs == {"blast radius", "backstop", "anchor on (the first plausible idea)"}
    row = next(r for r in rows if r["expr"] == "backstop")
    assert row["date"] == "2026-06-17"
    assert row["link"] == "daily/2026-06-17/new-expressions.md"


def test_parse_index_missing_file_returns_empty(tmp_path):
    assert review.parse_index(tmp_path) == []


def test_select_unreviewed_sorts_oldest_first_and_limits(tmp_path):
    _index(tmp_path, SAMPLE)
    picks = review.select_unreviewed(tmp_path, 2)
    assert [p["expr"] for p in picks] == ["backstop", "anchor on (the first plausible idea)"]


def test_select_unreviewed_excludes_reviewed(tmp_path):
    _index(tmp_path, SAMPLE)
    review.save_reviewed(tmp_path, {"backstop": "2026-06-19"})
    picks = review.select_unreviewed(tmp_path, 10)
    assert [p["expr"] for p in picks] == [
        "anchor on (the first plausible idea)", "blast radius"]


def test_select_unreviewed_exhausted_returns_empty(tmp_path):
    _index(tmp_path, SAMPLE)
    review.save_reviewed(tmp_path, {
        "backstop": "d", "anchor on (the first plausible idea)": "d", "blast radius": "d"})
    assert review.select_unreviewed(tmp_path, 10) == []


def test_mark_reviewed_persists_and_resumes_on_new_expr(tmp_path):
    _index(tmp_path, SAMPLE)
    review.mark_reviewed(tmp_path, ["backstop", "blast radius"], "2026-06-21")
    data = json.loads((tmp_path / "state" / "reviewed.json").read_text(encoding="utf-8"))
    assert data["backstop"] == "2026-06-21"
    # 새 표현이 index 에 추가되면 다시 선택 대상이 된다
    _index(tmp_path, SAMPLE + "- [new one](daily/2026-06-21/new-expressions.md) — 2026-06-21\n")
    picks = review.select_unreviewed(tmp_path, 10)
    assert [p["expr"] for p in picks] == ["anchor on (the first plausible idea)", "new one"]
