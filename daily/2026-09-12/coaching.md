# 2026-09-12 — 코칭

## 한글→영어

### 카드 1 — 반출 승인 문구 추가   (내가 쓴 한글)
- 내가 쓴 한글: "추가: 반출 시 담당 MI팀 승인 필요."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Add this line: "Exporting data requires approval from the responsible MI team."
- 왜 이렇게: "반출 시 … 승인 필요"는 명사를 이어 붙인 메모체다. 영어로 `When export, MI team approval need` 처럼 옮기면 문장이 안 된다. 행위 자체를 동명사 주어 `Exporting data` 로 세우고 `requires approval` 로 받으면 UI 문구로 바로 쓸 수 있다. "담당"은 `the responsible MI team` 이나 `the MI team in charge` 로 옮긴다. 배너처럼 짧아야 하면 `Export requires MI team approval.` 까지 줄여도 된다.

### 카드 2 — 영어 문장에 섞어 쓴 화면 이름들   (내가 쓴 한글)
- 내가 쓴 한글: "이미지 갤러리", "측정 근거 레이어", "장비 모델 그룹", "데이터 반출 금지", "시스템 상태"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: image gallery / measurement evidence layer / tool model group / "No data export" notice / System Status card
- 왜 이렇게: 영어 요청 속에 한글 라벨을 끼우면 코드에서 검색할 땐 편하다. 대신 문법 역할이 흐려진다. `move the 데이터 반출 금지 to …` 에서는 이게 문구인지 카드인지 안 드러나니 뒤에 `notice`·`card`·`button` 같은 UI 명사를 붙이자. "반출"은 회사 밖으로 내보낸다는 뜻이라 `export` 가 맞다. `take out` 은 "꺼내다"로 읽힌다. 금지 표시는 표지판 문체인 `No data export` 가 `Data export is prohibited` 보다 짧고 자연스럽다.

### 카드 3 — 두 문장을 줄 나눈 이유   (고급 한글 · 번역)
- 한글 원문: "두 문장을 한 문단으로 이어 쓰지 않고 줄을 나눴습니다. 금지 안내와 승인 절차가 따로 읽힙니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: I put the two sentences on separate lines instead of running them together, so the ban and the approval step read as two separate things.
- 번역 포인트: "이어 쓰지 않고"는 `without connecting` 보다 `instead of running them together` 가 글쓰기 맥락에 맞다. `run together` 는 글자·문장이 붙어 버린다는 관용이다. "따로 읽힙니다"는 피동으로 옮기지 말고 자동사 `read` 를 쓴다. `The sentence reads well` 처럼 영어는 글이 "읽힌다"를 능동 자동사로 표현한다. 두 문장은 `so` 하나로 묶어 원인과 효과를 이었다.

### 카드 4 — 늘어나도 가운데   (고급 한글 · 번역)
- 한글 원문: "문장이 늘어도 묶음 전체가 가운데에 놓입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: However many lines you add, the block as a whole stays centered.
- 번역 포인트: "~해도"를 `even if` 로 옮기면 가정이 너무 도드라진다. 수량이 얼마든 결과가 같다는 뜻이라 `However many …` 양보절이 정확하다. "묶음 전체"는 `the whole bundle` 보다 레이아웃 용어 `the block as a whole` 이 낫다. "놓입니다"는 위치를 옮긴다는 `is placed` 가 아니라 상태를 유지한다는 `stays centered` 로 옮긴다.

### 카드 5 — 헷갈리지 않을 만큼만   (고급 한글 · 번역)
- 한글 원문: "줄바꿈된 첫 문장의 두 줄과 헷갈리지 않을 만큼만 떨어져 있습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: They sit just far enough apart that you won't mistake them for the two wrapped lines of the first sentence.
- 번역 포인트: "~할 만큼만"의 "만"이 핵심이다. `just far enough … that …` 으로 옮기면 "딱 그만큼, 더는 아니고"가 산다. `enough` 뒤 결과절에 `that` 을 쓰면 부정을 자연스럽게 담을 수 있다(`to` 부정사로 쓰면 `not to be confused with` 로 무거워진다). "헷갈리다"는 `confuse` 보다 `mistake A for B` 가 "A 를 B 로 잘못 본다"는 방향을 정확히 짚는다.

## 영어 다듬기

### 카드 1 — 포트로 직접 붙기
- 내가 쓴 영어: "what do i need to enable to access the llm models directly with the port?"   (출처: transcript:[user] llm-serving)
- 정정: 문장 첫 글자와 `i` 는 대문자(`What`, `I`). `with the port` → `on their ports` / `through the port`. 포트에는 전치사 `on` 이나 `through` 가 붙는다.
- 더 나은 표현: What do I need to turn on to reach the models directly on their ports?
- 왜: `access` 도 틀리진 않지만 네트워크로 닿는다는 뜻이면 `reach` 가 더 흔하다. `enable` 뒤엔 보통 목적어가 오니 무엇을 켜는지 모를 땐 `turn on` 이 덜 어색하다. `the llm models` 는 LLM 안에 model 이 이미 들어 있어 `the models` 로 충분하다.

### 카드 2 — 코드 서버에서 보이는 것
- 내가 쓴 영어: "what I see in the code server, the port forwarded with base_url/proxy/8006/.."   (출처: transcript:[user] llm-serving)
- 정정: 본동사가 없어 문장이 끝나지 않았다. `What I see … is the port forwarded at …` 처럼 `is` 가 필요하다. URL 앞 전치사는 `with` 가 아니라 `at`.
- 더 나은 표현: In code-server, I can see the port forwarded at `<base_url>/proxy/8006/`.
- 왜: `What I see is X` 유사 분열문은 `is` 가 빠지면 무너진다. 짧게 쓰려면 분열문을 버리고 `I can see …` 로 바로 가는 편이 낫다. 제품명 code-server 에는 관사를 붙이지 않는다.

### 카드 3 — env 파일 합치기
- 내가 쓴 영어: "it is rather complicated for me to handle multiple env, site.env and so on. can we unified them? several vlm token can also use the same key."   (출처: transcript:[user] llm-serving)
- 정정: `can we unified` → `can we unify` (조동사 뒤는 동사원형). `multiple env` → `multiple env files` (셀 수 있는 명사가 빠졌다). `several vlm token` → `the VLM tokens` (복수형).
- 더 나은 표현: Juggling several env files — site.env and the rest — is getting hard to keep straight. Can we merge them into one? The VLM tokens could all share a single key, too.
- 왜: `rather complicated for me to handle` 은 문법상 맞지만 밋밋하다. 여러 개를 동시에 붙들고 있다는 뜻의 `juggling` 과 헷갈리지 않게 정리한다는 `keep straight` 가 답답함을 더 잘 담는다. 마지막 문장은 제안이라 `can` 보다 `could` 가 부드럽다.

### 카드 4 — 모델 폴더를 옮겼다
- 내가 쓴 영어: "I move the file path to pjt_shared_pool/models."   (출처: transcript:[user] llm-serving)
- 정정: 이미 끝난 일이라 `I move` → `I moved` / `I've moved`. 옮긴 건 경로가 아니라 파일이니 `the file path` → `the model files`.
- 더 나은 표현: I've moved the model files to `pjt_shared_pool/models`.
- 왜: 방금 끝났고 지금 영향을 주는 변경은 현재완료가 가장 자연스럽다. 상대가 "그럼 경로를 고쳐야겠네"로 바로 이어갈 수 있다. 경로는 옮기는 대상이 아니라 바뀌는 속성이라 `move the path` 는 어색하다.

### 카드 5 — 하네스 엔지니어링을 배우고 싶다
- 내가 쓴 영어: "I want to learn about harness engineering for AI Agent in production level. what is the core concept of harness engineering and what should I care the most? make the folder harness and write down in md files what do I need to learn."   (출처: transcript:[user] pm-notes)
- 정정: `for AI Agent` → `for AI agents` (복수·소문자). `in production level` → `at production level` / `production-grade`. `care the most` → `care about most` (`care` 는 `about` 이 필요하다). `write down … what do I need to learn` → `what I need to learn` (문장 속 간접의문문은 도치하지 않는다).
- 더 나은 표현: I want to learn harness engineering for production-grade AI agents. What's the core idea, and what matters most? Create a `harness/` folder and write up what I need to learn as Markdown files.
- 왜: `what should I care about most` 를 `what matters most` 로 바꾸면 주어가 사물로 서서 짧아진다. `write down` 은 메모를 적는 느낌이고 정리된 문서를 만들 땐 `write up` 이 맞다.

### 카드 6 — 줄이 너무 길다
- 내가 쓴 영어: "good. however, make proper new line. some lines are too long to read it in a screen size."   (출처: transcript:[user] pm-notes)
- 정정: `make proper new line` → `add proper line breaks`. `too long to read it` → `too long to read` (`too … to V` 구문에서는 주어가 곧 목적어라 `it` 을 다시 쓰지 않는다). `in a screen size` → `on one screen`.
- 더 나은 표현: Good. One thing, though: please wrap the lines — some are too long to read on one screen.
- 왜: 줄바꿈을 넣는 작업은 `wrap` 한 단어로 된다. `however` 는 글에서 쓰는 접속부사라 대화에서는 `One thing, though:` 가 덜 딱딱하다.

### 카드 7 — 갤러리와 겹치는 기능 빼기
- 내가 쓴 영어: "in skewvoir, we offer 이미지 갤러리. not sure what I can do offer via 측정 근거 레이어.. remove the button and its feature."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `what I can do offer` → `what I can offer` (동사가 두 번 겹쳤다). `we offer 이미지 갤러리` → `we already offer an image gallery` (가산명사에 관사).
- 더 나은 표현: Skewvoir already has an image gallery, and I'm not sure what the measurement evidence layer adds on top of it. Let's remove the button and the feature behind it.
- 왜: 기능이 겹친다는 판단은 `what X adds on top of Y` 로 말하면 정확하다. `its feature` 보다 `the feature behind it` 이 "버튼이 여는 기능"이라는 관계를 또렷이 보여준다.

### 카드 8 — 선택 없이 시작하기
- 내가 쓴 영어: "in the tttm page, we must start with non-selections for 장비 모델 그룹. Instead of de-selecting tools, selecting tools seem much easier for the users."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the tttm page` → `on the TTTM page` (페이지에는 `on`). `non-selections` 는 없는 말이라 `nothing selected`. `selecting tools seem` → `seems` (동명사 주어는 단수).
- 더 나은 표현: On the TTTM page, the tool model group should start with nothing selected. Picking tools in is much easier for users than unchecking the ones they don't want.
- 왜: 요구 사항이라도 `must` 는 규정 문서 느낌이 강해 동료에게는 `should` 가 자연스럽다. `Instead of A, B seems easier` 보다 `B is easier than A` 로 비교를 한 문장에 넣으면 논리가 곧게 선다.

### 카드 9 — 경고 문구를 카드 안으로
- 내가 쓴 영어: "in the landing page, can we move the 데이터 반출 금지 to the inside the Metrology Workspace component? We can place it in the right side of the 시스템 상태 component. as a result, 시스템 상태 would be placed in the middle and the far right side, there is warning remark."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the landing page` → `on the landing page`. `to the inside the` → `inside the` (관사가 겹쳤다). `in the right side of` → `to the right of`. `the far right side, there is warning remark` → `the warning on the far right` (앞 절과 병렬이 깨졌고 `remark` 에 관사가 빠졌다).
- 더 나은 표현: On the landing page, can we move the "No data export" notice into the Metrology Workspace card, just to the right of System Status? That would put System Status in the middle and the warning on the far right.
- 왜: `That would put A in X and B in Y` 한 틀에 두 위치를 나란히 넣으면 레이아웃이 머릿속에 바로 그려진다. `as a result … would be placed` 수동보다 짧다. 옆 위치는 `in the right side of`(내부 오른쪽)가 아니라 `to the right of`(바깥 오른편)다.

### 카드 10 — 같은 스타일로 맞추기
- 내가 쓴 영어: "have the same style as 시스템 상태. place the main text in the center. and draw the lines between 데이터 반출 금지 and main text"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `draw the lines` → `draw a line` (구분선은 하나). `and main text` → `and the main text` (관사).
- 더 나은 표현: Match the System Status card's style: center the message, and add a divider between the title and the message.
- 왜: `have the same style as X` 는 `match X's style` 로 줄어든다. `center` 는 동사로 바로 쓰고, UI 에서 가로 구분선은 `divider` 라고 부른다. 세 지시를 콜론 하나 뒤에 묶으면 명령이 흩어지지 않는다.

### 카드 11 — 기여자는 무엇을 준비하나
- 내가 쓴 영어: "@docs/contributing/ based on this folder, what contributors should prepare to make their front / back ends in order to be attached to my project?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 직접 의문문이라 도치가 필요하다: `what contributors should prepare` → `what should contributors prepare`. `in order to be attached` 는 수동이 어색하니 `so their work can plug into …`.
- 더 나은 표현: Based on docs/contributing/, what do contributors need to prepare on the frontend and backend so their work can plug into my project?
- 왜: 물음표로 끝나는 질문에 평서 어순을 쓰면 간접의문문으로 읽혀 문장이 미완성처럼 보인다. `plug into` 는 모듈이 기존 시스템에 끼워진다는 뜻이라 이 맥락에 딱 맞는다.

### 카드 12 — HV-SEM 이미지가 비어 보인다
- 내가 쓴 영어: "When I use HV-SEM to see data in skewvoir/analysis, in SEM images component, sometimes, I do see just empty images (place holders). with refreshing the page, it sometimes display the images. HV-SEM tend to have tiff images and tend to have many images for a single msr. Can you check the codebase for HV-SEM skewvoir image displaying? it handles well tiff images with the converting to webp well?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `with refreshing the page` → `if I refresh the page`. `it sometimes display` → `displays` (3인칭 단수). `HV-SEM tend` → `tends`. `it handles well tiff images with the converting to webp well?` → `Does it handle TIFF images and the WebP conversion well?` (의문문 도치가 없고 `well` 이 두 번 나온다). `place holders` → `placeholders`.
- 더 나은 표현: In skewvoir/analysis with HV-SEM, the SEM Images panel sometimes shows only empty placeholders, and a refresh sometimes brings the images back. HV-SEM data tends to be TIFF, with many images per MSR. Could you trace how HV-SEM images get displayed, and check whether the TIFF-to-WebP conversion holds up?
- 왜: 증상은 `shows only empty placeholders`, 우연히 회복되는 건 `brings the images back` 으로 동사를 세우면 재현 조건이 선명해진다. `I do see` 의 강조 `do` 는 반박할 때 쓰는 말이라 여기선 필요 없다. 코드 경로를 따라가 달라는 부탁은 `check the codebase for` 보다 `trace how …` 가 정확하다.

### 카드 13 — 가장 작은 수정으로
- 내가 쓴 영어: "let's do smallest fixes"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 최상급 앞에는 `the`: `the smallest fixes`.
- 더 나은 표현: Let's go with the smallest fixes.
- 왜: 제안된 선택지 중 하나를 고를 땐 `do` 보다 `go with` 가 자연스럽다. 상대 목록에 있던 걸 가리키니 정관사가 꼭 필요하다.
