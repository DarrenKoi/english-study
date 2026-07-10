# 2026-07-11 — 코칭

## 한글→영어

### 카드 1 — Phase 1 골격 구현 요청   (내가 쓴 한글)
- 내가 쓴 한글: "Phase 1 코드 골격(3-표상 저장 + OpenSearch 색인기) 구현해줘"   (출처: transcript:[user] 62687dfa…)
- 자연스러운 영어: "Please implement the Phase 1 code skeleton — the three-representation store plus the OpenSearch indexer."
- 왜 이렇게: "코드 골격"은 code skeleton(또는 scaffolding). 한국어의 괄호 나열은 영어에서 대시(—) 뒤 명사구 병렬로 풀면 자연스럽습니다. "A + B"의 +는 구어체 영어에서 plus 그대로 써도 좋습니다.

### 카드 2 — Phase 1.5 골격 추가 요청   (내가 쓴 한글)
- 내가 쓴 한글: "Phase 1.5 벤치용 차트-온리 golden 질의셋 골격도 만들어줘"   (출처: transcript:[user] 62687dfa…)
- 자연스러운 영어: "Also scaffold the chart-only golden query set for the Phase 1.5 benchmark."
- 왜 이렇게: "골격을 만들다"는 동사 scaffold 한 단어로 해결됩니다. "~용"은 for the ~, 조사 "도"는 문두 Also가 가장 가볍습니다. chart-only처럼 하이픈 합성어를 만들면 어순이 깔끔해집니다.

### 카드 3 — 데이터셋 분리 보고 + 질문   (내가 쓴 한글)
- 내가 쓴 한글: "두개 data set들을 분리했어. MIN_S=3은 무슨의미야? 지금 1셋은 workflow_3/align_images_golden, 나머지 2 셋은 align_consensus_history에 있어"   (출처: transcript:[user] 66c408dd…)
- 자연스러운 영어: "I've split the two datasets. What does MIN_S=3 mean? Right now one set is in workflow_3/align_images_golden and the other two are in align_consensus_history."
- 왜 이렇게: 방금 마친 일의 보고는 현재완료(I've split)가 기본. "무슨 의미야?"는 What does X mean?(용도를 물으면 What is X for?). "나머지 2셋"은 the other two — 명사를 반복하지 않아도 됩니다.

### 카드 4 — OM 2장·SEM 3장 도메인 사실 공유   (내가 쓴 한글)
- 내가 쓴 한글: "msr에는 OM이미지는 측정 한번에 보통 2장이 만들어지고, SEM 이미지는 보통 3장이 만들어져. 이 점을 알고 있어? modality별로 권장 이미지가 달라야겠지? Align 잡을 때 OM은 두 위치를 잡고 SEM은 3 위치를 잡거든."   (출처: transcript:[user] 66c408dd…)
- 자연스러운 영어: "In msr, a single measurement usually produces two OM images and three SEM images. Were you aware of that? The recommended image count should differ by modality, right? During alignment, OM locks onto two positions and SEM onto three."
- 왜 이렇게: 한국어의 "만들어진다"(수동)는 영어에서 무생물 주어 능동(a measurement produces)이 훨씬 자연스럽습니다. "~겠지?"의 동의 구하기는 부가의문 ", right?"가 정확한 온도. 마지막 문장은 SEM 뒤의 동사를 생략(and SEM onto three)해 병렬을 살렸습니다.

### 카드 5 — 검증 불필요 + 다운로드 계획   (내가 쓴 한글)
- 내가 쓴 한글: "검증은 필요없고, OM과 SEM은 동일한 숫자가 나오지 않으니 이미지 필요 수를 조정해야해. 3건을 기준으로 조사를 해서 다운로드 할거야"   (출처: transcript:[user] 66c408dd…)
- 자연스러운 영어: "No need for the validator. Since OM and SEM don't come in equal numbers, we need to adjust the required image counts. I'll base the survey on three measurements per recipe and download accordingly."
- 왜 이렇게: "~은 필요없고"는 문장 첫머리 No need for ~ 한 마디로 끝납니다. "~을 기준으로"는 base X on Y 구문. "그에 맞춰"는 accordingly 부사 하나로 처리해 문장을 늘리지 않습니다.

### 카드 6 — 업데이트할 것 없나   (내가 쓴 한글)
- 내가 쓴 한글: "@poc/workflow_2/golden_eval_config.example.py 업데이트할 것 없나?"   (출처: transcript:[user] 66c408dd…)
- 자연스러운 영어: "Anything we should update in golden_eval_config.example.py?" (또는 "Does golden_eval_config.example.py need updating?")
- 왜 이렇게: "~할 것 없나?"는 Anything (that) ~? 생략 의문문이 실무 채팅에서 가장 자연스럽습니다. 두 번째 안의 need updating(need + 동명사 = 수동 의미)은 시험에도 나오는 유용한 구문 — need to be updated보다 간결합니다.

### 카드 7 — 순차 정렬이라 전부 중요   (내가 쓴 한글)
- 내가 쓴 한글: "OM과 SEM은 각각 순차적으로 Align Point을 잡기 때문에 (OM, OM, SEM, SEM, SEM) 전부 중요한 요소야. 각각 bench를 돌리는게 맞아. 지금까지 그렇게 하지 않았다는게 좀 놀라운데?"   (출처: transcript:[user] 66c408dd…)
- 자연스러운 영어: "Since OM and SEM lock their align points sequentially (OM, OM, SEM, SEM, SEM), every one of them matters. Running the bench for each separately is the right call. I'm a bit surprised we haven't been doing it that way."
- 왜 이렇게: "전부 중요한 요소야"는 every one of them matters — matter 동사 하나로 "중요한 요소" 명사구를 대체합니다. "~하는 게 맞아"는 is the right call. 계속된 부작위("지금까지 안 했다")는 현재완료진행 haven't been doing이 정확합니다.

### 카드 8 — silent omission은 더 잘 숨는다   (고급 한글 · 번역)
- 한글 원문: ""있어야 할 게 없는" 결함(silent omission)은 "잘못된 값"보다 훨씬 잘 숨습니다. SEM 점수가 정상으로 나오는 한, OM 칸이 빈 건 누구도 의심하지 않죠."   (출처: transcript:[assistant] 66c408dd…)
- 자연스러운 영어: "A defect where something that should be there simply isn't hides far better than a wrong value. As long as the SEM scores look healthy, nobody questions the empty OM column."
- 번역 포인트: 한국어의 명사화("있어야 할 게 없는 결함")를 영어는 관계절(a defect where ... simply isn't)로 풉니다 — isn't 뒤를 비워 두는 생략이 원문의 "없음"을 그대로 형상화. "~하는 한"은 as long as, "누구도 의심하지 않죠"는 부정 주어 nobody questions로 옮기면 단정의 힘이 삽니다.

### 카드 9 — 코드 리뷰가 못 잡는 버그   (고급 한글 · 번역)
- 한글 원문: "이건 코드 리뷰가 못 잡고 도메인 지식이 잡는 전형입니다. 다섯 명이 `most_common(1)` 을 봐도 "합리적인 선택"으로 보여요."   (출처: transcript:[assistant] 66c408dd…)
- 자연스러운 영어: "This is a textbook case of a bug that code review can't catch but domain knowledge can. Five reviewers could stare at most_common(1) and it would still read as a perfectly reasonable choice."
- 번역 포인트: "전형"은 a textbook case of. "못 잡고 / 잡는"의 대구는 can't catch but ~ can — 뒤쪽 동사를 생략한 병렬이 영어답습니다. "봐도 ~로 보여요"의 양보는 could stare ... and it would still read as의 가정법으로: "아무리 뚫어져라 봐도"의 뉘앙스까지 전달됩니다.

### 카드 10 — shared_tune의 진짜 의미   (고급 한글 · 번역)
- 한글 원문: "`shared_tune` 은 "modality 분리 하지 말라"가 아니라 "이 실패 유형은 공유다"입니다. recall_miss 를 edge_ncc 로 줄여보고, 그 효과가 modality별로 갈리면 그때가 resolver 를 modality-aware 로 쪼갤 시점입니다."   (출처: transcript:[assistant] 66c408dd…)
- 자연스러운 영어: "shared_tune doesn't mean 'don't split by modality' — it means 'this failure type is shared.' Try cutting recall_miss with edge_ncc first, and if the effect diverges by modality, that's the moment to split the resolver into a modality-aware one."
- 번역 포인트: "A가 아니라 B다"는 doesn't mean A — it means B의 대시 구조가 가장 명쾌합니다. "갈리면"은 diverge(한 지점에서 갈라진다는 그림까지 일치). "그때가 ~할 시점이다"는 that's the moment to ~ — when절 없이 시점을 명사로 고정하는 관용 패턴입니다.

## 영어 다듬기

### 카드 1 — DRM 추출 최적화 요청
- 내가 쓴 영어: "I am able to use local api with GLM 5.2 and Kimi-K2.6 in my office. Along with flask-deployed vlms, do the best to optimize to extract the drm-projected pdf, pptx, docx, and so on. to extract the data."   (출처: transcript:[user] 62687dfa…)
- 정정: ① "do the best" → **do your best** (관용구는 소유격 고정). ② "drm-projected" → **DRM-protected** (projected는 '투사된'; 보호는 protected). ③ "to extract ... to extract the data"처럼 목적의 to부정사가 중복 — 하나로 합치고, 끝의 "to extract the data."는 주어·동사 없는 문장 조각(fragment)이라 앞 문장에 붙여야 합니다.
- 더 나은 표현: "I can use the local API with GLM 5.2 and Kimi-K2.6 at my office. Together with the Flask-deployed VLMs, please optimize the pipeline to extract data from DRM-protected PDF, PPTX, and DOCX files."
- 왜: "am able to"는 can으로 충분(able은 능력 강조가 필요할 때만). 요청은 "do the best to optimize"보다 please optimize가 직접적이고, extract data **from** X 구조로 잡으면 "무엇에서 무엇을 뽑는지"가 명확해집니다.

### 카드 2 — 테스트 이미지 준비 질문
- 내가 쓴 영어: "I need to prepare images for the testing, where @poc/workflow_2/golden_combined_eval_cond.py file paths indicates?"   (출처: transcript:[user] 66c408dd…)
- 정정: ① "for the testing" → **for testing** (일반 용도의 동명사엔 관사 불필요). ② 주어가 복수(file paths)이므로 "indicates" → **indicate**. ③ 평서문에 물음표만 붙인 형태 — 의문문은 조동사 도치가 필요합니다.
- 더 나은 표현: "I need to prepare images for testing — where exactly do the file paths in golden_combined_eval_cond.py expect them to be?"
- 왜: 핵심 질문("어디에 놓아야 하나")을 별도 의문문으로 분리하면 상대가 답할 지점이 명확해집니다. expect them to be는 "코드가 기대하는 위치"라는 계약의 뉘앙스까지 전달합니다.

### 카드 3 — 데이터셋 중복 가능 여부
- 내가 쓴 영어: "for the consensus_history, I have downloaded the images to workflow_3/align_consensus_history/… . The one set for Golden data set in msr images can be the same as one in @align_consensus_history."   (출처: transcript:[user] 66c408dd…)
- 정정: 둘째 문장은 명사구가 겹쳐(one set / data set / in msr images) 주어가 무엇인지 읽히지 않습니다. 허락·가능을 묻는 내용이므로 평서문 "can be"보다 의문문 "Can ... be ...?"가 의도에 맞습니다.
- 더 나은 표현: "For consensus_history, I've downloaded the images to workflow_3/align_consensus_history/. Can the msr set in the golden folder be the same images as the ones in align_consensus_history?"
- 왜: 질문이었다면 의문문으로 물어야 상대가 위험(데이터 누수)을 짚어줄 확률이 높아집니다. the same images as the ones in ~ 비교 구조로 "무엇과 무엇이 같아도 되는가"를 명시하는 것이 포인트.

### 카드 4 — edge_ncc 배선 요청
- 내가 쓴 영어: "Wire edge_ncc into the consensus arm. and also I intentionally gather consensus rich data so that there is no empty consensus. still you can do test with rcp and msr in golden folder if you want. How can I wire edge_ncc?"   (출처: transcript:[user] 66c408dd…)
- 정정: ① 문장 첫 글자 대문자(And/Still). ② "I intentionally gather"는 이미 한 일이므로 현재완료 **I've intentionally gathered**. ③ "consensus rich data" → **consensus-rich data**(하이픈 합성 형용사) 또는 rich consensus data. ④ "do test" → **run a test / test it** (do + 무관사 명사는 비문).
- 더 나은 표현: "Wire edge_ncc into the consensus arm. Also, I've intentionally gathered rich consensus data so that no recipe ends up with an empty consensus. You can still test with the rcp and msr sets in the golden folder if you want. How do I wire edge_ncc?"
- 왜: "How can I ~?"는 가능성을, "How do I ~?"는 절차를 묻습니다 — 여기서는 설정 방법을 묻는 것이므로 do가 정확. ends up with는 "결과적으로 ~가 되어버리다"로 원문의 "빈 consensus가 생기지 않도록"을 살립니다.

### 카드 5 — edge_ncc 설정 위치 질문
- 내가 쓴 영어: "Run edge_ncc and compare SEM recall first. can you sett edge_ncc in the code? or I can see it in the golden_eval_config.py"   (출처: transcript:[user] 66c408dd…)
- 정정: ① "sett" → **set** (오타). ② "or I can see it in ~"는 평서문 — 선택지를 묻는 것이므로 **or should I set it in ~?** 의문문으로. ③ 파일명 앞의 "the"는 불필요(in golden_eval_config.py).
- 더 나은 표현: "Let's run edge_ncc and compare SEM recall first. Can you set edge_ncc in the code, or should I set it in golden_eval_config.py myself?"
- 왜: "A할까, 아니면 내가 B할까?"의 양자택일은 Can you A, or should I B? 패턴이 정석입니다. 끝의 myself가 "내 쪽에서 하겠다"는 대비를 만들어 줍니다.

### 카드 6 — 3채널 arm 설정법
- 내가 쓴 영어: "how can I set 3 channel arm?"   (출처: transcript:[user] 66c408dd…)
- 정정: ① 특정 대상을 가리키므로 정관사 필요 — **the** 3-channel arm. ② 수사+명사 합성 형용사는 하이픈으로: **3-channel**.
- 더 나은 표현: "How do I set up the 3-channel arm?"
- 왜: 구성·설정에는 set보다 **set up**이 자연스럽습니다. "수사-명사" 하이픈 합성(a 3-channel arm, a 2-stage pipeline)은 기술 영어에서 매일 쓰는 패턴이니 몸에 붙여두면 좋습니다.

### 카드 7 — 새 세션 시작 지시
- 내가 쓴 영어: "yes. do (1) first and then (2) let's starts new session for these jobs. make handoff /journal"   (출처: transcript:[user] 66c408dd…)
- 정정: ① "let's starts" → **let's start** (let us + 동사원형). ② "new session" → **a new session** (가산 단수엔 관사). ③ (1)과 (2) 사이 구두점이 없어 "(2) let's"가 한 덩어리로 읽힙니다 — 쉼표나 마침표로 분리.
- 더 나은 표현: "Yes — do (1) first, then (2). Let's start a new session for these jobs; write the handoff and journal."
- 왜: let's 뒤는 항상 동사원형입니다(3인칭 -s 금지). 지시가 여러 개면 문장을 짧게 끊는 쪽이 오독이 없고, make a handoff보다 write the handoff가 산출물(문서)에는 더 정확한 동사입니다.
