# Professional register

격식 있는 업무/문서 영어. 보고서, ADR, 설계 결정문에서 쓰기 좋은 표현.

## 2026-06-17
- **single source of truth** — 모두가 참조하는 단 하나의 정본 기준. [→ daily](../../daily/2026-06-17/new-expressions.md)
- **the bridge between X and Y** — 분리된 두 세계를 잇는 다리.
- **document what it actually returns, not what feels canonical** — 이상이 아니라 실제 동작을 문서화하라.
- **conservative default** — 안전한 쪽을 기본값으로 두는 전략.
- **first-class** — 시스템이 정식으로 동등하게 대우하는 대상.
- **must implement these contracts identically** — 스펙을 한 치도 다르지 않게 구현하라.
- **easier to grant later than to take away** — 권한은 주는 게 뺏는 것보다 쉽다.

### auto_recipe_creator 배치
- **anchor on (the first idea)** — 처음 가설에 고착되다.
- **stress-test a plan** — 계획을 까다로운 시나리오로 두드려 약점을 찾다.
- **be opinionated** — 소신 있게 하나로 정하라.
- **measure first, fix second** — 추측으로 손대기 전에 먼저 재라.
- **As-Is / To-Be** — 현재 모습 / 목표 모습 (기획 보고서 단골).
- **load-bearing** — 빠지면 전체가 무너지는 핵심 요소.

### auto_recipe_creator 배치 (추가 발굴)
- **earning its keep** — (모듈·코드가) 제 값어치를 하다.
- **a strong read, not a menu** — 메뉴 나열 말고 소신 있는 추천 하나.
- **re-litigate (a decision)** — 끝난 결정을 다시 끄집어내 따지다.
- **would take a quarter to swap out** — 갈아치우는 데 한 분기는 걸릴 만큼 무거운.
- **the explicit no's are as valuable as the yes's** — "안 한다"는 결정도 그만큼 값지다.
- **reads like a specification** — (테스트·코드가) 명세서처럼 읽힌다.
- **backstop** — 모든 게 실패해도 받쳐주는 최후방 안전장치.
- **before an irreversible action** — 되돌릴 수 없는 작업을 하기 전에 (확인 게이트).

### auto_recipe_creator 배치 (4회차: grill-with-docs)
- **sharpen fuzzy language** — 두루뭉술한 말을 표준 용어로 또렷이 다듬다.
- **call it out** — 모순·문제를 그 자리에서 짚어 말하다 (격식: flag / point out).
- **don't batch these up — capture them as they happen** — 모아뒀다 말고 생기는 즉시 기록하라.
- **offer (something) sparingly** — 아껴서·드물게만 하라 (반대: liberally).
- **as decisions crystallise** — 결정이 또렷이 굳어가는 대로 (문어).

## 2026-06-18 — wiki_for_office 아키텍처/ADR 배치
- **If X, it has failed.** — 목표를 *반대 상황으로* 정의하는 단정형(조건절+현재완료).
  - 예: If the migration makes the on-call engineer's job harder, it has failed, no matter how elegant the internals are.
- **made structurally impossible** — 검사가 아니라 *구조 자체가* 불가능하게 만들다 (≈ safe by construction).
  - 예: Keeping content in a separate repo with no public remote makes a leak structurally impossible, not just unlikely.
- **surfaced, never silently reconciled** — 충돌을 숨겨 봉합하지 말고 *드러내다*.
  - 예: Conflicting facts are surfaced for the human to judge, never silently reconciled into one tidy answer.
- **masquerade as** — ~인 척 위장하다 / ~으로 둔갑하다 (버그가 정상처럼 보일 때).
  - 예: Reading a renamed page by path could fetch the wrong file — a bug that would masquerade as "insufficient evidence".
- **the system's own case law** — 자기 실수에서 쌓은 누적 규칙을 *판례*에 빗댄 비유.
  - 예: Each approved constraint becomes part of the system's own case law — a rule learned from a past mistake and applied automatically thereafter.
- **(the design) converged** — 반복 검토 끝에 더 다툴 게 없는 안정점에 *수렴*하다.
  - 예: After three rounds of adversarial review, the design converged where further scrutiny would need real implementation code to verify.
- **stop earning its keep** — (규칙·모듈이) 더는 제 값어치를 못 하다 → 폐기 판단의 근거.
  - 예: A constraint moves to "retired" when it stops earning its keep — when the failure it guarded against can no longer occur.

## 2026-06-19 — wiki_for_office 아키텍처 개요 + 장기실행 진단 배치
- **the trust boundary is X, not Y** — 신뢰 경계가 어디냐를 한 줄로 못 박는 보안 정의문 (`X, not Y`로 흔한 오해를 먼저 부정).
  - 예: The trust boundary is the company network, not one machine: data may flow to internal services but never to public ones.
- **grounded in (the literature)** — 막연한 직관이 아니라 ~(선행연구·근거)에 단단히 기반을 둔 (수동태로 자주).
  - 예: The wiki layer is grounded in the LLM-Wiki and Retrieval-as-Reasoning literature.
- **deferred deliberately** — 빠뜨린 게 아니라 *일부러* 미룬 결정임을 강조 (스코프 방어).
  - 예: Report drafting was deferred deliberately: it is the least valuable and least testable thing to build first.

## 2026-06-20 — skewnono 하드웨어 mock spec/plan 배치
- **in scope / out of scope** — 이번 라운드에 *할 일 / 안 할 일*의 경계를 못 박는 표준 쌍.
  - 예: The skewvoir button is out of scope this round; the hardware page only needs to read the deep-link params.
- **coexist by design** — 둘이 나란히 있는 게 실수가 아니라 *의도된* 결정(중복 오해 방어). ↔ accidental duplication.
  - 예: The two BSM representations coexist by design; reconciling them is deferred to a future round.
- **honour (a constraint / rule)** — (제약·규칙을) 준수하다(미국식 honor; respect 보다 격식). ↔ violate/break.
  - 예: These are project-wide rules; every task must honour all of them.
- **escape hatch** — 기본 동작을 강제하되 필요시 빠져나갈 수 있게 남겨둔 예외 통로. ↔ hard constraint.
  - 예: We force the ensemble matcher by default, but setting the flag to 0 is an escape hatch for baseline comparison.
- **green-light (something)** — 검토 후 진행해도 좋다고 공식 승인하다(동사). ↔ block/put on hold.
  - 예: The bin-level results green-light porting the box-crop feature to production.
- **abstain** — 확신이 없을 때 행동하지 않고 보류·기권하다(시스템이 사람에게 넘김). ↔ act/commit.
  - 예: When the score is ambiguous, the gate should abstain rather than click the wrong point.
- **the headline ask** — 여러 요청 중 가장 핵심이 되는 요구사항(ask=명사 '요청'). ↔ a nice-to-have.
  - 예: Phase 2 is the headline ask: make the fresh template actually flow into the correction path.
- **fast-follow** — 지금은 범위 밖이지만 출시 직후 곧바로 이어 할 후속 작업. ↔ out of scope.
  - 예: The in-page recipe switcher across those three views is the documented fast-follow.
- **well-established (and sound)** — 이미 학계·업계에서 충분히 정립·검증된. ↔ ad hoc / experimental.
  - 예: The overall pattern is well-established and sound.
- **ad hoc** — 일반 원칙이 아니라 그 경우만을 위한 임시변통의(약간 부정적). ↔ principled / systematic.
  - 예: The best-3-plus-worst weighting is explicitly ad hoc tolerance for one broken side.
- **the main fragility is X** — 결론에서 "가장 큰 취약점은 ~다"라고 한 문장으로 짚는 문형.
  - 예: The main fragility is the outermost-wall selection, which can discard the correct candidate.
- **ordered by severity** — (목록을) 심각도 순으로 정렬했다고 헤더에서 밝힐 때.
  - 예: The concerns below are ordered by severity, with the most damaging one first.
- **drill into / drill down** — 요약·상위 뷰에서 세부 항목으로 파고들다.
  - 예: Show the overlap grid first, then let the user drill into a parameter's attribute matrix.
- **nudge (someone) toward** — 강제하지 않고 슬쩍 어떤 선택으로 유도하다. ↔ force / require.
  - 예: The UI nudges the user toward the distribution view once the count passes a threshold.
- **course-correction(s)** — 진행 중 깨달은 잘못을 바로잡은 방향 수정. 회고·리뷰에서 "왜 바꿨나"를 묶을 때.
  - 예: This section lists the key decisions and course-corrections we made mid-build.
- **baked into (a plan/decision)** — 설계에 이미 박혀 떼어내기 어려운 전제. ↔ configurable.
  - 예: These three assumptions are baked into the plan, so confirm them before executing.
- **redirect here first** — 다른 접근을 원하면 작업 시작 전에 먼저 알려 달라는 협업 신호.
  - 예: If you'd rather the counts live on the main table, redirect here first.
- **a clean surface** — 레거시를 안 건드리고 새 기능에 주는 정돈된 독립 공간. ↔ a cluttered/legacy surface.
  - 예: A new sibling page keeps the legacy view untouched and gives the descriptive view a clean surface.
- **survivorship (bias)** — 실패분을 분모에서 빼 지표가 거짓 상승하는 통계 함정. 고정 분모로 방지.
  - 예: To avoid survivorship, a no-candidate frame counts as a miss instead of being dropped from the denominator.
- **generous (for the ~N target)** — 한도가 실제 필요보다 넉넉한. (수치의 여유) ↔ tight / conservative.
  - 예: The 200-recipe cap is generous for the ~100 target; revisit it only if the office reuses the handler.
- **a request ceiling, not a guarantee** — 요청 상한일 뿐, 그만큼 받는다는 보장이 아니다. ↔ a guaranteed minimum / a floor.
  - 예: `gather_max_events=8` is the request ceiling, not a guarantee — if the recipe has fewer recent successes, you get fewer.
- **diminishing returns** — 수확 체감; 투입을 늘려도 추가 이득이 점점 줄어드는 구간. ↔ a step change.
  - 예: From three to eight images there's no evidence of meaningful gain — likely diminishing returns.
- **in lockstep with** — ~와 한 치 어긋남 없이 발맞춰 같이 움직이는. ↔ drift apart / get out of sync.
  - 예: Use the shared helper so the cond location stays in lockstep with what the reader expects.
- **falsify (an idea) cheaply** — 큰 투자 전에 아이디어를 적은 비용으로 반증하다(실험 우선 사고).
  - 예: This spec is deliberately structured to falsify the idea cheaply before investing in a full eval arm.
- **front-load** — 위험·검증·노력을 일정의 앞단으로 당겨 배치하다. ↔ back-load.
  - 예: The kill-test is front-loaded so we rule out the failure mode before trusting any aggregate lift.
- **rubber-stamp** — 제대로 검증 않고 형식적으로 통과시키다, 거수기 노릇을 하다.
  - 예: The negative-case test proves the harness can detect its own failure mode rather than rubber-stamp the hypothesis.
- **a known class of problem** — (우리만의 일이 아니라) 이미 알려진 부류의 문제다.
  - 예: PaddleOCR-VL hallucinating text on UI screenshots is a known class of problem with VLM-based OCR.
- **the lever is X, not Y** — 진짜 지렛대(핵심 수단)는 Y가 아니라 X다. ↔ a marginal tweak.
  - 예: Record the negative result; the lever is re-registration, not this matcher change.

## 2026-06-26 — auto_recipe_creator re-registration 스펙 배치
- **hit the same wall** — 여러 다른 시도가 결국 *같은 한계*에 부딪히다 (한 번이면 hit a wall). ↔ break through.
  - 예: Three matcher-fusion methods all hit the same wall: they recover the true point but rank it #1 only half the time.
- **the validated next move** — 추측이 아니라 *검증으로 확정된* 다음 수순(전략적 "한 수"). ↔ an untested gamble.
  - 예: Re-registration onto a more distinctive region is the validated next move.
- **de-risk (something) first** — 본격 착수 전 가장 위험한 부분을 *맨 앞 태스크로 먼저 걷어내다*. ↔ leave it to chance.
  - 예: Pin the join key first to de-risk the rest of the implementation.
- **rank them worst-first** — 가장 *나쁜 것부터* 정렬해 우선순위를 매기다. ↔ best-first.
  - 예: The worklist ranks recipes worst-first, so the engineer tackles the most broken keys before anything else.
- **a hard failure signal, not a quiet X** — 조용히 넘기지 말고 *명백한 실패로* 다뤄라 (fail-fast 문어체). ↔ fail silently.
  - 예: A near-zero match rate is a hard failure signal, not a quiet fallback.
- **the one real X (hazard)** — 여럿처럼 보여도 *진짜 위험은 이것 하나*라고 콕 집다. ↔ a minor edge case.
  - 예: Join-key mismatch is the one real implementation hazard here; everything else is mechanical.

## 2026-06-27 — skewnono 설계/plan + document_extraction 배치
- **fall back to (X)** — 정상 경로가 불가능·위험할 때 더 안전한 대안으로 물러나다(설계 근거 문어). ↔ stay on the primary path.
  - 예: When the renderer can't launch Chromium, the stage falls back to HTML so the run never hard-fails.
- **resistant to (X)** — (방법이) 교란 요인에 견고하다고 강점을 못 박을 때. ↔ fragile / sensitive to.
  - 예: The chosen statistic is resistant to outliers, which is exactly why it suits the small MSR selections.
- **surgical (역할·변경)** — 광범위하게 바꾸지 않고 꼭 필요한 곳만 정밀 개입. ↔ sweeping / broad-brush.
  - 예: We keep the change surgical: only the hardware route is touched, and the detection logic stays put.
- **self-hosted** — 데이터 반출 제약 때문에 vendor API 대신 사내 운영 모델을 쓴다고 못 박을 때. ↔ cloud/managed.
  - 예: Data must not leave the network, so every model in the pipeline is self-hosted on-prem.
- **X is what ships** — 이론상 상한이 아니라 실제 의사결정·반영 기준이 무엇인지 한 줄로 정할 때. ↔ a theoretical ceiling.
  - 예: Compare rank-1, not in_topk — in_topk is a ceiling, but rank-1 is what ships.

## 2026-06-28 — skewnono journal + auto_recipe_creator 트랜스크립트 배치
- **escalate to (a second opinion / a human)** — 자체적으로 못 풀 때 상위 단계·다른 주체로 넘기다(폴백 흐름). ↔ handle inline / resolve locally.
  - 예: When the CV matcher flags an ambiguous match, the system escalates to a VLM for a second opinion.
- **X is complementary, not a replacement** — 새 기법을 대체가 아니라 보완으로 자리매김하는 정석 문형(과잉기대 억제). ↔ a drop-in replacement.
  - 예: PixelRAG is complementary, not a replacement: it adds recall but produces no provenance or structured fields.
- **the X axis is exhausted** — 한 방향의 개선 여지를 다 소진했다(→ 레버를 바꿔라). ↔ there's still headroom.
  - 예: All three fusion methods hit the same wall, so the matcher-fusion axis is exhausted — the lever is key distinctiveness.
- **the seam (that X leaves you)** — 앞 작업이 다음 단계에 남긴 깔끔한 이음매·확장 지점(handoff). ↔ a tangled boundary.
  - 예: The seam Phase 1 leaves you is clean: scoring is stable, so Phase 2 only adds the detectors.
- **trade away (X)** — 어떤 이점을 얻는 대가로 ~을 내주다(설계 절충의 동사형). ↔ preserve / retain.
  - 예: A single-vector index stays fast, trading away the patch-level precision of late-interaction models.
- **hit a ceiling (a discriminability ceiling)** — 점수·성능이 더 못 오르는 한계 천장에 부딪히다.
  - 예: You've hit a discriminability ceiling on the matcher itself, so a fourth edge channel won't help.
- **trapped in the lab** — 실험·연구 단계에만 갇혀 정작 운영(프로덕션)으로 못 넘어가다. ↔ shipped / in the loop.
  - 예: The abstain gate that would make the scores trustworthy is trapped in the eval harness.
- **structurally disconnected from (production)** — 우연이 아니라 구조상 ~와 단절되어 있다. ↔ wired into / integrated with.
  - 예: Your single biggest lab win is structurally disconnected from production.
- **ground myself in (X)** — 주장·계획에 앞서 실제 현황·사실에 발을 디디다. ↔ speculate / guess.
  - 예: Let me ground myself in the exact current architecture so my plan reuses your existing structures.
- **pressure-test (a design)** — 설계·계획을 가혹하게 따져 약점을 캐다(= stress-test; 반박을 원할 때). ↔ rubber-stamp.
  - 예: Pressure-test this matching design for flaws — I want an adversarial second opinion, not validation.
- **reframe (the whole thing)** — 문제를 보는 틀 자체를 바꿔 "진짜 목표"를 다시 정의하다. ↔ take at face value.
  - 예: That reframes the whole thing: raising the mean score is the wrong target.
- **make the comparison apples-to-apples** — 같은 잣대로(동일 조건에서) 공정하게 비교하는. ↔ apples-to-oranges.
  - 예: Change the gate to match exactly so the `min_s="3"` bin comparison is apples-to-apples.
- **kept in lock-step** — 두 곳을 늘 함께·동시에 갱신해야 하는(안 그러면 조용히 어긋남). ↔ out of sync.
  - 예: Any new modality key must update both dicts in lock-step, or the two will silently diverge.
- **inert in practice** — 이론상 결함이나 실제 입력에선 결코 안 터지는, 사실상 무해한. ↔ a live defect.
  - 예: A label literally equal to "total" would double-count, but the classifier never emits it, so the bug is inert in practice.
- **a merge blocker** — 병합 전 반드시 고쳐야 할 만큼 중대한 사안. ↔ a nice-to-have.
  - 예: It is a real but minor coverage gap, not a merge blocker.
- **matches the file's house style** — (그 팀·파일의) 고유 관행을 따르는. ↔ an outlier.
  - 예: The new print matches the seven pre-existing Korean warnings — changing it to English would break the file's house style.
- **confirm or overrule** — (상위 검토자가) 하위 판단을 인정하거나 번복하다. ↔ defer / leave undecided.
  - 예: The controller's tentative call is WONTFIX; the senior reviewer can confirm or overrule it.
- **a faithful transcription of the spec** — 명세를 자의적 해석 없이 글자 그대로 옮긴 것. ↔ a loose interpretation.
  - 예: The implementation is a faithful, minimal transcription of the spec — every requirement met, nothing extra.
- **bolted on (as a special case)** — 기존 구조에 녹지 않고 외부에 특수 케이스로 억지로 덧붙이다(부정적). ↔ baked in / first-class.
  - 예: The bank arms are bolted on as a free-floating parallel pass rather than registered as a proper arm.
- **a too-shallow fix / a fragile bandaid** — 근본 원인 대신 증상만 덮은 얕은·임시 수정. ↔ a proper fix at the root.
  - 예: A pass that must be hand-kept-in-sync with another function is a classic too-shallow fix.
- **no collateral damage** — 변경이 의도한 곳만 바꾸고 무관한 코드·동작을 망가뜨리지 않음. ↔ a regression.
  - 예: Collateral damage: none — the diff touches only the two described lines and leaves the no-data returns untouched.
- **scope creep** — 정해진 작업 범위가 야금야금 늘어남. "not scope creep"으로 범위 확장 아님을 변호. ↔ stay in scope / YAGNI.
  - 예: Updating the old assertions is sanctioned by the plan, not scope creep.
- **a head-to-head (comparison)** — 두 방식을 같은 조건에서 정면으로 맞붙여 비교함. ≈ apples-to-apples.
  - 예: If the eligible sets diverge, the head-to-head comparison between the two arms becomes invalid.
- **a plausible-but-wrong guess** — 그럴듯해 보여도 사실이 아닌 추측. ↔ a grounded, verified answer.
  - 예: Do NOT fabricate a data path — this honesty is more valuable than a plausible guess.
