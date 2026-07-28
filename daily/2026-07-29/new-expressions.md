# 2026-07-29 — 새 표현

## "roll over (at 20GB or 7 days)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md
- 맥락: 로그 인덱스·파일이 한도에 닿아 다음 것으로 갈아타는 동작을 설계 문서에 못 박을 때(문어·격식).
- 한국어: (한도에 닿으면 새 것으로) 넘어가다, 이월되다
- 설명: 굴러서 넘어간다는 그림에서 왔다. 금융에서 만기를 연장할 때도 같은 단어를 쓴다. 동사는 두 단어 `roll over`, 명사·형용사는 붙인 `rollover` 로 갈린다 — `the rollover alias`, `roll over at 20GB`.
- 예문: Both families roll over at 20GB or 7 days, use 2 primary shards, 1 replica, and a 30-second refresh interval.
- 유사어: rotate (로그 파일 회전에 오래 쓰인 말, 더 구식), cycle to a new index (뜻만 풀어 쓴 평이한 표현)
- 반의어: write to a single fixed index

## "a preflight (check)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md
- 맥락: 본 작업에 들어가기 전에 전제가 맞는지 먼저 확인하고, 아니면 아예 시작하지 않을 때.
- 한국어: 사전 점검, 이륙 전 점검
- 설명: 조종사가 이륙 전에 체크리스트를 훑는 데서 온 말. 그래서 "실패하면 그냥 안 뜬다"는 뉘앙스가 붙는다. 실행 도중이 아니라 **시작 시점에** 잡아낸다는 점이 핵심이라, 설정 오류를 새벽 3시가 아니라 기동 순간에 터뜨리고 싶을 때 쓴다.
- 예문: The handler runs a rollover-alias preflight before the first bulk write, so a misconfigured alias fails at startup instead of at midnight.
- 유사어: a sanity check (더 가볍고 구어에 가까움), a guard clause (코드 안 조기 반환), validate up front
- 반의어: fail at runtime, discover it in production

## "an allowlist of X"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (배포 번들에 무엇이 들어가는지 확인하는 대목)
- 한국어: 허용 목록
- 맥락: "무엇을 막을까"가 아니라 "무엇만 통과시킬까"로 뒤집어 설명할 때. 보안·배포 문서에서 기본 어휘.
- 설명: `whitelist` 를 쓰던 자리를 요즘 문서는 `allowlist` 로 바꿔 쓴다. 색 은유를 버리고 뜻만 남긴 말이라 회사 문서에서 더 안전한 선택. 짝은 `denylist`(옛 `blacklist`).
- 예문: `scripts/deploy/pack.py:36` uses an allowlist of seven `INCLUDED_ROOTS`, and `office_utils` isn't one of them.
- 유사어: a whitelist (같은 뜻, 오래된 표기), an explicit include list (평이하게 풀어 쓴 말)
- 반의어: a denylist, a blocklist

## "make the typecheck go red"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: (테스트·타입 검사를) 일부러 먼저 빨갛게 만들다
- 맥락: 고치기 전에 실패를 먼저 만들어 증거로 삼는 순서를 설명할 때. 개발자끼리의 구어에 가깝지만 설계 문서에도 그대로 들어간다.
- 설명: 빨강(실패) → 초록(통과)의 신호등 은유. `go red` 는 저절로 그렇게 됐다는 뜻이고, `make it go red` 는 그걸 **노리고** 만들었다는 뜻이라 의도가 드러난다. 반대 방향은 `take it to green`.
- 예문: Now the frontend type declarations — this is the change that makes `typecheck` go red.
- 유사어: fail first (짧고 담백), turn the suite red, write the failing test first (TDD 정석 표현)
- 반의어: go straight to green (증거 없이 바로 고쳐 버리다)

## "shadow (the real package)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: (같은 이름으로) 진짜를 가려 버리다
- 맥락: import 경로·PATH 순서 때문에 가짜가 진짜보다 먼저 잡힐 위험을 경고할 때.
- 설명: 그림자가 덮어 가린다는 그림. 지우거나 망가뜨리는 게 아니라 **그냥 안 보이게** 한다는 데 무서움이 있다. 그래서 뒤에 오는 문장은 대개 조용한 실패를 설명한다.
- 예문: A tracked copy would shadow the real package at the office and serve fabricated data at HTTP 200.
- 유사어: mask, take precedence over (중립·문어), win the import (구어)
- 반의어: defer to the real module

## "a (home) stand-in"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/recipe_idp.txt, transcript:[assistant]
- 한국어: 대역, 대신 세워 둔 것
- 맥락: 진짜를 쓸 수 없는 환경에서 같은 자리·같은 이름으로 세워 둔 물건을 가리킬 때.
- 설명: 영화 촬영의 대역 배우에서 온 말이라, "겉과 인터페이스는 같지만 알맹이는 아니다"라는 뜻이 처음부터 붙어 있다. `stub` 이 최소한만 흉내 낸 것이라면 `stand-in` 은 **자리까지 대신 차지한다**는 쪽이 강하다.
- 예문: The stand-in's whole payoff is that it verifies the import, the signature, and the column dtypes through the real code path.
- 유사어: a stub (더 기술적·최소한), a placeholder (자리만 채움), a body double (사람 비유, 구어)
- 반의어: the real thing, the production implementation

## "progressive enhancement"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 한국어: 점진적 향상 — 없어도 되고, 있으면 더 좋아지는 층
- 맥락: JS·부가 기능을 필수가 아닌 덤으로 두겠다고 제약에 못 박을 때(설계 문서).
- 설명: 바닥(HTML)은 혼자서도 읽히게 두고 그 위에 얹는다는 순서 개념. 위에서 깎아 내려오는 `graceful degradation` 과 목표는 같지만 출발점이 반대다.
- 예문: JavaScript is progressive enhancement: article content and basic navigation remain usable when it is disabled.
- 유사어: graceful degradation (반대 방향에서 같은 목표), works without JavaScript (평이)
- 반의어: a hard dependency on JavaScript

## "internet egress"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md
- 한국어: 외부로 나가는 통신
- 맥락: 사내망 밖으로 한 바이트도 못 나가게 하겠다고 보안 제약을 쓸 때(격식).
- 설명: 라틴어 어원의 딱딱한 단어라 회의에서 말로 하면 어색하다. 말할 때는 `nothing calls out to the internet` 쪽이 자연스럽다. 짝은 `ingress`(들어오는 쪽).
- 예문: The application and every logging destination remain inside the company network; do not add external SaaS or internet egress.
- 유사어: outbound traffic (중립), calling out to the internet (회화)
- 반의어: ingress

## "your premise doesn't hold"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: 그 전제가 성립하지 않는다
- 맥락: 상대의 걱정을 반박하되 사람이 아니라 **깔고 있던 전제**만 겨냥할 때. 회의·리뷰에서 쓸 수 있을 만큼 부드럽다.
- 설명: `hold` 는 여기서 "버티다·성립하다"라는 자동사. `You're wrong` 이 사람을 치는 반면 이 문형은 문장 하나만 치기 때문에 대화가 이어진다. 앞에 `Checked it —` 처럼 근거를 먼저 붙이면 더 안전하다.
- 예문: Checked it — your premise doesn't hold, and the reason is worth knowing.
- 유사어: that assumption doesn't survive checking (더 격식), that's not actually the case (평이·회화)
- 반의어: your premise checks out, that holds

## "an invariant that may only be a tendency"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: 불변식인 줄 알았지만 그저 경향일지도 모르는 것
- 맥락: "보통 그렇다"는 관찰을 코드가 "항상 그렇다"로 굳혀 버렸을 때 그 위험을 한 줄로 지적하는 말.
- 설명: `invariant`(언제나 참) 와 `tendency`(대체로 참) 를 나란히 놓아 대비를 만든다. 이 대비가 있으면 "확인해 봐야 한다"는 요구가 잔소리가 아니라 정의상 필요한 절차로 읽힌다.
- 예문: You described that rule as "usually" true, so the mock is currently teaching an invariant that may only be a tendency.
- 유사어: a rule versus a pattern, always true versus usually true (더 평이한 대비)
- 반의어: a confirmed invariant, a guarantee

## "before any UI leans on it"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: (아직 확인 안 된 사실에) 기대어 만들기 전에
- 맥락: 검증되지 않은 사실 위에 기능을 얹지 말자고 말할 때. 설계 근거를 글로 남길 때 잘 어울린다.
- 설명: `lean on` 은 무게를 실어 기댄다는 몸짓 그대로다. `use it` 이 그냥 쓰는 것이라면 `lean on it` 은 **그게 무너지면 같이 무너진다**는 함의까지 담는다.
- 예문: It needs a look across several recipes before any UI leans on it.
- 유사어: rely on, build on top of, take it as given
- 반의어: treat it as unverified, hold it at arm's length

## "so it cannot be mistaken for X"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md
- 한국어: X로 오인될 수 없도록
- 맥락: 이름·라벨을 정하는 이유를 대며 "헷갈릴 여지 자체를 없앤다"고 못 박을 때.
- 설명: 수동태 `be mistaken for` 는 오해하는 사람을 지목하지 않아서 비난이 빠진다. `so that nobody confuses A with B` 보다 한 단계 격식 있고 문서에 어울린다.
- 예문: Set demo index names to `skewnono_logging_local-demo` so the label cannot be mistaken for production.
- 유사어: to rule out any confusion with (격식), so no one confuses it with (회화)
- 반의어: be indistinguishable from

## "that's the gap this question exposes"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: 이 질문이 실제로 드러낸 빈틈이 그것이다
- 맥락: 상대의 질문이 정답은 아니었지만 진짜 구멍을 찾아냈을 때, 그 공을 돌려주며 방향을 트는 말.
- 설명: 질문자를 세워 주면서 논점을 옮기는 두 가지 일을 한 문장이 같이 한다. `actually` 를 끼우면 "표면의 걱정은 아니었지만 그 밑은 맞았다"는 결이 살아난다.
- 예문: That's the gap this question actually exposes — one line each, and it guards the file you were worried about.
- 유사어: that's the real hole here, this surfaces a blind spot (더 문어)
- 반의어: close the gap

## "force through (a blocker)"
- 레지스터: professional, conversational
- 출처: transcript:[user] skewnono_v3_nuxt (executing-plans 스킬 문서)
- 한국어: 막힌 것을 억지로 밀고 나가다
- 맥락: 막혔을 때 멈춰 물으라고 지시할 때. 명령형 부정 `Don't force through ~` 로 굳어져 쓰인다.
- 설명: `push through` 가 중립이거나 칭찬일 수 있는 반면 `force through` 는 거의 늘 경고다. 억지로라는 뜻이 `force` 에 이미 들어 있어서다.
- 예문: Don't force through blockers — stop and ask.
- 유사어: push through (중립·긍정도 가능), barrel ahead (더 거칠고 구어), power through (버텨 내다, 칭찬 쪽)
- 반의어: stop and ask, park it

## "worth knowing"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: 알아 둘 만하다
- 맥락: 설명을 덧붙이기 전에 "지금 시간 쓸 값어치는 있다"고 미리 표시하는 말.
- 설명: `worth + -ing` 는 목적어를 앞으로 뺀 형태라 `worth to know` 가 아니다. 짧아서 붙이기 쉽고, 상대가 계속 읽을지 말지 판단하게 해 준다.
- 예문: Your premise doesn't hold, and the reason is worth knowing.
- 유사어: worth understanding, worth a minute of your time (더 가벼움), instructive (격식)
- 반의어: not worth dwelling on

## "leaving X alone"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 한국어: (남이 쓰고 있는 것을) 건드리지 않고 그대로 두다
- 맥락: 검증하느라 뭔가를 띄웠지만 상대가 쓰던 환경은 손대지 않았다고 안심시킬 때.
- 설명: 분사구문 `leaving ~ alone` 을 문장 뒤에 달면 "그렇게 하면서 동시에 이건 안 건드렸다"가 한 호흡에 들어간다. 사람에게 쓰면 "내버려 둬"라 무례할 수 있지만 포트·파일·프로세스에는 중립이다.
- 예문: Browser-verified on a worktree instance (:3001/:5051, leaving your running :3000/:5050 alone).
- 유사어: leave untouched (문어), keep out of the way of, without disturbing (격식)
- 반의어: clobber, overwrite, take over the port

## "space out (the calls)"
- 레지스터: conversational, technical
- 출처: transcript:[user] skewnono_v3_nuxt (verify 스킬 문서)
- 한국어: 간격을 두고 띄엄띄엄 보내다
- 맥락: 호출 제한에 걸리지 않게 요청 사이에 시간을 두라고 일러 줄 때. 구어체 지시.
- 설명: 이어 붙은 것을 벌려 놓는다는 뜻의 일상어. 시스템이 대신 조절하는 `throttle` 과 달리 **사람이 손으로 벌리는** 쪽이다. 엇갈리게 배치하는 `stagger` 는 간격보다 순서에 초점이 있다.
- 예문: Rate limit: 20 requests per 5 seconds per user — space out curl loops or vary `LASTUSER`.
- 유사어: stagger (엇갈리게 배치), throttle (시스템이 속도를 제한), add a delay between calls (설명형)
- 반의어: hammer (한꺼번에 두들기다), fire them off back-to-back
