# 2026-09-24 — 코칭

> 오늘 `[user]` 한국어는 대부분 pm-notes 오케스트레이션 세션(pi·pi-subagents 사내 배선)에서 나왔고 equipment-data-map 의 AutoRAG 검토 세션에서 두 개가 더 나왔다. (a) 카드 24장. "전부 OK.", "덮어도 좋아.", "응 codex 페인 닫아줘" 처럼 고칠 게 없는 짧은 답은 뺐다. (b) 는 같은 세션의 어시스턴트 한국어에서 4문장. 영어 다듬기는 equipment-data-map 세션 7장, pm-notes 4장으로 11장. english-study 파이프라인 프롬프트와 herdr 스킬 본문은 `[user]` 로 찍혔어도 내가 쓴 글이 아니라 제외했다.

## 한글→영어

### 카드 1 — 이 저장소를 우리 프로젝트에 쓸 수 있을까   (내가 쓴 한글)
- 내가 쓴 한글: "github에서 marker-inc-korea의 AutoRAG repo를 발견했어. 이걸 우리가 하려고 하는 프로젝트에 활용 가능한 건지 검토해줘."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: I came across Marker-Inc-Korea's AutoRAG repo on GitHub. Could you check whether it would be useful for what we're building?
- 왜 이렇게: "발견했어"는 찾아다니다 찾은 게 아니라 우연히 본 것이라 `found` 보다 `came across` 가 맞다. "우리가 하려고 하는 프로젝트"를 `the project that we are trying to do` 로 옮기면 길고 어색해서 `what we're building` 으로 줄였다. "활용 가능한 건지 검토해줘"는 `check whether it would be useful for` 로 `whether` 절을 쓴다.

### 카드 2 — 여기 본 거 맞아?   (내가 쓴 한글)
- 내가 쓴 한글: "여기 확인한거 맞아? main branch"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Is this the one you looked at? The main branch?
- 왜 이렇게: "확인한 거 맞아?"는 `Did you check this?` 보다 `Is this the one you looked at?` 이 "딴 걸 본 거 아니야?"라는 의심을 더 잘 싣는다. 뒤에 붙인 "main branch"는 영어에서도 짧은 되묻기 `The main branch?` 로 그대로 살린다.

### 카드 3 — 모델 사이즈별로 LLM 을 연결해 놨어   (내가 쓴 한글)
- 내가 쓴 한글: "orchestration 폴더를 만들고 가장 최근 orchestration 트렌드를 반영해서 herdr에서 pi coding agent를 이용한 orchestration 구조를 만들어줘. 회사에서 사용할 예정이고. HCP-Big-Latest, HCP-Medium-Latest, Qwen3.8-27b와 같이 모델 사이즈별로 최신 LLM들을 연결해놓았어. 각각 GLM-5.3, GLM-5.3-flash for Big and Medium에 해당됩니다."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Create an `orchestration` folder and set up an orchestration structure that runs the pi coding agent inside herdr, following the latest orchestration trends. We'll be using it at work. I've connected the latest LLMs by size — HCP-Big-Latest, HCP-Medium-Latest and Qwen3.8-27b. Big and Medium map to GLM-5.3 and GLM-5.3-flash respectively.
- 왜 이렇게: "트렌드를 반영해서"는 `reflecting` 도 되지만 `following` 이나 `in line with` 가 더 자연스럽다. "사용할 예정이고"로 끊긴 조각은 `We'll be using it at work.` 로 완결한다. "각각 ~에 해당됩니다"는 `map to … respectively` 가 딱 맞고 `correspond to` 는 조금 더 격식. 한 문장에 존댓말과 반말이 섞였는데 영어에선 드러나지 않는다.

### 카드 4 — pi 에서 뭘 쓰는 거야?   (내가 쓴 한글)
- 내가 쓴 한글: "pi에서 어떤게 사용하는거지?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Which parts of pi does this actually use?
- 왜 이렇게: "어떤 게 사용하는 거지?"는 주어와 목적어가 섞였다. 뜻은 "(이 구조가) pi 의 어떤 기능을 쓰는 거지?"이므로 주어를 `this` 로 세운다. `actually` 를 넣으면 "문서 말고 실제로"라는 궁금증이 산다.

### 카드 5 — 이미 설치돼 있어   (내가 쓴 한글)
- 내가 쓴 한글: "회사에 pi-subagents 이미 설치 되어 있어"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: pi-subagents is already installed at work.
- 왜 이렇게: "회사에"는 장소라 `at the company` 보다 `at work` 나 `on our office machines` 가 자연스럽다. 이 말은 "그러니 그걸 써도 된다"는 암시라 뒤에 `so we can use it` 을 붙이면 의도가 더 분명해진다.

### 카드 6 — 퇴근할 때만이 아니라 업무 중에도   (내가 쓴 한글)
- 내가 쓴 한글: "퇴근 원샷뿐만 아니라 업무 중에도 사용할 예정."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'll use it during the workday too, not just for the one-shot run when I leave.
- 왜 이렇게: "~뿐만 아니라 ~도"를 `not only A but also B` 로 옮기면 문어체가 된다. 채팅에서는 `B too, not just A` 순서가 가볍다. "퇴근 원샷"은 영어에 없는 조어라 `the one-shot run when I leave (for the day)` 로 풀어 준다.

### 카드 7 — 업무 중엔 어떻게 쓰면 돼?   (내가 쓴 한글)
- 내가 쓴 한글: "업무 중에 활용하려면 어떤식으로 진행하면 되는거지?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: How should I use it during the day?
- 왜 이렇게: "어떤 식으로 진행하면 되는 거지?"는 "어떻게 하면 돼?"의 긴 버전이다. 영어에선 `How should I …?` 하나로 끝난다. "활용"과 "진행"을 둘 다 옮기려 하면 `utilize … proceed` 처럼 딱딱해지니 동사 하나만 고른다.

### 카드 8 — codex 와 구조를 논의하고 검증받아   (내가 쓴 한글)
- 내가 쓴 한글: "codex에게 전체적인 구조에 대해 논의하고, 검증을 받아 개선 작업 진행해줘."   (출처: transcript:[user] pm-notes, /herdr 인자)
- 자연스러운 영어: Talk the overall design through with Codex, have it review the design, and make the improvements.
- 왜 이렇게: "codex에게 논의하고"는 조사가 어긋났다. 논의는 "~와" 하는 것이라 영어도 `with Codex`. `discuss about` 은 틀린 표현이다(`discuss` 는 타동사). "검증을 받아"는 사역 `have it review` 가 자연스럽다. "개선 작업 진행해줘"의 "작업 진행"은 영어에서 사라지고 `make the improvements` 만 남는다.

### 카드 9 — 세팅이 잘 됐는지 확인할 스크립트   (내가 쓴 한글)
- 내가 쓴 한글: "처음에 orchestration이 잘 세팅이 되었는지 테스트해볼 수 있는 코드나 세트를 진행하려면 어떻게 해야하지? script 만들 수 있나."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: How can I check that the orchestration is set up correctly the first time? Could you write a script for that?
- 왜 이렇게: "테스트해볼 수 있는 코드나 세트를 진행하려면"은 뜻이 겹겹이 쌓였다. 알맹이는 "처음 세팅이 맞는지 확인하는 방법"이라 `check that … is set up correctly` 로 줄인다. "만들 수 있나"는 혼잣말 같은 질문이지만 영어에선 요청 `Could you write …?` 로 옮긴다.

### 카드 10 — 지우고 커밋해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "orch.sh랑 roles/ 지우고 커밋해줘"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Delete `orch.sh` and `roles/`, then commit.
- 왜 이렇게: "~하고 ~해 줘"의 순서는 `A, then B` 로 드러낸다. `and commit` 도 되지만 `then` 이 "지운 다음에"를 분명히 한다. 명령문 자체가 요청이라 `please` 없이도 동료 사이에선 무례하지 않다.

### 카드 11 — 이미 운영 중이야   (내가 쓴 한글)
- 내가 쓴 한글: "pi models.json에는 이미 모델들 구성해서 운영 중."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: The models are already set up in pi's `models.json` and running in production.
- 왜 이렇게: "운영 중"은 `operating` 이 아니라 `in use` 나 `running in production`. "구성해서"는 `configured` 나 `set up`. 한국어 메모체의 명사 종결(" 운영 중.")은 영어에서 완결 문장으로 바꿔야 읽힌다.

### 카드 12 — 27b 가 더 낫지 않나?   (내가 쓴 한글)
- 내가 쓴 한글: "HCP-Small-Latest는 Qwen3.6-35B-A3B로 되어있어. Qwen3.8-27b가 더 좋지 않나?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: HCP-Small-Latest points to Qwen3.6-35B-A3B. Wouldn't Qwen3.8-27b be better?
- 왜 이렇게: "~로 되어 있어"는 별칭이 실제 모델을 가리키는 것이라 `points to` 나 `is mapped to` 가 정확하다. "더 좋지 않나?"는 부정 의문 `Wouldn't … be better?` 로 옮기면 "내 생각엔 그런데"라는 뉘앙스까지 산다.

### 카드 13 — Vision 도 같은 모델   (내가 쓴 한글)
- 내가 쓴 한글: "HCP-Vision-Latest도 Qwen3.6-35B-A3B"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: HCP-Vision-Latest is also Qwen3.6-35B-A3B.
- 왜 이렇게: 동사가 빠진 한국어 메모는 영어에서 `is also` 를 채워야 한다. 앞 메시지와 이어지는 말이면 `Same for HCP-Vision-Latest.` 가 더 짧고 자연스럽다.

### 카드 14 — DRM 추출 파이프라인도 봐 줘   (내가 쓴 한글)
- 내가 쓴 한글: "DRM 문서 추출 파이프라인도 한번 봐줘 3B보다는 27B가 더 좋지 않겠어"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Take a look at the DRM document-extraction pipeline too. Wouldn't 27B do better than 3B there?
- 왜 이렇게: "한번 봐 줘"의 "한번"은 `once` 가 아니라 가볍게 부탁하는 말투라 `take a look at` 에 이미 들어 있다. "더 좋지 않겠어"는 성능 비교라 `be better` 보다 `do better` 가 "일을 더 잘한다"는 뜻을 준다.

### 카드 15 — 업데이트했어? / 테스트 방법은?   (내가 쓴 한글)
- 내가 쓴 한글: "orchestration 내용 업데이트 했어?" / "orchestration test 방법은?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Did you update the orchestration docs? / How do I test the orchestration?
- 왜 이렇게: "내용"은 대개 옮기지 않거나 구체 명사(`docs`, `README`)로 바꾼다. "방법은?"처럼 명사로 끝낸 질문을 `What is the method?` 로 옮기면 딱딱하다. `How do I …?` 가 영어의 기본형.

### 카드 16 — PowerShell 에서는 어떻게 돌려?   (내가 쓴 한글)
- 내가 쓴 한글: "PS에서 어떻게 실행하지"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: How do I run it from PowerShell?
- 왜 이렇게: 셸에서 실행할 때 전치사는 `from` 이나 `in` 이다. `PS` 같은 약어는 상대가 헷갈릴 수 있어 한 번은 풀어 쓴다.

### 카드 17 — 같은 provider 인데 왜 Big 만 안 될까   (내가 쓴 한글)
- 내가 쓴 한글: "HCP-Big-Latest와 HCP-Medium-Latest 모두 같은 provider인데 이상하다. 왜 Big만 안될까"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: That's odd — HCP-Big-Latest and HCP-Medium-Latest are on the same provider. Why is only Big failing?
- 왜 이렇게: "이상하다"를 문장 끝에 두면 영어에서는 어색하니 `That's odd —` 로 앞에 세우고 근거를 대시 뒤에 붙인다. "안 될까"는 `not work` 보다 진행형 `is … failing` 이 "지금 계속 실패 중"을 잘 전한다. `only` 는 `Big` 바로 앞에 둔다.

### 카드 18 — 병합은? / 회사 LLM 에게 어떻게 시킬까   (내가 쓴 한글)
- 내가 쓴 한글: "병합은 어떻게 하지?" / "orchestration을 쓰는 회사에도 LLM이 있어. LLM 어떤식으로 요청하면 좋을까? json 병합?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: How do I do the merge? / We have an LLM at the office where I'll run the orchestration too. How should I ask it to do this — have it merge the JSON?
- 왜 이렇게: "병합은 어떻게 하지?"는 `How do I merge it?` 로도 충분하다. "LLM 어떤 식으로 요청하면"에서 "LLM 에게"의 조사가 빠졌다. 영어에선 `ask it to` 로 대상이 드러나는 구조. 끝의 "json 병합?"은 제안형 되묻기라 대시 뒤 `have it merge the JSON?` 으로 붙인다.

### 카드 19 — 1단계 결과 보고   (내가 쓴 한글)
- 내가 쓴 한글: "1단계 프롬프트 실행해보니, defaultModel: HCP-Big-Latest. subagetns 블록 : 있음. 키:agentOverrides. 안에 reviewer 하나." / "이미 존재하는 reviewr 교체해도 상관 없음. 2단계 프롬프트도 office-setup.md에 있나?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I ran the step 1 prompt. `defaultModel` is HCP-Big-Latest, and there's a `subagents` block with an `agentOverrides` key containing one entry, `reviewer`. / It's fine to replace the existing `reviewer`. Is the step 2 prompt in `office-setup.md` too?
- 왜 이렇게: 키-값 메모("블록 : 있음")는 영어에서 `there's a … block with …` 처럼 존재문으로 묶으면 읽기 쉽다. "안에 reviewer 하나"는 `containing one entry` 로 관계를 드러낸다. "상관 없음"은 허락이라 `It's fine to …` 나 `Go ahead and …`. `subagetns`, `reviewr` 오타도 같이 고친다.

### 카드 20 — LLM 으로 전부 테스트하니 repo 도 맞춰야 해   (내가 쓴 한글)
- 내가 쓴 한글: "이제 LLM으로 전부 다 테스트를 진행하니 그거에 맞게 여기 repo도 수정해야해. 현재 office-setup.md 하나하나 llm을 통해서 진행하는 중" / "4까지 돌리고 나니 5번 확인 불가가 나왔어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Since we're now running every test through the LLM, this repo needs to be updated to match. I'm currently going through `office-setup.md` step by step with the LLM. / After running up to step 4, step 5 came back as "unable to verify."
- 왜 이렇게: "그거에 맞게"는 `to match` 두 단어로 끝난다. "하나하나 진행하는 중"은 `going through … step by step`. "확인 불가가 나왔어"는 결과가 돌아온 것이라 `came back as` 가 딱 맞다. 도구 출력 문구는 따옴표로 감싼다.

### 카드 21 — RPM·TPM 한도를 pi 에서 관리할 수 있나   (내가 쓴 한글)
- 내가 쓴 한글: "my-local-provider의 경우 RPM이 50, TPM 500000으로 되어 있어서 API call이 너무 낮거나 많으면 문제가 될텐데 이런 것들을 잘 관리할 수 있게 pi에서 세팅할 수 있어?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: `my-local-provider` is capped at 50 RPM and 500,000 TPM, so too many API calls could get us throttled. Can pi be configured to stay within those limits?
- 왜 이렇게: "~로 되어 있어서"는 한도라서 `is capped at` 이 정확하다. "너무 낮거나 많으면"은 뜻이 헷갈리는데, 문제는 호출이 많을 때뿐이라 `too many API calls` 로 좁혔다. "잘 관리할 수 있게 세팅"은 `be configured to stay within those limits` 로 목적을 동사구에 담는다.

### 카드 22 — 다른 harness 에서도 안정적인 거지?   (내가 쓴 한글)
- 내가 쓴 한글: "이거는 내가 다른 harness에서 역시 my-local-provider를 운영한다고 볼 떄 충분히 안정적인거지?"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Is this stable enough, given that I also run `my-local-provider` from other harnesses?
- 왜 이렇게: "~라고 볼 때"는 전제를 까는 말이라 `given that` 이 정확하다. "충분히 안정적"은 `stable enough` 로 `enough` 를 형용사 뒤에 둔다. `enough stable` 은 틀린 어순이다.

### 카드 23 — 야간 무인만은 아니야   (내가 쓴 한글)
- 내가 쓴 한글: "무인 야간 실행은 꼭 아니야. 업무 시간에도 자주쓰기때문에" / "야간에 무인으로 돌릴 때는 one shot prompt로 진행하고 계속 한시간마다 prompt를 실행하도록 windows task scheduler를 사용 중이긴 해."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: It's not only for unattended overnight runs — I use it a lot during work hours too. / For unattended overnight runs, I do use a one-shot prompt, with Windows Task Scheduler re-running it every hour.
- 왜 이렇게: "꼭 ~은 아니야"는 `not necessarily` 나 `not only for` 로 부분 부정을 만든다. "때문에"로 끝난 조각은 대시로 앞 문장에 붙인다. "사용 중이긴 해"의 "~긴 해"는 양보의 뉘앙스라 강조 조동사 `I do use` 로 살린다.

### 카드 24 — 어디서부터 하면 될까 / 7번까지 통과   (내가 쓴 한글)
- 내가 쓴 한글: "office-setup 어디서부터 진행하면 될까" / "배선 전부 실제 작업으로 확인됨. 프롬프트 7까지 통과함"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Where should I start in `office-setup`? / All the wiring is confirmed on real tasks. Prompts 1 through 7 passed.
- 왜 이렇게: "어디서부터 진행하면 될까"는 `Where should I start?` 면 충분하다. "확인됨·통과함" 같은 보고 종결은 영어에서 수동 `is confirmed` 와 과거형 `passed` 로 나눈다. "7까지"는 `up to 7` 도 되지만 `1 through 7` 이 범위를 분명히 한다.

### 카드 25 — 반쯤 하고 멈추는 게 낫다   (고급 한글 · 번역)
- 한글 원문: "나는 자리에 없다. 물어볼 사람이 없으니, 승인받지 않은 결정이 필요해지면 추측해서 진행하지 말고 멈추고 기록해라. 절반만 한 채 멈추는 것이 틀린 방향으로 끝까지 가는 것보다 낫다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: I'm not at my desk, and there's no one to ask. If you hit a decision that hasn't been approved, don't guess and carry on — stop and write it down. Stopping halfway is better than going all the way in the wrong direction.
- 번역 포인트: "자리에 없다"는 `I'm away` 나 `I'm not at my desk`. "추측해서 진행하지 말고"는 동사 두 개(`guess and carry on`)를 한 덩어리로 부정한다. 마지막 문장은 동명사 주어 둘(`Stopping halfway`, `going all the way`)을 맞세워 대구를 살리는 게 핵심이다. `halfway` 와 `all the way` 가 짝을 이룬다.

### 카드 26 — 되돌리기를 위한 장치가 되돌리기를 망쳤다   (고급 한글 · 번역)
- 한글 원문: "되돌리기를 쉽게 하려고 넣은 장치가 오히려 되돌리기를 망가뜨리는 구조였습니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: The very mechanism I added to make reverts easy was what broke them.
- 번역 포인트: "오히려"는 `rather` 로 옮기기보다 `The very …` 로 아이러니를 살리는 편이 영어답다. "~하는 구조였습니다"의 "구조"는 옮기지 않는다. 같은 단어 "되돌리기"를 두 번 쓴 한국어의 반복은 `reverts … them` 으로 대명사가 받는다.

### 카드 27 — 느린 비용 < 놓친 비용   (고급 한글 · 번역)
- 한글 원문: "scout은 전체 작업의 한 단계일 뿐이고 물량은 worker가 집니다. 정찰 한 번 느린 비용 < 정찰 한 번 놓친 비용."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: The scout is only one step in the job; the workers carry the volume. A slow scouting pass costs less than a scouting pass that misses something.
- 번역 포인트: "물량은 worker가 집니다"의 "지다"는 짐을 지는 은유라 `carry the volume` 이나 `do the heavy lifting` 이 대응한다. 부등호 표어는 영어로 `costs less than` 문장으로 풀되 `slow` 와 `misses something` 을 대칭으로 둔다. 표어 느낌을 살리려면 `Slow beats blind.` 처럼 줄여도 된다(작성).

### 카드 28 — 착시를 만든 건 내 출력이었다   (고급 한글 · 번역)
- 한글 원문: "이상한 게 아니라 제 출력이 오해를 만들었습니다. Medium은 통과한 게 아니라 검사조차 안 됐습니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: It's not strange — my output was misleading. Medium didn't pass; it was never checked at all.
- 번역 포인트: "A가 아니라 B"를 두 번 쓴 구조는 영어에서 대시와 세미콜론으로 나누면 리듬이 산다. "오해를 만들었다"를 `created a misunderstanding` 으로 직역하기보다 형용사 `misleading` 하나로 줄인다. "~조차"는 `at all` 이나 `never` 가 받는다.

## 영어 다듬기

### 카드 1 — graphify 를 쓸 수 있을까
- 내가 쓴 영어: "do you think can we utilize graphify to understand the tools file structure?? Here is the git codebase."   (출처: transcript:[user] equipment-data-map)
- 정정: `do you think can we` → `do you think we can`. `do you think` 뒤의 간접 의문문은 평서 어순이다. `the tools file structure` → `the tool's file structure` (소유격 아포스트로피).
- 더 나은 표현: Do you think we could use graphify to understand the tool's file structure? Here's the repo.
- 왜: `utilize` 는 `use` 로 충분하고 더 자연스럽다. `could` 가 가능성을 묻는 말투를 부드럽게 한다. `git codebase` 보다 `repo` 가 흔한 말이다.

### 카드 2 — 태그가 있으면 좋겠다
- 내가 쓴 영어: "that's good to have the extracted/inferred evidence tag."   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: It'd be good to have the extracted/inferred evidence tag.
- 왜: `that's good to have` 는 틀리진 않지만 `that` 이 무엇을 가리키는지 흐리다. 가주어 `It'd be good to have …` 가 "있으면 좋겠다"는 바람을 정확히 전한다.

### 카드 3 — Linux 기반이라 sh 파일이 많다
- 내가 쓴 영어: "also the tools that I am looking for is running based on Linux so that I can see many sh files. do you think is it worth of using graphify based on the file extensions?"   (출처: transcript:[user] equipment-data-map)
- 정정: `the tools … is` → `the tool … runs` (주어와 동사 수 일치). `so that` → `so` (`so that` 은 목적, 결과는 `so`). `is it worth of using` → `it's worth using` (`worth` 뒤엔 `of` 없이 동명사, 간접 의문문은 평서 어순).
- 더 나은 표현: Also, the tool I'm looking at runs on Linux, so there are a lot of `.sh` files. Given those file types, do you think graphify is worth using?
- 왜: `running based on Linux` 는 `runs on Linux` 로 줄인다. `looking for` 는 "찾는 중", `looking at` 은 "살펴보는 중"이라 뜻이 다르다. `based on the file extensions` 는 `Given those file types` 로 옮기면 이유가 앞에 선다.

### 카드 4 — 얻은 건 개념 하나뿐
- 내가 쓴 영어: "I see. we only get the concept of extracted, inferred."   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: I see — so the only thing we take away is the extracted/inferred distinction.
- 왜: `get the concept` 은 "개념을 이해하다"로도 읽혀 모호하다. `take away` 가 "건지다"에 맞다. 두 단어를 쉼표로 늘어놓기보다 `the extracted/inferred distinction` 으로 묶으면 "구분 자체"가 핵심이라는 게 드러난다.

### 카드 5 — rollout 까지 기다리자
- 내가 쓴 영어: "yes let's wait until we get the rollout."   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Yes, let's hold off until the first rollout is done.
- 왜: `get the rollout` 은 "rollout 을 받다"처럼 들린다. 기다리는 건 rollout 이 끝나는 시점이라 `until … is done`. `hold off` 는 "보류하다"는 뉘앙스를 준다.

### 카드 6 — 가짜 FTP 테스트를 빼자
- 내가 쓴 영어: "however, I suggest we skip the test of ftp server with local host (fake test) since I have been using the ftp_handler and its proxy without any problems from other projects. I am frustrated to type ftp fake info during the test before rollout"   (출처: transcript:[user] equipment-data-map)
- 정정: `without any problems from other projects` → `in other projects without any problems` (다른 프로젝트"에서" 써 왔다는 뜻이라 `in`). `I am frustrated to type` → `It's frustrating to type` 또는 `I'm tired of typing` (`be frustrated to + 동사` 는 쓰지 않는다).
- 더 나은 표현: That said, I'd like to skip the fake FTP test on localhost. I've used `ftp_handler` and its proxy in other projects without any issues, and typing fake FTP details before every rollout is frustrating.
- 왜: 문두 `however` 는 앞 흐름을 뒤집는 격식 연결어라 채팅에선 `That said` 가 부드럽다. `the test of ftp server with local host (fake test)` 는 `the fake FTP test on localhost` 로 한 번에 말한다. 두 문장을 `and` 로 이어 이유를 하나로 묶었다.

### 카드 7 — 한글이 깨져서 못 읽겠다
- 내가 쓴 영어: "lots of some Korean return. not able to read the text"   (출처: transcript:[user] pm-notes)
- 정정: `lots of some` → `lots of` (수량 한정사는 하나만). `Korean return` → `Korean output` (`return` 은 여기서 명사로 안 맞는다). 주어가 빠진 조각은 완결 문장으로.
- 더 나은 표현: A lot of the Korean output comes out garbled, so I can't read it.
- 왜: 깨진 글자는 `garbled` 나 `mojibake` 로 말한다. 증상과 결과를 `so` 로 이으면 무엇이 문제인지 한 번에 전해진다.

### 카드 8 — 무엇이 실패했는지만 알려 줘
- 내가 쓴 영어: "for L0 I just want you to tell what failed."   (출처: transcript:[user] pm-notes)
- 정정: `tell what failed` → `tell me what failed`. `tell` 은 듣는 사람 목적어가 필요하다(`say what failed` 는 목적어 없이 가능).
- 더 나은 표현: For L0, just tell me what failed.
- 왜: `I just want you to` 를 빼고 명령문으로 줄여도 무례하지 않다. `just` 가 "그것만"이라는 범위를 잡아 준다.

### 카드 9 — JSON 설명을 영어로
- 내가 쓴 영어: "can you use english for description in json that enable subagents?"   (출처: transcript:[user] pm-notes)
- 정정: `for description` → `for the descriptions` (셀 수 있는 명사라 관사·복수). `in json that enable` → `in the JSON that enables` (선행사 `JSON` 이 단수라 `enables`).
- 더 나은 표현: Could you write the descriptions in the subagent-config JSON in English?
- 왜: `the JSON that enables subagents` 를 `the subagent-config JSON` 으로 명사 수식으로 줄이면 관계절이 사라진다. `use English for` 보다 `write … in English` 가 더 흔하다.

### 카드 10 — md 파일로 단계별 지시해 줘
- 내가 쓴 영어: "since we have already connected models into pi in my office, you can instruct me to set things up in the office via md files. I can send the prompt step by step made from you."   (출처: transcript:[user] pm-notes)
- 정정: `connected models into pi` → `connected the models to pi` (`connect A to B`). `the prompt step by step made from you` → `the prompts you write, step by step` (`made from` 은 재료, 만든 사람은 관계절로).
- 더 나은 표현: Since the models are already connected to pi at the office, you can give me the setup steps as Markdown files, and I'll feed your prompts in one step at a time.
- 왜: `instruct me to set things up` 보다 `give me the setup steps` 가 가볍다. `feed … in one step at a time` 이 "하나씩 넣겠다"는 역할 분담을 분명히 한다.

### 카드 11 — 병렬 작업 부분을 빼자
- 내가 쓴 영어: "@equipment-data-parser/index.md We need to get rid of parallel job content since this can be done by agent manager by itself. and for the night jot setup (while I am away), we have to set things up before the agent keeps running."   (출처: transcript:[user] equipment-data-map)
- 정정: `by agent manager` → `by the agent manager` (특정 대상이라 관사). `night jot` → `night job` (오타). `before the agent keeps running` → `before the agent starts running` (`keep` 은 계속, 시작 전이면 `start`).
- 더 나은 표현: Let's remove the parallel-jobs section from `index.md`; the agent manager handles that on its own. And for overnight runs while I'm away, everything needs to be set up before the agent starts its loop.
- 왜: `get rid of … content` 는 `remove the … section` 으로 대상을 구체적으로. `by itself` 는 `on its own` 이 더 자연스럽다. `we have to set things up` 을 수동 `everything needs to be set up` 으로 바꾸면 누가 하는지보다 "준비돼 있어야 한다"에 초점이 간다.
