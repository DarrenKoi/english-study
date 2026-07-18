# 2026-07-19 — 코칭

## 한글→영어

### 카드 1 — 파이프라인이 원래 이렇게 오래 걸리나 (내가 쓴 한글)
- 내가 쓴 한글: "pipeline이 계속 돌고 있는데 원래 이렇게 오래걸리나?" (출처: transcript:[user] english-study 세션)
- 자연스러운 영어: The pipeline is still running — is it normal for it to take this long?
- 왜 이렇게: "계속 돌고 있는데"는 진행형(is still running)으로, "원래 ~하나?"는 "is it normal for X to …?" 구문이 딱 맞는다. 더 구어체로는 "Does it usually take this long?"도 좋다. 대시(—)로 상황 제시와 질문을 잇는 게 and보다 자연스럽다.

### 카드 2 — 세 가지 문제가 모두 닫혔다 (고급 한글 · 번역)
- 한글 원문: "이로써 처음 문제 제기했던 세 가지가 모두 닫혔습니다: 문서의 예산 독점, 트랜스크립트 기아, 코칭 원료 부재로 인한 coaching.md 결락. 내일 새벽 자동 실행부터는 별도 조치 없이 이 구조로 돌아갑니다." (출처: transcript:[assistant] english-study 세션)
- 자연스러운 영어: That closes out all three issues originally raised: the docs monopolizing the budget, transcript starvation, and the missing coaching.md for lack of raw material. Starting with tomorrow's overnight run, everything works this way with no further action needed.
- 번역 포인트: "닫혔습니다"는 이슈 트래커 관용어 close out을 쓰면 정확하다. "~로 인한 결락"은 "the missing X for lack of Y"로 명사구 안에 원인을 눌러 담는다. "별도 조치 없이"는 with no further action needed — required보다 needed가 부드럽다.

### 카드 3 — 프로세스는 살아 있고 (고급 한글 · 번역)
- 한글 원문: "프로세스는 살아 있고(CPU 소비 중) 산출물 쓰기 단계 전입니다 — 파일들이 아직 새벽 버전 그대로인 걸 보면 지금 배치를 읽고 추출하는 중입니다." (출처: transcript:[assistant] english-study 세션)
- 자연스러운 영어: The process is alive (still burning CPU) and hasn't reached the write phase yet — judging by the files still being the overnight versions, it's currently reading and extracting from the batch.
- 번역 포인트: "~인 걸 보면"은 judging by가 정석. "단계 전입니다"를 hasn't reached … yet으로 옮기면 진행 방향까지 담긴다. CPU 소비 중은 burning/consuming CPU 둘 다 되지만 burning이 더 살아 있는 어감.

### 카드 4 — 지금 밀도가 적당하다 (고급 한글 · 번역)
- 한글 원문: "백로그를 더 빨리 소화하고 싶으면 char_budget을 올리는 방법이 있지만, 하루 학습량으로는 지금 밀도가 적당해 보입니다." (출처: transcript:[assistant] english-study 세션)
- 자연스러운 영어: If you want to work through the backlog faster, raising char_budget is an option — but as a daily study load, the current density feels about right.
- 번역 포인트: "소화하다"는 digest보다 work through(차근차근 처리하다)가 업무 맥락에 맞는다. "~하는 방법이 있다"는 "X is an option"으로 담백하게. "적당해 보입니다"는 feels about right — about이 "대략 그 지점"이라는 여유를 준다.

## 영어 다듬기

### 카드 1 — Flask가 office.py를 읽게 하려면
- 내가 쓴 영어: "once I fill in code office.py, how can I set the env so that the flask read data from office.py?" (출처: transcript:[user] skewnono 세션)
- 정정: "the flask read" → "Flask reads" — Flask는 고유명사라 관사 없이 쓰고, so that 절의 3인칭 단수 주어에는 -s가 붙는다. "fill in code office.py"는 "fill in office.py"면 충분하다.
- 더 나은 표현: Once I've filled in office.py, how do I set the env var so that Flask reads from it?
- 왜: 미래에 완료될 조건은 once + 현재완료(I've filled in)가 자연스럽고, "the env"보다 "the env var"가 구체적이다. 같은 파일명 반복은 대명사 it으로 정리.

### 카드 2 — 내가 직접 확인할게
- 내가 쓴 영어: "no I will check by myself. just amend the code so that I can apply it later on. not only for the sem_list, other folders should be taken care of." (출처: transcript:[user] skewnono 세션)
- 정정: "check by myself" → "check it myself" — "직접"이라는 뜻의 재귀 강조는 by 없이 myself만 쓴다(by myself는 "혼자서, 남 없이"라는 다른 뜻).
- 더 나은 표현: No, I'll check that myself. Just update the code so I can apply it later — and not just sem_list; the other folders need the same treatment.
- 왜: amend는 커밋·법률문서에 어울리는 격식어라 코드에는 update/change가 맞다. "should be taken care of"의 막연한 수동태 대신 "need the same treatment"로 요구를 또렷하게.

### 카드 3 — 집에서 푸시되면 회사에서 리셋해야 하나
- 내가 쓴 영어: "I am worried that if office.py is updated at home and pushed to the main branch meanwhile I am working in the office, I have to reseut to the origin/main somehow. right?" (출처: transcript:[user] skewnono 세션)
- 정정: "meanwhile I am working" → "while I'm working" — meanwhile은 접속사가 아니라 부사라 절을 이끌 수 없다. "reseut"는 reset의 오타.
- 더 나은 표현: My worry is: if office.py gets updated at home and pushed to main while I'm working at the office, I'd end up having to reset to origin/main, right?
- 왜: "I'd end up having to …"가 "결국 ~해야 하는 처지가 된다"는 우려의 뉘앙스를 정확히 싣는다. 회사에서 일할 때는 in the office도 통하지만 at the office가 더 일반적.

### 카드 4 — 회사에서는 git pull만 한다
- 내가 쓴 영어: "In my office, only do I is about "git pull"." (출처: transcript:[user] skewnono 세션)
- 정정: "only do I is about" — 어순이 무너졌다. "내가 하는 것의 전부"는 의사분열문 "all I do is …"로 쓴다.
- 더 나은 표현: At the office, all I do is git pull.
- 왜: "All I do is + 동사원형"이 "~만 한다"의 정석 구문. only를 문두에 두면 도치(Only at the office do I …)가 일어나 뜻이 달라지니 주의.

### 카드 5 — OpenRouter를 회사에서 막고 싶다
- 내가 쓴 영어: "the chat page, I want to make sure that the openrouter stop (prevent) from working in my office." (출처: transcript:[user] skewnono 세션)
- 정정: "the openrouter stop from working" → "OpenRouter is stopped/blocked from working" — stop A from B-ing 구문은 능동이면 "stop OpenRouter from working"으로 목적어가 stop 뒤에 온다.
- 더 나은 표현: On the chat page, I want to make sure OpenRouter can't be reached from the office — my company's monitoring would flag the outbound call.
- 왜: 네트워크 차단 맥락에서는 "can't be reached"(도달 불가)가 기술적으로 정확하다. 걱정의 이유(회사 모니터링)를 대시 뒤에 붙이면 상대가 설계 방향을 바로 잡는다.

### 카드 6 — tmux 스크롤이 안 보인다
- 내가 쓴 영어: "when I connect the terminal via tmux, I do not see the contents that much. can you manage the tmux so that I can scroll up to see more texts?" (출처: transcript:[user] skewnono 세션)
- 정정: "more texts" → "more text" — 출력물이라는 뜻의 text는 불가산명사다(texts는 문자 메시지들). "the tmux"도 관사 없이 tmux.
- 더 나은 표현: When I attach over tmux, I can barely see any scrollback. Can you configure tmux so I can scroll up through more output?
- 왜: tmux 세계의 동사는 attach가 관용이고, 지난 출력은 scrollback/output이라는 도메인 명사가 있다. "manage"보다 "configure"가 설정 변경 요청임을 분명히 한다.

### 카드 7 — /usage에 왜 비용이 안 보이나
- 내가 쓴 영어: "how come I can't see the total cost when I run /usage?" (출처: transcript:[user] skewnono 세션)
- 더 나은 표현: Why doesn't /usage show a total cost? / (격식) Shouldn't /usage include the total cost somewhere?
- 왜: 문법 오류는 없다. how come은 자연스러운 구어지만 살짝 캐주얼하고, 도구를 주어로 세우면(Why doesn't /usage show …) "내가 못 찾는 것"이 아니라 "화면에 없는 것"임이 분명해져 질문이 더 정확해진다.
