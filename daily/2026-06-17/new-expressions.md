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

---

# 새 표현 (3차 발굴) — `repo:auto_recipe_creator`

> 같은 배치를 다시 훑어 1·2차에서 빠진 표현만 새로 골랐습니다. 스킬 문서(tdd, diagnose,
> improve-codebase-architecture)의 영어가 워낙 알차서 관용구·설계 어휘가 더 나왔어요.
> 이미 notes 에 있는 표현(stress-test, be opinionated 등)은 건너뛰었습니다.

## "outrun your headlights"
- 레지스터: conversational, casual
- 출처: repo:skills/tdd/SKILL
- 한국어: 자기 헤드라이트보다 앞서 달리다 → (앞이 안 보이는데) 분수에 넘게 앞서 나가다.
- 설명: 밤 운전에서 전조등이 비추는 범위보다 빨리 달리면 위험하다는 비유. "아직 이해도 못 한 일을 미리 다 정해버리는" 성급함을 꼬집을 때. 원문: "You outrun your headlights, committing to test structure before understanding the implementation."
- 예문: Writing all the tests up front means you outrun your headlights — you commit before you understand the code.

## "earning its keep"
- 레지스터: conversational, professional
- 출처: repo:skills/improve-codebase-architecture/LANGUAGE (deletion test)
- 한국어: 제 밥값을 하다 / 존재 가치를 증명하다.
- 설명: `keep` = 먹여 살리는 비용. 어떤 모듈/코드가 그 자리를 차지할 만큼 값어치를 하는지 물을 때. 원문: "If complexity reappears across N callers, the module was earning its keep."
- 예문: Delete it in your head — if the complexity scatters across callers, the module was earning its keep.

## "a strong read, not a menu"
- 레지스터: professional, conversational
- 출처: repo:skills/improve-codebase-architecture/INTERFACE-DESIGN
- 한국어: (선택지 나열이 아니라) 분명한 소신 있는 견해를 내라.
- 설명: `a read` = 상황에 대한 판단/해석. `a menu` = 골라 먹으라는 식의 선택지 나열. 추천을 요청받았을 때 "이것저것 늘어놓지 말고 강하게 하나를 밀어라"는 뜻. `be opinionated` 와 짝.
- 예문: When they ask which design wins, give a strong read, not a menu.

## "re-litigate (a decision)"
- 레지스터: professional
- 출처: repo:skills/improve-codebase-architecture/SKILL
- 한국어: (이미 끝난 결정을) 다시 끄집어내 따지다 / 재론하다.
- 설명: 법정의 litigate(소송하다)에서 온 비유. 합의된 결정을 자꾸 처음부터 다시 논쟁하는 것을 막을 때. 원문: "ADRs record decisions the skill should not re-litigate."
- 예문: The ADR exists so we don't re-litigate this every quarter.

## "would take a quarter to swap out"
- 레지스터: professional
- 출처: repo:skills/grill-with-docs/ADR-FORMAT
- 한국어: 갈아치우는 데 한 분기(3개월)는 걸릴 (만큼 무거운).
- 설명: 비즈니스 영어에서 `a quarter` = 회계 분기. `swap out` = 통째로 교체하다. 교체 비용이 큰 핵심 기술을 가리킬 때. 원문: "just the ones that would take a quarter to swap out."
- 예문: We only ADR the choices that would take a quarter to swap out — not every library.

## "the explicit no's are as valuable as the yes's"
- 레지스터: professional
- 출처: repo:skills/grill-with-docs/ADR-FORMAT
- 한국어: "안 한다"는 명시적 결정도 "한다"만큼 값지다.
- 설명: 무엇을 안 하기로 했는지(scope 밖)를 기록하는 게 중요하다는 설계 격언. 범위/경계 결정을 정당화할 때.
- 예문: Document the boundaries — the explicit no's are as valuable as the yes's.

## "deep module / shallow module"
- 레지스터: technical
- 출처: repo:skills/tdd/deep-modules
- 한국어: 깊은 모듈(작은 인터페이스 + 큰 구현) / 얕은 모듈(큰 인터페이스 + 빈약한 구현).
- 설명: Ousterhout 'A Philosophy of Software Design' 용어. **deep** = 적게 노출하고 많이 숨김(좋음), **shallow** = 거의 통과만 하는 껍데기(피함). 설계 리뷰 단골.
- 예문: Hide the complexity behind a small interface — make it a deep module.

## "the interface is the test surface"
- 레지스터: technical
- 출처: repo:skills/improve-codebase-architecture/LANGUAGE
- 한국어: 인터페이스가 곧 테스트 면(테스트가 닿는 지점)이다.
- 설명: 내부 구현이 아니라 공개 인터페이스를 통해 테스트하라는 원칙. `test surface` = 테스트가 맞닿는 표면. 원문: "If you want to test past the interface, the module is the wrong shape."
- 예문: Test through the public API — the interface is the test surface.

## "tracer bullet (vertical slice)"
- 레지스터: technical
- 출처: repo:skills/tdd/SKILL
- 한국어: 예광탄 = 끝에서 끝까지 관통하는 가장 얇은 한 줄기 구현.
- 설명: 군사 예광탄처럼 "경로가 뚫리는지"를 먼저 한 방으로 확인하는 얇은 수직 슬라이스. 반대는 `horizontal slice`(테스트만 잔뜩, 구현은 나중). 원문: "Vertical slices via tracer bullets. One test → one implementation → repeat."
- 예문: Build a tracer bullet first — one test, one impl, prove the path end-to-end.

## "never refactor while RED; get to GREEN first"
- 레지스터: technical
- 출처: repo:skills/tdd/SKILL
- 한국어: 테스트가 빨간불(실패)인 동안엔 리팩터링하지 마라 — 먼저 초록불(통과)을 만들어라.
- 설명: TDD red-green-refactor 규율. 실패 상태에서 구조를 바꾸면 무엇이 깨졌는지 분간 못 하므로 "통과부터, 정리는 나중".
- 예문: Don't clean it up yet — never refactor while RED, get to GREEN first.

## "reads like a specification"
- 레지스터: professional, technical
- 출처: repo:skills/tdd/SKILL
- 한국어: (명세서처럼) 읽힌다 / 읽으면 그대로 사양이 된다.
- 설명: 좋은 테스트/코드가 "무엇을 하는가"를 그 자체로 설명한다는 칭찬. `X reads like Y` = X가 Y처럼 읽힌다(문장 구조에 주목). 원문: "A good test reads like a specification."
- 예문: Name the test for the behavior so it reads like a specification.

## "progressive disclosure"
- 레지스터: technical, professional
- 출처: repo:skills/write-a-skill/SKILL
- 한국어: 점진적 공개 — 필요한 만큼만 먼저 보여주고 상세는 뒤로 미루는 설계.
- 설명: UX/문서 설계 용어. 처음엔 핵심만, 깊은 내용은 링크/하위 파일로 단계적으로 드러냄. 정보 과부하 방지.
- 예문: Keep SKILL.md short and link the details — that's progressive disclosure.

## "hot path"
- 레지스터: technical
- 출처: repo:auto_recipe_creator CLAUDE.md
- 한국어: 핫 패스 = 가장 자주/성능에 민감하게 실행되는 핵심 실행 경로.
- 설명: 루프에서 매번 도는 성능 결정 구간. "NOT in the loop hot path" = 그 무거운 처리는 핵심 경로 밖이라 성능에 안 걸린다는 뜻.
- 예문: Keep logging off the hot path; do it asynchronously.

## "backstop"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator CLAUDE.md ("popup backstop")
- 한국어: 최후방 방어선 / 받쳐주는 안전장치.
- 설명: 야구 포수 뒤 그물(backstop)에서 온 말. 앞의 모든 처리가 실패해도 마지막에 받아주는 보장 장치. 원문: cleanup이 step이 아니라 try/finally로 "guaranteed by a popup backstop".
- 예문: The try/finally is a backstop — even if a step throws, the tool still closes.

## "safety net"
- 레지스터: conversational, professional
- 출처: repo:journals/260603 handoff (안전망)
- 한국어: 안전망.
- 설명: 곡예사 아래 그물. 실패해도 큰 사고를 막아주는 대비책. 원문은 "tail safety net (lean)" vs "load-bearing(정식 구축)" 으로 규모를 대비 — 드물게만 필요하면 가벼운 안전망, 자주 필요하면 핵심 구조.
- 예문: Keep the VLM fallback as a lean safety net, not the main path.

## "before an irreversible action"
- 레지스터: professional, technical
- 출처: repo:project_plan/chatbot_collaboration_strategy (비가역 작업 전 확인 게이트)
- 한국어: 되돌릴 수 없는 작업을 하기 전에.
- 설명: `irreversible` = 비가역의. 저장/실행처럼 무를 수 없는 동작 앞에 사람 확인(human-in-the-loop checkpoint)을 두는 설계 원칙을 말할 때.
- 예문: Require explicit approval before an irreversible action like saving the recipe.
