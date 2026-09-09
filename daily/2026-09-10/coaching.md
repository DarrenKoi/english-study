# 2026-09-10 — 코칭

## 한글→영어

### 카드 1 — 축소해도 읽히는 그림   (내가 쓴 한글)
- 내가 쓴 한글: "before / after workflow를 좀 더 단순하게 시각화를 해야할 듯. 이미지를 축소해도 내용을 이해할 수 있어야 함"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The before/after workflow needs a simpler visual — it has to stay readable when the image is scaled down.
- 왜 이렇게: "~해야할 듯" 은 확신을 낮춘 지시라 `needs` 정도가 딱 맞는다. `should probably be` 도 되지만 문서 리뷰에서는 명사 주어 + `needs` 가 더 담백하다. 두 번째 문장의 "내용을 이해할 수 있어야 함" 을 `you have to be able to understand it` 로 직역하면 주어가 늘어진다. 그림을 주어로 세우고 `stay readable` 로 옮기면 조건(축소)과 결과(가독)가 한 눈에 붙는다. `even at a smaller size` 로 바꿔도 자연스럽다.

### 카드 2 — 심사위원 눈높이   (내가 쓴 한글)
- 내가 쓴 한글: "채점자들은 rank-1, in_topk 이런 의미를 모름. 좀 더 풀어서 간단하게 설명."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The judges won't know what rank-1 or in_topk mean — spell them out in plain language.
- 왜 이렇게: "모름" 을 `don't know` 로 쓰면 지금 상태만 말하지만, `won't know` 는 "앞으로 읽을 때도 모를 것" 이라는 예측이라 요구의 근거가 된다. "풀어서 설명" 은 `explain in detail` 이 아니다 — 자세히가 아니라 **전문용어를 걷어내라**는 뜻이니 `spell out` + `in plain language` 가 정확하다. 유의어로 `unpack the terms`, 더 격식은 `define them for a non-specialist reader`.

### 카드 3 — 안 되던 걸 바꿔서 끌어올림   (내가 쓴 한글)
- 내가 쓴 한글: "기존 단순 비교로 안되어서 consensus 도입 (최근 성공 사례 취합)해서 성공률을 극적으로 끌어올림."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Plain image matching wasn't good enough, so we switched to a consensus of recent successful alignments — and that's what pushed the success rate up sharply.
- 왜 이렇게: "안되어서" 를 `didn't work` 로 옮기면 아예 작동 불능처럼 들린다. 실제로는 성능이 모자랐던 것이니 `wasn't good enough` 가 사실에 맞다. "도입" 은 `introduce` 보다 `switch to` 가 대체를 분명히 한다. "극적으로 끌어올림" 은 `dramatically` 를 바로 붙이는 대신 `that's what pushed ... up sharply` 로 원인을 앞세우면 자화자찬 톤이 빠지고 인과가 남는다.

### 카드 4 — 그림 말고 진짜 도형으로   (내가 쓴 한글)
- 내가 쓴 한글: "ppt에 그림을 박지 말고 진짜로 ppt 도형을 이용해서 만들어줘"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Don't drop a flat image into the deck — build it out of real PowerPoint shapes.
- 왜 이렇게: "박지 말고" 의 거칠고 단호한 어감은 `paste` 보다 `drop ... into` 가 살린다. "진짜로" 는 부사가 아니라 형용사 자리로 옮겨 `real shapes` 로 붙이는 게 영어다운 처리다. `flat` 을 앞에 얹으면 "편집이 안 되는 납작한 이미지" 라는 불만까지 한 단어에 담긴다. `native shapes`, `editable shapes` 도 같은 자리에 쓴다.

### 카드 5 — 용어 통일   (내가 쓴 한글)
- 내가 쓴 한글: "나머지 "사람" 표현도 현업 담당자로 통일해줘" / "웨이퍼 -> Wafer 로 표현 일괄"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Standardize the remaining instances of "사람" to "현업 담당자", and use "Wafer" consistently throughout.
- 왜 이렇게: "통일해줘" 는 `unify` 가 아니다 — 영어에서 `unify` 는 조직·이론을 합치는 말이라 표기 규칙에는 안 맞는다. 문서 표기는 `standardize on X`, 또는 `normalize`. "일괄" 은 `at once` 로 직역할 필요 없이 `throughout` 하나로 범위가 해결된다. 실제 편집 요청에서는 `replace every remaining "사람" with "현업 담당자"` 처럼 동사를 더 구체화해도 좋다.

### 카드 6 — 너무 잘게 쪼개짐   (내가 쓴 한글)
- 내가 쓴 한글: "1~4까지 너무 세분화가 되어있어."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Sections 1 through 4 are broken up too finely.
- 왜 이렇게: "세분화되어 있다" 는 상태를 말하는 수동이니 영어도 `are broken up` 수동이 맞다. 다만 `subdivided` 는 부동산·행정 냄새가 나서 문서 구조에는 `broken up` / `chopped up` 이 자연스럽다. `too finely` 처럼 정도부사를 뒤에 붙이는 게 핵심 — `too much detail` 로 쓰면 "내용이 많다" 로 오해된다. 여기서 문제는 양이 아니라 **분할의 잘기**다.

### 카드 7 — 정정 후 재계산   (내가 쓴 한글)
- 내가 쓴 한글: "미안 건당 4분 회수 (5분 -> 1분 대응)"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Sorry — it's 4 minutes saved per case, not 5 (5 minutes down to 1).
- 왜 이렇게: 스스로 고칠 때 영어는 `X, not Y` 로 틀린 값을 명시적으로 지운다. 그냥 새 숫자만 말하면 상대가 앞 숫자를 어떻게 처리할지 모른다. "회수" 는 시간 맥락에서 `recovered` 보다 `saved` 가 흔하고, 장비 가동 시간을 되찾는다는 뜻을 살리려면 `4 minutes of equipment time recovered per case` 로 대상을 밝힌다.

### 카드 8 — 기간 서술 간소화   (내가 쓴 한글)
- 내가 쓴 한글: "2.4 소요 기간은 필요 없음. 간단하게 2월부터 진행했고 7.5개월 소요 표현."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Drop §2.4 — just say the work started in February and ran about 7.5 months.
- 왜 이렇게: "필요 없음" 은 `is not necessary` 보다 명령형 `Drop` 이 편집 지시로 훨씬 자연스럽다. "간단하게 ... 표현" 은 `express simply` 가 아니라 `just say` — `just` 하나가 "그 이상 쓰지 마라" 는 상한을 만든다. 기간에는 `took` 도 되지만 `ran about 7.5 months` 가 프로젝트가 흘러간 느낌을 준다.

### 카드 9 — 축이 잡혀 있었다   (고급 한글 · 번역)
- 한글 원문: "같은 날 바로 `test/vlm_input_control` 모듈이 들어온 걸 보면 시작부터 "VLM으로 화면 보고 마우스/키보드 조작" 이 축이 잡혀 있었다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The fact that `test/vlm_input_control` landed the same day tells you the core idea — a VLM reading the screen and driving the mouse and keyboard — was fixed from day one.
- 번역 포인트: "~걸 보면" 은 근거→추론의 한국어 특유 연결이다. `If you look at ...` 로 직역하면 조건절이 되어 힘이 빠지니, 증거를 주어로 세우고 `tells you` 로 받는 게 영어의 자연스러운 방향이다. "축이 잡혀 있었다" 는 은유 그대로 `axis` 를 쓰면 통하지 않는다 — 뜻은 "방향이 이미 정해져 있었다" 이므로 `the core idea was fixed` 또는 `the direction was set`. "시작부터" 는 `from the start` 도 되지만 첫 커밋이라는 구체성이 있으니 `from day one` 이 낫다.

### 카드 10 — 그 여파로   (고급 한글 · 번역)
- 한글 원문: "페이지 4 아래가 그림 2 가 안 들어가 비어 있고 그 여파로 §2 가 3장이 됩니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Figure 2 doesn't fit, so the bottom of page 4 is left empty — and that spillover pushes §2 onto a third page.
- 번역 포인트: "그 여파로" 를 `as a result` 로 쓰면 정확하지만 밋밋하다. 인쇄 레이아웃에서 밀려난다는 물리적 그림이 있으니 `spillover` + `pushes ... onto` 가 원문의 연쇄 감각을 살린다. 한국어는 "안 들어가 비어 있고" 처럼 원인·결과를 `-고` 로 평평하게 잇지만, 영어는 `so` 와 대시로 층을 만들어 어느 쪽이 원인인지 표시해야 한다.

### 카드 11 — 단일 원본   (고급 한글 · 번역)
- 한글 원문: "SVG 가 단일 원본이라 md/HTML 용 PNG 와 PPT 가 항상 같은 모양이 됩니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Because the SVG is the single source of truth, the PNGs for md/HTML and the PPT can never drift apart.
- 번역 포인트: "단일 원본" 의 업계 정착 표현이 `single source of truth` 다. `single original` 은 통하지 않는다. "항상 같은 모양이 됩니다" 를 `always look the same` 으로 옮겨도 맞지만, 긍정을 부정으로 뒤집어 `can never drift apart` 로 쓰면 이 설계가 막아 주는 **실패**(따로 놀기)가 드러나 설득력이 올라간다. 한국어 원인절 "~라" 를 문장 앞 `Because` 로 올린 것도 의도적이다 — 근거를 먼저 깔아야 결론이 무게를 받는다.

## 영어 다듬기

### 카드 12 — 표에 행 번호 붙이기
- 내가 쓴 영어: "in 장비 상태 pages, we need to add numbering for each row. (When we have many tools in the table, we are not sure where we are at)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in 장비 상태 pages` → `on the 장비 상태 pages`. 웹 페이지 위에 놓인 요소는 `on a page` 가 관용이고, 특정 페이지들을 가리키므로 관사 `the` 가 필요하다. `where we are at` 의 끝 `at` 은 중복 전치사라 격식체에서 걷어낸다 (`where we are` 로 충분).
- 더 나은 표현: On the 장비 상태 pages, each row needs a number — with a long tool list it's easy to lose track of where you are.
- 왜: `we need to add numbering for each row` 는 요청자가 주어라 지시가 앞에 서지만, `each row needs a number` 로 뒤집으면 **화면이 무엇을 필요로 하는지**가 보인다. 이슈·티켓에 그대로 옮길 수 있는 형태다. 괄호 안 이유는 괄호에 가두지 말고 대시로 이어 붙이는 게 낫다 — 요구의 근거는 요구만큼 중요하다. `we are not sure where we are at` 대신 `it's easy to lose track of where you are` 를 쓰면 특정 개인의 혼란이 아니라 UI 의 성질로 일반화된다.

### 카드 13 — PID 경고 문의
- 내가 쓴 영어: "can I just start start_all once the qwen3 model is uploaded in the cloud? should I kill all before start_all? I see warning like Kiiping PID file because some process are still alive (qwen3.8-27b.pid) no problem?"   (출처: transcript:[user] llm-serving)
- 정정: `uploaded in the cloud` → `uploaded to the cloud` (이동의 도착점은 `to`). `I see warning like` → `I see a warning saying` (가산명사 관사 + 인용에는 `saying`). `some process are still alive` → `some processes are still alive` (주어 복수 일치). `no problem?` → `is that a problem?` (명사구를 의문문으로 쓰면 되묻는 어투가 된다).
- 더 나은 표현: Once the Qwen3 model finishes uploading to the cloud, can I just run `start_all`, or do I need to stop everything first? It warns "Keeping PID file because some processes are still alive" (`qwen3.8-27b.pid`) — is that safe to ignore?
- 왜: 세 개의 물음표를 두 문장으로 줄이면 상대가 답을 구조화하기 쉽다. 앞의 두 질문은 실은 하나의 선택지라 `or` 로 묶는 게 자연스럽다. `kill all` 은 정확하지만 거칠어서 문서화된 절차를 물을 때는 `stop everything` 이 낫다. 마지막은 `no problem?` 처럼 안심을 구하는 대신 `is that safe to ignore?` 로 물으면 판단 기준을 함께 요구하게 된다.

### 카드 14 — 설정 파일 필요성 질문
- 내가 쓴 영어: "@deploy_vlms/config/common.env is necessary? since we use each model give different settings"   (출처: transcript:[user] llm-serving)
- 정정: `is necessary?` → `Is common.env still necessary?` (영어 의문문은 조동사·be 동사를 앞으로 보내야 한다). `we use each model give different settings` 는 동사가 둘(`use`, `give`)이라 문장이 성립하지 않는다 → `each model has its own settings`.
- 더 나은 표현: Is `common.env` still pulling its weight? Every model already overrides those values in its own `.env`.
- 왜: `still` 한 단어가 "예전엔 필요했겠지만 지금은?" 이라는 시간 축을 넣어 질문을 훨씬 정확하게 만든다. 이유를 `since` 종속절로 붙이면 반쯤 삼킨 근거가 되는데, 독립된 두 번째 문장으로 세우면 상대가 그 사실 자체를 검증하게 된다. `pulling its weight` 는 오늘 표현 카드의 `earn its place` 와 짝이다 — 둘 다 "존재값을 증명하라" 는 뜻으로 구어에서 자주 쓴다.

### 카드 15 — 최적화 지시
- 내가 쓴 영어: "optimize the qwen3.8 model for the H200 setting. 16bit used with 52GB sized model. if no more, just leave it there. check flask port too."   (출처: transcript:[user] llm-serving)
- 정정: `16bit used with 52GB sized model` 은 동사 없는 조각 → `it runs in 16-bit and the weights are about 52GB`. `52GB sized model` 처럼 명사를 겹치기보다 `a 52GB model` 로 줄인다. `if no more` 는 목적어가 없어 뜻이 열려 있다 → `if there's nothing left to tune`.
- 더 나은 표현: Tune the Qwen3.8 config for a solo H200 — it runs BF16 with roughly 52GB of weights. If there's nothing left to gain, leave it as is. Check the Flask port while you're in there.
- 왜: `optimize` 는 목표가 없으면 공허하다. `for a solo H200` 처럼 제약을 붙이면 지시가 검증 가능해진다. `just leave it there` 는 장소를 말하는 것처럼 들리니 `leave it as is`(현상 유지) 가 맞다. 마지막 `too` 를 `while you're in there` 로 바꾸면 "이미 그 파일을 열 테니 겸사겸사" 라는 맥락까지 전달된다.

### 카드 16 — 저장소 공개 요청
- 내가 쓴 영어: "make it public in the github"   (출처: transcript:[user] equipment-data-map)
- 정정: `in the github` → `on GitHub`. 플랫폼 위에서는 `on` 을 쓰고, GitHub 은 고유명사라 관사가 붙지 않는다.
- 더 나은 표현: Let's make this repo public on GitHub — scan it for anything that shouldn't ship first.
- 왜: 문법만 고치면 요청은 통하지만 위험한 작업을 무조건으로 던지게 된다. `Let's` 로 톤을 낮추고 안전 조건을 붙이면 되돌리기 어려운 작업에 게이트가 생긴다. `shouldn't ship` 은 "밖에 나가면 안 되는 것" 을 뭉뚱그려 가리키는 실무 표현으로, 비밀키·내부 호스트명을 일일이 열거하지 않아도 된다.

### 카드 17 — 프로젝트 시작 시점 질문
- 내가 쓴 영어: "when we started this project?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 의문사 의문문은 조동사가 주어 앞에 와야 한다 → `When did we start this project?`. 원문은 간접의문문(`I wonder when we started ...`)의 어순이 그대로 새어 나온 형태다.
- 더 나은 표현: When did this project actually start? First commit, not first meeting.
- 왜: `actually` 를 넣으면 "기억 말고 기록으로 확인해 달라" 는 뜻이 실린다. 두 번째 조각은 기준을 못 박는 장치 — 완전한 문장이 아니어도 영어에서 이런 짧은 명사구 단서는 자연스럽고, 답이 엉뚱한 날짜로 오는 것을 막는다.

### 카드 18 — 오래된 내용 정리
- 내가 쓴 영어: "remove contents that I am not interested anymore."   (출처: transcript:[user] pm-notes)
- 정정: `interested` 는 전치사 `in` 을 요구한다 → `that I'm not interested in anymore`. `contents` 는 "목차·내용물 목록" 쪽이라 여기서는 불가산 `content` 또는 `entries`·`sections` 가 맞다.
- 더 나은 표현: Prune the entries I no longer care about.
- 왜: `remove` 는 중립적 삭제지만 `prune` 은 "쓸모없는 가지만 골라 친다" 는 선별의 뉘앙스라 노트 정리에 정확하다. `not ... anymore` 보다 `no longer` 가 한 단계 격식이 높고 문장도 짧아진다. `care about` 은 `be interested in` 보다 구어에서 자연스럽고 전치사 실수도 줄여 준다.
