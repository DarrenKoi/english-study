# 2026-07-07 — 코칭

## 한글→영어

### 카드 1 — 단서와 원인: race 가 지표를 오염시켰다   (내가 쓴 한글)
- 내가 쓴 한글: "직전 결합 패널에서 OM/SEM rcp가 msr과 분간없이 섞여 보인 게 단서였고, 원인은 _localize 가 om·sem rcp template 둘 다 매칭 후 최고 score 채택(race)이라 틀린 modality whitebox 가 이겨 지표를 오염시킨 것."   (출처: transcript:[user] modality 라우팅 리뷰 요청)
- 자연스러운 영어: "The clue was that in the last combined panel, the OM and SEM recipes showed up mixed in with the msr frames, indistinguishable from one another. The root cause: _localize matched both recipe templates and took whichever scored higher — a race — so the wrong modality's whitebox could win and contaminate the metrics."
- 왜 이렇게: "~게 단서였고"는 `The clue was that + 절`로 시작하면 한국어 어순 그대로 살릴 수 있다. "분간없이"는 형용사구 `indistinguishable from one another`를 뒤로 빼는 게 자연스럽다. "원인은 ~것"은 `The root cause:` 콜론 구문이 보고체에 딱 맞고, "(race)" 같은 괄호 명명은 영어에선 대시 삽입 `— a race —`가 관례. "지표를 오염시키다"는 `contaminate the metrics`.

### 카드 2 — 의도대로 제외되는지 (0점 아님)   (내가 쓴 한글)
- 내가 쓴 한글: "skip 된 S행이 _summarize 셀 통계서 제외되는 게 의도대로인지(0점 아님)"   (출처: transcript:[user] modality 라우팅 리뷰 요청)
- 자연스러운 영어: "whether skipped S rows are excluded from the cell statistics in _summarize as intended — excluded, not counted as zeros"
- 왜 이렇게: "의도대로인지"는 `as intended`가 정확한 짝. 괄호 속 "(0점 아님)"의 핵심 대비는 영어에서 `excluded, not counted as zeros`처럼 **X, not Y** 구조로 펼쳐야 명확하다 — "not zero-scored" 한 단어보다 오해가 없다.

### 카드 3 — spec 에 박을 값, 코드 변경 금지   (내가 쓴 한글)
- 내가 쓴 한글: "이제 spec 에 박을 구체 파라미터/수식을 정해줘. 코드 변경 금지, 값+근거만."   (출처: transcript:[user] ensemble 설계 파라미터 요청)
- 자연스러운 영어: "Now pin down the concrete parameters and formulas to bake into the spec. No code changes — just values, each with a one-line rationale."
- 왜 이렇게: "정해줘"는 여기선 확정의 뉘앙스이므로 `pin down`(못 박다). "spec에 박다"는 `bake into the spec`(구워 넣다 — 되돌리기 어렵게 고정)이 개발 관용구. "값+근거만" 같은 전보체는 영어에서도 `No code changes — just values ...`처럼 대시로 끊어 명령의 리듬을 유지한다.

### 카드 4 — 점수면을 뾰족하게   (내가 쓴 한글)
- 내가 쓴 한글: "점수면을 뾰족하게 하는 게 목적."   (출처: transcript:[user] ensemble 설계 파라미터 요청)
- 자연스러운 영어: "The goal is to sharpen the score surface."
- 왜 이렇게: "~하는 게 목적"은 `The goal is to + 동사원형`이 가장 깔끔하다. "뾰족하게 하다"는 CV 문맥에서 `sharpen`(peak 를 날카롭게) 한 단어로 충분하고, 결과 상태를 강조하면 `make the score surface more peaked`.

### 카드 5 — 함정 미리 경고, 간결하게   (내가 쓴 한글)
- 내가 쓴 한글: "함정/실패모드 1~2개 미리 경고. 간결하게."   (출처: transcript:[user] ensemble 설계 파라미터 요청)
- 자연스러운 영어: "Flag one or two pitfalls or failure modes up front. Keep it brief."
- 왜 이렇게: "미리 경고"는 `warn in advance`보다 `flag ... up front`(초장에 표시해 두다)가 리뷰 요청 톤에 맞다. "간결하게" 한 마디는 `Keep it brief.` / `Be concise.` — 부사 하나로 던지는 한국어 명령은 영어에선 짧은 명령문으로 받는다.

### 카드 6 — 미사여구 금지, 문체만 손대라   (내가 쓴 한글)
- 내가 쓴 한글: "과한 문학적 표현·미사여구 추가 금지. 간결함 유지, 문체·리듬·표현만 자연스럽게."   (출처: transcript:[user] 경영진 보고서 윤문 지시)
- 자연스러운 영어: "Don't add flowery language or rhetorical flourishes. Keep it concise — change only the style, rhythm, and wording."
- 왜 이렇게: "미사여구"는 `rhetorical flourishes`, "문학적 표현"은 `flowery language`가 관용 짝. "~만 자연스럽게"의 한정은 `change only the style ...`처럼 **only 를 목적어 앞에** 둬야 "내용은 건드리지 말라"는 제약이 살아난다.

### 카드 7 — RRF k0 선택 근거   (고급 한글 · 번역)
- 한글 원문: "리스트가 top-8~24 수준이면 classic 60은 rank 차이를 과압축해 union voting처럼 변하고, 10이 상위 rank 신호를 보존함."   (출처: transcript:[assistant] 파라미터 권고 답변)
- 자연스러운 영어: "With lists in the top-8-to-24 range, the classic 60 over-compresses rank differences and degenerates into union voting, whereas 10 preserves the signal from the top ranks."
- 번역 포인트: 조건절 "~수준이면"은 `With + 명사구`로 가볍게 처리(if-절보다 문어적). "~처럼 변하고"는 단순 becomes 가 아니라 `degenerates into`(질이 나빠지며 변한다)로 평가를 실어야 원문의 부정적 뉘앙스가 산다. 대조는 `whereas`가 격식 짝.

### 카드 8 — weighted mean 이 가장 일관된 이유   (고급 한글 · 번역)
- 한글 원문: "min은 한 방향만 맞아도 과대평가하고, 단순 sum은 edge 많은 bin이 지배하므로 weighted mean이 기존 Chamfer 평균거리 규약과 가장 일관됨."   (출처: transcript:[assistant] 파라미터 권고 답변)
- 자연스러운 영어: "Min overestimates whenever a single orientation happens to line up, and a plain sum lets edge-heavy bins dominate, so a weighted mean is most consistent with the existing Chamfer mean-distance convention."
- 번역 포인트: "~만 맞아도"의 우연성은 `whenever ... happens to line up`으로 옮긴다(happen to = 어쩌다). "지배하므로"는 사역 `lets ... dominate`가 간결하다. "규약"은 이 문맥에서 rule 이 아니라 `convention`(관례적 약속). 세 절을 and/so 로 묶어 한 문장의 논증 리듬을 유지.

### 카드 9 — tolerance 를 바꾸면 신호가 오염된다   (고급 한글 · 번역)
- 한글 원문: "tolerance를 바꾸면 proposer 개선과 평가 완화가 섞여 A/B 신호가 오염됨."   (출처: transcript:[assistant] 파라미터 권고 답변)
- 자연스러운 영어: "Changing the tolerance would mix genuine proposer improvement with a looser yardstick, contaminating the A/B signal."
- 번역 포인트: 가정의 부작용 경고이므로 `would`. "평가 완화"를 직역(evaluation relaxation)하지 않고 `a looser yardstick`(느슨해진 잣대)이라는 은유 명사로 받으면 영어다워진다. 뒤따르는 결과는 분사구문 `contaminating ...`으로 붙여 인과를 압축.

## 영어 다듬기

### 카드 1 — 전보체 두 조각을 한 문장으로
- 내가 쓴 영어: "Be rigorous on the RRF fusion logic (load-bearing). Proportionate otherwise."   (출처: transcript:[user] Task 4 리뷰 지시)
- 정정: (문법 오류 없음 — 전보식 생략체)
- 더 나은 표현: "Be rigorous on the RRF fusion logic — it's load-bearing — and proportionate everywhere else."
- 왜: 두 번째 조각 "Proportionate otherwise."는 동사가 없어 읽는 쪽이 한 박자 멈춘다. and 로 이어 형용사 두 개(rigorous / proportionate)를 한 동사(Be)에 걸면 대구가 살아난다. 괄호 `(load-bearing)`보다 대시 삽입 `— it's load-bearing —`이 이유 제시로 자연스럽다.

### 카드 2 — 한 단어 질문 "Sane?"
- 내가 쓴 영어: "match_radius: `max(8, int(0.05*short))` where short = min(template h,w). Sane?"   (출처: transcript:[user] Task 4 리뷰 지시)
- 정정: (오류 아님 — 동료 간 구어체로는 통용)
- 더 나은 표현: "Does `max(8, int(0.05*short))` look sane as the match radius, with `short` being the template's shorter side?"
- 왜: "Sane?" 한 단어 질문은 채팅에선 경제적이지만, 리뷰 지시문에선 무엇의 무엇을 판정하라는 건지 모호해진다. `Does X look sane as Y?` 완전 의문문이면 판정 대상과 기준이 문장 안에 고정된다. `look/seem sane` 은 "합리적으로 보이는가"의 관용 짝.

### 카드 3 — 출력 계약은 동사를 살려서
- 내가 쓴 영어: "Real, nameable issues only. If none, []."   (출처: transcript:[user] NCC 버그 탐색 지시)
- 정정: (문법 오류 없음)
- 더 나은 표현: "Report only real, nameable issues; if there are none, return an empty array."
- 왜: 명사구만 나열한 계약은 "누가 무엇을 하라"가 생략돼 있다. 지시문에서는 동사(Report / return)를 살려야 수행 주체와 행동이 명시된다. `[]` 같은 기호도 산문에서는 `an empty array`로 한 번 풀어 주는 쪽이 격식 있다 — 코드블록 안에서라면 `[]` 그대로가 낫다.
