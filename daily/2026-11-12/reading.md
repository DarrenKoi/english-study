# 2026-11-12 — 정독

## 단락 1

**Default to** a sibling pane in the current tab and current working directory. Do not create a workspace, tab, worktree, or different cwd **unless the user explicitly requests** that topology or location. **Honor** a direction requested by the user. **Otherwise** inspect the caller pane's current rectangle: (…) Split a wide pane to the right and a narrow or tall pane down. Avoid repeated same-direction splits **that would create** unusably narrow columns or short rows. Keep the user's focus in the calling pane.

**문법·구조**: 일곱 문장이 모두 주어 없는 명령문이고, 순서가 곧 판단 순서입니다. 기본값(`Default to`)을 먼저 정하고, 금지와 예외(`Do not … unless …`)를 붙이고, 사용자 지시가 있을 때(`Honor …`)와 없을 때(`Otherwise …`)로 갈라집니다. `unless` 절은 "~하지 않는 한"이라 `if … not` 보다 예외라는 느낌이 뚜렷합니다. `a direction requested by the user` 는 과거분사가 명사를 뒤에서 꾸미는 꼴로, `that the user requested` 를 줄인 형태입니다. 다섯째 문장은 `Split A to the right and B down` 에서 둘째 동사를 생략해 대구를 맞췄습니다. `that would create …` 의 `would` 는 "그렇게 쪼개면 생길"이라는 가정이라, 아직 일어나지 않은 결과를 미리 막는 말투가 됩니다. `unusably narrow` 는 부사가 형용사의 정도를 "못 쓸 만큼"으로 못 박습니다.

**핵심 표현**:
- `Default to X` — 따로 지시가 없으면 X. 컨벤션 문서의 첫 문장으로 좋습니다.
- `Honor a direction requested by the user` — 사용자의 지시를 "존중해 그대로 따른다". `follow` 보다 약속을 지킨다는 무게가 실립니다.
- `Keep the user's focus in the calling pane` — 백그라운드 작업이 화면을 빼앗지 않게 한다.

**격식 짝** (작성):
- refined: Absent an explicit instruction from the user, the agent should default to a sibling pane and leave the user's focus undisturbed.
- plain: If the user didn't say where, just open it next to the current pane and don't steal their focus.

<sub>출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively. 중간의 코드 블록은 (…)로 생략)</sub>

---

## 단락 2

For normal background work, wait for the agent to start working. **If the pane remains** in a background tab or workspace, wait for `done` **before reading** its transcript: (…) If the user is watching that tab, completion reports `idle` **instead**, so wait for `idle`. Always treat **either** `idle` **or** `done` as completed when inspecting `pane get`; **the difference is whether** the result has been seen. If a wait times out, inspect `herdr pane get <returned-pane-id>` and `pane read` before deciding what to do. A `blocked` agent needs input; an `unknown` pane **may not yet contain** a detected or integrated agent.

**문법·구조**: 조건절 `If …` 가 세 번 나오고 그때마다 주절은 명령문입니다. 경우를 나눠 행동을 정해 주는 런북 문체입니다. `wait for the agent to start working` 은 `wait for + 목적어 + to부정사` 로 "누가 무엇을 하기를 기다리다"를 한 덩어리로 만듭니다. `before reading`, `before deciding` 은 주어가 주절과 같아서 절 대신 동명사로 줄였습니다. 셋째 문장의 `completion reports idle` 은 무생물 주어(완료라는 사건)가 "보고한다"는 동사를 받는 영어다운 구문입니다. 한국어로는 "완료되면 idle로 표시된다"로 풀어야 자연스럽습니다. 넷째 문장은 세미콜론 앞에서 규칙을 주고 뒤에서 근거를 댑니다. `whether the result has been seen` 은 현재완료 수동태로, "누가 봤는지"는 중요하지 않고 "봤다는 결과가 지금 남아 있는지"만 묻습니다. 마지막 문장은 세미콜론으로 두 상태를 나란히 두고, `may not yet contain` 으로 "아직은 없을 수도 있다"고 단정을 피합니다.

**핵심 표현**:
- `If a wait times out, … before deciding what to do` — 시간 초과가 나면 판단보다 확인이 먼저.
- `treat either A or B as completed` — 둘 중 어느 쪽이든 완료로 본다. `treat A as B` 는 "A를 B로 취급하다".
- `completion reports idle instead` — `instead` 한 단어가 "(done이 아니라) 대신"을 맡습니다.

**격식 짝** (작성):
- refined: Should a wait time out, examine the pane's status and recent output before determining how to proceed.
- plain: If the wait times out, look at what the pane is doing first, then decide.

<sub>출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively 후반. 중간의 코드 블록은 (…)로 생략)</sub>

---

## 단락 3

I checked the REA docs against the upstream release notes and updated five files. Codex drafted a new know-how page in a sibling pane, and I verified its key claims before keeping it. Nine links were dead because upstream had moved its docs into subfolders, so I pointed each one at its new path. One earlier claim no longer held: since 6.8.0, `analyze_function` returns only a summary by default. I haven't run any of this on the office PC, so treat the prompts as untested there. The slide deck still describes the old behavior and has not been touched. If anything in the new page looks wrong, say so rather than fixing it quietly.

**문법·구조**: 작업 보고는 "한 일(과거) → 왜(과거완료) → 지금 상태(현재·현재완료)"로 시제가 움직입니다. `Nine links were dead because upstream had moved its docs` 에서 과거완료 `had moved` 는 링크가 죽기 전에 먼저 일어난 일을 표시합니다. `One earlier claim no longer held:` 뒤 콜론은 무엇이 틀렸는지를 바로 풀고, 그 내용은 지금도 참이라 현재형 `returns` 로 씁니다. `I haven't run any of this` 의 현재완료는 "지금까지 한 번도"이고, 뒤의 `so treat … as untested` 가 독자가 취할 태도를 정해 줍니다. `has not been touched` 는 수동태로 "누가"를 빼고 슬라이드의 상태만 말합니다. 마지막 문장은 오늘 표현 `say so rather than …` 을 부탁하는 말로 바꿔 쓴 것입니다.

**핵심 표현**:
- `checked A against B` — A를 B와 대조했다. "대조"는 `compare with` 보다 `check against` 가 검증의 느낌을 줍니다.
- `no longer held` — 더는 성립하지 않았다. 자동사 `hold` 는 "(주장이) 유효하다".
- `treat the prompts as untested there` — 확인하지 못한 범위를 숨기지 않고 독자에게 넘기는 말.

**격식 짝** (작성):
- refined: None of these changes has been validated on the office machine; the prompts should therefore be regarded as untested in that environment.
- plain: I haven't tried any of this on the office PC yet, so don't assume the prompts work there.

<sub>출처: 모범 단락(작성). 오늘 대화의 한국어 작업 보고를 바탕으로 썼습니다.</sub>
