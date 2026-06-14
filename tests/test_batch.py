from pipeline import batch


def _unit(kind, uid, text):
    return {"kind": kind, "id": uid, "provenance": f"{kind}:{uid}",
            "text": text, "advance": {uid: True}}


def test_build_batch_includes_until_budget(tmp_path):
    units = [_unit("request", "r1", "a" * 100),
             _unit("repo", "p1", "b" * 100),
             _unit("transcript", "t1", "c" * 100)]
    text, consumed = batch.build_batch(units, char_budget=250, today="2026-06-14")
    # 첫 두 단위(=200자)는 들어가고 세 번째는 예산 초과로 제외
    assert [u["id"] for u in consumed] == ["r1", "p1"]
    assert "request:r1" in text and "repo:p1" in text
    assert "transcript:t1" not in text


def test_build_batch_always_includes_at_least_one(tmp_path):
    units = [_unit("repo", "big", "x" * 10000)]
    text, consumed = batch.build_batch(units, char_budget=10, today="2026-06-14")
    assert [u["id"] for u in consumed] == ["big"]


def test_build_batch_empty_units():
    text, consumed = batch.build_batch([], char_budget=100, today="2026-06-14")
    assert consumed == []
    assert "2026-06-14" in text
