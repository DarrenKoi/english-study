# 2026-09-25 — 새 표현

> 오늘 배치는 transcript 8건뿐이고 repo 문서와 spool 노트는 없었다. 표현 22개는 모두 `[assistant]` 영어에서 골랐다. 출처는 skewnono 세션 셋(TTTM 화면 개편, 장비 상태 방문 집계와 API 키 로그, venv), equipment-data-map 세션 둘(위키 레이아웃 개편, ftp 크기 확인), auto-recipe-creator 세션 둘(이벤트 폴더 로깅, 다중 알람 처리). `in lockstep with`, `push back`, `age out`, `that's your call`, `cosmetic`, `on purpose`, `a drop-in replacement` 는 노트에 이미 있어서 뺐다.

## "a rewiring job and a deletion job"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 기능 개편이 새 로직 없이 연결만 바꾸고 지우는 일이라고 작업 성격을 규정할 때(설계 메모·리뷰, 격식 중간).
- 한국어: 배선을 다시 하는 일이자 지우는 일
- 설명: `job` 앞에 명사를 붙여 "어떤 종류의 작업인지"를 한 번에 말한다. 원문은 이 말 뒤에 `No new math is needed.` 를 붙여 "어려운 계산은 이미 있다"를 못 박는다. 작업 규모를 가늠시키는 데 효과가 크다.
- 예문: Making the tuning reactive is therefore a rewiring job (map click → `picked`) and a deletion job (chip, picker bar, gate fetch).
- 유사어: mostly plumbing (구어, "배관 작업"), a wiring change rather than new logic (설명적), a refactor, not a feature (개발자 구어)
- 반의어: a from-scratch build (처음부터 새로 짓는 일)

## "One decision I made for you:"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 위임받은 일 중 상대 확인 없이 내가 정해 버린 부분을 보고서에서 따로 밝힐 때(작업 보고·채팅).
- 한국어: 제가 대신 정한 게 하나 있습니다:
- 설명: `I made for you` 는 관계대명사가 빠진 접촉절. 결정 사실을 숨기지 않고 앞에 내세우면 되돌릴 기회를 주는 셈이 된다. 원문도 끝에 `If you still want …, tell me and I'll add it back` 으로 되돌리는 길을 열어 둔다.
- 예문: One decision I made for you: removing PM 튜닝 also takes the Up gate card, the pm_planning fetch and the Hold stat off this page.
- 유사어: One call I made without asking: (구어, 솔직함), I took the liberty of … (격식, 약간 사과조), Heads-up on one decision: (가벼움)
- 반의어: I'll leave that decision to you. (결정을 넘김)

## "the smallest honest place (for X) is …"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 빼 버린 기능을 되살린다면 어디에 두는 게 최소 변경이면서 억지가 없는지 제안할 때(설계 논의).
- 한국어: (X 를 둔다면) 가장 작으면서도 억지 없는 자리는 …
- 설명: `honest` 는 코드·UI 가 실제 동작을 속이지 않는다는 뜻으로 개발 글에서 자주 쓴다. `smallest` 로 변경 범위를, `honest` 로 정합성을 동시에 챙긴다. 뒤에 `That means …` 로 그 대가를 이어 말하면 완성된다.
- 예문: If you want it back, the smallest honest place is inside the 튜닝 목표 card for the clicked tool.
- 유사어: the least invasive spot (기술 문서체), the natural home for it (평이), the minimal correct place (딱딱함)
- 반의어: a bolt-on (억지로 덧붙인 것)

## "so I have a real position to argue from"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 토론·협상 전에 근거 자료를 먼저 챙기는 이유를 말할 때(회의 준비, 구어·문어 모두).
- 한국어: 제대로 된 입장을 가지고 논쟁할 수 있도록
- 설명: `a position to argue from` 은 "~에서부터 논증을 펼칠 입장"으로 전치사 `from` 이 끝에 남는 구조. `real` 은 막연한 의견이 아니라 사실에 기댄 입장이라는 뜻을 더한다.
- 예문: Before opening Codex I need the current layout on record, so I have a real position to argue from.
- 유사어: so I'm arguing from facts (평이), to ground my position (격식), so I'm not just guessing (구어)
- 반의어: argue from thin air (근거 없이 주장하다)

## "Where X changed my mind"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 토론 결과를 정리하면서 상대 주장에 설득된 지점을 소제목으로 세울 때(회의록·보고서).
- 한국어: X 가 내 생각을 바꾼 부분
- 설명: `where` 절이 통째로 명사 노릇을 하는 소제목. 설득당한 부분을 따로 밝히면 토론이 형식이 아니었음을 보여 준다. 원문은 앞서 `I'm pushing back on three` 로 반대한 지점도 밝혀 균형을 맞췄다.
- 예문: Where Codex changed my mind: "the file exists" isn't enough to skip a download.
- 유사어: Points I conceded (격식, 협상 어휘), What I got wrong (구어, 자기비판 강함), Where I came around (구어)
- 반의어: Where I held my ground (입장을 지킨 부분)

## "\"X\" isn't enough to Y."
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 누군가 내건 단순한 조건이 판단 근거로 부족하다고 반박할 때(설계 리뷰, 격식 중간).
- 한국어: "X"만으로는 Y 하기에 부족하다.
- 설명: 상대 조건을 따옴표로 그대로 세워 주어로 쓴다. 바로 다음 문장에 반례(`A half-finished download … also exists.`)를 붙여야 설득력이 생긴다.
- 예문: "The file exists" isn't enough to skip: a half-finished download or a hand-copied file also exists.
- 유사어: X alone doesn't justify Y (격식), X is necessary but not sufficient (논리 용어), X doesn't cut it (구어)
- 반의어: X is reason enough to Y (그것만으로 충분하다)

## "solve different problems"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 비슷해 보이는 두 방안이 사실은 다른 문제를 푼다고 갈라 설명할 때(설계 논의).
- 한국어: 서로 다른 문제를 푼다
- 설명: 두 해법을 주어로 묶고 `solve different problems` 로 끝낸 뒤 세미콜론 뒤에서 `the first …; the second …` 로 하나씩 풀어 준다. 혼동된 두 개념을 떼어 놓는 가장 짧은 방법.
- 예문: The old SHA dedup and your "skip if already downloaded" solve different problems.
- 유사어: aren't substitutes for each other (명확), address separate concerns (격식), are apples and oranges (구어)
- 반의어: do the same job (같은 일을 한다)

## "The drift is already real."
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 문서가 두 곳에 중복돼 있으면 어긋날 수 있다는 걱정이 가정이 아니라 이미 벌어졌다고 지적할 때(리뷰).
- 한국어: 어긋남은 이미 실제로 일어났다.
- 설명: `drift` 는 사본끼리 조금씩 달라지는 현상. `already real` 로 "앞으로 그럴 수 있다"가 아니라 "벌써 그렇다"를 강조한다. 뒤에 실제로 어긋난 예를 하나 들어야 한다.
- 예문: The drift is already real: `spike.py` keeps whichever directory is visited first, not the first in code point order.
- 유사어: they've already diverged (평이), this isn't hypothetical (강조), the copies already disagree (구체)
- 반의어: it's only a theoretical risk (아직 가정일 뿐)

## "a pass-through, not a reimplementation"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 중계 계층이 로직을 새로 짜지 않고 원래 구현을 그대로 호출할 뿐이라고 설명할 때(아키텍처 설명).
- 한국어: 새로 구현한 게 아니라 그냥 넘겨주는 통로
- 설명: `A, not B` 대비로 역할을 좁힌다. 이 성질 덕분에 두 경로가 같은 결과를 낸다는 주장이 뒤따른다.
- 예문: The proxy server route just calls the direct class's `size_dirs` and serializes the report, so the proxy is a pass-through, not a reimplementation.
- 유사어: a thin wrapper (흔한 기술 용어), it just forwards the call (구어), a relay (간결)
- 반의어: a parallel implementation (따로 짠 구현)

## "fail loudly instead of silently"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 테스트·타입 계약이 문제를 조용히 넘기지 않고 드러나게 만든다고 말할 때(기술 설명).
- 한국어: 조용히 넘어가지 않고 요란하게 실패하다
- 설명: `make + 목적어 + fail` 5형식과 함께 자주 쓴다. 원문에서는 `what makes a signature drift … fail loudly instead of silently` 구조로 주어가 명사절이다.
- 예문: The Protocol plus `test_both_transports_are_drop_in` is what makes a signature drift between the two classes fail loudly instead of silently.
- 유사어: surface immediately (중립), blow up early (구어), fail fast (설계 원칙 용어)
- 반의어: slip through unnoticed (눈치채지 못한 채 지나가다)

## "only if that X proves awkward in practice"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 지금은 기존 방식으로 충분하니 실제로 불편이 드러나면 그때 새로 만들자고 할 때(리뷰·설계, 격식).
- 한국어: 실제로 써 보니 그 방식이 불편하다고 드러날 때만
- 설명: `prove + 형용사` 는 "(해 보니) ~로 판명되다". `in practice` 가 "이론이 아니라 실제로"를 덧붙인다. YAGNI 를 정중하게 말하는 틀.
- 예문: Add a dedicated method only if that call shape proves awkward in practice.
- 유사어: if it turns out to be clumsy (평이), should it prove cumbersome (격식↑), if it actually gets in the way (구어)
- 반의어: just in case (혹시 몰라서 미리)

## "I think you're right to question it."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 상대가 던진 의문이 타당하다고 먼저 인정하고 근거를 이어 말할 때(회의·채팅, 부드러움).
- 한국어: 의문을 가지신 게 맞는 것 같아요.
- 설명: `be right to + 동사` 는 "~하는 게 옳다". 상대의 판단력을 인정하는 말이라 이어지는 설명이 반박이 아닌 확인으로 들린다.
- 예문: I think you're right to question it: every time someone picks a tool on home, 장비 상태 gets counted.
- 유사어: Good instinct. (구어, 짧음), Your concern is well founded. (격식), You've put your finger on something. (관용)
- 반의어: I don't think that's a concern. (걱정할 일 아니다)

## "What's really being counted is X, not Y."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 지표가 겉으로 재는 것과 실제로 재는 것이 다르다고 짚을 때(데이터 분석·보고).
- 한국어: 실제로 세고 있는 건 Y 가 아니라 X 다.
- 설명: `What's being counted` 는 수동 진행형이 든 명사절 주어. `really` 로 겉과 속을 가르고 `X, not Y` 로 정정한다. 지표 해석 오류를 지적하는 정석 문형.
- 예문: What's really being counted is how often people entered e-beam, not how often they used 장비 상태.
- 유사어: This metric actually measures X (중립), In effect, we're counting X (격식), It's really a proxy for X (분석 용어)
- 반의어: It measures exactly what it says. (지표 그대로다)

## "The data is already there; what's missing is X."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 새 기능 요청에 "수집은 이미 되고 있고 보여 주는 화면만 없다"고 범위를 좁혀 답할 때(요구사항 논의).
- 한국어: 데이터는 이미 있다. 빠진 건 X 다.
- 설명: 세미콜론으로 "있는 것 / 없는 것"을 한 문장에 대칭으로 놓는다. `what's missing` 명사절이 주어. 작업량이 생각보다 작다는 메시지를 준다.
- 예문: Yes. The data is already there; what's missing is a screen that shows it.
- 유사어: We already capture it; we just don't surface it. (기술 구어), The gap is visibility, not collection. (격식)
- 반의어: We'd have to start logging it first. (수집부터 해야 함)

## "\"Who\" really means \"whose X\""
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 질문에 쓴 단어의 실제 의미가 다르다고 한 단어 바꿔치기로 짚을 때(설명·주의 사항).
- 한국어: "누가"는 사실 "누구의 X 인지"를 뜻한다
- 설명: 따옴표로 두 단어를 나란히 세워 정의를 바로잡는다. `who` 와 `whose token` 처럼 한 글자 차이로 대비가 선명하다.
- 예문: "Who" really means "whose token": a token shared with a colleague still shows up under the owner.
- 유사어: Strictly speaking, X is Y (격식), What you'll see is Y, not X (평이)
- 반의어: mean exactly what it says (말 그대로다)

## "Don't fork into X. Fix it in place."
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 새 폴더·복제본을 만들지 말고 기존 코드를 고치자고 단호하게 권할 때(설계 권고, 결론 먼저).
- 한국어: X 로 갈라 복사하지 말고 그 자리에서 고쳐라.
- 설명: 명령문 두 개로 결론을 먼저 던진다. `fork into` 는 "~라는 갈래로 복제해 나가다", `in place` 는 "제자리에서". 바로 다음에 복제의 대가(`every future fix twice`)를 댄다.
- 예문: Don't fork into `workflow_3_deploy`. Fix it in place.
- 유사어: Amend the existing code rather than copying it. (평이), Keep a single codebase. (원칙형)
- 반의어: Start a fresh copy. (새 사본으로 시작하다)

## "patches around this problem"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 기존 코드가 근본 원인을 고치지 않고 우회로 땜질하고 있다고 지적할 때(코드 리뷰).
- 한국어: 이 문제를 우회해서 땜질한다
- 설명: `patch` 뒤에 `around` 가 붙으면 문제를 없애는 게 아니라 비켜 가는 뉘앙스. 이어서 어떻게 땜질하는지(`guessing … from their file modified times`)를 보여 주면 비판이 구체적이 된다.
- 예문: `monitor/cycle_images.py` already patches around this problem by copying images after each cycle.
- 유사어: works around it (중립), papers over it (부정적, 덮어 버림), a band-aid for it (구어)
- 반의어: fixes the root cause (근본 원인을 고친다)

## "so one tool can't hog X"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 공유 자원을 하나가 독차지하지 못하게 막는 장치를 설명할 때(구어체 기술 설명).
- 한국어: 한 장비가 X 를 독차지하지 못하게
- 설명: `hog` 는 원래 돼지. 동사로 쓰면 "혼자 욕심껏 차지하다". 회의나 채팅에서 자원 독점을 가볍게 말할 때 딱 맞다. 문서체에서는 `monopolize` 로 바꾼다.
- 예문: Tools that fail or are occupied go into a 300s cooldown, so one tool can't hog the RCS cursor.
- 유사어: monopolize (격식), starve the others (기술 용어, 다른 쪽이 굶는다), keep it all to itself (평이)
- 반의어: take turns (돌아가며 쓰다)

## "which I don't think is worth it"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 고칠 수 있는 한계를 인정하면서 비용 대비 가치가 없다고 판단을 덧붙일 때(보고·채팅).
- 한국어: 그럴 가치는 없다고 본다
- 설명: 계속적 용법 `, which` 가 앞 절 전체(대책)를 받고 그 안에 `I don't think` 가 끼어든 구조. 영어는 부정을 `think` 쪽에 둔다(`I think it isn't` 보다 자연스럽다).
- 예문: Fixing that would mean tagging output per thread, which I don't think is worth it.
- 유사어: which isn't worth the complexity (구체), which I'd skip (구어), the cost outweighs the benefit (격식)
- 반의어: which is well worth doing (충분히 할 만하다)

## "nearly impossible in practice. Still, …"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 버그가 실제로 일어날 확률은 낮다고 인정하면서도 고쳐야 하는 이유를 댈 때(리뷰 판정).
- 한국어: 실제로는 거의 불가능하다. 그래도 …
- 설명: `in practice` 로 이론과 현실을 가른 뒤 `Still,` 로 뒤집는다. 확률이 아니라 원칙(`the Episode files are meant never to be deleted`)을 근거로 삼는 흐름.
- 예문: It's nearly impossible in practice, because the alarm feed handles each alarm only once. Still, the Episode files are meant never to be deleted.
- 유사어: vanishingly unlikely (격식), a one-in-a-million case (구어), an edge case at best (평이)
- 반의어: bound to happen sooner or later (언젠가 반드시 터진다)

## "an optimization nobody has needed yet"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 리뷰 제안 중 성능 개선을 건너뛴 이유를 한 줄로 댈 때(리뷰 응답).
- 한국어: 아직 아무도 필요로 하지 않은 최적화
- 설명: `nobody has needed` 는 현재완료 부정으로 "지금까지 필요한 적이 없다". `yet` 이 "나중엔 필요할 수도"를 열어 둔다. 거절이지만 상대 제안을 깎아내리지 않는다.
- 예문: Caching extraction for files with identical bytes: skipped, because it's an optimization nobody has needed yet.
- 유사어: premature optimization (용어, 약간 비판조), not a bottleneck today (구체), nice to have, not needed (구어)
- 반의어: a known bottleneck (이미 드러난 병목)

## "That tension is the whole decision."
- 레지스터: professional
- 출처: transcript:[user] equipment-data-map (writing-for-agents 스킬 본문)
- 맥락: 양쪽 극단의 부작용을 나란히 보인 뒤 판단의 핵심을 한 문장으로 요약할 때(글·강의, 격식 중간).
- 한국어: 그 긴장이 결정의 전부다.
- 설명: 앞 문장 `Push too little down and the top bloats; push too much and you hide …` 는 "명령문 + and" 조건 구조가 둘 겹친 것. 그 뒤에 짧은 단정문을 놓아 무게를 싣는다.
- 예문: Push too little down and the top bloats; push too much and you hide material the agent needs. That tension is the whole decision.
- 유사어: That trade-off is the crux. (격식), That's the balancing act. (구어), Everything hinges on that trade-off. (평이)
- 반의어: There's no real trade-off here. (고민할 거리가 없다)
