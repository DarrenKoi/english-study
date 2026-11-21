# 2026-11-22 — 코칭

오늘 내가 쓴 한국어는 Radmin 장비를 SecureVDI 너머에서 자동화할 수 있는지 묻는 글입니다. "~있음", "~확인 했음", "~예정"처럼 명사로 끊은 메모체가 많고 주어가 거의 없어요. 영어로 옮길 때는 주어(`I`, `we`, `some tools`)를 세우고, "A -> B -> C" 로 적은 접속 경로를 `through`, `via`, `from … to` 로 풀어야 합니다. "컨트롤", "foreground", "headless" 처럼 이미 영어인 낱말이 문장 안에서 어떤 품사로 들어가는지도 함께 봅니다. 내가 영어로 쓴 문장은 없어서 영어 다듬기는 건너뜁니다.

## 한글→영어

### 카드 1 — RCS 가 아닌 Radmin 기반 장비   (내가 쓴 한글)
- 내가 쓴 한글: "fab 장비 중에 RCS가 아닌 Radmin 기반으로 사용되는 장비들이 있음"   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: Some of the fab tools are accessed through Radmin rather than RCS.
- 왜 이렇게: "~중에 …이 있음"은 `There are tools that …` 보다 `Some of the fab tools …` 로 주어를 바로 세우는 쪽이 짧습니다. "RCS 가 아닌 Radmin"은 `Radmin rather than RCS` 또는 `Radmin, not RCS`. "기반으로 사용되는"을 `are used based on Radmin` 으로 옮기면 어색해요. 실제 뜻은 원격으로 붙는 수단이니 `are accessed through` 나 `run on Radmin` 이 맞습니다. 반도체 현장에서는 장비를 `equipment`(셀 수 없음)보다 `tools` 라고 부르는 일이 많습니다.

### 카드 2 — headless 로 컨트롤할 수 있나?   (내가 쓴 한글)
- 내가 쓴 한글: "이 경우 Radmin viewer로 접속해야 하는데, radmin viewer를 headless로 컨트롤 (view, mouse keyboard등등) 할 수 있나?"   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: For those, we have to connect with Radmin Viewer. Is there a way to drive Radmin Viewer headlessly, meaning screen capture plus mouse and keyboard input?
- 왜 이렇게: "~해야 하는데, ~할 수 있나?"는 배경과 질문이 한 문장에 붙어 있습니다. 영어는 둘로 끊는 편이 읽기 쉬워요. `headless` 는 형용사라서 "headless 로"는 부사 `headlessly` 나 `in headless mode` 가 됩니다. 프로그램을 코드로 조작한다는 뜻의 "컨트롤"은 `control` 도 되지만 자동화 맥락에서는 `drive` 를 많이 씁니다(`drive the browser`). 괄호 속 예시는 `meaning …` 이나 `i.e., …` 로 풀고, "등등"은 `and so on` 을 붙이기보다 대표 항목만 적는 편이 깔끔합니다.

### 카드 3 — 다음과 같은 구조를 거쳐야 함   (내가 쓴 한글)
- 내가 쓴 한글: "회사에서 팹 내의 장비를 사무실에서 Radmin으로 컨트롤 할 수 있는데 다음과 같은 구조를 거쳐야 함. 사무실 PC -> SecureVDI (web app) 접속 -> SecureVDI 상에서 Radmin 실행 -> Radmin 거쳐서 장비 모니터 접속."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: At work, we can control the fab tools from the office with Radmin, but only by going through the following chain: office PC → log in to SecureVDI (a web app) → launch Radmin inside SecureVDI → reach the tool's screen through Radmin.
- 왜 이렇게: "~할 수 있는데 …거쳐야 함"은 `can …, but only by -ing` 로 받으면 "되긴 되는데 조건이 붙는다"가 한 번에 나옵니다. "구조를 거치다"의 "구조"는 `structure` 가 아니라 여러 단계가 이어진 경로라서 `chain`, `path`, `hops` 가 맞아요. "사무실에서"는 `from the office` 입니다. 조종하는 사람이 있는 자리라서 `in` 이 아니라 `from` 을 씁니다. "SecureVDI 상에서"는 `inside SecureVDI` 나 `in the SecureVDI session`.

### 카드 4 — ~까지 확인했음   (내가 쓴 한글)
- 내가 쓴 한글: "RCS를 쓸 때는 사무실 PC -> RCS -> 장비 모니터 접속이 바로 되어서 headless로 컨트롤 할 수 있는 것 까지 확인 했음."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: With RCS, the office PC connects straight to the tool's screen, and I've already confirmed that headless control works.
- 왜 이렇게: "RCS 를 쓸 때는"은 `When we use RCS` 보다 `With RCS,` 가 짧습니다. "바로 되어서"는 중간 단계가 없다는 뜻이라 `straight` 나 `directly`. "~까지 확인했음"의 "까지"는 "거기까지는 진도가 나갔다"는 말인데, 영어에서는 현재완료와 `already` 가 그 일을 합니다. 범위를 더 드러내려면 `I've gotten as far as confirming that …`. 확인한 내용은 `that headless control works` 처럼 절로 풀면 "할 수 있는 것"이라는 명사화가 사라집니다.

### 카드 5 — VDI 를 통해서만 볼 수 있음   (내가 쓴 한글)
- 내가 쓴 한글: "하지만 Radmin을 쓸 때는 secureVDI (가상 윈도우 환경)을 통해서 Radmin viewer를 볼 수 있음."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: With Radmin, though, Radmin Viewer is only reachable through SecureVDI, a virtual Windows desktop.
- 왜 이렇게: 원문에는 "만"이 없지만 뜻은 "통해서만"이라 `only` 를 넣어야 문제 제기가 됩니다. 넣지 않으면 그냥 가능하다는 말로 읽혀요. "볼 수 있음"을 `can see` 로 옮기면 눈으로 보인다는 뜻뿐이라 `is reachable`, `can be accessed` 가 맞습니다. "하지만"은 문두 `But` 대신 문장 가운데 `though` 를 끼우면 앞 문장과 대비가 부드럽게 이어집니다. 괄호 풀이는 쉼표 뒤 동격 명사구로 붙입니다.

### 카드 6 — A 하거나, B 하거나, 또는 C 하거나   (내가 쓴 한글)
- 내가 쓴 한글: "Radmin viewer를 사무실 PC에서 direct로 보거나, 아니면 장비의 radmin server를 viewer를 통하지 않고 컨트롤 할 수 있거나, 또는 별도 cloud 서버를 운영해서 (이 경우 secureVDI를 통하지 않고 장비에 통신 가능) 장비를 컨트롤 하거나.."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: I can think of three options: opening Radmin Viewer directly on the office PC, controlling the tool's Radmin server without going through the viewer, or running a separate cloud server that can reach the tools without SecureVDI.
- 왜 이렇게: 한국어는 "~하거나"를 세 번 이으면 되지만 영어는 세 항목의 꼴을 맞춰야 합니다. 여기서는 전부 동명사(`opening`, `controlling`, `running`)로 맞췄고, 앞에 `three options:` 를 둬서 나열임을 미리 알립니다. "direct 로"는 부사 `directly`. "viewer 를 통하지 않고"는 `without going through the viewer`, 더 짧게는 `bypassing the viewer` 인데 `bypass` 는 보안 통제를 피해 간다는 인상을 줄 때가 있어서 맥락을 가려 씁니다. 괄호 속 설명은 `a server that can reach …` 관계절로 넣으면 문장이 끊기지 않아요.

### 카드 7 — 현실적으로 가능한지, 시도해볼 만한지   (내가 쓴 한글)
- 내가 쓴 한글: "어떤 방법이 현실적으로 가능한 지 또는 시도해볼만 한지 궁금해."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: Which of these is realistically feasible, or at least worth trying?
- 왜 이렇게: "궁금해"를 `I'm curious which …` 로 옮겨도 되지만 답을 바라는 말이라 직접 의문문이 더 자연스럽습니다. 조금 공손하게는 `I'd like to know which of these …`. "현실적으로 가능한"은 `realistically feasible`, 구어로는 `actually doable`. "시도해볼 만한"은 `worth trying` 이고 `worth` 뒤에는 늘 `-ing` 가 옵니다(`worth to try` 는 틀림). `or at least` 를 넣으면 "확실하지 않아도 해 볼 만은 한"이라는 한 단계 낮춘 기준이 살아납니다.

### 카드 8 — 전용 클라이언트를 띄우는 런처   (내가 쓴 한글)
- 내가 쓴 한글: "웹이 실제로는 전용 클라이언트를 띄우는 런처야. 웹에서 로그인해서 토큰을 인정 받으면 vdi 런처가 실행이 돼."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: The web page is really just a launcher for a dedicated client. Once you log in on the web and your token is validated, the VDI launcher starts.
- 왜 이렇게: "실제로는 ~야"는 겉보기와 다르다는 말이라 `is really just` 나 `turns out to be` 가 맞습니다. "전용"은 `dedicated`, "띄우다"는 `launch` 인데 주어를 `launcher` 로 잡았으니 `a launcher for …` 로 줄였어요. "토큰을 인정 받으면"은 `the token is validated`(유효성 확인), 권한 쪽이면 `you're authenticated`. "~하면 …가 실행돼"는 순서가 요점이라 `If` 보다 `Once` 가 어울립니다.

### 카드 9 — 내가 확인했던 거는 ~만 했던 거야   (내가 쓴 한글)
- 내가 쓴 한글: "내가 확인했던 거는 VDI 상에서 스크린 샷 기반으로 마우스, 키보드 입력만 했던거야."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: All I've actually tested is screenshot-based mouse and keyboard input inside the VDI.
- 왜 이렇게: "내가 한 거는 ~뿐이야"는 `All I've done is …` 가 그대로 맞습니다. `What I tested was only …` 보다 "그것밖에 안 해 봤다"는 한정이 또렷해요. "스크린샷 기반으로"는 하이픈 형용사 `screenshot-based` 로 명사 앞에 붙입니다. "VDI 상에서"는 `on` 이 아니라 `inside the VDI`. 세션 안쪽이라는 위치가 이 논의의 쟁점이라서 `inside` 가 정확합니다.

### 카드 10 — 항상 foreground 에 있어야 하는 거지?   (내가 쓴 한글)
- 내가 쓴 한글: "점유 문제는, 사무실 PC에서 VDI를 통해서 radmin viewer를 컨트롤 하려면 항상 VDI가 foreground에 있어야 하는 거지?"   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: About tying up the PC: to control Radmin Viewer through the VDI from the office PC, the VDI window has to stay in the foreground the whole time, right?
- 왜 이렇게: "~하는 거지?"는 내 이해가 맞는지 확인하는 말이라 평서문 끝에 `, right?` 를 붙입니다. 부가의문문 `doesn't it?` 보다 구어에서 흔해요. "점유 문제는,"은 화제를 꺼내는 말이므로 `About …:` 이나 `On the … issue,` 로 엽니다. "점유"는 PC 를 다른 일에 못 쓰게 된다는 뜻이라 `tie up the PC` 가 잘 맞습니다(`occupy` 는 자리·공간 쪽). "항상 있어야"는 `has to stay in the foreground` 로, `be` 보다 `stay` 가 계속 유지한다는 뜻을 살립니다. `foreground` 앞에는 `the` 를 붙입니다.

### 카드 11 — 끊으면 안 될 거야   (내가 쓴 한글)
- 내가 쓴 한글: "연결을 끊으면 안될거야."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: I don't think it'll survive a disconnect.
- 왜 이렇게: 이 말은 금지("끊지 마")가 아니라 예측("끊으면 동작 안 할 것")입니다. `You must not disconnect.` 로 옮기면 뜻이 달라져요. 예측은 `It won't work if we disconnect.` 가 가장 평이하고, `I don't think …` 로 부정을 앞에 두면 추측의 어감이 삽니다. `survive a disconnect` 는 "끊겨도 살아남다"라는 개발자 말투로, 세션·프로세스·상태에 두루 씁니다(`survive a restart`).

### 카드 12 — ~하면 가능하다고 들었음   (내가 쓴 한글)
- 내가 쓴 한글: "2번 시험할 때. 1:python 설치 가능. VLM 서버는 방화벽 해제 요청하면 가능하다고 들었음."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: On the checks for option 2 — (1) Python can be installed. I've been told the VLM server will be reachable once we request a firewall exception.
- 왜 이렇게: "들었음"은 `I heard` 도 되지만 담당자에게서 안내받았다는 뜻이면 `I've been told` 나 `I'm told` 가 더 믿을 만하게 들립니다. "방화벽 해제"는 방화벽을 끄는 것이 아니라 한 경로만 여는 것이라 `a firewall exception` 또는 `have the port opened`. `disable the firewall` 로 쓰면 방화벽 전체를 내린다는 뜻이 됩니다. "설치 가능"은 `Python can be installed`, 내가 주어라면 `we're allowed to install Python`(허가라는 뜻이 분명해짐).

### 카드 13 — 엔지니어가 자리에 있을 때만 실행할 예정   (내가 쓴 한글)
- 내가 쓴 한글: "2: 확인해야 함. 3: 세션 끊을 가능성 있음. 장비 컨트롤은 엔지니어가 자리에 있을 때만 실행할 예정."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: (2) Still needs checking. (3) The session may well get dropped. We only plan to run tool control while an engineer is at their desk.
- 왜 이렇게: "확인해야 함"은 `needs checking` 또는 `needs to be checked`(`need + -ing` 가 수동의 뜻). "끊을 가능성 있음"은 `may get dropped`, 가능성이 꽤 높다고 보면 `may well`. 세션은 스스로 끊기는 것이 아니라 끊김을 당하니 `get dropped` 나 `time out` 을 씁니다. "자리에 있을 때"는 `at their desk`, `present`, `on hand` 가 있고 `in the seat` 은 쓰지 않습니다. "~할 예정"은 `plan to`, `only` 는 `plan` 앞에 두는 것이 구어에서 자연스러워요. "자리에 있는 동안 내내"라서 `when` 보다 `while` 이 맞습니다.

### 카드 14 — 가장 큰 병목   (내가 쓴 한글)
- 내가 쓴 한글: "VDI안에서 git pull이 안됨. 사실 코드, 프로그램 전달이 가장 큰 병목 from 사무실 to VDI"   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: `git pull` doesn't work inside the VDI. Honestly, the biggest bottleneck is getting code and programs from the office into the VDI.
- 왜 이렇게: "~이 가장 큰 병목"은 `The biggest bottleneck is + 동명사` 로 받습니다. "전달"을 `delivery` 로 옮기면 택배 같아서 `getting … into` 나 `moving … into` 가 맞아요. 끝에 붙인 "from 사무실 to VDI"는 방향을 잘 잡았는데, 경계 안쪽으로 들여보낸다는 뜻이라 `to` 보다 `into` 가 정확합니다. 보안 구역 반입이라는 뜻을 살리려면 `transferring files into the VDI`. "사실"은 `Actually` 보다 속내를 꺼내는 `Honestly,` 나 `To be honest,` 가 이 문맥에 가깝습니다. "안 됨"은 `doesn't work`, 정책으로 막혔다면 `is blocked`.

### 카드 15 — ~할 수 있는지로 진행해야 할 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "일단은 사무실 PC에서 VDI foreground 전략을 사용해서 자동화 할 수 있는 지로 진행해야 할 것 같아."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: For now, I think we should go with the foreground approach on the office PC and see whether the automation works at all.
- 왜 이렇게: "일단은"은 `For now,` 가 가장 가깝습니다(`First of all` 은 순서, `For now` 는 잠정). "~해야 할 것 같아"는 `I think we should` 로, `It seems that we have to` 는 번역투예요. "전략을 사용해서"는 `go with the … approach`. `strategy` 는 사업 계획처럼 크게 들려서 기술 선택에는 `approach` 가 어울립니다. "할 수 있는지로 진행"은 `see whether … works` 로 풀었고, 끝의 `at all` 이 "일단 되기는 하는지"라는 어감을 보탭니다.

### 카드 16 — 못 쓰지만 그래도 feasibility 는 알 수 있으니까   (내가 쓴 한글)
- 내가 쓴 한글: "자동화가 동작하는 동안 엔지니어가 pC를 컨트롤 할 수 없지만 그래도 자동화 프로젝트 feasibility를 알 수 있으니까."   (출처: transcript:[user] auto-recipe-creator e61f3271)
- 자연스러운 영어: The engineer won't be able to use the PC while the automation is running, but it will at least tell us whether the project is feasible.
- 왜 이렇게: "~지만 그래도 ~니까"는 양보 뒤에 이유를 대는 꼴입니다. `but … at least` 가 "그래도 이것만은 건진다"를 받아요. "feasibility 를 알 수 있다"를 `know the feasibility` 로 옮기면 어색하고, `tell us whether … is feasible` 처럼 형용사로 풀거나 `give us a read on feasibility` 로 씁니다. "PC 를 컨트롤할 수 없다"는 사람이 자기 PC 를 쓰는 이야기라 `use the PC` 가 맞습니다. `control` 은 원격 조종 쪽이에요. "동작하는 동안"은 `while … is running`.

### 카드 17 — 접는 것이 맞습니다   (고급 한글 · 번역)
- 한글 원문: "역공학은 비용과 보안 양쪽에서 맞지 않습니다."   (출처: transcript:[assistant] auto-recipe-creator e61f3271)
- 자연스러운 영어: Reverse-engineering it doesn't make sense on either cost or security grounds.
- 번역 포인트: "맞지 않습니다"는 틀렸다는 뜻이 아니라 수지가 안 맞는다는 판단입니다. `is wrong` 이 아니라 `doesn't make sense`, `isn't justified`, `doesn't add up` 을 골라요. "양쪽에서"는 `on both counts` 도 좋고, 부정문이라 `on either … or … grounds` 로 받았습니다. `on … grounds` 는 "~라는 근거에서"로, 판단의 이유를 격식 있게 대는 틀입니다. 같은 답변의 "접는 것이 맞습니다"는 `It's best to drop that option.` 이나 `That one should be shelved.`

### 카드 18 — 승인이 전제이며   (고급 한글 · 번역)
- 한글 원문: "이 경로는 SecureVDI의 감사·녹화 통제를 우회하는 구조입니다. RCS 때의 \"AI 전용 계정 + 방화벽 해제\"처럼 정식 승인이 전제이며, 임의로 경로를 뚫는 것은 권하지 않습니다."   (출처: transcript:[assistant] auto-recipe-creator e61f3271)
- 자연스러운 영어: This route bypasses SecureVDI's audit and recording controls. As with the "dedicated AI account plus firewall exception" we used for RCS, it depends on formal approval, and I wouldn't recommend opening a path on your own.
- 번역 포인트: "~하는 구조입니다"는 `is a structure that …` 로 받지 않고 동사 하나(`bypasses`)로 줄입니다. 한국어의 "~구조다", "~방식이다"는 영어에서 대개 사라져요. "~이 전제이며"는 `presupposes` 가 직역이고 `depends on`, `is contingent on`, `requires … first` 가 더 자주 쓰입니다. "임의로"는 `arbitrarily` 가 아니라 "허락 없이 혼자서"이므로 `on your own` 이나 `without sign-off`. "경로를 뚫다"는 `open a path`, 부정적인 어감을 살리려면 `punch a hole through the firewall`.

### 카드 19 — 얇은 에이전트만 두고 로직은 바깥에   (고급 한글 · 번역)
- 한글 원문: "그러면 VDI 안에는 거의 바뀌지 않는 얇은 에이전트 하나만 두고, 로직은 전부 git이 되는 바깥에 두는 구조가 맞습니다."   (출처: transcript:[assistant] auto-recipe-creator e61f3271)
- 자연스러운 영어: In that case, the right design is to keep only a thin agent that rarely changes inside the VDI, and leave all the logic outside, where git works.
- 번역 포인트: "~하는 구조가 맞습니다"는 `the right design is to …` 로 주어를 먼저 세우고 내용을 to 부정사 둘(`keep …, and leave …`)로 나란히 답니다. "거의 바뀌지 않는"은 `that rarely changes`, "얇은 에이전트"는 `a thin agent`(`thin client` 와 같은 용법). "git 이 되는 바깥"은 쉼표 뒤 `where git works` 로 붙였어요. 장소를 꾸미면서 그곳을 고른 이유까지 말해 주는 비제한 관계절입니다. "그러면"은 `Then` 보다 `In that case` 가 조건을 받아 결론을 낸다는 느낌에 가깝습니다.

### 카드 20 — 제약은 옮겨가는데 문제가 되지 않는다   (고급 한글 · 번역)
- 한글 원문: "이 경우 foreground 제약은 VDI 내부 데스크톱으로 옮겨가는데, 그 데스크톱은 사람이 쓰지 않으니 문제가 되지 않습니다."   (출처: transcript:[assistant] auto-recipe-creator e61f3271)
- 자연스러운 영어: In that setup, the foreground constraint simply moves to the desktop inside the VDI, and since nobody uses that desktop, it stops being a problem.
- 번역 포인트: "제약이 옮겨가다"는 `moves to` 나 `shifts to`. 없어지는 것이 아니라 자리만 바뀐다는 뜻이라 `simply` 를 넣어 "그저 옮겨갈 뿐"을 살렸습니다. "사람이 쓰지 않으니"는 `since nobody uses …` 로, 이미 아는 사실을 이유로 댈 때는 `because` 보다 `since` 가 가볍습니다. "문제가 되지 않습니다"는 `is not a problem` 도 맞지만 `stops being a problem` 이 "전에는 문제였는데 이제는 아니다"라는 변화를 담아요.
