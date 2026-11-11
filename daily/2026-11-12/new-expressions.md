# 2026-11-12 — 새 표현

출처는 pm-notes 세션(0270bee8) 하나입니다. REA 문서를 최신 내용으로 고치면서 Codex에게 herdr로 같은 조사를 맡긴 대화입니다. 영어는 세션에 실린 `herdr` 스킬 문서, 하니스가 끼워 넣는 안내 문구, 어시스턴트의 짧은 영어 보고에서 골랐습니다. 두 번째 대화(english-study)는 어제 배치를 처리한 기록이라 한 문장만 가져왔습니다.

## "never construct an ID from a workspace or display number"
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, IDs and current context)
- 맥락: 식별자를 규칙으로 짐작해 만들지 말고 응답에서 읽으라고 못 박을 때(API·CLI 문서)
- 한국어: 워크스페이스 번호나 화면 번호로 ID를 조립하지 말 것
- 설명: `construct A from B` 는 "B를 재료로 A를 짜 맞추다"입니다. 바로 앞의 `Re-read … responses after mutations` 와 세미콜론으로 이어져 "다시 읽어라; 절대 만들지 마라"라는 긍정·부정 짝을 이룹니다.
- 예문: Re-read the create response after each split; never construct an ID from a workspace or display number.
- 유사어: don't guess the ID (구어), do not derive IDs from position (같은 문서의 다른 표현), don't hand-build identifiers (캐주얼)
- 반의어: read the ID from the response (응답에서 읽다)

## "which may belong to the user or another client"
- 레지스터: technical, professional
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, IDs and current context)
- 맥락: 기본값이 가리키는 대상이 내 것이 아닐 수도 있다고 경고할 때(문서·리뷰)
- 한국어: 그건 사용자나 다른 클라이언트의 것일 수도 있는데
- 설명: 쉼표 뒤 계속적 용법 `which` 로 위험을 덧붙입니다. `may belong to` 는 소유를 단정하지 않는 조심스러운 말투입니다. 문장 전체는 `Omitting a target can use the UI-focused pane, which may belong to …` 로, 동명사 주어가 "대상을 안 적으면"이라는 조건을 대신합니다.
- 예문: Omitting a target can use the UI-focused pane, which may belong to the user or another client.
- 유사어: which might not be yours (구어), which is not necessarily owned by the caller (격식), and that could be someone else's (캐주얼)

## "the same underlying semantic state with different attention state"
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Control agents through panes)
- 맥락: 이름이 다른 두 상태가 실은 같은 상태이고 한 축만 다르다고 설명할 때(설계 문서)
- 한국어: 바탕의 의미 상태는 같고, 봤는지 여부만 다른
- 설명: `underlying` 은 "겉 이름 아래에 깔린"입니다. `the same A with different B` 틀은 공통점과 차이점을 한 구에 담습니다. `attention state` 는 결과를 사용자가 봤는지를 가리키는 이 문서의 용어입니다.
- 예문: `idle` and `done` are the same underlying semantic state with different attention state.
- 유사어: two labels for one state (구어), semantically identical, differing only in X (격식), basically the same thing, just flagged differently (캐주얼)
- 반의어: two genuinely distinct states (정말 다른 두 상태)

## "Default to a sibling pane"
- 레지스터: technical, professional
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively)
- 맥락: 별말 없으면 이쪽을 고르라고 기본 동작을 정할 때(지침·컨벤션 문서)
- 한국어: 기본은 옆 pane으로 한다
- 설명: `default to X` 는 동사로 "따로 지시가 없으면 X를 택하다"입니다. `sibling` 은 같은 부모(탭) 아래 나란히 있는 것을 가리킵니다. 뒤 문장 `Do not create … unless the user explicitly requests …` 가 예외 조건을 맡습니다.
- 예문: Default to a sibling pane in the current tab and current working directory.
- 유사어: use a sibling pane unless told otherwise (풀어 쓴 형태), fall back to X (다른 선택이 실패했을 때의 기본값), go with X by default (구어)

## "Keep the user's focus in the calling pane"
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively)
- 맥락: 백그라운드 작업이 사용자의 화면·커서를 빼앗지 않게 하라고 할 때(도구 지침)
- 한국어: 사용자의 포커스는 호출한 pane에 그대로 둔다
- 설명: `keep A in B` 는 "A를 B에 머물게 하다"입니다. `the calling pane` 의 `calling` 은 "명령을 부른 쪽"이라는 현재분사 형용사로, `the caller` 와 같은 뿌리입니다.
- 예문: Split to the right with `--no-focus` to keep the user's focus in the calling pane.
- 유사어: without moving the user's focus (같은 문서의 다른 표현), don't steal focus (구어, 흔한 UI 용어), leave focus where it is (평이)
- 반의어: switch focus to the new pane (새 pane으로 포커스를 옮기다)

## "Do not pass the task as an argv prompt by default."
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively)
- 맥락: 작업 내용을 실행 인자로 넘기지 말고 대화형으로 띄운 뒤 입력하라고 할 때(CLI 지침)
- 한국어: 기본적으로는 작업을 실행 인자 프롬프트로 넘기지 않는다
- 설명: `pass A as B` 는 "A를 B 형태로 넘기다"입니다. 문장 끝 `by default` 가 금지를 누그러뜨려 "사용자가 요청하면 예외"라는 여지를 남깁니다.
- 예문: Do not pass the task as an argv prompt by default; start the TUI first and submit the task once it is idle.
- 유사어: don't put the prompt on the command line (평이), avoid one-shot invocation unless asked (격식)
- 반의어: launch non-interactively with the prompt as an argument (인자로 넘겨 비대화형 실행)

## "instead of coordinating `send-text` and `send-keys` separately"
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively)
- 맥락: 두 단계를 따로 맞추지 말고 한 번에 하는 명령을 쓰라고 권할 때(문서)
- 한국어: 두 명령을 따로 맞춰 쓰는 대신
- 설명: `coordinate A and B` 는 "A와 B의 순서·타이밍을 맞추다"입니다. `instead of + 동명사` 로 권하는 방법과 피할 방법을 한 문장에 둡니다.
- 예문: Use `pane run` for initial prompts and follow-ups instead of coordinating `send-text` and `send-keys` separately.
- 유사어: rather than juggling two commands (구어), in place of sequencing them by hand (격식), so you don't have to time them yourself (캐주얼)

## "If a wait times out, inspect … before deciding what to do."
- 레지스터: technical, professional
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Start agents interactively)
- 맥락: 시간 초과가 나면 바로 재시도하지 말고 상태부터 보라고 할 때(런북·지침)
- 한국어: 대기가 시간 초과되면, 어떻게 할지 정하기 전에 먼저 살펴본다
- 설명: `time out` 은 자동사 구동사입니다(명사는 붙여서 `timeout`). `before deciding what to do` 는 `before + 동명사 + 의문사 to부정사` 구조라 "판단은 확인 뒤"라는 순서를 문법으로 보여 줍니다.
- 예문: If a wait times out, inspect the pane's status and recent output before deciding what to do.
- 유사어: on timeout, check the state first (메모체), don't retry blindly (구어), investigate before acting (격식)
- 반의어: retry right away (곧바로 재시도)

## "Do not derive them from sidebar order or examples."
- 레지스터: technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Safety and coordination rules)
- 맥락: 값을 화면 순서나 예시에서 유추하지 말라고 할 때(지침)
- 한국어: 사이드바 순서나 예시에서 미루어 만들지 말 것
- 설명: `derive A from B` 는 "B에서 A를 이끌어 내다"입니다. 앞 문장 `Parse IDs from JSON responses.` 와 짝이 되어 `parse from`(읽기)과 `derive from`(추론)을 맞세웁니다.
- 예문: Parse IDs from JSON responses. Do not derive them from sidebar order or examples.
- 유사어: don't infer them from X (추론 쪽), don't work them out from the UI (구어), don't copy them from the docs (예시 쪽만)

## "panes, or sessions you did not create"
- 레지스터: professional, technical
- 출처: transcript:pm-notes 0270bee8 (herdr 스킬, Safety and coordination rules)
- 맥락: 자기가 만들지 않은 자원은 건드리지 말라는 범위 규칙(운영 지침·팀 합의)
- 한국어: 내가 만들지 않은 pane이나 세션
- 설명: 관계대명사 `that` 을 생략한 `sessions (that) you did not create` 입니다. 소유를 "만든 사람" 기준으로 정의하는 짧은 틀이라 정리(cleanup) 규칙에 자주 나옵니다.
- 예문: Do not close workspaces, tabs, panes, or sessions you did not create unless the user explicitly asked.
- 유사어: resources you don't own (소유 기준), anything that isn't yours (구어), pre-existing sessions (시점 기준, 격식)
- 반의어: the ones you spun up yourself (내가 띄운 것)

## "This is how Claude Code surfaces messages the user sends mid-turn"
- 레지스터: technical, professional
- 출처: transcript:pm-notes 0270bee8 (하니스 안내 문구)
- 맥락: 시스템이 어떤 정보를 "어떤 방식으로 보여 주는지" 설명할 때(제품 문서)
- 한국어: 사용자가 작업 도중에 보낸 메시지를 Claude Code는 이런 식으로 띄워 준다
- 설명: `surface` 를 타동사로 쓰면 "묻혀 있던 것을 보이게 올리다"입니다. `This is how + 절` 은 방금 본 현상을 설명으로 받는 틀입니다. `messages (that) the user sends mid-turn` 에서 관계대명사가 빠졌습니다.
- 예문: This is how the dashboard surfaces alerts that fire while a deploy is still running.
- 유사어: this is how X shows you … (평이), X presents … in this way (격식), that's how … pop up (캐주얼)
- 반의어: bury (묻어 버리다), swallow silently (조용히 삼키다)

## "take it as the current state rather than reverting it"
- 레지스터: professional, technical
- 출처: transcript:pm-notes 0270bee8 (하니스 안내 문구, 파일이 디스크에서 바뀌었을 때)
- 맥락: 누가 바꿔 놓은 것을 되돌리지 말고 지금 상태로 받아들이라고 할 때(협업 규칙)
- 한국어: 되돌리지 말고 지금 상태로 받아들여라
- 설명: `take A as B` 는 "A를 B로 받아들이다"입니다. `rather than + 동명사` 가 하지 말 행동을 붙입니다. 앞에 `That's usually deliberate, so …` 가 있어 이유(대개 일부러 한 변경)부터 깝니다.
- 예문: The config changed while you were away; that's usually deliberate, so take it as the current state rather than reverting it.
- 유사어: treat it as the source of truth (기준으로 삼다), go with what's there (구어), accept the change as given (격식)
- 반의어: roll it back (되돌리다), restore the old version (옛 버전으로 복구)

## "if the change looks wrong, say so rather than undoing it yourself"
- 레지스터: conversational, professional
- 출처: transcript:pm-notes 0270bee8 (하니스 안내 문구)
- 맥락: 이상하면 직접 고치지 말고 말부터 하라고 할 때(팀 규칙·리뷰 문화)
- 한국어: 변경이 틀려 보이면 직접 되돌리지 말고 그렇다고 말해라
- 설명: `say so` 의 `so` 는 앞 절 내용(틀려 보인다)을 받는 대용어입니다. `undo it yourself` 의 `yourself` 가 "네 손으로"를 강조해 권한의 선을 긋습니다.
- 예문: If the change looks wrong, say so rather than undoing it yourself.
- 유사어: flag it instead of fixing it (짧은 구어), raise it with the author (격식), speak up before you touch it (캐주얼)
- 반의어: quietly revert it (말없이 되돌리다)

## "otherwise no need to call it out"
- 레지스터: conversational
- 출처: transcript:pm-notes 0270bee8 (하니스 안내 문구)
- 맥락: 문제가 없으면 굳이 언급하지 않아도 된다고 덧붙일 때(구어·메모)
- 한국어: 그게 아니면 굳이 짚어 말할 필요는 없다
- 설명: `(there is) no need to …` 에서 `there is` 를 뺀 메모체입니다. `call out` 은 "콕 집어 언급하다"이고, 문맥에 따라 "공개적으로 지적하다"라는 센 뜻도 됩니다.
- 예문: Mention it if the numbers look off; otherwise no need to call it out.
- 유사어: no need to mention it (평이), it doesn't warrant a note (격식), don't bother flagging it (캐주얼)
- 반의어: worth calling out (짚어 둘 만하다)

## "say in a few words what you're doing, then continue"
- 레지스터: conversational
- 출처: transcript:pm-notes 0270bee8 (하니스 안내 문구)
- 맥락: 길게 설명하지 말고 지금 뭐 하는지만 한마디 하라고 할 때(구어)
- 한국어: 지금 뭘 하는지 몇 마디로 말하고 계속해라
- 설명: `in a few words` 가 동사와 목적어절 사이에 끼어 "짧게"를 먼저 들려줍니다. 목적어는 의문사절 `what you're doing` 입니다. 앞 문장 `The user hasn't heard from you in a while` 의 현재완료는 "아까부터 지금까지 소식이 없다"는 뜻입니다.
- 예문: The team hasn't heard from you in a while, so say in a few words what you're doing, then continue.
- 유사어: give a quick status update (업무 구어), drop a one-liner on where you are (캐주얼), briefly state your progress (격식)

## "I'll restore the file and insert only the new lines."
- 레지스터: conversational, technical
- 출처: transcript:english-study f02163d6 ([assistant] 인덱스 정렬 실수 뒤 보고)
- 맥락: 내 실수를 한 문장으로 밝히고 곧바로 복구 계획을 말할 때(작업 중 보고)
- 한국어: 파일을 되돌리고 새 줄만 끼워 넣겠습니다
- 설명: 앞 문장 `My sort reordered existing index lines.` 가 원인이고 이 문장이 조치입니다. `only` 를 `the new lines` 바로 앞에 둬서 "새 줄만"으로 범위를 좁힙니다. `restore` 는 원래 상태로 돌려놓는다는 뜻이라 `revert` 보다 "망가진 것을 복구"하는 느낌이 납니다.
- 예문: My sort reordered existing index lines. I'll restore the file and insert only the new lines.
- 유사어: I'll revert and add just the new entries (구어), I'll back that out and re-apply the additions only (개발자 구어), the file will be restored and only the additions re-applied (격식 보고서)

## "a tool you did not anticipate"
- 레지스터: professional
- 출처: transcript:pm-notes 0270bee8 (claude-in-chrome MCP 지침)
- 맥락: 미리 예상하지 못한 필요가 나중에 생겼을 때만 추가 조치를 하라고 할 때(지침·계획 문서)
- 한국어: 미리 예상하지 못한 도구
- 설명: `anticipate` 는 `expect` 보다 "앞서 내다보고 대비하다"에 가깝습니다. 원문은 `Only issue a second ToolSearch if …` 로 `only … if` 가 조건을 하나로 좁힙니다. `issue` 는 요청·명령을 "내다"라는 격식 있는 동사입니다.
- 예문: Only issue a second ToolSearch if the task later needs a tool you did not anticipate.
- 유사어: a tool you didn't see coming (캐주얼), an unforeseen requirement (격식, 명사구), something you hadn't planned for (구어)
- 반의어: a tool you expected to need (필요할 줄 알았던 도구)
