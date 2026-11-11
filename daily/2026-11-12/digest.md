# 2026-11-12 — 오늘의 표현

1. **Default to X** — 따로 지시가 없으면 X로 한다. 컨벤션 문서에서 기본 동작을 정하는 첫 문장.
2. **take it as the current state rather than reverting it** — 누가 바꿔 놓은 것은 되돌리지 말고 지금 상태로 받아들인다.
3. **if the change looks wrong, say so rather than undoing it yourself** — 이상하면 직접 고치지 말고 말부터. `say so` 의 `so` 가 앞 절을 받습니다.
4. **otherwise no need to call it out** — 문제없으면 굳이 언급하지 않아도 된다. `call out` = 콕 집어 말하다.
5. **If a wait times out, inspect … before deciding what to do.** — 시간 초과가 나면 재시도보다 확인이 먼저.
6. **sessions you did not create** — 내가 만들지 않은 자원은 닫지 않는다는 범위 규칙.
7. **This is how X surfaces …** — 시스템이 정보를 어떤 식으로 보여 주는지 설명하는 틀. `surface` 는 타동사.

### 오늘의 정독
단락 2: herdr 스킬의 대기 규칙입니다. `If …` 조건절 세 개가 각각 명령문을 이끌고, `the difference is whether the result has been seen` 의 현재완료 수동태가 "봤다는 결과가 남아 있는지"만 묻습니다. → `reading.md`

### 오늘의 코칭
- 한글→영어: "응 완성형으로 바꿔줘" → "Yes, make them ready to use as-is." "완성형"은 `complete` 보다 `ready to use as-is`.
- 한글→영어: "완료 후 commit and push. claude artifact에 republish도 진행." → "Once that's done, commit and push, and republish the Claude artifact too." `republish` 는 목적어를 바로 받습니다.
- 번역 정독: "다만 대부분 그대로 붙여 넣을 완성형은 아닙니다." → "Most of them aren't ready to paste in as-is, though." → `coaching.md`

> 처리 항목 2개 / 미뤄진 항목 167개
