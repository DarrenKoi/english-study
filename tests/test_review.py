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


def test_prune_dead_index_links_removes_only_reviewed_and_dead(tmp_path):
    # 복습 끝났고 링크 대상이 사라진 줄만 지운다. 미복습 죽은 링크는 복습 큐 유지를 위해 보존.
    (tmp_path / "daily" / "2026-06-20").mkdir(parents=True)
    (tmp_path / "daily" / "2026-06-20" / "new-expressions.md").write_text("x", encoding="utf-8")
    _index(tmp_path, "\n".join([
        "# 표현 인덱스",
        "",
        "- [alpha](daily/2026-05-01/new-expressions.md) — 2026-05-01",   # reviewed + dead → 제거
        "- [beta](daily/2026-05-02/new-expressions.md) — 2026-05-02",    # unreviewed + dead → 보존
        "- [gamma](daily/2026-06-20/new-expressions.md) — 2026-06-20",   # reviewed + live → 보존
    ]) + "\n")
    review.save_reviewed(tmp_path, {"alpha": "2026-05-20", "gamma": "2026-06-20"})

    removed = review.prune_dead_index_links(tmp_path)

    assert removed == ["alpha"]
    text = (tmp_path / "notes" / "index.md").read_text(encoding="utf-8")
    assert "alpha" not in text
    assert "beta" in text            # 미복습 죽은 링크 보존 (복습 큐)
    assert "gamma" in text           # live 링크 보존
    assert "# 표현 인덱스" in text     # 비-인덱스 줄 보존
    # 보존된 beta 는 여전히 복습 후보로 선택된다
    assert [p["expr"] for p in review.select_unreviewed(tmp_path, 10)] == ["beta"]


def test_prune_dead_index_links_noop_when_missing(tmp_path):
    assert review.prune_dead_index_links(tmp_path) == []


def test_mark_reviewed_persists_and_resumes_on_new_expr(tmp_path):
    _index(tmp_path, SAMPLE)
    review.mark_reviewed(tmp_path, ["backstop", "blast radius"], "2026-06-21")
    data = json.loads((tmp_path / "state" / "reviewed.json").read_text(encoding="utf-8"))
    assert data["backstop"] == "2026-06-21"
    # 새 표현이 index 에 추가되면 다시 선택 대상이 된다
    _index(tmp_path, SAMPLE + "- [new one](daily/2026-06-21/new-expressions.md) — 2026-06-21\n")
    picks = review.select_unreviewed(tmp_path, 10)
    assert [p["expr"] for p in picks] == ["anchor on (the first plausible idea)", "new one"]
