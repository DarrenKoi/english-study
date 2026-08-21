# 2026-08-22 — 코칭

## 한글→영어

### 카드 1 — VOC 를 근거로 기능 설명서를 제안하기   (내가 쓴 한글)
- 내가 쓴 한글: "skewnono를 배포했는데 엔지니어들의 VOC는 기능이 너무 많아 어떻게 활용해야 할지 모르겠다이다. intro page에 어떤식으로 사용해야 하는 지 page별 설명문이 필요하다."   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: We've shipped skewnono, and the feedback we're getting from engineers is that there are so many features they can't tell how to actually use it. I think the intro page needs a per-screen walkthrough.
- 왜 이렇게: "VOC 는 ~이다"를 `the VOC is that ~` 로 직역하면 영어권 개발 문맥에서 낯설다. VOC(Voice of Customer)는 제조·품질 쪽 사내 용어라 사외에서는 `the feedback we're getting` 이나 `what users are telling us` 로 푸는 편이 안전하다. "너무 많아 ~모르겠다"의 인과는 `so many … (that) they can't ~` 구문 하나로 붙는다. "설명문"은 정적인 `description` 보다 **따라가며 배우는** `walkthrough` 가 의도에 맞고, "page별"은 `per-screen` 처럼 `per-` 접두로 한 단어에 넣는다.

### 카드 2 — 원인 층을 잘라 보고하기   (내가 쓴 한글)
- 내가 쓴 한글: "설정/ 데이터 게이트는 통과. 원인은 런타임 쪽."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Config and data gates both pass — so it's the runtime, not the setup.
- 왜 이렇게: 명사만 끊어 적은 한국어 메모를 영어로 옮길 때 그대로 명사구로 두면(`Config gate pass. Cause is runtime.`) 전보문처럼 딱딱해진다. 동사를 하나 살려 `both pass` 로 만들면 자연스러운 구어가 된다. "원인은 ~쪽"은 `the cause is on the runtime side` 도 되지만, **X, not Y** 대조로 바꾸면 "그럼 어디가 아니냐"까지 한 번에 전해져 진단 대화에서 훨씬 유용하다.

### 카드 3 — 재현 케이스를 발견했다고 알리기   (내가 쓴 한글)
- 내가 쓴 한글: "룰에 적용되는 recipe들 중에 WAFER 13개 측정 중인데 룰 위배로 인식되는 케이스들을 발견했어. debugging이 필요해."   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: I'm seeing recipes that measure WAFER at 13 points getting flagged as violations even though 13 is within the rule. Can you dig into it?
- 왜 이렇게: "발견했어"를 `I found` 로 옮기면 한 번 본 것처럼 들린다. `I'm seeing` 은 현재진행이라 **지금도 계속 나온다**는 재현성을 실어 주며, 버그 신고에서 압도적으로 흔한 첫 문장이다. "룰 위배로 인식되다"는 이 도메인의 정확한 동사가 `get flagged as` 다 — `be recognized as` 는 사람의 인지를 뜻해 어긋난다. "13개 측정 중인데"의 역접은 `even though` 로 명시해 주는 편이 낫고, "debugging이 필요해"를 `We need debugging` 으로 직역하면 어색하니 `Can you dig into it?` 처럼 요청으로 돌린다.

### 카드 4 — 손쓸 수 없는 상태의 답답함 전하기   (내가 쓴 한글)
- 내가 쓴 한글: "문제 발생했는데 내가 어떤 조치도 못하고 끝날때까지 기다려야하는 문제 발생"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: The real problem is that when something goes wrong, I can't do anything about it — I just have to wait it out.
- 왜 이렇게: "문제 발생"이 한 문장에 두 번 나오는데 뜻이 다르다. 앞은 사고, 뒤는 그 사고를 못 막는다는 **메타 문제**다. 영어는 이걸 `The real problem is that ~` 로 층을 갈라 준다. "어떤 조치도 못하고"는 `can't take any action` 보다 `can't do anything about it` 이 훨씬 자연스럽고, "끝날 때까지 기다려야 한다"는 오늘의 표현 `wait it out` 이 정확히 그 뜻이다. 앞의 `just` 가 무력감을 얹는다.

### 카드 5 — 선택을 상대에게 위임하기   (내가 쓴 한글)
- 내가 쓴 한글: "구현이 쉬운쪽으로 선택해주세요"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: Go with whichever is easier to implement — your call.
- 왜 이렇게: `Please select the easier one to implement` 는 문법은 맞지만 상사가 지시하는 톤이다. `Go with ~` 는 "그걸로 하자"는 결정 어휘라 훨씬 가볍고, `whichever` 하나로 "둘 중 어느 쪽이든"을 처리해 선택지를 다시 나열할 필요가 없다. 끝의 `your call` 은 "네가 정해"를 두 단어로 끝내는 관용구이며, 위임을 명시해 상대가 되묻지 않게 한다.

### 카드 6 — 필수 요건을 못 박기   (내가 쓴 한글)
- 내가 쓴 한글: "recipe version 체크 과정이 반드시 필요 (new version 인지 old version인지 확인 필요)"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: A recipe version check is a hard requirement — we need to know whether the tool is on the current version or an old one.
- 왜 이렇게: "반드시 필요"를 `is definitely needed` 로 하면 강조가 부사에 실려 흐려진다. `a hard requirement` 는 **협상 불가**를 뜻하는 명사구라 요건 문서에서 그대로 쓴다(반대는 `nice to have`). 괄호 안의 부연은 영어에서 대시로 빼는 게 자연스럽고, "new version 인지 old version인지"는 `whether A or B` 로 묶는다. `new version` 을 `the current version` 으로 바꾼 이유는, 비교 대상이 "새것"이 아니라 **최신본**이기 때문이다.

### 카드 7 — 재사용 판단이 실패하는 지점   (고급 한글 · 번역)
- 한글 원문: "재사용 판단에서 가장 흔한 실패가 이 모양입니다 — 함수가 하는 일이 아니라 함수의 이름이 맞아떨어지는 경우."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: This is the most common way reuse goes wrong — the function's name fits the question, but what the function does doesn't.
- 번역 포인트: "이 모양입니다"는 영어에 그대로 옮길 말이 없다. `This is the most common way X goes wrong` 이라는 틀로 갈아타면 "모양"이 `way` 에 흡수된다. "A가 아니라 B"를 `not A but B` 로 직역하면 강조가 약한데, **긍정을 먼저 놓고 부정을 뒤에 붙이는** `the name fits …, but what it does doesn't` 순서가 영어의 리듬에 맞다. 끝의 `doesn't` 는 `doesn't fit` 의 반복을 피한 대동사 생략이며, 짧게 닫히는 만큼 타격이 커진다.

### 카드 8 — 설계가 결함을 만든 게 아니라 드러냈다   (고급 한글 · 번역)
- 한글 원문: "레이아웃 설계가 잠복 결함을 드러낸 것이지 만든 게 아닙니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: The layout design surfaced a latent defect; it didn't create one.
- 번역 포인트: "~한 것이지 ~한 게 아니다"는 한국어가 즐겨 쓰는 정정 구문인데, 영어에서 `It is A, not B` 로 옮기면 명사구가 되어 동사의 힘이 죽는다. 동사 두 개를 세미콜론으로 나란히 두면 대비가 살아난다. "드러내다"의 정확한 짝은 `reveal` 보다 `surface` 다 — 물속에 있던 것이 수면 위로 올라온다는 그림이라 `latent`(잠복한)와 어울린다. 마지막 `one` 은 `a latent defect` 를 받아 반복을 피한 부정대명사다.

### 카드 9 — mock 이 버그를 가려 놓았다   (고급 한글 · 번역)
- 한글 원문: "이 버그 유형은 mock 이 구조적으로 가려 놓은 것이고, 사무실 데이터에서는 그대로 터집니다."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: This whole class of bug is one the mock structurally hides from us — and it will fire as-is against office data.
- 번역 포인트: "이 버그 유형"은 `this bug type` 보다 `this class of bug` 가 관용적이다(`a class of` = 한 갈래). "가려 놓은 것이고"의 완료 뉘앙스는 `hides from us` 라는 **현재시제**로 충분하다 — 지금도 계속 가리고 있기 때문이며, `has hidden` 을 쓰면 이미 끝난 일로 읽힌다. "그대로 터집니다"의 "그대로"는 `as-is`(손대지 않은 상태로)가 정확하고, "터지다"는 폭발 어휘 `blow up` 보다 결함이 발현된다는 뜻의 `fire` 가 이 문맥에 맞는다. 미래를 `will` 로 단언한 것은 화자가 확신하고 있기 때문이다.

## 영어 다듬기

### 카드 1 — 데이터 출처를 확인하는 질문
- 내가 쓴 영어: "do we use v3_df_sem_avail from redis to display in 장비 상태, 미연결 장비 pages?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `display in ... pages` → `display on ... pages`. 화면·페이지 위에 무언가를 보여줄 때는 전치사가 `on` 이다(`on the screen`, `on that page`). `in` 은 문서·책 안의 내용을 가리킬 때 쓴다.
- 더 나은 표현: Do we read `v3_df_sem_avail` from Redis to populate the 장비 상태 and 미연결 장비 pages?
- 왜: `use ... to display` 는 뜻이 통하지만 두 동작(읽기·그리기)이 뭉개진다. `read X to populate Y` 는 데이터 흐름을 출처→화면 순서로 세워 주며, `populate`(값을 채우다)는 화면에 뿌리는 동작의 표준 동사다. 열거는 쉼표만으로 끝내지 말고 마지막 항목 앞에 `and` 를 넣는다.

### 카드 2 — 어떤 상황에서 실행하는지 묻기
- 내가 쓴 영어: "let me test with diagnose_correction_gates.py In what circumstance should I run the py file? commit and push both"   (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `In what circumstance` → `Under what circumstances`. 이 관용구는 전치사가 `under` 이고 거의 항상 복수형이다. ② 앞 문장 끝에 마침표가 빠져 두 문장이 붙었다.
- 더 나은 표현: Let me try `diagnose_correction_gates.py`. Under what circumstances should I run it? Commit and push both, please.
- 왜: `test with X` 는 X 를 **도구로 삼아 다른 것을 시험한다**는 뜻이라, X 자체를 돌려 보려는 의도와 어긋난다. `try X` 면 충분하다. 앞에서 파일 이름을 댔으니 뒤는 `the py file` 대신 대명사 `it` 으로 받는 게 자연스럽다.

### 카드 3 — 기능 제안을 조건과 함께 던지기
- 내가 쓴 영어: "When we have align fail occurs (not about meas fail), can we display the align OM, SEM images in the page ... We can keep the images for a day (since we only display the alarm for 20 mins, I think it is enough)."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `When we have align fail occurs` — `have`(사역·소유)와 `occurs`(자동사) 두 개가 겹쳐 동사가 둘이다. `When an align fail occurs` 또는 `When we get an align fail` 중 하나만 골라야 한다. ② `(not about meas fail)` → `(not a meas fail)`. `about` 은 화제를 가리키므로 여기서는 불필요하다. ③ `in the page` → `on the page`.
- 더 나은 표현: When an align fail comes in — an align fail, not a meas fail — can we surface the OM and SEM align images on the live-alarm page, cached in MinIO? A one-day retention should be plenty, since we only show the alarm for 20 minutes.
- 왜: 괄호로 밀어 넣은 단서를 대시 한 쌍으로 올리면 본문 무게가 유지되어 오해를 확실히 막는다. `display` 를 `surface` 로 바꾸면 "숨어 있던 것을 꺼내 보여준다"는 뜻이 더해져 기능 제안에 어울린다. `I think it is enough` 는 자신 없어 들리므로 `should be plenty` 로 바꾸면 판단은 유지하되 근거가 있는 톤이 된다.

### 카드 4 — 다른 도구를 써 보라고 권하기
- 내가 쓴 영어: "you can consult with /oc-discuss to get the live-alarm solution robust too."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `consult with` 는 사람과 상의할 때 쓴다. 도구·문서는 전치사 없이 `consult X`. ② `get + 목적어 + 형용사` 는 "그렇게 되도록 만들다"인데 이 자리에는 `make ~ robust` 가 맞다. `get the solution robust` 는 비문에 가깝다.
- 더 나은 표현: Feel free to run `/oc-discuss` on the live-alarm design too, to harden it.
- 왜: `you can ~` 은 문자 그대로 "할 수 있다"라 허가인지 권유인지 모호하다. `Feel free to ~` 가 권유임을 분명히 한다. 형용사 `robust` 를 동사 `harden`(견고하게 만들다) 하나로 접으면 문장이 짧아지고, 보안·안정성 문맥의 표준 동사라 의도가 정확히 전달된다.

### 카드 5 — 이미 적용했는지 확인하는 질문
- 내가 쓴 영어: "have we applied the rule for WAFER and its son parameters are exempted from the measurement rule in device-statistics? I still see them as WAFER violate the rules (measuring 13points)"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① 문장 구조가 중간에 갈아탔다. `the rule for WAFER and its son parameters` 까지는 명사구인데 갑자기 `are exempted` 라는 정동사가 나온다. 명사구 뒤에 내용을 붙이려면 동격의 `that` 절이 필요하다 — `the rule that WAFER and its son parameters are exempt from ~`. ② `I still see them as WAFER violate the rules` 는 `see A as B`(A를 B로 여기다)에 절이 들어가 깨졌다. `I'm still seeing WAFER flagged as violating the rule` 로 고친다. ③ `13points` → `13 points`.
- 더 나은 표현: Did we ever apply the rule that exempts WAFER and its son parameters from the measurement cap? I'm still seeing WAFER flagged as a violation at 13 points.
- 왜: 형용사 `exempt` 는 be동사와 함께 쓰는 게 기본이고(`is exempt from`), `exempted` 는 "누가 면제해 줬다"는 동작을 가리킨다. 규칙이 주어일 때는 능동 `the rule that exempts ~` 가 가장 짧다. `Did we ever ~` 의 `ever` 는 "한 번이라도 한 적 있느냐"를 담아, 실제로 적용된 적 없던 이 상황에 정확히 맞았다.

### 카드 6 — 더 나은 구조를 제안해 달라고 부탁하기
- 내가 쓴 영어: "can you think of better idea to organize by combining align_images and debug_images? while I run @poc/workflow_3/monitor/align_fail_monitor?"   (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `better idea` → `a better idea`. 가산명사 단수에는 관사가 필요하다. ② `while I run ...?` 가 물음표 뒤에 따로 떨어져 조각 문장이 됐다. 앞 문장에 붙이거나 완전한 문장으로 세워야 한다.
- 더 나은 표현: Can you think of a better way to organize this by merging `align_images` and `debug_images`? Note I've got `align_fail_monitor` running right now.
- 왜: `a better idea to organize` 는 `idea` 뒤에 목적어가 없어 허전하다. `a better way to organize this` 가 자연스럽다. 마지막 조각은 시간 조건이 아니라 **주의 사항**이었으므로, `Note (that) ~` 로 독립시키면 의도가 살아난다. 실제로 이 정보가 "지금은 배포하면 안 된다"는 결론을 만들었으니, 곁가지가 아니라 본문으로 올릴 값어치가 있었다.

### 카드 7 — 예전에 정한 예외를 되짚기
- 내가 쓴 영어: "we have exempted some recipe with some suffix that are exempted from the rule?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `exempted` 가 한 문장에 두 번 나와 뜻이 겹친다. 뒤의 관계절을 지운다. ② `some recipe` → `some recipes`. `some` 뒤의 가산명사는 복수다. ③ `some recipe ... that are` — 선행사가 단수인데 동사가 복수라 수가 어긋난다(②를 고치면 함께 해결된다).
- 더 나은 표현: Didn't we exempt recipes with certain suffixes from that rule?
- 왜: `some` 을 두 번 쓰면 "뭔가 있었던 것 같은데"라는 흐릿함이 문장에 남는다. 두 번째를 `certain` 으로 바꾸면 "특정한 몇몇"이라는 윤곽이 생긴다. 확인 질문은 `we have ~?` 보다 부정의문문 `Didn't we ~?` 가 자연스럽다 — 기억을 확인하는 뉘앙스가 붙고, 상대가 "맞다/아니다" 어느 쪽으로도 답하기 쉬워진다.

### 카드 8 — 원격 제어 중 마우스가 잠기는 증상 설명
- 내가 쓴 영어: "while it moves mouse in the remote monitor, the mouse is locked that I cannot control."   (출처: transcript:[user] auto_recipe_creator)
- 정정: ① `moves mouse` → `moves the mouse`. ② `in the remote monitor` → `on the remote machine`. 모니터는 표시 장치라 그 "안"에서 마우스가 움직이지는 않는다. ③ `locked that I cannot control` — 결과절을 이끌려면 `so ... that ...` 이 짝을 이뤄야 한다. `so locked that I can't control it` 이거나, 더 쉽게 `locked, so I can't control it`.
- 더 나은 표현: While it's driving the cursor on the remote machine, my own mouse is locked out — I can't move it at all.
- 왜: `it moves the mouse` 는 반복 동작 한 번을 가리키는 반면, 실제 증상은 **계속되는 상태**라 진행형 `it's driving` 이 맞다. `drive`(장비를 조작하다)는 자동화 문맥의 표준 동사다. `locked out`(밖으로 잠겨 나옴)은 `locked` 보다 "내 것인데 내가 못 쓴다"는 억울함까지 담는다.

### 카드 9 — 둘 중 하나를 고르는 질문에 답하기
- 내가 쓴 영어: "Q9: yes. good idea with (ii)."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: (문법 오류 없음)
- 더 나은 표현: Q9: go with (ii) — the separate prefix.
- 왜: 문법은 멀쩡한데 뜻이 갈렸다. (i)이냐 (ii)냐를 묻는 **양자택일 질문에 `yes` 로 답하면** 앞의 선택지를 고른 것으로 읽히는데, 뒤에서 (ii)를 칭찬해 모순이 생겼고 상대가 되물어야 했다. 영어에서 A-or-B 질문에 `yes`/`no` 는 원칙적으로 답이 되지 않는다. 고른 쪽을 이름으로 말하고, 번호만으로는 헷갈리니 `(ii) — the separate prefix` 처럼 **한 마디 요약을 덧붙이는** 습관이 오해를 없앤다.

### 카드 10 — 정리 작업을 조건부로 지시하기
- 내가 쓴 영어: "check worktrees and if their jobs are done, clean up"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: (문법 오류 없음 — 메모체 명령문으로 자연스럽다)
- 더 나은 표현: Check the worktrees, and if their work has landed, clean them up.
- 왜: `clean up` 은 자동사로 쓰면 "정리 좀 해라"라는 막연한 말이 되고, 목적어 `them` 을 넣어야 대상이 확정된다. `jobs are done` 은 "작업이 끝났다"까지만 말하는데, git 문맥에서 실제 조건은 **main 에 안착했는가**이므로 `has landed` 가 정확하다. 오늘 정독 단락 2의 `the landing record` 와 같은 계열의 동사다.
