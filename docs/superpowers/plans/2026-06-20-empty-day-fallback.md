# Empty-Day Fallback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 빈 날(정상 collect 가 0개)에 ① 7일 너머 노화 문서를 따라잡고(backlog) ② 그래도 없으면 `notes/` 누적 표현으로 복습을 생성하며(review) ③ 둘 다 비면 중단(empty)하도록 파이프라인을 확장한다.

**Architecture:** `collect()` 가 `mode`("normal"|"backlog"|"review"|"empty")를 반환한다. 정상 패스가 비면 같은 문서 수집 로직을 더 넓은 윈도(`backlog_days`)로 재실행하고, 그래도 비면 신규 `pipeline/review.py` 가 `notes/index.md` 의 미복습 표현을 골라 복습 단위를 만든다. 백로그 문서는 기존 `doc` kind 를 그대로 써서 finalize 의 ledger 가 무변경으로 동작하고, 복습 진행은 별도 ledger `state/reviewed.json` 으로 추적한다.

**Tech Stack:** Python 3, pytest, monkeypatch. 외부 의존성 없음(표준 라이브러리만).

## Global Constraints

- 정상 흐름 무변경: 폴백은 정상 패스의 `consumed` 가 비었을 때만 진입한다.
- 상태 전진은 성공(finalize) 시에만: `docs_seen` 과 동일하게 `reviewed.json` 도 finalize 에서만 전진한다.
- 파일 도구만: 무인 LLM 호출은 `Read,Edit,Write,Glob` 로 제한된다(기존 `run.py` 규약 유지).
- 설정 기본값: `backlog_days` 기본 14, 복습 개수는 기존 `digest_max`(기본 7) 재사용.
- 한국어 주석/메시지는 기존 코드 톤을 따른다.
- 테스트 실행: `PYTHONPATH=scripts uv run pytest`.

---

### Task 1: `pipeline/review.py` — 복습 소재 관리 모듈

**Files:**
- Create: `scripts/pipeline/review.py`
- Test: `tests/test_review.py`

**Interfaces:**
- Produces:
  - `parse_index(root: Path) -> list[dict]` — 각 항목 `{"expr": str, "date": str, "link": str}`. `notes/index.md` 부재 시 `[]`.
  - `load_reviewed(root: Path) -> dict` — `state/reviewed.json`(표현→복습일), 부재 시 `{}`.
  - `save_reviewed(root: Path, data: dict) -> None`
  - `mark_reviewed(root: Path, exprs: list[str], today: str) -> None` — 각 표현을 `today` 로 표시해 저장.
  - `select_unreviewed(root: Path, n: int) -> list[dict]` — reviewed 에 없는 표현을 수집일 오래된 순으로 최대 `n`개(표현 중복 제거).

- [ ] **Step 1: Write the failing tests**

Create `tests/test_review.py`:

```python
import json
from pathlib import Path

from pipeline import review


def _index(root: Path, body: str) -> None:
    (root / "notes").mkdir(parents=True, exist_ok=True)
    (root / "notes" / "index.md").write_text(body, encoding="utf-8")


SAMPLE = """# 표현 인덱스

- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20
- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17
- [anchor on (the first plausible idea)](daily/2026-06-18/new-expressions.md) — 2026-06-18
"""


def test_parse_index_extracts_expr_date_link(tmp_path):
    _index(tmp_path, SAMPLE)
    rows = review.parse_index(tmp_path)
    exprs = {r["expr"] for r in rows}
    assert exprs == {"blast radius", "backstop", "anchor on (the first plausible idea)"}
    row = next(r for r in rows if r["expr"] == "backstop")
    assert row["date"] == "2026-06-17"
    assert row["link"] == "daily/2026-06-17/new-expressions.md"


def test_parse_index_missing_file_returns_empty(tmp_path):
    assert review.parse_index(tmp_path) == []


def test_select_unreviewed_sorts_oldest_first_and_limits(tmp_path):
    _index(tmp_path, SAMPLE)
    picks = review.select_unreviewed(tmp_path, 2)
    assert [p["expr"] for p in picks] == ["backstop", "anchor on (the first plausible idea)"]


def test_select_unreviewed_excludes_reviewed(tmp_path):
    _index(tmp_path, SAMPLE)
    review.save_reviewed(tmp_path, {"backstop": "2026-06-19"})
    picks = review.select_unreviewed(tmp_path, 10)
    assert [p["expr"] for p in picks] == [
        "anchor on (the first plausible idea)", "blast radius"]


def test_select_unreviewed_exhausted_returns_empty(tmp_path):
    _index(tmp_path, SAMPLE)
    review.save_reviewed(tmp_path, {
        "backstop": "d", "anchor on (the first plausible idea)": "d", "blast radius": "d"})
    assert review.select_unreviewed(tmp_path, 10) == []


def test_mark_reviewed_persists_and_resumes_on_new_expr(tmp_path):
    _index(tmp_path, SAMPLE)
    review.mark_reviewed(tmp_path, ["backstop", "blast radius"], "2026-06-21")
    data = json.loads((tmp_path / "state" / "reviewed.json").read_text(encoding="utf-8"))
    assert data["backstop"] == "2026-06-21"
    # 새 표현이 index 에 추가되면 다시 선택 대상이 된다
    _index(tmp_path, SAMPLE + "- [new one](daily/2026-06-21/new-expressions.md) — 2026-06-21\n")
    picks = review.select_unreviewed(tmp_path, 10)
    assert [p["expr"] for p in picks] == ["anchor on (the first plausible idea)", "new one"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `PYTHONPATH=scripts uv run pytest tests/test_review.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'pipeline.review'`

- [ ] **Step 3: Write `scripts/pipeline/review.py`**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `PYTHONPATH=scripts uv run pytest tests/test_review.py -v`
Expected: PASS (6 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/review.py tests/test_review.py
git commit -m "feat(review): notes/index.md parsing + reviewed.json ledger"
```

---

### Task 2: config + `collect.py` 문서 수집 추출 (무동작-변경 리팩터)

`backlog_days` 설정을 추가하고, 정상/백로그 패스가 공유할 문서-단위 생성 로직을 `_doc_units` 헬퍼로 추출한다. 이 태스크는 동작을 바꾸지 않으며 기존 테스트가 모두 통과해야 한다.

**Files:**
- Modify: `config/sources.json`
- Modify: `scripts/pipeline/collect.py:104-118` (문서 수집 루프 추출)
- Test: `tests/test_collect.py` (기존 테스트로 회귀 확인)

**Interfaces:**
- Produces: `_doc_units(base: Path, cfg: dict, seen: dict, char_budget: int) -> tuple[list[dict], int]` — `(doc units, unread)`. 각 unit 은 기존과 동일한 `kind="doc"` 형태.

- [ ] **Step 1: Add `backlog_days` to config**

Edit `config/sources.json` — `"recent_days": 7,` 줄 다음에 추가:

```json
  "recent_days": 7,
  "backlog_days": 14,
```

- [ ] **Step 2: Extract `_doc_units` helper in `collect.py`**

`scripts/pipeline/collect.py` 상단 상수 영역에 추가(기존 `DEFAULT_RECENT_DAYS = 7` 아래):

```python
DEFAULT_BACKLOG_DAYS = 14
```

`discover_doc_files` 함수 정의 바로 아래에 새 헬퍼를 추가:

```python
def _doc_units(base: Path, cfg: dict, seen: dict, char_budget: int) -> tuple[list[dict], int]:
    """문서 폴더에서 ledger(seen)에 없는 최근 수정 문서를 예산 내에서 단위로 만든다.
    cfg 의 recent_days 윈도를 그대로 쓰므로, 더 넓은 윈도(backlog)에도 재사용한다.
    반환: (units, unread). unread = 예산에 밀려 읽지 않은 문서 수."""
    units: list[dict] = []
    doc_chars, unread = 0, 0
    for d in discover_doc_files(base, cfg):
        doc_id = f"{d['project']}/{d['relpath']}"
        key = _doc_key(d["project"], d["relpath"], d["mtime"], d["size"])
        if seen.get(doc_id) == key:
            continue
        if doc_chars >= char_budget:
            unread += 1
            continue
        text = d["path"].read_text(encoding="utf-8", errors="replace")
        units.append({"kind": "doc", "id": doc_id,
                      "provenance": f"repo:{d['project']} {d['relpath']}",
                      "text": text, "advance": {"doc_id": doc_id, "doc_key": key}})
        doc_chars += len(text)
    return units, unread
```

- [ ] **Step 3: Replace the inline doc loop in `collect()` with the helper**

`collect()` 안의 문서 수집 블록(현재 `char_budget = cfg.get(...)` 부터 `doc_chars += len(text)` 까지, 약 `collect.py:104-118`)을 다음으로 교체:

```python
    char_budget = cfg.get("char_budget", 200000)
    doc_units, unread = _doc_units(base, cfg, seen, char_budget)
    units.extend(doc_units)
```

(주의: 그 앞의 `for project ... gitutil.pull(project)` 루프와 `seen`/`base`/`exclude` 정의는 그대로 둔다.)

- [ ] **Step 4: Run the full collect suite to verify no behavior change**

Run: `PYTHONPATH=scripts uv run pytest tests/test_collect.py -v`
Expected: PASS (기존 9개 테스트 모두 통과)

- [ ] **Step 5: Commit**

```bash
git add config/sources.json scripts/pipeline/collect.py
git commit -m "refactor(collect): extract _doc_units, add backlog_days config"
```

---

### Task 3: `collect.py` 빈 날 폴백 (backlog → review → empty)

**Files:**
- Modify: `scripts/pipeline/collect.py` (import, `_review_units`, `collect()` 폴백·매니페스트·반환)
- Test: `tests/test_collect.py`

**Interfaces:**
- Consumes: `review.select_unreviewed` (Task 1), `_doc_units` (Task 2).
- Produces: `collect()` 반환 dict 에 `"mode"` 추가; 매니페스트에 `"reviewed": list[str]`, `"mode": str` 추가.

- [ ] **Step 1: Write the failing tests**

`tests/test_collect.py` 끝에 추가:

```python
def _index(root: Path, body: str) -> None:
    (root / "notes").mkdir(parents=True, exist_ok=True)
    (root / "notes" / "index.md").write_text(body, encoding="utf-8")


def test_empty_day_backlog_pass_picks_aged_doc(tmp_path, monkeypatch):
    # 정상 윈도(7일) 밖, 백로그 윈도(14일) 안의 미처리 문서를 빈 날에 따라잡는다.
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _write(codes / "proj" / "docs" / "aged.md", "Aged backlog body.", age_days=10)

    result = collect.collect(root=root)
    assert result["mode"] == "backlog"
    assert result["item_count"] == 1
    assert "Aged backlog body." in _batch(root)
    assert set(_manifest(root)["docs"]) == {"proj/docs/aged.md"}


def test_empty_day_review_pass_when_no_backlog(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14, digest_max=7)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _index(root,
           "- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17\n"
           "- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20\n")

    result = collect.collect(root=root)
    assert result["mode"] == "review"
    assert result["item_count"] == 1            # 복습 단위 하나
    m = _manifest(root)
    assert m["reviewed"] == ["backstop", "blast radius"]
    assert "backstop" in _batch(root)


def test_empty_day_returns_empty_when_nothing(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)

    result = collect.collect(root=root)
    assert result["mode"] == "empty"
    assert result["item_count"] == 0


def test_review_pass_skips_already_reviewed(tmp_path, monkeypatch):
    root, codes = tmp_path / "study", tmp_path / "codes"
    _sources(root, codes, backlog_days=14)
    _no_transcripts(monkeypatch)
    _no_git(monkeypatch)
    _index(root,
           "- [backstop](daily/2026-06-17/new-expressions.md) — 2026-06-17\n"
           "- [blast radius](daily/2026-06-20/new-expressions.md) — 2026-06-20\n")
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state" / "reviewed.json").write_text(
        json.dumps({"backstop": "2026-06-19"}), encoding="utf-8")

    result = collect.collect(root=root)
    assert result["mode"] == "review"
    assert _manifest(root)["reviewed"] == ["blast radius"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `PYTHONPATH=scripts uv run pytest tests/test_collect.py -k "empty_day or review_pass" -v`
Expected: FAIL — `KeyError: 'mode'` (collect 가 아직 mode 를 반환하지 않음)

- [ ] **Step 3: Implement the fallback in `collect.py`**

import 줄 수정:

```python
from pipeline import config, gitutil, transcripts, spool, batch, review
```

`discover_doc_files`/`_doc_units` 아래에 복습 단위 헬퍼 추가:

```python
def _review_units(root: Path, cfg: dict) -> list[dict]:
    """notes/ 미복습 표현을 골라 복습 단위 하나로 묶는다. 없으면 빈 리스트."""
    picks = review.select_unreviewed(root, cfg.get("digest_max", 7))
    if not picks:
        return []
    lines = "\n".join(f"- {p['expr']} ({p['link']})" for p in picks)
    return [{"kind": "review", "id": "review", "provenance": "review",
             "text": f"복습 대상 표현:\n{lines}",
             "advance": {"reviewed": [p["expr"] for p in picks]}}]
```

`collect()` 에서 정상 패스 조립 직후(현재 `batch_text, consumed = batch.build_batch(units, char_budget, today)` 줄)부터 매니페스트 생성 직전까지를 다음으로 교체:

```python
    # 예산 내 조립 (정상 패스)
    batch_text, consumed = batch.build_batch(units, char_budget, today)
    mode = "normal"

    # 빈 날 폴백: 정상 패스가 비면 ① 백로그(7일 너머 노화 문서) → ② 복습(notes/ 미복습)
    if not consumed:
        backlog_cfg = {**cfg, "recent_days": cfg.get("backlog_days", DEFAULT_BACKLOG_DAYS)}
        units, unread = _doc_units(base, backlog_cfg, seen, char_budget)
        batch_text, consumed = batch.build_batch(units, char_budget, today)
        mode = "backlog"
        if not consumed:
            units, unread = _review_units(root, cfg), 0
            batch_text, consumed = batch.build_batch(units, char_budget, today)
            mode = "review" if consumed else "empty"

    # 매니페스트(소비 단위만 상태 전진 대상)
    manifest = {"transcripts": {}, "spool": [], "docs": {}, "reviewed": [],
                "mode": mode, "deferred": (len(units) - len(consumed)) + unread}
    for u in consumed:
        adv = u.get("advance")
        if u["kind"] == "transcript":
            manifest["transcripts"][adv["transcript"]] = adv["offset"]
        elif u["kind"] == "spool":
            manifest["spool"].append(adv["note"])
        elif u["kind"] == "doc":
            manifest["docs"][adv["doc_id"]] = adv["doc_key"]
        elif u["kind"] == "review":
            manifest["reviewed"].extend(adv["reviewed"])
```

(주의: 기존 매니페스트 블록 전체를 위 블록으로 대체한다 — `manifest = {...}` 정의와 `for u in consumed:` 루프를 새 버전으로 바꾸는 것.)

`collect()` 반환문에 `mode` 추가:

```python
    return {"item_count": len(consumed), "deferred": manifest["deferred"],
            "batch_path": str(batch_path), "today": today, "mode": mode}
```

- [ ] **Step 4: Run the full collect suite**

Run: `PYTHONPATH=scripts uv run pytest tests/test_collect.py -v`
Expected: PASS (기존 9개 + 신규 4개 = 13개 통과). 기존 빈-날 테스트(`test_same_day_rerun_skips_after_successful_finalize`, `test_new_day_skips_unchanged_doc`)는 notes/index.md 가 없어 review 가 [] → `mode="empty"`, `item_count == 0` 으로 그대로 통과한다.

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/collect.py tests/test_collect.py
git commit -m "feat(collect): empty-day backlog + review fallback with mode"
```

---

### Task 4: `finalize.py` — 복습 ledger 전진

**Files:**
- Modify: `scripts/pipeline/finalize.py` (import + reviewed 전진)
- Test: `tests/test_finalize.py`

**Interfaces:**
- Consumes: 매니페스트의 `"reviewed": list[str]` (Task 3), `review.mark_reviewed` (Task 1).

- [ ] **Step 1: Write the failing test**

`tests/test_finalize.py` 끝에 추가:

```python
from pipeline import review


def test_finalize_advances_reviewed_ledger(tmp_path, monkeypatch):
    # 복습한 표현은 state/reviewed.json 에 today 로 누적된다(성공 시에만).
    root = tmp_path
    (root / "state").mkdir()
    config.save_state({"transcripts": {}, "docs_seen": {}, "last_run": None},
                      root / "state" / "progress.json")
    (root / "state" / "consumed-2026-06-21.json").write_text(json.dumps({
        "transcripts": {}, "spool": [], "docs": {},
        "reviewed": ["backstop", "blast radius"], "mode": "review", "deferred": 0,
    }), encoding="utf-8")
    monkeypatch.setattr(finalize, "_git_commit_push", lambda root, msg: None)

    finalize.finalize(root=root, today="2026-06-21")

    data = review.load_reviewed(root)
    assert data == {"backstop": "2026-06-21", "blast radius": "2026-06-21"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=scripts uv run pytest tests/test_finalize.py::test_finalize_advances_reviewed_ledger -v`
Expected: FAIL — `review.load_reviewed` 가 `{}` 반환(finalize 가 아직 전진시키지 않음)

- [ ] **Step 3: Implement reviewed advancement in `finalize.py`**

import 줄 수정:

```python
from pipeline import config, review
```

`finalize()` 안에서 `state["last_run"] = today` 다음, `config.save_state(...)` 호출 전후로 복습 전진을 추가 (spool 아카이브 루프 앞이 적당):

```python
    # 복습한 표현을 영구 ledger(reviewed.json)에 전진시킨다 — docs_seen 과 동일 규율.
    reviewed = manifest.get("reviewed") or []
    if reviewed:
        review.mark_reviewed(root, reviewed, today)
```

- [ ] **Step 4: Run the finalize suite**

Run: `PYTHONPATH=scripts uv run pytest tests/test_finalize.py -v`
Expected: PASS (기존 3개 + 신규 1개 = 4개)

- [ ] **Step 5: Commit**

```bash
git add scripts/pipeline/finalize.py tests/test_finalize.py
git commit -m "feat(finalize): advance reviewed.json ledger on success"
```

---

### Task 5: `run.py` mode 별 프롬프트 + `prompts/review.md`

**Files:**
- Modify: `scripts/pipeline/run.py` (`run()` 의 empty 분기, `_build_prompt` 의 프롬프트 선택)
- Create: `prompts/review.md`
- Test: `tests/test_run.py`

**Interfaces:**
- Consumes: `collect()` 반환의 `"mode"` (Task 3).

- [ ] **Step 1: Write the failing tests**

`tests/test_run.py` 끝에 추가:

```python
def test_run_empty_mode_skips_llm(tmp_path, monkeypatch):
    calls = {"claude": 0}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 0, "deferred": 0,
                                                  "batch_path": "x", "today": "2026-06-21",
                                                  "mode": "empty"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda *a, **k: calls.__setitem__("claude", 1) or "{}")
    result = runmod.run(root=tmp_path)
    assert calls["claude"] == 0
    assert result["status"] == "empty"


def test_run_uses_review_prompt_for_review_mode(tmp_path, monkeypatch):
    (tmp_path / "state").mkdir()
    (tmp_path / "prompts").mkdir()
    (tmp_path / "prompts" / "process.md").write_text("PROCESS-PROMPT", encoding="utf-8")
    (tmp_path / "prompts" / "review.md").write_text("REVIEW-PROMPT", encoding="utf-8")
    seen = {}
    monkeypatch.setattr(runmod, "collect",
                        lambda root, today=None: {"item_count": 1, "deferred": 0,
                                                  "batch_path": str(tmp_path / "b.md"),
                                                  "today": "2026-06-21", "mode": "review"})
    monkeypatch.setattr(runmod, "_invoke_claude",
                        lambda prompt, root: seen.update(prompt=prompt) or json.dumps(
                            {"usage": {"input_tokens": 1, "output_tokens": 1,
                                       "cache_read_input_tokens": 0}, "total_cost_usd": 0.0}))
    monkeypatch.setattr(runmod, "finalize", lambda root, today=None: None)
    runmod.run(root=tmp_path)
    assert "REVIEW-PROMPT" in seen["prompt"]
    assert "PROCESS-PROMPT" not in seen["prompt"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `PYTHONPATH=scripts uv run pytest tests/test_run.py -k "empty_mode or review_prompt" -v`
Expected: FAIL — review 모드에서도 `process.md` 가 선택되어 `REVIEW-PROMPT` 가 프롬프트에 없음

- [ ] **Step 3: Update `run.py`**

`run()` 의 종료 분기를 mode 기준으로 바꾼다. 기존:

```python
    if info["item_count"] == 0:
        print(f"[{today}] 처리할 새 항목 없음. 종료.")
        return {"status": "empty", "today": today}
```

를 다음으로 교체:

```python
    if info.get("mode") == "empty" or info["item_count"] == 0:
        print(f"[{today}] 처리할 새 항목 없음. 종료.")
        return {"status": "empty", "today": today}
```

`_build_prompt` 에서 mode 에 따라 베이스 프롬프트 파일을 고른다. 기존:

```python
def _build_prompt(root: Path, info: dict) -> str:
    process_md = root / "prompts" / "process.md"
    base = process_md.read_text(encoding="utf-8") if process_md.exists() else ""
```

를 다음으로 교체:

```python
def _build_prompt(root: Path, info: dict) -> str:
    fname = "review.md" if info.get("mode") == "review" else "process.md"
    prompt_md = root / "prompts" / fname
    base = prompt_md.read_text(encoding="utf-8") if prompt_md.exists() else ""
```

- [ ] **Step 4: Create `prompts/review.md`**

```markdown
# 복습 가공 지침 (review 모드)

너는 영어 학습 파이프라인의 **복습** 단계다. 새 입력이 없는 날, 이미 모아 둔
표현을 다시 꺼내 정착시키는 것이 목표다. 파일 도구(Read/Edit/Write/Glob)만 쓴다.

## 입력
배치 파일에는 `복습 대상 표현:` 아래에 표현 목록과 각 표현이 처음 수집된
daily 링크가 들어 있다. 필요하면 그 링크의 `new-expressions.md` 를 읽어 원래
맥락을 참고하라.

## 출력
`daily/<날짜>/review.md` 를 만들고, 각 표현마다 다음을 담는다:
- 한국어 뜻과 뉘앙스 한 줄
- 새 예문 1–2개 (처음 수집 때와 다른 맥락)
- 짧은 사용 퀴즈 1개 (빈칸 채우기 또는 한→영)
- 응용 한 줄 (실제로 쓸 법한 상황)

이어서 `daily/<날짜>/digest.md` 를 복습본으로 작성한다: 오늘 복습한 표현을
한눈에 보이게 묶고, 가장 헷갈리기 쉬운 2–3개를 골라 강조한다.

## 원칙
- 새 표현을 발명하지 말 것 — 배치에 주어진 표현만 다룬다.
- 예문은 자연스러운 실제 영어로. 억지 문장 금지.
- 코칭 톤은 `prompts/process.md` 의 규약을 따른다.
```

- [ ] **Step 5: Run the run suite**

Run: `PYTHONPATH=scripts uv run pytest tests/test_run.py -v`
Expected: PASS (기존 3개 + 신규 2개 = 5개)

- [ ] **Step 6: Commit**

```bash
git add scripts/pipeline/run.py prompts/review.md tests/test_run.py
git commit -m "feat(run): select review prompt by mode; add prompts/review.md"
```

---

### Task 6: 전체 회귀 + 문서 동기화

**Files:**
- Modify: `CLAUDE.md` (흐름 설명에 빈 날 폴백 한 줄 추가)

- [ ] **Step 1: Run the whole suite**

Run: `PYTHONPATH=scripts uv run pytest -q`
Expected: PASS (기존 32개 + 신규 13개 전부 통과; 실패 0)

- [ ] **Step 2: Update `CLAUDE.md` 흐름 설명**

`## 흐름` 의 1번 `collect` 항목 끝(상태 추적 문단 뒤)에 한 줄 추가:

```markdown
   - **빈 날 폴백**: 새 항목이 0개면 ① `backlog_days`(기본 14일) 윈도로 7일 너머
     미처리 문서를 따라잡고, 그래도 없으면 ② `notes/` 누적 표현 중 아직 복습 안 한
     것을 골라 복습본을 생성한다(`state/reviewed.json` 추적). 둘 다 없으면 중단한다.
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: note empty-day backlog/review fallback in CLAUDE.md"
```

---

## Self-Review

**Spec coverage:**
- 빈 날 트리거(정상 0 → 폴백) → Task 3 ✓
- ① 백로그(backlog_days, ledger 제외, doc kind 재사용) → Task 2(config·헬퍼) + Task 3(패스) ✓
- ② 복습(notes/index.md 파싱, reviewed.json, 소진 후 중단, 자가 재개) → Task 1 + Task 3 ✓
- finalize 복습 전진(성공 시에만) → Task 4 ✓
- run.py mode 별 프롬프트 + prompts/review.md → Task 5 ✓
- config backlog_days, digest_max 재사용 → Task 2 ✓
- 테스트(test_review/collect/finalize/run) → 각 태스크 ✓
- 정상 흐름 무변경 → Task 2 회귀 + Task 3 Step 4 주석 ✓

**Placeholder scan:** 모든 코드 스텝에 실제 코드/명령/기대 출력 포함. 플레이스홀더 없음.

**Type consistency:** `select_unreviewed(root, n)`, `mark_reviewed(root, exprs, today)`, `parse_index → {expr,date,link}`, manifest `reviewed: list[str]`, `collect() → {... "mode"}` 가 Task 1·3·4·5 에서 일관되게 사용됨. `_doc_units(base, cfg, seen, char_budget) → (units, unread)` 가 Task 2 정의와 Task 3 호출에서 일치.
