# 2026-09-29 — 새 표현

> 오늘 배치는 repo 문서 8건과 transcript 12건이다. repo 문서 7건은 skewnono 의 `docs/datatables/hitachi/` 로, 사무실 LLM 에게 보내는 영어 브리프(`hardware_field_usage.md`, `hardware_fdc_sce_characterization.md`, `hardware_fdc_fleet_verification.md`)가 표현 소스가 됐다. `.txt` 쪽은 한국어 메모와 필드 목록이라 뺐다. 나머지 1건은 auto_recipe_creator 의 `docs/agents/domain.md`. transcript 는 OM align 보정의 2nd 후보 진단, FDC fleet view 구축과 사무실 배포 준비, 공지사항 N 배지 제거 세션이 중심이다. `Red for the right reason`, `burn the retry budget`, `load-bearing`, `by construction`, `that's your call` 은 노트에 이미 있어서 제외.

## "A gap is useful; a guess dressed as a finding is not."
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 조사·검증을 맡기면서 "모르면 모른다고 적어라"를 못 박을 때(작업 지시서·리뷰 규칙, 격식).
- 한국어: 빈칸은 쓸모가 있지만 발견인 척하는 추측은 쓸모가 없다.
- 설명: `dressed as` 는 "~의 옷을 입은, ~로 꾸민"이다. 추측이 발견의 옷을 입고 있으면 읽는 쪽이 둘을 가려낼 수 없다는 경고. 세미콜론 앞뒤로 `A is useful; B is not` 대구를 만들어 한 줄 규칙으로 기억되게 했다. 앞 문장 `Say what you could not answer and why.` 와 한 묶음이다.
- 예문: Say what you could not answer and why. A gap is useful; a guess dressed as a finding is not.
- 유사어: Don't pass off a guess as a fact. (구어, `pass off A as B` = A를 B로 속여 넘기다), Flag speculation as speculation. (격식, 지시문), Better an honest "unknown" than a confident guess. (격언조)
- 반의어: a finding backed by evidence (근거 있는 발견)

## "Report numbers, not rows."
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 데이터 조사를 맡길 때 원본 덤프 말고 요약 수치로 답하라고 할 때(지시문, 격식·간결).
- 한국어: 행(원본 레코드)을 붙이지 말고 숫자로 보고하라.
- 설명: 명령문에 `A, not B` 를 붙인 네 단어짜리 규칙. `rows` 는 쿼리 결과를 통째로 붙여 넣는 행위를 가리킨다. 자매 문서에서는 `Report statistics, not rows.` 로 바꿔 썼다. 뒤따르는 `keep it to the size asked for` 가 예외(샘플 요청)의 한도를 정한다.
- 예문: Report numbers, not rows. Where a sample is asked for, keep it to the size asked for.
- 유사어: Summarize, don't dump. (구어), Give me the aggregates, not the raw data. (평이), Provide summary statistics rather than raw records. (격식)
- 반의어: paste the raw output (원본을 그대로 붙이다)

## "copy what engineers already trust before inventing a view"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 새 화면·도구를 설계하기 전에 현장이 이미 쓰는 것부터 확인하자고 할 때(설계 원칙, 격식 중간).
- 한국어: 새 화면을 발명하기 전에 엔지니어들이 이미 믿고 보는 것부터 베껴라.
- 설명: `copy` 와 `invent` 를 대비해 "새로 만드는 게 능사가 아니다"를 짧게 말한다. `already trust` 가 핵심이다. 익숙함이 곧 신뢰라서 이미 쓰는 화면을 닮게 만들면 받아들여지기 쉽다. 원문에서는 `Decides` 열에 적혀 이 질문이 무엇을 결정하는지 알려 준다.
- 예문: Before we design the dashboard, let's copy what engineers already trust before inventing a view of our own. (작성)
- 유사어: start from what people already use (평이), don't reinvent the wheel (관용구, 구어), build on existing practice (격식)
- 반의어: design from a blank slate (백지에서 설계하다)

## "so the home mocks stop teaching false shapes"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 가짜 데이터(mock)가 실제와 달라 개발자를 잘못 길들이고 있다고 지적할 때(기술 문서).
- 한국어: 집의 mock 이 더는 틀린 모양을 가르치지 않도록
- 설명: mock 을 "가르치는" 주체로 의인화했다. 틀린 mock 으로 화면을 만들면 그 모양이 정답인 줄 알게 되니까. `stop + -ing` 는 "하던 것을 그만두다". `stop to teach` 로 쓰면 "가르치려고 멈추다"라는 다른 뜻이 된다.
- 예문: Give plain numbers for cadence and value ranges, so the home mocks stop teaching false shapes.
- 유사어: so the mocks stop misleading us (평이), so the fixtures reflect reality (격식), so we stop building against fake data (구어)
- 반의어: a mock calibrated to real data (실측에 맞춘 mock)

## "character for character"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 두 값이 대소문자·공백까지 완전히 같아야 한다고 강조할 때(스펙·설정 문서).
- 한국어: 한 글자도 다르지 않게, 글자 그대로
- 설명: `word for word`(한 단어도 빠짐없이)와 같은 짜임이다. 원문은 `must match … character for character` 로 쓰고 바로 뒤에서 "철자가 하나 다르면 0건이 돌아오고 에러 없이 빈 차트로 보인다"는 결과까지 적었다. 부사구라 문장 끝에 둔다.
- 예문: The roster's `eqp_id` must match each index's stored `eqp_id` character for character.
- 유사어: exactly (가장 평이), verbatim (격식, 문장·인용에 주로), byte for byte (기술, 바이트 수준)
- 반의어: roughly the same (대충 같은)

## "It shows as an empty chart, not an error."
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 실패가 어떤 모습으로 사용자 눈에 드러나는지 설명할 때(장애 진단 가이드, 구어체 설명).
- 한국어: 에러가 아니라 빈 차트로 나타난다.
- 설명: `show as X` 는 "X 의 모습으로 보이다". 조용한 실패(silent failure)를 설명하는 틀이라 `not an error` 로 사람들이 기대하는 모습을 부정해 준다. 같은 문서에 `You would see the newest ~9h of data missing, not an error.` 도 같은 패턴이다.
- 예문: A spelling difference returns zero documents. It shows as an empty chart, not an error.
- 유사어: it surfaces as (격식), it looks like (구어), it manifests as (격식·기술)
- 반의어: it fails loudly (시끄럽게 실패하다, 에러를 낸다)

## "on the user's word"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 직접 확인하지 않았고 누군가의 말을 근거로 바꿨다고 출처를 밝힐 때(변경 기록·보고).
- 한국어: 사용자의 말을 믿고 / 사용자가 그렇다고 해서
- 설명: `on someone's word` 는 "그 사람의 보증을 근거로". 원문 `was corrected on the user's word (user-confirmed)` 는 데이터로 검증한 게 아니라 사람 말에 기댔다는 한계를 정직하게 남긴다. `take someone's word for it`(말을 그대로 믿다)과 같은 계열.
- 예문: `Ellipticity` was spelled `Ellipicity` here until 2026-09-28 and was corrected on the user's word.
- 유사어: on the user's say-so (구어, 약간 회의적), based on the user's confirmation (격식), because the user said so (평이)
- 반의어: verified against the data (데이터로 검증한)

## "suspect a change in the ingestion rule, not the tool"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 지표가 움직일 때 어디부터 의심해야 하는지 미리 알려 줄 때(진단 가이드).
- 한국어: 장비가 아니라 적재 규칙이 바뀐 걸 의심하라
- 설명: `suspect` 를 동사로 써서 "원인 후보로 먼저 보라"는 지시를 짧게 한다. `If its trend moves, suspect X, not Y.` 전체가 조건 → 지시 → 오답 배제의 3단 짜임이다. 사람이 자연스레 떠올릴 원인(장비)을 `not` 뒤에 둬서 오진을 막는다.
- 예문: If its trend moves, suspect a change in the ingestion rule, not the tool.
- 유사어: look at the ingestion rule first (평이), the likely culprit is the pipeline (구어), attribute it to the ingestion rule (격식)
- 반의어: rule out the ingestion rule (적재 규칙을 원인에서 배제하다)

## "that's a signal"
- 레지스터: conversational, professional
- 출처: repo:auto_recipe_creator docs/agents/domain.md
- 맥락: 뭔가가 없거나 어긋난 상황 자체를 의미 있는 단서로 읽으라고 할 때(가이드·코칭).
- 한국어: 그 자체가 신호다(뭔가를 알려 준다)
- 설명: 원문은 `If the concept you need isn't in the glossary yet, that's a signal — either …, or …` 로 이어진다. 대시 뒤에 신호가 가리키는 두 가능성을 `either … or` 로 펼친다. "막혔다"를 "알려 주는 게 있다"로 바꿔 읽게 하는 말.
- 예문: If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use, or there's a real gap.
- 유사어: that tells you something (구어), that's a red flag (경고 쪽, 구어), that's worth noting (격식 중간)
- 반의어: that's just noise (의미 없는 잡음)

## "worth reopening"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/agents/domain.md
- 맥락: 이미 확정된 결정(ADR 등)을 다시 논의할 가치가 있다고 조심스럽게 꺼낼 때(설계 리뷰, 격식).
- 한국어: 다시 열어 볼 만하다, 재논의할 가치가 있다
- 설명: `reopen` 은 닫힌 이슈·결정을 다시 여는 동사. `worth + -ing` 로 "그럴 가치가 있다"를 붙여서 기존 결정을 존중하면서도 이의를 제기한다. 원문은 `Contradicts ADR-0007 … — but worth reopening because…` 로, 충돌을 먼저 밝히고 `but` 뒤에 이유를 단다.
- 예문: This contradicts ADR-0007, but it's worth reopening because the traffic pattern has changed. (작성)
- 유사어: worth revisiting (가장 흔함, 격식 중간), worth a second look (구어), merits reconsideration (격식)
- 반의어: settled (이미 결론 난), not up for debate (재론 불가)

## "barely better than no loop"
- 레지스터: technical, conversational
- 출처: transcript:[user] auto-recipe-creator (diagnosing-bugs 스킬 본문)
- 맥락: 있긴 하지만 질이 낮아 없는 것과 다를 바 없다고 평가할 때(기술 조언, 구어).
- 한국어: 루프가 없는 것보다 겨우 나은 수준
- 설명: `barely` 는 "간신히, 거의 ~ 아니게". `barely better than nothing` 이 관용 틀이고 원문은 `nothing` 자리에 `no loop` 을 넣었다. 문장 전체 `A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight` 는 세미콜론으로 나쁜 예와 좋은 예를 맞세운다.
- 예문: A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight.
- 유사어: hardly better than nothing (같은 뜻, 약간 문어), next to useless (구어, 더 강함), of marginal value (격식)
- 반의어: a huge improvement (큰 개선)

## "Search-around can't fix a wrong gate."
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 뒷단의 복구 장치가 앞단의 판정 오류를 구해 줄 수 없는 구조를 설명할 때(원인 분석).
- 한국어: 판정(gate)이 틀리면 search-around 로는 못 고친다.
- 설명: `X can't fix a wrong Y` 는 "하류 장치는 상류 오류를 못 메운다"는 틀. 원문은 바로 `it reuses the same gate, so a broken ambiguity signal turned into a guaranteed abort` 로 이유를 잇는다. 같은 판정을 재사용하니 폴백이 폴백 구실을 못 한다는 논리다.
- 예문: Search-around can't fix a wrong gate: it reuses the same gate, so a broken ambiguity signal turned into a guaranteed abort.
- 유사어: a fallback can't rescue a bad check (평이), garbage in, garbage out (관용구, 구어), downstream retries won't compensate for a faulty decision (격식)
- 반의어: the fallback recovers the miss (폴백이 놓친 것을 되살린다)

## "a genuine lookalike"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 진짜로 닮은 다른 대상과 같은 것이 두 번 잡힌 경우를 구분할 때(이미지 매칭·중복 판별).
- 한국어: 진짜 닮은꼴 (같은 것이 중복된 게 아니라 실제로 다른 비슷한 대상)
- 설명: `lookalike` 는 "닮은 사람·닮은 것"이라는 명사. `genuine` 을 붙여 "중복 집계가 아닌 진짜"를 강조한다. 원문은 `the same key counted twice, not a real lookalike` 와 `a genuine lookalike (two copies) must still read as ambiguous` 를 대비해 테스트 양쪽을 설계한다.
- 예문: A unique key must not look ambiguous, and a genuine lookalike (two copies) must still read as ambiguous.
- 유사어: a real look-alike (같은 말, 하이픈 표기도 흔함), a near-duplicate (기술, 거의 같은 것), a doppelgänger (구어·재치, 사람에게 주로)
- 반의어: a duplicate of the same item (같은 대상의 중복)

## "Office truth wins."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 두 출처가 어긋날 때 어느 쪽을 기준으로 삼는지 한마디로 정할 때(팀 내 구어, 결정 선언).
- 한국어: 사무실(실데이터) 쪽이 정답이다, 사무실 기준으로 간다.
- 설명: `X wins` 는 충돌 시 우선순위를 말하는 구어 관용. 원문은 사무실이 필드 이름을 다르게 적어 보내자 `Office truth wins, so the writer helper gets realigned` 로 곧장 조치까지 잇는다. `truth` 를 형용사처럼 앞에 둔 명사 복합어라 짧고 단단하다.
- 예문: The office wrote the fields under different names from mine. Office truth wins, so the writer helper gets realigned before anything reads those fields.
- 유사어: the office is the source of truth (격식·기술), the office version takes precedence (격식), we go with what the office says (구어)
- 반의어: our local copy is authoritative (로컬 쪽이 기준)

## "A wrong type is caught cheaply then; later it needs a rollover to fix."
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 지금 확인하면 싸고 나중에 발견하면 비싸다고 점검 시점을 앞당기자고 할 때(배포 계획).
- 한국어: 그때 잡으면 잘못된 타입도 싸게 고치지만 나중엔 rollover 가 있어야 고쳐진다.
- 설명: 부사 `cheaply` 가 수동태 `is caught` 를 꾸며 "싸게 잡힌다"가 된다. 세미콜론 앞뒤로 `then`(그때) ↔ `later`(나중) 대비. `it needs X to fix` 는 "고치려면 X 가 필요하다". 비용 차이를 들어 순서를 설득하는 전형적인 구조다.
- 예문: Check V0.2 right after the first 6-hour run, not in 2–3 days. A wrong type is caught cheaply then; later it needs a rollover to fix.
- 유사어: it's cheap to fix now but expensive later (평이), catch it early while it's still cheap (구어), early detection keeps the remediation cost low (격식)
- 반의어: it's easy to fix at any time (언제 고쳐도 쉽다)

## "go-ahead message"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 상대에게 "진행해도 좋다"는 허가를 보낼 때 그 메시지를 가리키는 말(업무 연락).
- 한국어: 진행 승인 메시지, 착수 허가 연락
- 설명: `go-ahead` 는 "허가, 승인"이라는 명사(하이픈 필수). `give the go-ahead`, `get the go-ahead` 로 흔히 쓴다. 원문 `three things should go in the go-ahead message` 는 허가와 함께 조건을 붙이는 상황이고 실제 문안도 `Go ahead with the side-field writer deploy. Three conditions:` 로 시작한다.
- 예문: The code side is ready, but three things should go in the go-ahead message.
- 유사어: green light (구어, 비유), sign-off (격식, 최종 승인), approval (가장 평이)
- 반의어: a hold (보류 지시), a stop order (중단 지시)

## "something users truly must not miss"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 강조 장치(고정·알림)를 아껴 쓰라고 조언할 때(UX 조언).
- 한국어: 사용자가 정말 놓쳐서는 안 되는 것
- 설명: 원문 `save the flag for something users truly must not miss` 에서 `save A for B` 는 "A 를 B 에 쓰려고 아껴 두다". `truly` 가 문턱을 높인다. 모든 공지를 고정하면 고정이 의미를 잃으니 정말 중요한 것만 쓰라는 뜻.
- 예문: They'd show above the timeline whatever page of the list you're on, so save the flag for something users truly must not miss.
- 유사어: something critical (평이), a must-see (구어, 명사), information of critical importance (격식)
- 반의어: nice-to-know information (알면 좋은 정도의 정보)

## "bars on a truncated axis exaggerate small differences"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 차트 형태를 바꾼 이유를 데이터 시각화 원칙으로 설명할 때(리뷰·설계 근거).
- 한국어: 잘린 축 위의 막대는 작은 차이를 부풀린다
- 설명: `truncated axis` 는 0 에서 시작하지 않는 축. 막대는 길이로 값을 읽게 해서 축이 잘리면 차이가 과장된다. 원문 `The laser ranking uses dots: bars on a truncated axis exaggerate small differences.` 는 콜론 앞에 결정, 뒤에 이유를 둔다.
- 예문: The laser ranking uses dots: bars on a truncated axis exaggerate small differences.
- 유사어: make small gaps look huge (구어), overstate minor differences (격식), visually inflate the gap (기술 중간)
- 반의어: understate the difference (차이를 축소해 보이게 하다)

## "fights the layout"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 어떤 조작이 구조와 맞지 않아 자꾸 틀어질 때 우회로를 택하는 이유를 말할 때(구어 작업 보고).
- 한국어: 레이아웃과 씨름하게 된다, 레이아웃이 말을 안 듣는다
- 설명: `fight X` 는 "X 에 맞서 억지로 하다"는 구어 비유. `fight the framework`, `fight the tool` 처럼 개발 대화에서 자주 쓴다. 원문은 `Scrolling the inner container fights the layout. Instead I'll make the viewport tall enough to show everything at once.` 로, 싸우지 말고 판을 바꾸자는 흐름이다.
- 예문: Scrolling the inner container fights the layout. Instead I'll make the viewport tall enough to show everything at once.
- 유사어: works against the layout (평이), goes against the grain (관용구), is at odds with the layout (격식)
- 반의어: works with the layout (구조에 맞춰 가다)

## "That's a flaw in the check, not in Codex's code."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 실패의 책임이 검사 도구 쪽에 있음을 분명히 해 남의 작업을 공정하게 평가할 때(리뷰·협업).
- 한국어: 그건 Codex 코드가 아니라 검사 쪽 결함이다.
- 설명: `a flaw in X, not in Y` 로 결함의 위치를 정확히 짚는다. 원문은 `My oracle had a bug: the output format is ℹ fail 0, not # fail 0.` 로 자기 실수를 먼저 인정한 뒤 이 문장을 쓴다. 비난의 방향을 바로잡는 공정한 말투.
- 예문: My oracle had a bug: the output format is `ℹ fail 0`, not `# fail 0`. That's a flaw in the check, not in Codex's code.
- 유사어: the test was wrong, not the code (평이), the fault lies with the check (격식), that's on me, not Codex (구어, 책임 인정)
- 반의어: the code itself is broken (코드 자체의 결함)

## "without being asked"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 요청 범위를 넘어 누군가 임의로 바꾼 것을 지적할 때(리뷰·보고, 중립적 구어).
- 한국어: 시키지도 않았는데, 요청받지 않고
- 설명: `without + being + p.p.` 는 동명사 수동형이라 "~당하지 않고", 즉 "요청받지 않은 채로"가 된다. 원문 `it had deleted the 중복 없음 warning without being asked, so I restored it.` 는 사실만 적고 조치로 넘어가 비난조가 약하다. 칭찬에도 쓴다: `She fixed it without being asked.`
- 예문: I reviewed its diff; it had deleted the `중복 없음` warning without being asked, so I restored it.
- 유사어: unprompted (간결, 중립), on its own initiative (격식, 긍정적일 때 많음), out of the blue (구어, 뜬금없이)
- 반의어: as requested (요청대로)

## "a rehearsal run first"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 실제 장비·운영 환경에서 돌리기 전에 부작용 없는 시험 실행부터 하라고 권할 때(운영 안내).
- 한국어: 먼저 리허설(시험) 실행
- 설명: `rehearsal` 은 공연 전 예행연습에서 온 말. 기술에서는 `dry run` 과 비슷하지만 "실제와 똑같이 해 보되 결과는 남기지 않는다"는 연습 느낌이 강하다. 원문의 `SAFE_MODE=1 … # rehearsal first: no clicks, no scrolling` 주석과 `pull and do a rehearsal run first` 가 짝이다.
- 예문: To try it in the office, pull and do a rehearsal run first.
- 유사어: dry run (기술 표준어), trial run (평이), practice run (구어)
- 반의어: a live run (실전 실행)
