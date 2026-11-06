# 2026-11-07 — 정독

## 단락 1

**Keep MAI-UI-8B for now.** Several newer open-weight models score higher on public benchmarks. But MAI-UI-8B already hits 100% on our internal benches, so a straight swap can at best tie. It also wouldn't reduce the number of vLLM instances, which is the real limit on the server. The one change that could pay off is merging roles into fewer instances, and that needs a test on our own saved screens first.

**문법·구조**: 결론을 명령문 `Keep ... for now.` 로 맨 앞에 박는 **BLUF**(bottom line up front) 배치입니다. 둘째 문장이 반대 근거(공개 점수가 더 높다)를 먼저 인정하고, 셋째 문장이 `But` 으로 뒤집습니다. 양보 → 반박 순서라 독자가 품을 반론을 미리 받아 냅니다. 넷째 문장의 `It also wouldn't` 는 가정법 `would` 로 "만약 바꾼다면"이라는 가정을 깔고, `, which is the real limit` 는 쉼표 뒤 **계속적 관계절**이라 앞 절 전체(인스턴스 수)를 받아 보충합니다. 마지막 문장은 `The one change that could pay off is + 동명사` 로 유일한 대안을 주어 자리에 세우고 `and that needs ... first` 로 선행 조건까지 붙여 닫습니다. 시제는 사실은 현재형(`score`, `hits`), 가정은 `can/would/could` 로 깔끔하게 갈립니다.

**핵심 표현**:
- `a straight swap can at best tie` — 바꿔 봐야 기껏 동점. 이미 만점인 상황에서 교체 이득의 상한을 짚습니다.
- `the real limit on the server` — 진짜 병목은 따로 있다. `real` 하나로 앞서 논의한 점수가 핵심이 아니라고 돌려 말합니다.
- `that needs a test on our own saved screens first` — 우리 화면으로 먼저 시험해야 한다. `first` 를 문장 끝에 둬 순서를 강조합니다.

**격식 짝**:
- refined: "We recommend retaining MAI-UI-8B; given its perfect internal score, a direct replacement could at most match current performance." (작성)
- plain: "Let's keep MAI-UI. It's already at 100%, so swapping can only tie." (작성)

<sub>출처: transcript:auto-recipe-creator 59bde568 (MAI-UI 교체 조사 결론 첫 단락)</sub>

---

## 단락 2

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure.

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. You can't test everything — agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case.

**문법·구조**: 첫 문장 `X, not Y` 대구로 원칙을 세우고, 둘째 문장은 세미콜론으로 `Code can change entirely; tests shouldn't.` 를 붙여 대비를 극단까지 밀어붙입니다. `shouldn't` 뒤에는 `change` 가 생략됐습니다. 셋째 문장은 대시 사이에 예시를 끼워 넣은 뒤 주어 `A good test` 에 동사 두 개(`reads like`, `survives`)를 `and` 로 잇습니다. 둘째 문단의 `the public boundary you test at` 은 관계대명사가 빠지고 전치사 `at` 이 끝에 남은 구조입니다. 구어적이지만 기술 글에서 흔합니다. 콜론 뒤 `the interface where ...` 는 앞 명사를 다시 풀어 주는 동격입니다. 셋째 문단의 `No test is written at an unconfirmed seam.` 은 수동태로 행위자를 지워 규칙처럼 들리게 합니다. 마지막 문장은 대시 뒤에서 동명사 주어 `agreeing the seams up front` 가 `is how ...` 와 만나 "~하는 것이 곧 ~하는 방법이다"라는 정의문을 만듭니다.

**핵심 표현**:
- `survives refactors` — 리팩터링을 견딘다. 테스트를 살아 있는 주체로 그립니다.
- `without reaching inside` — 안을 들여다보지(손대지) 않고. `reach inside` 의 손 비유가 "내부 구현 접근"을 쉽게 풀어 줍니다.
- `up front` — 시작 전에 미리. 계획 단계 합의에 단골로 쓰입니다.

**격식 짝**:
- refined: "Agreeing on the test seams in advance concentrates effort on critical paths rather than on every conceivable edge case." (작성)
- plain: "Pick the seams first, so you test what matters, not every little edge case." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (지시서에 실린 tdd 스킬 본문)</sub>

---

## 단락 3

**Why:** 시계열 비교's section "05 측정 소요시간" (shipped 2026-10-08) reports each measurement's duration from the Info block's Start Time and End Time. A 36-point recipe and a 9-point recipe cannot be compared on total duration; seconds per measured point is the figure that says whether the tool is getting slower.
**What:** in that section, alongside the existing duration, show duration ÷ point count for each measurement that has a duration, and the per-recipe median of it next to the existing per-recipe median/min–max. (…) A measurement with no duration keeps its existing reason text; a point count of zero or unknown gives no per-point figure, never a division by zero or Infinity.

**문법·구조**: `Why:` 와 `What:` 라벨로 동기와 요구를 갈라 둡니다. Why 첫 문장은 현재형 `reports` 로 지금 화면이 하는 일을 사실로 깔고, 괄호 `(shipped 2026-10-08)` 로 출시일을 덧붙입니다. 둘째 문장은 수동태 `cannot be compared on total duration` 으로 문제를, 세미콜론 뒤에서 해답 지표를 내놓습니다. `compare A and B on X` 의 `on` 은 "X를 기준으로"입니다. What 은 명령문 `show ...` 가 중심이고, `alongside`, `next to` 같은 위치 전치사로 새 값이 놓일 자리까지 정합니다. `for each measurement that has a duration` 의 제한적 관계절이 계산 대상을 좁힙니다. 마지막 문장은 경계 사례 두 개를 세미콜론으로 잇고 `X, never Y` 로 금지할 결과(0 나누기, Infinity)를 못 박습니다.

**핵심 표현**:
- `cannot be compared on total duration` — 총 소요시간으로는 비교할 수 없다. 비교의 "기준"을 `on` 으로 붙입니다.
- `is the figure that says whether ...` — ~인지를 말해 주는 수치다. 지표를 의인화해 쓸모를 정의합니다.
- `gives no per-point figure, never a division by zero` — 값을 비워 두되 0 나누기는 절대 내지 마라.

**격식 짝**:
- refined: "Because recipes differ in point count, total duration is not a comparable measure; duration per point is the appropriate indicator of tool slowdown." (작성)
- plain: "You can't compare a 36-point recipe with a 9-point one by total time. Divide by the points." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature A 지시서, 중간 생략)</sub>
