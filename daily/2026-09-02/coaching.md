# 2026-09-02 — 코칭

## 한글→영어

### 카드 1 — align_fail_monitor 버그 리포트   (내가 쓴 한글)
- 내가 쓴 한글: "@poc/workflow_3/monitor/align_fail_monitor.py 중에 발견한 문제점. align fail 상태에서 장비 모니터에 접속 후 consensus가 없거나, 등록된 recipe로 위치를 잡을 수 없을 때 다른 조치를 취하지 않고 hold 상태로 그대로 있음."   (출처: transcript:[user] auto-recipe-creator 5603304e)
- 자연스러운 영어: A problem I found in `align_fail_monitor.py`: when it connects to the equipment monitor in an align-fail state and either has no consensus or can't locate the registered recipe, it doesn't take any further action — it just stays in hold.
- 왜 이렇게: "발견한 문제점"으로 시작하는 한국어 개조식 보고는 영어에서 콜론 뒤에 본문을 잇는 한 문장으로 묶는 게 자연스럽다(`A problem I found in X: ...`). "다른 조치를 취하지 않고"는 부정 동사를 나열하는 대신 `it doesn't take any further action — it just stays in hold`처럼 대시로 결과를 덧붙이면 원인·결과가 또렷해진다. "그대로 있음"의 '그대로'는 `just stays`의 `just`가 담당한다.

### 카드 2 — 팝업 위치 정정   (내가 쓴 한글)
- 내가 쓴 한글: "장비 모니터 상 가운데 RCS popup windows로 뜸."   (출처: transcript:[user] auto-recipe-creator 5603304e)
- 자연스러운 영어: The RCS popup shows up inside the equipment monitor view, not as a separate window.
- 왜 이렇게: 원문은 명사구만 나열한 메모체지만, 상대가 "로컬 top-level 창"으로 잘못 가정하고 있었기 때문에 이 정정의 핵심은 위치 대비다. `not as a separate window`를 덧붙이면 무엇을 바로잡는지 대화 맥락에서 분명해진다 — 원문에 없는 정보지만 뜻을 살리려면 반드시 필요하다. "~로 뜸"의 '뜨다'는 팝업이 나타나는 동작이라 `shows up`이 정확하다.

### 카드 3 — v2→v3 서비스 대수 확장 안내문   (내가 쓴 한글)
- 내가 쓴 한글: "기존 v2는 약 270대만 상대했으나, v3는 HV-SEM 67대 추가, CD-SEM까지 포함 약 400여대를 서비스할 수 있게 되었습니다."   (출처: transcript:[user] skewnono-v3-nuxt 558d3b8a, 사내 공지 초안)
- 자연스러운 영어: Where v2 covered only about 270 units, v3 now serves roughly 400 — adding 67 HV-SEM units and extending coverage to CD-SEM as well.
- 왜 이렇게: "~했으나"의 역접은 `Where X, Y now`처럼 `where`를 대조 부사절로 쓰면 공지문 특유의 정중한 대비가 산다(`while`보다 격식체에 더 어울린다). "서비스할 수 있게 되었습니다"의 완곡한 피동은 영어에서 단순 현재형 `now serves`로 충분하다 — 영어 공지문은 "할 수 있게 된" 과정을 굳이 드러내지 않는다. 증설 요인 두 가지는 분사구 `adding ~ and extending ~`으로 뒤에 붙여 본문 흐름을 끊지 않는다.

### 카드 4 — CD-SEM 대수 확인 답변   (내가 쓴 한글)
- 내가 쓴 한글: "CD-SEM 대수가 늘어난 게 맞으니 그대로 두세요"   (출처: transcript:[user] skewnono-v3-nuxt 558d3b8a)
- 자연스러운 영어: That's right, the CD-SEM count did go up — leave the wording as is.
- 왜 이렇게: 상대가 숫자 불일치(270+67=337≠400)를 지적하며 확인을 요청한 데 대한 답이므로, 단순 서술이 아니라 "네 맞습니다"라는 확인부터 와야 한다. 조동사 강조형 `did go up`을 쓰면 "정말 그게 맞다"는 확인의 힘이 산다. "그대로 두세요"는 문서 수정 지시라 `leave it as is`가 관용구로 굳어 있다.

### 카드 5 — announcement 기능 추가 요청   (내가 쓴 한글)
- 내가 쓴 한글: "announcement에 실험실에 새로운 기능들이 추가되었으니 많은 이용 바랍니다. 넣어줘."   (출처: transcript:[user] skewnono-v3-nuxt 428e8d25)
- 자연스러운 영어: Add a line to the announcement saying new features have been added to the Lab, and inviting people to try them out.
- 왜 이렇게: "많은 이용 바랍니다"는 한국 사내 공지 특유의 정중한 청유형이라 직역(`please use it a lot`)하면 어색하다. 영어 공지는 동명사구 `inviting people to try them out`으로 같은 기능(사용 권장)을 수행한다. "넣어줘"라는 실제 지시 동사는 `add`로 앞에 내세우고, 담을 문구는 `saying ~`으로 목적어절 처리한다.

### 카드 6 — 반출 금지 고지문 두 건   (내가 쓴 한글)
- 내가 쓴 한글: "Recipe 정보 사외 반출 시 반드시 MI팀과 협의를 거쳐서 진행되어야 합니다." / "스큐노노에서 볼 수 있는 모든 데이터는 사외 반출을 엄격히 금지합니다."   (출처: transcript:[user] skewnono-v3-nuxt 5a311ce2)
- 자연스러운 영어: Any external transfer of recipe information must go through MI team approval first. / Exporting any data visible in SKEWNONO outside the company is strictly prohibited.
- 왜 이렇게: 두 고지문 모두 사규 안내문 특유의 강한 의무형("반드시 ~해야 합니다")이라 `must` 하나로 그 힘을 그대로 옮긴다. 첫 문장은 "협의를 거쳐서 진행되어야"라는 두 동사를 `must go through MI team approval first`로 압축하는 게 영어 고지문의 관례다. 둘째 문장의 "엄격히 금지합니다"는 수동태 `is strictly prohibited`가 표준 고지 문구다 — 능동 명령형(`Do not export`)보다 공식 게시문 톤에 맞는다.

### 카드 7 — 사본과 상수 블록의 우선순위 다툼   (고급 한글 · 번역)
- 한글 원문: "사본은 조용히 이기거나 조용히 지지만, 상수 블록은 자기가 진 것을 콘솔에 남깁니다."   (출처: transcript:[assistant] auto-recipe-creator b8c35a47, 설정 우선순위 디버깅)
- 자연스러운 영어: The copy wins quietly or loses quietly, but the constants block logs it when it loses.
- 번역 포인트: "이기거나 지지만"의 대구를 영어도 `wins ... or loses ...`로 그대로 살려야 원문의 리듬이 산다. "자기가 진 것을 콘솔에 남깁니다"는 주어를 사람이 아니라 설정 블록 자체로 두는 의인화 표현이라, `logs it when it loses`처럼 주체를 그대로 `the constants block`에 두고 결과절을 붙인다 — `admits defeat` 같은 과한 의인화 번역은 원문보다 무거워진다.

### 카드 8 — 도착 게이트와 hold 해제는 별개다   (고급 한글 · 번역)
- 한글 원문: "장비 hold 해제와 루프 재시도는 별개 문제다. 재시도만 고쳐도 장비는 계속 hold 고, 대화상자를 눌러도 자산이 없으면 다음에 또 같은 곳에서 멈춘다."   (출처: transcript:[assistant] auto-recipe-creator 5603304e)
- 자연스러운 영어: Releasing the equipment from hold and fixing the retry loop are two separate problems. Fix only the retry and the equipment stays on hold; click through the dialog and, without the assets, it stalls at the same place next time.
- 번역 포인트: "별개 문제다"라는 짧은 단언은 영어에서도 `are two separate problems`로 짧게 두는 편이 원문의 단호함을 살린다. 뒤 두 절은 조건문처럼 읽히지만 한국어 원문에 `-면`이 없으므로, 영어도 `If`를 넣지 않고 명령형에 가까운 `Fix only the retry and X`(그리고 X 하다) 구문으로 옮기면 같은 건조한 어조가 유지된다.

### 카드 9 — 검출 경로 교체는 협력자 교체다   (고급 한글 · 번역)
- 한글 원문: "검출 경로를 바꾸면서 access_request.py 는 한 줄도 안 건드렸습니다... '창 제목으로 찾기'를 '프레임 변화로 찾기'로 갈아끼우는 게 협력자 교체 하나입니다."   (출처: transcript:[assistant] auto-recipe-creator 5603304e)
- 자연스러운 영어: I changed the detection path without touching `access_request.py` at all — swapping "find by window title" for "find by frame change" is just a single collaborator swap.
- 번역 포인트: "협력자 교체"는 디자인 패턴 용어(하나의 의존성을 같은 인터페이스의 다른 구현으로 갈아 끼우는 것)를 그대로 영어로 옮긴 것이라 `collaborator swap`이 정확한 대응어다. "갈아끼우는 게 ~하나입니다"의 서술적 결론은 `is just a single X`처럼 `just`로 규모를 축소해, 큰 변경처럼 보이는 일이 실은 국소적임을 강조한다.

### 카드 10 — lenient 의 의미가 뒤집히는 지점   (고급 한글 · 번역)
- 한글 원문: "도착 판정에서 status 를 쓰면 안 되는 게 미묘한 지점이었습니다... 클릭 경로의 lenient 는 '누를 대상은 있는데 글자를 못 읽었다'는 뜻인데, 여기서는 대상 존재 자체가 질문이라 의미가 뒤집힙니다."   (출처: transcript:[assistant] auto-recipe-creator 5603304e)
- 자연스러운 영어: The subtle point was that arrival detection can't rely on `status`. In the click path, "lenient" means "the target exists but its text couldn't be read" — here, existence itself is the question, so the meaning flips.
- 번역 포인트: "미묘한 지점이었습니다"는 `was subtle`이 아니라 `The subtle point was that ~`처럼 명사구를 주어로 세워야 "무엇이 미묘했는지"가 바로 이어진다. "의미가 뒤집힙니다"의 '뒤집히다'는 단순 반전이라 `is reversed`보다 `flips`가 구어에 가까운 만큼 더 생생하다 — 원문 자체가 설명문이지만 결론부는 구어체로 끝나는 리듬이라 어울린다.

## 영어 다듬기

### 카드 11 — 타임스탬프 UTC 확인 질문
- 내가 쓴 영어: "I found that @timestamp stored with UTC time with zero. Not Korean time. can you check it?"   (출처: transcript:[user] skewnono-v3-nuxt 4feef4b1)
- 정정: `stored with UTC time with zero` → `stored in UTC with a zero offset`. 시간대에 "저장된다"고 할 때는 `stored with`가 아니라 `stored in`을 쓴다. `with zero`는 무엇이 0인지 불분명해 `a zero offset`으로 채워야 한다. `Not Korean time.`은 마침표로 끊긴 조각 문장이라 앞 문장에 이어야 한다.
- 더 나은 표현: I found that `@timestamp` is stored in UTC with a zero offset, not in Korean time — can you check that?
- 왜: 대시로 이으면 "정정 요청"이라는 원래 의도가 한 호흡에 전달된다. `can you check it?`의 `it`도 무엇을 확인해 달라는지 모호해 `check that`으로 앞 진술 전체를 받게 하는 편이 명확하다.

### 카드 12 — 채팅 타임아웃 증가 요청
- 내가 쓴 영어: "we have to increase timeout for the chat. some takes too long to get the response"   (출처: transcript:[user] skewnono-v3-nuxt 5a311ce2)
- 정정: `some takes` → `some take`. "some"이 가리키는 대상(응답들)이 복수이므로 동사도 원형 `take`가 맞는다.
- 더 나은 표현: We need to increase the chat timeout — some responses take too long to come back.
- 왜: `we have to`는 의무를 강하게 못 박는 표현이라 요청·제안 톤에는 `we need to`가 더 자연스럽다. `get the response`도 관사 없이 막연해 `come back`(응답이 돌아오다)으로 바꾸면 주어(some responses)와 자연스럽게 이어진다.

### 카드 13 — 반출 금지 고지문 삽입 지시
- 내가 쓴 영어: "in recipe-search page, we have to add the comment like Recipe 정보 사외 반출 시 반드시 MI팀과 협의를 거쳐서 진행되어야 합니다. Also in the landing page, we have to add a mark like 스큐노노에서 볼 수 있는 모든 데이터는 사외 반출을 엄격히 금지합니다. check the spelling and grammar of Korean and display them."   (출처: transcript:[user] skewnono-v3-nuxt 5a311ce2)
- 정정: 문법 오류는 없음.
- 더 나은 표현: On the recipe-search page, add a notice along the lines of "..." — and on the landing page, add one saying "...". Please check the Korean for spelling and grammar before you place them.
- 왜: `the comment`는 소스코드 주석을 먼저 연상시키므로 화면에 노출되는 안내문에는 `a notice`가 더 정확하고, 뒤 문장의 `a mark`도 같은 이유로 `notice`로 통일하는 편이 낫다. "검토하고 게시하라"는 두 동작의 순서가 원문에서는 불분명한데, `before you place them`으로 순서를 명시하면 지시가 또렷해진다.

### 카드 14 — 반출 금지 고지문 삭제 지시
- 내가 쓴 영어: "remove the recipe 정보 사외 반출 시 반드시 MI팀과 협의를 거쳐야 합니다. from the recipe-search."   (출처: transcript:[user] skewnono-v3-nuxt 5a311ce2)
- 정정: 지울 대상(한글 문구)과 지시 동사 사이에 구두점이 없어 문장이 어디서 끊기는지 불분명하다. 인용부호나 괄호로 경계를 표시해야 한다.
- 더 나은 표현: Remove the notice ("Recipe 정보 사외 반출 시 반드시 MI팀과 협의를 거쳐야 합니다.") from the recipe-search page.
- 왜: 인용 경계를 표시하면 "무엇을 지우라는 건지"가 코드 리뷰에서도 오해 없이 전달된다. `the recipe-search`도 페이지를 가리키므로 `the recipe-search page`로 명사를 채워야 완전한 문장이 된다.

### 카드 15 — figures.py 정규식 수정 지시
- 내가 쓴 영어: "For the chat page (you are the chat agent). fix the figures.py. Change the regex to allow Hangul + spaces while maintaining the existing path-traversal protections. fix the docstring too. the stem is an arbitrary filename. so spaces/korean are the norm."   (출처: transcript:[user] skewnono-v3-nuxt c872b54e)
- 정정: 마침표로 문장을 잘게 끊어 놓고도 다음 문장을 소문자로 시작해(`fix the docstring too.`, `the stem is...`) 새 문장인지 이어지는 구절인지 불분명하다.
- 더 나은 표현: For the chat page — you're acting as the chat agent — fix `figures.py`: change the regex to allow Hangul and spaces while keeping the existing path-traversal protections, and fix the docstring too. The stem is an arbitrary filename, so spaces and Korean characters are the norm.
- 왜: 관련된 두 지시(정규식 변경, docstring 수정)를 콜론과 `and`로 한 문장에 묶고, 마지막 근거 문장만 독립시키면 "무엇을 왜 고치는지"의 구조가 또렷해진다. 마침표로 끊긴 조각들을 이어 붙이면 지시문이 목록이 아니라 하나의 요청으로 읽힌다.
