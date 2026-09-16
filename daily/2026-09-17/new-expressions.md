# 2026-09-17 — 새 표현

> repo 문서 2건(equipment-data-map 아키텍처, skewnono Recipe TAT 구현 계획)은 본문이 한국어고 영어는 식별자·명령어·파일 경로뿐이라 표현을 뽑지 않았다. 19개 모두 transcript 에서 나왔고 그중 `trim down` 은 내가 쓴 `[user]` 문장이다. 노트에 이미 있는 `the vintage of X`, `just say the word`, `idempotent`, `fail closed`, `on purpose`, `backfill`, `byte-for-byte identical`, `reach for` 는 뺐다.

## "trim down"
- 레지스터: conversational
- 출처: transcript:[user] auto-recipe-creator
- 맥락: 로그·문서·목록처럼 양이 넘치는 것을 필요한 만큼만 남기자고 할 때(구어·협업 채팅)
- 한국어: (넘치는 부분을) 쳐내서 줄이다
- 설명: 내가 쓴 `can we trim down some RCS related info` 에서 나왔다. `trim` 은 머리카락이나 잔가지를 다듬는 동사라 "전부 없애자"가 아니라 모양은 살리고 넘치는 것만 깎자는 말로 들린다. `down` 이 붙어 양을 줄이는 방향이 또렷해진다. 목적어가 명사면 `trim down the logs`, `trim the logs down` 둘 다 되지만 대명사면 반드시 가운데에 넣어 `trim it down` 으로 쓴다.
- 예문: Can we trim down the RCS logs so the errors actually stand out?
- 유사어: cut down on (구어, 양 감소에 초점), pare down (조금 격식, 핵심만 남긴다는 어감), declutter (시각적 정리)
- 반의어: pad out, bulk up

## "those are readings, not chatter"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 로그를 줄이면서 어떤 줄은 왜 남기는지 근거를 댈 때(작업 보고·코드 리뷰)
- 한국어: 그건 측정값이지 잡담 로그가 아니다
- 설명: 원문은 `bbox/refined-point lines kept — those are readings, not chatter.` 이다. `chatter` 는 원래 쉴 새 없는 수다를 말한다. 로그 맥락에서는 "돌고 있다"는 사실 말고는 정보가 없는 줄이 된다. `readings` 는 계기에서 읽어 낸 값이라 판단 근거로 쓰인다. `A, not B` 대구 하나로 남길 줄과 지울 줄의 기준을 세웠다.
- 예문: Keep the coordinate lines in quiet mode; those are readings, not chatter.
- 유사어: signal, not noise (가장 흔한 대체, 중립), data, not status spam (구어, 조금 거칢)
- 반의어: pure noise

## "X pays rent"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 평소엔 번거롭게 느껴지던 규칙이나 설계가 실제 상황에서 값을 해냈다고 말할 때(회고·설계 논의)
- 한국어: (그 규칙이) 제 몫을 한다, 밥값을 한다
- 설명: 원문은 `This is why the "One CLI, thin skills" invariant pays rent.` 이다. 자리를 차지하고 사는 대가로 월세를 내듯, 지켜야 하는 규칙이 그만한 가치를 돌려준다는 은유다. 한국어 "밥값 한다"와 결이 거의 같다. 사전에 실린 표준형은 `earn its keep` 이고 `pays rent` 는 개발자 글에서 자주 보이는 가벼운 변형이다.
- 예문: The extra hash in every done line felt fussy, but today it paid rent: it caught three stale letters.
- 유사어: earns its keep (가장 표준적인 관용구), pays for itself (비용 회수에 초점), pulls its weight (구성원·구성요소가 제 몫을 할 때)
- 반의어: dead weight

## "not one byte of it touches X"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 변경분이 특정 영역에 전혀 닿지 않는다고 강하게 안심시킬 때(변경 영향 분석·리뷰)
- 한국어: 그중 단 1바이트도 X 를 건드리지 않는다
- 설명: 원문은 `Critically: not one byte of it touches letter 14.` 이다. `not one + 단수명사` 는 `no` 보다 훨씬 세게 부정해서 "하나라도 있으면 내가 틀린 것"이라는 자신감이 실린다. 코드 변경 분석이라 단위로 `byte` 를 골랐다. 일반 글이라면 `not one word`, `not one line` 으로 바꿔 끼운다. 문두의 `Critically:` 는 "여기가 핵심인데"라는 표지다.
- 예문: The refactor is large, but not one byte of it touches the payment module.
- 유사어: none of it goes anywhere near X (구어), leaves X untouched (중립), X is entirely outside the scope of the change (격식)
- 반의어: it cuts right through X

## "one fat-fingered command away"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 파괴적인 동작이 오타 한 번이면 실행될 만큼 가까이 있다고 경고할 때(운영·도구 설계 논의)
- 한국어: 손가락 한 번 삐끗하면 바로 터지는 거리에 있는
- 설명: 원문은 `the destructive path was one fat-fingered command away` 다. `fat-finger` 는 굵은 손가락이 옆 키를 누른다는 데서 온 말로 동사(`I fat-fingered the IP`)로도 형용사로도 쓴다. `one X away` 는 "X 한 번이면 닿는 거리"라는 틀이라 `one click away`, `one typo away` 처럼 앞말만 갈아 끼우면 된다. 사고 가능성을 과장 없이 눈앞에 그려 준다.
- 예문: With `rm -rf` sitting in the shell history, a wiped home directory is always one fat-fingered command away.
- 유사어: one typo away (중립), an accident waiting to happen (구어, 더 일반적인 경고)
- 반의어: requires a deliberate flag, can't happen by accident

## "undersell"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 이름·제목·설명이 실제 기능이나 가치보다 작게 들린다고 지적할 때(리뷰·구어)
- 한국어: 실제보다 낮춰 말하다, 제값을 못 알리다
- 설명: 원문은 `The filename now undersells it — it defaults to refreshing, not resetting.` 이다. 물건을 제값보다 싸게 판다는 뜻이 "제대로 알리지 못한다"로 넓어졌다. 주어가 사람이 아니라 파일명·제목일 때 특히 자연스럽다. 대시 뒤에 무엇을 빠뜨렸는지 곧바로 붙이는 게 정석이다. 반대쪽 `oversell` 은 "과장하다"다.
- 예문: "Quick fix" undersells this PR — it also closes the race condition we've been chasing for a month.
- 유사어: doesn't do it justice (구어, 칭찬조), understate (격식), sell short (구어, 사람에게도 씀)
- 반의어: oversell, overstate

## "take its own word for it"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 시스템이나 기록이 외부 검증 없이 자기 보고만으로 사실로 취급된다고 꼬집을 때(설계 리뷰)
- 한국어: 제 말만 믿고 넘어가다
- 설명: 원문은 `The ledger was the one piece of state still taking its own word for it.` 이다. 기본형 `take someone's word for it` 은 "증거 없이 그 사람 말을 믿다"인데, `its own` 으로 바꿔 자기가 자기 말을 믿는 순환을 짚었다. 바로 앞 문장 `self-verifying rather than self-reported` 를 사람 비유로 한 번 더 말한 셈이다. 기본형은 `Don't take my word for it` 처럼 "직접 확인해 봐"라는 권유로도 많이 쓴다.
- 예문: Don't take my word for it — run the test suite and see for yourself.
- 유사어: take it on faith (구어), accept at face value (중립·격식), self-reported (문어·기술)
- 반의어: verify independently, trust but verify

## "stop X cold"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 어떤 조건 하나가 진행을 그 자리에서 완전히 멈춰 세운다고 경고할 때(일정·위험 논의)
- 한국어: X 를 그 자리에서 딱 멈춰 세우다
- 설명: 원문은 `that's the item that stops letter 18 cold` 다. 같은 대화 뒤쪽에서는 `can stop letter 18 dead` 라고도 했다. `cold`·`dead` 둘 다 "완전히, 단번에"를 뜻하는 강조어라서 느려진다는 말이 아니다. 아예 한 발짝도 못 나간다는 말이다.
- 예문: A missing firewall approval will stop the pilot cold, no matter how ready the code is.
- 유사어: stop X dead (거의 동의), stop X in its tracks (구어, 조금 더 극적), be a hard blocker for X (업무 문어)
- 반의어: slow X down, wave X through

## "the one with the longest lead time"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 준비 기간이 긴 항목부터 착수하라고 우선순위를 정할 때(프로젝트 관리·회의)
- 한국어: 확보까지 시간이 가장 오래 걸리는 항목
- 설명: 원문은 `it's the one with the longest lead time — worth resolving now rather than discovering at stage 3.` 이다. `lead time` 은 요청한 시점부터 실제로 손에 들어오기까지 걸리는 시간이다. 승인·계정·장비처럼 내가 애써도 당길 수 없는 대기에 주로 쓴다. 뒤따르는 `worth resolving now rather than discovering at stage 3` 는 `worth + 동명사` 로 "지금 풀어 둘 만하다"를 짧게 만든다.
- 예문: Start the access request today; it's the one with the longest lead time.
- 유사어: turnaround time (요청 처리 시간, 중립), takes the longest to come through (구어)
- 반의어: can be done on the spot

## "the critical path"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 전체 일정을 실제로 좌우하는 작업 사슬이 어디인지 짚을 때(일정 회의·계획서)
- 한국어: 크리티컬 패스(하루 밀리면 전체 완료가 하루 밀리는 작업 경로)
- 설명: 원문은 `The letter sequence isn't the critical path to letter 18. Your site gates are.` 이다. 일정 관리 용어로 `on the critical path` 형태가 가장 흔하다. `isn't the critical path` 는 눈에 잘 보이는 작업이 실제 병목은 아니라고 반박할 때 쓴다. 둘째 문장 `Your site gates are.` 는 `are (the critical path)` 에서 보어를 생략하고 be 동사만 남긴 구조다.
- 예문: The UI polish isn't on the critical path; the security review is.
- 유사어: the bottleneck (한 지점에 초점, 구어), the long pole (구어, 텐트 기둥 비유), what gates the launch (중립)
- 반의어: has slack, a nice-to-have

## "sitting in someone's queue"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 일이 멈춘 원인이 작업량이 아니라 남의 승인·처리 대기라고 짚을 때(일정 논의)
- 한국어: 누군가의 처리 대기열에 묶여 있는
- 설명: 원문은 `the actual constraint is a approval or a credential sitting in someone's queue` 다. `sitting` 은 진척 없이 놓여 있다는 뜻이라 `waiting` 보다 방치된 느낌이 짙다. 명사 뒤에 현재분사구를 붙여(`a credential sitting in …`) 관계절 `that is sitting` 을 줄였다. 원문의 `a approval` 은 오타로, 모음 소리 앞이라 `an approval` 이 맞다.
- 예문: The fix is done; it's just sitting in someone's review queue.
- 유사어: stuck waiting on someone (구어), pending approval (격식·문서), in limbo (구어, 언제 풀릴지 모름)
- 반의어: in progress, moving

## "the win here is X, not Y"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 개선 효과가 실제로 어디서 나오는지 상대의 기대를 바로잡을 때(설계 논의·구어)
- 한국어: 여기서 얻는 건 Y 가 아니라 X 다
- 설명: 원문은 `the loop is designed for repeated one-shots, so the win here is turnover, not concurrency.` 다. 명사 `win` 은 "이득, 성과"라는 뜻으로 개발자 구어에 아주 흔하다(`a quick win`, `a big win`). `turnover` 는 세션을 짧게 끝내고 새로 여는 회전율이다. 상대는 병렬화를 기대했는데 진짜 이득은 회전율에 있다고 초점을 옮겨 놓았다.
- 예문: Caching helps a little, but the win here is fewer round trips, not faster queries.
- 유사어: the payoff is X (중립), where this really helps is X (구어), the main benefit is X (격식)
- 반의어: the cost here is X

## "That's your cue."
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 어떤 신호가 보이면 이제 상대가 나설 차례라고 알려 줄 때(작업 안내·구어)
- 한국어: 그게 나설 신호다
- 설명: 원문은 `It stops itself at a waiting line, which is your cue.` 와 `that's your cue to supply whatever it's waiting for.` 다. `cue` 는 무대에서 배우에게 등장 순간을 알리는 신호다. `your cue to + 동사원형` 으로 무엇을 할지까지 붙인다. 노트의 `a cue to X, not a Y in its own right` 가 알림의 무게를 정하는 명사구라면, 이쪽은 상대에게 차례를 넘기는 구어 한 문장이다.
- 예문: When the build turns red, that's your cue to pull the latest schema.
- 유사어: that's your signal (중립), that's when you step in (구어), at that point, please … (격식 안내문)

## "scaffolding you then throw away"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 결과물을 만들려고 잠깐 쓰고 버리는 절차·도구를 최종 산출물과 구분할 때(설계 문서·회고)
- 한국어: 다 짓고 나면 걷어 내는 비계
- 설명: 원문은 `The subtle answer to "what do I get" is: a repeatable operation, and scaffolding you then throw away.` 이다. `scaffolding` 은 건물 공사 때 세우는 비계인데, 완공되면 철거된다는 점이 비유의 핵심이다. `you then throw away` 는 관계대명사가 생략된 접촉절이고 `then` 이 "다 쓰고 나서"라는 순서를 더한다. 20통의 편지(letter)는 산출물이 아니라 비계라는 판단을 명사구 하나에 담았다.
- 예문: The migration scripts are scaffolding you then throw away; the schema is what we keep.
- 유사어: a one-time bootstrap (같은 답변에 나온 기술 어휘), throwaway tooling (구어), a means to an end (일반·중립)
- 반의어: the lasting deliverable

## "division of labour"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 두 구성요소나 두 사람이 각각 무엇을 맡는지 정리할 때(설계 문서·회의)
- 한국어: 역할 분담, 분업
- 설명: 원문은 `The division of labour is the point: index.md says what may be batched, pi decides how to start it.` 이다. 경제학 용어 "분업"이 일상과 기술 글로 넓게 퍼졌다. `labour` 는 영국식 철자이고 미국식은 `labor` 다. 콜론 뒤에 `A says what …, B decides how …` 처럼 두 주체의 몫을 나란히 적는 짝 구조가 자주 따라온다.
- 예문: The division of labour is simple: the CLI enforces the rules, and the skills only relay commands.
- 유사어: split of responsibilities (중립·기술), who owns what (구어)
- 반의어: overlapping responsibilities

## "a ratchet rather than a treadmill"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 개선이 되돌아가지 않고 쌓이게 만드는 절차를 설명할 때(프로세스 설계·회고)
- 한국어: 제자리걸음이 아니라 한 칸씩 올라가면 물러서지 않는 구조
- 설명: 원문은 `Two rules make it a ratchet rather than a treadmill` 이다. `ratchet` 은 한 방향으로만 돌고 반대로는 걸려 잠기는 톱니, `treadmill` 은 아무리 걸어도 제자리인 러닝머신이다. `make + 목적어 + 명사 보어` 로 규칙이 과정의 성격 자체를 바꾼다고 말한다. 곧이어 규칙 두 개를 제시해 은유를 구체로 받쳤다. 노트에 있는 `a one-way ratchet` 이 단조성만 말한다면 이쪽은 대비 항까지 갖췄다.
- 예문: Turning every production bug into a regression test makes QA a ratchet rather than a treadmill.
- 유사어: locks in progress (중립), compounding gains (격식·비즈니스)
- 반의어: running in place, going around in circles

## "First the blunt part:"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대가 듣기 싫을 수 있는 말을 먼저 꺼내겠다고 예고할 때(조언·구어)
- 한국어: 듣기 불편한 얘기부터 하자면
- 설명: 원문은 `First the blunt part: parallel pi tabs on the model folder will break the run` 이다. 동사 없이 `First + 명사구 + 콜론` 으로 말할 순서를 잡는다. 여기서 `blunt` 는 "돌려 말하지 않는"이다. 미리 예고해 두면 뒤에 오는 반대 의견이 공격이 아니라 솔직함으로 받아들여진다. 노트의 `a blunt heuristic` 에서는 같은 단어가 "무딘, 거친"이었다.
- 예문: First the blunt part: this won't ship by Friday.
- 유사어: To be frank, (격식), I'll be honest with you: (구어), Bad news first: (구어)
- 반의어: To put it gently,

## "the more natural home for X"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 기록이나 기능을 어디에 두는 게 더 맞는지 선택지를 제안할 때(도구·문서 구조 논의)
- 한국어: X 를 두기에 더 어울리는 자리
- 설명: 원문은 `issues may be the more natural home for "which extractor next."` 다. `home` 은 정보나 기능이 소속될 자리라는 비유로 기술 글에서 흔하다(`find a home for this helper`). 저장소 Markdown 파일과 GitHub issue 두 후보를 견주는 맥락이라 비교급에 정관사가 붙었다. `may be` 로 결정권을 상대에게 남겨 제안의 세기를 낮췄다.
- 예문: The team wiki may be the more natural home for these setup notes.
- 유사어: a better fit for X (구어), belongs in … (단정적), the appropriate place for X (격식)
- 반의어: feels out of place in …

## "I'd keep it to a page."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 새 문서나 작업을 제안하면서 분량 상한을 먼저 약속해 부담을 덜 때(제안·구어)
- 한국어: 한 쪽 안으로 줄여 쓸게요
- 설명: 원문은 `Want me to write it? I'd keep it to a page.` 다. `keep it to + 분량` 은 "그 선을 넘기지 않다"로 `keep it to five minutes`, `keep it to two slides` 처럼 쓴다. `I'd` 에는 "당신이 좋다고 하면"이라는 가정이 깔린다. 제안 바로 뒤에 분량을 못 박으니 상대가 부담 없이 yes 할 수 있다.
- 예문: Happy to write up the retro — I'd keep it to a page.
- 유사어: keep it short (구어), limit it to one page (격식), no more than a page (중립)
- 반의어: go into full detail
