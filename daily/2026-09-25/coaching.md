# 2026-09-25 — 코칭

> 오늘 `[user]` 글은 거의 영어였고 한국어는 화면 라벨과 짧은 판단 몇 마디뿐이었다. (a) 카드 3장은 TTTM 개편 요청에 섞인 한국어에서 나왔다. (b) 는 긴 한국어 문장이 없어 어시스턴트가 쓴 UI 문구 2개로 채웠다. 영어 다듬기는 28장이다. "commit and push", "close port 3000" 처럼 고칠 게 없는 짧은 명령은 뺐고 english-study 파이프라인 프롬프트와 herdr·tdd·writing-for-agents 스킬 본문은 `[user]` 로 찍혔어도 내가 쓴 글이 아니라 제외했다.

## 한글→영어

### 카드 1 — "오늘" 대신 선택한 기간으로   (내가 쓴 한글)
- 내가 쓴 한글: "오늘의 consensus 잔차보다는 선택한 수집기간으로 보는게 좋을 듯. 오늘 data 기준은 모호하다."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I think it'd be better to show the consensus residual over the selected collection period rather than for today. "Today's data" is ambiguous.
- 왜 이렇게: "~보다는 ~로 보는 게 좋을 듯"은 `it'd be better to A rather than B` 가 딱 맞는다. "~듯"의 추측 말투는 앞에 `I think` 를 붙여 살린다. "오늘 data 기준은 모호하다"를 `the standard of today data` 로 직역하면 어색하고 모호한 건 "오늘 데이터"라는 말 자체라서 따옴표로 묶어 주어로 세웠다.

### 카드 2 — 가장 가까운 장비마저 허용 오차 밖   (내가 쓴 한글)
- 내가 쓴 한글: "장비 그룹 배치도 too. 가장 가까운 장비마저 허용 오차 밖. sounds weird to me."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The 장비 그룹 배치도 label "Even the closest tool is out of tolerance" sounds odd to me.
- 왜 이렇게: "~마저"는 `even` 이 정확히 대응한다. "허용 오차 밖"은 `outside the tolerance` 도 되지만 제조 현장에서는 `out of tolerance` 가 굳은 표현이다. 원문은 조각 셋으로 흩어져 있어서 "무엇이 이상한지"를 주어 하나로 모았다.

### 카드 3 — 자세히는 필요 없어   (내가 쓴 한글)
- 내가 쓴 한글: "explain kindly. (No need to use 자세히). just explain."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Explain it plainly — no need for the "자세히" (details) folds. Just say it.
- 왜 이렇게: 여기서 "자세히"는 부사가 아니라 접이식 UI 이름이라 `the "자세히" folds` 처럼 명사로 다뤄야 뜻이 산다. "친절하게 설명해"를 `kindly` 로 옮기면 "상냥하게"로 읽힌다. 실제 뜻은 "쉽고 명확하게"라서 `plainly` 나 `in simple terms` 가 맞다.

### 카드 4 — 허용 오차 안에 맞는 장비 있음/없음   (고급 한글 · 번역)
- 한글 원문: "허용 오차 안에 맞는 장비 있음 / 허용 오차 안에 맞는 장비 없음"   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: At least one tool within tolerance / No tool within tolerance
- 번역 포인트: 한국어 범례는 "~있음/없음" 명사형 종결로 짧게 끝나는 반면 영어 범례를 `There is a tool …` 처럼 문장으로 쓰면 길어진다. 명사구 대비(`At least one … / No …`)로 옮기면 두 항목 길이가 비슷해지고 한눈에 대조된다. "맞는"은 따로 옮기지 않아도 `within tolerance` 에 들어 있다.

### 카드 5 — 지금 만져도 되는지   (고급 한글 · 번역)
- 한글 원문: "지금 만져도 되는지"   (출처: transcript:[assistant] skewnono-v3-nuxt, Up gate 설명)
- 자연스러운 영어: Safe to adjust now?
- 번역 포인트: "만지다"를 `touch` 로 직역하면 영어에서도 구어로 통하지만 장비 파라미터 조정 맥락에서는 `adjust` 나 `tune` 이 정확하다. "~해도 되는지"는 허락보다 안전 여부를 묻는 말이라 `Is it OK to …` 보다 `Safe to … ?` 가 게이트 이름으로 어울린다. 주어와 be동사를 빼 라벨답게 줄였다.

## 영어 다듬기

### 카드 6 — TTTM 페이지 개편 요청
- 내가 쓴 영어: "We need to renovate tttm page. PM 튜닝 옵션 seems not needed."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `renovate tttm page` → `renovate the TTTM page` (특정 페이지라 정관사). `seems not needed` → `doesn't seem necessary` (영어는 부정을 `seem` 쪽에 둔다).
- 더 나은 표현: We need to rework the TTTM page. The PM 튜닝 option doesn't seem necessary anymore.
- 왜: `renovate` 는 건물 수리 느낌이 강하다. 화면 개편에는 `rework`, `revamp`, `overhaul` 이 더 자연스럽다.

### 카드 7 — 반응형 컴포넌트
- 내가 쓴 영어: "Instead of PM 튜닝, we have reactive compenet that display how much the parameter of the tool should be changed."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `compenet` → `component` (철자). `reactive compenet that display` → `a reactive component that displays` (셀 수 있는 명사엔 관사, 단수 주어엔 3인칭 -s).
- 더 나은 표현: Instead of PM 튜닝, let's have a reactive card that shows how far each of the tool's parameters needs to move.
- 왜: 원하는 걸 말할 땐 `we have` 가 아니라 `let's have` 나 `we should have`. `how much … should be changed` 보다 `how far … needs to move` 가 "중심까지의 거리"라는 그림을 더 잘 보여 준다.

### 카드 8 — 버튼 위치 옮기기
- 내가 쓴 영어: "Also, 데이터 요청 button should be relocated. hard to tell what to click from the user side. Rather make it placed below 수집 기간, 데이터 요청. rather than far away from the buttons."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `데이터 요청 button` → `the 데이터 요청 button`. `hard to tell` → `It's hard to tell` (주어 필요). `make it placed below` → `place it below` (`make + 목적어 + 과거분사` 는 "~된 상태로 만들다"라서 위치 지정엔 안 맞는다).
- 더 나은 표현: Also, please move the 데이터 요청 button. Users can't easily tell what to click. Put it right below the 수집 기간 chips instead of far away from them.
- 왜: `from the user side` 는 `users can't tell` 로 주어를 사람으로 세우면 더 짧다. `rather … rather than` 이 연달아 나와 중복이라 `instead of` 하나로 정리했다.

### 카드 9 — 설명 문구가 장황하다
- 내가 쓴 영어: "Your text explaning the pages are not clear and too verbose."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `explaning` → `explaining` (철자). `Your text … are` → `Your text … is` (주어는 `text`, 불가산 단수).
- 더 나은 표현: The explanatory text on the page is unclear and too wordy.
- 왜: 수식어가 길면 주어와 동사가 멀어져 수 일치를 놓치기 쉽다. `explaining the pages` 를 형용사 `explanatory` 로 줄이면 동사와 주어가 가까워진다.

### 카드 10 — 점선은 안 써
- 내가 쓴 영어: "Renovate the chart of skew 트렌드 too. We do not use 점선 here. Never seen it."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Rework the skew 트렌드 chart too. We don't use dashed lines here — I've never seen them used.
- 왜: `the chart of X` 보다 명사를 앞에 붙인 `the X chart` 가 자연스럽다. 경험을 말할 땐 `I've never seen` 현재완료가 맞고 주어를 빼면 채팅에선 통해도 글에선 끊겨 보인다.

### 카드 11 — 선이 너무 많으면
- 내가 쓴 영어: "When too many tools are selected, hard lines make it hard to track down. just use scatter plot instead of line plot. (instead make the dots noticeable)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `use scatter plot instead of line plot` → `use a scatter plot instead of a line plot` (가산 명사엔 관사).
- 더 나은 표현: When lots of tools are selected, the solid lines are hard to follow. Just use a scatter plot, and make the dots easy to see.
- 왜: `track down` 은 "추적해서 찾아내다"라 여기엔 안 맞는다. 선을 눈으로 따라가는 건 `follow`. `hard lines` 는 "딱딱한 선"으로 읽힐 수 있어 `solid lines` 가 정확하다.

### 카드 12 — 드롭다운 대신 버튼
- 내가 쓴 영어: "the parameters can be displayed in buttons. rather than using drop down."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `rather than using drop down` → `rather than in a dropdown` (관사, 병렬 구조 맞춤).
- 더 나은 표현: Show the parameters as toggle buttons rather than in a dropdown.
- 왜: 버튼 "안에" 표시하는 게 아니라 버튼 "형태로" 보여 주는 것이라 `as buttons` 가 맞다. `rather than` 앞뒤는 같은 꼴(`as buttons` ↔ `in a dropdown`)로 맞춘다.

### 카드 13 — Codex 로 구현하고 리뷰 받기
- 내가 쓴 영어: "Since we do renovate the page, implement the job with codex (use herdr skill). actively use simplify and request thorough review to the codex."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `Since we do renovate` → `Since we're renovating` (진행 중인 일은 진행형. 강조 `do` 는 여기선 어색하다). `request thorough review to the codex` → `ask Codex for a thorough review` (`request` 는 `to` 를 받지 않는다. 사람에겐 `ask A for B`).
- 더 나은 표현: Since this is a full rework, have Codex implement it through the herdr skill. Make heavy use of simplify, and ask Codex for a thorough review.
- 왜: `implement the job` 은 어색한 결합. 일을 맡길 땐 `have + 사람 + 동사원형` 사역이 자연스럽다.

### 카드 14 — 위키 결과가 보기 흉하다
- 내가 쓴 영어: "I run the parser folder with the office llm and get to the result of wiki. I found that it is really ugly. hash style is not the way of human-friendly."   (출처: transcript:[user] equipment-data-map)
- 정정: `I run … and get to` → `I ran … and got` (이미 한 일이라 과거형). `hash style is not the way of human-friendly` → `hash-style names aren't human-friendly` (`the way of` 뒤에 형용사는 못 온다).
- 더 나은 표현: I ran the parser folder with the office LLM and got the wiki output. It's really ugly — hash-style names aren't human-friendly.
- 왜: `I found that it is really ugly` 는 "알아냈다"는 과정이 불필요하게 길다. 감상은 `It's really ugly` 로 바로 말한다.

### 카드 15 — 다른 방식으로 접근해야
- 내가 쓴 영어: "You said it was the way of avoiding duplicated files, but we have to apporach differently."   (출처: transcript:[user] equipment-data-map)
- 정정: `the way of avoiding` → `the way to avoid` (방법은 `way to + 동사`). `apporach` → `approach` (철자). `approach differently` → `approach it differently` (`approach` 는 타동사라 목적어 필요).
- 더 나은 표현: You said hashing was how we avoid duplicate files, but we need a different approach.
- 왜: `duplicated files` 는 "복제된 파일", `duplicate files` 는 "중복 파일". 여기선 후자가 맞다.

### 카드 16 — 이미 받은 파일은 건너뛰기
- 내가 쓴 영어: "Just avoid downloading if it is already downloaded to the local with the same file name."   (출처: transcript:[user] equipment-data-map)
- 정정: `to the local` → `locally` (`local` 은 형용사라 명사처럼 못 쓴다).
- 더 나은 표현: Skip the download if a file with the same name already exists locally.
- 왜: `avoid downloading if it is already downloaded` 는 같은 동사가 반복된다. `skip` 하나로 "건너뛰다"를 말하고 조건절은 파일을 주어로 세우면 깔끔하다.

### 카드 17 — 폴더마다 index.md
- 내가 쓴 영어: "The final result of wiki should be identical to the fab tool's file structure. In the index.md can describe the file folders briefily."   (출처: transcript:[user] equipment-data-map)
- 정정: `In the index.md can describe` → `The index.md can describe` (주어가 없다. 전치사구는 주어가 될 수 없다). `briefily` → `briefly` (철자).
- 더 나은 표현: The final wiki should mirror the tool's file structure, and each index.md should briefly describe the folders.
- 왜: `identical to` 도 맞지만 "구조를 그대로 따라 한다"는 `mirror` 가 더 짧고 정확하다.

### 카드 18 — 이렇게 하면 LLM 이 찾기 쉽다
- 내가 쓴 영어: "With the cascade of index.md, the llm can search the files easily."   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: With an index.md at every level, the LLM can find files easily.
- 왜: 문법 오류는 없다. `the cascade of index.md` 는 무엇이 어떻게 이어지는지 흐릿하니 `at every level` 로 그림을 준다. `search the files` 는 "파일 안을 뒤지다"로 읽혀서 `find files` 가 뜻에 맞다.

### 카드 19 — 리셋해야 해 그냥 복사해?
- 내가 쓴 영어: "need to reset for the copy to the qwen? or just copy?"   (출처: transcript:[user] equipment-data-map)
- 정정: `need to reset` → `Do I need to reset` (의문문은 조동사와 주어가 필요하다).
- 더 나은 표현: Do I need to reset before copying it to the qwen folder, or can I just copy it?
- 왜: `for the copy` 는 목적처럼 읽혀 어색하다. 순서를 말하려면 `before copying`. 두 선택지는 `A, or can I just B?` 로 한 문장에 묶는다.

### 카드 20 — 방문으로 세야 할까
- 내가 쓴 영어: "in activity page, 장비 상태 is a kind of initial page for the selected fab. I don't know if it is good to be counted as the visiting page."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in activity page` → `On the activity page` (페이지 "위에"는 `on`, 특정 페이지라 `the`). `the visiting page` → `a page visit` (방문 "한 건"은 `visit` 이 명사).
- 더 나은 표현: On the activity page, 장비 상태 is basically the landing page for the selected fab, so I'm not sure it should count as a page visit.
- 왜: `a kind of initial page` 는 `basically the landing page` 가 웹 용어로 자연스럽다. `I don't know if it is good to be counted` 는 `I'm not sure it should count` 로 줄인다. `count as` 는 자동사로 "~로 쳐지다".

### 카드 21 — API 키로 누가 가져가는지
- 내가 쓴 영어: "Can we also track down on who is getting data via endpoints with api key?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `track down on who` → `track who` (`track down` 은 타동사구라 `on` 이 붙지 않는다).
- 더 나은 표현: Can we also track who is pulling data through the endpoints with an API key?
- 왜: `track down` 은 "숨은 걸 찾아내다", `track` 은 "계속 기록하다". 여기선 후자라 `track` 만 쓴다. 데이터를 가져가는 건 `pull data` 가 개발자 구어로 자연스럽다.

### 카드 22 — Codex 의 도움 받기
- 내가 쓴 영어: "do both, separate commits. and you can get helped by codex with herdr (use tabs)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `get helped by codex` → `get help from Codex` (`help` 는 명사로 받는 쪽이 자연스럽다).
- 더 나은 표현: Do both, as separate commits. Feel free to get help from Codex through herdr, in a separate tab.
- 왜: `you can` 은 허락이지만 `Feel free to` 가 "써도 좋다"를 더 부드럽게 전한다.

### 카드 23 — 실제 업무에 돌리려니
- 내가 쓴 영어: "I want to run the workflow_3 in real work. but I found it quite hard to track down on bugs and issues. currently all images, logs are separately stored."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `track down on bugs` → `track down bugs` (`on` 불필요). `the workflow_3` → `workflow_3` (고유 이름엔 관사를 안 붙인다).
- 더 나은 표현: I want to run workflow_3 in production, but tracking down bugs is hard right now because the images and logs are all stored in different places.
- 왜: `in real work` 는 `in production` 이나 `on real equipment` 가 자연스럽다. `separately stored` 는 뜻은 통하지만 "흩어져 있다"는 `stored in different places` 가 더 선명하다. 원인과 결과는 `because` 로 한 문장에 묶는다.

### 카드 24 — 한 이벤트 폴더에 모으기
- 내가 쓴 영어: "I want to store them in a single event folder (like, <tool_id>-<timestamp>. under the folder all loggings and images should be stored."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `loggings` → `logs` (`logging` 은 행위라 복수형으로 쓰지 않는다. 결과물은 `logs`). 괄호가 닫히지 않았다.
- 더 나은 표현: I want everything for one event in a single folder, such as `<tool_id>-<timestamp>/`, with all its logs and images inside.
- 왜: `like,` 는 말할 때의 군말이라 글에서는 `such as` 나 `e.g.` 로 바꾼다.

### 카드 25 — 새 폴더로 시작할까 고칠까
- 내가 쓴 영어: "what do you think? should I start with a new folder like workflow_3_deploy? or can you manage to amend the code for having organized loggings?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `for having organized loggings` → `so the logs are organized` (목적은 `for + 동명사` 보다 `so (that)` 절이 자연스럽다).
- 더 나은 표현: What do you think — should I start a new folder like `workflow_3_deploy`, or can you restructure the existing code so the logs are organized?
- 왜: 두 선택지를 한 의문문에 `A, or B?` 로 넣으면 비교가 한눈에 보인다. `manage to amend` 는 "간신히 고치다"로 읽혀 `restructure` 가 의도에 맞다.

### 카드 26 — Codex 에 리뷰 요청
- 내가 쓴 영어: "ask for the review to the codex (herdr, with a new tab)."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `ask for the review to the codex` → `ask Codex for a review` (`ask + 사람 + for + 것`. `to` 는 쓰지 않는다).
- 더 나은 표현: Ask Codex to review it in a new herdr tab.
- 왜: 카드 13 과 같은 실수다. "누구에게 무엇을 요청하다"는 `ask A for B` 나 `ask A to do` 로 기억해 둔다.

### 카드 27 — 이 스크립트도 새 방식이야?
- 내가 쓴 영어: "so manual_align_correction.py is also based on the newly updated logging style?"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: So does `manual_align_correction.py` use the new logging layout too?
- 왜: 문법 오류는 없다. 평서문 끝을 올리는 의문은 말로는 자연스럽지만 글에서는 `does … use` 어순이 분명하다. `is based on the newly updated` 는 `use the new` 로 반 이상 줄어든다.

### 카드 28 — 여러 장비에서 동시에 터지면
- 내가 쓴 영어: "what I am worried when I run the poc/workflow_3 in real work, what would happen when align fail happens multiple times from several tools? how can you manage that?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `what I am worried` → `What I'm worried about` (`worried about` 의 전치사를 빠뜨리면 안 된다).
- 더 나은 표현: What worries me about running workflow_3 in production is this: what happens when several tools hit align fail at the same time, and how would you handle it?
- 왜: 문장이 `what … , what …?` 로 두 번 시작해 꼬였다. `What worries me is this:` 로 걱정을 세운 뒤 콜론 뒤에 질문을 모으면 한 번에 읽힌다.

### 카드 29 — 알람 행은 계속 남아
- 내가 쓴 영어: "alarm row stay in the feed. even if it is cleared, still you can the rows in the alarm  with the same UTC9."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `alarm row stay` → `Alarm rows stay` (복수 주어). `still you can the rows` → `you can still see the rows` (동사 `see` 가 빠졌고 `still` 은 조동사 뒤).
- 더 나은 표현: Alarm rows stay in the feed. Even after an alarm clears, its row is still there with the same UTC9.
- 왜: 빈도·지속 부사 `still` 은 조동사 뒤, 일반동사 앞에 둔다. 주어를 `its row` 로 세우면 "사람이 본다"가 아니라 "데이터가 남는다"는 사실이 바로 보인다.

### 카드 30 — 엔지니어가 먼저 고쳤다면
- 내가 쓴 영어: "What I am worried is when the align fail monitor starts, if a tool is detected as a align fail but within a small period, a engineer fixed the issue. then what would happen? In short, align fail occurs in the alarm but already solved by engineer before the agent enters the tool monitor."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `What I am worried is` → `What I'm worried about is`. `a align fail`, `a engineer` → `an align fail`, `an engineer` (모음 소리 앞은 `an`). `already solved` → `has already been solved` (수동 완료형에 be동사 필요).
- 더 나은 표현: Here's my worry: the monitor detects an align fail on a tool, but an engineer fixes it a moment later, before the agent gets into the tool. What happens then?
- 왜: 가정 상황을 `if … but within …` 로 한 문장에 넣으면 시점이 섞인다. 상황을 현재형으로 차례대로 적고 질문은 마지막에 따로 두면 훨씬 읽기 쉽다.

### 카드 31 — 기존 기능을 건드리지 않고
- 내가 쓴 영어: "is it possible to add size checking method to ftp_handler without touching the current feature? you must have proxy and direct download working in the same way (same input and output, same def names)"   (출처: transcript:[user] equipment-data-map)
- 정정: `add size checking method` → `add a size-checking method` (관사, 복합 형용사엔 하이픈).
- 더 나은 표현: Can we add a size-checking method to `ftp_handler` without touching existing behavior? Proxy and direct download must work the same way — same inputs, outputs and function names.
- 왜: `you must have … working` 은 상대에게 명령하는 투라 강하다. 요구 조건은 대상(`Proxy and direct download`)을 주어로 세우면 명세처럼 읽힌다.

### 카드 32 — agent-browser 로 확인
- 내가 쓴 영어: "can you verify with using /agent-browser ?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `verify with using` → `verify it using` 또는 `verify it with` (`with` 와 `using` 은 같은 뜻이라 하나만).
- 더 나은 표현: Can you verify it with /agent-browser?
- 왜: 물음표 앞에는 띄어쓰기를 하지 않는다. `verify` 는 목적어 `it` 을 넣어야 무엇을 확인하는지 분명해진다.

### 카드 33 — zsh 에서 venv 켜기
- 내가 쓴 영어: "how can I activate .venv in zsh"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: How do I activate `.venv` in zsh?
- 왜: 문법 오류는 없다. 방법을 물을 땐 `How can I` 보다 `How do I` 가 흔하다. `can` 은 "가능하긴 한가"라는 뉘앙스가 살짝 섞인다.
