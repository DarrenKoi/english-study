from pathlib import Path

def pending_requests(root: Path) -> list[Path]:
    inbox = Path(root) / "requests" / "inbox"
    if not inbox.exists():
        return []
    return sorted(inbox.glob("*.md"))
