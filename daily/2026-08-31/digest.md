# 2026-08-31 — 오늘의 표현

1. **contract drift** — 백엔드가 필드를 지웠는데 프론트 타입은 남은, 아무 신호 없이 벌어지는 계약 불일치. JSON 경계는 타입 검사가 닿지 않는다.
2. **this comment now lies** — 코드가 바뀌어 주석이 거짓이 된 상태. `is outdated` 와 달리 "읽는 사람을 속인다"는 능동적 판정이라 훨씬 세다.
3. **not swap-safe** — 겉보기에 같아도 그대로 갈아 끼우면 동작이 바뀌는. 리팩터링 범위를 한 줄로 가를 때 쓴다.
4. **makes silence the failure mode** — 기본값이 그럴듯한 값이라 틀려도 아무도 못 알아채게 만든다. 빈 화면보다 `a confidently wrong one` 이 나쁘다.
5. **a feature nobody finds** — 있어도 발견되지 않으면 없는 것과 같다. 기본값을 꺼 둘지 정할 때의 반대 논거.
6. **duplication documented in prose rather than removed** — 중복을 없애는 대신 "여기는 저기와 같음" 주석만 달아 둔 상태. 주석 개수가 곧 증거가 된다.
7. **Deliberately not done:** — 보고 끝에 안 한 일과 그 이유를 밝히는 소제목. `Skipped` 보다 강해 "몰라서가 아니라 재 보고 판단했다"가 된다.

### 오늘의 정독
단락 1 — 탭이 두 개 켜진 버그의 원인 보고. 강조 조동사 `did`(`/tttm` *did* have a branch)로 예외를 먼저 인정한 뒤 그것을 증거로 되돌리는 수를 눈여겨볼 것. 콜론 뒤 명령형이 조건절을 대신한다(`forget a branch and you get…`). → `reading.md`

### 오늘의 코칭
- 한글→영어: "실험실 페이지에서 상단 FeatureTabs 의 "장비 상태" 가 함께 활성으로 표시됨" → `the top-level FeatureTabs bar lights 장비 상태 as active as well` — 개조식 "표시됨"은 수동태 대신 화면 요소를 주어로 세운 능동으로.
- 영어 다듬기: `Is there way to combine the two pages into a single one?` → 관사 `a way` 가 빠졌고 `into a single one` 은 늘어진다. `Could these two pages be merged into one?` → `coaching.md`

> 처리 항목 36개 / 미뤄진 항목 933개
