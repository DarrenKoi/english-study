from pathlib import Path

def pending_notes(root: Path) -> list[Path]:
    """사용자가 spool/ 에 직접 적은 학습 노트(.md/.txt)를 읽는다.
    이미 처리되어 spool/done/ 으로 보관된 것은 제외한다."""
    s = Path(root) / "spool"
    if not s.exists():
        return []
    notes = [p for p in s.glob("*.md")] + [p for p in s.glob("*.txt")]
    # README 는 폴더 안내문이라 학습 대상에서 제외
    notes = [p for p in notes if p.name.lower() != "readme.md"]
    return sorted(notes, key=lambda p: p.name)
