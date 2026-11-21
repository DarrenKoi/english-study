# 2026-11-22 — 새 표현

오늘 배치는 auto_recipe_creator 대화 한 건입니다. Radmin 으로만 붙는 장비를 SecureVDI 너머에서 자동화할 길이 있는지 따져 본 세션이에요. 대화 본문은 한국어라서 영어는 세션에 함께 실린 글에서 골랐습니다. 프로젝트 `CLAUDE.md`, Concise 출력 스타일 지침, ponytail 지침, 커밋 서명 안내 네 군데입니다. `CLAUDE.md` 쪽은 "왜 이렇게 묶어 뒀는가"를 한 문장으로 밝히는 설계 메모가 많고, Concise 쪽은 `A over B`, `never as B`, `only when` 처럼 둘 중 하나를 고르게 하는 틀이 이어집니다.

## "The user chose brevity over narration."
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 누가 무엇을 버리고 무엇을 택했는지 한 문장으로 못박을 때(지침·회의록, 중립 격식)
- 한국어: 사용자는 과정 설명보다 간결함을 택했다.
- 설명: `choose A over B` 는 "B 를 두고 A 를 고르다"입니다. `over` 하나가 "~대신, ~보다 우선해서"를 맡아서 `instead of` 보다 짧고, 둘을 저울에 올려 본 뒤 골랐다는 어감이 실립니다. `narration` 은 작업 과정을 중계하듯 풀어 쓰는 말이에요.
- 예문: For the incident report, we chose accuracy over speed and held it until the logs were verified.
- 유사어: prefer A to B (취향·경향, 한 번의 결정이라는 느낌은 약하다), opt for A rather than B (격식, 문어), go with A, not B (회화)
- 반의어: want both, refuse to pick

## "Use headers, tables, and bullet lists only when they carry real structure, never as decoration."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 문서 작성 규칙에서 서식을 쓸 조건과 쓰지 말 조건을 한 문장에 나란히 둘 때(스타일 가이드, 격식)
- 한국어: 제목·표·글머리표는 실제 구조를 담을 때만 쓰고 장식으로는 절대 쓰지 마라.
- 설명: `only when A, never as B` 가 허용 조건과 금지를 쉼표 하나로 맞세웁니다. `carry` 는 "담아 나르다"라서 `carry structure`, `carry meaning`, `carry weight` 처럼 형식이 내용을 실어 나른다는 그림이 됩니다. `as decoration` 은 관사 없이 "장식용으로".
- 예문: Use color in a chart only when it carries information, never as decoration.
- 유사어: only where they add structure (평이), solely to convey structure (격식), not just to look tidy (회화)
- 반의어: for show, as window dressing

## "Never trade correctness for brevity"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 두 가치가 부딪칠 때 어느 쪽을 내주면 안 되는지 규칙으로 적을 때(가이드·리뷰 코멘트, 격식)
- 한국어: 간결함을 얻자고 정확성을 내주지 마라.
- 설명: `trade A for B` 는 "A 를 내주고 B 를 얻다"입니다. 순서를 헷갈리기 쉬운데 내주는 쪽이 먼저 와요. 명사 `trade-off` 와 뿌리가 같고, `Never` 로 시작해서 흥정 자체를 막습니다.
- 예문: We should never trade data integrity for a faster release.
- 유사어: sacrifice A for B (잃는 쪽이 아깝다는 어감, 격식), give up A to get B (회화), compromise on A for the sake of B (타협이라는 뉘앙스)
- 반의어: have it both ways, keep both

## "Conciseness never means withholding requested information."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 규칙이 엉뚱하게 해석되지 않도록 경계를 그을 때(정책 문서, 격식)
- 한국어: 간결하게 쓴다는 것이 요청받은 정보를 주지 않는다는 뜻은 결코 아니다.
- 설명: `X never means doing Y` 는 "X 라고 해서 Y 해도 된다는 뜻은 아니다"라고 오해를 미리 막는 틀입니다. `withhold` 는 줄 수 있는데도 쥐고 안 내주는 것으로, 정보·급여·동의·세금에 두루 씁니다. `requested information` 은 과거분사가 앞에서 꾸민 꼴.
- 예문: Being polite never means withholding bad news from the customer.
- 유사어: hold back (구어), keep … from someone (평이), leave out (빠뜨린다는 쪽, 고의성은 약하다)
- 반의어: disclose, hand over, volunteer

## "Skip hedging boilerplate."
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 글에서 버릇처럼 붙는 "~일 수도 있습니다" 류 문구를 빼라고 할 때(글쓰기 피드백, 구어에 가까움)
- 한국어: 얼버무리는 상투 문구는 빼라.
- 설명: `hedge` 는 원래 울타리이고, 말에서는 단정을 피하려고 둘러치는 `might`, `perhaps`, `it could be that` 따위입니다. `boilerplate` 는 어디에나 똑같이 붙는 정형 문구. 둘을 붙여 "습관적으로 다는 면피용 단서"가 됐어요. `skip` 은 `omit` 보다 가볍습니다.
- 예문: Skip the hedging boilerplate and just tell me whether the migration is safe to run.
- 유사어: drop the disclaimers (회화), cut the qualifiers (글쓰기 조언), omit unnecessary caveats (격식)
- 반의어: hedge your bets, pile on caveats

## "Report outcomes, decisions, and anything the user must act on."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 보고에 무엇을 남길지 기준을 줄 때(업무 지침, 격식)
- 한국어: 결과와 결정, 그리고 사용자가 조치해야 할 것은 모두 보고하라.
- 설명: `act on` 은 "~을 근거로 움직이다, ~에 조치를 취하다"입니다. 정보·조언·피드백이 목적어로 와요. `anything the user must act on` 은 관계대명사가 빠지고 전치사 `on` 이 끝에 남은 관계절입니다.
- 예문: The weekly summary should list only the alerts that someone must act on.
- 유사어: anything that needs the user's attention (평이), action items (명사, 회의 용어), anything requiring follow-up (격식)
- 반의어: FYI only, for the record

## "Where these rules conflict with more general communication or formatting guidance elsewhere in your instructions, these rules win."
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)
- 맥락: 규칙 둘이 부딪칠 때 우선순위를 정해 두는 문장(정책·설정 문서, 격식이지만 동사는 구어)
- 한국어: 이 규칙이 지침의 다른 곳에 있는 일반적인 소통·서식 안내와 충돌하면 이 규칙이 이긴다.
- 설명: 문두의 `Where` 는 장소가 아니라 "~하는 경우에는"입니다. 법률·규정 문체에서 `If` 대신 자주 써요. 뒤는 `these rules win` 세 단어로 끝납니다. 길고 격식 있는 조건절 뒤에 짧은 구어 동사를 둬서 결론이 또렷합니다.
- 예문: Where the team style guide conflicts with the linter's defaults, the style guide wins.
- 유사어: take precedence (격식, 가장 흔한 문어 표현), override (기술 문서), prevail (법률 문체)
- 반의어: yield to, defer to

## "take precedence over this reminder"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (커밋 서명 안내 system-reminder)
- 맥락: 어느 지시가 먼저인지 문서로 밝힐 때(정책·계약·설정 설명, 격식)
- 한국어: 이 안내보다 우선한다.
- 설명: 원문은 `the user's own instructions … take precedence over this reminder`. `precedence` 는 `precede`(앞서다)의 명사로, 발음은 '프레서던스'에 가깝습니다. 전치사는 `over`. 위 항목의 `win` 과 뜻이 같고 격식만 다릅니다.
- 예문: Environment variables take precedence over the values in the config file.
- 유사어: win (구어), override (기술 문서, 덮어쓴다는 그림), come first (회화)
- 반의어: be subordinate to, give way to

## "one process, so the single RCS cursor stays serialized"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, workflow_3e Extension)
- 맥락: 락 없이도 동시 접근이 안 일어나는 이유를 설계 메모에 적을 때(기술 문서)
- 한국어: 프로세스가 하나라서 하나뿐인 RCS 커서는 직렬 상태를 유지한다.
- 설명: `serialize` 는 여기서 직렬화(JSON)가 아니라 "한 번에 하나씩 차례로 하게 하다"입니다. `stay + 과거분사` 는 그 상태가 깨지지 않고 이어진다는 뜻이고, `one process, so …` 는 주어·동사 없이 원인을 명사구로만 던진 메모 문체예요.
- 예문: All writes go through one worker, so access to the file stays serialized without a lock.
- 유사어: runs one at a time (평이), is mutually exclusive (격식, 이론 용어), never overlaps (결과만 말할 때)
- 반의어: runs concurrently, races

## "`WorkflowRunner` is not to be given routing"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, State-machine layer)
- 맥락: 설계 문서에서 "이건 하지 않기로 정했다"를 규정처럼 적을 때(격식, 문어)
- 한국어: `WorkflowRunner` 에 라우팅을 넣어서는 안 된다.
- 설명: `be to + 동사` 는 정해진 일·지시를 나타내고, 부정 `is not to be + p.p.` 는 "~되어서는 안 된다"는 금지입니다. `must not` 보다 덜 명령조이고 이미 내려진 결정을 알리는 말투예요. `give X routing` 의 수동이라 `be given routing` 꼴이 됐습니다.
- 예문: The staging database is not to be used for load tests.
- 유사어: must not be given (직접적인 금지), should stay free of (부드럽게), don't add routing to (회화·명령문)
- 반의어: is free to, may

## "prove a CV change in workflow_2 → port only the verified change into workflow_3"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Active offline CV bench)
- 맥락: 실험장과 운영 코드를 나눠 쓰는 작업 순서를 적을 때(개발 프로세스 메모)
- 한국어: CV 변경은 workflow_2 에서 입증하고, 검증된 것만 workflow_3 으로 옮긴다.
- 설명: `prove` 는 수학 증명만이 아니라 "실제로 통한다는 것을 보여 주다"로도 씁니다(`prove it out` 도 같은 뜻). `port A into B` 는 다른 환경으로 옮겨 심는 것. `only the verified change` 에서 `only` 의 자리가 옮길 범위를 좁힙니다.
- 예문: We prove each optimization on the benchmark first and port only the verified ones into the main branch.
- 유사어: validate … then migrate (격식), try it out in … and bring over what works (회화), backport (이전 버전으로 옮길 때만)
- 반의어: develop in place, ship untested

## "deliberately omits `eqp_id` so it can't be re-added"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Production consensus cache)
- 맥락: 빠진 것이 실수가 아니라 설계임을 코드 주석이나 문서에 남길 때(기술 문서)
- 한국어: 다시 넣지 못하게 하려고 `eqp_id` 를 일부러 뺐다.
- 설명: `deliberately` 가 "실수 아님"을 알리고, `so (that) it can't be …` 가 그렇게 한 목적을 답니다. 누가 선의로 되돌려 놓는 일을 막으려는 문장이에요. `re-add` 는 사전에 잘 없지만 `re-` 를 붙여 만든 말이 기술 문서에서는 자연스럽습니다.
- 예문: The function deliberately omits a timeout parameter so callers can't shorten it by accident.
- 유사어: leaves out … on purpose (구어), intentionally excludes (격식), has no … by design (결과만 말할 때)
- 반의어: forgets to include, accidentally drops

## "shared per-recipe staging would otherwise race across tools"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Production consensus cache)
- 맥락: 어떤 가드가 없으면 생길 경쟁 상태를 한 구절로 설명할 때(기술 문서)
- 한국어: 그러지 않으면 레시피별 공용 staging 을 두고 장비끼리 경쟁 상태가 된다.
- 설명: `race` 를 동사로 쓰면 "경쟁 상태에 빠지다"입니다. `would otherwise` 는 "이 장치가 없다면 ~했을 것"이라는 가정이고, 조건절을 따로 쓰지 않아도 됩니다. `across tools` 는 여러 장비에 걸쳐서.
- 예문: The lock exists because two cron jobs would otherwise race on the same output file.
- 유사어: would collide (충돌이라는 결과 쪽), would step on each other (회화), would contend for (자원을 두고 다툴 때, 격식)
- 반의어: is isolated per tool, runs sequentially

## "otherwise the code reads an empty root and rcp/msr appear absent"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Root constant)
- 맥락: 설정을 안 하면 겉으로 어떤 증상이 보이는지 미리 알려 줄 때(운영 문서, 트러블슈팅)
- 한국어: 그러지 않으면 코드가 빈 루트를 읽어서 rcp/msr 가 없는 것처럼 보인다.
- 설명: `appear absent` 는 "없다"가 아니라 "없어 보인다"입니다. 데이터는 다른 경로에 멀쩡히 있다는 뜻이 `appear` 한 단어에 들어 있어요. `appear + 형용사` 는 `seem` 보다 겉모습 쪽에 무게가 있고 문서에서 더 자주 씁니다.
- 예문: Set the region first; otherwise the CLI queries the wrong account and your buckets appear empty.
- 유사어: look like they're missing (회화), seem to be missing (평이), show up as missing (화면·로그에 그렇게 찍힐 때)
- 반의어: show up, are found

## "`action_enabled`/`typing_enabled` default to the inverse of `SAFE_MODE`"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Code Conventions)
- 맥락: 한 설정의 기본값이 다른 설정의 반대값으로 정해진다고 설명할 때(설정 문서)
- 한국어: `action_enabled`/`typing_enabled` 의 기본값은 `SAFE_MODE` 의 반대값이다.
- 설명: `the inverse of X` 는 불리언이면 뒤집은 값, 수학이면 역수·역함수입니다. `the opposite of` 보다 정확한 기술 용어예요. `default to` 는 주어가 사람이 아니라 설정값이어도 됩니다.
- 예문: The `verbose` flag defaults to the inverse of `quiet`, so setting both is rarely necessary.
- 유사어: the opposite of (평이), the negation of (논리 용어), mirrors … inverted (풀어 쓴 말)
- 반의어: follows, mirrors

## "Reviving one needs the checkpoint re-imported first"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Flask Proxy VLM Architecture)
- 맥락: 없앤 것을 되살리려면 먼저 무엇이 필요한지 적을 때(운영 문서)
- 한국어: 하나를 되살리려면 먼저 체크포인트를 다시 들여와야 한다.
- 설명: `need + 목적어 + 과거분사` 는 "목적어가 ~되어야 한다"입니다(`needs the checkpoint re-imported` = `needs the checkpoint to be re-imported`). 동명사 `Reviving one` 이 주어이고, `revive` 는 끊겼던 서비스·프로젝트·논의를 다시 살릴 때 씁니다.
- 예문: Reviving the old dashboard needs its database restored first.
- 유사어: bring back (구어), restore (원래 상태로 돌리는 쪽), resurrect (완전히 죽은 것을 살린다는 과장 섞인 말)
- 반의어: retire, decommission

## "What touches production today is only the read-only mirror"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, State-machine layer)
- 맥락: 새 구성요소가 운영에 미치는 범위를 좁게 못박을 때(설계 문서·리뷰 답변, 격식)
- 한국어: 지금 운영에 닿는 것은 읽기 전용 미러뿐이다.
- 설명: `What … is only X` 는 유사 분열문으로, 문장 끝의 X 에 초점이 갑니다. `touch production` 은 "운영 환경에 영향을 주다"이고 `today` 가 "지금은 그렇다, 나중은 모른다"는 단서를 답니다.
- 예문: What touches the payment tables today is only the nightly reconciliation job.
- 유사어: the only thing that affects production is (평이), production exposure is limited to (격식, 보고서), only … runs in prod (회화)
- 반의어: is wired into the hot path, runs everywhere

## "Lazy means writing less code, not picking the flimsier algorithm."
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (ponytail 지침 Rules)
- 맥락: 원칙이 잘못 쓰이는 경우를 잘라낼 때(팀 규칙·코드리뷰, 구어체)
- 한국어: 게으르다는 것은 코드를 덜 쓴다는 뜻이지, 더 부실한 알고리즘을 고른다는 뜻이 아니다.
- 설명: `X means A, not B` 로 정의와 오해를 한 번에 가릅니다. `flimsy` 는 얇아서 쉽게 찢어지는 물건에 쓰는 말이고, 근거·변명·코드가 허술할 때도 써요. 비교급 `flimsier` 는 둘 중 더 부실한 쪽.
- 예문: Moving fast means shipping smaller changes, not picking the flimsier design.
- 유사어: shakier (불안정하다는 쪽), weaker (가장 평이), less robust (격식, 기술 문서)
- 반의어: sturdier, more robust
