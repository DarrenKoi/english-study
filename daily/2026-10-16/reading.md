# 2026-10-16 — 정독

## 단락 1

These findings are from the diff alone and were not verified against the full files. The cap is `len(_IN_FLIGHT)`, which counts dict entries rather than live threads. The adjacent `is_alive()` check implies finished threads stay in the dict, so unless they are pruned before this line, after 4 distinct recipes every later consensus gather is skipped for the life of the process (silent permanent rcp fallback). When the 64-slot limit is hit, `_send_cube_async` returns False, but `CycleNotifier` has already set `_outcome_sent`. The outcome cube for that alarm is dropped with no retry, including the `corrected_unverified` and escalation outcomes that must reach the engineer. `_close_tool` now raises on `close_failed`. If the teardown runner does not isolate each step, the following `_close_alert` and popup backstop are skipped, leaving the alert window open.

**문법·구조**: 첫 문장이 전체의 신뢰 수준을 정한다. `were not verified` 는 과거 수동태로 "검증이라는 행위가 없었다"를 행위자 없이 밝힌다. 그 뒤 버그 설명은 전부 현재형이다. 코드가 지금 그렇게 동작한다는 사실 진술이라 `will` 을 쓰지 않는다. 셋째 문장은 `implies … , so unless … , after … , every later … is skipped` 로 추론 → 조건 → 시점 → 결과가 한 호흡에 이어진다. 길지만 쉼표마다 한 단계씩이라 따라 읽힌다. `returns False, but … has already set` 은 현재완료로 "돌려줄 때는 이미 늦었다"는 순서를 만든다. `including …` 은 앞 명사를 넓혀 피해 범위를 키우고, 마지막 `leaving the alert window open` 은 결과 분사구로 귀결만 꼬리에 단다.

**핵심 표현**:
- `counts dict entries rather than live threads` — "틀렸다" 대신 실제와 기대를 나란히 놓는다.
- `for the life of the process` — 영향 기간을 재시작 전까지로 정확히 묶는다.
- `It is only safe if …` (같은 리뷰의 둘째 항목) — 전체 파일을 안 본 리뷰어의 정직한 유보.

**격식 짝**:
- refined (작성): Unless completed threads are pruned beforehand, the limit is reached after four recipes and remains in effect until the process restarts.
- plain (작성): If nothing cleans out the finished threads, the cap fills up after four recipes and never frees up.
- refined (작성): The notification is discarded without a second attempt.
- plain (작성): That message just gets lost — nobody retries it.

<sub>출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과, 목록 항목을 이어 붙이고 일부 생략)</sub>

---

## 단락 2

Your angle: REUSE ONLY. Flag new code in the diff that re-implements something the codebase already has. For each candidate, grep the shared modules and name the exact existing helper (file:line) to call instead. Typical suspects: mean/σ/median/quantile/linear-regression/pearson math, number formatting, date/KST formatting, xlsx sheet building. Not in scope: correctness bugs, style nits, test files' internal duplication, docs. Do not propose changes that alter intended behaviour or visible strings. Verify every finding by reading both the new code and the existing helper — confirm the semantics really match (e.g. sample vs population σ, null handling). Drop anything you cannot confirm.

**문법·구조**: 명령문과 콜론 머리말이 번갈아 나오는 지시문이다. `Your angle:`, `Typical suspects:`, `Not in scope:` 는 동사 없이 콜론 뒤에 내용을 바로 둔다. 표처럼 훑기 좋다. 나머지는 모두 원형 동사로 시작하는 명령문(`Flag`, `grep`, `name`, `Verify`, `Drop`)이라 주어 `you` 가 생략돼 있다. `that re-implements …` 는 `new code` 를 꾸미는 관계절이고, 그 안의 `something the codebase already has` 는 `that` 을 뺀 접촉절이다. `name … to call instead` 의 `to call` 은 형용사적 to부정사로 "대신 호출할 (헬퍼)". 대시 뒤 `confirm …` 은 앞 `Verify` 를 구체화하는 재진술이다. 마지막 `Drop anything you cannot confirm.` 이 짧게 끊어서 기준을 못 박는다.

**핵심 표현**:
- `Not in scope:` — 할 일보다 하지 말 일을 먼저 적어 범위를 자른다.
- `confirm the semantics really match` — 이름이 같아도 동작이 같은지를 따진다.
- `Drop anything you cannot confirm.` — 짐작을 보고에서 걸러 내는 다섯 단어.

**격식 짝**:
- refined (작성): Exclude any finding that cannot be substantiated.
- plain (작성): If you can't back it up, leave it out.

<sub>출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문, 경로 목록 일부 생략)</sub>

---

## 단락 3

Some users could not find a device on the Device Statistics page even though its data was intact. The cause was not the data but a filter: category, lot, and tech selections are saved in the browser and keep applying across sessions. A badge now reads "Saved filters applied" whenever such a filter is narrowing the list, so a missing device can be traced to its filter at a glance. Devices that have no plan-step records at all are now labelled "No source step data" instead of being shown as an empty table, which makes it clear the gap lies in the source rather than in our pipeline. A device that remains in your selection but no longer exists in the catalog is flagged separately as a stale selection. We also fixed an issue in which some R-fab devices lost their category, causing the rule check to treat their memory type as unknown.

**문법·구조**: 공지문은 사용자 입장에서 증상 → 원인 → 조치 순으로 간다. 첫 두 문장은 과거형(`could not find`, `was`)으로 겪은 일을, 셋째부터는 `now` + 현재형으로 바뀐 상태를 말한다. `The cause was not the data but a filter` 는 `not A but B` 로 오해를 먼저 걷어 낸다. `are now labelled … instead of being shown as …` 는 수동태끼리 짝을 맞춰 "전과 후"를 대비하고, `which makes it clear …` 는 앞 절 전체를 받는 계속적 관계절이다. 마지막 문장의 `causing …` 은 단락 1의 `leaving …` 과 같은 결과 분사구다.

**핵심 표현**:
- `keep applying across sessions` — "세션 넘어 지속"을 동사로 옮긴 꼴.
- `the gap lies in the source rather than in our pipeline` — 원인 위치를 `lie in` 으로 가른다.
- `is flagged separately as a stale selection` — "오래된 선택"을 따로 표시한다.

**격식 짝**:
- refined (작성): The absence of step data originates in the source system, not in our processing pipeline.
- plain (작성): If you see "no step data", it's missing upstream — it's not our bug.

<sub>출처: 모범 단락(작성) — 2026-10-13 공지사항(디바이스 통계 수정 5건)을 영어 공지로 옮겨 씀</sub>
