# 2026-10-18 — 새 표현

오늘 배치는 문서 없이 대화 3건이었고 그중 하나는 이 파이프라인 자신의 어제 세션이라 뺐다. 영어는 두 군데서 나왔다. 하나는 skewnono 세션에 딸려 온 `Ponytail` 스킬 문서다. "게으른 시니어 개발자" 페르소나로 쓴 지침이라 짧은 격언과 `X, not Y` 대비문이 유난히 많다. 다른 하나는 같은 세션의 프로젝트 `CLAUDE.md` 로, 규칙 뒤에 "왜 그런가"를 한 문장씩 붙이는 설명문이 잘 쓰였다. 에이전트의 영어 보고와 코드 리뷰 결과에서 몇 줄을 더 골랐다. `load-bearing`, `kill switch`, `swap surface` 처럼 이미 노트에 있는 것은 건너뛰었다.

## "Lazy means efficient, not careless."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 오해받기 쉬운 말을 먼저 던지고 바로 뜻을 좁혀 줄 때(발표·지침·구어 모두)
- 한국어: 게으르다는 건 효율적이라는 뜻이지 대충 한다는 뜻이 아니다.
- 설명: `X means Y, not Z` 는 단어 하나를 자기 식으로 재정의하는 틀이다. 앞 문장에서 일부러 도발적인 말(`lazy`)을 쓴 다음 이 틀로 오해를 걷어 낸다. 쉼표 뒤 `not Z` 는 독립된 문장이 아니라 `Y` 에 붙는 대조구라 동사를 반복하지 않는다.
- 예문: Lazy means efficient, not careless; the goal is less code, not less care.
- 유사어: X here means Y (범위를 "여기서는"으로 한정), by X I mean Y (화자 기준임을 밝힘, 격식), X is about Y, not Z (구어·캐주얼)

## "been paged at 3am for one"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 운영 경험을 내세워 설계 판단에 무게를 실을 때(구어·개발자 사이)
- 한국어: 그런 코드 때문에 새벽 3시에 호출당해 봤다.
- 설명: `get paged` 는 온콜 알림을 받는다는 뜻으로, 원래 삐삐(pager)에서 온 말이다. `for one` 의 `one` 은 앞 문장의 `over-engineered codebase` 를 받는다. `3am` 은 영어 기술 글에서 "가장 괴로운 장애 시각"을 뜻하는 관용 숫자라 그대로 외워 두면 좋다.
- 예문: I've been paged at 3am for a cache layer nobody needed, so I'm wary of adding one here.
- 유사어: get woken up by an alert (평이한 풀이), be on call for it (책임이 있다는 쪽에 초점), carry the pager for X (X 의 운영 책임을 진다, 관용)

## "The best code is the code never written."
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 기능 추가를 거절하거나 삭제를 제안하며 원칙을 한 줄로 댈 때(격언·발표)
- 한국어: 가장 좋은 코드는 애초에 쓰지 않은 코드다.
- 설명: `the X is the X never Y-ed` 꼴의 격언이다. `never written` 은 `that was never written` 에서 관계사와 be 동사를 뺀 과거분사 수식이다. 같은 명사(`code`)를 두 번 반복해 리듬을 만든다.
- 예문: Before we add the retry wrapper, remember that the best code is the code never written.
- 유사어: Less is more. (가장 짧은 격언), No code is faster than no code. (성능 쪽 격언), Every line is a liability. (유지보수 비용 쪽)

## "Stop at the first rung that holds."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 우선순위가 매겨진 선택지를 위에서부터 훑되 되는 데서 멈추라고 지시할 때(지침·문어)
- 한국어: 성립하는 첫 번째 단계에서 멈춰라.
- 설명: `rung` 은 사다리의 가로대로, 원문은 선택지 목록을 `ladder` 에 빗댄다. `hold` 는 여기서 "성립하다, 버티다"라는 자동사다(`the argument holds`, `the rule still holds`). `the first X that Y` 는 조건을 만족하는 첫 항목을 가리키는 관계절 틀이다.
- 예문: Walk the options top to bottom and stop at the first rung that holds.
- 유사어: take the first option that works (평이), go with the simplest thing that could possibly work (XP 격언), stop at the first fit (짧은 구어)
- 반의어: climb all the way up (끝까지 올라간다, 모든 선택지를 다 검토한다)

## "Look before you write"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 새 코드를 짜기 전에 기존 코드를 먼저 찾아보라고 짧게 이를 때(구어·리뷰 코멘트)
- 한국어: 쓰기 전에 먼저 찾아봐라.
- 설명: 속담 `Look before you leap`(돌다리도 두들겨 보고 건너라)의 마지막 단어만 바꾼 말장난이다. 원형을 아는 독자는 즉시 알아듣는다. 격언을 변형해 자기 규칙을 만드는 영어식 글쓰기의 전형이다.
- 예문: Look before you write; the helper you need is probably a few files over.
- 유사어: check what's already there (평이), grep first (개발자 속어), don't reinvent the wheel (관용, 더 일반적)

## "the most common slop"
- 레지스터: casual, technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 질 낮은 코드를 가볍게 낮춰 부를 때(구어·비격식, 공식 리뷰에는 부적절)
- 한국어: 가장 흔한 날림 코드.
- 설명: `slop` 은 원래 "돼지 먹이, 흘린 음식 찌꺼기"로, 최근 개발자 사이에서는 성의 없이 찍어 낸 코드나 AI 가 뱉은 질 낮은 산출물을 가리킨다. 불가산명사라 `a slop` 이라고 하지 않는다. 원문은 "몇 파일 건너에 있는 걸 다시 구현하는 것"이 가장 흔한 slop 이라고 못 박는다.
- 예문: Re-implementing a helper that already lives three files over is the most common slop I see in reviews.
- 유사어: sloppy code (형용사형, 조금 덜 거침), cruft (오래 쌓인 군더더기), boilerplate (반복 틀, 중립적)
- 반의어: tight code (군더더기 없는 코드)

## "a reflex, not a research project"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 어떤 절차를 무겁게 하지 말고 습관처럼 빨리 넘기라고 할 때(구어·지침)
- 한국어: 반사 동작이지 연구 과제가 아니다.
- 설명: `A, not B` 대비에서 `reflex`(생각 없이 나오는 반응)와 `research project`(오래 파고드는 일)를 맞세웠다. 두 단어가 모두 `r` 로 시작해 두운이 맞는다. 영어 격언은 이런 소리 맞춤을 자주 노린다.
- 예문: Checking for an existing helper should be a reflex, not a research project.
- 유사어: second nature (몸에 밴 습관), a quick gut check (빠른 직감 점검), muscle memory (반복으로 익힌 동작)
- 반의어: a deep dive (깊이 파고드는 조사)

## "Deletion over addition. Boring over clever."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 가치 우선순위를 슬로건처럼 나열할 때(지침·발표 슬라이드)
- 한국어: 더하기보다 빼기. 영리함보다 지루함.
- 설명: `X over Y` 는 "Y 보다 X 를 택한다"는 선호 표현으로, 애자일 선언문(`Working software over comprehensive documentation`)에서 굳어진 틀이다. 동사 없이 명사(또는 형용사)만 둘 세워 마침표로 끊는다. 원문은 바로 뒤에 `clever is what someone decodes at 3am` 이라고 이유를 붙여 슬로건이 공허해지지 않게 한다.
- 예문: Our review bar is simple: deletion over addition, boring over clever.
- 유사어: prefer X to Y (완전한 문장형, 격식), favor X (한쪽만 밝힘), err on the side of X (불확실할 때 X 쪽으로 기운다)

## "Never stall on an answer you can default."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 사소한 결정을 묻느라 일을 멈추지 말고 기본값으로 진행하라고 할 때(지침·업무 대화)
- 한국어: 기본값으로 정할 수 있는 답을 기다리느라 멈추지 마라.
- 설명: `stall on X` 는 X 때문에 진행이 서다는 뜻이다. `default` 는 보통 명사지만 여기서는 "기본값으로 처리하다"라는 타동사로 썼다. `an answer (that) you can default` 에서 목적격 관계대명사가 생략됐다.
- 예문: If the naming question has an obvious default, take it and move on; never stall on an answer you can default.
- 유사어: don't block on it (가장 평이한 구어), make a reasonable assumption and proceed (격식), pick a sensible default (행동만 말함)
- 반의어: wait for sign-off (승인을 기다리다)

## "complexity smuggled back in as prose"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 코드를 줄여 놓고 설명을 길게 붙이는 행위를 꼬집을 때(리뷰·문어)
- 한국어: 글의 형태로 다시 몰래 들여온 복잡성.
- 설명: `smuggle in` 은 밀수하듯 몰래 들여온다는 뜻이고 `back` 이 붙어 "쫓아냈던 것을 다시"가 된다. `as prose` 는 "산문의 모습으로"라는 위장 수단이다. 원문은 단순화를 변호하는 문단 하나하나가 결국 복잡성이라고 주장한다.
- 예문: A three-paragraph justification for a one-line change is complexity smuggled back in as prose.
- 유사어: sneak in through the back door (관용, 같은 뉘앙스), creep back in (저절로 스며든다, 의도성 약함), reintroduce (중립·격식)

## "cut a real corner with a known ceiling"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 의도적으로 단순화한 부분과 그 한계를 밝힐 때(코드 주석·설계 메모)
- 한국어: 한계를 알고서 실제로 지름길을 택하다.
- 설명: `cut a corner` 는 "절차를 건너뛰어 대충 하다"라는 관용구인데, 보통은 부정적이다. 원문은 `real`(진짜 생략한) 과 `known ceiling`(어디까지 버티는지 아는 상한)을 붙여 "알고 하는 생략"으로 바꿔 놓았다. `ceiling` 은 성능·규모의 상한선을 뜻하는 기술 글 상용어다.
- 예문: The global lock cuts a real corner with a known ceiling, so the comment names the upgrade path.
- 유사어: take a shortcut (중립적), make a deliberate trade-off (격식, 의도성 강조), accept a known limitation (한계 쪽 초점)
- 반의어: gold-plate (필요 이상으로 공들이다)

## "dresses up as efficiency"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 나쁜 습관이 좋은 가치처럼 보이는 위장을 지적할 때(문어·논평)
- 한국어: 효율로 분장하고 나타난다.
- 설명: `dress up as X` 는 X 로 변장한다는 뜻으로, 할로윈 분장에도 쓰는 일상어다. 추상명사(`laziness`)를 주어로 세워 의인화했다. 원문 전체는 `it dresses up as efficiency and ships a confident wrong fix` 로, 위장과 결과를 `and` 로 이었다.
- 예문: Skipping the read-through dresses up as efficiency, but it ships a confident wrong fix.
- 유사어: masquerade as X (격식, 더 강한 속임수), pass for X (들키지 않고 통한다), look like X on the surface (평이)

## "Read fully, then be lazy."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 순서를 못 박는 짧은 지침(구어·슬로건)
- 한국어: 다 읽고 나서, 그다음에 게을러져라.
- 설명: `A, then B` 로 두 명령문을 잇되 쉼표와 `then` 만으로 선후를 분명히 한다. 부사 `fully` 가 `read` 뒤에 붙어 "끝까지"를 강조한다. 단락 전체(이해를 건너뛰는 게으름은 위험하다)를 다섯 단어로 접은 마무리 문장이다.
- 예문: Trace every caller first; read fully, then be lazy.
- 유사어: understand first, simplify second (격식), measure twice, cut once (목수 속담, 신중함 쪽), do your homework (준비를 다 하라, 구어)

## "Leave the calibration knob"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 최소 구현에서도 조정 가능한 값은 남겨 두라고 할 때(하드웨어·설정 설계)
- 한국어: 보정용 손잡이는 남겨 둬라.
- 설명: `knob` 은 돌리는 손잡이이고, 소프트웨어에서는 사용자가 돌려 맞출 수 있는 설정값을 비유한다. `calibration` 이 붙으면 측정 오차를 맞추는 값이 된다. 원문은 시계가 어긋나고 센서가 틀리는 "물리 세계" 때문에 코드만 줄이지 말고 이 손잡이는 두라고 한다.
- 예문: The motor runs a few percent fast, so leave the calibration knob even in the minimal version.
- 유사어: keep it configurable (평이·격식), expose a tuning parameter (기술 문어), leave a dial for it (`dial` 도 같은 비유)
- 반의어: hard-code it (값을 코드에 박다)

## "The shortest path to done is the right path."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 문서나 발표를 한 줄 구호로 닫을 때
- 한국어: 끝내는 데 가장 짧은 길이 옳은 길이다.
- 설명: `done` 은 보통 형용사지만 여기서는 `path to done` 처럼 "완료"라는 명사 자리에 섰다. 애자일의 `definition of done` 에서 익숙해진 용법이다. `the X path is the right path` 로 같은 명사를 되풀이해 격언 리듬을 낸다.
- 예문: Don't gold-plate the migration script; the shortest path to done is the right path.
- 유사어: ship the simplest thing that works (구어·실무), get to done (완료에 이르다, 동사구), path of least resistance (저항이 가장 적은 길, 때로 부정적)

## "Fix it once, where all callers route through."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 증상이 난 호출부마다 패치하지 말고 공통 경로 한 곳을 고치라고 할 때(리뷰·설계)
- 한국어: 모든 호출자가 지나가는 자리에서 한 번만 고쳐라.
- 설명: `route through X` 는 트래픽이 X 를 경유한다는 네트워크 비유로, 여기서는 함수 호출이 공통 함수를 거친다는 뜻이다. `where` 절이 "그 한 곳"의 조건을 설명한다. 바로 앞 문장 `patching only the path the ticket names leaves every sibling caller still broken` 과 짝으로 읽으면 뜻이 또렷하다.
- 예문: Put the null guard in the shared loader; fix it once, where all callers route through.
- 유사어: fix it at the source (근원에서 고쳐라), patch the choke point (병목 지점을 고쳐라), centralize the fix (격식)
- 반의어: patch each call site (호출부마다 땜질하다)

## "A report names a symptom."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서)
- 맥락: 버그 리포트를 그대로 믿지 말고 원인을 따로 찾으라고 전제를 깔 때(지침·문어)
- 한국어: 리포트에 적힌 건 증상이다.
- 설명: 네 단어짜리 단문이 단락의 전제를 세운다. `name` 은 여기서 "이름을 대다, 지목하다"라는 동사다. 뒤에 `Before you edit, grep every caller …` 가 이어지며 "그러니 원인은 네가 찾아라"로 넘어간다. 짧은 일반 진술 뒤에 긴 행동 지시를 붙이는 지침문의 전형이다.
- 예문: A report names a symptom, so the first job is to find where the symptom actually comes from.
- 유사어: the ticket describes what, not why (풀어 쓴 구어), symptoms aren't causes (격언형), take the report as a starting point, not a diagnosis (격식)

## "the same act that switches it on"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 한 행동이 두 가지 효과를 동시에 낸다는 점을 경고하듯 알릴 때(설계 문서)
- 한국어: 그걸 켜는 바로 그 행동이기도 하다.
- 설명: 원문은 `the cp that creates an adapter is the same act that switches it on` 이다. `the same X that Y` 는 "Y 하는 바로 그 X"라는 동일성 강조 틀이다. 파일 복사가 곧 기능 활성화라는 사실을 `act` 라는 추상명사로 한 번 묶어 두 동작이 분리될 수 없음을 못 박는다.
- 예문: Copying the template is the same act that switches the adapter on, so copy it only when you mean to go live.
- 유사어: X doubles as Y (X 가 Y 역할도 한다), X is also what Y (평이), in one and the same step (격식)

## "the failure mode to avoid"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 규칙을 정하면서 가장 경계하는 실패 형태를 짚을 때(설계 문서·회고)
- 한국어: 피해야 할 실패 형태.
- 설명: `failure mode` 는 공학 용어로 "어떤 식으로 고장 나는가"를 뜻한다. 뒤에 `to avoid` 부정사가 붙어 "피해야 할 바로 그 유형"이 된다. 원문은 `Updating only the doc is the failure mode to avoid` 로, 동명사구를 주어로 세워 규칙 위반을 구체적 행동으로 지목한다.
- 예문: Fixing the doc and leaving the mock untouched is the failure mode to avoid.
- 유사어: the trap to watch for (구어, 함정), the classic mistake (평이), the anti-pattern (개발자 용어)

## "standing in for the real thing rather than drifting from it"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 대역(mock·stub)이 원본을 충실히 대신해야 한다고 설명할 때(설계 문서)
- 한국어: 실물에서 멀어지지 않고 실물을 대신하도록.
- 설명: `stand in for X` 는 배우의 대역처럼 X 를 대신한다는 뜻이고, `drift from X` 는 조금씩 멀어진다는 뜻이다. `A rather than B` 로 둘을 맞세워 "대역이지 변질이 아니다"를 분명히 한다. 분사구문이라 앞 절(`so home development is …`)의 주어를 공유한다.
- 예문: Keep the mock's docstring current so it is standing in for the real thing rather than drifting from it.
- 유사어: faithfully mirror (격식, 충실히 반영), substitute for (중립적), serve as a stand-in (명사형)
- 반의어: diverge from (갈라져 나가다)

## "a guess never has to be avoided, only labelled"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 추정치를 써도 되지만 표시는 하라고 규칙을 세울 때(설계 문서·연구 노트)
- 한국어: 추측은 피할 필요가 없고, 표시만 하면 된다.
- 설명: `never X, only Y` 는 금지가 아니라 조건을 거는 틀이다. `has to be avoided` 와 `(has to be) labelled` 가 병렬이라 뒤쪽 동사구를 생략했다. 영국식 철자 `labelled`(미국식 `labeled`)를 썼다.
- 예문: Mark the fabricated value `OFFICE-VERIFY`; a guess never has to be avoided, only labelled.
- 유사어: assumptions are fine as long as they're flagged (구어 풀이), make the uncertainty explicit (격식), call it out as an estimate (추정치임을 밝히다)

## "That is where the seconds go."
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 느린 실행 시간의 원인을 지목하고 "비정상이 아니다"라고 안심시킬 때(구어·문서 괄호 설명)
- 한국어: 시간은 거기서 다 간다.
- 설명: `that is where X goes` 는 돈·시간·노력이 어디에 쓰이는지 짚는 구어 틀이다(`that's where the money goes`). 바로 앞 `The suite has not rotted` 와 짝으로 읽으면 "느려진 게 아니라 원래 무거운 테스트가 있다"는 변호가 된다. 복수 `seconds` 로 체감 시간을 구체화했다.
- 예문: Each snapshot test builds a real 4000-lot payload; that is where the seconds go.
- 유사어: that accounts for the runtime (격식), that's the bottleneck (병목에 초점), that's what eats the time (구어)

## "Nothing errors — the log just gets corrupted."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 조용히 망가지는 실패를 경고할 때(규칙 문서·리뷰)
- 한국어: 에러는 하나도 안 난다. 로그만 조용히 망가진다.
- 설명: `error` 를 자동사로 써서 `nothing errors`(아무것도 에러를 내지 않는다)라고 했다. 개발자 구어에서 흔한 품사 전환이다. 대시 뒤 `just` 가 "겨우 그것뿐"이 아니라 "그 대신 조용히"라는 뉘앙스를 만든다. 눈에 띄는 실패보다 조용한 실패가 더 나쁘다는 경고다.
- 예문: A broad `git add` won't fail; nothing errors — the log just gets corrupted.
- 유사어: it fails silently (가장 흔한 표현), no exception is raised (격식·정확), it breaks quietly (구어)
- 반의어: it fails loudly (눈에 띄게 실패하다)

## "mislead the next session about what work is still open"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 뒷정리를 안 했을 때 후임이 입는 피해를 설명할 때(인수인계·규칙 문서)
- 한국어: 다음 세션이 어떤 일이 아직 열려 있는지 잘못 알게 만든다.
- 설명: `mislead A about B` 는 A 에게 B 를 오해하게 한다는 뜻이다. `what work is still open` 은 간접의문문으로, `open` 이 "미완료"라는 업무 용어다(`open issue`, `open question`). 남은 워크트리가 거짓 신호가 된다는 점을 사람 아닌 `session` 에 적용했다.
- 예문: Leftover worktrees mislead the next session about what work is still open.
- 유사어: give a false picture of (평이), leave a misleading trail (흔적 쪽 비유), send the next person down the wrong path (구어)

## "is not untidy, it is an app that does not start"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 사소한 미관 문제로 보이는 것이 실은 치명적 오류임을 강조할 때(문서·리뷰)
- 한국어: 지저분한 게 아니라 아예 안 뜨는 앱이다.
- 설명: `is not A, it is B` 로 가벼운 판단(`untidy`)을 부정하고 무거운 사실(`does not start`)로 바꿔 친다. 뒤쪽 `an app that does not start` 는 형용사 대신 명사구로 써서 결과를 눈앞에 세운다. 쉼표로 두 절을 이은 것은 구어적 쉼표 접속이다.
- 예문: Two features with the same folder name is not untidy, it is an app that does not start.
- 유사어: not cosmetic but fatal (격식·압축), that's a hard failure, not a style issue (구어), this breaks boot (사실만)

## "Do not rename one side alone."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md)
- 맥락: 짝으로 묶인 이름을 한쪽만 바꾸지 말라고 경고할 때(규칙 문서·주석)
- 한국어: 한쪽만 따로 이름을 바꾸지 마라.
- 설명: `one side alone` 의 `alone` 은 "혼자서"가 아니라 "그것만 단독으로"라는 뜻이다. 앞 문장이 페이지 경로와 백엔드 폴더가 한 이름을 쓴다고 설명하고, 이 문장이 금지로 받는다. 뒤에 `a one-sided rename spreads across dozens of files` 라고 이유를 붙였다.
- 예문: The slug is shared by routing and logging, so do not rename one side alone.
- 유사어: rename them together or not at all (구어), keep both sides in lockstep (관용, 발맞춰), treat it as a single rename (격식)

## "the way it did before the link was added"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (에이전트 보고)
- 맥락: 변경을 되돌렸을 때 "예전 모습 그대로"임을 알릴 때(보고·구어)
- 한국어: 링크가 들어가기 전에 그랬던 것처럼.
- 설명: `the way it did` 는 `as it did` 의 구어형으로, `did` 가 앞의 동사구(`shows just the ID`)를 대신한다. `before the link was added` 는 수동태 시간절이라 누가 넣었는지는 묻지 않는다. 되돌림을 보고할 때 "원래 상태"를 짧게 가리키는 말이다.
- 예문: The column now shows just the ID, the way it did before the link was added.
- 유사어: as it was before (평이), back to its previous shape (명사형), exactly like it used to (구어)

## "changes how you get there, not who can get in"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (에이전트 보고)
- 맥락: 변경의 영향 범위를 두 측면으로 갈라 안심시킬 때(보고·리뷰)
- 한국어: 거기 가는 경로만 바뀌지, 누가 들어갈 수 있는지는 안 바뀐다.
- 설명: 간접의문문 두 개(`how you get there`, `who can get in`)를 `not` 으로 대비시켰다. 버튼을 지워도 권한 검사는 그대로라는 뜻을 `get there`(도달)와 `get in`(입장)의 대구로 압축했다. 범위가 좁은 변경임을 한 줄에 설명하는 보고 기술이다.
- 예문: Removing the button changes how you get there, not who can get in.
- 유사어: affects navigation, not access (격식·압축), it's a UX change, not a permission change (평이), the door is the same, only the path moved (비유)

## "so it doesn't linger as dead code"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/07a4eb85 (에이전트 보고)
- 맥락: 기능을 뺄 때 딸린 코드까지 지운 이유를 댈 때(커밋 메시지·보고)
- 한국어: 죽은 코드로 남아 있지 않게.
- 설명: `linger` 는 떠나야 할 것이 미적거리며 남는다는 뜻이라 `remain` 보다 부정적이다. `as dead code` 가 남는 형태를 밝힌다. `so (that) it doesn't …` 는 목적절이고 접속사 `that` 이 빠졌다.
- 예문: I removed the `prefix` field along with the labels so it doesn't linger as dead code.
- 유사어: so it isn't left behind (평이), to avoid leaving cruft (`cruft` = 찌꺼기), to keep it from rotting in place (썩는다는 비유)

## "not confirmed from the hunk whether …"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/6bb18a63 (code-review 결과)
- 맥락: diff 조각만 보고 판단할 때 확인 못 한 부분을 밝힐 때(리뷰 코멘트)
- 한국어: 이 hunk 만으로는 …인지 확인되지 않음.
- 설명: 리뷰어가 자기 판단의 한계를 적는 관용 꼬리말이다. `hunk` 는 diff 의 한 변경 덩어리다. 주절 없이 과거분사구(`not confirmed`)로 시작해 세미콜론 뒤에 붙였다. 지적을 하되 "틀릴 수도 있다"를 같은 문장 안에서 밝히는 격식이다.
- 예문: The new gate may block health probes; not confirmed from the hunk whether health is exempted earlier in the hook.
- 유사어: cannot tell from this diff alone (구어), unverified in this context (압축), I may be missing an earlier exemption (1인칭·완곡)
