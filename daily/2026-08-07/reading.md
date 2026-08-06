# 2026-08-07 — 정독

## 단락 1

**1. Crop padding spans ~3 rows.** `_tool_row_target` sets `vertical_pad_ratio=1.0`, so the crop handed to mai-ui extends one full bbox-height above and below. In a dense list, that crop contains the row above and the row below. mai-ui can pick a neighbouring row's ID and the result is accepted — bounded by the crop, so no sanity check fires. **2. A wrong-row click is reported as "occupied."** `_exec_wait_tool_window` waits for a window titled with *your* `eqp_id`. If you double-clicked the wrong tool, the wrong tool's window opens, the wait for your title fails, and the step returns `failure_class="rcs_occupied"`. Teardown then calls `close_tool(eqp_id)`, which matches on your ID, so the wrongly-opened tool window is left open on the RCS session.

**문법·구조**: 두 메커니즘을 굵은 소제목 + 설명으로 병렬 배치했고, 각 덩어리 안에서 시제가 일관되게 **현재형**이다. 이건 "지금 코드가 늘 그렇게 동작한다"는 일반적 진리를 말하는 자리라서 과거형을 쓰지 않는다. 둘째 덩어리의 `If you double-clicked …, the window opens, the wait fails, and the step returns …`는 조건절만 과거형(가정이 아니라 **선행 사건**)이고 주절은 현재형인 혼합 시제인데, "그 일이 일어났다면 그 뒤엔 늘 이렇게 된다"를 자연스럽게 만든다. 결과절 세 개를 `A, B, and C` 로 이어 인과 사슬을 한 문장에 담은 것도 눈여겨볼 만하다. 마지막 문장의 `which matches on your ID, so …`는 관계절이 원인을 대고 `so`가 결과를 받는 구조라, 이유를 따로 문장으로 떼지 않고 흐름 안에서 처리한다. `bounded by the crop, so no sanity check fires`는 주어·동사가 생략된 분사구로, 앞 절의 결과를 군더더기 없이 덧붙이는 기술 문서 특유의 압축이다.

**핵심 표현**: `spans ~3 rows`(범위가 세 행에 걸친다 — 수치 앞의 `~`를 "roughly"로 읽는다), `is left open`(닫히지 않은 채 남겨진다 — 행위자를 감추는 수동태가 "아무도 안 닫는다"를 정확히 표현), `masquerades as`의 사촌인 `is reported as`(실제와 다르게 보고된다).

**격식 짝**: (작성)
- refined: The stray window persists because the teardown routine matches solely on the requested equipment ID.
- plain: The other tool's window just stays open, since close only looks for *your* ID.

<sub>출처: transcript:auto_recipe_creator (RCS tool 선택 실패 분석)</sub>

---

## 단락 2

Either way, on the evidence so far no combo produced a single wrong-row click across 144 runs, so the list-tab task doesn't discriminate between these models the way I suggested it might. If the tool-window bench also comes back with zero wrong, the honest verdict is that both models are adequate here and you can choose on latency and operational simplicity — which is a legitimate reason to drop one, just not the reason I implied earlier. What the bench cannot see matters here: it ran on a single frame where the tools were visible. It never exercised the "tool not in this frame → maximize → scroll" path, the window-activation path, or anything after the double-click. Your real failures live in one of those.

**문법·구조**: 자기 주장을 스스로 철회하는 단락인데, 한 번도 사과하지 않는다. 비결은 **조건문의 사용**이다. `If the tool-window bench also comes back with zero wrong, the honest verdict is that …` — 결론을 단정 대신 조건 아래 두어, 아직 안 나온 데이터를 존중한다. `the way I suggested it might`은 관계부사 `the way`가 이끄는 절에 조동사 `might`가 남아 "내가 그럴 수도 있다고 했던 방식대로는"이라는 미묘한 자기지시를 만든다. 대시 뒤의 `which is a legitimate reason to drop one, just not the reason I implied earlier`는 앞 절 전체를 받는 계속적 관계절이고, `just not …`이 문장을 반쯤 되돌린다 — 결론은 살리고 근거만 취소하는 기술이다. 마지막 세 문장은 시제가 현재(`cannot see`) → 과거(`ran`, `never exercised`) → 현재(`live`)로 움직이는데, "도구의 한계(항상 참) → 이번 실행의 사실(과거) → 그래서 지금 어디를 봐야 하나(현재)"라는 논리 이동을 시제가 그대로 따라간다.

**핵심 표현**: `on the evidence so far`(지금까지 나온 증거로는 — 잠정 결론의 표준 서두), `doesn't discriminate between`(둘을 갈라내지 못한다 — 차별이 아니라 "구별력"의 뜻), `the honest verdict is that …`(솔직한 판정은 ~다 — 듣기 싫은 결론을 꺼낼 때의 완충).

**격식 짝**: (작성)
- refined: The absence of wrong-row clicks across 144 runs provides no basis for preferring either model on this task.
- plain: 144 runs, zero wrong rows — this test just can't tell them apart.

<sub>출처: transcript:auto_recipe_creator (벤치 결과 재해석)</sub>

---

## 단락 3

Two things about how to read it. Repeats aren't padding. The digest reports a `stab` column — how often repeats of the same combo agree. Your symptom is intermittent, so a combo with equal accuracy but lower stability is the worse choice, and one run per combo cannot see that. The verdict line is advisory. It flags whether the best single-model combo matches or beats production, but if the margin is inside run-to-run noise, treat it as "no evidence two models are needed" rather than proof — and consider more repeats or more tools before dropping a model. If a tool ID isn't visible in the captured frame, every combo scores `no_detect` for it — that's a config problem, not a model result, so drop that tool rather than reading it as failure.

**문법·구조**: 사용 설명이 아니라 **오독 방지 설명**이라, 세 문단이 모두 "이렇게 읽지 마라"의 형태를 띤다. 짧은 단정문(`Repeats aren't padding.` / `The verdict line is advisory.`)을 소제목처럼 앞세우고 그 뒤에 근거를 붙이는 리듬이 반복되는데, 문장 길이의 장단이 여기서 나온다. `treat it as "no evidence two models are needed" rather than proof`는 `treat A as B rather than C` 구문으로, 해석의 선택지를 명령형으로 지정한다 — 판단을 상대에게 넘기지 않고 기준을 준다. 마지막 문장의 `that's a config problem, not a model result, so drop that tool rather than reading it as failure`는 오늘 배치에서 계속 나오는 `X, not Y` 대조 + `rather than -ing` 조합이다. 동명사 `reading`이 앞의 `drop`과 병렬을 이루는 점도 정확하다.

**핵심 표현**: `advisory`(구속력 없는 참고용 — blocking의 반대), `equal accuracy but lower stability`(정확도는 같지만 안정성이 낮은 — 두 지표를 저울에 올리는 정형구), `rather than reading it as failure`(그걸 실패로 읽지 말고).

**격식 짝**: (작성)
- refined: The verdict line is advisory and should not be treated as a decision criterion on its own.
- plain: Take the verdict line as a hint, not a call.

<sub>출처: transcript:auto_recipe_creator (bench 사용 안내)</sub>
