# 2026-08-08 — 정독

## 단락 1

The activity sparkline's ECharts option, built without importing echarts. echarts is a runtime dependency of the component, not of this module: the option is a plain object literal and `npm test` runs this file directly under `node --test`, where pulling in echarts would cost a browser-only dependency for no gain. Keeping it out is what makes the bar mapping, the zoom toggle and the tooltip text testable as pure functions. Whether the chart is worth drawing at all: a 30-day window of zeroes is a real answer ("no activity"), and the component renders text for it rather than an empty canvas — which also means no ECharts instance is created for the inactive users in the user table.

**문법·구조**: 첫 문장에 동사가 없습니다. `built without importing echarts` 는 `which is built…` 에서 관계사와 be동사를 지운 과거분사구고, 앞의 명사구가 그대로 주어 겸 제목 노릇을 합니다 — JSDoc 첫 줄의 관례라 일반 산문에 그대로 옮기면 비문이 됩니다. 콜론은 주장(`not of this module`)과 근거를 잇는 자리에 놓였습니다. 그 뒤 `where pulling in echarts would cost…` 는 앞 절 전체를 받는 계속적 용법이고, 가정법 `would` 가 "실제로는 안 했다"를 표시합니다. 세 번째 문장 `Keeping it out is what makes X testable` 은 동명사 주어 + `what` 분열문이라, 여러 이유 중 *이것이* 결정적이라는 강조가 붙습니다. 마지막 `which also means…` 의 which 는 명사가 아니라 앞 절 전체를 받습니다.

**핵심 표현**: `for no gain` — 비용만 지고 얻는 게 없다는 판정을 세 단어로 끝냅니다. `worth drawing at all` — `worth + -ing` 이라 `worth to draw` 는 틀리고, `at all` 이 "그릴지 말지"라는 근본 판단임을 표시합니다. `a real answer` — 빈 데이터가 결함이 아니라 정보라는 재해석이 이 한 마디에 들어 있습니다.

**격식 짝** (작성):
- refined: Excluding it is precisely what renders the bar mapping testable in isolation.
- plain: Leaving it out is the whole reason we can test the bars on their own.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md (`activitySparkline.ts` 의 문서 주석 두 개를 파일 순서대로 이어 붙임)</sub>

---

## 단락 2

Which palette role paints the bars. The page uses two so the reader can tell "my activity" from "the user I expanded" at a glance; both follow the active ECharts theme rather than a hardcoded hex. The zoom slider needs ~20px, which is a third of the flat host. Only the standalone card can spare it — inside the user table the sparkline is a third of a row and the bars would vanish under the slider. The host sits inside `v-if`, so on an empty series it never mounts and no chart is created; useEchart's `elRef` watch initialises against the node when it does appear.

**문법·구조**: 주어가 전부 사물입니다 — the page, the zoom slider, the host. 한국어라면 "우리는 두 색을 쓴다"로 갈 자리를 `The page uses two` 로 돌려서, 사람의 선호가 아니라 화면의 성질처럼 읽히게 만듭니다. `so the reader can tell…` 은 `so that` 의 that 이 생략된 목적절이고, `tell A from B`(A와 B를 구별하다)는 `tell A and B apart` 와 짝을 이루는 관용구입니다. 세미콜론 두 번은 마침표를 찍으면 끊길 두 사실을 한 호흡에 묶습니다. `which is a third of the flat host` 는 앞의 `~20px` 를 받아 수치에 의미를 입히는 계속적 관계절이고, 대시 뒤 `the bars would vanish` 의 가정법이 "안 그랬으니 이런 일은 안 일어난다"를 말합니다. 마지막 `when it does appear` 의 `does` 는 강조 조동사로, "나타나기는 하는 그때"라는 조건의 예외성을 살립니다.

**핵심 표현**: `can spare it` — 20px 을 내줄 여유가 어느 쪽에 있는지로 기능 유무를 가릅니다. `at a glance` — 구별에 드는 시간이 0에 가깝다는 요구 수준을 지정합니다. `rather than a hardcoded hex` — 대안을 명시해 부정이 공허해지지 않게 막습니다.

**격식 짝** (작성):
- refined: Only the standalone card has the vertical headroom to accommodate the slider.
- plain: The big card is the only one with room for the slider.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md (`Sparkline.vue` 의 인라인 주석 세 개)</sub>

---

## 단락 3

The report said the tab came back empty for the M-fabs, but I could not reproduce it at home, and that mattered for where the fix belonged. The mock builds the recipe id from the same index it uses for the step number, so the two orderings coincide by construction and a click-through proves nothing. I pulled the comparator into a unit test instead — it is the only place the difference is observable until this reaches real recipe names. The deeper problem sits in the schema: the parameter map is a plain name-to-count dictionary, so there is no room for the flag the bucket depends on. One command at the office settles which story is true, and whichever way that goes there is a separate defect I can fix from here. A zero that means "we could not determine this" should never be drawn the same way as a zero that means "there is none."

**문법·구조**: 여섯 문장이 모두 "사실 → 그래서 무엇을 했나"로 닫혀, 조사 보고문의 뼈대를 보여줍니다. 시제가 셋 섞여 있는데 각자 일이 있습니다 — 과거(`said`, `could not reproduce`, `pulled`)는 이미 끝난 조사, 현재(`builds`, `sits`, `settles`)는 지금도 참인 코드의 성질, 조동사(`should never be drawn`)는 앞으로의 규범. 넷째 문장 `the flag the bucket depends on` 은 목적격 관계대명사가 생략된 관계절이고, 전치사 `on` 이 문미에 남는 게 자연스러운 자리입니다. 마지막 문장은 `A zero that means X … a zero that means Y` 로 같은 틀을 두 번 써서 대비를 만들고, 수동태 `be drawn` 이 그리는 주체를 지워 규칙처럼 들리게 합니다.

**핵심 표현**: `coincide by construction` — 검증이 왜 무의미했는지를 한 구로 끝냅니다. `whichever way that goes` — 미결 항목 옆에 확정 항목을 붙일 때의 접속 장치. `there is no room for` — 원인이 우리 코드가 아니라 상류 스키마에 있음을 가리킵니다.

**격식 짝** (작성):
- refined: The discrepancy has a material bearing on where the remedy belongs.
- plain: The mismatch matters, because it changes where the fix goes.

<sub>출처: 모범 단락(작성) — 오늘 배치의 조사 내용과 핵심 표현으로 구성</sub>
