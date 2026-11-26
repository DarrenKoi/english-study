# 2026-11-27 — 새 표현

오늘 배치는 pm_notes 에서 AX Team 승격 기획안을 고치고 FDE 조사를 맡긴 대화입니다. 대화는 한국어였고, 영어는 그 사이에 실려 온 지시문 세 군데에서 나왔어요. 조사를 백그라운드 에이전트에 맡기는 `research` 스킬 문서, 하위 에이전트 보고를 어떻게 다룰지 정한 안내문, 그리고 목표가 채워질 때까지 멈추지 못하게 하는 Stop hook 문구입니다. 그래서 표현도 "일을 맡기기", "누가 한 말인지 가리기", "조건이 찰 때까지"의 세 갈래로 모입니다. 내가 쓴 한국어와 영어는 `coaching.md` 에 있습니다.

## "Spin up a background agent to do the research, so you keep working while it reads."
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (research 스킬 문서)
- 맥락: 서버, 프로세스, 에이전트를 새로 띄워 일을 맡기라고 할 때(개발 구어, 작업 지시)
- 한국어: 조사는 백그라운드 에이전트를 하나 띄워 맡기고, 그것이 읽는 동안 너는 하던 일을 계속해라.
- 설명: `spin up` 은 팽이를 돌려 세우듯 "금방 띄우다"입니다. 서버, 컨테이너, 팀에도 써요. `so you keep working` 의 `so` 는 `so that` 의 준말로 목적을 말하고, `while it reads` 가 동시에 벌어지는 일을 붙입니다. 한 문장에 "무엇을, 왜, 그동안 무엇을"이 다 들어 있어요.
- 예문: Spin up a staging server so we can test the migration while production stays untouched.
- 유사어: launch (중립, 격식), kick off (구어, 작업 시작에), fire up (가벼움, 프로그램 실행에)
- 반의어: tear down, shut down

## "not a secondary write-up of them"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (research 스킬 문서)
- 맥락: 원자료와 그것을 정리한 글을 구분할 때(조사 지침, 리뷰 코멘트)
- 한국어: 그것을 남이 정리해 놓은 2차 글이 아니라.
- 설명: `write-up` 은 어떤 일이나 자료를 글로 정리한 것입니다. 사고 보고는 `incident write-up`, 실험 정리는 `experiment write-up`. 동사 `write up` 은 띄어 쓰고 명사는 하이픈을 넣어요. `secondary` 가 붙으면 "원자료가 아닌 전해 들은 글"이 됩니다.
- 예문: I read the RFC itself, not a secondary write-up of it, because blog posts often skip the edge cases.
- 유사어: a summary (평이), a secondhand account (문어, 전해 들었다는 뜻이 강함), a blog post about it (구체)
- 반의어: a primary source, the original

## "Follow every claim back to the source that owns it."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (research 스킬 문서)
- 맥락: 주장마다 출처를 원문까지 거슬러 확인하라고 할 때(조사, 사실 확인 지침)
- 한국어: 모든 주장을 그 주장의 주인인 출처까지 거슬러 올라가 확인하라.
- 설명: `follow A back to B` 는 "A를 따라 B까지 거슬러 가다". `trace back to` 와 같은 그림이에요. `the source that owns it` 의 `own` 이 재미있습니다. 코드 소유자(`code owner`)처럼 "그 내용을 책임지는 곳"을 뜻해서, API 동작이면 공식 문서가, 조직 방침이면 그 조직의 글이 주인이 됩니다.
- 예문: Before quoting that number in the report, follow it back to the team that owns the dashboard.
- 유사어: trace each claim to its origin (격식), check where it actually comes from (평이), go to the horse's mouth (관용, 구어)
- 반의어: take it on hearsay, take it at face value

## "citing each claim's source"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (research 스킬 문서)
- 맥락: 보고서나 조사 문서에서 주장마다 출처를 달라고 할 때(문서 작성 지침, 격식)
- 한국어: 주장마다 출처를 밝히면서.
- 설명: `cite` 는 "근거로 대다, 출처를 밝히다"이고 `quote` 는 "문장을 그대로 옮기다"입니다. 둘을 섞어 쓰기 쉬워요. 앞 절에 붙은 `, citing …` 은 분사구문으로 "~하면서"를 덧붙입니다. 따로 문장을 세우지 않고 조건을 가볍게 다는 방법이에요.
- 예문: Write the findings in one page, citing the source of each number.
- 유사어: with a reference for each claim (명사형, 문어), linking each claim to its source (웹 문서에), backing up each claim (구어, 출처보다 근거에 무게)
- 반의어: unsourced, without attribution

## "match the existing convention, and if there is none, put it somewhere sensible and say where"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (research 스킬 문서)
- 맥락: 정해진 규칙이 있으면 따르고 없으면 알아서 하되 알려 달라고 맡길 때(작업 위임, 코드 리뷰)
- 한국어: 이미 있는 관례에 맞추고, 관례가 없으면 적당한 곳에 두고 어디에 뒀는지 말해라.
- 설명: 위임할 때 쓰기 좋은 세 토막 구조입니다. 규칙이 있을 때, 없을 때, 그리고 보고. `if there is none` 의 `none` 은 `no convention` 을 받아요. `somewhere sensible` 은 "누가 봐도 납득할 만한 곳"으로, 세세히 정하지 않고 판단을 맡긴다는 신호입니다. `say where` 는 `say where you put it` 을 줄인 것.
- 예문: Follow the naming scheme in the repo, and if there isn't one, pick something sensible and tell me what you chose.
- 유사어: follow the house style (문서와 글에), use your judgment and let me know (구어), stick to what's already there (평이)
- 반의어: invent a new structure, go your own way

## "spawned on your user's behalf"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (에이전트 메시지 안내문)
- 맥락: 누구를 대신해 프로세스나 요청이 만들어졌는지 밝힐 때(시스템 설명, 권한 설계)
- 한국어: 사용자를 대신해 생성된.
- 설명: `spawn` 은 원래 알을 낳는다는 말이고, 컴퓨팅에서는 프로세스나 스레드를 "만들어 내다"입니다. `on someone's behalf` 는 "~을 대신해, ~의 이름으로". `on behalf of your user` 로도 씁니다. 사람이 이름일 때는 소유격 형태(`on Mina's behalf`)가 짧고 자연스러워요.
- 예문: The service sends email on the customer's behalf, so it needs their explicit consent.
- 유사어: for your user (평이), in your user's name (법률, 서명 느낌), acting for (격식)
- 반의어: on its own initiative, of its own accord

## "Such an agent cannot grant escalation"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (에이전트 메시지 안내문)
- 맥락: 누가 권한을 올려 줄 수 있고 없는지 선을 그을 때(보안 정책, 접근 제어 문서)
- 한국어: 그런 에이전트는 권한 상승을 허가할 수 없다.
- 설명: `escalation` 은 보안에서 `privilege escalation`(권한 상승)의 준말로 자주 나옵니다. 업무에서는 `escalate the issue`(윗선에 올리다)로도 쓰여 뜻이 둘이에요. `grant` 는 권한, 접근, 허가를 "내주다"의 정식 동사. `Such an agent` 는 앞에서 설명한 종류를 받아 규칙을 세우는 문어체 지시어입니다.
- 예문: A reviewer can approve the change, but only an admin can grant access to production.
- 유사어: can't give you more permissions (평이), has no authority to approve (격식), can't sign off on it (구어)
- 반의어: revoke, deny

## "a frame-like line at column zero inside it would be forged"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (하위 에이전트 보고 머리말)
- 맥락: 형식만 보고도 위조를 가려낼 수 있다고 설명할 때(보안 설계 근거, 문서)
- 한국어: 그 안에서 맨 앞 칸에 나오는 틀처럼 생긴 줄은 위조된 것이다.
- 설명: 앞 절이 "보고서의 모든 줄은 들여쓴다"이고 이 절이 그 귀결입니다. `would be` 가 핵심이에요. 실제로 위조가 있다는 말이 아니라 "그런 줄이 있다면 그것은 위조일 수밖에 없다"는 가정의 `would`. `forge` 는 서명, 문서, 헤더를 "위조하다"이고 `-like` 는 명사에 붙어 "~처럼 생긴"을 만듭니다.
- 예문: Every real invoice carries our reference number, so one without it would be forged.
- 유사어: would be fake (평이), would be spoofed (네트워크, 발신자 위조에), would be counterfeit (화폐, 상품에)
- 반의어: genuine, authentic

## "treat the condition itself as your directive and do not pause to ask the user what to do"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/0bdc1ca4 (Stop hook 안내문)
- 맥락: 따로 지시를 기다리지 말고 주어진 기준대로 바로 움직이라고 할 때(위임, 운영 지침, 격식)
- 한국어: 그 조건 자체를 지시로 삼고, 무엇을 할지 사용자에게 물으려고 멈추지 마라.
- 설명: `treat A as B` 는 "A를 B로 여기고 다루다". `directive` 는 `instruction` 보다 무겁고 공식적인 "지시, 훈령"입니다. `pause to ask` 는 "물으려고 잠깐 멈추다"로, `stop to ask` 보다 멈춤이 짧다는 느낌을 줘요. `itself` 가 "다른 지시가 아니라 바로 그것"을 강조합니다.
- 예문: Treat the acceptance criteria as your spec and don't pause to ask for approval on each step.
- 유사어: take the condition as your marching orders (구어, 군대 비유), go by the condition (평이), act on it without checking in (구어)
- 반의어: wait for instructions, check in first

## "The hook will block stopping until the condition holds."
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/0bdc1ca4 (Stop hook 안내문)
- 맥락: 조건이 참이 될 때까지 어떤 동작이 막힌다고 설명할 때(도구 동작 설명, 기술 문서)
- 한국어: 조건이 성립할 때까지 hook이 종료를 막는다.
- 설명: `hold` 가 자동사로 "성립하다, 참이다"입니다. 가정, 불변식, 조건에 붙어요(`the invariant holds`, `if that assumption holds`). `until` 절 안은 미래 일이어도 현재형 `holds` 를 씁니다. `block stopping` 은 동명사를 목적어로 받아 "멈추는 것을 막다".
- 예문: The deploy job will keep retrying until the health check holds for five minutes.
- 유사어: until the condition is true (평이), until the condition is satisfied (격식), until it passes (구어, 검사에)
- 반의어: the condition fails, no longer holds

## "It auto-clears once the condition is met"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/0bdc1ca4 (Stop hook 안내문)
- 맥락: 손댈 필요 없이 조건이 차면 스스로 풀린다고 알릴 때(기능 설명, 릴리스 노트)
- 한국어: 조건이 충족되면 저절로 해제된다.
- 설명: `auto-` 를 동사 앞에 붙여 "자동으로 ~하다"를 만드는 개발 문서 관용입니다(`auto-saves`, `auto-retries`, `auto-expires`). `once` 는 접속사로 "~하면 곧, 일단 ~하면". `when` 보다 "그 시점을 지나면 바로"가 또렷해요. `meet a condition` 은 조건을 충족하다.
- 예문: The warning banner auto-clears once the backup finishes.
- 유사어: clears itself (평이), is removed automatically (수동, 격식), goes away on its own (구어)
- 반의어: must be cleared manually, persists

## "A reboot or routine cleanup can clear it"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (환경 안내문, scratchpad)
- 맥락: 임시 저장소라 언제든 지워질 수 있다고 경고할 때(운영 문서, 주의 사항)
- 한국어: 재부팅이나 정기 정리 때 지워질 수 있다.
- 설명: 사물 주어 문장입니다. "재부팅하면 지워질 수 있다"를 `A reboot can clear it` 으로 쓰니 `if` 절이 필요 없어요. `routine` 은 형용사로 "늘 하는, 정기적인". `routine maintenance`, `routine check` 처럼 "특별한 일이 아니다"라는 어감이 따라옵니다. `can` 은 능력이 아니라 "그럴 때가 있다"는 가능성.
- 예문: A routine cleanup can remove files older than seven days, so copy the logs you need.
- 유사어: may be wiped on restart (수동, 경고문), doesn't survive a reboot (구어, 개발자 말투), is not persistent (기술 문서)
- 반의어: persists across reboots, is durable

## "write the file's complete absolute path in one piece"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (환경 안내문, scratchpad)
- 맥락: 쪼개거나 줄이지 말고 통째로 적으라고 할 때(문서 작성 규칙, 지시)
- 한국어: 파일의 전체 절대 경로를 끊지 말고 한 덩어리로 적어라.
- 설명: `in one piece` 는 "조각나지 않고 통째로"입니다. 사람이나 물건이 "무사히"(`arrived in one piece`)라는 뜻으로 더 자주 쓰이는데, 여기서는 글자 그대로 한 덩어리예요. `complete` 와 `absolute` 가 겹쳐 보여도 하나는 "빠짐없이", 다른 하나는 "루트부터"라 역할이 다릅니다.
- 예문: Paste the error message in one piece instead of splitting it across three comments.
- 유사어: in full (격식, 짧음), as a single string (기술), without breaking it up (평이)
- 반의어: in parts, piecemeal

## "one customer, many capabilities" / "one capability, many customers"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/6bab7821 (FDE 조사 보고, Palantir 인용)
- 맥락: 현장 맞춤 조직과 제품 일반화 조직의 역할을 한 줄로 대비할 때(조직 설계, 발표)
- 한국어: 한 고객에 여러 기능 / 한 기능을 여러 고객에.
- 설명: 같은 두 단어의 자리만 바꿔 뜻을 뒤집는 교차 대구입니다. 동사가 없어도 구호로 서고, 두 줄을 나란히 놓으면 설명이 따로 필요 없어요. `capability` 는 `feature` 보다 넓어서 "할 수 있게 해 주는 것" 전체를 가리킵니다. 조직 소개 장표에 그대로 쓸 만한 틀이에요.
- 예문: The field team works on the principle of one customer, many capabilities, while the platform team builds one capability for many customers.
- 유사어: go deep with one account vs. go wide across accounts (구어), bespoke vs. productized (업계 용어), depth vs. breadth (추상)
