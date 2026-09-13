# 2026-09-14 — 정독

## 단락 1

The measuring tool's FTP server caps concurrent sessions and engineers use their own tools against the same equipment, so a session is a shared, scarce resource. Two things make us open more of them than we need: the browser re-requests a slow image at 2.5s and 5s (utils/imageRetry.ts), and two people can open the same MSR at once. Both arrive as concurrent requests for the SAME cache key, and each used to open its own session. This module only provides the mutual exclusion. The dedup comes from the caller re-reading the cache while holding the gate. Without that re-read the waiters would simply take turns visiting the tool, which is slower and no lighter.

**문법·구조**: 첫 문장은 `A and B, so C` 로 두 사실을 먼저 깔고 `so` 뒤에 결론을 둔다. 결론이 `a shared, scarce resource` 라는 명사구 하나라서 이후 문단 전체의 전제가 된다. 두 번째 문장은 `Two things make us …:` 로 개수를 예고하고 콜론 뒤에 그 둘을 `and` 로 나열한다 — 독자가 세면서 읽게 만드는 장치다. 세 번째 문장의 `each used to open its own session` 은 `used to` 로 "예전 동작"을 표시해, 지금은 고쳤음을 말하지 않고도 암시한다. 네 번째와 다섯 번째 문장은 `only … / … comes from …` 으로 책임을 둘로 쪼갠다. 마지막 문장은 `Without that re-read` 라는 조건구 + `would` 로 반사실을 그린다. 재읽기가 없다면 어떻게 되는지를 단정하지 않고 가정법으로 보여 주는 설계 문서의 정형 시제다.

**핵심 표현**: `a shared, scarce resource` — 형용사 둘을 쉼표로 나란히 놓아 각각 독립된 근거로 읽히게 한다. / `open more of them than we need` — `more … than we need` 로 낭비를 수치 없이 표현. / `take turns visiting the tool` — `take turns + 동명사` 는 "번갈아 ~하다"이며, 여기서는 직렬화가 왜 해결이 아닌지의 근거가 된다.

**격식 짝**: (작성)
- refined: Absent that second cache read, the waiters would merely serialise their visits to the tool, gaining nothing in load.
- plain: If we don't re-check the cache, they just line up and each hits the tool anyway.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md</sub>

---

## 단락 2

Deliberately per-process and lock-free of any store: with one worker it is exact, and with several the duplication drops from unbounded to the worker count, which the shared MinIO cache already absorbs. A Redis lease would add TTLs, polling and failure modes to buy that last factor. There is no timeout. A waiter blocking IS the intent — the alternative is giving up and going to the tool, which is the load this exists to prevent — and the fetch it waits on is already bounded by ftp_timeout / host_timeout. The count is what lets the entry be removed safely: dropping it while someone still waits would hand the next arrival a different lock object and silently lose the exclusion.

**문법·구조**: 첫 문장은 주어와 동사가 없는 조각 문장 `Deliberately per-process …:` 으로 시작한다. docstring 에서 "이건 선택이다"를 먼저 선언하고 콜론 뒤에 근거를 다는 형식이다. 그 근거는 `with one worker … , and with several …` 의 대구로, 조건을 전치사구로만 세워 문장을 짧게 유지한다. `drops from unbounded to the worker count` 는 `from A to B` 로 개선 폭을 양 끝만 찍어 보여 준다. 세 번째 문장 `There is no timeout.` 은 세 단어짜리 단문이다. 앞뒤 긴 문장 사이에서 리듬을 끊어 "여기 주목"을 만든다. 네 번째 문장은 대시 두 개로 삽입절을 끼워 넣었는데, 삽입절 안에 다시 관계절(`which is the load this exists to prevent`)이 있어 3층 구조다. 그래도 주절 `A waiter blocking IS the intent … and the fetch … is already bounded` 가 대시 바깥에서 이어지므로 길을 잃지 않는다. 마지막 문장의 `The count is what lets …` 는 분열문으로 "이 값이 핵심"임을 집어 올린다.

**핵심 표현**: `which the shared MinIO cache already absorbs` — 남은 중복을 다른 층이 "흡수한다". `absorb` 는 완전 제거가 아니라 감당한다는 뜻. / `to buy that last factor` — 마지막 한 배수를 얻자고 복잡도를 지불한다는 은유. / `hand the next arrival a different lock object` — 다음 도착자를 의인화해 버그 시나리오를 그린다.

**격식 짝**: (작성)
- refined: The absence of a timeout is intentional; a blocked waiter is precisely the behaviour this gate is designed to produce.
- plain: There's no timeout on purpose — waiting is the whole point.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md</sub>

---

## 단락 3

The 시스템 상태 card and the 데이터 반출 금지 notice now sit inside one 2-column grid, fixed at 600px on large screens and anchored to the right. Both cells share the same width and stretch to the same height. I removed the card's own min/max-width clamp, since the grid cell now sizes it. Verified in Chrome at desktop width. Collapsed and expanded states both keep the two cards aligned. Typecheck passes, and lint shows only two pre-existing warnings in an unrelated skewvoir file. The earlier imbalance came from two cards each carrying their own sizing rule: one in scoped CSS, one in Tailwind utilities. Moving the width decision to a parent grid means neither card needs to know how wide it is, and the grid gives equal heights for free.

**문법·구조**: 작업 완료 보고의 전형이다. 앞 세 문장은 "무엇이 바뀌었나"를 현재시제(`now sit`, `share`, `stretch`)로 쓴다. 완료한 변경은 과거가 아니라 현재 상태로 적는 것이 보고문의 관례다. `fixed at 600px … and anchored to the right` 는 과거분사 둘을 나란히 붙여 문장을 늘리지 않고 속성을 추가한다. `Verified in Chrome at desktop width.` 는 주어를 뺀 조각 문장으로, 체크리스트처럼 읽히게 한 것이다. 원인 진단으로 넘어가는 문장은 `came from two cards each carrying …` 처럼 분사구문으로 원인을 명사에 붙인다. 마지막 문장은 동명사구 `Moving the width decision to a parent grid` 가 주어이고 `means` 뒤에 결과 두 개가 `and` 로 이어진다. 설계 변경의 효과를 "행위 → 결과"로 정리하는 틀이다.

**핵심 표현**: `sit inside one 2-column grid` — 요소가 어디에 "앉아 있는지"를 `sit` 으로. 레이아웃 설명의 기본 동사다. / `since the grid cell now sizes it` — `size` 를 타동사로 써 "크기를 정해 준다". / `each carrying their own sizing rule` — 규칙이 분산돼 있었다는 진단을 한 구로.

**격식 짝**: (작성)
- refined: Delegating width to the parent grid relieves each card of any knowledge of its own dimensions.
- plain: Let the grid decide the width, and the cards don't have to care how big they are.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt (불릿 구조만 풀어 문장 순서대로 이었음)</sub>

