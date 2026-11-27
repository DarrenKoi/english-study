# 2026-11-28 — 코칭

## 한글→영어

### 카드 1 — 조사 범위 열기   (내가 쓴 한글)
- 내가 쓴 한글: "computer-use를 자동화에 어떻게 최적화하고 적용하고 있는 지 최신 사례들이 있는 지 조사해보자."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Let's look into recent cases of how teams are applying computer-use to automation and optimizing it.
- 왜 이렇게: "~있는 지 조사해보자"를 `look into whether there are…` 로 옮기면 문장이 두 겹으로 늘어집니다. 영어는 "사례를 조사하자"로 바로 가요. `Let's look into` 는 동료에게 같이 알아보자고 할 때 가장 무난하고, 보고서 서두라면 `This report surveys recent cases of…` 로 바꿉니다. 주어 없는 한국어 "최적화하고 적용하고"는 `teams are` 를 넣어 누가 하는지 채웁니다.

### 카드 2 — 판단 분기점   (내가 쓴 한글)
- 내가 쓴 한글: "실제로 판단이 필요한 분기점에서 어떻게 적용되고 있는 지."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: In particular, how is it used at branch points that actually require a judgment call?
- 왜 이렇게: 한국어는 앞 문장에 기대어 "~지." 로 끝냈지만 영어는 의문문을 온전히 세워야 합니다. "판단이 필요한"은 `require a judgment call` 이 딱 맞아요. 사람이 재량으로 정하는 결정이라는 뉘앙스입니다. `In particular` 로 앞 질문의 하위 질문임을 표시합니다.

### 카드 3 — 시행착오 자동화   (내가 쓴 한글)
- 내가 쓴 한글: "실제 작업자는 try and error를 여러번 실행해서 최적점을 찾는 과정이 중간 중간에 있는데 이걸 computer use와 llm모델의 조합으로 automation이 되는 지 조사도 필요해."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Operators often go through rounds of trial and error mid-task to find the optimal setting. I also need to know whether that part can be automated by combining computer use with an LLM.
- 왜 이렇게: 한 문장에 상황과 요청이 같이 있어서 영어로는 둘로 끊는 편이 읽기 쉽습니다. "중간 중간에"는 `mid-task` 나 `at several points along the way`. "여러번 실행해서"는 `rounds of` 로 반복을 담습니다. "automation이 되는 지"는 `whether it can be automated` 처럼 수동태가 자연스러워요. 그리고 `try and error` 는 `trial and error` 가 맞습니다(영어 다듬기 카드 1).

### 카드 4 — 두 회사의 방향   (내가 쓴 한글)
- 내가 쓴 한글: "claude, openAI는 computer-use를 어떻게 발전시키고 있는 지도 조사해줘."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Also look at how Anthropic and OpenAI have been evolving their computer-use offerings.
- 왜 이렇게: 진행 중인 변화는 현재완료진행 `have been evolving` 이 잘 받습니다. `develop` 도 되지만 이미 있는 기능을 다듬어 가는 흐름이라 `evolve` 가 더 정확해요. 회사를 말할 때는 제품명 Claude 보다 회사명 Anthropic 을 짝으로 두는 게 자연스럽습니다.

### 카드 5 — 함께 조사하기   (내가 쓴 한글)
- 내가 쓴 한글: "codex와 힘을 합쳐 함께 조사해서 보고서를 작성해줘 (via herdr)"   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Team up with Codex through herdr, split the research, and write up a report.
- 왜 이렇게: "힘을 합쳐"는 `join forces with` 도 되지만 일상 업무에선 `team up with` 가 가볍습니다. "함께 조사해서"를 `split the research` 로 옮기면 각자 맡는다는 뜻까지 전달돼요. "보고서를 작성"은 `write up a report` — `write up` 은 조사 결과를 정리해 문서로 만든다는 구동사입니다.

### 카드 6 — 빠진 것 확인   (내가 쓴 한글)
- 내가 쓴 한글: "github에 있는 유명한 computer-use repo나 vercel에서 만든 agent-desktop, agent-browser와 같은 기능들도 조사했어?"   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Did you also cover the popular computer-use repos on GitHub, and tools like Vercel's agent-desktop and agent-browser?
- 왜 이렇게: "조사했어?"는 범위 점검이라 `research` 보다 `cover` 가 맞습니다(보고서에 들어갔느냐는 뜻). "vercel에서 만든"은 소유격 `Vercel's` 하나로 줄어요. "기능들"은 여기서 독립된 도구라 `features` 보다 `tools` 입니다.

### 카드 7 — 사내 조건 추가   (내가 쓴 한글)
- 내가 쓴 한글: "회사 안에서 사용하는 computer use 기능이고 llm을 사용할 때 vllm library 기반이어야 하고 소형 vlm 모델이나 vla를 써야 하는 것 고려해줘."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Keep in mind this is for in-house use: any LLM has to be served with vLLM, and we need to stick to small VLMs or VLAs.
- 왜 이렇게: "고려해줘"는 문장 끝보다 앞에 `Keep in mind` 로 꺼내면 듣는 쪽이 조건을 기다리며 읽습니다. 콜론 뒤에 조건을 나열하세요. "회사 안에서 사용하는"은 `in-house`, "~를 써야 한다"는 선택지를 좁힌다는 뜻이라 `stick to` 가 맞습니다. "소형 vlm 모델"의 `model` 은 VLM 에 이미 들어 있어 뺍니다.

### 카드 8 — latency 조건   (내가 쓴 한글)
- 내가 쓴 한글: "작업이 복잡하고 장시간 이어지는 경우도 많기 때문에 latency가 빠른 모델이어야 함."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Many of the tasks are complex and run for a long time, so the model needs low latency.
- 왜 이렇게: latency 는 "지연"이라 `fast latency` 가 아니라 `low latency` 입니다. "빠른 모델"을 살리고 싶으면 `a fast model` 이나 `a model with low latency`. "~때문에 ~이어야 함"은 영어에서 `so` 로 앞뒤를 이어 원인부터 말하는 편이 회화에서 자연스럽습니다.

### 카드 9 — 흐름도 요청   (내가 쓴 한글)
- 내가 쓴 한글: "computer use과 llm 조합으로 작업 자동화를 할 때 어떤식으로 llm이 개입하고 진행하는 지 workflow (flow chart)도 함께 artifact로 보고 싶어."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: I'd also like an artifact with a flowchart showing where the LLM steps in and how the work proceeds when we automate tasks with computer use plus an LLM.
- 왜 이렇게: "개입하다"는 `intervene` 이 사전 뜻이지만 문제가 생겨 끼어든다는 느낌이 강합니다. 정해진 지점에서 역할을 맡는다는 뜻이면 `step in` 이 더 맞아요. "보고 싶어"는 요청이라 `I'd like` 가 공손하고 자연스럽습니다.

### 카드 10 — 한계를 분명히   (내가 쓴 한글)
- 내가 쓴 한글: "현재 기술 조건으로 computer-use의 제약 사항과 한계도 무엇인지 명확히 알아보고 싶어."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: I also want a clear picture of what computer use can't do yet — its current constraints and limitations.
- 왜 이렇게: "명확히 알아보고 싶어"는 `get a clear picture of` 가 딱입니다. "현재 기술 조건으로"는 `yet` 이나 `with today's technology` 로 짧게 처리해요. 대시 뒤에 "제약 사항과 한계"를 다시 붙이면 무엇을 원하는지 한 번 더 또렷해집니다.

### 카드 11 — 마무리 지시   (내가 쓴 한글)
- 내가 쓴 한글: "조사 마치고 전체적으로 한글 표현이 매끄럽게 작성되었는 지 점검 /humanize-korean:humanize . 점검 한다음에 artifact에 올리고 보고자료도 docs 폴더에 남겨줘."   (출처: transcript:[user] arc-engine 466d352b)
- 자연스러운 영어: Once the research is done, run /humanize-korean:humanize to check that the Korean reads smoothly throughout. After that, publish it as an artifact and save a copy of the report in the docs folder.
- 왜 이렇게: "매끄럽게 작성되었는지"는 `reads smoothly` 로 옮깁니다. 글이 주어일 때 `read` 는 "읽히다"라는 자동사예요. 순서는 `Once…` / `After that,` 로 표시하고, "남겨줘"는 원본은 따로 있고 사본을 둔다는 뜻이라 `save a copy` 가 정확합니다.

### 카드 12 — 범위 빠짐 인정   (고급 한글 · 번역)
- 한글 원문: "아니요, 빠져 있었습니다. 오픈소스 쪽은 Stagehand 캐싱 한 줄만 들어갔고, GitHub 프로젝트와 Vercel의 agent-browser 같은 도구는 다루지 않았습니다."   (출처: transcript:[assistant] arc-engine 466d352b)
- 자연스러운 영어: No, that was missing. On the open-source side, all we had was a single line on Stagehand caching; GitHub projects and tools like Vercel's agent-browser weren't covered.
- 번역 포인트: "빠져 있었습니다"를 `I missed it` 으로 옮기면 사과가 앞서고, `that was missing` 은 사실을 먼저 인정합니다. "~쪽은"은 `On the … side`. "한 줄만 들어갔고"는 `all we had was a single line` 처럼 `all … was` 로 "그게 전부"를 강조합니다.

### 카드 13 — 윤문 결과 요약   (고급 한글 · 번역)
- 한글 원문: "문장 단위 번역투는 원래 거의 없었습니다. 주로 문서 수준의 반복을 걷어냈습니다."   (출처: transcript:[assistant] arc-engine 466d352b)
- 자연스러운 영어: There was very little translationese at the sentence level to begin with; most of the work was stripping out repetition at the document level.
- 번역 포인트: "원래"는 `originally` 보다 `to begin with` 가 "애초에 별로 없었다"는 뉘앙스를 잘 살립니다. "걷어냈다"는 `strip out` 이 쌓인 것을 벗겨 낸다는 그림과 맞아요. 두 문장을 세미콜론으로 붙이면 "그래서 실제로 한 일은"이라는 연결이 생깁니다.

### 카드 14 — 커밋 전 확인 부탁   (고급 한글 · 번역)
- 한글 원문: "작업 트리에는 이번 작업과 관계없는 core/ 수정도 있는데, 다른 세션에서 한 것으로 보여 건드리지 않았습니다."   (출처: transcript:[assistant] arc-engine 466d352b)
- 자연스러운 영어: The working tree also has changes in `core/` that are unrelated to this task; they look like they came from another session, so I left them alone.
- 번역 포인트: "~것으로 보여"는 추정이라 `they look like they came from` 처럼 단정을 피합니다. "건드리지 않았다"는 `didn't touch` 도 되지만 `left them alone` 이 "일부러 그대로 뒀다"는 의도까지 담아요. 오늘 표현 `which belong to other work` 와 같은 상황입니다.

## 영어 다듬기

### 카드 1 — try and error
- 내가 쓴 영어: "try and error"   (출처: transcript:[user] arc-engine 466d352b)
- 정정: **trial and error** — 영어 관용구는 명사 `trial`(시도) + `error`(실수)입니다. `try and error` 는 한국·일본식 표현이라 원어민에게는 어색하게 들려요.
- 더 나은 표현: Operators find the optimal setting **through trial and error**. / It's a **trial-and-error** process. (명사 앞에서는 하이픈)
- 왜: 같은 관용구가 동사로는 `iterate`, 문어에서는 `empirical tuning` 으로도 쓰입니다. 보고서 제목이라면 "Automating Trial-and-Error Tuning" 처럼 하이픈 형용사로 씁니다.

### 카드 2 — workflow (flow chart)
- 내가 쓴 영어: "workflow (flow chart)"   (출처: transcript:[user] arc-engine 466d352b)
- 더 나은 표현: a workflow **diagram** (a **flowchart**)
- 왜: 틀린 표현은 아닙니다. 다만 요즘은 `flowchart` 를 한 단어로 붙여 쓰는 쪽이 훨씬 흔해요. 그리고 `workflow` 자체는 절차를 가리키고 그림이 아닙니다. 그림을 원하면 `workflow diagram` 이나 `flowchart` 로 대상을 분명히 해 주세요. 괄호로 같은 말을 반복할 필요도 줄어듭니다.
