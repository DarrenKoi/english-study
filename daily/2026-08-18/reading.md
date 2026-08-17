# 2026-08-18 — 정독

## 단락 1

An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus marks the visible tab as seen, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion while the pane is unseen. With no foreground client, a new completion in the globally active tab is treated as seen while completions in background tabs still become `done`.

**문법·구조**: 상태 기계 하나를 산문으로 옮긴 단락이다. 전체가 현재시제 단순형(`reports`, `becomes`, `is created`)으로만 굴러가는데, 이게 규칙 서술의 기본 시제다. 과거형을 쓰면 관찰 기록이 되고 `will` 을 쓰면 예측이 되어, "언제나 이렇게 동작한다"는 규범의 힘이 빠진다.

첫 문장의 `An agent that first opens at its prompt` — 부정관사 `An` 이 특정 에이전트가 아니라 이 부류 전체를 대표한다. 그 뒤 `including in a background pane` 은 전치사구를 목적어로 받은 `including` 으로, 예외처럼 보이는 경우를 규칙 안으로 끌어들인다. 조건을 새 문장으로 떼지 않고 꼬리에 매단 덕분에 규칙 하나가 한 문장에 닫힌다.

둘째부터 넷째 문장은 조건절의 세 가지 얼굴을 나란히 보여준다. `After a working or blocked agent completes …`(시간), `when it completes in the active tab while …`(조건 안의 동시 조건), `If the foreground client is explicitly unfocused …`(가정). 셋 다 같은 사실의 다른 분기인데 접속사를 바꿔 리듬을 살렸다. 특히 셋째 문장의 `when … while …` 이중 종속은 "완료 시점"과 "그때의 포커스 상태"를 층으로 쌓는다 — 둘을 `and` 로 이으면 두 조건의 위계가 사라진다.

다섯째 문장의 주어가 이 단락의 백미다. `Focusing a pane, switching to its tab, or regaining outer terminal focus marks …` — 동명사 세 개를 병렬로 세워 단수 동사 `marks` 로 받는다. 세 행위가 **같은 하나의 효과**를 낸다는 뜻이 문법으로 표현된 자리다. 여기서 `mark A as seen` 은 상태를 부여하는 구문이라, 뒤이어 결과절 `so done becomes idle` 이 자연스럽게 붙는다.

여섯째 문장은 능동과 수동을 한 문장에서 갈아 쓴다. 앞절 `Switching away does not turn …` 은 능동으로 "이 행위는 그 일을 하지 않는다"를 부정하고, 세미콜론 뒤 `done is created by a later completion` 은 수동으로 초점을 상태 쪽에 옮긴 다음 `by` 로 진짜 원인을 지목한다. 흔한 오해를 지우고 정답을 제시하는 두 동작이 한 문장에 들어간 셈이다. 마지막 문장의 `is treated as seen` 역시 수동인데, 행위자를 감추려는 게 아니라 **행위자가 없다는 것**이 조건(`With no foreground client`)이기 때문이다.

**핵심 표현**: `its result is considered seen` — 결과를 사용자가 이미 확인한 것으로 간주한다(알림 설계의 핵심 어휘). `marks the visible tab as seen` — 상태를 부여하는 `mark A as B` 구문. `with no foreground client` — 조건을 전치사구로 압축해 문두에 두는 격식 어법.

**격식 짝**:
- refined: *A new completion in the globally active tab is treated as seen.* (작성)
- plain: *If it finishes on the tab you're already looking at, it counts as read.* (작성)
- refined: *Switching away does not turn an existing `idle` status into `done`.* (작성)
- plain: *Clicking off won't flip something that was already idle.* (작성)

<sub>출처: transcript:auto-recipe-creator/687a4050 (herdr 스킬 문서)</sub>

---

## 단락 2

DESIGN.md's defining rule is "**data values always get full ink; muted ink is for labels only**" and the `--sk-ink-muted` entry adds "*never data values*". The drift-sigma number is the data value the user came to read, but `TONE.ok` repaints it `--sk-ink-muted`, muting the majority of cells. The component's own comment justifies the *fill* (ok stays unfilled), but the muted *text* is not covered by that rationale — the two `warning`/`bad` branches keep status ink only on the fill while `ok` demotes the value itself. Overlay rule applies: "where the code and DESIGN.md disagree, the code is what gets corrected." Fix: keep `ok` unfilled but leave the value at full `--sk-ink`.

**문법·구조**: 규칙 인용 → 위반 지목 → 상대 논거 인정 → 판정 근거 → 조치. 리뷰 한 편의 다섯 단계가 다섯 문장에 하나씩 배정되어 있다. 문장 수와 논증 단계가 일치하니 어디를 반박할지 상대가 곧바로 찾을 수 있다.

첫 문장은 규칙을 **직접 인용**으로 주어 자리 옆에 앉힌다(`DESIGN.md's defining rule is "…"`). 요약하지 않은 게 요령이다. 인용해 두면 판정이 해석 다툼으로 흐르지 않는다. 이어 `the entry adds "…"` 의 `adds` 가 두 근거를 더하는 동사인데, `also says` 보다 짧고 "두 번째 문서가 첫 문서를 좁혀 준다"는 관계까지 담는다.

둘째 문장의 `the data value the user came to read` — 관계대명사가 생략된 목적격 관계절이다(`the value (that) the user came to read`). `came to read` 는 "읽으려고 온"이라는 목적이 과거 동작에 실려서, 그 숫자가 이 화면의 존재 이유임을 한 구로 세운다. 뒤의 `muting the majority of cells` 는 분사구문으로 결과를 덧붙인 것 — `and it mutes …` 로 풀면 두 절이 대등해져 부수 결과라는 성격이 사라진다.

셋째 문장이 논증의 축이다. `The component's own comment justifies the fill …, but the muted text is not covered by that rationale`. 상대 근거를 먼저 인정하고(`justifies`), 그 근거가 **닿는 범위**를 잘라 낸다(`not covered by that rationale`). 이탤릭 `fill` 과 `text` 가 대조축을 시각적으로 고정하는데, 두 단어만 기울인 절제가 핵심이다. 대시 뒤 `while ok demotes the value itself` 의 `while` 은 시간이 아니라 대조이며, 재귀대명사 `itself` 가 "채움이 아니라 값 자체"라는 구분을 못 박는다.

넷째 문장은 판정 규칙을 인용으로 불러오고(`Overlay rule applies: "…"`), 그 인용문 안에서 `the code is what gets corrected` 라는 분열문(`what` 절)이 고칠 대상을 하나로 지정한다. `the code gets corrected` 로 써도 뜻은 같지만, `what` 을 세우면 "문서가 아니라 코드"라는 선택이 문장 구조에 드러난다. 마지막 `Fix:` 는 명령형 조치를 콜론 뒤에 붙인 리뷰 관용 서식이라 주어를 아예 생략한다.

**핵심 표현**: `not covered by that rationale` — 근거가 있다는 건 인정하되 그 근거가 이 부분까지는 못 미친다. `demote the value itself` — 값을 한 등급 아래 서식으로 강등하다. `the code is what gets corrected` — 문서와 코드가 어긋날 때 어느 쪽을 손대는지 정하는 분열문.

**격식 짝**:
- refined: *The muted text is not covered by that rationale.* (작성)
- plain: *That comment explains the fill, not the grey text.* (작성)
- refined: *Where the code and the design document disagree, the code is what gets corrected.* (작성)
- plain: *If the code and the doc clash, fix the code.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md</sub>

---

## 단락 3

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals. **Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. You can't test everything — agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case.

**문법·구조**: 용어를 정의하고 그 정의에서 규칙을 끌어내는 짧은 교본 단락이다. 정의문 → 원칙 → 명령 → 절차 → 금지 → 이유의 순서인데, 마지막 "이유"가 있어 규칙이 계명이 아니라 설명으로 읽힌다.

첫 문장의 콜론 용법을 보자. `A seam is the public boundary you test at: the interface where you observe behavior …` — 콜론 앞에서 한 번 정의하고 뒤에서 같은 것을 다른 말로 다시 정의한다. 두 번째 정의가 첫 번째를 대체하는 게 아니라 **관찰 가능성**이라는 판별 기준을 덧붙인다. `the boundary you test at` 은 전치사가 관계절 끝에 남은 구조로(`the boundary at which you test`의 구어형), 기술 문서에서는 이 후치형이 오히려 표준이다. `without reaching inside` 의 `reach inside`(안으로 손을 뻗다)는 캡슐화 위반을 몸짓으로 옮긴 은유다.

둘째 문장 `Tests live at seams, never against internals.` 는 동사가 하나뿐인데 두 주장을 담는다. `never against internals` 는 `they live` 를 생략한 채 전치사만 갈아 낀 대조구다. `at`(경계 지점) 과 `against`(맞대고 겨루는)의 전치사 대비가 논지 전체를 지탱한다 — 어휘를 바꾸지 않고 전치사만으로 옳은 위치와 틀린 위치를 갈랐다.

셋째~다섯째 문장은 태를 갈아 쓰며 강도를 조절한다. `Test only at pre-agreed seams.` 는 명령형이고, `Before writing any test, write down …` 은 동명사 부사절을 앞세운 절차 지시다. 그런데 다섯째 문장은 갑자기 수동이다 — `No test is written at an unconfirmed seam.` 명령형(`Don't write a test at …`)으로 쓸 수도 있었지만, 수동으로 두면 지시가 아니라 **성립하지 않는 사태**로 읽힌다. 규칙을 사람의 의지에서 떼어 내 조건 자체로 만드는 어법이다.

마지막 문장의 `agreeing the seams up front is how testing effort lands on …` 은 `X is how Y happens` 구문으로, 수단과 결과를 등호로 묶는다. `how` 절이 보어 자리에 오면 "이것이 그 일이 일어나는 방식이다"가 되어 인과 주장이 조용해진다 — `agreeing the seams makes the effort land` 보다 단정이 덜하면서 설득력은 같다. 동사 `land on` 도 눈여겨볼 만하다. 노력이 여기저기 흩어지지 않고 목표 지점에 **떨어져 앉는다**는 그림이 `focus on` 보다 구체적이다.

**핵심 표현**: `the boundary you test at` — 관찰 지점으로서의 경계(전치사 후치가 표준). `never against internals` — 동사를 생략하고 전치사만 갈아 만든 대조. `X is how Y lands on Z` — 노력이 어디에 떨어질지를 정하는 수단·결과 구문.

**격식 짝**:
- refined: *No test is written at an unconfirmed seam.* (작성)
- plain: *Don't write a test until we've agreed where it goes.* (작성)
- refined: *Agreeing the seams up front is how testing effort lands on the critical paths.* (작성)
- plain: *Settle the seams first and you won't waste tests on edge cases.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt/bd4caa93 (`tdd` 스킬 문서)</sub>
