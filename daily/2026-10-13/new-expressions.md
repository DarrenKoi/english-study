# 2026-10-13 — 새 표현

> 오늘 배치는 repo 문서 9건과 transcript 5건이다. auto_recipe_creator 의 DL 학습 문서 다섯과 skewnono 의 TTTM 리뷰·분석 서비스 방향 문서는 본문이 한국어여서 표현 재료로 쓰지 않았다. 영어 재료는 셋이다. skewnono 세션에서 "내 장비·내 레시피" 개인화 페이지를 놓고 어시스턴트가 낸 제안과 grilling 1라운드, 그 세션의 하위 에이전트 조사 보고에서 열여덟, recipe-tat 티켓 01 에서 다섯, skewvoir 현황 노트에서 여섯을 골랐다. 티켓과 skewvoir 노트는 전에 훑은 문서라 그때 안 고른 것만 집었다. grilling·Herdr 스킬 문서, `/model`·`/clear` 명령, task-notification, 이 저장소의 지난 배치 프롬프트는 건너뛰었다. 노트에 이미 있어서 뺀 것: `The catch is that …`, `pressure-test`, `without spec sanction`, `smuggled in by implementation fiat`, `is dropped on the floor`, `thinner than their single-scope twins`, `silent limits`, `spot-check`, `division of labour`.

## "the scope needs choosing carefully"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 하자는 데는 동의하지만 범위를 잘못 잡으면 탈이 난다고 미리 짚을 때(대화·제안 서두, 중립).
- 한국어: 범위를 신중하게 골라야 한다
- 설명: `need + -ing` 는 `need to be + p.p.` 와 같은 뜻의 짧은 형태다. 주어가 동작을 받는 쪽인데도 능동 꼴 `choosing` 을 쓴다. 영국식에 가깝지만 미국 구어에서도 흔하다. 원문은 예전에 거절한 안과 겹친다는 사실을 꺼낸 직후 이 말로 문장을 닫는다.
- 예문: One version of this idea is something you rejected last week, so the scope needs choosing carefully.
- 유사어: the scope needs to be chosen carefully (같은 뜻, 조금 더 문어), we should be careful about scope (평이), scoping this is the delicate part (구어)
- 반의어: the scope is obvious

## "doesn't reopen the rejected design"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 새 제안이 이미 기각된 결정을 다시 건드리지 않는다고 안심시킬 때(설계 논의·문어와 구어 모두).
- 한국어: 기각된 설계를 다시 꺼내지 않는다
- 설명: `reopen` 은 닫힌 안건·논쟁·티켓을 다시 여는 것이다. 사람이 아니라 제안(`it`)을 주어로 세워 "이 안을 택해도 그 논쟁으로 되돌아가지 않는다"고 말한다. 결정권자의 과거 판단을 존중한다는 신호가 된다.
- 예문: Option A gets you most of the benefit, and it doesn't reopen the rejected design.
- 유사어: doesn't relitigate the earlier decision (법정 비유, 더 격식), leaves the earlier decision alone (구어), stays clear of what was ruled out (중립)
- 반의어: brings the rejected design back in through the side door

## "a hard cap on (how many features it reads)"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 넘으면 안 되는 상한을 설계 조건으로 못 박을 때(설계 논의·명세, 중립).
- 한국어: (읽는 기능 수의) 엄격한 상한
- 설명: `cap` 은 상한이고 `hard` 가 붙으면 예외 없이 지킨다는 뜻이 된다. 전치사는 `on` 이고 뒤에 명사나 `how many …` 절이 온다. `soft cap` 은 넘어도 경고만 하는 상한이다.
- 예문: I'd go with live cards, with a hard cap on how many features the page reads.
- 유사어: a strict limit on (평이), a ceiling on (문어), at most N (명세에 숫자로 쓸 때)
- 반의어: a soft cap, no limit

## "knowingly overrides (the coupling objection)"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 예전에 나온 반대 이유를 알면서도 이번엔 뒤집는다고 숨기지 않고 밝힐 때(설계 근거·문어).
- 한국어: (결합도 반론을) 알고서 뒤집는다
- 설명: `knowingly` 가 요점이다. 몰라서 어긴 것이 아니라 비용을 알고 고른 결정이라고 밝힌다. `override` 는 규칙·결정·반론을 위에서 덮는 동사다. 원문은 바로 뒤에 `so the cap is what keeps it from becoming the rejected hub` 로 뒤집는 대가를 어떻게 막는지 붙인다.
- 예문: This knowingly overrides the coupling objection, so the cap matters.
- 유사어: deliberately sets aside (문어), goes against … with eyes open (구어), accepts the coupling as a trade-off (중립)
- 반의어: inadvertently violates

## "the unambiguous "something is wrong now" signals"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 여러 후보 지표 중 해석의 여지가 없는 것만 골랐다고 설명할 때(제안·설계 논의).
- 한국어: 해석의 여지 없이 "지금 뭔가 잘못됐다"를 뜻하는 신호들
- 설명: 따옴표 친 문장을 통째로 형용사처럼 명사 앞에 놓았다. 영어 기술 글에서 흔한 방법으로, 긴 관계절(`signals that mean something is wrong now`)을 줄인다. `unambiguous` 는 `clear` 보다 "달리 읽을 수 없다"는 뜻이 강하다.
- 예문: Tool offline, fail issues and storage are the unambiguous "something is wrong now" signals.
- 유사어: the clear-cut signals (구어), signals that leave no room for interpretation (문어)
- 반의어: noisy signals, signals that need context to read

## "would mislead on a page you open once in the morning"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 데이터 자체는 맞지만 쓰이는 상황 때문에 오해를 부른다고 제외 이유를 댈 때(설계 논의).
- 한국어: 아침에 한 번 여는 페이지에서는 오해를 부를 것이다
- 설명: `mislead` 를 목적어 없이 자동사처럼 썼다. "사용자를"이 빠져도 뜻이 선다. `would` 는 아직 만들지 않은 화면을 가정하기 때문이다. `a page (that) you open once in the morning` 은 관계사 없는 접촉절로, 쓰임새 하나로 페이지를 규정한다.
- 예문: Live alarms expire after 30 minutes, so they would mislead on a page you open once in the morning.
- 유사어: would give the wrong impression (평이), would paint a false picture (문어), would look fine when it isn't (구어)
- 반의어: would be accurate at a glance

## "The lookup is back."
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 맡겨 둔 조사·조회 결과가 돌아왔다고 보고를 여는 첫마디(대화·채팅, 구어).
- 한국어: 조사 결과가 나왔다
- 설명: `be back` 은 사람뿐 아니라 결과·응답에도 쓴다(`The results are back`, `The tests came back clean`). `lookup` 은 명사일 때 붙여 쓰고 동사일 때는 `look up` 으로 뗀다.
- 예문: The lookup is back, and it doesn't change the Round 1 questions.
- 유사어: The results are in (가장 흔함), I've got the findings (구어), The search has returned (문어)
- 반의어: The lookup is still running

## "whole-fleet-then-filter"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: API 가 대상을 지정받지 못해 전체를 받아 클라이언트에서 거르는 방식을 한 단어로 부를 때(기술 보고).
- 한국어: 전체를 받아 온 뒤 거르는 방식
- 설명: `A-then-B` 는 절차의 순서를 이름으로 만드는 하이픈 조어다(`fetch-then-render`, `validate-then-write`). 원문은 `Everything else is whole-fleet-then-filter` 로 보어 자리에 놓았다. 명사 앞에도 둔다(`a whole-fleet-then-filter endpoint`).
- 예문: Only two endpoints accept an arbitrary tool list; everything else is whole-fleet-then-filter.
- 유사어: fetch everything and filter client-side (풀어 쓴 말), over-fetching (비용을 강조), no server-side filter (없는 것을 짚음)
- 반의어: server-side filtering, scoped queries

## "is misleadingly named"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 이름과 실제 하는 일이 달라 읽는 사람이 속는다고 코드 조사 보고에 적을 때.
- 한국어: 이름이 오해를 부른다
- 설명: `misleadingly` 는 부사로 과거분사 `named` 를 꾸민다. 뒤에 콜론을 찍고 실제 정체를 밝히는 것이 정석이다. 원문도 `is misleadingly named: it is the device-statistics point-count API` 로 썼다. `misnamed` 는 이름이 틀렸다는 뜻이고 `misleadingly named` 는 틀리진 않아도 다른 것을 떠올리게 한다는 뜻이다.
- 예문: The composable is misleadingly named: it wraps the point-count API, not recipe statistics.
- 유사어: is a misnomer (문어, 명사), the name is deceptive (평이), doesn't do what it says on the tin (영국 구어)
- 반의어: is aptly named

## "I did not trace which route exposes it"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 조사하다 여기서 멈췄다고 범위의 끝을 정직하게 표시할 때(조사 보고·문어).
- 한국어: 어느 경로가 그것을 내보내는지는 추적하지 않았다
- 설명: `trace` 는 코드 경로를 끝까지 따라가는 것이고 `expose` 는 내부 값을 API·화면으로 내놓는 것이다. "모른다" 대신 "안 따라가 봤다"라고 쓰면 없다는 주장이 아니라 확인을 안 했다는 뜻이 분명해진다. 같은 보고에 `I did not check the other features`, `I did not open the office adapters` 가 같은 구실로 나온다.
- 예문: The doc mentions an `oper_id` field for lot history; I did not trace which route exposes it.
- 유사어: I didn't follow that one through (구어), not traced further (메모체), out of scope for this pass (범위를 이유로)
- 반의어: I traced it end to end

## "unverified where noted"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 보고서 머리에서 "표시한 곳은 확인 못 한 것"이라고 한꺼번에 단서를 달 때(조사 보고·문어).
- 한국어: 표시한 부분은 검증되지 않음
- 설명: `where noted` 는 `where (it is) noted` 의 줄임이다. `except where noted`, `unless otherwise noted` 와 같은 계열이다. 단서를 문장마다 달지 않고 머리말에 한 번 달아 본문을 가볍게 한다.
- 예문: I did not open the office adapters, so office-side behaviour is unverified where noted.
- 유사어: not confirmed in the places marked (평이), treat flagged items as unconfirmed (지시형), except where noted (반대 방향의 단서)
- 반의어: verified throughout

## "is where the real cost of this page is"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 비용·위험이 몰린 한 곳을 손가락으로 짚을 때(설계 논의, 중립).
- 한국어: 이 페이지의 진짜 비용이 있는 곳이다
- 설명: `X is where Y is` 는 위치 비유로 초점을 맞추는 틀이다. `real` 은 겉보기 비용과 실제 비용을 가른다. 원문은 `My recommendation stays (a), but …` 뒤에 붙여 추천은 유지하되 대가를 숨기지 않았다.
- 예문: The tools section is cheap; the recipe section is where the real cost of this page is.
- 유사어: is the expensive part (평이), is where the budget goes (구어), accounts for most of the cost (문어)
- 반의어: is essentially free

## "one click instead of zero"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 작은 안이 큰 안보다 얼마나 덜 편한지 숫자 하나로 정직하게 말할 때(제안·구어).
- 한국어: (클릭이) 0번이 아니라 1번
- 설명: `A instead of B` 에 숫자를 넣어 차이를 가장 작은 단위로 보여 준다. 원문은 `A already delivers "sees it right away" as one click instead of zero` 로, 요구를 거의 채우되 한 번은 눌러야 한다는 차이를 숨기지 않았다.
- 예문: The cheaper option still gets you there, as one click instead of zero.
- 유사어: one extra click (평이), a single click away (광고 문구에 가까움), at the cost of one click (문어)

## "what keeps it from becoming (the rejected hub)"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 어떤 장치가 설계의 변질을 막는다고 그 장치의 존재 이유를 밝힐 때(설계 근거).
- 한국어: 그것이 (기각된 허브로) 변하지 않게 막아 주는 것
- 설명: `keep A from -ing` 는 "A 가 ~하지 못하게 막다"이다. 원문은 `the cap is what keeps it from becoming the rejected hub` 로 `what` 절을 보어에 놓아 상한이 유일한 안전장치라고 강조한다.
- 예문: The cap is what keeps the page from becoming the hub you rejected.
- 유사어: what stops it turning into (영국 구어), the only thing preventing it from becoming (더 강함), the guardrail against (명사형)
- 반의어: what turns it into

## "move only if someone asks"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 지금은 싼 쪽으로 시작하고 요청이 생기면 옮기겠다고 할 때(설계 논의·구어).
- 한국어: 누가 요청할 때만 옮긴다
- 설명: YAGNI 를 말로 하는 방법이다. `only if` 가 조건을 좁힌다. 같은 대화에 `add them when someone with two distinct responsibilities asks` 도 나온다. 둘 다 "수요가 증명되면"을 `someone asks` 로 구체화했다.
- 예문: I'd start with localStorage and move only if someone asks.
- 유사어: revisit when there's demand (문어), cross that bridge when we come to it (관용, 구어), defer until requested (메모체)
- 반의어: build it up front

## "are precedents (with no API prefix of their own)"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 새로 만들 것과 같은 꼴이 저장소에 이미 있다고 근거를 댈 때(코드 조사 보고).
- 한국어: (자체 API 접두사가 없는) 선례다
- 설명: `precedent` 는 가산명사로 써서 사례 하나하나를 센다. `of their own` 은 "자기 몫의"라는 뜻으로 `no … of its own` 꼴이 자주 나온다. 새 패턴이 아니라 이미 가는 길이라고 보여 주는 문장이다.
- 예문: `mag_pixel` and `chat` are precedents with no API prefix of their own.
- 유사어: there is prior art for this (개발자 구어), already work this way (평이), set the pattern (동사형)
- 반의어: would be a first

## "Yes in effect"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 형식상으로는 그런 기능이 없지만 실제 결과는 같다고 답할 때(표·보고서의 짧은 판정).
- 한국어: 사실상 그렇다
- 설명: `in effect` 는 "명목은 아니어도 실질은"이다. `in fact`(실제로, 사실은)와 다르다. 원문은 여러 레시피를 한 요청에 담을 수 있느냐는 물음에 `Yes in effect, since the msrs can come from any recipe` 라고 답했다. 그런 파라미터는 없지만 결과는 같다는 뜻이다.
- 예문: Can one request cover several recipes? Yes in effect, since the IDs can come from any recipe.
- 유사어: effectively yes (같은 뜻), for practical purposes (문어), technically no, but it works out the same (구어로 풀면)
- 반의어: only nominally

## "couples to (two features)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 한 모듈이 다른 것에 의존하게 된다고 비용 칸에 적을 때(설계 비교표).
- 한국어: (두 기능에) 결합된다
- 설명: `couple` 을 자동사로 썼다. 수동 `is coupled to` 가 더 흔하지만 표처럼 짧게 써야 하는 자리에서는 `home couples to two features` 처럼 능동으로 줄인다. 같은 글에 `a screen coupled to many features`, `home tied to everything` 이 나온다.
- 예문: With option B, home couples to two features and the rate limit caps the card count.
- 유사어: depends on (평이), is tied to (구어), takes a dependency on (공식 문서)
- 반의어: is decoupled from

## "may well be the right product call"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 구현이 내린 판단이 옳을 가능성을 인정하면서 절차 문제를 지적할 때(리뷰·티켓, 문어).
- 한국어: 제품 판단으로는 충분히 옳을 수 있다
- 설명: `may well` 은 "그럴 가능성이 꽤 높다"로 `may` 보다 강하다. `call` 은 판단·결정이다(`a judgment call`, `your call`). 원문은 `suppressing may well be the *right* product call (…), but that call belongs in the spec` 으로 내용은 인정하고 자리만 문제 삼았다.
- 예문: Suppressing the badge may well be the right product call, but it should be written down.
- 유사어: is quite possibly the right decision (문어), could easily be right (구어), is probably the correct trade-off (중립)
- 반의어: is clearly the wrong call

## "that call belongs in the spec"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 결정이 틀렸다는 게 아니라 기록될 자리가 잘못됐다고 지적할 때(리뷰·티켓).
- 한국어: 그 결정이 있어야 할 자리는 명세다
- 설명: `belong in` 은 "~에 있어야 마땅하다"이다. 사람이 아니라 결정(`that call`)을 주어로 세워 비난 없이 자리를 바로잡는다. 뒤에 `recorded with its reasoning` 을 붙여 이유까지 적으라고 요구한다.
- 예문: The rule may be right, but that call belongs in the spec, recorded with its reasoning.
- 유사어: should live in the spec (개발자 구어), is a spec-level decision (명사형), needs to be documented in the spec (평이)
- 반의어: can stay an implementation detail

## "This is not a mechanical fix"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 기계적으로 고칠 수 있는 일이 아니라 판단이 필요하다고 티켓의 성격을 밝힐 때.
- 한국어: 기계적으로 고치면 되는 일이 아니다
- 설명: `mechanical` 은 생각 없이 규칙대로 하면 되는 작업을 가리킨다(`a mechanical rename`). 부정문으로 써서 "먼저 결정해야 한다"는 경고가 된다. 원문은 콜론 뒤에 이유를 바로 붙였다.
- 예문: This is not a mechanical fix: someone has to decide which behavior is correct first.
- 유사어: this needs a decision, not a patch (대조형), it's a judgment call (구어), not a find-and-replace job (구어)
- 반의어: a mechanical change, a drive-by fix

## "Gates any future (badge-behavior) work"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 이 티켓이 끝나야 뒤따르는 작업을 시작할 수 있다고 의존 관계를 적을 때(티켓 메모체).
- 한국어: 앞으로의 (배지 동작) 작업을 모두 막고 있다
- 설명: 동사 `gate` 는 "통과 조건이 되다"이다. 주어를 생략한 메모체로, `Blocked by: None` 뒤에 붙어 "이건 막힌 데가 없지만 이게 남을 막는다"는 방향을 밝힌다. `block` 은 지금 막고 있다는 뜻이고 `gate` 는 통과해야 할 문이라는 뜻이다.
- 예문: This decision gates any future badge-behavior work.
- 유사어: is a prerequisite for (문어), blocks (티켓 용어), must land before (구어)
- 반의어: is independent of

## "narrows a shipped signal's behavior"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 이미 배포된 기능의 동작 범위를 구현이 슬그머니 줄였다고 지적할 때(리뷰).
- 한국어: 배포된 신호의 동작을 좁힌다
- 설명: `shipped` 가 무게를 싣는다. 초안이 아니라 사용자가 이미 쓰는 것을 바꿨다는 말이다. `narrow` 는 지우지는 않고 적용 범위를 줄였다는 뜻이라 `remove`·`break` 보다 정확하다.
- 예문: The implementation narrows a shipped signal's behavior without spec sanction.
- 유사어: restricts an existing feature (평이), quietly changes what users already rely on (구어), scopes down a released behavior (중립)
- 반의어: widens, extends

## "do not survive a view switch"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 화면을 바꾸면 사용자가 고른 값이 사라진다고 UX 결함을 적을 때(조사 보고).
- 한국어: 화면 전환을 넘기지 못하고 사라진다
- 설명: `survive` 는 상태가 어떤 사건을 견디고 남는다는 뜻으로 UI·시스템 글에서 자주 쓴다(`survive a reload`, `survive a restart`). 부정형은 "그때 날아간다"이다.
- 예문: Friction is concentrated in user choices that are not shareable or do not survive a view switch.
- 유사어: are lost on view change (평이), reset when you switch views (구어), are not persisted across views (문어)
- 반의어: persist across views

## "not wall clock"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 기준 시각이 실제 현재 시각이 아니라 데이터의 최신 시각이라고 구분할 때(기술 문서).
- 한국어: 실제 시계 시각이 아니다
- 설명: `wall clock (time)` 은 벽시계가 가리키는 실제 시각이다. CPU 시간이나 데이터 기준 시각과 가를 때 쓴다. 원문은 `anchor is the backend's newest timestamp, not wall clock` 으로 괄호 안에서 관사 없이 썼다.
- 예문: The date range is anchored to the backend's newest timestamp, not wall clock.
- 유사어: not the current time (평이), not `now()` (코드로), not real time (덜 정확)
- 반의어: data time, logical time

## "consumed once, then stripped"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: URL 파라미터를 한 번 읽고 주소에서 지운다는 동작을 짧게 적을 때(기술 문서의 괄호 주석).
- 한국어: 한 번 읽힌 뒤 제거된다
- 설명: 과거분사 둘을 `then` 으로 이어 순서를 보인다. `consume` 은 값을 읽어 써 버리는 것이고 `strip` 은 붙어 있던 것을 떼어 내는 것이다. 새로 고침해도 같은 동작이 반복되지 않는 이유가 이 한 줄에 들어 있다.
- 예문: The landing page takes `?q=…&fab=…`, which is consumed once, then stripped.
- 유사어: read once and removed (평이), one-shot (형용사), cleared after first use (평이)
- 반의어: kept in the URL

## "eventually stops reproducing"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 공유 링크가 시간이 지나면 같은 화면을 다시 못 보여 준다고 적을 때(조사 보고).
- 한국어: 언젠가는 재현이 안 된다
- 설명: `reproduce` 를 자동사로 썼다. 버그뿐 아니라 화면·결과에도 쓴다. `eventually` 는 "결국에는"이고 "가끔"이 아니다. 원문은 `sharing is a live re-query link, and pickles expire at 61 days` 를 원인으로 대고 `so` 로 이 결론을 끌었다.
- 예문: Sharing is a live re-query link, so a shared link eventually stops reproducing.
- 유사어: goes dead after a while (구어), will no longer show the same result (평이), has a shelf life (비유)
- 반의어: is a permanent record

## "all behaviour claims are from reading code"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 실행해 보지 않고 코드만 읽고 쓴 보고라고 근거의 등급을 밝힐 때(조사 보고 머리말).
- 한국어: 동작 서술은 전부 코드를 읽고 쓴 것이다
- 설명: `be from -ing` 로 출처를 밝힌다. 원문은 `Nothing was run in a browser, so …` 뒤에 붙였다. 하지 않은 일을 수동태로 먼저 적고 그 결과를 `so` 로 잇는다. `behaviour` 는 영국식 철자이고 미국식은 `behavior` 다.
- 예문: Nothing was run in a browser, so all behaviour claims are from reading code.
- 유사어: this is a static read, not a test (구어), based on code inspection only (문어), untested (한 단어)
- 반의어: confirmed by running it

## "is coarse for CD work"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 기준·해상도가 그 용도에는 너무 거칠다고 평가할 때(분석 보고).
- 한국어: CD 작업에는 (기준이) 거칠다
- 설명: `coarse` 는 `fine` 의 반대로 눈금·기준이 굵다는 뜻이다. `for` 로 용도를 한정해 "다른 데는 몰라도 여기에는"이라고 범위를 좁힌다. 원문은 콜론 뒤에 `a 20 % deviation on a 30 nm CD is 6 nm` 로 바로 숫자를 댔다.
- 예문: A ±20 % outlier rule is coarse for CD work: on a 30 nm CD that is 6 nm.
- 유사어: is too loose for (구어), lacks the resolution for (문어), is a blunt instrument for (비유)
- 반의어: is fine-grained enough for
