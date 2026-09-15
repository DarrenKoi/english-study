# 2026-09-16 — 코칭

> 오늘 내가 쓴 한국어는 llm-serving 세션의 질문 한 문장뿐이라 한글→영어 (a) 는 한 장이고, 같은 세션의 `[assistant]` 한국어 답변에서 (b) 번역 정독 세 문장을 골랐다. `info key 가 paused 화면에 보이지 않음.` 은 콘솔 로그를 붙여 넣은 줄이라 뺐다. english-study 세션의 `[user]` 는 파이프라인 프롬프트라 대상이 아니고, `yes. commita nd push` 는 오타뿐이라 다루지 않았다.

## 한글→영어

### 카드 1 — 단일 GPU 동시 처리량   (내가 쓴 한글)
- 내가 쓴 한글: "우리의 상황 H200 GPU1장으로 qwen3.8에 동시에 몇개의 요청을 처리할 수 있지?"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: In our setup, with a single H200, how many concurrent requests can qwen3.8 handle?
- 왜 이렇게: "우리의 상황"을 `our situation` 으로 옮기면 무슨 문제가 생긴 것처럼 들린다. 장비 구성을 말할 때는 `our setup` 이 맞다. "GPU 1장"의 "장"에 해당하는 영어 단위는 없으니 `a single H200` 이나 `one H200 GPU` 로 쓴다. "동시에 몇 개의 요청"은 부사 `concurrently` 보다 형용사 `concurrent requests` 로 명사에 붙이는 편이 짧다. 주어는 "우리"가 아니라 모델로 세워 `can qwen3.8 handle` 로 묻는다. 서빙 용량을 묻는 표준 틀이다.

### 카드 2 — 단서를 다는 "다만"   (고급 한글 · 번역)
- 한글 원문: "다만 "8개가 실제로 다 돌아가느냐"는 컨텍스트 길이에 달려 있고, 이 설정의 예산은 그 최악 조건까지 계산되어 있습니다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: That said, whether all eight actually run depends on context length, and this config's budget is sized for that worst case.
- 번역 포인트: "다만"은 앞의 답을 뒤집지 않고 단서만 달 때 쓰니 `But` 보다 `That said,` 가 어울린다. 인용된 물음 "~느냐"는 `whether` 명사절로 바꿔 주어 자리에 세운다. "최악 조건까지 계산되어 있다"를 `calculated up to` 로 직역하면 어색하다. 용량을 그 조건에 맞춰 잡았다는 뜻이니 `sized for that worst case` 가 영어다운 선택이다.

### 카드 3 — "A 하지 B 하지는 않는다"   (고급 한글 · 번역)
- 한글 원문: "여유가 모자라면 vLLM 이 알아서 preempt 하지 실패하지는 않습니다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: If memory runs short, vLLM preempts on its own rather than failing.
- 번역 포인트: "A 하지 B 하지는 않는다"는 한국어에서 흔한 대조 구문인데, 영어로는 `A rather than B` 나 `A instead of B` 한 줄로 담긴다. "알아서"는 `automatically` 도 되지만 `on its own` 이 "사람이 손대지 않아도"라는 결을 더 살린다. 한국어는 "여유"만 말해도 통하지만 영어는 무엇의 여유인지 밝혀야 해서 `memory` 를 넣었다.

### 카드 4 — 레버와 병목   (고급 한글 · 번역)
- 한글 원문: "동시성을 더 올리고 싶으면 레버는 `MAX_NUM_SEQS` 하나고, 스루풋 병목은 KV 가 아니라 27B dense 디코딩의 메모리 대역폭이라 8→16으로 올려도 개별 응답 속도는 느려집니다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: If you want more concurrency, `MAX_NUM_SEQS` is the only lever. The throughput bottleneck is memory bandwidth for dense 27B decoding, not the KV cache, so going from 8 to 16 will slow down each individual response.
- 번역 포인트: 한 문장에 조건, 주장, 원인, 결과가 다 들어 있어 영어에서는 두 문장으로 끊었다. "레버는 X 하나"는 `X is the only lever` 로 주어와 보어를 뒤집어야 강조가 산다. "A 가 아니라 B"는 `B, not A` 순서로 옮기면 핵심이 먼저 온다. "올려도 느려진다"는 모양은 양보(`even if`)지만 내용은 인과라서 `so … will slow down` 으로 이었다.

## 영어 다듬기

### 카드 1 — 소요 시간 로깅 요청
- 내가 쓴 영어: "I want to add logging to store information how long it does take to get the align point correct via llm. In a nutshell, timestamp to know how long it takes for the agent to finish the task for each align fail case"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `store information how long it does take` → `record how long it takes`. 간접의문문은 평서 어순이라 `does` 가 빠진다. `information` 뒤에 절을 바로 붙일 수도 없어서 쓰려면 `information about how long …` 이 된다. 둘째 문장 `timestamp to know …` 는 동사가 없는 조각이니 `I need timestamps …` 로 주어와 동사를 세운다. `llm` → `the LLM`.
- 더 나은 표현: I want to add logging that records how long the LLM takes to get the align point right. In short, I need timestamps showing how long the agent takes to finish each align-fail case.
- 왜: 둘째 문장에서는 `how long it takes` 로 맞게 썼으니 간접의문 어순은 이미 알고 있다. 첫 문장만 고치면 된다. `get X correct` 도 통하지만 구어에서는 `get X right` 가 훨씬 흔하다. `In a nutshell` 은 맞는 표현이고, 요청문 안에서는 `In short` 가 조금 가볍다.

### 카드 2 — 문서 의견과 수정 요청
- 내가 쓴 영어: "what do you think of docs/research/2026-09-15-qwen3.8-27b-vision-recovery.md edit the md file based on your opinion."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 질문과 지시가 구분 없이 붙어 있다(run-on). `… vision-recovery.md? Edit the file …` 처럼 물음표에서 끊는다.
- 더 나은 표현: What's your take on docs/research/2026-09-15-qwen3.8-27b-vision-recovery.md? Edit it to reflect your view.
- 왜: `What do you think of` 도 무난하다. `What's your take on` 은 입장을 정해서 말해 달라는 요구가 조금 더 또렷하다. `based on your opinion` 은 의견을 근거로 삼으라는 말이라 한 번 돌아가고, `to reflect your view` 는 의견을 문서에 반영하라고 바로 말한다. 파일명은 한 번 말했으면 다음부터 `it` 으로 받는다.

### 카드 3 — 탐색 로직이 반영됐는지 확인
- 내가 쓴 영어: "have we updated search around methods for @poc/workflow_3/monitor/manual_align_correction.py"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `search around methods` → `the search-around method`. 두 단어가 명사 앞에서 수식어로 쓰이면 하이픈으로 묶고(`search-around`), 특정한 대상이니 `the` 를 붙인다. 문장 끝에 물음표.
- 더 나은 표현: Does manual_align_correction.py pick up the updated search-around logic too?
- 왜: 실제로 궁금했던 건 "우리가 고쳤나"보다 "이 스크립트에도 반영됐나"였다. 어시스턴트도 이 스크립트는 `run_alarm_cycle` 을 부르기만 해서 따로 고칠 게 없다고 답했다. `pick up` 은 변경 사항을 받아 적용한다는 개발 구어다.

### 카드 4 — 보이는 키를 못 찾는 현상
- 내가 쓴 영어: "now I intentionally place near around the align key (visiable in the live sem box) and the agent fails to locate right away ( it worked a while ago) and go into the phase of search around. what is wrong?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `place near around the align key` → `placed the stage near the align key`. `place` 는 타동사라 목적어가 필요하고 `near around` 는 같은 뜻이 겹친다. `visiable` → `visible`. `fails to locate` → `fails to locate it` (`locate` 도 목적어 필요). `and go into` → `and goes into` (주어 `the agent` 는 3인칭 단수). 이미 해 본 일을 보고하는 것이라 시제는 과거(`placed`, `didn't find`, `fell back`)로 맞추는 게 자연스럽다.
- 더 나은 표현: I deliberately positioned the stage so the align key was visible in the live SEM box, but the agent didn't find it right away and fell back to search-around. It worked a while ago. What's going wrong?
- 왜: 괄호 두 개가 흐름을 끊어서 하나는 `so the align key was visible` 로 본문에 넣고, 하나는 `It worked a while ago.` 로 따로 세웠다. `go into the phase of search around` 는 단계 이름을 풀어 쓴 꼴이라 `fell back to search-around` 가 짧다. `What is wrong?` 도 되지만 원인을 같이 찾자는 뜻이면 `What's going wrong?` 이 더 구어답다.

### 카드 5 — 두 이미지 사이 위치 차이
- 내가 쓴 영어: "in locator you get the right position for the two targeted icon but in cloumn.jpg, they are drifted again. why is it so? what's the discrepency?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the two targeted icon` → `the two target icons` (복수). `they are drifted` → `they have drifted` 또는 `they drift`. `drift` 는 자동사라 수동태를 만들 수 없다. `discrepency` → `discrepancy`. `cloumn.jpg` 는 `column.jpg` 의 오타로 보인다.
- 더 나은 표현: The locator gets the right positions for both target icons, but in column.jpg they've drifted again. Why the mismatch?
- 왜: `you get` 은 상대(어시스턴트)를 주어로 세워 탓하는 말처럼 들린다. 위치를 잡는 건 도구니 `The locator gets` 가 맞다. `why is it so?` 는 옛 문어 느낌이 나서 `Why is that?` 이나 명사구 `Why the mismatch?` 가 자연스럽다. 뒤의 두 질문이 같은 걸 묻고 있어 하나로 합쳤다.

### 카드 6 — 갱신 뒤 재시작 방법
- 내가 쓴 영어: "with the updated contents, how to restart?"   (출처: transcript:[user] equipment-data-map)
- 정정: `how to restart?` 는 동사구 조각이라 질문 문장이 되지 않는다. `how do I restart?` 로 주어와 조동사를 세운다.
- 더 나은 표현: Now that the contents are updated, how should I restart?
- 왜: `with the updated contents` 는 "갱신된 내용을 가지고"로도 읽혀 조건인지 도구인지 흐리다. `Now that …` 은 "이제 ~됐으니"라는 전제를 분명히 한다. `how do I` 는 방법을, `how should I` 는 권장 절차를 묻는다. 문서에 정해진 절차를 물은 것이니 `should` 가 맞다.

### 카드 7 — merge 스크립트 요청
- 내가 쓴 영어: "give me the merge with python file. I use equipment-data-map-qwen3 folder separately"   (출처: transcript:[user] equipment-data-map)
- 정정: `the merge with python file` → `the merge as a Python script`. 형태를 말할 때는 `as` 를 쓰고, 가산명사 단수에는 관사가 붙는다. `use equipment-data-map-qwen3 folder` → `use the equipment-data-map-qwen3 folder`.
- 더 나은 표현: Can you give me the merge steps as a Python script? I keep the equipment-data-map-qwen3 folder separate.
- 왜: `use … separately` 는 "따로 사용한다"라서 무엇과 떨어져 있는지가 안 보인다. `keep X separate` 는 "X 를 별도로 둔다"는 상태를 말한다. 부사 `separately` 와 형용사 `separate` 의 차이다. 명령형 `give me` 도 틀리지 않지만 `Can you` 를 붙이면 부탁으로 들린다.

### 카드 8 — 깨끗한 재시작 허락
- 내가 쓴 영어: "I can restart cleanly. remove some files if needed"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: A clean restart is fine with me, so feel free to delete files if you need to.
- 왜: 문법 오류는 없다. 다만 `I can restart cleanly` 는 "나는 깔끔하게 재시작할 수 있다"는 능력으로도 읽힌다. 뜻한 건 허락이었으니 `is fine with me` 가 오해 없이 전달된다. `some` 은 "몇 개만"처럼 양을 제한하는 느낌이라 허락할 때는 빼는 편이 낫다. `feel free to` 가 허락의 정형이다.

### 카드 9 — .venv 때문에 폴더 전체 삭제 불가
- 내가 쓴 영어: "inside the qwen3 folder, I already set .venv so entire remove is not proper."   (출처: transcript:[user] equipment-data-map)
- 정정: `entire remove` → `removing the entire folder`. `remove` 는 동사라 주어로 쓰려면 동명사(`removing`)나 명사(`removal`)로 바꿔야 한다. `set .venv` → `set up a .venv` (환경을 구성할 때는 `set up`).
- 더 나은 표현: I've already set up a .venv inside the qwen3 folder, so deleting the whole folder won't work.
- 왜: `proper` 는 예절이나 격식에 맞는다는 쪽에 가까워 기술적으로 부적합하다는 말로는 어색하다. `won't work` 나 `isn't an option` 이 자연스럽다. `already` 가 있으면 현재완료 `I've already set up` 이 잘 붙는다.

### 카드 10 — gitignore 추가와 복사 코드
- 내가 쓴 영어: "add .venv to gitignore and commit. give me in the python code to copy. I do not use git for qwen3 folder"   (출처: transcript:[user] equipment-data-map)
- 정정: `give me in the python code to copy` → `give me the copy step as Python code`. `give` 는 목적어를 바로 받으니 `in` 이 끼면 안 되고, 무엇을 달라는지(`the copy step`)가 먼저 와야 한다. `for qwen3 folder` → `in the qwen3 folder`.
- 더 나은 표현: Add .venv to .gitignore and commit. Then give me the copy step as a Python script, since I don't use git in the qwen3 folder.
- 왜: 세 문장이 뚝뚝 떨어져 있어 셋째 문장이 둘째의 이유라는 게 보이지 않는다. `since` 로 이으면 "git 을 안 쓰니 Python 으로 달라"는 인과가 드러난다. 파일 이름은 점까지 넣어 `.gitignore` 로 쓴다.

### 카드 11 — 복사-붙여넣기 방식 알리기
- 내가 쓴 영어: "I directly copy and paste from equipment-data-parser to equipment-data-parser-<model> to test with different models. do you know that?"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: I test different models by copy-pasting equipment-data-parser into equipment-data-parser-<model>. Were you aware of that?
- 왜: 문법 오류는 없다. 그런데 `Do you know that?` 은 억양에 따라 "그것도 몰랐어?"라고 따지는 말로 들린다. 상대가 몰랐을 법한 사실을 확인할 때는 `Were you aware of that?` 이나 `Did you know that?` 이 부드럽다. `copy and paste from A to B` 는 `copy A into B` 로 줄일 수 있다. 목적 `to test` 를 앞으로 빼 `I test … by -ing` 로 뒤집으면 하고 싶은 말이 먼저 나온다.

### 카드 12 — 가이드 재작성 지시
- 내가 쓴 영어: "rewrite engineer-guide §1 for copy-paste, drop the checkpoint commits and push"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Rewrite engineer-guide §1 around the copy-paste workflow, drop the per-checkpoint commits, and push.
- 왜: 오류 없는 간결한 지시다. `for copy-paste` 는 "복사용으로"로 읽힐 여지가 있다. `around the copy-paste workflow` 라고 하면 그 워크플로를 중심에 두고 다시 쓰라는 뜻이 선다. 동사 셋을 나열할 때 마지막 `and` 앞에 쉼표(Oxford comma)를 넣으면 `drop … and push` 가 한 덩어리로 묶여 읽히지 않는다.

### 카드 13 — 복사 파일 설정 확인
- 내가 쓴 영어: "copy file is set well?"   (출처: transcript:[user] equipment-data-map)
- 정정: `copy file` → `the copy file` (관사). `set well` 은 영어에서 거의 쓰지 않는 조합이라 `set up correctly` 로 바꾼다.
- 더 나은 표현: Is the copy script set up correctly?
- 왜: 평서문 끝에 물음표만 붙이는 억양 질문은 말로는 통해도 글에서는 `Is …?` 로 도치하는 편이 분명하다. 어시스턴트가 "bash 스니펫은 문서에 있지만 Python 스크립트는 저장된 적이 없다"고 되물은 걸 보면 `copy file` 이 무엇인지도 흐렸다. `copy script` 로 대상을 좁히면 이런 되묻기가 준다.

### 카드 14 — 인자를 파일 안에 고정
- 내가 쓴 영어: "apply the argument inside the py file."   (출처: transcript:[user] equipment-data-map)
- 정정: `the argument` → `the arguments` (폴더 경로와 slug 두 개였다).
- 더 나은 표현: Hard-code the arguments as defaults at the top of the .py file.
- 왜: `apply` 는 "적용하다"라서 인자를 실행에 넘긴다는 말로 읽힌다. 원한 건 명령행 인자를 파일 안 상수로 옮기는 일이었으니 `hard-code … as defaults` 가 정확하다. 어시스턴트도 결과를 `The defaults now live at the top of tools/reset_model_folder.py` 로 보고했다.

### 카드 15 — Windows 프록시 강제
- 내가 쓴 영어: "make sure that in windows, you should use proxy from ftp_handler. no direct download allowed in the company."   (출처: transcript:[user] equipment-data-map)
- 정정: `make sure that … you should use` → `make sure (that) … uses`. `make sure` 뒤의 절은 보장할 사실을 평서형으로 쓰고 `should` 를 넣지 않는다. `windows` → `Windows`, `use proxy` → `use the proxy`. `no direct download allowed` 는 동사 없는 조각이라 `Direct downloads aren't allowed` 로 세운다.
- 더 나은 표현: Make sure Windows always goes through the ftp_handler proxy. Direct downloads aren't allowed on the company network.
- 왜: `you should use` 는 주어가 어시스턴트라 "네가 프록시를 써라"가 된다. 실제로 원한 건 코드가 Windows 에서 프록시만 타게 하는 것이니 주어를 `Windows` 로 바꿔야 요구 대상이 맞는다. `in the company` 는 "회사 사람들 사이에서"로도 읽혀서 망 정책이면 `on the company network` 가 정확하다.

### 카드 16 — 인덱스 위치 확인
- 내가 쓴 영어: "in chat page, do you consider where the index is located? in _rag folder?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in chat page` → `on the chat page` (웹 페이지에는 `on`, 관사 필요). `in _rag folder` → `in the _rag folder`.
- 더 나은 표현: Does the chat page account for where the index lives? Is it under the _rag folder?
- 왜: `do you consider` 는 "당신이 고려하느냐"라서 사람의 판단을 묻는다. 코드 동작을 물을 때는 `Does the chat page account for` 처럼 기능을 주어로 세운다. 파일 위치에는 `is located` 보다 `lives` 가 개발자 구어로 흔하다.

### 카드 17 — 짧은 되묻기 모음
- 내가 쓴 영어: "what do you recommend?" / "I see. let's test." / "is the index path documented in MIGRATION.md too?" / "what is the root here?"   (출처: transcript:[user] auto-recipe-creator, skewnono-v3-nuxt)
- 더 나은 표현: What would you recommend? / Makes sense. Let's test it. / Does MIGRATION.md cover the index path too? / What does "root" refer to here?
- 왜: 네 문장 모두 첫 글자 대문자 말고는 오류가 없다. `What would you recommend?` 는 `would` 가 들어가 한결 공손하다. `let's test` 에 목적어 `it` 을 붙이면 무엇을 시험할지가 닫힌다. `documented in` 도 맞고, `cover` 는 "다루고 있나"를 짧게 묻는다. `What is the root here?` 는 "root 값이 뭐냐"로 읽힐 수 있어 용어가 가리키는 대상을 물을 땐 `refer to` 가 정확하다.
