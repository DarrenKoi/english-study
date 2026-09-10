# 2026-09-11 — 코칭

## 한글→영어

### 카드 1 — 내가 기대한 그림   (내가 쓴 한글)
- 내가 쓴 한글: "나의 목적은 local LLM model이 api 형태로 연결되고, 장비의 ftp server ip, id, pw, 옵션으로 탐색하고자 하는 path가 주어지면, equipment-data-parser의 기준으로 장비의 data를 다운로드 / 열람 / 정보 추출 / wiki화 등이 이루어질 거라 생각했다."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: What I had in mind was this: an API-served local LLM, plus a machine's FTP host, credentials, and optionally a path to walk — and from there the parser downloads, reads, extracts, and turns it into a wiki page.
- 왜 이렇게: 한국어 원문은 조건절이 길게 이어지다 맨 끝에 "~거라 생각했다"가 붙는다. 영어에서 같은 순서로 쓰면 동사가 너무 늦게 나와 문장이 무너진다. `What I had in mind was this:` 로 결론 틀을 먼저 세우고 콜론 뒤에 재료를 늘어놓으면 순서가 뒤집혀도 읽힌다. "ip, id, pw" 는 영어로 묶어 `credentials` 한 단어가 자연스럽고, "옵션으로"는 부사 `optionally` 로 붙인다. "~이 이루어질 거라"는 무생물 수동을 그대로 옮기지 말고 주체(`the parser`)를 세워 능동으로 돌리는 편이 훨씬 짧다.

### 카드 2 — 진행이 왜 이렇게 느린가   (내가 쓴 한글)
- 내가 쓴 한글: "실제로 이 작업을 요청하면, 각 스텝별로 test py 파일을 만들고 테스트하면서 매우 느리게 진행되고 있는데, 원래 그런 스텝이 필요한건가? letters가 20까지 있는데, 몇시간 동안 04 단계까지밖에 진행을 못하고 있다."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: In practice it crawls — every step gets its own test file before anything moves. Is that step actually necessary? There are twenty letters, and after several hours we're only through 04.
- 왜 이렇게: "매우 느리게 진행되고 있다"를 `is progressing very slowly` 로 옮기면 밋밋하다. `it crawls` 한 단어가 답답함까지 나른다. "원래 ~인가?"의 "원래"는 `originally` 가 아니라 `actually` 나 `really` 다 — 시점이 아니라 당연함을 묻고 있다. 마지막 문장의 "~까지밖에 못하고 있다"는 영어에 대응 구조가 없어 `only through 04` 로 옮긴다. `through` 는 "거기까지 끝냈다"를 한 전치사로 처리한다.

### 카드 3 — 빠를 줄 알았다   (내가 쓴 한글)
- 내가 쓴 한글: "ftp_hanlder가 있기 때문에 빠르게 장비의 data를 탐색하고 진행할거라 생각했음."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: I assumed `ftp_handler` would let us walk the machine's files quickly and just keep moving.
- 왜 이렇게: "~라 생각했음"은 `I thought` 도 되지만, 결과적으로 빗나간 기대를 말할 때는 `I assumed` 가 정확하다 — 검증 없이 전제했다는 뉘앙스가 들어간다. "~가 있기 때문에"를 `Because ftp_handler exists,` 로 시작하면 딱딱하니, 도구를 주어로 올려 `would let us …` 로 돌린다. "탐색하고"는 파일 트리를 훑는 맥락이라 `explore` 보다 `walk` 가 이 분야 표준어다.

### 카드 4 — 실제 파이프라인은 하나뿐   (고급 한글 · 번역)
- 한글 원문: "몇 시간을 쓴 04까지 중 실제 파이프라인은 03 하나뿐이고, 그마저 가짜 FTP 서버를 세우는 데 절반이 갔다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: Of everything through 04 — hours of work — only 03 is actual pipeline, and half of that went into standing up a fake FTP server.
- 번역 포인트: "그마저"가 어렵다. 영어에 한 단어 대응이 없어 `and half of that` 로 대명사 `that` 이 앞 항목을 받게 하고, 양보의 뉘앙스는 문맥에 맡긴다. "절반이 갔다"의 "가다"는 `went into` 다 — 시간·노력이 어디로 흘러갔는지 말할 때의 관용이고, `was spent` 보다 아깝다는 감정이 살아 있다. "세우는"은 서버라서 `build` 가 아니라 `stand up` 이 맞다.

### 카드 5 — 문을 잠갔다   (고급 한글 · 번역)
- 한글 원문: "필요한 mtime은 같은 패키지 200줄 옆 `list_details()`에 이미 있는데, 편지가 그 문을 잠갔다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: The mtime you need is already there in `list_details()`, two hundred lines away in the same package — and the letter locked that door.
- 번역 포인트: "200줄 옆"은 직역하면 어색하다. `two hundred lines away` 로 거리 표현을 쓰면 "코앞인데"라는 함의까지 따라온다. "~인데"는 역접이 약해서 `but` 보다 대시(—)가 낫다. 대시는 앞을 뒤엎지 않고 결정타만 얹는다. "문을 잠갔다"는 은유가 영어에서도 그대로 통해서 `locked that door` 를 살렸다 — 은유는 통할 때만 직역한다.

### 카드 6 — 함대 API 의 대가   (고급 한글 · 번역)
- 한글 원문: "1대짜리 함대를 위해 함대 API를 쓰느라 1대용 API가 이미 갖고 있는 메타데이터를 잃었다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: To run a fleet of one, we went through the fleet API — and lost the metadata the single-host API already had.
- 번역 포인트: "1대짜리 함대"는 그 자체가 모순 어법이라 영어에서도 `a fleet of one` 로 살려야 맛이 산다. "~쓰느라"의 대가 뉘앙스는 `-ing` 분사구로는 안 나오니, `we went through X — and lost Y` 로 두 동사를 나란히 놓고 대시로 대가를 드러낸다. "1대용 API"는 `single-host API` 처럼 하이픈 복합어로 만드는 게 영어답다.

## 영어 다듬기

### 카드 1 — 포트를 하네스에 붙이기
- 내가 쓴 영어: "how can I use 8006 port (qwen model) with harness? how can I enable in opencode?"   (출처: transcript:[user] llm-serving)
- 정정: `8006 port` → `port 8006` (숫자를 붙인 명사는 영어에서 뒤에 온다 — `port 8006`, `room 302`, `chapter 4`). `with harness` → `with a harness` / `with my harness` (가산명사에 관사 필수). `how can I enable in opencode?` → `enable` 은 타동사라 목적어가 필요하다: `enable it`.
- 더 나은 표현: How do I point a coding harness at port 8006 (the Qwen model)? And how do I wire it up in opencode?
- 왜: `use X with Y` 는 뭉뚱그린 표현이라 원하는 게 "설정"인지 "연결"인지 안 드러난다. `point A at B` 는 클라이언트를 엔드포인트로 향하게 한다는 뜻이라 이 상황의 표준어다. 설정 작업 전반은 `wire up` 이 잘 맞는다. `How can I …` 는 가능성을 묻는 어감이라 절차를 물을 땐 `How do I …` 가 자연스럽다.

### 카드 2 — 뭘 빠뜨렸는지 모르겠다
- 내가 쓴 영어: "somehow, the 8006 is not directly accessible. don't know what I forget to set. just still work with /api/vlm_serve/qwen3.8-26b/v1"   (출처: transcript:[user] llm-serving)
- 정정: `what I forget to set` → `what I forgot to set` (이미 지난 누락이므로 과거형). `just still work with …` → 주어가 빠졌다: `it still works with …` 또는 의도가 "그냥 계속 쓰겠다"라면 `I'll just stick with …`. `the 8006` 의 관사는 빼고 `port 8006`.
- 더 나은 표현: For some reason port 8006 isn't reachable directly, and I can't tell what I've missed. I'll just stick with `/api/vlm_serve/qwen3.8-27b/v1` for now.
- 왜: `somehow` 는 "어떻게든"에 가까워 원인 불명에는 `for some reason` 이 맞다. `don't know what …` 보다 `I can't tell what …` 이 "조사해봤는데 안 잡힌다"는 뉘앙스를 준다. `for now` 를 붙이면 영구 포기가 아니라 잠정 선택임이 드러나 상대의 후속 제안 여지를 남긴다.

### 카드 3 — 초록불은 뜨는데
- 내가 쓴 영어: "in the code server, it show green mark on /proxy/6008/v1 but no response from outside"   (출처: transcript:[user] llm-serving)
- 정정: `it show` → `it shows` (3인칭 단수 -s). `green mark` → `a green dot` / `a green indicator` (관사 + 이 UI 의 통상 명칭). `in the code server` → `in code-server` (제품명이라 관사 없이).
- 더 나은 표현: code-server shows a green dot next to `/proxy/8006/v1`, but nothing answers from outside the pod.
- 왜: `it` 로 시작하면 무엇이 보여주는지 모호하니 주체(`code-server`)를 주어로 올린다. `on` 보다 `next to` 가 포트 목록 UI 를 정확히 그린다. `no response from outside` 는 명사 나열이라 힘이 없다 — `nothing answers` 처럼 동사로 세우면 문장이 살고, `from outside the pod` 로 경계를 밝히면 진단이 훨씬 빨라진다.

### 카드 4 — 결국 원래 방식으로
- 내가 쓴 영어: "all are not working. I might have to stick with vlm_serve method"   (출처: transcript:[user] llm-serving)
- 정정: `all are not working` 은 영어에서 "전부가 안 되는 건 아니다"로도 읽히는 위험한 형태다. 전체 부정은 `none of them work` 로 쓴다. `vlm_serve method` → `the vlm_serve method` (관사).
- 더 나은 표현: None of them work. I may just have to fall back on the `vlm_serve` route.
- 왜: `all … not` 대신 `none` 을 쓰는 습관은 영어 부정문에서 특히 중요하다. `stick with` 자체는 아주 좋은 선택이었고 원어민도 그렇게 쓴다 — 다만 다른 시도가 다 실패한 뒤라면 `fall back on X` 가 "차선으로 물러선다"는 경위까지 담는다. `method` 보다 `route` 가 이 문맥(네트워크 경로)에 정확하다.

### 카드 5 — 기능 제안
- 내가 쓴 영어: "Can we add the feature to download .{image_name}/cond.txt to display the image info? … (not always download to reduce the bandwidth). just click to see the image"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `add the feature` → `add a feature` (처음 언급하는 기능이므로 부정관사). `not always download` → 주어·시제가 없다: `it shouldn't always download` 또는 명사구로 `no eager download`.
- 더 나은 표현: Could we add a button that pulls `.{image_name}/cond.txt` and shows the image info — fetched lazily on click, not eagerly, so we don't waste bandwidth?
- 왜: `the feature to download …` 는 명사가 겹쳐 무겁다. `a button that pulls …` 처럼 실제 UI 를 주어로 세우면 요구사항이 한눈에 잡힌다. "필요할 때만 받기"는 프런트엔드에서 `lazily` / `on click` 이 표준어고, 그 반대말 `eagerly` 를 같이 대비시키면 의도가 오해 없이 전달된다. `Could we …` 는 `Can we …` 보다 한 단계 정중해 제안에 어울린다.

### 카드 6 — 버튼이 너무 작다
- 내가 쓴 영어: "not able to see i button easily. too small. why don't we use the same style as in SEM gallery when you click one of images then you display image info with wafer 위치 이동 / 측정 근거 레이어 and so on."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `not able to see i button easily` → 주어가 빠졌다: `I can't see the ⓘ button easily`. `one of images` → `one of the images` (`one of` 뒤에는 한정된 복수라 the 가 필요하다). `when you click … then you display …` 는 `when` 절에 `then` 이 겹쳐 어색하다 — 하나를 지운다.
- 더 나은 표현: The ⓘ button is too small to spot. Could we reuse the SEM gallery pattern instead — clicking an image opens the full info panel with 위치 이동, 측정 근거 레이어, and the rest?
- 왜: `not able to see … easily` 를 `too small to spot` 으로 바꾸면 증상과 원인이 한 문장에 들어간다. `too + 형용사 + to + 동사` 는 이런 불만을 압축하는 가장 짧은 틀이다. `the same style as in X` 보다 `the X pattern` 이 UI 논의의 관용이고, `and so on` 은 다소 사무적이라 구어에서는 `and the rest` 가 부드럽다.
