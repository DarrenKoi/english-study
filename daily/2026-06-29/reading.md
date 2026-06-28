<sub>2026-06-29 · 정독</sub>

## 단락 1

"High scores, but not enough for production" — this tells me the bottleneck isn't the *average* matching score at all. in_topk 0.876 is genuinely high. The gap is **trustworthiness at the operating point**: in production a *wrong* auto-locked align point is worse than abstaining to a human, so what matters is precision-at-act-threshold and a reliable "I'm not sure" gate — not recall@K. Raising the mean score is the *wrong target*. The right targets are the **false-lock rate** — how often we confidently act on a wrong point — and **trustworthy coverage**: how much we can auto-act on while keeping false-locks near zero.

**문법·구조**: 첫 문장은 인용구를 주어 자리에 던지고 대시(`—`)로 "이게 나에게 말해주는 바는…"으로 이어가는 영어 특유의 *부연 연결*이다. 핵심은 `isn't ... at all`(전혀 ~가 아니다)로 통념을 먼저 부정한 뒤, `The gap is X: ...` 콜론으로 X 를 곧바로 풀어 정의하는 흐름. `so what matters is A and B — not C` 는 *대조 구조*로, 대시 뒤 `not C` 가 "C 가 아니라"를 강하게 못 박는다. 마지막 문장의 `how often we ...` / `how much we can ...` 은 명사절(간접의문문)이 **동격(=앞 명사를 풀이)** 으로 쓰인 예 — 추상 명사(false-lock rate, coverage) 바로 뒤에 콜론·대시로 평이한 풀이를 붙여 "전문 용어 → 쉬운 말" 2단으로 읽히게 한다.
**핵심 표현**: `at the operating point`(실제 동작점에서), `abstain to a human`(사람에게 넘기고 자기는 판단 보류), `the wrong target`(엉뚱한 목표를 최적화하고 있었다).
**격식 짝**:
- refined: *What matters is precision at the act threshold, not recall.* (작성)
- plain: *What actually counts is being right when we click, not how often the answer is somewhere in the list.* (작성)

<sub>출처: transcript:auto-recipe-creator [assistant]</sub>

---

## 단락 2

Agreement suppresses distractors only if distractor peaks decorrelate across the recent-success crops while the real align-key structure stays spatially stable. That is a hypothesis, not a property of the data. On the same recipe and tool with a consistent process, every sharp bank member nominates the same wrong lattice point, and the NCC rerank is already weak evidence here. A falsely supported periodic candidate scoring 0.25 with three-member agreement will beat an unsupported true peak at 0.28. If you proceed, require a per-recipe analysis of how often the winning cluster lands on the ground-truth point versus a periodic offset — not just an aggregate recall lift.

**문법·구조**: 회의적 리뷰의 모범. `only if`(오직 ~할 때만)로 주장이 성립하는 *유일 조건*을 먼저 좁히고, 곧장 `That is a hypothesis, not a property of the data.`(이건 가정이지 데이터의 성질이 아니다)로 그 조건이 보장되지 않음을 친다 — `X, not Y` 대조가 또 등장한다. `every sharp bank member nominates ...` 은 현재시제로 *일반적 경향(반복되는 사실)* 을 단정하는 용법. 마지막 `If you proceed, require ...` 는 조건절 + 명령문으로 "그래도 한다면 이건 꼭 해라"는 *건설적 단서(conditional caveat)* 패턴이다. `versus`(=vs.)는 두 대안을 나란히 놓는 격식 연결어.
**핵심 표현**: `decorrelate across (frames)`(프레임마다 서로 어긋나 상관이 깨지다), `nominate the same wrong point`(다 같은 오답을 후보로 내밀다), `weak evidence`(증거력이 약함), `aggregate ... lift`(전체 합산 향상치).
**격식 짝**:
- refined: *That is a hypothesis, not a property of the data.* (원문)
- plain: *We're hoping that's true — but the data doesn't promise it.* (작성)

<sub>출처: transcript:auto-recipe-creator [assistant]</sub>

---

## 단락 3 (모범 단락 · 작성)

The two findings were coupled, so we sequenced the fix rather than chasing the mean score. Our biggest lab win was structurally disconnected from production: the correction path still matched against the stale registered template, so the freshest signal was gathered but thrown away. Meanwhile the abstain gate that would make the scores trustworthy was trapped in the lab, where the production gate stayed binary with no "I'm not sure" branch. Reframing it this way turned a "deep learning or VLM?" either/or into a which-failure-mode question, and the answer became a gated cascade: harden the cache and the decision layer first, and treat the learned-feature and VLM tiers as residual-only, revisited once we can measure the ceiling they would actually move.

**문법·구조**: 오늘 핵심 표현들을 한 흐름에 엮은 모범 단락. `so we sequenced ... rather than chasing ...`은 `rather than + -ing`로 "B 하기보다 A 했다"를 한 문장에 담는 *선택 대조*. `was gathered but thrown away`는 수동태 두 개를 `but`으로 묶어 "모으긴 했는데 버려졌다"는 아이러니를 압축한다. `Meanwhile`은 동시에 벌어진 두 번째 문제로 장면을 전환하는 연결어. `turned A into B` 구문이 관점 전환(reframe)을 동사로 표현하고, 마지막 콜론 뒤 `harden ... first, and treat ...`는 명령형 병렬로 결론(우선순위)을 또렷이 맺는다.
**핵심 표현**: `structurally disconnected from production`, `trapped in the lab`, `a gated cascade`, `an either/or → a which-X question`(양자택일을 어떤-유형 문제로 바꾸기).
**격식 짝**:
- refined: *We sequenced the fix rather than chasing the mean score.* (작성)
- plain: *Instead of trying to push the average up, we fixed things in order.* (작성)

<sub>출처: 모범 단락(작성) — 오늘 표현 종합</sub>
