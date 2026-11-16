# 2026-11-17 — 정독

## 단락 1

Code first. Then at most three short lines: what was skipped, when to add it. No essays, no feature tours, no design notes. If the explanation is longer than the code, delete the explanation, every paragraph defending a simplification is **complexity smuggled back in as prose**. Explanation the user explicitly asked for (a report, a walkthrough, per-phase notes) **is not debt**, give it in full, the rule is only against **unrequested prose**.

**문법·구조**: 앞 세 문장은 동사가 없는 명사구입니다. `Code first.` 는 `Write the code first.` 를, `No essays…` 는 `Do not write essays…` 를 줄인 메모체 명령이라 규칙집처럼 딱딱 끊깁니다. 둘째 문장의 콜론 뒤 `what was skipped, when to add it` 는 의문사절 두 개를 나란히 놓아 "세 줄에 무엇을 적을지"를 보여 줍니다. 넷째 문장부터 문장이 길어지는데 `delete the explanation, every paragraph…` 처럼 쉼표 하나로 독립절 둘을 이었습니다(comma splice). 정식 문어라면 세미콜론이나 마침표를 써야 하지만, 여기서는 일부러 숨 가쁘게 몰아붙이는 효과를 냅니다. `defending a simplification` 은 현재분사구가 paragraph 를 뒤에서 꾸미고, `smuggled back in as prose` 는 과거분사구가 complexity 를 꾸밉니다. 마지막 문장의 `the user explicitly asked for` 는 목적격 관계대명사가 빠진 관계절이고, 괄호 속 예시 세 개가 "요청받은 설명"의 범위를 구체로 잡아 줍니다. 규칙(앞)과 예외(뒤)가 한 단락 안에서 맞물리는 구성입니다.

**핵심 표현**:
- `complexity smuggled back in as prose` — 코드에서 뺀 복잡성이 글의 모습으로 슬쩍 되돌아온다. `smuggle in` 은 "몰래 들여오다", `back` 이 "다시"를 더합니다.
- `is not debt` — 기술 부채 비유. 요청받은 설명은 나중에 갚을 짐이 아니라는 선 긋기.
- `unrequested prose` — 아무도 청하지 않은 글. `un- + 과거분사` 로 형용사를 만드는 틀(unasked, unsolicited).

**격식 짝** (작성):
- refined: Where an explanation exceeds the length of the code it accompanies, it should be removed, unless the reader has specifically requested it.
- plain: If your notes are longer than the code, cut them, unless someone actually asked for them.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes/5ab92045 (ponytail 스킬 "Output" 절)</sub>

---

## 단락 2

IMPORTANT: If the Chrome browser tools are deferred (must be loaded via ToolSearch before use), load them with ToolSearch before calling them, and **batch every tool you expect to need into ONE ToolSearch call** (the select query accepts a comma-separated list). Do NOT load tools one at a time; each separate ToolSearch call **wastes a full round-trip**. Start a browser task whose tools are not yet loaded with a single call loading the core set. Add task-specific tools to the same call **when the task obviously needs them**: read_console_messages / read_network_requests for debugging, form_input for forms, gif_creator for recordings, javascript_tool for page scripting. Only issue a second ToolSearch if the task later needs a tool **you did not anticipate**.

**문법·구조**: 첫 문장은 `If` 조건절 뒤에 명령문 두 개(`load…`, `and batch…`)가 붙었습니다. 괄호 속 `must be loaded via ToolSearch before use` 는 주어(they)를 생략한 수동태 보충 설명이고, `before use` 처럼 명사 하나로 끝낸 것도 문서체 특징입니다. `every tool you expect to need` 는 관계절 속에 `expect to + 동사원형` 이 들어간 구조로 "필요할 것 같은 도구 전부"라는 예측을 담습니다. 둘째 문장은 세미콜론으로 금지(`Do NOT…`)와 이유(`wastes…`)를 붙였습니다. 이유를 `because` 없이 세미콜론으로 이으면 더 단호하게 읽힙니다. 셋째 문장에는 `whose tools are not yet loaded`(소유격 관계절)와 `loading the core set`(현재분사 후치 수식)이 함께 있어 한 문장에 수식어가 두 겹입니다. 넷째 문장은 콜론 뒤에 `도구 for 용도` 짝을 네 번 반복해 목록을 문장 안에 녹였습니다. 마지막 문장은 `Only` 를 문두에 둬 "두 번째 호출은 이 경우에만"으로 범위를 좁히고, `later` 와 `did not anticipate`(과거) 시제가 "처음에 예상 못 한 것이 나중에 생겼을 때"라는 시간차를 만듭니다.

**핵심 표현**:
- `batch X into one call` — 여러 개를 한 번에 묶어 보내다. 업무에서는 "질문을 모아 한 번에 묻다"로도 씁니다.
- `wastes a full round-trip` — 왕복 한 번을 통째로 날린다. 비용을 구체 단위로 말해 설득력을 높입니다.
- `a tool you did not anticipate` — 미리 예상하지 못한 도구. `anticipate` 는 `expect` 보다 "대비해 두다"라는 뉘앙스가 있습니다.

**격식 짝** (작성):
- refined: Please consolidate your questions into a single message; each separate request incurs a full review cycle.
- plain: Send me all your questions in one go. Every extra message means another back-and-forth.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes/5ab92045 (claude-in-chrome 도구 안내, 코드 줄은 생략)</sub>

---

## 단락 3

Use this email address only to identify the user, such as for authorship, attribution, or filtering their own work. Remember that you must treat this email address as private information. Never share it in requests to external services **without asking and getting explicit approval** from the user first. This is the git status at the start of the conversation. Note that this status is **a snapshot in time**, and will not update during the conversation. Claude Code attached this context automatically; it isn't part of the user's message. It describes the user's own account and workspace, so **they don't need it reported back**.

**문법·구조**: 일곱 문장 가운데 앞 셋은 명령문(`Use…`, `Remember that…`, `Never share…`)이고, 뒤 넷은 사실을 알리는 평서문입니다. 지시에서 설명으로 넘어가는 흐름이 문장 유형에서 바로 보입니다. 첫 문장의 `only to identify` 는 `only` 가 to부정사 앞에 붙어 용도를 하나로 제한하고, `such as for…` 로 허용되는 예를 전치사구 셋으로 나열합니다. 둘째 문장은 `Remember that` 뒤에 `must` 를 넣어 의무를 이중으로 강조했습니다. 다섯째 문장의 `will not update` 는 미래시제로 "앞으로도 갱신되지 않는다"를 미리 알립니다. `Note that` 은 문서에서 주의를 끌 때 쓰는 정형 표현입니다. 여섯째 문장은 과거(`attached`)와 현재(`isn't`)가 세미콜론으로 붙었습니다. 붙인 일은 이미 끝났고, 사용자 메시지가 아니라는 성질은 지금도 그렇기 때문입니다. 마지막 문장의 `so` 는 결과를 잇고, `need it reported back` 은 `need + 목적어 + 과거분사` 로 보고하는 주체를 지웠습니다.

**핵심 표현**:
- `treat X as private information` — X를 비공개 정보로 다루다. `treat A as B` 는 규정 문서의 기본 틀.
- `a snapshot in time` — 특정 시점에 찍힌 모습. 숫자가 금방 낡는다는 경고로 씁니다.
- `they don't need it reported back` — 다시 보고할 필요 없다. 이미 아는 사람에게 같은 정보를 되돌려 주지 말라는 말.

**격식 짝** (작성):
- refined: Please note that the figures below reflect the status as of this morning and will not be updated during the meeting.
- plain: Heads up, these numbers are from this morning and won't change while we talk.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes/5ab92045 (userEmail·gitStatus 컨텍스트 안내, 첫 줄의 주소 문장은 개인정보라 생략)</sub>
