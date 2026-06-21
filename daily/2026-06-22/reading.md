# 2026-06-22 — 정독

## 단락 1

Your dev setup is the real reason this matters: the Mac can't drive RCS, but it can run CV on synthetic images. The `vision/` package sits in Layer 2 and never imports `rcs/` or `monitor/`. So `test_align_key_match.py` runs on your Mac with zero RCS — and that's only possible because the layers don't tangle. The `rcs/` package, which is Windows-only, is quarantined, and nothing in `vision` or `vlm` drags in a Windows dependency. The `monitor/` package is the one place where "this only runs at the office" lives, because it's the only thing that wires GUI, alarms, and correction together. If these were one flat folder, importing the CV matcher would transitively pull in `pywinauto`, and nothing would run on your Mac.

**문법·구조**: 흐름이 **원인→결과**로 촘촘히 묶여 있습니다. 둘째 문장의 `So ... — and that's only possible because ...`는 결과(`So`)를 던진 뒤 대시로 끊고 `because`로 근거를 덧대는 구어적 설명 리듬입니다. 셋째 문장 `which is Windows-only`는 **비제한 관계절**(콤마로 감싸 부가 정보)로, 핵심 절(`is quarantined`)을 끊지 않고 배경만 끼워 넣습니다. 마지막 문장은 **가정법 과거**(`If these were ... would pull in ... would run`) — 실제로는 한 폴더가 아니므로 "만약 그랬다면"의 반사실 가정입니다. `were`(was 아님)가 가정법 신호입니다.
**핵심 표현**: `the layers don't tangle`(계층이 서로 엉키지 않는다 — 코드 구조 비유), `is quarantined`(격리돼 있다), `transitively pull in`(의존성을 줄줄이 끌어온다).
**격식 짝**: "계층이 엉키지 않아 가능하다"를 — refined: *This is feasible only because the layers remain cleanly decoupled.* / plain: *It only works because the layers don't get tangled up.* (작성)

<sub>출처: transcript:[assistant] auto_recipe_creator (모듈 분리 설명)</sub>

---

## 단락 2

The overall pattern is well-established and sound: heterogeneous proposal generators, a shared quality scorer, and argmax selection are exactly what Selective Search, RPN, and RANSAC hypothesis competition do. The individual score components are reasonable but hand-tuned rather than derived from a published metric. The main fragility is the outermost-wall selection and the area-first pruning, both of which can discard the correct candidate before the good scorer ever sees it.

**문법·구조**: 전형적인 **평가 결론** 단락입니다. 첫 문장은 콜론(`:`)으로 "주장 → 근거(나열)"를 잇고, `are exactly what X, Y, and Z do`라는 **관계절 강조 구문**으로 "바로 ~가 하는 일"이라고 못 박습니다. 둘째 문장의 `reasonable but hand-tuned rather than derived`는 `A but B rather than C` 골격 — 인정(A)하면서 한계(B)를 짚고 그 대비(C)를 명시하는, 리뷰에서 균형 잡힌 평가를 줄 때의 단골 패턴입니다. 셋째 문장 `both of which can discard ...`는 **비제한 관계절**로 앞의 두 약점을 한꺼번에 받아 부연합니다. `before the good scorer ever sees it`의 `ever`는 "아예 보기도 전에"라는 강조.
**핵심 표현**: `well-established and sound`(정립됐고 견실하다), `hand-tuned rather than derived`(원리 유도가 아니라 손으로 맞춘), `the main fragility is`(가장 큰 취약점은 ~다).
**격식 짝**: "이 수치들은 원리에서 나온 게 아니라 손으로 맞춘 것"을 — refined: *These constants are empirically tuned rather than analytically derived.* / plain: *These numbers were just hand-picked, not worked out from theory.* (작성)

<sub>출처: transcript:[assistant] auto_recipe_creator (codex 평가)</sub>
