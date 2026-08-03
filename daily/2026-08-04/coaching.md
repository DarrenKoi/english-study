# 2026-08-04 — 코칭

## 한글→영어

오늘 배치에서 내가 쓴 한국어는 영어 문장 사이에 끼워 넣은 화면 라벨들이다. 문장은 아니지만
그대로 두면 상대가 화면을 못 찾으므로, 영어로 옮기는 법을 정리해 둔다.

### 카드 1 — 화면 블록 이름 (내가 쓴 한글)
- 내가 쓴 한글: "any info like addressing and measurement **포커스, 패턴 인식, 빔 조건**"   (출처: transcript:[user] skewnono-v3-nuxt/7b3f8feb)
- 자연스러운 영어: the addressing and measurement blocks — focus, pattern recognition, and beam conditions
- 왜 이렇게: 세 항목이 앞의 addressing / measurement 두 단계에 각각 딸린 하위 블록이므로, 대시로 끊어 "상위 두 개, 그 안의 세 개"라는 층을 보이게 한다. 화면 라벨을 나열할 때는 관사를 붙이지 않는다. beam condition 은 전압·전류 등 설정 묶음이라 복수 conditions 가 자연스럽다.

### 카드 2 — 표 하나를 가리킬 때 (내가 쓴 한글)
- 내가 쓴 한글: "no amp, no sequence. only **측정 위치**."   (출처: transcript:[user] skewnono-v3-nuxt/7b3f8feb)
- 자연스러운 영어: no AMP, no sequence — only the measurement-point table renders.
- 왜 이렇게: measurement point 만 쓰면 "웨이퍼 위의 좌표"로 읽혀 화면 요소인지 데이터인지 갈린다. table 이나 panel 을 붙여야 "그 표만 나온다"가 된다. 수식어로 쓸 때는 하이픈을 넣고 단수(measurement-point table), 데이터 자체를 셀 때는 복수(measurement points).

### 카드 3 — 조작 순서 서술 (내가 쓴 한글)
- 내가 쓴 한글: "when parameter is selected from the **파라미터 요약** or List"   (출처: transcript:[user] skewnono-v3-nuxt/4eb3da27)
- 자연스러운 영어: when a parameter is selected from the parameter summary or the list
- 왜 이렇게: 어느 파라미터든 하나를 고르는 상황이므로 부정관사 a 가 필요하다. or 로 묶인 두 명사는 관사를 각각 붙이거나 둘 다 빼서 짝을 맞춘다 — 원문처럼 앞만 the 를 달고 뒤를 대문자 List 로 두면 고유명사처럼 읽힌다.

## 영어 다듬기

### 카드 1 — favicon 반복 요청
- 내가 쓴 영어: "still see get /favicon/favicon.sgv continue to sending from backend to the front-end when I am using /api/msr-image?.."   (출처: transcript:[user] skewnono-v3-nuxt/acabd470)
- 정정: 주어가 없다 → `I still see …`. `continue to sending` 은 두 형태(continue **to** send / continue send**ing**)를 섞은 것이고, 여기서는 수동이라 `continues to be sent` 가 맞다. `sgv` 는 `svg` 오타.
- 더 나은 표현: The browser keeps re-requesting `/favicon/favicon.svg` while I'm on the page that uses `/api/msr-image`.
- 왜: `keep -ing` 가 "계속 반복된다"를 동사 하나로 담아 continue 구문의 형태 고민을 없앤다. 그리고 요청을 만드는 주체는 브라우저이므로 그것을 주어로 세우면 "backend → frontend" 라는 방향 오해가 사라지고 진단이 빨라진다.

### 카드 2 — 502 신고 첫 줄
- 내가 쓴 영어: "from recipe-search/recipe-detail error. 502 error. upstreamd_data_error."   (출처: transcript:[user] skewnono-v3-nuxt/7b3f8feb)
- 정정: 동사가 하나도 없는 명사 나열이다. `upstreamd` → `upstream_data_error` 오타.
- 더 나은 표현: I'm getting a 502 (`upstream_data_error`) from `recipe-search/recipe-detail`.
- 왜: 버그 신고의 첫 줄은 `I'm getting <증상> from <위치>` 한 문장이면 충분하다. 에러 코드를 괄호로 달아 두면 나중에 로그에서 검색할 키가 그대로 남는다.

### 카드 3 — 화면 진입 서술
- 내가 쓴 영어: "now we get into the page of recipe-search/open and see the images as well for the selected parameter."   (출처: transcript:[user] skewnono-v3-nuxt/7b3f8feb)
- 정정: `get into the page of X` 는 "X 에 관심을 갖게 되다/끼어들다"로 읽힌다 → `open the X page`. `see the images as well for the selected parameter` 는 as well 의 자리가 틀렸다 → `see the images for the selected parameter as well`(as well 은 문장 끝).
- 더 나은 표현: The `recipe-search/open` page now loads and shows the images for the selected parameter. But none of the detail blocks render — no AMP, no sequence, only the measurement-point table.
- 왜: 화면을 주어로 세우면 "내가 뭘 했다"가 아니라 "화면이 무엇을 한다"가 되어 버그 서술에 맞는다. `none of X render` 가 "하나도 안 나온다"를 정확히 담고, 뒤의 no A, no B 나열이 그 증거로 붙는다.

### 카드 4 — 기존 동작 확인 요청
- 내가 쓴 영어: "in skewvoir/anaylsis we load images and see them in SEM Image. … you know this?"   (출처: transcript:[user] skewnono-v3-nuxt/4eb3da27)
- 정정: `anaylsis` → `analysis` 철자.
- 더 나은 표현: On the UX side, clicking a parameter prefetches every image for that parameter across sequences. Is that how it's actually wired?
- 왜: `you know this?` 는 상대의 지식을 묻는 말이라 "알고는 있지?"처럼 들린다. 확인하고 싶은 대상이 코드일 때는 `Is that how it's actually wired?` 로 초점을 옮긴다. prefetch 한 단어가 "미리 받아 둔다"를 대신하고, across sequences 가 "같은 파라미터의 여러 시퀀스"를 두 단어로 담는다.

### 카드 5 — 파일명이 잠깐 보이는 증상
- 내가 쓴 영어: "it looks awkward to see the text like "S11_XXX_3535.jpeg" in the SEM image before displaying the image. Can you remove or hide thext?"   (출처: transcript:[user] skewnono-v3-nuxt/4eb3da27)
- 정정: `thext` → `the text` 오타. 예시를 여는 `the text like X` 는 무관사가 맞다 → `text like X`. `before displaying the image` 는 주절 주어(it)와 -ing 의 주어가 달라 매달린 분사가 된다 → `before the image loads`.
- 더 나은 표현: Text like `S11_XXX_3535.jpeg` flashes in the SEM Image panel before the image paints. Can you hide it until the image has loaded?
- 왜: flash 가 "잠깐 떴다 사라진다"는 증상 자체를 짚어 준다. paint 는 브라우저가 실제로 화면에 그리는 순간을 뜻해, 데이터가 도착하는 load 보다 이 상황에 정확하다.

### 카드 6 — placeholder ↔ stakeholder
- 내가 쓴 영어: "async? or show some stakeholder?"   (출처: transcript:[user] skewnono-v3-nuxt/4eb3da27)
- 정정: `stakeholder`(프로젝트 이해관계자) → `placeholder`(내용이 준비될 때까지 자리를 지키는 임시 표시). 문법이 아니라 발음이 비슷해 생긴 어휘 혼동이다.
- 더 나은 표현: Since the image needs a moment to become available, that error shouldn't reach the console at all — could we load it asynchronously, or show a placeholder while it warms up?
- 왜: `remove this error code` 라고 하면 "에러 코드를 지워라"가 되어 원인이 아니라 표시를 없애라는 요구로 읽힌다. `shouldn't reach the console at all` 이 원하는 바(애초에 실패할 요청을 보내지 말 것)를 그대로 옮긴다. warm up 은 캐시를 미리 채운다는 뜻으로 이 코드베이스가 이미 쓰는 말이다.

### 카드 7 — 시간대 지적
- 내가 쓴 영어: "in diagnotics from /api/health/logging, the last_success_at seems not Korean time."   (출처: transcript:[user] skewnono-v3-nuxt/1c134071)
- 정정: `diagnotics` → `diagnostics` 철자. `seems not Korean time` → `doesn't seem to be in Korean time`. seem 의 부정은 `doesn't seem to be` 가 표준이고, 시간대 앞에는 전치사 in 이 붙는다.
- 더 나은 표현: In the diagnostics from `/api/health/logging`, `last_success_at` doesn't look like KST. Could you switch it to Korean time?
- 왜: KST 로 줄이면 "한국 시간"의 뜻이 한 번에 통한다. `doesn't look like` 는 단정 대신 관찰로 남겨, 내가 잘못 봤을 여지를 문장이 스스로 열어 둔다.

### 카드 8 — 배포 에러 신고
- 내가 쓴 영어: "I deploy to the cloud as test, I got error from minio_handler from pickle.loads."   (출처: transcript:[user] skewnono-v3-nuxt/910b1dcc)
- 정정: 이미 끝난 일이므로 `I deploy` → `I deployed`. 쉼표로 두 문장을 이은 comma splice → `and` 로 연결. `as test` → `as a test`. `got error` → `got an error`(error 는 가산명사). from 이 연달아 두 번 나와 어디가 위치이고 어디가 원인인지 흐려진다 — 위치는 in, 원인은 from.
- 더 나은 표현: I did a test deploy to the cloud and hit a `ModuleNotFoundError` from `pickle.loads` in `minio_handler`: No module named `numpy._core`.
- 왜: `do a test deploy` 가 "시험 삼아 배포했다"를 명사구로 담는다. hit 은 "부딪혔다"라 got 보다 신고에 어울리고, 에러 이름을 먼저 말한 뒤 콜론으로 원문 메시지를 붙이면 검색 키를 잃지 않는다.

### 카드 9 — 상황 수용과 결론
- 내가 쓴 영어: "I see. our cloud preinstall some of packages. so we have to update the the latest ones if needed."   (출처: transcript:[user] skewnono-v3-nuxt/910b1dcc)
- 정정: 주어가 3인칭 단수라 `preinstall` → `preinstalls`(주체를 정확히 하면 `our cloud image preinstalls`). `some of packages` → `some packages` 또는 `some of the packages`. `the the` 중복. `update the latest ones` 는 "이미 최신인 것을 갱신한다"가 되어 뜻이 뒤집힌다.
- 더 나은 표현: Right — the cloud image ships with some packages preinstalled, so we'll need to upgrade the ones that matter when a newer version is required.
- 왜: `ship with` 이 "제품에 딸려 온다"는 뜻의 배포 관용 동사다. update 는 내용을 갱신하는 것이고 upgrade 가 버전을 올리는 것이라, 여기서는 후자만 맞다. `the ones that matter` 가 "필요하면"이라는 흐린 조건을 "버전이 중요한 것들"로 좁혀 준다.
