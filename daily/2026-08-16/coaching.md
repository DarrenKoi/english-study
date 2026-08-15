# 2026-08-16 — 코칭

## 한글→영어

### 카드 1 — 아바타를 라벨로 교체 요청 (내가 쓴 한글)
- 내가 쓴 한글: "top nav 실험실 옆에 app 정보 (홍) mark를 교체해줘. 사람 성보다는 그냥 App 정보가 나은 것 같아"   (출처: transcript:[user] skewnono-v3-nuxt/d1605f19)
- 자연스러운 영어: In the top nav, replace the avatar next to 실험실 with an "App 정보" label. A surname on its own reads like nothing in particular — the app's name carries more.
- 왜 이렇게: "A를 B로 교체해줘"는 `replace A with B` 다. 한국어 어순대로 `replace B` 만 쓰면 무엇을 지우는지가 빠진다. "(홍) mark"는 성 한 글자를 딴 아바타이므로 `the avatar`로 옮기고, 괄호 안 정보는 뒤 문장에서 `a surname` 으로 풀었다. "~보다 낫다"를 `is better than` 으로 직역해도 되지만, 이유를 대는 문장에서는 `reads like` (…처럼 읽힌다)가 UI 얘기에 훨씬 잘 붙는다.

### 카드 2 — 앞선 답변의 한 항목을 캐물을 때 (내가 쓴 한글)
- 내가 쓴 한글: "마크업 중복은 무슨 내용이지?"   (출처: transcript:[user] skewnono-v3-nuxt/2a893ccf)
- 자연스러운 영어: What exactly is the markup duplication you mentioned?
- 왜 이렇게: "무슨 내용이지?"를 `What is the content of ~?` 로 옮기면 문서의 목차를 묻는 말이 된다. 여기서 궁금한 건 "그게 구체적으로 뭐냐"이므로 `What exactly is …` 가 맞다. 끝의 `you mentioned` 는 새 주제가 아니라 방금 상대가 꺼낸 항목이라고 붙들어 주는 장치라, 짧은 후속 질문에서 거의 항상 값을 한다.

### 카드 3 — 모델 교체 가능 여부와 순서 (내가 쓴 한글)
- 내가 쓴 한글: "oc skills들에 모델들을 변경하고 싶은데 가능할까 zen 과 go 두가지로 모델들이 서비스되고 있는데 go를 먼저 하는 걸로 진행할 수 있나"   (출처: transcript:[user] skewnono-v3-nuxt/a2f7644c)
- 자연스러운 영어: I'd like to swap the models the oc skills use — is that doable? They're served through two providers, Zen and Go. Can we make Go the one we try first?
- 왜 이렇게: 한 호흡에 이어진 세 가지(원함·가능성·순서)를 문장 셋으로 끊는 게 먼저다. 영어는 한 문장에 요구를 겹쳐 쌓으면 어디에 답해야 할지 흐려진다. "모델들"의 복수 `-들` 은 영어에서 `the models` 로 이미 표현되니 그대로 두면 되고, "두가지로 서비스되고 있다"는 `served through two providers` 로 수단을 `through` 에 실어 준다. "먼저 하는 걸로"는 `do Go first` 보다 `make Go the one we try first` 가 정확하다 — 실제로 원한 건 실행 순서가 아니라 *우선 시도 대상*이기 때문이다.

### 카드 4 — 다른 스킬로 진행해 달라는 요청 (내가 쓴 한글)
- 내가 쓴 한글: "grilling말고 /grill-me로 진행해줘"   (출처: transcript:[user] skewnono-v3-nuxt/6251bd4a)
- 자연스러운 영어: Use `/grill-me` for this instead of `grilling`.
- 왜 이렇게: "A 말고 B로"의 기본형은 `B instead of A` 이고, 영어는 원하는 쪽(B)을 앞에 세운다. 한국어 어순 그대로 `Not grilling but /grill-me` 로 가면 문어체 대조 구문이라 부탁으로는 무겁다. "진행해줘"는 `proceed` 보다 그냥 `use` 나 `run` 이 자연스럽다 — `proceed with` 는 이미 합의된 절차를 재개할 때 쓰는 말이다.

### 카드 5 — 결정을 미루고 자리를 뜰 때 (내가 쓴 한글)
- 내가 쓴 한글: "아직 정해지 못했어. 나중에 다시 올게"   (출처: transcript:[user] skewnono-v3-nuxt/6251bd4a)
- 자연스러운 영어: I haven't decided yet — I'll come back to this later.
- 왜 이렇게: "아직 ~못했다"는 현재완료 `haven't p.p. yet` 이 정확하다. 과거형 `I didn't decide` 로 쓰면 "그때 결정을 안 했다"가 되어 지금도 열려 있다는 뜻이 사라진다. "다시 올게"를 `I'll come again` 으로 옮기면 물리적으로 방문하는 그림이라, 논의를 뜻할 때는 `come back to this` 로 대상을 붙여 준다.

### 카드 6 — 검증된 적 없는 토큰 (고급 한글 · 번역)
- 한글 원문: "쓰이지 않는 토큰은 처음 쓰이는 날 검증된 적 없다는 사실이 잊힙니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/2a893ccf)
- 자연스러운 영어: A token nobody uses gets adopted one day with nobody remembering it was never verified.
- 번역 포인트: 한국어는 "사실이 잊힌다"로 피동을 썼지만, 영어에서 `the fact is forgotten` 은 주어가 무거워 문장이 가라앉는다. 잊는 주체를 `nobody` 로 세워 능동으로 돌리면 리듬이 산다. "처음 쓰이는 날"을 `on the day it is first used` 로 직역할 수도 있지만, `gets adopted one day` 가 "쓰이기 시작한다"는 사건성을 담아 더 짧다. 관계절 `nobody uses` 는 that 을 생략하는 게 구어에 가깝고, 격언조에 맞는다.

### 카드 7 — 색 통일의 성격 (고급 한글 · 번역)
- 한글 원문: "색 통일은 grep 작업처럼 보이지만 실제로는 의미 판정입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/2a893ccf)
- 자연스러운 영어: Unifying the colors looks like a grep job, but it is really a judgment call about meaning.
- 번역 포인트: "~처럼 보이지만 실제로는 ~이다"는 영어에서도 `looks like X, but it is really Y` 그대로 살아 있는 대조 골격이다. 어려운 자리는 "판정"이다 — `decision` 은 밋밋하고 `evaluation` 은 절차적이다. 정답 없는 사안을 사람이 골라야 한다는 뜻이라 `a judgment call` 이 맞고, 무엇에 대한 판단인지 `about meaning` 을 붙여 범위를 준다.

### 카드 8 — 늘리기와 줄이기의 비대칭 (고급 한글 · 번역)
- 한글 원문: "늘리는 건 나중에 싸고, 줄이는 건 이미 익숙해진 화면을 뺏는 일입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/6251bd4a)
- 자연스러운 영어: Raising the limit later is cheap; lowering it means taking away a screen people have already gotten used to.
- 번역 포인트: 두 절을 세미콜론으로 붙여 대구를 살렸다 — 접속사 `but` 을 쓰면 대조가 강조되지만, 여기서는 두 사실을 나란히 놓는 쪽이 원문의 담담함에 가깝다. "~하는 일입니다"는 `means -ing` 로 옮기면 "그렇게 하면 곧 이런 일이 벌어진다"는 함의까지 담긴다. "이미 익숙해진 화면"의 익숙함은 사용자에게 생긴 것이므로 주체를 `people` 로 되살려 `a screen people have already gotten used to` 로 풀었다.

## 영어 다듬기

### 카드 1 — 메뉴 항목 이동과 노출 범위
- 내가 쓴 영어: "api 리스트 should be moved into 앱 정보. and 실험실 should not be seen in the landing page. they are the services for CD-SEM and HV-SEM."   (출처: transcript:[user] skewnono-v3-nuxt/bb345f7a)
- 정정: `and` 로 문장을 시작했고 `they`·`api` 가 소문자다. 문장 첫 글자는 대문자로 쓰고, 앞 문장과 이으려면 `And` 로 시작하는 대신 쉼표나 세미콜론으로 붙인다. `the services` 의 정관사도 불필요하다 — 종류를 말할 때는 무관사 복수다.
- 더 나은 표현: Move the API 리스트 entry into 앱 정보, and hide 실험실 on the landing page — those are CD-SEM and HV-SEM services, so they don't belong on the hub.
- 왜: 지시에는 수동태(`should be moved`)보다 명령형(`Move …`)이 짧고 책임 소재가 분명하다. `should not be seen` 은 "보여선 안 된다"는 금지의 뉘앙스라 정책처럼 들리는데, 실제 요청은 "그 화면에서는 감춰라"이므로 `hide X on Y` 가 정확하다. 마지막 `so they don't belong on the hub` 는 원문에 없던 결론이지만, 영어는 근거를 대면 그 근거가 어떤 결론을 떠받치는지까지 적어 주는 편이 자연스럽다.

### 카드 2 — 다른 페이지에서 안 보인다는 후속 지적
- 내가 쓴 영어: "api 리스트 should be in listed moving into a page from the landing page. I do not see it in other pages"   (출처: transcript:[user] skewnono-v3-nuxt/bb345f7a)
- 정정: `should be in listed moving into` 가 문법적으로 성립하지 않는다. `be in` + 과거분사 `listed` + 동명사 `moving` 이 겹쳐 동사가 셋이 됐다. 하나만 남겨야 한다 — `should be listed` 또는 `should move into`.
- 더 나은 표현: API 리스트 should be listed inside 앱 정보 on every page, not just on the landing page — right now I don't see it anywhere else.
- 왜: 하고 싶었던 말은 "랜딩에서만 보이고 다른 페이지에는 없다"는 것이다. `not just on X` 로 범위를 열고 대시 뒤에 관찰을 붙이면 요구와 근거가 한 문장에 깔끔히 들어간다. `I do not see` 는 문법은 맞지만 축약하지 않은 `do not` 이 격식을 세워 구어 흐름을 끊는다 — 대화에서는 `don't` 가 기본이고, `right now` 를 앞세우면 "지금 상태"라는 시점도 살아난다.

### 카드 3 — 빈 화면을 채우자는 제안
- 내가 쓴 영어: "in recipe-search, you see the blank space below RECIPE LOOKUP component until you hit the search keyword and see the result. why don't we fill the search result with 최근 열어본 recipe?"   (출처: transcript:[user] skewnono-v3-nuxt/6251bd4a)
- 정정: `hit the search keyword` 는 키워드를 때린다는 말이 된다. 검색어는 `type`·`enter` 하는 것이고 `hit` 은 버튼·키에 쓴다 — `hit Enter` / `type a search term`. `below RECIPE LOOKUP component` 에는 관사가 빠졌다(`the RECIPE LOOKUP component`).
- 더 나은 표현: On recipe-search there's an empty area under the RECIPE LOOKUP card that stays blank until you run a search. Why not fill it with the recipes you've opened recently?
- 왜: 원문은 "채운다"의 대상을 `the search result` 라고 적었는데, 실제로 채우려는 건 결과가 아니라 결과가 들어올 *자리*다. `fill it`(= the empty area)로 받아야 뜻이 맞는다. `Why don't we ~?` 도 자연스럽지만, 아이디어를 툭 던지는 자리에서는 주어·조동사를 지운 `Why not ~?` 가 더 가볍다. 그리고 `until you hit the search keyword and see the result` 처럼 사용자의 동작을 둘로 늘어놓기보다 `until you run a search` 한 마디로 묶는 편이 읽기 쉽다.

### 카드 4 — 보관 개수를 정해 줄 때
- 내가 쓴 영어: "we might offer upto 20 recipe lists that the user opened."   (출처: transcript:[user] skewnono-v3-nuxt/6251bd4a)
- 정정: `upto` 는 한 단어가 아니다 — `up to` 로 띄어 쓴다. 그리고 20개가 되는 건 목록(list)이 아니라 목록 안의 항목이므로 `20 recipe lists` 가 아니라 `20 recipes` 다.
- 더 나은 표현: Let's keep up to 20 recently opened recipes.
- 왜: `we might offer` 는 "그럴 수도 있다"는 가능성 표현이라 결정을 전달하는 자리에서는 상대가 확정으로 못 받는다. 방금 질문에 답하는 자리라면 `Let's ~` 로 정하는 편이 낫다. `that the user opened` 관계절은 `recently opened` 형용사구로 줄이면 훨씬 조밀해지고, 이 기능의 이름(recently opened / recently viewed)과도 어휘가 맞아떨어진다.

### 카드 5 — 운영 에러 목록 진단 요청
- 내가 쓴 영어: "I deploy the web app in the cloud and see some issues via activity page. There are lots of http errors … examine these http error code for each endpoints"   (출처: transcript:[user] skewnono-v3-nuxt/91c6854e)
- 정정: 이미 배포를 마친 상태이므로 현재형 `I deploy` 가 아니라 완료형 `I've deployed` 다. 관사도 빠졌다(`via the activity page`). 그리고 `these … code` 는 지시사와 명사의 수가 어긋나고 `each endpoints` 는 `each` 뒤에 복수를 쓴 오류다 — `each endpoint` 가 맞다.
- 더 나은 표현: I've deployed the web app to the cloud, and the activity page is showing a lot of HTTP errors. Walk through what each status code means for the endpoint it came from.
- 왜: `deploy` 의 목적지에는 `in` 이 아니라 `to` 를 쓴다 — 배포는 위치가 아니라 이동이다. `lots of` 는 회화체라 요청문에서는 `a lot of` 나 `a number of` 가 무난하다. 마지막 문장의 `examine` 은 틀리지 않지만 무엇을 내놓아야 할지가 흐리다. `Walk through what each status code means for …` 로 바꾸면 "코드별로 뜻을 짚어 달라"는 산출물이 명시되어, 받는 쪽이 엉뚱한 형식으로 답할 여지가 줄어든다.

### 카드 6 — 시각과 스케줄러의 관계 확인
- 내가 쓴 영어: "00:01:41 is when the scheduler reboot the flask server right?"   (출처: transcript:[user] skewnono-v3-nuxt/91c6854e)
- 정정: 3인칭 단수 주어 `the scheduler` 에는 `reboots` 가 와야 한다. 부가의문 `right?` 앞에는 쉼표를 찍는다(`…, right?`).
- 더 나은 표현: 00:01:41 is when the scheduler restarts the Flask server, isn't it?
- 왜: 서버를 다시 띄우는 건 `reboot`(기계 전체를 껐다 켬)보다 `restart`(프로세스를 다시 시작)가 정확하고, 실제로 그 로그가 가리키는 것도 uWSGI 프로세스 재시작이다. 확인을 구하는 자리라면 `right?` 도 통하지만, 부가의문 `isn't it?` 이 "내 기억이 맞나요"라는 뉘앙스를 더 정중하게 담는다. 고유명사 `Flask` 는 대문자로 시작한다.

### 카드 7 — 두 스킬의 차이를 묻기
- 내가 쓴 영어: "tell me the skill difference between grilling and grill-me"   (출처: transcript:[user] skewnono-v3-nuxt/aeb51640)
- 정정: 문법 오류는 없다.
- 더 나은 표현: What's the difference between the `grilling` and `grill-me` skills?
- 왜: `the skill difference` 는 "스킬 차이"를 한국어 어순대로 붙인 형태라 영어에서는 어색하다. `difference` 를 수식하는 건 종류가 아니라 비교 대상이므로, 그 대상을 `between A and B` 로 뒤에 붙이고 `skills` 는 A·B 를 묶는 말로 내려 보낸다. 명령형 `tell me` 도 통하지만, 질문에는 의문문이 자연스럽고 상대에게 답의 형식을 강요하지 않는다.
