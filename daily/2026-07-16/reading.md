# 2026-07-16 — 정독

## 단락 1

The `skewvoir/analysis` Dashboard view spreads eight full-width/large panels down a tall page that requires scrolling. The linked-inspection panels (Wafer Map, Radius Plot, Measurement Points) — which share one `focusedSequence` so a click in one rings the others — are scattered across non-adjacent grid cells, so the sync is never visible at once. The Wafer Map is oversized, draws no actual wafer, and only offers a single dot view. The stat cards (coverage, 이상 사이트) and the parameter table consume a lot of vertical space.

**문법·구조**: 문제 상황을 서술하는 전형적인 **현재시제 서술** 단락입니다. 시제가 전부 현재형(spreads, share, is, draws, consume)인데, 이는 "지금 이 코드가 이렇게 되어 있다"는 **지속 상태**를 기술하기 때문이에요. 핵심은 둘째 문장의 **삽입 관계절**입니다: 주어 `The linked-inspection panels` 와 동사 `are scattered` 사이에 em-dash(—)로 `which share one focusedSequence so a click in one rings the others` 를 끼워 넣었죠. 이렇게 대시로 감싸면 "부가 설명이니 건너뛰고 읽어도 문장이 성립"함을 시각적으로 보여 줍니다(괄호보다 격식 있고, 콤마보다 경계가 뚜렷). 그리고 두 번 나오는 `so` 에 주목하세요 — 앞의 `so a click in one rings the others` 는 **목적/결과의 so(그래서 ~하도록)**, 뒤의 `so the sync is never visible at once` 는 **결과의 so(그 결과 ~하다)** 로, 원인→결과를 사슬처럼 잇습니다. 셋째 문장 `is oversized, draws no actual wafer, and only offers…` 는 하나의 주어에 **동사 세 개를 병렬**로 달아 결함을 리듬 있게 나열한 예입니다.

**핵심 표현**:
- **spread ... down a tall page** — (패널들이) 긴 페이지에 걸쳐 죽 늘어서다. 공간을 위아래로 "펼쳐 차지한다"는 그림.
- **a click in one rings the others** — 하나를 클릭하면 나머지에 (동기화) 표시가 켜진다. 여기서 `ring` 은 "링(테두리)을 두르다 → 강조 표시하다"라는 동사 용법.
- **never visible at once** — 한눈에 동시에 보이지 않는다. `at once` = 동시에/한꺼번에.

**격식 짝**:
- refined: *The synchronized selection is never visible simultaneously.* (문어·격식)
- plain: *You can't see the sync all at once.* (회화)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-15-skewvoir-analysis-compact-dashboard-design.md</sub>

---

## 단락 2

All B1 analytics collapse into one pure, unit-tested function `overviewSites()` (coverage + outlier count + status + table rows) that every panel renders — so coverage, outlier badge, wafer `◎`, and the navigator column can never disagree. A shared `focusedSequence` state in `useSkewvoirAnalysis` links the wafer map, radius plot, measurement-points table, and SEM image. Layout is a 12-column grid in `views/Dashboard.vue`.

**문법·구조**: 설계 의도를 밝히는 단락이라 역시 **현재시제**입니다. 첫 문장의 뼈대는 `analytics collapse into one function that every panel renders` 인데, `collapse into` 는 "여러 개가 하나로 합쳐져 내려앉다"는 강한 동사 선택이에요(단순히 combine 보다 "산만하던 것들이 한 점으로 수렴"하는 그림). 관계절 `that every panel renders` 는 앞의 `function` 을 수식합니다. 이어지는 em-dash 뒤 `so ... can never disagree` 는 **결과절**로 "그래서 서로 어긋날 수 없다"는 설계의 이득을 못 박습니다 — `can never disagree`(절대 불일치할 수 없다)라는 **강한 부정 조동사**가 단일 출처(single source)의 안전성을 강조하죠. 둘째 문장의 동사 `links`(A links B, C, and D)는 하나의 상태가 여러 패널을 "묶어 연결"함을 능동태로 간결히 표현합니다.

**핵심 표현**:
- **collapse into one function** — 여러 계산을 한 함수로 합쳐 버리다. 중복·불일치를 없애는 리팩터링 어법.
- **can never disagree** — (서로) 절대 어긋날 수 없다. 단일 출처 설계의 이득을 표현하는 관용적 문구.
- **a shared state links A, B, and C** — 공유 상태 하나가 A·B·C를 연결한다.

**격식 짝**:
- refined: *Consolidating the logic into a single function guarantees the panels cannot diverge.* (문어·격식)
- plain: *Put it all in one function and the panels can't get out of sync.* (회화)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-skewvoir-phase-b1-measurement-overview.md</sub>

---

## 단락 3

The new image service keeps its home and office builds behind a single seam, so only one thing changes between them: where the bytes come from. At home the mock generates a deterministic SVG on demand; in the office a thin client relays the real micrograph from the tool's FTP server. Everything around that seam — the disk cache, the "download all" job it kicks off, and the nightly purge — runs identically in both worlds. When the office source fails, the failure surfaces as an explicit JSON error rather than a fabricated image, and a circuit breaker keeps a flaky tool from dragging the whole service down. The rule is simple: relay what is real, and never invent data to paper over a gap.

**문법·구조**: 하루치 핵심 표현을 자연스러운 흐름에 녹인 **모범 단락**입니다. 첫 문장은 `so only one thing changes: where the bytes come from` 처럼 **콜론(:)으로 "그 하나가 무엇인지"를 뒤에 밝히는** 구조 — 콜론은 "지금부터 그 정체를 말하겠다"는 신호예요. 둘째 문장은 세미콜론(;)으로 **home 과 office 를 대조**시켰습니다(`At home ...; in the office ...`). 대조를 한 문장 안에 세미콜론으로 나란히 두면 두 경우가 한눈에 비교됩니다. 셋째 문장은 다시 em-dash로 목록을 삽입해 "그 seam 을 둘러싼 것들"을 열거하고, 관계절 `it kicks off`(그 job 을 그것이 시작한다)가 `job` 을 수식합니다. 넷째 문장의 `surfaces as ... rather than ...` 는 **"A로 드러난다, B가 아니라"**라는 대조 어법이고, 마지막 문장의 콜론+명령형(`relay what is real, and never invent data`)은 원칙을 표어처럼 압축합니다.

**핵심 표현**:
- **behind a single seam** — 단 하나의 이음새(교체 지점) 뒤에 숨겨. 홈↔오피스 차이를 한 곳에 격리.
- **the job it kicks off** — 그것이 시작(발동)하는 작업.
- **paper over a gap** — 빈틈을 대충 덮어 가리다(부정적).

**격식 짝**:
- refined: *The failure is surfaced as an explicit error rather than concealed behind a fabricated image.* (문어·격식)
- plain: *If it breaks, it says so instead of faking an image.* (회화)

<sub>출처: 모범 단락(작성) — 오늘의 표현(thin glue, relay, kick off, surface as, circuit breaker, invent data, purge, on demand, seam)을 엮음</sub>

---
