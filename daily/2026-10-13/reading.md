# 2026-10-13 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 skewnono 세션에서 하위 에이전트 조사가 돌아온 뒤 어시스턴트가 Q3 추천을 고쳐 말한 대목으로, 목록 두 항목을 머리 기호만 떼고 이어 붙였다. 단락 2는 같은 세션의 첫 답에서 "예전 결정과 부딪힌다"는 절과 추천 문단을 붙였고 사이의 비교표는 뺐다. 단락 3은 skewvoir 현황 노트의 머리말이다. 1은 사실 둘로 선택지를 좁히는 글, 2는 상대의 과거 결정을 근거로 범위를 줄여 권하는 글, 3은 조사 방법과 그 한계를 먼저 밝히는 글이다.

## 단락 1

**No step field in measurement history.** The only step-to-recipe mapping (`oper_id`, `oper_desc`) is in the device-statistics plan-step data, keyed by device lot, CD-SEM only. So "pick a process step" (option c) **can't be built directly**; the engineer picks recipes. **No endpoint summarises CD per recipe.** Today the recipe trend is built in the browser: `/meas-hist` for the runs, then `POST /msr-files` (up to 200 runs) for the values. That is two rate-limited requests per recipe, with a heavy second one. My recommendation stays (a), but the recipe section **is where the real cost of this page is**, and Round 2 will ask whether to cap the list or add a summary endpoint.

**문법·구조**: 두 사실이 같은 꼴로 시작한다. `No step field …`, `No endpoint summarises …` 처럼 `No + 명사` 를 주어로 세우면 `There is no …` 보다 단호하고 짧다. 첫째는 동사조차 없는 명사구 문장인데 제목 구실을 하므로 그대로 둔다. 둘째 문장의 `keyed by device lot, CD-SEM only` 는 과거분사구와 형용사구를 쉼표로 덧붙인 것으로, 관계절 둘(`which is keyed by …`, `which exists only for …`)을 줄였다. `So … can't be built directly; the engineer picks recipes` 는 세미콜론 앞에서 안 되는 것을 수동태로, 뒤에서 대신 일어나는 일을 능동태로 적는다. 만드는 사람은 중요하지 않고 고르는 사람은 중요하기 때문이다. `Today the recipe trend is built in the browser:` 뒤의 콜론은 절차를 풀고, `A for the runs, then B for the values` 가 `for` 로 각 요청의 목적을 단다. `That is two rate-limited requests per recipe, with a heavy second one` 의 `That` 은 앞 문장 전체를 받아 비용으로 환산한다. 마지막 문장은 `stays` 현재형으로 입장을 유지하고 `but` 뒤에서 대가를 인정한 다음 `will ask` 로 다음 라운드를 예고한다. 현재 → 현재 → 미래로 시제가 움직인다.

**핵심 표현**: `can't be built directly` — "안 된다"가 아니라 "곧바로는 못 만든다". `directly` 한 단어가 우회로를 남긴다. / `with a heavy second one` — `with` 부대 구문으로 "그중 둘째가 무겁다"를 덧붙인다. / `My recommendation stays (a), but …` — 새 사실이 나와도 추천을 바꾸지 않을 때의 틀.

**격식 짝**:
- refined (작성): The recommendation is unchanged; however, the recipe section accounts for most of this page's cost.
- plain (작성): I'd still go with (a), but the recipe part is the expensive bit.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>

---

## 단락 2

`docs/research/2026-10-05-page-value-brainstorm.md` §4 lists "홈 브리핑, 관심 장비 목록" **under things not to build**. **The reason given was that** it adds a collection job and Redis state, and makes the home page depend on many features. "He can see the issue right away when he visits" is **that same** home briefing if the home page itself computes and shows the issues. I recommend A, then B for exactly the two cards your examples describe (issues on my tools, CD summary for my recipes). A already delivers "sees it right away" as **one click instead of zero**, and it **doesn't reopen the rejected design**.

**문법·구조**: 첫 세 문장은 주어가 문서, 이유, 사용자의 말 순으로 바뀐다. 어시스턴트 자신(`I`)은 넷째 문장에야 나온다. 반대 근거를 "내 생각"이 아니라 "당신이 남긴 기록"으로 세우는 배치다. `The reason given was that …` 은 과거분사 `given` 이 `reason` 을 뒤에서 꾸미는 꼴로 "(그때) 제시된 이유는"이다. 누가 말했는지 밝히지 않고도 과거의 판단을 인용한다. `was` 는 과거인데 `that` 절 안의 `adds`, `makes` 는 현재형이다. 그 이유가 지금도 참이기 때문에 시제를 맞추지 않았다. 셋째 문장은 인용문 전체가 주어이고 `if` 절이 조건을 건다. 사용자의 요구가 언제 기각된 안과 같아지는지를 조건 하나로 좁혔다. `the home page itself` 의 재귀 강조는 "다른 페이지가 아니라 바로 홈이"를 뜻한다. `I recommend A, then B for exactly the two cards your examples describe` 에서 `then` 은 순서이고 `your examples describe` 는 관계사가 빠진 접촉절이다.

**핵심 표현**: `under things not to build` — "만들지 않을 것 항목 아래에". `to` 부정사의 부정은 `not to`. / `that same home briefing` — `that same` 은 "바로 그"로, 새 요구가 옛 안과 같다는 것을 지시어 하나로 잇는다. / `for exactly the two cards your examples describe` — `exactly` 가 범위를 더 넓히지 않겠다는 약속이 된다.

**격식 짝**:
- refined (작성): Option A satisfies the requirement at the cost of a single click, without revisiting the earlier decision.
- plain (작성): With A you're one click away, and we don't have to argue about the old decision again.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>

---

## 단락 3

How this was verified: I read directly `SearchLanding.vue`, `Workspace.vue`, `workspace/LeftRail.vue`, `views/Dashboard.vue`, `views/PositionStack.vue`, `views/Fdc.vue`, `useSkewvoirWorkspace.ts`, `useSkewvoirRoute.ts`, `UA/types.ts`, `UA/routeQuery.ts`, the three `contracts.py`, and `docs/issues/skewvoir/analysis-coverage-gap-analysis.md`. The remaining ~20k lines **were read by** four delegated read-only passes; I **spot-checked their load-bearing claims** by grep (ProvenanceDrawer unmounted, no caller for bulk download, no crosshair in skewvoir, `anomalyCfg` wiring, FDC key spellings, `focusError` consumers, no view beacon). Line numbers from the delegated passes **were not individually re-opened**. Nothing was run in a browser, so **all behaviour claims are from reading code**. Labels: **(a)** = exists today, **(b)** = data exists but is unused, **(c)** = inferred gap/opportunity. Anything under "Inferences" is inference, not fact.

**문법·구조**: 태가 근거의 등급을 가른다. 직접 한 일은 능동(`I read directly …`, `I spot-checked …`)이고, 남에게 맡겼거나 하지 않은 일은 수동(`were read by four delegated passes`, `were not individually re-opened`, `Nothing was run`)이다. 읽는 사람은 `I` 가 주어인 문장만 저자가 보증한다고 알게 된다. `I read directly A, B, C` 는 부사가 동사와 목적어 사이에 끼었다. 보통은 피하는 어순이지만 목적어가 열두 개라 `directly` 를 끝에 두면 너무 멀어진다. 둘째 문장의 세미콜론은 "위임했다"와 "그래서 내가 한 보완"을 한 호흡으로 묶고, 괄호 안 일곱 항목은 동사 없는 명사구로 무엇을 확인했는지 나열한다. `Nothing was run in a browser, so …` 는 부정 주어 `Nothing` 으로 예외가 없음을 밝히고 `so` 로 독자가 끌어낼 결론까지 대신 적는다. 마지막 `Anything under "Inferences" is inference, not fact` 는 `A, not B` 대조로 문서 전체에 걸리는 읽는 법을 한 줄로 정한다.

**핵심 표현**: `spot-checked their load-bearing claims` — 전부가 아니라 결론을 떠받치는 주장만 골라 확인했다. / `were not individually re-opened` — "하나하나 다시 열어 보지는 않았다". `individually` 가 한계의 크기를 정한다. / `inference, not fact` — 추론과 사실의 구분.

**격식 짝**:
- refined (작성): No runtime verification was performed; all statements about behaviour derive from static reading of the source.
- plain (작성): I didn't actually run any of it. Everything here is from reading the code.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md</sub>
