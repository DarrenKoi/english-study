# 2026-09-18 — 코칭

> 오늘 transcript 의 `[user]` 메시지는 전부 영어라 한글→영어 (a) 카드가 없다. `[assistant]` 도 영어로만 답해서 (b) 번역 정독 대상도 없다. 영어 다듬기는 두 저장소(auto-recipe-creator, equipment-data-map)의 `[user]` 문장에서 10장을 만들었다. `commit and push`, `yes. commit and push`, `commit and push all three repos` 는 고칠 데가 없어 뺐다.

## 영어 다듬기

### 카드 1 — 상황을 아는지 확인하는 질문
- 내가 쓴 영어: "you know that align fail happens, then popup window "Wait Input" is shown and OK button is located inside of the window?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `align fail happens, then popup window … is shown` → `when an align fail happens, a "Wait Input" popup is shown`. 두 절을 쉼표와 `then` 만으로 이으면 접속사가 없는 문장이 된다. 앞 절을 `when` 으로 묶는다. `popup window`, `OK button` 은 셀 수 있는 단수 명사라 관사가 필요하다(`a popup`, `the OK button`). `inside of the window` → `inside the window`. `of` 는 미국 구어에서 쓰이긴 해도 빼는 편이 깔끔하다.
- 더 나은 표현: You know how, when an align fail happens, a "Wait Input" popup comes up with the OK button inside it?
- 왜: 상대가 아는지 떠보며 화제를 꺼낼 때는 `You know that …?` 보다 `You know how …?` 가 입에 붙은 틀이다. `is shown` 보다 `comes up` / `pops up` 이 화면에 뜨는 동작을 자연스럽게 말한다. `with the OK button inside it` 으로 둘째 절을 전치사구로 접으면 문장이 하나로 닫힌다.

### 카드 2 — "Wait Input" 창만 확인하자
- 내가 쓴 영어: "Since OK buttons can be inside different popup windows, we have to make sure to observe "Wait Input" windows."   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Since OK buttons can show up in other popups too, we have to make sure we only click the one inside a "Wait Input" window.
- 왜: 문법은 맞다. 다만 `observe` 는 "관찰하다"라서 하려던 말("그 창일 때만 누른다")이 흐려진다. 실제로 어시스턴트는 뜻을 짐작해 "accept only a popup whose text reads Wait Input"으로 옮겼다. 제한은 `only` 로, 행동은 `click` 으로 직접 말하면 짐작할 여지가 없다. `different popup windows` 도 "서로 다른"보다 "다른 팝업에도"가 뜻이니 `other popups too` 가 맞는다.

### 카드 3 — 이슈 목록을 여는 첫 줄
- 내가 쓴 영어: "some of issues reported by office llms. letter 01. ftp_handler unimportable on Windwos without tzdata."   (출처: transcript:[user] equipment-data-map)
- 정정: `some of issues` → `some of the issues` 또는 `some issues`. `some of` 뒤에는 한정사(the, these, my)가 있어야 한다. `Windwos` → `Windows` (오타).
- 더 나은 표현: Here are some issues the office LLMs reported. Letter 01: ftp_handler can't be imported on Windows without tzdata.
- 왜: `Here are …` 로 시작하면 조각이 아니라 문장이 되고 "이제 목록이 나온다"는 신호가 된다. `unimportable` 은 뜻은 통하지만 사전에 없는 조어라 `can't be imported` 로 푸는 편이 안전하다. 메모체 항목이라도 `Letter 01:` 처럼 콜론을 쓰면 번호와 내용이 갈린다.

### 카드 4 — letter 02 메모
- 내가 쓴 영어: "letter 02. collection scope: under-pinned details, interpretation chosen. init in the collection's lifecycle. consuming stage binding change. for each strage, init should be configured properly."   (출처: transcript:[user] equipment-data-map)
- 정정: `strage` → `stage` (오타). `under-pinned` 는 주의가 필요하다. `underpin` 은 "떠받치다, 뒷받침하다"라서 `under-pinned details` 는 원어민에게 "근거가 부족한 세부"로 읽히기 쉽다. "덜 명시됐다"는 뜻이면 `underspecified` 가 정확하다.
- 더 나은 표현: Letter 02 (collection scope): several details were underspecified, so the office LLM had to pick an interpretation — where init sits in the collection's lifecycle, and how the consuming stage's binding changes. Init should be configured properly for each stage.
- 왜: 명사구만 나열하면 항목끼리의 관계를 읽는 사람이 맞춰야 한다. `so … had to pick an interpretation` 으로 원인과 결과를 잇고, 대시 뒤에 구체 항목 둘을 매달면 같은 정보가 한 문장에 선다. `for each stage` 는 문장 끝으로 보내야 영어 어순에 맞다.

### 카드 5 — 그룹핑을 가볍게
- 내가 쓴 영어: "I think grouping file based on family should be lighter. we can abort the file grouping except the files are made in the similar format so that we can think they are related in timely manner or they are related each other."   (출처: transcript:[user] equipment-data-map)
- 정정: `grouping file` → `grouping files` (복수). `except the files are made` → `unless the files are made`. `except` 는 전치사라 뒤에 절이 바로 올 수 없고, "~가 아닌 한"은 `unless` 다. `in the similar format` → `in a similar format` (`similar` 는 특정 하나를 가리키지 않으니 부정관사). `related each other` → `related to each other` (`related` 는 `to` 를 데리고 다닌다). `in timely manner` 는 관사가 빠졌고 뜻도 다르다. `in a timely manner` 는 "제때에"라서, 시간 순서로 이어진다는 뜻이면 `related in time` 이나 `form a time series` 다.
- 더 나은 표현: I think family-based grouping should be lighter. We can skip grouping altogether unless the files share a similar format, which suggests they're related — either as a sequence over time or to each other.
- 왜: `abort` 는 이미 돌고 있는 작업을 중간에 끊는다는 말이다. 처음부터 하지 않는다는 뜻은 `skip` 이 맞는다. `so that we can think` 는 목적("~하려고")으로 읽히는데 실제 뜻은 근거("그래서 ~라고 볼 수 있다")이므로 `which suggests` 로 바꿨다.

### 카드 6 — 샘플링 규칙
- 내가 쓴 영어: "based on the new rule from 06, we can sampling 3 files from latest and 2 files randomly so that we can have some broad perspective. if not, just pick randomly at 3 maximum."   (출처: transcript:[user] equipment-data-map)
- 정정: `we can sampling` → `we can sample`. 조동사 뒤는 동사원형이다. `3 files from latest` → `the 3 latest files`. 최상급 `latest` 에는 `the` 가 붙고 수사 뒤, 명사 앞에 온다. `at 3 maximum` → `up to 3` 또는 `3 at most`.
- 더 나은 표현: With the new rule from 06, we can sample the 3 latest files plus 2 random ones to get a broader view. Otherwise, just pick up to 3 at random.
- 왜: `have some broad perspective` 는 뜻은 통하지만 `get a broader view` 가 훨씬 흔한 연어다. `if not` 은 무엇이 아닌지 모호해서(규칙이 없으면? 패턴 파일군이 아니면?) `Otherwise` 로 받거나, 더 분명히 하려면 `For files that don't fit a pattern, …` 처럼 조건을 써 준다. 어시스턴트의 정리 문장 `the 3 latest eligible files plus 2 random picks from the rest` 도 통째로 외워 둘 만하다.

### 카드 7 — 왜 그 저장소가 엮였나
- 내가 쓴 영어: "why skewnono_v3_nuxt is involved in this repo?"   (출처: transcript:[user] equipment-data-map)
- 정정: `why skewnono_v3_nuxt is involved` → `why is skewnono_v3_nuxt involved`. 직접 의문문에서는 의문사 뒤에 be 동사가 주어 앞으로 나온다. `why + 주어 + 동사` 어순은 `I don't know why it is involved` 같은 간접 의문문에서만 쓴다.
- 더 나은 표현: Why did you touch skewnono_v3_nuxt? What does it have to do with this repo?
- 왜: `be involved in a repo` 는 어색한 조합이다. 궁금한 것은 "왜 거기를 건드렸나"와 "둘이 무슨 관계냐"이므로 `touch` 와 `have to do with` 로 나눠 묻는 쪽이 정확하다. `What does A have to do with B?` 는 관련성을 따질 때 쓰는 고정 틀이다.

### 카드 8 — 무엇을 지우라는 건지
- 내가 쓴 영어: "yes remove the unnecessary files"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Yes — remove the stray uv.lock and anything else your test runs left behind. Keep the commit.
- 왜: 문법 오류는 없다. 문제는 범위다. 그 시점에 걸려 있던 일은 `uv.lock` 삭제와 skewnono 커밋 되돌리기 두 가지였고, `the unnecessary files` 만으로는 어느 쪽까지인지 알 수 없었다. 그래서 어시스턴트가 `I read "unnecessary files" as …` 라고 해석을 밝히고 `If your "yes" also meant undoing that, say so` 라고 되물어야 했다. 선택지가 둘 이상인 질문에 `yes` 로 답할 때는 대상을 이름으로 적는다.

### 카드 9 — 장비 진입 단계를 건너뛰자
- 내가 쓴 영어: "we starting from entering the tool but I think it is redundant as I can already enter the tool by myself and run the code. So skip to search the tool in RCS list tab."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `we starting from` → `we're starting from` 또는 `the script starts by`. 진행형에는 be 동사가 있어야 한다. `skip to search the tool` → `skip searching for the tool`. `skip` 은 목적어로 동명사를 받는다. `skip to X` 는 "X 로 건너뛰어 가다"라서 정반대 뜻(검색 단계로 가라)이 된다. 실제로 첫 메시지에서 `skill` 로 잘못 쳤다가 고쳐 보냈는데, 고친 문장도 이 때문에 뜻이 흔들린다. `search the tool` 은 "도구 안을 뒤지다"이고, 도구를 찾는 것은 `search for the tool` 이다. `in RCS list tab` → `in the RCS List tab`.
- 더 나은 표현: The script starts by entering the tool, but that's redundant — I can open the tool myself before running it. So skip the step that searches for the tool in the RCS List tab.
- 왜: `by myself` 는 "혼자서, 도움 없이"이고 `myself` 만 쓰면 "내가 직접"이다. 여기서는 스크립트 대신 내가 한다는 뜻이므로 `myself` 가 맞는다. `skip the step that …` 으로 건너뛸 대상을 명사로 세우면 `skip to` 와 헷갈릴 일이 없다.

### 카드 10 — 콘솔에 뜨는 Pandas 줄
- 내가 쓴 영어: "when @poc/…/manual_align_correction.py runs, I found that in the beginning, [INFO] office integration, factory_loaded and then you see a bunch of Pandas(..) are they just for checking? they are not related to the recipe I am testing in manual."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 한 문장 안에 관찰과 질문이 이어 붙어 있다(`… a bunch of Pandas(..) are they just for checking?`). 마침표로 끊는다. `in the beginning` → `at the beginning` 또는 `at startup`. `in the beginning` 은 "태초에, 초창기에"처럼 긴 기간의 첫머리이고, 실행 시작 시점은 `at` 이다. `testing in manual` → `testing manually`. `in manual` 은 "설명서 안에서"로 읽힌다.
- 더 나은 표현: When manual_align_correction.py starts, I see "[INFO] office integration … factory_loaded" and then a bunch of Pandas(...) rows. Are those just some kind of check? They don't seem related to the recipe I'm testing manually.
- 왜: `I found that …` 은 조사 끝에 알아냈다는 말이고, 눈에 보인 것을 전할 때는 `I see` 가 맞다. 주어도 `I` 에서 `you` 로 바뀌었는데 하나로 통일한다. `They are not related` 는 단정인데 실제로는 확인을 구하는 중이므로 `don't seem related` 로 낮추면 질문과 어조가 맞는다.
