<sub>2026-06-26 — 정독</sub>

## 단락 1

Three matcher-fusion methods (median-consensus, soft-voting heatmap, RRF) all hit the same wall: on SEM they recover the true align point into the candidate set (in_topk ~0.92–0.94) but rank it #1 only ~0.5 of the time — a periodic distractor is a structurally equal template match. The conclusion: SEM is a ranking/distinctiveness problem, and the lever is the align key, not the matcher. Re-registration onto a more distinctive region is the validated next move.

Rank-1 on a recipe's own success frames is a cleaner, calibration-light distinctiveness signal — if the matcher can't rank the true point #1 even on a clean success frame, the key is ambiguous by construction — and it is already measured per recipe by the consensus eval.

**문법·구조**:
- **현재시제 = 일반적 진리.** `they recover ... but rank it #1 only ~0.5 of the time`, `a periodic distractor is a structurally equal template match` — 실험에서 *늘 관측되는 성질*을 단정하므로 과거시제가 아닌 현재시제다. 보고서에서 "관측된 사실"은 과거(We observed…)지만, "법칙처럼 늘 그렇다"는 현재로 쓴다.
- **콜론(`:`)의 두 가지 쓰임.** 첫 문장 `the same wall:` 뒤 콜론은 *앞 명사를 풀어 설명*(무슨 벽인지), 두 번째 `The conclusion:` 뒤 콜론은 *결론 내용을 제시*. 둘 다 "앞을 받아 뒤에서 펼친다".
- **대시(`—`)로 끼워 넣는 근거.** `only ~0.5 of the time — a periodic distractor is …` 의 대시는 바로 앞 사실의 *이유*를 삽입한다. 둘째 단락의 대시 한 쌍(`— if … by construction —`)은 문장 한가운데에 조건절을 통째로 끼워 넣은 삽입구다.
- **`the lever is X, not Y`.** "진짜 핵심은 Y가 아니라 X"라는 대조 단정. `not Y` 를 뒤에 붙여 흔한 오해(matcher 탓)를 먼저 부정한다.

**핵심 표현**:
- **hit the same wall** — 여러 방법이 똑같은 한계에 막혔다(요약 한 줄). [[hit-the-same-wall]]
- **the validated next move** — 검증으로 확정된 다음 수순. [[the-validated-next-move]]
- **ambiguous by construction** — 구조상 필연적으로 모호한. `even on a clean success frame` 의 양보가 이 단정을 떠받친다.

**격식 짝**:
- refined: *SEM is a ranking problem, and the lever is the align key, not the matcher.*
- plain: *The problem isn't the matcher — it's that the key itself is too hard to tell apart.* (작성)

<sub>출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md §1</sub>

---

## 단락 2

The reregister driver keys recipes as `f"{a.class_name}/{a.recipe_name}"`. The consensus `per_recipe["recipe"]` must use the same format for the join to land — historically there were `class/recipe` vs `eqp/class/recipe` collision differences between drivers. Implementation MUST, as task 1, verify the exact format the consensus driver emits and pin the join key to match. Emit a loud join-coverage line — `[INFO] rank1-join: matched M/N report recipes to consensus rows` — so a silent key mismatch (M≈0) is impossible to miss. A near-zero match rate is a hard failure signal, not a quiet NO_DATA flood.

**문법·구조**:
- **명령형 + 대문자 `MUST`.** 스펙·RFC 에서 `MUST` 를 대문자로 쓰면 "지켜야 하는 강제 요구"라는 약속된 규범어다(RFC 2119). `Implementation MUST … verify … and pin …` 처럼 주어를 두고도 동사 원형으로 강한 의무를 건다.
- **목적의 `so (that)`.** `… is impossible to miss` 앞의 `so` 는 "그렇게 해서 ~하도록"이라는 *목적절*. 앞 동작(loud line 출력)의 *이유*를 뒤에서 설명한다.
- **삽입 대시로 예시 코드 끼우기.** `a loud join-coverage line — \`[INFO] …\` — so …`: 대시 한 쌍이 "어떤 라인인지"를 실제 예로 보여주고 문장 흐름은 그대로 잇는다.
- **`for the join to land`.** `for + 목적어 + to부정사` = "조인이 성사되려면". 구어의 "to make the join work"보다 압축적·문어적.

**핵심 표현**:
- **the join to land** — (조인이) 성사되다/꽂히다. `land` 가 "의도한 자리에 안착"의 비유. [[impossible-to-miss]]
- **impossible to miss** — 못 보고 지나칠 수 없게.
- **a hard failure signal, not a quiet flood** — 조용히 쌓이는 게 아니라 단호한 실패로 다뤄라. [[a-hard-failure-signal]]

**격식 짝**:
- refined: *Emit a loud coverage line so a silent key mismatch is impossible to miss.*
- plain: *Print the match count loudly — that way you can't miss it if the keys don't line up.* (작성)

<sub>출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md §5</sub>
