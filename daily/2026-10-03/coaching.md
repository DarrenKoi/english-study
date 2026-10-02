# 2026-10-03 — 코칭

## 한글→영어

### 카드 1 — 그 코드 어디 있지   (내가 쓴 한글)
- 내가 쓴 한글: "file manager를 통해서 recipe를 여는 자동화 코드는 어디에 있지?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Where's the automation code that opens a recipe through the File Manager?
- 왜 이렇게: "어디에 있지?"는 `Where's …?` 면 된다. 코드 위치를 물을 때는 `Where does … live?` 도 흔하다. "~를 여는 코드"는 관계절 `the code that opens …` 로 뒤에서 꾸민다. "~를 통해서"는 말로 `through`, 글로는 `via`.

### 카드 2 — 리허설은 필요 없다   (내가 쓴 한글)
- 내가 쓴 한글: "리허설 필요 없어. 클릭 휠 사용해도 장비에 영향 없음."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: No need for a dry run. Clicking and scrolling there don't affect the tool.
- 왜 이렇게: 실제 효과 없이 미리 돌려 보는 것은 `dry run` 이다. `rehearsal` 은 공연이나 발표 연습에 쓴다. "필요 없어"는 `No need for + 명사`. "~해도 영향 없음"은 동명사를 주어로 세워 `don't affect` 로 받는다. 동사는 `affect`, 명사는 `effect`(`have no effect on the tool`). fab 장비는 `tool` 이 현장 용어.

### 카드 3 — EQP_ID 는 안 넣어도 된다   (내가 쓴 한글)
- 내가 쓴 한글: "EQP_ID 적용 필요 없음 현재 접속한  장비에서 바로 테스트 시작하기 때문."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: No need to set EQP_ID, since the test starts right on the tool I'm already connected to.
- 왜 이렇게: 값을 "적용"하는 일은 `set` 이나 `specify` 다. `apply` 는 패치나 설정 묶음에 쓴다. 덧붙이는 이유는 `because` 보다 가벼운 `since` 가 어울린다. "현재 접속한 장비"는 `the tool I'm already connected to` 로, 전치사 `to` 가 관계절 끝에 남는다. "바로"는 `right on`.

### 카드 4 — 녹화에서 workflow 를 만들려면   (내가 쓴 한글)
- 내가 쓴 한글: "지금은 open recipe를 위해서 순서대로 어디 어디를 클릭(작은 worfklow) 해달라고 너에게 요청하지만 나중에 recipe tuning (복잡한 task)의 경우, 엔지니어의 작업 화면을 녹화해서 마우스 클릭과 키보드 타이핑을 추출하려고 하는데, 이를 어떻게 worfklow 형태로 만들 수 있을까?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Right now, for something small like opening a recipe, I just tell you where to click and in what order. Later, for a complex task like recipe tuning, I plan to record the engineer's screen and extract the mouse clicks and keystrokes. How could we turn that into a workflow?
- 왜 이렇게: 한국어 한 문장을 영어 세 문장으로 끊었다. 지금, 나중, 질문 순이다. `Right now … Later …` 가 대비를 세운다. "어디 어디를 순서대로"는 `where to click and in what order`. "키보드 타이핑"은 `keystrokes` 한 단어. "~하려고 하는데"는 `I plan to`. "~형태로 만들다"는 `turn A into B` 가 맞고 `make it as a workflow form` 은 어색하다. `How could we` 의 `could` 가 "될까?" 하고 가능성을 떠보는 느낌을 준다. 철자는 `workflow`.

### 카드 5 — 그건 못 쓴다   (내가 쓴 한글)
- 내가 쓴 한글: "pynput 리스너 사용 불가능."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: A pynput listener isn't an option.
- 왜 이렇게: `impossible` 은 원리상 안 된다는 말이다. 사정이 있어 못 쓸 때는 `isn't an option` 이나 `is off the table` 을 쓴다. 이 답을 들은 어시스턴트가 이유를 되물었다. 영어로도 `… isn't an option, because the engineer works on a different PC.` 처럼 이유를 한 줄 붙이면 왕복이 한 번 준다.

### 카드 6 — 다른 곳에서 조작하니까   (내가 쓴 한글)
- 내가 쓴 한글: "엔지니어가 녹화 PC가 아닌 곳에서 조작하기 때문"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Because the engineer operates the tool from somewhere other than the recording PC.
- 왜 이렇게: "~가 아닌 곳에서"는 `from somewhere other than X`. 질문에 답하는 대화에서는 `Because` 절만 던져도 된다. 글로 쓸 때는 `That's because …` 로 주절을 세운다. 더 짧게 말하려면 `The engineer isn't working on the recording PC.`

### 카드 7 — 이미 구현된 거 아냐?   (내가 쓴 한글)
- 내가 쓴 한글: "이 것들은 이미 코드로 구현된 상태 아냐?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Aren't these already implemented?
- 왜 이렇게: 부정 의문문은 "내가 알기로는 그런데"를 깔고 묻는다. 한국어 "~아냐?"와 딱 맞는다. "구현된 상태"의 "상태"와 "코드로"는 `implemented` 안에 다 들어 있어 옮기지 않는다. 코드에 있다는 쪽을 세우려면 `Isn't all of this already in the code?`

### 카드 8 — 첫 항목부터, Codex 리뷰를 곁들여   (내가 쓴 한글)
- 내가 쓴 한글: "첫 항목부터 구현해줘. 완성도를 높이기 위해 codex와 함께 review를 하면서 진행해줘."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Start with the first item. To make it solid, have Codex review it as you go.
- 왜 이렇게: "~부터"는 `start with`. "완성도를 높이다"를 `raise the completeness` 로 옮기면 어색하고 `make it solid` 나 `make it more polished` 가 자연스럽다. "~하면서 진행"은 `as you go` 세 단어. `have + 사람 + 동사원형` 은 "시키다"로, 며칠째 나온 `ask Codex for a review` 와 같은 일을 다른 틀로 말한다.

### 카드 9 — 회신이 더 왔다   (내가 쓴 한글)
- 내가 쓴 한글: "추가로 더 회신이 왔어."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I got another reply.
- 왜 이렇게: "추가로 더"는 겹말이라 `another` 하나로 받는다. `reply` 는 셀 수 있는 명사다. 여러 건이면 `More replies came in.` 이고 `come in` 이 "들어왔다"는 느낌을 준다.

### 카드 10 — 질문서로 정리해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "Q1~Q15를 office agent에게 보낼 질문서로 정리해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Turn Q1–Q15 into a questionnaire I can send to the office agent.
- 왜 이렇게: 여기서 "정리"는 형태를 바꾸는 일이라 `turn A into B` 나 `compile A into B` 가 맞다. `organize` 는 순서나 분류를 가다듬는 쪽. "보낼 질문서"는 `a questionnaire (that) I can send` 로 관계사를 뺀다. 범위를 말로 읽을 때는 `Q1 through Q15`.

### 카드 11 — 없는 게 정상   (내가 쓴 한글)
- 내가 쓴 한글: "파일 종류 유무 컬럼은 전부 recipe 설정에 의존 - 부재를 정상 상태로 처리할 것."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: Which files and columns exist depends entirely on the recipe settings, so treat a missing one as normal, not as an error.
- 왜 이렇게: "유무"는 명사로 옮기지 않고 `which … exist` 절을 주어로 세운다. 절이 주어면 동사는 단수 `depends`. "~할 것"은 명령문. "부재"는 격식으로 `absence`, 평이하게는 `a missing one`. 뒤에 `not as an error` 를 붙여야 "정상"이 무엇과 반대인지 드러난다.

### 카드 12 — 단위는 헤더에서   (내가 쓴 한글)
- 내가 쓴 한글: "단위가 파일마다 다름. um/nm/pm/Pixel 반드시 헤더에서 읽을 것."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: The unit varies from file to file (um, nm, pm or Pixel), so always read it from the header.
- 왜 이렇게: "~마다 다르다"는 `vary from A to A` 로 관사 없이 같은 명사를 되풀이한다. "반드시"는 지침에서 `always` 가 자연스럽다. `must read` 는 규정 문서의 말투. 두 문장을 `so` 로 이으면 왜 헤더를 읽어야 하는지가 따라온다.

### 카드 13 — 아직 결정 아님   (내가 쓴 한글)
- 내가 쓴 한글: "결정은 아님 데이터가 쌓이면 재검증."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: This isn't final. We'll re-check it once more data has built up.
- 왜 이렇게: "결정은 아님"은 `isn't final` 이나 `not settled yet`. "쌓이면"은 시간 부사절이라 미래 일이어도 `will` 을 쓰지 않고 현재완료 `has built up` 으로 쓴다. 격식으로는 `once more data has accumulated`.

### 카드 14 — ETL 끝나면 다시 보내겠다   (내가 쓴 한글)
- 내가 쓴 한글: "ETL 끝난 후 데이터 형태 전달 다시 해주겠음."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: I'll send you the data format again once the ETL is done.
- 왜 이렇게: 한국어 메모는 명사를 늘어놓지만("전달 다시 해주겠음") 영어는 주어와 동사를 세운다. `once the ETL is done` 도 시간절이라 현재. `after the ETL will finish` 는 틀린다.

### 카드 15 — 하루에 여러 번 재측정   (내가 쓴 한글)
- 내가 쓴 한글: "같은 sample이 하루 여러번 재측정되며 (모니터링 recipe) 측정마다 info CSV가 있고 시각으로 구분됩니다."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: The same sample is re-measured several times a day (monitoring recipes). Each measurement has its own info CSV, and they are told apart by timestamp.
- 왜 이렇게: "하루 여러 번"은 `several times a day` 이고 `a` 가 `per` 구실을 한다. "측정마다 ~가 있다"는 `each … has its own`. "구분되다"는 평이하게 `are told apart`, 격식으로 `are distinguished by`. "~되며"로 이은 긴 문장은 둘로 끊는 편이 읽기 쉽다.

### 카드 16 — 위치로 맞춘다   (내가 쓴 한글)
- 내가 쓴 한글: "block 매칭은 위치로, Method ID 동일성으로 하면 안됨."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: Match blocks by position, not by whether their Method IDs are equal.
- 왜 이렇게: "block 매칭은"이라는 주제어를 버리고 명령문으로 시작한다. 기준은 `by`. "동일성"을 `by Method ID equality` 로 옮기면 딱딱하니 `whether … are equal` 절로 푼다. `A, not B` 가 "하면 안 됨"까지 맡는다.

### 카드 17 — 나중에 물어봐 줘   (내가 쓴 한글)
- 내가 쓴 한글: "ETL 적재 시작 중. 추후에 redis MinIO 정보 물어보길 바래."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: ETL loading has just started. Ask me about the Redis and MinIO details later.
- 왜 이렇게: "시작 중"은 현재완료에 `just` 를 붙인 `has just started`. "물어보길 바래"를 `I hope you ask` 로 옮기면 어색하다. `hope` 는 내가 정할 수 없는 일에 쓰는 말이라 부탁은 명령문이나 `Please check back with me later about …` 로 한다.

### 카드 18 — 남은 미정   (내가 쓴 한글)
- 내가 쓴 한글: "남은 미정: FALSE Valid 실물, 시간대"   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 메모)
- 자연스러운 영어: Still open: a real sample where Valid is FALSE, and the time zone.
- 왜 이렇게: "남은 미정"은 `Still open:` 이나 `Still TBD:`. "실물"은 `a real sample` 또는 `an actual instance`. "FALSE Valid 실물"처럼 명사를 쌓은 말은 `where Valid is FALSE` 관계절로 풀어야 읽힌다.

### 카드 19 — 녹화는 기록, workflow 는 갈라낸 것   (고급 한글 · 번역)
- 한글 원문: "녹화 한 편은 "한 번 일어난 일의 기록(trace)"이고, workflow는 그 기록에서 고정 부분·변수·분기를 갈라내야 만들어집니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: A single recording is a trace of something that happened once; a workflow only emerges when you separate the fixed parts, the variables and the branches out of that trace.
- 번역 포인트: "한 편"은 `a single recording` 으로 "하나뿐"을 살린다. 두 절은 세미콜론으로 나란히 세워 대비한다. "~해야 만들어진다"는 `only emerges when …` 으로, `only` 가 조건을 강조한다. "갈라내다"는 `separate … out of`, 좀 더 섬세하게는 `tease apart`.

### 카드 20 — 어떻게는 있고 왜는 없다   (고급 한글 · 번역)
- 한글 원문: "녹화에는 "어떻게 했는지"만 있고 "왜 그 값을 골랐는지"는 없습니다. (중략) 그래서 결과물은 완전 자동 workflow가 아니라, 절차 뼈대 + 판단 자리(slot) 가 됩니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: A recording captures how something was done, but not why that value was chosen. So what you get is not a fully automatic workflow but a procedural skeleton with slots for judgment.
- 번역 포인트: "~에는 ~만 있고 ~는 없다"는 `captures how …, but not why …` 로 간접의문문 둘을 맞세운다. 행위자가 중요하지 않아 수동태(`was done`, `was chosen`)를 썼다. "결과물"은 `the output` 보다 `what you get` 이 말하듯 자연스럽다. `not A but B` 가 "~가 아니라 ~가 된다"를 맡고, "판단 자리"는 `slots for judgment`.

### 카드 21 — 가정을 적어 둔 덕   (고급 한글 · 번역)
- 한글 원문: "질문서에 "현재 가정"을 적어 둔 덕에 절반이 한 단어로 닫혔습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Because the questionnaire spelled out our current assumption for each question, half of them were settled with a single word.
- 번역 포인트: "~한 덕에"는 `Because` 로 충분하고 고마움을 살리려면 `Thanks to spelling out …`. "적어 두다"는 `spell out`(빠짐없이 밝혀 적다). "닫혔다"는 `were settled` 또는 `were closed out`. `half of them` 은 복수로 받아 `were`.

### 카드 22 — 손으로 적은 dict   (고급 한글 · 번역)
- 한글 원문: "손으로 적은 dict는 producer와 키가 어긋나도 통과합니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: A hand-written dict passes even if its keys have drifted from what the producer emits.
- 번역 포인트: "어긋나다"는 서서히 벌어졌다는 느낌의 `drift from` 이 잘 맞는다. 상태로 말하면 `be out of sync with`. "producer와"는 비교 대상이 producer 가 아니라 producer 가 내는 키이므로 `what the producer emits` 로 푼다. "~해도"는 `even if`.

## 영어 다듬기

### 카드 1 — 회신 일부를 건네며
- 내가 쓴 영어: "Here is the part of reply from the office agent."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `the part of reply` → `part of the reply`. `reply` 는 셀 수 있는 단수 명사라 관사가 붙어야 한다. `part of` 앞의 `the` 는 어느 부분인지 정해져 있을 때만 쓴다.
- 더 나은 표현: Here's part of the office agent's reply.
- 왜: 관사 자리가 바뀌었다. "일부"는 `part of the X` 가 기본형. 소유격 `the office agent's reply` 로 묶으면 `from` 이 필요 없어 짧아진다. 발췌라는 점을 세우려면 `Here's an excerpt from the office agent's reply.`

### 카드 2 — 사무실 회신의 영어 부분
- 내가 쓴 영어: "What we can give Home (you) now is confirmed from raw data in skewnono-pjt-shared/AFM/ D1: Equipemnt IDs are MAP608, MAPC01, 5EAP1501. Code confirms MAPC01=R3, 5EAP1501=M15, the current mocks' mapping is wrong. Fab field doesn't exist anywhere in the raw data (미정)."   (출처: transcript:[user] skewnono-v3-nuxt, 사무실 회신을 옮겨 적은 글)
- 정정: `Equipemnt` → `Equipment`(철자). `Code confirms …, the current mocks' mapping is wrong.` 은 완결된 문장 둘을 쉼표만으로 이었다(comma splice). `, so` 를 넣거나 세미콜론으로 끊는다. `Fab field` 는 단수 가산명사라 관사가 필요하다.
- 더 나은 표현: Everything we can give Home (you) right now has been confirmed against the raw data in skewnono-pjt-shared/AFM/. D1: The equipment IDs are MAP608, MAPC01 and 5EAP1501. The code confirms MAPC01 = R3 and 5EAP1501 = M15, so the mapping in the current mocks is wrong. There is no fab field anywhere in the raw data (TBD).
- 왜: 사무실 agent 의 회신을 손으로 옮긴 글이라 문장 자체는 내 것이 아닐 수도 있다. 그래도 내가 다시 쓴다면 이렇게 고친다. `What we can give … is confirmed` 는 주는 것 전부가 확인됐다는 뜻이 흐릿하니 `Everything … has been confirmed` 로 바꿨다. 원본과 대조해 확인했다는 뜻은 `confirm against`. "어디에도 없다"는 `There is no X anywhere` 가 `X doesn't exist anywhere` 보다 흔하다.

### 카드 3 — 다음 단계로 넘기기
- 내가 쓴 영어: "good. go /simplify"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `go /simplify` → `run /simplify`. `go` 는 자동사라 명령 이름을 목적어로 받지 못한다.
- 더 나은 표현: Looks good. Go ahead and run /simplify.
- 왜: 채팅 줄임말로는 통한다. 다만 `go` 를 살리려면 `Go ahead and + 동사` 틀에 넣어야 한다. `good.` 도 `Looks good.` 으로 쓰면 방금 본 결과가 좋다는 말이 된다.

### 카드 4 — 커밋 범위까지 말하기
- 내가 쓴 영어: "commit and push"   (출처: transcript:[user] auto-recipe-creator, 같은 세션에서 두 번)
- 더 나은 표현: Commit just your changes and push to main.
- 왜: 문법은 맞다. 그런데 두 번째로 말했을 때 작업 트리에는 어시스턴트가 만들지 않은 변경(삭제 4건, 새 폴더)이 섞여 있었고, 어시스턴트가 알아서 자기 파일만 골라 넣었다. 범위(`just your changes`)와 목적지(`to main`)를 붙이면 상대가 짐작할 필요가 없다. 승인하는 말투를 더하려면 어제 카드의 `Go ahead and …` 를 앞에 둔다.
