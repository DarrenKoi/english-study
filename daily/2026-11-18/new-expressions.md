# 2026-11-18 — 새 표현

오늘 배치는 skewnono 대화 한 건입니다(VeritySEM·Provision recipe 기능 추가). 영어는 poteto-mode 스킬 지침과, 프론트엔드·백엔드 서브에이전트가 써 낸 작업 보고서 두 편에서 나왔습니다. 스킬 지침 쪽은 이미 많이 모았기 때문에 오늘은 보고서 문장을 중심으로 골랐습니다. "무엇을 했고, 무엇을 안 했고, 어디가 걸리는지"를 짧게 적는 보고체를 익히기 좋습니다.

## "One thing to reconcile before merge."
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 보고서 앞머리에서 "합치기 전에 맞춰야 할 것이 하나 있다"고 미리 짚을 때(PR 설명·인수인계 글, 중립~격식)
- 한국어: 병합 전에 정리해야 할 것 한 가지.
- 설명: `reconcile` 은 서로 어긋난 두 상태를 맞춘다는 뜻입니다. 장부 대조(`reconcile the accounts`)에서 온 말이라 "누가 틀렸다"가 아니라 "둘이 안 맞는다"는 어감입니다. 동사 없이 명사구로 끝낸 소제목 문장이고, `to reconcile` 이 thing 을 뒤에서 꾸밉니다.
- 예문: One thing to reconcile before merge: the migration file on my branch and the one on main both claim version 42.
- 유사어: one thing to sort out first (구어), an open item before we merge (회의체), a discrepancy to resolve (격식)
- 반의어: good to merge as is

## "the branch is red on `npm test` until it is committed"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 어떤 조건이 풀릴 때까지 테스트가 실패 상태임을 알릴 때(개발 채팅·PR, 중립)
- 한국어: 그 파일이 커밋되기 전까지 이 브랜치는 `npm test` 가 실패한다.
- 설명: `red` / `green` 은 CI 결과 색을 그대로 형용사로 씁니다. `red on + 검사 이름` 으로 어느 검사에서 실패하는지 붙이고, `until` 절로 언제 풀리는지 밝힙니다. 실패 사실과 해소 조건이 한 문장에 들어 있어 읽는 사람이 다음 행동을 바로 압니다.
- 예문: Main is red on the lint step until someone removes the unused import in `auth.ts`.
- 유사어: the tests fail until … (평이), the build is broken until … (구어), CI will not pass until … (격식)
- 반의어: the branch is green, all checks pass

## "I left it unstaged as theirs."
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 남이 고친 파일이라 내 커밋에 넣지 않았다고 밝힐 때(동료에게 쓰는 작업 메모)
- 한국어: 그건 그쪽 작업이라 스테이징하지 않고 뒀다.
- 설명: `leave + 목적어 + 형용사`(~한 상태로 두다) 뒤에 `as theirs` 가 이유를 대신합니다. "그들의 것으로서"라는 두 단어가 `because it was their change` 를 줄였습니다. 소유대명사 하나로 책임 경계를 긋는 표현입니다.
- 예문: The config change wasn't part of my task, so I left it unstaged as theirs.
- 유사어: I didn't touch it since it's their change (구어), I kept it out of my commit (평이)
- 반의어: I folded it into my commit

## "Nothing blocked the build."
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 문제 목록을 꺼내기 전에 "막힌 건 없었다"고 수위를 먼저 정해 줄 때(보고·회고)
- 한국어: 작업을 막은 건 없었다.
- 설명: 원문은 "Nothing blocked the build. Three gaps showed up:" 입니다. 뒤에 나올 세 항목이 장애물이 아니라 틈이라는 점을 첫 문장이 미리 알려 줍니다. `Nothing` 을 주어로 세워 부정문을 짧게 만드는 방식도 눈여겨보세요. 여기서 `build` 는 컴파일이 아니라 "만드는 일" 전체입니다.
- 예문: Nothing blocked the build, but two questions came up that the spec doesn't answer.
- 유사어: there were no blockers (회의체), it all went through fine (구어), no impediments were encountered (격식)
- 반의어: we hit a blocker, we got stuck on …

## "I did not invent a cadence."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 근거 없는 값을 지어내지 않았다고 밝힐 때(보고서·리뷰 답변, 격식~중립)
- 한국어: 갱신 주기를 제멋대로 지어내지 않았다.
- 설명: `cadence` 는 일이 되풀이되는 간격입니다(`release cadence`, `a weekly cadence`). `invent` 는 "발명하다"보다 "없는 걸 꾸며 내다"에 가깝게 쓰였습니다. 계약에 주기 정보가 없으니 화면에도 적지 않았다는 뜻이고, 축약형 `didn't` 대신 `did not` 을 써서 단호하게 들립니다.
- 예문: The source gave no refresh time, so I did not invent one; the page shows only the data date.
- 유사어: I didn't make one up (구어), I left it out rather than guess (평이), no value was assumed (격식·수동)
- 반의어: I assumed a daily refresh, I filled in a default

## "which I treated as a typo"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 원문의 이상한 부분을 어떻게 해석했는지 밝혀 둘 때(보고서의 가정 목록)
- 한국어: 그걸 오타로 보고 처리했다.
- 설명: 원문은 `the office note literally says "HH:MMSS", which I treated as a typo`. `treat A as B` 는 "A 를 B 로 간주하고 다루다"입니다. 관계절로 덧붙여서 "원문은 이렇고, 나는 이렇게 읽었다"를 한 문장에 담았습니다. `literally says` 는 "글자 그대로는 이렇게 적혀 있다"는 뜻입니다.
- 예문: The ticket says "Febuary 30", which I treated as a typo for February 28.
- 유사어: which I took to be a typo (같은 격식), which I assumed was a typo (평이), which I read as a slip (구어)
- 반의어: which I took literally, which I kept as written

## "Every field name is honoured; nothing diverges."
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 합의한 규격을 그대로 지켰다고 확인해 줄 때(API·계약 준수 보고, 격식)
- 한국어: 필드 이름은 전부 그대로 지켰고 어긋난 곳은 없다.
- 설명: `honour a contract / a promise` 는 "약속을 지키다"의 격식 표현입니다(영국식 철자, 미국식은 `honor`). `diverge` 는 갈라져 달라진다는 뜻. 세미콜론으로 긍정 진술과 부정 진술을 나란히 놓아 같은 사실을 두 번 못 박았습니다.
- 예문: Every deadline in the agreement is honoured; nothing diverges from the schedule we signed.
- 유사어: it matches the spec exactly (평이), I stuck to the contract (구어), fully conformant with the contract (문서체)
- 반의어: it deviates from the contract, it breaks the contract

## "Choices the contract left open"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 규격이 정해 주지 않아 내가 판단한 부분을 따로 묶어 보일 때(설계 메모·보고)
- 한국어: 계약이 정해 두지 않은 선택들.
- 설명: `leave + 목적어 + open` 은 "결정하지 않고 열어 두다"입니다. `Choices (that) the contract left open` 에서 목적격 관계대명사가 빠졌습니다. 사물인 contract 가 주어라서 "누가 빠뜨렸다"는 탓이 없습니다.
- 예문: Here are the choices the spec left open and how I settled each one.
- 유사어: points the spec doesn't cover (평이), unspecified details (문서체), judgment calls (구어)
- 반의어: what the contract pins down, fixed requirements

## "The tests caught one real mock bug"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 테스트가 실제로 값어치를 했다고 알릴 때(작업 보고·스탠드업)
- 한국어: 테스트가 진짜 mock 버그를 하나 잡아냈다.
- 설명: `catch a bug` 는 "버그를 잡아내다"의 기본 연어입니다. `real` 이 붙어서 "형식적 지적이 아니라 진짜 결함"이라는 뜻이 됩니다. 뒤 문장 `It is fixed.` 까지가 한 세트로, 발견과 처리를 두 문장에 끝냅니다.
- 예문: The new contract tests caught one real bug: the total came out as a string when the list was empty.
- 유사어: the tests flagged a genuine bug (조금 격식), the tests turned up a bug (구어), a defect was detected by the tests (격식·수동)
- 반의어: the bug slipped through the tests

## "That test exists to force a conversation"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프론트엔드 서브에이전트 보고)
- 맥락: 검사나 규칙의 목적이 "막기"가 아니라 "사람끼리 이야기하게 만들기"라고 설명할 때(설계 근거·리뷰)
- 한국어: 그 테스트는 논의를 강제하려고 있는 것이다.
- 설명: 원문은 `That test exists to force a conversation whenever a marker is added`. `exist to + 동사` 는 존재 이유를 말하는 틀입니다. `force a conversation` 은 "누군가 반드시 묻고 답하게 만든다"는 뜻으로, 승인 절차·체크리스트의 취지를 설명할 때 그대로 쓸 수 있습니다.
- 예문: The sign-off field exists to force a conversation between design and engineering before anything ships.
- 유사어: it's there to make us talk about it (구어), it serves as a checkpoint for discussion (격식), it's a tripwire (은유·구어)
- 반의어: it's just a formality, a rubber stamp

## "it was outside my scope"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 문제를 봤지만 맡은 범위가 아니라 손대지 않았다고 밝힐 때(보고·메일, 중립~격식)
- 한국어: 내가 맡은 범위 밖이었다.
- 설명: 원문은 `I did not edit CLAUDE.md; it was outside my scope.` 발견은 보고하되 고치지는 않았다는 선 긋기입니다. 핑계처럼 들리지 않으려면 원문처럼 "무엇이 어긋나 있는지"를 먼저 적고 이 말을 붙이면 됩니다.
- 예문: I noticed the pricing table is out of date, but I didn't change it; it was outside my scope.
- 유사어: that wasn't mine to change (구어), it fell outside my remit (영국식·격식), out of scope for this task (문서체)
- 반의어: within my scope, squarely my job

## "cannot be masked as a bad request"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (백엔드 서브에이전트 보고)
- 맥락: 서로 다른 오류가 한 가지 응답으로 뭉개지지 않게 했다고 설명할 때(코드 리뷰·설계 메모)
- 한국어: (엉뚱한 오류가) 잘못된 요청인 것처럼 가려질 수 없다.
- 설명: 원문은 `so an unrelated ValueError cannot be masked as a bad request`. `mask A as B` 는 A 가 B 의 가면을 쓰고 나타난다는 뜻입니다. 서버 버그가 400 응답으로 둔갑하면 원인을 못 찾으니 전용 예외를 따로 뒀다는 설명입니다. 수동태라서 초점이 "무슨 일이 생기지 않는가"에 있습니다.
- 예문: We raise a dedicated error type so that a database failure cannot be masked as a validation problem.
- 유사어: can't be mistaken for (평이), can't pass itself off as (구어), cannot be misreported as (격식)
- 반의어: surfaces as what it is, is reported accurately

## "A recommendation is a judgment, not a validation."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Autonomy" 절)
- 맥락: 의견을 달라는 말에 맞장구가 아니라 실제 판단을 내놓아야 한다고 말할 때(리뷰 문화·피드백 원칙)
- 한국어: 추천은 판단이지 승인 도장이 아니다.
- 설명: `validation` 은 "네 생각이 맞다고 확인해 주기"입니다. `A is B, not C` 대구로 두 낱말의 차이를 한 줄에 세웠습니다. 누가 "이거 괜찮죠?" 하고 물어도 좋다고만 답하지 말라는 원칙으로 씁니다.
- 예문: When I ask for your view on the design, remember that a recommendation is a judgment, not a validation.
- 유사어: I want your honest take, not a rubber stamp (구어), feedback is an assessment, not an endorsement (격식)
- 반의어: just tell me it's fine (구어)

## "Don't silently work around it."
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Non-negotiables" 절)
- 맥락: 고장 난 도구나 절차를 말없이 우회하지 말고 알리라고 할 때(팀 규칙·온보딩)
- 한국어: 말없이 돌아가지 마라.
- 설명: `work around` 는 문제를 고치지 않고 피해 가는 구동사입니다(명사 `a workaround`). 우회 자체보다 `silently` 가 금지의 핵심이라 "돌아가더라도 알려라"는 뜻이 됩니다. 원문 앞 문장은 `Don't block.` 으로, 멈추지도 말고 숨기지도 말라는 두 줄입니다.
- 예문: If the deploy script fails, file a ticket; don't silently work around it by copying files by hand.
- 유사어: don't quietly patch over it (구어), don't paper over it (관용), do not bypass it without reporting (격식)
- 반의어: flag it, raise it

## "You own every subagent's work."
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Subagents" 절)
- 맥락: 일을 맡겼어도 결과 책임은 맡긴 사람에게 있다고 말할 때(위임·매니징 원칙)
- 한국어: 맡긴 일의 결과도 전부 네 책임이다.
- 설명: 업무 영어의 `own` 은 "소유하다"보다 "끝까지 책임지다"입니다(`Who owns this ticket?`). 이어지는 문장이 `Review the diff and write your own summary, don't pass through what it said.` 인데, `pass through` 는 받은 말을 검토 없이 그대로 전달한다는 뜻입니다.
- 예문: You own every contractor's work, so read the report yourself before you forward it to the client.
- 유사어: you're accountable for it (격식), the buck stops with you (관용·구어), it's on you (아주 구어)
- 반의어: it's not on me, hand off responsibility

## "Every claim carries its evidence or its label in the same sentence."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Writing the reply" 절)
- 맥락: 보고서에서 주장마다 근거나 "추정" 표시를 붙이라는 글쓰기 규칙을 말할 때(문서 가이드, 격식)
- 한국어: 모든 주장은 같은 문장 안에 근거나 딱지(측정·추론·추측)를 달고 다닌다.
- 설명: `carry` 는 "지니고 다니다"로, 주장과 근거가 떨어지지 않는다는 그림을 만듭니다. `label` 은 뒤에 나오는 `Measured, inferred, or guess` 세 딱지를 가리킵니다. 현재시제 평서문인데 규칙으로 읽힙니다. 영어 가이드 문서가 `must` 없이 규범을 적는 흔한 방식입니다.
- 예문: In our incident reports, every claim carries its evidence or its label in the same sentence, so readers never wonder what was actually measured.
- 유사어: back up each claim or mark it as a guess (평이), cite or caveat (짧은 구호), substantiate or qualify every claim (격식)
- 반의어: an unsupported claim, hand-waving

## "however program-shaped the phrasing sounds"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Playbooks" 절)
- 맥락: 겉으로 어떻게 들리든 실질로 판단하라고 단서를 달 때(규정·가이드, 격식)
- 한국어: 말만 들으면 아무리 큰 프로젝트 같아 보여도.
- 설명: `however + 형용사 + 주어 + 동사` 는 "아무리 ~해도"의 양보절입니다. `program-shaped` 는 `명사-shaped` 로 즉석에서 만든 형용사로 "프로그램(장기 과제)처럼 생긴"이라는 뜻입니다. `pear-shaped`, `a you-shaped hole` 같은 조어법과 같습니다.
- 예문: A request one person can finish in a day is a task, not a project, however ambitious the wording sounds.
- 유사어: no matter how … it sounds (평이), even if it sounds like … (구어), regardless of how it is phrased (격식)

## "work the user steps away from to trust later"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (poteto-mode 스킬 "Playbooks" 절)
- 맥락: 자리를 비운 사이 돌아가고 나중에 결과를 믿고 받아야 하는 일을 가리킬 때(자동화·위임 설명)
- 한국어: 사용자가 자리를 떠났다가 나중에 믿고 받을 작업.
- 설명: `step away (from)` 은 "잠깐 자리를 비우다"입니다. 회의 중 `I need to step away for a minute` 처럼 씁니다. 여기서는 `work (that) the user steps away from` 으로 전치사가 관계절 끝에 남았고, `to trust later` 가 목적을 덧붙입니다.
- 예문: Overnight batch jobs are work you step away from to trust later, so they need clear logs.
- 유사어: hands-off work (형용사형), work you leave running unattended (평이), set-and-forget tasks (구어)
- 반의어: work you supervise live, hands-on work
