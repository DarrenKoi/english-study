# 2026-10-05 — 정독

> 세 단락 모두 배치 원문이고 skewnono 세션의 영어 보고다. 단락 1은 recipe-status 캐시 검토의 Insight 불릿 셋을 기호만 떼고 이어 붙였다. 단락 2는 사무실 요청서를 쓴 뒤 설계 결정 하나를 확인받는 대목. 도입 문장에 바로 아래 불릿 셋을 이었다. 단락 3은 AFM 시계열 비교 마무리 보고에서 "브라우저 점검이 잡은 버그" 목록과 "Not done" 목록을 이은 것으로, 목록을 여는 첫 문장 끝의 콜론만 마침표로 바꿨다. 순서대로 읽으면 "왜 이 방식이어야 하나", "왜 저 방식은 아닌가", "무엇을 고쳤고 무엇이 남았나".

## 단락 1

A plain "cache on first request" layer barely helps a low-traffic internal page: with a 1-hour lifetime, most opens are the first of that hour and still pay the 10 seconds. Pre-computing on a schedule is what makes it fast for everyone. The cache has to live in Redis, not in process memory. The scheduler runs only in uWSGI worker 1, so anything it computes in memory is invisible to the other three workers. The default open is a small key space: no dates are sent, so the server resolves "latest data date − 14 days", with no device filter. That leaves tool type × fab selection to pre-compute.

**문법·구조**: 여섯 문장이 전부 현재 시제다. 한 일을 보고하는 글이 아니라 시스템이 원래 어떻게 생겼는지를 말하는 글이어서 그렇다. 첫 문장은 콜론 앞이 주장이고 뒤가 근거. `barely` 는 "거의 ~않다"는 준부정어라 `not` 없이도 부정이다. `with a 1-hour lifetime` 은 조건절(`if the lifetime is one hour`) 노릇을 하는 전치사구. `most opens` 는 동사 `open` 을 명사로 돌려 복수로 센 것으로 "페이지를 여는 일"이다. 둘째 문장은 동명사 주어 `Pre-computing on a schedule` 뒤에 `is what makes it fast` 를 놓았다. `It makes it fast` 라고 해도 되지만 `what` 절을 쓰면 "빠르게 만드는 것은 바로 이것"으로 초점이 주어에 모인다. 셋째 문장은 `has to live in Redis, not in process memory` 에서 `not` 으로 틀린 후보를 바로 옆에 세운 꼴. 넷째 문장의 `anything it computes in memory` 는 `that` 이 빠진 관계절이 `anything` 을 꾸민다. 다섯째 문장의 `no dates are sent` 는 수동태. 누가 보내는지는 중요하지 않고 "날짜가 안 온다"는 사실만 필요해서다. 마지막 문장의 `That` 은 앞 문장 전체를 받는다.

**핵심 표현**: `barely helps` — "조금은 돕지만 의미 없는 수준"이라는 수위. `doesn't help` 보다 정확하다. / `is what makes it fast for everyone` — 해법의 핵심이 어디 있는지 짚는 말. / `That leaves … to pre-compute.` — 변수 둘을 지우고 남은 일을 내미는 마지막 줄.

**격식 짝**: (작성)
- refined: A cache populated on first request offers little benefit to a page with so few visitors; given a one-hour lifetime, most visits would be the first within the hour and would incur the full delay.
- plain: Caching on the first hit doesn't really help here. Hardly anyone opens the page, so most people would be the first one that hour and still wait the full 10 seconds.

<sub>출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)</sub>

---

## 단락 2

One design choice to confirm before you send it: the letter asks for a **pre-aggregated table**, not ready-made page results. If the office produced final results per scope (rankings, rates), the office agent would have to copy our formulas, and each fab or date selection would need its own key. Instead the letter asks for counts and sums at the finest grain: one row per day × fab × tool × recipe × lot. Everything the page shows can be summed from that, so one table answers any fab, date range or device selection. All formulas stay in SKEWNONO; the office job is a single group-by with no filters.

**문법·구조**: 첫 문장은 동사 없는 명사구에 콜론을 찍고 `A, not B` 로 결정을 한 줄에 담았다. 단락의 축은 둘째 문장. `If the office produced …, the office agent would have to …, and each … would need …` 는 가정법 과거로, 택하지 않은 안을 "그렇게 했다면 이런 부담이 생긴다"로 그려 보인다. `produced` 가 과거형이지만 과거 일이 아니다. 어제 정독의 `would have read as a control` 은 이미 지나간 선택이라 가정법 과거완료였고 오늘 것은 지금도 유효한 일반론이라 가정법 과거. 셋째 문장은 `Instead` 한 단어로 가정에서 빠져나와 직설법 현재(`asks`)로 돌아온다. 넷째 문장의 주어 `Everything the page shows` 는 `that` 이 빠진 관계절을 품었고 동사는 수동 `can be summed from that`. 누가 더하는지가 아니라 "더해서 나온다"는 가능성이 요점이다. `so one table answers any fab …` 에서는 표가 주어가 되어 `answer` 한다. `any + 단수 명사` 는 "어느 것이 오든". 마지막 문장은 세미콜론 양쪽에 두 저장소의 몫을 나란히 놓았다.

**핵심 표현**: `ready-made page results` — 받아서 바로 쓰는 완성품. 재료 쪽인 `pre-aggregated table` 과 맞선다. / `at the finest grain` — 가장 잘게 쪼갠 단위. 콜론 뒤가 그 정의다. / `one table answers any …` — 무생물 주어 `table` 이 질문에 답한다.

**격식 짝**: (작성)
- refined: Were the office to produce final results for each scope, it would need to replicate our formulas, and every selection would require a dedicated key.
- plain: If the office made the final numbers for us, they'd have to copy our formulas, and we'd need a separate key for every filter combo.

<sub>출처: transcript:skewnono-v3-nuxt (사무실 요청서 보고)</sub>

---

## 단락 3

The browser pass caught five bugs, all fixed before the commit. The 01 chart didn't render at all: Nuxt names the file `<AfmTrendChart>`, not the tag I'd used, and nothing errored. The lower limit line fell below the visible y-axis. The legend listed a recipe that had no line in the chart. In a mixed group, 02 averaged points across recipes and produced nonsense baselines. The repeat ratios disappeared in mixed groups.

Not done: No group I could build contains a STOPPED block, so the "블록 STOPPED" path is covered only by a unit test, not seen in the browser. The spec's μ is a plain mean while σ is outlier-resistant, so in a very small group one big excursion pulls μ far enough to put every point outside the limits. With 6 or more measurements it behaves, as the screenshots show.

**문법·구조**: 두 문단의 시제가 갈린다. 첫 문단은 과거(`didn't render`, `fell`, `listed`, `averaged`, `produced`, `disappeared`). 고쳐서 이제는 없는 버그들이다. 둘째 문단은 현재(`contains`, `is covered`, `pulls`, `behaves`). 지금도 그대로인 한계라서다. 버그를 과거로, 남은 문제를 현재로 적으면 독자는 시제만 보고도 무엇이 끝났는지 안다. 과거 문단 안에 현재형이 하나 있는데 `Nuxt names the file`. Nuxt 의 변하지 않는 규칙이라 과거로 물러나지 않는다. `the tag I'd used` 의 `I'd` 는 `I had` 로, 렌더 실패보다 먼저 쓴 태그라 과거완료다. 버그 문장은 하나같이 화면 요소가 주어(`The 01 chart`, `The lower limit line`, `The legend`). `I found that …` 을 붙이지 않고 증상을 주어에 세웠다. `a recipe that had no line in the chart` 는 관계절. 둘째 문단의 `No group I could build contains …` 는 부정 주어 문장으로 "내가 만들 수 있었던 그룹 가운데 …한 것이 없다"는 뜻이고 `I could build` 가 `that` 없이 `group` 을 꾸민다. `while` 은 대조, `far enough to put` 은 "…할 만큼 멀리". 마지막 문장은 `as the screenshots show` 로 근거를 붙여 닫는다.

**핵심 표현**: `caught five bugs, all fixed before the commit` — 잡은 것과 처리 결과를 한 줄에. / `and nothing errored` — 조용히 실패했다는 말. 찾기 어려웠던 이유이기도 하다. / `With 6 or more measurements it behaves` — 문제가 생기는 범위를 조건으로 좁힌다.

**격식 짝**: (작성)
- refined: Because none of the groups I was able to assemble included a STOPPED block, that path has been exercised solely by a unit test and has not been observed in the browser.
- plain: I couldn't build a group with a STOPPED block, so that path only has a unit test. I haven't actually seen it in the browser.

<sub>출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)</sub>
