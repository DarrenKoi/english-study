# 2026-10-05 — 코칭

> 내가 쓴 글은 skewnono 세션 다섯 곳에서 나왔다. 한국어 요청 여덟 건(긴 것 하나는 카드 둘로 나눔)과 recipe-status 캐시를 물은 영어 메시지 두 건. skewnono-afm-trend 세션의 영어 지시문(`Read … and do everything it says, start to finish …`)은 다른 세션이 작업을 넘기며 보낸 글로 보여 다듬기에서 빼고 표현으로만 다뤘다. `commit and push`, `new` 같은 한두 단어짜리도 뺐다.

## 한글→영어

### 카드 1 — 설치되어 있나?   (내가 쓴 한글)
- 내가 쓴 한글: "obsidian skill 설치되어 있나?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Is the Obsidian skill installed? / Do I have the Obsidian skill installed?
- 왜 이렇게: 상태를 묻는 "~되어 있나?"는 `Is … installed?`. 내 환경 얘기라는 점을 살리려면 `Do I have … installed?` 로 쓰고, 이건 `have + 목적어 + 과거분사` 틀이다. 특정 스킬 하나를 가리키니 `the` 가 붙는다. `Did you install …?` 은 "네가 설치했느냐"를 묻는 말이라 뜻이 달라진다.

### 카드 2 — 데이터 크기에 맞춰 따라오나   (내가 쓴 한글)
- 내가 쓴 한글: "웨이퍼 히트맵 in afm page, 데이터 길이가 dynamic 할텐데 그거에 맞춰서 chart에도 반영이 되나?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: For the wafer heatmap on the AFM page, the data size will vary from file to file. Does the chart adapt to that?
- 왜 이렇게: "dynamic 할 텐데"를 `will be dynamic` 으로 옮기면 뜻이 흐리다. 파일마다 달라진다는 말이니 `will vary from file to file`. "~할 텐데"의 추측은 `will` 이 맡는다. "길이"는 1차원이면 `length`, 격자면 `size` 나 `dimensions`. "그거에 맞춰서 반영이 되나"는 `Does the chart adapt to that?` 한 문장이고 `adjust accordingly` 도 된다. 위치는 `in afm page` 가 아니라 `on the AFM page`.

### 카드 3 — Codex 와 상의하고 문제없으면   (내가 쓴 한글)
- 내가 쓴 한글: "일단 너의 개선 방식에 대해서 codex와 상의를 하고 문제 없으면 진행해줘. herdr"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: First, run your approach by Codex, and if it has no objections, go ahead. Use herdr for that.
- 왜 이렇게: "~을 …와 상의하다"는 `run X by someone`. 의견을 구해 본다는 뜻이라 여기 꼭 맞는다. `discuss` 를 쓴다면 `discuss your approach with Codex` 이고 `discuss about` 은 틀린다. "문제 없으면"은 `if it has no objections`(반대가 없으면)나 `if nothing comes up`. "일단"은 `First`, "진행해줘"는 `go ahead`.

### 카드 4 — 남은 것도 마저, 메모체 지시   (내가 쓴 한글)
- 내가 쓴 한글: "확인하지 못한 것 / 남은 것들도 진행해줘. 필요하면 mock을 생성해서 진행. codex와 함께 확인 작업. agent-browser 적극 활용"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Please take care of the unverified and remaining items too. Create mocks where you need them, verify together with Codex, and make full use of agent-browser.
- 왜 이렇게: 한국어 메모는 "진행", "확인 작업", "활용"처럼 명사로 끝나도 지시가 된다. 영어는 동사로 시작하는 명령문을 나란히 놓는다(`Create …, verify …, and make …`). "적극 활용"은 `make full use of` 이고 구어로는 `lean on`. "확인하지 못한 것"은 `the unverified items` 나 `what you couldn't verify`. "필요하면"을 `where you need them` 으로 쓰면 "필요한 곳에만"이 된다.

### 카드 5 — ~라고 봐도 무방   (내가 쓴 한글)
- 내가 쓴 한글: "사용자들은 대부분 1920x FHD 모니터 (회사 제공)을 사용해서 노트북 이용은 없다고 봐도 무방"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Most users are on company-issued 1920-wide FHD monitors, so it's safe to assume nobody uses a laptop.
- 왜 이렇게: "~라고 봐도 무방하다"는 `it's safe to assume (that) …`. "회사 제공"은 `company-issued`. "모니터를 사용해서"는 `use` 도 되지만 `be on + 기기` 가 더 구어답다. "노트북"은 `laptop` 이고 `notebook` 은 공책으로 읽히기 쉽다. "노트북 이용은 없다"는 명사 주어를 버리고 `nobody uses a laptop` 으로 사람을 주어에 세운다.

### 카드 6 — 아직 못 받았지만 기능은 내야 한다   (내가 쓴 한글)
- 내가 쓴 한글: "AFM page에 대해서 아직 office agent가 MinIO data path와 redis key 값들을 전달해준 것은 아니지만 우리는 tiff 이미지를 유저들이  다운 받을 수 있는 (minIO에 저장됨) 기능을 제공해줘야 해."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: For the AFM page, the office agent hasn't sent us the MinIO data paths or the Redis keys yet, but we still need to let users download the TIFF images, which are stored in MinIO.
- 왜 이렇게: "아직 ~한 것은 아니지만"은 `hasn't … yet, but`. 부정문 안의 "A 와 B"는 `and` 가 아니라 `or` 로 잇는다. "기능을 제공해줘야 해"를 `provide a function` 으로 옮기면 딱딱하니 `let users download` 처럼 동사로 푼다. 괄호 속 "(minIO에 저장됨)"은 쉼표와 `which` 관계절로. "그래도"의 뜻은 `still` 이 맡는다.

### 카드 7 — 미리 선제적으로   (내가 쓴 한글)
- 내가 쓴 한글: "미리 선제적으로 코드 구현을 할 수 있으면 진행해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: If there's anything you can build ahead of time, go ahead.
- 왜 이렇게: "미리"와 "선제적으로"는 같은 말이라 영어로는 하나만 쓴다. 평소 말은 `ahead of time` 이나 `in advance` 이고 보고서라면 `proactively`. "코드 구현을 하다"는 `do code implementation` 이 아니라 `build` 나 `implement` 한 단어. "할 수 있으면"을 `If there's anything you can …` 으로 쓰면 "되는 부분만이라도"라는 뜻이 산다.

### 카드 8 — 한 번에 받기   (내가 쓴 한글)
- 내가 쓴 한글: "한번에 받는 기능도 넣는게 좋을 것 같아.  zip 다운로드 구현 가능해?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I think we should also add a way to download them all at once. Could you do it as a zip download?
- 왜 이렇게: "한 번에 받는 기능"은 `a way to download them all at once`. "기능"을 `function` 대신 `a way to …` 로 옮기면 자연스럽다. 영국식 구어로는 `in one go`. "넣는 게 좋을 것 같아"는 `I think we should add`. "구현 가능해?"는 `Is it possible to implement?` 보다 `Could you do it as …?` 나 `Is a zip download doable?` 이 대화답다.

### 카드 9 — 크게 문제없을 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "서버 메모리가 8GBs인데 문제 없을 것 같아 크게."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The server has 8 GB of memory, so I don't think it'll be much of a problem.
- 왜 이렇게: 단위에는 복수 `s` 를 붙이지 않는다(`8 GB`). "메모리가 8GB 인데"는 `has 8 GB of memory`. 한국어는 "문제없을 것 같아"처럼 뒤 절을 부정하지만 영어는 `I don't think it'll be …` 로 주절을 부정한다. 뒤에 덧붙인 "크게"는 영어에서 문장 끝에 떼어 둘 수 없어서 `much of a problem` 으로 안에 넣는다.

### 카드 10 — 반은 맞고 반은 아니다   (고급 한글 · 번역)
- 한글 원문: "반은 맞고 반은 아닙니다. 축·색 범위·통계는 데이터 길이에 맞춰 따라가지만, 2D 맵의 점 크기는 고정이라 격자 밀도에는 반응하지 않습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Yes and no. The axes, colour range and stats follow the data, but the dot size in the 2D map is fixed, so it doesn't respond to how dense the grid is.
- 번역 포인트: "반은 맞고 반은 아니다"는 `Yes and no.` 나 `Partly.` 로 짧게 끊는다. `Half right, half wrong` 은 상대의 주장을 채점하는 말이라 질문에 답할 때는 어색하다. "따라가다"는 `follow`. "격자 밀도"는 `grid density` 도 되지만 `how dense the grid is` 처럼 절로 풀면 말하듯 읽힌다. "고정이라"는 `is fixed, so` 로 원인과 결과를 나눈다.

### 카드 11 — 결함을 짚었고 둘 다 타당했다   (고급 한글 · 번역)
- 한글 원문: "제 원안(scatter를 유지하고 `symbolSize`를 직접 계산)에는 Codex가 두 가지 결함을 짚었고, 둘 다 타당했습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Codex pointed out two flaws in my original plan (keep the scatter series and compute `symbolSize` ourselves), and both were fair.
- 번역 포인트: 한국어는 "제 원안에는"을 앞에 세우지만 영어는 지적한 쪽(`Codex`)을 주어로 두고 `in my original plan` 을 뒤로 보낸다. "짚다"는 `point out`, 보고서에서는 `flag`. "타당했다"는 `both were valid` 가 격식이고 `both were fair` 는 "받아들일 만했다"는 구어 쪽 말이다. `both held up` 이라고 하면 따져 봐도 맞았다는 뜻이 된다.

### 카드 12 — 실수를 밝히고 수습까지   (고급 한글 · 번역)
- 한글 원문: "격자 판별을 고치다가 제 치환 실수로 `axisTitle` export를 지운 커밋을 로컬 `main`에 병합했습니다. 푸시 전에 발견해 복구하고 그 커밋을 amend했으므로 원격에는 정상 커밋만 있습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: While fixing the grid check, I merged a commit into local `main` that had deleted the `axisTitle` export, a find-and-replace slip on my part. I caught it before pushing, restored the export and amended the commit, so the remote only ever had the good one.
- 번역 포인트: "~하다가"는 `While fixing …`. "제 치환 실수로"는 문장 끝에 동격으로 붙인 `a find-and-replace slip on my part` 가 깔끔하다. `slip` 은 작은 실수, `on my part` 는 "내 쪽의". 삭제가 병합보다 먼저 일어났으니 `had deleted` 과거완료. "발견해"는 `caught it`. "원격에는 정상 커밋만 있습니다"는 `only ever had` 로 "나쁜 커밋이 올라간 적이 한 번도 없다"까지 담는다.

### 카드 13 — 같은 걱정을 다시 꺼내지 않도록   (고급 한글 · 번역)
- 한글 원문: "다음 사람이 같은 걱정을 다시 꺼내지 않도록 코드 주석에 이 판단을 남겨 두겠습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: I'll record this decision in a code comment so the next person doesn't raise the same concern again.
- 번역 포인트: "~하지 않도록"은 `so (that) … doesn't …`. `in order not to` 는 두 절의 주어가 같을 때만 쓴다. "걱정을 꺼내다"는 `raise a concern`. "판단"은 여기서 내린 결정을 가리키므로 `judgment` 보다 `decision` 이나 `call` 이 맞다. "남겨 두다"는 `record` 나 `leave a note of`.

## 영어 다듬기

### 카드 14 — 페이지를 주어로
- 내가 쓴 영어: "for the recipe-status page, in the office data, it tends to take about 10 seconds to open the page since it loads lots of data."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: With the office data, the recipe-status page takes about 10 seconds to open because it loads so much data.
- 왜: 문법 오류는 없다. 다만 `for the … page`, `it … to open the page` 로 같은 대상을 두 번 돌려 말했다. `the page` 를 주어로 세우면 한 줄로 줄어든다: `The page takes 10 seconds to open`. `in the office data` 는 "데이터 안에서"로 읽히니 "그 데이터를 쓸 때"라는 뜻의 `with` 가 맞다. 늘 그렇다면 `tends to` 없이 `takes` 로 충분.

### 카드 15 — every an hour
- 내가 쓴 영어: "I wonder if it is possible to cache the data (since the data refresh every an hour from the raw data)."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `every an hour` → `every hour`. `every` 뒤에는 관사 없이 단수 명사가 온다. 관사를 쓰려면 `once an hour`.
- 더 나은 표현: Could we cache it? The data is only rebuilt from the raw data once an hour.
- 왜: `I wonder if it is possible to` 는 공손하지만 길다. 동료에게는 `Could we …?` 면 충분. 이유를 괄호에서 꺼내 문장으로 세우면 `only … once an hour` 가 "그러니 캐시해도 된다"는 근거로 읽힌다. `data` 는 실무 글에서 단수로 받는 일이 많아 `the data is` 가 무난하다. 원문처럼 복수로 받아도 틀리지는 않는다.

### 카드 16 — worth of doing it
- 내가 쓴 영어: "We are running the scheduler in skewnono repo so check it please if it is feasible and worth of doing it."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `worth of doing it` → `worth doing`. `worth` 뒤에는 `of` 없이 바로 `-ing` 가 오고, 주어 `it` 이 `doing` 의 목적어라 `it` 을 또 쓰지 않는다. `in skewnono repo` → `in the skewnono repo`(관사 누락). `check it please if` → `please check whether`. `check it … if` 로 쓰면 `if` 가 "~라면 확인해 줘"라는 조건으로 읽힌다.
- 더 나은 표현: We already run a scheduler in the skewnono repo, so please check whether this is feasible and worth doing.
- 왜: `worth` 는 전치사처럼 쓰는 형용사다. `worth a look`, `worth the effort`, `worth doing`. `worth of` 는 `ten dollars' worth of gas` 처럼 `worth` 가 명사일 때만 나온다. 어시스턴트도 답에서 `feasible, and worth it` 으로 받았다. `already` 를 넣으면 "이미 있으니 거기 얹으면 된다"는 속뜻이 드러난다.

### 카드 17 — a scheduler separately running
- 내가 쓴 영어: "at the office we have a scheduler separately running to produce data for skewnono. you can ask the office agent to make a scheduler to produce the data for the recipe-status."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: At the office we have a separate scheduler that produces data for SKEWNONO. You can ask the office agent to add a job to it for the recipe-status data.
- 왜: `a scheduler separately running` 은 뜻이 통하지만 `a separate scheduler` 가 자연스럽다. 영어는 꾸미는 말을 명사 앞 형용사로 올리는 쪽을 좋아한다. `make a scheduler` 는 스케줄러를 새로 하나 만든다는 말이 된다. 실제로는 있는 스케줄러에 작업을 하나 넣는 일이라 `add a job to it`. 어시스턴트도 `scheduled task` 라고 받았다. `the recipe-status` 는 뒤에 `page` 나 `data` 를 붙여야 무엇을 가리키는지 선다.

### 카드 18 — enlist 와 register
- 내가 쓴 영어: "Write the letter about the purpose and  what data (key value) are needed so that the office agent can generate the code and enlist it to the scheduled task."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `enlist it to the scheduled task` → `register it as a scheduled task`. `enlist` 는 "입대시키다, (도움을) 얻어 내다"이고 "목록에 올리다"는 뜻이 없다.
- 더 나은 표현: Write a letter explaining the purpose and which keys and values we need, so the office agent can write the code and register it as a scheduled task.
- 왜: `list` 에 `en-` 을 붙인 말처럼 보여 헷갈리기 쉽다. `enlist` 는 `enlist in the army`, `enlist someone's help` 에만 쓴다. 등록은 `register`, 일정에 넣기는 `schedule`, 목록에 추가는 `add to`. `about the purpose and what data are needed` 는 `explaining …` 으로 받으면 편지가 할 일이 동사로 드러난다. 처음 꺼내는 편지라 `a letter`. 어제 카드에서 다룬 `write down the letter` 가 오늘은 `Write the letter` 로 바로 쓰였다.
