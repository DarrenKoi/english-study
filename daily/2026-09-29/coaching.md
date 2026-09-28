# 2026-09-29 — 코칭

## 한글→영어

### 카드 1 — 파일 특정 줄 확인 부탁   (내가 쓴 한글)
- 내가 쓴 한글: "UPLOAD.md 167줄 근처 확인해줘"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: Can you take a look at UPLOAD.md around line 167?
- 왜 이렇게: "~줄 근처"는 `around line 167` 이다. `near the 167th line` 은 어색하고 줄 번호는 `line + 숫자` 로 쓴다. "확인해줘"는 무엇을 검증하라는 게 아니라 한번 봐 달라는 뜻이라 `check` 보다 `take a look at` 이 부드럽다. 무엇을 봐야 하는지 알면 `… and see whether the diagnose_paths check is there` 처럼 목적을 붙이면 더 좋다.

### 카드 2 — 파일 비우기   (내가 쓴 한글)
- 내가 쓴 한글: "now.md 비워줘"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: Clear out now.md.
- 왜 이렇게: 파일 내용을 비우는 건 `clear (out)` 또는 `empty` 다. `delete now.md` 로 쓰면 파일 자체를 지우라는 뜻이 되니 주의. `out` 을 붙이면 "싹 비운다"는 느낌이 산다. 파일은 남기고 내용만 지운다는 걸 확실히 하려면 `Empty now.md but keep the file.`

### 카드 3 — 두 절의 역할 분담   (고급 한글 · 번역)
- 한글 원문: "두 절이 다른 시점을 맡는 게 이 문서의 설계다. 58줄은 48GB 를 올리기 전, 167줄은 이미 올린 뒤."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: The doc is designed so that its two sections cover different moments: line 58 is for before you upload 48 GB, and line 167 is for after.
- 번역 포인트: "~하는 게 이 문서의 설계다"를 `The design of this doc is that …` 으로 직역하면 무겁다. `is designed so that` 으로 동사화하면 자연스럽다. "시점을 맡다"는 `cover different moments` 나 `handle different stages` 로 옮긴다. 원문 둘째 문장은 동사가 없는 명사문인데 영어에서는 `is for before … / after` 로 전치사구를 보어로 써서 짧게 유지한다.

### 카드 4 — 이유가 문서에 남았다   (고급 한글 · 번역)
- 한글 원문: "진단 코드가 왜 그렇게 생겼는지가 코드가 아니라 문서에 남았다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: The reason the diagnostic code looks the way it does is written down in the doc, not in the code.
- 번역 포인트: "왜 그렇게 생겼는지"는 `why it looks the way it does` 가 관용 틀이다. 이 절을 그대로 주어로 쓰면(`Why the code looks … is recorded`) 문법은 맞아도 머리가 무거워 `The reason (that) …` 으로 푼다. "남았다"는 `remained` 가 아니라 기록됐다는 뜻이라 `is written down` / `is recorded`. `A, not B` 대비는 영어에서도 그대로 살린다.

### 카드 5 — 조치가 같아도 기록하라   (고급 한글 · 번역)
- 한글 원문: "재시작은 원인을 안 남기니까. 조치가 같아도 진단을 기록하라는 것."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: A restart leaves no trace of the cause, so even when the fix is the same, record the diagnosis.
- 번역 포인트: 원문은 이유("~니까")를 먼저 끊어 말하고 결론을 "~라는 것"으로 닫는 구어체다. 영어는 `A, so B` 한 문장으로 합치는 편이 자연스럽다. "원인을 안 남긴다"는 `leaves no trace of the cause` 가 딱 맞다. `doesn't leave the cause` 는 뜻이 통하지 않는다. "조치"는 여기서 `fix` 또는 `remedy`, "~라는 것"은 번역하지 않고 명령문으로 바꾼다.

### 카드 6 — 인계가 아니라 버퍼   (고급 한글 · 번역)
- 한글 원문: "`now.md` 의 두 줄은 이미 커밋된 작업을 가리키고 있다 — 실제 인계가 아니라 그냥 안 지워진 버퍼다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: The two lines in `now.md` point to work that's already committed. They aren't a real handoff, just a buffer nobody cleared.
- 번역 포인트: "인계"는 `handoff` 가 개발 협업에서 굳은 말이다. "안 지워진 버퍼"를 `an undeleted buffer` 로 옮기면 어색하다. 관계절 `a buffer nobody cleared` 로 "아무도 안 치웠다"는 뉘앙스를 살린다. `not A but B` 대신 `aren't A, just B` 를 쓰면 "별것 아니다"는 가벼운 톤이 난다.

## 영어 다듬기

### 카드 1 — 그 파일 어디 있지
- 내가 쓴 영어: "where is the file that I used to click "File Manager"?"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Where's the script I used to click the "File Manager" button?
- 왜: 문법은 통한다. 다만 `click "File Manager"` 만으로는 무엇을 누르는지 흐리니 `the … button` 을 붙인다. 실행 파일이면 `file` 보다 `script` 가 정확하고 목적격 관계대명사 `that` 은 빼도 된다. 문장 첫 글자는 대문자.

### 카드 2 — 워크플로 요청
- 내가 쓴 영어: "I want you to make a workflow to open a recipe starting from opening the File Manager. once you click the File Manager, you will have a big window to display recipe list."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `to display recipe list` → `that displays the recipe list`. 특정 목록이라 관사 `the` 가 필요하다. 문장 첫 `once` 는 대문자 `Once`.
- 더 나은 표현: Build a workflow that opens a recipe, starting from the File Manager. Clicking File Manager brings up a large window with the recipe list.
- 왜: `starting from opening` 처럼 -ing 가 겹치면 무겁다. `starting from the File Manager` 로 충분하다. "창이 뜬다"는 `you will have a window` 보다 `brings up a window` / `opens a window` 가 자연스럽다.

### 카드 3 — 열 네 개와 행 클릭
- 내가 쓴 영어: "it has 4 columns. Class, IDW, IDP, Recipe. Firstly, you click the one of rows in Class."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the one of rows` → `one of the rows`. `one of + the + 복수명사` 가 정해진 틀이다. 열 이름 나열은 마침표 대신 콜론으로 앞 문장에 붙인다.
- 더 나은 표현: It has four columns: Class, IDW, IDP and Recipe. First, click one of the rows in the Class column.
- 왜: 단계 안내에서는 `Firstly` 보다 `First` 가 흔하다. 지시할 때는 `you click` 보다 명령문 `click` 이 간결하다. `in Class` 는 `in the Class column` 으로 열이라는 걸 밝혀 준다.

### 카드 4 — 스크롤하거나 입력하거나
- 내가 쓴 영어: "Either you can drag the scroll to search the class name or type in the column to search it."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `Either you can A or B` → `You can either A or B`. `either` 는 `or` 와 짝이 되는 요소 바로 앞에 둔다. `the scroll` → `the scrollbar`.
- 더 나은 표현: You can either drag the scrollbar to find the class name or type it into the column's search box.
- 왜: 이미 있는 항목을 찾는 거라 `search the class name` 보다 `find the class name` 이 맞다. `search` 는 `search for` 로 써야 "~를 찾다"가 된다. `search the list for the name` 처럼 목적어가 장소일 때만 전치사 없이 쓴다.

### 카드 5 — 같은 방식으로
- 내가 쓴 영어: "and then you click the class name. next you click the Recipe name (4th column) in the same way you do find class."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `in the same way you do find class` → `the same way you found the class`. 강조 조동사 `do` 가 불필요하고 시제는 이미 끝낸 동작이라 과거형, `class` 에는 관사가 필요하다.
- 더 나은 표현: Then click the class name. Next, find the recipe name in the Recipe column (the 4th) the same way, and click it.
- 왜: `and then` 으로 문장을 시작하지 않는다. `the same way` 는 `in` 없이도 부사로 쓰여 더 가볍다.

### 카드 6 — 새 파일 만들어도 돼
- 내가 쓴 영어: "you can make a new py file."   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Feel free to create a new `.py` file.
- 왜: `you can` 은 능력·허가 둘 다로 읽힌다. `Feel free to` 는 "그래도 괜찮다"는 허가의 뜻이 분명하다. 파일은 `make` 보다 `create` 가 표준이고 확장자는 `.py` 로 표기한다.

### 카드 7 — recipe_ID 형식 알려 주기
- 내가 쓴 영어: "you know that recipe_ID comes with like RJ1BXXX_CG6300/RJ1B_ISOCO_EUVSPT. and class name is the RJ1BXXX_CG6300 and Recipe is the RJ1B_ISOCO_EUVSPT"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `comes with like` → `looks like` 또는 `comes in the form`. `comes with` 는 "~이 딸려 온다"는 뜻. 고유 값 앞 `the RJ1BXXX_CG6300` 의 `the` 는 빼고 `class name` 앞에는 `the` 를 붙인다.
- 더 나은 표현: Note that a recipe_ID looks like `RJ1BXXX_CG6300/RJ1B_ISOCO_EUVSPT`: the part before the slash is the class name, and the part after it is the recipe.
- 왜: `you know that …` 은 "알다시피"라 상대가 모르는 정보를 줄 때 어색하다. `Note that` 이 맞다. 예시 값을 두 번 반복하는 대신 "슬래시 앞/뒤"라는 규칙으로 말하면 짧고 일반화된다.

### 카드 8 — 공지사항에 반영
- 내가 쓴 영어: "update what we have done so far in 공지사항"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Add a 공지사항 entry covering what we've done so far.
- 왜: `update X in Y` 는 "Y 안의 X 를 고치다"로 읽힌다. 새 공지를 추가하는 거라 `add an entry` 가 정확하다. `covering` 은 "~을 다루는"이다.

### 카드 9 — 거의 같은데 아직 실패
- 내가 쓴 영어: "I think the recipe and consensus is almost identical to the images from real wafer. still fail in alignment correction for OM image and fall back to search around (still cannot find it while searching around)."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 주어가 `the recipe and consensus` 둘이라 `is` → `are`. `real wafer` → `the real wafer`. 둘째 문장은 주어가 없다. `It still fails …, falls back to …`.
- 더 나은 표현: The recipe and consensus images look almost identical to the real wafer, but OM alignment correction still fails. It falls back to search-around and doesn't find the key there either.
- 왜: `still … still` 반복을 `still` 과 `either` 로 나눴다. 괄호 속 부연은 문장으로 풀어 쓰면 읽기 쉽다. "~인데도 실패"의 대비는 `but` 하나로 잡힌다.

### 카드 10 — 초록 박스 위치
- 내가 쓴 영어: "the green box locates correctly. Not sure the key box is wider than 128 px. The green box seem stretch upto 1/3 of the image."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `locate` 는 타동사라 `the green box is located correctly` 또는 `is in the right place`. `seem stretch` → `seems to stretch` (3인칭 단수 + `to` 부정사). `upto` → `up to`.
- 더 나은 표현: The green box is in the right place. I'm not sure whether the key box is wider than 128 px, but the green box seems to span about a third of the image.
- 왜: `Not sure …` 도 구어로 통하지만 `I'm not sure whether` 가 완결된 문장. 길이를 말할 때 `span` 이 `stretch up to` 보다 간결하고 `1/3` 은 문장에서 `a third` 로 쓴다.

### 카드 11 — 사무실 답장 전달
- 내가 쓴 영어: "sent the @docs/datatables/hitachi/hardware_fdc_sce_characterization.md to the office agent and here's the reply. There is must fix (breaks today)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 주어 `I` 가 빠졌다. `There is must fix` → `There are must-fix items`. `must-fix` 는 형용사로 쓸 때 하이픈을 넣고 뒤에 명사가 와야 한다.
- 더 나은 표현: I sent the characterization brief to the office agent, and here's the reply. Some items are must-fix: they break today.
- 왜: `(breaks today)` 를 괄호로 달기보다 콜론 뒤 절로 풀면 이유가 분명해진다. 채팅 메모라면 `Must-fix (breaks today):` 머리말 형식도 괜찮다.

### 카드 12 — unlazy 로 적용해
- 내가 쓴 영어: "use /unlazy apply the node given my the office agent. amend the code base."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 오타 `node` → `notes`, `my` → `by`. `use X apply` → `use X to apply` (목적의 `to` 부정사).
- 더 나은 표현: Use /unlazy to apply the office agent's notes and update the codebase accordingly.
- 왜: `the notes given by the office agent` 는 소유격 `the office agent's notes` 로 줄인다. `amend` 는 문서·법안·커밋을 "수정하다"에 주로 쓰고 코드 전반에는 `update … accordingly` 가 자연스럽다. `codebase` 는 붙여 쓴다.

### 카드 13 — 게으르지만 옳은 수정
- 내가 쓴 영어: "in scheduler, we go lazy correct fix: emit typed side-fields at write time in the FDC task, keep values untouched. … so that we have fleet views become native, cheap aggregations instead of raw pulls."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `we go lazy correct fix` → `we'll go with the lazy but correct fix` (`go with` = 택하다). `so that we have fleet views become` 는 `have` 와 `become` 이 겹친다. `so that the fleet views become …`.
- 더 나은 표현: In the scheduler, let's go with the lazy but correct fix: emit typed side-fields at write time in the FDC task and leave `values` untouched. That way the fleet views become cheap, native aggregations instead of raw pulls.
- 왜: `keep values untouched` 도 되지만 `leave … untouched` 가 더 관용적. 형용사 순서는 의견·평가(`cheap`)가 성질(`native`)보다 앞에 오는 게 자연스럽다. `so that` 대신 `That way` 로 문장을 끊으면 지시와 효과가 나뉜다.

### 카드 14 — 이제 진행해도 되나
- 내가 쓴 영어: "so now, are we ready to tell the office agent to change the data for hardware?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: So, are we ready to give the office agent the go-ahead on the hardware data change?
- 왜: 오류는 없다. `tell … to change` 는 "바꾸라고 말하다"라 지시만 담긴다. `give … the go-ahead` 는 "진행 승인"이라 오늘 대화의 맥락(조건 붙은 착수 허가)에 더 맞는다. `the data for hardware` 는 명사 수식으로 `the hardware data` 가 짧다.

### 카드 15 — 새 코드가 돌기 시작
- 내가 쓴 영어: "now for hardware renovated code-base starts to run. we will check tomorrow."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 어순과 관사. `for hardware renovated code-base` → `the renovated hardware codebase`. 지금 막 시작해 진행 중인 상태라 `starts to run` → `has started running` 또는 `is now running`.
- 더 나은 표현: The renovated hardware code is now live at the office. We'll check on it tomorrow.
- 왜: 운영 환경에 올라갔다는 뜻이면 `is live` 가 정확하다. `check` 는 목적어 없이 끝나면 어색해 `check on it`(상태를 살피다)으로 쓴다.

### 카드 16 — N 표기 제거
- 내가 쓴 영어: "remove (N) notation in the 공지사항 page. I think most of users don't consider that much."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `most of users` → `most users` (`most of` 뒤에는 한정사가 필요하다: `most of the users`). 페이지 "위에" 있는 요소라 `in the page` → `on the page`.
- 더 나은 표현: Remove the "N" badge on the 공지사항 page. I don't think most users pay much attention to it.
- 왜: `consider` 는 "고려하다, 숙고하다"라 "눈여겨보다"에는 `pay attention to` / `notice` 가 맞다. 영어는 `I think … don't` 보다 `I don't think …` 로 부정을 앞으로 올리는 게 자연스럽다. 이번 세션에서는 `(N) notation` 이 모호해서 어시스턴트가 칩 개수로 잘못 읽었다. UI 요소는 `badge` 처럼 이름을 짚어 주면 오해가 준다.

### 카드 17 — N 이 뜻하는 것
- 내가 쓴 영어: "N means new. including unread badge." / "N means unread badge. ."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: By "N", I mean the unread badge.
- 왜: `N means …` 는 기호의 사전적 뜻을 설명하는 말이라 "내가 말한 N 은 ~이다"에는 `By X, I mean Y` 가 정확하다. `including unread badge` 는 주어·동사가 없는 조각이다. 정정할 때는 한 문장으로 다시 말하는 편이 낫다.

### 카드 18 — agent-browser 로 확인
- 내가 쓴 영어: "you agent-browser to check it"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 오타 `you` → `use`.
- 더 나은 표현: Use agent-browser to check it on the page.
- 왜: `use X to do` 틀 그대로다. 무엇을 확인하는지(`on the page`, `that the badge is gone`)를 붙이면 검증 기준까지 전달된다.

### 카드 19 — 맨 위에 둘 필요 없다
- 내가 쓴 영어: "you do not need to place v3 정식 출시 at the top. That's just just one of normal updates."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `just just` 중복. `one of normal updates` → `one of the regular updates` (`one of + the + 복수`).
- 더 나은 표현: No need to pin "v3 정식 출시" to the top. It's just a regular update like the others.
- 왜: UI 에서 맨 위에 고정하는 건 `pin` 이 정확한 동사다. `place … at the top` 은 한 번 올려놓는 느낌. 일상 대화라 `You do not need to` 보다 `No need to` 가 가볍다.

### 카드 20 — 검증 브리프 요청
- 내가 쓴 영어: "write a brief for the office agent to verify the fleet view"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Write a brief asking the office agent to verify the fleet view against real data.
- 왜: 오류는 없다. `for … to verify` 는 "검증하라고"와 "검증용"으로 둘 다 읽힐 수 있다. `asking … to` 로 쓰면 요청이라는 게 분명하다. `against real data` 를 붙이면 무엇과 대조하는지까지 담긴다.
