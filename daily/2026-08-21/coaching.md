# 2026-08-21 — 코칭

## 한글→영어

### 카드 1 — 방화벽을 열었는데 아직 "미연결"   (내가 쓴 한글)
- 내가 쓴 한글: "미연결" (출처: transcript:[user] — "what is the logic to show the tables in tool-roster page? 미연결. since I lift up some tools' firewalls still see them in the list.")
- 자연스러운 영어: What decides which tools land in the "not yet connected" list on the tool-roster page? I've had the firewall opened for a few of them, but they're still showing up there.
- 왜 이렇게: 화면 라벨은 따옴표로 묶어 **고유명사처럼** 다루는 게 안전하다 — `the "not yet connected" list` 는 번역이 아니라 UI 에 그렇게 적힌 이름이라는 신호다. 상태 용어라 `unconnected`(단순 사실)와 `not yet connected`(아직 절차가 안 끝남)가 갈리는데, 방화벽 승인을 기다리는 중이라면 후자가 맞다. `pending` 을 쓰면 더 짧아진다: `the pending list`. 그리고 원문의 `since` 는 여기서 이유가 아니라 대조라 `but` 이 정확하다.

### 카드 2 — 두 지점에 훅을 건다   (내가 쓴 한글)
- 내가 쓴 한글: "녹화 캡처 실패 (창 닫힘)", "engineer watch 종료" (출처: transcript:[user] — "…that can be hooked when 녹화 캡처 실패 (창 닫힘) and engineer watch 종료")
- 자연스러운 영어: We could hook it in two places: when the recording capture fails because the window is gone, and when the engineer watch exits.
- 왜 이렇게: 한글의 명사형 종결(`실패`, `종료`)을 영어로 그대로 옮기면 `on capture failure and watch termination` 처럼 딱딱해진다. 훅이 걸리는 **순간**을 말하는 자리이므로 `when + 절` 로 푸는 편이 자연스럽다. 괄호 안 `(창 닫힘)` 은 원인 설명이라 `because the window is gone` 으로 절에 녹인다. 프로세스가 끝나는 것은 `finish`(할 일을 다 함)보다 `exit`(루프를 빠져나감)가 정확하고, 이 저장소 로그도 그 어휘를 쓴다.

### 카드 3 — 검색 결과 표의 행 클릭   (내가 쓴 한글)
- 내가 쓴 한글: "검색 결과 table" (출처: transcript:[user] — "in skewvoir, you have 검색 결과 table and you can click one of rows to see the data in analysis page")
- 자연스러운 영어: In Skewvoir there's a search-results table, and clicking a row is supposed to open that measurement on the analysis page.
- 왜 이렇게: 명사를 이어 수식할 때는 하이픈으로 묶어 `search-results table` 로 만든다 — 하이픈이 없으면 `results` 와 `table` 중 무엇이 핵인지 흐려진다. `you have a table` 은 상대가 소유한 물건을 말하는 어감이라 화면 구성 요소에는 `there's a table` 이 낫다. 그리고 "원래는 되던 동작"을 말하는 자리이므로 `is supposed to` 를 넣으면 뒤에 이어지는 "지금은 안 된다"가 자연스럽게 연결된다.

### 카드 4 — 인자를 받지 않는 스크립트   (고급 한글 · 번역)
- 한글 원문: "inspect_redis_key 는 인자를 받지 않습니다. 조사할 key 는 이 파일 안의 KEY_NAME 이며, 편집한 뒤 다시 실행합니다." (출처: transcript:[assistant] skewnono_v3_nuxt — 잘못된 인자를 준 사용자에게 스크립트가 찍는 안내문)
- 자연스러운 영어: `inspect_redis_key` takes no arguments. The key it inspects is the `KEY_NAME` constant in this file — edit it and run the script again.
- 번역 포인트: `인자를 받지 않습니다` 는 `does not receive arguments` 가 아니라 `takes no arguments` 다. 함수·CLI 의 인자에는 `take` 가 굳은 짝이고, 부정을 `not` 대신 `no` 로 명사에 붙이면 "하나도 없다"가 한 단어로 실린다. 둘째 문장의 연결어미 `~이며` 는 영어에 대응물이 없어 그냥 문장을 끊거나 대시로 받는 게 낫다 — `and` 로 이으면 두 지시가 대등해 보여 순서가 흐려진다. `편집한 뒤 다시 실행합니다` 는 평서형이지만 실제로는 지시이므로, 영어에서는 명령형 `edit it and run` 으로 옮겨야 사용자가 할 일이 분명해진다.

## 영어 다듬기

### 카드 1 — 실행 중인 프로세스를 관찰하며
- 내가 쓴 영어: "during @poc/workflow_3/monitor/align_fail_monitor running, I see live search is activated. I found it interestingly it goes fast enough to look around inside live SEM box but is it really going through CV process to get to the location of align point?" (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `during X running` → `while X is running`. `during` 은 명사(구)만 받고 절을 못 받는다. ② `I found it interestingly` → `I found it interesting that` 또는 문두의 `Interestingly,`. `find it + 형용사` 자리라 부사가 올 수 없다. ③ `going through CV process` → `going through a CV process`, `location of align point` → `the location of the align point`. 셀 수 있는 단수 명사 앞에는 관사가 반드시 붙는다. ④ `inside live SEM box` → `inside the live SEM box`.
- 더 나은 표현: While `align_fail_monitor` is running I can see the live search kick in. Interestingly, it moves around inside the live SEM box fast enough to make me wonder — is it actually running CV to locate the align point, or just sweeping?
- 왜: `kick in`(작동이 시작되다)이 `is activated` 보다 자연스럽고, 관찰자가 지켜보는 상황에 맞는다. 원문의 진짜 논점은 "너무 빨라서 못 미덥다"이므로 `fast enough to make me wonder` 로 속도와 의심을 한 구에 묶으면 질문의 동기가 드러난다. 마지막에 `or just sweeping?` 처럼 대안을 하나 붙여 주면 상대가 무엇과 무엇을 갈라 답해야 하는지 알게 된다.

### 카드 2 — 전례를 근거로 요청하기
- 내가 쓴 영어: "like we have done for the image test in align_image folder and debug image, can you gather the images that are processed during the job?" (출처: transcript:[user] auto_recipe_creator)
- 정정: `like we have done for` → `as we did for`. `like` 를 접속사로 쓰는 것은 회화에서는 흔하지만 글에서는 `as` 가 맞고, 이미 끝난 한 번의 작업이므로 현재완료가 아니라 단순과거다.
- 더 나은 표현: Same as we did for the image tests under `align_images/` and `debug_images/` — can you collect the images produced during a job run?
- 왜: `Same as we did for X` 는 전례를 근거로 요청을 여는 상용구다. `gather` 도 통하지만 산출물을 한데 모으는 맥락에서는 `collect` 가 표준이고, `that are processed`(처리를 당한)보다 `produced`(만들어진)가 실제로 원하는 것 — 결과물 — 을 가리킨다.

### 카드 3 — 단점을 되묻기
- 내가 쓴 영어: "any disadvantage we if use two-hook scope?" (출처: transcript:[user] auto_recipe_creator)
- 정정: 어순이 무너졌다. `we` 가 `if` 앞으로 새어 나왔다 → `Any disadvantage if we use a two-hook scope?` 명사 앞 관사도 필요하다.
- 더 나은 표현: Any downside to hooking it in two places?
- 왜: 짧은 되물음에서는 `if` 절보다 `to + 동명사` 가 가볍다 — `any downside to -ing` 가 통째로 굳은 틀이다. `disadvantage` 는 목록에 오르는 항목을 세는 느낌이라 격식이 있고, 대화 중 즉석 확인에는 `downside` 가 맞다. `two-hook scope` 처럼 명사를 쌓기보다 `hooking it in two places` 로 동작을 드러내면 상대가 무엇을 따져야 할지 바로 안다.

### 카드 4 — 제안을 받아들이며 정리하기
- 내가 쓴 영어: "I see. finally line is worth adding and avoid unnecessary two hooks" (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `finally line` → `` the `finally` line ``. 키워드를 가리키므로 관사와 백틱이 필요하다. ② `is worth adding and avoid` → 병렬이 깨졌다. `worth` 뒤의 동명사와 `avoid` 를 나란히 둘 수 없으므로 `is worth adding, and it avoids …` 로 절을 새로 세운다.
- 더 나은 표현: Got it — the `finally` line is worth adding, and it saves us two unnecessary hooks. Let's go with that.
- 왜: `I see` 는 이해했다는 신호일 뿐 결정을 담지 않아서, 상대가 계속 설명해야 하나 망설이게 된다. `Got it` 뒤에 `Let's go with that` 을 붙이면 이해와 결정이 한 번에 전달된다. `avoid two hooks`(훅을 피한다)보다 `saves us two hooks`(훅 둘을 덜어 준다)가 이득의 방향을 명시한다.

### 카드 5 — 마우스가 움직이지 않는다는 버그 신고
- 내가 쓴 영어: "when align fail occurs and the agent enters into the remote monitor, why the mouse cursor is not moving? … Even if it fails, at least we need to see the mouse moving to show it is trying. now, mouse no moves at all." (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `enters into` → `enters`. `enter` 는 타동사라 전치사를 겹쳐 쓰지 않는다(`enter into` 는 계약·논의에 들어갈 때만). ② `why the mouse cursor is not moving?` → `why isn't the mouse cursor moving?` 직접의문문은 주어와 조동사를 도치한다. ③ `mouse no moves at all` → `the mouse doesn't move at all`. 부정은 `no` 가 아니라 `doesn't` 로 만든다.
- 더 나은 표현: When an align failure comes in and the agent takes over the remote monitor, why doesn't the mouse cursor move at all? I don't see any image processing — no consensus analysis, no CV pass to work out the right position. Even a failed attempt should show the cursor moving, so we can tell it tried. Right now it never moves.
- 왜: 버그 신고는 **기대 → 관찰 → 대비** 순으로 놓을 때 가장 빨리 읽힌다. `Even a failed attempt should show …` 로 기대치를 먼저 못 박고 `Right now it never moves` 로 현실을 짧게 닫으면 그 낙차가 곧 버그의 크기가 된다. `so we can tell it tried` 는 왜 그 움직임이 필요한지 — 사용자에게 시도했다는 증거를 보이는 것 — 를 한 절로 설명한다.

### 카드 6 — 방화벽을 열었는데도 목록에 남아 있다
- 내가 쓴 영어: "since I lift up some tools' firewalls still see them in the list." (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① 주절의 주어가 없다 → `I still see them in the list`. ② `lift up ... firewalls` → 방화벽은 `lift`(들어 올리다) 하지 않고 `open`(연다)하거나 규칙을 `lift`(해제한다) 한다: `had the firewall opened for some tools`. ③ `since` 는 이유 접속사인데 여기 논리는 대조라 `but` 이 맞다.
- 더 나은 표현: I've had the firewall opened for a few of these tools, but they're still sitting in the list.
- 왜: 방화벽 해제는 내가 직접 한 일이 아니라 IT 팀에 요청해 이뤄진 일이므로 `have + 목적어 + 과거분사` 사역 구문이 사실에 맞다 — `I opened the firewall` 은 내가 콘솔을 만졌다는 뜻이 된다. `still sitting in the list` 는 `still in the list` 보다 "빠졌어야 하는데 눌러앉아 있다"는 불만이 실린다.

### 카드 7 — 스크립트 수정 요청
- 내가 쓴 영어: "update inspect_redis_key in a way that key is used inside the py file. not as argument" (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `in a way that` → `so that`. 목적을 말하는 자리라 방식을 뜻하는 `in a way that` 은 겉돈다. ② 관사 누락: `the key`, `the .py file`, `as an argument`.
- 더 나은 표현: Change `inspect_redis_key` so the key is set inside the script itself, not passed as an argument.
- 왜: `update` 는 최신화·갱신 쪽이라 동작을 바꾸는 요청에는 `change` 가 정확하다. `the py file` 대신 `the script itself` 를 쓰면 `itself` 가 "다른 데가 아니라 바로 거기"라는 대비를 실어 준다. 그리고 `set`(값을 정해 둔다)과 `passed`(밖에서 넘긴다)를 짝지어 놓으면 두 방식의 차이가 동사만으로 드러난다.

### 카드 8 — 클릭이 안 되는 문제 신고
- 내가 쓴 영어: "in skewvoir, you have 검색 결과 table and you can click one of rows to see the data in analysis page, but now the click is not activated. I see there is data obtained and stored in minIO." (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `one of rows` → `one of the rows`. `one of` 뒤 복수명사에는 한정사가 붙는다. ② `in analysis page` → `on the analysis page`. 화면·페이지는 `on` 을 쓴다. ③ `there is data obtained and stored` → `the data is there — fetched and stored in MinIO`.
- 더 나은 표현: In Skewvoir, clicking a row in the search-results table used to open that measurement on the analysis page, but the rows aren't clickable any more. The data is definitely there — I can see it fetched and stored in MinIO.
- 왜: `the click is not activated` 는 무엇이 안 되는지가 흐리다. `the rows aren't clickable any more` 로 주어를 UI 요소로 바꾸면 개발자가 바로 그 요소를 찾아간다. `used to open …, but …` 은 회귀를 신고하는 표준 틀이라 "전에는 됐다"가 자동으로 실린다. `definitely` 는 "내가 확인했다"를 한 단어로 담아, 데이터 유무를 다시 묻는 왕복을 아낀다.

### 카드 9 — 원인을 스스로 짚어 주기
- 내가 쓴 영어: "I am trying to put the msr value in opensearch DB again by changing the scheduler. the scheduler as it is use _id and pop up the msr in the field. that's why." (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `the scheduler as it is use` → `the scheduler as it stands uses`. 3인칭 단수 `-s` 누락이고, `as it is` 보다 `as it stands`(현행 그대로)가 이 뜻에 맞는 관용구다. ② `pop up the msr in the field` → `pops it out of the field`. `pop up` 은 화면에 불쑥 뜨는 것이고, 값을 꺼내 없애는 동작은 `pop … out of` 다.
- 더 나은 표현: I'm changing the scheduler to write the `msr` value back into OpenSearch. As it stands, the scheduler uses `msr` as the `_id` and then pops it out of the field — that's why it's missing.
- 왜: 원문은 원인을 다 알고도 `that's why` 로 끝나 무엇의 이유인지 목적어가 비어 있다. `that's why it's missing` 으로 결과를 채워 주면 문장 하나로 원인 규명이 닫힌다. `put … again` 보다 `write it back into` 가 "원래 있어야 하는데 빠진 것을 되돌린다"는 방향까지 담는다.

### 카드 10 — 비용만 가볍게 물어보기
- 내가 쓴 영어: "if we moved to use msr field to _id, does that costs a lot to change code here? (just asking)" (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `does that costs` → 조동사 `does` 뒤에는 동사원형이므로 `does that cost`. 여기서는 가정이므로 `would that cost` 가 더 맞다. ② `moved to use msr field to _id` → `switched from the msr field to _id`. 이동의 출발점과 도착점은 `from … to …` 로 잡는다.
- 더 나은 표현: If we switched from the `msr` field to `_id`, would that be a big change on our side? Just curious — not proposing it.
- 왜: 가정을 묻는 자리이므로 조건절 `If we switched` 와 주절 `would` 를 맞춰야 문법과 어감이 함께 산다. `(just asking)` 은 괄호에 갇혀 있어 약한데, `Just curious — not proposing it` 으로 풀면 "지금 결정하자는 게 아니다"까지 명시되어 상대가 착수하지 않는다. `a big change on our side` 는 비용을 우리 저장소 범위로 한정해, 답이 엉뚱하게 넓어지는 것을 막는다.
