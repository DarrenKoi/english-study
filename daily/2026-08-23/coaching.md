# 2026-08-23 — 코칭

## 한글→영어

### 카드 1 — 느린데 되긴 된다고 말하기   (내가 쓴 한글)
- 내가 쓴 한글: "skewvoir에서 사용자가 검색할 때 처음에는 결과가 나오는데 너무 오래걸리는데, opensearch connection에 문제가 있는걸까?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: In skewvoir, a search *does* come back with results — it just takes far too long. Could the OpenSearch connection be the problem?
- 왜 이렇게: "나오는데 … 오래걸리는데" 처럼 `-는데` 를 두 번 쓴 문장은 영어로 한 문장에 다 담으면 접속사가 꼬인다. 앞은 강조의 `does come back`(되긴 된다), 뒤는 `it just takes …` 로 끊어 두 문장으로 나누는 게 자연스럽다. `does` 는 "안 되는 게 아니라" 라는 양보를 한 단어로 실어 준다. 원인 추측은 `Is X the problem?` 보다 `Could X be the problem?` 이 낫다 — 단정하지 않으면서 조사 방향을 지정한다.

### 카드 2 — 사전 확인 항목에 번호로 답하기   (내가 쓴 한글)
- 내가 쓴 한글: "1 문제 없음. 2. nginx 앞에 있음. 3. 나만 쓰는 url임"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: 1. No problem there. 2. There's an nginx sitting in front of it. 3. It's a URL only I use.
- 왜 이렇게: 번호 답변은 영어에서도 명사구·짧은 절로 끊어 쓰는 게 정상이니 전보체를 그대로 살려도 된다. 다만 `nginx 앞에 있음` 은 주어를 세워야 말이 되므로 `There's an nginx …` 로 존재문을 쓴다. 프록시 문맥에서 "앞단에 있다" 는 관용적으로 `in front of it` 이고, `sitting` 을 넣으면 "그냥 배치돼 있다" 는 뉘앙스가 붙어 더 구어답다. `나만 쓰는` 은 관계절 `only I use` 로 뒤에서 수식한다.

### 카드 3 — 설정이 되어 있는지 확인해 달라고 하기   (내가 쓴 한글)
- 내가 쓴 한글: "우리가 opensearch / minIO로 data를 불러올 때 async / 병렬 방식으로 빠르게 가져오도록 세팅이 되어 있는 지 궁금해"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I'm curious whether our OpenSearch and MinIO reads are actually set up to run async or in parallel.
- 왜 이렇게: "불러올 때 … 가져오도록" 처럼 동사가 두 번 나오는 자리는 영어에서 명사 하나(`reads`)로 압축하면 문장이 살아난다. `~인지 궁금해` 는 `I wonder if` 도 되지만, 답을 실제로 받고 싶을 때는 `I'm curious whether` 가 요청으로 더 또렷하다. `actually` 한 단어가 "그렇게 되어 있다고 알고는 있는데 진짜인지" 라는 의심을 담아, 확인 요청의 성격을 분명히 한다.

### 카드 4 — 무조건 이득인지 되묻기   (내가 쓴 한글)
- 내가 쓴 한글: "msearch로 바꾸면 무조건 이득인가? 현재 opensearch-py library로도 구현 가능한거야?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Is switching to msearch always a win, or are there cases where it isn't? And can it be done with the `opensearch-py` client we already have?
- 왜 이렇게: "무조건" 을 `unconditionally` 로 옮기면 어색하다. 이득 판단에는 `always a win` 이 표준이고, 뒤에 `or are there cases where it isn't` 를 붙이면 상대가 "네" 로 뭉개고 넘어갈 수 없게 된다. "구현 가능한거야" 는 주어를 세우지 않는 게 자연스러워 수동 `can it be done` 을 쓴다. `현재 … library로도` 의 "도" 는 `we already have` 로 옮겨야 뜻이 산다 — 새로 깔지 않아도 되냐는 질문이기 때문이다.

### 카드 5 — 논의할 축을 지정하기   (내가 쓴 한글)
- 내가 쓴 한글: "를 통해서 논의해줘. 경제성, 구현 가능성, 버그 발생 가능성등 (flask와 조합)"   (출처: transcript:[user] skewnono-v3-nuxt, /oc-discuss 인자)
- 자연스러운 영어: Debate it on cost, feasibility, and bug risk — specifically in combination with Flask.
- 왜 이렇게: 한국어의 "-성" 세 개를 영어에서 `-ity` 로 맞춰 옮기면(economics / implementability / bugginess) 하나같이 어색해진다. 실제로 쓰는 짝은 `cost`, `feasibility`, `bug risk` 다. "발생 가능성" 처럼 확률을 말할 때는 `-risk` 접미가 가장 짧고 흔하다. "등" 은 영어로 굳이 `etc.` 를 붙이지 않고 세 항목만 세우는 편이 낫고, 조건은 `— specifically …` 로 대시 뒤에 붙여 강조한다.

### 카드 6 — 모르는 용어를 인정하며 조사 요청하기   (내가 쓴 한글)
- 내가 쓴 한글: "bm_pm 9시간 anchor 버그가 먼지 확인해줘 /oc-review도 함께 진행해서. anchor 버그의 의미를 몰라."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Can you find out what the bm_pm 9-hour anchor bug actually is, running `/oc-review` alongside it? I don't know what "anchor bug" even means here.
- 왜 이렇게: "9시간" 이 뒤 명사를 꾸미면 하이픈으로 묶고 단수로 쓴다 — `9-hour anchor bug`(`9 hours anchor` 가 아니다). "함께 진행해서" 는 동시 수행이니 분사구 `running … alongside it` 이 깔끔하다. "의미를 몰라" 를 `I don't know the meaning of` 로 직역하면 사전을 찾는 말이 되고, 여기서는 이 저장소에서 그 말이 무엇을 가리키는지를 묻는 것이라 `what X even means here` 가 맞다. `even` 이 "아예 감이 없다" 를 담는다.

### 카드 7 — 조사에 결정적인 사실을 뒤늦게 알려 주기   (내가 쓴 한글)
- 내가 쓴 한글: "대부분 회사 데이터는 한국 시간 기준으로 생성되고 있어"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: For what it's worth, most of our company data is generated on Korean time.
- 왜 이렇게: 시간대를 말할 때 "~기준으로" 는 `based on` 이 아니라 전치사 `on`(`on Korean time`) 또는 `in KST` 다. 정식 문서라면 `in KST` 를 쓰고, 대화에서는 `on Korean time` 이 자연스럽다. 조사 중에 단서를 던지는 말이므로 `For what it's worth`(도움이 될지 모르겠지만) 를 앞에 붙이면 끼어드는 느낌 없이 정보만 얹을 수 있다.

### 카드 8 — 더 해봐야 소득이 없다고 판단하기   (고급 한글 · 번역)
- 한글 원문: "3라운드는 마찰을 만들어내는 것에 불과하므로 여기서 멈춥니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: A third round would only manufacture friction, so I'm stopping here.
- 번역 포인트: "3라운드" 를 `Round 3` 로 옮기면 이미 정해진 일정처럼 들린다. 아직 하지 않은 가정이므로 부정관사 `A third round` 에 가정법 `would` 를 얹어야 "했다면" 이 산다. "만들어내는 것에 불과하므로" 의 폄하는 부사 `only` 와 동사 `manufacture` 가 함께 만든다 — `create` 였다면 중립이지만 `manufacture` 는 "억지로 찍어낸다" 는 뉘앙스라 마찰이 인위적임을 드러낸다. 결론은 진행형 `I'm stopping here` 로 두어 방금 내린 판단임을 표시한다.

### 카드 9 — 근거 없는 판단이 결과를 망친다   (고급 한글 · 번역)
- 한글 원문: "근거 없이 인정하거나 방어하면 판정이 오염됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Conceding or defending without checking first would contaminate the verdict.
- 번역 포인트: "인정하거나 방어하면" 은 조건절이지만, 영어에서 `If I concede or defend …, the verdict is contaminated` 로 풀면 문장이 늘어진다. 동명사 주어(`Conceding or defending`)로 조건을 주어 자리에 넣으면 한 문장으로 끝난다. "오염됩니다" 는 수동태 `is contaminated` 보다 능동 `would contaminate` 가 낫다 — 오염의 원인이 무엇인지가 주어에 드러나야 문장이 경고로 작동한다. `verdict` 는 재판 어휘라 "판정" 의 무게를 그대로 옮긴다.

### 카드 10 — 전제가 빠진 절차는 자기 채점이 된다   (고급 한글 · 번역)
- 한글 원문: "스펙 축은 스펙 없이 돌리면 'diff 로부터 스펙을 지어내 그 diff 를 채점하는' 것이 되므로 생략하겠습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Running the spec axis without a spec amounts to inventing a spec from the diff and then grading the diff against it, so I'm skipping it.
- 번역 포인트: "~하면 …것이 된다" 는 `becomes` 보다 `amounts to`(결국 ~인 셈이다) 가 정확하다. 형태가 아니라 실질이 같다는 뜻이라, 절차의 무의미함을 지적하는 자리에 맞는다. `amounts to` 뒤에는 동명사가 오므로 `inventing … and grading …` 으로 병렬을 맞춘다. "채점하다" 는 시험 어휘 `grade` 를 쓰되 기준을 `against it` 으로 명시해야 "자기가 만든 잣대로 자기를 잰다" 는 순환이 드러난다.

## 영어 다듬기

### 카드 1 — 지금 겪는 문제를 배경부터 설명하기
- 내가 쓴 영어: "@deploy_vlms/ her we are serving models via flask server. I have to upload the openweight models from local pc to here flask server. I tried to upload in code server (Web browser) by drag and drop the files but it often fails (not sure why)."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `her` → `here` (오타). `via flask server` → `via a Flask server` (가산명사 단수에는 관사 필수). `to here flask server` → `to this Flask server` (`here` 는 부사라 명사를 꾸미지 못한다 — 한정사 `this` 를 쓴다). `to upload in code server` → `to upload through code-server` (도구를 거쳐 하는 동작은 `in` 이 아니라 `through`/`via`). `by drag and drop the files` → `by dragging and dropping the files` (전치사 `by` 뒤에는 동명사).
- 더 나은 표현: In `@deploy_vlms/` we serve models from a Flask server, and I need to get the open-weight models onto it from my local PC. Dragging and dropping them through code-server in the browser works sometimes, but it fails often enough that I can't rely on it.
- 왜: `I have to upload A from B to C` 는 문법은 맞지만 경로를 세 번 말해 늘어진다. `get A onto it from B` 로 목적지를 대명사로 받으면 한 번만 말하고 끝난다. `often fails (not sure why)` 의 괄호는 말끝을 흐리는데, `fails often enough that I can't rely on it` 으로 바꾸면 빈도가 아니라 **왜 문제인지**가 전달돼 요청의 근거가 선다.

### 카드 2 — 원인 가설을 조심스럽게 내놓기
- 내가 쓴 영어: "I think over 1GB uploading in the web browser leading to fail."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `over 1GB uploading … leading to fail` → `uploads over 1 GB fail`. 동명사구를 주어로 세우려다 정동사가 사라졌다(`leading` 은 분사라 문장의 술어가 될 수 없다). 또 `fail` 은 자동사라 `lead to fail` 처럼 쓰지 않는다 — 명사가 필요하면 `lead to failure` 다.
- 더 나은 표현: My guess is that anything over 1 GB is too big for a browser upload.
- 왜: `I think` 는 무난하지만 뒤에 that절이 오면 문장이 무거워진다. `My guess is that …` 은 같은 길이에 "확인 안 된 추측" 이라는 표시까지 실어, 상대가 그 가설부터 검증하게 만든다. `too big for a browser upload` 는 원인을 크기 문제로 못 박아 `leading to fail` 보다 훨씬 조사하기 쉬운 형태다.

### 카드 3 — 요구 사항을 번호로 못 박기
- 내가 쓴 영어: "can you make streaming method to upload file from local to this flask server? I want 1. streaming, 2. re-start where it stops due to some accidents. 3. binary check for file integrity."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `make streaming method` → `build a streaming upload` (관사 누락). `to upload file` → `to upload files` (총칭은 복수 또는 `a file`). `re-start where it stops due to some accidents` → `resume from where it left off if something goes wrong` (`re-start` 는 처음부터 다시 시작이라 뜻이 반대다. `due to some accidents` 는 영어에서 쓰지 않는 결합이다).
- 더 나은 표현: Could you build a streaming upload from my local machine to this Flask server? Three things I need: (1) it streams rather than buffering the whole file, (2) it resumes from where it left off if the connection drops, and (3) it verifies integrity with a checksum.
- 왜: 요구 목록은 명사만 던지기보다 **각 항목을 절로 세우는** 편이 오해가 없다. `it resumes …`, `it verifies …` 처럼 주어와 동사를 넣으면 무엇이 그 동작을 해야 하는지가 분명해진다. 이어받기는 `resume from where it left off` 가 정착된 관용구이고, 무결성 검사는 `binary check` 가 아니라 `checksum`(또는 `hash check`)이라고 해야 통한다.

### 카드 4 — 운영에서 발견한 오류를 신고하기
- 내가 쓴 영어: "I found that there are many 404 errors in the production mode where recipe-search/recipe-image. can you find the possible root-cause?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the production mode` → `in production` (환경을 가리킬 때는 무관사 관용구다. `mode` 는 앱의 동작 모드를 말할 때만 쓴다). `where recipe-search/recipe-image` → `on the recipe-search/recipe-image endpoints` (`where` 는 접속사라 명사구를 이끌 수 없다).
- 더 나은 표현: We're seeing a lot of 404s in production on the `recipe-search/recipe-image` endpoints. Can you track down the root cause?
- 왜: `I found that there are …` 는 세 겹 구조라 정작 사실이 맨 뒤로 밀린다. `We're seeing …` 진행형으로 열면 "지금도 계속되는 중" 이라는 긴급성이 붙고 문장도 짧아진다. `find the possible root-cause` 의 `possible` 은 요청을 약하게 만드니 빼고, 대신 `track down`(끝까지 추적하다)을 쓰면 원인이 바로 안 보일 수 있다는 사정까지 담긴다.

### 카드 5 — 설정 파일에 뭐가 들어 있는지 묻기
- 내가 쓴 영어: "what do we have a settings in config of .claude"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 의문사 의문문의 어순이 무너졌다. `what` 이 목적어이므로 그 뒤 명사(`a settings`)가 또 올 수 없다 → `What settings do we have …`. `a settings` 는 관사와 복수가 충돌한다(`settings` 는 항상 복수형). `in config of .claude` → `in the .claude config` (소유·소속은 `of` 보다 명사를 앞에 붙이는 쪽이 자연스럽다).
- 더 나은 표현: What's currently configured in `.claude`?
- 왜: `What settings do we have` 도 맞지만, 명사(`settings`)를 동사(`configured`)로 바꾸면 훨씬 짧아지면서 "지금 상태" 를 묻는 질문이 된다. `currently` 가 "예전에 뭘 넣었는지 말고 지금" 이라는 시점을 지정해, 상대가 파일을 실제로 열어 보게 만든다.

### 카드 6 — 설정 항목을 지워 달라고 하기
- 내가 쓴 영어: "in env. CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0 remove it"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Drop `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` from the `env` block.
- 왜: 문법 오류라기보다 위치를 앞에 두고 목적어를 뒤에 두는 바람에 `it` 이 무엇을 가리키는지 한 박자 늦게 도착한다. 영어 명령문은 **동사 → 대상 → 위치** 순서가 기본이라, `Drop X from Y` 로 뒤집으면 대명사가 아예 필요 없다. `remove` 도 맞지만 설정 항목을 없앨 때는 `drop` 이 더 가볍고 흔하다.

### 카드 7 — 화면에 필요한 것을 요청하기
- 내가 쓴 영어: "device-statistics/measurement-rules we need 뒤로가기 button."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: `device-statistics/measurement-rules` needs a back button.
- 왜: 경로를 앞에 던지고 `we need` 로 다시 시작하면 주제와 주어가 따로 놀아 두 조각처럼 읽힌다. 경로를 그대로 주어로 세우면 `X needs Y` 한 문장으로 끝나고, 요청하는 사람이 아니라 **화면**이 필요로 한다는 형태가 되어 근거가 화면 쪽에 선다. "뒤로가기 버튼" 은 `back button` 이 표준이다(`go-back button` 은 쓰지 않는다).

### 카드 8 — 실행 결과를 수치로 보고하기
- 내가 쓴 영어: "bm_pm.office ran. clause isolation on down_dt: eqp_id only (no time): 31 docs, time range only : 10000docs, eqp_id+window : 31 docs. stored down_dt = '2026-05-31T08:57:00 -> row shows '2026-05-31 08:57'"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `bm_pm.office ran` 은 도구가 스스로 실행됐다는 뜻이 되므로 `I ran bm_pm.office` 가 맞다. `10000docs` 는 붙여 쓰면 안 되고 `10,000 docs`. 여는 따옴표만 있고 닫는 따옴표가 없다(`'2026-05-31T08:57:00'`).
- 더 나은 표현: I ran `bm_pm.office`. Isolating the clauses on `down_dt` gives: `eqp_id` alone (no time filter) → 31 docs; the time range alone → 10,000 docs; `eqp_id` + window → 31 docs. A stored `down_dt` of `'2026-05-31T08:57:00'` renders in the row as `2026-05-31 08:57`.
- 왜: 전보체 보고는 영어에서도 정상이지만, 항목 안에 쉼표가 있으면 항목 사이는 세미콜론으로 올려야 끊어 읽힌다. `clause isolation on X` 같은 명사 덩어리는 `Isolating the clauses on X gives:` 로 동사를 살리면 무엇이 무엇을 낳았는지가 분명해진다. 저장값과 표시값의 대비는 `stored … / renders as …` 짝으로 두면 "같은 값인데 표시만 다르다" 가 한눈에 들어온다 — 시간대 버그 보고에서 결정적인 구분이다.
