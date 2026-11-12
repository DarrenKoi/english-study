# 2026-11-13 — 정독

## 단락 1

Bug fix = root cause, not symptom. A report **names** a symptom. **Before you edit**, grep every caller of the function **you're about to touch**. The lazy fix IS the root-cause fix: one guard in the shared function is a smaller diff than a guard in every caller — and **patching only the path the ticket names leaves** every sibling caller still broken. Fix it once, **where all callers route through**.

**문법·구조**: 다섯 문장이 주장, 근거, 행동 순으로 흘러갑니다. 첫 줄은 등호를 쓴 표어이고, 둘째 문장이 그 이유를 네 단어로 댑니다. `names` 는 동사로 "지목한다"는 뜻이고, 현재시제라 일반적 사실로 읽힙니다. 셋째 문장은 `Before you edit` 로 시점을 먼저 박고 명령문을 냅니다. `the function you're about to touch` 는 목적격 관계대명사가 빠진 절이며, `be about to` 가 "막 손대려는"이라는 직전 시점을 만듭니다. 넷째 문장이 가장 깁니다. 콜론 뒤에서 `one guard … is a smaller diff than a guard in every caller` 로 비교하고, 대시 뒤 `and` 로 두 번째 근거를 더합니다. 여기서 주어는 동명사구 `patching only the path the ticket names` 전체이고 동사는 `leaves` 입니다. 대문자 `IS` 는 "게으른 수정과 근본 원인 수정이 다르지 않다"는 동일성을 힘주어 말합니다. 마지막 문장의 `where` 절은 장소 부사절로, "모든 호출자가 지나가는 그 자리에서"를 뜻합니다.

**핵심 표현**:
- `A report names a symptom` — 신고는 증상을 가리킬 뿐 원인을 말해 주지 않는다. 이슈를 읽는 태도를 한 줄로.
- `leaves every sibling caller still broken` — `leave + 목적어 + 형용사` 로 "고장 난 채 남긴다".
- `Fix it once, where all callers route through` — 한 번만, 공통 경로에서.

**격식 짝** (작성):
- refined: A fix applied only to the reported code path leaves the remaining call sites defective; the correction belongs in the shared function.
- plain: If you only patch the spot in the ticket, everything else that calls it is still broken. Fix it in the shared function instead.

<sub>출처: transcript:pm-notes 6a5d0980 (ponytail 지침, The ladder 절 끝의 Bug fix 단락)</sub>

---

## 단락 2

Never lazy about understanding the problem. The ladder shortens the solution, **never the reading**. Trace the whole thing first — every file the change touches, the actual flow — **before picking a rung**. Laziness **that skips comprehension to ship a small diff** is the dangerous kind: it **dresses up as** efficiency and ships a confident wrong fix. Read fully, **then** be lazy.

**문법·구조**: 첫 문장은 주어와 동사(`Be`)를 뺀 조각문이라 구호처럼 들립니다. 둘째 문장은 쉼표 뒤에서 동사를 생략하고 `never the reading` 만 남겨 대비를 압축했습니다. 셋째 문장은 대시 한 쌍 사이에 `the whole thing` 의 내용을 동격으로 풀어 넣습니다. `every file the change touches` 에도 관계대명사가 빠져 있습니다. `before picking a rung` 은 주절과 주어가 같아 동명사로 줄인 형태입니다. 넷째 문장의 주어는 `Laziness` 이고, `that skips comprehension to ship a small diff` 가 그 게으름의 종류를 한정합니다. 여기서 `to ship` 은 목적("작은 diff 를 내려고")입니다. 콜론 뒤 `it` 은 그 게으름을 받고, 동사 두 개(`dresses up`, `ships`)가 `and` 로 나란히 이어집니다. `a confident wrong fix` 는 형용사 두 개를 쉼표 없이 붙여 "자신만만하게 틀린 수정"이라는 한 덩어리 개념으로 만들었습니다. 마지막 문장은 `then` 하나로 순서를 정합니다. 읽기가 먼저입니다.

**핵심 표현**:
- `shortens the solution, never the reading` — 줄여도 되는 것과 안 되는 것을 한 문장에.
- `is the dangerous kind` — "~은 위험한 부류다". `kind` 뒤 명사를 생략해 앞 주어를 받습니다.
- `Read fully, then be lazy` — 두 명령을 `then` 으로 순서 지어 원칙을 닫는 방식.

**격식 짝** (작성):
- refined: Brevity in implementation must not come at the expense of understanding; the entire change path should be traced before a solution is chosen.
- plain: Keep the code short, but don't skip the reading. Go through the whole flow first, then pick the easy fix.

<sub>출처: transcript:pm-notes 6a5d0980 (ponytail 지침, When NOT to be lazy)</sub>

---

## 단락 3

Provider selection is not a single switch; it is the conjunction of two independent questions. The first asks whether the process is running in the office, and the second asks whether an adapter has been written for the feature. A feature serves office data only when both answers are yes, **which means** copying the template is at once the act of creating the adapter and the act of enabling it. Some combinations fail without raising an error. If the storage adapter is present but the equipment roster is still a mock, the join matches nothing, and the table renders empty with a 200 response. **Treat that as a configuration fault, not a missing capability.** The startup check **therefore** validates the resolved pairs and refuses to boot, **rather than silently serving** an empty page.

**문법·구조**: 오늘 배치의 한국어 문서(`provider-selection.md`)를 바탕으로 쓴 설계 설명문입니다. 첫 문장은 세미콜론으로 `is not A; it is B` 를 잇습니다. 정의를 내릴 때 `but` 보다 단정한 방법입니다. 둘째 문장의 `whether` 절 두 개는 시제가 다릅니다. `is running` 은 지금 상태를 묻고 `has been written` 은 현재완료 수동태로 "이미 작성돼 있는가"를 묻습니다. 셋째 문장의 `, which means` 는 앞 절 전체를 받는 계속적 용법이고, `at once A and B` 는 "A 이면서 동시에 B"입니다. 넷째 문장은 일부러 짧게 두어 다음 예시로 넘어가는 다리 구실을 합니다. 다섯째 문장은 `If` 절 안에서 `but` 으로 두 조건을 대비시키고, 주절에서 결과 둘을 `and` 로 잇습니다. `renders empty` 의 `empty` 는 보어로 쓰인 형용사입니다. 여섯째 문장은 오늘 표현 `Treat this as A, not B` 를 그대로 가져왔습니다. 마지막 문장의 `rather than silently serving` 도 오늘 표현의 틀로, 동사 원형이 아니라 동명사가 온다는 점을 확인합니다.

**핵심 표현**:
- `the conjunction of two independent questions` — "서로 독립된 두 질문의 논리곱". 문서의 한국어 표현을 그대로 옮긴 말입니다.
- `fail without raising an error` — 오류 없이 실패하다. 조용한 실패를 말하는 기본 표현.
- `refuses to boot` — 부팅을 거부하다. 무생물 주어에 `refuse` 를 쓰는 영어식 표현입니다.

**격식 짝** (작성):
- refined: The startup check validates the resolved pairs and refuses to boot rather than silently serving an empty page.
- plain: The app checks the pairs when it starts and just won't come up if they don't match, so you never get a blank page with no error.

<sub>출처: 모범 단락(작성). 내용은 repo:skewnono_v3_nuxt docs/back-end/provider-selection.md 의 1절과 7절</sub>
