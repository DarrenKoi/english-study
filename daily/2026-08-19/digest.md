# 2026-08-19 — 오늘의 표현

1. **What checks out** — 리뷰 보고서에서 지적을 꺼내기 전에 "여기까지는 이상 없다"를 먼저 묶는 소제목. 통과분을 세워 두면 뒤의 지적이 트집이 아니라 판정으로 읽힌다.
2. **silent truncation ↔ surface it** — 상한에 걸려 잘렸는데 아무 신호도 안 나가는 결함. 짝이 되는 동사가 `surface`(드러내다)라, "감지한다 + 드러낸다"를 나눠 쓰면 어디가 빠졌는지 분명해진다.
3. **structurally cannot catch it** — 픽스처가 결함을 똑같이 복제하고 있어 테스트를 더 돌려도 소용없다는 말. `didn't catch` 와 무게가 다르다.
4. **X is still decoration** — 화면에 뜨지만 아무것도 보증하지 않는 지표. 값이 틀렸다가 아니라 뜻이 없다는 지적이라 반박하기 어렵다.
5. **a chicken-and-egg (in the gating)** — 선택해야 데이터가 오는데 데이터가 와야 선택지가 생기는 교착. 관용구라 설명 없이 곧장 "그럼 게이트를 어디 걸까"로 넘어간다.
6. **an explicit empty state** — 비어 있음을 숨기지 않는 화면. 스켈레톤은 데이터가 오는 중이라는 약속으로 읽히므로, 아무것도 요청하지 않았을 때는 거짓말이 된다.
7. **zero file overlap, so I rebased rather than merged** — 근거를 앞, 결정을 뒤에 두는 보고 순서. 뒤집으면 사후 정당화처럼 들린다.

### 오늘의 정독
`reading.md` 단락 1 — "The gated page fetches 44 KB to use 1.2 KB." 숫자 두 개의 대비로 낭비를 증명한 뒤, 자기가 쓴 `necessary` 에 따옴표를 씌워 되받으며 예상 반론을 미리 좁히는 문장 운용을 봅니다.

### 오늘의 코칭
- 한글→영어: "실제 align fail 발생했을 때 녹화하는게 더 확실하지 않으려나?" → `Though — wouldn't recording an actual align fail be more convincing?` (확신 없는 되짚기는 부정 의문문 자리)
- 한글→영어: "생성 스크립트도 같이 커밋해줘" → `Commit the generator scripts alongside it.` ("같이"는 `together` 가 아니라 `alongside`)
- 영어 다듬기: `The recipes I tried to get them are available in ...` → 관계절 안에 목적어를 또 쓰는 이중 목적어 오류. `The recipes I tried to open ...`
- 영어 다듬기: `Wait until the agent finished the job` → `until` 절은 미래 완료 시점이라 과거형이 아니라 `has finished`. 더 나은 표현은 `Hold off until the agent in the first pane is done`.

자세한 건 `coaching.md`.

> 처리 항목 9개 / 미뤄진 항목 5개
