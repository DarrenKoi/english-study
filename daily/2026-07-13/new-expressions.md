# 2026-07-13 — 새 표현

오늘 배치: auto_recipe_creator — consensus 라이브 보정 배선의 최종 리뷰·구현 서브에이전트,
rcp/msr 다운로더 디커플링 디버깅, weekly report 제작 대화 transcript 8건.
코드리뷰 판정문과 "문제의 본질을 짚는" 대화 표현이 풍부한 날 — 16개를 골랐습니다.

## "creep in (crept in)"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator agent-ac5e234f… ("Confirm no OTHER unintended algorithmic divergence crept in.")
- 맥락: 의도치 않은 변경·버그가 아무도 모르게 스며들었는지 점검할 때(코드리뷰·회귀 검증, 문어·구어 모두)
- 한국어: (원치 않는 것이) 슬그머니 스며들다, 끼어들다
- 설명: creep(기어가다)의 그림 그대로 — 명시적 결정 없이 조금씩 들어온 변화를 말합니다. 포팅·리팩토링 리뷰에서 "divergence/bug/complexity crept in"은 거의 고정 짝입니다. 명사형 scope creep, parameter creep과 같은 뿌리.
- 예문: The port looks faithful, but let's diff it once more to confirm no unintended change crept in.
- 유사어: sneak in (더 구어·은밀함 강조), slip in (부주의로 들어옴), find its way in (출처 불명 뉘앙스)
- 반의어: be deliberately introduced (의도적으로 들여오다)

## "line up at every boundary"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator agent-ac5e234f… ("Do the data shapes/keys line up at every boundary?")
- 맥락: 모듈 경계마다 데이터 형태·키·규약이 서로 맞물리는지 물을 때(통합 리뷰, 문어·구어)
- 한국어: (경계마다) 아귀가 맞다, 정합하다
- 설명: line up은 줄이 맞는 그림 — 두 쪽의 계약이 어긋남 없이 만난다는 뜻입니다. "Keys line up", "the numbers don't line up"처럼 정합성 확인 전반에 씁니다. at every boundary를 붙이면 인터페이스 단위 점검이라는 뉘앙스가 정확해집니다.
- 예문: Trace one real call end-to-end and check that the shapes and keys line up at every boundary.
- 유사어: match up (중립), be consistent across (격식), agree (수치·기록이 일치하다, 격식)
- 반의어: mismatch / be out of sync (어긋나다)

## "collapse (distinct things) into one"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 8657d569… ("there are three distinct things that you're collapsing into one")
- 맥락: 상대가 서로 다른 문제·개념을 하나로 뭉뚱그리고 있음을 정중히 짚을 때(디버깅 대화·리뷰)
- 한국어: (별개인 것들을) 하나로 뭉뚱그리다
- 설명: 접힌다(collapse)는 그림 — 구분이 무너져 한 덩어리로 보인다는 뜻. "You're collapsing X into one"은 상대 오해의 구조를 지적하는 세련된 방법으로, 비난 대신 "구분해 보자"로 대화를 돌립니다.
- 예문: The download failure feels like one bug, but you're collapsing three distinct mechanisms into one.
- 유사어: conflate A with B (격식·학술), lump together (구어, 대충 묶다), blur the line between (경계가 흐려지다)
- 반의어: tease apart / disentangle (하나씩 풀어 구분하다)

## "get at the heart of"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 8657d569… ("Good questions — they get at the heart of the decoupling.")
- 맥락: 질문·지적이 문제의 정곡을 건드렸다고 인정해 줄 때(회의·리뷰 답변, 구어)
- 한국어: 핵심을 건드리다, 정곡을 찌르다
- 설명: get at은 "닿으려 하다" — 표면이 아니라 심장부(heart)에 닿는 질문이라는 칭찬입니다. 상대 질문을 존중하며 본질 논의로 넘어가는 부드러운 전환구.
- 예문: That question gets at the heart of why we split the downloader from the notifier.
- 유사어: cut to the core (더 강함), go to the crux (격식), hit the nail on the head (정답을 맞혔다는 뉘앙스)
- 반의어: dance around (the issue) (핵심을 피해 돌다)

## "That's the deciding detail."
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator 8657d569… ("That's the deciding detail — and it actually makes your life easier, not harder.")
- 맥락: 상대가 준 정보 하나가 설계 방향을 확정지었을 때(질의응답 도중, 구어)
- 한국어: 그게 결정적인 한 조각이다
- 설명: 여러 선택지 사이에서 저울이 기울게 만든 바로 그 사실(detail)을 가리킵니다. 뒤에 "— and …"로 함의를 바로 이어 붙이면 "네 답 덕분에 결론이 났다"는 협업 리듬이 삽니다. the deciding factor의 구어 변형.
- 예문: You embed the images from those paths? That's the deciding detail — we keep both callers.
- 유사어: the deciding factor (중립·격식), the clincher (구어, 승부를 굳힌 것), the key piece of the puzzle (비유)
- 반의어: a side detail (지엽적인 사항)

## "attack the exact blocker"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 68f829b0… ("Your offer to collect ≥4 S images attacks the *exact* blocker")
- 맥락: 어떤 제안이 진짜 병목을 정면으로 공략한다고 평가할 때(설계 논의, 문어·구어)
- 한국어: 바로 그 차단 요인을 정면 공략하다
- 설명: attack을 문제에 쓰면 "정면으로 달려들다"는 적극적 그림이 됩니다. the exact를 붙여 "다른 것도 아니고 바로 그" 병목임을 강조 — 제안의 가치를 한 문장으로 승인하는 표현입니다.
- 예문: Collecting more success images attacks the exact blocker that kept consensus out of production.
- 유사어: go straight at (구어), target (중립), tackle head-on (정면 대응 강조)
- 반의어: work around (우회하다)

## "the single highest-leverage thing"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 68f829b0… ("That's the single highest-leverage thing you could do here.")
- 맥락: 여러 후보 중 투입 대비 효과가 가장 큰 행동 하나를 추천할 때(우선순위 논의)
- 한국어: 지렛대 효과가 가장 큰 단 하나의 일
- 설명: leverage(지렛대)를 형용사화한 high-leverage에 최상급 + single을 겹쳐 "이거 하나만 하면 판이 바뀐다"를 만듭니다. 우선순위를 딱 하나로 좁혀 주는 강한 추천 구문.
- 예문: If you can only do one thing this week, implementing the downloader is the single highest-leverage thing you could do.
- 유사어: the biggest bang for the buck (구어·비용 대비), the most impactful move (중립), where the lever is (은유 유지)
- 반의어: a low-leverage chore (해도 판이 안 바뀌는 일)

## "necessary but not sufficient"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 8657d569… ("The code reading the workflow_3 tree is necessary but not sufficient.")
- 맥락: 조건 하나가 충족돼도 그것만으로는 부족함을 논리적으로 말할 때(설계 근거·분석, 격식)
- 한국어: 필요조건이지만 충분조건은 아니다
- 설명: 논리학 용어가 그대로 업무 영어에 들어온 관용구. "경로 설정은 맞다, 그러나 쓰는 쪽도 같은 경로여야 한다"처럼 반쪽 해결을 짚을 때 정확합니다. 격식 있는 문어에서 특히 힘을 발휘합니다.
- 예문: Pointing the reader at the right directory is necessary but not sufficient — the writer has to land files there too.
- 유사어: only half the story (구어), a precondition, not a guarantee (풀어쓰기)
- 반의어: sufficient on its own (그것만으로 충분한)

## "a judgment call (I shouldn't make unilaterally)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 68f829b0… ("That's a judgment call I shouldn't make unilaterally.")
- 맥락: 정답이 없어 가치판단이 필요한 결정을 상대에게 넘길 때(에스컬레이션, 문어·구어)
- 한국어: (정답 없는) 재량 판단 — 나 혼자 내릴 일은 아니다
- 설명: judgment call은 규칙으로 못 정하고 판단력으로 정하는 결정. unilaterally(일방적으로)를 붙이면 "권한 밖이라서가 아니라, 합의가 필요해서 넘긴다"는 존중의 뉘앙스가 실립니다.
- 예문: Diverging from the validated bench is a judgment call I shouldn't make unilaterally — your call.
- 유사어: a discretionary decision (격식), your call (구어, 결정권 이양), a coin-toss decision (어느 쪽도 답인)
- 반의어: a clear-cut decision (판단 여지 없는 결정)

## "do double duty (as)"
- 레지스터: conversational, technical
- 출처: transcript:auto_recipe_creator 8657d569… ("The `test_` prefix here is doing double duty as a delivery channel, not a test")
- 맥락: 하나가 두 역할을 겸하고 있음을 지적하거나 설계 의도를 설명할 때(구어)
- 한국어: 1인 2역을 하다, 두 몫을 겸하다
- 설명: 군대 용어 double duty(이중 근무)에서 온 일상 관용구. 코드에선 파일·매개변수·네이밍이 본래 역할 외의 몫까지 질 때 씁니다 — 좋은 재활용일 수도, 결합도 경고일 수도 있어 문맥이 판정합니다.
- 예문: The dest_dir parameter does double duty — a directive in Case 2, an assertion in Case 1.
- 유사어: serve two purposes (중립), wear two hats (사람에 대해), pull double duty (미국 구어)
- 반의어: have a single responsibility (한 가지 역할만 맡다)

## "cheap insurance (against)"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator 8657d569… ("`_warn_if_outside` is the cheap insurance against your *original* bug")
- 맥락: 비용은 몇 줄인데 큰 사고를 막아 주는 방어 코드를 정당화할 때(리뷰·설계, 구어)
- 한국어: 값싼 보험 — 몇 줄로 큰 사고를 막는 안전장치
- 설명: 보험 은유 — 평소엔 아무 일도 안 하지만 사고 나면 본전을 뽑는 코드. "It's cheap insurance"는 가드·assert·경고 로그를 지키자는 논거의 정형구입니다.
- 예문: The existence check is cheap insurance against a partial download slipping through.
- 유사어: a safety net (중립), a guardrail (방향 이탈 방지), a seatbelt (극구어 비유)
- 반의어: dead weight (아무 사고도 못 막으면서 자리만 차지하는 것)

## "optional polish, not required for correctness"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator 8657d569… ("but that's optional polish, not required for correctness")
- 맥락: 개선 제안의 등급을 매길 때 — 해도 좋지만 안 해도 틀리지 않음(리뷰 판정, 문어)
- 한국어: 선택적 다듬기일 뿐, 정합성에 필수는 아니다
- 설명: polish(광내기)는 동작이 아니라 마감 품질을 올리는 손질. "X, not Y" 대구로 필수/선택 경계를 한 문장에 긋습니다. 리뷰에서 nit와 must-fix를 가르는 어휘.
- 예문: Moving the two functions into their own module is optional polish, not required for correctness.
- 유사어: a nice-to-have (구어), cosmetic (겉모양만), icing on the cake (비유)
- 반의어: a must-fix / required for correctness (필수 수정)

## "You're fully unblocked."
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 8657d569… ("Pushed. You're fully unblocked.")
- 맥락: 상대 진행을 막던 요소가 모두 제거됐음을 선언할 때(핸드오프·협업 채팅, 구어)
- 한국어: 이제 막히는 것 없이 진행할 수 있다
- 설명: blocked(막힘)의 반대 상태를 사람 주어로 선언하는 협업 어휘. fully를 붙여 "부분 해제가 아니라 전부"임을 명시합니다. 짧은 완료 보고 뒤에 붙이면 다음 행동 주체가 상대에게 넘어갔음이 분명해집니다.
- 예문: The wiring is merged and the template is on main — you're fully unblocked at the office.
- 유사어: you're clear to proceed (격식), nothing is blocking you now (풀어쓰기), the path is clear (비유)
- 반의어: still blocked on (X) (여전히 X에 막혀 있는)

## "always one alarm behind (one step behind)"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator 8657d569… ("the download at step 3 was always one alarm behind")
- 맥락: 데이터·처리가 필요 시점보다 항상 한 사이클 늦게 도착하는 지연 버그를 묘사할 때
- 한국어: 늘 한 박자(한 사이클) 늦다
- 설명: one step behind(한 걸음 뒤)의 단위를 도메인 단위(alarm, release, sprint…)로 갈아 끼운 패턴. "다운로드는 되는데 항상 직전 알람용"이라는 타이밍 결함을 한 구로 요약합니다.
- 예문: The cache did fill, but it was always one alarm behind, so each correction read last incident's images.
- 유사어: perpetually stale (항상 낡은 상태), lagging by one cycle (중립·계측적)
- 반의어: ahead of time / in time for (제때·앞서)

## "a ship/no-ship assessment"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator agent-ac5e234f… ("an overall ship/no-ship Assessment" → "Assessment: SHIP")
- 맥락: 리뷰의 최종 판정을 출시 가부 이진 결정으로 요구·선언할 때(최종 리뷰, 문어)
- 한국어: 출시 가부 판정
- 설명: go/no-go(발사 가부)의 소프트웨어판. 리뷰어에게 "장단점 나열 말고 배포 가능 여부로 답하라"고 요구하는 형식이며, 답도 "SHIP" 한 단어로 선언됩니다.
- 예문: End the review with a ship/no-ship assessment, not a list of observations.
- 유사어: a go/no-go decision (항공우주 유래·범용), a merge-yes/merge-no verdict (리뷰 국지어)
- 반의어: (마땅한 대체 표현 없음)

## "the whole picture (I have the full picture now)"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 8657d569… ("That confirms the whole picture — and reveals the timing was actually worse…")
- 맥락: 흩어진 단서가 모두 모여 상황 전체가 이해됐다고 선언할 때(디버깅 중간 보고, 구어)
- 한국어: 전체 그림, 전모
- 설명: 퍼즐 조각이 모여 그림이 완성되는 은유. "That confirms the whole picture"는 마지막 단서가 가설을 확정했다는 신호로, 뒤이어 결론 설명으로 넘어가는 담화 표지 역할을 합니다.
- 예문: Your answer about the embed paths confirms the whole picture — the download was coupled to the notification all along.
- 유사어: the full story (구어), a complete understanding (격식), connect the dots (조각을 잇다 — 동사구)
- 반의어: a partial view (부분적 이해)
