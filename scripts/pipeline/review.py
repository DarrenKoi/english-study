import json
import re
from pathlib import Path

# notes/index.md 한 줄: "- [표현](daily/.../new-expressions.md) — YYYY-MM-DD"
# 표현 안에는 ']' 가 없으므로 마지막 ']' 까지를 표현으로, 그 뒤 (...) 를 링크로 본다.
_LINE = re.compile(r"^- \[(?P<expr>.+)\]\((?P<link>[^)]+)\)\s*—\s*(?P<date>\d{4}-\d{2}-\d{2})\s*$")


def parse_index(root: Path) -> list[dict]:
    """notes/index.md 를 파싱해 [{expr, date, link}, ...] 를 파일 순서대로 반환한다."""
    path = Path(root) / "notes" / "index.md"
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _LINE.match(line.strip())
        if m:
            rows.append({"expr": m.group("expr"), "link": m.group("link"),
                         "date": m.group("date")})
    return rows


def _reviewed_path(root: Path) -> Path:
    return Path(root) / "state" / "reviewed.json"


def load_reviewed(root: Path) -> dict:
    """state/reviewed.json (표현→복습일) 을 읽는다. 없으면 {}."""
    path = _reviewed_path(root)
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_reviewed(root: Path, data: dict) -> None:
    path = _reviewed_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def mark_reviewed(root: Path, exprs: list[str], today: str) -> None:
    """주어진 표현들을 today 로 복습 완료 표시(누적 저장)."""
    data = load_reviewed(root)
    for e in exprs:
        data[e] = today
    save_reviewed(root, data)


def select_unreviewed(root: Path, n: int) -> list[dict]:
    """아직 복습하지 않은 표현을 수집일 오래된 순으로 최대 n개 반환(표현 중복 제거)."""
    reviewed = load_reviewed(root)
    seen: set[str] = set()
    picks: list[dict] = []
    for e in sorted(parse_index(root), key=lambda x: x["date"]):
        if e["expr"] in reviewed or e["expr"] in seen:
            continue
        seen.add(e["expr"])
        picks.append(e)
        if len(picks) >= n:
            break
    return picks
