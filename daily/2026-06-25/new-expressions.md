# 2026-06-25 — 새 표현

## "falsify (an idea) cheaply"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-24-template-bank-matching-design.md
- 맥락: 큰 투자 전에 가설을 싸게 반증할 수 있게 실험을 설계했다고 밝힐 때(연구·실험 설계 글, 격식)
- 한국어: (아이디어를) 적은 비용으로 반증하다/틀렸음을 빨리 가려내다.
- 설명: 과학철학의 `falsify`(반증)를 엔지니어링에 가져온 표현. "비싸게 다 만들기 전에, 틀렸으면 싸게 죽이자"는 실험 우선 사고를 한마디로 담는다.
- 예문: This spec is deliberately structured to falsify the idea cheaply before investing in a full eval arm.
- 유사어: kill (an idea) early (조기에 폐기, 회화·구어), de-risk cheaply (리스크를 싸게 걷어내다), a cheap kill-test (싼 판별 실험)
- 반의어: over-invest before validating (검증 전에 과투자하다)

## "front-load"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-24-template-bank-matching-design.md
- 맥락: 위험·검증·노력을 일정의 앞쪽으로 당겨 배치한다고 할 때(계획·일정·리스크 관리, 격식)
- 한국어: (작업·위험을) 앞단으로 당겨 배치하다, 초반에 몰아 처리하다.
- 설명: 동사로 "앞에 무게를 싣다". 가장 위험한 판단을 먼저 끝내 나중에 헛수고를 막는다는 의미. 반대 개념은 `back-load`(뒤로 미룸).
- 예문: The kill-test is front-loaded so we rule out the failure mode before trusting any aggregate lift.
- 유사어: tackle up front (먼저 처리하다, 회화), prioritize early, do the risky part first
- 반의어: back-load (뒤로 미루다), defer to the end

## "rubber-stamp"
- 레지스터: professional, conversational
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-24-template-bank-matching-design.md
- 맥락: 제대로 검증 안 하고 형식적으로 승인·통과시키는 것을 비판할 때(리뷰·승인 절차, 약간 부정적)
- 한국어: 형식적으로 도장만 찍어 통과시키다, 거수기 노릇을 하다.
- 설명: "고무도장을 찍듯" 검토 없이 자동 승인한다는 비유. 테스트·리뷰가 실패를 못 잡고 무조건 OK 내는 상황을 꼬집는다.
- 예문: The negative-case test proves the harness can detect its own failure mode rather than rubber-stamp the hypothesis.
- 유사어: wave through (그냥 통과시키다, 회화), sign off without scrutiny, give it a pass
- 반의어: scrutinize (꼼꼼히 따지다), push back on (이의를 제기하다)

## "manufacture lift"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-24-template-bank-matching-design.md
- 맥락: 자유 파라미터를 만지작거려 "성능 향상을 인위적으로 지어낸다"고 경계할 때(실험·통계 엄밀성 논의)
- 한국어: (튜닝 여지로) 성능 개선을 인위적으로 만들어내다/조작하다.
- 설명: `lift`는 기준 대비 개선폭. 노브가 많을수록 데이터에 끼워맞춰 가짜 개선을 "제조"할 수 있다는 경고. `manufacture`(없는 걸 만들어내다)의 부정적 용법.
- 예문: Fewer free parameters means less room to manufacture lift, so a gain is more likely real.
- 유사어: cherry-pick results (유리한 것만 고르다), overfit to the benchmark (벤치에 과적합), game the metric (지표를 농간하다)
- 반의어: a genuine/attributable gain (진짜·귀속 가능한 개선)

## "X proposes, Y disposes"
- 레지스터: technical, professional
- 출처: transcript:[assistant] 07b2cb20 (outline_live_sem_box 설명)
- 맥락: 두 단계의 역할 분담을 한 줄로 못박을 때 — 한쪽이 후보를 제안하고 다른 쪽이 최종 결정한다(설계 원칙 서술)
- 한국어: A는 제안하고, B가 (최종) 결정한다.
- 설명: 속담 "Man proposes, God disposes"(일은 사람이 꾸미고 이루는 건 하늘)를 비튼 패턴. 여기선 "VLM proposes, CV disposes" — VLM이 대략 영역을 제안, CV가 정확한 좌표를 확정. 역할 경계를 기억하기 좋게 만든다.
- 예문: The two stages follow one rule: the VLM proposes the region, and the CV disposes by locking onto the exact border pixels.
- 유사어: division of labor (역할 분담), A suggests, B decides, propose-then-verify (제안 후 검증)
- 반의어: one stage does everything (한 단계가 다 처리), end-to-end (통짜 처리)

## "a known class of problem"
- 레지스터: professional, technical
- 출처: transcript:[assistant] 22bf3627 (PaddleOCR 환각 진단)
- 맥락: 특정 버그가 우리만 겪는 게 아니라 "이미 알려진 유형"임을 짚어 안심·맥락을 줄 때(진단·설명, 중립)
- 한국어: (이미) 알려진 부류의 문제다, 흔히 보고되는 유형의 이슈다.
- 설명: `class of problem`은 개별 사례가 아니라 "문제의 종류". 새 버그처럼 보여도 well-documented한 패턴임을 알려 대응 방향을 잡아준다.
- 예문: PaddleOCR-VL hallucinating text on UI screenshots is a known class of problem with VLM-based OCR.
- 유사어: a well-documented failure mode (잘 알려진 실패 양상), a familiar pitfall, not a new problem
- 반의어: a novel/unseen failure (처음 보는 실패), an isolated incident (단발성 사례)

## "the lever is X, not Y"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/weekly_report/2026-06-24/weekly_report.md
- 맥락: 여러 선택지 중 "진짜 효과를 내는 핵심 수단"이 무엇인지 결론지을 때(전략·우선순위 결정, 격식)
- 한국어: 진짜 지렛대(핵심 수단)는 Y가 아니라 X다.
- 설명: `lever`(지렛대)는 작은 힘으로 큰 변화를 내는 핵심 변수. "어디를 눌러야 결과가 움직이나"를 비유. `the real lever`, `the right lever` 형태로도 자주.
- 예문: Record the negative result; the lever is re-registration, not this matcher change.
- 유사어: the real driver (실제 동인), what actually moves the needle (실제로 바늘을 움직이는 것), the high-leverage change
- 반의어: a marginal tweak (미미한 손질), a red herring (헛다리)

