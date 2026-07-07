# 2026-07-08 — 코칭

## 한글→영어

### 카드 1 — first lever 하나만 골라줘   (내가 쓴 한글)
- 내가 쓴 한글: "가장 적은 구현 비용으로 가장 큰 recall 상승이 기대되는 'first lever' 하나를 골라줘(나는 이걸 먼저 A/B 하고 싶다)."   (출처: transcript:[user] codex 설계 자문)
- 자연스러운 영어: "Pick the single first lever that promises the biggest recall gain for the least implementation cost — I want to A/B this one first."
- 왜 이렇게: "가장 적은 X로 가장 큰 Y"는 영어에서 `the biggest Y for the least X` 한 구문으로 압축됩니다(for가 교환 관계를 표현). "하나를 골라줘"의 "하나"는 one보다 `the single ...`이 "여럿 말고 딱 하나"라는 강제성을 살립니다. promise는 "기대되는"을 사물 주어로 자연스럽게 옮기는 동사입니다.

### 카드 2 — 정직한 A/B 방법   (내가 쓴 한글)
- 내가 쓴 한글: "ensemble 의 gt_in_topk 상승을 golden_localization_eval_cond 위에서 어떻게 A/B 해야 정직한가(proposer recall 만 격리)."   (출처: transcript:[user] codex 설계 자문)
- 자연스러운 영어: "How should I A/B the ensemble's gt_in_topk gain on top of golden_localization_eval_cond so that the comparison stays honest — isolating proposer recall only?"
- 왜 이렇게: "어떻게 ~해야 정직한가"는 `How should I ... so that ... stays honest` — 목적·조건을 so that 절로 뒤에 붙이는 게 영어 어순입니다. honest는 실험 방법론에서 실제로 쓰는 형용사(an honest comparison/benchmark)라 그대로 살릴 수 있습니다. "~만 격리"는 분사구 `isolating X only`로 부가하면 괄호 없이도 자연스럽습니다.

### 카드 3 — 1차 지표 금지   (내가 쓴 한글)
- 내가 쓴 한글: "공정 드리프트로 pixel 동일성(NCC/SSIM) 1차 지표 금지 — 기하/구조 기반만."   (출처: transcript:[user] codex 설계 자문)
- 자연스러운 영어: "Because of process drift, pixel-identity metrics (NCC/SSIM) are off the table as a primary signal — geometry- and structure-based features only."
- 왜 이렇게: "금지"를 forbidden으로 직역하면 규정 문서 냄새가 나는데, 설계 제약을 말할 땐 `off the table`(선택지에서 제외)이 관용적입니다. "1차 지표"는 `as a primary signal`로 자격을 나타내는 as 구문. "기하/구조 기반만"처럼 명사구로 끊는 한국어 스타일은 영어에서도 `X only` 단편문으로 대응 가능해, 제약 나열 문맥에선 완전문보다 오히려 자연스럽습니다.

### 카드 4 — 하드게이트가 정답을 버림   (내가 쓴 한글)
- 내가 쓴 한글: "NCC 가 저-chamfer 정답을 고르면 score 가 낮아 decision='low' → 호출자 하드게이트가 정답 좌표를 버림."   (출처: transcript:[user] codex 설계 리뷰 요청)
- 자연스러운 영어: "When NCC picks a low-chamfer true positive, the score comes out low, the decision lands on 'low', and the caller's hard gate throws away the correct coordinates."
- 왜 이렇게: 한국어의 "→" 인과 사슬은 영어에서 `when ..., A, B, and C` 병렬절로 풀어 씁니다(화살표를 쓰지 않고 동사로 잇기). `come out low`(결과적으로 낮게 나오다), `land on 'low'`(판정이 ~로 떨어지다)는 결과 상태를 나타내는 구동사이고, "버림"은 discard보다 `throw away`가 "아깝게 내다버린다"는 어이없음을 더 잘 전달합니다.

### 카드 5 — 캘리브 선행이 합리적인가   (내가 쓴 한글)
- 내가 쓴 한글: "threshold 캘리브를 구현보다 선행시키는 순서가 합리적인지, 더 단순한 대안."   (출처: transcript:[user] codex 설계 리뷰 요청)
- 자연스러운 영어: "Is it reasonable to sequence the threshold calibration ahead of the implementation, and is there a simpler alternative?"
- 왜 이렇게: "A를 B보다 선행시키다"는 `sequence A ahead of B`(순서를 짜다) 또는 `do A before B`. 명사형으로 끝나는 한국어 질문("~인지, 대안.")은 영어에선 의문문 두 개를 and로 묶는 편이 명확합니다. reasonable 대신 `the right call`을 쓰면 한 단계 구어체로 내려갑니다.

### 카드 6 — 불변 주장 검증   (내가 쓴 한글)
- 내가 쓴 한글: "top_n cap 이 검증된 e2e 0.608 을 바꾸지 않는지(selection 출력 불변 주장 검증) + guard 의미가 정말 개선인지."   (출처: transcript:[user] codex 코드 리뷰 요청)
- 자연스러운 영어: "whether the top_n cap leaves the validated e2e 0.608 untouched (verify the claim that the selection output is unchanged), and whether the guard's semantics are genuinely an improvement."
- 왜 이렇게: "바꾸지 않는지"는 `does not change`보다 `leaves X untouched`가 "검증된 수치를 건드리지 않는다"는 보존 뉘앙스를 정확히 전달합니다. "주장 검증"은 동격 that절 `the claim that ...`로. "정말 개선인지"의 "정말"은 really보다 `genuinely`가 문어에서 격이 맞습니다.

### 카드 7 — 병목은 proposer   (고급 한글 · 번역)
- 한글 원문: "현재 병목은 compute_chamfer_candidates()가 정답 후보를 못 넣는 문제이며, ORB/RANSAC은 candidates[0] 검증에만 붙으므로 first lever로 부적합합니다."   (출처: transcript:[assistant] 설계 자문 답변)
- 자연스러운 영어: "The current bottleneck is that compute_chamfer_candidates() fails to get the true answer into the candidate pool; ORB/RANSAC only attaches to verifying candidates[0], which makes it a poor first lever."
- 번역 포인트: "못 넣는 문제이며"는 `the bottleneck is that ...` 보어절로 — "문제"를 problem으로 또 번역하면 중복(bottleneck이 이미 문제)입니다. "~에만 붙으므로 부적합하다"는 이유절 대신 `which makes it a poor X` 관계절로 결과를 잇는 게 영어답고, "부적합"은 unsuitable보다 `a poor first lever`처럼 형용사+명사가 평가문에서 자연스럽습니다.

### 카드 8 — proposer와 reranker가 섞임   (고급 한글 · 번역)
- 한글 원문: "금지: reranker 점수로 후보 순서를 바꾼 뒤 gt_in_topk 계산 — 그러면 proposer와 reranker가 섞임."   (출처: transcript:[assistant] 설계 자문 답변)
- 자연스러운 영어: "Never reorder the candidates by reranker score before computing gt_in_topk — that conflates the proposer with the reranker."
- 번역 포인트: 명사형 금지 조항("금지: ~계산")은 영어에서 `Never + 동사원형` 명령문이 가장 힘 있습니다. "섞임"은 mix가 아니라 `conflate`(구분해야 할 두 개념을 뒤섞다)가 정확한 학술·리뷰 어휘이고, "그러면"은 that 지시대명사 주어 하나로 처리됩니다.

### 카드 9 — recall@24 진단법   (고급 한글 · 번역)
- 한글 원문: "recall@24가 크게 오르면 proposer 다양성이 부족한 것. recall@24도 낮으면 채널 자체가 틀린 것."   (출처: transcript:[assistant] 설계 자문 답변)
- 자연스러운 영어: "If recall@24 jumps, the proposer lacks diversity; if even recall@24 stays low, the channel itself is wrong."
- 번역 포인트: "크게 오르면"은 rises a lot보다 한 단어 동사 `jumps`가 간결하고, "~도"의 양보는 `even`을 recall@24 앞에 놓아 처리합니다. "~한 것(이다)"라는 한국어 진단 종결은 영어에서 그냥 현재형 평서문 — "it means that..."을 덧붙이면 오히려 장황해집니다. 두 조건의 대구는 세미콜론으로 묶으면 원문의 리듬이 삽니다.

## 영어 다듬기

### 카드 1 — 보고서를 믿지 마라
- 내가 쓴 영어: "Do NOT trust the implementer's report — verify by reading the actual code."   (출처: transcript:[user] 검증 태스크 지시문)
- 더 나은 표현: "Take nothing in the implementer's report on faith — verify every claim against the code itself."
- 왜: 원문도 이미 명확하고 강합니다. 제안문은 `take X on faith`(검증 없이 믿다)라는 관용구로 "무엇을 믿지 말라는지"를 nothing으로 전칭화하고, `verify A against B`(A를 B에 대조해 검증하다)로 검증의 *방법*까지 동사 하나에 실었습니다. every claim은 보고서의 문장 단위 검증이라는 뉘앙스를 추가합니다.

### 카드 2 — 느리면 끝까지 돌려라
- 내가 쓴 영어: "If `uv run pytest poc/workflow_2/` is very slow (ensemble is ~1s/frame and some tests may exercise real ensemble), that's acceptable — let it finish. Report duration if notable."   (출처: transcript:[user] Task 4 지시문)
- 더 나은 표현: "If the full suite runs slow (ensemble costs ~1s/frame, and some tests exercise the real thing), that's expected — let it run to completion, and note the duration if it's unusual."
- 왜: 문법 오류는 없습니다. `is very slow` → `runs slow`(동작 동사)로 문장이 살아나고, acceptable(허용)보다 `expected`(예상된 일)가 "놀라지 마라"는 의도에 더 정확합니다. `let it run to completion`은 let it finish의 한 단계 격식 위 표현이고, `if notable`은 뜻은 통하지만 `if it's unusual`이 완전한 절이라 지시문에서 더 매끄럽습니다.

### 카드 3 — 실재하는 문제만
- 내가 쓴 영어: "Only real, nameable issues. If none, return []."   (출처: transcript:[user] 버그 헌트 지시문)
- 더 나은 표현: "Report only concrete, defensible issues — ones you could name and reproduce. If nothing qualifies, return []."
- 왜: 원문의 단편문 스타일은 지시문에서 유효합니다. 제안문은 동사(Report)를 복원해 지시임을 분명히 하고, real → `concrete`(구체적), nameable → `defensible`(따져 물어도 방어 가능한)로 판정 기준을 한 단계 올렸습니다. `If nothing qualifies`는 If none보다 "기준을 통과한 것이 없으면"이라는 심사 뉘앙스를 살립니다.
