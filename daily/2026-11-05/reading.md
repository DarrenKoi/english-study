# 2026-11-05 — 정독

## 단락 1

This is about what's available, not error handling — if a dedicated MCP tool errors, debug or report it rather than silently retrying via a slower tier. **Look before you assert.** If the user asks about app state (what's open, what's connected, what an app can do), take a screenshot and check before answering. Don't answer from memory — the user's setup or app version may differ from what you expect. If you're about to say an app doesn't support an action, that claim should be grounded in what you just saw on screen, not general knowledge. Similarly, `list_granted_applications` or a fresh `screenshot` is cheaper than a wrong assertion about what's running.

**문법·구조**: 명령문이 주를 이루는 지침인데, 명령마다 **조건 → 명령 → 이유** 가 짝지어 나옵니다. 첫 문장은 `This is about X, not Y` 로 범위를 먼저 좁히고, 대시 뒤 `if ..., debug or report it rather than silently retrying` 에서 `rather than + -ing` 로 "하지 말아야 할 쪽"을 동명사로 붙입니다. 둘째 문장 `Look before you assert.` 는 4단어짜리 원칙이고, 나머지 문장이 이걸 풀어 줍니다. 셋째 문장의 괄호 속 `what's open, what's connected, what an app can do` 는 **의문사절 세 개를 나란히** 둔 명사절이라 app state 가 무엇인지 예시로 채웁니다. 넷째 문장은 대시 뒤에 `may differ from what you expect` 로 이유를 달았고, 다섯째 문장은 `If you're about to say ...` (막 ~하려는 참이라면)로 행동 직전의 순간을 잡습니다. 여기서 명령 대신 `that claim should be grounded in` 이라는 **수동 + should** 를 써서 사람이 아니라 주장 자체에 기준을 겁니다. 마지막 `Similarly` 는 앞 원칙을 비용 비교로 한 번 더 정리하는 연결어입니다.

**핵심 표현**:
- `rather than silently retrying via a slower tier` — 조용히 우회하지 말라. silently 가 "보고 없이"라는 비판을 실어 줍니다.
- `grounded in what you just saw on screen, not general knowledge` — 주장의 근거를 직접 본 것에 둬라. `X, not Y` 대비가 첫 문장과 수미상관을 이룹니다.
- `is cheaper than a wrong assertion` — 확인 비용을 틀렸을 때의 비용과 견줘 확인 쪽을 당연하게 만듭니다.

**격식 짝**:
- refined: "Any statement about the current state of the system should be verified against direct observation before it is made." (작성)
- plain: "Don't guess — just check first, then say it." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (computer-use 지침, "Look before you assert" 절)</sub>

---

## 단락 2

**Access flow:** before any computer-use action you must call `request_access` with the list of applications you need. The user approves each application explicitly, and you may need to call it again mid-task if you discover you need another application. Finder is an application like any other: clicking the desktop, the Dock, or a Finder window (including Go to Folder) requires a Finder grant. The menu bar does not, as long as the app that is frontmost is one you already have access to. **Tiered apps:** some apps are granted at a restricted tier based on their category — the tier is displayed in the approval dialog and returned in the `request_access` response.

**문법·구조**: 절차 설명이라 **현재시제**가 줄곧 이어지고, 의무는 `must`, 가능성은 `may` 로 갈라 씁니다. 둘째 문장 `you may need to call it again mid-task if you discover you need another application` 에서는 `discover` 뒤에 접속사 that 이 생략된 명사절이 옵니다. 셋째 문장은 콜론 앞에서 `Finder is an application like any other` 로 원칙을 말하고, 콜론 뒤에 동명사 주어 `clicking the desktop, the Dock, or a Finder window` 를 세워 원칙을 구체화합니다(동명사 주어라 동사는 단수 `requires`). 넷째 문장 `The menu bar does not` 은 앞 문장의 `require a Finder grant` 를 **대동사 does** 로 받아 반복을 피했습니다. 이어지는 `as long as` 는 "~하는 한"이라는 조건이고, 그 안의 `one you already have access to` 는 관계대명사가 빠진 관계절이라 전치사 to 가 끝에 남았습니다. 마지막 문장은 **수동태 두 개**(`is displayed in`, `returned in`)를 and 로 묶습니다. 사용자가 아니라 tier 정보가 어디에 나타나는지가 관심이라 수동이 자연스럽습니다.

**핵심 표현**:
- `mid-task` — 작업 도중에. in the middle of the task 를 한 단어로.
- `an application like any other` — 특별 취급하지 않는다는 말. "예외 없음"을 부드럽게 전합니다.
- `as long as the app that is frontmost is one you already have access to` — 조건을 하나 걸어 예외의 범위를 정확히 긋습니다.

**격식 짝**:
- refined: "Additional permissions may be requested during execution should further applications become necessary." (작성 — should 도치로 if 를 대신한 격식체)
- plain: "If you need another app halfway through, just ask again." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (computer-use 지침, Access flow · Tiered apps)</sub>

---

## 단락 3

When the fourth office reply came back, the first thing it did was correct us. In the third round we had assumed that the "most recent document" in question S3 was the one with the highest `version`; the office checked and found it was the one with the latest `modified` time. That kind of mistake is cheap to fix in a reply document and expensive to discover in production. The reply also flagged something that looked off: for R7QA and R7QC, table A records the fab as R4 while table D says R3, so joining A to D on `fac_id` splits one device across two fabs. None of this is about error handling — nothing failed, and no query threw. It is about what each index actually holds, which is why the rule for the next round is simple. Look before you assert, and treat any field we have not read in the raw index as suspicious by default.

**문법·구조**: 사실(과거) → 판단(현재) → 원칙(명령) 순서로 시제가 움직입니다. 둘째 문장은 **과거완료 `had assumed`** 로 "회신이 오기 전에 이미 그렇게 가정했다"는 앞선 시점을 표시하고, 세미콜론 뒤 `found it was` 는 시제 일치로 과거를 유지합니다. 셋째 문장의 `cheap to fix ... and expensive to discover` 는 **형용사 + to부정사** 두 쌍을 대구로 놓아 비용을 대비합니다. 넷째 문장은 콜론 뒤에서 `while` 로 두 표의 값을 맞세우고 `so` 로 결과(device 가 둘로 갈림)를 냅니다. 다섯째·여섯째 문장은 단락 1의 `This is about X, not Y` 를 부정형(`None of this is about`)과 긍정형(`It is about`)으로 나눠 다시 씁니다. `which is why` 는 앞 절 전체를 받는 계속적 관계절로 결론을 엽니다.

**핵심 표현**:
- `looked off` — 확신은 없지만 이상해 보였다는 직감.
- `cheap to fix ... expensive to discover` — 확인을 미루면 비용이 커진다는 논리를 한 문장에.
- `suspicious by default` — 원본에서 읽기 전까지는 믿지 않는다는 기본값.

**격식 짝**:
- refined: "The discrepancy was identified prior to deployment, which substantially reduced the cost of remediation." (작성)
- plain: "We caught it early, so it was an easy fix." (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/office-migration/reply-device-statistics-families-261104-r4.md 의 T4 정정·R7QA/R7QC fab 불일치 내용을 오늘 표현으로 옮겨 씀</sub>
