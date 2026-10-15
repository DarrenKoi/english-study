# 2026-10-16 — 새 표현

오늘 배치는 문서 8건이 거의 한국어였고, 영어는 두 갈래에서 나왔다. 하나는 auto-recipe-creator 의 diff 리뷰 결과(`/code-review low`)로, 버그를 "어떤 조건에서 무엇이 깨지는가"까지 한 줄에 담는 문장이 많다. 다른 하나는 정리용 하위 에이전트에게 준 "REUSE ONLY" 지시문이다. 범위를 자르고, 확인 못 한 것은 버리라고 명령하는 표현이 모여 있다. ops_store DAG 가이드에서는 한국어 문장 속 영어 기술어 두 개를 골랐다.

## "counts X rather than Y"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 코드 리뷰에서 "세는 대상이 틀렸다"를 짚을 때(문어·리뷰 코멘트)
- 한국어: Y 가 아니라 X 를 센다.
- 설명: 원문은 `the cap is len(_IN_FLIGHT), which counts dict entries rather than live threads`. 버그를 "틀렸다"고 하지 않고 실제로 세는 것과 세야 할 것을 나란히 놓아 독자가 스스로 결론을 내리게 한다. `rather than` 앞에 실제, 뒤에 기대를 둔다.
- 예문: The cap is `len(_IN_FLIGHT)`, which counts dict entries rather than live threads.
- 유사어: measures X instead of Y (중립), is counting the wrong thing (구어, 덜 구체적)
- 반의어: counts exactly what it claims to (의도대로 센다)

## "for the life of the process"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 한번 꼬인 상태가 재시작 전까지 안 풀린다는 영향 범위를 말할 때(문어·기술)
- 한국어: 프로세스가 살아 있는 내내.
- 설명: `life` 를 "수명"으로 써서 기간을 정확히 못 박는다. `forever` 보다 정확하고(재시작하면 풀린다는 뜻이 들어 있다) `for a while` 보다 심각하다. `for the lifetime of the session` 처럼 대상만 바꿔 쓴다.
- 예문: After four distinct recipes, every later consensus gather is skipped for the life of the process.
- 유사어: until the process restarts (구체적, 구어도 가능), for the lifetime of the process (같은 뜻, 조금 더 격식)
- 반의어: only for the current call (이번 호출에 한정)

## "(a) silent permanent fallback"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 오류는 안 나는데 대체 경로로 영영 빠져 버리는 최악의 실패 유형을 이름 붙일 때(기술)
- 한국어: 아무 경고 없이 대체 경로로 영구히 빠지는 것.
- 설명: 형용사 두 개가 각각 다른 위험을 말한다. `silent` 는 로그·알림이 없다는 것, `permanent` 는 다시 돌아오지 않는다는 것. 괄호 속 요약으로 원문처럼 결과를 한마디로 묶어 줄 때 쓰기 좋다.
- 예문: Every later gather is skipped for the life of the process (silent permanent rcp fallback).
- 유사어: fails quietly and never recovers (구어 풀이), a silent degradation (조금 더 넓은 뜻)
- 반의어: a loud failure (바로 드러나는 실패), a transient fallback (잠깐 우회했다가 돌아옴)

## "It is only safe if …"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: diff 만 보고는 확신할 수 없을 때 "이 조건이 지켜지면 괜찮다"로 판정을 유보할 때(리뷰·문어)
- 한국어: ~일 때에만 안전하다.
- 설명: 버그라고 단정하지 않고 안전 조건을 드러낸다. 리뷰어가 전체 파일을 안 봤을 때 정직한 화법이다. 뒤에 `otherwise …` 로 조건이 깨졌을 때의 결과를 붙이는 짝이 표준형이다.
- 예문: It is only safe if the prune runs before this check on every call; otherwise rcp downloads stop after four distinct keys.
- 유사어: This holds only as long as … (격식), This works provided that … (격식), This is fine as long as … (구어)
- 반의어: It is safe regardless of … (조건과 무관하게 안전하다)

## "is dropped with no retry"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 메시지·이벤트가 한 번 실패하면 그대로 사라진다고 경고할 때(기술)
- 한국어: 재시도 없이 버려진다.
- 설명: `drop` 은 네트워크·큐에서 "떨어뜨리다, 잃다". 수동태라 누가 버렸는지보다 메시지의 운명에 초점이 간다. `with no retry` 가 "단 한 번의 기회"를 강조한다.
- 예문: The outcome cube for that alarm is dropped with no retry.
- 유사어: is lost for good (구어), is discarded without a second attempt (격식)
- 반의어: is retried until it succeeds (성공할 때까지 재시도된다), is queued for redelivery

## "…, leaving the alert window open"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 앞 문장이 낳은 결과 상태를 분사구로 꼬리에 붙일 때(문어)
- 한국어: (그 결과) 알림 창이 열린 채로 남는다.
- 설명: 결과 분사구문이다. `…, which leaves the window open` 을 줄인 꼴로 문장을 새로 시작하지 않고 귀결을 덧붙인다. `leave + 목적어 + 형용사` 는 "~을 ~한 상태로 두다".
- 예문: The following `_close_alert` and popup backstop are skipped, leaving the alert window open.
- 유사어: …, so the window stays open (구어), …, with the result that the window remains open (격식, 길다)
- 반의어: …, closing the window cleanly (깔끔하게 닫힌다)

## "X implies (that) Y"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 직접 확인하지 못한 사실을 주변 코드에서 추론했다고 밝힐 때(리뷰·문어)
- 한국어: X 로 보아 Y 일 것이다.
- 설명: 원문은 `The adjacent is_alive() check implies finished threads stay in the dict`. 증거(옆 줄의 검사)를 주어로 세워 "내 추측"이 아니라 "코드가 그렇게 말한다"로 들리게 한다. `suggests` 보다 논리적 함의가 강하다.
- 예문: The adjacent `is_alive()` check implies finished threads stay in the dict.
- 유사어: X suggests Y (더 약한 추론), X indicates Y (중립), judging by X, Y (구어)
- 반의어: X rules out Y (Y 를 배제한다)

## "unless they are pruned before this line"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 끝난 항목을 컬렉션에서 쳐내는 정리 작업이 있어야만 코드가 맞다고 단서를 달 때(기술)
- 한국어: 이 줄보다 앞에서 정리(제거)되지 않는 한.
- 설명: `prune` 은 가지치기에서 온 말로 "죽은·끝난 항목을 걷어내다". `unless … before this line` 은 실행 순서까지 조건에 넣는다. 리뷰에서 "어디서 정리되는지 못 봤다"를 부드럽게 말하는 방법이다.
- 예문: Unless finished threads are pruned before this line, the cap fills up after four recipes.
- 유사어: unless they are cleaned out first (구어), unless stale entries are evicted (캐시 맥락)
- 반의어: if they accumulate (쌓이면)

## "must reach the engineer"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator subagent agent-a914a110 (code-review 결과)
- 맥락: 알림·보고가 반드시 사람에게 도달해야 하는 중요도를 강조할 때(업무)
- 한국어: 엔지니어에게 반드시 전달돼야 한다.
- 설명: `reach` 는 사람을 목적어로 받아 "닿다, 전달되다". `be delivered to` 보다 짧고, "결국 사람 손에 들어가느냐"에 초점이 있다. 메시지가 주어다.
- 예문: The escalation outcomes must reach the engineer even when the send queue is full.
- 유사어: must get to the engineer (구어), must be delivered to the engineer (격식)
- 반의어: never reaches anyone (아무에게도 안 간다)

## "re-implements something the codebase already has"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 중복 구현을 찾는 리뷰 범위를 정의할 때(지시·문어)
- 한국어: 코드베이스에 이미 있는 것을 다시 구현한다.
- 설명: `re-` 접두사 하나로 "또"의 뉘앙스가 붙는다. `the codebase already has` 는 관계대명사 없이 `something` 을 꾸미는 접촉절이다(`something that the codebase already has`).
- 예문: Flag new code in the diff that re-implements something the codebase already has.
- 유사어: duplicates an existing helper (중립, 더 짧음), reinvents the wheel (구어·관용)
- 반의어: reuses the existing helper (기존 헬퍼를 쓴다)

## "Typical suspects:"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 문제가 숨어 있을 법한 후보를 먼저 일러 줄 때(지시문·반쯤 구어)
- 한국어: 흔히 의심할 만한 곳들:
- 설명: 관용구 `the usual suspects`(늘 의심받는 단골 용의자)를 비튼 말이다. 콜론 뒤에 목록을 둔다. 딱딱한 지시문에 살짝 위트를 넣는다.
- 예문: Typical suspects: mean/σ/median math, number formatting, date formatting, and xlsx sheet building.
- 유사어: the usual suspects (원형 관용구, 구어), Common places to look: (중립·격식)
- 반의어: unlikely places (잘 안 숨는 곳)

## "confirm the semantics really match"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 이름이 같아도 동작이 같은지 확인하라고 할 때(기술 리뷰)
- 한국어: 의미(동작 규칙)가 정말 같은지 확인하라.
- 설명: `semantics` 는 코드에서 "겉모양이 아니라 실제 의미·동작". 원문은 괄호로 `sample vs population σ, null handling` 을 예로 든다. `really` 가 "겉보기에 비슷해도"를 깔고 있다.
- 예문: Confirm the semantics really match, e.g. sample vs population σ and null handling.
- 유사어: check they behave the same (구어), verify behavioural equivalence (격식)
- 반의어: only the names match (이름만 같다)

## "Drop anything you cannot confirm."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 리뷰·조사 결과에서 추측성 항목을 걸러 내라고 지시할 때(지시)
- 한국어: 확인할 수 없는 것은 빼라.
- 설명: 다섯 단어짜리 명령문이 품질 기준 전체를 정한다. `drop` 은 "목록에서 빼다". 위의 `is dropped` 와 같은 동사지만 여기선 의도적으로 걸러 내는 쪽이다.
- 예문: Verify every finding against the existing helper, and drop anything you cannot confirm.
- 유사어: Leave out anything unverified (중립), Only report what you can back up (구어)
- 반의어: Include everything, even hunches (짐작까지 다 넣어라)

## "Not in scope:"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 지시문·기획서에서 하지 말아야 할 범위를 머리말로 못 박을 때(문어)
- 한국어: 범위 밖:
- 설명: 동사 없는 머리말 + 콜론 + 목록. `Out of scope:` 도 같은 뜻이다. 하지 말 일을 미리 적어 두면 작업자가 엉뚱한 데 시간을 안 쓴다.
- 예문: Not in scope: correctness bugs, style nits, test files' internal duplication, docs.
- 유사어: Out of scope: (같은 뜻), Leave alone: (구어), Excluded: (격식)
- 반의어: In scope: (범위 안)

## "most valuable first"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 결과 목록의 정렬 기준을 짧게 지정할 때(지시)
- 한국어: 가장 가치 있는 것부터.
- 설명: `X-est first` 꼴의 정렬 지정. 버그 리뷰는 `most-severe first`, 정리 리뷰는 `most valuable first` 처럼 기준 형용사만 갈아 끼운다.
- 예문: Return at most 12 findings, most valuable first.
- 유사어: in order of value (격식), best ones up top (구어)
- 반의어: least valuable first / in no particular order (순서 없이)

## "areas you checked and found clean"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 문제가 없었던 곳도 보고에 남기라고 할 때(리뷰·감사)
- 한국어: 확인해 보니 문제없던 영역.
- 설명: `find + 목적어 + 형용사` 는 "확인해 보니 ~였다". `clean` 은 리뷰에서 "지적할 것 없음". 빈 결과도 "안 봤다"와 "봤는데 없었다"를 갈라 적게 만든다.
- 예문: End with a one-line note on areas you checked and found clean.
- 유사어: areas that came back clean (구어), areas with no findings (중립)
- 반의어: areas you did not get to (손대지 못한 영역)

## "concrete cost"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 문제를 지적할 때 "그래서 얼마나 손해인가"를 수치로 달라고 할 때(업무)
- 한국어: 구체적 비용(손해).
- 설명: 원문은 `concrete cost (lines duplicated / drift risk)`. `concrete` 는 "막연하지 않고 셀 수 있는". 지적의 무게를 독자가 판단하게 해 준다.
- 예문: For each finding, give the concrete cost: lines duplicated and the risk of the copies drifting apart.
- 유사어: tangible impact (격식), what it actually costs us (구어)
- 반의어: a vague concern (막연한 우려)

## "alter intended behaviour"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt subagent agent-acd2e2cf (정리 리뷰 지시문)
- 맥락: 리팩터링 제안이 동작을 바꾸면 안 된다는 경계를 칠 때(문어)
- 한국어: 의도된 동작을 바꾸다.
- 설명: `alter` 는 `change` 의 문어체. `intended` 가 "지금 동작이 맞다는 전제"를 깐다. 영국식 철자 `behaviour` 그대로다.
- 예문: Do not propose changes that alter intended behaviour or visible strings.
- 유사어: change what the code does (구어), modify the expected behaviour (중립)
- 반의어: preserve behaviour / behaviour-preserving (동작을 보존하는)

## "There's a … page — that's the …"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt da5cd7a3 [assistant]
- 맥락: 상대가 쓴 말이 코드의 무엇을 가리키는지 짚어 연결할 때(구어·작업 중 혼잣말)
- 한국어: ~ 페이지가 있네요 — 그게 (말씀하신) ~예요.
- 설명: 원문은 ``There's a `/notices` page — that's the 공지사항.`` 앞절에서 존재를 알리고 대시 뒤 `that's the X` 로 "당신이 말한 그것"과 동일시한다. 정관사 `the` 가 "우리 둘 다 아는 그것"을 가리킨다.
- 예문: There's a `/notices` page — that's the announcements board you meant.
- 유사어: That must be the … (추정), I'm guessing that's the … (구어)
- 반의어: That's not the … I'm looking for (내가 찾던 게 아니다)

## "Now X, then Y."
- 레지스터: conversational
- 출처: transcript:english-study 8766b3cd [assistant]
- 맥락: 작업 중 다음 순서를 짧게 알릴 때(구어·진행 보고)
- 한국어: 이제 X, 그다음 Y.
- 설명: 원문은 `Now digest, then register notes and index.` 동사를 빼고 명사만 남긴 전보체다. 진행 상황을 말로 알릴 때는 이 정도가 자연스럽다. 글로 쓸 때는 `I'll write the digest next, then …` 처럼 동사를 살린다.
- 예문: Now the tests, then the docs.
- 유사어: Next up: X, then Y. (구어), Next, I will …, followed by … (격식)
- 반의어: (마땅한 반대 표현 없음)

## "operator wiring"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ops_store/docs/with_dag_usage.md
- 맥락: Airflow DAG 파일이 맡는 일(태스크를 서로 잇는 것)을 업무 로직과 구분할 때(기술 문서)
- 한국어: 오퍼레이터 배선(태스크 연결).
- 설명: 원문은 한국어 문장 속 `schedule, dependency, operator wiring만 담당`. `wiring` 은 전선을 잇는 일에서 온 말로 "부품을 서로 연결하는 접착 코드"다. 로직은 다른 곳에 두고 DAG 는 연결만 한다는 설계 원칙을 한 단어로 담는다.
- 예문: The DAG file handles only scheduling, dependencies, and operator wiring; the business logic lives in plain Python functions.
- 유사어: plumbing (구어, 더 넓은 뜻), glue code (중립)
- 반의어: business logic (실제 업무 로직)

## "JSON-safe"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ops_store/docs/with_dag_usage.md
- 맥락: 그대로 직렬화해도 깨지지 않는 값으로 바꾼다고 말할 때(기술 문서)
- 한국어: JSON 으로 안전하게 직렬화 가능한.
- 설명: `X-safe` 합성어 패턴이다(`thread-safe`, `URL-safe`, `type-safe`). 원문은 `datetime`, `Decimal`, `NaN` 같은 값을 `JSON-safe 값으로 변환`. 하이픈을 넣어 형용사 하나로 묶는다.
- 예문: `normalize_document` converts `datetime`, `Decimal`, and `NaN` into JSON-safe values.
- 유사어: JSON-serializable (같은 뜻, 더 정식), safe to dump as JSON (구어)
- 반의어: non-serializable (직렬화 불가)
