# 2026-09-15 — 코칭

> 오늘 `[user]` 메시지는 거의 다 영어라 한글→영어 (a) 는 한 장뿐이고, `[assistant]` 응답도 전부 영어라 (b) 번역 정독은 없다. `/private/tmp/equipment-map-claude-review-…` 세션의 긴 critique 요청문은 도구가 생성해 넘긴 글로 보고 다듬기 대상에서 뺐다.

## 한글→영어

### 카드 1 — 준비 대기 중 타임아웃   (내가 쓴 한글)
- 내가 쓴 한글: "qwen3.8-27b 준비 대기중 but it takes longer than 900s and stop running the instance."   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: While waiting for qwen3.8-27b to become ready, the launcher hits the 900s limit and stops the instance.
- 왜 이렇게: "준비 대기중"은 명사구라 영어에서는 절로 풀어야 한다. `while waiting for X to become ready` 가 그 자리다. 원문의 `it` 은 무엇을 가리키는지 없어서 `the launcher` 를 주어로 세웠다. 뒤의 `stop running the instance` 는 주어가 사라져 명령문처럼 읽히므로 `stops the instance` 로 붙였다. "~중"을 `-ing` 로 옮기려다 한글·영어를 섞으면 주어와 시제가 동시에 끊긴다.

## 영어 다듬기

### 카드 1 — 타임아웃 연장 요청
- 내가 쓴 영어: "qwen3.8-27b 준비 대기중 but it takes longer than 900s and stop running the instance. can we make it longer than 900s?"   (출처: transcript:[user] llm-serving)
- 정정: `and stop running` → `and (it) stops running` 또는 `and the instance gets stopped`. 3인칭 단수 `it` 에 맞춰 `-s` 가 필요하고, 실제로는 런처가 인스턴스를 멈추는 것이라 주어가 바뀐다.
- 더 나은 표현: Waiting for qwen3.8-27b takes longer than 900s, so the launcher kills the instance. Can we raise the limit above 900s?
- 왜: "make it longer than 900s" 에서 `it` 이 대기 시간인지 제한값인지 모호하다. `raise the limit` 이면 바꿔 달라는 대상이 설정값임이 분명하다. 원인과 결과는 `but` 보다 `so` 로 잇는 편이 맞다.

### 카드 2 — 모델별 작업 분리 요청
- 내가 쓴 영어: "Can we add a layer to insert what model we are using? I run the letters in parallel with different llm models in my office, and the info they filled in interfere each other. think about to seperate the jobs based on the model. working in the different folders."   (출처: transcript:[user] equipment-data-map)
- 정정: `interfere each other` → `interfere with each other` (`interfere` 는 자동사라 `with` 가 필요). `the info … interfere` → `interferes` (`info` 는 단수). `think about to seperate` → `think about separating` (`about` 뒤엔 동명사, 철자는 `separate`). `working in the different folders.` 는 주어·동사 없는 조각이라 앞 문장에 붙여야 한다.
- 더 나은 표현: Can we add a way to record which model each run uses? In the office I run the letters in parallel with different LLMs, and what they write interferes with each other. Consider splitting the jobs by model, each in its own folder.
- 왜: "insert what model we are using" 은 "어디에 넣는지"가 빠져 있다. `record which model each run uses` 로 하면 목적이 드러난다. `based on the model` 도 틀리진 않지만 `by model` 이 짧고 관용적이다. `each in its own folder` 는 조각 문장을 부사구로 흡수하는 정형이다.

### 카드 3 — 허브와 복사본 레이아웃 설명
- 내가 쓴 영어: "i will copy the folder into different name so that we can work seperately. thid repo will be used only for the remote git connection. other folders with model names are only local"   (출처: transcript:[user] equipment-data-map)
- 정정: `copy the folder into different name` → `copy the folder under a different name` (복사 결과에 붙는 이름은 `under`; 관사 `a` 필요). `seperately` → `separately`. `thid` → `this`.
- 더 나은 표현: I'll copy the folder under a different name so we can work separately. This repo is only for the remote git connection; the model-named folders stay local.
- 왜: "are only local" 은 문법상 맞지만 `stay local` 이 "원격에 올리지 않는다"는 의도를 더 잘 살린다. `will be used only for` 는 `is only for` 로 줄여도 뜻이 같다. `other folders with model names` 는 `the model-named folders` 처럼 복합 형용사로 압축하면 문장이 가볍다.

### 카드 4 — office 브랜치 생성 중단 요청
- 내가 쓴 영어: "in my office local, it continues to make office branch. we have to use only origin/main branch."   (출처: transcript:[user] equipment-data-map)
- 정정: `make office branch` → `create an office branch` (가산명사 단수엔 관사). `use only origin/main branch` → `use only the origin/main branch`. `in my office local` 은 `local` 이 명사로 쓰이지 않으므로 `on my office machine` 또는 `in my local office clone`.
- 더 나은 표현: On the office machine it keeps creating an office branch. We should stay on main only.
- 왜: "continues to make" 보다 `keeps creating` 이 "자꾸 그런다"는 짜증 섞인 어감을 정확히 낸다. "use only origin/main branch" 는 실제 의도가 "브랜치를 따지 말고 main 에 머물자"이므로 `stay on main` 이 더 직접적이다.

### 카드 5 — 아키텍처 문서 작성 요청
- 내가 쓴 영어: "describe how @equipment-data-parser/ behave with llm with md files and html. write down in @docs/architecture/"   (출처: transcript:[user] equipment-data-map)
- 정정: `behave` → `behaves` (폴더 하나가 주어라 3인칭 단수). `write down in` → `write it up in` 또는 `put it under` (`write down` 은 목적어가 필요하고, 문서를 "작성해 두다"는 `write up`).
- 더 나은 표현: Describe how equipment-data-parser drives the LLM with its Markdown files and HTML, and write it up under docs/architecture/.
- 왜: `with llm with md files` 처럼 `with` 가 두 번 이어지면 무엇이 무엇의 수단인지 흐려진다. 어시스턴트도 이 부분을 가정으로 표시하고 확인을 요청했다. `drives the LLM with …` 로 동사를 바꾸면 "Markdown 이 LLM 을 움직인다"는 관계가 드러난다.

### 카드 6 — 단일 LLM 규칙으로 변경
- 내가 쓴 영어: "we change the rule. one llm takes all. not the step for multi llms are used. we have to finish the whole process first with a single llm."   (출처: transcript:[user] equipment-data-map)
- 정정: `we change the rule` → `we're changing the rule` 또는 `let's change the rule` (지금 결정을 알리는 말은 진행형·청유형). `not the step for multi llms are used` 는 주어·동사 구조가 무너졌다 → `no multi-LLM step for now`.
- 더 나은 표현: Let's change the rule: one LLM does everything. No multi-LLM stage for now. We need to finish the whole process with a single LLM first.
- 왜: `one llm takes all` 은 `winner takes all` 을 빌린 재치 있는 표현이지만 어시스턴트가 "두 역할 모두인가"를 되물을 만큼 범위가 불분명했다. `does everything` 이나 `handles both roles` 로 쓰면 그 질문이 생기지 않는다. 짧은 문장 셋을 콜론과 마침표로 정리하면 결정문답게 읽힌다.

### 카드 7 — npm deprecated 경고 질문
- 내가 쓴 영어: "As we moved to the new folder to frontend, I install npm packages with npm install. and I see many deprecated like lodash.isequal, rimraf, fstream, uuid. is it find to leave it as it is?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `I install` → `I installed` 또는 `I ran npm install` (이미 한 일은 과거). `many deprecated like …` → `many deprecation warnings like …` (`deprecated` 는 형용사라 명사가 필요). `is it find` → `is it fine`. `leave it` → `leave them` (경고 여럿).
- 더 나은 표현: Since we moved the frontend into a new folder, I ran npm install and got a lot of deprecation warnings (lodash.isequal, rimraf, fstream, uuid). Is it fine to leave them as they are?
- 왜: "moved to the new folder to frontend" 는 `to` 가 둘이라 무엇을 어디로 옮겼는지 뒤집혀 읽힌다. `moved the frontend into a new folder` 로 목적어와 방향을 분리한다. `As` 는 "~하면서"라 시간이 겹치는 느낌인데, 여기서는 이유이므로 `Since` 가 맞다.

### 카드 8 — Ghostty 테마 설정
- 내가 쓴 영어: "configure ghostty theme to Adventure. reference https://ghostty.org/docs/config"   (출처: transcript:[user] ~)
- 더 나은 표현: Set the Ghostty theme to Adventure. Reference: https://ghostty.org/docs/config
- 왜: 문법 오류는 없다. 다만 `configure X to Y` 는 드물고, 값 하나를 지정할 땐 `set X to Y` 가 관용이다. `configure` 는 여러 옵션을 한꺼번에 손볼 때 어울린다. 링크 앞의 `reference` 는 동사로 읽히면 "참조해라"라는 명령이 되므로, 콜론을 붙여 명사 라벨로 만들면 뜻이 또렷하다.
