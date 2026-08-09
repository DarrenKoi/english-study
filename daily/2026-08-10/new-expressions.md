# 2026-08-10 — 새 표현

## "treat every ID as an opaque string"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 값의 내부 구조를 뜯어보지 말라고 못박을 때(설계 문서·API 규약, 격식)
- 한국어: 모든 ID를 속을 들여다보지 않는 불투명한 문자열로 다뤄라
- 설명: `opaque` 는 "불투명한", 즉 **안을 파싱하거나 규칙을 추측하면 안 되는** 값이라는 뜻. 접미사에 의미가 있어 보여도 그걸 근거로 코드를 짜지 말라는 경고다.
- 예문: The encoded suffix can grow beyond one character, so treat every ID as an opaque string.
- 유사어: don't parse it, just pass it through (평이한 회화체), treat it as a black box (은유적·좀 더 넓은 범위)
- 반의어: derive the value from its parts

## "the installed binary is the authority for command syntax"

- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 문서와 실물이 어긋날 때 무엇을 믿을지 정할 때(규약 문서, 격식)
- 한국어: 명령 문법의 기준은 설치된 실행 파일이다
- 설명: `X is the authority for Y` 는 "Y 에 관해서는 X 가 최종 판단 기준"이라는 틀. 문서가 낡을 수 있는 영역에서 진실의 출처를 한 곳으로 못박는다.
- 예문: The installed binary is the authority for command syntax, so begin with `herdr --help` rather than the examples in this file.
- 유사어: X is the source of truth (더 흔한 기술 관용구), defer to X (동사형·회화에도 씀)
- 반의어: the documentation is authoritative

## "its result is considered seen"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 상태 기계에서 "사용자가 확인했다고 간주되는" 조건을 정의할 때(명세, 격식)
- 한국어: 그 결과는 이미 본 것으로 간주된다
- 설명: `be considered + 형용사/과거분사` 는 판정 주체를 감춘 채 규칙만 남기는 명세용 수동태다. "누가 봤는가"가 아니라 "본 것으로 처리된다"가 요점.
- 예문: An idle pane means the agent is waiting and its result is considered seen.
- 유사어: is treated as acknowledged (격식·좀 더 사무적), counts as read (평이·짧음)
- 반의어: its result has not been seen

## "keep X on one stable control surface"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 여러 조작을 한 창구로 모으는 설계 이유를 밝힐 때(설계 근거, 격식)
- 한국어: X 를 하나의 안정된 조작 지점 위에 모아 둔다
- 설명: `control surface` 는 원래 항공기 조종면에서 온 말인데, 소프트웨어에서는 "무언가를 조작할 때 손을 대는 표면"을 뜻한다. `stable` 이 붙으면 그 손잡이가 도중에 바뀌지 않는다는 약속이다.
- 예문: Use the pane ID as the control target for agents, shells, servers, and logs — this keeps spawning, input, reads, waits, and cleanup on one stable control surface.
- 유사어: a single entry point (더 평이·구조적), one handle for everything (회화체)
- 반의어: scatter the controls across several APIs

## "do not infer a larger topology from X"

- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 작은 요청을 확대 해석하지 말라고 선을 그을 때(에이전트 지침, 격식)
- 한국어: X 로부터 더 큰 구조를 멋대로 추론하지 마라
- 설명: `infer A from B` 는 "B 를 근거로 A 를 추론하다". 여기에 `larger` 를 넣어 "요청보다 큰 것을 짓지 마라"는 범위 제한이 된다. 사람에게도 그대로 쓸 수 있는 문형이다.
- 예문: Do not infer a larger topology from a request to start an agent or command.
- 유사어: don't read more into it than was asked (회화·부드러움), stay within the requested scope (사무적)
- 반의어: extrapolate from the request

## "Inspect before waiting."

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 절차 규칙을 한 줄 격언으로 압축할 때(체크리스트·규약)
- 한국어: 기다리기 전에 먼저 들여다봐라
- 설명: 동명사 두 개를 `before` 로 이은 두 단어짜리 명령. 이미 나와 있는 출력을 확인하지 않고 다음 출력을 기다리면 영영 안 온다는 실전 함정을 압축한 표현이다.
- 예문: Inspect before waiting — read the current output first, then wait for the next state you expect.
- 유사어: look before you leap (관용구·비유적), check the current state first (풀어쓴 평이체)
- 반의어: block on the next event straight away

## "when X is evidence"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)
- 맥락: 무거운 옵션을 언제 켤지 조건을 달 때(가이드 문서)
- 한국어: X 자체가 증거일 때에 한해
- 설명: 명사 `evidence` 를 보어로 써서 "그것이 판단 근거가 되는 경우"라는 조건을 만든다. 색상·서식처럼 평소엔 장식인 것이 문제 상황에서는 증거가 된다는 뉘앙스가 산다.
- 예문: Use `--format ansi` when colors and terminal styling are evidence; otherwise use text.
- 유사어: when X actually matters to the diagnosis (풀어쓴 회화체), when X is diagnostic (더 격식)
- 반의어: when X is only cosmetic

## "tee up a concrete restart"

- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)
- 맥락: 다음 사람이 바로 시작할 수 있게 준비만 해 둘 때(업무 인수인계·구어에 가까운 업무체)
- 한국어: 곧바로 착수할 수 있는 재개 지점을 세팅해 두다
- 설명: 골프에서 공을 티 위에 올려 두는 동작에서 온 말. "대신 쳐 주는 게 아니라, 치기 좋게 올려 둔다"는 절제가 핵심이다.
- 예문: Surface the unfinished work and tee up a concrete restart, but do not start coding until the user picks a job.
- 유사어: line up the next step (평이), set the stage for X (연극 은유·좀 더 격식)
- 반의어: leave it wide open

## "Keep it scannable."

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)
- 맥락: 문서·보고 형식을 지시할 때(짧은 지시문)
- 한국어: 훑어서 읽히게 써라
- 설명: `scannable` 은 "정독하지 않고 눈으로 훑어도 요점이 잡히는" 상태. 목록·굵은 글씨·짧은 행을 요구하는 완곡한 지시로 자주 쓴다.
- 예문: Show the jobs grouped as they're stored and keep it scannable.
- 유사어: make it skimmable (거의 동의·더 구어), easy to take in at a glance (풀어쓴 회화체)
- 반의어: written as dense prose

## "momentum is cheapest there"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)
- 맥락: 여러 후보 중 하나를 고른 이유를 한 줄로 댈 때(추천·설득)
- 한국어: 거기서 다시 속도를 붙이는 비용이 가장 싸다
- 설명: 추상명사 `momentum` 에 `cheap` 을 붙여 "재개 비용"을 경제 용어로 환산한 은유. 최상급 + `there` 로 "다른 데보다 여기가"라는 비교를 압축한다.
- 예문: Normally pick the top in-progress item, since its next action is already written and momentum is cheapest there.
- 유사어: it's the easiest one to pick back up (평이한 회화체), the lowest activation energy (물리 은유·기술 문서)
- 반의어: starting there means paying the ramp-up cost twice

## "so the user can dive straight in"

- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)
- 맥락: 준비 단계를 없애 준 결과를 말할 때(구어·업무 대화)
- 한국어: 바로 뛰어들 수 있게
- 설명: `dive in` 은 "준비운동 없이 곧장 착수하다". `straight` 가 들어가면 중간 절차가 전혀 없다는 점이 강조된다. 회화체라 명세서보다는 안내문·대화에 어울린다.
- 예문: Restate that exact next action so the user can dive straight in.
- 유사어: get going right away (가장 평이), hit the ground running (관용구·이미 속도가 붙은 상태 강조)
- 반의어: have to re-read everything first

## "Don't invent jobs."

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)
- 맥락: 자료가 비어 있을 때의 행동을 못박을 때(짧은 금지 지시)
- 한국어: 없는 일감을 지어내지 마라
- 설명: `invent` 는 "발명하다"보다 여기서는 **사실이 아닌 것을 만들어 낸다**는 부정적 의미. 빈 입력을 그럴듯하게 채우려는 충동을 겨냥한 한 줄이다.
- 예문: If the carryover is missing, say there's nothing carried over — don't invent jobs.
- 유사어: don't make things up (가장 평이), don't fabricate entries (격식·문어)
- 반의어: reconstruct the list from git history

## "dense is better than verbose"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (claude-md-improver 스킬 문서)
- 맥락: 문서 분량 기준을 제시할 때(작성 가이드)
- 한국어: 장황한 것보다 빽빽한 편이 낫다
- 설명: `dense` 를 칭찬으로 쓰는 게 요점이다. 정보 밀도가 높다는 뜻이지 읽기 어렵다는 뜻이 아니고, 반대편에 `verbose`(말만 많은)를 세워 대비시킨다.
- 예문: CLAUDE.md should stay human-readable; dense is better than verbose.
- 유사어: say it once, say it short (구어체 대구), high signal-to-noise (기술 은유)
- 반의어: padded out with explanation

## "one-off fixes unlikely to recur"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (claude-md-improver 스킬 문서)
- 맥락: 문서에 남길 것과 버릴 것을 가를 때(작성 기준)
- 한국어: 다시 생길 것 같지 않은 일회성 수정
- 설명: `one-off` 는 "딱 한 번뿐인". 뒤에 형용사구 `unlikely to recur` 를 관계대명사 없이 바로 붙여 문장을 짧게 유지했다 — 문어에서 흔한 후치 수식이다.
- 예문: Keep it minimal: skip generic best practices and one-off fixes unlikely to recur.
- 유사어: a one-time workaround (평이), an isolated incident (사건 쪽 어휘)
- 반의어: a recurring failure mode

## "when a one-liner suffices"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 2fc9f8aa (claude-md-improver 스킬 문서)
- 맥락: 설명을 늘리지 말라고 조건을 붙일 때(편집 지침, 격식)
- 한국어: 한 줄이면 충분한데도
- 설명: `suffice` 는 `be enough` 의 격식체 동사. 짧아서 지시문에 잘 맞고, `when a one-liner suffices` 는 통째로 "굳이 길게 쓸 자리가 아닌데" 라는 비판이 된다.
- 예문: Avoid verbose explanations when a one-liner suffices.
- 유사어: when one line would do (같은 뜻의 회화체), where brevity serves better (더 문어적)
- 반의어: when the reasoning genuinely needs a paragraph

## "a thin forwarder only"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 70b03c04 (codex rescue 명령 문서)
- 맥락: 중간 계층의 역할을 최소로 못박을 때(설계 규약)
- 한국어: 그저 얇게 넘겨 주기만 하는 중계자
- 설명: `thin` 은 로직을 거의 담지 않았다는 뜻이고 `forwarder` 는 받아서 그대로 넘기는 쪽. 끝의 `only` 가 "그 이상 하지 마라"는 금지까지 얹는다.
- 예문: The subagent is a thin forwarder only — it runs one command and returns that command's stdout as-is.
- 유사어: a pass-through layer (거의 동의·기술 문서), a dumb pipe (구어·업계 은어)
- 반의어: an orchestrator that owns the decision

## "report findings ranked by severity"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 70b03c04 (Codex 리뷰 요청문)
- 맥락: 리뷰·감사 결과의 제출 형식을 지정할 때(의뢰문, 격식)
- 한국어: 심각도 순으로 정렬해 보고하라
- 설명: `ranked by X` 는 과거분사 후치 수식으로 "X 기준 정렬된"을 붙인다. 리뷰 의뢰문의 표준 문구라 그대로 외워 두면 좋다.
- 예문: Do not change code — report findings ranked by severity with file:line.
- 유사어: list them worst-first (평이한 회화체), prioritized by impact (영향 기준으로 바꾼 변형)
- 반의어: report them in the order you found them

## "be adversarial, look for real defects"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 70b03c04 (Codex 리뷰 요청문)
- 맥락: 리뷰어에게 동조하지 말고 흠을 찾으라고 주문할 때(의뢰문)
- 한국어: 적대적으로 보라, 진짜 결함을 찾아라
- 설명: `adversarial` 은 "일부러 반대편에 서는" 태도. 뒤에 `real` 을 붙인 이유가 핵심인데, 스타일 지적이 아니라 실제로 깨지는 것만 가져오라는 제한이다.
- 예문: Be adversarial and look for real defects, not style nits.
- 유사어: try to break it (가장 평이·강함), poke holes in it (관용구·구어)
- 반의어: sanity-check it

## "I'm mid-turn running the scan"

- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (assistant)
- 맥락: 자기 상태가 결과에 섞여 들어온 이유를 밝힐 때(구어에 가까운 설명)
- 한국어: 나는 지금 턴 도중에 그 스캔을 돌리는 중이다
- 설명: `mid-` 접두사를 명사에 붙여 `mid-turn`, `mid-flight`, `mid-migration` 처럼 "그 일이 아직 안 끝난 시점"을 한 단어로 만든다. 진행형과 함께 쓰면 자연스럽다.
- 예문: Seeing my own pane as `working` is expected — I'm mid-turn running the scan, so I show up in my own results.
- 유사어: in the middle of doing X (풀어쓴 회화체), while X is still in flight (기술 은유)
- 반의어: between turns

## "a stale-credential surprise"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 8ff8dc4b (assistant)
- 맥락: 나중에 터질 뻔한 실패를 미리 막았다고 말할 때(기술 설명)
- 한국어: 만료된 자격증명 때문에 뒤늦게 터지는 사고
- 설명: `명사-명사 + surprise` 조합은 "예고 없이 나중에 드러나는 문제"를 가리키는 구어적 기술 표현이다. 하이픈으로 앞을 한 덩어리 형용사로 묶는 게 관건.
- 예문: The check round-trips through the app-server, so this won't fail later with a stale-credential surprise.
- 유사어: a nasty surprise down the line (더 구어·범용), a latent auth failure (격식·중립)
- 반의어: a verified, live session

## "quote anyway for predictability"

- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 9cb33a18 (assistant)
- 맥락: 안 해도 되지만 습관으로 하라고 권할 때(실무 조언)
- 한국어: 어차피 되긴 하지만, 예측 가능하게 쓰려면 따옴표를 쳐라
- 설명: `anyway` 가 "필요 없다는 건 알지만 그래도"라는 양보를 한 단어로 처리한다. `for + 추상명사` 로 이유를 짧게 붙이는 틀(`for safety`, `for consistency`)도 함께 익혀 두면 쓸모가 많다.
- 예문: The label argument is variadic, so unquoted multi-word names get joined rather than rejected — quote anyway for predictability.
- 유사어: it's optional, but do it (가장 평이), belt and braces (관용구·이중 안전장치 뉘앙스)
- 반의어: skip the quotes when the shell won't split it
