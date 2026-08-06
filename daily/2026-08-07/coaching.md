# 2026-08-07 — 코칭

## 한글→영어

### 카드 1 — 구현 선택지를 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "어떤 방식으로 구현할 수 있을까? 선택지가 궁금해."   (출처: transcript:[user] skewnono chat RAG 브레인스토밍)
- 자연스러운 영어: How could we build this? I'd like to see the options before we commit to one.
- 왜 이렇게: "궁금해"를 `I'm curious`로 옮기면 감정 표현이 되어 요청이 흐려진다. 영어 회의에서는 `I'd like to see the options`처럼 **원하는 산출물**을 말하는 쪽이 훨씬 자연스럽다. `How could we …`의 could 는 "지금 정하자"가 아니라 "가능성을 훑자"는 신호를 준다.

### 카드 2 — 상대 의견에 동의하며 범위를 정하기   (내가 쓴 한글)
- 내가 쓴 한글: "(A)에 해당됩니다. 너의 말대로 실제 계측 데이터는 skewnono가 직접 관로하는게 좋을 것 같아."   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: It's (A). And you're right — the live measurement data should stay with skewnono.
- 왜 이렇게: "너의 말대로"를 `As you said`로 직역하면 인용에 가까워 밋밋하다. `You're right —`가 동의를 먼저 확실히 찍고 넘어간다. "직접 관장한다"는 소유를 뜻하므로 `stay with X`(그대로 X가 쥔다)가 `manage directly`보다 결정 뉘앙스에 맞는다. 참고로 원문의 "관로"는 "관장"의 오타.

### 카드 3 — 결정을 되짚어 확인하기   (내가 쓴 한글)
- 내가 쓴 한글: "그럼 다시 원안대로 하는게 통제를 하는데 있어서 더 좋은거지?"   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: So sticking with the original plan gives us more control — is that right?
- 왜 이렇게: 한국어의 "~거지?"는 문장 끝의 확인 어미인데, 영어에서 이걸 통째로 의문문으로 만들면 자신 없어 보인다. **평서문으로 주장을 세우고 뒤에 짧은 확인구**(`is that right?` / `right?`)를 붙이는 형태가 원어민의 기본형이다. "원안대로 하다"는 `stick with the original plan`이 관용이다.

### 카드 4 — 전제를 정리하고 필요 조건만 확인하기   (내가 쓴 한글)
- 내가 쓴 한글: "동일한 opensearch에 RAG data를 올릴 것이고, 거기에서 hybrid search로 chunk를 추출하면 되는거니까, 서로 어떤 meta data, section, page, locator 등등 정보만 일치하면 되는거지?"   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: We'll index the RAG data into the same OpenSearch cluster and pull chunks out with hybrid search — so all we really need to agree on is the field set: metadata, section, page, locator. Is that the whole list?
- 왜 이렇게: "~하면 되는거니까"라는 긴 전제를 그대로 붙이면 영어 문장이 무너진다. 대시로 전제와 질문을 끊는 게 안전하다. "정보만 일치하면 된다"의 **~만**은 `all we really need to agree on is …` 구문이 정확히 받아낸다. 끝을 `Is that the whole list?`로 좁히면 상대가 빠진 항목을 짚어주기 쉬워진다 — 실제로 그 답이 다섯 개 항목으로 돌아왔다.

### 카드 5 — 판단 근거를 대고 의견을 구하기   (내가 쓴 한글)
- 내가 쓴 한글: "계속 업데이트 되는 케이스 이기 때문에 지금처럼 skewnono에 박기 어려울 것 같아. 어떻게 생각해?"   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: Since those sources keep getting updated, I don't think we can hard-wire them into skewnono the way we're doing now. Does that hold up?
- 왜 이렇게: "박다"는 `hard-wire`(코드에 고정해 넣다)나 `bake in`이 대응한다. "지금처럼"은 `the way we're doing now`로 뒤에 붙여야 자연스럽다. 그리고 "어떻게 생각해?"를 `What do you think?`로 끝내면 열린 질문이 되어 답이 흩어진다. **내 근거가 성립하는지 물을 때는 `Does that hold up?`**이 훨씬 날카롭다 — 실제로 그 근거가 반박당했다.

### 카드 6 — 아직 확정 못 한 이유를 설명하기   (내가 쓴 한글)
- 내가 쓴 한글: "schema도 당장 정할 필요 없는건가? … 단어들이 정확히 와닿지 않고 있어서"   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: Do we need to lock the schema down now? The labels don't quite sit right with me yet.
- 왜 이렇게: "정하다"가 스키마와 붙으면 `lock down`(더는 못 바꾸게 확정)이 뉘앙스까지 맞는다. "와닿지 않는다"는 `I don't understand`가 아니라 **어휘가 몸에 안 붙는 감각**이므로 `don't sit right with me`가 정확하다. 끝의 `yet`이 "아직 그렇다, 곧 정리될 것"이라는 여지를 남긴다.

### 카드 7 — 숙제를 나눠 맡기   (내가 쓴 한글)
- 내가 쓴 한글: "이거는 RAG 만드는 쪽에서 제대로 정한 뒤에 알려줄게. chunk 크기 중첩등을 테스트하는 것도 잊지 않을게"   (출처: transcript:[user] 같은 세션)
- 자연스러운 영어: I'll come back to you once the RAG side has settled it properly. And I won't forget to test chunk size and overlap.
- 왜 이렇게: "알려줄게"를 `I'll let you know`로 해도 되지만, 뒤에 조건절이 붙을 때는 `I'll come back to you once …`가 더 매끄럽다. `once`는 `after`보다 "그게 끝나는 대로"의 즉시성이 있다. "잊지 않을게"는 `I won't forget to …` 그대로가 자연스럽고, 앞에 `And`를 두어 두 약속을 한 호흡으로 묶었다.

### 카드 8 — 결과 한 줄 보고   (내가 쓴 한글)
- 내가 쓴 한글: "wrong_row 없음."   (출처: transcript:[user] auto_recipe_creator 벤치 결과)
- 자연스러운 영어: No wrong_row — zero across the board.
- 왜 이렇게: 한국어의 명사형 종결("없음")은 영어에서 `No X.` 단독으로 옮기면 무뚝뚝하기만 하고 정보가 없다. **범위를 한 마디 덧붙이는 것**(`across the board` = 전 항목에 걸쳐)이 관건이다. 상대가 "몇 건 중에?"를 되묻지 않게 된다.

### 카드 9 — 서비스 경계를 긋는 기준   (고급 한글 · 번역)
- 한글 원문: "서비스 경계는 데이터가 얼마나 자주 바뀌느냐가 아니라 운영 책임과 권한 모델이 어디서 갈라지느냐로 긋는 게 맞습니다."   (출처: transcript:[assistant] skewnono chat RAG)
- 자연스러운 영어: Service boundaries should be drawn where operational ownership and the permission model diverge, not by how often the data changes.
- 번역 포인트: "긋는 게 맞습니다"의 당위를 `should`로 받고, 한국어의 `A가 아니라 B` 순서를 영어에서는 **B를 먼저, `not A`를 뒤로** 돌렸다. 영어는 긍정 주장을 앞세우고 부정 대비를 후치하는 쪽이 훨씬 읽힌다. "어디서 갈라지느냐"는 명사절로 풀지 말고 관계부사 `where`로 붙이면 문장이 반으로 줄어든다. "운영 책임"은 responsibility 보다 `ownership`이 소프트웨어 조직 문맥의 표준어다.

### 카드 10 — 스키마의 진짜 비용   (고급 한글 · 번역)
- 한글 원문: "스키마 항목의 진짜 비용은 '정하기'가 아니라 '바꾸기'이고, 그 비용은 값이 어디까지 새어나갔는지로 결정됩니다."   (출처: transcript:[assistant] 같은 세션)
- 자연스러운 영어: The real cost of a schema field isn't choosing it — it's changing it later, and that cost is set by how far the value has leaked.
- 번역 포인트: 따옴표로 강조된 두 동명사를 영어에서도 `choosing` / `changing`으로 대칭시키되, 대시로 끊어 두 번째를 강조 위치에 놓았다. "새어나가다"는 `leak`가 그대로 통한다 — 값이 인덱스 밖 여러 소비자에게 퍼진 상태를 가리키는 비유가 두 언어에서 같다. `later`를 넣어야 "나중에 바꿀 때"라는 시간축이 살아난다.

### 카드 11 — 라벨링이 망설여지는 이유   (고급 한글 · 번역)
- 한글 원문: "라벨링할 때마다 망설여진다면 그건 어휘가 나쁜 게 아니라 축이 하나로 눌려 있는 것입니다."   (출처: transcript:[assistant] 같은 세션)
- 자연스러운 영어: If you hesitate every time you label something, the vocabulary isn't the problem — you've collapsed several axes into one.
- 번역 포인트: "눌려 있다"의 피동을 그대로 옮기면(`is pressed into one`) 뜻이 안 산다. 차원을 하나로 뭉갠다는 뜻의 관용 동사는 `collapse`이며, 여기서는 능동 `you've collapsed`로 돌려 책임 소재를 부드럽게 지목했다. `isn't the problem`은 "나쁜 게 아니라"를 옮기는 가장 흔한 완충 표현이다.

## 영어 다듬기

### 카드 1 — RAG를 붙이자는 첫 제안
- 내가 쓴 영어: "For the chat page, we have to make RAG that is to be connected to the llm so that users search the real tool's contents.."   (출처: transcript:[user] skewnono)
- 정정: `make RAG` → `build a RAG pipeline` (RAG는 기법 이름이라 관사 없이 목적어로 쓰기 어렵다). `that is to be connected` → `connected` (be to be 부정사는 과도한 격식이며 여기선 어색). `so that users search` → `so that users can search` (목적절에는 조동사가 필요하다).
- 더 나은 표현: For the chat page, we need a RAG layer wired into the LLM so users can search what's actually in the tool manuals.
- 왜: `wire A into B`가 "붙여 연결하다"를 한 단어로 처리해 관계절이 사라진다. `the real tool's contents`는 소유격이 겹쳐 모호하니 `what's actually in the tool manuals`처럼 풀면 "진짜 내용"의 강조까지 함께 산다.

### 카드 2 — 증상 보고
- 내가 쓴 영어: "I have several times of failure (sometimes it works) to access to the tool when align failure occurs in RCS."   (출처: transcript:[user] auto_recipe_creator)
- 정정: `several times of failure` → `failed several times` (failure를 명사로 세면 `several failures`여야 하고, `times of failure`는 비문). `access to the tool` → `access the tool` (동사 access 는 전치사를 취하지 않는다 — 명사 access 일 때만 `access to`).
- 더 나은 표현: Connecting to the tool fails intermittently when an align alarm fires in RCS — it does work sometimes.
- 왜: "several times … (sometimes it works)"가 말하려는 건 빈도가 아니라 **간헐성**이라 `intermittently` 한 단어가 정확하다. 그리고 주어를 사람(`I`)이 아니라 동작(`Connecting to the tool`)으로 두면 장애 보고가 훨씬 객관적으로 읽힌다.

### 카드 3 — 모델을 하나로 줄이자는 조건
- 내가 쓴 영어: "If one of them is only needed, then I want to drop one of the vlm model for this project."   (출처: transcript:[user] 같은 세션)
- 정정: `is only needed` → `is enough` 또는 `if only one of them is needed` (only 의 위치가 틀려 "필요하기만 하다"로 읽힌다 — only 는 수식할 말 바로 앞에 둔다). `one of the vlm model` → `one of the VLMs` (of 뒤에는 복수).
- 더 나은 표현: If one model turns out to be enough, I'd like to drop the other one from this project.
- 왜: `turns out to be`가 "벤치를 돌려 보니 그렇더라"라는 **검증 후 판명**의 뉘앙스를 담는다. 그리고 둘 중 하나를 버리는 상황이므로 `one of them`보다 `the other one`이 지시가 분명하다.

### 카드 4 — 표본을 늘리자는 요청
- 내가 쓴 영어: "let's add more tool names to be more precise."   (출처: transcript:[user] 같은 세션)
- 더 나은 표현: Let's add more tool names so the numbers mean something.
- 왜: 문법 오류는 없다. 다만 `to be more precise`는 영어에서 "좀 더 정확히 말하자면"이라는 **삽입 관용구**로 먼저 읽혀서, 의도한 "정밀도를 높이자"와 충돌한다. 목적을 `so the numbers mean something`처럼 결과로 바꾸면 그 충돌이 사라지고 요청의 이유까지 전달된다. 격식을 원하면 `to make the measurement more reliable`.

### 카드 5 — 두 번째 벤치를 제안
- 내가 쓴 영어: "Do you think mai-ui__mai-ui comes with the better result to read a tool's monitor? can we benchmark this case too?"   (출처: transcript:[user] 같은 세션)
- 정정: `comes with the better result` → `performs better` (come with 는 "~이 딸려 온다"는 뜻이라 성능 비교에 안 맞는다). `the better` → 비교 대상이 명시되지 않았으니 `better`.
- 더 나은 표현: Do you think mai-ui__mai-ui would also do better at reading a tool window? Can we bench that case too?
- 왜: 아직 안 해본 일이므로 `would`가 맞다 — `does`는 이미 아는 사실을 묻는 어감이 된다. `also`를 넣으면 "list 에서 이겼는데 여기서도?"라는 논리 연결이 드러난다. `bench`는 benchmark 의 동사형 축약으로, 개발자끼리는 이쪽이 더 자연스럽다.

### 카드 6 — 로그 분류 오류 신고
- 내가 쓴 영어: "in admin/logs, I found that /api/cdsem/live-alarm is enlisted as feature \"cdsem\". fix this. live-alarm is live-alarm. also in activity. (do they connected right?)"   (출처: transcript:[user] skewnono)
- 정정: `is enlisted as` → `is listed as` (enlist 는 "입대하다·협력을 얻다"라서 뜻이 전혀 다르다). `do they connected right?` → `are they wired up correctly?` (do + 과거분사는 비문. 상태를 묻는 자리라 be동사).
- 더 나은 표현: In admin/logs, `/api/cdsem/live-alarm` is being filed under the feature `cdsem` — it should be `live-alarm`. Same for the activity ranking; can you check both are wired up correctly?
- 왜: `be filed under`가 "어느 분류로 들어간다"를 정확히 짚는다. `fix this`만 던지는 대신 `it should be …`로 기대값을 붙이면 상대가 되묻지 않는다. 끝의 확인 질문은 `can you check …`으로 감싸면 지시와 질문이 한 문장에 정리된다.

### 카드 7 — 재실행 결과 보고와 다음 요청
- 내가 쓴 영어: "I re-ran the bench_tool_locator. and got main-ui__mai-ui is the best. ui-venus__mai-ui is 0.583. Can I now test in the tool's monitor …"   (출처: transcript:[user] auto_recipe_creator)
- 정정: `and got main-ui__mai-ui is the best` → `and mai-ui__mai-ui came out best` (`got` + that절 없는 절은 비문이고, `main-ui`는 `mai-ui`의 오타). `test in the tool's monitor` → `test on the tool window` (화면 위에서 시험하므로 in 이 아니라 on).
- 더 나은 표현: I re-ran bench_tool_locator: mai-ui__mai-ui came out best again, and ui-venus__mai-ui dropped to 0.583. Can I move on to the tool window now?
- 왜: 두 결과를 콜론 뒤에 나란히 두면 보고가 한 덩어리로 읽힌다. `again`과 `dropped to`가 **이전 실행과의 변화**를 드러내 상대가 해석할 근거를 준다 — 실제로 그 변화가 답변의 핵심이 되었다. `move on to`는 "다음 단계로 넘어가다"의 관용구.

### 카드 8 — 가정이 확정으로 바뀜을 알리기
- 내가 쓴 영어: "in mag-pixel, for GT2000, we have mags 600K~1000K. now they are not 가정 anymore. they are confirmed."   (출처: transcript:[user] skewnono)
- 더 나은 표현: For GT2000 in mag-pixel, the 600K–1000K mags are confirmed now — they're no longer assumptions.
- 왜: 문법 오류는 없다. 다만 `not … anymore`를 별도 문장으로 두면 부정이 먼저 오고 사실이 나중에 온다. **확정 사실을 앞세우고 부정을 대시 뒤로 미루면** 정보의 무게가 제자리를 찾는다. `no longer`는 `not anymore`보다 한 단계 격식이 있고 문어에 어울린다. 범위 표시는 물결(`~`)이 아니라 en dash(`–`)가 영어 관례다.
