# 2026-09-27 — 오늘의 표현

- **change the question rather than pad the answer** — 모델이 약한 종류의 답을 보정값으로 덧대지 말고 묻는 방식을 바꾸자는 설계 원칙. `rather than` 앞뒤로 동사원형을 맞춘다.
- **Two gates on the same fact are not twice as safe.** — 같은 사실을 두 번 검사하면 더 안전하다는 직관을 뒤집는 한 줄. `twice as + 원급` 배수 비교.
- **That is a deliberate trade, but it has a weak point.** — 알고 고른 절충이라고 방어하면서 약점도 같이 인정한다.
- **in order of likelihood** — 원인 후보를 확률 순으로 늘어놓겠다고 먼저 알리는 말. `in order of importance` 와 같은 틀.
- **Not quite.** — `No` 보다 부드러운 정정. 바로 다음 문장에서 어디가 다른지 짚어야 퉁명스럽지 않다.
- **building ahead of the data** — 결과가 안 나온 단계 위에 다음 작업을 미리 쌓는 걸 말린다. `would be` 로 부드럽게.
- **silently revert to X** — 에러 없이 조용히 약한 동작으로 돌아가는 함정. 개발 영어에서 `silently` 는 "경고 없이".

### 오늘의 정독
coarse bbox 를 읽어 fine 단계의 보정을 버리고 있던 버그를 설명한 단락. `Found it.` 으로 시작해 과거진행형 `I was throwing the correction away` 로 "계속 버리고 있었다"를 드러낸다. 설계 약점을 인정하는 단락과 `Not quite.` 로 상대 이해를 바로잡는 단락은 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "한칸씩 밀려있다" → `They're all off by one button.` 개발자에게 익숙한 off-by-one 을 그대로 쓴다. / "~하도록 되어 있지?" → `What order is it set up to run in?` 로 먼저 묻고 선택지를 `Does it A? Or does it B?` 로 나눈다.
- 영어 다듬기: `twice longer` → `twice as long`(배수 비교). / `ask for the help how to set properly to codex` → `ask Codex how to set this up properly`. 묻는 상대를 `ask` 바로 뒤에 두는 틀은 어제에 이어 또 나왔다. 관사 누락(`a git issue`, `a single trusted user`)도 여전하다. 카드 58장은 `coaching.md`.

> 처리 항목 10개 / 미뤄진 항목 385개
