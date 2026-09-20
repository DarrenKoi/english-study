# 2026-09-21 — 코칭

> 오늘 `[user]` 한국어는 equipment-data-map 세션 2건과 auto-recipe-creator 세션 3건이다. auto-recipe-creator 의 첫 메시지가 길어 다섯 장으로 나눴고 (a) 카드는 모두 12장이다. (b) 는 같은 두 세션의 어시스턴트 한국어에서 4문장을 골랐다. 영어 다듬기는 skewnono 세션 4건의 `[user]` 영어에서 15장. `go ahead`, `push`, `commit and push`, `verify with agent-browser`, "A+B 적용해줘"는 고칠 데도 배울 데도 없어 뺐다. equipment-data-map 의 `<pasted_content>` 영어는 Codex 가 herdr 로 보낸 글이고 english-study 세션의 `[user]` 는 파이프라인 프롬프트라 둘 다 내 글로 보지 않았다.

## 한글→영어

### 카드 1 — 한 사이클 돌고 나면 그다음은?   (내가 쓴 한글)
- 내가 쓴 한글: "office llm으로 전체 사이클 한번 돌고나면 어떤 순서로 진행해야하나?"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Once we've run one full cycle with the office LLM, what should we do next, and in what order?
- 왜 이렇게: "~하고 나면"은 `once + 현재완료` 가 맞는다. 미래에 끝날 일이라도 시간 부사절 안에서는 `will have run` 이 아니라 `have run` 을 쓴다. "한번 돌다"는 `run one full cycle` 이나 `do one full pass`. "어떤 순서로"는 `in what order` 인데 구어에서는 `what order should we do things in` 처럼 전치사를 뒤에 남겨도 된다. "진행해야 하나"를 `proceed` 로 옮기면 딱딱하니 `what should we do next` 로 풀었다.

### 카드 2 — 부담이 되니 문제가 없다면 고쳐 줘   (내가 쓴 한글)
- 내가 쓴 한글: "응 진행해줘. 새 rollout마다 1-2단계를 계속하는건 부담이 되니 그것도 문제가 없다면 고쳐줘."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Yes, go ahead. Re-running stages 1–2 for every new rollout is a burden, so fix that too, as long as it doesn't break anything.
- 왜 이렇게: "~하는 건 부담이 된다"는 동명사를 주어로 세워 `Re-running … is a burden` 으로 쓴다. 비용 얘기라면 `gets expensive` 나 `adds up` 도 좋다. "문제가 없다면"을 `if there is no problem` 으로 직역하면 어떨까? 무슨 문제인지 흐릿하다. 걱정하는 내용이 부작용이니 `as long as it doesn't break anything` 이나 `if it's safe to` 로 구체화한다. "그것도"의 `too` 는 문장 끝에 둔다.

### 카드 3 — 버튼 하나 누르려고 몇 번이나 고쳐야 했다   (내가 쓴 한글)
- 내가 쓴 한글: "manual_click_button.py 을 테스트하면서 느낀 것은 File Manager 버튼을 한번 클릭하기 위해 여러번 테스트를 진행해서 최적점을 찾기 위해 여러번 프롬프트와 세팅 값들을 수정해야 했다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: What I noticed while testing `manual_click_button.py` is that just to click the File Manager button once, I had to run test after test, tweaking the prompt and the settings each time until I found the sweet spot.
- 왜 이렇게: "느낀 것은 ~다"는 `What I noticed … is that …` 으로 옮긴다. `feel` 은 감정 쪽이라 관찰한 사실에는 `notice` 나 `realize` 가 맞는다. 원문에서 걸리는 곳은 두 번 겹친 "~하기 위해". 영어에서 `to` 부정사 둘을 포개면 어느 쪽이 목적인지 헷갈리므로 목적은 `just to click … once` 하나만 남겼다. 나머지는 분사 `tweaking …` 과 `until I found` 로 풀었다. "여러 번" 되풀이한 느낌을 살리는 말은 `test after test`. "최적점"은 구어로 `the sweet spot` 이고 "세팅 값들"은 `settings` 만으로 충분하다.

### 카드 4 — 내가 설명하는 것보다 모델에게 시키는 게 낫나?   (내가 쓴 한글)
- 내가 쓴 한글: "내가 매번 화면의 구성 요소와 위치를 설명하는 것보다 Qwen3.8-27b로 화면 구성 요소와 위치를 확인 시켜주는 게 더 좋나? mai-ui와 OCR로도 그게 가능한건가?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Would it be better to have Qwen3.8-27b identify the screen elements and their positions, rather than me describing them every time? Can mai-ui plus OCR do that too?
- 왜 이렇게: "~에게 …시키다"는 사역 `have + 목적어 + 동사원형` 이다. "A 하는 것보다 B 가 낫나"는 `Would it be better to B rather than A` 틀에 넣는다. `rather than me describing` 에서 동명사의 의미상 주어는 구어에서 `me`, 격식에서 `my`. 화면의 "구성 요소"는 UI 에서 `elements` 가 표준이다. "그게 가능한 건가"는 `Is that possible with …` 보다 도구를 주어로 세운 `Can X do that` 이 영어답다.

### 카드 5 — 지금까지는 위치 찾는 데만 써 왔는데   (내가 쓴 한글)
- 내가 쓴 한글: "지금까지 mai-ui를 특정 component에 대한 위치를 찾는 것으로 활용해왔는데, 전체 UI/UX를 describe을 할 수 있는 기능이 있는 건지? 아니면 qwen3.8-27b나 회사에서 제공해주는 kimi-k2.7로 할 수 있는 건지 조사가 필요하다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: So far I've only used mai-ui to locate specific components. Can it also describe the whole UI? Or is that something Qwen3.8-27b, or the Kimi-K2.7 my company provides, could do? That needs looking into.
- 왜 이렇게: "지금까지 ~해 왔다"는 `So far I've (only) used` 로 현재완료다. "~하는 것으로 활용하다"는 `use X to V` 면 되고 `utilize` 는 필요 없다. "component에 대한 위치"의 "~에 대한"은 영어에서 사라진다(`locate specific components`). 한 문장에 물음 둘과 결론 하나가 들어 있어 영어는 넷으로 끊었다. "조사가 필요하다"는 `That needs looking into` 가 짧다. `need + -ing` 는 수동의 뜻. "회사에서 제공해주는"은 관계대명사를 뺀 `the Kimi-K2.7 my company provides` 다. 화면을 묘사하는 대상은 UI 이고 UX 는 경험이라 여기서는 뺐다.

### 카드 6 — 처음 화면 기억 → 바뀐 화면 나열 → 바로 클릭   (내가 쓴 한글)
- 내가 쓴 한글: "codex (with herdr skill)로 의논해서 어떻게 하면 최초의 화면 구성 요소를 기억하고 필요시에는 변경된 현재 화면의 구성 요소(열려 있는 윈도우들, 보이는 버튼들)들의 위치를 나열하고 원하는 버튼을 곧바로 찾아서 클릭할 수 있는가?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Talk it over with Codex (via the herdr skill): how can we remember the initial screen layout, list where things are on the current screen when it has changed (open windows, visible buttons), and then find and click the button we want right away?
- 왜 이렇게: 한국어는 지시와 질문이 한 문장에 녹아 있다. 영어는 명령문을 먼저 세우고 콜론 뒤에 질문을 붙이면 깔끔하다. 동사 셋(`remember`, `list`, `find and click`)을 같은 꼴로 나란히 두는 것이 뼈대. "구성 요소들의 위치를 나열"은 `list the positions of the elements` 보다 간접의문문 `list where things are` 가 가볍다. "필요시에는 변경된"은 `when it has changed` 로 옮겼다. "곧바로"는 `right away` 다.

### 카드 7 — 템플릿으로 만들어 버튼 이름만 넣고 싶다   (내가 쓴 한글)
- 내가 쓴 한글: "프롬프트를 일종에 템플릿화를 해서 원하는 버튼만 argument로 넣어 바로바로 찾아서 클릭하고 싶어."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I'd like to turn the prompt into a kind of template, so I can just pass the button name as an argument and have it found and clicked on the spot.
- 왜 이렇게: "템플릿화하다"는 `templatize` 라는 말이 있긴 하지만 `turn X into a template` 이 자연스럽다. "일종의"는 `a kind of` 다(원문 "일종에"는 "일종의"를 잘못 친 것). "argument로 넣다"는 `pass … as an argument` 가 굳은 짝이다. "바로바로"는 `on the spot` 이나 `every time, instantly` 로 옮긴다. `have it found and clicked` 는 `have + 목적어 + 과거분사` 로 "찾아서 눌러지게 한다"는 뜻이라 내가 직접 누르는 게 아님이 드러난다.

### 카드 8 — 할 수 있긴 함 / 해 볼 만하다   (내가 쓴 한글)
- 내가 쓴 한글: "qwen3.8-27b thinking mode를 none이나 low로 설정해서 진행할 수 있긴 함. 나중에 qwen으로 두 장 비교는 테스트 해볼만 하다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: We can actually run Qwen3.8-27b with thinking set to none or low. The two-image comparison with Qwen is worth testing later.
- 왜 이렇게: "할 수 있긴 함"의 "긴"은 상대 말을 바로잡는 어감이다. 어시스턴트가 "thinking 을 끌 수 없다"고 한 데 답한 말이라 `actually` 가 그 역할을 한다. "설정해서"는 어떻게 붙일까? `with + 목적어 + 과거분사`(`with thinking set to low`)를 쓰면 절을 하나 줄인다. "~해 볼 만하다"는 `be worth -ing` 다. `worth to test` 는 틀린 꼴이니 주의한다.

### 카드 9 — 같은 이름 버튼이 창마다 있을 수도 있잖아   (내가 쓴 한글)
- 내가 쓴 한글: "File Manager처럼 유니크한 이름의 버튼이 있을 수도 있고, OK 버튼처럼 여러곳에 존재하지만 각자 다른 window에 존재할 수 도 있잖아. 그거도 고려했나?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Some buttons have a unique name, like File Manager, but others, like OK, show up in several places, each in a different window. Did you take that into account?
- 왜 이렇게: "~도 있고 ~도 있다"는 `Some …, but others …` 가 기본 틀이다. "여러 곳에 존재하다"는 `exist` 보다 `show up in several places` 가 화면 얘기에 어울린다. "각자 다른 window에"는 `each in a different window` 로 뒤에 덧붙인다. "~잖아"는 어떻게 옮길까? 상대도 아는 사실을 환기하는 말인데 영어에는 딱 맞는 어미가 없어 평서문으로 말하고 바로 질문으로 넘어갔다. "고려했나"는 `take that into account` 나 `account for that` 이다.

### 카드 10 — 벤치는 건너뛰고 실제 클릭 타이밍을 같이 본다   (내가 쓴 한글)
- 내가 쓴 한글: "오피스 무클릭 벤치는 안해도 됨 (테스트할 때 클릭해도 무방한 버튼들 위주로 내가 선정해서 할 예정이기 때문에 실제 클릭이 제대로 되는 지 타이밍도 같이 봐야함. remote control로 인한 미세한 통신 delay)."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: We can skip the no-click bench at the office. I'll pick buttons that are safe to click and test with those, because we also need to see whether real clicks land properly and how the timing behaves, given the slight lag that remote control adds.
- 왜 이렇게: "안 해도 됨"은 `We can skip` 이 가장 짧다. "클릭해도 무방한"은 `safe to click` 이다. "제대로 되는지"는 `whether real clicks land properly`. 입력이 목표에 가 닿는다는 뜻으로는 `land` 나 `register` 를 쓴다. "~로 인한 미세한 통신 delay"를 `delay caused by` 로 직역하지 않고 원인을 관계절의 주어로 돌렸다(`the slight lag that remote control adds`). 원격 입력이 늦게 먹는 현상은 `delay` 보다 `lag` 나 `latency` 가 맞는 말이다.

### 카드 11 — 일단 1, 2 진행 + 버튼 위치 설명   (내가 쓴 한글)
- 내가 쓴 한글: "일단 1, 2 구현 진행. 테스트할 버튼 목록 -> AMP 버튼 (File Manager 버튼 아래에 있음), Rot.. 버튼 (rotation. PM 버튼 주변에 있음)."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: For now, go ahead and implement 1 and 2. Buttons to test: the AMP button (just below the File Manager button) and the Rot. button (rotation; near the PM button).
- 왜 이렇게: "일단"은 `For now` 나 `To start with` 다. "구현 진행"처럼 명사를 나열한 지시는 영어에서 동사로 세운다(`go ahead and implement`). 위치 전치사를 구별하자. `below` 는 떨어져 있어도 아래쪽이면 되고 `under` 는 바로 밑에 덮여 있다는 어감이다. 화면 배치에는 `below` 가 맞는다. "주변에"는 `near`, 붙어 있으면 `next to`. `around` 는 둘러싼다는 뜻이라 여기에는 안 맞는다.

### 카드 12 — 최신 코드는 저쪽, 여기 것은 이제 낡았다   (내가 쓴 한글)
- 내가 쓴 한글: "Qwen thinking low 가능 여부는 @../llm_serving/ 을 통해서 최신 코드베이스 확인 가능( auto_recipe_creator repo에서 vlm serving은 이제 outdated). 화면 두장 비교 가능한지 확인해줘."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: You can check whether Qwen supports low thinking in `../llm_serving/`, which has the current code (the VLM serving code in the auto_recipe_creator repo is out of date now). Also check whether it can compare two screenshots.
- 왜 이렇게: "가능 여부"는 `whether` 한 단어다. "~을 통해서 확인 가능"의 "통해서"를 `through` 로 옮기지 말자. 장소를 말하는 `in` 이면 된다. "최신 코드베이스"는 비제한 관계절 `, which has the current code` 로 덧붙였다. `outdated` 는 명사 앞에서 잘 쓰이고(`outdated docs`) 서술 자리에서 더 흔한 쪽은 `out of date`. "확인해줘"는 `check whether` 나 `find out if` 다.

### 카드 13 — 모델을 바꾼다고 튜닝이 없어지지는 않는다   (고급 한글 · 번역)
- 한글 원문: "모델을 바꾼다고 매번 하던 프롬프트 튜닝이 없어지지는 않습니다. 버튼 정보를 레지스트리로 모으고 프롬프트를 공통 템플릿 하나로 만드는 쪽이 가장 작은 해법입니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Swapping the model won't make the per-button prompt tuning go away. The smallest fix is to gather the button details into a registry and reduce the prompt to a single shared template.
- 번역 포인트: "~한다고 ~하지는 않는다"는 동명사 주어 + `won't make … go away` 가 가장 짧다. `Just because you swap the model doesn't mean …` 도 되지만 길다. "매번 하던"은 무엇마다 반복했는지를 밝혀 `per-button`. "~하는 쪽이 가장 작은 해법"은 `The smallest fix is to …` 로 보어 자리에 to부정사 둘을 나란히 둔다. "하나로 만들다"는 `reduce … to a single …` 이 "줄여서 하나로"라는 방향까지 담는다.

### 카드 14 — 같은 OCR 이 게이트와 정답을 겸하면   (고급 한글 · 번역)
- 한글 원문: "같은 OCR로 게이트와 정답을 둘 다 판단하면 잘못된 좌표를 승인해도 잡아내지 못합니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: If the same OCR serves as both the gate and the ground truth, a wrongly approved coordinate will go undetected.
- 번역 포인트: 평가 기준이 되는 "정답"은 `answer` 가 아니라 `ground truth` 다. "둘 다 판단하면"은 `serve as both A and B` 로 역할을 겸한다는 뜻을 살렸다. 한국어는 주어 없이 "잡아내지 못한다"로 끝나지만 영어는 주어가 필요해 좌표를 주어로 세우고 `go undetected` 를 썼다. `go + un-과거분사` 는 "~되지 않은 채 넘어가다"는 틀이다(`go unnoticed`, `go unanswered`).

### 카드 15 — 변수를 하나만 바꾸기 위해서   (고급 한글 · 번역)
- 한글 원문: "모델 비교를 마지막에 두는 이유는 변수를 하나만 바꾸기 위해서입니다. letter가 아직 바뀌는 중이면, 결과 차이가 모델 때문인지 letter 수정 때문인지 가를 수 없습니다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: The model comparison comes last so that only one variable changes at a time. While the letters are still in flux, there's no telling whether a difference in results comes from the model or from the letter edits.
- 번역 포인트: "~하는 이유는 ~위해서입니다"를 `The reason … is to …` 로 옮기면 무겁다. `comes last so that …` 으로 목적절을 바로 붙인다. "아직 바뀌는 중"에 딱 맞는 관용은 `still in flux`. "가를 수 없다"는 `there's no telling whether A or B` 로, `there's no -ing` 는 "~할 길이 없다"는 뜻이다. "~때문인지"는 `comes from` 을 두 번 받아 `from the model or from the letter edits` 로 짝을 맞췄다.

### 카드 16 — 모르고 고치면 조용히 깨지는가   (고급 한글 · 번역)
- 한글 원문: "요약에 남길지 말지는 "모르고 고치면 조용히 깨지는가"로 갈랐습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: One question decided what stayed in the summary: would it break silently if someone changed the code without knowing the rule?
- 번역 포인트: "~로 갈랐다"는 기준을 주어로 세워 `One question decided …` 로 뒤집었다. 콜론 뒤에 그 질문을 통째로 놓으면 따옴표가 필요 없다. "남길지 말지"는 `whether to keep it or not` 보다 간결한 쪽이 결과에서 본 `what stayed`. "모르고 고치면"은 가정이라 `would … if someone changed` 다. "조용히 깨진다"는 `break silently` 로, 오류 없이 틀린 동작을 하는 상황을 가리키는 개발 현장의 굳은 말이다.

## 영어 다듬기

### 카드 1 — 9/10 에 정식으로 공개했다
- 내가 쓴 영어: "for the notices pages, can you collect our update history? Only big changes needed. before 9/10, it was open beta and on 9/10 I officially released to my company via email."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `I officially released to my company` → `I officially released it to the company`. `release` 는 타동사라 목적어가 있어야 한다. `it was open beta` → `it was in open beta`. 단계는 `in` 으로 말한다.
- 더 나은 표현: For the notices page, can you put together our update history? Just the big changes. It was in open beta until 9/10, when I officially announced the release to the company by email.
- 왜: 날짜를 `before 9/10 … and on 9/10 …` 로 두 번 부르지 않고 `until 9/10, when …` 으로 한 번에 잇는다. 메일로 한 일은 출시가 아니라 출시 발표다. 어시스턴트가 표에 받아 적은 말도 `Official release announced by email`. `Only big changes needed` 는 생략체로 문제없다.

### 카드 2 — 8/10 부터 시작해도 괜찮다
- 내가 쓴 영어: "no issue starting from 8/10. and use Korean. continue. read from design"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Starting from 8/10 is fine. Write the notices in Korean. Go ahead, and build the page from the design file.
- 왜: 메모체로 뜻은 통한다. 다만 `no issue starting from 8/10` 은 "8/10 부터는 이슈가 없었다"로도 읽힌다. 승인하는 말로 가장 분명한 것은 `X is fine`. `read from design` 은 디자인 파일을 읽으라는 것인지 거기서 값을 가져오라는 것인지 애매해 `build the page from the design file` 로 목적을 밝혔다.

### 카드 3 — Codex 에게 코드 리뷰를 맡겨
- 내가 쓴 영어: "good. ask code review to codex (with herdr) for the notices page."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `ask code review to codex` → `ask Codex for a code review`. `ask` 는 `ask + 사람 + for + 원하는 것` 또는 `ask + 사람 + to + 동사` 로 쓴다. "~에게"를 `to` 로 옮긴 한국어식 어순이다.
- 더 나은 표현: Good. Have Codex review the notices page (via herdr).
- 왜: "시켜라"는 사역 `have + 사람 + 동사원형` 이 가장 짧다. 같은 버릇이 카드 14 의 `Reqeust the implentation jobs to codex` 에도 나온다. `ask`, `request`, `tell` 뒤에는 사람이 먼저 온다는 것을 오늘의 교정 포인트로 삼자.

### 카드 4 — pane 과 pain
- 내가 쓴 영어: "close the pain"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `pain` → `pane`. 둘은 발음이 같은 동음이의어다(/peɪn/). 바로 다음 메시지에서 스스로 `close the pane` 으로 고쳤다.
- 더 나은 표현: You can close the Codex pane now.
- 왜: `pane` 은 원래 창틀에 끼운 유리 한 장(`windowpane`)이고 거기서 분할된 화면 한 칸이라는 뜻이 나왔다. 어느 pane 인지 이름을 붙여 주면 여러 개가 열려 있어도 헷갈리지 않는다.

### 카드 5 — 컨텍스트 창은 256K, 서비스는 이미 운영 중
- 내가 쓴 영어: "it supports JSON Schema. the context windows is 256K tokens. The chat service is currently released and used by users actively."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `the context windows is` → `the context window is`. 창은 하나이므로 단수다. `used by users actively` → `actively used by users`. 양태 부사는 과거분사 앞이 자연스럽다.
- 더 나은 표현: It supports JSON Schema, and the context window is 256K tokens. The chat service is already live and in active use.
- 왜: `release` 는 한 시점의 동작이라 `currently` 와 어울리지 않는다. 지금 돌아가는 상태는 `live` 다. 어시스턴트가 답에서 받은 말도 `since the service is live`. `in active use` 는 "활발히 쓰이는 중"을 전치사구 하나로 말한다.

### 카드 6 — 뭘 설치해야 하나 / 필요하면 RAG 쪽이 채우면 된다
- 내가 쓴 영어: "To support datatable, should I install something? filling it from access control can be filled in from the rag agent if it needs filling."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 있는지 없는지 모르고 묻는 의문문에서는 `something` → `anything`. `datatable` → `data tables`(셀 수 있는 명사라 복수나 관사가 필요하다). 둘째 문장은 주어가 `filling it` 인데 동사가 다시 `can be filled in` 이라 "채우기가 채워진다"가 됐다. → `The RAG agent can fill it in from access control if it needs filling.`
- 더 나은 표현: Do I need to install anything to support data tables? As for the fab scope, the RAG agent can fill it in from access control if needed.
- 왜: 행위자(`the RAG agent`)를 주어로 세우면 문장이 바로 선다. `if it needs filling` 은 맞는 표현이고(`need + -ing`) `if needed` 가 더 짧다. `it` 이 무엇인지 앞 문맥에 없으니 `As for the fab scope` 로 화제를 먼저 세웠다.

### 카드 7 — 넓은 시야 없이는 판단하기 어려운 상황
- 내가 쓴 영어: "my final goal is to make a report for certain conditions that users cannot judgement without broader pespection so that I want to provide such as time-ranged information (tools' condition, abnormal situation/data and so on)."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `cannot judgement` → `cannot judge`. 조동사 뒤에는 동사원형이 오고 `judgement` 는 명사다. `pespection` → `perspective`. `so that I want to` → `so I want to`. `so that` 은 목적("~하도록")이고 결과("그래서")는 `so` 다. `provide such as X` → `provide information such as X`. `such as` 앞에는 명사가 있어야 한다.
- 더 나은 표현: My end goal is reports for situations users can't judge without a broader view, so I want to provide information over a time range: tool condition, abnormal events and data, and so on.
- 왜: `final goal` 보다 `end goal` 이나 `ultimate goal` 이 흔한 짝이다. `time-ranged` 는 사전에 없는 조어라 `over a time range` 로 푼다. 어시스턴트가 받은 문장은 `A report over a time range needs aggregate and trend data`. "넓은 시야"는 `a broader view` 나 `the bigger picture` 다.

### 카드 8 — 단건은 페이지에서, 채팅은 시간이 걸려도 종합 보고
- 내가 쓴 영어: "I believe for a single event and data, users can simpliy use the skewnono pages. so for the chat service, even if it takes a while, we can gather various information, analyze, report it to the user so that we can provide high-level complext information."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 철자 `simpliy` → `simply`, `complext` → `complex`. `analyze, report it` → `analyze it, and report it`. 타동사마다 목적어가 필요하고 마지막 항목 앞에 `and` 가 온다. `a single event and data` → `a single event or data point`. `data` 는 셀 수 없어 `a single` 과 맞지 않는다.
- 더 나은 표현: For a single event or data point, users can just use the skewnono pages. The chat service can take its time: gather information from several sources, analyze it, and report back, so that users get a high-level picture.
- 왜: `even if it takes a while` 은 잘 쓴 표현이다. 같은 뜻을 `take its time` 으로도 말한다. 여기 `so that` 은 목적이라 제대로 쓰였으니 카드 7 의 `so that I want` 와 견줘 보자. `high-level complex information` 은 형용사가 겹쳐 무거워서 `a high-level picture` 로 줄였다.

### 카드 9 — Playwright 대신 agent-browser 로
- 내가 쓴 영어: "instead of playwright, can you also do the test with agent-browser? if the agent-browser skill can replace the verification of the web, I do prefer agent-browser"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Can you run the same check with agent-browser as well? If it can replace Playwright for browser verification, I'd prefer to use it from now on.
- 왜: 문법 오류는 없다. 다만 `instead of` 와 `also` 가 부딪친다. "대신"인지 "추가로"인지 한쪽만 고르자. `I do prefer` 의 `do` 는 누가 의심할 때 "아니, 정말로"라고 힘주는 강조라 여기서는 과하다. 조건이 붙은 선호는 `I'd prefer` 가 맞는다. `the verification of the web` 은 `browser verification` 으로 줄인다.

### 카드 10 — 랜딩 페이지에 지금 띄우는 공지를 다 지워 줘
- 내가 쓴 영어: "remove all notifications currently we show up in the landing page."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `currently we show up` → `we currently show`. `show up` 은 "나타나다"는 자동사라 목적어를 못 받는다. 부사 `currently` 는 주어와 동사 사이에 둔다. `in the landing page` → `on the landing page`. 화면과 페이지 "위"는 `on` 이다.
- 더 나은 표현: Remove all the notices currently shown on the landing page.
- 왜: 관계절을 분사 `shown` 으로 줄이면 어순 고민이 사라진다. `notification` 은 주로 푸시 알림이고 페이지에 걸어 두는 글은 `notice` 나 `announcement` 다. 어시스턴트도 `both landing-page notices` 로 받았다.

### 카드 11 — 공지사항 페이지와 새 공지 표시
- 내가 쓴 영어: "and I am thinking about having a page "공지사항" so that users know what we have updated. Also a small component that display if there is a new 공지. As we have small code base changes (update) yesterday. 공지사항 should be in Korean mainly."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `a small component that display` → `displays`(3인칭 단수). `As we have … yesterday` 는 `yesterday` 와 현재형이 부딪치고 `As` 절만 있고 주절이 없는 문장 조각이다. → `We made some small changes yesterday, so …`. `in Korean mainly` → `mainly in Korean`.
- 더 나은 표현: I'm also thinking of adding a "공지사항" page so users can see what we've updated, plus a small indicator that shows when there's a new notice. We shipped a few small updates yesterday, so those can be the first entry. The page should be mainly in Korean.
- 왜: `display if` 는 "~이면 표시한다"인지 "~인지를 표시한다"인지 갈린다. `shows when there's a new notice` 가 분명하다. 이유를 말하는 절은 홀로 두지 말고 결론과 한 문장으로 묶는다.

### 카드 12 — 스큐보아가 잘 만들어졌으니 최대한 활용하자
- 내가 쓴 영어: "Now we have skewvoir built well and ready to utilize at maximum. I think we can make connection between pages."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `ready to utilize at maximum` → `ready to be used to the fullest`. skewvoir 는 쓰이는 쪽이라 수동이어야 하고 `at maximum` 은 수치의 상한에 쓰는 말이다. `make connection` → `make connections`. 셀 수 있는 명사다.
- 더 나은 표현: Skewvoir is in good shape now, so let's make the most of it. I think we can link the other pages to it.
- 왜: "최대한 활용하다"는 `make the most of` 가 굳은 표현이다. `have X built well` 은 문법상 가능하지만 상태를 말하려면 `X is in good shape` 가 자연스럽다. `make connections between pages` 보다 동사 `link` 하나가 가볍다.

### 카드 13 — 아이콘 하나, 표 하나
- 내가 쓴 영어: "So that we can see the recently measured history in 검색 결과 for that tool only. Likewise, we can do the same thing in Recipe 현황. With icon to 스큐보아 right next to 열어보기, 횡전개, 측정 이력 … In the table of displaying recipes for a lot cd in the popup, we can add a list of links"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `With icon` → `With an icon`. 셀 수 있는 단수 명사에는 관사가 필요하다. `the table of displaying recipes` → `the table that displays recipes`. `of + -ing` 는 "~하는"이라는 수식이 되지 않는다. `the recently measured history` → `the recent measurement history`. 측정된 것은 이력이 아니라 값이다.
- 더 나은 표현: That way we can see the recent measurement history for just that tool in 검색 결과. Likewise in Recipe 현황: add a 스큐보아 icon right next to 열어보기, 횡전개 and 측정 이력, carrying the selected fab and recipe name. In the lot 요약 popup, the table that lists recipes for a lot code can get the same set of links, each opening in a new tab.
- 왜: `So that …` 으로 문장을 시작하면 조각이 된다. 앞 문장과 끊으려면 `That way …` 로 시작한다. `for that tool only` 의 `only` 는 꾸미는 말 바로 앞에 두는 `for just that tool` 이 덜 헷갈린다.

### 카드 14 — Codex 를 불러 병렬로 맡겨라
- 내가 쓴 영어: "This is a sort of big code change, so you should get helped by codex (herder skill). Reqeust the implentation jobs to codex. You do review and simplify the code. Since we are working on several pages, you can either go or ask codex do the jobs in parellel. Go for it!!"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `get helped by` → `get help from`. `Reqeust the implentation jobs to codex` → `Ask Codex to do the implementation`. `request` 도 `request A to B` 꼴은 없고 `request something from someone` 이다. `ask codex do` → `ask Codex to do`. 철자는 `Reqeust` → `Request`, `implentation` → `implementation`, `parellel` → `parallel`, `herder` → `herdr`.
- 더 나은 표현: This is a fairly big change, so bring in Codex (herdr skill). Hand the implementation off to Codex; you review and simplify what comes back. Since several pages are involved, either do some yourself or have Codex work on them in parallel. Go for it!
- 왜: `a sort of big` 은 망설이는 구어라 글에서는 `a fairly big` 이 낫다. `You do review` 는 강조의 `do` 로 읽힌다. 역할을 나누는 말이라면 `you review` 만으로 되지 않을까? `you can either go` 는 `go` 뒤가 비어 무엇을 하라는지 알 수 없어 `do some yourself` 로 채웠다.

### 카드 15 — 두 mock 을 맞추되 서로 독립으로
- 내가 쓴 영어: "yes go ahead with aligning the two mocks. make them work separately."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Yes, go ahead and align the two mocks, but keep them independent of each other.
- 왜: 오류는 없다. 다만 `work separately` 가 애매해서 어시스턴트가 `I read it as keeping the two mocks independent rather than merging their generators. If you meant something else, say so` 라고 해석부터 밝혀야 했다. "맞추되 섞지는 마라"는 긴장을 `but` 으로 드러내고 `independent of each other` 로 못 박으면 되묻는 일이 없다.
