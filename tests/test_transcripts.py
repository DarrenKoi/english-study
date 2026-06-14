import json
from pathlib import Path
from pipeline import transcripts

def _write_jsonl(path, lines):
    path.write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in lines) + "\n",
                    encoding="utf-8")

def test_extract_text_from_string_and_blocks():
    assert transcripts._extract_text({"message": {"content": "hello"}}) == "hello"
    obj = {"message": {"content": [{"type": "text", "text": "a"},
                                    {"type": "tool_use", "name": "Bash"},
                                    {"type": "text", "text": "b"}]}}
    assert transcripts._extract_text(obj) == "a\nb"

def test_new_messages_respects_offset(tmp_path):
    d = tmp_path / "proj"
    d.mkdir()
    f = d / "sess.jsonl"
    _write_jsonl(f, [
        {"type": "user", "message": {"role": "user", "content": "first"}},
        {"type": "assistant", "message": {"role": "assistant",
                                          "content": [{"type": "text", "text": "second"}]}},
    ])
    recs, offsets = transcripts.new_messages(tmp_path, {})
    texts = [r["text"] for r in recs]
    assert texts == ["first", "second"]
    rel = "proj/sess.jsonl"
    assert offsets[rel] == 2

    # 같은 오프셋으로 다시 호출하면 새 메시지 없음
    recs2, offsets2 = transcripts.new_messages(tmp_path, offsets)
    assert recs2 == []
    assert offsets2[rel] == 2
