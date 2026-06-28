# 2026-06-29 — 새 표현

## "hit a ceiling (a discriminability ceiling)"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 성능·점수가 더는 안 오르고 한계에 부딪혔다고 진단할 때(엔지니어링·구어/문어 둘 다).
- 한국어: (성능의) 천장에 부딪히다, 한계에 도달하다.
- 설명: `ceiling` 은 더 못 올라가는 상한선. 무엇의 한계인지를 형용사로 붙여 `discriminability ceiling`(식별력 한계)처럼 구체화한다. `hit/reach/run into a ceiling` 형태로 쓴다.
- 예문: You've hit a discriminability ceiling on the chamfer/NCC matcher itself, so a fourth edge channel won't help.
- 유사어: plateau (점진적으로 정체되다, 더 완만한 뉘앙스), max out (한계까지 다 써버리다·구어), reach the limit (평이)
- 반의어: break through / break the ceiling (한계를 돌파하다)

## "a gated cascade"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 여러 처리 단계를 "조건을 만족할 때만 다음 단계로 넘기는" 구조로 설계할 때(아키텍처 설명·문어).
- 한국어: 게이트(관문)로 걸러 단계적으로 넘기는 캐스케이드 구조.
- 설명: `cascade` 는 단계가 순차로 이어지는 구조, `gated` 는 각 단계 진입에 통과 조건(gate)이 있다는 뜻. 비싼 뒤 단계를 꼭 필요한 경우에만 태우는 설계 패턴.
- 예문: The answer isn't "DL or VLM" — it's a gated cascade where the peak-isolation predictor is the trigger.
- 유사어: a staged pipeline (단계형 파이프라인, 게이트 강조 약함), a tiered/escalation flow (계층적 단계 처리)
- 반의어: a flat / single-pass pipeline (조건 분기 없는 일괄 처리)

## "trapped in the lab"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 실험·연구 단계에서만 잘 되고 정작 운영(프로덕션)에 못 옮겨졌다고 지적할 때(회의·구어, 글에도).
- 한국어: 실험실(랩)에만 갇혀 있다 = 실제 제품에 반영이 안 됨.
- 설명: 비유적 표현. 좋은 성과인데 운영 코드로 못 빠져나왔다는 아쉬움을 생생하게 전한다. `trapped in X` = X 안에 갇혀 못 나옴.
- 예문: The abstain gate that would make scores trustworthy is trapped in the eval harness.
- 유사어: stuck in the lab (구어), never made it to production (서술적), confined to the prototype (격식)
- 반의어: shipped to production / in the loop (실제 동작 경로에 들어가 있음)

## "structurally disconnected from (production)"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 두 부분이 우연이 아니라 구조상 서로 안 이어져 있음을 강조해 진단할 때(설계 리뷰·문어).
- 한국어: 구조적으로 ~와 단절되어 있다.
- 설명: `disconnected from` 에 `structurally` 를 붙이면 "어쩌다 끊긴 게 아니라 설계상 연결 통로 자체가 없다"는 더 무거운 진단이 된다.
- 예문: Your single biggest lab win (+0.442) is structurally disconnected from production.
- 유사어: decoupled from (중립적·의도된 분리일 수도), siloed from (칸막이처럼 격리됨)
- 반의어: wired into / integrated with (배선처럼 연결됨)

## "ground myself in (X)"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 계획·주장을 펴기 전에 "실제 현황·사실에 발을 디디겠다"고 말할 때(격식·문어).
- 한국어: ~에 근거를 두다, ~을 토대로 자리잡다.
- 설명: `ground X in Y` = X 를 Y 라는 사실적 토대 위에 세우다. `ground myself / ground the plan in the architecture` 처럼 추측이 아닌 실증에 기반함을 강조.
- 예문: Let me ground myself in the exact current architecture so my plan reuses your existing structures.
- 유사어: anchor in (닻을 내리듯 고정), base on (평이), root in (뿌리내리다·문어)
- 반의어: speculate / guess (근거 없이 추측하다)

## "a completely different animal"
- 레지스터: casual, conversational
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 겉보기엔 비슷해 보여도 본질이 전혀 다른 것임을 강조할 때(구어·친근한 비유).
- 한국어: 완전히 다른 물건(종류)이다, 차원이 다르다.
- 설명: 관용구. `animal` 은 실제 동물이 아니라 "종류·부류"를 뜻하는 구어 표현. 혼동을 바로잡을 때 즐겨 쓴다.
- 예문: It's a small, specialized vision model that's a completely different animal from your large VLMs.
- 유사어: a whole different beast (더 구어·강조), a different breed (부류가 다름), apples and oranges (비교 불가)
- 반의어: much the same thing / cut from the same cloth (사실상 같은 부류)

## "buy (you) one thing"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 어떤 선택이 (대가는 있지만) 정확히 무엇을 얻게 해주는지 짚을 때(설계 논의·구어/문어).
- 한국어: ~을 (하나) 가져다준다, ~만큼은 벌어준다.
- 설명: `buy` 의 비유적 용법 — 돈이 아니라 "얻는 이득". `X buys you Y` = X 가 Y 를 확보해 준다. 절충을 설명할 때 "이건 이거 하나는 얻게 해준다"로 자주 쓴다.
- 예문: The median wash-out the design avoids actually buys one thing: it blurs periodic detail harder than the true key region.
- 유사어: get you (구어), gain you (얻게 하다), afford (격식·문어)
- 반의어: cost you (대가로 잃게 하다)

## "a negative-control arm"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 실험에서 "효과가 없어야 정상인" 대조군을 둬, 측정된 향상이 진짜인지 검증할 때(실험 설계·문어).
- 한국어: 음성 대조군(아무 효과 없어야 하는 비교 팔).
- 설명: 실험의 `arm` = 비교 갈래/팔. `negative control` 은 효과가 없을 것으로 기대되는 기준선으로, 그 팔이 "향상"을 보이면 측정 자체가 허상임을 드러낸다.
- 예문: Run soft-voting heatmap accumulation as a negative-control arm before crediting the bank mechanism for the lift.
- 유사어: a baseline arm (기준선 팔, 음성성 강조는 약함), a sanity-check control (검증용 대조)
- 반의어: the treatment / experimental arm (실제 처치 팔)

## "pressure-test (a design)"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator [user]
- 맥락: 결정·설계를 일부러 가혹하게 따져 약점을 드러내 달라고 요청할 때(리뷰·격식 있는 구어/문어).
- 한국어: (설계·계획을) 압박해 가며 검증하다, 약점을 캐다.
- 설명: `stress-test`(이미 수집함)와 거의 같은 뜻이되 `pressure-test` 는 "압력을 가해 무너지나 본다"는 결정·논증 검증에 특히 자주 쓰인다. 검증(validation)이 아니라 반박을 원한다는 톤.
- 예문: Pressure-test this matching design for flaws and missing considerations — I want an adversarial second opinion, not validation.
- 유사어: stress-test (사실상 동의어), poke holes in (구어·허점을 찾다), red-team (적의 입장에서 공격하듯 검증)
- 반의어: rubber-stamp (따지지 않고 통과시키다)

## "reframe (the whole thing)"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 문제를 보는 틀 자체를 바꿔 "진짜 풀어야 할 것"을 다시 정의할 때(전략 논의·문어/구어).
- 한국어: (문제·논의를) 다시 틀 잡다, 관점을 재정의하다.
- 설명: `frame` = 틀. `reframe` 은 같은 사실을 다른 프레임으로 다시 봄. 종종 "그래서 ~가 잘못된 목표였다"는 통찰로 이어진다.
- 예문: That reframes the whole thing: raising the mean score is the wrong target.
- 유사어: recast (다시 주조하듯 재정의·문어), reframe as (~로 바꿔 보다), look at it differently (평이·구어)
- 반의어: take at face value (있는 그대로 받아들이다)

## "circular (by construction)"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 어떤 지표·논증이 "전제가 곧 결론"이라 아무것도 입증 못 한다고 비판할 때(분석·격식).
- 한국어: 순환 논리다, 구조상 자기 결론을 되먹임한다.
- 설명: `circular` = 순환적(전제가 결론을 가정함). `by construction` 은 "설계상 필연적으로 그렇다"는 뜻으로, 순환성이 우연이 아님을 못 박는다.
- 예문: Reporting support on the selected winner is circular: the mechanism selects supported clusters, then the diagnostic observes support.
- 유사어: question-begging (논점 선취·문어), self-fulfilling (자기 충족적), tautological (동어 반복)
- 반의어: an independent check (독립적 검증)

## "the operating point"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator [assistant]
- 맥락: 모델·시스템이 실제로 작동하는 임계값/동작 지점을 두고 성능을 논할 때(ML·신호처리·문어).
- 한국어: (실제) 동작점, 운용 임계점.
- 설명: 평균 성능이 아니라 "실제로 행동을 결정하는 그 지점"에서의 신뢰도를 가리킨다. `trustworthiness at the operating point` = 그 동작점에서 믿을 만한가.
- 예문: The gap is trustworthiness at the operating point, not the average matching score.
- 유사어: the decision threshold (결정 임계값), the act threshold (행동 임계점)
- 반의어: aggregate / average performance (전체 평균 성능)
