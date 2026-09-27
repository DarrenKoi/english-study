# 2026-09-28 — 새 표현

> 오늘 배치는 repo 문서 6건과 transcript 9건. repo 문서는 auto_recipe_creator 의 `docs/features/*.md` 로, CLAUDE.md 에서 옮겨 온 한국어 원문이라 표현 소스에서 뺐다. 그래서 표현 22개는 전부 transcript 에서 나왔다. 출처 세션은 skewnono 의 폴더 이름 변경 뒤 office 설정 복구, HV-SEM 빈 이미지 타일 수정, CLAUDE.md/AGENTS.md 정리와 `/doctor` 점검, equipment-data-map 의 spike 작성과 ftp_handler 수정. writing-for-agents 스킬 본문에서도 두 개를 가져왔다. `tell A from B`, `not a blocker`, `best-effort`, `I left it alone`, `Short answer`, `rules out`, `Nothing left to commit` 은 노트에 이미 있어서 제외.

## "The cause is almost certainly X."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 원인을 거의 확신하지만 아직 현장에서 확인하지 못했을 때 결론부터 말하는 첫 문장(장애 답변, 격식 중간).
- 한국어: 원인은 거의 확실히 X다.
- 설명: `almost certainly` 가 확신의 정도를 정확히 적어 준다. `The cause is X.` 는 단정이라 틀리면 신뢰를 잃고 `It might be X.` 는 너무 약하다. 원문은 이 문장 뒤에 커밋 해시와 날짜를 대고 답 끝에서 `I haven't confirmed it against your actual office traceback` 으로 확인 범위를 다시 밝힌다.
- 예문: The cause is almost certainly the folder rename.
- 유사어: The most likely culprit is X (구어, 범인 비유), I'm fairly confident it's X (주관 강조), All signs point to X (정황 강조)
- 반의어: It's hard to say what's causing it. (원인 불명)

## "stayed behind"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 이동·이름 변경·배포 뒤에 따라오지 못하고 원래 자리에 남은 파일이나 설정을 가리킬 때(구어·기술 설명).
- 한국어: (옮겨 가지 못하고) 남아 있다
- 설명: `stay behind` 는 사람이 "뒤에 남다"라는 뜻인데 파일에도 그대로 쓴다. git 이 추적하지 않는 `.env` 가 rename 을 따라가지 못한 상황을 딱 이 동사로 짚었다. 원문에서는 굵은 소제목 `What stayed behind in the old folder:` 로 등장. `left behind` 로 바꾸면 "누가 두고 갔다"는 행위자가 느껴진다.
- 예문: The ignored files stayed behind in the old folder when the repo was renamed. (작성)
- 유사어: got left behind (누군가 빠뜨린 느낌), didn't come along (구어), weren't carried over (격식)
- 반의어: moved over with the rename (함께 옮겨 갔다)

## "Only one of them actually has to be recovered. The rest can be recreated."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 잃어버린 것 목록을 듣고 당황한 상대에게 진짜 급한 건 하나뿐이라고 범위를 좁혀 줄 때(복구 안내).
- 한국어: 실제로 되찾아야 하는 건 하나뿐이고 나머지는 다시 만들면 된다.
- 설명: `recover`(원본을 되찾다)와 `recreate`(새로 만들다)를 대비해 할 일을 두 종류로 가른다. `actually` 는 "보기보다 적다"는 안심의 말. 둘 다 수동태라 파일이 주어가 되어 작업 목록처럼 읽힌다.
- 예문: Only one of them actually has to be recovered. The rest can be recreated.
- 유사어: Only one of these is irreplaceable. (격식), You really only need to get one back. (구어)
- 반의어: All of them are gone for good. (전부 복구 불가)

## "best first"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 선택지 목록을 내밀면서 좋은 순서대로 적었다고 먼저 알려 줄 때(안내문·답변 머리).
- 한국어: 좋은 것부터(순서대로)
- 설명: 원문 `Three places to get it back, best first:` 는 동사 없는 머리말이다. `best first` 두 단어가 "목록 순서에 뜻이 있다"를 알려 줘서 읽는 사람이 1번부터 시도하면 된다. `easiest first`, `most likely first` 처럼 형용사만 바꿔 쓴다.
- 예문: Here are three places to get it back, best first. (작성)
- 유사어: in order of preference (격식), starting with the best option (풀어쓴 말), in order of likelihood (확률 순)
- 반의어: in no particular order (순서 의미 없음)

## "has been working as a backup"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 원래 다른 목적으로 만든 것이 모르는 사이 백업 노릇을 해 왔다고 짚을 때(원인 분석·회고).
- 한국어: (모르는 사이) 백업 역할을 해 왔다
- 설명: 현재완료진행형 `has been working` 이 "과거부터 지금까지 계속"을 담는다. 배포 번들이 비밀 파일 백업으로 설계된 건 아니지만 실제로는 그렇게 기능해 왔다는 말이다. `work as` 는 "~로 기능하다". 의도와 결과를 가르는 표현이라 회고에서 자주 쓴다.
- 예문: The cloud deploy bundle has been working as a backup of those secrets.
- 유사어: has doubled as a backup (본래 용도 겸용), has served as a backup (격식), has quietly been our backup (구어, 의외성 강조)
- 반의어: was never meant to be a backup (의도 부정)

## "The catch is that …"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 설계가 옳다고 인정한 바로 다음에 그 설계의 함정을 꺼낼 때(설계 설명, 구어에 가까움).
- 한국어: 문제는 ~라는 점이다 / 함정은 ~다
- 설명: `catch` 는 "숨은 조건, 함정". 원문은 먼저 `Falling back to mock when the site is unknown is deliberate` 로 설계를 인정하고 `The catch is that …` 으로 약점을 든다. `The problem is` 보다 덜 비난조고 "좋긴 한데 조건이 하나 있다"는 뉘앙스다.
- 예문: The catch is that a misconfigured office PC looks exactly like a home PC.
- 유사어: The downside is that … (중립), The trouble is … (구어), The caveat is that … (격식)
- 반의어: There's no catch. (함정 없음)

## "happen to match"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 두 설정이 의도해서가 아니라 우연히 같아서 돌아가고 있을 때, 그 우연이 깨지기 쉽다고 경고하며(기술 설명).
- 한국어: 우연히 일치하다
- 설명: `happen to + 동사원형` 은 "마침/우연히 ~하다". 여기서는 "설계된 일치가 아니다"를 드러내는 게 핵심이다. 원문 바로 다음 문장이 `Setting PORT on only one side quietly breaks that.` 우연에 기댄 설정은 한쪽만 바꿔도 깨진다.
- 예문: When a port is set nowhere, both sides default to 5050 and happen to match.
- 유사어: line up by coincidence (풀어쓴 말), match by accident (구어)
- 반의어: are kept in sync on purpose (의도적으로 맞춰 둠)

## "That will pin it down."
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 원인 후보가 여럿일 때 특정 정보를 달라고 부탁하고 그걸로 결론이 난다고 알릴 때(원격 디버깅 대화).
- 한국어: 그걸로 확정할 수 있다.
- 설명: `pin down` 은 핀으로 꽂아 고정하듯 "정확히 특정하다". 원문은 `Tell me which page … and paste its row … That will pin it down.` 부탁 바로 뒤에 붙여 왜 그 정보가 필요한지 알려 준다. 같은 대화의 `Paste what it returns and we'll narrow it down.` 은 "후보를 좁히다" 단계라 `pin down` 보다 한 걸음 앞이다.
- 예문: Tell me which page shows mock data and paste its row from the boot log (or the whole table). That will pin it down.
- 유사어: That'll narrow it down. (후보 축소, 아직 하나는 아님), That should settle it. (결론 강조)
- 반의어: That won't tell us much. (도움 안 되는 정보)

## "That error isn't why you're seeing X."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 상대가 새로 발견한 에러를 원인으로 오해할 때 곁가지라고 선을 긋고 본론으로 돌아갈 때(디버깅 대화).
- 한국어: 그 에러 때문에 X가 보이는 건 아니다.
- 설명: `why` 절이 보어 자리에 들어간 구조(`A isn't why B`)로 "A는 B의 원인이 아니다"를 짧게 말한다. 원문은 이어서 `You can ignore it for now.` 로 행동 지침까지 준다. 상대 발견을 무시하지 않고 `What it is:` 로 정체를 설명한 뒤 `Back to the real problem.` 으로 돌아가는 흐름이 좋다.
- 예문: That error isn't why you're seeing mock data.
- 유사어: That's unrelated to X. (평이), That's a separate issue. (중립), That's a red herring. (관용, 가짜 단서)
- 반의어: That's exactly why you're seeing X. (바로 그게 원인)

## "the one mode … is the one mode without a safety net"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 가장 중요한 경우가 하필 보호 장치가 빠진 경우라는 아이러니를 짚을 때(원인 분석·리뷰).
- 한국어: 사용자에게 꼭 필요한 바로 그 모드만 안전망이 없다
- 설명: `the one X … is the one X …` 반복 구조가 "하필 그것"을 강조한다. `the one` 은 "유일한 바로 그". 앞부분에 `reused the URLs but not the retry wrapper` 로 무엇이 빠졌는지 대고 결론을 이 대구로 맺는다. 노트의 `safety net` 은 명사 하나였고 여기서는 문형 전체가 학습 포인트다.
- 예문: The grid mode was added later for HV-SEM and reused the URLs but not the retry wrapper, so the one mode HV-SEM users actually need is the one mode without a safety net.
- 유사어: the case that matters most is the least protected (평이), ironically, the critical path has no fallback (격식)
- 반의어: the riskiest path is the best guarded (가장 위험한 곳이 가장 잘 막혀 있다)

## "sticky (per session)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 한번 정해진 상태가 저절로 풀리지 않고 세션 끝까지 남는 동작을 설명할 때(상태 관리 버그 설명).
- 한국어: (한번 걸리면) 계속 붙어 있는, 풀리지 않는
- 설명: `sticky` 는 "끈적한"이라서 상태가 들러붙어 안 떨어지는 모습이다. 범위를 정하는 건 `per session`. 원문에서 `gaveup` 상태가 세션 내내 남아 같은 파라미터로 돌아와도 다시 시도하지 않는 게 버그의 절반이었다. 반대 방향의 수정 커밋은 `a non-sticky gaveup` 이라고 불렀다.
- 예문: The gate's ceiling is a "stuck job" guard, but it cannot tell a stuck job from a large one that is still making progress, and `gaveup` is sticky per session.
- 유사어: persists for the session (평이), pinned for the session (원문 다른 곳에서 쓴 말)
- 반의어: resets on the next visit (다음 방문에 초기화)

## "This alone turns X into Y."
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 여러 수정안 중 하나만으로도 증상 대부분이 바뀐다고 효과를 구체적으로 말할 때(수정 제안).
- 한국어: 이것 하나만으로도 X가 Y로 바뀐다
- 설명: `This alone` 은 "다른 건 안 해도 이것만으로". `turn X into Y` 는 상태 변화를 보여 준다. 원문은 빈 타일이 사라진다고 하지 않고 `late-arriving images`(늦게 도착하는 이미지)로 바뀐다고 적어서 과장 없이 효과를 그렸다.
- 예문: This alone turns most blank tiles into late-arriving images.
- 유사어: On its own, this fixes most of X. (평이), This single change converts X into Y. (격식)
- 반의어: This barely moves the needle. (효과 미미)

## "targeted the wrong thing"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 내가 돌린 작업이 엉뚱한 대상을 향했다고 스스로 밝히고 바로 원인과 재실행을 알릴 때(작업 보고).
- 한국어: 엉뚱한 대상을 겨냥했다
- 설명: 주어를 `The review I launched` 로 잡아 내 실수임을 숨기지 않는다. 콜론 뒤에 원인(`passing a commit hash made it review that commit`)을 한 문장으로 대고 다음 문장에서 `Re-running against my commit.` 으로 조치를 알린다. 실수 → 원인 → 조치 세 박자가 짧다.
- 예문: The review I launched targeted the wrong thing: passing a commit hash made it review that commit (the earlier FTP fix), not my change on top of it.
- 유사어: was aimed at the wrong target (평이), reviewed the wrong commit (구체), missed the mark (구어, 결과 강조)
- 반의어: hit the right target (제대로 겨냥했다)

## "Your setup is in good shape."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 점검 결과를 보고할 때 큰 문제가 없다는 결론부터 말할 때(상태 보고 첫 문장).
- 한국어: 설정 상태가 양호하다.
- 설명: `in good shape` 는 몸 상태에 쓰는 말을 시스템에 옮긴 관용구. 원문은 이 한 문장 뒤에 근거(clean install, latest version, auto mode 기본값)를 나열하고 `The only cleanup is small` 로 남은 일을 줄여서 알린다. 결론 → 근거 → 남은 일 순서.
- 예문: Your setup is in good shape.
- 유사어: Everything looks healthy. (중립), You're in decent shape. (조금 낮춘 평가), No major issues. (격식)
- 반의어: This needs some work. / It's in rough shape. (손볼 곳이 많다)

## "The frontier is X."
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 할 일 지도에서 지금 막 착수할 수 있는 맨 앞 작업을 가리킬 때(다음 단계 안내).
- 한국어: 지금 최전선(다음에 할 일)은 X다.
- 설명: `frontier` 는 개척지의 경계. 의존 관계가 있는 작업 목록에서 "선행 조건이 다 풀려 지금 할 수 있는 것"을 한 단어로 가리킨다. 원문은 `Everything left on the map waits on its result` 로 이어서 나머지가 왜 멈춰 있는지 설명한다. `wait on` 은 결과가 나오기를 기다리며 막힌 상태.
- 예문: The frontier is issue #6, the office run.
- 유사어: The next unblocked task is X. (평이), X is up next. (구어)
- 반의어: X is still blocked. (아직 막혀 있음)

## "Agreed, and that is cleaner given X."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대 제안에 동의하면서 왜 더 나은지 근거 하나를 바로 붙일 때(코드 논의).
- 한국어: 동의한다. X 를 생각하면 그쪽이 더 깔끔하다.
- 설명: `Agreed` 한 단어로 동의를 먼저 주고 `given X` 로 이유를 붙인다. `given` 은 "~를 고려하면"(`considering` 보다 짧은 말). 뒤에 명사절(`ftp_handler/ is read-only here`)이 접속사 없이 바로 온다. 동의만 하면 맞장구, 이유가 붙으면 판단이 된다.
- 예문: Agreed, and that is cleaner given `ftp_handler/` is read-only here.
- 유사어: Good call — that's cleaner since X. (구어), I agree; that approach is cleaner in light of X. (격식)
- 반의어: I'd push back on that. (반대 의견 개진)

## "Stale skills do more damage than stale docs."
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 낡은 문서보다 낡은 자동 실행 지시가 더 위험하다고 우선순위를 매길 때(점검 결과 설명).
- 한국어: 낡은 스킬은 낡은 문서보다 해가 크다.
- 설명: `stale A … than stale B` 로 같은 형용사를 반복해 A와 B만 비교하게 만든다. `do damage` 는 "해를 끼치다"로 `harm` 보다 구어적이다. 원문은 이유로 스킬 설명이 매 세션 컨텍스트에 있고 자동으로 발동한다는 점을 댄다.
- 예문: Stale skills do more damage than stale docs.
- 유사어: An outdated skill is worse than an outdated doc. (평이), A stale instruction is more dangerous than a stale reference. (일반화)
- 반의어: harmless leftovers (해 없는 잔재)

## "check facts against the files on disk, not against other documentation"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 감사·검증 원칙을 말할 때. 다른 문서끼리 대조하지 말고 실제 파일로 확인하라는 교훈(회고·리뷰).
- 한국어: 다른 문서가 아니라 디스크의 실제 파일로 사실을 확인하라
- 설명: `check A against B` 는 "A를 B에 대 보다". `not against …` 로 전치사까지 반복해 대조를 선명하게 했다. 원문 사례는 Python 버전이었다. CI 설정과 옛 커밋 메시지가 전부 3.14라 맞는 줄 알았는데 `.venv/pyvenv.cfg` 는 3.11이었다.
- 예문: In an audit, check facts against the actual files on disk, not against other documentation.
- 유사어: verify against the source of truth (격식), go to the source (구어)
- 반의어: take the docs' word for it (문서 말을 그대로 믿다)

## "nothing left to fall out of sync over"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 두 파일의 중복을 없애서 이제 서로 어긋날 거리 자체가 없다고 설명할 때(문서 정리 보고).
- 한국어: 어긋날 거리가 남아 있지 않다
- 설명: `fall out of sync over X` 는 "X 를 두고 어긋나다". 목적어 X 가 `nothing` 으로 앞에 나가면서 전치사 `over` 가 문장 끝에 홀로 남았다(전치사 좌초). 영어에서는 자연스러운 어순이다. 격식체로 바꾸면 `nothing over which to fall out of sync` 인데 거의 안 쓴다.
- 예문: `AGENTS.md` now holds only content that `CLAUDE.md` doesn't have, so the two files have nothing left to fall out of sync over.
- 유사어: no overlap left to drift (간결), nothing that can go stale in two places (풀어쓴 말)
- 반의어: bound to drift apart (결국 어긋날 수밖에 없다)

## "could actually have misled X"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 고친 오류들 중 실제로 피해를 냈을 법한 하나를 골라 강조할 때(수정 보고).
- 한국어: 실제로 X 를 잘못 이끌 수도 있었다
- 설명: `could have + p.p.` 는 "(일어나진 않았지만) 그럴 수 있었다". `actually` 가 "다른 항목은 사소하지만 이건 진짜"라는 대비를 준다. 목록 중간에 이 한 줄을 끼워서 읽는 사람의 주의를 모았다.
- 예문: This one could actually have misled Codex.
- 유사어: This one had real potential to mislead X. (격식), This one might have sent X down the wrong path. (구어)
- 반의어: This one was harmless. (피해 없음)

## "earn its place"
- 레지스터: professional, technical
- 출처: transcript:[user] auto-recipe-creator (writing-for-agents 스킬 본문)
- 맥락: 문서·코드의 한 줄이 존재할 값을 하는지 따질 때(글쓰기 원칙·리뷰, 격식).
- 한국어: 자리값을 하다, 있을 자격을 얻다
- 설명: `earn` 은 노력해서 얻는다는 뜻이라 "그냥 있는 게 아니라 쓸모로 자리를 번다"는 뉘앙스다. 원문은 `only as …` 로 조건을 좁힌다. 금지문은 긍정문으로 바꿀 수 없는 가드레일일 때만 자리값을 한다는 말. 같은 문서의 `it earns even harder pruning` 처럼 `earn` 을 "(대가로) 받을 만하다"로도 쓴다.
- 예문: A prohibition earns its place only as a hard guardrail you cannot phrase positively.
- 유사어: justify its existence (격식), pull its weight (구어, 제 몫을 하다)
- 반의어: dead weight (자리만 차지하는 짐)

## "sediment"
- 레지스터: technical, professional
- 출처: transcript:[user] auto-recipe-creator (writing-for-agents 스킬 본문)
- 맥락: 추가는 쉽고 삭제는 두려워서 문서에 낡은 층이 쌓이는 현상을 이름 붙일 때(문서·코드 유지보수 논의).
- 한국어: 퇴적물(쌓이기만 하는 낡은 층)
- 설명: 지질학 비유다. 콜론 뒤 `stale layers that settle because adding feels safe and removing feels risky` 가 정의이고 `feels safe` / `feels risky` 대구가 원인을 짚는다. `until you must core down through them` 은 시추하듯 파 내려가야 한다는 그림으로 비유를 끝까지 밀고 간다.
- 예문: Without a pruning discipline the default fate is sediment: stale layers that settle because adding feels safe and removing feels risky, until you must core down through them to find what is still live.
- 유사어: cruft (개발 속어, 쓸모없는 잔재), accretion (격식, 서서히 쌓임), bit rot (코드가 낡아 가는 현상)
- 반의어: a well-pruned document (잘 가지치기된 문서)
