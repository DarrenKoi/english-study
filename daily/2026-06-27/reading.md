# 2026-06-27 — 정독

## 단락 1

A framework-free pure util (`madOutliers.ts`) computes per-point boolean flags from a numeric array. `AnalyzePanel`'s `timeSeriesPoints` computed runs it over the selection's means and stds, attaching an `outlier` flag to each `TimeSeriesPoint`. `TimeSeriesChart` reads that flag to style the `mean` series per-datum (color + symbol size) and adds one tooltip line. Detection is relative to the current selection, so it stays in the frontend.

**문법·구조**: 네 문장이 모두 **현재시제(단순현재)** 입니다. 코드·시스템이 *늘 그렇게
동작한다*는 일반적 사실을 기술할 때 영어는 과거나 미래가 아니라 **단순현재**를 씁니다
(computes / runs / reads / stays). 셋째 문장의 `reads that flag **to style** … **and adds** …`
는 **to부정사(목적)** 와 등위접속 `and` 로 두 동작을 한 흐름에 묶습니다 — "플래그를 읽어서
(그 목적이) 스타일링하고 + 한 줄 추가". 둘째 문장의 `attaching an outlier flag …` 는
**분사구문(현재분사)** 으로, 앞 절(`runs it …`)에 *부수적으로 따라오는 동작*을 콤마 뒤에
가볍게 덧붙입니다(= "…over the means and stds, and it attaches …" 를 줄인 것). 마지막
`so it stays in the frontend` 의 **so**는 *결과* 접속사 — "선택 기준이라(원인) → 그래서
프런트에 남는다(결과)".

**핵심 표현**: `compute X from Y`(Y로부터 X를 산출하다, 데이터 변환의 표준 동사),
`run it over (the means)`(컬렉션 전체에 *훑어 적용하다*), `relative to (the selection)`
(~을 기준으로 한, 절대값이 아니라 *상대적*임을 못 박는 표현).

**격식 짝**:
- refined(문어): *Detection is relative to the current selection, so it remains a frontend concern.* (작성)
- plain(회화): *It only looks at what you've picked, so we just do it in the browser.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-26-skewvoir-cd-outlier-detection.md</sub>

---

## 단락 2

A pure consumer step inside `golden_reregister_report_cond.run()`. It reads the consensus driver's `summary.json`, normalizes the join key, classifies each recipe's fix type against a single distinctiveness floor, prioritizes worst-first, and writes the worklist next to the existing report. No change to the consensus eval and no new CV computation. New logic is pure helpers; only path resolution touches I/O.

**문법·구조**: 둘째 문장이 이 단락의 핵심 — **하나의 주어(It)에 다섯 개의 동사가
병렬(parallel)** 로 걸립니다: *reads … , normalizes … , classifies … , prioritizes … ,
and writes …*. 모두 **-s 형(3인칭 단수 현재)** 으로 형태를 맞춰, 한 단계가 하는 일을
리듬감 있게 나열합니다. 영어 기술문서에서 "이 컴포넌트는 A하고 B하고 C한다"를 쓸 때
이 **동사 병렬 + 단순현재**가 가장 깔끔한 틀입니다. 셋째 문장 `No change … and no new …`
는 **동사 없는 명사구(verbless)** 로, *하지 않는 것*을 단호하게 못 박습니다(스코프 방어).
넷째 문장의 세미콜론 `;` 은 밀접한 두 절을 한 문장으로 붙이는 격식 부호 — "새 로직은 순수
헬퍼다; (그중) I/O를 건드리는 건 경로 해석뿐."

**핵심 표현**: `classify X against (a floor)`(기준선에 *대조해* 분류하다),
`prioritize worst-first`(가장 나쁜 것부터 우선순위를 매기다), `touch I/O`(입출력을 *건드리다*
= 부수효과가 있다 ― 순수성을 논할 때의 관용 동사).

**격식 짝**:
- refined(문어): *Only path resolution touches I/O; the rest is pure.* (작성)
- plain(회화): *The only part that actually hits the disk is figuring out the paths — everything else is just plain functions.* (작성)

<sub>출처: repo:auto_recipe_creator poc/workflow_2/docs/plans/2026-06-26-reregister-phase3-rank1-worklist-plan.md</sub>
