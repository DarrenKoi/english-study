# English Study Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 매일 밤 Mac에서 자동 실행되어, git 공유 프로젝트 docs와 Claude Code 대화에서 영어 표현을 증분 수집하고, Claude로 해설·분류·번역해 날짜별 학습 다이제스트를 만드는 파이프라인을 구축한다.

**Architecture:** 결정적 단계(Python: git 증분 수집·상태 관리·토큰 로그)와 LLM 단계(`claude -p` 헤드리스: 추출·분류·코칭)를 분리한다. collect가 토큰 예산 안에서 "소비한 단위"를 매니페스트로 기록하고, LLM 가공 후 finalize가 그 매니페스트만큼만 상태를 전진시켜(all-or-nothing per unit) 증분의 멱등성을 보장한다. launchd가 매일 23:00에 트리거한다.

**Tech Stack:** Python 3.11+ (stdlib only: `json`, `subprocess`, `pathlib`, `datetime`, `re`, `fnmatch`), **uv**(환경·실행 관리), pytest(dev 의존성), git, `claude -p --output-format json`, macOS launchd.

---

## 모듈 구조

```
english-study/
├─ pyproject.toml                # uv 프로젝트: requires-python, dev=pytest, pytest pythonpath
├─ .python-version               # uv 가 고정할 Python 버전 (3.11)
├─ config/
│   └─ sources.json              # 출처 repo + glob + 토큰/문자 예산
├─ state/                        # progress.json·token-log.jsonl 은 커밋, batch-*/consumed-* 는 gitignore
│   └─ progress.json             # repo SHA, 트랜스크립트 오프셋, last_run (런타임 생성)
├─ prompts/
│   └─ process.md                # claude -p 에 주입할 LLM 작업 지침
├─ scripts/
│   ├─ pipeline/
│   │   ├─ __init__.py
│   │   ├─ config.py             # 경로·설정·상태 로드/저장
│   │   ├─ gitutil.py            # head_sha, changed_md_files, pull, glob 매칭
│   │   ├─ transcripts.py        # 오프셋 기준 새 대화 메시지 추출
│   │   ├─ requests_inbox.py     # requests/inbox 읽기
│   │   ├─ batch.py              # 예산 내 배치 조립 + 소비 단위 반환
│   │   ├─ collect.py            # 수집 오케스트레이션 → batch + consumed 매니페스트
│   │   ├─ tokenlog.py           # claude json usage 파싱 → token-log.jsonl
│   │   ├─ finalize.py           # 상태 전진·요청 이동·git commit/push
│   │   └─ run.py                # collect → claude -p → finalize
│   ├─ run.sh                    # launchd 진입점 (env 세팅 후 run.py)
│   └─ com.daeyoung.english-study.plist
├─ tests/
│   └─ test_*.py                 # import 경로는 pyproject 의 pytest pythonpath 로 해결
├─ daily/                        # LLM 출력 (날짜별 학습거리)
├─ notes/                        # LLM 출력 (영구 아카이브)
├─ requests/{inbox,done}/        # 주문서
└─ CLAUDE.md                     # 헤드리스 실행 지침
```

**경계 원칙:** 각 모듈은 한 책임만 가진다. `gitutil`/`transcripts`/`requests_inbox`는 순수 입력 어댑터(테스트 쉬움), `batch`는 예산 로직, `collect`/`finalize`/`run`은 오케스트레이션, LLM 지식은 `prompts/process.md`에만 둔다.

**표준 데이터 스키마 (전 태스크 공통):**

`config/sources.json`
```json
{
  "base_path": "~/Codes",
  "transcripts_dir": "~/.claude/projects",
  "char_budget": 200000,
  "digest_min": 5,
  "digest_max": 7,
  "repos": [
    { "name": "skewnono_v3_nuxt",   "globs": ["docs/**/*.md"] },
    { "name": "auto_recipe_creator", "globs": ["**/*.md"] },
    { "name": "wiki_for_office",     "globs": ["docs/**/*.md"] }
  ]
}
```

`state/progress.json`
```json
{
  "repos": { "skewnono_v3_nuxt": "abc123" },
  "transcripts": { "<rel/path.jsonl>": 42 },
  "last_run": "2026-06-14"
}
```

소비 단위(Unit) dict — collect 가 만들고 batch 가 소비:
```python
{ "kind": "request"|"repo"|"transcript",
  "id": "wiki_for_office",            # 표시용 식별자
  "provenance": "repo:wiki_for_office (docs/**/*.md)",
  "text": "...원문...",
  "advance": {...} }                  # finalize 가 상태 전진에 쓰는 데이터
```

`state/consumed-<date>.json` (매니페스트)
```json
{ "repos": {"wiki_for_office": "newsha"},
  "transcripts": {"<rel/path.jsonl>": 57},
  "requests": ["requests/inbox/poetic.md"],
  "deferred": 2 }
```

---

## Task 0: 프로젝트 스캐폴딩 & uv/테스트 인프라

**Files:**
- Create: `pyproject.toml`
- Create: `.python-version`
- Create: `scripts/pipeline/__init__.py` (빈 파일)
- Create: `config/sources.json`
- Create: `.gitignore`

- [ ] **Step 1: 패키지·디렉터리 생성**

```bash
mkdir -p scripts/pipeline tests prompts requests/inbox requests/done daily notes/by-register state
touch scripts/pipeline/__init__.py
```

- [ ] **Step 2: `pyproject.toml` 작성** (uv 프로젝트 + pytest pythonpath)

```toml
[project]
name = "english-study"
version = "0.1.0"
description = "Nightly English-expression study pipeline"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = ["pytest>=8"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["scripts"]   # tests 가 `from pipeline.X import Y` 로 import 가능
```

- [ ] **Step 3: `.python-version` 작성** (uv 가 이 버전을 고정·자동 설치)

```
3.11
```

- [ ] **Step 4: `config/sources.json` 작성** — 위 표준 스키마 그대로 사용 (3개 repo)

- [ ] **Step 5: `.gitignore` 작성**

```
__pycache__/
.pytest_cache/
.venv/
state/batch-*.md
state/consumed-*.json
state/run.log
```

- [ ] **Step 6: uv 환경 동기화 + pytest 가 빈 상태로 동작하는지 확인**

Run: `uv sync && uv run pytest -q`
Expected: uv 가 `.venv` 생성 + pytest 설치, 그리고 `no tests ran` (collection 에러 없이 종료)

- [ ] **Step 7: Commit** (`uv.lock` 포함 — 재현성)

```bash
git add pyproject.toml .python-version uv.lock scripts/pipeline/__init__.py config/sources.json .gitignore
git commit -m "chore: scaffold english-study uv project and test infra"
```

---

## Task 1: config 모듈 (경로·설정·상태 로드/저장)

**Files:**
- Create: `scripts/pipeline/config.py`
- Test: `tests/test_config.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
import json
from pipeline import config

def test_load_config_expands_and_reads(tmp_path):
    cfg_file = tmp_path / "sources.json"
    cfg_file.write_text(json.dumps({"base_path": "~/Codes", "repos": []}), encoding="utf-8")
    cfg = config.load_config(cfg_file)
    assert cfg["repos"] == []
    assert cfg["base_path"] == "~/Codes"

def test_load_state_missing_returns_default(tmp_path):
    st = config.load_state(tmp_path / "nope.json")
    assert st == {"repos": {}, "transcripts": {}, "last_run": None}

def test_save_then_load_state_roundtrip(tmp_path):
    p = tmp_path / "progress.json"
    config.save_state({"repos": {"a": "sha"}, "transcripts": {}, "last_run": "2026-06-14"}, p)
    assert config.load_state(p)["repos"]["a"] == "sha"
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_config.py -q`
Expected: FAIL (`ModuleNotFoundError: No module named 'pipeline.config'` 또는 attribute 없음)

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/config.py`)

```python
import copy
import json
from pathlib import Path

DEFAULT_STATE = {"repos": {}, "transcripts": {}, "last_run": None}

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
    # deepcopy 로 매 호출 독립 사본 반환 (DEFAULT_STATE 중첩 dict 오염 방지)
    if not path.exists():
        return copy.deepcopy(DEFAULT_STATE)
    data = json.loads(path.read_text(encoding="utf-8"))
    return {**copy.deepcopy(DEFAULT_STATE), **data}

def save_state(state: dict, path: Path | None = None) -> None:
    path = Path(path) if path else state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_config.py -q`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/config.py tests/test_config.py
git commit -m "feat: add config/state loader for pipeline"
```

---

## Task 2: gitutil 모듈 (HEAD SHA, 증분 변경 .md, glob 매칭)

**Files:**
- Create: `scripts/pipeline/gitutil.py`
- Test: `tests/test_gitutil.py`

- [ ] **Step 1: 실패하는 테스트 작성** (임시 git repo fixture 사용)

```python
import subprocess
from pathlib import Path
import pytest
from pipeline import gitutil

def _run(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True,
                   capture_output=True, text=True)

@pytest.fixture
def repo(tmp_path):
    r = tmp_path / "proj"
    r.mkdir()
    _run(r, "init", "-q")
    _run(r, "config", "user.email", "t@t.t")
    _run(r, "config", "user.name", "t")
    (r / "docs").mkdir()
    (r / "docs" / "a.md").write_text("first", encoding="utf-8")
    (r / "README.md").write_text("readme", encoding="utf-8")
    _run(r, "add", "-A")
    _run(r, "commit", "-q", "-m", "c1")
    return r

def test_glob_to_regex_matches_nested():
    assert gitutil._glob_to_regex("docs/**/*.md").match("docs/x/y.md")
    assert gitutil._glob_to_regex("docs/**/*.md").match("docs/a.md")
    assert not gitutil._glob_to_regex("docs/**/*.md").match("src/a.md")
    assert gitutil._glob_to_regex("**/*.md").match("anything/here.md")

def test_head_sha_returns_40_hex(repo):
    sha = gitutil.head_sha(repo)
    assert len(sha) == 40

def test_changed_md_since_none_returns_all_matching(repo):
    files = gitutil.changed_md_files(repo, None, ["docs/**/*.md"])
    assert files == ["docs/a.md"]   # README.md 는 glob 밖

def test_changed_md_since_sha_returns_only_new(repo):
    old = gitutil.head_sha(repo)
    (repo / "docs" / "b.md").write_text("second", encoding="utf-8")
    _run(repo, "add", "-A")
    _run(repo, "commit", "-q", "-m", "c2")
    files = gitutil.changed_md_files(repo, old, ["docs/**/*.md"])
    assert files == ["docs/b.md"]
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_gitutil.py -q`
Expected: FAIL (module/attr 없음)

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/gitutil.py`)

```python
import re
import subprocess
from pathlib import Path

def _git(repo: Path, *args: str) -> str:
    res = subprocess.run(["git", "-C", str(repo), *args],
                         capture_output=True, text=True, check=True)
    return res.stdout.strip()

def _glob_to_regex(glob: str) -> re.Pattern:
    # ** => 디렉터리 가로지름, * => 한 세그먼트 내. 순서대로 치환.
    g = glob.replace(".", r"\.")
    g = g.replace("**/", "\x00").replace("**", "\x01").replace("*", "[^/]*")
    g = g.replace("\x00", "(?:.*/)?").replace("\x01", ".*")
    return re.compile("^" + g + "$")

def _matches_any(path: str, globs: list[str]) -> bool:
    return any(_glob_to_regex(g).match(path) for g in globs)

def head_sha(repo: Path) -> str:
    return _git(repo, "rev-parse", "HEAD")

def pull(repo: Path) -> None:
    # 새벽 무인 실행: 충돌 시 조용히 건너뛴다(다음 실행에서 재시도)
    try:
        _git(repo, "pull", "--ff-only", "--quiet")
    except subprocess.CalledProcessError:
        pass

def changed_md_files(repo: Path, since_sha: str | None, globs: list[str]) -> list[str]:
    if since_sha is None:
        candidates = _git(repo, "ls-files").splitlines()
    else:
        candidates = _git(repo, "diff", "--name-only", "--diff-filter=ACMR",
                          f"{since_sha}", "HEAD").splitlines()
    out = [p for p in candidates
           if _matches_any(p, globs) and (repo / p).exists()]
    return sorted(out)
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_gitutil.py -q`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/gitutil.py tests/test_gitutil.py
git commit -m "feat: add git incremental markdown collector with glob matching"
```

---

## Task 3: transcripts 모듈 (오프셋 기준 새 대화 추출)

**Files:**
- Create: `scripts/pipeline/transcripts.py`
- Test: `tests/test_transcripts.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
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
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_transcripts.py -q`
Expected: FAIL (module/attr 없음)

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/transcripts.py`)

```python
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
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_transcripts.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/transcripts.py tests/test_transcripts.py
git commit -m "feat: add transcript reader with per-file offset tracking"
```

---

## Task 4: requests_inbox 모듈

**Files:**
- Create: `scripts/pipeline/requests_inbox.py`
- Test: `tests/test_requests_inbox.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
from pipeline import requests_inbox

def test_pending_requests_lists_only_md(tmp_path):
    inbox = tmp_path / "requests" / "inbox"
    inbox.mkdir(parents=True)
    (inbox / "poetic.md").write_text("이 표현 시적으로", encoding="utf-8")
    (inbox / "notes.txt").write_text("ignore", encoding="utf-8")
    found = requests_inbox.pending_requests(tmp_path)
    assert [p.name for p in found] == ["poetic.md"]

def test_pending_requests_empty_when_no_inbox(tmp_path):
    assert requests_inbox.pending_requests(tmp_path) == []
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_requests_inbox.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/requests_inbox.py`)

```python
from pathlib import Path

def pending_requests(root: Path) -> list[Path]:
    inbox = Path(root) / "requests" / "inbox"
    if not inbox.exists():
        return []
    return sorted(inbox.glob("*.md"))
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_requests_inbox.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/requests_inbox.py tests/test_requests_inbox.py
git commit -m "feat: add requests inbox reader"
```

---

## Task 5: batch 모듈 (예산 내 조립 + 소비 단위 반환)

**Files:**
- Create: `scripts/pipeline/batch.py`
- Test: `tests/test_batch.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
from pipeline import batch

def _unit(kind, uid, text):
    return {"kind": kind, "id": uid, "provenance": f"{kind}:{uid}",
            "text": text, "advance": {uid: True}}

def test_build_batch_includes_until_budget(tmp_path):
    units = [_unit("request", "r1", "a" * 100),
             _unit("repo", "p1", "b" * 100),
             _unit("transcript", "t1", "c" * 100)]
    text, consumed = batch.build_batch(units, char_budget=250, today="2026-06-14")
    # 첫 두 단위(=200자)는 들어가고 세 번째는 예산 초과로 제외
    assert [u["id"] for u in consumed] == ["r1", "p1"]
    assert "request:r1" in text and "repo:p1" in text
    assert "transcript:t1" not in text

def test_build_batch_always_includes_at_least_one(tmp_path):
    units = [_unit("repo", "big", "x" * 10000)]
    text, consumed = batch.build_batch(units, char_budget=10, today="2026-06-14")
    assert [u["id"] for u in consumed] == ["big"]

def test_build_batch_empty_units():
    text, consumed = batch.build_batch([], char_budget=100, today="2026-06-14")
    assert consumed == []
    assert "2026-06-14" in text
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_batch.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/batch.py`)

```python
def build_batch(units: list[dict], char_budget: int, today: str) -> tuple[str, list[dict]]:
    header = f"# 수집 배치 — {today}\n\n"
    parts = [header]
    consumed: list[dict] = []
    used = 0
    for u in units:
        block = f"\n## [{u['provenance']}]\n\n{u['text']}\n"
        # 최소 한 단위는 무조건 포함, 이후엔 예산을 지킨다
        if consumed and used + len(block) > char_budget:
            continue
        parts.append(block)
        consumed.append(u)
        used += len(block)
    return "".join(parts), consumed
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_batch.py -q`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/batch.py tests/test_batch.py
git commit -m "feat: add budget-bounded batch assembler"
```

---

## Task 6: tokenlog 모듈 (claude json usage 파싱)

**Files:**
- Create: `scripts/pipeline/tokenlog.py`
- Test: `tests/test_tokenlog.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
import json
from pipeline import tokenlog

SAMPLE = json.dumps({
    "type": "result", "subtype": "success",
    "total_cost_usd": 0.0421,
    "usage": {"input_tokens": 1200, "output_tokens": 3400,
              "cache_read_input_tokens": 800, "cache_creation_input_tokens": 0},
    "result": "done"
})

def test_parse_usage_extracts_fields():
    u = tokenlog.parse_usage(SAMPLE)
    assert u["input_tokens"] == 1200
    assert u["output_tokens"] == 3400
    assert u["cache_read_input_tokens"] == 800
    assert u["cost_usd"] == 0.0421

def test_parse_usage_defensive_on_garbage():
    u = tokenlog.parse_usage("not json")
    assert u["input_tokens"] == 0 and u["cost_usd"] == 0.0

def test_append_token_log_writes_jsonl(tmp_path):
    tokenlog.append_token_log(tmp_path, "2026-06-14",
                              {"input_tokens": 10, "output_tokens": 20,
                               "cache_read_input_tokens": 0, "cost_usd": 0.01},
                              items_processed=3)
    log = tmp_path / "state" / "token-log.jsonl"
    line = json.loads(log.read_text(encoding="utf-8").strip())
    assert line["date"] == "2026-06-14"
    assert line["output_tokens"] == 20
    assert line["items_processed"] == 3
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_tokenlog.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/tokenlog.py`)

```python
import json
from pathlib import Path

def parse_usage(claude_json: str) -> dict:
    try:
        obj = json.loads(claude_json)
    except (json.JSONDecodeError, TypeError):
        obj = {}
    u = obj.get("usage", {}) if isinstance(obj, dict) else {}
    return {
        "input_tokens": u.get("input_tokens", 0),
        "output_tokens": u.get("output_tokens", 0),
        "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
        "cost_usd": obj.get("total_cost_usd", 0.0) if isinstance(obj, dict) else 0.0,
    }

def append_token_log(root: Path, date: str, usage: dict, items_processed: int) -> None:
    log = Path(root) / "state" / "token-log.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    entry = {"date": date, **usage, "items_processed": items_processed}
    with log.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_tokenlog.py -q`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/tokenlog.py tests/test_tokenlog.py
git commit -m "feat: add claude token usage parser and log"
```

---

## Task 7: collect 오케스트레이션

**Files:**
- Create: `scripts/pipeline/collect.py`
- Test: `tests/test_collect.py`

- [ ] **Step 1: 실패하는 통합 테스트 작성** (모듈 함수 주입으로 git/transcript 격리)

```python
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
    (root / "requests" / "inbox").mkdir(parents=True)
    (root / "requests" / "inbox" / "poetic.md").write_text("시적으로", encoding="utf-8")

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
    assert manifest["requests"] == ["requests/inbox/poetic.md"]
    assert result["item_count"] == 3   # request + repo + transcript
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_collect.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/collect.py`)

```python
import json
import os
from datetime import date
from pathlib import Path

from pipeline import config, gitutil, transcripts, requests_inbox, batch

def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))

def collect(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()
    cfg = config.load_config(root / "config" / "sources.json")
    state = config.load_state(root / "state" / "progress.json")

    units: list[dict] = []
    repo_heads: dict[str, str] = {}

    # 1) 요청(주문서) — 최우선
    for req in requests_inbox.pending_requests(root):
        rel = req.relative_to(root).as_posix()
        units.append({"kind": "request", "id": req.name,
                      "provenance": f"request:{rel}", "text": req.read_text(encoding="utf-8"),
                      "advance": {"request": rel}})

    # 2) repo 별 증분 마크다운 (repo 1개 = 단위 1개, all-or-nothing)
    base = _expand(cfg["base_path"])
    for r in cfg["repos"]:
        repo_path = base / r["name"]
        if not repo_path.exists():
            continue
        gitutil.pull(repo_path)
        since = state["repos"].get(r["name"])
        files = gitutil.changed_md_files(repo_path, since, r["globs"])
        repo_heads[r["name"]] = gitutil.head_sha(repo_path)
        if not files:
            continue
        body = []
        for f in files:
            body.append(f"### {f}\n\n{(repo_path / f).read_text(encoding='utf-8', errors='replace')}")
        units.append({"kind": "repo", "id": r["name"],
                      "provenance": f"repo:{r['name']} ({','.join(r['globs'])})",
                      "text": "\n\n".join(body),
                      "advance": {"repo": r["name"], "sha": repo_heads[r["name"]]}})

    # 3) 트랜스크립트 — 파일 1개 = 단위 1개
    tx_dir = _expand(cfg["transcripts_dir"])
    recs, new_offsets = transcripts.new_messages(tx_dir, state["transcripts"])
    by_file: dict[str, list[str]] = {}
    for rec in recs:
        by_file.setdefault(rec["file"], []).append(f"[{rec['role']}] {rec['text']}")
    for fname, texts in by_file.items():
        units.append({"kind": "transcript", "id": fname,
                      "provenance": f"transcript:{fname}", "text": "\n\n".join(texts),
                      "advance": {"transcript": fname, "offset": new_offsets[fname]}})

    # 예산 내 조립
    batch_text, consumed = batch.build_batch(units, cfg.get("char_budget", 200000), today)

    # 매니페스트(소비 단위만 상태 전진 대상)
    manifest = {"repos": {}, "transcripts": {}, "requests": [], "deferred": len(units) - len(consumed)}
    for u in consumed:
        adv = u["advance"]
        if u["kind"] == "repo":
            manifest["repos"][adv["repo"]] = adv["sha"]
        elif u["kind"] == "transcript":
            manifest["transcripts"][adv["transcript"]] = adv["offset"]
        elif u["kind"] == "request":
            manifest["requests"].append(adv["request"])

    (root / "state").mkdir(parents=True, exist_ok=True)
    batch_path = root / "state" / f"batch-{today}.md"
    batch_path.write_text(batch_text, encoding="utf-8")
    (root / "state" / f"consumed-{today}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"item_count": len(consumed), "deferred": manifest["deferred"],
            "batch_path": str(batch_path), "today": today}

if __name__ == "__main__":
    print(collect())
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_collect.py -q`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/collect.py tests/test_collect.py
git commit -m "feat: add collect orchestration producing batch and consumed manifest"
```

---

## Task 8: finalize 오케스트레이션 (상태 전진·요청 이동·커밋)

**Files:**
- Create: `scripts/pipeline/finalize.py`
- Test: `tests/test_finalize.py`

- [ ] **Step 1: 실패하는 테스트 작성**

```python
import json
from pathlib import Path
from pipeline import finalize, config

def test_finalize_advances_state_and_moves_requests(tmp_path, monkeypatch):
    root = tmp_path
    (root / "state").mkdir()
    (root / "requests" / "inbox").mkdir(parents=True)
    (root / "requests" / "done").mkdir(parents=True)
    (root / "requests" / "inbox" / "poetic.md").write_text("시적", encoding="utf-8")

    config.save_state({"repos": {}, "transcripts": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-14.json").write_text(json.dumps({
        "repos": {"proj": "newsha"},
        "transcripts": {"s.jsonl": 5},
        "requests": ["requests/inbox/poetic.md"],
        "deferred": 0,
    }), encoding="utf-8")

    # git 호출은 가짜로
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-14")

    st = config.load_state(root / "state" / "progress.json")
    assert st["repos"]["proj"] == "newsha"
    assert st["transcripts"]["s.jsonl"] == 5
    assert st["last_run"] == "2026-06-14"
    # 요청이 done 으로 이동
    assert not (root / "requests" / "inbox" / "poetic.md").exists()
    assert (root / "requests" / "done" / "2026-06-14-poetic.md").exists()
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_finalize.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/finalize.py`)

```python
import json
import shutil
import subprocess
from datetime import date
from pathlib import Path

from pipeline import config

def _git_commit_push(root: Path, msg: str) -> None:
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=False)
    subprocess.run(["git", "-C", str(root), "commit", "-m", msg], check=False)
    subprocess.run(["git", "-C", str(root), "push"], check=False)

def finalize(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()

    manifest_path = root / "state" / f"consumed-{today}.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    state = config.load_state(root / "state" / "progress.json")
    state["repos"].update(manifest.get("repos", {}))
    state["transcripts"].update(manifest.get("transcripts", {}))
    state["last_run"] = today
    config.save_state(state, root / "state" / "progress.json")

    # 처리된 요청을 done 으로 이동 (멱등성)
    done_dir = root / "requests" / "done"
    done_dir.mkdir(parents=True, exist_ok=True)
    for rel in manifest.get("requests", []):
        src = root / rel
        if src.exists():
            shutil.move(str(src), str(done_dir / f"{today}-{src.name}"))

    _git_commit_push(root, f"study: nightly digest {today}")
    return {"committed": True, "today": today}

if __name__ == "__main__":
    print(finalize())
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_finalize.py -q`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/finalize.py tests/test_finalize.py
git commit -m "feat: add finalize step advancing state and committing output"
```

---

## Task 9: LLM 작업 지침 (`prompts/process.md`)

**Files:**
- Create: `prompts/process.md`

이 파일은 단위 테스트 대상이 아니다(LLM 프롬프트). Task 11의 통합 실행에서 검증한다.

- [ ] **Step 1: `prompts/process.md` 작성** (아래 내용 그대로)

````markdown
당신은 한국인 개발자의 영어 학습 튜터입니다. 주어진 배치 파일을 읽고
의미 있는 영어 표현을 추출해 학습 자료로 가공합니다.

## 입력
- 배치 파일 경로는 이 프롬프트 끝에 주어집니다. Read 도구로 읽으세요.
- 배치는 `## [provenance]` 헤더로 구분된 원문 묶음입니다.
  provenance 종류: `request:` (사용자 주문), `repo:` (프로젝트 docs), `transcript:` (대화).

## 작업
1. **표현 추출**: 배치에서 학습 가치가 있는 영어 문장/숙어/표현을 고릅니다.
   사소한 보일러플레이트(코드, 경로, 반복 문구)는 버립니다.
2. **레지스터 분류**: 각 표현을 professional / conversational / casual / technical 중
   하나 이상으로 태깅합니다.
3. **한글→영어 코칭**: 원문이 한국어인 경우(특히 transcript 의 사용자 프롬프트),
   "내가 쓴 한글 / 자연스러운 영어 / 왜 이렇게" 3단으로 코칭 카드를 만듭니다.
4. **중복 제거**: `notes/by-register/*.md` 의 기존 표현과 텍스트가 정확히 일치하면 건너뜁니다.
5. **요청 수행**: `request:` 항목은 사용자 주문(예: "특정 단어로 문장 더", "시적으로 표현")
   을 실제로 수행해 결과를 만듭니다.

## 출력 (모두 마크다운, UTF-8)
오늘 날짜와 출력 폴더는 프롬프트 끝에 주어집니다.

- `daily/<날짜>/new-expressions.md` — 그날 수집한 표현 전체 해설. 각 항목:
  ```
  ## "표현"
  - 레지스터: conversational, professional
  - 출처: repo:wiki_for_office
  - 한국어: ...
  - 설명: ...
  - 예문: ...
  ```
- `daily/<날짜>/digest.md` — 그중 핵심 5~7개만 1~2줄로 요약한 "오늘의 표현".
  맨 끝에 `> 처리 항목 N개 / 미뤄진 항목 M개` 푸터.
- `daily/<날짜>/requests/<요청이름>.md` — 각 주문 결과(요청이 있을 때만).
- `notes/by-register/<레지스터>.md` — 새 표현을 해당 레지스터 파일에 append.
- `notes/index.md` — 표현명 + daily 링크를 알파벳 순으로 갱신.

## 원칙
- 새 표현이 없으면 그날 daily 폴더에 "수집된 새 표현이 없습니다"만 적습니다.
- 추측해서 표현을 지어내지 말고 배치에 실제로 등장한 영어만 다룹니다.
- 한국어 해설로 친절하게, 그러나 간결하게.
````

- [ ] **Step 2: Commit**

```bash
git add prompts/process.md
git commit -m "docs: add LLM processing prompt for study extraction"
```

---

## Task 10: run.py 오케스트레이터 (collect → claude -p → finalize)

**Files:**
- Create: `scripts/pipeline/run.py`
- Test: `tests/test_run.py`

- [ ] **Step 1: 실패하는 테스트 작성** (claude 호출을 가짜로 대체)

```python
import json
from pathlib import Path
from pipeline import run as runmod

def test_run_skips_llm_when_no_items(tmp_path, monkeypatch):
    calls = {"claude": 0, "finalize": 0}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 0, "deferred": 0,
                                                  "batch_path": "x", "today": "2026-06-14"})
    monkeypatch.setattr(runmod, "_invoke_claude", lambda *a, **k: calls.__setitem__("claude", 1) or "{}")
    monkeypatch.setattr(runmod, "finalize", lambda root, today=None: calls.__setitem__("finalize", 1))
    runmod.run(root=tmp_path)
    assert calls["claude"] == 0          # 아이템 0이면 LLM 호출 안 함
    assert calls["finalize"] == 0

def test_run_invokes_llm_and_logs_tokens(tmp_path, monkeypatch):
    (tmp_path / "state").mkdir()
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 2, "deferred": 1,
                                                  "batch_path": str(tmp_path / "b.md"),
                                                  "today": "2026-06-14"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda prompt, root: json.dumps(
                            {"usage": {"input_tokens": 5, "output_tokens": 7,
                                       "cache_read_input_tokens": 0},
                             "total_cost_usd": 0.02}))
    finalized = {}
    monkeypatch.setattr(runmod, "finalize",
                        lambda root, today=None: finalized.__setitem__("done", today))
    runmod.run(root=tmp_path)
    log = (tmp_path / "state" / "token-log.jsonl").read_text(encoding="utf-8").strip()
    assert json.loads(log)["output_tokens"] == 7
    assert finalized["done"] == "2026-06-14"
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `uv run pytest tests/test_run.py -q`
Expected: FAIL

- [ ] **Step 3: 최소 구현 작성** (`scripts/pipeline/run.py`)

```python
import subprocess
from pathlib import Path

from pipeline import config, tokenlog
from pipeline.collect import collect
from pipeline.finalize import finalize

def _invoke_claude(prompt: str, root: Path) -> str:
    # 무인 실행: 도구를 파일 계열로만 제한한다. 배치에 섞일 수 있는
    # 프롬프트 인젝션이 Bash·네트워크로 번지지 못하게 막는 방어선.
    # (git push 는 LLM 이 아니라 finalize 의 Python 이 수행)
    res = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json",
         "--allowedTools", "Read,Edit,Write,Glob"],
        cwd=str(root), capture_output=True, text=True)
    if res.returncode != 0:
        return ""
    return res.stdout

def run(root: Path | None = None) -> dict:
    root = Path(root) if root else config.root()
    info = collect(root=root)
    today = info["today"]
    if info["item_count"] == 0:
        print(f"[{today}] 처리할 새 항목 없음. 종료.")
        return {"status": "empty", "today": today}

    prompt = _build_prompt(root, info)
    out = _invoke_claude(prompt, root)
    # LLM 호출 실패 시 상태를 전진시키지 않는다 (다음 실행에서 재시도, 데이터 유실 방지)
    if not out.strip():
        print(f"[{today}] LLM 호출 실패 — 상태를 전진시키지 않고 종료(다음 실행에서 재시도).")
        return {"status": "llm_failed", "today": today}
    usage = tokenlog.parse_usage(out)
    tokenlog.append_token_log(root, today, usage, info["item_count"])

    finalize(root=root, today=today)
    print(f"[{today}] 완료. 항목 {info['item_count']}개, 미뤄짐 {info['deferred']}개, "
          f"토큰 out={usage['output_tokens']}, 비용 ${usage['cost_usd']}")
    return {"status": "done", "today": today, **usage}

def _build_prompt(root: Path, info: dict) -> str:
    process_md = root / "prompts" / "process.md"
    base = process_md.read_text(encoding="utf-8") if process_md.exists() else ""
    today = info["today"]
    return (f"{base}\n\n---\n"
            f"처리할 배치 파일: {info['batch_path']}\n"
            f"오늘 날짜: {today}\n"
            f"출력 폴더 접두사: daily/{today}/\n")

if __name__ == "__main__":
    run()
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `uv run pytest tests/test_run.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: 전체 테스트 스위트 확인**

Run: `uv run pytest -q`
Expected: PASS (전 태스크 합계, 실패 0)

- [ ] **Step 6: Commit**

```bash
git add scripts/pipeline/run.py tests/test_run.py
git commit -m "feat: add run orchestrator wiring collect, claude -p, and finalize"
```

---

## Task 11: launchd 진입 스크립트 & plist & CLAUDE.md

**Files:**
- Create: `scripts/run.sh`
- Create: `scripts/com.daeyoung.english-study.plist`
- Create: `CLAUDE.md`

Mac 전용 구성. 단위 테스트 대신 Task 12에서 수동 검증한다.

- [ ] **Step 1: `scripts/run.sh` 작성**

```bash
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
```

> 주의: launchd PATH 에 `uv` 설치 위치가 포함돼야 한다. `which uv` 로 확인 후
> 다른 경로면 위 `export PATH` 에 추가한다 (대개 `$HOME/.local/bin`).

- [ ] **Step 2: 실행 권한 부여**

```bash
chmod +x scripts/run.sh
```

- [ ] **Step 3: `scripts/com.daeyoung.english-study.plist` 작성**

`<경로>` 두 곳을 실제 Mac 절대경로(`/Users/<you>/Codes/english-study`)로 바꿔서 사용.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.daeyoung.english-study</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>/Users/<you>/Codes/english-study/scripts/run.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key><integer>23</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>/Users/<you>/Codes/english-study/state/launchd.out.log</string>
  <key>StandardErrorPath</key>
  <string>/Users/<you>/Codes/english-study/state/launchd.err.log</string>
</dict>
</plist>
```

- [ ] **Step 4: `CLAUDE.md` 작성** (헤드리스 실행 시 동작 지침)

```markdown
# english-study — 자동 영어 학습 파이프라인

매일 밤 23:00 Mac launchd 가 `scripts/run.sh` → `python3 -m pipeline.run` 을 실행한다.

## 흐름
1. `collect` — git 공유 docs + Mac 트랜스크립트 + `requests/inbox` 에서 새 영어를
   토큰 예산 안에서 `state/batch-<날짜>.md` 로 모은다. 소비분은 `state/consumed-<날짜>.json` 에 기록.
2. `claude -p` — `prompts/process.md` 지침대로 추출·분류·코칭하여 `daily/`·`notes/` 에 쓴다.
3. `finalize` — 소비한 만큼만 `state/progress.json` 을 전진시키고, 처리한 요청을
   `requests/done/` 으로 옮기고, commit & push.

## 직접 쓰는 법
- 자기 전 `requests/inbox/<주문>.md` 에 요청을 적어두면 다음 실행이 처리한다.
- 아침에 `daily/<오늘날짜>/digest.md` 를 읽는다.
- 토큰 사용 추이는 `state/token-log.jsonl`.

## 수동 실행
`PYTHONPATH=scripts uv run python -m pipeline.run`
```

- [ ] **Step 5: Commit**

```bash
git add scripts/run.sh scripts/com.daeyoung.english-study.plist CLAUDE.md
git commit -m "feat: add launchd entry script, plist, and runtime CLAUDE.md"
```

---

## Task 12: Mac 통합 검증 & launchd 설치 (수동)

**Files:** 없음 (운영 절차). 이 태스크는 **Mac에서** 수행한다.

- [ ] **Step 1: uv 동기화 + 수동 1회 실행으로 end-to-end 확인**

```bash
cd ~/Codes/english-study
uv sync                                          # .venv + pytest 준비
uv run pytest -q                                 # Mac 에서도 코어 통과 확인
PYTHONPATH=scripts uv run python -m pipeline.run
```
Expected: `daily/<오늘>/digest.md` 와 `new-expressions.md` 생성, `state/token-log.jsonl` 에 1줄 추가, `state/progress.json` 의 SHA/오프셋 전진, 새 커밋 1개.

- [ ] **Step 2: 증분 동작 확인 (재실행 시 빈 처리)**

```bash
PYTHONPATH=scripts uv run python -m pipeline.run
```
Expected: `처리할 새 항목 없음. 종료.` (이미 다 처리됨 → 멱등)

- [ ] **Step 3: 요청 메커니즘 확인**

```bash
echo "'resilient' 가 들어간 예문 3개 만들어줘" > requests/inbox/test-req.md
PYTHONPATH=scripts uv run python -m pipeline.run
ls daily/$(date +%F)/requests/        # 결과 생성 확인
ls requests/done/                     # test-req.md 가 날짜 접두사로 이동됐는지
```

- [ ] **Step 4: launchd 등록**

```bash
cp scripts/com.daeyoung.english-study.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.daeyoung.english-study.plist
launchctl list | grep english-study   # 등록 확인
```

- [ ] **Step 5: 즉시 1회 강제 실행으로 launchd 경로 검증**

```bash
launchctl start com.daeyoung.english-study
sleep 5
tail -n 20 state/run.log               # 정상 로그 확인
```

- [ ] **Step 6: GitHub remote 연결 (최초 1회)**

```bash
gh repo create DarrenKoi/english-study --private --source=. --remote=origin --push
```

- [ ] **Step 7: 운영 메모를 README 로 커밋**

```bash
cat > README.md <<'EOF'
# english-study
매일 밤 23:00 Mac launchd 가 프로젝트 docs·대화에서 영어를 모아 학습 다이제스트를 만든다.
- 주문: `requests/inbox/<이름>.md` 에 적어두면 다음 새벽에 처리.
- 아침 학습: `daily/<날짜>/digest.md`.
- 상태: `state/progress.json`, 토큰: `state/token-log.jsonl`.
- 수동 실행: `PYTHONPATH=scripts uv run python -m pipeline.run`
EOF
git add README.md
git commit -m "docs: add operations README"
git push
```

---

## Self-Review 체크 결과

- **Spec 커버리지:** Mac 로컬(Task 11-12), git SHA 증분(Task 2/7/8), 트랜스크립트 수집(Task 3), 레지스터 분류·한글→영어 코칭(Task 9 prompt), daily/notes 2층 구조(Task 9 출력), 요청 메커니즘(Task 4/8/12), 토큰 트래킹(Task 6/10), 일일 예산·큐잉(Task 5/7), 23:00 launchd(Task 11). ✅ 전 항목 대응.
- **타입 일관성:** Unit dict(`kind/id/provenance/text/advance`), manifest 키(`repos/transcripts/requests/deferred`), state 키(`repos/transcripts/last_run`), usage 키(`input_tokens/output_tokens/cache_read_input_tokens/cost_usd`) — 전 태스크에서 동일하게 사용. `collect`/`finalize`/`run` 함수 시그니처 일치. ✅
- **Placeholder:** 코드/명령/프롬프트 모두 실제 내용으로 채움. plist 의 `<you>` 절대경로만 의도적 사용자 치환 지점(주석 명시). ✅
```
