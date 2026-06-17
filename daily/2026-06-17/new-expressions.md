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

---

# 2차 배치 — `repo:auto_recipe_creator` (docs · skills · journals)

> 같은 날 두 번째 배치. 스킬 문서(diagnose/grill-with-docs 등)와 저널·연간 로드맵에서
> 다른 글에도 통하는 자연스러운 영어 위주로 골랐습니다. 프로젝트 고유어(crosshair, recipe, RCS 등)는 제외.

## "anchor on (the first plausible idea)"
- 레지스터: professional, technical
- 출처: repo:skills/diagnose/SKILL
- 한국어: (처음 떠오른 그럴듯한 생각에) 고착되다 / 닻을 내리다.
- 설명: 인지 편향 용어 "anchoring" 의 동사형. 첫 가설에 매여 더 나은 설명을 못 보는 상태를 경고할 때. 원문: "Single-hypothesis generation anchors on the first plausible idea."
- 예문: Don't anchor on the first explanation — list three before you test any.

## "that's a vibe" / "the hypothesis is a vibe"
- 레지스터: casual, technical
- 출처: repo:skills/diagnose/SKILL
- 한국어: (근거 없는) 그냥 느낌·분위기일 뿐이다.
- 설명: 최근 영어권 엔지니어 구어. 검증 가능한 근거가 없는 주장을 가볍게 깎아내릴 때. 원문: "If you cannot state the prediction, the hypothesis is a vibe — discard or sharpen it."
- 예문: "It feels slow" isn't a measurement, that's just a vibe.

## "stress-test (a plan / a design)"
- 레지스터: professional
- 출처: repo:skills/grill-with-docs/SKILL
- 한국어: (계획·설계를) 압박해 시험하다, 한계까지 몰아붙여 검증하다.
- 설명: 원래 금융·공학의 "stress test" 가 일반화된 표현. 아이디어를 일부러 까다로운 시나리오로 두드려 약점을 찾는다는 뜻.
- 예문: Let's stress-test this design with a few edge-case scenarios before we commit.

## "call it out" / "surface it"
- 레지스터: professional, conversational
- 출처: repo:skills/grill-with-docs/SKILL
- 한국어: (문제·모순을) 짚어 말하다 / 겉으로 드러내다.
- 설명: `call out` = 문제를 콕 집어 지적하다, `surface` = 묻혀 있던 것을 수면 위로 올리다(동사). 리뷰·회의에서 매우 자주 씀. 원문: "If you find a contradiction, surface it."
- 예문: If the spec and the code disagree, call it out instead of guessing.

## "why on earth …?"
- 레지스터: casual
- 출처: repo:skills/grill-with-docs/ADR-FORMAT
- 한국어: 도대체 왜 …?
- 설명: 의문문 강조 삽입구 `on earth` (= in the world). 황당함·강한 의문을 담아 "대체 왜"를 표현. 원문: "a future reader will wonder 'why on earth did they do it this way?'"
- 예문: Why on earth is this function called twice on every render?

## "be opinionated"
- 레지스터: professional, conversational
- 출처: repo:skills/grill-with-docs/CONTEXT-FORMAT
- 한국어: 소신 있게 (하나로) 정하라 / 입장을 분명히 하라.
- 설명: 칭찬·지침으로 쓰이는 긍정적 형용사. 여러 선택지를 미적대지 말고 "이게 정답"이라 못 박는 태도. 원문: "Be opinionated. When multiple words exist for the same concept, pick the best one."
- 예문: A good style guide is opinionated — it picks one way and sticks to it.

## "carry lock-in"
- 레지스터: technical
- 출처: repo:skills/grill-with-docs/ADR-FORMAT
- 한국어: (기술 선택이) 종속(락인)을 수반하다.
- 설명: `lock-in` = 한번 도입하면 갈아타기 어려운 종속. `carry` 와 묶여 "그 결정이 락인을 동반한다"는 뜻. 원문: "Technology choices that carry lock-in."
- 예문: Picking a managed database carries real lock-in — migrating later is a quarter of work.

## "load-bearing" (vs. a lean / tail safety net)
- 레지스터: technical, professional
- 출처: repo:journals/260603 handoff (VLM 백업 sizing)
- 한국어: (구조를) 떠받치는 핵심의 / 없으면 무너지는.
- 설명: 건축의 "내력벽(load-bearing wall)" 비유. 코드·계획에서 "이게 빠지면 전체가 무너진다"는 핵심 요소를 가리킴. 반대는 `lean`(군더더기 없는) 또는 `tail safety net`(드문 경우용 안전망). 원문: "Most pass → tail safety net (lean). Many fail → load-bearing (build it properly)."
- 예문: That helper looks trivial, but it's load-bearing — half the pipeline calls it.

## "fail-safe"
- 레지스터: technical
- 출처: repo:journals/260603 white-box-vs-crosshair
- 한국어: 실패해도 안전한 쪽으로 떨어지는 (설계).
- 설명: 오작동·불확실 시 "위험한 추측" 대신 "안전한 거부/폴백"을 택하도록 만든 설계. 원문: "The effect is fail-safe — on a busy background it rejects rather than mis-detects."
- 예문: When the model isn't confident, fail safe: return nothing instead of a wrong coordinate.

## "As-Is / To-Be"
- 레지스터: professional
- 출처: repo:project_plan/2026_annual_roadmap_ppt
- 한국어: 현재 모습(As-Is) / 목표 모습(To-Be).
- 설명: 기획·컨설팅 보고서 단골 짝. 현 상태와 지향 상태를 나란히 대비할 때. 슬라이드 제목으로 자주 등장.
- 예문: Slide 2 shows the As-Is; slide 3 lays out the To-Be we want by year-end.

## "create X lazily — only when needed"
- 레지스터: technical
- 출처: repo:skills/grill-with-docs/SKILL
- 한국어: 필요해질 때 비로소 (게으르게) 생성하라.
- 설명: `lazily` = 미리 만들지 않고 최초 필요 시점까지 미룸(lazy initialization). 디렉토리·파일·객체 생성 지침에 자주. 원문: "Create files lazily — only when you have something to write."
- 예문: Don't pre-create the cache dir; build it lazily on the first write.

## "measure first, fix second"
- 레지스터: professional, technical
- 출처: repo:skills/diagnose/SKILL
- 한국어: 측정이 먼저, 수정은 그 다음.
- 설명: 성능 튜닝 격언. 추측으로 손대기 전에 먼저 재서 병목을 확인하라는 순서 강조 (`A first, B second`). 원문: "Measure first, fix second."
- 예문: Before optimizing the query, measure first, fix second — you might be wrong about the bottleneck.

## "last resort"
- 레지스터: conversational, professional
- 출처: repo:skills/diagnose/SKILL
- 한국어: 최후의 수단.
- 설명: 다른 방법이 다 안 될 때만 쓰는 마지막 카드. 원문에서 사람-개입 루프를 "Last resort" 로 표기. 종종 `as a last resort`.
- 예문: Restarting the server is a last resort, not a fix.
