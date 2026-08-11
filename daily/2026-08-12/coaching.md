# 2026-08-12 — 코칭

오늘 배치에는 내가 쓴 한국어도, 어시스턴트의 한국어 문장도 없었다(대화가 전부 영어였다).
그래서 한글→영어 섹션은 비우고, 영어 다듬기만 싣는다.

## 영어 다듬기

### 카드 1 — 실행하고 결과를 훑어봤다고 보고하기
- 내가 쓴 영어: "I ran the filter_recording and skim through the images."   (출처: transcript:[user] auto-recipe-creator d5dd7c25)
- 정정: `skim` → `skimmed`. `ran` 과 `and` 로 묶인 등위 동사라 시제가 같아야 한다. 스크립트 이름 앞의 `the` 도 뺀다 — 파일·명령 이름은 고유명사처럼 무관사로 쓴다.
- 더 나은 표현: I ran `filter_recording` and skimmed the output frames.
- 왜: `skim through` 도 맞지만 목적어가 이미 "훑을 것"이면 `through` 없이 `skim the images` 가 더 간결하다. 무엇을 봤는지 `output frames` 로 좁혀 주면 상대가 어느 산출물인지 되묻지 않는다.

### 카드 2 — 실패 원인을 절로 이어 붙이기
- 내가 쓴 영어: "the mouse tracking failed a lot due to there is an icon looking like a hand palm (right next to live sem box)"   (출처: transcript:[user] auto-recipe-creator d5dd7c25)
- 정정: `due to there is …` 는 성립하지 않는다. `due to` 는 전치사구라 뒤에 **명사구**만 오고, 주어와 동사가 있는 절을 이으려면 `because` 를 쓴다. `a hand palm` 은 겹말이라 `a palm` 또는 `an open hand` 로 줄인다.
- 더 나은 표현: Cursor tracking failed often, because there's an open-hand icon sitting right next to the live SEM box.
- 왜: 원인을 명사구로 압축하려면 `due to an open-hand icon next to the live SEM box` 처럼 아예 절을 없애야 한다. 둘을 섞은 `due to + 절` 이 한국인 영작에서 가장 자주 나오는 형태이고, 원어민에게는 문장이 중간에 끊긴 느낌을 준다.

### 카드 3 — 무엇이 무엇과 헷갈리는지 방향 잡기
- 내가 쓴 영어: "vlm reads mouse cursor switching between the real one and this human-hand icon"   (출처: transcript:[user] auto-recipe-creator d5dd7c25)
- 정정: 관사를 넣어 `the VLM reads the mouse cursor` 로 해야 하고, `reads X switching` 은 "X 가 전환되는 것을 읽는다"로 읽혀 의도와 어긋난다. 헷갈리는 주체는 커서가 아니라 VLM 이다.
- 더 나은 표현: The VLM keeps flip-flopping between the real cursor and that hand icon.
- 왜: `keep + -ing` 이 "계속 반복해서"를 맡아 `a lot` 을 대신하고, `flip-flop between A and B` 는 두 답 사이를 오가며 확정 못 하는 상태를 그대로 그린다. 좀 더 격식 있게는 `alternates between` / `confuses the hand icon with the real cursor`.

### 카드 4 — 판정을 보수적으로 하라고 지시하기
- 내가 쓴 영어: "You have to be very conservative if you decide to pick mouse cursor inside the live SEM box as well."   (출처: transcript:[user] auto-recipe-creator d5dd7c25)
- 정정: `pick mouse cursor` → `pick the cursor`(가산명사에 관사). `as well` 이 문장 끝에 있으면 무엇에 "또한"인지 흐려진다.
- 더 나은 표현: Be equally conservative about accepting a cursor hit inside the live SEM box.
- 왜: 지시문에서는 `You have to be` 보다 명령형이 짧고 분명하다. `equally` 를 앞으로 당기면 "앞서 말한 그 경우만큼"이라는 비교 대상이 살아난다. 탐지 결과 하나를 가리킬 때는 `a cursor hit` / `a detection` 이 관용적이다.

### 카드 5 — 복수 주어에 동사 맞추기
- 내가 쓴 영어: "since the images in the sem box keeps changing and the mouse cursor is white colored while it is black outside of the sem box."   (출처: transcript:[user] auto-recipe-creator d5dd7c25)
- 정정: `the images … keeps` → `keep`(주어가 복수 `images`, `in the sem box` 는 수식어일 뿐이다). `white colored` 는 겹말이라 `white` 만으로 충분하다. `outside of` 는 `outside` 로 줄인다. `since` 로 시작한 조각은 앞 문장에 붙여야 문장이 된다.
- 더 나은 표현: — the SEM image repaints constantly, and the cursor turns white in there while it stays black everywhere else.
- 왜: 주어와 동사 사이에 전치사구가 끼면 바로 앞 명사(`box`)에 동사를 맞추는 실수가 잦다. `turns white` / `stays black` 처럼 변화 동사와 유지 동사를 맞세우면 대비가 선명해지고, `everywhere else` 가 `outside of the sem box` 의 반복을 없앤다.

### 카드 6 — 폴백이 제대로 걸려 있는지 확인 요청하기
- 내가 쓴 영어: "In recipe_search/providers/office.py _locate_idp raise LookupError. … we still fall back to check redis's to see idw, idp location right? have we set well?"   (출처: transcript:[user] skewnono-v3-nuxt 9d946c68)
- 정정: `raise` → `raises`(3인칭 단수). `redis's` 의 소유격은 근거가 없어 `Redis` 로 둔다. `have we set well?` 은 `set` 의 목적어가 없어 문장이 성립하지 않는다.
- 더 나은 표현: `_locate_idp` raises `LookupError` — no document in `meas_hist_cdsem`. When a recipe has never been measured, do we still fall back to Redis for the idw/idp location? Is that wired up correctly?
- 왜: `set` 은 홀로 "설정하다"를 못 맡는다. `set up` · `configure` · `wire up` 처럼 구동사를 완성해야 하고, 이 중 `wire up` 이 "배선이 이어져 있느냐"라는 뉘앙스라 폴백 경로를 물을 때 딱 맞는다. `For the case of no measurement` 는 `When a recipe has never been measured` 로 절을 살리는 편이 읽기 쉽다.

### 카드 7 — 설정 방법을 조언으로 구하기
- 내가 쓴 영어: "As we move to use only vml (mai-ui, small VLM) discarding ui-venus, how can we set the mai-ui.env ? … how can we set effectively using 2 GPUs"   (출처: transcript:[user] auto-recipe-creator abd41f20)
- 정정: `how can we set effectively using 2 GPUs` 는 `set` 의 목적어가 없고 `using` 이 어디에 걸리는지 모호하다. `discarding ui-venus` 분사구문은 주절 주어와 시점이 어긋나 `and dropping ui-venus` 로 푸는 편이 낫다.
- 더 나은 표현: Now that we're dropping ui-venus and keeping only mai-ui and PaddleOCR, how should `mai-ui.env` be configured? What's the most effective way to spread the two models across the two GPUs?
- 왜: 사실을 묻는 `how can we`(가능한가) 와 조언을 구하는 `how should we`(어떻게 하는 게 맞나) 는 다르다. 여기서는 후자다. `As we move to …` 는 `Now that …` 으로 바꾸면 이미 정해진 전환이라는 뜻이 분명해지고, 목적을 묻는 문장은 `What's the most effective way to …` 로 명사구를 세워 주면 목적어 없는 `set` 을 피할 수 있다.

### 카드 8 — 빌드 실패를 신고하고 원인 조사 부탁하기
- 내가 쓴 영어: "npm run build fail in .../fdc/Sequence here. can you find it why?"   (출처: transcript:[user] skewnono-v3-nuxt e4cdbee9)
- 정정: `fail` → `fails`(명령 이름이 단수 주어). `find it why` 의 `it` 은 자리가 없다 — `find out why` 가 맞는 구동사다.
- 더 나은 표현: `npm run build` fails somewhere under `.../fdc/`. Can you work out why?
- 왜: `find out` 은 사실을 알아내는 것, `work out` 은 따져서 답을 도출하는 것이라 원인 진단에는 `work out` 이 조금 더 어울린다. 실패 지점이 확실치 않으면 `in` 대신 `somewhere under` 를 써서 범위로 말해 두는 편이 나중에 정정할 일이 없다.

### 카드 9 — 이제 된다고 알리기
- 내가 쓴 영어: "oh now it builds done."   (출처: transcript:[user] skewnono-v3-nuxt e4cdbee9)
- 정정: `builds done` 은 성립하지 않는다. 여기서 `build` 는 자동사("빌드가 된다")라서 뒤에 `done` 같은 보어가 붙지 못한다.
- 더 나은 표현: Oh — it builds fine now. / That did it: the build is clean.
- 왜: "다 됐다"를 영어로 옮길 때 `done` 을 동사 뒤에 붙이고 싶어지지만, `done` 은 `I'm done` · `the build is done` 처럼 be동사와 짝지어야 한다. `That did it` 은 앞서 한 조치가 문제를 해결했음을 짚어 주는 회화 관용구라, 원인이 밝혀진 직후에 쓰기 좋다.

### 카드 10 — 다른 파일들과 같은 규약을 맞춰 달라고 하기
- 내가 쓴 영어: "can you make it work inside console like other files do in scripts folder?"   (출처: transcript:[user] skewnono-v3-nuxt e4cdbee9)
- 정정: `inside console` → `in the console`, `in scripts folder` → `in the `scripts` folder`. 둘 다 관사가 빠졌다.
- 더 나은 표현: Can you make `pack.py` runnable from the console the way the other scripts in `scripts/` are?
- 왜: `make it work` 는 "어떻게든 돌아가게" 쪽이고, 여기서 원한 건 실행 방식이므로 `runnable from the console` 이 정확하다. `like other files do` 대신 `the way the other scripts … are` 를 쓰면 비교 대상이 "그 폴더의 나머지 스크립트 전부"로 분명해진다 — 규약을 맞춰 달라는 요청에서 `the` 하나가 뜻을 바꾼다.

### 카드 11 — 사용자 선택을 기억해 달라고 요청하기
- 내가 쓴 영어: "SEM image support multiple images with the small buttons at the top … can you make it remembered the location once picked for the parameter? Since this suffix info varied based on the recipe and parameters,"   (출처: transcript:[user] skewnono-v3-nuxt d5b1f8a7)
- 정정: `support` → `supports`. `make it remembered` → `make it remember` — 사역동사 `make` 뒤에는 원형부정사가 온다(대상이 스스로 기억해야 하므로 수동도 아니다). `varied` → `varies`(지금도 그렇다는 현재 사실). 마지막 쉼표는 마침표로.
- 더 나은 표현: In `skewvoir/analysis`, the SEM image panel exposes several shots through those small suffix buttons at the top (U/T/M/L). Can we make it remember which one I picked, per parameter? The suffix set differs from recipe to recipe, so the pick shouldn't reset every time.
- 왜: `the location` 은 좌표처럼 읽혀 실제 요구(어느 접미사를 골랐는지)와 어긋난다. `which one I picked` 로 풀면 오해가 없다. 조건을 `per parameter` 로 뒤에 달면 요구사항이 한 줄에 정리되고, 마지막 문장을 `so …` 로 닫아 "왜 그래야 하는지"까지 넘겨 주면 상대가 설계 판단을 대신 해 줄 수 있다.

### 카드 12 — 엉뚱한 fab 으로 조회되는 것 같다고 묻기
- 내가 쓴 영어: "have we set corrently in recipe_search/provider/office? … the full_name is the recipe used in fab "R3" but try to find from the fab "M16"?"   (출처: transcript:[user] skewnono-v3-nuxt 2f1bb741)
- 정정: `corrently` → `correctly`(오타). `have we set correctly in X` 는 목적어가 없어 성립하지 않는다. `but try to find from …` 은 주어가 빠져 앞 절의 `the full_name` 이 찾는 주체처럼 읽힌다.
- 더 나은 표현: Is `recipe_search/providers/office.py` set up correctly? I'm getting `LookupError: no document in meas_hist_cdsem` — the `full_name` is a recipe that runs in fab R3, but we seem to be looking it up under M16. Just curious whether that's even possible with the current code.
- 왜: `we seem to be looking it up under M16` 처럼 `seem to` 를 넣으면 단정하지 않고 관찰만 보고하게 되어, 코드가 실제로 그런지 상대가 확인해 답하기 편하다. 마지막의 `Just curious whether …` 는 이미 쓴 그대로 훌륭하다 — 답을 재촉하지 않는 질문을 여는 표현이라 그대로 살렸다.

### 카드 13 — 로그에 찍힌 에러를 옮겨 적기
- 내가 쓴 영어: "in paddleocr and mai-ui.log api_server.py error unrecognized arguments: --swap-space."   (출처: transcript:[user] auto-recipe-creator abd41f20)
- 정정: 문장에 정동사가 없다. 로그를 인용할 때도 "무엇이 무엇을 보여 준다"는 주절이 필요하다.
- 더 나은 표현: Both `paddleocr.log` and `mai-ui.log` show `api_server.py: error: unrecognized arguments: --swap-space`.
- 왜: `show` · `report` · `say` 중 아무거나 주절 동사로 세우면 인용문과 서술이 분리돼 읽힌다. 로그 전문을 그대로 옮길 때는 백틱으로 감싸 어디까지가 인용인지 표시하는 게 관례다.

### 카드 14 — 드디어 뜬다고 알리기
- 내가 쓴 영어: "now it starts to run."   (출처: transcript:[user] auto-recipe-creator abd41f20)
- 정정: 문법 오류는 없다.
- 더 나은 표현: It's up and running now. / That did it — both servers came up.
- 왜: `start to run` 은 "이제 막 달리기 시작한다"는 시작 시점에 초점이 있어서, 여러 번 고친 끝에 정상 가동됐다는 뜻으로는 약하다. 서버·서비스가 떴다고 알릴 때의 관용 표현은 `be up` 이고, `up and running` 은 "떠 있고 실제로 동작한다"까지 담는 짝 표현이다.
