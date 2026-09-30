# 2026-10-01 — 정독

> 세 단락 모두 배치 원문(어시스턴트 답변)이다. 단락 1은 "폴더를 복사해 사무실 LLM 에게 주면 되지 않나"라는 질문에 왜 안 되는지를 가정법으로 풀어 간다. 단락 2는 NCC 예외 규칙을 모든 레시피에 써도 되느냐는 질문의 답으로, 결론 → 근거 → 원리 순서가 교과서적이다. 단락 3은 틀린 점을 찍고도 OK 를 누른 사고의 원인 분석에서 번호 목록 두 항목을 이어 붙였다(번호와 굵은 소제목 표시만 뗐다).

## 단락 1

Copying the folder won't work the way you expect. Almost everything in workflow_3 imports itself by absolute path: 214 files contain 1,032 `from poc.workflow_3.…` imports. In a copy like `poc/workflow_3_office/`, those imports still load the **original** `poc/workflow_3`. The office LLM would edit files in the copy, but the code that actually runs would be the original, so its changes would do nothing and it wouldn't be obvious why. On top of that, you'd have two copies drifting apart and would need to merge them by hand.

**문법·구조**: 첫 문장은 동명사 주어 `Copying the folder` 에 미래 부정 `won't` 를 붙여 상대 계획의 결과를 먼저 말한다. 둘째 문장은 콜론 앞에 주장(절대 경로로 import 한다)을, 뒤에 숫자 근거(214개 파일, 1,032개 import)를 둔다. 셋째 문장은 현재시제 `still load` 다. 복사본에서도 늘 그렇게 동작한다는 사실이라서다. 넷째 문장부터 `would` 가 연달아 나온다. 아직 일어나지 않은 계획을 가정하고 결과를 그려 보는 가정법이다. `the code that actually runs` 의 관계절이 "고치는 파일"과 "실제로 도는 코드"를 갈라 놓는 게 이 단락의 요점이다. 끝의 `it wouldn't be obvious why` 에서 `why` 뒤에는 `its changes would do nothing` 이 생략됐다. 마지막 문장은 `On top of that,` 으로 두 번째 문제를 덧붙이고 `you'd have … and would need …` 로 조동사 하나 아래 동사 둘을 묶었다. `two copies drifting apart` 는 명사 + 현재분사로 "점점 어긋나는 두 사본"이다.

**핵심 표현**: `won't work the way you expect` — 안 된다고 자르지 않고 "생각과 다르게 동작한다"로 돌려 말하기. / `it wouldn't be obvious why` — 고장보다 무서운 "왜 안 되는지 모르는" 상태를 짚는 말. / `On top of that,` — 문제를 하나 더 얹을 때 쓰는 구어 연결어(격식이면 `Moreover,`).

**격식 짝**: (작성)
- refined: Because every module is imported by its absolute path, a duplicated folder would continue to execute the original code, and any modifications made in the copy would have no effect.
- plain: The copy still runs the old code, so whatever the office LLM changes there just won't do anything.

<sub>출처: transcript:auto-recipe-creator (사무실 LLM 병렬 작업 상담)</sub>

---

## 단락 2

Not yet for all recipes, and not by adding branches by guesswork either. The rule is sound for the failure we saw, but we have one recorded case. Adding conditions now would mean guessing at failures we haven't observed. The key is wide and short. Sliding the template along its horizontal lines barely changes the chamfer score, which is why `2nd비` sits around 0.98 even when the match is right. At the slid position the vertical structure doesn't line up, so NCC collapses (0.612 vs -0.023). The rule adds no new way of finding the key. It only confirms the spot the matcher already picked, in a case where chamfer can't tell the key from a sideways copy.

**문법·구조**: 첫 문장은 주어·동사가 없는 답변문이다. 질문("모든 레시피에 써도 되나? 분기를 넣어야 하나?")을 받아 `Not yet …, and not … either` 로 둘 다 한 번에 부정한다. 둘째 문장 `sound … but …` 은 인정과 한계를 한 문장에 담는다. 셋째 문장의 `would mean + 동명사` 는 "그렇게 하면 ~하는 셈이 된다"로, 가정한 행동의 실제 의미를 풀어 준다. `failures we haven't observed` 는 관계대명사를 생략한 목적격 관계절이고 현재완료가 "지금까지 한 번도"를 담는다. 넷째 문장부터 원리 설명이다. 짧은 문장(`The key is wide and short.`)으로 전제를 세우고 긴 문장으로 결과를 끌어낸다. `, which is why …` 는 앞 절 전체를 받는 계속적 관계대명사로 "그래서 ~이다"를 만든다. `At the slid position` 의 `slid` 는 slide 의 과거분사가 형용사로 쓰였다. 마지막 두 문장은 `adds no new way` ↔ `only confirms` 로 규칙의 범위를 좁혀, 이 규칙이 위험하지 않은 이유를 대비로 보여 준다.

**핵심 표현**: `by guesswork` — 근거 없이 짐작으로. / `guessing at failures we haven't observed` — `guess at` 은 확신 없이 헛짚는 뉘앙스. / `can't tell the key from a sideways copy` — `tell A from B` 는 "A 와 B 를 구별하다".

**격식 짝**: (작성)
- refined: With only a single recorded case, introducing additional conditions at this stage would amount to speculating about failure modes that have not yet been observed.
- plain: We've only seen this once, so adding more rules now would just be guessing.

<sub>출처: transcript:auto-recipe-creator (NCC 예외 규칙 확장 검토)</sub>

---

## 단락 3

The point it acted on had `2nd비=1.000`. That means its edge match was exactly as good 164px away. This is over the 0.98 ambiguity limit, so it should have gone to engineer review. The recenter check can't catch a wrong key. After each click it re-matches the same template. Once the look-alike is at the center, it passes again, reads as "converged", and OK is clicked. That check only confirms the click landed where the matcher wanted. It can't tell whether the matcher picked the right spot.

**문법·구조**: 첫 문장 `The point it acted on` 은 관계대명사가 생략되고 전치사 `on` 이 끝에 남은 형태다(= the point on which it acted). 구어·기술 글에서는 이쪽이 훨씬 자연스럽다. 둘째 문장의 `That means` 가 숫자를 사람 말로 번역해 준다. `exactly as good 164px away` 는 원급 비교 `as good (as the key)` 에서 비교 대상을 생략하고 거리 부사구를 붙였다. 셋째 문장 `should have gone` 은 `should have + p.p.` 로 "그랬어야 했는데 안 됐다"는 과거의 어긋남이다. 넷째 문장부터 두 번째 원인이다. `After each click`, `Once …` 로 시간 순서를 짚으며 절차를 따라간다. 여섯째 문장은 동사 셋(`passes`, `reads as`, `is clicked`)을 나열하는데 마지막만 수동태다. OK 를 누르는 행위자보다 "눌렸다"는 결과가 중요해서다. 마지막 두 문장은 `only confirms …` ↔ `can't tell whether …` 로 검사가 확인하는 것과 확인하지 못하는 것을 나란히 둔다. `confirms (that) the click landed` 는 that 이 생략된 명사절이다.

**핵심 표현**: `should have gone to engineer review` — 원래 가야 했던 경로를 과거 사실과 대비. / `reads as "converged"` — 판정 결과가 어떻게 "읽히는지"를 `read as` 로. / `can't tell whether …` — 검사의 한계를 한 줄로 긋는 틀.

**격식 짝**: (작성)
- refined: The recentering check verifies only that the click reached the intended location; it cannot determine whether that location was correct in the first place.
- plain: The check just makes sure it clicked where it meant to. It has no idea if that was the right place.

<sub>출처: transcript:auto-recipe-creator (틀린 점에서 OK 를 누른 사고 분석)</sub>
