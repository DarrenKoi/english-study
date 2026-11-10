# 2026-11-11 — 정독

## 단락 1

The office databases are unreachable from home, so **mock data is the only carrier of what we know about them**. Whenever I tell you something new about an office DB — a key name, an index alias, a field, a value convention, coverage, a gotcha — update **both** of these in the same change: (…) Updating only the doc is the failure mode to avoid: the doc is read when someone writes an office adapter, but `mock.py` is what every home session actually runs against. A fact recorded in one and not the other is a fact the next home session will contradict. "Update mock.py" usually means the **docstring** — what the mock stands in for, and where it deliberately differs (grain, ranges, fabricated correlations). Change generated values when the current ones would teach something false about the real data.

**문법·구조**: 첫 문장은 `A, so B` 로 전제(집에서 사내 DB에 못 닿는다)와 결론(mock이 유일한 통로다)을 한 번에 깝니다. 이어지는 `Whenever … , update …` 는 조건절 뒤에 명령문을 둔 규칙 문장입니다. 대시(—) 사이에 예시 여섯 개를 끼워 "새로 알게 된 것"이 어디까지인지 범위를 정합니다. 셋째 문장은 콜론 앞에서 판정(`the failure mode to avoid`)부터 내리고 콜론 뒤에서 이유를 `but` 대조로 풉니다. `the doc is read`(수동태)와 `mock.py is what every home session actually runs against`(능동·what 명사절)를 맞세워, 문서는 가끔 읽히지만 mock은 매번 실행된다는 빈도 차이를 문장 모양으로 보여 줍니다. 넷째 문장 `A fact … is a fact …` 는 같은 명사를 반복한 경구입니다. 마지막 두 문장은 "mock.py를 고쳐라"가 실제로 무슨 뜻인지 좁혀 가며 규칙을 행동으로 바꿉니다. `would teach something false` 의 `would` 는 "그대로 두면 ~하게 될" 가정입니다.

**핵심 표현**:
- `the only carrier of what we know about them` — 데이터가 아니라 지식을 나르는 매개라는 시각. 설계 문서에서 어떤 산출물의 무게를 올릴 때 씁니다.
- `the failure mode to avoid` — 피해야 할 전형적 실패. `to avoid` 가 명사를 뒤에서 꾸미는 to부정사 형용사 용법입니다.
- `what the mock stands in for` — mock이 대신하는 대상. `stand in for` 는 대역·대리를 뜻합니다.

**격식 짝** (작성):
- refined: Recording a fact in only one of the two places is the failure mode we most need to avoid.
- plain: If you only update one of them, that's exactly how things go wrong.

<sub>출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md "Office DB knowledge lands in TWO places, always")</sub>

---

## 단락 2

Once it's red, shrink the repro to the **smallest scenario that still goes red**. Cut inputs, callers, config, data, and steps **one at a time**, re-running the loop after each cut, and keep only what's load-bearing for the failure. Why bother: a minimal repro shrinks the hypothesis space in Phase 3 (fewer moving parts left to suspect) and becomes the clean regression test in Phase 5. Done when **every remaining element is load-bearing**: removing any one of them makes the loop go green. Do not proceed until you have reproduced **and** minimised. Generate **3–5 ranked hypotheses** before testing any of them. Single-hypothesis generation anchors on the first plausible idea.

**문법·구조**: 거의 전부 명령문이고 주어 없는 조각문(`Why bother:`, `Done when …`)이 섞여 있습니다. 지침서 특유의 압축 문체입니다. `Once it's red` 의 `once` 는 "일단 ~하면"이라는 시간 접속사입니다. 둘째 문장은 명령 두 개(`Cut … and keep …`) 사이에 분사구 `re-running the loop after each cut` 를 끼워 "자를 때마다 다시 돌려라"를 따로 문장으로 빼지 않고 붙입니다. `Why bother:` 는 독자가 던질 반문을 먼저 꺼내 답하는 장치입니다. 답 문장은 동사 두 개(`shrinks`, `becomes`)로 이점을 둘 내놓습니다. `Do not proceed until you have reproduced and minimised` 는 `until + 현재완료` 로 "두 가지를 끝내기 전엔"을 조건으로 겁니다. 마지막 문장은 무생물 주어 `Single-hypothesis generation` 이 `anchors on` 하는 구조라 사람을 탓하지 않고 방법의 결함을 짚습니다. 철자 `minimised`·`parallelise` 는 영국식입니다.

**핵심 표현**:
- `load-bearing` — 하중을 받치는(빼면 무너지는). 꼭 필요한 요소를 가리키는 비유로 자주 씁니다.
- `fewer moving parts left to suspect` — 의심할 움직이는 부품이 줄어든다. `left to + 동사` 는 "아직 ~할 게 남은".
- `anchors on the first plausible idea` — 처음 그럴듯한 생각에 닻을 내린다(앵커링 편향).

**격식 짝** (작성):
- refined: Generating several ranked hypotheses guards against anchoring on the first plausible explanation.
- plain: If you only come up with one idea, you'll get stuck on it — so list a few first.

<sub>출처: transcript:skewnono-v3-nuxt d0eba2c5 (diagnosing-bugs 스킬 Phase 2–3)</sub>

---

## 단락 3

**Always tear the worktree down once the work is on `main`.** Merging and pushing is not the end of the task: run `git worktree remove` and `git branch -d` in the same session, immediately after the push succeeds. A task is only done when `git worktree list` shows the main tree alone. Leftover worktrees accumulate stale checkouts, hold onto merged branches, and mislead the next session about what work is still open. This is the one sanctioned exception to "work directly on `main`" — the branch exists only to carry the worktree and is deleted on merge, so it is not a feature branch. Single-file edits stay in the main tree; the worktree setup is not worth it there.

**문법·구조**: 첫 문장 `Always … once …` 는 빈도부사 명령에 시간절을 붙여 "언제 하라"까지 정합니다. 둘째 문장은 오해(`Merging and pushing is not the end`)를 먼저 깨고 콜론 뒤에 할 일을 내놓습니다. 동명사 두 개가 주어인데 한 덩어리 행위로 봐서 단수 `is` 를 썼습니다. `A task is only done when …` 은 `only` 로 완료 조건을 좁힙니다. 넷째 문장은 무생물 주어 하나에 동사 셋(`accumulate`, `hold onto`, `mislead`)을 나란히 붙여 방치의 대가를 쌓습니다. 다섯째 문장은 대시 뒤에서 왜 예외가 규칙과 충돌하지 않는지 해명합니다. `exists only to carry` 의 to부정사가 목적을, `is deleted on merge` 수동태가 자동 정리를 말합니다. 마지막은 세미콜론으로 규칙과 이유를 붙인 짧은 마무리입니다.

**핵심 표현**:
- `tear the worktree down` — 환경을 철거·정리하다. 구동사 목적어가 명사면 `tear down the worktree` 도 됩니다.
- `the one sanctioned exception` — 공식으로 허용된 단 하나의 예외. `sanctioned` 는 "승인된".
- `is not worth it there` — 거기서는 들이는 수고만큼 값어치가 없다.

**격식 짝** (작성):
- refined: For single-file edits, the overhead of a worktree outweighs its benefit.
- plain: For a one-file change, setting up a worktree just isn't worth it.

<sub>출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md Git Workflow)</sub>
