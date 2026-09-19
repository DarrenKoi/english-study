# 2026-09-20 — 오늘의 표현

- **If you catch yourself (doing X), stop** — 무심코 나쁜 습관으로 빠지는 순간을 짚는다. `find yourself` 보다 "들켰다"는 어감이 짙다.
- **Don't block on it** — 확인은 요청하되 답을 기다리느라 멈추지는 마라. 스레드 용어를 사람에게 빌려 썼다.
- **each one reproduces** — 버그를 주어로 한 자동사 `reproduce`. "재현된다"를 `is reproduced` 로 옮기지 않아도 된다.
- **the test locks the defect in** — 테스트가 틀린 동작을 기대값으로 굳혀 버렸다. 좋은 뜻의 `lock in` 을 뒤집어 썼다.
- **hold up** — 따져 봐도 버틴다. `Most of the fixes hold up, but one … remains` 가 재리뷰의 기본 틀.
- **Taking that as: …** — 애매한 지시를 되묻지 않고 내 해석을 한 줄로 밝힌 뒤 진행한다.
- **One thing worth repeating, since it affects how you read the numbers** — 반복하는 이유를 `since` 로 먼저 대서 잔소리로 들리지 않게 한다.

### 오늘의 정독
DESIGN.md 완료 보고 단락 — 지금 상태는 현재, 한 일은 과거, 고치기 전 문제도 과거로 시제를 나눠 쓴다. `The doc couldn't be built from before.` 는 `from before` 가 한 덩어리가 아니라 문장 끝에 남은 전치사 `from` 과 부사 `before` 다. 결함 논증 단락(`asserts that pending` 의 `that` 은 지시어)과 herdr 상태 규칙 단락은 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "코드에 반영해줘" → `apply it to the code`. `reflect` 는 한국어 화자의 버릇이다. / "문제는 … 잘 집어냄. 하지만 …" → 정상 케이스를 먼저 말하고 `The problem is when …` 을 뒤에 둔다.
- 영어 다듬기: `after the next running` → `after the next run` (한 번의 실행은 셀 수 있는 `run`) / `fix the uncommited changes` → `Commit and push the pending changes.` (`fix` 가 "고쳐라"로도 읽혀 어시스턴트가 해석부터 밝혀야 했다). 카드 13장은 `coaching.md`.

> 처리 항목 19개 / 미뤄진 항목 465개
