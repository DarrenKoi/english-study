# 2026-08-24 — 코칭

## 한글→영어

### 카드 1 — 검증 대상을 지정하며 일 시키기   (내가 쓴 한글)
- 내가 쓴 한글: "@poc/workflow_3/monitor/align_fail_monitor 를 진행하려고 해. 녹화 on 기능 잘 동작하는지 확인 부탁하고, align fail 발생했을 때 실제로 마우스 움직여서 align point 찾는 지 확인해야해 <- 이부분 녹화 필요"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: I'm about to run `align_fail_monitor`. Two things to check: that the recording flag actually takes effect, and that on an align fail the agent really moves the mouse to find the align point — that second part is what I need on video.
- 왜 이렇게: "진행하려고 해"는 `I'm about to` 가 딱 맞는다. `I will run` 은 결심, `I'm going to run` 은 예정, `I'm about to run` 은 "지금 곧" — 지금 확인을 부탁하는 맥락이니 셋째가 맞다. "확인 부탁하고 ... 확인해야해"처럼 확인이 둘이면 영어는 `Two things to check:` 로 먼저 개수를 알리고 `that ...` 명사절 둘을 나란히 놓는다. 화살표(`<- 이부분`)는 영어 문장에 그대로 못 옮기니 `that second part is what I need on video` 라는 분열문으로 되살렸다.

### 카드 2 — 자동 실행 범위를 넓혀 달라고 하기   (내가 쓴 한글)
- 내가 쓴 한글: "클릭까지 가도록 해줘"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: Take it all the way through the click.
- 왜 이렇게: "~까지 가도록"은 `all the way through X` 가 그대로 대응한다. `up to the click` 은 "클릭 직전까지"로 읽혀 정반대가 되니 쓰면 안 된다. 되돌릴 수 없는 조작을 켜는 지시라 `Go ahead and enable the actual click` 처럼 승인 어휘를 붙이면 더 분명해진다.

### 카드 3 — 설정 하나를 일단 보류하기   (내가 쓴 한글)
- 내가 쓴 한글: "RECORD_PRELUDE는 None으로 일단 갈게"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: Let's leave `RECORD_PRELUDE` at `None` for now.
- 왜 이렇게: "일단 ~로 갈게"는 결정이자 유보다. `for now` 가 그 유보를 맡고, `leave X at Y` 가 "바꾸지 않고 그대로 둔다"를 맡는다. `set it to None` 은 새로 바꾼다는 뜻이라 이미 그 값인 경우엔 어긋난다. 회의에서 쓰면 `Let's park that one at None for now` 도 자연스럽다.

### 카드 4 — 증거가 안 보일 때 확인 경로를 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "화면상에서 마우스가 움직이는게 안보이는데, 그러면 align fail 위치 조정을 했는 지 어떻게 확인하지? 로그가 있나?"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: I can't see the cursor moving on screen, so how do I confirm the align-fail reposition actually happened? Is there a log line for it?
- 왜 이렇게: "~했는 지 어떻게 확인하지"의 핵심은 `confirm` 이다. `check` 는 "한번 봐 본다", `confirm` 은 "일어났음을 확정한다"라 증거를 요구하는 이 자리엔 후자다. "로그가 있나?"를 `Is there a log?` 로 끝내면 파일 존재를 묻는 말이 되니, 찾고 싶은 게 한 줄이라면 `a log line for it` 까지 붙이는 편이 답을 정확히 끌어낸다.

### 카드 5 — 기본 동작을 예외적으로 뒤집어 달라고 하기   (내가 쓴 한글)
- 내가 쓴 한글: "다른 엔지니어 점유 중 발생중인데, 보정 건너뛰지 말고 진행해줘. 내가 엔지니어에게 말해서 agent가 작업 끝날 떄까지 기다려달라고 할게"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: These are firing while another engineer has the tool, so don't skip the correction — go ahead and run it. I'll ask them to hold off until the agent is done.
- 왜 이렇게: "점유 중"은 `has the tool` 이 가장 짧고 자연스럽다. `is occupying` 은 물리적 점거처럼 들린다. "말해서 ~해달라고 할게"는 `I'll tell them and ask them to ...` 로 두 동사를 다 옮기면 무겁다 — 영어는 `I'll ask them to ...` 하나로 충분하고, 부탁의 내용에 `hold off`(하던 걸 잠시 멈추고 기다림)를 쓰면 "기다려 달라"의 뉘앙스가 정확히 산다. 대상 엔지니어의 성별을 모르므로 `them` 이 안전하고 자연스러운 선택이다.

### 카드 6 — 상대의 전제를 사실로 정정하기   (내가 쓴 한글)
- 내가 쓴 한글: "ZOOM_PROBE = None으로 되어있어 config.py"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: `ZOOM_PROBE` is `None` in my `config.py`, not `0`.
- 왜 이렇게: 상대가 틀린 값을 근거로 경고했을 때 영어는 맞는 값만 던지기보다 `not X` 를 붙여 무엇이 틀렸는지까지 한 문장에 담는다. `is set to None` 도 되지만 파일을 인용하는 자리에선 `is None` 이 더 담백하다. 위치를 밝히는 `in my config.py` 를 뒤에 붙이면 "네가 본 사본과 다르다"는 함의가 자연히 생긴다.

### 카드 7 — 현재 동작을 확인 삼아 되묻기   (내가 쓴 한글)
- 내가 쓴 한글: "누가 장비에 이미 점유 중일 때는 건너뛰는 거지?"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: So it skips when someone already has the tool, right?
- 왜 이렇게: "~하는 거지?"는 정보를 묻는 게 아니라 이해한 바를 확인하는 부가의문이다. 영어에서는 문장 끝의 `right?` 가 그 역할을 하고, 문두 `So` 가 "지금까지 들은 걸 정리하면"을 담는다. `Does it skip ...?` 로 쓰면 처음 묻는 질문이 되어 확인의 뉘앙스가 사라진다.

### 카드 8 — 방향에 따라 다른 규칙을 지정하기   (내가 쓴 한글)
- 내가 쓴 한글: "RCS 상에서 장비로 접근 시도했을 때 이미 다른 엔지니어가 점유 중이면 건너뛰기. 장비 안에서 (remote monitoring via RCS) 우리가 작업 중일 때 다른 엔지니어가 접근하면 허용해주기."   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: Two directions, two rules. Going in: if another engineer already has the tool, skip. Already inside: if another engineer asks to come in while we're working, let them in.
- 왜 이렇게: 두 규칙이 대칭이라는 게 요구의 핵심이니 `Two directions, two rules.` 로 그 대칭을 먼저 선언한다. 방향은 `Going in:` / `Already inside:` 라는 짧은 라벨로 잡으면 조건절을 두 번 길게 쓰지 않아도 된다. 조건-결과는 `if ..., skip` 처럼 명령문으로 닫는 게 규칙 서술의 표준 형태다.

### 카드 9 — 예외를 삼키는 폴백을 변호하기   (고급 한글 · 번역)
- 한글 원문: "폴백이 '예외를 삼킨다'처럼 보이지만 의도된 계약입니다. consensus는 정확도 향상 레버이지 필수 입력이 아니라서, 실패 시 회귀 위험이 0인 rcp 경로로 떨어지는 게 루프를 멈추는 것보다 낫습니다."   (출처: transcript:[assistant] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: The fallback looks like it swallows exceptions, but that's the intended contract. Consensus is an accuracy lever, not a required input, so dropping to the zero-regression rcp path on failure beats stopping the loop.
- 번역 포인트: "~처럼 보이지만"은 `It looks like X, but ...` 로 절을 세우는 편이 `Although it appears to ...` 보다 구어에 가깝고 힘이 있다. "레버이지 필수 입력이 아니라서"의 대조는 영어에서도 `A, not B` 를 그대로 살린다 — 한국어의 `-이지 ... 아니라서` 와 구조가 겹친다. 마지막 절의 "~보다 낫습니다"에 `is better than` 대신 `beats` 를 쓰면 설계 판단의 단호함이 살고 문장도 짧아진다.

### 카드 10 — 설계가 결함을 만든 게 아니라 드러냈다고 말하기   (고급 한글 · 번역)
- 한글 원문: "이 결함이 지금까지 안 보인 이유는 폴더가 recipe 기준 경로에 묻혀 있어서입니다. '폴더 하나 = 테이크 하나'를 표방하는 순간 같은 폴더가 두 번 쓰이는 게 계약 위반으로 드러납니다. 레이아웃 설계가 잠복 결함을 드러낸 것이지 만든 게 아닙니다."   (출처: transcript:[assistant] auto-recipe-creator 03c7c8ef)
- 자연스러운 영어: The defect stayed invisible because the folder was buried under a recipe-shaped path. The moment you claim "one folder, one take", reusing the same folder becomes a contract violation. The layout design surfaced a latent defect; it did not create one.
- 번역 포인트: "~한 이유는 ~해서입니다"를 `The reason X is because Y` 로 옮기면 영어에서는 군더더기다. `X stayed invisible because Y` 로 이유절을 바로 붙이는 게 표준. "표방하는 순간"의 `순간` 은 `The moment (that) ...` 이 시간 접속사로 그대로 대응한다. 마지막 줄의 "드러낸 것이지 만든 게 아닙니다"는 세미콜론 + `it did not create one` 으로 받는 게 자연스럽다 — 접속사 없이 붙여 두 절을 한 판정으로 묶는다.

### 카드 11 — 상한이 있는데도 상한이 없다고 지적하기   (고급 한글 · 번역)
- 한글 원문: "wall-clock 상한이 없는 게 설계 공백입니다. 상한이 전부 '횟수'라, 장비가 느려 매 제스처 settle이 길어지면 총 시간이 선형으로 늘어나는데 이를 끊는 장치가 없습니다."   (출처: transcript:[assistant] auto-recipe-creator 5a0a54c3)
- 자연스러운 영어: The missing wall-clock cap is a gap in the design. Every budget here counts *attempts*, so when the tool is slow and each gesture takes longer to settle, total time grows linearly with nothing to cut it off.
- 번역 포인트: "~이 없는 게 공백입니다"는 `The missing X is a gap` 처럼 형용사 `missing` 을 명사구 안으로 밀어 넣으면 주어가 짧아진다. `The fact that there is no X` 는 문법적으로 맞지만 무겁다. "이를 끊는 장치가 없습니다"를 별도 문장으로 떼지 않고 `with nothing to cut it off` 라는 부대상황 `with` 구로 붙이면, 원문의 "늘어나는데"가 담고 있던 아쉬움의 어조까지 옮겨진다.

## 영어 다듬기

### 카드 12 — 도구를 특정 모델로 띄워 달라고 하기
- 내가 쓴 영어: "can you spawn a pane to use opencode model with GLM-5.3 in Go mode?"   (출처: transcript:[user] skewnono-v3-nuxt 8949d97d)
- 정정: `use opencode model` → `use opencode` 또는 `run the opencode agent`. `opencode` 는 고유명사라 `model` 을 덧붙이면 "opencode 라는 모델"로 읽혀 실제 관계(도구 안에서 GLM-5.3 이라는 모델을 쓴다)가 뒤집힌다.
- 더 나은 표현: Can you spawn a pane running opencode on `opencode-go/glm-5.3`?
- 왜: `to use ...` 부정사 대신 현재분사 `running ...` 을 쓰면 pane 을 바로 수식해 "무엇이 도는 pane 인지"가 한 덩어리로 붙는다. 모델 지정은 전치사 `on` 이 관용이고(`run X on model Y`), 제공자 접두사까지 적어 주면 상대가 되물을 일이 없다.

### 카드 13 — 모드를 바꿔 달라고 하기
- 내가 쓴 영어: "can you switch in build mode"   (출처: transcript:[user] skewnono-v3-nuxt 8949d97d)
- 정정: `switch in build mode` → `switch to build mode`. `switch to X` 가 상태 전환이고, `switch in` 은 "끼워 넣다"(부품 교체)라 뜻이 다르다. 물음표도 빠졌다.
- 더 나은 표현: Can you switch it to build mode?
- 왜: 목적어 `it` 이 있어야 "그 pane 을"이 분명해진다. 없으면 상대 자신이 모드를 바꾸는 것처럼 읽힐 여지가 있다. 더 짧게는 `Switch it to build, please.` — 명령문 + `please` 가 도구 조작 지시에서 가장 흔한 형태다.

### 카드 14 — 방금 한 조작의 명령어를 되묻기
- 내가 쓴 영어: "what is the command to open the opencode with GLM-5.3 go high?"   (출처: transcript:[user] skewnono-v3-nuxt 8949d97d)
- 정정: `the opencode` → `opencode`. 프로그램 이름 앞에는 관사를 붙이지 않는다(`open Chrome`, `run git`). 문두 `What` 도 대문자로.
- 더 나은 표현: What's the exact command to launch opencode with GLM-5.3 on Go, variant `high`?
- 왜: `exact` 한 단어가 "설명 말고 그대로 복사할 줄"을 요청한다. `go high` 처럼 수식어 둘을 붙여 놓으면 무엇이 무엇을 꾸미는지 모호하니, `on Go, variant high` 로 제공자와 변형을 갈라 놓는 게 안전하다. `open` 보다 `launch` 가 실행 파일에 어울린다.

### 카드 15 — 정리 아이디어를 요청하기
- 내가 쓴 영어: "can you think of better idea to organize by combining align_images and debug_images? while I run @poc/workflow_3/monitor/align_fail_monitor?"   (출처: transcript:[user] auto-recipe-creator 03c7c8ef)
- 정정: `better idea` → `a better idea`(가산 단수엔 관사 필수). 그리고 `while I run ...?` 는 동사 없는 조각이라 앞 문장에 붙여야 한다.
- 더 나은 표현: Can you think of a better way to organize these — maybe merging `align_images` and `debug_images`? I'll be running `align_fail_monitor` in the meantime.
- 왜: `a better idea to organize by combining X and Y` 는 방법(`by combining`)이 요청 안에 못 박혀 있어 다른 답을 막는다. `a better way to organize these` 로 열어 두고 `maybe merging ...` 을 제안으로 낮추면 더 나은 안이 나올 문이 열린다. 실제로 상대가 내놓은 답은 병합이 아니라 제3의 폴더였다. 끝의 `in the meantime` 은 "그동안 나는 딴 걸 돌리고 있다"를 한 구로 처리한다.

### 카드 16 — 리팩터를 미루고 대안을 요청하기
- 내가 쓴 영어: "so it is hard to refactor all the code right now as we are in the middle of testing important features."   (출처: transcript:[user] auto-recipe-creator 03c7c8ef)
- 더 나은 표현: A full refactor is off the table right now — we're mid-test on features that matter.
- 왜: 문법 오류는 없다. 다만 `it is hard to ...` 는 "어렵다"에 머물러 상대가 "그래도 해 보죠"로 되받을 여지를 남긴다. `off the table` 은 선택지에서 제외됐다는 확정이라 협상이 끝난다. `in the middle of testing` → `mid-test` 로 줄이면 문장 길이가 결정의 단호함과 맞는다.

### 카드 17 — 실시간 판정 화면을 요청하기
- 내가 쓴 영어: "can you display important monitorings like live SEM box detection, align position (where agent notices) sort of things that I can see if the test is successfull or not. This triger when we get out from the remote monitoring."   (출처: transcript:[user] auto-recipe-creator 03c7c8ef)
- 정정: ① `monitorings` → `monitoring` 또는 `monitoring output`. `monitoring` 은 불가산이라 복수형이 없다. ② `sort of things that I can see if ...` → `so that I can see whether ...`. 목적을 나타내는 자리라 `so that` 이고, "~인지 아닌지"는 `whether` 다. ③ `successfull` → `successful`(l 하나). ④ `triger` → `triggers`. ⑤ `get out from` → `come out of` / `exit`. `get out from` 은 어색한 결합이다.
- 더 나은 표현: Instead, can you print the key signals at the end of each cycle — live SEM box detection, the align position the agent picked, that sort of thing — so I can tell at a glance whether the run succeeded? It should fire right when we come out of the remote session.
- 왜: `that sort of thing` 이 관용형이다(`sort of things` 는 쓰지 않는다). `display` 는 GUI 를 연상시키니 콘솔 출력이면 `print` 가 정확하다. `where agent notices` 는 뜻이 흐릿해 `the align position the agent picked` 로 목적어를 분명히 했다. 판정 목적은 `so I can tell at a glance` — `tell` 이 "구별해 낸다"를 맡아 `see` 보다 이 맥락에 맞는다.

### 카드 18 — 오류를 그대로 붙여 보고하기
- 내가 쓴 영어: "ImportError from cycle.py. cannot import name 'capture_screen' from poc.workflow_3.util"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 더 나은 표현: Office box throws on startup: `ImportError: cannot import name 'capture_screen' from poc.workflow_3.util` — raised from `cycle.py`.
- 왜: 오류 문자열을 붙이는 건 옳은 습관이다. 다만 **어디서** 났는지가 빠지면 상대가 재현 조건을 되묻는다. `Office box throws on startup` 한 구절이 환경과 시점을 동시에 준다. 원문·해설을 백틱으로 갈라 두면 어디까지가 붙여넣기인지도 분명해진다.

### 카드 19 — 고쳐졌다고 알리기
- 내가 쓴 영어: "now it works."   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 더 나은 표현: That fixed it — the monitor starts clean now.
- 왜: 오류 없다. 다만 `it works` 는 무엇이 어디까지 되는지를 안 말해 준다. `That fixed it` 으로 원인·결과를 연결하고 대시 뒤에 확인한 범위를 한 구절 붙이면, 상대가 "다른 것도 확인해 볼까요"를 물을 필요가 없어진다. 회화에서는 `We're good — it starts up fine now.` 가 같은 일을 한다.

### 카드 20 — 두 증상을 함께 보고하기
- 내가 쓴 영어: "I see RCSSEMMonitor 좌표 배율 캘리브레이션 미완료.  in the console. and also no see reposition 더블클릭 recenter. . We have to fix this issue"   (출처: transcript:[user] auto-recipe-creator 5a0a54c3)
- 정정: ① `no see X` → `I don't see X`. 부정은 조동사 `do` 로 만들고, 주어를 생략하려면 `and no sign of X` 처럼 명사구로 가야 한다. ② `and also` 는 중복이니 둘 중 하나만. ③ 문장 부호가 `. .` 로 겹쳤다.
- 더 나은 표현: The console shows the coordinate-calibration warning, and there's no `reposition: 더블클릭 recenter` line at all. Can we get to the bottom of it?
- 왜: "보인다/안 보인다"를 `I see` / `I don't see` 로 반복하는 대신 콘솔을 주어로 세우면(`The console shows ...`) 두 증상이 같은 출처에서 나온 관찰로 묶인다. 없는 쪽은 `there's no X at all` 이 자연스럽고 `at all` 이 "한 줄도"를 담는다. `We have to fix this issue` 는 명령에 가까우니, 원인이 아직 불명일 때는 `Can we get to the bottom of it?`(원인부터 파자)이 실제 요청에 더 맞는다.

### 카드 21 — 레이트 리밋 해제를 요청하기
- 내가 쓴 영어: "the rate limit occurs when people request fail-issue/devices. can we remove the rate-limit for the pages in the recipe-status (it tend to request lots of data from the backend)"   (출처: transcript:[user] skewnono-v3-nuxt df011192)
- 정정: ① `it tend` → `they tend`. 앞의 `the pages` 를 받으므로 복수 주어이고, 단수라도 3인칭 현재는 `tends` 다. ② `the rate limit occurs` 는 어색하다 — 제한은 "발생"하는 게 아니라 사람이 "걸린다". `we hit the rate limit` 또는 `users get rate-limited`.
- 더 나은 표현: Users are getting rate-limited when they hit `fail-issue/devices`. Can we exempt the recipe-status pages from the limit? They pull a lot of data from the backend by design.
- 왜: `remove the rate-limit for X` 는 "X 에 대해 제한을 없애라"로 읽혀 기능 자체를 지우는 것처럼 들린다. `exempt X from the limit` 이 실제로 벌어진 일(예외 목록에 추가)과 정확히 맞고, 구현자가 곧바로 그 어휘로 코드를 찾는다. 괄호 안 사족은 독립 문장으로 올리고 `by design` 을 붙이면 "설계상 그런 것이니 버그가 아니다"까지 전달된다.
