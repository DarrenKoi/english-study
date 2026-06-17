# 새 표현 — 2026-06-17

> 출처는 모두 `repo:skewnono_v3_nuxt` (docs). 사용자 주문/대화 항목은 이번 배치에 없었습니다.
> 프로젝트 고유어(lot, recipe, fab 등)는 버리고, 다른 글에서도 통하는 영어 표현만 골랐습니다.

## "single source of truth"
- 레지스터: professional, technical
- 출처: repo:adr/0003-admin-only-rule-editor
- 한국어: 단일 진실 공급원 — 모두가 믿고 참조하는 *유일한* 기준 데이터/문서.
- 설명: 같은 사실이 여러 곳에 흩어져 서로 어긋나는 것을 막기 위해 "정본은 여기 하나" 라고 못 박을 때 씁니다. 약어 SSOT 로도 자주 씁니다.
- 예문: The rule table is the single source of truth; every traffic-light color is computed from it.

## "the bridge between X and Y"
- 레지스터: professional, conversational
- 출처: repo:api-contracts/README
- 한국어: X 와 Y 를 잇는 다리(연결 고리).
- 설명: 두 분리된 세계를 매개하는 무언가를 설명할 때 쓰는 비유. 원문: "These contracts are the bridge between home (frontend) and work (backend) development."
- 예문: The spec layer is the bridge between the home mock and the office backend.

## "document what it actually returns, not what feels canonical"
- 레지스터: professional, technical
- 출처: repo:api-contracts/README
- 한국어: "정석처럼 *느껴지는* 모양" 이 아니라 "*실제로* 반환되는 모양" 을 적어라.
- 설명: 이상적인 설계가 아니라 현실의 동작을 문서화하라는 실무 지침. `what feels canonical` = "교과서적으로 맞아 보이는 것" 을 가리키는 좋은 관용 표현.
- 예문: Document what the endpoint actually returns, not what feels canonical.

## "a row count separate from the row payload"
- 레지스터: technical
- 출처: repo:api-contracts/README
- 한국어: 행 데이터(payload) 와 *별도로* 가지는 행 개수(총계).
- 설명: `payload` = 실제 알맹이 데이터, `separate from ~` = "~ 와 따로". API 가 `{ data: [...], total: N }` 처럼 총계를 따로 줄 때의 설명문.
- 예문: Use an envelope when you need a row count separate from the row payload.

## "first-class"
- 레지스터: technical, professional
- 출처: repo:adr/0002-shared-url-across-audiences
- 한국어: 일등 시민 — 시스템이 *정식으로 동등하게* 대우하는 대상.
- 설명: 프로그래밍에서 "first-class citizen"(일급 객체)에서 온 말. "곁다리가 아니라 정식 지원 대상" 이라는 뜻으로 설계 글에 자주 등장.
- 예문: Both operators and executives are first-class audiences of this page.

## "conservative default"
- 레지스터: professional, technical
- 출처: repo:adr/0003-admin-only-rule-editor (보수적 default)
- 한국어: 보수적인(안전한 쪽의) 기본값.
- 설명: 나중에 풀어주긴 쉬워도 거둬들이긴 어려운 결정에서, *덜 주는 쪽* 을 기본으로 두는 전략. `default` 는 "기본값/기본 설정".
- 예문: We start read-only as a conservative default — it's easier to grant access later than to take it away.

## "bus-factor 1"
- 레지스터: conversational, technical
- 출처: repo:adr/0003-admin-only-rule-editor
- 한국어: 버스 지수 1 — "그 사람이 버스에 치이면(=빠지면) 프로젝트가 멈춘다", 즉 핵심 지식이 한 사람에게만 묶인 위험.
- 설명: 농담조지만 실무에서 진지하게 쓰는 리스크 용어. 숫자가 작을수록 위험. `bus-factor of one` 이라고도.
- 예문: Only one person can edit the rules — that's a bus-factor of one, so we need a backup admin.

## "worst-case"
- 레지스터: technical
- 출처: repo:adr/0005-metrology-sampling
- 한국어: 최악의 경우(를 기준으로).
- 설명: 평균이 아니라 *가장 나쁜 값* 을 합격 기준으로 삼는다는 뉘앙스. 형용사로 `worst-case gap`, 부사구로 `in the worst case`.
- 예문: We accept the reduction only if the worst-case uniformity gap stays within tolerance.

## "overfit" / "rank-deficient"
- 레지스터: technical
- 출처: repo:adr/0005-metrology-sampling
- 한국어: 과적합 / (행렬이) 계수 부족 — 데이터가 부족해 모델이 우연한 패턴까지 외워버리는 상태.
- 설명: 통계·ML 단골 용어. "데이터가 적으면 rank-deficient 라 overfit 한다" 처럼 원인-결과로 자주 묶임.
- 예문: With fewer than ten wafers the matrix is rank-deficient, so the model overfits.

## "borrow strength"
- 레지스터: technical
- 출처: repo:adr/0005-metrology-sampling
- 한국어: (통계에서) 이웃/유사 그룹의 정보를 빌려 추정력을 보강하다.
- 설명: 표본이 적은 집단을 비슷한 집단과 묶어 추정을 안정화하는 기법을 가리키는 정식 용어 ("borrowing strength").
- 예문: Pooling similar tools lets the model borrow strength across sparse recipes.

## "human-readable"
- 레지스터: technical
- 출처: repo:api-contracts/README
- 한국어: 사람이 읽을 수 있는 (기계용이 아니라).
- 설명: `machine-readable` 의 짝. 식별자/코드 옆에 사람이 이해할 설명을 둘 때 쓰는 표준 표현.
- 예문: Each field needs a short, human-readable description.

## "must implement these contracts identically"
- 레지스터: professional, technical
- 출처: repo:api-contracts/README
- 한국어: 이 계약(스펙)을 *똑같이* 구현해야 한다.
- 설명: 두 구현(mock/실서버)이 한 치도 다르지 않아야 함을 강조. `identically` = "동일하게". 계약/인터페이스 글에서 강한 요구를 표현.
- 예문: Both the mock server and the Flask backend must implement these contracts identically.

## "easier to grant later than to take away"
- 레지스터: professional, conversational
- 출처: repo:adr/0003 (되돌리기 어려운 이유 단락의 논지)
- 한국어: 나중에 *주는* 게 *뺏는* 것보다 쉽다.
- 설명: 권한·기능 설계의 격언. 비가역적 결정을 정당화할 때 쓰기 좋은 대비 구문 (`easier to A than to B`).
- 예문: Lock it down first — it's easier to grant access later than to take it away.
