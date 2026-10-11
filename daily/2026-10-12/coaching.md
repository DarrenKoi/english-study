# 2026-10-12 — 코칭

> 내가 쓴 글은 세션 다섯에서 나왔다. auto-recipe-creator 의 workflow 그래프 저장 방식 변경과 코드 리뷰, skewnono 의 문서 정리·Provision 연결 검토·히트맵 라벨 버그, pm-notes 의 SLM 튜닝 질문이다. 한국어는 여섯 건인데 한 메시지에 문장이 여럿이라 나눠서 카드 열넷이 됐다. 영어는 일곱 건. `commit and push` 는 어제 다뤄서 뺐고 `/clear`·`/model`·`/code-review high` 같은 명령, task-notification, 스킬 문서, 이 저장소의 배치 프롬프트도 다루지 않았다. 번역 정독은 어시스턴트 답변에서 네 문장을 골랐다.

## 한글→영어

### 카드 1 — 거의 보지 않고 있어   (내가 쓴 한글)
- 내가 쓴 한글: "지금 poc/workflow_3를 가동할 때 저장되는 log 중에 workflow html 차트가 있는데, 거의 보지 않고 있어."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: One of the logs poc/workflow_3 saves on each run is a workflow HTML chart, and I hardly ever look at it.
- 왜 이렇게: "~ 중에 ~가 있는데"는 `Among the logs, there is …` 로 시작하면 번역투가 난다. `One of the logs … is …` 로 주어를 세우면 곧다. "가동할 때 저장되는"은 수동 `that are saved when it runs` 도 되지만 프로그램을 주어로 한 능동 `the logs workflow_3 saves on each run` 이 짧다. "거의 안 본다"는 `hardly ever` 또는 `rarely`. `I almost don't look at it` 은 틀리지는 않아도 원어민은 잘 안 쓴다.

### 카드 2 — 나중에 바꿀 수 있는 형태로 저장하자   (내가 쓴 한글)
- 내가 쓴 한글: "일단은 나중에 html로 변경할 수 있는 형태로 저장하자."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: For now, let's save it in a format we can convert to HTML later.
- 왜 이렇게: "일단은"은 `for now`. `first of all` 은 순서를 말하는 것이어서 뜻이 다르다. "변경하다"를 `change to html` 로 옮기면 파일을 고친다는 말로도 들린다. 형식을 바꾸는 일은 `convert to` 또는 `render as`. "~할 수 있는 형태로"는 `in a format (that) we can …` 관계절로 받는다. 격식을 올리면 `Let's store it in an intermediate format that can be rendered to HTML on demand.`

### 카드 3 — 문제 없는지 확인해줘   (내가 쓴 한글)
- 내가 쓴 한글: "문제 없는 지 확인해줘"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Check that nothing's broken.
- 왜 이렇게: 방금 한 변경이 다른 것을 망가뜨리지 않았는지 묻는 맥락이라 `nothing's broken` 이 딱 맞다. 더 넓게 보라는 뜻이면 `Make sure there are no issues with the change.` `check if there is no problem` 은 부정이 어색하게 겹친다. 긍정으로 뒤집어 `Check that everything still works.` 라고 해도 같은 말이다. 리뷰를 시키는 것이면 `Give it a review.`

### 카드 4 — 전부 고쳐야 해   (내가 쓴 한글)
- 내가 쓴 한글: "전부 고쳐야해"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: All of them need to be fixed.
- 왜 이렇게: 상대에게 시키는 말이면 `Fix all of them.` 이 가장 짧다. "~해야 해"를 `must` 로 옮기면 규정처럼 딱딱해지고 `need to` 나 `have to` 가 일상 말투다. 하나도 빼지 말라는 뜻을 세우려면 `Every one of them needs fixing.` `need fixing` 은 `need to be fixed` 와 같은 뜻의 구어형이다.

### 카드 5 — 곧 production 으로 배포할 텐데   (내가 쓴 한글)
- 내가 쓴 한글: "이제 곧 production mode로 배포할텐데 문제가 없어야 함."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: We're about to deploy this to production, so it can't have any problems.
- 왜 이렇게: "이제 곧 ~할 텐데"는 `be about to` 가 맞다. 임박했다는 느낌이 `will soon` 보다 강하다. `production mode` 는 설정 스위치를 가리킬 때 쓰는 말이고 배포 대상은 `to production` 이라고 한다. "문제가 없어야 함"은 `it must have no problem` 보다 `it can't have any problems` 나 `it has to be solid` 가 자연스럽다. 앞 카드와 묶으면 `Fix all of them. We're about to go to production, and it has to be clean.`

### 카드 6 — Provision 장비를 연결하는 작업을 하려고 하는데   (내가 쓴 한글)
- 내가 쓴 한글: "이제 Provision 장비를 연결하는 작업을 하려고 하는데"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I'm about to start hooking up the Provision tools.
- 왜 이렇게: "~하는 작업을 하려고 한다"를 `I'm going to do the work of connecting` 으로 옮기면 "작업"이 군더더기다. 동사 하나로 줄인다. 시스템에 새 장비를 붙이는 일은 `hook up`(구어), `integrate`(중립), `onboard`(조직·제품 용어)를 쓴다. "이제"는 `now` 를 따로 넣지 않아도 `I'm about to start` 가 품는다. 문서에는 `Next up is integrating the Provision tools.`

### 카드 7 — tif 이미지가 매우 많고 multi tif 를 도입했어   (내가 쓴 한글)
- 내가 쓴 한글: "provision의 특징은 한 recipe당 생성되는 tif 이미지가 매우 많기도 하고, multi tif 개념을 도입했어."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: What sets Provision apart is that each recipe produces a huge number of TIFF images, and it also uses multi-page TIFFs.
- 왜 이렇게: "~의 특징은"을 `The characteristic of Provision is` 로 옮기면 교과서 문장이 된다. `What sets X apart is …`(남과 다른 점은), `The thing about X is …`(구어)가 자연스럽다. "한 recipe당 생성되는"은 `generated per recipe` 수동보다 recipe 를 주어로 세운 `each recipe produces` 가 읽기 쉽다. "개념을 도입했어"는 `introduced the concept of` 로 직역하지 않고 `uses` 로 줄인다. 영어권에서는 한 파일에 여러 장이 든 TIFF 를 `multi-page TIFF` 라고 부른다.

### 카드 8 — 2~3GB가 되는 경우도 있어   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 한 측정에서 생성되는 총 이미지 수가 2~3GBs가 되는 경우도 있어."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: A single measurement can produce 2–3 GB of images in total.
- 왜 이렇게: 한국어 원문이 "이미지 수"와 용량을 섞었다. 영어에서는 `the number of images` 는 개수이고 GB 는 크기여서 `2–3 GB of images` 로 써야 맞는다. "~하는 경우도 있다"는 `There are cases where …` 대신 조동사 `can` 하나로 받는다. 단위는 복수 s 를 붙이지 않고 `3 GB` 로 쓴다. 말로는 `three gigs` 라고 한다. `a single` 은 `one` 보다 "단 한 번에"를 강조한다.

### 카드 9 — minIO 로 문제 없이 처리 가능할까?   (내가 쓴 한글)
- 내가 쓴 한글: "minIO로 문제 없이 처리 가능할까?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Can MinIO handle that without any trouble?
- 왜 이렇게: "처리 가능할까"는 `Is it possible to process with MinIO?` 보다 도구를 주어로 세운 `Can MinIO handle that?` 이 곧다. `handle` 은 "감당하다"까지 품는다. 걱정이 섞인 물음이면 `Will MinIO cope with that?`(영국식), `Is MinIO going to be okay with that?`(구어). 설계 문서에는 `Is MinIO suitable for objects of this size?`

### 카드 10 — multi tiff 의 특징을 알려줘   (내가 쓴 한글)
- 내가 쓴 한글: "multi tiff의 특징을 알려줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Tell me how multi-page TIFFs work.
- 왜 이렇게: "특징을 알려줘"를 `Tell me the characteristics of` 로 옮기면 뜻은 통하지만 뻣뻣하다. 실제로 알고 싶은 것은 구조와 동작이므로 `how … work` 로 묻는다. 훑어 달라는 뜻이면 `Give me a rundown of multi-page TIFFs.` `rundown` 은 요점을 차례로 짚는 짧은 설명이다. `Walk me through …` 는 단계별로 설명해 달라는 말.

### 카드 11 — 분해해서 따로 볼 수도 있는 건가?   (내가 쓴 한글)
- 내가 쓴 한글: "우리가 분해해서 따로 볼 수도 있는건가?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Can we split one up and view the frames individually?
- 왜 이렇게: "분해하다"를 `disassemble` 이나 `decompose` 로 옮기면 기계나 수학 이야기가 된다. 파일을 낱장으로 나누는 것은 `split (up)`, `break apart`, 또는 `extract the frames`. "따로 보다"는 `view them separately` 도 되고 `individually` 나 `one at a time` 이 더 또렷하다. "~수도 있는 건가?"처럼 가능성을 떠보는 말투는 `So we could split it up and look at each frame on its own?` 처럼 평서문에 물음표를 달아도 산다.

### 카드 12 — SLM 을 받아서 회사에 맞게 tuning 하려고 한다면   (내가 쓴 한글)
- 내가 쓴 한글: "내가 SLM 오픈 웨이트 모델을 받아서 회사에 맞게 tuning을 하려고 한다면"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Say I wanted to take an open-weight SLM and fine-tune it for my company.
- 왜 이렇게: "~하려고 한다면"으로 가정을 깔 때 `If I try to …` 보다 `Say I wanted to …` 나 `Suppose I want to …` 가 대화에 가깝다. 과거형 `wanted` 는 "아직 계획 단계"라는 거리를 둔다. "받아서"는 `download` 도 되지만 `take A and B it` 틀이 "가져다가 ~한다"를 한 호흡에 담는다. "회사에 맞게"는 `for my company`, 더 구체적으로는 `on our internal data`, `for our use case`. 모델을 조정하는 일은 `tune` 보다 `fine-tune` 이 정확한 용어다.

### 카드 13 — 어떤 순서로, 어떤 프레임워크로, 어떤 데이터셋을   (내가 쓴 한글)
- 내가 쓴 한글: "어떤 순서대로, 어떤 프레임 워크 (있다면), 어떤 데이터 셋을 준비해서 진행해야 하는 지 알려줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: What steps should I follow, which framework should I use (if any), and what datasets do I need to prepare?
- 왜 이렇게: 한국어는 "어떤 A, 어떤 B, 어떤 C 를 ~해야 하는지 알려줘"로 한 동사에 다 걸지만 영어는 의문사마다 맞는 동사를 따로 준다(`follow` steps, `use` a framework, `prepare` datasets). "(있다면)"은 `if any` 두 단어다. 선택지가 정해진 범위에서 고를 때는 `which`, 열려 있을 때는 `what` 을 쓴다. 한 문장으로 줄이면 `Walk me through the steps, the framework (if any), and the datasets I'd need.`

### 카드 14 — 카드 12·13을 한 문단으로   (내가 쓴 한글)
- 내가 쓴 한글: "내가 SLM 오픈 웨이트 모델을 받아서 회사에 맞게 tuning을 하려고 한다면 어떤 순서대로, 어떤 프레임 워크 (있다면), 어떤 데이터 셋을 준비해서 진행해야 하는 지 알려줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: If I wanted to take an open-weight small language model and fine-tune it for my company, how should I go about it? I'd like to know the order of steps, which framework to use (if any), and what datasets to prepare.
- 왜 이렇게: 긴 한국어 한 문장을 영어 한 문장에 다 넣으면 `if` 절 뒤 주절이 너무 길어진다. 큰 질문(`how should I go about it?`)을 먼저 던지고 세부를 둘째 문장으로 넘긴다. `go about X` 는 "X 를 어떤 식으로 해 나가다"라는 구동사다. 둘째 문장은 `의문사 + to 부정사`(`which framework to use`, `what datasets to prepare`)로 맞춰 병렬을 지킨다.

### 카드 15 — 바꿔 끼울 수 있는 부품, 결과를 가르는 것   (고급 한글 · 번역)
- 한글 원문: "프레임워크는 사실상 바꿔 끼울 수 있는 부품이고, 결과를 가르는 것은 평가셋과 학습 데이터입니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: The framework is essentially a swappable part; what decides the outcome is the eval set and the training data.
- 번역 포인트: "바꿔 끼울 수 있는"은 `swappable` 또는 `interchangeable`. "결과를 가르다"는 `divide the result` 가 아니라 `decide the outcome`, `make the difference`, `determine how it turns out` 이다. 한국어의 "~은 ~이고, ~하는 것은 ~입니다" 대비는 세미콜론과 `what … is …` 분열문으로 살린다. 구어로는 `The framework barely matters. It's the eval set and the training data that make or break it.`

### 카드 16 — 유실 대신 중복을 택했습니다   (고급 한글 · 번역)
- 한글 원문: "같은 알림이 두 번 갈 수 있습니다. 유실 대신 중복을 택했습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The same notification may be sent twice. I chose duplication over loss.
- 번역 포인트: 두 선택지 가운데 하나를 골랐다는 말은 `choose A over B` 가 가장 짧다. `instead of` 를 쓰면 `I chose to duplicate instead of losing` 처럼 늘어진다. 설계 문서에서는 같은 결정을 `at-least-once delivery` 라는 용어로 부른다(`Delivery is at-least-once: a duplicate is possible, a loss is not.`). "갈 수 있습니다"는 가능성이므로 `may` 나 `can`. `will` 을 쓰면 항상 두 번 간다는 뜻이 된다.

### 카드 17 — 무엇을 아는가보다 어떻게 행동하는가   (고급 한글 · 번역)
- 한글 원문: "튜닝은 "무엇을 아는가"보다 "어떻게 행동하는가"를 바꾸는 데 적합합니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Fine-tuning is better suited to changing how a model behaves than what it knows.
- 번역 포인트: "A 보다 B 에 적합하다"는 `is better suited to B than A`. 따옴표 친 두 물음은 간접의문문 `how a model behaves` / `what it knows` 로 옮기면 따옴표 없이도 대구가 선다. 한국어는 "무엇을 아는가"가 먼저 나오지만 영어는 강조할 쪽(`how it behaves`)을 `than` 앞에 둔다. 한 줄 요약으로는 `Fine-tune for behaviour, retrieve for knowledge.`

### 카드 18 — 점수가 부풀려집니다   (고급 한글 · 번역)
- 한글 원문: "같은 원천의 변형이 학습과 평가 양쪽에 들어가면 점수가 부풀려집니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: If variants of the same source end up in both the training and eval sets, the scores come out inflated.
- 번역 포인트: "부풀려지다"는 `be inflated`. "들어가면"은 의도하지 않았는데 그렇게 된다는 뜻이어서 `are included` 보다 `end up in` 이 맞다. ML 에서는 이 현상을 `data leakage` 또는 `train–test contamination` 이라 부르므로 한 단어로 줄이면 `That's leakage, and it inflates your scores.` "같은 원천의 변형"은 `variants of the same source` 이고 `variations` 는 변화의 폭이라는 뜻으로 더 자주 쓰인다.

## 영어 다듬기

### 카드 1 — 필요 없어진 것을 지워 줘
- 내가 쓴 영어: "remove outdated / solved issues and no need anymore from the folders like .scratch, .remember, .playwright-mcp, .superpowers"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `no need anymore` → `anything we no longer need`. `no need` 는 "필요 없음"이라는 명사구여서 `remove` 의 목적어로 `issues` 와 나란히 놓이지 못한다. 병렬하려면 명사(구)끼리 맞춘다. `from the folders like` → `from folders like`. 특정 폴더들이 아니라 예를 드는 것이라 `the` 를 뺀다.
- 더 나은 표현: Clean out anything outdated, resolved, or no longer needed from folders like .scratch, .remember, .playwright-mcp, and .superpowers.
- 왜: 형용사 셋(`outdated`, `resolved`, `no longer needed`)을 `anything` 뒤에 나란히 걸면 병렬이 맞는다. 이슈가 풀렸다는 말은 `solved` 보다 `resolved` 를 쓴다(`solved` 는 문제·퍼즐). `clean out` 은 안을 비워 낸다는 구동사여서 폴더 정리에 `remove` 보다 어울린다. 목록 마지막 항목 앞에는 `and` 를 넣는다.

### 카드 2 — 네가 정해
- 내가 쓴 영어: "(json? toml? or whatever, you decide)"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: (JSON, TOML, whatever works. Your call.)
- 왜: 오류는 없고 채팅에서는 그대로 통한다. `or whatever` 는 "아무거나, 알 게 뭐야"로 들릴 때가 있어 `whatever works` 나 `whatever fits best` 로 바꾸면 맡긴다는 뜻만 남는다. `you decide` 대신 `Your call.` 이나 `I'll leave it to you.` 를 쓰면 결정권을 넘긴다는 관용 표현이 된다. 격식을 올리면 `Pick whichever format you think is best.`

### 카드 3 — Codex pane 닫아
- 내가 쓴 영어: "close codex pane"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `close codex pane` → `close the Codex pane`. 이미 둘 다 아는 특정 pane 이라 정관사가 붙는다. 명령어 스타일의 메모로는 관사를 떼기도 하지만 문장으로 쓸 때는 넣는다.
- 더 나은 표현: You can close the Codex pane now.
- 왜: 명령형만 쓰면 짧지만 `You can … now` 를 붙이면 "이제 볼일 끝났으니"라는 이유가 실린다. 제품 이름 `Codex` 는 대문자로 쓴다. 여러 개를 열었다면 `Close the pane you opened for Codex.`

### 카드 4 — .scratch 의 끝난 작업을 지워
- 내가 쓴 영어: "remove outdated / finished tasks in the .scratch folder"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Clear out any outdated or finished tasks from the .scratch folder.
- 왜: 문법 오류는 없다. 슬래시는 글에서 `or` 로 푼다. `in the folder` 는 "폴더 안에 있는 것을"이고 `from the folder` 는 "폴더에서 빼낸다"여서 지우는 동사와는 `from` 이 더 잘 붙는다. `any` 를 넣으면 "있다면 전부"가 된다. 지우지 말고 옮기라는 뜻이면 `Archive any finished tasks in .scratch.`

### 카드 5 — 낡은 문서라서 지웠어
- 내가 쓴 영어: "I removed them as I think they are outdated docs"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: I removed them because they're outdated.
- 왜: 틀린 곳은 없다. 이유를 대는 `as` 는 글에서는 괜찮지만 말이나 채팅에서는 "~할 때"로도 읽혀 `because` 가 안전하다. `they are outdated docs` 에서 `docs` 는 앞의 `them` 이 이미 문서여서 빼도 된다. `I think` 는 확신이 없을 때만 남긴다. 확신이 덜하다면 `I removed them since I figured they were outdated.`(`figure` 는 "~라고 판단하다"). 시제도 맞춘다. 지울 당시의 판단이면 `I thought they were outdated`.

### 카드 6 — 낡은 인용도 지워
- 내가 쓴 영어: "remove the stale citations too"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Go ahead and strip the stale citations as well.
- 왜: 원문 그대로 흠이 없고 `stale` 을 정확히 썼다. 상대가 "원하면 지우겠다"고 물은 데 답하는 자리여서 `Go ahead and …` 를 붙이면 허락의 뜻이 선다. `strip` 은 본문은 두고 붙은 것만 벗겨 낸다는 동사여서 인용 제거에 잘 맞고, 어시스턴트도 답에서 `Citations are stripped` 라고 받았다. `as well` 은 `too` 보다 살짝 격식 있다.

### 카드 7 — y축 맨 아래 장비 이름이 안 나와
- 내가 쓴 영어: "in hardware FDC -> Fab 전체, you have chuck 온도 fab 비교. the y axis, the tool name in the bottom is not displayed."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the bottom` → `at the bottom`. 위치의 끝자리는 `at the bottom / at the top` 이다(`in the bottom` 은 "바닥 속에"). `the y axis, the tool name …` 은 명사구 둘이 쉼표로만 이어져 관계가 안 보인다. `on the y-axis` 로 전치사를 붙인다. `y-axis` 는 하이픈으로 쓴다.
- 더 나은 표현: In Hardware → FDC → Fab 전체, the "Chuck 온도 fab 비교" heatmap is missing the bottom tool name on its y-axis.
- 왜: 버그 보고는 "어디서 / 무엇이 / 어떻게 잘못됐나"를 한 문장에 순서대로 담으면 읽기 쉽다. `you have …` 로 화면을 소개하는 문장을 따로 두지 않고 차트 이름을 주어로 세운다. `is missing X` 는 "X 가 빠져 있다"를 능동으로 말하는 버그 보고의 단골 틀이다(`The page is missing its title`). 수동으로 쓰려면 `The bottom tool name on the y-axis isn't showing.` 화면 버그에는 `is not displayed` 보다 `isn't showing` 이나 `doesn't show up` 을 더 자주 쓴다.
