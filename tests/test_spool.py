from pipeline import spool


def test_pending_notes_reads_md_and_txt(tmp_path):
    s = tmp_path / "spool"
    s.mkdir()
    (s / "grammar.md").write_text("explain affect vs effect", encoding="utf-8")
    (s / "curious.txt").write_text("why 'a' before historic?", encoding="utf-8")
    (s / "ignore.json").write_text("{}", encoding="utf-8")
    found = [p.name for p in spool.pending_notes(tmp_path)]
    assert found == ["curious.txt", "grammar.md"]  # sorted, .md+.txt only


def test_pending_notes_excludes_done(tmp_path):
    s = tmp_path / "spool"
    (s / "done").mkdir(parents=True)
    (s / "active.md").write_text("answer me", encoding="utf-8")
    (s / "done" / "2026-06-14-old.md").write_text("already answered", encoding="utf-8")
    found = [p.name for p in spool.pending_notes(tmp_path)]
    assert found == ["active.md"]


def test_pending_notes_excludes_readme(tmp_path):
    s = tmp_path / "spool"
    s.mkdir()
    (s / "README.md").write_text("안내 파일", encoding="utf-8")
    (s / "real-question.md").write_text("answer me", encoding="utf-8")
    found = [p.name for p in spool.pending_notes(tmp_path)]
    assert found == ["real-question.md"]   # README 는 학습 대상 아님


def test_pending_notes_empty_when_no_spool(tmp_path):
    assert spool.pending_notes(tmp_path) == []
