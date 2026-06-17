# Technical register

엔지니어링·통계·API 맥락의 전문 용어와 표현.

## 2026-06-17
- **single source of truth** — 단일 진실 공급원(SSOT). [→ daily](../../daily/2026-06-17/new-expressions.md)
- **a row count separate from the row payload** — 데이터(payload) 와 별도의 행 개수(총계).
- **first-class** — 일급 객체 / 정식 지원 대상.
- **worst-case** — 최악값 기준.
- **overfit / rank-deficient** — 과적합 / 행렬 계수 부족.
- **borrow strength** — 유사 그룹의 정보를 빌려 추정을 안정화.
- **human-readable** — 사람이 읽을 수 있는 (vs machine-readable).
- **must implement these contracts identically** — 계약을 동일하게 구현.

### auto_recipe_creator 배치
- **anchor on (the first idea)** — 처음 가설에 고착되다 (anchoring 편향).
- **carry lock-in** — (기술 선택이) 종속을 수반하다.
- **load-bearing** — 빠지면 전체가 무너지는 핵심. 반대 `lean`.
- **fail-safe** — 불확실하면 안전한 거부로 떨어지는 설계.
- **create X lazily — only when needed** — 최초 필요 시점까지 생성을 미루다.
- **measure first, fix second** — (성능) 측정이 먼저, 수정은 그 다음.

### auto_recipe_creator 배치 (추가 발굴)
- **deep module / shallow module** — 작은 인터페이스+큰 구현(깊음) vs 껍데기(얕음).
- **the interface is the test surface** — 공개 인터페이스를 통해 테스트하라.
- **tracer bullet (vertical slice)** — 끝에서 끝까지 관통하는 가장 얇은 한 줄기 구현.
- **never refactor while RED; get to GREEN first** — 실패 중엔 리팩터 금지, 통과부터.
- **progressive disclosure** — 핵심만 먼저, 상세는 단계적으로 드러내는 설계.
- **hot path** — 가장 자주/성능에 민감하게 도는 핵심 실행 경로.
