# 빈 날 2단계 폴백: backlog → review → stop

날짜: 2026-06-20
상태: 설계 승인 대기

## 문제

평소 `collect` 가 새 항목 0개를 모으면 `run.py` 는 `claude -p` 를 호출하지 않고
`status="empty"` 로 즉시 종료한다 (`run.py:24-26`). 그 결과:

1. **진짜 빈 날엔 아무 산출물도 없다** — 그날 `daily/<날짜>/digest.md` 가 생기지 않아
   아침 읽기 흐름이 끊긴다.
2. **최근이지만 미처리된 콘텐츠가 유실된다.** 수집 세 소스(spool·docs·transcripts)가
   전부 증분이고, 문서는 `recent_days`(7일) 윈도에 갇혀 있다. 예산(`char_budget`)에
   계속 밀린 문서는 7일이 지나는 순간 윈도 밖으로 떨어져 **영영 학습되지 못한다.**
   실측: `state/consumed-2026-06-20.json` 의 `deferred: 1339` — 큰 백로그가 실재한다.

핵심 통찰: **진짜 "빈 날" = 7일 윈도가 바닥난 날**이다 (윈도 안에 밀린 문서가 있으면
예산이 비는 빈 날에 그게 소비되어 `item_count > 0` 이 된다). 따라서 빈 날은
(a) 7일보다 과거로 손을 뻗어 노화된 미처리 문서를 따라잡고, (b) 그래도 없으면
누적 표현으로 복습을 생성하기에 가장 좋은 날이다.

## 목표

빈 날에 두 단계 폴백을 순서대로 시도한다:

1. **① 백로그 따라잡기** — 7일을 넘겨(`backlog_days`=14) ledger(`docs_seen`)에 없는,
   즉 한 번도 처리 못 하고 노화된 문서를 집어와 **정상 문서로** 처리한다.
2. **② 복습(생성형)** — 백로그도 비면, `notes/` 누적 표현 중 아직 복습 안 된 것으로
   새 예문·퀴즈·응용을 생성한다. 전부 한 바퀴 돌면(소진) 중단한다.
3. 둘 다 비면 `status="empty"` 로 중단한다 (억지 콘텐츠를 만들지 않는다).

새 표현이 나중에 정상 실행으로 `notes/index.md` 에 쌓이면, 복습 ledger 에 없으므로
복습이 자연히 재개된다 (자가 충전).

## 비목표 (YAGNI)

- 간격 반복(spaced repetition) 알고리즘 — 미복습 표현을 수집일 오래된 순으로 한 번씩만 돈다.
- 복습 표현 난이도/약점 가중치.
- 백로그 전용 별도 예산 — 기존 `char_budget` 을 공유해 여러 빈 날에 걸쳐 소진한다.

## 흐름

```
collect():
  normal pass (현행)
    └ 소비분 ≥ 1 → mode="normal"
    └ 0개 → ① backlog pass (docs, backlog_days 윈도, ledger 제외)
              └ 소비분 ≥ 1 → mode="backlog"
              └ 0개 → ② review pass (notes/index.md 중 미복습, 최대 digest_max)
                        └ 소비분 ≥ 1 → mode="review"
                        └ 0개 → mode="empty"

run():
  mode=="empty" → 지금처럼 종료 (claude 호출 안 함)
  그 외 → 프롬프트 선택 후 claude -p → finalize
```

## 컴포넌트

### 1. `pipeline/review.py` (신규)

단일 책임: 복습 소재 관리. 단독 테스트 가능.

- `parse_index(root) -> list[dict]` — `notes/index.md` 를 파싱해
  `[{"expr": <표현 텍스트>, "date": <수집일>, "link": <daily 링크>}, ...]` 반환.
  형식: `- [표현](daily/.../new-expressions.md) — YYYY-MM-DD`.
  index.md 가 없으면 `[]`.
- `load_reviewed(root) -> dict` — `state/reviewed.json` (표현→복습일) 로드, 없으면 `{}`.
- `select_unreviewed(root, n) -> list[dict]` — reviewed 에 없는 표현을
  **수집일 오래된 순**으로 최대 `n`개 반환. 동률은 index.md 등장 순.

`state/reviewed.json` 형태: `{ "<표현 텍스트>": "<복습일 YYYY-MM-DD>", ... }`.

### 2. `pipeline/collect.py` (수정)

`collect()` 끝부분, 정상 패스의 `consumed` 가 비었을 때만 폴백 진입. 반환 dict 에
`mode` 필드 추가 (`"normal"|"backlog"|"review"|"empty"`).

- **백로그 패스**: `discover_doc_files(base, cfg)` 를 `recent_days` 대신
  `backlog_days` 로 호출(임시 cfg override)하고 `docs_seen` 에 있는 것을 제외.
  결과 단위는 **기존 `doc` kind 그대로** (`provenance="repo:..."`,
  `advance={doc_id, doc_key}`). `build_batch` 로 예산 내 조립.
  → manifest 의 `docs` 에 들어가 finalize 의 ledger 승격이 **무변경**으로 동작.
- **복습 패스**: `review.select_unreviewed(root, cfg.get("digest_max", 7))`.
  선택된 표현들을 `kind="review"` 단위 하나로 묶는다:
  `provenance="review"`, `text` = 표현 목록(각 표현 + daily 링크),
  `advance={"reviewed": [표현 텍스트들]}`.
  manifest 에 새 키 `reviewed: [...]` 기록.
- 백로그/복습 패스의 `deferred` 계산은 정상 패스와 동일 규칙(소비 못 한 단위 수).

manifest 스키마 확장:
```json
{ "transcripts": {...}, "spool": [...], "docs": {...},
  "reviewed": [...], "mode": "review", "deferred": N }
```

### 3. `pipeline/finalize.py` (수정)

manifest 의 `reviewed`(리스트)를 `state/reviewed.json` 에 합친다 — `docs_seen` 과
동일하게 **성공(=finalize) 시에만** 전진. 각 표현을 `today` 로 표시.

### 4. `pipeline/run.py` (수정)

`collect()` 의 `mode` 를 받아:
- `mode=="empty"` → 현행 `status="empty"` 종료.
- `mode in {"normal","backlog"}` → 기존 `process.md` 프롬프트 (백로그는 그냥 문서).
- `mode=="review"` → 신규 `prompts/review.md` 프롬프트.
`_build_prompt` 가 mode 에 따라 베이스 프롬프트 파일을 고르고, 배치 경로·날짜·
출력 접두사를 동일하게 덧붙인다. 반환 dict 의 `status` 값에 `mode` 를 함께 노출.

### 5. `prompts/review.md` (신규)

복습 모드 지침: 배치에 실린 각 표현에 대해 **새 예문 1–2개·짧은 사용 퀴즈·
한국어 뜻/뉘앙스·응용 한 줄**을 생성하여 `daily/<날짜>/review.md` 에 쓰고,
오늘자 `daily/<날짜>/digest.md` 를 복습 버전으로 작성한다. 파일 도구만 사용
(무인 실행 제약과 동일). `process.md` 의 코칭 톤·출력 규약을 따른다.

### 6. `config/sources.json` (수정)

`"backlog_days": 14` 한 줄 추가. 복습 개수는 기존 `digest_max`(7) 재사용.

## 데이터 흐름 / 상태 전진

- **백로그 문서**: 소비분 → manifest `docs` → finalize 가 `docs_seen` 승격.
  미소비분은 ledger 에 안 들어가 다음 빈 날에 재발견(14일 윈도 안인 동안).
- **복습 표현**: 소비분 → manifest `reviewed` → finalize 가 `reviewed.json` 전진.
  LLM 실패 시 finalize 안 됨 → 같은 표현 다음 실행에서 재시도.

## 엣지 케이스

- `notes/index.md` 부재/빈 파일 → 복습 패스 0개 → empty.
- 모든 표현 복습 완료(소진) → 복습 패스 0개 → empty (의도된 중단).
- 14일 넘긴 미처리 문서 → 백로그 윈도 밖 → 영구 포기 (의도된 경계).
- 정상 실행이 새 표현 추가 → reviewed.json 에 없음 → 다음 빈 날 복습 재개.
- 백로그 패스가 예산 초과 → 일부만 소비, 나머지 deferred → 다음 빈 날 이어서.

## 테스트 (TDD)

- **신규 `test_review.py`**: `parse_index`(정상/빈/없음), `select_unreviewed`
  (미복습 선정·수집일 정렬·n 제한), 소진 후 0개, 새 표현 추가 시 재개.
- **`test_collect.py` 확장**: 정상 0 → 백로그 패스 발동(노화 문서 수집),
  백로그 0 → 복습 패스 발동, 둘 다 0 → `mode="empty"`. 백로그 문서가
  `doc` kind 로 manifest `docs` 에 들어가는지.
- **`test_finalize.py` 확장**: manifest `reviewed` → `reviewed.json` 전진,
  성공 시에만 승격.
- **`test_run.py` 확장**: `mode` 별 프롬프트 선택, `mode="empty"` 시 claude 미호출.

## 영향 범위

신규: `pipeline/review.py`, `prompts/review.md`, `tests/test_review.py`,
`state/reviewed.json`(런타임 생성). 수정: `collect.py`, `finalize.py`, `run.py`,
`config/sources.json`, `tests/test_collect.py`, `tests/test_finalize.py`,
`tests/test_run.py`. 기존 정상 흐름은 무변경 (정상 패스가 비었을 때만 폴백 진입).
