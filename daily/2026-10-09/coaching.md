# 2026-10-09 — 코칭

> 내가 쓴 글은 skewnono 세션 여섯, auto-recipe-creator 세션 하나, pm-notes 세션 하나에서 나왔다. 한국어는 열한 건이고 긴 메시지는 문장 단위로 나눴다. 영어는 여섯 건. "브라우저에서 /activity 화면 확인해줘"와 "시계열 비교 화면도 브라우저로 확인해줘 agent-browser"는 카드 6과 틀이 같아 그 카드에 묶었고 "commit하고 push 해줘"는 앞선 날 카드와 겹쳐 뺐다. english-study 세션의 `[user]` 메시지는 파이프라인 지시문이라 내가 쓴 글로 보지 않았다. repo 문서에 옮겨 적힌 내 영어 메모(`Since this result data is based on …`)는 출처가 repo 여서 다루지 않았다.

## 한글→영어

### 카드 1 — 보스가 납득할 수 있어야 한다   (내가 쓴 한글)
- 내가 쓴 한글: "my-task에 중요한 요소. 내가 개발 한 것들이 회사에서 어떤 임팩트 / 영향 / 효과를 줬는 지 보스가 납득할 수 있어야 한다."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: One thing that matters for my-task: my boss has to come away convinced of the impact the things I built have had on the company.
- 왜 이렇게: "납득할 수 있어야 한다"를 `should be able to understand` 로 옮기면 이해 여부만 남는다. 설득됐다는 뜻은 `be convinced of` 가 맡고 `come away convinced` 는 "읽고 나서 그렇게 믿게 된다"까지 담는다. "임팩트 / 영향 / 효과"는 영어로 `impact` 하나면 되고 굳이 가르면 `the impact it had and the results it produced`. "개발한 것들"은 지금까지 이어진 효과라 `have had` 현재완료로 받았다.

### 카드 2 — 왜 해야 하는지가 부족함   (내가 쓴 한글)
- 내가 쓴 한글: "equipment-data-mapping agent의 경우 왜 이걸 해야 하는 지 요소가 부족함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: For the equipment-data-mapping agent, the "why" is missing — it doesn't explain why we need to do this at all.
- 왜 이렇게: "~의 경우"는 `In the case of` 보다 `For …,` 가 가볍다. "왜 해야 하는지 요소"는 영어에서 `the "why"` 로 명사처럼 쓰는 것이 흔하다(`the why behind it`). 격식을 올리면 `the rationale` 이나 `the case for doing it`. "부족함"은 `is lacking` 도 되지만 아예 빠졌다는 지적이면 `is missing` 이 또렷하고 덜 빠졌다면 `is thin` 을 쓴다.

### 카드 3 — ~에도 이 원칙 추가해줘   (내가 쓴 한글)
- 내가 쓴 한글: "my-task CLAUDE.md에도 이 원칙 추가해줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Add this principle to my-task's CLAUDE.md as well.
- 왜 이렇게: "~에도"의 "도"는 `too` 나 `as well` 을 문장 끝에 둔다. `also` 를 쓰면 `Also add this principle to …` 처럼 동사 앞에 놓는다. `add A to B` 의 전치사는 `to` 이고 `in` 을 쓰면 "그 파일 안에서 더한다"처럼 들려 어색하다. `my-task CLAUDE.md` 는 소유격 `my-task's` 를 붙이거나 `the CLAUDE.md in my-task` 로 푼다.

### 카드 4 — 탭으로 나눠서 따로따로 보는 게 좋을 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "방문자 추이 분석 in admin/visitors, DAU/WAU/MAU 이걸 탭으로 나눠서 따로따로 보는게 좋을 것 같아."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: On the visitor trend chart in admin/visitors, I think it'd be better to split DAU, WAU and MAU into tabs and view them one at a time.
- 왜 이렇게: 화면 위의 것을 가리킬 때 전치사는 `on`(`on the chart`, `on the page`)이고 경로는 `in admin/visitors`. "~하는 게 좋을 것 같아"는 `I think it'd be better to …` 가 딱 그 세기다. `We should` 는 조금 더 세다. "탭으로 나누다"는 `split … into tabs`, "따로따로"는 `separately` 나 `one at a time`. 문장 중간의 "이걸"은 영어에서 다시 받을 필요가 없어 뺐다.

### 카드 5 — 상대적으로 매우 낮은 막대로만 보여서   (내가 쓴 한글)
- 내가 쓴 한글: "세 정보가 함께 있으니 DAU가 상대적으로 매우 낮은 Bar로만 표시되고 있어서 추이 변화를 보기 어려워."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: With all three on the same chart, the DAU bars are tiny next to the others, so it's hard to see how DAU changes over time.
- 왜 이렇게: "함께 있으니"는 `Because they are together` 보다 `With all three on the same chart,` 가 자연스럽다. `with + 명사 + 전치사구` 가 이유와 상황을 한꺼번에 맡는다. "상대적으로 매우 낮은"은 `relatively very low` 로 부사를 겹치지 않고 `tiny next to the others` 나 `dwarfed by WAU and MAU` 로 비교 대상을 드러낸다. "추이 변화"는 `trend change` 가 아니라 `how it changes over time` 이나 그냥 `the trend`.

### 카드 6 — ~도 브라우저에서 확인해줘   (내가 쓴 한글)
- 내가 쓴 한글: "WAU 탭도 브라우저에서 확인해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Check the WAU tab in the browser too.
- 왜 이렇게: "브라우저에서"는 `in the browser`, `on` 이 아니다. 화면 속 대상은 `on the page` 지만 프로그램 안에서 본다는 말은 `in`. 같은 날 쓴 "브라우저에서 /activity 화면 확인해줘"는 `Check the /activity page in the browser.`, "시계열 비교 화면도 브라우저로 확인해줘 agent-browser"는 `Check the 시계열 비교 page in the browser too, using agent-browser.` 로 도구를 `using` 이나 `with` 로 붙인다. 조금 정중하게는 `Could you verify the WAU tab in the browser as well?`

### 카드 7 — 아무것도 안 들어가게 해줄 수 있어?   (내가 쓴 한글)
- 내가 쓴 한글: "제목만 있고 설명이 없을 때 | | (빈칸), 영상에 아래부분에 아무것도 안들어가게 해줄 수 있어?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: When a row has a title but no description (an empty `| |`), can you make it so nothing gets drawn at the bottom of the video?
- 왜 이렇게: "제목만 있고 설명이 없을 때"는 `has a title but no description` 으로 `only` 없이도 뜻이 선다. "~하게 해줄 수 있어?"는 `can you make it so (that) …` 이 구어에서 가장 흔한 꼴이고 글로는 `Can you leave the bottom of the frame empty in that case?` 가 깔끔하다. "아래 부분에"는 `at the bottom of the video`. `under` 를 쓰면 영상 바깥 아래가 된다.

### 카드 8 — 넣었더니 조그맣게 마크가 남네   (내가 쓴 한글)
- 내가 쓴 한글: "공간으로 넣었더니 조그맣게 마크가 남네"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I tried putting a space in there, but it still leaves a small mark.
- 왜 이렇게: "~했더니 ~네"는 해 보고 뜻밖의 결과를 봤다는 말이라 `I tried …ing, but it still …` 이 맞는다. `try + -ing` 는 "시험 삼아 해 봤다"이고 `try to` 는 "하려고 애썼다"여서 뜻이 갈린다. "공간"은 여기서 띄어쓰기 한 칸이니 `a space`. `space` 에 관사가 없으면 여백이나 우주가 된다. "마크가 남다"는 `leaves a small mark` 로 주어를 `it` 에 맡긴다.

### 카드 9 — 어떤 페이지가 제일 많이 쓰이는지 구분 필요함   (내가 쓴 한글)
- 내가 쓴 한글: "activity에서 어떤 페이지가 제일 많이 사용되는 지 구분 필요함. tips/usage/recipes"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: In activity, we need to be able to tell which page gets used the most — tips, usage, or recipes.
- 왜 이렇게: "구분 필요함"을 `need to distinguish` 로 옮겨도 되지만 "알아볼 수 있어야 한다"는 뜻이면 `tell which …` 가 구어에서 훨씬 흔하다. 기능 요구로 적는다면 `Activity should count the tips, usage, and recipes pages separately.` 가 정확하다. "제일 많이 사용되는"은 `is used the most` 나 `gets used the most`. `get` 수동은 말할 때 자연스럽다. 메모체 "~함"은 `we need to` 로 주어를 살렸다.

### 카드 10 — 라벨 잘리는 것 고쳐줘   (내가 쓴 한글)
- 내가 쓴 한글: "카드에서 라벨 잘리는 것 고쳐줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Fix the label getting cut off on the card.
- 왜 이렇게: 글자가 칸에 안 들어가 끊기는 것은 `get cut off`, UI 용어로는 `truncated`. `cut` 만 쓰면 누가 일부러 잘랐다는 말이 된다. "잘리는 것"은 `the label getting cut off` 로 명사 뒤에 `-ing` 를 붙이거나 명사로 `the label truncation` 이라 한다. 이슈 제목이라면 `Fix truncated label on the stat card`.

### 카드 11 — 맨 아래에 줌 넣을 수 있어?   (내가 쓴 한글)
- 내가 쓴 한글: "시계열 차트 맨 아래에 Zoom in/out 넣을 수 있어?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Can you add a zoom control at the very bottom of the time-series charts?
- 왜 이렇게: `Zoom in/out` 은 동작이라 "넣는" 대상으로는 `a zoom control` 이나 `a zoom slider` 처럼 명사로 바꾼다. "맨 아래"의 "맨"은 `the very bottom`. `very` 가 명사 앞에서 "바로 그, 가장 끝의"를 뜻한다. "넣을 수 있어?"는 가능 여부를 묻는 꼴이지만 실제로는 부탁이라 `Can you add …?` 가 그대로 맞는다.

### 카드 12 — 하나로 4개가 한 번에 움직이게   (내가 쓴 한글)
- 내가 쓴 한글: "하나로 4개가 한번에 움직이게"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: One control that moves all four charts together.
- 왜 이렇게: 앞 문장에 붙는 조건이라 영어도 명사구 조각으로 받았다. 문장으로 쓰면 `I want a single control to drive all four at once.` 이고 `drive` 는 "하나가 여럿을 움직인다"는 UI 설명에 잘 맞는다. "한 번에"는 `at once`, "같이 맞물려"는 `together` 나 `in sync`. "하나로"를 `with one` 으로 옮기면 무엇이 하나인지 흐려지니 `one control` 처럼 명사를 세운다.

### 카드 13 — 막대는 길이로, 선은 기울기로   (고급 한글 · 번역)
- 한글 원문: "막대는 길이로 읽히므로 0에서 시작해야 하고, 선은 기울기로 읽히므로 축을 잘라도 됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: A bar is read by its length, so it has to start at zero; a line is read by its slope, so truncating the axis is fine.
- 번역 포인트: 한국어는 "-고"로 두 절을 이었지만 영어는 세미콜론으로 갈라 대구를 살린다. 두 절의 짜임(`is read by its …, so …`)을 똑같이 맞추면 대비가 저절로 선다. "축을 자르다"는 `truncate the axis` 가 차트 용어이고 `cut` 은 잘 쓰지 않는다. "~해도 됩니다"는 `can` 보다 `is fine` 이 "문제없다"는 판정에 가깝다.

### 카드 14 — 제가 추론한 것이라 확인이 필요합니다   (고급 한글 · 번역)
- 한글 원문: "다만 넣은 근거는 보고서 안의 다른 항목에서 제가 추론한 것이라, 실제 문제와 맞는지 확인이 필요합니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: That said, the rationale I added is something I inferred from other items in the report, so please check whether it matches the actual problem.
- 번역 포인트: "다만"은 `However` 보다 `That said,` 가 앞 문장을 인정한 채 단서를 다는 느낌에 맞는다. "제가 추론한 것이라"는 `is something I inferred from …` 로 풀어 "사실이 아니라 추론"임을 드러낸다. "확인이 필요합니다"를 `confirmation is needed` 로 직역하면 누가 확인하는지 사라진다. 영어는 `please check` 나 `you'll want to confirm` 으로 행위자를 세운다.

### 카드 15 — 소급 분리되지 않습니다   (고급 한글 · 번역)
- 한글 원문: "과거 데이터는 소급 분리되지 않습니다. … 30일 창에서 빠질 때까지는 측정 결과가 실제보다 크게 보입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Past data is not split retroactively. Until those rows age out of the 30-day window, 측정 결과 will look larger than it really is.
- 번역 포인트: "소급"은 부사 `retroactively` 하나로 옮겨진다. "창에서 빠지다"는 `age out of the window` 가 제격인데, 시간이 지나 범위 밖으로 밀려난다는 뜻을 동사 하나가 담는다(`roll off` 도 쓴다). "실제보다 크게 보인다"는 `look larger than it really is`. 한 낱말로는 `be overstated` 가 있고 보고서에 어울린다. `until` 절은 미래 일이어도 현재형이다.

### 카드 16 — 넓히지 않은 이유는 ~ 때문입니다   (고급 한글 · 번역)
- 한글 원문: "카드 폭을 넓히지 않은 이유는 3열 그리드라 한 카드를 넓히면 옆의 두 카드가 좁아지기 때문입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: I didn't widen the card because it sits in a three-column grid, and widening one card would squeeze the two next to it.
- 번역 포인트: "~한 이유는 ~ 때문입니다"를 `The reason … is because …` 로 옮기면 `reason` 과 `because` 가 겹친다. 영어는 `I didn't … because …` 로 곧장 쓴다. "넓히면 ~ 좁아진다"는 실제로 하지 않은 일이라 `would` 가정으로 받고 "좁아지다"는 `squeeze` 가 밀려서 좁아지는 그림을 준다. "3열 그리드라"는 `it sits in a three-column grid` 로 `sit` 이 놓인 자리를 말한다.

## 영어 다듬기

### 카드 17 — 어떤 기능을 제공하는지 요약
- 내가 쓴 영어: "summarize what features we are offering in the afm page."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the afm page` → `on the AFM page`. 웹 페이지 위에 있는 것은 `on`. 제품·장비 약어는 대문자 `AFM`.
- 더 나은 표현: Summarize the features the AFM page offers.
- 왜: `what features we are offering` 은 틀리지 않았지만 간접의문문이 길다. 주어를 페이지로 바꾸면 `the features the AFM page offers` 로 줄어든다. 늘 제공하는 기능이니 진행형보다 단순현재가 맞다. 목록을 원하면 `List every feature …`, 개요를 원하면 `Give me an overview of …` 로 동사를 고른다.

### 카드 18 — 폐기하고 통합한다
- 내가 쓴 영어: "We deprecate afm.skhynix.com page and combine the afm into skewnono along with more features."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `We deprecate` → `We are deprecating`(지금 진행 중인 계획은 현재진행형). `afm.skhynix.com page` → `the afm.skhynix.com site`(관사 필요, 도메인 전체는 `site`). `combine the afm into` → `merge AFM into`(`combine` 은 `with` 와 짝이고 "안으로 합치다"는 `merge … into`).
- 더 나은 표현: We're retiring afm.skhynix.com and folding AFM into SKEWNONO, with some new features added.
- 왜: `deprecate` 는 "쓰지 말라고 권고한다"는 기술 용어라 사이트를 닫는다는 말로는 `retire` 나 `shut down` 이 정확하다. `fold A into B` 는 작은 것을 큰 것 안으로 접어 넣는 그림이라 통합에 잘 맞는다. `along with more features` 는 `with some new features added` 로 풀어야 "옮기면서 더했다"가 읽힌다.

### 카드 19 — 한국어로 docs 폴더에 써 줘
- 내가 쓴 영어: "write down in Korean into the docs/afm folder"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `write down` 뒤에 목적어가 빠졌다 → `write it down`. `into the docs/afm folder` → `in the docs/afm folder`(파일이 놓일 자리는 `in`. `into` 는 `put it into` 처럼 이동 동사와 쓴다).
- 더 나은 표현: Write it up in Korean and save it under docs/afm.
- 왜: `write down` 은 잊지 않으려고 받아 적는다는 뜻이고 정리된 문서로 만든다는 말은 `write up`. 경로를 말할 때 `under docs/afm` 은 "그 폴더 아래 어딘가"로 개발자끼리 흔히 쓴다. 동사 둘(`write`, `save`)로 가르면 언어와 위치가 한 전치사구에 엉키지 않는다.

### 카드 20 — 0001부터 시작하게 정렬
- 내가 쓴 영어: "In the detail page of the afm, 측정 포인트 and 분석 이미지. we have to sort the data in the front-end like should start with 0001.. (currently it is random like 0003..)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `In the detail page` → `On the AFM detail page`. `like should start with 0001` 은 주어가 없다 → `so that it starts with 0001`. `it is random like 0003` → `it starts at a random point, e.g. 0003`(`random like` 는 "0003 처럼 무작위다"로 읽혀 뜻이 어긋난다).
- 더 나은 표현: On the AFM detail page, the 측정 포인트 table and the 분석 이미지 strip should be sorted on the front end so they start from 0001. Right now the order looks arbitrary and starts at something like 0003.
- 왜: 두 문장으로 나눠 "바라는 동작"과 "지금 상태"를 가른다. `we have to sort` 보다 대상을 주어로 세운 `should be sorted` 가 요구 사항 문장답다. `random` 은 정말 난수라는 뜻이 될 수 있어 "기준을 모르겠는 순서"는 `arbitrary` 나 `out of order` 가 안전하다. `front-end` 는 형용사일 때 하이픈(`front-end code`), 명사일 때는 `the front end`.

### 카드 21 — ~도 확인해 줘
- 내가 쓴 영어: "check the popup and 시계열 비교 page in the browser too" / "check the other image tabs in the popup too" / "shuffle the mock rows too"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Check the popup and the 시계열 비교 page in the browser as well. / Check the remaining image tabs in the popup too. / Go ahead and shuffle the mock rows as well.
- 왜: 세 문장 모두 문법은 맞다. 첫 문장은 `popup` 에만 관사가 걸려 있어 `the 시계열 비교 page` 에도 `the` 를 한 번 더 주면 두 대상이 또렷이 갈린다. `the other tabs` 는 "나머지 전부"라는 뜻으로 맞고 `the remaining` 은 "아직 안 본 것"이 더 분명하다. 상대가 제안한 일을 받아들이는 말이면 `Go ahead and …` 가 "그렇게 해"의 어감을 살린다. `too` 를 세 번 잇기보다 `as well` 과 섞는다.

### 카드 22 — 잘 만들어졌고 배포 준비됨
- 내가 쓴 영어: "the afm page is well built up and currently it runs smoothly. I think we are ready to roll out."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `is well built up` → `is well built` 또는 `is in good shape`. `build up` 은 쌓아 올리거나 늘린다는 뜻(`build up trust`, `traffic builds up`)이라 완성도를 말하는 자리에 맞지 않는다.
- 더 나은 표현: The AFM page is in good shape and running smoothly, so I think we're ready to roll it out.
- 왜: `currently it runs` 는 `is running` 진행형이 "요즘 계속 그렇다"를 더 잘 말하고 `currently` 는 빼도 된다. 두 문장을 `so` 로 이으면 상태가 판단의 근거라는 것이 드러난다. `roll out` 은 목적어를 받는 동사라 `roll it out` 으로 쓴다. 목적어 없이 쓰려면 `ready for rollout` 이나 `ready to launch`.

### 카드 23 — 공지 페이지와 메일 HTML
- 내가 쓴 영어: "Make a 공지사항 page for the afm. and write down the html (used for email) to announce the afm page like we have done before"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `write down the html` → `write the HTML`(`write down` 은 받아 적기). `like we have done before` → `like we did before` 또는 `as we've done before`. 문장 중간의 `. and` 는 마침표를 빼고 `, and` 로 잇는다.
- 더 나은 표현: Add a 공지사항 entry for AFM, and write the HTML for the announcement email the same way we did last time.
- 왜: 공지 "페이지"를 새로 만드는 것이 아니라 기존 공지 목록에 한 건을 올리는 일이면 `add a … entry` 나 `post a notice` 가 맞다. `the html (used for email)` 은 괄호 대신 `the HTML for the announcement email` 로 명사구 안에 넣는다. `like we did before` 는 구어에서 괜찮고 글에서는 접속사 자리에 `as` 를 쓴다. `the same way we did last time` 은 "지난번 형식 그대로"를 가장 분명하게 전한다.
