# 2026-09-27 — 코칭

> 오늘 내가 쓴 한국어는 auto-recipe-creator 의 SEM 아이콘 위치 설명 넷과 equipment-data-map 연구·스펙 지시 여섯. 한 메시지가 길면 둘로 나눠 (a) 카드 10장을 만들었다. (b) 는 equipment-data-map 에서 어시스턴트가 쓴 한국어 가운데 네 문장을 골랐다. 영어 다듬기는 44장. "commit and push", "review with codex, open a tab" 처럼 고칠 게 없는 짧은 명령은 뺐다. english-study 파이프라인 프롬프트, herdr·research·back-to-office 스킬 본문, 붙여 넣은 ftp_handler 리뷰 본문은 `[user]` 로 찍혔어도 내가 쓴 글이 아니라서 제외했다.

## 한글→영어

### 카드 1 — 윗부분이 잘린 상태   (내가 쓴 한글)
- 내가 쓴 한글: "from the images, strip은 윗부분이 잘린 상태. crosshair와 l_shape은 극히 일부분만 crop해서 사람이 볼 때도 오해할 수 있음. 여전히 mislocated mouse cursor."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: From the images, the top of the strip is cut off. The crosshair and L-shape crops show only a tiny part of each icon, so even a person could misread them. And the mouse cursor still lands in the wrong place.
- 왜 이렇게: "잘린 상태"처럼 명사로 끝나는 상태 묘사는 영어에선 `is cut off` 로 동사를 살린다. "극히 일부분만"은 `only a tiny part of`. "사람이 볼 때도"의 "도"는 `even a person` 으로 주어 앞에 `even` 을 둔다. "여전히 mislocated"는 형용사 하나로 두지 말고 `still lands in the wrong place` 처럼 문장으로 풀어야 무엇이 틀렸는지 보인다.

### 카드 2 — 아래부터 버튼 순서   (내가 쓴 한글)
- 내가 쓴 한글: "live sem box에서 오른쪽에는 맨 아래 DDS 버튼이 있음. 이걸 기준으로 아래부터 button들이 DDS, Next, ACD, AMS, 그림, AMP, empty button, 우물정자 shape, L shape, 네모, 십자가 (crosshair), =, ||. 이렇게 위치하고 있음. 그럼 더 프롬프트가 더 정확해지나?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: To the right of the live SEM box, the DDS button sits at the very bottom. Counting up from there, the buttons are DDS, Next, ACD, AMS, a picture icon, AMP, an empty button, a hash (#) shape, an L shape, a square, a crosshair, =, and ||. Would that make the prompt more accurate?
- 왜 이렇게: "이걸 기준으로 아래부터"는 `Counting up from there` 한 구로 기준과 방향을 함께 담는다. "위치하고 있음"은 `is located` 보다 `sits` 가 짧고 자연스럽다. "우물정자"는 `hash (#) shape`, 그림 아이콘은 `a picture icon`. "그럼 ~해지나?"는 가정이라 `Would that make … ?` 로 묻는다. 원문처럼 "더"를 두 번 쓰면 영어에서도 `more … more` 가 되니 한 번만 남겼다.

### 카드 3 — 한 칸씩 밀려 있다   (내가 쓴 한글)
- 내가 쓴 한글: "The location should be one button upward. 한칸씩 밀려있다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: They're all off by one button — each one should be a button higher.
- 왜 이렇게: "한 칸씩 밀려 있다"는 `off by one` 이 딱 맞는다. 개발자라면 아는 off-by-one error 의 그 표현이다. 방향까지 말하려면 `shifted down by one button`. `upward` 를 형용사처럼 쓰기보다 `a button higher` 로 비교급을 쓰면 짧다.

### 카드 4 — 왜 column.jpg 에서는 밀리지?   (내가 쓴 한글)
- 내가 쓴 한글: "여전히 failed. but locator 폴더 안에 있는 zoom in overlay 이미지들은 정확하게 locating을 하고 있는데 왜 column.jpg에서는 한칸씩 아래로 밀리는거지?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Still failing. The zoom-in overlay images in the locator folder show the right spots, so why is everything in column.jpg shifted down by one?
- 왜 이렇게: "~하고 있는데 왜 ~지?"는 대조와 의문이 한 문장에 겹친 꼴. 영어에선 앞을 사실로 끊고 `so why …?` 로 이으면 "그런데 왜"의 답답함이 산다. 이미지가 주어일 땐 "locating 을 한다"가 아니라 `show the right spots` 처럼 이미지가 할 수 있는 동사를 고른다. "여전히 failed"는 `Still failing.` 두 단어면 된다.

### 카드 5 — md 파일을 코드에 접목   (내가 쓴 한글)
- 내가 쓴 한글: "이걸 workflow agent로만들어내는 방법도 연구해서 알려줘. md 파일을 어떻게 코드로 접목시키는게 좋을까. langchain의 agent (create_agents) 를 고려중이야"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Also research how to build this as a workflow agent and let me know. What's the best way to bring the md files into the code? I'm considering LangChain's `create_agent`.
- 왜 이렇게: "~하는 방법도 연구해서 알려줘"는 `Also research how to … and let me know` 로 동사 두 개를 `and` 로 잇는다. "접목시키다"는 `bring into`, `wire into`, `integrate with` 가 자연스럽다. "어떻게 ~하는 게 좋을까"는 `What's the best way to …?`. "고려 중이야"는 `I'm considering` 뒤에 명사를 바로 붙인다. 동사를 붙일 땐 어제 카드처럼 `considering using` 이다.

### 카드 6 — 루프를 돌 때마다 더 정교하게   (내가 쓴 한글)
- 내가 쓴 한글: "active learning 방식으로 loop을 여러 번 돌아 파일끼리 구조를 파악하고 카테고리를 생성 (loop를 돌때마다 이미 생성된 wiki를 기반으로 더 정교하게 장비의 파일 구조를 파악하는게 목적이야)."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Run the loop several times, active-learning style, to work out how the files relate to each other and to build categories. The goal is for each pass to build on the wiki from earlier passes and understand the tool's file structure more precisely.
- 왜 이렇게: "~방식으로"는 명사 뒤에 `style` 을 붙여 부사처럼 쓴다(`active-learning style`). "파일끼리 구조를 파악하다"는 `how the files relate to each other` 가 관계를 정확히 짚는다. "~을 기반으로"는 `build on`. 앞에서 쌓은 결과 위에 올린다는 느낌이 산다. "~하는 게 목적이야"는 `The goal is for X to …` 로 주체를 넣는다.

### 카드 7 — 결과 나오면 Codex 와 토론해서 정리   (내가 쓴 한글)
- 내가 쓴 한글: "연구 결과가 나오면 codex (with herdr, open a tab) 와 discuss 해서 내용 정리해줘."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: When the research comes back, open a herdr tab, discuss it with Codex, and write up where you land.
- 왜 이렇게: "결과가 나오면"은 `comes back` 이 "돌려받는다"는 느낌까지 준다. 괄호 속 부가 지시(`with herdr, open a tab`)는 실제 순서대로 동사를 세워 풀었다. "내용 정리해 줘"는 토론 뒤라 `write up where you land`(어디로 결론이 났는지 정리)가 딱 맞는다. `summarize` 만 쓰면 결론 없는 요약이 돌아오기 쉽고.

### 카드 8 — 경로 노출, 설명 필요함   (내가 쓴 한글)
- 내가 쓴 한글: "wiki page에 디렉토리 경로 노출 한다. 사내 LLM은 GLM-5.3, Qwen3.8과 같은 모델 사용 중. openAI compatible. max_passes 기본값과 budget은 설명 필요함."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: We'll show directory paths on the wiki pages. Our in-house LLMs are models like GLM-5.3 and Qwen3.8, served through an OpenAI-compatible API. I'd like an explanation of the `max_passes` default and the budget.
- 왜 이렇게: "노출하다"를 `expose` 로 옮기면 보안 사고처럼 들린다. 일부러 보여 주기로 한 결정이면 `show` 나 `include` 가 맞다. "사내"는 `in-house`. "openAI compatible"은 따로 떼지 말고 `served through an OpenAI-compatible API` 로 앞 문장에 붙인다. "설명 필요함"은 `I'd like an explanation of …` 이나 `Can you explain …?` 로 요청 형태를 갖춘다.

### 카드 9 — 두 절 개정안 작성   (내가 쓴 한글)
- 내가 쓴 한글: "스펙 두 절 개정안 작성해줘"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Draft the revisions for those two sections of the spec.
- 왜 이렇게: "개정안 작성"은 명사 둘이지만 영어는 동사 `draft` 하나가 "안을 작성하다"를 다 품는다. `write a revision draft` 는 군더더기다. "절"은 문서에서 `section`. 앞에서 언급한 두 절이니 `those two` 로 가리킨다.

### 카드 10 — 하나씩인지 일괄인지   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 지금 파일 하나 받고 office llm이 그걸 읽고 정리하고 그런 순서로 진행하는 건지? 아니면 일단 일괄 받아놓고 정리하는 건지 어떤 순서로 진행하도록 되어있지?"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Also, what order is it set up to run in? Does it download one file, have the office LLM read and summarize it, and then move on? Or does it download everything first and process it afterward?
- 왜 이렇게: 한국어는 선택지 둘을 먼저 말하고 질문을 끝에 둔다. 영어는 `what order …?` 로 묻고 나서 선택지를 `Does it A? Or does it B?` 로 나눈다. "~하도록 되어 있지?"는 설계 의도를 묻는 `is it set up to` 로. "일괄"은 `everything first`, "일단 ~해 놓고"는 `first … afterward` 로 시간 순서를 드러낸다. "LLM 이 읽게 하다"는 사역 `have the LLM read`.

### 카드 11 — 같은 에이전트에 범위를 추가로   (고급 한글 · 번역)
- 한글 원문: "연구 에이전트가 아직 돌고 있으니, 새 에이전트를 띄우는 대신 같은 에이전트에 범위를 추가로 보내겠습니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: Since the research agent is still running, I'll send the extra scope to it instead of spinning up a new one.
- 번역 포인트: "띄우다"는 개발 영어에서 `spin up` 이 정해진 말이다(서버·컨테이너·에이전트). "돌고 있다"는 `is still running`. 같은 명사가 반복되면 영어는 대명사로 받는다. 두 번째 "에이전트"는 `it`, 세 번째는 `a new one`.

### 카드 12 — 수렴은 "맞다"가 아니다   (고급 한글 · 번역)
- 한글 원문: "정확도 목표로 `max_passes`를 정하지는 않습니다. 수렴 신호는 "할 일이 없다"이지 "맞다"가 아닙니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: We don't pick `max_passes` to hit an accuracy target. Convergence means "nothing left to do", not "correct".
- 번역 포인트: "~이지 ~가 아니다"는 영어 `A, not B` 와 짝이 딱 맞고 짧게 끊어 대비하는 리듬까지 같다. "수렴 신호는"을 `The convergence signal is` 로 옮겨도 되지만 `Convergence means` 가 더 짧고 정의처럼 들린다. "정하지는 않는다"의 대조 조사 "는"은 영어에 따로 표시할 필요 없음. 그 역할은 `to hit an accuracy target` 의 목적 부정사가 맡는다.

### 카드 13 — 표본을 한꺼번에 봐야   (고급 한글 · 번역)
- 한글 원문: "LLM은 파일군 전체의 통계와 여러 표본을 한꺼번에 봐야 의미를 말할 수 있고, 다운로드 budget과 승인 hash는 LLM이 도중에 범위를 넓힐 수 없을 때만 지켜집니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: The LLM can only say what a file family means once it sees the family's overall statistics and several samples together, and the download budget and approval hash only hold if the LLM can't widen the scope midway.
- 번역 포인트: "~해야 ~할 수 있다"는 `can only … once …` 로 조건을 뒤로 보낸다. `only` 는 조동사 뒤에 둬야 제한이 동사에 걸린다. "지켜지다"를 `be kept` 로 옮기면 약속처럼 들리니 조심. 보장이나 불변식이 유지된다는 뜻이면 `hold` 가 정확하다. "도중에"는 `midway` 나 `partway through`.

### 카드 14 — 필요해지면 그때 넓히면 된다   (고급 한글 · 번역)
- 한글 원문: "개정 범위를 줄이기 위해서이며, 필요해지면 그때 넓히면 됩니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: That keeps the revision small; we can widen it later if we need to.
- 번역 포인트: "~하기 위해서이며"처럼 이유를 명사절로 설명하는 한국어는 영어에서 앞 결정을 주어로 세우고 효과를 동사로 쓰면 자연스럽다(`That keeps …`). "그때 ~하면 된다"는 `we can … if we need to` 로 충분하다. 끝의 `to` 는 `widen it` 을 받는 대부정사라 동사를 반복하지 않는다.

## 영어 다듬기

### 카드 15 — mai-ui 가 틀리게 찾는다
- 내가 쓴 영어: "@poc/workflow_3/check_tool_occupancy.py fix the code. mai-ui locates wrongly."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `locates wrongly` → `locates the wrong row` (`locate` 는 타동사라 목적어가 필요하다)
- 더 나은 표현: Fix check_tool_occupancy.py — mai-ui is locating the wrong row.
- 왜: 무엇을 틀리게 찾는지 목적어를 넣어야 증상이 전달된다. 지금 벌어지는 문제라 진행형 `is locating` 이 자연스럽다.

### 카드 16 — 맨 오른쪽 열
- 내가 쓴 영어: "now you get the MC ID right, but the Connection User column is not inside the cropped image. It is located in the  far-right side."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `in the far-right side` → `on the far right` (측면·위치는 `on`, `side` 는 빼도 된다)
- 더 나은 표현: The MC ID is right now, but the Connection User column isn't in the crop. It's the column on the far right.
- 왜: `the cropped image` 는 `the crop` 한 단어로 줄인다. `It is located in` 보다 `It's the column on …` 이 짧고 구어답다.

### 카드 17 — Remote 도 잘못 읽힌다
- 내가 쓴 영어: "now the Remote column is also misread, fix it, not inside the cropped image."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 쉼표로 세 절을 이어 붙인 comma splice → 문장을 나눈다.
- 더 나은 표현: Now the Remote column is misread too — it isn't inside the crop either. Please fix it.
- 왜: 증상과 이유를 앞에 두고 요청은 끝에 따로 둔다. 부정문에서 "~도"는 `too` 가 아니라 `either`.

### 카드 18 — 두 배 길게
- 내가 쓴 영어: "row.jpg got the right row. in cells.jpg, MC ID should be half sized but Remote should be twice longer, Connection User lost the first two letters in the cropped image."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `twice longer` → `twice as long` (배수 비교는 `twice as + 원급`). `half sized` → `half as wide`.
- 더 나은 표현: row.jpg has the right row. In cells.jpg, the MC ID crop should be half as wide and the Remote crop twice as wide, and Connection User is missing its first two letters.
- 왜: 폭 이야기라 `long` 보다 `wide` 가 정확하다. 셋째 증상은 `and` 로 이어 목록을 닫는다.

### 카드 19 — Remote 는 잊고 Connection User 만
- 내가 쓴 영어: "faileld List 점유 판독 실패. invalid remote column bounds. forget about the column for remote 1, just check the column Connection User. and that is the last column in the RCS."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `faileld` → `failed` (오타). `the column Connection User` → `the Connection User column` (이름이 명사 앞에서 꾸민다).
- 더 나은 표현: It failed with "invalid remote column bounds". Forget the Remote 1 column and just check Connection User — it's the last column in RCS.
- 왜: 에러 메시지는 `failed with "…"` 로 인용하면 깔끔하다. 이유를 덧붙이는 `and that is …` 는 대시로 앞 문장에 붙인다.

### 카드 20 — 한 번에 다 찾게 하나?
- 내가 쓴 영어: "are you asking the vlm to locate all things mc id and Connection User at once?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `all things mc id and Connection User` → `both the MC ID and Connection User` (둘이면 `both`)
- 더 나은 표현: Are you asking the VLM to locate the MC ID and Connection User columns in a single call?
- 왜: `at once` 도 되지만 API 호출 이야기라 `in a single call` 이 정확하다. 약어 VLM, MC ID 는 대문자로 쓴다.

### 카드 21 — 여전히 unknown
- 내가 쓴 영어: "Connection User cell is now clipped well but when it is occupied  still occupancy reads as unknown. diagnosis fine mc id mismatch. but you get the name right."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 관사 `The Connection User cell`. `still occupancy reads` → `occupancy still reads` (`still` 은 일반동사 앞).
- 더 나은 표현: The Connection User cell is cropped correctly now, but an occupied cell still reads as unknown. The diagnosis says fine_mc_id_mismatch, even though you read the name correctly.
- 왜: `clip` 은 "끝이 잘려 나가다"라 잘 잘렸다는 칭찬엔 `crop` 이 맞다. 마지막 `but` 은 `even though` 로 바꿔 대조를 한 문장에 담았다.

### 카드 22 — 일부러 빈 장비를 골랐다
- 내가 쓴 영어: "I intentionally pick the unoccupied tool name and it fails as detected as occupied by others"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 이미 한 일이라 `pick` → `picked`. `it fails as detected as occupied` → `it was detected as occupied`.
- 더 나은 표현: I deliberately picked a free tool, and it was flagged as occupied by someone else.
- 왜: `as … as …` 가 겹치면 읽기 어렵다. 판정 결과는 `was flagged as` 한 구로 충분하다.

### 카드 23 — Control 접두어가 없으면 빈 것
- 내가 쓴 영어: "actually unoccupied but it reads as occupied. failed!. user_connection_user_ocr.txt reads as [Table_Page_Number] when it is empty. in the text, if you do not read Control as prefix, then no one occupied the tool"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 주어가 필요하다(`It's actually unoccupied`). `failed!.` 구두점 중복. `as prefix` → `as a prefix`. `no one occupied` → `no one is using` (지금 상태라 현재형).
- 더 나은 표현: It's actually free, but it reads as occupied, so it failed. When the cell is empty, user_connection_user_ocr.txt contains [Table_Page_Number]. If the text doesn't start with "Control", nobody is using the tool.
- 왜: `if you do not read Control as prefix` 는 `doesn't start with "Control"` 로 규칙을 텍스트 기준으로 쓰면 코드로 옮기기 쉽다.

### 카드 24 — 이제 된다
- 내가 쓴 영어: "now works. free tool reads free, occupied reads occupied. we can use this code for checking for the occupance in @align_fail_monitor.py"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `now works` → `It works now` (주어). `occupance` → `occupancy`. `for checking for` → `for the check` (전치사 중복).
- 더 나은 표현: It works now: a free tool reads free and an occupied one reads occupied. Let's use this code for the occupancy check in align_fail_monitor.py.
- 왜: 결과를 콜론 뒤에 붙이면 "된다 → 이렇게 된다"가 한 흐름이 된다. 제안은 `Let's` 로.

### 카드 25 — 새 방식 반영했어?
- 내가 쓴 영어: "have you modified the manual_align_correction.py based on the new search around method and recently updated code?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 파일 이름 앞 `the` 는 뺀다. `search around method` → `search-around method` (명사를 꾸밀 땐 하이픈).
- 더 나은 표현: Have you updated manual_align_correction.py to reflect the new search-around method and the recent changes?
- 왜: `based on` 보다 `to reflect` 가 "새 내용을 반영했냐"를 정확히 묻는다.

### 카드 26 — 커서는 맞는데 화면이 안 움직인다
- 내가 쓴 영어: "When you locate the align point based on the algorithm, you place the mouse position correctly but no move to the point (in the live sem box, you have to click twice to move the position therefore the position is centered in the live sem monitor."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `no move to the point` → `the view doesn't move there` (동사 필요). `therefore` 는 접속사가 아니라 절을 못 잇는다 → `so that`. 괄호가 닫히지 않았다.
- 더 나은 표현: When you locate the align point, the cursor lands in the right spot, but the view doesn't move there. In the live SEM box you have to double-click to recenter the view on that point.
- 왜: `place the mouse position` 은 `the cursor lands` 로 주어를 커서로 바꾸면 짧다. `click twice to move … so that … is centered` 는 `double-click to recenter` 한 구로 줄어든다.

### 카드 27 — 흔한 OK 버튼
- 내가 쓴 영어: "and I found some bugs from there. you place the right position and move straight to the OK button. but given that OK buttons is quite commmon button, you click the ok button in the wrong window."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `OK buttons is` → `OK is` (단수 일치). `commmon` → `common`. 이미 벌어진 일이라 `you click` → `you clicked`.
- 더 나은 표현: I found a bug there too: you place the cursor correctly and go straight to OK, but since OK is such a common button, you clicked the OK in the wrong window.
- 왜: `given that` 은 문어라 대화에선 `since` 가 편하다. `such a common button` 이 "워낙 흔한"의 강조를 살린다.

### 카드 28 — 십자 아이콘과 L 자 아이콘
- 내가 쓴 영어: "one more thing to note, in the live sem box, you have crosshair icon and L shaped icon. when crosshair icon is clicked, you have to double clicks to move around in the live sem box and when L shaped icon is clicked, you can move around with a single click."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 관사 `a crosshair icon and an L-shaped icon`. `double clicks` → `double-click` (동사). `L shaped` → `L-shaped`.
- 더 나은 표현: One more thing: the live SEM box has a crosshair icon and an L-shaped icon. With the crosshair selected, you double-click to move around; with the L-shape selected, a single click does it.
- 왜: 두 모드를 `With A selected, …; with B selected, …` 로 맞추면 대비가 한눈에 보인다.

### 카드 29 — 아무 장비에서나?
- 내가 쓴 영어: "click_mode can be tested in any tools?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 의문문 어순 `Can click_mode be tested …?`. `any tools` → `any tool` ("어느 것이든"의 `any` 는 단수와 잘 어울린다).
- 더 나은 표현: Can I test click_mode on any tool?
- 왜: 사람을 주어로 세우면 수동태 없이 짧아진다. 장비 "위에서" 돌리는 거라 `on`.

### 카드 30 — 더 자세한 프롬프트?
- 내가 쓴 영어: "click_mode is not detected.  maybe we need to give more detailed prompt? or use method like coarse to fine? the icons is located to the right side of the live sem box.. the icons are aligned vertically."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 관사 `a more detailed prompt`, `a method like coarse-to-fine`. `the icons is` → `the icons are`.
- 더 나은 표현: click_mode isn't detecting anything. Should we give it a more detailed prompt, or try a coarse-to-fine approach? The icons sit in a vertical column to the right of the live SEM box.
- 왜: 감지가 안 되는 건 모드가 아니라 기능이 못 찾는 거라 능동 `isn't detecting` 이 맞다. 위치와 정렬 두 문장은 `sit in a vertical column` 하나로 합친다.

### 카드 31 — 세 번째, 다섯 번째
- 내가 쓴 영어: "the crosshair icon is in the third position from the top. the L shape icon is the fifth"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: The crosshair is the third icon from the top, and the L-shape is the fifth.
- 왜: 문법 오류는 없다. `in the third position` 보다 `the third icon` 이 짧다. 두 문장을 `and` 로 이으면 뒤쪽 명사도 생략된다.

### 카드 32 — 조금 아래로
- 내가 쓴 영어: "you located almost there but the both are located a bit lower side so that place in the wrong icons."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the both` → `both`. `a bit lower side` → `a bit too low`. `so that place in` → `so they land on`.
- 더 나은 표현: You're close, but both points are slightly too low, so they land on the wrong icons.
- 왜: "거의 다 왔다"는 `You're close` 가 관용이다. `too low` 의 `too` 가 "원하는 곳보다 지나치게"를 담는다.

### 카드 33 — 흐릿한 라벨
- 내가 쓴 영어: "OCR='A\nN' 거부. next run read "N", strip you get the right size of width. AMP, AMS, ACD, Next. those texts look vague. DDS looks clean (activated button). or you can approach from the top to search || button. right below you have ="   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the right size of width` → `the right width`. `those texts` → `those labels` (`text` 는 보통 셀 수 없다). `to search || button` → `to search for the || button`.
- 더 나은 표현: The next run read "N". The strip width is right now. The AMP, AMS, ACD and Next labels are faint, but DDS is clear because it's the active button. Or you could work down from the top: find the || button, and = is right below it.
- 왜: 글씨가 흐린 건 `vague`(뜻이 모호함)가 아니라 `faint`. `search` 는 "장소를 뒤지다"라 찾는 대상 앞엔 `for` 가 붙는다.

### 카드 34 — 등호 바로 아래
- 내가 쓴 영어: "you anchored equal sign correctly. the crosshair right below the eqaul sign. and you have square shape button. below of the square button, you have L shaped button."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the crosshair right below` → `the crosshair is right below` (동사 누락). `eqaul` → `equals`. `below of` → `below`. 관사 `a square button`, `the L-shaped button`.
- 더 나은 표현: You anchored the equals sign correctly. The crosshair is right below it, then a square button, and below the square is the L-shaped button.
- 왜: 위에서 아래로 나열할 땐 `then` 으로 이어 가면 된다. 마지막은 도치 `below the square is …` 로 위치를 앞에 둬 흐름을 살렸다.

### 카드 35 — 우리 목표는
- 내가 쓴 영어: "from the locator debugging, they are located correctly with zoom-in of mai-ui. But the our target is to locate crosshair and l_shape. still 미검출."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the our` → `our` (소유격과 관사는 같이 못 쓴다). 관사 `the crosshair and the L-shape`.
- 더 나은 표현: The locator debug images show them in the right place with mai-ui's zoom-in, but what we actually need is the crosshair and the L-shape, and those still aren't detected.
- 왜: `what we need is …` 로 강조 구문을 쓰면 "근데 정작 필요한 건"이 산다.

### 카드 36 — 한 칸씩 아래로
- 내가 쓴 영어: "from the column, I see that they all are shifted downward. The location should be one button upward."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `they all are` → `they are all` (`all` 은 be 동사 뒤)
- 더 나은 표현: In column.jpg, everything is shifted down by one button; each box should be one button higher.
- 왜: `downward` / `upward` 보다 `down by one` / `higher` 가 짧다. 한글 카드 3의 `off by one` 도 같은 자리에 쓸 수 있다.

### 카드 37 — 왜 직접 안 찾아?
- 내가 쓴 영어: "failed. in locator why do you not create crosshair and L shaped cases?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `why do you not` → `why don't you` (구어에선 축약). 뜻상 `create … cases` 보다 `locate … directly`.
- 더 나은 표현: It failed. Why doesn't the locator look for the crosshair and the L-shape directly?
- 왜: "케이스를 만든다"는 한국어식 표현이다. 영어로는 무엇을 찾게 하는지 동사로 바로 말한다.

### 카드 38 — 이런 일에 맞는 에이전트
- 내가 쓴 영어: "on what is the best way to make agents for this kind of jobs? should I use library like langchain create_agents? now we are focusing on the parsing data from tools but eventually, I would like to service this one to teammates so that they can use general cases."   (출처: transcript:[user] equipment-data-map)
- 정정: `this kind of jobs` → `this kind of job` (단수) 또는 `these kinds of jobs`. `library like` → `a library like`. `the parsing data` → `parsing data`. `service this one to teammates` → `offer this to teammates` (`service` 동사는 "정비하다").
- 더 나은 표현: What's the best way to build agents for this kind of job? Should I use a library like LangChain's `create_agent`? Right now we're focused on parsing tool data, but eventually I'd like to offer this to teammates for general use.
- 왜: `this kind of` 뒤엔 단수 명사가 짝이다. `so that they can use general cases` 는 `for general use` 두 단어로 줄어든다.

### 카드 39 — 사람이 읽을 수 있는 형식
- 내가 쓴 영어: "the parsed data should be human-readable (like llm-wiki, and obsidian). think about the data format the best possible way."   (출처: transcript:[user] equipment-data-map)
- 정정: `the best possible way` 앞에 `in` 이 필요하다. 다만 뜻을 살리면 `the best possible data format` 이 낫다.
- 더 나은 표현: The parsed data should be human-readable, like an LLM wiki or an Obsidian vault, so think hard about the best data format.
- 왜: 예시 둘은 `like A or B`. `think hard about` 이 "제대로 고민해 달라"를 자연스럽게 전한다.

### 카드 40 — 문서도 갱신
- 내가 쓴 영어: "based on this update, also update contents in docs"   (출처: transcript:[user] equipment-data-map)
- 정정: `contents in docs` → `the docs` (`contents` 는 목차·내용물 느낌)
- 더 나은 표현: Based on this update, please update the docs as well.
- 왜: `also` 를 동사 앞에 두는 것보다 `as well` 을 문장 끝에 두는 편이 부드럽다.

### 카드 41 — HTML 파일 어디 있어?
- 내가 쓴 영어: "where is the corsshair explanation html file?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `corsshair` → `crosshair` (오타). `html` → `HTML`.
- 더 나은 표현: Where's the HTML file that explains the crosshair?
- 왜: 명사 세 개를 쌓은 `crosshair explanation html file` 은 관계절로 풀면 읽기 쉽다.

### 카드 42 — OpenCode 탭 열고 부탁해
- 내가 쓴 영어: "open a opencode with herdr (new tab) and ask him to generate html file to explain the crosshair overlay method (center and align point and its drift or skew should be inlcuded in the explanation)."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `open a opencode` → `open OpenCode` (제품명엔 관사 없음, 붙인다면 모음 앞 `an`). `him` → `it`. `html file` → `an HTML file`. `inlcuded` → `included`.
- 더 나은 표현: Open OpenCode in a new herdr tab and ask it to write an HTML page explaining the crosshair overlay method, covering the center, the align point, and any drift or skew.
- 왜: 괄호 속 요구 사항은 분사 `covering …` 으로 문장 안에 넣는다.

### 카드 43 — codex-maker 에게 고쳐 달라고
- 내가 쓴 영어: "based on the review result, ask to renovate the html to codex-maker with herdr."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `ask to renovate the html to codex-maker` → `ask codex-maker to revise the HTML` (`ask + 사람 + to 부정사`)
- 더 나은 표현: Based on the review, use herdr to ask codex-maker to revise the HTML.
- 왜: `renovate` 는 건물을 리모델링할 때 쓴다. 문서는 `revise`, `rework`, 크게 뜯어고치면 `overhaul`.

### 카드 44 — 이미 켜져 있다
- 내가 쓴 영어: "codex-maker is already on."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: codex-maker is already running in its own tab.
- 왜: 문법은 맞다. 다만 `on` 은 기계 전원 느낌이라 에이전트엔 `running` 이 자연스럽다. 탭 위치를 덧붙이면 새로 열지 말라는 뜻까지 전해진다.

### 카드 45 — API 키 필요해?
- 내가 쓴 영어: "do ftp_handler need api key?"   (출처: transcript:[user] equipment-data-map)
- 정정: 3인칭 단수 주어 → `Does`. 관사 `an API key`.
- 더 나은 표현: Does ftp_handler need an API key?
- 왜: 모듈 이름도 3인칭 단수다. `an` 은 API 의 첫소리 "에이"가 모음이라서.

### 카드 46 — 토큰 없음
- 내가 쓴 영어: "no token, it's trusted single user"   (출처: transcript:[user] equipment-data-map)
- 정정: 관사 `a single trusted user`
- 더 나은 표현: No token — it's used by a single trusted user.
- 왜: 형용사가 둘이면 수량 `single` 이 성질 `trusted` 앞에 오는 게 자연스럽다. 프록시가 사용자인 건 아니라 `it's used by` 로 관계를 바로잡았다.

### 카드 47 — git 문제를 깨달았다
- 내가 쓴 영어: "I realized that there is git issue as the office llms continue to update the contents inside equipment-data-parser. we have to separate the jobs from here home and the office so that makes git clean."   (출처: transcript:[user] equipment-data-map)
- 정정: 관사 `a git issue`. `from here home and the office` → `between home and the office`. `so that makes git clean` → `so that git stays clean`.
- 더 나은 표현: I've realized we have a git problem: the office LLMs keep changing files inside equipment-data-parser. We need to split the work between home and the office so the history stays clean.
- 왜: 둘로 나누는 건 `between A and B`. `so that` 뒤엔 주어+동사 절이 온다. `continue to update` 보다 `keep changing` 이 "자꾸 건드린다"는 불만을 살린다.

### 카드 48 — 이제 폴더를 안 건드려?
- 내가 쓴 영어: "so now, the office llm no edit in the parser folder and write in a separate folder?"   (출처: transcript:[user] equipment-data-map)
- 정정: `no edit` → `doesn't edit` (동사 부정은 조동사로)
- 더 나은 표현: So now the office LLM doesn't touch the parser folder and writes to a separate folder instead?
- 왜: 평서문에 물음표만 붙여 확인하는 질문은 구어에서 흔하다. 주어가 3인칭 단수라 `writes`. `instead` 가 "대신"을 채운다.

### 카드 49 — Codex 에게 도움 청하기
- 내가 쓴 영어: "yes. ask for the help how to set properly to codex via herdr by opening a new tab."   (출처: transcript:[user] equipment-data-map)
- 정정: `ask for the help how to set properly to codex` → `ask Codex how to set this up properly`. 어제 나온 `ask Codex for a review` 와 같은 틀로, 묻는 상대를 `ask` 바로 뒤에 둔다. `set` 은 `set up` 으로.
- 더 나은 표현: Yes. Open a new herdr tab and ask Codex how to set this up properly.
- 왜: `ask + 사람 + 의문사절` 이 가장 짧다. 수단(`by opening a new tab`)은 동사로 앞에 세운다.

### 카드 50 — 브랜치 있어? main 에 합쳐
- 내가 쓴 영어: "do we have branch?" / "merge into the main."   (출처: transcript:[user] equipment-data-map)
- 정정: `branch` → `any other branches` (셀 수 있는 명사). `the main` → `main` (브랜치 이름엔 관사 없음).
- 더 나은 표현: Do we have any other branches? / Merge it into main.
- 왜: 있는지 묻는 질문엔 `any` 가 짝이다. 합칠 대상 `it` 을 넣어야 명령이 완성된다.

### 카드 51 — 결과는 손으로 가져올게
- 내가 쓴 영어: "yes. I will bring you findings by hand."   (출처: transcript:[user] equipment-data-map)
- 정정: 관사 `the findings` (앞에서 말한 그 결과)
- 더 나은 표현: Yes, I'll bring the findings over by hand.
- 왜: `bring … over` 는 "이쪽으로 옮겨 오다"라서 사무실에서 집으로 가져오는 그림이 산다.

### 카드 52 — 어떻게 시작해?
- 내가 쓴 영어: "how Do i begin?"   (출처: transcript:[user] equipment-data-map)
- 정정: 대소문자 `How do I begin?`
- 더 나은 표현: Where do I start?
- 왜: 절차를 물을 땐 `Where do I start?` 나 `How do I get started?` 가 더 흔하다.

### 카드 53 — 00 완료
- 내가 쓴 영어: "00 done, dirs=5 files=106, llm_success=3 llm_failed=0, no modification needed to spike.py. all steps completed."   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Letter 00 is done: dirs=5, files=106, llm_success=3, llm_failed=0. spike.py didn't need any changes, and every step completed.
- 왜: 메모체라 오류라고 할 건 없다. 숫자는 콜론 뒤에 몰고 사실은 완전한 문장으로 쓰면 보고서로 옮겨 붙이기 좋다.

### 카드 54 — #6 댓글 진행해
- 내가 쓴 영어: "go ahead for #6 comment" / "what do I need to do now"   (출처: transcript:[user] equipment-data-map)
- 정정: `go ahead for` → `go ahead with` (진행할 대상 앞은 `with`). 관사 `the #6 comment`. 질문엔 물음표.
- 더 나은 표현: Go ahead and post the comment on #6. / What do I need to do next?
- 왜: `go ahead and + 동사` 가 "그럼 해"라는 허락에 가장 흔하다. "이제 뭐 해?"는 `now` 보다 `next` 가 순서를 묻는 말이다.

### 카드 55 — Inferred 는 틀렸다
- 내가 쓴 영어: "Inferred is a kind of wrong. As it doesn't know the detail of the tool by looking at the single folder. We first defer inferred, instead more focus on observed. (later we infer from observed facts)"   (출처: transcript:[user] equipment-data-map)
- 정정: `a kind of wrong` → `kind of wrong` (부사 `kind of` 앞엔 관사가 없다). `As it doesn't …` 는 종속절만 있는 문장 조각 → 앞 문장에 붙인다. `the single folder` → `a single folder`. `instead more focus on` → `and focus more on`.
- 더 나은 표현: Inferred is kind of wrong, because the model can't know the tool's details from a single folder. Let's defer Inferred for now and focus on Observed; we can infer from the observed facts later.
- 왜: 이유는 `because` 로 앞 문장에 붙이는 게 안전하다. 괄호 속 계획은 세미콜론 뒤 문장으로 살렸다.

### 카드 56 — 제외할 확장자
- 내가 쓴 영어: "and we should exclude some file extensions with .bak, .iso, .lock. also contain string like temp, tmp in file name."   (출처: transcript:[user] equipment-data-map)
- 정정: `extensions with .bak` → `extensions like .bak`. 둘째 문장은 주어가 없다 → `and any file whose name contains …`.
- 더 나은 표현: We should also skip files with extensions like .bak, .iso and .lock, and any file whose name contains temp or tmp.
- 왜: 소유격 관계대명사 `whose name contains` 가 "이름에 ~이 들어간 파일"을 한 번에 표현한다.

### 카드 57 — 그게 무슨 말이야?
- 내가 쓴 영어: "what's infered verdict?"   (출처: transcript:[user] equipment-data-map)
- 정정: `infered` → `inferred` (r 두 개). 관사 `the`.
- 더 나은 표현: What do you mean by "Inferred verdict"?
- 왜: 상대가 쓴 말을 되물을 땐 `What do you mean by …?` 가 정해진 틀이다. 따옴표로 상대 표현임을 표시한다.

### 카드 58 — 제안된 수정 사항
- 내가 쓴 영어: "for the ftp_handler, here is the suggested fixes. … With your decision, amend the code if necessary."   (출처: transcript:[user] equipment-data-map)
- 정정: `here is the suggested fixes` → `here are` (복수 일치). `With your decision` → `Use your judgment`.
- 더 나은 표현: Here are the suggested fixes for ftp_handler. Use your judgment and change the code where needed.
- 왜: `here is/are` 는 뒤의 명사에 수를 맞춘다. "판단에 맡긴다"는 `Use your judgment` 나 `It's your call` 이 자연스럽다.
