import copy
import json
from pathlib import Path

DEFAULT_STATE = {"transcripts": {}, "docs_seen": {}, "last_run": None}

def root() -> Path:
    # scripts/pipeline/config.py -> english-study/
    return Path(__file__).resolve().parents[2]

def config_path() -> Path:
    return root() / "config" / "sources.json"

def state_path() -> Path:
    return root() / "state" / "progress.json"

def load_config(path: Path | None = None) -> dict:
    path = Path(path) if path else config_path()
    return json.loads(path.read_text(encoding="utf-8"))

def load_state(path: Path | None = None) -> dict:
    path = Path(path) if path else state_path()
    if not path.exists():
        return copy.deepcopy(DEFAULT_STATE)
    data = json.loads(path.read_text(encoding="utf-8"))
    return {**copy.deepcopy(DEFAULT_STATE), **data}

def save_state(state: dict, path: Path | None = None) -> None:
    path = Path(path) if path else state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
