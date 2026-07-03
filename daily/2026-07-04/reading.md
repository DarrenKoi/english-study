# 2026-07-04 — 정독

## 단락 1

Most likely the key genuinely isn't well-framed at 6.00k — the FOV is zoomed or panned away from the registered view, so nothing on screen forms a sharp, unique match. OM/SEM views of semiconductor patterns are **highly periodic** — arrays of near-identical cells, lines, and vias. The align key region looks like many other regions, so the chamfer score surface is flat: the true peak barely beats its periodic neighbors. So the matcher is being honest: "I think it's here, but I **can't rule out** that identical-looking place 20 µm over." For an automated reposition, locking onto the wrong periodic instance is dangerous, so it escalates to ambiguous rather than auto-correcting — which is exactly correct behavior, even though it looks visually close to you.

**문법·구조**: ① `Most likely` 를 문두 부사로 세워 확신도를 먼저 깔고 시작 — 뒤 문장 전체가 추정임을 한 단어로 표시한다. ② `isn't well-framed`, `is zoomed or panned away` 처럼 수동태가 연속되는데, 행위자(장비·엔지니어)가 아니라 *화면 상태*가 논점이기 때문이다. ③ `so ~, so ~` 로 인과를 짧게 이어가다 마지막 문장에서 `rather than auto-correcting`(대안 배제) + `which is exactly correct behavior`(계속적 용법 관계절로 앞 절 전체를 평가) 로 매듭짓는 흐름이 전형적인 진단 서술 구조다.
**핵심 표현**: `well-framed`(화면에 잘 잡힌), `can't rule out`(배제할 수 없다 — 불확실성을 정직하게 남기는 부정형), `escalate to X rather than Y`(자동 처리 대신 상위 판단으로 넘기다).
**격식 짝**: refined — "It escalates to engineer review rather than committing to an uncertain match." ↔ plain — "It kicks it up to a human instead of guessing." (작성)

<sub>출처: transcript:auto_recipe_creator (score 해석 세션)</sub>

---

## 단락 2

What was wrong: RCS relays the local PC's mouse *movement* to the remote tool. A single `mouse.position = (x, y)` assignment is an instantaneous teleport — one OS event — which RCS samples right past, so the remote cursor never actually entered the live SEM box. That's why the captured frame showed the pointer outside the box and the wheel hit the wrong panel. The fix is to emit a stream of small move events — a glide — and then a tiny jiggle on arrival, so RCS tracks the cursor all the way into the box and registers it at rest there before the wheel fires. This belongs in the mouse primitive, not the ladder: every RCS cursor move benefits, and the gating is unchanged.

**문법·구조**: ① `What was wrong:` — 의문사절을 명사로 세운 표제형 도입. 보고서에서 `What changed:` / `What I found:` 로 응용 빈도가 높다. ② `which RCS samples right past` — 전치사가 뒤에 남는 관계절(sample past X = X를 지나쳐 샘플링하다). ③ `so that` 대신 `so RCS tracks ... and registers ...` 로 목적을 가볍게 잇고, 시간 순서를 `before the wheel fires` 종속절로 고정. ④ 마지막 문장 `This belongs in X, not Y` 는 수정의 *위치*(어느 계층에 고칠 것인가)를 논증하는 설계 문형.
**핵심 표현**: `samples right past (it)`(그냥 지나쳐 버린다 — right 가 "완전히"를 강조), `at rest`(정지 상태로), `belongs in the primitive, not the ladder`(수정은 공용 프리미티브 계층에 있어야 한다).
**격식 짝**: refined — "The correction belongs in the shared primitive so that every caller benefits." ↔ plain — "Fix it in the low-level helper — then everyone gets it for free." (작성)

<sub>출처: transcript:auto_recipe_creator (RCS glide 세션)</sub>

---

## 단락 3

The riskiest miss was hidden by my own first filter: I excluded lines containing `align_images` to skip the intentional data path, which also masked one file's stale run-path, because the filename contains the substring. The full re-grep after editing caught it — a reminder that a too-clever exclusion filter can hide real hits, so always re-scan unfiltered before declaring done. The debug-path fixes, meanwhile, were verifiable rather than guessed: the test actually wrote its summary to the new directory at runtime, proving the docstring now matches what the code does. Tracing the code before editing a "doc-only" line is what separated stale-but-correct from stale-and-wrong.

**문법·구조**: ① `was hidden by my own first filter` — 수동태 + `my own` 으로 "내 손으로 만든 필터가 나를 가렸다"는 자기 귀책을 압축. ② `, which also masked ...` 계속적 관계절로 부작용을 덧붙이고 `because` 절로 기제를 설명하는 3단 문장. ③ `a reminder that ...` 동격 명사구 — 사건에서 교훈으로 승격시키는 회고의 관용 장치. ④ 마지막 문장은 동명사구(`Tracing the code ...`)를 주어로 세우고 `what separated A from B` 의사분열문으로 결정적 요인을 강조한다. `stale-but-correct` / `stale-and-wrong` 같은 하이픈 합성 형용사 대비도 눈여겨볼 것.
**핵심 표현**: `a too-clever exclusion filter`(과하게 영리해서 탈이 난 필터), `before declaring done`(완료 선언 전에), `verifiable rather than guessed`(추측이 아니라 검증 가능한).
**격식 짝**: refined — "Re-scan the tree unfiltered before declaring the migration complete." ↔ plain — "Grep the whole thing one more time with no filters before you call it done." (작성)

<sub>출처: transcript:auto_recipe_creator (docstring 일괄 정리 회고)</sub>
