# 2026-11-20 — 코칭

오늘 내가 쓴 한국어는 대부분 질문입니다. Radmin 구성 요소, VNC 라이선스, RFB 확인 방법을 물었습니다. 한국어 질문은 "~는 어떻게 되는가", "~하는 건가"처럼 서술문 끝만 바꾸면 되지만 영어는 의문사와 어순부터 정해야 합니다. 원격 제어 구조를 말할 때 쓰는 `run on`, `be installed on`, `under the hood`, `varies by` 를 챙겨 두세요. 내가 쓴 영어 문장은 없어서 영어 다듬기는 쉽니다.

## 한글→영어

### 카드 1 — 구성 요소는 어떻게 되는가   (내가 쓴 한글)
- 내가 쓴 한글: "radmin으로 팹 내의 장비를 컨트롤 하고 있는데, 그 구성 요소는 어떻게 되는가?"   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: We control the tools in the fab through Radmin. What are its components?
- 왜 이렇게: "~하고 있는데, ~는?"은 배경 문장과 질문 문장으로 끊는 편이 깔끔합니다. "어떻게 되는가"를 `How is …?` 로 옮기면 상태를 묻는 말이 되므로 `What are its components?` 나 `What does the setup consist of?` 로 씁니다. 팹의 "장비"는 현장에서 `tool` 이라고 부르고 일반 문서에서는 `equipment`(셀 수 없음)입니다. "~으로"는 수단이라 `through` 나 `with`, 원격임을 살리려면 `We remote into the fab tools with Radmin` 도 됩니다.

### 카드 2 — 장비에도 설치되어 있어야 하나   (내가 쓴 한글)
- 내가 쓴 한글: "장비 내에도 어떤 서버나 radmin이 설치되어 있어야 하는건가?"   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: Does the tool itself also need some kind of server, or Radmin, installed on it?
- 왜 이렇게: "설치되어 있어야 하다"는 `need + 목적어 + installed` 가 가장 짧습니다(`need something installed`). `Does something have to be installed on the tool as well?` 도 맞습니다. 소프트웨어는 기기 "위에" 깔리므로 전치사는 `in` 이 아니라 `on` 입니다. "장비 내에도"의 "도"는 `itself also` 로 살렸습니다. 제어하는 쪽 말고 제어받는 쪽에도 필요하냐는 뜻이니까요. "어떤 서버"는 `some kind of server`.

### 카드 3 — 내부적으로 VNC를 쓴다   (내가 쓴 한글)
- 내가 쓴 한글: "RCS는 내부적으로 VNC를 사용하고 있어 (licensed 된게 일반적인가? opensource도 있는건가?)"   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: RCS uses VNC under the hood. (Is it usually a licensed product, or are there open-source versions too?)
- 왜 이렇게: "내부적으로"는 `internally` 도 맞지만 "겉으로는 안 보이는 구현"이라는 뜻으로는 `under the hood` 가 개발자 말에 가깝습니다. "licensed 된 게 일반적인가"는 `Is it usually …?` 로 빈도를 묻습니다. "상용"을 분명히 하려면 `commercially licensed` 나 `proprietary`. `open source` 는 명사로 쓸 때 띄우고 명사 앞에서 꾸밀 때 하이픈을 넣습니다(`open-source versions`). 한 단어 `opensource` 는 표준 표기가 아닙니다.

### 카드 4 — 장비마다 다르다   (내가 쓴 한글)
- 내가 쓴 한글: "RCS를 쓸 수도 있고 Radmin으로 쓸 수 도 있고, 팹 장비마다 달라."   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: Some tools are accessed through RCS and others through Radmin; it varies from tool to tool.
- 왜 이렇게: "A일 수도 있고 B일 수도 있고"를 `can … or can …` 으로 옮기면 한 장비에서 둘 다 고를 수 있다는 뜻으로 읽힙니다. 장비별로 정해져 있다는 뜻이면 `Some … and others …` 가 정확합니다. "~마다 다르다"는 `varies from tool to tool`, `varies by tool`, 구어로는 `It depends on the tool.` `others through Radmin` 은 반복되는 `are accessed` 를 생략한 꼴입니다.

### 카드 5 — 인기가 더 많은 편   (내가 쓴 한글)
- 내가 쓴 한글: "회사에서는 Radmin이 인기가 더 많은 편."   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: At our company, Radmin tends to be the more popular of the two.
- 왜 이렇게: "~인 편"의 누그러뜨림은 `tend to` 가 받습니다. 단정하지 않고 경향만 말하는 장치예요. 둘 중 하나를 비교할 때는 `the more popular of the two` 처럼 비교급 앞에 `the` 를 붙입니다. 구어로는 `People here mostly prefer Radmin.` 이 더 편합니다. "인기가 많다"를 `has much popularity` 로 직역하지 않고 형용사 `popular` 로 씁니다.

### 카드 6 — 설명 부탁해   (내가 쓴 한글)
- 내가 쓴 한글: "RFB 설명 부탁해."   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: Can you explain RFB?
- 왜 이렇게: `explain` 은 타동사라 목적어를 바로 붙입니다. `explain about RFB` 는 틀립니다. 듣는 사람을 넣을 때는 `explain RFB to me` 이고 `explain me RFB` 는 안 됩니다. 조금 가볍게는 `Can you walk me through RFB?`, 짧은 개요만 원하면 `Give me a quick rundown of RFB.`

### 카드 7 — ~인지 확인하는 방법   (내가 쓴 한글)
- 내가 쓴 한글: "RCS가 표준 RFB인지 오피스에서 확인하는 방법 알려줘"   (출처: transcript:[user] auto-recipe-creator 168ab999)
- 자연스러운 영어: How can I check from the office whether RCS speaks standard RFB?
- 왜 이렇게: "방법 알려줘"는 `Tell me the method` 보다 `How can I …?` 가 자연스럽습니다. "~인지"는 `whether` 이고 구어에서는 `if` 도 됩니다. 프로그램이 프로토콜을 "쓴다"고 할 때 `speak` 를 자주 씁니다(`speaks HTTP`). "오피스에서"는 사무실 자리에서 원격으로 본다는 뜻이라 `at` 보다 `from the office` 가 맞습니다. `check` 를 격식 있게 올리면 `verify`.

### 카드 8 — 템플릿을 md 로 정리해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "현재 pptx를 만드는 템플릿을 md 파일 형태로 구성해줘. 다른 르포에서도 사용하고 싶어."   (출처: transcript:[user] pm-notes 5ab92045)
- 자연스러운 영어: Write up the template we currently use to build the pptx as a Markdown file. I want to reuse it in other repos.
- 왜 이렇게: "md 파일 형태로 구성하다"는 흩어진 것을 문서로 정리한다는 뜻이라 `write up … as a Markdown file` 이 맞습니다. `compose` 나 `organize into the form of` 는 번역투로 들립니다. "현재 pptx를 만드는 템플릿"은 `the template (that) we currently use to build the pptx` 처럼 관계절로 뒤에서 꾸밉니다. "다른 곳에서도 사용"은 `reuse` 한 단어에 "도"의 뜻까지 들어 있습니다. "르포"는 `repo`(repository 의 준말)입니다.

### 카드 9 — 전문적으로 보이지 않아   (내가 쓴 한글)
- 내가 쓴 한글: "내용에 자기 PC라는게 있는데 전문적으로 보이지 않아. 본인 PC로 수정"   (출처: transcript:[user] pm-notes 5ab92045)
- 자연스러운 영어: The text says "자기 PC," which doesn't sound professional. Change it to "본인 PC."
- 왜 이렇게: "~라는 게 있는데"는 `The text says …` 처럼 무생물을 주어로 둡니다. 글의 어감을 평가할 때는 `look` 보다 `sound` 나 `read` 를 씁니다(`It doesn't read as professional`). 앞 문장 전체를 받는 `, which` 로 두 문장을 이었습니다. 수정 지시는 `Change A to B` 또는 `Replace A with B`. 영어 문서라면 이 구분은 `their own PC` 하나로 끝나서 한국어처럼 격식 차이가 생기지 않습니다.

### 카드 10 — 창이 아니라 픽셀 버퍼   (고급 한글 · 번역)
- 한글 원문: "핵심은 화면을 '창'이나 '버튼'이 아니라 그냥 픽셀 버퍼(framebuffer)로 다룬다는 점입니다. 그래서 OS나 애플리케이션 종류와 무관하게 동작하고, 클라이언트는 화면에 무엇이 있는지 모릅니다."   (출처: transcript:[assistant] auto-recipe-creator 168ab999)
- 자연스러운 영어: The key point is that RFB treats the screen as a plain pixel buffer, not as windows or buttons. That is why it works regardless of the OS or application, and why the client has no idea what is actually on the screen.
- 번역 포인트: 한국어 원문에는 주어가 없지만 영어는 `RFB treats …` 로 주어를 채워야 합니다. "A가 아니라 B로 다룬다"는 `treat X as B, not as A` 로 순서를 뒤집어 긍정을 먼저 말하면 읽기 쉽습니다. "그냥"은 `just` 보다 `plain` 이 "아무 구조 없는"이라는 뜻을 살립니다. "~와 무관하게"는 `regardless of`. "모릅니다"는 `doesn't know` 도 되지만 `has no idea` 가 "전혀"를 더합니다.

### 카드 11 — 서버가 밀어내지 않는다   (고급 한글 · 번역)
- 한글 원문: "서버가 일방적으로 밀어내지 않으므로, 느린 클라이언트는 중간 프레임을 건너뛰고 최신 상태만 받습니다."   (출처: transcript:[assistant] auto-recipe-creator 168ab999)
- 자연스러운 영어: Because the server never pushes updates on its own, a slow client simply skips the intermediate frames and receives only the latest state.
- 번역 포인트: "일방적으로"를 `unilaterally` 로 옮기면 외교 문서처럼 들립니다. 요청 없이 스스로 보낸다는 뜻이라 `on its own` 이 맞습니다. "밀어내다"는 통신 용어 `push` 그대로인데 영어는 목적어가 필요해서 `updates` 를 채웠습니다. "~만 받는다"의 `only` 는 한정하는 말 바로 앞에 둡니다(`receives only the latest state`). `simply` 는 "별다른 처리 없이"라는 어감입니다.

### 카드 12 — 모르고 끼어들 수 있다   (고급 한글 · 번역)
- 한글 원문: "직접 붙으면 RCS의 Connection User 표시나 점유 팝업을 우회하게 되어, 엔지니어가 쓰는 중인 장비에 모르고 끼어들 수 있습니다."   (출처: transcript:[assistant] auto-recipe-creator 168ab999)
- 자연스러운 영어: If you connect directly, you bypass RCS's Connection User indicator and occupancy pop-up, so you could unknowingly barge in on a tool an engineer is using.
- 번역 포인트: "붙다"는 `attach` 보다 `connect` 가 네트워크 접속에 맞습니다. "우회하게 되어"의 "~하게 되다"는 영어에서 따로 옮기지 않고 `you bypass` 로 단언합니다. "모르고"는 `unknowingly`, 구어로는 `without realizing it`. "끼어들다"는 `barge in on` 이 "무례하게 불쑥"이라는 느낌까지 담고, 중립으로는 `interfere with` 입니다. 가능성을 말하는 `could` 가 "~할 수 있습니다"를 받습니다.

### 카드 13 — 결국 ~의 차이   (고급 한글 · 번역)
- 한글 원문: "따라서 장비마다 다르다는 것은 결국 그 장비 PC에 어떤 서버(VNC Server, Radmin Server, 또는 둘 다)가 설치되어 있느냐의 차이입니다."   (출처: transcript:[assistant] auto-recipe-creator 168ab999)
- 자연스러운 영어: So "it varies by tool" really comes down to which server is installed on that tool's PC: VNC Server, Radmin Server, or both.
- 번역 포인트: "결국 ~의 차이입니다"는 `comes down to` 가 딱 맞습니다. 여러 겹을 걷어 내면 남는 한 가지를 말할 때 쓰는 구동사예요. "~느냐"는 간접의문문 `which server is installed` 로 옮기고 어순은 평서문 그대로 둡니다. 한국어의 괄호 나열은 영어에서 콜론 뒤로 빼면 문장 뼈대가 먼저 보입니다. `is a difference of` 로 직역하면 어색합니다.
