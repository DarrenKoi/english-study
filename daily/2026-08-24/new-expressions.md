# 2026-08-24 — 새 표현

## "stale-while-revalidate"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 캐시 갱신 전략을 한 단어로 지칭할 때(설계 문서·리뷰, 격식)
- 한국어: 낡은 값을 일단 내주고 뒤에서 갱신하는 방식
- 설명: HTTP 캐시 헤더에서 온 이름이 그대로 설계 어휘가 됐다. 잠금 경쟁에서 진 요청이 기다리지 않고 직전 보드를 돌려주는 동작을 이 한 단어로 부른다. 하이픈으로 묶어 형용사·명사 양쪽으로 쓴다.
- 예문: The loser serves the previous board (stale-while-revalidate), so no request ever waits on another request.
- 유사어: serve from cache and refresh in the background (풀어쓴 설명체, 비전문가 상대), optimistic caching (뉘앙스가 넓고 덜 정확)
- 반의어: block until fresh (신선해질 때까지 응답을 붙들어 둠)

## "The lock is also the backoff."
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 장치 하나가 두 역할을 겸한다고 밝힐 때(설계 근거, 격식)
- 한국어: 그 잠금이 곧 재시도 지연 장치이기도 하다
- 설명: `A is also B` 는 "따로 만들 필요가 없다"는 절약 논증의 압축형이다. 뒤에 `One mechanism, no second key.` 처럼 무동사 조각을 붙여 결론을 못 박는 게 이 문서의 리듬.
- 예문: Releasing the lock only on success suppresses retries for twenty seconds — the lock is also the backoff.
- 유사어: it does double duty (회화체·가벼움), one mechanism covers both (평이하고 중립적)
- 반의어: that needs a second mechanism

## "a fresh heartbeat over missing data"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 모니터링이 "살아 있음"만 보고하고 내용은 비어 있는 상태를 지적할 때(설계·장애 리뷰, 격식)
- 한국어: 데이터는 없는데 최신 시각만 찍혀 있는 상태
- 설명: `over` 가 "덮어씌운다"는 그림을 만든다. 심장박동만 뛰고 속은 빈 화면 — 모니터링 시스템에서 가장 위험한 실패라는 걸 은유 하나로 전달한다. `the one failure mode this feature exists to prevent` 와 붙여 쓰면 우선순위까지 같이 선언된다.
- 예문: A fresh heartbeat over missing data is the one failure mode this feature exists to prevent.
- 유사어: a green light on an empty pipeline (같은 은유의 다른 판본), false liveness (짧고 학술적)
- 반의어: an honest stale marker

## "self-corrects on the next poll"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 일시적 이상이 개입 없이 풀린다고 안심시킬 때(설계 근거·장애 보고, 격식)
- 한국어: 다음 폴링에서 저절로 바로잡힌다
- 설명: 결함을 인정하면서 동시에 대응이 불필요함을 밝히는 두 겹의 문장. `That is honest` 처럼 상태를 먼저 정당화한 뒤 이 구절로 닫으면 "버그가 아니라 설계"라는 주장이 완성된다.
- 예문: A cold cache whose lock was lost returns an empty board marked stale, and it self-corrects on the next poll.
- 유사어: it heals itself (구어), it converges without intervention (더 격식)
- 반의어: it needs a manual reset

## "Dropping silently was rejected."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 검토했다가 버린 대안을 문서에 남길 때(설계 결정문, 격식)
- 한국어: 조용히 버리는 방식은 채택하지 않았다
- 설명: 동명사 주어 + 수동태로 행위자를 지우면 개인 취향이 아니라 팀의 판정으로 읽힌다. 바로 뒤에 `because` 대신 콜론이나 새 문장으로 근거를 붙이는 게 이 문서의 습관.
- 예문: Dropping silently was rejected: a roster gap and a genuinely quiet fab would render identically.
- 유사어: we considered X and ruled it out (능동·회화체), X was ruled out (같은 격식, 더 짧음)
- 반의어: X was adopted without objection

## "not a stylistic preference"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 지시가 취향 문제로 오해받아 무시될 위험이 있을 때 미리 못 박는 말(설계·리뷰, 격식)
- 한국어: 취향 문제가 아니다
- 설명: `X is a real constraint, not a stylistic preference` 처럼 A-not-B 구조로 쓴다. 읽는 사람이 "그건 스타일 문제니 나중에" 하고 넘길 여지를 문장 안에서 미리 닫아 버린다.
- 예문: The import ordering above is a real constraint on the implementation sequence, not a stylistic preference.
- 유사어: this isn't bikeshedding (구어·자조적), this is load-bearing (같은 뜻을 은유로)
- 반의어: that one's down to taste

## "stale but still green"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 테스트가 통과하지만 무의미해진 상태를 지적할 때(코드 리뷰, 반격식)
- 한국어: 낡았는데도 여전히 통과하는
- 설명: CI 의 초록불을 `green` 으로 받아, 통과가 곧 유효함이 아니라는 걸 두 단어의 대조로 보여준다. 뒤에 `it merely asserts a rule about a file nobody will ever create` 처럼 그 테스트가 실제로 무엇을 지키는지 밝히면 지적이 완성된다.
- 예문: That parametrized case is stale but still green — it merely asserts a rule about a file nobody will ever create.
- 유사어: a vacuous test (학술적·짧음), it passes for the wrong reason (풀어쓴 구어)
- 반의어: it fails the moment the contract moves

## "cannot surface the difference"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 특정 환경에서만 결함이 안 드러나는 이유를 설명할 때(장애 분석·설계, 격식)
- 한국어: 그 차이를 드러내지 못한다
- 설명: `surface` 를 타동사로 쓰면 "표면으로 끌어올린다"는 그림이 살아난다. 사람이 아니라 개발 환경을 주어로 세워, 놓친 사람을 탓하지 않고 조건을 탓하는 문장이 된다.
- 예문: R3 is the single value where the two keys coincide, which is exactly why development focused on R3 cannot surface the difference.
- 유사어: the bug is invisible in that setup (평이한 구어), the test environment masks it (`mask` 는 능동적 은폐 뉘앙스)
- 반의어: it reproduces on the first run

## "Here's the actual shape of the problem."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 조사를 마치고 상대가 물은 것과 다른 진짜 구도를 꺼낼 때(구두 보고·슬랙, 반격식)
- 한국어: 문제의 실제 모양은 이렇습니다
- 설명: `the actual shape` 이 "당신이 말한 그 문제가 아니라"를 부드럽게 깔아 둔다. 앞에 `Looked at every writer.` 처럼 주어를 생략한 조사 보고를 두면 근거→구도 순서가 자연스럽다.
- 예문: Looked at every writer — here's the actual shape of the problem.
- 유사어: what's really going on is (더 구어), the underlying structure is (더 격식·건조)
- 반의어: to restate your question as asked

## "That last one is the nastiest."
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 목록·표를 보여준 직후 그중 하나를 골라 무게를 실을 때(구두 설명, 구어)
- 한국어: 그중 마지막이 제일 고약합니다
- 설명: `nasty` 의 최상급은 기술 대화에서 "심각하다"가 아니라 "다루기 까다롭고 짜증난다"에 가깝다. 표 바로 아래에 놓아 독자의 시선을 한 행으로 다시 데려오는 장치.
- 예문: That last one is the nastiest: the runner stamps its own run_id, so two folders for the same alarm can't be joined by name.
- 유사어: that's the one that bites (더 구어), that is the most consequential (격식·중립)
- 반의어: that one's harmless

## "scatter into"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 한 사건의 산출물이 여러 곳으로 흩어져 쌓이는 구조를 지적할 때(설계 검토, 반격식)
- 한국어: ~로 흩어져 들어가다
- 설명: 자동사 `scatter` 에 `into` 를 붙여 "흩어져서 어디로 들어가는지"까지 한 번에 말한다. 숫자를 함께 세면(`four roots with three naming schemes`) 인상이 아니라 측정이 된다.
- 예문: One alarm cycle currently scatters into four roots with three different naming schemes.
- 유사어: spread across (중립적), end up in half a dozen places (구어·불평조)
- 반의어: land in one place

## "get honest, narrow jobs"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 역할이 뒤섞인 모듈을 정리한 뒤 각자의 책임을 재선언할 때(설계 제안, 반격식)
- 한국어: 각자 정직하고 좁은 역할을 갖게 된다
- 설명: `honest` 가 "이름과 실제가 일치한다", `narrow` 가 "그 하나만 한다"를 맡아 두 형용사가 서로 다른 일을 한다. 새 구조를 제안한 다음 문단을 여는 말로 쓰면 "그래서 나머지는 어떻게 되나"에 바로 답한다.
- 예문: Then the two old trees get honest, narrow jobs: one is MES input, the other is our disposable output.
- 유사어: each gets a single responsibility (SOLID 어휘, 더 격식), each stops pretending to be two things (구어·비꼼)
- 반의어: both keep doing a bit of everything

## "an honest count"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 제안의 비용을 축소 없이 세어 보이겠다고 예고할 때(설계 제안·견적, 반격식)
- 한국어: 부풀리지도 줄이지도 않은 계산
- 설명: 제목이나 괄호에 넣어 뒤따를 목록의 성격을 미리 밝힌다. 제안자가 자기 제안의 비용을 스스로 세는 자리라 `honest` 한 단어가 신뢰를 산다.
- 예문: What it costs — an honest count: seven easy call sites, two medium, and one runner change.
- 유사어: the real cost, not the optimistic one (풀어쓴 구어), a full accounting (더 격식)
- 반의어: a back-of-the-envelope guess

## "mint its own timestamp"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 두 컴포넌트가 같은 사건에 서로 다른 식별자를 붙여 조인이 깨지는 상황을 설명할 때(디버깅, 반격식)
- 한국어: 자기 나름의 타임스탬프를 새로 찍어 낸다
- 설명: 화폐를 주조한다는 `mint` 가 "받아쓰지 않고 스스로 만들어 낸다"는 부정적 뉘앙스를 싣는다. 그래서 뒤에 오는 "이름으로 조인할 수 없다"가 자연스러운 귀결로 읽힌다.
- 예문: The runner mints its own timestamp, so the journal folder and the recording folder for the same alarm differ by a second or two.
- 유사어: generate its own id (중립적·건조), roll its own (구어, "굳이 직접 만든다"는 핀잔)
- 반의어: take the id from the caller

## "uglier but never silently fails"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator 03c7c8ef
- 맥락: 보기 나쁜 쪽을 일부러 고른 이유를 밝힐 때(설계 근거, 반격식)
- 한국어: 볼품은 없지만 조용히 실패하지는 않는다
- 설명: 심미적 손해를 먼저 인정하고 `but` 뒤에 결정적 이득을 놓는 순서가 설득의 핵심. `never` 를 써서 "가끔은 괜찮다"는 반박의 여지를 닫는다.
- 예문: A one-line text file is uglier but never silently fails, which a symlink on an unelevated Windows box cannot promise.
- 유사어: less elegant but more honest (같은 구조의 격식형), ugly and correct beats pretty and wrong (격언조)
- 반의어: cleaner but fails quietly

## "blow through (a budget)"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 한도를 순식간에 소진하는 동작을 묘사할 때(장애 분석·구두 설명, 구어)
- 한국어: 한도를 단숨에 써 버리다
- 설명: `exceed` 가 넘었다는 사실만 말한다면 `blow through` 는 속도와 무신경까지 담는다. 그래서 뒤에 `because` 로 왜 그렇게 빨랐는지 붙이는 흐름이 잘 맞는다.
- 예문: The recipe-status page blows through it because each tab fires about five analytics calls per filter change.
- 유사어: burn through (같은 구어, 소진 쪽에 무게), exhaust the budget (격식·중립)
- 반의어: stay well inside the budget

## "has to argue for itself"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 예외 목록에 항목을 추가하려는 다음 사람에게 입증 책임을 넘길 때(코드 주석·리뷰, 격식)
- 한국어: 스스로 근거를 대야 한다
- 설명: 코드나 규칙을 주어로 세워 사람을 지목하지 않고 책임만 옮긴다. 앞에 판정 기준을 한 줄로 적어 두면(`one page view legitimately exceeds the budget`) 그 기준이 다음 심사의 잣대가 된다.
- 예문: The comment states the admission rule, so the next addition has to argue for itself.
- 유사어: the burden of proof sits with the next change (더 격식·법률 어휘), you'll have to make the case (구어·직접적)
- 반의어: it can be added on precedent alone

## "a data change, not a design change"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 요청의 규모를 축소 판정해 안심시킬 때(리뷰·견적, 반격식)
- 한국어: 설계를 바꾸는 게 아니라 값만 바꾸는 일이다
- 설명: 기존 장치가 이미 있음을 확인한 뒤 이 A-not-B 로 닫으면 "며칠 걸리나요"에 대한 답이 문장 하나로 끝난다. `change` 를 두 번 반복해 대조가 귀에 걸린다.
- 예문: The exemption mechanism already exists, so this is a data change, not a design change.
- 유사어: it's a config change (더 좁고 구체적), no architecture moves here (구어)
- 반의어: this reopens the design

## "One tradeoff to flag."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 작업을 끝냈다고 보고한 뒤 남은 위험 하나를 덧붙일 때(보고 말미, 반격식)
- 한국어: 하나 짚어 둘 맞바꿈이 있습니다
- 설명: `flag` 는 "지금 고치자"가 아니라 "기록에 남긴다"는 뜻이라, 완료 보고의 신뢰를 깎지 않으면서 책임은 남긴다. 숫자 `One` 이 앞에 붙어 목록이 길지 않다는 것도 미리 알려 준다.
- 예문: One tradeoff to flag: a runaway client loop now hits OpenSearch unbounded on these routes.
- 유사어: worth noting (더 가볍고 약함), for the record (기록 목적을 앞세움)
- 반의어: nothing outstanding on this one

## "just the request people noticed"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 신고된 증상이 원인이 아니라 표본일 뿐임을 밝힐 때(장애 분석, 반격식)
- 한국어: 사람들 눈에 띈 요청이었을 뿐이다
- 설명: 사용자가 지목한 대상을 부정하지 않으면서 지위를 낮추는 말. 앞에 공유 자원이라는 진짜 구조를 설명하고 이 문장으로 닫으면, 신고가 틀렸다고 말하지 않고도 초점이 옮겨간다.
- 예문: Because the budget is app-wide, the user pill and the page-view beacon 429'd too — fail-issue/devices is just the request people noticed.
- 유사어: that's the symptom, not the cause (평이·교과서적), it happened to be the loudest one (구어)
- 반의어: that request is the actual culprit

## "I left it alone."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt df011192
- 맥락: 범위 밖의 이상을 발견했지만 손대지 않았다고 보고할 때(작업 말미, 구어)
- 한국어: 손대지 않고 두었습니다
- 설명: 짧은 과거형 한 문장이 "봤다 + 판단했다 + 안 건드렸다"를 다 담는다. 앞에 `Unrelated:` 를 붙여 본 작업과 분리해 두면 보고가 흐트러지지 않는다.
- 예문: Unrelated: git worktree list shows a checkout still open from another session — I left it alone.
- 유사어: I didn't touch it (같은 뜻, 더 무심함), that's outside this change (범위를 근거로 든 격식형)
- 반의어: I cleaned it up while I was in there

## "the objections that landed"
- 레지스터: professional
- 출처: transcript:[skill] .claude/skills/oc-discuss
- 맥락: 반박 중 실제로 유효했던 것만 골라 가리킬 때(리뷰 회신·토론 정리, 반격식)
- 한국어: 실제로 먹힌 지적들
- 설명: 권투의 `a punch that lands` 에서 온 비유라 "말해졌다"와 "맞았다"를 구분한다. `Do not skip the ones that landed` 처럼 명령문에 넣으면 회신에서 약한 지적만 골라 답하는 회피를 정면으로 막는다.
- 예문: Answer every objection — do not skip the ones that landed.
- 유사어: the criticisms that stuck (거의 같은 구어), the valid objections (건조·중립)
- 반의어: the ones you could wave away

## "the ceiling, not the target"
- 레지스터: professional
- 출처: transcript:[skill] .claude/skills/oc-discuss
- 맥락: 상한으로 정한 수치가 달성 목표로 오해될 때 바로잡는 말(절차 문서·회의, 격식)
- 한국어: 상한이지 목표치가 아니다
- 설명: 예산·라운드 수·재시도 횟수처럼 "쓸 수 있는 최대"가 어느새 "채워야 할 양"으로 변질되는 흔한 왜곡을 한 구절로 막는다. 뒤에 반례를 한 문장 붙이면 규칙이 실제 판단으로 내려온다.
- 예문: Three rounds is the ceiling, not the target — a clean concession in round one is a finished debate.
- 유사어: an upper bound, not a quota (더 건조·수학적), you don't have to use all of it (구어)
- 반의어: that's the number to hit

## "Weak opposition is worse than no opposition."
- 레지스터: professional
- 출처: transcript:[skill] .claude/skills/oc-discuss
- 맥락: 검토자·반대자의 수준을 낮추면 안 되는 이유를 댈 때(절차 설계·리뷰 정책, 격식)
- 한국어: 약한 반대는 반대가 없느니만 못하다
- 설명: `worse than none` 구조는 "없는 것보다 못하다"는 강한 판정이라 근거가 반드시 따라와야 한다. 여기서는 `it produces an AGREED that nobody earned` 가 그 근거 — 형식적 합의가 검증을 통과한 것처럼 위장한다는 지적.
- 예문: Weak opposition is worse than no opposition: it produces an agreement that nobody earned.
- 유사어: a rubber-stamp review is worse than skipping review (더 구체적), token dissent (한 단어로 압축)
- 반의어: opposition worth answering
