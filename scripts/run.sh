#!/bin/zsh
# launchd 진입점. launchd 는 최소 env 로 실행하므로 PATH 를 명시한다.
# uv 가 Python·venv·의존성을 자동 관리하므로 시스템 python3 를 찾을 필요가 없다.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin:$HOME/.claude/local"
export PYTHONPATH="$ROOT/scripts"
cd "$ROOT"
git pull --ff-only --quiet || true
uv run python -m pipeline.run >> "$ROOT/state/run.log" 2>&1
