# 2026-10-07 — 코칭

> 내가 쓴 글은 skewnono 세션 일곱과 auto-recipe-creator 세션 하나에서 나왔다. 한국어는 스무 건 남짓이고 긴 메시지는 문장 단위로 나눴다. 영어는 여덟 건. 세 메시지는 내가 쓴 글로 보지 않고 뺐다. Redis 공통 규칙과 key 명세, Q32~Q41 회신, 히트맵 데이터 설명은 사무실 쪽 답을 붙여 넣은 글이다(히트맵 메시지는 마지막 한 문장만 내 말로 보고 카드 15로 만들었다). "30건으로 진행해줘", "응 커밋하고 push 해줘"는 어제까지의 카드와 겹쳐 뺐다.

## 한글→영어

### 카드 1 — ~할 필요가 없나?   (내가 쓴 한글)
- 내가 쓴 한글: "afm page에서 개발 recipe detail에 대해서 tip 관련 분석은 제공할 필요가 없나? tip의 상태/수명에 대해서는 별도록 제공해야 하는건가?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: On the AFM page, don't we need any tip analysis in the recipe detail view? Or should tip condition and lifetime get a page of their own?
- 왜 이렇게: "필요가 없나?"는 필요할 것 같다는 쪽으로 기운 물음이라 부정 의문문 `Don't we need …?` 가 맞다. `Is it unnecessary to …?` 로 옮기면 중립적인 확인이 된다. "별도로 제공"은 `separately` 도 되지만 `a page of their own` 이 "따로 자리를 준다"는 뜻을 더 잘 살린다. 팁의 "상태"는 `condition`, "수명"은 `lifetime`(남은 수명이면 `remaining life`). 두 물음을 `Or` 로 이으면 "이쪽이 아니면 저쪽인가"가 드러난다.

### 카드 2 — 얘기해 보고 결정할게   (내가 쓴 한글)
- 내가 쓴 한글: "알았어. 이건 현업 AFM 담당자들과 얘기를 해보고 결정할게"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Got it. I'll talk to the AFM engineers on the floor and decide after that.
- 왜 이렇게: "~해 보고 결정할게"는 `I'll … and decide after that` 이나 `I'll decide once I've talked to …`. 지금 정한 미래라 `will` 을 쓴다. "현업 담당자"는 영어에 딱 맞는 낱말이 없어서 `the engineers who actually run the tools` 처럼 풀거나 공장 문맥이면 `on the floor` 를 붙인다. "결정을 미룬다"를 앞세우려면 `Let me check with the AFM team first.` 도 좋다.

### 카드 3 — ~하면 좋겠다는 의사 표현이 있었어   (내가 쓴 한글)
- 내가 쓴 한글: "AFM 담당 엔지니어가 Tip 불량 모니터링 현황을 볼 수 있으면 좋겠다는 의사 표현이 있었어."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The AFM engineer said they'd like to be able to see the status of tip defect monitoring.
- 왜 이렇게: "의사 표현이 있었어"는 명사로 굳힌 한국어다. 영어는 사람을 주어로 세워 `said they'd like to …` 로 푼다. `There was an expression of intent` 는 회의록에서도 어색하다. 요청의 세기를 올리면 `asked for`, 낮추면 `mentioned it would be nice to`. "볼 수 있으면"은 `would like to be able to see`. 성별을 모르는 한 사람은 `they` 로 받는다. "현황"은 `status`.

### 카드 4 — 종류별로 나누고 spec 으로 관리   (내가 쓴 한글)
- 내가 쓴 한글: "Tip 별로 카테고리를 나누고 여러 parameter 값으로 spec 관리를 할 수 있으면 좋겠어"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I'd like to group the tips into categories and manage specs on several parameters.
- 왜 이렇게: "~할 수 있으면 좋겠어"가 내 바람일 때는 `I'd like to …`. `It would be good if we can …` 은 시제가 어긋나고(`could` 여야 한다) 힘도 빠진다. "카테고리를 나누다"는 `group A into categories` 나 `categorize the tips by type`. "spec 관리"는 `manage specs` 그대로 통하고 뜻을 풀면 `set spec limits on several parameters and track them`. "여러"는 `several`. `various` 는 가짓수보다 다양함을 말한다.

### 카드 5 — ~처럼 만들자, ~가 되겠지   (내가 쓴 한글)
- 내가 쓴 한글: "팁 모니터링을 skewnono e-beam처럼 top navbar를 만들자. 측정 결과와 팁 모니터링 두개의 구조가 되겠지."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Let's give AFM a top navbar like the one e-beam has. It'd have two tabs: measurement results and tip monitoring.
- 왜 이렇게: 원문은 "팁 모니터링을 … navbar를 만들자"로 목적어가 둘이다. 영어에서는 받는 쪽과 주는 것을 갈라 `give AFM a top navbar` 로 쓴다. "e-beam처럼"은 `like e-beam` 만 쓰면 무엇이 닮았는지 흐려지니 `like the one e-beam has`. "~가 되겠지"는 추측 섞인 예상이라 `It'd have …` 나 `So that makes two tabs`. "두 개의 구조"는 `two structures` 가 아니라 실제 물건인 `two tabs`.

### 카드 6 — A 가 좋은지 B 가 좋은지 선택해줘   (내가 쓴 한글)
- 내가 쓴 한글: "afm_d2_measurements가 좋은지 아니면 별도의 key를 redis에서 가지는게 좋은 지 선택해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Which is better — adding to afm_d2_measurements, or keeping a separate key in Redis? Pick one.
- 왜 이렇게: "A 가 좋은지 B 가 좋은지"는 `whether A or B is better` 로 접을 수도 있지만 물음과 명령을 나누면 더 또렷하다. `Pick one.` 이 "선택해줘"를 짧게 맡고 `Make the call.` 은 결정권을 넘긴다는 느낌이 더하다. "key를 가지다"는 `have` 보다 `keep a separate key`. 원문의 앞쪽 선택지에는 동사가 없어서 `adding to` 를 보탰다.

### 카드 7 — 요청 문서, 그리고 확인할 것   (내가 쓴 한글)
- 내가 쓴 한글: "적재 담당자에게 보낼 요청 문서 작성해줘. 추가로 office agent가 체크 혹은 테스트해야할 게 있으면 적어줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Write up a request doc for whoever owns the loader. Also list anything the office agent needs to check or test.
- 왜 이렇게: "적재 담당자"는 직함이 없으니 `whoever owns the loader` 나 `the person in charge of ingestion`. `own` 은 그 일을 책임진다는 뜻으로 개발 조직에서 널리 쓴다. "~에게 보낼"은 `for` 한 낱말이면 된다. "있으면 적어줘"는 `if there is anything` 을 따로 세우지 않고 `list anything …` 에 녹인다. `anything` 이 이미 "있다면"을 품는다. "추가로"는 문두의 `Also`.

### 카드 8 — 개선이 필요한데, ~해서 진행해줘   (내가 쓴 한글)
- 내가 쓴 한글: "tips 페이지 UI/UX 개선이 필요한데 claude design을 사용해서 개선 진행 해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The tips page needs a UI/UX pass. Use Claude Design for it.
- 왜 이렇게: "개선이 필요한데 … 개선 진행해줘"는 같은 말이 두 번 나온다. 영어로는 한 번만 말하고 수단을 따로 세운다. `a UI/UX pass` 의 `pass` 는 "한 차례 손보기"(`a cleanup pass`, `a second pass`). "진행해줘"는 옮기지 않아도 명령문이 그 일을 한다. 한 문장으로는 `Improve the tips page's UI/UX using Claude Design.`

### 카드 9 — 있을 텐데, 한눈에 판단할 수 있게   (내가 쓴 한글)
- 내가 쓴 한글: "장비 / recipe 마다 사용되는 tip들이 있을텐데. 그 tip 별로 상태가 어떤지 쉽게 판단할 수 있는 구조가 되어야 해"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Each tool and recipe will have its own set of tips. The layout should make it easy to tell how each tip is doing.
- 왜 이렇게: "있을 텐데"는 확인하지 않은 추측이고 영어에서는 `will` 이 이 일을 한다(`That'll be the courier`). `must have` 는 근거 있는 단정이라 조금 세다. "쉽게 판단할 수 있는 구조"는 `a structure where we can easily judge` 로 따라가지 말고 `make it easy to tell` 로 뒤집는다. 여기서 `tell` 은 "알아보다". "상태가 어떤지"는 `how each tip is doing` 이 구어, `each tip's condition` 이 문어.

### 카드 10 — 시스템에 무리가 가지 않을까?   (내가 쓴 한글)
- 내가 쓴 한글: "검색에서 최근 측정 모두 담기가 있고 이거를 그룹으로 함께 보기를 사용자가 시전하면 매우 많은 데이터들이 불러와서 시스템에 무리가 가지 않을까?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Search has an "add all recent measurements" option. If a user then opens the whole group in the compare view, won't that load a huge amount of data and put a strain on the system?
- 왜 이렇게: 한 문장에 조건이 둘 겹쳐 있어서 사실(기능이 있다)과 걱정(누르면?)을 두 문장으로 갈랐다. "~하지 않을까?"는 걱정이 담긴 부정 의문 `won't that …?`. "무리가 가다"는 `put a strain on`. 더 구어로는 `hammer the backend`, 격식으로는 `overload the system`. "시전하다"는 게임에서 온 말이라 그냥 `opens` 나 `uses`. "데이터들"은 `data` 가 셀 수 없어서 `a huge amount of data`. "함께 보기"는 화면 이름이라 원문은 그대로 두고 영어에서는 `the compare view` 로 풀었다.

### 카드 11 — 일단 돌렸고, 고칠 점 찾는 중   (내가 쓴 한글)
- 내가 쓴 한글: "일단 office.py를 통해서 가동했고.. 고칠점 찾는 중이야."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I've got it running on office.py for now, and I'm looking for things to fix.
- 왜 이렇게: "가동했고"는 한 번 켠 사건보다 지금 돌아가고 있는 상태가 요점이다. `I've got it running` 이 그 뜻을 싣는다. `I ran it` 은 돌려 봤다는 과거에 그친다. "~를 통해서"는 `through` 가 아니라 `on`(그 설정 위에서)이나 `with`. "일단"은 `for now`. "고칠 점"은 `things to fix` 이고 `fix points` 는 콩글리시.

### 카드 12 — 원본 크기로 보여 줘야 해   (내가 쓴 한글)
- 내가 쓴 한글: "발견한 거는, 분석 이미지에서 팝업에서 보기 서비스를 제공하고 있는데, horizontal mode에서 클릭했을 때 popup으로 원본 이미지 사이즈로 표시를 해줘야 해."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Here's what I found. The analysis images have a "view in popup" option, and clicking an image in horizontal mode should open it in the popup at its original size.
- 왜 이렇게: "발견한 거는"으로 열고 긴 설명이 따르는 말은 `Here's what I found.` 로 한 번 끊는다. "서비스를 제공하고 있는데"는 `have a … option` 이면 된다. `provide a service` 는 회사가 고객에게 하는 일로 들린다. "원본 사이즈로"는 `at its original size` 이고 전치사는 `at`. 개발 용어로는 `at full resolution`, CSS 쪽에서는 `natural size`. "~해 줘야 해"는 요구 사항이라 `should`.

### 카드 13 — 자세히 보려고 쓰는 모드   (내가 쓴 한글)
- 내가 쓴 한글: "팝업에서 보기는 분석 이미지를 심층적으로 보기 위해 진행하는 모드이고, 여기에서 역시 원본 이미지 사이즈를 보여줄 수 있어야 함. 팝업에서 오른쪽에 보여주는 이미지도 원본 사이즈가 아니기 떄문에 작음."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The popup view is for looking at the images closely, so it should show them at original size too. The image on the right side of the popup is also too small because it's scaled down.
- 왜 이렇게: "~하기 위해 진행하는 모드"는 `is for -ing` 로 줄인다. `a mode that is conducted in order to …` 는 한국어 뼈대가 그대로 남은 문장이다. "심층적으로 보다"는 `look at … closely` 나 `inspect … in detail`. `deeply` 는 생각이나 감정에 쓰는 말이라 이미지에는 어울리지 않는다. "원본 사이즈가 아니기 때문에 작음"은 원인을 `scaled down`(줄여서 표시됨)으로 구체화했다. "역시"는 문장 끝의 `too`.

### 카드 14 — 차라리 화살표를 넣자   (내가 쓴 한글)
- 내가 쓴 한글: "좋아. 목록으로 버튼이 너무 작아서 사용자가 바로 확인하기 어려움. 차라리 양 옆으로 이동할 수 있게 화살표를 넣어서 다른 이미지를 볼 수 있도록 하는 것도 넣어주자 (키보드로도 양 옆 가능 해야함, 탭을 누르면 Align Tip, Capture, Result 스위치) 그리고 이 내용에 대해서 작게 설명해주는 것도 추가해야함."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Nice. The "back to list" button is too small to notice right away. Let's also add left and right arrows so users can move between images — the arrow keys should work too, and Tab should switch between Align, Tip, Capture and Result. And add a small hint that explains all this.
- 왜 이렇게: "너무 작아서 ~하기 어렵다"는 `too small to notice`. "차라리"는 보통 `I'd rather` 지만 뒤에 "~하는 것도"가 붙어 실제 뜻은 추가라서 `Let's also` 로 옮겼다. 버튼을 대신하자는 뜻이었다면 `Let's add arrows instead`. "양 옆으로"는 `left and right`. "키보드로도 가능해야 함"은 `the arrow keys should work too`. "작게 설명해주는 것"은 UI 에서 `a small hint` 나 `a short caption`.

### 카드 15 — 렌더링하다 멈춰 버린다   (내가 쓴 한글)
- 내가 쓴 한글: "data 사이즈가 매우 클 때 웹이 랜더링하다 멈춰버리는 현상 있을 수 있어서 대책 필요함."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: When the data is very large, the page can freeze while rendering, so we need a safeguard.
- 왜 이렇게: "멈춰 버리다"는 화면이라면 `freeze` 나 `hang`. `stop` 은 정상 종료처럼 들린다. "~하다(가)"는 `while rendering`. "현상이 있을 수 있어서"의 "현상"은 옮기지 않고 `can` 에 가능성을 맡긴다. `a phenomenon` 은 과학 용어다. "대책"은 `countermeasure` 가 사전의 첫 뜻이지만 소프트웨어에서는 `a safeguard`, `a guard`, `a cap` 이 흔하다. "data 사이즈가 크다"는 `the data is large`.

### 카드 16 — ~는 어때?   (내가 쓴 한글)
- 내가 쓴 한글: "그럼 tab 대신 숫자키로 이동하는건 어때? 1, 2, 3, 4"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: How about using the number keys instead of Tab, then? 1, 2, 3, 4.
- 왜 이렇게: "~는 어때?"는 `How about -ing …?` 나 `What if we used …?`. 뒤쪽은 가정법 과거라 조금 더 조심스럽다. "그럼"은 문두의 `Then` 보다 문장 끝 `, then?` 이 구어에 가깝다. "숫자키"는 `the number keys`. `numeric keys` 는 매뉴얼 말투. "대신"은 `instead of Tab`.

### 카드 17 — 기존 것을 v3.0 으로, 이번 건 v3.1 로   (내가 쓴 한글)
- 내가 쓴 한글: "intro page / history 페이지에 AFM 추가한 걸 넣어야 함. 기존 v3을 v3.0으로 하고 이번 afm 추가건 (10월) v3.1로 하자."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The AFM addition needs to go on the intro and history pages. Let's rename the existing v3 to v3.0 and call this AFM release (October) v3.1.
- 왜 이렇게: "넣어야 함"은 넣을 것을 주어로 세워 `needs to go on` 으로 쓴다. `go on / go in` 은 "~에 들어가야 한다"를 말하는 가장 가벼운 동사다. "A 를 B 로 하다"는 이름을 바꾸는 쪽이면 `rename A to B`, 새로 이름을 붙이는 쪽이면 `call A B`. 한국어는 둘 다 "~로 하다"라서 영어로 옮길 때 갈라야 한다. "기존"은 `the existing`, "이번 추가건"은 `this release`.

### 카드 18 — 그래도 넣자   (내가 쓴 한글)
- 내가 쓴 한글: "머리말 그래도 넣자. 공통된 key 값들은 고정적이라 생각하고 중요한 정보는 꺼내 쓰도록 하자."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Let's keep the header after all. We can treat the keys both layouts share as fixed and pull the important ones out.
- 왜 이렇게: "그래도"는 앞의 결정을 뒤집는 말이라 `after all` 이 맞는다. `anyway` 는 반대 이유가 있어도 밀고 간다는 뜻이고 `still` 은 문장 가운데 놓인다. "고정적이라 생각하고"는 믿는다는 뜻이 아니라 그렇게 치자는 가정이라 `think` 가 아니라 `treat … as fixed` 나 `assume … are stable`. "공통된 key"는 `the keys both layouts share`(관계대명사 생략). "꺼내 쓰다"는 `pull out`. "머리말"은 화면에서는 `header`, 글에서는 `preface`.

### 카드 19 — 정리해줘, 새 질문만 남기는 형태로   (내가 쓴 한글)
- 내가 쓴 한글: "docs/afm에 있는 to-questionnaire-afm- 을 정리해줘 (답을 받은 건 docs/datables에 기록이 되고 코드로 afm page에 구현이 된 건지 확인. 새로운 질문만 남기는 형태로 정리)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Clean up the to-questionnaire-afm-* files in docs/afm. For each answered question, check that the answer is recorded in docs/datatables and implemented on the AFM page, then keep only the questions that are still open.
- 왜 이렇게: "정리하다"는 영어에서 갈린다. 흩어진 것을 줄이는 일은 `clean up` 이나 `consolidate`, 순서를 잡는 일은 `organize`, 요약은 `summarize`. 여기서는 다섯 파일을 줄이는 일이라 `clean up`. "~된 건지 확인"은 `check that …`. `check if` 는 결과를 모를 때, `check that` 은 그래야 한다고 기대할 때 쓴다. "새로운 질문만"은 문맥상 아직 답이 없는 질문이라 `new` 보다 `still open` 이 정확하다. "답을 받은 건"은 `For each answered question` 으로 문두에 세운다.

### 카드 20 — 단순하게 붙이고 싶어, 가능한가?   (내가 쓴 한글)
- 내가 쓴 한글: "단순하게 두개의 mp4 파일을 붙이고 싶어. python으로 가능한가?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I just want to join two MP4 files end to end. Can that be done in Python?
- 왜 이렇게: 영상을 "붙이다"는 `join`, `concatenate`(개발자 말로 `concat`), `stitch together`. `attach` 는 첨부, `paste` 는 붙여넣기다. `end to end` 를 달면 앞뒤로 잇는다는 뜻이 분명해진다. "단순하게"는 방법이 아니라 내 바람이 소박하다는 말이라 `simply` 보다 `I just want to`. "~로 가능한가?"는 `Can that be done in Python?` 이나 `Is that doable in Python?`. 언어 앞 전치사는 `in`.

### 카드 21 — 곧바로 바뀌면 이상하니까   (내가 쓴 한글)
- 내가 쓴 한글: "PWI로 넘어갈 때 PWI Auto Recipe Creation Card 넣어줘. 곧바로 화면이 바뀌면 이상하니까.. Card는 우리가 이미 demo에 사용했던 걸 이용."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Put the "PWI Auto Recipe Creation" card in at the cut to the PWI part — a hard cut would feel abrupt. Reuse the card we already made for the demo.
- 왜 이렇게: "곧바로 화면이 바뀌면 이상하니까"는 영상 용어로 `a hard cut would feel abrupt`. 직역 `it is strange if the screen changes immediately` 도 통하지만 `strange` 는 "기묘하다" 쪽이고 여기 뜻은 "갑작스럽다"다. `would` 는 카드를 넣지 않았을 경우를 가정한다. "넘어갈 때"는 `at the cut to …` 나 `where it switches to …`. "이미 썼던 걸 이용"은 `reuse` 한 낱말. `use again` 을 풀어 쓸 까닭이 없다.

### 카드 22 — 내가 직접 실행할 예정   (내가 쓴 한글)
- 내가 쓴 한글: "파일은 내가 office에서 직접 실행할 에ㅓㅈ"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I'll run the script myself at the office.
- 왜 이렇게: 끝의 "에ㅓㅈ"은 "예정"의 오타로 읽었다. "~할 예정"은 `I'm planning to` 도 되지만 이미 마음먹은 일은 `I'll` 이나 `I'm going to` 가 자연스럽다. "직접"은 재귀대명사 `myself` 를 문장 뒤쪽에 둔다. `directly` 는 중간 단계 없이라는 뜻이라 "내 손으로"와는 다르다. "office에서"는 `at the office`. "파일"은 실행하는 대상이니 `the script`.

### 카드 23 — 완성! ~할 필요 없음   (내가 쓴 한글)
- 내가 쓴 한글: "완성! gitignore 할 필요 없음"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Done! No need to gitignore it.
- 왜 이렇게: "완성!"은 `Done!` 이나 `All done!`. `Complete!` 는 게임 화면 문구 같고 `Finished!` 는 조금 무겁다. "~할 필요 없음"은 `No need to …` 로 주어 없이 쓰는 메모체가 한국어의 개조식과 잘 맞는다. `gitignore` 는 개발자끼리 동사로도 쓴다. 풀어 쓰면 `No need to add it to .gitignore.`

### 카드 24 — 하드코딩 금지, 있는 것만 표시   (내가 쓴 한글)
- 내가 쓴 한글: "디테일 페이지에 측정 정보 key들은 13, 15 variation이 있다. … 키 하드코딩 금지 존재하는 키만 화면에 표시, 빈 값은 null 처리."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: The measurement info on the detail page comes in two variants, with 13 keys or 15. Don't hard-code the keys: show only the ones that are present, and treat empty values as null.
- 왜 이렇게: "variation이 있다"는 `comes in two variants`. `come in` 은 제품이 몇 가지 종류로 나온다고 할 때 쓰는 동사다(`comes in three sizes`). 종류 하나하나는 `variant`, 차이 자체는 `variation`. "~ 금지"는 `Don't …` 명령문이면 충분하고 규칙 문서라면 `Never hard-code the keys.` "존재하는 키만"은 `only the ones that are present`. "null 처리"는 `treat … as null`. `process as null` 은 쓰지 않는다.

### 카드 25 — 일부만으로 계산한 통계가 정상처럼   (고급 한글 · 번역)
- 한글 원문: "실패를 `null`로 삼키는 설계는 한두 건 누락에는 맞지만, 429처럼 한꺼번에 실패하면 '일부만으로 계산한 통계'가 정상처럼 보이게 됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Swallowing failures as `null` is fine when one or two requests drop, but when they fail all at once, as with a 429, statistics computed from partial data end up looking normal.
- 번역 포인트: "~하는 설계는"을 `A design that swallows …` 로 따라가면 주어가 길어진다. 동명사 `Swallowing failures as null` 로 행위를 주어에 세운다. "한두 건 누락에는 맞지만"은 `is fine when one or two requests drop`. "한꺼번에"는 `all at once`. "일부만으로 계산한 통계"는 과거분사 후치 수식 `statistics computed from partial data`. "~하게 됩니다"는 의도하지 않은 결말이라 `end up -ing`.

### 카드 26 — 자기를 잡아야 할 관리선   (고급 한글 · 번역)
- 한글 원문: "σ가 MAD 기반이라 이상치 하나가 자기를 잡아야 할 관리선을 넓히지 못합니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Because σ is MAD-based, a single outlier can't widen the very control limits that are supposed to catch it.
- 번역 포인트: 재미있는 대목은 "자기를 잡아야 할". 영어로는 관계절 `that are supposed to catch it` 으로 풀고 `the very` 를 붙여 "바로 그"라는 아이러니를 살린다. `be supposed to` 는 마땅히 해야 할 역할. "넓히지 못합니다"는 능력의 부정이라 `can't widen`. "MAD 기반"은 하이픈 형용사 `MAD-based`. "관리선"은 SPC 용어로 `control limits`. `Because` 절을 앞에 두면 원인 다음 결과라는 한국어 순서가 그대로 선다.

### 카드 27 — 다시 붙이는 일만 생긴다   (고급 한글 · 번역)
- 한글 원문: "같은 grain을 두 key로 나누면 `unique_key`로 다시 붙이는 일만 생깁니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Splitting the same grain across two keys buys you nothing but a join back on `unique_key`.
- 번역 포인트: "~하는 일만 생깁니다"는 얻는 것 없이 일만 는다는 뜻이다. `buys you nothing but X` 가 그 손익 계산을 그대로 옮긴다. 평이하게는 `just means you have to join them back`. "두 key 로 나누다"는 `split … across two keys` 이고 전치사 `across` 가 "여러 곳에 걸쳐"를 맡는다. "다시 붙이다"는 데이터 문맥이라 `join back on`(조인 키 앞에는 `on`). `grain` 은 데이터 모델링에서 한 행이 무엇을 나타내는가를 가리키는 용어여서 그대로 둔다.

### 카드 28 — 키와 문구가 따로 놀지 않는다   (고급 한글 · 번역)
- 한글 원문: "설명 문구의 번호는 탭을 만드는 `TYPES` 목록에서 그대로 읽어 오므로, 나중에 종류가 추가되거나 순서가 바뀌어도 키와 문구가 따로 놀지 않습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: The numbers in the hint are read straight from the `TYPES` list that builds the tabs, so the keys and the hint can't drift apart even if a type is added or the order changes later.
- 번역 포인트: "따로 놀다"는 둘이 맞물리지 않고 어긋난다는 관용 표현. 코드 문맥에서는 `drift apart` 나 `get out of sync` 가 맞는다. "그대로 읽어 오므로"는 `are read straight from`. `straight` 가 중간에 손대지 않는다는 뜻을 싣는다. 읽는 주체가 중요하지 않아 수동태로 썼다. "~해도"는 `even if`. "탭을 만드는 목록"은 관계절 `the list that builds the tabs` 로 뒤에 붙인다.

## 영어 다듬기

### 카드 29 — commit and push all
- 내가 쓴 영어: "commit and push all"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Commit and push everything.
- 왜: `all` 은 혼자서 목적어 자리에 서는 일이 드물다. 대명사로 쓰려면 `all of it`, 아니면 `everything`. `push all changes` 처럼 명사 앞에 두면 문제없다. 뜻은 통하니 오류라기보다 어색함에 가깝다.

### 카드 30 — now can I make office.py
- 내가 쓴 영어: "now can I make office.py for the afm page?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Can I create office.py for the AFM page now? / Is the AFM page ready for me to create office.py?
- 왜: 문법은 맞다. 문두의 `now` 는 "자, 그럼"이라는 화제 전환으로도 읽히므로 "이제는 되나?"라는 뜻이면 문장 끝에 두는 쪽이 분명하다. 파일은 `make` 보다 `create` 가 흔하다. 둘째 문장은 허락이 아니라 준비 상태를 묻는 꼴이고 실제 답도 `the template is ready to copy` 로 시작했다.

### 카드 31 — I give you the info, codes
- 내가 쓴 영어: "for afm, I give you the info about redis. update what we have here (docs, codes like office_example.py)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `I give you` → `I'm giving you` 또는 `here's`. 지금 건네는 동작은 단순현재가 아니라 진행형으로 쓴다. `codes` → `code`. 프로그램 코드는 셀 수 없는 명사이고 `codes` 는 암호나 코드 번호(`error codes`)를 말할 때만 복수가 된다.
- 더 나은 표현: Here's the Redis spec for AFM. Update what we have to match — the docs and the code, e.g. office_example.py.
- 왜: 자료를 건넬 때는 `Here's …` 가 가장 흔한 출발이다. `info about redis` 는 `the Redis spec` 으로 좁히면 무엇을 주는지 또렷하다. `to match` 는 "이 명세에 맞게"를 두 낱말로 붙인다. `what we have here` 는 잘 쓴 표현이라 살렸다.

### 카드 32 — write the questionnaire
- 내가 쓴 영어: "write the questionnaire for the office about the OFFICE-VERIFY items"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Draft a questionnaire for the office covering the OFFICE-VERIFY items.
- 왜: 오류는 없다. 다만 아직 없는 문서를 새로 쓰는 일이라 `the` 보다 `a` 가 맞고 이미 넷이 있었으니 `the next questionnaire` 도 된다. `draft` 는 검토를 받을 초안이라는 뜻을 싣고 `covering` 은 `about` 보다 빠짐없이 다룬다는 느낌이 있다.

### 카드 33 — I found that 404 errors … in the path
- 내가 쓴 영어: "from admin/logs, I found that 404 errors from User anonymous in the path /api/msr-image. is that on purpose?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `I found that 404 errors from … in the path …` 는 `that` 절에 동사가 없다. `that` 을 빼서 `I found 404 errors …` 로 하거나 `I found that there are 404 errors …` 로 동사를 넣는다. 경로 앞 전치사는 `in` 이 아니라 `on`(`on the path /api/msr-image`). 문장 첫 글자는 대문자 `Is`.
- 더 나은 표현: In admin/logs I'm seeing 404s on /api/msr-image from the user `anonymous`. Is that intentional?
- 왜: 로그에서 지금 보이는 현상은 `I'm seeing …` 으로 말하는 것이 개발자 구어다. `404 errors` 는 `404s` 로 줄인다. `on purpose` 는 자연스러운 구어이고 `intentional` 은 한 단계 격식, `by design` 은 설계가 그렇다는 쪽이다. 답변이 세 표현을 다 썼다.

### 카드 34 — error_name is Not Found.
- 내가 쓴 영어: "error_name is  Not Found."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: The error_name column just says "Not Found".
- 왜: 문법은 맞다. 필드나 화면에 적힌 값을 전할 때는 `says` 나 `reads` 가 `is` 보다 "그렇게 쓰여 있다"를 잘 전한다. `just` 를 넣으면 "그것뿐이라 더 알 수가 없다"는 뜻이 실리고 값에 따옴표를 치면 어디까지가 값인지 분명해진다.

### 카드 35 — is not responsive anymore
- 내가 쓴 영어: "작게 보통 크게 is not responsive anymore."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 주어가 버튼 셋이라 `is` → `are`. 묶음 하나로 보려면 `The 작게/보통/크게 toggle is …` 처럼 단수 명사를 세운다.
- 더 나은 표현: The 작게/보통/크게 buttons don't do anything anymore.
- 왜: 웹에서 `responsive` 는 화면 폭에 따라 레이아웃이 바뀐다는 뜻으로 먼저 읽힌다. 눌러도 반응이 없다는 뜻이면 `don't do anything` 이나 `have stopped working`, 조금 격식 있게는 `no longer respond to clicks`. 형용사를 살리려면 `unresponsive` 가 그 뜻에 가깝다. `anymore` 는 맞게 썼다.

### 카드 36 — in the video folder from the root
- 내가 쓴 영어: "I will place the two mp4 files in the video folder from the root. SmartAlignment_Agent.mp4 and ARC_PWI_자막_배속조정-후반부 2배속.mp4."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the video folder from the root` → `the video folder at the repo root`. 위치는 `at` 이나 `under`(`under the root`)로 말한다. `from the root` 는 경로를 세는 기준점을 말할 때 쓴다(`the path relative to / from the root`).
- 더 나은 표현: I'll put the two MP4 files in the `video` folder at the repo root: SmartAlignment_Agent.mp4 and ARC_PWI_자막_배속조정-후반부 2배속.mp4.
- 왜: 대화에서는 `I will` 보다 `I'll` 이, `place` 보다 `put` 이 자연스럽다. `place` 는 설명서 말투다. 파일 이름 둘은 동사 없는 조각 문장으로 떼지 말고 콜론으로 앞 문장에 붙이면 "그 두 파일이 이것"이라는 관계가 선다.
