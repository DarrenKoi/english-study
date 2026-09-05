# 2026-09-06 — 코칭

## 한글→영어

### 카드 1 — 설명 문서를 요청하기   (내가 쓴 한글)
- 내가 쓴 한글: "친절한 설명문 필요함. OM, SEM 네모 박스에 어떤 점을 align point로 잡는 지 cond.txt에서 !locator 인자를 받아와서 계산하는데, 어떤 식으로 진행하는 지 그림과 함께 설명해줘. md와 html로 만들어줘. html에는 visual 요소들도 같이 넣어줘."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: "I need a proper walkthrough of this. For the OM/SEM boxes, the code pulls the `!locator` argument out of `cond.txt` and works out which point becomes the align point — walk me through how that happens, with diagrams. Write it up as both markdown and HTML, and put the visuals in the HTML version."
- 왜 이렇게: "친절한 설명문" 을 kind explanation 으로 옮기면 사람의 태도를 요구하는 말이 된다. 영어는 문서의 **종류** 로 받는다 — walkthrough(단계를 따라가는 해설), explainer(개념 소개), primer(입문). "어떤 식으로 진행하는 지" 같은 간접의문문은 `how that happens` 처럼 의문사절로 통째로 목적어에 넣는다. "~해줘" 명령형 셋(설명해줘/만들어줘/넣어줘)은 영어에서도 명령형으로 이어 붙이되 `and` 로 묶어야 목록처럼 흩어지지 않는다.

### 카드 2 — 다른 곳에도 적용되는지 확인하기   (내가 쓴 한글)
- 내가 쓴 한글: "이 방식이 최근 업데이트한 align image 중심점 표현에도 잘 적용 된거겠지?"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: "This should carry over to the align-image centre markers I updated recently, right?"
- 왜 이렇게: "적용되다" 를 `be applied to` 로 직역하면 누가 적용했는지를 묻는 문장이 된다. 규칙이 다른 영역에서도 성립하느냐를 물을 때는 `carry over to` 나 `hold for` 를 쓴다. "~겠지?" 의 확인 뉘앙스는 문장 끝 `right?` 하나로 충분하다 — `Is it correctly applied?` 처럼 물으면 의심이 실린다.

### 카드 3 — 방침을 바꾸며 혼잣말처럼 결론 내기   (내가 쓴 한글)
- 내가 쓴 한글: "이미지 중심과 박스 중심 둘 다 표현을 해야겠네."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: "We should draw both, then — the image centre and the box centre."
- 왜 이렇게: "~해야겠네" 는 지시가 아니라 방금 깨달은 결론이다. 영어에서 그 결을 만드는 건 문장 끝의 `then` — 앞의 설명을 받아 "그렇다면" 이 된다. "표현하다" 는 시각 산출물이니 `express` 가 아니라 `draw`·`mark`·`show` 다.

### 카드 4 — 두 구성이 공존 가능한지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "opencode, pi coding agent와 같은 harness에서 qwen3.8 27b를 원활하게 운용하기 위해 stream true로 세팅을 바꾸고, flask proxy가 아닌 포트에 직접 연결해 사용을 하고 싶다. flask proxy와 동시에 이 구성이 가능한가?"   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "To run qwen3.8-27b smoothly from harnesses like opencode or the pi coding agent, I want to turn streaming on and connect straight to the port instead of going through the Flask proxy. Can that coexist with the proxy?"
- 왜 이렇게: "원활하게 운용하다" 는 `operate smoothly` 로도 되지만 서버 문맥에서는 `run` 이 더 자연스럽다. "A가 아닌 B에 직접" 은 `straight to B instead of going through A` — instead of 뒤에 `going through` 를 넣어야 프록시가 경유지였다는 그림이 산다. 마지막 질문의 핵심어는 `coexist` 다. `Is it possible at the same time?` 은 시각을 묻는 말처럼 들리고, `coexist` / `run alongside` / `run side by side` 가 "둘 다 살아 있을 수 있나" 를 정확히 담는다.

### 카드 5 — 변경 사항 세 가지를 한 번에 지시하기   (내가 쓴 한글)
- 내가 쓴 한글: "reasoning_effort를 기본 값은 medium으로 하고 싶다. HOST를 사내 IP로 변경해야 한다. (이미 cloud & flask에 VLLM으로 모델들 가동 중) API_KEY도 추가할게 (간단하게 "dummy")"   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "I'd like `reasoning_effort` to default to medium. `HOST` needs to point at our internal IP — the models are already up on cloud and Flask under vLLM. And I'll add an `API_KEY` too; keep it simple, just `dummy`."
- 왜 이렇게: "기본 값은 medium으로 하고 싶다" 에서 default 를 **동사**로 쓰면(`to default to medium`) 명사 두 개(the default value)를 쓰는 것보다 짧고 관용적이다. "사내" 는 `in-house` 보다 `internal` 이 네트워크 문맥의 기본어다. 한국어 괄호 보충 두 개는 영어에서 각각 대시와 세미콜론으로 갈라 놓는 게 읽기 좋다 — 괄호를 연달아 쓰면 문장이 각주투가 된다.

### 카드 6 — 필수 여부를 확인하고 대안을 제안하기   (내가 쓴 한글)
- 내가 쓴 한글: "VLM SERVE UPSTREAM API KEY와 TOKEN은 무조건 설정이 되어 있어야 하나? dummy가 실제 API KEY처럼 작용한다면, itc-one-stop-solution으로 바꾸고 싶다."   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "Do `VLM_SERVE_UPSTREAM_API_KEY` and `VLM_SERVE_TOKEN` both have to be set, no matter what? If `dummy` really does act as a live key, I'd rather change it to `itc-one-stop-solution`."
- 왜 이렇게: "무조건" 은 `unconditionally` 가 아니다 — 필수성을 묻는 자리에서는 `no matter what` 이나 `strictly required` 로 간다. "실제 API KEY처럼 작용한다면" 의 조건절에 `really does` 를 넣으면 "정말 그렇다면" 의 반신반의가 살아난다. 그리고 "바꾸고 싶다" 는 `I want to change` 보다 `I'd rather` 가 낫다 — 선택지 사이의 선호를 담아 지시가 아니라 상의가 된다.

### 카드 7 — 현재 상태를 알리고 다음 단계를 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "응 아직은 약한 단계로 api key를 유지했어. 이제 설정한 뒤에 qwen을 재가동해야 하나?"   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "Right — I've kept the API key at the weaker setting for now. Now that it's configured, do I need to restart qwen?"
- 왜 이렇게: "유지했어" 는 과거 한 번의 행위가 아니라 지금까지 이어지는 상태라 현재완료 `I've kept` 다. `I kept` 라고 하면 그 뒤에 바뀌었을 여지가 생긴다. "설정한 뒤에" 를 `after configuring` 으로 옮기면 시간 순서만 남는데, 여기서 묻는 건 "설정이 끝난 지금 상황에서" 라 `Now that ...` 이 조건까지 담아 정확하다.

### 카드 8 — 관리 주체를 선언하기   (내가 쓴 한글)
- 내가 쓴 한글: "이제 이 repo를 중심으로 flask server를 관리할 거야."   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "From now on, this repo is where the Flask server is managed."
- 왜 이렇게: "~를 중심으로" 를 `centered on` 으로 옮기면 물리적 배치를 말하는 문장이 된다. 영어는 이런 선언을 **장소 비유**로 처리한다 — `this repo is where X lives`, `this repo is the home for X`, `X is managed out of this repo`. 셋 다 "여기가 정본" 을 담는다.

### 카드 9 — 건드리면 안 되는 것을 못박기   (내가 쓴 한글)
- 내가 쓴 한글: "auto_recipe_creator에 서빙하는 구조는 유지해야함. 그곳에서 진행하고 있는 작업들에 3개 모델들이 사용되고 있음"   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "The serving setup for `auto_recipe_creator` has to stay as it is — three of the models are in use by work that's running over there."
- 왜 이렇게: "유지해야함" 의 명사형 종결은 메모체다. 영어에는 대응하는 축약형이 없어서 `has to stay as it is` / `must stay intact` 처럼 절로 풀어야 한다. "3개 모델들이" 의 "들" 은 한국어에서 복수 표지를 겹친 것인데, 영어는 `three of the models` 로 수가 이미 확정되니 복수 표시를 더 얹을 자리가 없다.

### 카드 10 — 한 줄로 폐기 통보하기   (내가 쓴 한글)
- 내가 쓴 한글: "mai_ui_2b 사용 안함. 폐기."   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "We're not using `mai-ui-2b` any more. Retire it."
- 왜 이렇게: "폐기" 한 단어에 대응하는 영어는 격식에 따라 셋으로 갈린다 — `decommission`(운영 자산을 절차대로 내리다, 가장 격식), `retire`(더 쓰지 않기로 하다, 중립), `drop`(그냥 뺀다, 구어). 한국어 명사 한 마디의 단호함은 영어에서 **명령형 두 단어**로 옮기는 게 가장 가깝다.

### 카드 11 — 단위를 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "reload-on-rss=400 400은 어떤 단위?"   (출처: transcript:[user] llm_serving)
- 자연스러운 영어: "`reload-on-rss=400` — what unit is the 400 in?"
- 왜 이렇게: 단위를 물을 때 영어는 전치사를 문장 끝에 남긴다(`what unit is it in?`, `measured in what?`). `What is the unit of 400?` 은 문법은 맞지만 시험 문제 같은 어투다. 설정값을 인용한 뒤 대시로 질문을 붙이는 배치도 그대로 익혀 둘 만하다.

### 카드 12 — 배타적 점유라는 개념 자체가 없다   (고급 한글 · 번역)
- 한글 원문: "클라이언트가 하나 더 붙는 건 vLLM 입장에서 아무 일도 아니다. 배타적 점유 같은 개념이 없다."   (출처: transcript:[assistant] llm_serving)
- 자연스러운 영어: "One more client attaching means nothing to vLLM. It has no notion of exclusive ownership."
- 번역 포인트: "~입장에서" 는 `from the standpoint of` 로 늘릴 필요가 없다 — 영어는 전치사 `to` 하나로 처리한다(`means nothing to vLLM`). "아무 일도 아니다" 의 대응어는 `is a non-event` 도 있는데 조금 더 구어적이다. 마지막 문장의 `has no notion of` 는 "그런 개념 자체가 없다" 를 담는 굳은 표현으로, `does not support` 와 결정적으로 다르다 — 지원 여부가 아니라 **범주의 부재**를 말한다.

### 카드 13 — 증상이 원인과 전혀 다른 자리에서 나타난다   (고급 한글 · 번역)
- 한글 원문: "즉 헤더 하나가 빠졌을 때의 증상은 '인증 오류'가 아니라 '전체 기동 실패' 다. 모델은 멀쩡히 떠 있는데 런처가 스스로 죽인다."   (출처: transcript:[assistant] llm_serving)
- 자연스러운 영어: "So the symptom of one missing header is not an auth error but a total startup failure: the model comes up fine and the launcher kills it itself."
- 번역 포인트: 문두의 "즉" 에 `In other words` 를 붙이면 문장이 무거워진다 — `So` 한 단어가 같은 일을 한다. "~가 아니라 ~다" 는 `not A but B` 로 그대로 옮겨지고, 이때 A·B 를 같은 품사·같은 길이로 맞춰야 대비가 산다(`an auth error` / `a total startup failure`). 둘째 문장의 "~는데" 역접은 영어에서 굳이 `but` 을 쓰지 않고 콜론으로 앞 문장에 매다는 편이 더 세다 — 역접이 아니라 **설명**으로 읽히면서 부조리함이 드러난다. "스스로" 는 재귀 `itself` 를 동사 뒤에 놓는다.

### 카드 14 — 값이 갈라지는 순간의 증상   (고급 한글 · 번역)
- 한글 원문: "값이 두 벌이면 언젠가 갈라지고, 갈라지는 순간의 증상이 401 이라 원인 찾기가 나쁘다."   (출처: transcript:[assistant] llm_serving)
- 자연스러운 영어: "Keep two copies of the value and they will drift apart eventually; when they do, the symptom is a 401 — a poor trail to follow back to the cause."
- 번역 포인트: 조건절 "~이면" 을 `If you keep ...` 대신 **명령형 + and** 로 옮기면(`Keep two copies and they will ...`) 조건이 아니라 예언처럼 들려 경고의 힘이 붙는다. "갈라지다" 는 `diverge` 도 되지만 `drift apart` 가 "서서히, 아무도 모르게" 를 담는다. 마지막이 번역의 고비다 — "원인 찾기가 나쁘다" 는 한국어 특유의 압축이라 영어로는 무엇이 나쁜지를 명사로 세워야 한다. `a poor trail to follow back to the cause`(원인까지 되짚어 갈 단서로는 형편없다)처럼 풀면 401 이 왜 나쁜 증상인지까지 옮겨진다.

## 영어 다듬기

### 카드 1 — 다른 저장소에서 라이브러리 가져오기
- 내가 쓴 영어: "can you copy ftp_handler from ../skewnono_v3_nuxt/ to this repo? we want to use this ftp library"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: "Could you bring `ftp_handler` over from `../skewnono_v3_nuxt/` into this repo? We want to reuse that FTP library here."
- 왜: 문법 오류는 없다. 다만 `copy A to B` 는 파일 복사 그 자체를 말하고, 저장소 사이의 이식은 `bring X over` 가 관용이다. `use` 를 `reuse` 로 바꾸면 새로 만드는 게 아니라 이미 검증된 걸 가져다 쓴다는 의도가 한 글자로 드러난다. `this ftp library` 의 this 는 아직 이 저장소에 없는 물건이라 that 이 자연스럽다.

### 카드 2 — 프록시도 쓰자고 덧붙이기
- 내가 쓴 영어: "we should use proxy as well."   (출처: transcript:[user] equipment-data-map)
- 정정: `proxy` 앞에 관사가 빠졌다 → `the proxy`. 셀 수 있는 단수 명사는 관사 없이 홀로 서지 못한다.
- 더 나은 표현: "We should wire up the proxy path too."
- 왜: `use the proxy` 는 무엇을 어디에 붙이라는 건지 비어 있다. `wire up` 이 "배선해서 실제로 동작하게 만든다" 를 담아 요청이 실행 가능한 크기가 된다. `as well` 은 문어체이고 이런 짧은 지시에는 `too` 가 가볍다.

### 카드 3 — 조건 두 개가 걸린 지시 쓰기
- 내가 쓴 영어: "and we have to update letters_to_agent/ we do not use uv but pip. And use ftp_handler to download files if it goes ftp (must use proxy handler if it is windows)"   (출처: transcript:[user] equipment-data-map)
- 정정: (1) 두 개의 절이 접속사도 구두점도 없이 붙은 run-on 이다 → `update letters_to_agent/ — we use pip there, not uv.` (2) `if it goes ftp` 는 주어 it 이 무엇인지 불명확하고, `go + 프로토콜` 이라는 용법도 없다 → `if the transfer goes over FTP`. (3) `windows` → `Windows` (고유명사).
- 더 나은 표현: "We also need to update `letters_to_agent/` — we use pip there, not uv. And have it download over FTP through `ftp_handler`, falling back to the proxy handler on Windows."
- 왜: `not A but B` 는 영어에서 무거운 구문이라 짧은 지시에는 `B, not A` 로 뒤집는다(`pip, not uv`). 조건을 if 절로 두 번 늘어놓는 대신 뒤쪽을 분사구(`falling back to ...`)로 접으면 두 문장이 하나의 규칙으로 읽힌다.

### 카드 4 — 의도된 삭제임을 밝히기
- 내가 쓴 영어: "I deleted on purpose. commit nad push all"   (출처: transcript:[user] equipment-data-map)
- 정정: (1) `delete` 는 타동사라 목적어가 있어야 한다 → `I deleted them on purpose.` (2) `nad` 는 `and` 오타.
- 더 나은 표현: "Those were deleted on purpose — commit and push everything."
- 왜: 수동태로 두면 "누가 지웠나" 보다 "의도된 삭제였다" 가 앞으로 나온다. 상대가 되돌리려 할 때 막는 게 목적이니 그 순서가 맞다. `all` 은 형용사·한정사라 목적어 자리에 홀로 서면 어색하고, 그 자리를 채우는 대명사는 `everything` 이다.

### 카드 5 — 문서에 설명을 추가해 달라고 하기
- 내가 쓴 영어: "Recently we made a md and html file to explain about align om / sem image's center. we have to add the explanation for image center and align center."   (출처: transcript:[user] auto_recipe_creator)
- 정정: (1) `a md` → `an md` — 관사는 철자가 아니라 **소리**를 따른다(md 는 /em/ 로 시작). (2) `explain about` 은 비표준이다. explain 은 타동사라 목적어를 바로 받는다 → `explain the align point`. (3) `the explanation for` → `an explanation of` (아직 존재하지 않는 설명이므로 부정관사).
- 더 나은 표현: "We recently wrote up an md and an HTML page explaining how the align point is found on OM/SEM images. We should cover image centre and align centre in there too."
- 왜: `made a file to explain` 은 뜻은 통하지만 문서 작업의 관용은 `write up`이다. `to explain` 대신 분사 `explaining` 을 쓰면 목적이 아니라 그 문서의 성격이 되어, 이미 만들어진 것을 가리키는 문장과 시제가 맞는다.

### 카드 6 — 정적 분석 지적을 일괄 수정하자고 제안하기
- 내가 쓴 영어: "can we scan to fix to meet pylance format rule?"   (출처: transcript:[user] equipment-data-map)
- 정정: to부정사 세 개가 연달아(`scan to fix to meet`) 목적 관계가 끊겼다. 또 `rule` 은 규칙 집합이므로 복수 → `Pylance's formatting rules`.
- 더 나은 표현: "Can we sweep the codebase and fix whatever Pylance flags?"
- 왜: `scan ... to meet rules` 는 사람이 규칙에 자신을 맞춘다는 뜻인데, 실제로 원한 건 "도구가 지적한 것을 고쳐라" 다. `flag` 가 정적 분석 도구의 지적을 가리키는 표준 동사라 한 단어로 의도가 맞고, `whatever ... flags` 가 "지적된 것 전부" 를 열어 둔다. `scan` 은 도구가 하는 일이고 사람이 하는 일은 `sweep` 이다.

### 카드 7 — 학습 자료를 만들어 달라고 하기
- 내가 쓴 영어: "in docs/study, I want to learn about vllm and llm openweight serving."   (출처: transcript:[user] llm_serving)
- 정정: 문법 오류는 없다. 다만 `openweight` 는 보통 `open-weight` 로 하이픈을 넣는다.
- 더 나은 표현: "Put something together in `docs/study/` — I want to get up to speed on vLLM and serving open-weight models."
- 왜: `I want to learn about X` 는 소망 진술이라 요청으로는 약하다. 앞에 명령형을 하나 두면 무엇을 해 달라는지가 분명해지고, 뒤의 문장은 그 이유가 된다. `get up to speed on` 은 "교양으로 안다" 가 아니라 "실무에 쓸 만큼 따라잡는다" 를 담아 자료의 수준까지 지정해 준다.
