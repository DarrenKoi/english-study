# 2026-07-01 — 오늘의 표현

코드리뷰 대화에서 건진 **엔지니어링 설계 비평** 어휘 위주입니다.

- **bolted on (as a special case)** — 기존 구조에 녹지 않고 특수 케이스로 억지로 덧붙이다(부정적).
- **a too-shallow fix** — 근본 원인 대신 증상만 덮은 얕은 수정. "a classic too-shallow fix"로 비꼬는 상투구.
- **no collateral damage** — 변경이 무관한 곳을 망가뜨리지 않았다. 리뷰 결론에서 "Collateral damage: none."
- **scope creep** — 작업 범위가 야금야금 늘어남. "not scope creep"으로 "범위 확장 아님"을 변호.
- **swallow an exception** — 예외를 잡고도 처리·전파 없이 묻어버려 오류가 숨다(안티패턴).
- **a latent bug** — 평소엔 안 터지지만 특정 조건에서만 드러나는 잠복 결함.

### 오늘의 정독
영어 명령문 단락의 모범 — "If … STOP and report … do NOT guess … this honesty is more valuable than a plausible guess." 조건문 + would 인과 + 단정의 흐름을 `reading.md`에서.

### 오늘의 코칭
- 한글→영어: "제대로 못 잡고 있다" → *isn't reliably locking onto the point* (잡다=locate/lock onto 구분); "검증된 변경만 포팅한다" → *Only validated changes get ported back* (방침 진술=수동태 현재시제). 자세히는 `coaching.md`.

> 처리 항목 17개 (표현 11 · 정독 2 · 코칭 4) / 미뤄진 항목 0개
