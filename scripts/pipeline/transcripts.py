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
    # 메인 세션(사람과의 실제 대화)을 먼저, subagents/ 트랜스크립트를 뒤로.
    # 같은 급에서는 최신 수정순 — 문서 수집과 같은 원칙. 순수 알파벳 정렬이면
    # 사전순으로 앞선 프로젝트가 배치 예산을 선점해, 코칭 원료인 사용자 한글이
    # 든 최근 세션이 밀린다.
    def _order(f: Path):
        try:
            mtime = f.stat().st_mtime
        except OSError:
            mtime = 0.0
        return ("subagents" in f.parts, -mtime)
    files = sorted(transcripts_dir.rglob("*.jsonl"), key=_order)
    for f in files:
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
                # subagent 파일의 'user' 는 사람이 아니라 오케스트레이터 LLM 이 쓴
                # 디스패치 프롬프트 — 영작 코칭("내가 쓴 글")의 대상이 아니므로 재표기.
                if role == "user" and "subagents" in Path(rel).parts:
                    role = "agent-prompt"
                records.append({"file": rel, "role": role, "text": text, "line": i})
        new_offsets[rel] = len(lines)
    return records, new_offsets
