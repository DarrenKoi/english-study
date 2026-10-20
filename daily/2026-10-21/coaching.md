# 2026-10-21 — 코칭

오늘 내가 새로 쓴 한국어는 성과 리뷰에 수상 경력을 넣던 대화의 세 문장이다. 영어 쪽은 commit 지시 한 줄과 AFM 작업 브리프 지시문이다. (스큐노노 tip 모니터링 대화의 내 한국어는 압축 요약 속에 다시 실렸을 뿐이고, 10-07 코칭에서 이미 다뤘다.)

## 한글→영어

### 카드 1 — 수상 경력도 있어 (내가 쓴 한글)
- 내가 쓴 한글: "@achievement_review/ 에서 스큐노노도 수상경력이 있어. 2025년 말 AI/DT Summit 최우수상 수상작"   (출처: transcript:[user] pm_notes my-task)
- 자연스러운 영어: SKEWNONO has an award too — add it to `achievement_review/`. It won the grand prize at the AI/DT Summit in late 2025.
- 왜 이렇게: "수상경력이 있다"는 `has an award history` 가 아니라 `has an award` 또는 `is an award winner` 로 충분하다. "~도"는 `too` 를 문장 끝에 둔다. 원문 둘째 줄은 명사로 끝나는 메모체("수상작")라 영어에서는 `It won …` 으로 주어와 동사를 세워야 한다. "최우수상"은 행사 성격에 따라 `grand prize`, `top award`, `first prize` 중 고르는데, 여러 부문 위의 최고 상이면 `grand prize` 가 맞다. "2025년 말"은 `in late 2025`.

### 카드 2 — 공식 행사명은 ~ (내가 쓴 한글)
- 내가 쓴 한글: "공식 행사명은 기반기술센터 AI/DT Summit 2025"   (출처: transcript:[user] pm_notes my-task)
- 자연스러운 영어: The official name of the event is the Foundation Technology Center AI/DT Summit 2025.
- 왜 이렇게: 한국어는 "~은 X" 로 동사 없이 끝나도 통하지만 영어는 `is` 를 꼭 넣는다. 고유 행사명 앞에는 정관사 `the` 를 붙인다(`the … Summit 2025`). 조직명 "기반기술센터"는 사내 공식 영문명이 있으면 그걸 쓰고, 없으면 위처럼 풀어 쓴다. 정정하는 맥락이니 구어로는 `Just to correct that: the official name is …` 로 시작해도 좋다.

### 카드 3 — 공개본에서도 정식 명칭 (내가 쓴 한글)
- 내가 쓴 한글: "공개본에서 정식 명칭 사용."   (출처: transcript:[user] pm_notes my-task)
- 자연스러운 영어: Use the official name in the public versions too.
- 왜 이렇게: "~ 사용." 같은 명사형 종결 지시문은 영어에서 명령문 `Use …` 로 바꾸면 된다. "공개본"은 파일이 셋이라 복수 `the public versions`. 앞서 어시스턴트가 "공개본은 숨기는 방식"이라고 했던 걸 뒤집는 결정이라, `too` 나 `as well` 을 붙여야 "사내용처럼 공개본에도"라는 뜻이 산다.

### 카드 4 — 평균이 끌려가서 생긴 오판 (고급 한글 · 번역)
- 한글 원문: "구현 중에 관리선의 중심을 평균에서 중앙값으로 바꿨습니다. 테스트를 쓰다 보니, 나빠지는 팁이 평균을 자기 쪽으로 끌고 가서 멀쩡한 측정이 오히려 관리선 밖으로 밀리는 경우가 실제로 나왔습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: During implementation, I moved the centre of the control limits from the mean to the median. While writing the tests, I hit real cases where a degrading tip dragged the mean toward itself and pushed perfectly healthy measurements outside the limits.
- 번역 포인트: "끌고 가서"는 `dragged … toward itself` 로 물리적 비유를 그대로 살린다. "멀쩡한"은 `normal` 보다 `perfectly healthy` 가 "아무 문제 없는데도"의 억울함을 담는다. "오히려"는 따로 `rather` 를 넣기보다 `pushed healthy measurements outside` 라는 대비 자체로 전달된다. "~하는 경우가 실제로 나왔다"는 `I hit real cases where …` 로, 관계부사 `where` 가 경우를 풀어 준다.

### 카드 5 — 그 방식과 어긋납니다 (고급 한글 · 번역)
- 한글 원문: "공개본은 'AI Summit 2026'을 '사내 AI 행사'로 바꿔 쓰는 등 행사명과 조직명을 숨기는 방식이라, '기반기술센터'를 넣으면 그 방식과 어긋납니다."   (출처: transcript:[assistant] pm_notes my-task)
- 자연스러운 영어: The public versions hide event and organisation names — "AI Summit 2026" became "an internal AI event", for instance — so adding "Foundation Technology Center" would break that convention.
- 번역 포인트: "~하는 등"은 `such as` 로 문장 안에 넣으면 길어지니, 대시로 예시를 끼워 넣고 `for instance` 로 닫는다. "방식"은 `method` 보다 `convention`(지켜 온 관례)이 맞다. "어긋나다"는 `be inconsistent with` 도 되지만 동사 하나 `break` 가 짧고 분명하다. "넣으면"은 가정이라 `would` 를 쓴다.

### 카드 6 — 장비의 사실이라 (고급 한글 · 번역)
- 한글 원문: "장착된 팁 표시는 장비의 사실이라 필터와 무관하게 유지됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: The mounted-tip marker stays put regardless of the filter, because which tip is mounted is a fact about the tool, not about the view.
- 번역 포인트: "장비의 사실"은 직역(`the tool's fact`)하면 어색해서 `a fact about the tool` 로 풀고, 무엇과 대비되는지(`not about the view`)를 덧붙여 논리를 드러냈다. "무관하게"는 `regardless of`. "유지됩니다"는 수동 `is kept` 대신 `stays put`(제자리에 그대로 있다)이 화면 동작에 잘 맞는다.

## 영어 다듬기

### 카드 7 — 그리고 commit and push
- 내가 쓴 영어: "그리고 commit and push"   (출처: transcript:[user] pm_notes my-task)
- 더 나은 표현: Go ahead and commit and push those.
- 왜: 한국어 "그리고"를 그대로 `And` 로 옮기면 영어에서는 앞말에 덧붙이는 느낌이 된다. 앞 질문("커밋하고 push할까요?")에 답하는 말이니 `Go ahead and …` 가 "네, 진행하세요"를 자연스럽게 준다. `those` 로 대상(공개본 3개)을 짚으면 더 분명하다. 아주 짧게는 `Yes — commit and push.` 도 좋다.

### 카드 8 — 브리프대로 다 해, 묻지 말고
- 내가 쓴 영어: "Read ./BRIEF-common.md and ./BRIEF-afm-usage.md and do everything they say, without asking me questions. Stop when ./REPORT-afm-usage.md is written."   (출처: transcript:[user] skewnono-afm-usage)
- 더 나은 표현: Read ./BRIEF-common.md and ./BRIEF-afm-usage.md, then carry out everything they ask for without checking back with me. You're done once ./REPORT-afm-usage.md is written.
- 왜: 문법 오류는 없다. `and … and` 가 두 번 이어지는 걸 `, then` 으로 끊으면 순서(읽고 → 실행)가 또렷해진다. `do everything they say` 는 구어로 충분히 좋고, 글로는 `carry out everything they ask for` 가 한 단계 위다. `without asking me questions` 는 `without checking back with me` 로 바꾸면 "중간에 확인받지 말라"는 의도가 정확해진다. `Stop when …` 은 명령이 갑작스러우니 `You're done once …` 가 완료 조건으로 더 부드럽다.

### 카드 9 — 단수 they / it 맞춤
- 내가 쓴 영어: "Read ./ROUND2-afm-usage.md and do everything it says, without asking me questions."   (출처: transcript:[user] skewnono-afm-usage)
- 더 나은 표현: Read ./ROUND2-afm-usage.md and work through every item in it on your own.
- 왜: 파일이 하나라 `it says`, 둘이던 브리프에서는 `they say` 로 정확히 맞췄다. 대명사 일치가 잘 돼 있다. 라운드 문서는 지적 항목 목록이니 `work through every item` 이 "하나씩 처리하라"를 더 잘 살린다. `on your own` 이 "묻지 말고 알아서"를 두 단어로 줄여 준다.
