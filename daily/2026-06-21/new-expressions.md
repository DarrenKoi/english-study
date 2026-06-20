# 2026-06-21 — 새 표현

오늘 배치는 거의 전부 한국어 기술 명세였고, 그 안에 박힌 영어 표현 중 학습 가치가 있는 것을 골랐습니다.
(이미 노트에 있는 `backstop`, `source of truth`, `graceful degradation`, `deferred` 는 중복이라 제외 — `defer` 는 spool 답변 참조.)

## "escape hatch"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-11-box-crop-localization-validation-design.md
- 맥락: 기본 동작을 강제하되 "필요하면 빠져나갈 수 있는 예외 통로"를 남겨둘 때(설계 설명·격식~중립).
- 한국어: 비상 탈출구 → 비유적으로 "기본값을 우회할 수 있는 예외 경로".
- 설명: 원래 잠수함·우주선의 비상 탈출구. 코드/정책에서 "평소엔 이렇게 강제하지만, 이 조건이면 빠져나갈 수 있게 열어둔 길"을 뜻합니다.
- 예문: We force the ensemble matcher by default, but setting the flag to 0 is an escape hatch for baseline comparison.
- 유사어: opt-out (선택적 제외; 더 중립), workaround (임시 우회책; 의도된 설계가 아님), safety valve (압력을 빼주는 안전판; 비슷한 비유)
- 반의어: hard constraint / no opt-out (빠져나갈 수 없는 강제)

## "best-effort"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-11-multi-tool-serial-queue-design.md
- 맥락: "되면 좋고 실패해도 전체를 막지 않는" 비보장(non-guaranteed) 작업을 설명할 때(엔지니어링·격식).
- 한국어: 최선을 다하되 보장은 하지 않는 (실패해도 그냥 넘어가는).
- 설명: 형용사로 명사 앞에 붙습니다(best-effort delivery). "성공을 보장하지 않고 시도만 한다"는 계약상·기술상 의미. 네트워크(best-effort delivery)에서 온 표현.
- 예문: Gathering the consensus images is a best-effort step — if it fails, the loop just keeps the existing cache and moves on.
- 유사어: on a best-effort basis (부사구 버전), non-blocking (막지 않는; 동시성 뉘앙스), fire-and-forget (보내고 결과를 안 챙김)
- 반의어: guaranteed / must-succeed (반드시 성공해야 하는), blocking (성공할 때까지 막는)

## "green-light (something)"
- 레지스터: professional, conversational
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-11-box-crop-localization-validation-design.md
- 맥락: 검토·검증 후 "진행해도 좋다"고 공식 승인할 때(회의·업무 구어~중립). 동사로 씁니다.
- 한국어: (프로젝트·다음 단계를) 승인하다, 진행 허가를 내다.
- 설명: 신호등 초록불에서 온 동사. "green-light the project" = 프로젝트에 go 사인을 주다. 명사 "get the green light(승인을 받다)"로도 씁니다.
- 예문: The bin-level results green-light porting the box-crop feature to production.
- 유사어: sign off on (서명·최종 승인; 더 격식), approve (중립·격식), give the go-ahead (승인하다; 회화)
- 반의어: block / veto (막다·거부하다), put on hold (보류하다)

## "a wash"
- 레지스터: conversational, casual
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-11-box-crop-localization-validation-design.md
- 맥락: 두 방안의 득실이 상쇄돼 "결국 차이가 없다"고 말할 때(회의·구어, 약간 비격식).
- 한국어: 비기는 셈, 도긴개긴, 차이 없음(이득과 손해가 상쇄).
- 설명: "It's a wash" = 한쪽 이득이 다른 쪽 손해로 씻겨 나가 순효과가 0. 도박/회계 구어에서 옴. 글보다 말·캐주얼한 메모에서 자주.
- 예문: Even if the aggregate number is a wash, a hidden gain in the far-distance bin could still be there.
- 유사어: a break-even (손익분기; 더 중립), six of one, half a dozen of the other (이러나저러나 똑같음; 관용구), it nets out to zero (상쇄되어 0; 중립)
- 반의어: a clear win (확실한 이득), a net gain / net loss (순이득 / 순손실)

## "abstain (to a human)"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/plans/2026-06-10-production-trust-consensus-cache-and-decision-layer.md
- 맥락: 확신이 없을 때 "행동하지 않고 보류·기권"하기로 결정할 때(설계·격식). 자동 시스템이 "모르겠으니 사람에게 넘긴다"는 맥락.
- 한국어: 기권하다, (행동을) 삼가다 / 보류하다.
- 설명: 보통 투표 맥락("기권하다")이지만, 여기선 시스템이 "틀리게 행동하느니 차라리 행동하지 않는다"는 결정을 가리킵니다. `abstain from -ing` 형태로도. "act / abstain / escalate" 3분기 결정처럼.
- 예문: When the score is ambiguous, the gate should abstain rather than click the wrong point.
- 유사어: hold off (보류; 회화), refrain from (삼가다; 격식), defer to a human (사람에게 넘기다 — 오늘 spool 의 defer 와 연결)
- 반의어: act / commit (행동하다·확정하다), proceed regardless (그래도 진행하다)

## "the headline ask"
- 레지스터: conversational, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/plans/2026-06-10-production-trust-consensus-cache-and-decision-layer.md
- 맥락: 여러 요청 중 "가장 핵심이 되는 요구사항"을 짚을 때(업무 구어~중립). headline=신문 1면 표제어 비유.
- 한국어: 핵심 요구사항, 제일 중요한 요청.
- 설명: "ask" 가 명사로 쓰여 "요청·요구사항"(주로 업무 영어). "headline" 이 형용사처럼 붙어 "가장 눈에 띄는·핵심" 을 뜻. "a big ask(무리한 부탁)" 도 같은 명사 용법.
- 예문: Phase 2 is the headline ask: make the fresh template actually flow into the correction path.
- 유사어: the core requirement (격식), the main deliverable (산출물 강조), the centerpiece (중심축)
- 반의어: a nice-to-have (있으면 좋은 부차적 항목), a side ask (부차적 요청)

## "trade-off curve"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/plans/2026-06-10-production-trust-consensus-cache-and-decision-layer.md
- 맥락: 두 지표가 서로 맞바꿈 관계일 때, 단일 평균값이 아니라 "그 맞바꿈 곡선 전체를 보고하라"고 할 때(데이터·격식).
- 한국어: 상충(맞교환) 곡선 — 하나를 얻으면 다른 하나를 잃는 관계를 그린 곡선.
- 설명: "trade-off" 는 "하나를 얻으려면 다른 하나를 포기"하는 관계(명사). 여기에 curve 를 붙여 "정밀도 vs 재현율"처럼 한 축을 올리면 다른 축이 깎이는 전체 곡선을 가리킵니다.
- 예문: The digest must report the act/abstain trade-off curve, not just a single in_topk number.
- 유사어: trade-off (맞교환 자체), give-and-take (주고받음; 회화), cost-benefit balance (비용-편익 균형)
- 반의어: free lunch / win-win (희생 없는 이득; "there's no free lunch" 로 자주 부정형)

## "ground truth"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-11-matching-improvement-roadmap.md
- 맥락: 모델·알고리즘의 정답을 가늠하는 "검증된 실제 정답값"을 가리킬 때(ML·CV 기술 격식).
- 한국어: (정답으로 쓰는) 실측값, 참값, 정답 레이블.
- 설명: 원래 원격탐사 용어("위성이 본 걸 지상에서 실제 확인한 값"). ML/CV 에서 "모델 출력과 비교하는 진짜 정답". `ground-truth` 로 형용사처럼도 씁니다(ground-truth location).
- 예문: Even when the template is placed exactly at the ground-truth location, the best chamfer peak still drifts 67% of the time.
- 유사어: gold standard (기준이 되는 최상 정답; 더 평가·의료 뉘앙스), reference label (참조 레이블), the actual / true value (참값)
- 반의어: prediction / estimate (모델의 예측·추정값), noisy label (오염된 레이블)
