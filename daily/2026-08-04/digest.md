# 2026-08-04 — 오늘의 표현

1. **an assumption with no mechanism behind it** — 강제할 장치가 없는 기대는 가정일 뿐이다.
   "'pandas will bring a good numpy' is an assumption with no mechanism behind it."
2. **import success proves presence, never version** — 증거가 어디까지 증명하는지 잘라 말하는 틀.
   `X proves A, never B` 로 검사 방식을 바꾼 이유를 한 문장에 담는다.
3. **the corollary is counter-intuitive** — 상식에 어긋나는 조언을 "앞 논증의 귀결"로 포장해 내놓기.
4. **silent-wrong instead of loud-broken** — 조용히 틀리는 실패와 요란하게 터지는 실패의 대비.
   낡은 사본이 옛 키로 계속 대답하면 화면은 멀쩡한 채 값만 틀린다.
5. **the error you see is the error path, not the cause** — 지금 보이는 예외는 진단 코드가 죽은 자리다.
   `sorted(frames)` 가 원인을 설명하려다 먼저 터져 진짜 원인을 가렸다.
6. **request-order luck** — 되고 안 되고가 설계가 아니라 요청 순서 운에 달려 있었다.
   짝이 되는 표현: **nobody was listening** — 신호는 있었는데 받는 쪽이 없었다.
7. **a two-minute check on your side** — 넘기는 일의 크기를 시간으로 미리 못 박기.

### 오늘의 정독

단락 1이 축이다 — `pip install -r` 이 업그레이드 명령이 아니라는 사실 하나에서 "버전이 중요한
간접 의존성은 직접 선언하라"는 반직관적 결론까지 끌고 간다. 현재시제로 규칙을 적고,
`only if` 로 필요조건을 건 뒤 대시로 세 번째 범주를 얹는 전개를 눈여겨볼 것. → `reading.md`

### 오늘의 코칭

- **한글→영어**: "only 측정 위치" → `only the measurement-point table renders.`
  화면 요소를 가리킬 땐 table/panel 을 붙여야 좌표 데이터와 갈린다.
- **영어 다듬기**: "or show some stakeholder?" → `or show a placeholder?`
  발음이 비슷해 생긴 어휘 혼동. placeholder 는 준비될 때까지 자리를 지키는 임시 표시다.
- **영어 다듬기**: "update the the latest ones" → `upgrade the ones that matter.`
  update(내용 갱신)와 upgrade(버전 올리기)는 다르고, 여기서는 후자다.

→ `coaching.md`

> 처리 항목 16개 / 미뤄진 항목 1163개
