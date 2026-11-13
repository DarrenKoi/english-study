# 2026-11-14 — 정독

## 단락 1

**Clarity**: can the agent tell done from not-done? A vague bound ("understanding reached") invites **premature completion**: ending the step before it is genuinely done, attention slipping to *being done*. The visible steps still ahead (the **post-completion steps**) supply the pull; the criterion's clarity is the resistance. Defend in order: **sharpen the bound first** (local and cheap); only if it is irreducibly fuzzy *and* you observe the rush, hide the later steps by splitting the sequence. Hiding only works across a real context boundary (a hand-off or a subagent dispatch; an inline call leaves the later steps in context and clears nothing).

**문법·구조**: 전체가 현재시제다. 일반 원리를 말하는 글이라 시제 변화가 없고, 대신 구두점이 논리를 나른다. 콜론은 매번 "곧 풀어 말하면"이라는 뜻으로 쓰였다(`premature completion: ending the step…` 은 용어 뒤에 정의, `Defend in order: sharpen…` 은 예고 뒤에 내용). 세미콜론은 대등한 두 절을 맞세운다. `supply the pull; … is the resistance` 는 끄는 힘과 버티는 힘을 물리 비유로 나란히 놓은 문장이다. `attention slipping to being done` 은 주어가 따로 있는 분사구문(독립 분사구문)이라 "주의가 '끝냈다'는 쪽으로 미끄러지면서"로 읽는다. `only if A and B, hide…` 는 조건 두 개를 다 채워야 뒤 명령이 성립한다는 구조이고, 원문이 `and` 를 기울여 써서 그 점을 강조했다. 주어를 사람 대신 사물(a vague bound, the visible steps, hiding)로 세우는 방식이 문단 내내 이어진다.

**핵심 표현**:
- `tell done from not-done` — `tell A from B` 는 "A와 B를 구별하다". 형용사 `done` 을 그대로 명사처럼 썼다.
- `invites premature completion` — `invite` 는 나쁜 결과를 "불러들이다". `invite errors`, `invite criticism` 처럼 쓴다.
- `irreducibly fuzzy` — 더 줄일 수 없을 만큼 모호한. 고칠 수 있는 모호함과 구분하는 말.

**격식 짝** (작성):
- refined: A vague completion criterion invites premature completion.
- plain: If "done" isn't clear, people will stop too early.
- refined: Sharpen the bound first; hide the later steps only as a last resort.
- plain: First make the goal clearer. Only hide the next steps if that doesn't work.

<sub>출처: transcript:-Users-daeyoung-Codes (writing-for-agents 스킬 본문, "Steps and completion criteria")</sub>

---

## 단락 2

**Negation** is the failure mode beside this lever: steering by prohibition drags the forbidden behaviour into context and makes it *more* available, not less. *Don't think of an elephant*, and the elephant is all there is; the negation is a weak modifier the strongly-activated concept overruns, so the ban half-reads as an instruction to do the thing. Prompt the **positive**: state the target behaviour ("write one-line comments") so the banned one is never spoken. A prohibition earns its place only as a hard guardrail you cannot phrase positively; even then, pair it with the positive target so attention lands on what to do.

**문법·구조**: 문장은 넷뿐인데 세미콜론으로 절이 여섯 개쯤 들어 있다. 첫 문장의 주어 `steering by prohibition` 은 동명사구이고, 동사 둘(`drags`, `makes`)이 `and` 로 이어진다. 끝의 `more available, not less` 는 예상과 반대라는 점을 대비로 찍는다. 둘째 문장 `Don't think of an elephant, and the elephant is all there is` 는 `명령문 + and` 조건 구문이다("코끼리를 생각하지 말라고 하면 코끼리만 남는다"). `a weak modifier the strongly-activated concept overruns` 에서는 목적격 관계대명사 `that` 이 빠졌다. `overruns` 의 목적어가 앞의 `modifier` 라는 걸 놓치면 문장이 안 읽힌다. `half-reads as` 는 "반쯤은 ~로 읽힌다"로, `read` 가 수동 의미의 자동사로 쓰인 경우다(`This sentence reads well`). 셋째·넷째 문장의 `so` 는 둘 다 목적(`so that`)이고, 수동태 `is never spoken` 은 누가 말하느냐보다 "입 밖에 나오지 않는다"는 결과에 초점을 둔다.

**핵심 표현**:
- `drags the forbidden behaviour into context` — 금지한 행동을 오히려 맥락 안으로 끌고 들어온다. `drag A into B` 는 원치 않는 것을 끌어들일 때.
- `earns its place` — 거기 있을 자격을 얻다. 오늘 표현 목록의 `split only when the cut earns it` 과 같은 계열.
- `even then` — "그런 경우에도". 예외를 허용한 직후 다시 조건을 붙일 때 쓰는 연결어.

**격식 짝** (작성):
- refined: Steering by prohibition makes the forbidden behaviour more available, not less.
- plain: Telling someone "don't do X" just puts X in their head.
- refined: State the target behaviour so the banned one is never spoken.
- plain: Say what you want instead of what you don't want.

<sub>출처: transcript:-Users-daeyoung-Codes (writing-for-agents 스킬 본문, "Leading words")</sub>

---

## 단락 3

**Pact: reject the tooling, keep two ideas.** The tooling needs an HTTP mock server and a broker. Our boundary is in-process Python calls and nothing can go back over the network. Keep these: home's contract tests are the pact and the office just replays them, and named preconditions ("provider states") let the office reply separate "no data" from "contract violation". Fowler's ContractTest agrees: a failure means "update your fake", not "break the build".

**문법·구조**: 앞의 두 단락과 같은 날 같은 대화에 나온 글인데 문체가 전혀 다르다. 문장이 짧고, 주어-동사-목적어가 곧게 이어지며, 세미콜론이 하나도 없다. 조사 결과를 바쁜 사람에게 넘기는 보고체다. 첫 줄은 `대상: 판정` 꼴의 소제목으로, 명령형 둘(`reject…, keep…`)이 결론을 먼저 준다. 이어지는 두 문장은 근거인데 `because` 없이 나란히 놓기만 했다. "도구는 A가 필요하다. 우리는 A가 불가능하다."를 붙여 두면 독자가 인과를 스스로 읽는다. `Keep these:` 뒤 긴 문장은 `and` 로 묶은 절 세 개이고, 마지막 절의 `let the office reply separate A from B` 는 `let + 목적어 + 동사원형` 사역 구문이다(목적어가 `the office reply` 라는 명사구, 동사원형이 `separate`). `agrees:` 처럼 사람·문헌을 주어로 세워 근거를 대는 방식도 보고서에 흔하다. 마지막 `means A, not B` 는 인용부호 안의 명령문 둘을 대비시켜 해석을 한 줄로 고정한다.

**핵심 표현**:
- `reject the tooling, keep two ideas` — 도구는 버리고 아이디어 둘만 취한다. 통째로 받거나 버리지 않는 부분 채택을 말하는 틀.
- `nothing can go back over the network` — 네트워크로 되돌아갈 수 있는 게 없다. `over the network` 의 `over` 는 경로.
- `separate "no data" from "contract violation"` — `separate A from B`. 단락 1의 `tell A from B` 와 뜻이 가깝고, separate 쪽이 "분리해서 따로 표시한다"는 능동적 느낌이다.

**격식 짝** (작성):
- refined: We recommend against adopting the Pact tooling, though two of its underlying ideas merit retention.
- plain: Pact: reject the tooling, keep two ideas.
- refined: A failing contract test indicates that the fake requires updating; it should not block the build.
- plain: A failure means "update your fake", not "break the build".

<sub>출처: transcript:-Users-daeyoung-Codes (서브에이전트 조사 보고서)</sub>
