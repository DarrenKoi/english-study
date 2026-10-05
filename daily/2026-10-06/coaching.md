# 2026-10-06 — 코칭

> 내가 쓴 글은 skewnono 세션 셋에서 나왔다. AFM 적재 방식을 정한 세션의 한국어 다섯 건(긴 것은 문장 단위로 나눔), 테스트 정리 세션의 "진행 고고", 그리고 페이지 가치 브레인스토밍을 시킨 영어 메시지 한 건. auto-recipe-creator 세션과 skewnono 테스트 정리 세션에 `[user]` 로 찍힌 긴 한국어 요청은 Codex 가 Herdr 창으로 보낸 글이라 뺐다("실행 에이전트 Codex입니다", "Codex가 아래 위험을 발견했고"). `commit and push` 두 건도 고칠 데가 없어 뺐다.

## 한글→영어

### 카드 1 — ~하지 않았었나?   (내가 쓴 한글)
- 내가 쓴 한글: "우리 최근에 afm 관련해서 office agent에게 요청할 내용 만들지 않았었나? md file로?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Didn't we recently put together a request for the office agent about AFM? As a Markdown file?
- 왜 이렇게: 기억을 더듬어 확인하는 "~하지 않았었나?"는 부정 의문문 `Didn't we …?`. 한국어의 "-었었-"에 끌려 `Hadn't we` 로 쓸 필요는 없고 `recently` 가 붙은 단순 과거면 된다. "요청할 내용을 만들다"는 `put together a request`. `put together` 는 이것저것 모아 하나로 만든다는 뜻이라 문서에 잘 맞는다. "md file로"는 형식을 말하니 `as a Markdown file`.

### 카드 2 — 파일 내용   (내가 쓴 한글)
- 내가 쓴 한글: "그 파일 내용 보여줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Show me what's in that file.
- 왜 이렇게: "내용"을 명사로 옮기면 `the contents of that file` 이고 이때는 복수 `contents` 다. 단수 `content` 는 글이 담은 "내용물 전반"(`web content`)을 말할 때 쓴다. 대화에서는 명사를 버리고 `what's in that file` 로 푸는 쪽이 가볍다. 부탁으로 낮추려면 `Can you show me …?`.

### 카드 3 — 이제 막 시작한 단계   (내가 쓴 한글)
- 내가 쓴 한글: "지금 office agent는 각 afm 장비로부터 파일을 시작한 단계에 있어. 아직 office.py에 대한 존재를 모르고 있으니 그거에 대한 설명 필요 없음."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Right now the office agent has only just started pulling files from each AFM tool. It doesn't know office.py exists yet, so there's no need to explain it.
- 왜 이렇게: 원문에는 "파일을" 뒤에 "추출"이 빠져 있어서 다음 문장("파일 추출 후")에 맞춰 `pulling files` 로 보탰다. "~한 단계에 있다"는 `is at the stage of` 로도 되지만 `has only just started -ing` 가 "아직 초입"이라는 뜻을 더 잘 살린다. "존재를 모르다"는 명사 "존재"를 동사로 돌려 `doesn't know (that) X exists`. `the existence of office.py` 는 문어체로 들린다. "설명 필요 없음"은 `there's no need to explain it` 이고 더 짧게는 `so leave that out`. 반도체 현장의 "장비"는 `tool` 이 보통이다.

### 카드 4 — 추출, 정제, 적재   (내가 쓴 한글)
- 내가 쓴 한글: "파일 추출 후 정제를 한 뒤에 minIO와 redis 혹은 sqlite에 필요한 데이터를 적재할 예정이야."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Once the files are extracted and cleaned, it'll load the data we need into MinIO and either Redis or SQLite.
- 왜 이렇게: "A 후 B 한 뒤에 C"처럼 순서가 셋이면 앞의 둘을 `Once … extracted and cleaned` 로 묶고 주절에 C 를 둔다. `after` 를 두 번 쓰면 문장이 늘어진다. 데이터 "정제"는 `clean` 이고 `refine` 은 품질을 한 단계 올린다는 말이라 여기엔 넘친다. "적재하다"는 `load … into`(ETL 의 L). "필요한 데이터"는 `the data we need` 로 사람을 넣어 준다. "redis 혹은 sqlite"는 `either Redis or SQLite`.

### 카드 5 — 서로 맞추면 될 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "그러면 그걸 너는 Mock과 office_example.py에 사용할 수 있도록 서로 데이터 path, format, type등을 공유하면 될 것 같아."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: So the two of you just need to agree on the data paths, formats and types, so that you can use them in the mock and in office_example.py.
- 왜 이렇게: "서로 공유하다"는 `share … with each other` 도 되지만 양쪽이 같은 값을 쓰기로 맞춘다는 뜻이니 `agree on` 이 더 정확하다. "~하면 될 것 같아"는 `just need to`. `I think it would be okay if …` 로 직역하면 허락처럼 들린다. "사용할 수 있도록"은 `so that you can use them`. "등"은 영어에서 빼도 되고 넣는다면 `and so on`. 문장 맨 앞의 "그러면"은 `So`.

### 카드 6 — ~인 거지?   (내가 쓴 한글)
- 내가 쓴 한글: "SQLite보다는 redis가 좋은거지?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: So Redis is the better choice over SQLite, right?
- 왜 이렇게: 이미 마음이 기운 채 확인만 받는 "~인 거지?"는 평서문 끝에 `, right?` 를 붙인다. 부가의문문 `isn't it?` 도 같은 일을 한다. 한 단계 올리면 `I take it Redis is the better fit here?`. `I take it …` 은 "~라고 이해하면 되지?"에 해당한다. "A 보다는 B"는 `B over A` 나 `B rather than A`. 둘 가운데 고르는 일이라 `the better choice` 에 `the` 가 붙는다.

### 카드 7 — 탈락시키자   (내가 쓴 한글)
- 내가 쓴 한글: "SQLite는 탈락시키자. redis에는 측정 이력과 minIO에 올려진 파일 path들만 담겨놓는 방식으로 해야지."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Let's drop SQLite. Redis should hold only the measurement history and the paths of the files uploaded to MinIO.
- 왜 이렇게: 후보에서 빼는 "탈락시키다"는 `drop`. `rule out` 도 좋고 더 가볍게는 `SQLite is out`. `eliminate` 는 보고서 말투다. "~하는 방식으로 해야지"는 통째로 `should` 한 단어가 맡는다. `only` 는 한정할 말 바로 앞에 둔다(`hold only the …`). "minIO에 올려진 파일 path들"은 과거분사를 뒤에 붙여 `the files uploaded to MinIO`. 원문의 "담겨놓는"은 "담아 놓는"으로 읽었다.

### 카드 8 — 3개월치만, 그 이상은 안 볼 것   (내가 쓴 한글)
- 내가 쓴 한글: "데이터는 가장 최근 3개월치만 저장하는 방향으로 생각 중. 그 이상 지나면 사람들이 보지 않을거라 생각."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I'm thinking we keep only the last three months of data. I doubt anyone will look at anything older than that.
- 왜 이렇게: "~하는 방향으로 생각 중"은 `I'm thinking (that) we …` 이고 조금 더 기울었으면 `I'm leaning toward keeping …`. "3개월치"는 `three months of data` 나 `three months' worth of data`. 어제 카드에서 `worth of` 는 `worth` 가 명사일 때만 나온다고 했는데 이것이 그 경우다. "보지 않을 거라 생각"은 영어에서 주절을 부정해 `I don't think anyone will …` 로 쓰고 `I doubt anyone will …` 이면 더 짧다. "그 이상 지나면"은 조건절로 풀지 않고 `anything older than that` 이라는 목적어로 접는다.

### 카드 9 — 진행 고고   (내가 쓴 한글)
- 내가 쓴 한글: "진행 고고"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Go ahead with it. / Go for it.
- 왜 이렇게: "고고"는 한국식 구호라 영어로 `Go go` 라고 쓰면 재촉(`Go, go, go!`)으로 들린다. 허락은 `Go ahead`, 응원을 섞으면 `Go for it`. 이 메시지에는 무엇을 진행할지가 없어서 어시스턴트가 "이미 끝나 있어서 제가 더 진행할 것이 없습니다"라고 답한 뒤 무슨 뜻이었는지 되물었다. 영어에서도 `Go ahead with the cleanup` 처럼 대상을 붙이면 그런 왕복이 줄어든다.

### 카드 10 — 누수를 서비스 중단으로 바꾼다   (고급 한글 · 번역)
- 한글 원문: "상한은 '멈춘 호출이 언젠가 돌아온다'는 전제에서만 안전합니다. 돌아오지 않으면 상한은 누수를 서비스 중단으로 바꿉니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: A cap is only safe on the assumption that a stuck call eventually returns. If it never does, the cap turns a leak into an outage.
- 번역 포인트: "~라는 전제에서만"은 `only … on the assumption that`. 인용 부호 속 문장은 `that` 절로 녹인다. "돌아오지 않으면"은 동사를 되풀이하지 않고 대동사로 `If it never does`. "A 를 B 로 바꾼다"는 `turn A into B` 인데 한국어처럼 무생물 `the cap` 이 주어여도 영어에서 자연스럽다. "서비스 중단"은 `outage` 한 단어. "멈춘 호출"은 `a stuck call` 이나 `a hung call`.

### 카드 11 — 내 근거가 반만 맞았다   (고급 한글 · 번역)
- 한글 원문: "8은 제가 권한 값이고, 'drop분은 어차피 도착 못 했을 것'이라는 근거는 서버가 죽어 있는 동안만 맞습니다. 복구 뒤의 경우를 빠뜨렸습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Eight was my recommendation, and my reasoning — that the dropped messages wouldn't have arrived anyway — only holds while the server is down. I missed the case after it recovers.
- 번역 포인트: 자기 실수를 인정하는 문장이라 주어를 숨기지 않는다(`my recommendation`, `my reasoning`, `I missed`). "어차피 도착 못 했을 것"은 실제로 일어나지 않은 일의 추측이라 `wouldn't have arrived anyway`. "~동안만 맞다"는 `only holds while …` 이고 여기서 `hold` 는 "성립하다". "빠뜨렸다"는 `missed` 가 담백하고 `overlooked` 는 격식. "복구 뒤의 경우"는 `the case after it recovers` 처럼 절로 풀었다.

### 카드 12 — 반대면   (고급 한글 · 번역)
- 한글 원문: "Redis 행을 먼저, MinIO 파일을 나중에 지워 달라고 했습니다. 반대면 목록에는 있는데 파일이 없는 측정이 화면에 나옵니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: I asked them to delete the Redis rows first and the MinIO files second. Do it the other way round, and the page will show measurements that are in the list but have no files behind them.
- 번역 포인트: "반대면"은 `the other way round`(미국식 `around`). `If the order is reversed` 라고 써도 되지만 `명령문 + and + will` 로 쓰면 "그렇게 하면 이렇게 된다"는 경고가 짧게 선다. "목록에는 있는데 파일이 없는 측정"은 관계절 하나에 서술어 둘을 `but` 으로 묶는다. `behind them` 은 "그 뒤를 받치는"이라는 뜻으로 보탠 말. "먼저, 나중에"는 `first … second` 나 `first … then`.

### 카드 13 — 소급할 수 없다   (고급 한글 · 번역)
- 한글 원문: "이력은 소급할 수 없으니, 이 기능을 원하시면 그때 수집기가 첫 작업입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: History can't be collected after the fact, so if you ever want this feature, the collector is the first thing to build.
- 번역 포인트: "소급하다"를 사전대로 `retroactively` 로 옮겨도 되지만 `after the fact`(일이 지난 뒤에)가 대화에 더 맞다. 데이터 쪽 용어로는 `backfill` 이 있어 `There's nothing to backfill from` 처럼 쓴다. "원하시면 그때"의 "그때"는 `if you ever want` 의 `ever` 몫. "첫 작업"은 `the first task` 보다 `the first thing to build` 가 무엇을 하는지 드러낸다.

## 영어 다듬기

### 카드 14 — ask me, discuss it
- 내가 쓴 영어: "brainstorm with codex via herdr (Don't ask to me, decide after discuss with codex)."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `Don't ask to me` → `Don't ask me`. `ask` 는 사람을 바로 목적어로 받고 `to` 가 끼지 않는다. `after discuss with codex` → `after discussing it with Codex`. 전치사 `after` 뒤에는 동명사가 오고 `discuss` 는 타동사라 목적어 `it` 이 있어야 한다.
- 더 나은 표현: Brainstorm with Codex via Herdr. Don't check with me — talk it through with Codex and decide between yourselves.
- 왜: `ask to + 사람` 은 10-02 카드까지 다섯 번 나온 `ask for the help to codex` 와 뿌리가 같다. 한국어 "~에게"가 `to` 를 부르는데 `ask`, `tell`, `call` 은 사람을 그냥 받는 동사. `check with me` 는 "나한테 확인받다"라서 "묻지 말고 알아서 해"에 꼭 맞는다. `talk it through` 는 끝까지 이야기해서 정리한다는 뜻이고 `decide between yourselves` 가 "둘이 정해". `via Herdr` 는 수단이라 그대로 좋다.

### 카드 15 — what to add more value
- 내가 쓴 영어: "Think about what to add more value to each page (what we are missing in the pages and what we features we can add)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `what to add more value` → `how to add more value` 또는 `what would add more value`. `what to add` 에서는 `what` 이 `add` 의 목적어인데 뒤에 `more value` 가 또 와서 목적어가 둘이 됐다. `what we features we can add` → `what features we can add`(`we` 가 한 번 더 들어간 오타). `in the pages` → `on the pages`.
- 더 나은 표현: Think about what would make each page more valuable: what's missing and what features we could add.
- 왜: `what would make X more valuable` 에서는 `what` 이 주어라 구조가 꼬이지 않는다. 괄호 대신 콜론을 쓰면 뒤의 두 질문이 앞 문장의 풀이로 읽힌다. `what we are missing in the pages` 는 `what's missing` 두 단어면 충분. 화면 "위"의 것은 `on the page`. 가능성을 여는 자리에는 `can` 보다 `could` 가 부드럽다.

### 카드 16 — write down in Korean into a md file
- 내가 쓴 영어: "write down in Korean into a md file."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `write down in Korean` → `write it down in Korean`. `write down` 은 목적어가 필요하다. `into a md file` → `in an md file`. 파일 "안에" 쓰는 것은 `in` 이고 `into` 는 옮겨 넣을 때 쓴다. `md` 는 "엠디"로 읽어 모음 소리로 시작하니 관사는 `an`. 풀어서 `a Markdown file` 로 쓰면 관사 고민이 없다.
- 더 나은 표현: Write up the results in Korean and save them as a Markdown file.
- 왜: `write down` 은 들은 것을 받아 적는다는 말이고 정리해서 글로 만드는 일은 `write up` 이다. 10-04 카드의 `write down the letter` 와 같은 자리. `save … as a Markdown file` 로 쓰면 형식이 `as` 에 실린다. 원문은 앞 문장의 닫는 괄호 뒤에 마침표 없이 이어졌다. 문장을 끊고 대문자로 시작하면 지시가 하나 더 있다는 것이 보인다.

### 카드 17 — more deep analysis
- 내가 쓴 영어: "I want to give more deep analysis to the users via skewnono project."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `more deep` → `deeper`. 1음절 형용사의 비교급은 `-er`. `via skewnono project` → `through the skewnono project`(관사 누락).
- 더 나은 표현: I want SKEWNONO to give users deeper analysis.
- 왜: `give A to B` 보다 `give B A`(사람 먼저)가 짧고 B 가 `users` 처럼 가벼운 말일 때 특히 그렇다. 특정 집단이 아닌 사용자 일반은 관사 없이 `users`. 프로젝트는 수단이 아니라 분석을 주는 주체라서 `via` 를 떼고 주어 자리에 세웠다. `more` 를 살리고 싶으면 `more in-depth analysis`. `analysis` 는 여기서 셀 수 없는 명사라 `a` 도 `-es` 도 붙지 않는다.
