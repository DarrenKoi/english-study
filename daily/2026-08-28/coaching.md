# 2026-08-28 — 코칭

오늘 배치의 `[user]` 메시지는 전부 영어라 "내가 쓴 한글" 카드는 없다. 대신 영어 다듬기가 여섯 장이다.

## 한글→영어

### 카드 1 — 표의 성격을 설명하는 한 줄   (고급 한글 · 번역)
- 한글 원문: "선택한 장비에서 실행한 레시피를 모두 모은 표입니다. 그 장비에서 실행 이력이 없는 레시피는 —로 표시합니다."   (출처: transcript:[assistant] skewnono-v3-nuxt f9b54b3d)
- 자연스러운 영어: Every recipe that ran on any of the selected tools, in one table. A dash means that tool has no run history for that recipe.
- 번역 포인트: "모두 모은 표입니다"를 `a table that gathers all …` 로 직역하면 관계절이 무거워진다. 명사구 하나(`Every recipe that ran on …`)에 `in one table` 을 붙이면 UI 캡션 길이에 맞는다. "실행 이력이 없는"은 부정 관계절 대신 소유 구문 `has no run history` 로 뒤집는 편이 짧고, 주어를 표시 기호(`A dash`)로 잡아 화면에서 눈에 보이는 것부터 말하는 게 UI 문구의 어순이다. `—` 를 그대로 두지 말고 영어로는 `a dash` 라고 이름을 불러 줘야 스크린리더에서도 읽힌다.

### 카드 2 — 다시 쓰기 전의 문장   (고급 한글 · 번역)
- 한글 원문: "선택 장비들이 돈 레시피의 합집합입니다. 돌지 않은 장비는 —로 표시됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt f9b54b3d)
- 자연스러운 영어: The union of the recipes the selected tools ran. Tools that didn't run are shown as a dash.
- 번역 포인트: 사용자가 "부자연스럽다"고 지적한 그 문장인데, 영어로 옮겨 보면 왜 어색한지가 드러난다. `union` 은 집합론 용어라 화면에서 읽는 사람에게는 한 겹의 번역이 더 필요하고, 둘째 문장은 주어가 어긋나 있다 — 실제로 대시가 붙는 것은 장비가 아니라 **그 장비·레시피 칸**이다. 한국어 원문의 "돌지 않은 장비는"이 그 오류를 그대로 안고 있었고, 번역하면 `Tools … are shown as a dash` 라는 말이 안 되는 문장이 된다. 번역은 이렇게 원문의 논리 결함을 드러내는 검사 도구로도 쓸 수 있다.

## 영어 다듬기

### 카드 1 — 이미지 갤러리 레이아웃 요청
- 내가 쓴 영어: "In image gallery from skewvoir/analysis, the way we display images should be organized. We can use lattice style of table. The images are displayed based on the chip (field locations). Images are thumnaled (small sized images) inside the lattice and below the images we can also see the cd values. Of course, some users want to see the image in a large (original size). So we can offer the option to look what I just described."   (출처: transcript:[user] skewnono-v3-nuxt 86fb71e7)
- 정정:
  - `In image gallery from skewvoir/analysis` → `In the image gallery on skewvoir/analysis`. 특정 화면 하나를 가리키므로 정관사가 필요하고, 페이지 위의 요소는 `from` 이 아니라 `on` 이다.
  - `lattice style of table` → `a lattice-style table`. 명사를 형용사로 쓸 때는 하이픈으로 붙이고 `of` 를 넣지 않는다.
  - `thumnaled` → 철자 오류이자 존재하지 않는 동사다. `shown as thumbnails` 로 푼다.
  - `see the image in a large (original size)` → `at original size`. 크기에는 `at` 을 쓰고, `a large` 는 명사가 빠져 성립하지 않는다.
  - `the option to look what I just described` → `look` 은 목적어에 `at` 이 필요하다. 여기서는 `view` 가 더 낫다.
- 더 나은 표현: In the skewvoir/analysis gallery, the images need a real layout instead of a flat list. Lay them out on a lattice keyed to the chip (field) position, each image as a thumbnail with its CD value underneath. Some users will still want the full-size original, so keep a way to open any thumbnail at 100%.
- 왜: 원문은 다섯 문장에 걸쳐 "이렇게 하면 된다"를 나열하는데, 요구사항은 명령형으로 쓸 때 훨씬 짧고 오해가 없다. `We can use …` 를 반복하면 제안인지 지시인지 모호해진다. `keyed to` 는 "무엇을 기준으로 배치하는가"를 한 단어로 지정하는 UI 어휘이고, 마지막 문장의 `still` 이 "썸네일로 바꿔도 원본 요구는 남는다"는 전제를 살려 준다.

### 카드 2 — pm-planning 컨트롤 위치 요청
- 내가 쓴 영어: "In the pm-planning page, 튜닝할 장비 is the foremost important option but now it is placed the far-right side and hard to noticeable to users. can you move the 튜닝할 장비 component and make more noticeable?"   (출처: transcript:[user] skewnono-v3-nuxt 584bd187)
- 정정:
  - `In the pm-planning page` → `On the pm-planning page`. 페이지 위에 놓인 것을 말할 때는 `on` 이다.
  - `the foremost important` → `foremost` 자체가 최상급이라 `important` 와 겹친다. `the single most important` 로 쓴다.
  - `it is placed the far-right side` → 전치사가 빠졌다. `it sits on the far right` 또는 `it's placed at the far right`.
  - `hard to noticeable` → `hard to` 뒤에는 동사원형이 온다. `hard to notice`, 또는 자연스럽게 `easy to miss`.
  - `make more noticeable` → 목적어가 필요하다. `make it more noticeable`.
- 더 나은 표현: On the pm-planning page, 튜닝할 장비 is the single most important control, but it currently sits at the far right where users miss it. Could you move it somewhere more prominent?
- 왜: `option` 보다 `control` 이 화면 위젯을 가리키는 정확한 단어다. `hard to notice` 를 `where users miss it` 이라는 관계부사절로 바꾸면 불평이 아니라 관찰 보고가 되고, 문제(위치)와 증상(놓친다)이 한 절에 묶인다. 요청은 `Could you …?` 로 여는 편이 `can you` 보다 부드러우면서도 지시의 힘은 그대로다.

### 카드 3 — 페이지 재그룹 의견 요청
- 내가 쓴 영어: "If you would group the pages based on the similar characteristics, how would you group the pages? compared to the current setting in the top nav (recipe-search, 실험실, etc). give me your opinion. As we grow up and make more pages down the road. we might need to reorganize the pages and re-group them."   (출처: transcript:[user] skewnono-v3-nuxt f0e35121)
- 정정:
  - `If you would group` → 가정을 세울 때는 `If you were to group`. `would` 는 조건절이 아니라 주절에 온다.
  - `based on the similar characteristics` → 일반적인 성질을 말하므로 정관사를 뺀다. `by shared characteristics`.
  - `As we grow up` → `grow up` 은 사람이 어른이 되는 것이다. 앱·조직에는 `As we grow` 또는 `As the app grows`.
  - `As we grow up and make more pages down the road.` → 마침표로 끊겨 종속절만 남은 조각 문장이다. 뒤 문장과 이어야 한다.
- 더 나은 표현: If you were to group the pages by shared characteristics, how would you group them — and how does that compare with what the top nav does today (recipe-search, 실험실, and so on)? I'd like your opinion. As the app grows and we add pages down the road, we may need to reorganize and regroup them.
- 왜: 두 번째 `the pages` 를 대명사 `them` 으로 받으면 반복이 사라진다. `compared to …` 를 독립된 조각으로 두는 대신 대시로 붙여 하나의 질문에 넣으면 "네 안을 말하고, 현재와 비교까지 해 달라"는 요구가 한 번에 전달된다. `give me your opinion` 은 명령형이라 다소 퉁명스럽게 읽히므로 `I'd like your opinion` 이 무난하다.

### 카드 4 — AFM·Thickness 의 분기 판단
- 내가 쓴 영어: "AFM, Thinkness will lead to separate pages with different styles (bifurcate from the landing page). Skewvoir also should be remain as standalone as it continues to grow."   (출처: transcript:[user] skewnono-v3-nuxt f0e35121)
- 정정:
  - `Thinkness` → `Thickness` 철자 오류.
  - `AFM, Thinkness will lead to` → 두 항목을 나열할 때는 쉼표가 아니라 `and` 로 잇는다. `AFM and Thickness will …`.
  - `should be remain` → `be` 와 `remain` 이 겹친다. `should remain`.
  - `also should` → 부사 위치가 어색하다. `should also remain`.
  - `as standalone` → 보어로 쓸 때는 관사 없이 `standalone` 이거나 `as a standalone app`.
- 더 나은 표현: AFM and Thickness will each need their own pages with their own visual language — they branch off at the landing page. Skewvoir should also stay standalone as it keeps growing.
- 왜: `lead to separate pages` 는 "결과적으로 그렇게 된다"로 읽혀 주체가 흐려진다. `will each need` 로 바꾸면 요구사항 진술이 되고 `each` 가 둘을 따로 취급함을 표시한다. `bifurcate` 는 정확한 단어지만 괄호에 가둬 두기엔 아깝다 — 본문 동사 `branch off` 로 올리면 문장이 스스로 설명한다. `remain` 보다 `stay` 가 구어 요청에 어울린다.

### 카드 5 — 아직 구현하지 말라는 지시
- 내가 쓴 영어: "not yet. this is just planning. just give me the outlook of the tabs with html file. so I can understand better"   (출처: transcript:[user] skewnono-v3-nuxt f0e35121)
- 정정:
  - `the outlook of the tabs` → `outlook` 은 전망·관점이지 겉모습이 아니다. 여기서는 `a mockup of the tabs` 또는 `what the tabs would look like`.
  - `with html file` → `as an HTML file`. 산출물의 형식을 말할 때는 `as` 를 쓰고 관사가 필요하다.
  - `so I can understand better` → 목적어가 없어 허전하다. `so I can picture it` 또는 `so I get a better feel for it`.
- 더 나은 표현: Not yet — this is still planning. Just mock up what the tabs would look like as an HTML file so I can picture it.
- 왜: 짧은 지시문 세 개를 나열하는 대신 대시와 `so` 로 이으면 "지금은 아니다 → 이유 → 대신 이것을" 이 한 흐름이 된다. `mock up` 은 동사로 쓰면 "시안을 만들다"라는 뜻이 정확히 전달되고, `Just` 를 문두에 두어 범위를 제한하는 어감을 유지했다. `picture` 는 "머릿속에 그리다"라서 `understand` 보다 이 상황에 맞는다.

### 카드 6 — recipe-status 컬럼 수정 요청
- 내가 쓴 영어: "In recipe-status page, we have 장비별 tab and are able to see 레시피 구성 비교. the Korean sentence you wrote does not seem natural to me. And the numbers you display are hard to understand. You can amend the column and may well to explain the meaning of numbers in the columns for eqp_id list. use skills /unlazy. check tat, align fail and meas fail."   (출처: transcript:[user] skewnono-v3-nuxt f9b54b3d)
- 정정:
  - `In recipe-status page` → `On the recipe-status page`. 관사와 전치사 둘 다.
  - `we have 장비별 tab and are able to see` → 주어가 `we` 로 이어지며 문장이 늘어진다. `the 장비별 tab shows …` 로 주어를 화면 요소에 넘긴다.
  - `may well to explain` → `may well` 뒤에는 `to` 없이 동사원형이 오고, 뜻도 "아마 ~할 것이다"라 여기 의도와 다르다. `and it would help to explain`.
  - `the meaning of numbers in the columns for eqp_id list` → 전치사구가 세 겹으로 쌓였다. `what each number in the eqp_id columns means` 로 절로 푼다.
  - `use skills /unlazy` → `use the /unlazy skill`. 단수이고 관사가 필요하다.
- 더 나은 표현: On the recipe-status page, the 장비별 tab shows 레시피 구성 비교. The Korean sentence you wrote there doesn't read naturally to me, and the numbers are hard to interpret. Please rework the columns and spell out what each number in the eqp_id columns means. Use the /unlazy skill, and cover TAT, align fail, and meas fail.
- 왜: `does not seem natural` 도 통하지만 문장을 평가할 때는 `doesn't read naturally` 가 관용적이다 — 정독 단락 2의 `the table still reads …` 와 같은 `read` 용법이다. `hard to understand` 를 `hard to interpret` 로 바꾸면 "숫자가 무엇을 뜻하는지 판단이 안 된다"는 뜻이 정확해진다. `spell out` 은 "명시적으로 풀어 적다"라 `explain the meaning of` 를 두 단어로 대체한다. 마지막 문장의 `cover` 는 "이 세 가지를 빠짐없이 다뤄라"를 한 동사로 전한다.
