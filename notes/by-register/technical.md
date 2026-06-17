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

### auto_recipe_creator 배치 (4회차: grill-with-docs)
- **stress-test (a plan/scenario)** — 극단 시나리오로 두드려 약점을 찾다.
- **don't couple X to Y** — 두 관심사를 서로 얽매지 마라 (loose coupling).
- **pin down (a faint box)** — 흐릿한 것을 정확히 짚어내다.
- **benchmark against (real data)** — 실데이터를 기준으로 성능을 재다.

## 2026-06-18 — wiki_for_office 아키텍처 + ML 설계 spec 배치
- **degrade gracefully / graceful degradation** — 의존 서비스가 없어도 죽지 않고 품질만 낮춰 계속 동작.
  - 예: When the glossary service is unreachable, retrieval degrades gracefully — it just skips acronym expansion instead of failing the whole query.
- **safe by construction** — 검사가 아니라 구성 방식 자체로 안전(≈ made structurally impossible).
  - 예: The two-repo split is safe by construction: there is simply no public remote for the content to leak through.
- **silently drift** — 기준에서 소리 없이(경고 없이) 어긋나다 / 표류하다.
  - 예: A fact pinned to a regenerable extract can silently drift while still looking properly cited.
- **opt-in, default-OFF** — 직접 켜야 동작하고 기본값은 꺼짐 (안전 기본값).
  - 예: Auto-capture is an opt-in, default-OFF per-user toggle, so nothing is recorded unless the user turns it on.
- **shadow mode** — 결정에 반영하지 않고 점수/결과만 기록하며 검증하는 출시 단계.
  - 예: We'll ship the scorer in shadow mode first — it logs a score on every match but doesn't change the ranking.
- **kill switch** — 문제 시 즉시 비활성화하는 비상 플래그 (보통 로드 실패 시 자동 폴백과 짝).
  - 예: The metric scorer is flag-gated with a kill switch: if the model fails to load, it falls back to the old reranker and logs a warning.
- **sit behind (an interface)** — 구현이 우리가 소유한 인터페이스 뒤에 가려져 교체·테스트 가능.
  - 예: Company services sit behind wiki-owned interfaces, each with a real and a fake implementation, so the core stays testable off the company network.
- **train/serve skew** — 학습 때와 추론 때 입력 처리가 달라 생기는 성능 괴리.
  - 예: We extract candidate patches with the same function at train and serve time to keep train/serve skew to a minimum.
