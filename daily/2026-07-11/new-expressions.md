# 2026-07-11 — 새 표현

오늘 배치: auto_recipe_creator 문서추출·차트 RAG 설계 문서 + edge_ncc A/B 세션 transcript.
영어 원문이 풍부한 날 — 리서치 리포트와 실험 해석 대화에서 14개를 골랐습니다.

## "leave (points) on the table"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator subagents/agent-a392b5d8… (차트 RAG 리서치 리포트)
- 맥락: 선택 가능한 이득을 챙기지 않고 남겨뒀음을 지적할 때(성능 비교·협상·보고, 구어·문어 모두)
- 한국어: (가질 수 있는 이득을) 고스란히 놓치다, 챙기지 않고 남겨두다
- 설명: 도박판에서 딴 돈을 테이블에 두고 일어난다는 비유. 원문 "captions-only indexing leaves ~30-40 nDCG points on the table"처럼 기회비용을 수치와 함께 생생하게 전달합니다.
- 예문: Indexing captions only leaves 30–40 nDCG points on the table compared to a vision retriever.
- 유사어: miss out on (더 일반적·구어), forgo (격식, 의도적 포기 뉘앙스), pass up (기회를 그냥 보내다)
- 반의어: capture the full upside (이득을 온전히 챙기다)

## "close (most of) the gap"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator subagents/agent-a392b5d8… ("Single-vector + reranker closes most of the gap")
- 맥락: 두 대안 사이 성능·수준 격차를 좁혔다고 보고할 때(벤치마크 비교·경쟁 분석, 문어)
- 한국어: 격차를 (대부분) 좁히다, 메우다
- 설명: gap은 두 방식·경쟁자 사이의 차이. "most of"를 끼워 넣어 "전부는 아니고 대부분"이라고 정도를 정직하게 한정하는 것이 이 표현의 요령입니다.
- 예문: A single-vector model plus a reranker closes most of the gap to late-interaction retrieval at a fraction of the storage.
- 유사어: narrow the gap (좁히다 — 아직 남았다는 뉘앙스), bridge the gap (잇다·메우다), catch up (따라잡다, 구어)
- 반의어: widen the gap (격차를 벌리다)

## "a non-issue"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator subagents/agent-a392b5d8… ("Storage/compute at your scale is a non-issue")
- 맥락: 걱정거리로 오르내리는 사안이 실제로는 문제가 안 된다고 일축할 때(회의·리뷰)
- 한국어: 문제 축에도 못 드는 것, 걱정할 일이 아님
- 설명: issue에 non-을 붙여 "논의할 필요조차 없는 사안"을 만든 명사. 근거(수치)와 함께 쓰면 단호하면서도 무례하지 않습니다.
- 예문: At a few thousand pages, storage is a non-issue — even unreduced multi-vector fits in single-digit gigabytes.
- 유사어: not a blocker (진행을 막지는 않음), negligible (무시할 수준, 격식), nothing to worry about (구어)
- 반의어: a showstopper (치명적 문제)

## "drop straight into (something)"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator 62687dfa… ("Qwen3-VL-Embedding … drops straight into OpenSearch kNN")
- 맥락: 새 부품이 개조 없이 기존 시스템에 바로 꽂힌다고 말할 때(아키텍처 논의, 구어적)
- 한국어: (개조 없이) 그대로 꽂히다, 바로 들어맞다
- 설명: a drop-in replacement의 동사판. 어댑터나 마이그레이션 없이 기존 슬롯에 들어간다는 저마찰 호환성을 강조합니다.
- 예문: Because it emits one vector per page, the model drops straight into an existing OpenSearch kNN field.
- 유사어: slot into (자리에 끼워지다), plug into (연결되다), work as a drop-in replacement (명사형 관용구)
- 반의어: require a sidecar service (별도 인프라를 요구하다)

## "conflate A with B"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("the +5pp conflates 'ensemble vs chamfer' with 'C4 added'")
- 맥락: 서로 다른 두 요인·개념이 한 결과에 뒤섞여 구분이 안 된다고 지적할 때(실험 해석·리뷰, 격식)
- 한국어: A와 B를 뒤섞어 하나로 취급하다
- 설명: 실험에서 변수 두 개를 동시에 바꿔 효과의 귀속이 불가능해졌을 때 딱 맞는 동사. a confound(교란 요인)와 한 세트로 기억하세요.
- 예문: This A/B conflates the ensemble upgrade with the new channel, so we can't tell which one produced the gain.
- 유사어: mix up (구어), lump together (뭉뚱그리다), confound (통계 용어)
- 반의어: disentangle / tease apart (분리해 내다)

## "pay off"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("the headline is: the fix paid off.")
- 맥락: 투자한 노력·결정이 실제 성과로 돌아왔다고 확인할 때(결과 보고의 첫 문장, 구어)
- 한국어: (노력·결정이) 결실을 맺다, 본전을 뽑다
- 설명: "빚을 갚다"라는 원뜻에서 "들인 것이 이득으로 돌아오다"로 확장. 결과 발표에서 "the fix paid off" 한 줄이면 그대로 헤드라인이 됩니다.
- 예문: The per-modality fix paid off — both OM and SEM rows are populated for the first time.
- 유사어: bear fruit (열매를 맺다, 다소 문어), be worth it (구어), deliver (기대한 성과를 내다)
- 반의어: fall flat (기대에 못 미치다)

## "don't over-read (it)"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("Caveats (don't over-read)")
- 맥락: 데이터에서 실제 근거 이상의 결론을 끌어내지 말라고 경고할 때(결과 해석의 캐비엇)
- 한국어: 과대 해석하지 마라
- 설명: read(해석하다)에 over-를 붙인 조어. 작은 표본·잡음 섞인 수치를 두고 성급한 결론으로 달려가는 것을 막는 완곡한 브레이크입니다.
- 예문: The S>=10 bin looks worse, but don't over-read it — those bins are small and uneven.
- 유사어: don't read too much into it (같은 뜻의 풀어쓴 형), don't over-index on (한 신호에 과잉 반응 말라), take it with a grain of salt (에누리해서 들어라)
- 반의어: take it at face value (액면 그대로 받아들이다)

## "burn an office run on (something)"
- 레지스터: conversational, casual
- 출처: transcript:auto_recipe_creator 66c408dd… ("before you burn an office run on it")
- 맥락: 횟수가 제한된 귀한 시도(사내 실행·실장비 시간)를 소모한다고 말할 때(구어)
- 한국어: 아까운 (사내) 실행 기회를 한 번 태워 쓰다
- 설명: burn은 "소모하다"의 구어. 왕복이 비싼 자원을 쓰기 전에 미리 검증하자는 맥락에서 자주 나옵니다. 기존 노트의 burn the retry budget과 같은 계열.
- 예문: Let me sanity-review the driver before you burn an office run on it.
- 유사어: use up (다 써버리다), spend a run on (중립적), waste a trip on (허탕 뉘앙스)
- 반의어: save a round trip (왕복을 아끼다)

## "the worst of both worlds"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("you get the worst of both worlds: no LOO protection and train==test overlap")
- 맥락: 절충안이 두 대안의 장점은 다 잃고 단점만 조합했다고 비판할 때(설계·결정 비판)
- 한국어: 양쪽의 단점만 취한 최악의 조합
- 설명: the best of both worlds(양쪽 장점만 취함)의 반전형. "같은 이미지를 두 폴더에 다 넣으면 LOO 보호도 없고 train-test 중첩까지 생긴다"처럼 한 방에 전달합니다.
- 예문: Reusing the same frames in both roots gives you the worst of both worlds — no leave-one-out protection and train-test overlap.
- 유사어: lose-lose (양쪽 다 손해), the downsides of both (풀어쓴 형)
- 반의어: the best of both worlds (양쪽 장점만 취함)

## "you're clear to (do something)"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 66c408dd… ("You're clear to prep counts and run.")
- 맥락: 선행 조건이 다 풀렸으니 진행해도 된다고 신호를 줄 때(항공 관제 어법, 협업 보고)
- 한국어: 이제 ~해도 됩니다(진행 허가)
- 설명: 관제탑의 "cleared for takeoff"에서 온 어법. 검토·차단 요소가 해소됐다는 정보가 담겨 있어 단순한 "you can"보다 말해주는 것이 많습니다.
- 예문: All four commits are pushed and tested — you're clear to pull at the office and run the A/B.
- 유사어: good to go (구어), green-light (동사: 승인하다), all clear (명사형 신호)
- 반의어: blocked on (~에 막혀 있다)

## "that's the tell"
- 레지스터: conversational, casual
- 출처: transcript:auto_recipe_creator 66c408dd… ("That's the tell: the next move is a run at the office, not a Mac edit.")
- 맥락: 여러 정황 중 결론을 드러내는 결정적 단서를 짚을 때(포커 용어 유래, 구어)
- 한국어: 그게 결정적 단서다, 그 대목에서 답이 드러난다
- 설명: 포커에서 상대 패를 누설하는 무의식적 버릇을 tell이라고 합니다. 추론을 설명하며 "이 신호가 정답을 알려준다"고 짚을 때 씁니다.
- 예문: The final deliverable was a runbook, not code — that's the tell that the next step is an office run.
- 유사어: the giveaway (정체를 폭로하는 단서), the telltale sign (전형적 징후, 다소 격식), the smoking gun (결정적 증거, 더 강함)
- 반의어: a red herring (주의를 흩뜨리는 가짜 단서)

## "that settles it"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("That settles the interpretation.")
- 맥락: 마지막 증거가 나와 논쟁·해석의 여지가 닫혔다고 선언할 때(결론 선언, 구어)
- 한국어: 이걸로 결론 났다, 논쟁 끝
- 설명: settle(분쟁을 매듭짓다)의 관용형. "one run that settles it"처럼 "무엇이 결론을 내려주는가"를 주어로 세우는 변형도 유용합니다.
- 예문: Production already uses the 3-channel ensemble — that settles it: the bench baseline was understated.
- 유사어: that decides it (같은 뜻), case closed (사건 종결, 캐주얼), that puts the question to rest (격식)
- 반의어: that reopens the question (다시 논쟁거리로 만들다)

## "sunk cost fallacy"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 66c408dd… (TDD 스킬 인용 — "Sunk cost fallacy. The time is already gone.")
- 맥락: 이미 들인 비용이 아까워 나쁜 선택을 계속하는 오류를 지적할 때(의사결정 논의, 격식)
- 한국어: 매몰 비용 오류
- 설명: 경제학 용어. "이미 쓴 시간은 어느 쪽을 골라도 돌아오지 않으니 지금부터의 선택만 비교하라"는 논리로, 코드 폐기나 방향 전환을 설득할 때 강력합니다.
- 예문: Keeping the untested code because you spent five hours on it is the sunk cost fallacy — the time is gone either way.
- 유사어: throwing good money after bad (밑 빠진 독에 물 붓기), escalation of commitment (심리학 용어)
- 반의어: cut your losses (손절하다)

## "split the credit"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 66c408dd… ("To split the credit, run the middle arm — 3 channels, no C4.")
- 맥락: 개선이 여러 요인 중 어느 것 덕분인지 나눠 귀속시키자고 제안할 때(실험 설계, ablation)
- 한국어: 공을 (요인별로) 나눠 귀속시키다
- 설명: credit(공로)을 분할한다는 비유로 ablation(중간 조건 실행)의 목적을 한 마디로 요약합니다. conflate 문제의 해결책에 해당하는 표현.
- 예문: Run the 3-channel arm to split the credit between the ensemble upgrade and the new C4 channel.
- 유사어: attribute the gain (이득을 귀속시키다, 격식), tease apart the contributions (기여를 분리하다)
- 반의어: conflate A with B (뒤섞어 구분 못 하게 하다)
