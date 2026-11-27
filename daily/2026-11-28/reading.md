# 2026-11-28 — 정독

## 단락 1

An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus marks the visible tab as seen, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion while the pane is unseen. With no foreground client, a new completion in the globally active tab is treated as seen while completions in background tabs still become `done`.

**문법·구조**: 명세서 문체의 정석입니다. 모든 문장이 **현재 시제**예요. 미래의 동작도 "규칙"으로 서술하면 현재형을 씁니다(`it reports`, `becomes`). 조건은 세 가지 장치로 나눠 걸었습니다. 시간 조건은 `after` / `when`, 동시 조건은 `while`, 가정은 `if` 가 맡아요. 다섯째 문장은 동명사 세 개(`Focusing…, switching…, or regaining…`)가 한꺼번에 주어가 되고, `so` 로 결과를 잇습니다. 여섯째 문장에서는 세미콜론이 "아니다"와 "그럼 무엇이 만드는가"를 한 문장에 붙여요. 마지막 문장의 `is treated as seen` 은 판단 주체를 감춘 수동태라 규칙이 시스템 자체의 성질처럼 읽힙니다.

**핵심 표현**:
- `including in a background pane` — 앞 문장에 예외처럼 보이는 경우를 덧붙여 "여기도 마찬가지"라고 못 박습니다. `including` 뒤에 전치사구가 바로 와도 됩니다.
- `turn A into B` — 상태를 바꾸다. 부정문(`does not turn an existing idle status into done`)으로 "이 동작은 이런 변화를 일으키지 않는다"를 분명히 합니다.
- `even in the active tab` — `even` 이 "예상과 달리 여기서도"를 더합니다.

**격식 짝**:
- refined: Regaining focus marks the visible tab as seen. ↔ plain: Once you click back into the tab, it counts as seen.
- refined: `done` is created by a later completion while the pane is unseen. ↔ plain: You only get `done` if something finishes while nobody's looking at that pane.

<sub>출처: transcript:arc-engine 466d352b (herdr 스킬 문서)</sub>

---

## 단락 2

Most teams that run computer-use in production do not let the model look at every screen from scratch. Instead, they replay a recorded path deterministically and call the model only on the steps where the screen has changed. On the healthy path, this means zero model calls; when a step fails its precondition check, the system walks down a resolution ladder that ends with a closed VLM question. The model is asked which branch the screen is in — A, B, or unknown — and an unknown answer goes straight to a human. Because most agent failures are false success, an independent verifier then compares the screen with the expected result. Trial-and-error tuning follows the same logic, with the work split three ways: the LLM proposes a value, a deterministic scoring function judges it, and restricted tools apply it within a fixed range. None of this is new technology, but it is what keeps a small model usable on long tasks.

**문법·구조**: 첫 문장은 `do not let + 목적어 + 동사원형` 사역 구문으로 "하지 않는 것"부터 말하고, 둘째 문장의 `Instead` 가 대안으로 방향을 틉니다. 셋째 문장은 세미콜론으로 정상 경로와 실패 경로를 한 문장 안에서 대비해요. 넷째 문장의 `is asked which branch…` 는 간접의문문이 목적어 자리에 들어간 수동태입니다. 다섯째 문장은 `Because` 절로 이유를 먼저 깔고 `then` 으로 순서를 표시했어요. 여섯째 문장의 `with the work split three ways` 는 오늘 표현 `with the summary block stripped` 와 같은 `with + 명사 + 과거분사` 부대상황 구문이고, 콜론 뒤에 역할 셋을 같은 꼴로 늘어놓습니다. 마지막은 `None of this is …, but it is what keeps …` 로 양보 뒤 주장을 세우는데, `what` 관계대명사절이 보어 자리에서 "바로 그것"을 강조합니다.

**핵심 표현**:
- `from scratch` — 처음부터, 아무 기억 없이. 매 실행마다 화면을 새로 해석하는 비효율을 짚을 때.
- `walks down a resolution ladder` — 사다리를 한 칸씩 내려가며 폴백을 시도한다는 비유. `walk through` 와 달리 순서가 정해진 단계라는 느낌이 강합니다.
- `goes straight to a human` — 중간 단계 없이 바로 사람에게 간다. `escalate to` 보다 구어적입니다.

**격식 짝**:
- refined: An unknown answer is escalated to a human operator. ↔ plain: If it says "unknown," a person takes over.
- refined: The system invokes the model only for steps whose preconditions fail. ↔ plain: We only call the model when a step doesn't look the way it should.

<sub>출처: 모범 단락(작성) — 오늘 표현(on the healthy path, resolution ladder, a closed VLM question, false success, splits the work three ways)을 녹여 씀</sub>
