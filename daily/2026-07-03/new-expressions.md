# 2026-07-03 — 새 표현

출처는 하루치 전체가 한 개의 개발 대화 로그입니다(CD-SEM align-key 매칭 실험). 격식 있는 기술 영어가 풍부해 professional/technical 표현 위주로 골랐습니다.

## "office-gated"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator
- 맥락: "이 검증은 (내 Mac이 아니라) 사무실 데이터·환경에서만 가능하다"고 표시할 때 (기술·격식)
- 한국어: (정확도 검증 등이) 사무실 환경에서만 가능하도록 게이트가 걸린.
- 설명: `X-gated` = X라는 관문·조건을 통과해야 진행되는. `feature-gated`, `office-gated`, `login-gated`처럼 생산적으로 조합됩니다. "여기선 못 하고 저기 가야 된다"를 한 단어로.
- 예문: Tasks 1–5 are fully verifiable on Mac, but Task 6's accuracy is office-gated.
- 유사어: environment-dependent (더 일반적·평이), blocked on the office run (구어), gated behind X (일반형)
- 반의어: locally verifiable, Mac-testable

## "a cosmetic fix"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator
- 맥락: 코드 리뷰에서 "겉만 바꾸고 실제 동작은 그대로인 헛수정"을 꼬집을 때 (기술·격식)
- 한국어: 표면만 바꾸고 실질 효과는 없는 수정.
- 설명: cosmetic(화장품 cosmetics)에서 온 비유로 "겉치레의". 버그가 그대로 남아 있는데 고쳤다고 착각하는 상황을 경고합니다.
- 예문: My earlier fix was cosmetic — moving the gate to `< 2` did nothing, because the very next line was the real filter.
- 유사어: superficial (겉핥기의), a band-aid (임시방편), papering over the problem
- 반의어: a root-cause fix, a substantive fix

## "over-promise"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator
- 맥락: 어떤 라벨·기능·문서가 근거보다 더 많은 것을 보장한다고 지적할 때 (격식)
- 한국어: (실제 근거보다) 과하게 약속·보장하다.
- 설명: over- + promise. 흔히 "over-promise and under-deliver"(과대약속하고 실제론 못 미치다) 짝으로 씁니다. 근거가 못 받치는 강한 단정을 경계.
- 예문: The `FRESH_SNAPSHOT` label over-promises: its "region is fine" evidence is the median, but the fix installs a single snapshot.
- 유사어: overstate (격식), oversell (구어)
- 반의어: under-promise, understate

## "manage expectations"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator
- 맥락: 결과가 제한적일 수 있으니 미리 기대치를 낮춰두자고 할 때 (회의·격식 모두)
- 한국어: (미리) 기대치를 조절·관리하다.
- 설명: 상대가 과도하게 기대하지 않도록 현실적 한계를 먼저 알려두는 비즈니스 매너 표현. 뒤에 흔히 `on ...`을 붙여 무엇에 대한 기대인지 명시합니다.
- 예문: Only 28 recipes are E-bearing, so manage expectations on how many `E_CONFIRMED` you can ever get from this set.
- 유사어: set realistic expectations, temper expectations (격식)
- 반의어: overhype, raise expectations

## "with one sharpening"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator
- 맥락: 큰 틀은 동의하되 한 군데만 더 정밀하게 다듬어 말할 때 (격식·토론)
- 한국어: 한 가지만 더 날카롭게(정밀하게) 다듬자면.
- 설명: `sharpen a claim` = 주장을 더 정확·엄밀하게 만들다. "Agree — with one sharpening"은 동의에 미세 보정을 얹는 세련된 화법으로, 상대를 부정하지 않으면서 정밀도를 높입니다.
- 예문: Agree — with one sharpening, because the precise version of the claim matters for what you do next.
- 유사어: with one caveat (단서를 하나 달자면), with one refinement, with one qualification
- 반의어: without reservation, unconditionally

## "no height to fall from"
- 레지스터: conversational, technical
- 출처: transcript:auto-recipe-creator
- 맥락: "이미 낮으니 더 붕괴할(떨어질) 여지가 없다"는 원리를 비유로 짚을 때 (구어적 비유)
- 한국어: 이미 낮아서 떨어질 높이가 없다 → 붕괴를 잴 여지가 없다.
- 설명: 점수 붕괴(collapse)를 측정하려면 높은 기준선이 있어야 하는데 애초에 낮으면 측정 자체가 불가능하다는 직관을 물리적 비유로 전달합니다.
- 예문: A key that's already weak on success frames has no height to fall from, so a collapse signal can never form.
- 유사어: no room to collapse, nothing to lose from that baseline
- 반의어: a tall baseline that craters (높은 기준선이 급락하다)

## "a (non-blocking) loose end"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator
- 맥락: 아직 마무리 안 됐지만 진행을 막지는 않는 잔무를 가리킬 때 (격식)
- 한국어: (진행을 막지 않는) 미결 잔무·마무리 안 된 실마리.
- 설명: loose end = 풀린 실 끝 → 미처리 과제. 동사구 `tie up loose ends`(잔무를 마무리하다)로도 자주 씁니다. non-blocking을 앞에 붙여 "급하진 않다"를 명시.
- 예문: There's one non-blocking loose end from Phase 1: a full uncapped office run to confirm `w_sugg=1` on the whole set.
- 유사어: an open item, an outstanding task, a dangling to-do
- 반의어: a closed item, a resolved thread

## "in structural conflict"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator
- 맥락: 두 설계·요구가 표면 버그가 아니라 근본 구조상 양립 불가함을 진단할 때 (격식)
- 한국어: (근본) 구조적으로 서로 충돌하는.
- 설명: 단순히 "맞지 않는(at odds)"보다 강하게, 설계 전제끼리 어긋나 한쪽을 만족하면 다른 쪽이 반드시 깨지는 상태를 뜻합니다.
- 예문: The two designs are in structural conflict: you can't measure a collapse on keys that never stood up.
- 유사어: fundamentally at odds, mutually incompatible
- 반의어: complementary (상보적), mutually reinforcing

## "starting guesses (uncalibrated)"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator
- 맥락: 아직 실측으로 보정 안 된 초기 임계값을 정직하게 표시할 때 (기술·격식)
- 한국어: (아직 보정 안 된) 초기 추정값.
- 설명: 최종값이 아니라 잠정 출발점임을 밝혀 "이 수치는 바뀔 수 있다"는 정직한 경계선을 긋습니다. 동사 `calibrate`(실측으로 보정하다)와 짝을 이룹니다.
- 예문: The three thresholds shipped as starting guesses, uncalibrated for the real score distribution.
- 유사어: initial estimates, placeholder values, seed values
- 반의어: calibrated values, tuned parameters

## "the vindication of (a thesis)"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator
- 맥락: 실망스러워 보이는 결과가 사실은 기존 가설을 입증해 준다고 재해석할 때 (격식·글)
- 한국어: (어떤 가설·주장의) 정당성 입증·확증.
- 설명: 동사 `vindicate` = (의심받던 것을) 옳았음을 증명하다. 부정적으로 읽힐 결과를 "오히려 우리 논지를 확증한다"로 전환하는 수사적 표현입니다.
- 예문: This isn't a surprise result — it's the vindication of the entire re-registration thesis.
- 유사어: confirmation, corroboration (격식), a proof-out
- 반의어: a refutation, a debunking

## "ride along (as a row)"
- 레지스터: conversational, technical
- 출처: transcript:auto-recipe-creator
- 맥락: 어떤 항목이 별 기여 없이 그저 딸려서 처리될 때 (구어적)
- 한국어: (기여 없이) 그냥 딸려 가다·묻어 가다.
- 설명: ride along = 차에 얹혀 타다 → 능동적 역할 없이 함께 실려 처리됨. 여기선 보정 신호를 못 주면서 목록에 얹혀만 있는 항목을 가리킵니다.
- 예문: An S-only recipe contributes zero calibration signal — it just rides along as a Phase-1 latent-risk row.
- 유사어: tag along, come along for the ride, be carried along
- 반의어: pull its weight, contribute actively
