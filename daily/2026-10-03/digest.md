# 2026-10-03 — 오늘의 표현

- **none blocking** — 지적은 있지만 머지를 막을 건 없다. `Three small findings, none blocking; otherwise the diff is clean.` 한 줄에 개수, 심각도, 나머지 상태가 다 들어간다.
- **not made worse by the diff** — 문제는 있어도 이번 변경이 키운 게 아니라서 안 건드린다는 근거.
- **half-applied** — 고친 방식은 옳은데 절반만 적용됐다. `is the right mechanism, but` 뒤에 붙인다.
- **a hypothesis, not something I tested** — 주장 뒤에 "돌려 본 건 아니다"를 스스로 밝히는 한 줄.
- **closeness in time does not prove that …** — 시간상 가깝다고 원인은 아니다. "상관은 인과가 아니다"의 구체판.
- **sorts before** — `sort` 를 자동사로. `10000 sorts before 1000` 처럼 문자열 정렬 버그를 설명할 때.
- **is a fine answer** — 최선은 아니어도 그렇게 하면 된다. 뒤에 `just say which one is being used` 같은 조건을 단다.

### 오늘의 정독
Codex 가 "클릭 직후의 화면 변화는 버리자"는 설계에 반대하는 다섯 문장. `Hypothesis:` 로 검증 수준을 먼저 밝히고 `The safer rule is to merge … but never delete one because …` 로 대안을 낸다. 9,999 프레임을 넘으면 정렬이 뒤집히는 버그 보고와, env 에 쓴 값이 호출보다 오래 남는다는 지적(`The env write outlives the call.`)도 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "리허설 필요 없어" → `No need for a dry run.` / "사용 불가능" → `… isn't an option.` / "이를 어떻게 workflow 형태로" → `How could we turn that into a workflow?` / "쌓이면 재검증" → `once more data has built up`(시간절에는 `will` 을 쓰지 않는다).
- 영어 다듬기: `the part of reply` → `part of the reply`. / `go /simplify` → `Go ahead and run /simplify`. 카드 26장은 `coaching.md`.

> 처리 항목 17개 / 미뤄진 항목 266개
