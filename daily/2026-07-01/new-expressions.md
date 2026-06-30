# 2026-07-01 — 오늘의 표현

오늘 배치는 대부분 코드리뷰 대화(영어)와 한국어 기획 문서였습니다. 코드리뷰 영어에서
**엔지니어링 설계 비평** 표현을 골랐습니다. 기존 레지스터 노트와 텍스트가 정확히 겹치는 것은 건너뛰었습니다.

## "bolted on (as a special case)"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (코드리뷰 — altitude angle)
- 맥락: 설계 리뷰에서 어떤 기능이 기존 구조에 유기적으로 녹아들지 않고 외부에 임시로 덧붙었다고 비판할 때(격식·문어)
- 한국어: (구조에 통합되지 않고) 억지로/땜빵식으로 덧붙이다
- 설명: bolt on = 볼트로 겉에 붙이다 → 비유적으로 아키텍처에 제대로 들어가지 않고 특수 케이스로 부착했다는 부정적 뉘앙스. "is bolted on" 수동태로 자주 씀.
- 예문: The bank arms are bolted on as a free-floating parallel pass rather than registered as a proper arm in the driver.
- 유사어: tacked on (더 가볍고 구어적), grafted on (이식하듯 갖다 붙임), shoehorned in (억지로 끼워 넣음)
- 반의어: baked in / first-class (처음부터 구조에 통합된)

## "a too-shallow fix / a fragile bandaid"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (코드리뷰)
- 맥락: 근본 원인을 안 고치고 증상만 임시로 덮은 해결책을 지적할 때(리뷰·문어)
- 한국어: 너무 얕은(피상적) 수정 / 부서지기 쉬운 임시방편
- 설명: bandaid(반창고) = 임시 처방, fragile = 곧 깨질. "too-shallow"는 문제를 충분히 깊은 곳에서 다루지 못했다(깊이·altitude가 안 맞다)는 리뷰 어휘. "a classic X"로 "전형적인 X"라 비꼴 수 있음.
- 예문: A special-case pass that must be hand-kept-in-sync with another function is a classic too-shallow fix.
- 유사어: a stopgap (임시 땜빵, 중립적), paper over the problem (덮어 가리다), a quick hack (날림 처리)
- 반의어: a proper/deep fix, address it at the root (근본 해결)

## "no collateral damage"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (재리뷰)
- 맥락: 한 수정이 의도한 곳만 바꾸고 무관한 코드·동작엔 부작용이 없음을 확인해 줄 때(리뷰·문어)
- 한국어: 부수적 피해 없음, 곁가지 손상 없음
- 설명: collateral damage = 군사 용어(부수적 피해)에서 온 비유. 변경이 주변을 망가뜨리지 않았다는 뜻. 리뷰 결론에서 "Collateral damage: none." 형태로 자주 단정.
- 예문: Collateral damage: none — the diff touches only the two described lines and leaves the no-data returns untouched.
- 유사어: no side effects (부작용 없음), no regressions (회귀 없음 — 테스트 관점), a self-contained change (자기완결적 변경)
- 반의어: a regression (회귀), an unintended side effect (의도치 않은 부작용)

## "scope creep"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 5 브리프)
- 맥락: 원래 정한 작업 범위를 넘어 일이 슬금슬금 늘어나는 것을 경계하거나, 반대로 "이건 범위 확장이 아니다"라고 변호할 때(프로젝트·문어)
- 한국어: 범위가 야금야금 늘어남, 작업 범위의 무단 확장
- 설명: scope(범위) + creep(슬금슬금 기어듦). 계획에 없던 추가 작업이 끼어드는 현상. 부정문 "not scope creep"으로 "계획이 승인한 변경이라 범위 확장이 아니다"라고 자주 씀.
- 예문: Updating the old assertions to the new format is expected and sanctioned by the plan, not scope creep.
- 유사어: feature creep (기능 비대), gold-plating (불필요한 과잉 완성), mission creep (임무 확대)
- 반의어: stay in scope (범위 안에 머물다), YAGNI (필요한 것만 만든다)

## "a head-to-head (comparison)"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (코드리뷰)
- 맥락: 두 방식을 같은 조건에서 정면으로 맞붙여 비교할 때(회의·문어)
- 한국어: 정면 대결, 일대일 직접 비교
- 설명: head-to-head = 머리를 맞대고 → 직접 맞대결. A/B 비교에서 두 arm을 같은 데이터로 견주는 상황. 형용사·부사 모두로 쓰임("a head-to-head test" / "compare them head-to-head").
- 예문: If the eligible recipe sets diverge, the head-to-head comparison between the two arms becomes invalid.
- 유사어: apples-to-apples (동일 조건임을 강조), side-by-side (나란히 두고 비교), one-to-one
- 반의어: (마땅한 대체 표현 없음)

## "a plausible-but-wrong guess"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 7 브리프)
- 맥락: 모르면서 그럴듯하게 지어내느니 모른다고 정직하게 보고하라고 지시할 때(엔지니어링 문화·문어)
- 한국어: 그럴듯하지만 틀린 추측
- 설명: plausible = (겉보기에) 그럴듯한. 맞아 보여도 사실이 아닌 답을 경계하는 말. "honesty is more valuable than a plausible guess"는 "정직함이 그럴듯한 추측보다 낫다"는 규범 문장으로 통째 외워둘 만함.
- 예문: Do NOT fabricate a parallel data path — this honesty is explicitly more valuable than a plausible guess.
- 유사어: a confident hallucination (자신만만한 환각), a best guess that masquerades as fact (사실인 척하는 추측)
- 반의어: a grounded answer / a verified answer (근거 있는·검증된 답)

## "phantom (zeros / a phantom default)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (코드리뷰 — BUG #3)
- 맥락: 실제로는 존재하지 않는 값을 코드가 기본값으로 만들어내 통계를 왜곡할 때(기술·문어)
- 한국어: 유령 값(실체 없이 만들어진 가짜 값)
- 설명: phantom = 실체 없는 허깨비. `.get(key, 0.0)` 같은 기본값이 데이터 없는 항목에 0을 채워 평균을 끌어내리는 상황을 "phantom zeros"라 부름.
- 예문: The 0.0 default fabricates a consensus rate for recipes that have none, so the digest compares means over different populations — phantom zeros.
- 유사어: a spurious value (거짓·가짜의), a fabricated value (지어낸 값)
- 반의어: (마땅한 대체 표현 없음)

## "swallow an exception / a swallowed exception"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (FINDER 코드리뷰)
- 맥락: 예외를 잡고도 다시 던지거나 로그하지 않고 묻어버려 오류가 숨는 코드를 지적할 때(기술·문어)
- 한국어: 예외를 삼키다(잡고도 조용히 무시하다)
- 설명: try/except로 잡았지만 처리·전파를 안 해 실패가 보이지 않게 됨. 보통 안티패턴. 반대로 "이 예외는 삼켜지지도 않고 그대로 전파된다"처럼도 씀.
- 예문: This ValueError is not caught by the gray-load try/except, so it is not even swallowed — it propagates and aborts the whole run.
- 유사어: silence an error (잠재우다), suppress an exception (억누르다 — 중립적·의도적일 수 있음)
- 반의어: propagate / re-raise (다시 던지다), surface the error (드러내다)

## "a forward reference (resolved at call time)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Task 6 리뷰)
- 맥락: 함수가 자기보다 나중에 정의된 이름을 본문에서 불러도 안전한 이유를 설명할 때(기술·문어)
- 한국어: 전방 참조(나중에 정의되는 이름을 먼저 참조함), 호출 시점에 해석됨
- 설명: Python에서 함수 본문 안의 이름은 def 시점이 아니라 call(호출) 시점에 조회되므로, 뒤에 정의된 함수를 앞 함수가 본문에서 참조해도 NameError가 안 남.
- 예문: A forward reference inside a function body is safe in Python because name lookup happens at call time, not at def time.
- 유사어: late binding (늦은 바인딩 — 더 일반적인 개념)
- 반의어: (마땅한 대체 표현 없음)

## "off-by-one (error)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (FINDER 지침)
- 맥락: 경계 인덱스를 1 차이로 잘못 잡는 흔한 버그를 가리킬 때(기술·구어/문어)
- 한국어: 하나 차이 오류(경계를 1만큼 빗나간 버그)
- 설명: 루프·슬라이스에서 `<` vs `<=`, `len` vs `len-1` 같은 1 차이로 생기는 고전적 버그. 형용사처럼 "an off-by-one bug"로 자주 씀.
- 예문: Read every line and look for inverted conditions, off-by-one errors, and None dereferences.
- 유사어: a boundary bug / an edge-case bug (경계 버그 — 더 넓음), a fencepost error (같은 뜻의 별칭)
- 반의어: (마땅한 대체 표현 없음)

## "a latent bug"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (FINDER — seed_env 분석)
- 맥락: 지금은 안 터지지만 특정 조건에서만 드러날 잠재 결함을 표시할 때(기술·문어)
- 한국어: 잠복 버그, 아직 드러나지 않은 결함
- 설명: latent = 잠재된. 평소엔 숨어 있다가 특정 입력(예: `bool False`를 `str()`하면 `"False"`가 됨)에서만 발현되는 버그. "low risk, but a latent bug" 식으로 위험도를 낮게 평가하며 기록.
- 예문: The example file uses integer 1/0, so this is low risk — but it is a latent bug if a user writes False instead.
- 유사어: a lurking bug (도사린 버그), a dormant defect (휴면 상태의 결함), a time bomb (더 강한 구어)
- 반의어: (마땅한 대체 표현 없음)
