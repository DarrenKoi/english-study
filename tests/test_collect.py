import json
from pathlib import Path
from pipeline import collect

def test_collect_builds_batch_and_manifest(tmp_path, monkeypatch):
    root = tmp_path
    (root / "config").mkdir()
    (root / "config" / "sources.json").write_text(json.dumps({
        "base_path": str(tmp_path / "codes"),
        "transcripts_dir": str(tmp_path / "tx"),
        "char_budget": 100000,
        "repos": [{"name": "proj", "globs": ["docs/**/*.md"]}],
    }), encoding="utf-8")
    (root / "spool").mkdir(parents=True)
    (root / "spool" / "poetic.md").write_text("시적으로", encoding="utf-8")

    # gitutil/transcripts 를 가짜로 대체
    monkeypatch.setattr(collect.gitutil, "pull", lambda repo: None)
    monkeypatch.setattr(collect.gitutil, "head_sha", lambda repo: "newsha")
    monkeypatch.setattr(collect.gitutil, "changed_md_files",
                        lambda repo, sha, globs: ["docs/a.md"])
    proj = tmp_path / "codes" / "proj" / "docs"
    proj.mkdir(parents=True)
    (proj / "a.md").write_text("Let's circle back to this.", encoding="utf-8")
    monkeypatch.setattr(collect.transcripts, "new_messages",
                        lambda d, off: ([{"file": "s.jsonl", "role": "user",
                                          "text": "hello world", "line": 0}],
                                        {"s.jsonl": 1}))

    result = collect.collect(root=root)

    batch_files = list((root / "state").glob("batch-*.md"))
    assert batch_files, "batch 파일이 생성돼야 함"
    manifest = json.loads(
        next((root / "state").glob("consumed-*.json")).read_text(encoding="utf-8"))
    assert manifest["repos"]["proj"] == "newsha"
    assert manifest["transcripts"]["s.jsonl"] == 1
    assert manifest["spool"] == ["spool/poetic.md"]
    assert result["item_count"] == 3   # spool note + repo file + transcript
