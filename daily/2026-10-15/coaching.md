# 2026-10-15 — 코칭

## 한글→영어

### 카드 1 — 증상을 전하고 해법·범위 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "ftp_handler로 proxy를 통해 windows 서버에 접속에는데, 한글 파일명이 프록시의 utf-8 디코딩을 깨트려 나열이 전부 실패하고 있다고 해. flask_proxy)에 cp949 처리를 넣어야 하는데 어떻게 해결 가능해? direct download도 문제가 있을 수 있는 지 확인해야함."   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: We connect to the Windows server through the proxy with `ftp_handler`, and apparently Korean filenames break the proxy's UTF-8 decoding, so every listing fails. I think we need cp949 handling in `flask_proxy` — how would you fix it? Also, please check whether direct download has the same problem.
- 왜 이렇게: "~다고 해"는 전해 들은 말이라 `apparently` 하나로 충분하다(`they say` 보다 가볍다). "나열이 전부 실패"는 `every listing fails` 로 주어를 세우면 짧아진다. "~를 넣어야 하는데"는 내 추측이라 `I think we need …` 로 열어 두면, 상대가 "거기가 아니다"라고 반박할 여지가 생긴다(실제로 답은 `flask_proxy` 가 아니었다). "확인해야함"은 혼잣말 메모체라 요청으로 바꿔 `please check whether …` 로 쓴다. 참고로 "접속에는데"는 "접속하는데"의 오타.

### 카드 2 — 진행 승인과 범위 추가   (내가 쓴 한글)
- 내가 쓴 한글: "응, 진행해줘. flask_module도 함께 수정"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Yes, go ahead — and fix `flask_modules` as well.
- 왜 이렇게: 승인은 `go ahead` 가 표준이다. 덧붙이는 범위는 대시 뒤에 `and … as well` 로 붙이면 한 문장에 담긴다. `too` 도 되지만 문장 끝 `as well` 이 조금 더 단정하다.

### 카드 3 — 재배포가 필요한지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "ftp_handler에서 flask proxy에 업데이트 된 내용이 있어? 재배포 필요한가 해서"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Did anything change on the flask proxy side of `ftp_handler`? I'm wondering if we need to redeploy it.
- 왜 이렇게: "업데이트 된 내용이 있어?"는 `Did anything change …?` 가 가장 자연스럽다(`Is there updated content` 는 직역투). "~한가 해서"는 질문의 이유를 붙이는 말이라 `I'm wondering if …` 가 딱 맞는다. 진행형이 "지금 머릿속에 든 생각"이라 부드럽다.

### 카드 4 — 사무실에 넘길 변경 요약 요청   (내가 쓴 한글)
- 내가 쓴 한글: "사무실에 전달할 내용 알려줘 변경 내역"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Can you write up the changes so I can pass them on to the office?
- 왜 이렇게: 명사를 이어 붙인 메모체는 영어로 옮기면 목적을 `so I can …` 으로 풀어야 산다. `write up` 은 "정리해서 문서 형태로 쓰다", `pass on to` 는 "전달하다"다. 짧게는 `Give me a change summary for the office.` 도 된다.

### 카드 5 — 문서로 저장 요청   (내가 쓴 한글)
- 내가 쓴 한글: "이 내용 docs/office-migration에 문서로 저장해줘"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Save this as a doc under `docs/office-migration`.
- 왜 이렇게: "~에 문서로"는 `as a doc under …`. 폴더 안이면 `in` 도 되지만 경로 아래라는 느낌은 `under` 가 더 자연스럽다.

### 카드 6 — 테스트 결과 전하고 의견 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "ftp_handler 수정본을 가지고 office agent가 테스트한 결과, 한글이 아니라 꺠진 바이트 (binary garbage) 파일명이 ㅆ었다. 10개 비ASCII 이름이 cp949, utf-8 어느 것도 아닌 난수형 바이트. 손상된 파일명이지 인코딩 문제가 아니였다. 그래서 latin-1이 특정 호스트에는 정답일 수 있다는데 어떻게 생각해?"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: The office agent tested the patched `ftp_handler`, and it turns out the filenames weren't Korean at all — they were binary garbage. All ten non-ASCII names are random bytes that are neither cp949 nor UTF-8. So it's corrupted filenames, not an encoding problem. They're suggesting latin-1 might be the right answer for certain hosts. What do you think?
- 왜 이렇게: "~한 결과 ~였다"는 `it turns out …` 이 "예상과 달랐다"는 반전까지 담는다. "A가 아니라 B"는 `not A at all — B` 나 `B, not A` 로. "어느 것도 아닌"은 `neither … nor …`. "~라는데"(전해 들은 제안)는 `They're suggesting …` 으로 출처를 분명히 하고, 의견 질문은 문장을 따로 끊어 `What do you think?` 로 묻는다. 원문의 "꺠진", "ㅆ었다", "아니였다"는 각각 "깨진", "있었다", "아니었다"의 오타다.

### 카드 7 — 진행 + 기본값 유지 지시   (내가 쓴 한글)
- 내가 쓴 한글: "진행해줘. 기본값은 utf-8 유지"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Go ahead, but keep the default at UTF-8.
- 왜 이렇게: "유지"는 `keep X at Y` 가 정확하다(값을 그 자리에 붙들어 두다). 앞의 승인과 조건을 `but` 으로 이으면 "진행은 하되 이건 바꾸지 마"라는 선이 선명해진다.

### 카드 8 — 짧은 수긍·전체 push   (내가 쓴 한글)
- 내가 쓴 한글: "오키 알았어." / "push해줘" / "오케이 전부 push"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: Okay, got it. / Go ahead and push. / Okay, push everything.
- 왜 이렇게: "알았어"는 이해했다는 뜻이라 `Got it.` 이 가장 가깝다(`I know` 는 "이미 알아"라서 틀린 짝). "push해줘"는 명령만 써도 되지만 `Go ahead and …` 를 붙이면 승인 어조가 된다. "전부"는 `everything` 또는 `push both repos` 처럼 대상을 밝혀도 좋다.

### 카드 9 — 사무실 회신을 메모체로 전달   (내가 쓴 한글)
- 내가 쓴 한글: "A hitachi 계정과 다름. 계열별로 갈림. veritysem = rtauser, provision = wf.. 둘다 회사내에서 데이터 취득 가능. B 1 계열마다 다름. veritysem D:\Output, provision /I_Drive + /D_drive/ C 1 잇음."   (출처: transcript:[user] skewnono-v3-nuxt/065d8f78)
- 자연스러운 영어: A: Different from the Hitachi account — it's split by product line: VeritySEM uses `rtauser`, Provision uses `wf…`. Both can pull data from inside the company network. B: Option 1 — it differs by line: VeritySEM is `D:\Output`, Provision is `/I_Drive` + `/D_drive/`. C: Option 1 — yes, it exists.
- 왜 이렇게: 항목별 답장은 영어에서도 메모체가 허용되지만 콜론으로 라벨을 달면 훨씬 읽기 쉽다. "계열별로 갈림"은 `it's split by …`, "회사 내에서 취득 가능"은 `can pull data from inside the company network`. "잇음"은 "있음"의 오타라 `yes, it exists` 로 옮긴다.

### 카드 10 — 증상 위치와 원인 위치는 다르다   (고급 한글 · 번역)
- 한글 원문: "'proxy에서 고쳐야 한다'는 증상이 보인 위치를 가리킬 뿐입니다. 공유 함수 `_session()` 한 곳을 고치면 proxy, direct, recipe_search, msr_image가 한꺼번에 해결됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: "Fix it in the proxy" only points to where the symptom showed up. Fix the one shared function, `_session()`, and the proxy, direct, recipe_search and msr_image paths are all fixed at once.
- 번역 포인트: "~를 가리킬 뿐"은 `only points to` 로 `only` 위치가 중요하다(동사 앞). 둘째 문장은 "명령문 + and + 결과" 구문(`Fix X, and Y`)을 쓰면 조건문(`If you fix …`)보다 단단하고 설득력이 있다. "한꺼번에"는 `all … at once`.

### 카드 11 — 가짜 객체가 버그를 못 잡는 이유   (고급 한글 · 번역)
- 한글 원문: "기존 테스트의 FakeFTP는 ftplib 자체를 대체하기 때문에, 바로 그 층에 있는 이 버그를 원리상 잡을 수 없었습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: The existing tests' FakeFTP replaces ftplib itself, so by design it could never catch a bug that lives in that very layer.
- 번역 포인트: "원리상"은 `in principle` 도 되지만 테스트 설계 맥락에서는 `by design` 이 "구조적으로 애초에"를 더 정확히 전한다. "바로 그 층에 있는"은 `that lives in that very layer` 로, 버그가 "산다"(`live`)는 개발자 구어가 자연스럽다.

### 카드 12 — 배포 순서를 풀어 준 설계   (고급 한글 · 번역)
- 한글 원문: "새 키는 '보내는 쪽은 그냥 보내고, 받는 쪽은 없으면 기본값'으로 설계했습니다. 그래서 따로 배포되는 proxy와 클라이언트의 배포 순서를 맞출 필요가 없습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: The new key follows "the sender just sends it; the receiver falls back to a default if it's missing." That way the proxy and the client, which ship separately, don't have to be deployed in any particular order.
- 번역 포인트: 설계 원칙을 따옴표로 옮길 때 영어는 세미콜론으로 두 쪽을 대칭으로 세운다. "없으면 기본값"은 `falls back to a default` 가 정형구다. "따로 배포되는"은 관계절 `which ship separately` 로 넣고, "순서를 맞출 필요가 없다"는 `don't have to be deployed in any particular order` 로 부정의 범위를 `any` 가 잡아 준다.

### 카드 13 — 기각 이유가 사라졌다   (고급 한글 · 번역)
- 한글 원문: "앞서 제가 기각했던 이유가 사라졌습니다. … latin-1은 실패를 막을 뿐 이름을 고쳐 주지 않습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/e3eac2d8)
- 자연스러운 영어: The reason I rejected it earlier no longer holds. … latin-1 only keeps things from failing; it doesn't repair the names.
- 번역 포인트: "이유가 사라졌다"를 `disappeared` 로 옮기면 어색하다. 논리·근거에는 `no longer holds`(더는 성립하지 않는다)를 쓴다. "~할 뿐 ~하지 않는다"는 `only …; it doesn't …` 로 세미콜론 대비를 만든다. "실패를 막다"는 `keep things from failing` 이 `prevent failure` 보다 구어답다.

## 영어 다듬기

### 카드 14 — 인덱스가 너무 많다, 롤오버를 늘려 달라
- 내가 쓴 영어: "for the skewnono_logging, I found that they are too many index created with numbering. can we reduce that? make enlarged rollover"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 정정: For skewnono_logging, I found that **there are** too many **indices** created with numbering. Can we reduce that? **Make the rollover interval longer.** — 존재를 말할 때는 `they are` 가 아니라 `there are`. `many` 뒤 명사는 복수(`indices` 또는 `indexes`). `enlarged rollover` 는 롤오버 자체를 "크게 만든" 것처럼 읽혀 뜻이 흐리다. 늘릴 대상(주기)을 밝혀야 한다.
- 더 나은 표현: skewnono_logging is creating too many numbered indices. Can we cut that down by making the rollover period longer?
- 왜: 관찰(`is creating too many numbered indices`)과 해법(`by making … longer`)을 한 문장에 묶으면 요청이 한 번에 읽힌다. `numbered indices` 는 "번호가 붙은 인덱스"를 형용사 하나로 끝낸다. `cut down` 은 `reduce` 의 구어다.

### 카드 15 — 기존 번호 인덱스는 어떻게 되나
- 내가 쓴 영어: "after this run, what happen to the existant indice with numberings?"   (출처: transcript:[user] skewnono-v3-nuxt/e3eac2d8)
- 정정: After this run, what **happens** to the **existing** numbered **indices**? — `what` 이 주어인 의문문은 3인칭 단수 동사(`happens`)를 받는다. `existant` 는 영어에 없는 철자로, `existing` 이 맞다(`extant` 는 "현존하는"이라는 문어). `indice` 는 단수형이 아니다. 단수는 `index`, 복수는 `indices`. `with numberings` 는 `numbered` 로 줄인다.
- 더 나은 표현: Once this runs, what will happen to the existing numbered indices?
- 왜: 앞으로 일어날 일을 묻는 거라 `will happen` 이 시점을 분명히 한다. `Once this runs` 는 "이게 돌고 나면"으로 `After this run` 보다 말맛이 자연스럽다.
