# 2026-10-11 — 코칭

> 내가 쓴 글은 세션 넷에서 나왔다. Orca 정리, skewnono 패키지 점검, pm-notes 의 AI-DT 커리큘럼 grilling, 활동 지표 질문이다. 한국어는 스무 건 남짓이고 grilling 답변처럼 번호를 달아 여러 건을 한꺼번에 쓴 메시지는 문장 단위로 나눠 카드 스물여섯 장이 됐다. 영어는 두 건. skewnono 세션에 `[user]` 로 찍힌 "Codex 교차 검토 요청입니다…" 계열 다섯 건은 Codex 가 Herdr 로 보낸 글이어서 다루지 않았다. 스킬 문서(grilling, research, Herdr)와 task-notification, 서브에이전트 보고도 같은 이유로 뺐다. 번역 정독은 어시스턴트 답변에서 네 문장을 골랐다.

## 한글→영어

### 카드 1 — 휴지통으로 보냈어, 잔여물도 지워   (내가 쓴 한글)
- 내가 쓴 한글: "orca를  trash로 보냈어. 잔여물도 지워"   (출처: transcript:[user] Codes)
- 자연스러운 영어: I've moved Orca to the Trash. Clean up whatever it left behind, too.
- 왜 이렇게: 방금 한 일을 알리고 그 결과가 지금 상황의 전제가 되므로 현재완료 `I've moved` 가 맞다. macOS 휴지통은 고유한 자리라 `the Trash` 로 관사를 붙이고 대문자로 쓴다. "잔여물"을 `residue` 로 옮기면 화학 찌꺼기처럼 들린다. 파일 이야기에는 `leftover files`, `leftovers`, 또는 `whatever it left behind` 가 자연스럽다. "지워"는 흩어진 것을 찾아 치우라는 뜻이니 `delete` 보다 `clean up`.

### 카드 2 — 꼭 올려야 하는 게 있으면 목록으로   (내가 쓴 한글)
- 내가 쓴 한글: "npm packages 들 중에 최신 버젼으로 업데이트를 꼭 해야하는 경우가 있으면 리스트로 알려줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: List any npm packages that really need to be updated to the latest version.
- 왜 이렇게: "~가 있으면 알려줘"는 `if there are any, tell me` 로 풀지 않아도 `List any … that …` 한 문장이면 된다. `any` 가 "있다면"을 품는다. "꼭 해야 하는"은 `must be updated` 도 되고 급한 정도를 묻는 말투로는 `really need to be updated` 가 구어에 가깝다. "~들 중에"를 `among npm packages` 로 시작하면 번역투가 난다. "경우"는 옮기지 않는다.

### 카드 3 — 호환 여부 확인해줘   (내가 쓴 한글)
- 내가 쓴 한글: "typescript 7.0에 대한  vue-tsc와 @nuxt/eslint의 호환 여부 확인 해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Check whether vue-tsc and @nuxt/eslint are compatible with TypeScript 7.0.
- 왜 이렇게: "호환 여부"라는 명사구를 `the compatibility of A with B` 로 옮기면 무겁다. 영어는 `whether A is compatible with B` 처럼 절로 푼다. 전치사는 `with`. 도구 쪽을 주어로 세워 `whether they support TypeScript 7.0 yet` 이라 해도 같은 물음이고 `yet` 이 "지금 시점에 벌써"를 더한다.

### 카드 4 — 관련 있는 건가? 아직 적용 안 한 거야?   (내가 쓴 한글)
- 내가 쓴 한글: "vue-tsc는 nuxt랑 관련 있는건가? nuxt는 아직 typescript 7를 적용 안한거야?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Does vue-tsc have anything to do with Nuxt? And has Nuxt not moved to TypeScript 7 yet?
- 왜 이렇게: "~랑 관련 있다"는 `have something to do with` 이고 의문문에서는 `anything` 으로 바뀐다. 소속을 묻는 것이면 `Is vue-tsc part of Nuxt?` 가 더 곧다. "적용"을 `apply` 로 옮기면 패치를 바른다는 뜻이 되어 어색하다. 새 버전으로 넘어가는 일은 `move to`, `adopt`, `support`. "안 한 거야?"처럼 그럴 것 같다고 짐작하며 확인하는 물음은 평서문 어순에 물음표만 붙여 `So Nuxt hasn't moved to TypeScript 7 yet?` 이라 해도 된다.

### 카드 5 — 이 조합으로 가면 문제가 없을까?   (내가 쓴 한글)
- 내가 쓴 한글: "Node 24 최신 패치 → ESLint 10.12.0 + @nuxt/eslint 1.17.0 → vue-tsc 3.3.12 → TypeScript 6.0.3 로 했을 때 문제가 없을까?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Would we run into any problems if we went with the latest Node 24 patch, then ESLint 10.12.0 with @nuxt/eslint 1.17.0, then vue-tsc 3.3.12, then TypeScript 6.0.3?
- 왜 이렇게: 아직 안 해 본 일을 가정해 묻는 것이어서 `Would … if we went with …` 가정법이 어울린다. `go with` 는 여러 선택지 가운데 "그걸로 간다". "문제가 없을까"는 `run into problems`(문제에 부딪힌다)로 받으면 생생하다. 짧게는 `Do you see any issues with this combination: …?` 화살표로 적은 설치 순서는 `then` 을 반복해서 살린다.

### 카드 6 — 전체적으로 audit 진행해줘   (내가 쓴 한글)
- 내가 쓴 한글: "전체적으로 package 상태와 버젼에 문제 없는 지 audit 진행해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Run a full audit of the packages and make sure nothing is off with their state or versions.
- 왜 이렇게: "audit 을 진행하다"는 `run an audit` 또는 `do an audit`. `proceed an audit` 은 틀린 말이고 `proceed with` 는 이미 정해진 일을 계속할 때 쓴다. "전체적으로"는 `full` 이나 `across the board`. "문제 없는지"는 `make sure nothing is off`. `off` 는 "어딘가 어긋난"이라는 구어 형용사이고 격식을 올리면 `verify that there are no issues with`.

### 카드 7 — 권장대로 진행할게   (내가 쓴 한글)
- 내가 쓴 한글: "권장대로 진행할게"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Let's go with your recommendation.
- 왜 이렇게: 실제로 손을 움직이는 쪽은 상대여서 `I'll proceed` 보다 `Let's go with …` 나 `Go ahead as you recommended.` 가 상황에 맞다. `as recommended` 는 "권장대로"를 두 단어로 줄인 꼴이다(`Proceed as recommended.`). 한국어 "~할게"를 그대로 `I will` 로 옮기면 내가 직접 한다는 뜻이 된다.

### 카드 8 — 내가 방금 종료했어   (내가 쓴 한글)
- 내가 쓴 한글: "dev 서버 내가 방금 종료 했어"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: I just shut down the dev server.
- 왜 이렇게: "방금 ~했어"는 미국식으로 `I just + 과거형`, 영국식으로 `I've just + 과거분사`. 서버를 내리는 동사는 `shut down`, `stop`, 거칠게는 `kill`. `shut` 은 과거형도 `shut` 이다. "내가"에 힘을 주려면 끝에 `myself` 를 붙이지만 이 문맥은 "이제 빌드 돌려도 돼"라는 신호여서 `The dev server's down now.` 처럼 상태로 말해도 뜻이 통한다.

### 카드 9 — 규모는 상관없지만 대상은 정해야   (내가 쓴 한글)
- 내가 쓴 한글: "규모는 상관 없지만 대상을 정해야 함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: The size doesn't matter, but we do need to define who it's for.
- 왜 이렇게: "상관없다"는 `doesn't matter`. "대상을 정하다"는 `define the target audience` 가 격식이고 말로는 `decide who it's for` 가 쉽다. `we do need` 의 `do` 는 앞 절의 "상관없다"와 맞서 "이쪽은 꼭"을 강조한다. "~함"으로 끝나는 메모체는 영어에서 주어를 살려 `we need to` 로 풀어야 누가 해야 하는지 보인다.

### 카드 10 — 이런 사람들을 대상으로 교육   (내가 쓴 한글)
- 내가 쓴 한글: "코드를 짤 수 있는 사람, 네트워크 (클라우드), 회사에서 제공하는 서비스에 대한 이해가 있는 사람등을 대상으로 교육해야할거야."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: It should be aimed at people who can write code and who understand networking (cloud) and the services the company provides.
- 왜 이렇게: "~을 대상으로 교육하다"는 `be aimed at` 이나 `target`. `educate for people` 은 안 쓴다. 조건 둘은 관계절 `who … and who …` 로 나란히 놓는다. "이해가 있는"은 `have an understanding of` 보다 동사 `understand` 나 `are familiar with` 가 짧다. 분야 이름은 `network` 가 아니라 `networking`. "회사에서 제공하는 서비스"는 `the services the company provides` 이고 줄이면 `our internal services`.

### 카드 11 — 양식은 없지만 5단 구성 좋아   (내가 쓴 한글)
- 내가 쓴 한글: "양식은 없지만 5단 구성 좋아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: There's no set format, but the five-part structure works for me.
- 왜 이렇게: "정해진 양식"은 `a set format` 이나 `a required template`. `set` 이 형용사로 "미리 정해진"이다. "좋아"를 `is good` 으로 옮겨도 되지만 제안을 받아들이는 말로는 `works for me`, `sounds good` 이 흔하다. "5단"은 `five-part` 처럼 하이픈으로 묶고 `part` 를 단수로 둔다.

### 카드 12 — 꼭 연결 지을 필요는 없음   (내가 쓴 한글)
- 내가 쓴 한글: "Fast Track 수료하지 않고도 Agent를 개발하는 사람들이 있기 때문에 꼭 연결 지을 필요는 없음."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Some people build agents without ever completing Fast Track, so the two don't need to be tied together.
- 왜 이렇게: 한국어는 "~때문에"로 이유를 먼저 묶는데 영어 구어는 사실을 평서문으로 말하고 `so` 로 잇는 쪽이 가볍다. `Because …,` 로 시작해도 문법은 맞다. "~하지 않고도"는 `without -ing` 이고 `ever` 를 넣으면 "한 번도 안 거치고도"가 산다. "연결 짓다"는 `tie A to B`, `link`, `make A a prerequisite for B`(선수 조건으로 삼다). "꼭 ~할 필요는 없다"는 `don't need to` 나 `don't necessarily have to`.

### 카드 13 — 참여한 경우를 봐야 할 거야   (내가 쓴 한글)
- 내가 쓴 한글: "(c) 교육 이수를 하고 본인이 만든 Agent도 있고, (b)를 위해 협업을 통해 개발한 Agent 혹은 다른 팀을 도와 가이드를 해서 만든 Agent등 참여한 경우를 봐야 할 거야."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: (c): they should complete the training and have an agent of their own. For (b), we should look at agents they were involved in, whether co-developed or built by another team under their guidance.
- 왜 이렇게: 긴 한 문장을 둘로 끊었다. "본인이 만든 Agent"는 `an agent of their own`. "협업을 통해 개발한"은 `co-developed` 한 단어로 줄어든다. "A 혹은 B 등"처럼 두 유형을 드는 자리는 `whether A or B` 가 깔끔하다. "다른 팀을 도와 가이드를 해서 만든"은 만든 주체가 다른 팀이므로 `built by another team under their guidance` 로 수동과 `under` 를 쓴다. "참여한"은 `be involved in`.

### 카드 14 — 질 낮은 Agent 난립을 막고 고도화를 이끌 Expert   (내가 쓴 한글)
- 내가 쓴 한글: "무분별하게 쏟아지는 질 낮은 Agent를 사전에 방지하고, 1인 1Agent가 오면 각자 Agent를 잘 유지하고 보수, 장기적으로 고도화 될 수 있도록 가이드를 해주는 Expert가 필요함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We need Experts who can head off a flood of low-quality agents and, once everyone has an agent of their own, guide people in maintaining theirs and improving them over the long run.
- 왜 이렇게: "무분별하게 쏟아지는"은 `a flood of` 가 그림까지 옮긴다. "사전에 방지"를 `prevent in advance` 로 쓰면 뜻이 겹친다. `prevent` 에 이미 "미리"가 들어 있어서다. `head off`(오기 전에 막아선다)가 잘 맞는다. "1인 1Agent 가 오면"은 `once everyone has an agent of their own`. "고도화"는 `advance` 나 `upgrade` 보다 `improve`, `mature` 가 뜻에 가깝다. "~할 수 있도록 가이드를 해주는"은 `guide people in -ing`.

### 카드 15 — 구성원에게 발표, 나중에 임원 보고   (내가 쓴 한글)
- 내가 쓴 한글: "카테고리별로 커리큘럼을 만드는 구성원들에게 발표. 나중에 임원에게 보고."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: First I present it to the people building the curriculum for each category; later it goes up to the executives.
- 왜 이렇게: "발표하다"는 `present it to` 사람. `announce` 는 공지라서 다르다. "카테고리별로 커리큘럼을 만드는 구성원"은 분사구 `the people building the curriculum for each category` 로 뒤에서 꾸민다. "임원에게 보고"는 `report to the executives` 도 되지만 `report to` 는 "직속 상사가 누구다"로도 읽힌다. `brief the executives` 나 `it goes up to the executives`(위로 올라간다)가 오해가 없다.

### 카드 16 — 팀의 챔피언으로 성장   (내가 쓴 한글)
- 내가 쓴 한글: "Expert를 양성해서 각자 팀에서 챔피언으로 활동. 질 낮은 agent가 되지 않도록 가이드를 하는 구성원으로 성장."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We train Experts, and they act as champions on their own teams, growing into the people who keep agents from turning out badly.
- 왜 이렇게: "양성하다"는 `train` 이나 `develop`. "챔피언으로 활동"은 `act as champions` 이고 여기서 `champion` 은 우승자가 아니라 "앞장서 퍼뜨리는 사람"이다. 팀 소속은 미국식으로 `on a team`. "~로 성장"은 `grow into`. "~되지 않도록"은 `keep A from -ing`, "결과물이 나쁘게 나오다"는 `turn out badly`.

### 카드 17 — 마켓에 올리려면 승인을 받아야 (1차 관문)   (내가 쓴 한글)
- 내가 쓴 한글: "추후 agent / tool market에 올리기 위해서는 각 팀의 expert의 승인을 받아야 함 (1차 관문)"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Later on, anything listed on the agent/tool marketplace will need sign-off from the team's Expert — the first gate.
- 왜 이렇게: 앱·도구를 올리는 장터는 `market` 보다 `marketplace` 라고 부른다. "올리다"는 `list` 나 `publish`. "승인을 받아야 한다"는 `need approval from` 이 중립이고 실무 구어로는 `sign-off`(서명해서 통과시킴). "~의 ~의" 소유격이 겹치는 `each team's expert's approval` 은 `from` 으로 풀어 피한다. "1차 관문"은 `the first gate` 이고 뒤에 2차가 있다는 것까지 말하려면 `the first of two gates`.

### 카드 18 — 진행. 그런데 커리큘럼은 우리가 만들어야   (내가 쓴 한글)
- 내가 쓴 한글: "진행. 그런데 builder / guide에 대한 커리큘럼을 우리가 만들어야 하고 어떤 것들을 가르쳐야 하는 지 정해야 함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Go ahead. That said, we still have to build the Builder and Guide curricula ourselves and decide what to teach.
- 왜 이렇게: 한 단어 "진행"은 `Go ahead.` 승인하면서 다른 얘기를 꺼내는 "그런데"는 `That said,` 나 `One thing, though:`. `By the way` 는 화제를 아예 돌릴 때다. "우리가"의 강조는 문장 끝 `ourselves` 로 옮긴다. "어떤 것들을 가르쳐야 하는지"는 `what to teach` 세 단어로 줄어든다. `curriculum` 의 복수는 `curricula`(또는 `curriculums`).

### 카드 19 — 공개된 커리큘럼을 벤치마크할 수 있는지 조사   (내가 쓴 한글)
- 내가 쓴 한글: "현 상황에서 public하게 공개된 커리큘럼이 있고 그것을 우리가 Benchmark 해서 사용할 수 있는 지 함께 조사해야함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We should also look into whether any curricula are publicly available right now and whether we can benchmark against them.
- 왜 이렇게: "public 하게 공개된"은 뜻이 겹치므로 `publicly available` 하나로 쓴다. `benchmark` 를 동사로 쓸 때 기준으로 삼는 대상에는 `against` 를 붙인다(`benchmark against them`). 가져다 쓰겠다는 뜻이 더 크면 `use them as a baseline`, `adapt them`. "함께 조사"의 "함께"는 "이것도 같이"여서 `together` 가 아니라 `also` 다. "조사하다"는 `look into`. 묻는 것이 둘이므로 `whether` 를 두 번 세운다.

### 카드 20 — 공동 개발 이력도 인정된다는 점 명심   (내가 쓴 한글)
- 내가 쓴 한글: "가이드 자격에는 함께 공동 개발한 이력도 적용된다는 점 명심."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Keep in mind that co-development experience also counts toward Guide eligibility.
- 왜 이렇게: "명심"은 `Keep in mind that …` 이고 조금 더 격식 있게는 `Bear in mind`. "적용된다"를 `is applied` 로 옮기면 뜻이 흐려진다. 요건을 채우는 실적으로 쳐 준다는 말이므로 `count toward` 가 정확하다(`These credits count toward your degree`). "함께 공동"은 `co-` 하나면 된다. "자격"은 `eligibility`(요건을 갖춤)이고 `qualification` 은 이미 딴 자격증 쪽이다.

### 카드 21 — 실습으로 메울 수 있다고 생각해   (내가 쓴 한글)
- 내가 쓴 한글: "리뷰 심사 실습으로 메울 수 있다고 생각해."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I think the review and assessment exercises can close that gap.
- 왜 이렇게: "공백을 메우다"는 `close the gap`, `fill the gap`, `make up for it`. 한국어는 목적어 "그 공백"을 생략했지만 영어는 `that gap` 을 꼭 넣는다. "실습"은 `exercises` 나 `hands-on practice`. `practice` 만 쓰면 "관행"으로도 읽힌다. 주어를 사람이 아니라 `exercises` 로 세워 "실습이 메운다"고 하면 `can be filled by` 같은 수동을 피한다.

### 카드 22 — 끝나면 세 결과 합쳐서 정리해줘   (내가 쓴 한글)
- 내가 쓴 한글: "opencode 끝나면 세 결과 합쳐서 정리해줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Once OpenCode is done, pull the three results together into one summary.
- 왜 이렇게: "~하면"이 시간 순서를 말할 때는 `once` 나 `when` 을 쓰고 그 절 안은 미래 일이어도 현재시제(`is done`)다. `will be done` 은 틀린다. "합쳐서 정리"는 `pull together`, `combine … into one summary`, 격식으로는 `consolidate`. `into` 가 합친 결과물의 모양을 가리킨다.

### 카드 23 — 반영해서 정리해줘   (내가 쓴 한글)
- 내가 쓴 한글: "반영해서 정리해줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Work those in and write it up.
- 왜 이렇게: "반영하다"를 `reflect` 로 옮기면 "비추다, 숙고하다"로 읽혀 어색하다. 문서에 넣는다는 뜻은 `incorporate`, 구어로 `work in`, `fold in`. "정리하다"는 깔끔한 문서로 만든다는 뜻이어서 `write it up` 이나 `put together a clean version`. 한국어는 목적어를 다 뺐지만 영어는 `those`(권고들)와 `it`(문서)을 채워야 문장이 선다.

### 카드 24 — 어떤 식으로 계산되는 거야?   (내가 쓴 한글)
- 내가 쓴 한글: "DAW/MAU 는 어떤식으로 계산이 되는거야?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: How are DAU and MAU calculated?
- 왜 이렇게: 계산하는 주체가 중요하지 않으므로 수동 의문문이 자연스럽다. "어떤 식으로"는 `how` 하나면 충분하고 `in what way` 는 과하다. 구어로는 `How do you work out DAU and MAU?` 도 쓴다. `work out` 은 "셈해서 구한다". 원문의 DAW 는 DAU(Daily Active Users)의 오타다. 슬래시로 쓴 `DAU/MAU` 는 영어에서 두 값의 비율로 읽히니 둘을 따로 물을 때는 `and` 로 잇는다.

### 카드 25 — 여러 번 접속해도 한 명으로 치나?   (내가 쓴 한글)
- 내가 쓴 한글: "한명에 하루에 여러번 접속해도 활동한 사람수는 하나로 카운트 되는건가?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: If one person visits several times in a day, do they still count as just one active user?
- 왜 이렇게: "~로 카운트되다"는 `count as` 로 자동사처럼 쓴다(`It counts as one`). `is counted as` 도 맞지만 길다. "~해도"의 양보는 `even if` 가 정석이고 `still` 을 주절에 넣으면 `if` 만으로도 그 느낌이 산다. 성별을 모르는 한 사람은 `they` 로 받는다. "접속"은 웹 도구라면 `visit` 이나 `log in`. `access` 를 동사로 쓰면 목적어가 필요하다.

### 카드 26 — 그럼 MAU 가 WAU 보다 높게 나오겠네   (내가 쓴 한글)
- 내가 쓴 한글: "그럼 WAU보다 MAU가 높은 식으로 카운트가 되겠네 한달동안 한번이라도 들어온 횟수면?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: So MAU will always come out at least as high as WAU, then, if it counts everyone who came in at least once during the month?
- 왜 이렇게: 앞 답에서 결론을 끌어내 확인하는 말투는 `So …, then?`. "~식으로 카운트가 되겠네"는 계산해 보니 그렇게 나온다는 뜻이어서 `come out`(결과가 ~로 나오다)이 맞다. 같을 수도 있으므로 `higher than` 보다 `at least as high as` 가 정확하다. "한 번이라도"는 `at least once`. 원문은 "횟수"라고 썼지만 세는 것은 사람이어서 `everyone who came in` 으로 옮겼다. 어시스턴트도 답에서 이 점을 짚었다.

### 카드 27 — 떠넘기는 꼴이 된다   (고급 한글 · 번역)
- 한글 원문: "선택지 7개를 내밀면 결정을 청중에게 떠넘기는 꼴이 됩니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Put seven options in front of the audience and you've handed the decision off to them.
- 번역 포인트: "~하면 ~하는 꼴이 된다"는 `If you …, you end up -ing` 로 옮겨도 되고 `명령문 + and + 결과` 로 쓰면 경고의 힘이 세진다. "내밀다"는 `put … in front of`, "떠넘기다"는 `hand off` 나 `offload onto`. 책임 회피의 뜻이 짙으면 `pass the buck`. 결과절을 현재완료(`you've handed`)로 두면 "그 순간 이미 넘긴 셈"이라는 "꼴이 된다"의 느낌이 산다. 격식을 올리면 `Presenting seven options amounts to delegating the decision to the audience.`

### 카드 28 — 책임을 지우면 아무도 하지 않는다   (고급 한글 · 번역)
- 한글 원문: "승인자에게 사고 책임을 지우면 아무도 Guide를 하지 않습니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Hold approvers liable for incidents and no one will want to be a Guide.
- 번역 포인트: "책임을 지우다"는 `hold A liable for B`(법적·제재가 따르는 책임)나 `hold A accountable for B`(설명할 책임). 제재가 걸린 문맥이라 `liable` 을 골랐다. "아무도 하지 않는다"는 `no one will do Guide` 가 아니라 `no one will want to be a Guide` 로 "하려 들지 않는다"는 속뜻을 꺼낸다. 격식형은 `If approvers bear responsibility for incidents, no one will take on the role.`

### 카드 29 — 인증의 성격이 자격으로 바뀐다   (고급 한글 · 번역)
- 한글 원문: "승인 권한이 붙으면 인증의 성격이 "역량 증명"에서 "자격"으로 바뀝니다. 갱신과 효력정지가 형식이 아니라 실제 통제 수단이 됩니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Once approval authority is attached, the certification stops being proof of competence and becomes a licence. Renewal and suspension are no longer formalities; they are real controls.
- 번역 포인트: "성격이 A 에서 B 로 바뀐다"를 `the nature changes from A to B` 로 옮기면 추상명사가 주어가 되어 힘이 빠진다. `stops being A and becomes B` 처럼 동사 둘로 풀었다. "자격"은 무언가를 할 권한이 따르는 것이어서 `licence`(미국식 `license`)가 `qualification` 보다 맞다. "형식이 아니라"는 `no longer formalities`. `formality` 는 "절차상 거치기만 하는 것"이다. "통제 수단"은 `means of control` 보다 복수 명사 `controls` 가 감사·보안 문서에서 쓰는 말이다.

### 카드 30 — MAU 는 한 달 뒤에야 떨어진다   (고급 한글 · 번역)
- 한글 원문: "한 번 온 사람은 30일 동안 MAU에 남기 때문에, 사용이 줄어도 MAU는 한 달 뒤에야 떨어집니다. 최근 변화는 DAU·WAU에서 먼저 보입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: Because anyone who visits once stays in MAU for 30 days, MAU doesn't drop until a month after usage falls off. Recent changes show up in DAU and WAU first.
- 번역 포인트: "~뒤에야 ~한다"는 영어에서 부정으로 뒤집어 `not … until` 로 쓴다. "한 번 온 사람"은 `anyone who visits once`. "사용이 줄다"는 `usage falls off` 나 `drops`. 같은 동사를 피하려고 MAU 쪽에 `drop`, 사용 쪽에 `fall off` 를 나눠 썼다. "~에서 먼저 보인다"는 `show up in … first`. 지표 용어로 줄이면 `MAU is a lagging indicator; DAU and WAU lead.`

## 영어 다듬기

### 카드 31 — grilling for → grill me on
- 내가 쓴 영어: "grilling for the ai-dt curriculum"   (출처: transcript:[user] pm-notes)
- 더 나은 표현: Grill me on the AI-DT curriculum. / Let's pick the grilling session on the AI-DT curriculum back up.
- 왜: 명사구로 던진 메모라서 틀린 데는 없다. 다만 `grill` 은 `grill someone on/about a topic` 꼴로 쓰는 동사이고 주제 앞 전치사는 `for` 보다 `on` 이 맞는다. 동사로 시작하면 누가 누구를 몰아붙이는지 분명해진다. 지난 세션을 이어 가는 것이었으니 `pick … back up`(하던 것을 다시 집어 든다)을 넣으면 "재개"까지 전한다. 약어는 대문자 `AI-DT`.

### 카드 32 — and close the panes
- 내가 쓴 영어: "커밋하고 push 해줘. and close the panes"   (출처: transcript:[user] pm-notes)
- 더 나은 표현: Commit and push, then close the panes you opened.
- 왜: 문법은 맞다. 세 동작을 한 문장에 넣고 `then` 으로 순서를 주면 "push 가 끝난 뒤에 닫아라"가 분명하다. `the panes` 만 쓰면 어느 패널까지인지 열려 있다. 실제로 워크스페이스에 어시스턴트가 열지 않은 패널이 하나 더 있었고 그것은 닫지 않았다고 따로 보고가 왔다. `you opened` 나 `the Codex and OpenCode panes` 처럼 범위를 붙이면 그런 확인이 필요 없어진다.
