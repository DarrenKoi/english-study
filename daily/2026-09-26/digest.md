# 2026-09-26 — 오늘의 표현

- **It's by design.** — 이상해 보이는 동작이 버그가 아니라 설계라고 첫마디에 정리한다. 뒤에 누가 정했는지(`The spec … require it`)를 붙여야 변명으로 안 들린다.
- **Mostly yes, with two catches.** — 대체로 맞다고 인정하고 단서 개수를 먼저 밝힌다. 이어서 `Catch 1: …` 로 번호를 붙여 푼다.
- **Next to these, X is negligible.** — 진짜 병목을 먼저 보인 뒤 상대가 걱정한 비용을 접는다. `next to` 는 "~에 비하면".
- **real but second-order** — 효과를 인정하되 순위를 매긴다. 뒤에 `measure … before and after rather than guessing` 을 붙이면 측정 제안까지 된다.
- **the wrong rung to stop at** — 시험 순서를 사다리로 세운 뒤 "지금 멈출 단계가 아니다". 문장 끝에 전치사 `at` 이 남는다.
- **collapse X and Y into one** — 구별해야 할 두 경우를 한 경우로 뭉갠 실수를 인정하는 말. 과거완료 `I'd collapsed` 로 시간 순서를 드러낸다.
- **the gating question, not a nice-to-have** — 선택 사항이던 확인을 다음 단계를 막는 관문으로 끌어올린다.

### 오늘의 정독
Codex 리뷰로 드러난 자기 버그를 설명한 단락. `My bug, and the sharpest one yet.` 으로 책임부터 지고 과거완료 `I'd collapsed them into one` 으로 실수의 시점을 짚는다. 해싱 성능 걱정에 답한 단락과 glide 기능 추가를 순서 문제로 돌린 단락은 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "SMB는 아직 사용 안하니 제거하자. (필요할 때 추가)" → `Since we don't use SMB yet, let's drop it — we can add it back when we need it.` 괄호 메모는 `add it back` 문장으로 살린다. / "keystore waiting 풀기. 세세한 체크포인트도 완화" → `lift the keystore wait, and relax the fine-grained checkpoints`.
- 영어 다듬기: `have we considered to use` → `considered using`. `consider` 는 `-ing` 를 받는다. / `What I am concern is` → `My concern is`. 요청 짝 `ask Codex for a review` 와 `an engineers` 관사 실수는 어제에 이어 또 나왔다. 카드 35장은 `coaching.md`.

> 처리 항목 9개 / 미뤄진 항목 392개
