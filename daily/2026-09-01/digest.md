# 2026-09-01 — 오늘의 표현

1. **X buys A and costs B** — 한 주어에 `buy` 와 `cost` 를 걸어 득실을 나란히 놓는 대구. 이득을 사소하게, 비용을 구체적으로 적으면 판정이 문장 안에서 저절로 난다. → *Moving them under one folder buys a shorter `ls` and costs a repo-wide rename.*
2. **not mine to fix here** — 내 변경과 무관한 기존 실패를 발견했을 때. `here` 가 "영원히 안 고친다"를 "이 작업 범위에서는 아니다"로 좁혀 준다.
3. **removes the whole failure class** — 개별 버그를 막는 가드 대신 기능을 삭제한 이유. 이 말이 붙으면 회귀 테스트를 안 쓴 근거까지 자동으로 설명된다.
4. **which is worse than never** — "가끔 맞는" 절충안을 반대할 때. 앞에 `sometimes` 를 강조해 두고 뒤에서 받는 대구로 쓴다.
5. **no amount of staring at code will save you** — 재현 수단 없이 코드만 읽는 디버깅을 말리는 말. 노력 부족이 아니라 접근법이 틀렸다는 프레임.
6. **a design call that's genuinely yours** — 조사는 다 해 놓고 마지막 선택만 넘길 때. `genuinely` 가 사교적 양보와 진짜 위임을 가른다.
7. **if the itch is X, the cheaper fix is Y** — 큰 요청을 거절하면서 진짜 불만만 싼값에 해소해 줄 때. 요청의 형태와 동기를 갈라놓는 장치.

전체 19개는 [new-expressions.md](new-expressions.md).

### 오늘의 정독
단락 1은 디버깅에서 **피드백 루프를 먼저 만들라**는 지침 — 조건절·세미콜론·짧은 명령문이 어떻게 "규칙 선언"의 리듬을 만드는지 본다. 단락 2는 리팩터링 제안을 거절하는 답변으로, 조동사 `would` 하나가 지시와 권고를 가르는 자리다. [reading.md](reading.md)

### 오늘의 코칭
- 한글→영어: "한번에 가자"는 `let's go at once` 가 아니라 `let's do it all in one pass` — '한 번에'가 시점이 아니라 작업 분할을 뜻하기 때문. "컨트롤이 둘이 되면서 게이트 이름이 거짓말을 하기 시작합니다" → *the gate's name starts to lie* (영어에서 이름·지표가 주어면 `lie` 를 자동사로 그냥 쓴다).
- 영어 다듬기: `why not making` → `why not make`(`why not` 뒤는 동사원형), `the old files that no more needed` → `that are no longer needed`. 포트에는 `clean` 이 아니라 `free up ports 5050 and 3000` 이 굳은 짝이다.

전체 15장은 [coaching.md](coaching.md).

> 처리 항목 25개 / 미뤄진 항목 899개
