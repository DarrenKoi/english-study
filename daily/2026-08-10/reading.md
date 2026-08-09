# 2026-08-10 — 정독

## 단락 1

`idle` and `done` are the same underlying semantic state with different attention state. An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus marks the visible tab as seen, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion while the pane is unseen.

**문법·구조**: 상태 기계 명세는 전부 **단순현재**로 씁니다 — `reports`, `becomes`, `is created`. 지금 일어나는 일이 아니라 "언제나 그렇게 동작한다"는 규칙이라서, 진행형이나 미래형을 쓰면 오히려 어색해집니다. 세 번째~다섯 번째 문장이 `when` / `while` / `if` 로 조건을 하나씩 갈아 끼우며 같은 골격을 반복하는데, 대상이 상태 전이표라 이 반복이 지루함이 아니라 **빠짐없음**의 표시가 됩니다. 여섯 번째 문장의 주어는 동명사 셋(`Focusing`, `switching`, `regaining`)을 묶은 긴 주부인데, 동사는 단수 `marks` 입니다 — "이 행위들 중 아무거나 하나"가 아니라 "이 행위"라는 한 덩어리로 보기 때문입니다. 마지막 문장의 세미콜론은 앞뒤가 **부정 → 긍정** 짝이라 마침표보다 붙여 읽히게 하려는 선택이고, `is created by` 수동태는 행위자(사용자·클라이언트)를 일부러 지워 조건만 남깁니다.

**핵심 표현**: `attention state` — 같은 상태를 "봤는가/안 봤는가"로 한 축 더 쪼갠 개념어. `its result is considered seen` — 판정 주체를 감춘 명세용 수동태. `marks the visible tab as seen` — `mark A as B` 는 시스템이 플래그를 세우는 동작에 쓰는 기본 동사구.

**격식 짝**: (작성)
- refined: `An agent that completes while its tab is in the background reports done rather than idle.`
- plain: `If it finishes while you're looking somewhere else, it says done instead of idle.`

<sub>출처: transcript:skewnono_v3_nuxt 9cb33a18 (herdr 스킬 문서)</sub>

---

## 단락 2

Show the jobs grouped as they're stored. Keep it scannable. Call out anything whose `since` date is several days old — that's a job at risk of being forgotten, and the user should decide whether it still matters or should be dropped. Pick one job to resume and say why — normally the top in-progress item, since its next action is already written and momentum is cheapest there. Restate that exact next action so the user can dive straight in. If the user passed an argument naming a job, focus on that instead. Then confirm which job before writing any code. The carryover tells you where the user stopped; only the user knows where they want to start.

**문법·구조**: 처음 여섯 문장이 전부 **명령형**입니다(`Show`, `Keep`, `Call out`, `Pick`, `Restate`, `focus`). 주어 `You` 를 지우면 지시가 짧아지고, 읽는 쪽이 곧바로 행동으로 옮길 수 있습니다. 세 번째와 네 번째 문장의 대시(`—`)는 둘 다 **앞말의 근거를 덧붙이는** 자리인데, 콜론이 "이제 설명한다"고 예고하는 것과 달리 대시는 말을 하다 말고 덧붙이는 호흡이라 지침 문서에서도 딱딱해지지 않습니다. `whose `since` date is several days old` 는 사물을 선행사로 받은 `whose` 로, 관계대명사 중 유일하게 사람·사물을 가리지 않습니다. 마지막 문장은 세미콜론을 축으로 `stopped` ↔ `start`, `The carryover` ↔ `only the user` 를 맞세운 대구인데, 시제까지 과거 대 현재로 갈라 두 시점의 차이를 문법으로 보여 줍니다.

**핵심 표현**: `call out X` — 눈에 띄게 짚어 알리다(회의·리뷰에서 매우 흔함). `at risk of being forgotten` — `at risk of + 동명사` 로 아직 일어나지 않은 위험을 붙임. `momentum is cheapest there` — 재개 비용을 최상급 형용사 하나로 환산한 은유.

**격식 짝**: (작성)
- refined: `Flag any item whose recorded date suggests it has gone unattended, and ask whether it should be dropped.`
- plain: `If something's been sitting there for days, say so and ask if it still matters.`

<sub>출처: transcript:skewnono_v3_nuxt 2fc9f8aa (back-to-office 스킬 문서)</sub>

---

## 단락 3 (모범 단락 · 작성)

When you hand a review to another agent, say what you want in the order you want it back. Be adversarial, look for real defects, and report findings ranked by severity with file:line — that sentence alone removes most of the guesswork. Keep the wrapper a thin forwarder only, so the reviewer's words reach you unedited. Inspect before waiting: read whatever output is already there, and only then block on the next transition. Treat every identifier it returns as an opaque string, because the suffix that looks meaningful today is the one that grows a character tomorrow. If the run surprises you, remember that the installed binary is the authority for command syntax, not the examples you memorised. And when you write the result up, keep it scannable — dense is better than verbose.

**문법·구조**: 첫 문장은 `When you …, say …` 로 조건절을 앞세워 조언의 무대를 깔고, `in the order you want it back` 은 관계부사가 생략된 관계절(`the order [in which] you want it back`)입니다. 두 번째 문장은 명령 셋을 콤마로 나열한 뒤 대시로 그 효과를 붙였는데, 나열이 길어질수록 마지막에 짧은 평가절을 다는 리듬이 잘 먹힙니다. 네 번째 문장의 콜론은 격언을 먼저 던지고 풀이를 뒤에 대는 자리라 대시와 역할이 다릅니다. `because the suffix that looks meaningful today is the one that grows a character tomorrow` 는 관계절 두 개를 `today` ↔ `tomorrow` 로 대칭시킨 문장이고, 마지막 문장의 `And` 로 시작하는 문두 접속사는 글 전체에 한 번만 써야 힘이 남습니다.

**핵심 표현**: `removes most of the guesswork` — 추측할 여지를 없앤다는 실무 칭찬. `reach you unedited` — 과거분사를 문장 끝에 놓아 "손대지 않은 채로"를 부사처럼 씀. `the one that grows a character tomorrow` — 막연한 미래 변화를 구체적 사건으로 바꿔 경고를 실감나게 만드는 방식.

**격식 짝**: (작성)
- refined: `State the desired output format in the request itself; a reviewer cannot infer the ordering you expect.`
- plain: `Tell them how you want it back — they can't guess the order.`

<sub>출처: 모범 단락(작성)</sub>
