# 2026-09-20 — 정독

> repo 문서는 오늘도 한국어 본문이라 인용할 영어 단락이 없다. 단락 1·2는 transcript 의 `[assistant]` 영어, 단락 3은 세션에 주입된 herdr 스킬 문서다. 셋 다 원문 그대로이며 굵은 글씨와 불릿 기호만 풀어 한 단락으로 이었다. 앞의 둘은 채팅 보고체, 셋째는 레퍼런스 문서체라 같은 현재 시제가 어떻게 다르게 쓰이는지 견줘 읽으면 좋다.

## 단락 1

`DESIGN.md` now works as a handoff: it has a starter section teammates can copy from without Tailwind, NuxtUI or our `Sk*` components. I built a page from only what that section contains and screenshotted it in light and dark; both match the app. `npm run lint:md` is clean, and the change is pushed to `main` as `79deed7d`. Only `DESIGN.md` changed. The doc couldn't be built from before. Teammate apps are standalone Vite builds (`apps/<slug>/`) or separate servers, and both contributor guides tell them to carry token values over from `DESIGN.md`. But `DESIGN.md` gave no value for seven tokens (`--sk-ok-soft`, `--sk-warn-border`, `--sk-chip-bg`, …), and its component rules assumed `<SkChip>` and the NuxtUI bridge.

**문법·구조**: 완료 보고의 시제 배치가 교과서적이다. 지금 상태는 현재(`now works`, `is clean`, `is pushed`), 내가 한 일은 과거(`built`, `screenshotted`), 고치기 전의 문제도 과거(`couldn't`, `gave`, `assumed`)다. `is pushed` 는 `was pushed` 와 달리 동작이 아니라 "올라가 있는 상태"를 말하는 상태 수동이다. 눈여겨볼 문장은 `The doc couldn't be built from before.` 다. `from before` 가 한 덩어리처럼 보이지만 아니다. 능동문 `You couldn't build (a page) from the doc` 을 수동으로 돌리면서 전치사 `from` 이 문장 끝에 남았다. `before` 는 "이전에는"이라는 부사다. 첫 문장의 `a starter section teammates can copy from` 도 같은 구조로, 관계대명사가 생략되고 전치사만 뒤에 남았다. 한국어 화자는 `from which teammates can copy` 처럼 전치사를 앞으로 끌고 가기 쉬운데, 일상 영어는 뒤에 남기는 쪽이 자연스럽다. `from only what that section contains` 의 `what` 은 선행사를 품은 관계사(= the things that)다. 짧은 문장 `Only DESIGN.md changed.` 는 변경 범위에 선을 긋는다. 마지막 문장은 `But` 으로 시작해 "가이드는 여기서 값을 가져가라는데, 정작 값이 없었다"는 모순을 드러낸다. 무생물 주어 `its component rules` 가 `assumed` 를 받는 것도 영어다운 구성이다.

**핵심 표현**: `works as a handoff` — 넘겨받은 사람이 이것만 보고 일할 수 있는 문서 구실을 한다. / `carry (token values) over from` — 값을 그대로 옮겨 가다. 목적어가 사이에 끼는 분리형 구동사다. / `gave no value for` — 값을 아예 주지 않았다. 동사를 부정하지 않고 `no + 명사` 로 부정을 목적어에 얹었다.

**격식 짝**: (작성)
- refined: Previously, the document did not contain sufficient information from which a page could be built.
- plain: Before this, you couldn't actually build a page from the doc.
- refined: I constructed a page using solely the contents of that section and verified it under both themes.
- plain: I built a page from just that section and checked it in light and dark.

<sub>출처: transcript:[assistant] skewnono_v3_nuxt</sub>

---

## 단락 2

Folder requests never finish. A folder request counts as done only when every file under it is done. Blocked files never become done, and unsampled files can't be submitted, because `submitted` only accepts samples. Any folder with a denied or `.lock` file, or a pattern family with more than 5 members, stays pending forever. Repro: a request on `/Data/Logs`, the only sample submitted and succeeded after it, and no unexplored folders below. It still shows `pending`. `test_folder_request_…` asserts that `pending`, so the test locks the defect in.

**문법·구조**: 결함 하나를 "주장 → 규칙 → 전제 둘 → 일반화 → 재현 → 테스트"로 몰아가는 논증 단락이다. 전부 단순 현재인데, 코드의 동작은 언제 돌려도 같은 사실이라서다. `never` 두 번과 `forever` 가 "가끔"이 아니라 "구조적으로 항상"임을 못 박는다. `counts as done only when …` 의 `only when` 은 문장 중간에 있어 도치가 없다. 어제 정독의 `Only if the backlog overflows do clients see 502s` 와 견주면, 도치는 `only` 구가 문두로 나올 때만 일어난다는 걸 알 수 있다. 셋째 문장은 전제 둘을 `and` 로 묶고 이유를 `because` 로 댄다. `can't be submitted` 가 수동인 까닭은 누가 제출하느냐가 중요하지 않아서다. 넷째 문장은 주어가 길다. `Any folder with …, or a pattern family with …,` 까지가 주어이고 동사는 `stays` 다. `stay + 형용사` 는 "계속 ~인 채로 있다". `Repro:` 뒤는 동사 없이 명사구 셋을 나열한 메모체다. `the only sample submitted and succeeded after it` 은 `the only sample was submitted and succeeded` 를 분사로 압축했다. 함정은 마지막 문장의 `asserts that pending` 이다. 이 `that` 은 접속사가 아니라 "그 (잘못된) pending"을 가리키는 지시 형용사다. 접속사로 읽으면 뒤에 절이 없어 문장이 끊긴다.

**핵심 표현**: `count as done` — 완료로 쳐 주다. 판정 기준을 말할 때 쓴다. / `stay pending forever` — 영영 대기 상태로 남다. / `lock the defect in` — 테스트가 틀린 동작을 기대값으로 굳혀 버리다.

**격식 짝**: (작성)
- refined: A folder request is considered complete only once every file beneath it has been completed.
- plain: A folder request is only done when every file under it is done.
- refined: The existing test asserts the erroneous state and thereby entrenches the defect.
- plain: The test expects the wrong answer, so it keeps the bug alive.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 3

An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus marks the visible tab as seen, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion while the pane is unseen. With no foreground client, a new completion in the globally active tab is treated as seen while completions in background tabs still become `done`.

**문법·구조**: 상태 기계를 글로 푼 레퍼런스 문서다. `you` 도 `I` 도 없고 주어는 전부 `An agent`, `It`, `completion` 같은 3인칭이다. 앞의 두 단락이 "내가 확인한 사실"을 현재형으로 말했다면 여기서는 "시스템의 규칙"을 현재형으로 말한다. 조건을 거는 방법이 문장마다 다른 점을 보자. `After …`(선후), `when …`(시점), `while …`(동안), `If …`(가정), `With no foreground client`(전치사구로 줄인 조건)가 차례로 나온다. 셋째 문장은 `when` 절 안에 `while` 절이 들어 있어 "활성 탭에서 끝났는데, 그때 클라이언트에 포커스가 있었다면"이라는 이중 조건이 된다. `can become` 의 `can` 은 능력이 아니라 "그럴 수도 있다"는 가능성이라 단정형 `reports` 와 구별된다. 다섯째 문장은 동명사 셋(`Focusing`, `switching`, `regaining`)이 `or` 로 묶인 주어다. `or` 연결이라 동사가 단수 `marks` 다. 여섯째 문장의 세미콜론은 "A 는 아니다; B 가 맞다"는 대비를 접속사 없이 잇는다. 뒤쪽 절이 수동(`is created by`)인 것은 화제인 `done` 을 주어 자리에 두기 위해서다. `while` 이 두 가지 뜻으로 쓰인 것도 챙겨 두자. 여섯째 문장에서는 "~하는 동안", 마지막 문장에서는 "반면에"다.

**핵심 표현**: `mark (the tab) as seen` — 확인한 것으로 표시하다. `mark A as B` 틀이다. / `turn A into B` — A 를 B 로 바꾸다. 부정문과 함께 "~한다고 바뀌지는 않는다"는 오해 방지에 쓰였다. / `With no foreground client` — `If there is no …` 를 전치사구로 줄인 조건.

**격식 짝**: (작성)
- refined: Switching away does not convert an existing `idle` status into `done`.
- plain: Just clicking away won't flip `idle` to `done`.
- refined: In the absence of a foreground client, a completion in the active tab is nonetheless treated as seen.
- plain: Even if nobody's looking at all, a finish in the active tab still counts as seen.

<sub>출처: transcript:auto-recipe-creator (herdr 스킬 본문)</sub>
