# 2026-09-05 — 코칭

## 한글→영어

### 카드 1 — 소형 LLM 도입 가능성 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "workflow_3 이후에 소형 llm을 이용한다면 workflow 판단에 도움이 될 수 있을까?"   (출처: transcript:[user] auto_recipe_creator 2c85695a)
- 자연스러운 영어: After workflow_3, would a small LLM help with the decision-making in the workflow?
- 왜 이렇게: "이용한다면 ~ 도움이 될 수 있을까"를 `if we use ... could it help` 로 다 옮기면 조건절이 무겁다. 영어는 가정을 `would` 하나에 실어 조건절을 지운다. "판단"은 judgment 로 직역하면 개인의 안목처럼 들리므로, 시스템이 내리는 결정이면 `decision-making` 이 정확하다. 더 짧게는 `Could a small LLM take over some of the workflow's decisions after workflow_3?` 도 자연스럽다.

### 카드 2 — 검토 중인 모델 알려 주기   (내가 쓴 한글)
- 내가 쓴 한글: "qwen3.8 27b을 고려하고 있어."   (출처: transcript:[user] auto_recipe_creator 2c85695a)
- 자연스러운 영어: I'm thinking of Qwen3.8 27B.
- 왜 이렇게: `I am considering Qwen3.8 27B.` 도 맞지만 앞 대화의 흐름을 잇는 짧은 답이니 `I'm thinking of ...` 가 어울린다. 상대가 방금 "새 모델을 띄울 필요 없다"고 했으니 `I actually have Qwen3.8 27B in mind.` 처럼 `actually` 를 넣으면 "이미 후보가 있다"는 반전이 살아난다.

### 카드 3 — 대안을 제안하기   (내가 쓴 한글)
- 내가 쓴 한글: "VLM이기 보다는 소형 LLM (vlm 기능이 있는 Qwen3.8 27B)를 도입해서 workflow에 판단을 맡기는 건 어떨까?"   (출처: transcript:[user] auto_recipe_creator 2c85695a)
- 자연스러운 영어: Rather than a VLM, what about bringing in a small LLM that also has vision (Qwen3.8 27B) and letting it make the workflow's decisions?
- 왜 이렇게: "~보다는"은 `Rather than X,` 로 문두에 두면 대조가 바로 보인다. "도입하다"는 `introduce` 보다 `bring in` 이 회화체에 맞고, "판단을 맡기다"는 `entrust the judgment to` 처럼 딱딱하게 가지 말고 `let it make the decisions` 로 푼다. "vlm 기능이 있는"은 `with VLM capability` 보다 `that also has vision` 이 짧고 자연스럽다.

### 카드 4 — 공모전 작성 요청   (내가 쓴 한글)
- 내가 쓴 한글: "2026년 AX 업무 혁신 사례 공모전이 있고 거기에 제출해야해. … 우리가 작성한 doc 문서들을 참고해서 다음 내용을 기입하면 좋겠어."   (출처: transcript:[user] auto_recipe_creator 9948b438)
- 자연스러운 영어: There's a 2026 AX work-innovation case contest I need to submit to. I'd like you to fill in the sections below, drawing on the docs we've written.
- 왜 이렇게: "공모전이 있고 거기에 제출해야 해"는 두 문장으로 나누지 말고 관계절 `I need to submit to` 로 붙인다. 전치사 to 가 문장 끝에 남는 구조가 구어에서는 정상이다. "참고해서"는 `referring to` 보다 `drawing on` 이 "재료로 삼아"라는 뜻에 가깝다. "기입하면 좋겠어"의 완곡한 부탁은 `I'd like you to` 가 딱 그 온도다.

### 카드 5 — 진행 방식 지시   (내가 쓴 한글)
- 내가 쓴 한글: "주제 별로 작성 진행 부탁. 중간 중간 모르면 물어봐도 좋음"   (출처: transcript:[user] auto_recipe_creator 9948b438)
- 자연스러운 영어: Please work through it section by section, and feel free to check with me whenever something's unclear.
- 왜 이렇게: "주제별로"는 `by topic` 보다 문서 구조가 정해져 있으니 `section by section` 이 맞다. "물어봐도 좋음"은 허락이므로 `you can ask` 보다 `feel free to check with me` 가 자연스럽고, "모르면"은 `if you don't know` 대신 `whenever something's unclear` 로 쓰면 상대를 탓하는 어감이 없어진다.

### 카드 6 — 확인된 사실 전달   (내가 쓴 한글)
- 내가 쓴 한글: "투입 인원 2명. … 실측 대응 시간 1분 미만 확인. 완주 건수는 3건. (이제 현업 배치 시작)."   (출처: transcript:[user] auto_recipe_creator 9948b438)
- 자연스러운 영어: Two people on the project. Measured response time is under a minute, confirmed. Three cases completed end to end, and we're now starting the production rollout.
- 왜 이렇게: 메모체 한글은 영어에서도 명사구로 끊어도 되지만, 숫자마다 동사를 하나씩 주면 훨씬 읽기 쉽다. "완주"는 `completed end to end` 가 "처음부터 끝까지 한 번에"를 담는다. "현업 배치"는 `deploy to the field` 보다 `production rollout` 이 사내 용어에 가깝고, 문장 끝의 `confirmed` 한 단어가 "확인"의 무게를 그대로 전한다.

### 카드 7 — 그대로 써도 된다고 허락하기   (내가 쓴 한글)
- 내가 쓴 한글: "사내 시스템명은 그대로 써도 됩니다."   (출처: transcript:[user] auto_recipe_creator 9948b438)
- 자연스러운 영어: The internal system names can stay as they are.
- 왜 이렇게: "써도 됩니다"를 `you can use` 로 옮기면 누가 쓰는지가 튀어나온다. `can stay as they are` 는 주어를 이름 자체로 두어 "손대지 말라"는 결정만 남긴다. 더 짧게는 `Keep the internal system names as is.` 도 된다.

### 카드 8 — 닫힌 표를 LLM 으로 조회하면   (고급 한글 · 번역)
- 한글 원문: "닫힌 표를 LLM으로 조회하면 얻는 건 없고 잃는 건 재현성입니다."   (출처: transcript:[assistant] auto_recipe_creator 2c85695a)
- 자연스러운 영어: Querying a closed table through an LLM gains you nothing and costs you reproducibility.
- 번역 포인트: "얻는 건 없고 잃는 건 ~"의 대구를 `gains you nothing and costs you X` 로 동사 둘의 병렬로 옮긴다. 주어는 동명사구 `Querying ...` 하나로 세워 "~하면"의 조건절을 없앴다. "닫힌 표"는 앞 문맥에서 열거형 status 표를 뜻하므로 `a closed table` 로 직역해도 통하고, 더 풀면 `a fixed lookup table` 이다.

### 카드 9 — 측정 계층 위에 얹는 층   (고급 한글 · 번역)
- 한글 원문: "통계를 만들려고 지은 계층 위에 통계를 못 만들게 하는 층을 얹는 꼴입니다."   (출처: transcript:[assistant] auto_recipe_creator 2c85695a)
- 자연스러운 영어: That amounts to stacking a layer that defeats measurement on top of the layer you built precisely to enable it.
- 번역 포인트: "~하는 꼴이다"는 `amounts to` 가 "결국 그런 셈"이라는 평가를 정확히 준다. "통계를 만들려고 지은"은 `built to produce statistics` 보다 `built precisely to enable it` 처럼 앞 명사(measurement)를 it 으로 받아 반복을 피한다. 한글의 "통계"를 두 번 쓰는 리듬은 영어에서 `defeats ... / enable it` 의 반의어 대비로 대신했다.

### 카드 10 — 판단 기준 하나   (고급 한글 · 번역)
- 한글 원문: "판단 기준 하나: 틀렸을 때 장비가 아니라 사람이 손해를 보는 곳."   (출처: transcript:[assistant] auto_recipe_creator 2c85695a)
- 자연스러운 영어: One test: put it where a wrong answer costs a person's time, not a machine's.
- 번역 포인트: "판단 기준"을 `criterion` 으로 옮기면 무겁다. 영어 기술 글에서는 `One test:` 나 `The rule of thumb:` 처럼 짧은 명사 뒤에 콜론을 두는 편이 흔하다. "손해를 보다"는 주체를 바꿔 `a wrong answer costs ...` 로 오답을 주어에 세우면 문장이 능동적이 된다. "장비가 아니라 사람이"는 `a person's time, not a machine's` 로 소유격을 반복해 대구를 살린다.

### 카드 11 — 표기 구분 보고   (고급 한글 · 번역)
- 한글 원문: "문서에 근거가 없는 값은 [확인 필요], 벤치·테스트 측정값은 [검증], 환산·계획값은 [목표]로 구분해 표기했습니다."   (출처: transcript:[assistant] auto_recipe_creator 9948b438)
- 자연스러운 영어: I tagged each figure by provenance: [needs confirmation] where the docs give no basis, [verified] for bench or test measurements, and [target] for derived or planned values.
- 번역 포인트: 세 갈래 분류를 옮길 때는 먼저 `tagged each figure by provenance:` 처럼 분류의 축을 한 단어(provenance)로 선언하고 콜론 뒤에 항목을 나열한다. 한글은 "값은 ~로"를 세 번 반복하지만 영어는 `where` / `for` / `for` 로 전치사만 바꿔 리듬을 준다. "환산"은 `converted` 가 아니라 `derived` 가 "실측에서 계산해 낸 값"이라는 뜻에 맞는다.

## 영어 다듬기

### 카드 1 — 지연을 "enhance" 한다고 쓴 질문
- 내가 쓴 영어: "how can I enhance the latency of qwen3.8?"   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 정정: `enhance the latency` → `reduce the latency`. enhance 는 "더 크게·좋게 만들다"라 지연을 늘리겠다는 뜻이 된다. 낮춰야 좋은 지표(latency, error rate, cost)에는 reduce / cut / bring down 을 쓴다.
- 더 나은 표현: What are my options for cutting qwen3.8's latency?
- 왜: `How can I` 는 방법 하나를 묻는 느낌이고, 실제로 원한 건 선택지 목록이었다. `What are my options for` 가 그 의도에 맞고, 답도 자연스럽게 목록 형태로 돌아온다.

### 카드 2 — 두 GPU 배치 방법 묻기
- 내가 쓴 영어: "and how can we set if we use the H200 2ea for the qwen? along with one for mai-ui and the other one for paddleOCR."   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 정정: `how can we set if` → `how would we set it up if`. set 은 목적어가 필요하고, 구성을 뜻할 땐 `set up` 이다. `2ea` 는 한국 산업 문서의 수량 표기라 영어권에서는 안 통한다(`both H200s`). `the qwen` 의 정관사는 모델 이름 앞에서 빠진다.
- 더 나은 표현: And how would we configure it if qwen used both H200s, with mai-ui and paddleOCR each sharing one of the cards?
- 왜: 원문은 "둘 다 qwen 에" 와 "하나는 mai-ui, 다른 하나는 paddleOCR" 가 충돌해 읽힌다. `each sharing one of the cards` 로 "공유"를 명시하면 의도한 TP=2 + 공존 배치가 한 문장에 정리된다.

### 카드 3 — 장단점 묻기
- 내가 쓴 영어: "what is the pros and cons when I run the qwen model in the both GPU while running the two other models"   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 정정: `what is the pros and cons` → `what are the pros and cons` (복수 주어). `in the both GPU` → `on both GPUs` (GPU 위에서 돌리므로 on, both 앞에 the 없음, 복수형).
- 더 나은 표현: What are the trade-offs of running qwen across both GPUs alongside the other two models?
- 왜: pros and cons 는 틀리지 않지만 `trade-offs` 가 "얻는 것과 잃는 것이 맞물려 있다"는 엔지니어링 어감을 준다. `across both GPUs` 는 텐서 병렬로 "걸쳐" 돌린다는 뜻이 살고, `alongside` 가 "동시에 돌아가는 다른 모델과 함께"를 한 단어로 처리한다.

### 카드 4 — NVLink 확인 보고
- 내가 쓴 영어: "it is NVlink."   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 더 나은 표현: Confirmed, the topo shows NVLink.
- 왜: 문법 오류는 없다. 다만 상대가 "topo 를 확인해 달라"고 했으니 `Confirmed` 로 시작하면 "네가 시킨 확인을 했고 결과는 이렇다"가 한 번에 전달된다. 표기는 NVLink (L 대문자).

### 카드 5 — 현 배치 유지 결정
- 내가 쓴 영어: "I will keep the qwen on the single GPU.. for now"   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 정정: `the qwen` → `qwen` (고유명 앞 정관사 제거). `the single GPU` → `a single GPU` (특정 GPU 가 아니라 "한 장" 이라는 뜻). 마침표 두 개(`..`)는 영어에서 주저함으로 읽히니 쉼표나 대시로.
- 더 나은 표현: I'll leave qwen on a single GPU for now.
- 왜: keep 도 되지만 `leave ... as is` 계열의 leave 가 "바꾸지 않고 둔다"는 결정을 더 정확히 담는다. `for now` 를 문장 끝에 그대로 두면 "나중에 다시 볼 수 있다"는 여지가 살아 있다.

### 카드 6 — 남은 RAM 보고
- 내가 쓴 영어: "I have about 4 GB free after the three models are running"   (출처: transcript:[user] llm_serving 1aaa1e3c)
- 더 나은 표현: With all three models warm, I've got about 4 GB of headroom.
- 왜: 문법 오류는 없다. `after ... are running` 은 시제가 살짝 어색한데(after 뒤엔 완료된 사건이 자연스럽다), `with all three models warm` 처럼 상태를 with 구로 만들면 그 문제가 사라진다. `headroom` 은 "여유 공간"의 엔지니어링 단어라 free 보다 대화 상대의 어휘와 맞는다.

### 카드 7 — scripts 폴더 요청
- 내가 쓴 영어: "make the folder named scripts where suggest to utilize qwen3.8 model to the maximum. how to use the thinking / effort. I want to tast its capability"   (출처: transcript:[user] llm_serving 86c08517)
- 정정: `where suggest to utilize` 는 관계절에 주어가 없다 → `that shows how to get the most out of`. `tast` → `test`. `qwen3.8 model` → `the qwen3.8 model` 또는 그냥 `qwen3.8`.
- 더 나은 표현: Create a `scripts/` folder that shows how to get the most out of qwen3.8, including how to drive thinking and effort. I want to put its capabilities to the test.
- 왜: "최대로 활용"은 `utilize to the maximum` 보다 `get the most out of` 가 관용구다. 두 번째 문장이 명사구로 떠 있으니 `including how to ...` 로 앞 문장에 붙인다. "capability 를 시험해 보고 싶다"는 `put ... to the test` 가 정확히 그 뜻이다.

### 카드 8 — 경로 되돌리기 요청
- 내가 쓴 영어: "amend real site path now. the issue solved when I restart the pod of the cloud"   (출처: transcript:[user] llm_serving 86c08517)
- 정정: `the issue solved` → `the issue was solved` / `got resolved` (solve 는 타동사라 수동태 필요). `when I restart` → `when I restarted` (과거 사건). `the pod of the cloud` → `the cloud pod` (명사 수식은 of 구보다 앞에 붙이는 명사가 자연스럽다).
- 더 나은 표현: Revert the real site path now. The issue went away once I restarted the cloud pod.
- 왜: amend 는 "고쳐서 다듬다"라 방향이 모호하고, 실제 의도는 "원래 자리표시자로 되돌리기"였다. `revert` 가 그 뜻을 정확히 짚어 상대가 해석을 선언할 필요가 없어진다. `went away once` 는 "재시작하자마자 사라졌다"는 인과와 시점을 한 번에 준다.
