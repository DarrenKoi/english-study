# 2026-09-11 — 새 표현

## "Two things stand in the way."
- 레지스터: professional, conversational
- 출처: transcript:llm-serving (assistant)
- 맥락: 막힌 원인을 두세 개로 정리해 알릴 때. 회의·리뷰·이슈 코멘트에서 두루 쓰고, 격식은 중간.
- 한국어: 걸림돌이 두 가지 있다.
- 설명: `stand in the way (of X)` 는 "X 를 가로막고 서 있다". 사람이 주어면 "훼방 놓다"까지 가지만, 사물·조건이 주어면 담담한 진단이 된다. 숫자를 앞세워 `Two things stand in the way.` 로 끊고 각각을 소제목으로 펼치는 게 기술 글의 전형이다.
- 예문: The model is running fine, but two things stand in the way of reaching it from outside.
- 유사어: block X (직접적·짧다), get in the way (구어, 사소한 방해), be a blocker (팀 용어, 티켓·스탠드업에서), prevent X (격식·문어)
- 반의어: clear the way (걸림돌을 치우다), unblock X

## "Then the diagnosis stands."
- 레지스터: professional, technical
- 출처: transcript:llm-serving (assistant)
- 맥락: 상대가 사실 하나를 정정했는데도 앞선 진단이 그대로 유효할 때. 차분하게 결론을 붙잡는 말.
- 한국어: 그럼 진단은 그대로다.
- 설명: `stand` 를 자동사로 써서 "유효한 채로 남아 있다"는 뜻. 계약·규칙·제안·기록에도 붙는다 — `the offer stands`, `the record stands`. 오타를 정정받은 뒤 `Then …` 으로 받는 흐름이 자연스럽다.
- 예문: You meant 8006, not 6008 — then the diagnosis stands: code-server's login page is swallowing the request.
- 유사어: still holds (조금 더 구어), remains valid (격식·문어), doesn't change anything
- 반의어: that changes things, the diagnosis falls apart

## "The proxy path is the right call."
- 레지스터: professional, conversational
- 출처: transcript:llm-serving (assistant)
- 맥락: 상대가 이미 내린 선택을 지지해줄 때. 평가가 아니라 동의로 읽히는 게 장점이다.
- 한국어: 프록시 경로로 가는 게 맞는 판단이다.
- 설명: `call` 이 명사로 "판정·결정"이다(심판이 내리는 call 에서 왔다). `the right call` / `a tough call` / `your call` 로 묶어 외우면 쓸 자리가 넓어진다. `the right decision` 보다 덜 무겁고 구어에 가깝다.
- 예문: Given the firewall, sticking with the proxy is the right call.
- 유사어: the right move (조금 더 캐주얼), the sensible choice (격식), you made the right decision (문어·정중)
- 반의어: the wrong call, a misstep

## "Stick with the Flask proxy path already in your opencode config."
- 레지스터: conversational, professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 여러 대안을 검토한 끝에 "지금 쓰는 걸 계속 쓰자"고 권할 때. 구어체지만 업무 문서에도 흔하다.
- 한국어: 이미 설정에 있는 Flask 프록시 경로를 그대로 쓰자.
- 설명: `stick with X` 는 바꾸지 않고 유지한다는 뜻. `stick to X` 는 규칙·계획을 어기지 않고 지킨다는 쪽이라 결이 다르다 — `stick to the plan` 은 이탈 금지, `stick with the plan` 은 갈아타지 않기.
- 예문: All three routes failed, so I'll stick with the method that already works.
- 유사어: go with X (새로 고를 때), keep using X (밋밋·중립), stay on X (버전·브랜치에 잘 붙는다)
- 반의어: switch to X, move off X

## "Long thinking runs get cut off."
- 레지스터: technical, conversational
- 출처: transcript:llm-serving (assistant)
- 맥락: 타임아웃·버퍼 때문에 응답이 끝까지 안 온다고 설명할 때.
- 한국어: 오래 생각하는 요청은 중간에 잘린다.
- 설명: `cut off` 는 수동으로 써서 "말·전송이 끊기다". 전화·화상회의에서도 그대로 쓴다(`Sorry, you got cut off`). 여기서 `get + 과거분사` 는 be 수동보다 사고·사건의 뉘앙스가 강하다.
- 예문: The 300-second read timeout means anything that thinks for longer gets cut off mid-answer.
- 유사어: get truncated (문어·기술), time out (원인을 지목), drop (연결이 끊길 때)
- 반의어: run to completion, come through in full

## "Ways forward, in order of how well they fit this stack."
- 레지스터: professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 선택지를 나열하기 직전 한 줄. 무슨 기준으로 줄을 세웠는지 미리 밝혀 독자의 판단을 돕는다.
- 한국어: 앞으로의 선택지, 이 스택에 맞는 순서대로.
- 설명: `in order of X` 는 정렬 기준을 밝히는 전치사구다(`in order of priority`, `in order of cost`). 기준이 한 단어로 안 잡히면 여기처럼 `how well they fit …` 같은 간접의문절을 통째로 넣는다.
- 예문: I listed three options in order of how much work each one needs from the platform team.
- 유사어: ranked by X (더 딱딱·데이터적), best first (짧고 구어), in descending order of X (격식·수치)

## "One catch: the slug is qwen3.8-27b, not 26b."
- 레지스터: conversational, professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 좋은 소식 뒤에 작은 함정 하나를 덧붙일 때. 메일·슬랙·PR 설명에서 흔하다.
- 한국어: 한 가지 함정: 슬러그가 26b 가 아니라 27b 다.
- 설명: `catch` 는 "겉보기엔 좋은데 숨어 있는 조건". `What's the catch?` 는 "뭐가 문제인데?"라는 반문이다. `One catch:` 로 콜론을 찍고 문장을 이어붙이면 경고 무게를 딱 한 단계만 올릴 수 있다.
- 예문: The proxy route works from anywhere — one catch, it uses the team token, not the vLLM key.
- 유사어: one gotcha (더 캐주얼·개발자 은어), one caveat (격식·문어), the fine print is …
- 반의어: no strings attached

## "Run these from your laptop in order and stop at the first one that fails."
- 레지스터: technical, professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 단계별 진단 절차를 넘길 때. 상대가 전부 실행하고 로그를 통째로 보내는 사태를 막는다.
- 한국어: 노트북에서 순서대로 돌리고, 처음 실패하는 데서 멈춰라.
- 설명: `stop at the first one that fails` 에서 `one` 은 앞의 `these` 를 받는 대명사다. 관계절 `that fails` 가 `the first one` 을 좁혀 "실패하는 것들 중 첫 번째"를 만든다. 명령문 두 개를 `and` 로 잇는 이 형태가 절차 안내의 기본형이다.
- 예문: Work down the list and stop at the first check that fails — that is where the break is.
- 유사어: bail out at the first failure (기술·구어), stop as soon as one errors
- 반의어: run all of them regardless, run to completion

## "Skipped, needs your call."
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: 작업 보고 맨 끝에서 "여기부터는 내가 못 정한다"를 짧게 넘길 때.
- 한국어: 건너뜀 — 판단은 네 몫이다.
- 설명: `your call` 은 `the right call` 과 같은 뿌리다. 주어·조동사를 다 지운 전보체(`Skipped, needs your call.`)라 보고서 불릿·체크리스트 끝에 잘 붙고, 문장으로 풀면 `I skipped this because it needs your decision.`
- 예문: I left the eager fetch out — it's your call whether reviewers open the panel often enough to justify it.
- 유사어: up to you (구어·따뜻함), at your discretion (격식·문어), I'll defer to you on this
- 반의어: I went ahead and decided, I took the liberty of …

## "Dead flexibility."
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (simplification reviewer)
- 맥락: 코드 리뷰에서 "쓰지도 않는 확장 여지"를 지적할 때. 한 단어로 근거까지 실어 나른다.
- 한국어: 죽은 유연성 — 아무도 안 쓰는 확장 포인트.
- 설명: `dead` 를 붙여 "존재하지만 도달하지 않는" 것을 가리키는 계열이다 — `dead code`, `dead link`, `dead letter`. 매개변수를 열어뒀는데 호출부가 전부 기본값이면 그게 dead flexibility 다.
- 예문: The `source` parameter has one caller that never passes it — dead flexibility, hard-code it.
- 유사어: speculative generality (리팩터링 교과서 용어·격식), YAGNI (약어·구어), unused extension point
- 반의어: a hook that earns its keep, load-bearing abstraction

## "That is commit-message material sitting in the code forever."
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (simplification reviewer)
- 맥락: 주석에 변경 이력을 적어둔 걸 지적할 때. "틀렸다"가 아니라 "자리가 틀렸다"고 말하는 방식.
- 한국어: 그건 커밋 메시지에 들어갈 내용이 코드에 영원히 눌러앉은 것이다.
- 설명: `X material` 은 "X 감·X 거리"다 — `management material`, `front-page material`. 뒤의 현재분사 `sitting in the code forever` 가 명사를 뒤에서 꾸며, 관계절(`which sits …`)보다 가볍게 붙는다.
- 예문: The changelog line in that docstring is commit-message material; move it to the commit body.
- 유사어: belongs in the commit, that's history, not documentation
- 반의어: that earns its place in the code
