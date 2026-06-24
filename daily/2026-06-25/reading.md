<sub>2026-06-25 · 정독</sub>

## 단락 1

RRF can only fuse candidates that reached each member's top-K. In the 0.2–0.3 regime the true point is often in **no** member's top-K — that *is* the `gt_in_topk` ~68% bottleneck — so RRF never sees it. Dense accumulation sums the true point's weak-but-consistent response across members **even when no single member ranked it**, so a weak-everywhere peak can still rise. This attacks `gt_not_in_topk` directly.

**문법·구조**: 첫 문장은 `can only fuse candidates that reached ...` — `only`가 동사 앞에 붙어 "오직 ~만 할 수 있다"는 제한을 건다. `that reached`는 candidates를 꾸미는 관계절(과거시제 — 이미 top-K에 든 후보들). 둘째 문장의 대시(—) 삽입구 `that *is* the ... bottleneck`은 앞 절을 풀어 "그게 바로 그 병목이다"라고 동격으로 짚는데, `is`를 이탤릭으로 강조해 "다름 아닌 그것"의 어조를 준다. 셋째 문장 `even when no single member ranked it`은 양보의 부사절로, "어떤 멤버도 그걸 순위에 안 올렸어도"라는 핵심 반전을 담는다. 마지막 짧은 문장 `This attacks ... directly`는 능동·현재시제로 결론을 못박는 마무리 — 긴 설명 뒤 단문으로 끊어 강조하는 영어 글쓰기의 전형이다.
**핵심 표현**: `in the 0.2–0.3 regime`(0.2~0.3 점수대에서 — `regime`은 "(특정 조건이 지배하는) 구간/영역"). `weak-but-consistent`(약하지만 일관된 — 하이픈으로 묶어 형용사화). `a weak-everywhere peak can still rise`(어디서나 약한 신호도 합산되면 떠오를 수 있다 — `still`이 "그럼에도"의 반전).
**격식 짝**: "RRF는 각 멤버의 top-K에 든 후보만 융합할 수 있다"
- refined: *RRF can fuse only those candidates that surfaced in each member's top-K.* (작성)
- plain: *RRF only works with what already made each member's shortlist.* (작성)

<sub>출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-24-template-bank-matching-design.md</sub>

---

## 단락 2

Neither alone is enough: the VLM knows *which* rectangle is the live feed — it reads the "Optics/OM" label, recognizes the noisy wafer video, and ignores the toolbar — but its coordinates are coarse. The CV knows nothing about *what* the box is, but given a rough location it can lock onto the exact border pixels. Summing along the full side length is what makes it robust: a true box border is a long continuous line, so it accumulates a huge projection sum, while random noise inside the band averages out.

**문법·구조**: 첫 문장의 `Neither alone is enough`은 "둘 중 어느 하나만으로는 부족하다"는 부정 주어 구문. 콜론(:) 뒤로 그 이유를 풀고, 대시 삽입구로 VLM이 "하는 일"을 세 동사 `reads / recognizes / ignores`로 병렬 나열한다(현재시제 = 일반적 능력 기술). 끝의 `but its coordinates are coarse`로 한계를 대비시켜 한 문장 안에 장점·단점을 같이 담았다. 둘째 문장 `given a rough location`은 분사구문(= if it is given ...)으로 조건을 짧게 줄인 형태. 셋째 문장 `Summing ... is what makes it robust`는 동명사 주어 + `what` 강조구문으로 "바로 이것이 견고함의 원천"이라고 짚고, `while random noise ... averages out`의 `while`은 대조("반면")를 만든다.
**핵심 표현**: `lock onto`(정확히 포착·고정하다 — 레이더가 표적을 "락온"하듯). `coarse`(거친·대략적인 ↔ fine/precise). `averages out`(평균을 내면 상쇄돼 사라지다 — 노이즈가 가라앉는다는 뜻).
**격식 짝**: "어느 하나만으로는 부족하다"
- refined: *Neither mechanism is sufficient on its own.* (작성)
- plain: *Neither one cuts it by itself.* (작성)

<sub>출처: transcript:[assistant] 07b2cb20-26b2-418d-b774-d1cca7603190</sub>

---

## 단락 3

PaddleOCR-VL is a document parser, not a general screen reader. Its stable, intended pipeline is two-stage: a small detector finds and crops each text region, then the VLM recognizes one crop at a time. The office serves it the whole tool-monitor screenshot with a bare `OCR:` token, which skips that first stage — so this isn't a tuning bug, it's using a document model on a UI in the one mode it's worst at. Tuning only bounds the damage; it won't make it a trustworthy gate.

**문법·구조**: 첫 문장 `is a document parser, not a general screen reader`는 `A, not B` 대비 구문으로 정체성을 한 번에 규정한다(콤마로 부정 동격). 둘째 문장은 콜론 뒤에 `finds and crops ... then ... recognizes ...`로 파이프라인을 순서대로(then) 풀어 단계성을 보여준다. 셋째 문장의 관계대명사 `which skips that first stage`는 앞 절 전체(전체 스크린샷을 통째로 보냄)를 받아 결과를 잇고, 대시 뒤 `so this isn't a tuning bug, it's ...`로 진단을 못박는다 — 여기서도 `A, not B`의 변형(`isn't X, it's Y`)이 핵심 메시지를 만든다. 마지막 문장은 세미콜론(;)으로 두 짧은 절을 병치해 "튜닝은 피해를 줄일 뿐, 신뢰 가능한 게이트로는 못 만든다"는 결론을 대조적으로 닫는다.
**핵심 표현**: `a bare ... token`(아무 맥락 없이 토큰만 달랑 — `bare`는 "벌거벗은/최소한의"). `the one mode it's worst at`(하필 가장 못하는 그 모드에서 — 최상급 + 관계절로 "콕 집어 그 하나"). `bounds the damage`(피해를 (어떤 한도로) 억제하다 ↔ 근본 해결).
**격식 짝**: "튜닝은 피해를 줄일 뿐 근본 해결은 아니다"
- refined: *Tuning merely bounds the damage; it does not address the root cause.* (작성)
- plain: *Tuning just keeps it from getting worse — it doesn't actually fix it.* (작성)

<sub>출처: transcript:[assistant] 22bf3627-1bd1-4b13-9449-1fdc1c6721e0</sub>
