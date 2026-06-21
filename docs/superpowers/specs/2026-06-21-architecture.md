# english-study — 아키텍처 / 데이터 파이프라인 문서

- 작성일: 2026-06-21
- 상태: 현행 코드 기준 (as-built)
- 대상: `~/Codes/english-study`
- 짝 문서: [`2026-06-21-architecture.html`](2026-06-21-architecture.html) (다이어그램 포함 시각본)

> 이 문서는 *지금 동작하는* 코드의 구조와 로직을 정리한 것이다. 설계 의도/결정 배경은
> [`2026-06-14-english-study-design.md`](2026-06-14-english-study-design.md), 부분 기능의 설계는
> [`2026-06-19-coaching-cards-design.md`](2026-06-19-coaching-cards-design.md),
> [`2026-06-20-empty-day-fallback-design.md`](2026-06-20-empty-day-fallback-design.md) 참고.

---

## 1. 한눈에 보기

매일 밤 `~/Codes` 전 프로젝트와 Claude Code 대화 로그에서 영어를 자동 수집해, 그날의
**학습 다이제스트**(`daily/`)와 누적 **표현 노트**(`notes/`)로 가공하고 git push 한다.

```
launchd (00:01)
   │
   ▼
scripts/run.sh ──► uv run python -m pipeline.run
                          │
   ┌──────────────────────┼──────────────────────────┐
   ▼                      ▼                           ▼
 collect()           claude -p                    finalize()
 (Python)         (process.md / review.md)         (Python)
 수집·예산·중복필터    추출·분류·코칭                 상태전진·아카이브·prune·push
```

핵심 설계 원칙 — **역할 분리**:

| 책임 | 담당 |
|---|---|
| 파일 수집 · 증분(중복) 필터 · 토큰 예산 · 상태 전진 · git push | **Python 코드** (`pipeline/*`) |
| 영어 표현 추출 · 레지스터 분류 · 코칭 · 정독 단락 작성 | **`claude -p`** (LLM, 파일 도구만) |

LLM 은 `Read,Edit,Write,Glob` 만 허용된다. 배치에 섞일 수 있는 프롬프트 인젝션이
Bash·네트워크로 번지는 것을 막는 방어선이다. git push 는 LLM 이 아니라 `finalize` 의
Python 이 수행한다.

---

## 2. 디렉터리 구조

```
english-study/
├─ config/
│  └─ sources.json          # 수집 소스·예산·보존 기간 등 모든 설정
├─ scripts/
│  ├─ run.sh                # launchd 진입점 (PATH 설정 → uv run)
│  ├─ com.daeyoung.english-study.plist  # launchd 잡 (매일 00:01)
│  └─ pipeline/             # 파이썬 패키지 (PYTHONPATH=scripts)
│     ├─ run.py             # 오케스트레이터: collect → claude -p → finalize
│     ├─ collect.py         # 소스 수집 + 예산 조립 + 빈 날 폴백
│     ├─ batch.py           # 단위 목록 → 예산 내 배치 텍스트 조립
│     ├─ spool.py           # 사용자 직접 노트 수집
│     ├─ transcripts.py     # Claude Code 대화 로그 증분 파싱
│     ├─ gitutil.py         # 소스 repo git pull (베스트에포트)
│     ├─ review.py          # 복습 큐 / notes index 파싱·정리
│     ├─ finalize.py        # 상태 전진·아카이브·prune·commit&push
│     ├─ tokenlog.py        # 토큰/비용 사용량 기록
│     └─ config.py          # config/state 로더, 경로 헬퍼
├─ prompts/
│  ├─ process.md            # 정상 가공 지침 (LLM)
│  └─ review.md             # 복습 모드 가공 지침 (LLM)
├─ spool/                   # 사용자가 직접 적는 학습 질문 (.txt/.md)
│  └─ done/                 # 처리된 노트 아카이브 (날짜 접두)
├─ state/                   # 모든 런타임 상태 (대부분 .gitignore)
│  ├─ progress.json         # 영구 원장: transcripts offset, docs_seen
│  ├─ reviewed.json         # 복습 완료 표현 원장
│  ├─ batch-<날짜>.md       # 그날 수집된 배치 (LLM 입력)
│  ├─ consumed-<날짜>.json  # 그날 소비된 단위 매니페스트 (collect→finalize 핸드오프)
│  └─ token-log.jsonl       # 일자별 토큰/비용 추이
├─ daily/<날짜>/            # 일일 산출물 (process/review 가 씀, 20일 보존)
└─ notes/                   # 누적 표현 아카이브 (영구)
   ├─ by-register/*.md      # 레지스터별 표현 정본 (한글 설명 + 예문)
   └─ index.md              # 표현 → daily 링크 인덱스 (= 복습 큐)
```

---

## 3. 데이터 파이프라인 (3 단계)

### 단계 0 — 진입 (`run.sh` → `run.py`)

`run.sh` 는 launchd 의 최소 env 에서 호출되므로 `PATH` 와 `PYTHONPATH` 를 명시한 뒤
`uv run python -m pipeline.run` 을 실행한다 (`uv` 가 Python·venv·의존성 자동 관리).
먼저 자기 repo 를 `git pull --ff-only` 한다.

`run.run()` 의 흐름 (`scripts/pipeline/run.py`):

```
info = collect(root)
  └─ 새 항목 0개 또는 mode == "empty"  →  종료 (상태 전진 없음)
prompt = _build_prompt(root, info)        # mode 에 따라 process.md / review.md 선택
out = _invoke_claude(prompt, root)        # claude -p --allowedTools Read,Edit,Write,Glob
  └─ 출력 비었으면(LLM 실패)  →  종료 (상태 전진 없음 → 다음 실행 재시도)
tokenlog.append_token_log(...)            # 토큰/비용 기록
finalize(root, today)                     # 상태 전진 + push
```

**중요한 안전 속성**: `collect` 가 비거나 LLM 호출이 실패하면 `finalize` 를 *호출하지
않는다*. 상태 원장은 `finalize` 안에서만 전진하므로, 실패한 입력은 다음 실행에서
그대로 재시도된다.

### 단계 1 — `collect()` : 수집 · 예산 · 중복 필터

`collect.py` 는 4 종류의 입력을 **단위(unit)** 리스트로 만든다. 각 단위는:

```python
{"kind": "spool|doc|transcript|review",
 "id": ...,
 "provenance": "spool:... | repo:<project> <relpath> | transcript:... | review",
 "text": <원문>,
 "advance": {...}}   # finalize 가 이 단위 소비를 어떻게 기록할지
```

수집 우선순위와 출처:

1. **spool 노트** (최우선) — `spool/*.{md,txt}` (README 제외). 사용자가 직접 적은 학습
   질문. → `spool.pending_notes()`
2. **문서 폴더** — `~/Codes` 의 각 프로젝트(`exclude_projects` 제외)를 먼저 `git pull`
   한 뒤, 깊이 무관하게 `doc`/`docs`/`shared_docs` 폴더를 찾아 그 안의 `.md`/`.txt` 중
   **최근 `recent_days`(7일) 안에 수정된** 파일만 최신순으로. `node_modules`·hidden·빌드
   산출물은 가지치기. → `discover_doc_files()` → `_doc_units()`
3. **트랜스크립트** — `~/.claude/projects/**/*.jsonl` 에서 저장된 오프셋 이후의 새
   메시지만 (파일당 단위 1개). → `transcripts.new_messages()`

수집된 단위는 `batch.build_batch()` 로 `char_budget`(200k 자) 안에서 배치 텍스트로
조립된다. 예산을 넘으면 단위를 건너뛰되 **최소 한 단위는 무조건 포함**한다.

#### 증분(중복 제거) 로직 — 두 개의 원장

상태 추적 없이 매 실행 다시 훑되, 두 원장으로 "이미 처리한 것"을 거른다:

| 입력 | 원장 (state) | 동일성 키 | 키가 바뀌는 조건 |
|---|---|---|---|
| 문서 | `progress.json` → `docs_seen` (경로→키) | `project/relpath:mtime:size` | 파일을 고치면(mtime/크기 변동) → 재수집 |
| 트랜스크립트 | `progress.json` → `transcripts` (파일→오프셋) | 줄 오프셋 | 새 줄이 추가되면 → 그 줄부터 수집 |

`_doc_key()` 는 **stat 만으로 동일성을 판정**한다(`mtime`+`size`). 변경 없는 파일은
내용을 읽지도 않는다. 원장은 `finalize` 가 성공해야 전진하므로, LLM 이 실패한 뒤의
재실행은 같은 문서를 다시 집어 든다.

#### 빈 날 폴백 (2 단계)

정상 패스(`mode="normal"`)에서 소비 단위가 0개면:

```
① backlog (mode="backlog")
   recent_days 를 backlog_days(14일)로 넓혀 7일 너머 미처리 문서를 따라잡는다.
        │ 그래도 0개면
        ▼
② review (mode="review")
   notes/index.md 의 아직 복습 안 한 표현(state/reviewed.json 추적)을
   수집일 오래된 순으로 골라 "복습 단위" 하나로 묶는다.
        │ 그래도 0개면
        ▼
   mode="empty"  →  run.py 가 즉시 종료
```

`mode` 는 `run._build_prompt()` 가 어떤 프롬프트를 쓸지 결정한다:
`review` 면 `prompts/review.md`, 그 외엔 `prompts/process.md`.

#### 매니페스트 출력

`collect` 의 마지막 산출물은 두 파일이다:

- `state/batch-<날짜>.md` — LLM 입력 (provenance 헤더로 구분된 원문 묶음)
- `state/consumed-<날짜>.json` — **소비된 단위만** 기록한 매니페스트. `transcripts`(파일→오프셋),
  `spool`(경로 목록), `docs`(경로→키), `reviewed`(표현 목록), `mode`, `deferred`(밀린 수)를 담는다.
  이것이 `collect → finalize` 사이의 유일한 핸드오프다.

### 단계 2 — `claude -p` : LLM 가공

`run._invoke_claude()` 가 `claude -p <prompt> --output-format json --allowedTools
Read,Edit,Write,Glob` 를 `root` 에서 실행한다. 프롬프트는 `prompts/process.md`(또는
`review.md`) 본문 + 배치 경로/날짜/출력 접두사를 덧붙인 것이다.

LLM 의 작업 (`process.md` 요약):

1. **표현 추출** — 학습 가치 있는 문장/숙어를 고르고 보일러플레이트는 버림
2. **레지스터 분류** — professional / conversational / casual / technical
3. **맥락 설명** — 언제·어느 격식에서 쓰는지 한 줄
4. **정독 단락** — 잘 쓰인 5~10문장 단락을 인용·문법 해설 (없으면 모범 단락 작성)
5. **격식 짝** — refined(문어) ↔ plain(회화) 대비
6. **유사어·반의어** — 뉘앙스/격식 차이와 함께
7. **한글→영어 코칭** — (a) 내가 쓴 한국어(`[user]`+`spool:`) 우선, (b) 어시스턴트
   고급 한국어 번역 보조 (하루 2~4문장)

산출물:
- `daily/<날짜>/` — `new-expressions.md`, `reading.md`, `coaching.md`, `digest.md` 와
  spool 답변 `spool/<이름>.md` 등 (그날 분량; 코칭은 한국어 입력이 있는 날만)
- `notes/by-register/*.md` — 레지스터별 표현 정본에 누적 추가
- `notes/index.md` — 표현 → daily 링크 한 줄씩 추가 (복습 큐)

`review.md`(복습 모드)는 새 표현을 발명하지 않고, `notes/by-register/*` 에서 원래
맥락을 grep 해 `daily/<날짜>/review.md` + `digest.md` 복습본을 만든다.

### 단계 3 — `finalize()` : 상태 전진 · 아카이브 · 정리 · push

`finalize.py` 는 `consumed-<날짜>.json` 매니페스트를 읽어, **소비한 만큼만** 상태를
전진시킨다:

1. **원장 전진** — `progress.json` 의 `transcripts`(오프셋)·`docs_seen`(문서 키) 갱신,
   `last_run` 기록. → 이제부터 그 문서/대화는 안 바뀌는 한 다시 안 집힘.
2. **복습 전진** — 소비된 `reviewed` 표현을 `state/reviewed.json`(표현→복습일)에 누적.
3. **spool 아카이브** — 처리된 노트를 `spool/done/<날짜>-<이름>` 으로 이동(멱등성:
   같은 날 같은 이름이면 `-2,-3…` 접미).
4. **오래된 daily prune** — `prune_old_daily()` 가 `today` 기준 `daily_retention_days`
   (20일)보다 오래된 `daily/<YYYY-MM-DD>/` 폴더를 삭제. 경계(정확히 N일 전)는 보존,
   날짜로 못 읽는 폴더는 안 건드림.
5. **죽은 인덱스 링크 정리** — `prune_dead_index_links()` 가 `notes/index.md` 에서
   링크 대상이 사라졌고(prune됨) **이미 복습한** 표현 줄만 삭제. 미복습 표현은 죽은
   링크여도 **보존**한다 — index 가 복습 큐라, 지우면 복습 대상에서 영영 빠지기 때문
   (맥락 정본은 `notes/by-register` 에 있으므로 링크가 죽어도 복습 가능).
6. **commit & push** — `git add -A && commit -m "study: nightly digest <날짜>" && push`.

`finalize` 가 6 번까지 끝나야 한 실행이 "완료"된다. 그 전에 죽으면 원장이 전진하지
않았으므로 다음 실행이 재시도한다.

---

## 4. 상태 파일 모델

| 파일 | 쓰는 주체 | 역할 | 수명 |
|---|---|---|---|
| `state/progress.json` | finalize | 영구 원장: `transcripts`(파일→오프셋), `docs_seen`(경로→키), `last_run` | 영구 |
| `state/reviewed.json` | finalize (review) | 복습 완료 표현 → 날짜 | 영구 |
| `state/batch-<날짜>.md` | collect | 그날 LLM 입력 | 1회용 |
| `state/consumed-<날짜>.json` | collect | collect→finalize 핸드오프 매니페스트 | 1회용 |
| `state/token-log.jsonl` | run (tokenlog) | 일자별 input/output/cache/cost/items | 누적 append |
| `notes/index.md` | LLM (process) | 표현→daily 링크 = 복습 큐 | 영구 (정리만) |
| `notes/by-register/*.md` | LLM (process) | 표현 정본(한글 설명+예문) | 영구 |
| `daily/<날짜>/*` | LLM | 일일 산출물 | 20일 |

`config.DEFAULT_STATE = {"transcripts": {}, "docs_seen": {}, "last_run": None}` — 상태
파일이 없으면 이 기본값으로 시작하고, 로드 시 기본값 위에 저장된 값을 병합한다.

---

## 5. 설정 (`config/sources.json`)

```json
{
  "base_path": "~/Codes",                 // 문서 소스 루트
  "transcripts_dir": "~/.claude/projects",// 대화 로그 루트
  "char_budget": 200000,                  // 배치 1회 문자 예산
  "digest_min": 5, "digest_max": 7,       // 다이제스트/복습 표현 개수
  "doc_dirs": ["doc", "docs", "shared_docs"],
  "doc_exts": [".md", ".txt"],
  "recent_days": 7,                       // 정상 패스 mtime 윈도
  "backlog_days": 14,                     // 빈 날 ① 백로그 윈도
  "daily_retention_days": 20,             // daily/ 보존 기간
  "exclude_projects": ["english-study"]   // 자기 자신 제외
}
```

모든 동작 파라미터가 이 한 파일에 모여 있다. 코드는 `cfg.get(key, DEFAULT)` 로 읽어
키가 없어도 기본값으로 동작한다.

---

## 6. 실행 모드

| 모드 | 트리거 | 가공 주체 | 웹 검색 | 안전 |
|---|---|---|---|---|
| **야간 무인** | launchd 00:01 | `claude -p` (파일 도구만, 네트워크 차단) | ✗ | 인젝션 격리 |
| **대화형** | Claude Code 세션 `/study [토픽]` | 대화형 LLM | ✓ (고품질 원문 추가) | 감독 하 |
| **순수 수동** | `PYTHONPATH=scripts uv run python -m pipeline.run` | `claude -p` | ✗ | — |

대화형 모드는 같은 collect/finalize 골격을 쓰되 가운데 가공만 대화형 LLM 이 맡고,
감독 하에 실행되므로 웹 검색으로 정독 자료를 추가할 수 있다.

---

## 7. 직접 쓰는 법 (사용자 워크플로)

1. 궁금한 것을 `spool/` 에 `.txt`/`.md` 로 적어두면 다음 실행이 **최우선**으로 답한다
   (답: `daily/<날짜>/spool/<이름>.md`, 원본: `spool/done/` 보관).
2. 아침에 `daily/<오늘날짜>/digest.md` 를 읽는다.
3. 토큰/비용 추이는 `state/token-log.jsonl`.
4. 누적 표현은 `notes/by-register/*.md`, 복습 큐는 `notes/index.md`.

---

## 8. 테스트

`tests/` 에 단위 테스트(`test_batch`, `test_collect`, `test_config`, `test_finalize`,
`test_gitutil` 등). 실행: `PYTHONPATH=scripts uv run pytest`. (현재 53개 통과)
