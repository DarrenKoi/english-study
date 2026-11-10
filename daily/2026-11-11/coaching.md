# 2026-11-11 — 코칭

출처는 모두 `transcript:` skewnono-v3-nuxt d0eba2c5 세션입니다(CLAUDE.md·AGENTS.md 점검 → CI lint 추가 → tool_files 테스트 진단 → werkzeug 버전 고정). 직접 쓴 영어 문장이 없어서 영어 다듬기는 생략합니다.

## 한글→영어

### 카드 1 — 둘 다 적용   (내가 쓴 한글)
- 내가 쓴 한글: "둘 다 적용해줘"   (출처: transcript:[user])
- 자연스러운 영어: Go ahead and apply both.
- 왜 이렇게: 제안을 받고 승인하는 장면이라 `Go ahead and …` 가 딱 맞습니다. "해줘"를 `please` 로 옮기면 부탁처럼 들리고, `Go ahead` 는 "그렇게 해도 좋다"는 허락입니다. 더 짧게는 `Both, please.`

### 카드 2 — ~도 점검   (내가 쓴 한글)
- 내가 쓴 한글: "AGENTS.md 파일들도 점검해줘"   (출처: transcript:[user])
- 자연스러운 영어: Can you review the AGENTS.md files too?
- 왜 이렇게: "~도"는 문장 끝 `too` 나 `as well` 로 둡니다. "점검"은 문서 품질을 보는 일이라 `check` 보다 `review` 나 `audit` 가 정확합니다. 앞 작업에 이어 붙이는 요청이면 `While you're at it, …` 로 열어도 자연스럽습니다.

### 카드 3 — CI에 넣기   (내가 쓴 한글)
- 내가 쓴 한글: "CI에 lint 넣어줘"   (출처: transcript:[user])
- 자연스러운 영어: Add the lint step to CI.
- 왜 이렇게: "넣다"는 `add … to` 가 기본입니다. 실패하면 머지를 막는 단계라는 뜻까지 담으려면 `Gate CI on lint.` 라고 합니다. 대화 속 문서도 `not gated` 라는 표현을 썼습니다.

### 카드 4 — 파 보다   (내가 쓴 한글)
- 내가 쓴 한글: "tool_files 파봐"   (출처: transcript:[user])
- 자연스러운 영어: Dig into the tool_files failure.
- 왜 이렇게: "파 보다"는 영어에서도 같은 비유인 `dig into` 를 씁니다. 대상이 폴더가 아니라 실패한 테스트라서 `the tool_files failure` 로 목적어를 분명히 합니다. 더 캐주얼하게는 `Take a look at tool_files.`

### 카드 5 — 원인 추측 + 확인 질문   (내가 쓴 한글)
- 내가 쓴 한글: "Windows, linux 두 OS에서 다 사용하기 때문인데, 이제 문제 해결된건가?"   (출처: transcript:[user])
- 자연스러운 영어: I figured it was because we use it on both Windows and Linux. So is it fixed now?
- 왜 이렇게: 원문은 "~때문인데"로 내 추측을 깔고 확인을 묻습니다. 영어는 두 문장으로 나누는 편이 깔끔합니다. 추측은 `I figured it was because …`, 확인은 `So is it fixed now?` 로 씁니다. 원인을 단정하지 않고 열어 두려면 `I assumed it was a Windows/Linux thing — is that right, and is it fixed?`

### 카드 6 — 그럼 고정   (내가 쓴 한글)
- 내가 쓴 한글: "version을 그럼 고정해줘."   (출처: transcript:[user])
- 자연스러운 영어: Then let's pin the version.
- 왜 이렇게: 의존성 버전을 "고정하다"는 `pin` 이 표준 용어입니다(`fix` 는 "고치다"와 헷갈림). "그럼"은 앞 설명을 받는 `Then` 이나 `In that case` 로 둡니다. 정확히 밝히려면 `pin Werkzeug to 3.1.9`.

### 카드 7 — A가 아니라 B였다   (고급 한글 · 번역)
- 한글 원문: "깨진 건 업로드 방어 코드가 아니라 테스트의 기대값이었습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: What broke wasn't the upload guard; it was the test's expected value.
- 번역 포인트: "깨진 건"을 `What broke` 라는 what 명사절 주어로 살리면 한국어의 초점 구조가 그대로 옮겨집니다. `not A but B` 보다 세미콜론으로 끊는 쪽이 대조가 또렷합니다. "방어 코드"는 `defensive code` 보다 `guard` 가 짧고 개발자에게 익숙합니다.

### 카드 8 — "로컬은 통과, CI는 실패"가 생긴 경우   (고급 한글 · 번역)
- 한글 원문: "버전을 고정하지 않은 의존성 때문에 '로컬은 통과, CI는 실패'가 생긴 경우입니다."   (출처: transcript:[assistant])
- 자연스러운 영어: This is a classic "passes locally, fails in CI" case, caused by an unpinned dependency.
- 번역 포인트: 따옴표 속 구절을 명사처럼 형용사 자리에 넣는 영어 패턴(`a "works on my machine" bug`)을 쓰면 원문 리듬이 삽니다. "~경우입니다"는 `This is a … case` 로 두고 `classic` 을 더하면 흔한 유형이라는 뉘앙스가 붙습니다. "고정하지 않은"은 한 단어 `unpinned`.

### 카드 9 — 읽기보다 돌려 보는 편이 빠르다   (고급 한글 · 번역)
- 한글 원문: "이런 문제는 코드를 읽기보다 버전 조합을 몇 초 만에 돌려 보는 편이 빠릅니다."   (출처: transcript:[assistant])
- 자연스러운 영어: With problems like this, it's faster to spend a few seconds running the version combinations than to read the code.
- 번역 포인트: "~보다 ~하는 편이 빠르다"는 `it's faster to A than to B`. 두 to부정사의 모양을 맞춥니다. "이런 문제는"은 주어가 아니라 화제라서 `With problems like this,` 로 문두에 뺍니다. "몇 초 만에"는 `in seconds` 도 되지만 `spend a few seconds` 가 비용 비교를 더 분명히 합니다.

### 카드 10 — 앞으로 직접 챙겨야 해서 권하지 않음   (고급 한글 · 번역)
- 한글 원문: "대신 버전을 올리는 일을 앞으로 직접 챙겨야 해서, 지금은 권하지 않습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: The catch is that you'd have to handle upgrades yourself from then on, so I wouldn't recommend it for now.
- 번역 포인트: "대신"은 대가를 말하는 `The catch is that …` 이 자연스럽습니다(`instead` 는 대체라 뜻이 다름). "챙기다"는 `handle`·`keep on top of` 로 옮깁니다. 권유를 부드럽게 거절할 때는 `I don't recommend` 보다 가정의 `I wouldn't recommend` 가 한결 정중합니다.
