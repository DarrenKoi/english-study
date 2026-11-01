# 2026-11-02 — 정독

## 단락 1

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure. A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals. Test only at pre-agreed seams. Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. You can't test everything — agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case.

**문법·구조**: 전부 현재 시제입니다. 규칙과 정의를 말하는 글이라 시간에 묶이지 않는 일반 진리로 씁니다. 첫 문장의 "A, not B"는 대조를 가장 짧게 세우는 틀이고, 둘째 문장 "Code can change entirely; tests shouldn't."는 세미콜론으로 두 절을 맞세워 리듬을 만듭니다(shouldn't 뒤에 change 생략). "the public boundary you test at"과 "the interface where you observe…"는 각각 관계대명사 생략 + 전치사 후치, where 관계부사입니다. "No test is written at an unconfirmed seam."은 수동태로 행위자를 지워 규칙처럼 들리게 합니다. 마지막 문장은 동명사 주어(agreeing the seams up front)가 "is how …"로 이어지는 구조로, 방법을 명사절로 받아냅니다.

**핵심 표현**:
- reads like a specification — 글처럼 "읽힌다". 테스트 이름이 곧 사양서 문장이 돼야 한다는 기준.
- reaching inside — 내부로 손을 뻗다. 테스트가 구현 세부를 들여다보는 행위를 몸짓으로 그립니다.
- up front — 미리, 시작 단계에서. 회의·문서 양쪽에서 흔합니다.

**격식 짝**:
- refined: Testing effort should be concentrated on critical paths rather than distributed across every edge case. (작성)
- plain: Agree on the seams first, so you test what matters instead of every little edge case. (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af (서브에이전트에 넘긴 tdd 스킬 문서)</sub>

---

## 단락 2

Efficiency review of the AFM detail page — read-only, nothing measured; costs are counts from the code. Server caps a profile at 65,536 samples, so that is the client's worst case, not 260k. Thumbnails load the full-size image through the rate-limited API. `image.url` is `/api/afm/files/…/images/<type>/<name>`, and `afm` is not in `_EXEMPT_BLUEPRINTS`. A popup grid at the 130px density shows roughly 80 tiles, so one open can exceed 50 requests / 5 s. I did not observe a 429. Cheaper: exempt the image-file routes (as `msr_image` is) and set `Cache-Control` on `backend/afm/routes.py:275`, which sends none.

**문법·구조**: 첫 문장은 동사 없는 제목형 문장에 대시로 조건(read-only, nothing measured)을 붙여 신뢰 범위를 먼저 밝힙니다. 이어지는 "X, so Y" 두 번은 근거 → 결론 순서를 고정해 독자가 계산 과정을 따라오게 합니다. "one open can exceed …"의 can 은 가능성, 바로 뒤 "I did not observe a 429."는 과거 시제 관측 보고입니다. 추정과 관측을 서로 다른 문장, 서로 다른 시제로 나눠 놓은 점이 이 단락의 핵심입니다. 마지막 "(as `msr_image` is)"는 is 뒤에 exempt 가 생략된 비교절이고, ", which sends none"은 계속적 용법 관계절로 현재 상태를 덧붙입니다.

**핵심 표현**:
- costs are counts from the code — 비용은 측정이 아니라 코드에서 센 숫자라는 단서. 보고의 근거 종류를 밝히는 습관.
- that is the worst case, not X — 상한을 바로잡는 틀.
- Cheaper: — 대안을 한 단어 라벨로 여는 메모체.

**격식 짝**:
- refined: Although this scenario could exceed the rate limit, no 429 responses have been observed to date. (작성)
- plain: It could hit the rate limit, but I haven't actually seen a 429. (작성)

<sub>출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 서브에이전트 보고, 도입 + 1번 지적)</sub>

---

## 단락 3

AFM stores raw height samples per point (profile X/Y/Z float arrays), the richest data the AFM section has, and today they are only viewed one point of one measurement at a time on 측정 상세. An engineer comparing wafers wants to see whether the profile SHAPE at a site changed, which a summary number such as a step height cannot show. Only profiles that are comparable are drawn together: same recipe (existing rule), same point name, 1D, and the SAME unit. Anything else is listed under the chart with its reason (no profile for this point, 2D grid, different unit, fetch failed) — never silently dropped, never unit-converted, never resampled onto another's X grid.

**문법·구조**: 첫 문장의 "the richest data the AFM section has"는 앞 명사구와 같은 대상을 다시 가리키는 동격 구문입니다. "are only viewed"는 수동태로 데이터가 주인공이 되게 합니다. 둘째 문장 "comparing wafers"는 현재분사 후치 수식, "whether … changed"는 명사절, ", which … cannot show"는 앞 절 전체를 받는 계속적 관계절입니다. 이 두 문장이 "왜"를, 뒤 두 문장이 "무엇을"을 맡습니다. 뒤쪽은 콜론으로 조건 목록을 열고, 대시 뒤 "never …, never …, never …" 3연속 부정 과거분사로 금지 사항을 못 박습니다. 반복이 곧 강조입니다.

**핵심 표현**:
- one point of one measurement at a time — 한 번에 하나씩만 볼 수 있는 현재의 한계를 구체적으로.
- which a summary number cannot show — 요약값의 한계를 관계절 하나로.
- never silently dropped — 조용히 빠뜨리지 말 것. 데이터 화면 사양의 단골 문구.

**격식 짝**:
- refined: Profiles that fail the comparability criteria are listed beneath the chart together with the reason for their exclusion. (작성)
- plain: If a profile can't be compared, show it under the chart and say why. (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af (서브에이전트 브리프의 Why 절 + Scope 2번)</sub>
