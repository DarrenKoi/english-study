import json
from pathlib import Path

def _extract_text(obj: dict) -> str:
    msg = obj.get("message") or {}
    content = msg.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [b.get("text", "") for b in content
                 if isinstance(b, dict) and b.get("type") == "text"]
        return "\n".join(p for p in parts if p)
    return ""

def new_messages(transcripts_dir: Path, offsets: dict) -> tuple[list[dict], dict]:
    transcripts_dir = Path(transcripts_dir)
    new_offsets = dict(offsets)
    records: list[dict] = []
    if not transcripts_dir.exists():
        return records, new_offsets
    for f in sorted(transcripts_dir.rglob("*.jsonl")):
        rel = f.relative_to(transcripts_dir).as_posix()
        start = offsets.get(rel, 0)
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        for i in range(start, len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            text = _extract_text(obj)
            if text.strip():
                role = (obj.get("message") or {}).get("role", obj.get("type", "?"))
                records.append({"file": rel, "role": role, "text": text, "line": i})
        new_offsets[rel] = len(lines)
    return records, new_offsets
