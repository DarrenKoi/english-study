# 2026-09-22 — 코칭

> 오늘 `[user]` 한국어는 auto-recipe-creator 세션 2건과 equipment-data-map 세션 1건이다. 긴 메시지 하나(SEM search-around 와 OM-D)를 두 장으로 나눠 (a) 카드는 12장. (b) 는 equipment-data-map 세션의 어시스턴트 한국어에서 4문장을 골랐다. 영어 다듬기는 auto-recipe-creator 2건과 skewnono 3건으로 5장이고 고칠 데가 없는 `commit and push` 는 뺐다. 일부러 제외한 글도 있다. back-to-office·journal·browser-verify·agent-browser 스킬 본문과 english-study 세션의 파이프라인 프롬프트는 `[user]` 로 찍혔어도 내가 쓴 글이 아니라서.

## 한글→영어

### 카드 1 — 녹화 여러 개를 이어 붙여 영상으로   (내가 쓴 한글)
- 내가 쓴 한글: "@poc/workflow_3/monitor/manual_align_correction.py 하고 난 뒤 몇몇 recording들은 영상으로 만들고 싶어. 어떻게 하면 될까? 폴더 리스트들이 여러개 인 경우 하나로 이어 붙여서 (1st trial, 2nd trail)이런식으로 쭉 연결해서 영상으로 만들고 싶어."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: After running `manual_align_correction.py`, I'd like to turn some of the recordings into videos. How should I go about it? When there are several folders, I want to stitch them into one video, labeled "1st trial", "2nd trial", and so on.
- 왜 이렇게: "~하고 난 뒤"는 동명사 `After running …` 으로 짧아진다. "영상으로 만들다"는 `turn X into a video`, "이어 붙이다"는 `stitch together` 가 영상 편집에서 흔히 쓰는 말이고 기술적으로는 `concatenate`. "이런 식으로 쭉"은 목록 끝의 `and so on` 한마디면 된다. "폴더 리스트들이 여러 개인 경우"에서 "리스트"는 영어로 옮길 필요가 없다(`When there are several folders`). 괄호 속 `2nd trail` 은 오타다. `trail` 은 "자취, 오솔길"이고 "시도"는 `trial`.

### 카드 2 — 리뷰 진행해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "@docs/architecture/equipment-data-map.md review 진행해줘."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Please review `docs/architecture/equipment-data-map.md`.
- 왜 이렇게: "진행해 줘"를 `proceed with the review` 로 옮기면 이미 시작한 리뷰를 이어 가라는 말로 들린다. 새로 맡기는 일은 동사 하나 `review` 로 충분하다. 범위를 좁히고 싶다면 `Can you review … and flag anything that conflicts with the letters?` 처럼 무엇을 봐 달라는지 덧붙이자.

### 카드 3 — 추천대로 전부 고쳐 줘   (내가 쓴 한글)
- 내가 쓴 한글: "추천대로 전부 수정해줘"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Go ahead and fix everything as you recommended.
- 왜 이렇게: "~대로"는 `as you recommended`, 글에서는 `per your recommendations`. "전부 수정해"를 `apply all of your recommendations` 로 하면 리뷰 항목을 하나씩 반영하라는 뜻이 더 또렷해진다. `Go ahead and …` 가 허락의 어감을 얹는다.

### 카드 4 — 그렇게 커밋해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "그렇게 커밋 진행해줘"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Sounds good. Commit it that way.
- 왜 이렇게: "그렇게"가 가리키는 건 바로 앞 제안(문서 네 개를 같은 커밋에 넣자)이라 `that way`. 무엇을 받아들였는지 밝히고 싶으면 `Commit them together, as you suggested.` "진행해 줘"는 이번에도 영어에서 사라진다.

### 카드 5 — push 하고 이제 office 에서는?   (내가 쓴 한글)
- 내가 쓴 한글: "push 해줘. 어떻게 office에서 진행하면 되지 이제?"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Please push it. So what do I do at the office now?
- 왜 이렇게: "어떻게 진행하면 되지"를 `How should I proceed?` 로 옮겨도 틀리지 않지만 구어로는 `What do I do now?` 나 `How do I take it from here?` 가 가볍다. "이제"는 `now` 로 문장 끝에 둔다. 장소 "office 에서"는 `at the office`. `in the office` 라고 하면 건물 안이라는 점이 두드러진다.

### 카드 6 — 스크립트를 돌렸더니 이런 줄이 나왔다   (내가 쓴 한글)
- 내가 쓴 한글: "rest_model_folder 했을 때 changed letters already marked done: 02 12 가 나왔어."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: When I ran `reset_model_folder`, it printed "changed letters already marked done: 02 12".
- 왜 이렇게: "~했을 때"의 "하다"는 스크립트라 `ran`. "~가 나왔어"는 스크립트를 주어로 세운 `it printed …` 나 나를 주어로 한 `I got …`. 출력 문구는 따옴표로 감싸야 설명과 섞이지 않는다. `rest_` 는 `reset_` 의 오타.

### 카드 7 — 08 은 목록에 없어   (내가 쓴 한글)
- 내가 쓴 한글: "08은 목록에 없어."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: 08 isn't in the list the script printed.
- 왜 이렇게: `08 isn't on the list.` 로도 뜻은 통한다. 그런데 어시스턴트는 곧바로 "목록"이 스크립트 출력인지 ledger 인지 되물어야 했다. 어느 목록인지 관계절(`the list the script printed`)로 붙였다면 한 번에 끝났을 일. 명단은 `on the list`, 출력·데이터 목록은 `in the list` 가 흔하다.

### 카드 8 — wip 뒤에 다음 날 done 으로 찍혀 있다   (내가 쓴 한글)
- 내가 쓴 한글: "progress.md에 tktlf 02, 12 전부 wip 이후 다음 날 done으로 찍혀있어. 과거에 진행했던 progress들이 다 남아있네."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Actually, in `progress.md`, both 02 and 12 show `wip` followed by `done` the next day. Looks like all the old progress entries are still there.
- 왜 이렇게: `tktlf` 는 한영 전환 없이 친 "사실"이다. 영어로는 문장 앞 `Actually,` 가 그 자리다. 로그에 "~로 찍혀 있다"는 `show` 나 `be logged as`. "A 이후 다음 날 B"는 `A followed by B the next day` 로 순서를 그대로 따라간다. "남아 있네"의 "~네"는 새로 알아챈 어감이라 `Looks like …` 가 맞다. 주어 `It` 까지 떨어뜨리면 구어답다.

### 카드 9 — 어떻게 진행하면 될까   (내가 쓴 한글)
- 내가 쓴 한글: "어떻게 진행하면 될까"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: OK, so where do we go from here?
- 왜 이렇게: 카드 5와 같은 질문이 한 세션에 두 번 나왔다. 매번 `How should I proceed?` 로 옮기면 단조로우니 바꿔 가며 쓰자. `What's next?`(가장 짧음), `Where do we go from here?`(상황을 정리하고 방향을 묻는 말), `Walk me through the next steps.`(절차를 차근차근 알려 달라).

### 카드 10 — 저널 써 줘   (내가 쓴 한글)
- 내가 쓴 한글: "journal 작성해줘"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Can you write up a journal entry for this session?
- 왜 이렇게: "작성하다"를 `write` 가 아니라 `write up` 으로 하면 흩어진 내용을 정리해 문서로 만든다는 뜻까지 담긴다. `journal` 은 일지 전체라 한 번 쓰는 글은 `a journal entry`.

### 카드 11 — OM/SEM 은 방식이 다르고 OM-D 도 있다   (내가 쓴 한글)
- 내가 쓴 한글: "이제 SEM Search Around도 해야해. 알다시피 OM/SEM은 다른 방식이야. 그리고 OM-D도 있었어. OM (dark mode) 이 경우 OM의 이미지가 반전되기 때문에 OM-D일 때는 Live SEM Box 근처에 있는 Image Dropdown 화살표 선택 후 OM-D로 바꿔야해."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Next we need SEM search-around too. As you know, OM and SEM work differently. There's also OM-D, which is OM in dark mode. The image is inverted, so for OM-D you have to open the Image dropdown arrow near the Live SEM box and switch it to OM-D.
- 왜 이렇게: "~은 다른 방식이야"는 `are different methods` 보다 `work differently` 가 자연스럽다. "OM-D 도 있었어"를 과거형으로 옮기면 지금은 없다는 말이 된다. 한국어의 "있었어"는 "깜빡했는데 ~도 있다"는 상기의 어감이라 영어는 현재형 `There's also …`. 괄호 풀이 `OM (dark mode)` 는 관계절 `which is OM in dark mode` 로 녹인다. "~이기 때문에 ~해야 해"는 원인을 먼저 짧게 말하고 `so` 로 잇는 편이 구어에서 가볍다.

### 카드 12 — 버튼 위치를 알려 주고 코드를 부탁하다   (내가 쓴 한글)
- 내가 쓴 한글: "dropdown 버튼은 Optics... & OM ABC 버튼 위에 자리잡고 있어. 버튼을 발견하고 변경하는 코드를 만들어줘. manual_image_mode_change.py로 만들어줘."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The dropdown sits just above the "Optics..." and "OM ABC" buttons. Write a script that finds it and changes the mode, and call it `manual_image_mode_change.py`.
- 왜 이렇게: "자리 잡고 있다"는 위치 설명에서 `sit` 가 가장 가볍다. 글이라면 `is located`. "발견하고 변경하는 코드"는 관계절 `a script that finds … and changes …`. `discover` 는 몰랐던 것을 알아낸다는 뜻이라 화면에서 찾는 일에는 `find` 나 `locate`. 파일 이름을 정하는 "~로 만들어 줘"는 `call it …` 이나 `name it …`. 두 번 나온 "만들어 줘"는 한 문장으로 합쳤다.

### 카드 13 — 사람용 설계서이면서 동시에 프롬프트   (고급 한글 · 번역)
- 한글 원문: "이 문서는 사람용 설계서이면서 동시에 저사양 LLM의 프롬프트입니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: This document is a design spec for people, and it doubles as the prompt for a low-end LLM.
- 번역 포인트: "~이면서 동시에 ~이다"를 `both A and B` 로 옮겨도 되지만 `double as`(~를 겸하다)가 한 역할이 다른 역할을 떠맡는다는 뉘앙스까지 살린다. "사람용"은 `for people` 이나 `human-facing`. "저사양 LLM"은 `low-end LLM` 이 짧다. 더 공손하게는 `a smaller, less capable model`.

### 카드 14 — 둘로만 나누는데 제3의 상태다   (고급 한글 · 번역)
- 한글 원문: "머리말은 절을 "현행"과 "목표" 둘로만 나누는데, 이 문단은 "오프라인에는 구현됐지만 letter 계약은 아닌" 제3의 상태입니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: The preamble sorts sections into just two kinds, "current" and "target", but this paragraph is in a third state: implemented offline, yet not part of any letter's contract.
- 번역 포인트: "~으로만 나누다"는 `sort into just two kinds` 로 `just` 가 "~만"을 맡는다. 한국어는 "~아닌 제3의 상태"처럼 긴 수식을 명사 앞에 쌓지만 영어는 `a third state` 를 먼저 말하고 콜론 뒤에서 풀어 준다. "~됐지만 ~는 아닌"은 과거분사 `implemented` 와 `yet not …` 을 맞세우면 동사 없이도 대조가 선다.

### 카드 15 — 확실히 배제하는 대신 치르는 값   (고급 한글 · 번역)
- 한글 원문: "scope ID에 epoch을 넣은 결정은 stale 자료를 확실히 배제해 줍니다. 그 대신 설정이 조금만 바뀌어도 전부 재수집해야 합니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: Putting the epoch in the scope ID reliably keeps stale data out. The price is that even a small config change forces a full re-collection.
- 번역 포인트: "~을 넣은 결정은"을 `The decision to put …` 으로 옮기면 무겁다. 동명사 `Putting …` 을 주어로 세우면 결정의 내용이 곧 주어가 된다. "배제해 준다"는 `keep … out`. "그 대신"은 `instead` 가 아니라 `The price is that …` 이나 `The trade-off is that …` 이 맞다. 대안이 아니라 대가를 말하는 자리라서다. "~해야 한다"는 사람 주어를 찾지 말고 `a small change forces …` 처럼 무생물 주어에 맡긴다.

### 카드 16 — 확인하지 않고 단정한 제 실수   (고급 한글 · 번역)
- 한글 원문: "제가 "다시 빌드되는 letter는 없다"고 한 것은 오늘 커밋만 따진 결과였습니다. office가 어느 커밋까지 받았는지 확인하지 않고 단정한 제 실수입니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: When I said no letters would be rebuilt, I was only looking at today's commit. That was my mistake: I stated it as fact without checking which commit the office had last pulled.
- 번역 포인트: "~고 한 것은 ~한 결과였다"를 `What I said was the result of …` 로 직역하면 어색하다. `When I said …, I was only looking at …` 으로 시점과 원인을 나누자. 간접화법이라 `will` 이 `would` 로 물러났다. "단정하다"는 `state it as fact` 나 `assert`. "어느 커밋까지 받았는지"는 간접의문문 `which commit the office had last pulled`. 확인하지 않은 시점보다 앞선 일이라 과거완료로 썼다. 콜론 뒤에 실수의 내용을 풀면 사과가 구체적으로 들린다.

## 영어 다듬기

### 카드 1 — cond.txt 에서 모드를 읽고 있나
- 내가 쓴 영어: "I am not sure we have extract mode condition like OM/SEM from cond.txt when align point is corrected."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `we have extract mode condition` → `we extract the mode condition`. `have` 뒤에 동사원형을 바로 붙일 수 없다(완료형 `have extracted` 이거나 `extract` 단독). 가산 명사 `condition`, `align point` 앞에는 관사 `the` 가 필요하다.
- 더 나은 표현: I'm not sure we actually read the mode (OM/SEM) from `cond.txt` when we correct the align point.
- 왜: `extract` 도 맞지만 설정 파일에서 값을 가져오는 일은 `read … from` 이나 `pull … from` 이 더 흔하다. `when align point is corrected` 는 수동태라 누가 보정하는지 흐려지니 `when we correct …` 로 주어를 세웠다. `actually` 가 "정말 하고 있긴 한가"라는 의심을 담는다. 어시스턴트의 첫 답도 `You're right — it isn't extracted.`

### 카드 2 — 바꾼 내용을 한국어 보고서로
- 내가 쓴 영어: "OM Search around now works! Can you generate the report what you have changed in Korean?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the report what you have changed` → `a report on what you've changed`. 명사 `report` 뒤에 `what` 절을 바로 붙일 수 없어 전치사 `on`(또는 `of`)이 필요하다. 처음 부탁하는 보고서라 관사는 `a`.
- 더 나은 표현: OM search-around works now! Could you write up a report in Korean on what you changed?
- 왜: `generate` 는 기계로 뽑아내는 어감이고 사람이 읽을 글을 정리해 달라면 `write up`. 원문처럼 `in Korean` 이 문장 끝에 오면 `changed` 를 꾸미는 듯 읽힐 수 있다. `report` 바로 뒤로 옮기면 그런 오독이 사라진다. `now` 도 동사 뒤로 보내는 쪽이 구어에서 자연스럽다.

### 카드 3 — 이미지 갤러리의 "이미지 있음" 버튼이 이상하다
- 내가 쓴 영어: "in skewvoir/analysis, 이미지 갤러리, we have 이상 실패 우선, 이미지 있음 buttons.  이미지 있음 buttons sound weird where we display images only anyways. what is the purpose of this button?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `where we display images only anyways` → `since we only display images anyway`. 이유를 댈 때는 `where` 가 아니라 `since` 나 `given that` 이다. `anyways` 는 구어 비표준이라 글에서는 `anyway`. 가리키는 버튼이 하나라 `이미지 있음 button sounds` 로 단수를 맞춘다.
- 더 나은 표현: In the image gallery on skewvoir/analysis, there are two toggles: 이상·실패 우선 and 이미지 있음. The 이미지 있음 one sounds odd, since the gallery only shows images anyway. What is it for?
- 왜: 장소를 쉼표로 늘어놓지 말고 `In the image gallery on …` 한 구로 묶었다. 버튼 두 개를 콜론 뒤에 나열하면 무엇을 말하는지 먼저 보인다. `What is the purpose of this button?` 도 맞지만 말로는 `What is it for?` 가 짧다. 문장 첫 글자는 대문자로.

### 카드 4 — 그 이름으로 하자
- 내가 쓴 영어: "rename it to 이미지 없음 제외"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Let's go with 이미지 없음 제외. Please rename it.
- 왜: 명령문으로도 충분히 통한다. 어시스턴트가 후보 둘을 내놓은 뒤라 `Let's go with X`(그걸로 하자)가 고르는 답으로 더 자연스럽다. 이유를 한마디 붙이면 다음 사람이 이름의 뜻을 안다(`It says what the toggle hides.`).

### 카드 5 — 브라우저에서 확인해 줘
- 내가 쓴 영어: "check it in the browser with agent-browser"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Can you verify it in the browser using agent-browser?
- 왜: 결과가 맞는지 확인해 달라는 부탁이면 `check` 보다 `verify` 가 목적이 뚜렷하다. 도구를 쓰는 방법은 `with` 도 되지만 `using` 이 더 분명하다. 도구 지정을 강조하려면 `Please check it in the browser, and use agent-browser for it.` 처럼 두 문장으로 나누자. 스킬 설명에 따르면 기본 도구가 따로 있으니, 이렇게 짚어 주는 게 쓸모 있다.
