# 2026-10-14 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 AFM 표의 긴 lot ID 수정을 보고한 어시스턴트 답에서 Insight 블록을 뺀 본문을 이어 붙였다. 단락 2는 VS Code 에 남은 프롬프트 편집기 프로세스를 정리한 보고로, 머리 기호 두 개와 Insight 두 줄을 문장으로 풀어 이었다. 단락 3은 연구 하위 에이전트에게 준 보고서 작성 규칙이다. 1은 수정·검증·남은 의문을 순서대로 보고하는 글, 2는 한 일과 못 한 일을 가르는 글, 3은 권고의 근거 요건을 긴 문장으로 쌓는 격식 지시문이다.

## 단락 1

Fixed and pushed: a long lot ID now shows in full inside its tag, and the Slot column stays where it is on every row. The change is one line in `frontend/app/components/afm/SearchBar.vue`. I checked it in the browser by injecting `XED0504TZ_TE` into one row: that row's Lot tag grew leftwards to 126px, and the Slot column sat at the same position as its neighbours. Normal rows are unchanged. On the missing slot number: the overflow **should not have been hiding it**. The Slot tag is drawn on top of the Lot tag, so its number would still show. An empty Slot tag **more likely means** the office data has a blank `slot_number` for that measurement — possibly the loader failing to read the slot for a lot named like `…_TE`, but I can't confirm that from home. At the office, look at that row again after this fix. If the Slot tag is still blank, **the gap is in the loader's data, not the UI**. I skipped showing a `–` placeholder for a blank slot; say so if you want it.

**문법·구조**: 첫 문장은 `Fixed and pushed:` 두 분사로 시작해 콜론 뒤에 결과를 현재형(`shows`, `stays`)으로 적는다. 한 일은 과거, 그 결과로 지금 성립하는 상태는 현재다. `stays where it is` 는 `where` 명사절이 장소 보어가 된 꼴로 "지금 있는 자리에 그대로"를 뜻한다. 검증 문장은 `I checked it … by injecting …:` 처럼 `by + -ing` 으로 방법을 대고 콜론 뒤에 관찰 결과를 과거형 둘(`grew`, `sat`)로 나열한다. `On the missing slot number:` 는 화제 전환 표지로, 질문 둘 중 둘째로 넘어감을 알린다. `should not have been hiding it` 은 과거 진행의 추론 부정이다. 직접 못 봤으니 `wasn't` 라 단언하지 않고 구조상 불가능함을 말한다. 바로 뒤 `so its number would still show` 의 `would` 도 같은 가정법 거리다. `more likely means` 는 비교급 부사로 두 가설의 확률을 저울질하고, `possibly … but I can't confirm that from home` 이 추측과 그 한계를 한 문장에 담는다. 끝의 두 문장은 명령문(`look at that row again`)과 조건문(`If … , the gap is …`)으로 상대가 사무실에서 할 판정을 미리 짜 준다.

**핵심 표현**: `shows in full` — 잘리지 않고 전부 보인다. / `the gap is in the loader's data, not the UI` — 증상이 남으면 어느 층 문제인지 미리 가르는 판정 기준. / `I skipped showing … ; say so if you want it` — 일부러 안 한 선택을 밝히고 결정을 넘긴다.

**격식 짝**:
- refined (작성): The overflow is unlikely to account for the missing value; the Slot tag is rendered above the Lot tag and would remain visible.
- plain (작성): The overflow shouldn't have hidden it — the Slot tag sits on top, so the number would still be there.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt/8b037e20</sub>

---

## 단락 2

Closed it. There was one leftover prompt-editor process (PID 61845), and it is gone now; your main VS Code window was not touched and is still running. What it was: a `code -w` waiter started yesterday for the same `claude-prompt-b45f5823…` file. Its session had already ended and deleted the file, so it was **orphaned with no window of its own**. Not checked: I couldn't list VS Code's open tabs (the query timed out), so if a dead `claude-prompt-….md` tab is still showing in your main window, close that one **by hand**. `code -w` exits when its wait-marker file is deleted, so removing that marker **lets a stuck waiter go without killing anything**. A VS Code process with only GPU and network helpers and no renderer has no window, which is how I told the waiter apart from your real instance.

**문법·구조**: `Closed it.` 은 주어를 뺀 두 단어 보고다. 결과를 먼저 말하고 설명은 뒤로 미룬다. 둘째 문장은 `There was … , and it is gone now; … was not touched and is still running` 으로 과거(있었다) → 현재(없다) → 과거 수동(건드리지 않았다) → 현재(돌고 있다) 를 한 문장에 묶어 "지운 것"과 "지키지 않은 것"을 대비한다. `What it was:` 와 `Not checked:` 는 명사구 머리말로 단락을 둘로 가르는 장치다. 둘째가 핵심인데, 못 한 일을 보고 중간에 숨기지 않고 제목으로 세운다. `Its session had already ended and deleted the file, so it was orphaned` 는 과거완료 → 과거의 순서로 원인(세션 종료)이 결과(고아)보다 앞섬을 시제로 보인다. `so if … is still showing … , close that one by hand` 는 `so` 뒤에 조건절과 명령문을 넣어 "내가 못 봤으니 네가 확인하라"를 자연스럽게 넘긴다. 마지막 두 문장은 일반 현재(`exits when … is deleted`, `has no window`)로 도구의 성질을 말하고, `which is how I told … apart` 의 `which` 가 앞 문장 전체를 받아 "그 사실이 구별 근거였다"로 닫는다.

**핵심 표현**: `Not checked:` — 확인 못 한 범위를 제목으로 세운다. / `lets a stuck waiter go without killing anything` — 강제 종료 없이 조건만 바꿔 끝낸다. / `told X apart from Y` — 비슷한 둘을 구별했다.

**격식 짝**:
- refined (작성): The open tabs could not be enumerated because the query timed out; any remaining stale tab should therefore be closed manually.
- plain (작성): I couldn't see the tab list (it timed out), so if a dead tab is still there, just close it yourself.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt/c0567c9e</sub>

---

## 단락 3

The answer must respect what the notes record as already shipped, already planned, and already rejected by the owner — do not re-propose rejected ideas, and where existing internal documents already make a recommendation, **build on and assess them rather than repeating them**. Recommendations must be **grounded in data the notes confirm actually exists**, must distinguish what can be built at home on mock data from what needs office data or a loader change, and must **carry through the notes' own evidence grading**: claims the researchers saw only in search-result snippets or abstracts, vendor marketing claims, unverified formulas, and the researchers' own inferences must be **labelled as such rather than stated as established fact**.

**문법·구조**: 두 문장뿐인데 각각이 긴 병렬 구조다. 첫 문장의 `what the notes record as already shipped, already planned, and already rejected` 는 `record A as B` 의 B 자리에 과거분사 셋을 `already` 로 묶어 나열했다. 그 뒤 대시로 끊고 금지(`do not re-propose`)와 조건부 지시(`where … , build on and assess …`)를 `and` 로 이었다. 이 `where` 는 "~한 경우에는"이다. 둘째 문장은 `Recommendations must …, must …, and must …` 로 조동사 `must` 를 세 번 반복해 요건 셋을 같은 무게로 세운다. 둘째 요건 `distinguish what can be built … from what needs …` 는 `distinguish A from B` 의 A·B 가 둘 다 `what` 명사절이다. 콜론 뒤는 셋째 요건의 구체화로, 주어가 넷(`claims …`, `vendor marketing claims`, `unverified formulas`, `the researchers' own inferences`)이고 첫 주어 안에 접촉 관계절(`claims [that] the researchers saw only in …`)이 들어 있다. 동사는 끝에서 `must be labelled as such rather than stated as …` 하나로 넷을 다 받는다. 긴 문장이지만 반복되는 틀(`must`, `rather than`, `as`)이 독자를 잡아 준다.

**핵심 표현**: `respect what the notes record as …` — 기록된 상태를 전제로 삼으라. / `distinguish what … from what …` — 두 범주를 `what` 절로 가른다. / `labelled as such` — 앞에 열거한 종류 그대로 표시하라.

**격식 짝**:
- refined (원문): Claims the researchers saw only in search-result snippets must be labelled as such rather than stated as established fact.
- plain (작성): If they only saw it in a search snippet, say so — don't write it up as if it's settled.

<sub>출처: transcript:[agent-prompt] skewnono-v3-nuxt/466cd9af</sub>

