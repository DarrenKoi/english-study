# 2026-10-21 — 정독

## 단락 1
I pinned the grid rather than reading the chart instance: `useEchart` exposes neither the instance nor a ready hook, and I left `useEchart.ts` unmodified. Both chart components now set `grid.outerBoundsMode: 'none'`, and the bar charts' left margin went from 40 to 56px so a four-digit tick fits. `DayBars.vue` draws both bar charts, so all three charts are covered. In the browser I replayed a MAP608 list with 1,200 measurements on 2026-10-05 and picked that day. The band sits on that day's column in all three charts, and axis labels up to `1,500` fit in the margin.

**문법·구조**: 설계 선택 → 바꾼 것 → 범위 → 검증 → 결과 순서다. 첫 문장은 `rather than + -ing` 로 고르지 않은 길을 옆에 두고, 콜론 뒤에 이유 두 개를 `and` 로 잇는다. 이유 쪽 `exposes neither A nor B` 는 "둘 다 없다"를 한 번에 말하고, `left … unmodified` 는 `leave + 목적어 + 형용사(과거분사)` 로 "건드리지 않은 채 두었다"를 만든다. 두 번째 문장은 현재형 `set` 과 과거형 `went from 40 to 56px` 가 섞이는데, 앞은 지금의 상태, 뒤는 바뀐 사건이라 그렇다. 세 번째 문장의 `so all three charts are covered` 는 결과의 `so` 로 "그래서 범위가 다 찬다"를 닫는다. 네 번째 문장은 장소 부사구 `In the browser` 를 맨 앞에 내세워 검증 환경을 먼저 밝혔다. 마지막 문장은 현재형 `sits`, `fit` 으로 지금 확인된 사실을 단언한다. 과거형으로 쓰면 "그때 한 번 그랬다"로 약해진다.

**핵심 표현**:
- `I pinned X rather than Y-ing` — 두 방법 중 하나를 골랐다고 첫 마디에 밝힌다. 뒤에 콜론으로 이유를 붙인다.
- `went from 40 to 56px` — 수치 변화를 `go from A to B` 로 담백하게 말한다. `was changed from` 보다 짧다.
- `so all three charts are covered` — 고친 범위가 빠짐없다는 것을 결과절 하나로 확인한다.

**격식 짝**:
- refined (작성): Rather than querying the chart instance, which the composable does not expose, I fixed the grid margins explicitly.
- plain (작성): I couldn't get at the chart itself, so I just locked the margins in place.

<sub>출처: transcript:skewnono-afm-usage [assistant] (Round 3 보고)</sub>

---

## 단락 2
The mark's position assumes ECharts keeps the plot at the fixed grid margins with equal-width day columns. That held in every screenshot, but adding `dataZoom` or `containLabel` later would make it drift. The mark is not part of the PNG export, since it sits above the canvas. A 기간 change still resets the legend, because the series themselves change. I did not replay the heat map's narrowed-colour-range case in the browser; the cause is removed from both charts, but only the legend case was reproduced. MAPC01 was not re-opened this round.

**문법·구조**: 원문은 "Limits" 아래 불릿 목록인데, 이어 읽으면 한계 보고의 모범 단락이 된다. 첫 문장은 `assumes (that) …` 로 가정을 명시한다. 두 번째 문장이 그 가정을 받아 과거 `held`(지금까지 확인한 사실)와 가정법 `would make it drift`(조건부 미래 위험)를 `but` 으로 대비시킨다. 세 번째·네 번째 문장은 둘 다 "결과, + 이유" 구조인데, 접속사를 `since` 와 `because` 로 다르게 골랐다. `since` 는 듣는 쪽도 바로 납득할 원인(오버레이니까 당연히 안 찍힌다)에, `because` 는 설명이 필요한 원인(시리즈가 바뀌어서)에 붙었다. 다섯 번째 문장은 세미콜론으로 "안 한 것"과 "한 것의 범위"를 붙인다. 뒤 절의 현재완료 대신 현재형 `is removed` 는 지금의 상태를 말한다. 마지막 문장의 `re-opened` 는 접두사 `re-` 로 "이번 라운드엔 다시 열지 않았다"를 정확히 한다. 여섯 문장 모두 짧고 평서문이라 체크리스트처럼 읽힌다.

**핵심 표현**:
- `That held …, but … would make it drift.` — 지금 맞는 가정과 미래에 깨질 조건을 한 문장에 묶는다.
- `is not part of X, since it sits above Y` — 구현 방식에서 오는 부수 효과를 원인과 함께 말한다.
- `the cause is removed …, but only X was reproduced` — 고친 범위와 확인한 범위를 갈라 말하는 정직한 보고 문형.

**격식 짝**:
- refined (작성): This approach relies on the plot area remaining fixed; introducing zoom controls would invalidate that assumption.
- plain (작성): It works as long as the chart doesn't move around. If we add zoom later, the mark will slide off.

<sub>출처: transcript:skewnono-afm-usage [assistant] (Round 2 보고의 Limits 목록)</sub>

---

## 단락 3
In 2026, SKEWNONO grew from a lookup tool for E-Beam metrology equipment into a service the floor relies on every day, with 60 to 70 users a day. Its device statistics tab is the only way the Inspection & Metrology Efficiency TF can track which parameters each device measures and at how many points. Once every over-measuring recipe was visible, the team cut measurement points and brought total measurement time down by 10%. For inline shift operators, real-time alarms replaced watching CCTV feeds one tool at a time, so an Align Fail now shows up within ten seconds instead of four to five minutes. AFM data has since moved onto the same platform, which brings SKEWNONO one step closer to a single Metrology Workspace. Next, we will finish standardizing device descriptions so the rule checks stop wavering, and extend support to VeritySEM, Provision and Thickness.

**문법·구조**: 오늘 배치의 한국어 성과 보고(`skewnono_year_end_report_2026.md`) 요약을 영어로 옮겨 지은 단락이다. 첫 문장의 `grew from A into B` 는 "A 에서 B 로 성장했다"는 변화 서사 틀이다. `a service the floor relies on` 은 관계대명사 `that` 을 생략한 목적격 관계절이다. 두 번째 문장은 현재형 `is` 로 지금도 유효한 사실을 말하고, 간접의문문 `which parameters … and at how many points` 를 `track` 의 목적어로 쓴다. 세 번째 문장은 `Once` 절(과거)로 원인을 깔고 주절에서 동사 두 개(`cut`, `brought down`)로 결과를 잇는다. 네 번째 문장의 `replaced watching …` 은 동명사구가 `replace` 의 목적어가 된 경우다. 끝의 `instead of` 가 이전과 지금을 대비한다. 다섯 번째 문장의 `has since moved` 는 현재완료에 `since`(그 이후로)를 끼워 넣어 "그 뒤로 옮겨 왔다"를 만든다. 이어지는 `, which …` 는 앞 절 전체를 받는 계속적 용법이다. 마지막 문장만 `will` 미래로 이후 과제를 연다. 과거 성과 → 현재 상태 → 앞으로의 순서다.

**핵심 표현**:
- `grew from A into B` — 한 해의 변화를 한 문장으로 요약하는 성과 보고의 첫 문장 틀.
- `a service the floor relies on every day` — `the floor` 는 생산 현장(현업)을 가리킨다. 관계절로 "현업이 매일 기대는"을 붙인다.
- `brings X one step closer to Y` — 장기 목표에 다가섰다는 걸 과장 없이 말한다.

**격식 짝**:
- refined (작성): Real-time alarms reduced Align Fail detection time from up to five minutes to under ten seconds.
- plain (작성): Operators used to spot an Align Fail after four or five minutes. Now they see it in ten seconds.

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/progress_report/skewnono_year_end_report_2026.md 내용을 바탕으로</sub>
