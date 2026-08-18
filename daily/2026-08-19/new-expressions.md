# 2026-08-19 — 새 표현

## "What checks out"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 코드 리뷰·감사 보고서에서 지적 목록을 꺼내기 전에 "여기까지는 이상 없다"를 먼저 묶는 소제목(문어·격식).
- 한국어: 확인 결과 문제없는 것들
- 설명: `check out` 은 "대조해 보니 맞다". 명사절 `what checks out` 으로 만들면 항목 나열의 제목이 된다. 지적부터 던지지 않고 통과분을 먼저 세워 두면 뒤의 HARD finding 이 트집이 아니라 판정으로 읽힌다.
- 예문: What checks out: every exact-match field uses its `.keyword` sub-field, and the archive dates are discovered rather than computed.
- 유사어: what's sound (덜 격식·더 일상), no findings here (판정문투로 더 건조), the clean bill (구어·과장기)
- 반의어: HARD findings / what breaks

## "silent truncation"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 상한에 걸려 데이터가 잘렸는데 아무 신호도 안 나갈 때 그 결함에 이름을 붙이는 말(문어·기술 문서).
- 한국어: 조용한 절단 — 잘린 사실을 알리지 않는 잘림
- 설명: 짝이 되는 동사가 `surface`(드러내다)다. `detects truncation via doc_count > len(hits) and surfaces it` 처럼 "감지한다 + 드러낸다" 두 동작을 나눠 쓰면 어디가 빠졌는지가 분명해진다. 잘린 값은 없는 값보다 나쁘다 — 그럴듯해 보이기 때문이다.
- 예문: `_bsm_by_tool` caps `top_hits` at forty with no `doc_count` check, so a thirty-day window truncates silently and the week-after average quietly becomes a day-13 reading.
- 유사어: quiet data loss (덜 전문적), capped without warning (풀어쓴 평이체), lossy by default (더 넓은 뜻)
- 반의어: surface the truncation / fail loudly

## "Speculative Generality"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 리팩터링 냄새 이름을 그대로 판정 라벨로 쓸 때(리뷰 문서·격식). 대문자로 고유명사처럼 쓴다.
- 한국어: 언젠가 쓸까 봐 미리 만들어 둔 일반화
- 설명: Fowler 의 code smell 목록에서 온 말. 호출자가 없는 export, 구현체가 하나뿐인 인터페이스가 전형이다. "나중에 쓸 것 같아서"는 근거가 아니라 증상이라는 뜻을 라벨 하나로 전달한다.
- 예문: `_office_mdc.latest_snapshot` is exported with no caller in this change — Speculative Generality, so I deleted it along with its Redis path.
- 유사어: YAGNI violation (더 구어·개발자 은어), built for a caller that doesn't exist (풀어쓴 설명체), premature abstraction (덜 특정적)
- 반의어: built to the one caller we have

## "a chicken-and-egg"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: 두 조건이 서로를 기다려 시작점이 없을 때, 설계 논의에서 문제 유형에 이름을 붙이며(구어에 가깝지만 문서에도 씀).
- 한국어: 닭이 먼저냐 달걀이 먼저냐 — 서로가 서로의 전제인 교착
- 설명: 명사로 통째로 쓰고 뒤에 `in ~` 으로 어디에 있는 교착인지 붙인다. 관용구라 설명이 필요 없어, 곧바로 "그래서 게이트를 어디에 걸 것인가"로 넘어갈 수 있다.
- 예문: There's a chicken-and-egg in the gating: the roster the dropdowns render comes from the payload itself, so refusing to fetch would leave nothing to pick from.
- 유사어: a circular dependency (기술적·중립), you can't get there from here (구어·체념조)
- 반의어: a clean starting point

## "the choice is unstated"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 판단 자체는 옳지만 근거가 코드에도 문서에도 없을 때, 사람을 탓하지 않고 결함만 짚는 리뷰 문장(격식).
- 한국어: 그 선택이 어디에도 적혀 있지 않다
- 설명: `Defensible but the choice is unstated` 형태로 앞에 인정, 뒤에 지적을 배치한다. `undocumented` 보다 좁다 — 문서가 없다는 게 아니라 *왜 그렇게 갈렸는지*가 없다는 말이다.
- 예문: The asymmetry is defensible — MDC is load-bearing here — but the choice is unstated, so I wrote the reason into the docstring instead of changing the behaviour.
- 유사어: the rationale never made it into the code (풀어쓴 회화체), silently divergent (더 날 선)
- 반의어: the reasoning is written down beside it

## "X is still decoration"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 화면에 뜨긴 하지만 아무것도 보증하지 않는 지표를 두고, 스펙 문서의 표현을 그대로 되받아 쓸 때(격식).
- 한국어: 여전히 장식일 뿐이다
- 설명: 값이 틀렸다는 게 아니라 *뜻이 없다*는 지적이라 반박이 어렵다. 뒤에 무엇을 세면 장식이 아니게 되는지를 한 줄 붙여야 지적이 완결된다.
- 예문: Run-count-based confidence is still decoration: one run measuring six features scores High on its own, which is exactly the pseudo-replication the estimator avoids.
- 유사어: cosmetic (동작 무관한 변경 쪽에 더 자주), for show, not for load (구어·비유적)
- 반의어: it carries weight / it gates something

## "structurally cannot catch it"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 테스트가 통과한 이유가 코드가 맞아서가 아니라 픽스처가 결함을 복제하고 있어서일 때(리뷰·격식).
- 한국어: 구조상 잡을 수 없다
- 설명: `didn't catch it`(이번에 못 잡았다)과 `cannot catch it`(어떤 실행에서도 못 잡는다)은 무게가 다르다. `structurally` 를 얹으면 "테스트를 더 돌려도 소용없다"까지 한 단어로 전달된다.
- 예문: The test doubles carry `tzinfo=KST` too, so the home suite structurally cannot catch the nine-hour leak.
- 유사어: green for the wrong reason (구어·리뷰 은어), the fixture reproduces the bug (풀어쓴 설명체)
- 반의어: the regression test fails on the old code

## "Same smell, lower risk"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 앞서 지적한 것과 같은 패턴이지만 파급이 작은 항목을 강등해 배치할 때 쓰는 소제목(리뷰·간결체).
- 한국어: 같은 냄새, 낮은 위험
- 설명: 명사구 두 개를 쉼표로만 이은 대구라 판정 라벨처럼 읽힌다. 같은 결함을 두 번 길게 설명하지 않으면서 "봐준 게 아니라 순위를 매긴 것"임을 밝힌다.
- 예문: Same smell, lower risk: `maintenance_events` also skips the `doc_count` check, though twenty-four documents over sixty days will rarely reach the cap.
- 유사어: the same pattern, less exposure (더 평이), non-blocking variant of the above (더 절차적)
- 반의어: a new failure mode

## "an explicit empty state"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (user·assistant)
- 맥락: 아직 조건이 안 채워진 화면을 무엇으로 채울지 정할 때, 스켈레톤·빈 그래프와 대비해서(설계 논의).
- 한국어: "선택하세요"라고 대놓고 말하는 빈 화면
- 설명: `empty state` 는 UI 용어로 굳은 명사구다. `explicit` 이 붙으면 "비어 있음을 숨기지 않는다"는 선택이 강조된다. 스켈레톤은 데이터가 오는 중이라는 약속으로 읽히므로, 아무것도 요청하지 않은 상태에는 거짓말이 된다.
- 예문: The downstream panels render an explicit empty state until both the tool model and the recipe are chosen.
- 유사어: a blank slate with a prompt (풀어쓴 회화체), a zero-data view (더 건조)
- 반의어: a loading skeleton

## "a skeleton implies data is coming"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: UI 선택을 정당화할 때, 화면 요소가 사용자에게 어떤 *약속*을 하는지로 논거를 세우며(설계 문서·격식에 가까움).
- 한국어: 스켈레톤은 데이터가 오고 있다는 뜻이 된다
- 설명: 주어를 사람이 아니라 화면 요소로 두는 것이 요령이다 — 취향 다툼이 아니라 요소의 의미에 대한 진술이 된다. `imply` 대신 `promise`·`read as` 로 바꿔도 같은 구조가 굴러간다.
- 예문: A skeleton implies data is coming, so an explicit empty state is the honest option while nothing has even been requested.
- 유사어: it reads as a computed verdict (같은 구조의 변형), that element makes a promise we can't keep (더 회화체)
- 반의어: it says nothing it can't back up

## "correct on the headline laws"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 스펙 위반을 여럿 지적한 뒤, 그래도 큰 규칙은 지켰다고 균형을 잡아 마무리할 때(리뷰·격식).
- 한국어: 큰 원칙에서는 맞다
- 설명: `headline` 이 형용사로 붙어 "여러 규칙 중 표제급"을 뜻한다. 지적 목록 끝에 이 문장을 놓으면 리뷰가 흠집내기가 아니라 저울질로 읽힌다.
- 예문: Correct on the headline laws: run-as-unit, median-not-mean, zero-diagonal symmetric matrices, and None where a value is genuinely absent.
- 유사어: the fundamentals hold (더 평이), sound where it counts (구어에 가까움)
- 반의어: it misses the point of the spec

## "the contract has the slot, but nobody asked"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md
- 맥락: 기술적으로 허용되지만 요구된 적 없는 추가물을 범위 지적으로 올릴 때(리뷰·약간 구어).
- 한국어: 자리는 계약에 있지만, 아무도 요청하지 않았다
- 설명: `nobody asked` 는 단독으로는 무례한 인터넷 말투지만, 앞에 허용 사실을 인정하는 절을 붙이면 범위 판정 문장이 된다. 대구가 방어와 지적을 동시에 담는다.
- 예문: The `raw` diagnostics dict is `NotRequired` in the contract, so it's legal — but nobody asked for it, and it ships on every payload.
- 유사어: allowed, not requested (극단적으로 압축), outside what the ticket covers (격식·중립)
- 반의어: this was the explicit ask

## "zero file overlap, so I rebased rather than merged"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: 남의 커밋이 먼저 올라온 뒤 자기 작업을 어떻게 얹었는지 보고할 때(작업 로그·간결체).
- 한국어: 파일이 하나도 겹치지 않아 머지가 아니라 리베이스로 얹었다
- 설명: 근거절(`zero file overlap`)을 앞에 두고 결정을 뒤에 두는 순서가 핵심이다. 뒤집으면 "리베이스했다, 왜냐하면"이 되어 사후 정당화처럼 들린다. `rather than` 이 선택지 둘을 실제로 저울질했음을 보여준다.
- 예문: Their commit was backend-only — zero file overlap, so I rebased rather than merged and re-ran the browser check.
- 유사어: no touched files in common (풀어쓴 평이체), disjoint diffs (더 기술적·짧음)
- 반의어: we both edited the same file

## "stale by the time it lands"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: 다른 작업이 도는 동안 파일을 읽지 않겠다고 밝힐 때, 기다림을 게으름이 아니라 판단으로 만드는 문장(구어·업무).
- 한국어: 그게 들어올 즈음엔 이미 낡은 정보가 된다
- 설명: `land` 는 "작업이 브랜치에 안착하다"는 개발 은어다. `by the time ~` 절이 시점 비교를 만들어, 지금 읽는 것과 나중의 진실 사이 간극을 한 문장에 담는다.
- 예문: A read I take now could be stale by the time their work lands, so I armed a watcher instead of opening the file.
- 유사어: out of date before I use it (평이·회화), invalidated on arrival (더 건조·기술적)
- 반의어: the tree is quiet, so a read holds

## "decisions locked in"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt (assistant)
- 맥락: 착수 전에 합의된 사항만 목록으로 못박아 두고 대기 상태를 알릴 때(업무 보고·중간 격식).
- 한국어: 확정한 결정들
- 설명: `lock in` 은 "더 논의하지 않기로 고정하다". 완료형 분사구(`Decisions locked in:`)로 제목을 만들면 동사도 주어도 없이 상태만 남아, 목록이 깔끔하게 붙는다.
- 예문: Decisions locked in for when I start: explicit empty state, one shared component name, top-bar placement on both pages.
- 유사어: settled and not up for debate (더 단호), agreed scope (명사구·건조)
- 반의어: still open / to be resolved from the code
