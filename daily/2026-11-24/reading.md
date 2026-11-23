# 2026-11-24 — 정독

두 단락 다 세션에 실린 영어 안내문에서 그대로 옮겼습니다. 단락 1은 ponytail 규칙에서 "게을러도 되는 것과 안 되는 것"을 가르는 대목이고, 단락 2는 computer-use 서버가 도구 선택 순서를 정한 대목입니다. 앞은 짧은 문장을 쌓아 주장을 세우고, 뒤는 조건문을 되풀이해 절차를 세웁니다.

## 단락 1

Never lazy about understanding the problem. The ladder shortens the solution, never the reading. Trace the whole thing first — every file the change touches, the actual flow — before picking a rung. Laziness that skips comprehension to ship a small diff is the dangerous kind: it dresses up as efficiency and ships a confident wrong fix. Read fully, then be lazy.

**문법·구조**: 다섯 문장 가운데 완전한 평서문은 둘뿐입니다. 첫 문장은 주어와 동사를 뺀 조각(`[Be] never lazy about …`)이라 구호처럼 읽혀요. 둘째 문장은 `shortens the solution, never the reading` 으로 동사 하나에 목적어 둘을 걸고 뒤쪽을 `never` 로 부정합니다. `not A but B` 를 뒤집어 `B, never A` 로 쓴 꼴입니다. 셋째 문장은 대시 사이에 `the whole thing` 을 풀어 주는 동격 명사구 둘을 끼웠고, `before picking a rung` 의 `before + -ing` 로 순서를 못박았습니다. 넷째가 가장 길어요. 주어 `Laziness` 에 관계절 `that skips comprehension to ship a small diff` 가 붙고, `to ship` 은 목적의 부정사입니다. 콜론 뒤에서 `it` 이 그 게으름을 받아 동사 둘(`dresses up`, `ships`)로 왜 위험한지 풉니다. 시제는 모두 현재라서 한 번 있었던 일이 아니라 늘 그런 성질을 말합니다. 마지막 문장은 명령 둘을 `then` 으로 이어 앞의 네 문장을 순서 하나로 접었습니다.

**핵심 표현**: `the dangerous kind` 는 `kind` 뒤에 `of laziness` 가 빠진 말로, "게으름에도 종류가 있는데 이건 위험한 쪽"이라고 갈라 줍니다. `dress up as` 는 분장하다, 곧 겉모습을 꾸민다는 뜻이에요. `pick a rung` 의 `rung` 은 사다리 가로대인데, 앞에서 해결책 후보를 사다리 칸에 빗댔기 때문에 나온 말입니다.

**격식 짝** (작성):
- refined: Economy of effort must never come at the expense of understanding the problem.
- plain: Be lazy about the code, not about figuring out what's wrong.
- refined: A change made without tracing the full flow may appear efficient while being incorrect.
- plain: If you skip the reading, your small fix just looks smart and is wrong.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task-arc-tf/77eb8e9c (ponytail 규칙)</sub>

---

## 단락 2

Dedicated MCP for the app — if the task is in an app that has its own MCP (Slack, Gmail, Calendar, Linear, etc.) and that MCP is connected, use it. API-backed tools are fast and precise. Chrome MCP — if the target is a web app and there's no dedicated MCP for it, use the browser tools. DOM-aware, much faster than clicking pixels. If the Chrome extension isn't connected, ask the user to install it rather than falling through to computer use. Computer use — for native desktop apps (Maps, Notes, Finder, Photos, System Settings, any third-party native app) and cross-app workflows. Computer use IS the right tool here — don't decline a native-app task just because there's no dedicated MCP for it. This is about what's available, not error handling — if a dedicated MCP tool errors, debug or report it rather than silently retrying via a slower tier.

**문법·구조**: 세 단계가 같은 틀로 되풀이됩니다. "이름 — `if` 조건, 명령. 이유." 순서예요. 이유 문장은 갈수록 줄어서 `API-backed tools are fast and precise.` 는 완전한 문장인데 `DOM-aware, much faster than clicking pixels.` 는 주어와 동사가 빠진 형용사구입니다. 앞에서 틀을 익혔으니 생략해도 읽힙니다. `an app that has its own MCP` 는 주격 관계절이고, `if` 절 안에서 `and` 가 조건 둘(전용 MCP 가 있다, 연결돼 있다)을 묶어요. `rather than` 은 두 번 나오는데 둘 다 `-ing` 를 받습니다(`falling through`, `silently retrying`). 명령문 뒤에서 "이쪽 말고"를 붙이는 자리입니다. `just because … ` 는 `don't` 와 짝이 되어 "~라는 이유만으로 ~하지는 마라"가 됩니다. 대문자 `IS` 는 글로 낸 강세로, 말로 하면 `is` 를 세게 읽는 것과 같아요. 마지막 문장의 `This is about A, not B` 는 앞 내용의 범위를 좁히는 틀이고, `errors` 는 여기서 동사("오류를 내다")입니다.

**핵심 표현**: `fall through to` 는 위 단계가 안 맞아서 아래 단계로 떨어져 내려간다는 말로, `switch` 문의 fall-through 와 같은 그림입니다. `decline a task` 는 `refuse` 보다 정중한 거절이에요. `a slower tier` 의 `tier` 는 층·등급으로, 앞의 1·2·3 단계를 가리킵니다.

**격식 짝** (작성):
- refined: Where a dedicated integration exists and is connected, it should be used in preference to general-purpose tools.
- plain: If the app has its own tool and it's hooked up, just use that.
- refined: A tool failure should be investigated or reported rather than masked by a silent retry through a slower channel.
- plain: If the tool breaks, fix it or say so. Don't quietly try the slow way.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task-arc-tf/77eb8e9c (computer-use 서버 설명, 번호 목록을 이어 붙임)</sub>
