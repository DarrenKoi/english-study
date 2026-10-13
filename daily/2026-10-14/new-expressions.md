# 2026-10-14 — 새 표현

오늘 배치는 repo 문서 18건이 거의 전부 한국어·스키마 표였고, 영어는 Claude Code 세션 13건에서 나왔다. AFM 표의 긴 lot ID 수정, VS Code 고아 프로세스 정리, 데모 영상 초단축본, 조사용 하위 에이전트 지시문이 주 출처다.

## "I read your order literally"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 지시를 글자 그대로 따랐더니 상대가 기대하지 않았을 결과가 났을 때, 그 선택을 먼저 밝히며(구어·보고)
- 한국어: 말씀하신 순서를 그대로 받아들였습니다.
- 설명: `literally` 는 "비유 없이, 적힌 대로". `I read X literally` 는 "해석을 보태지 않았다"는 뜻이라, 뒤에 "그래서 빠진 것이 있다"가 자연스럽게 따라온다. 비난 대신 사실 진술로 책임 소재를 정리한다.
- 예문: I read your order literally, so the alarm-response clip is not in this cut.
- 유사어: I took you at your word (더 구어, 사람을 믿었다는 뉘앙스), I followed the list as written (문어·중립)
- 반의어: I read between the lines (의도를 짐작해 보탰다)

## "flows through here too"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 한 곳을 고치면 다른 파일에도 자동으로 반영된다고 설명할 때(설계 설명·코드 리뷰)
- 한국어: 여기에도 그대로 흘러 들어온다.
- 설명: 변경이 물처럼 "흘러서" 도달한다는 은유. 하드코딩 없이 원본을 참조하기 때문에 생기는 효과를 한 동사로 말한다. `too` 가 "원본뿐 아니라 여기도"를 받는다.
- 예문: Editing the main cut's wording or swapping the recording flows through here too.
- 유사어: propagates here (격식·기술), is picked up here automatically (중립), carries over (살짝 구어)
- 반의어: has to be changed in both places (양쪽을 따로 고쳐야 한다)

## "stay in step (unless you override the constants)"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 두 산출물이 같은 설정을 공유해 어긋나지 않는다고 보증할 때(설계 메모)
- 한국어: 두 컷이 발을 맞춰 간다 — 상수를 덮어쓰지 않는 한.
- 설명: `in step` 은 행진에서 발을 맞춘 상태. `stay in step` 은 "계속 같이 움직인다". `unless` 절로 어긋날 수 있는 유일한 조건을 붙여 보증의 범위를 정확히 긋는다.
- 예문: The two cuts stay in step unless you override the constants at the top of the new file.
- 유사어: stay in sync (더 흔한 기술 표현), move together (평이함), track each other (한쪽이 다른 쪽을 따라간다)
- 반의어: drift apart (조금씩 어긋나다)

## "out of context"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 문장이나 자막이 앞뒤가 바뀌어 뜻이 안 맞게 됐을 때(짧은 제목·구어)
- 한국어: 맥락에서 떨어져 나왔다.
- 설명: 원래 앞에 오던 장면이 빠지자 자막이 엉뚱하게 읽힌다는 뜻. `take a quote out of context` 처럼 인용에도 흔히 쓴다. 명사 앞에 붙이면 `an out-of-context subtitle`.
- 예문: The cube subtitle is now out of context, since it follows Search Around instead of a failed correction.
- 유사어: reads oddly now (더 구어), no longer fits (중립), is orphaned from its setup (기술·비유)
- 반의어: in context (제 맥락 안에서)

## "if it reads oddly"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 글·자막이 독자에게 어색하게 보일 수 있으니 고쳐도 좋다고 열어 둘 때(구어·메모)
- 한국어: 읽기에 어색하면.
- 설명: `read` 는 자동사로 "~하게 읽히다". 글이 주어이고 독자의 인상이 부사로 온다(`reads well`, `reads oddly`, `reads as a threat`). "어색하다"를 글 쪽에 두어 독자를 탓하지 않는다.
- 예문: Change `IMAGE_SUBTITLE` at the top of the file if it reads oddly.
- 유사어: if it sounds off (더 구어), if the wording feels wrong (평이), if it doesn't land (설득력 쪽)
- 반의어: if it reads fine as is

## "Three things you might not expect"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 결과 보고에서 상대가 놀랄 수 있는 점을 미리 묶어 꺼낼 때(보고서·PR 설명)
- 한국어: 예상 밖일 수 있는 세 가지.
- 설명: 접촉 관계절(`things [that] you might not expect`)로 소제목을 만든다. `might` 가 "놀랄 수도 있다"의 공손한 거리를 둔다. 숫자를 앞에 두어 읽는 쪽이 분량을 가늠한다.
- 예문: Three things you might not expect: the alarm clip is dropped, the cube subtitle is out of context, and the cut range is not carried over.
- 유사어: A few surprises (더 구어), Caveats (한 단어·격식), Things to note (중립)
- 반의어: (마땅한 대체 표현 없음)

## "Nothing is committed."
- 레지스터: technical
- 출처: transcript:auto-recipe-creator/baf56f9b [assistant]
- 맥락: 작업을 끝냈지만 커밋은 하지 않았다고 보고 끝에 못박을 때(작업 보고)
- 한국어: 커밋한 것은 없습니다.
- 설명: 수동태 현재형으로 상태만 말한다. `I didn't commit` 보다 짧고, "다음 결정은 당신 몫"이라는 뜻이 담긴다. 반대 상태는 `Pushed <hash> to main`.
- 예문: I also added the run line to `CLAUDE.md` and one test; nothing is committed.
- 유사어: Not committed yet (더 짧음), The working tree still has the changes (풀어 말함), Left uncommitted for your review (격식)
- 반의어: Pushed to main.

## "fits about 9 characters"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 고정 너비가 몇 글자까지 들어가는지 수치로 환산해 설명할 때(UI 버그 설명)
- 한국어: 글자 아홉 개쯤이 들어간다.
- 설명: `fit` 은 "들어가다/맞다". 사물이 주어(`the track fits 9 characters`)여도 되고 내용물이 주어(`9 characters fit in the track`)여도 된다. `about` 으로 폰트에 따라 달라짐을 열어 둔다.
- 예문: The Lot column was a fixed 6.5rem track, which fits about 9 characters.
- 유사어: holds about 9 characters (담는다), has room for about 9 characters (여유 공간 쪽), accommodates (격식)
- 반의어: overflows at 9 characters

## "spilled out of the tag and ran underneath"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 텍스트가 상자를 넘어 다른 요소 밑으로 깔리는 레이아웃 버그를 묘사할 때
- 한국어: 태그 밖으로 흘러넘쳐 그 아래로 깔렸다.
- 설명: `spill out of` 는 액체가 넘치는 그림, `run underneath` 는 글줄이 다른 요소 밑을 "달린다". CSS 의 `overflow` 를 동사 두 개로 생생하게 풀었다. 과거형은 고치기 전 상태.
- 예문: A 12-character ID spilled out of the tag and ran underneath the Slot tag.
- 유사어: overflowed the tag (기술 용어 그대로), bled into the next column (인쇄 은유), got clipped (잘렸을 때)
- 반의어: stayed inside its tag

## "everything to the right stays aligned"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 한 열이 늘어나도 나머지 열은 정렬이 깨지지 않는다고 보증할 때(UI 수정 설명)
- 한국어: 오른쪽은 전부 정렬이 그대로 유지된다.
- 설명: `everything to the right` 가 "오른쪽에 있는 것 모두"를 한 덩어리 주어로 만든다. `stay + 형용사` 는 상태 유지. 레이아웃 변경의 부작용 범위를 한 문장으로 닫는다.
- 예문: A long-lot row takes the extra width from its own recipe name, and everything to the right stays aligned.
- 유사어: the remaining columns hold their position (격식), nothing else shifts (구어), the rest is unaffected (중립)
- 반의어: pushes the other columns out

## "the overflow should not have been hiding it"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 의심받는 원인이 실제로는 그 증상을 낼 수 없다고 논리적으로 배제할 때
- 한국어: 넘침 때문에 가려졌을 리는 없다.
- 설명: `should not have been -ing` 는 "(원리상) 그러고 있었을 리 없다"는 추론이다. 과거 사실을 부정하는 `wasn't hiding` 보다 "직접 보지 못했지만 구조상 아니다"라는 거리가 있다. 뒤에 근거(`The Slot tag is drawn on top`)가 따라야 한다.
- 예문: On the missing slot number: the overflow should not have been hiding it, because the Slot tag is drawn on top of the Lot tag.
- 유사어: couldn't have been hiding it (더 단정), is unlikely to be the cause (중립·완곡), isn't what hid it (사실 단언)
- 반의어: was almost certainly hiding it

## "the gap is in X, not the UI"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 증상이 남아 있다면 어느 층의 문제인지 미리 가르는 판정 기준을 줄 때(인계 메모)
- 한국어: 빠진 건 UI 가 아니라 적재 데이터 쪽이다.
- 설명: `gap` 은 "있어야 하는데 없는 것". `A, not B` 로 두 층 중 하나를 지운다. 조건절(`If the Slot tag is still blank`)과 짝지으면 상대가 스스로 판정할 수 있는 지시가 된다.
- 예문: If the Slot tag is still blank after this fix, the gap is in the loader's data, not the UI.
- 유사어: the problem lies upstream (위치만 가리킴), it's a data issue, not a display issue (평이), the fault sits with the loader (격식)
- 반의어: it's a rendering bug after all

## "I skipped showing X; say so if you want it"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 할 수 있었지만 하지 않은 선택을 밝히고 결정을 상대에게 넘길 때(보고 끝)
- 한국어: X 는 넣지 않았습니다. 원하시면 말씀하세요.
- 설명: `skip + -ing` 은 "일부러 건너뛰다". 못 한 게 아니라 안 한 것이다. `say so` 는 앞 절 전체를 받아 "그렇다고 말해 달라". 두 절이 세미콜론으로 붙어 짧은 결정 요청이 된다.
- 예문: I skipped showing a `–` placeholder for a blank slot; say so if you want it.
- 유사어: I left X out on purpose (의도를 더 강조), X is deliberately omitted (격식·수동), I held off on X (보류 뉘앙스)
- 반의어: I went ahead and added X

## "Only an empty string gets the dash."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 어떤 입력에 어떤 표시가 나오는지 규칙을 한 문장으로 적을 때(동작 명세)
- 한국어: 빈 문자열일 때만 대시가 붙는다.
- 설명: `get` 이 "받는다/배정된다"로 쓰여 입력(빈 문자열)이 주어, 출력(대시)이 목적어가 된다. `Only` 를 문두에 두어 경계 조건이 하나뿐임을 먼저 알린다. 다음 문장 `Where the slot is not known at all, …` 과 짝으로 다른 경우를 처리한다.
- 예문: Only an empty string gets the dash; an unknown slot keeps the tag hidden.
- 유사어: The dash applies only to empty strings (격식), Empty strings alone show the dash (중립)
- 반의어: Every blank state gets the dash

## "Where the slot is not known at all"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/8b037e20 [assistant]
- 맥락: 명세에서 "~인 경우에는"을 조건절로 열 때(문서·규칙 서술)
- 한국어: 슬롯 값을 전혀 모르는 경우에는.
- 설명: 이 `where` 는 장소가 아니라 `in cases where` 의 줄임이다. 법률·명세 문체에서 `if` 보다 "그런 상황 전반"을 가리킨다. `not known at all` 의 `at all` 은 빈 문자열(알지만 비어 있음)과 미지(null)를 가르는 강조다.
- 예문: Where the slot is not known at all, the Slot tag stays hidden as before.
- 유사어: In cases where (풀어 쓴 형), When the slot is unknown (평이), If no slot value exists (조건문)
- 반의어: (마땅한 대체 표현 없음)

## "a dead buffer"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/4921f2b7 [assistant]
- 맥락: 파일은 지워졌는데 편집기 탭만 남은 상태를 한 단어로 부를 때
- 한국어: 뒤에 파일이 없는 죽은 버퍼(탭).
- 설명: 편집기 용어 `buffer` 는 메모리에 올라온 파일 내용. 원본이 사라져 저장할 곳도 없으면 `dead`. `dead code`, `dead link` 와 같은 계열로, "손대도 아무 영향 없다"는 뜻이 따라온다.
- 예문: The temp file itself is already gone, so the tab is just a dead buffer.
- 유사어: an orphaned tab (주인을 잃음), a stale tab (오래되어 안 맞음), a leftover (남은 것)
- 반의어: a live file

## "orphaned with no window of its own"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/c0567c9e [assistant]
- 맥락: 부모 세션이 끝나 홀로 남은 프로세스를 설명할 때(시스템 진단 보고)
- 한국어: 자기 창도 없이 고아가 된.
- 설명: `orphaned` 는 부모(세션·프로세스)가 사라져 홀로 남은 상태. `with no X of its own` 은 "자기 소유의 X 가 없는"으로, 그 프로세스가 사용자 눈에 안 보이는 이유를 설명한다. 둘을 붙여 "죽여도 잃을 창이 없다"는 결론을 준비한다.
- 예문: Its session had already ended and deleted the file, so it was orphaned with no window of its own.
- 유사어: left behind (평이), a zombie (더 거친 비유, 정확히는 다른 상태), detached from its parent (격식)
- 반의어: attached to a live window

## "lets a stuck waiter go without killing anything"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/c0567c9e [assistant]
- 맥락: 강제 종료 대신 조건을 바꿔 프로세스가 스스로 끝나게 했다고 설명할 때
- 한국어: 멈춰 있던 대기 프로세스를 아무것도 죽이지 않고 풀어 준다.
- 설명: `let X go` 는 붙잡은 것을 놓아준다는 그림이라 `kill` 과 대비된다. `stuck` 은 진행 못 하고 걸린 상태. `without -ing` 으로 피한 수단을 명시해 안전성을 강조한다.
- 예문: Removing that marker lets a stuck waiter go without killing anything.
- 유사어: releases the waiter cleanly (격식), unblocks it (기술·중립), lets it exit on its own (풀어 말함)
- 반의어: force-kills the process

## "safe to ignore"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt/c0567c9e [assistant]
- 맥락: 눈에 띄지만 신경 쓸 필요 없는 파일·경고·로그를 정리해 줄 때
- 한국어: 무시해도 됩니다.
- 설명: `safe to + 동사` 는 "그렇게 해도 위험하지 않다". `You can ignore it` 보다 "무시가 올바른 선택"이라는 보증이 들어간다. 경고 메시지(`safe to ignore this warning`)에 흔하다.
- 예문: It is not part of the repo and is safe to ignore.
- 유사어: harmless (한 단어), nothing to worry about (구어), can be disregarded (격식)
- 반의어: needs attention

## "the name tells you what it was"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/c0567c9e [assistant]
- 맥락: 실물은 없지만 이름만으로 정체를 추론해 설명할 때(구어)
- 한국어: 이름만 봐도 무엇이었는지 알 수 있다.
- 설명: 사물(`the name`)이 주어가 되어 `tell you` 한다. 영어는 이런 무생물 주어가 자연스럽다. 한국어로 옮기면 "이름을 보면 알 수 있다"가 되듯 주어를 바꿔야 한다.
- 예문: That file is gone now, but the name tells you what it was.
- 유사어: the name gives it away (더 구어), you can tell from the name (사람 주어), the filename is self-explanatory (격식)
- 반의어: the name doesn't say much

## "close that one by hand"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/c0567c9e [assistant]
- 맥락: 자동화가 못 미친 마지막 한 단계를 사람이 직접 하라고 할 때
- 한국어: 그건 직접 닫아 주세요.
- 설명: `by hand` 는 "수작업으로". `manually` 와 같은 뜻인데 더 구어다. `that one` 은 앞에서 언급한 특정 탭 하나를 가리킨다. 자동화의 한계를 설명한 뒤 남는 작업을 넘길 때 쓴다.
- 예문: If a dead tab is still showing in your main window, close that one by hand.
- 유사어: manually (격식·한 단어), yourself (사람을 강조), on your end (네 쪽에서)
- 반의어: let the script handle it

## "that isn't granted"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/4921f2b7 [assistant]
- 맥락: 권한이 없어 작업을 못 했다고 원인을 짚을 때(실패 보고)
- 한국어: 그 권한이 부여돼 있지 않다.
- 설명: 권한은 `grant`(부여) / `revoke`(회수) 로 말한다. 수동태 현재 `isn't granted` 는 상태 서술. 콜론 뒤에 "무엇이 필요하고 그것이 없다"를 두 절로 잇는 구조가 깔끔하다.
- 예문: Controlling VS Code needs macOS Accessibility permission for the Claude desktop app, and that isn't granted.
- 유사어: hasn't been granted (과정을 강조), is missing (평이), is not enabled (설정 쪽)
- 반의어: is granted / is already allowed

## "Read-only fact-finding"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/4cd67431 [agent-prompt]
- 맥락: 하위 조사자에게 임무의 성격을 한 구로 규정할 때(지시문 머리)
- 한국어: 읽기만 하는 사실 조사.
- 설명: `fact-finding` 은 판단 없이 사실만 모으는 조사(`a fact-finding mission`). `read-only` 를 앞에 붙여 코드를 고치지 말라는 제약을 함께 건다. 명사구만으로 역할을 정의하는 지시문 문체.
- 예문: Read-only fact-finding, breadth "very thorough": report with file:line references.
- 유사어: a survey (더 넓고 느슨함), reconnaissance (정찰, 군사 은유), an audit (판정이 들어감)
- 반의어: a design review (판단·권고 포함)

## "I need facts, not design advice."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/4cd67431 [agent-prompt]
- 맥락: 조사를 맡기면서 받고 싶지 않은 종류의 답을 미리 막을 때
- 한국어: 사실만 필요하고 설계 조언은 필요 없다.
- 설명: `A, not B` 대구로 원치 않는 산출물을 명시한다. 조사자가 권고로 흐르기 쉬운 것을 알고 선을 긋는 문장이다. 짧고 단호해서 지시문 앞머리에 어울린다.
- 예문: I am designing the page myself; I need facts, not design advice.
- 유사어: Stick to what exists (구어), Findings only, no recommendations (목록 문체), Describe, don't prescribe (격언형)
- 반의어: Tell me what you'd build

## "roughly how heavy is the response"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/4cd67431 [agent-prompt]
- 맥락: API 응답 크기를 정확한 바이트가 아니라 대략의 등급으로 물을 때
- 한국어: 응답이 대략 얼마나 무거운가.
- 설명: `heavy` 는 응답·요청·쿼리의 부담을 뭉뚱그린 기술 구어다. 크기·시간·비용을 다 담는다. `roughly` 로 "전체 fleet 덩어리냐 요약이냐" 정도의 답만 요구한다.
- 예문: Note roughly how heavy the response is — a whole-fleet payload or a summary.
- 유사어: how large the payload is (크기만), how expensive the call is (비용 쪽), the response footprint (격식·명사)
- 반의어: a lightweight response

## "span more than one fab"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/4cd67431 [agent-prompt]
- 맥락: 한 요청이 여러 범위에 걸칠 수 있는지 물을 때(API 분석)
- 한국어: 한 요청이 둘 이상의 fab 에 걸치다.
- 설명: `span` 은 다리처럼 양 끝을 잇는 그림으로 "~에 걸치다". 기간(`span three years`), 범위(`span multiple teams`)에 쓴다. `more than one` 은 `multiple` 보다 "하나 넘기만 하면"을 정확히 묻는다.
- 예문: Can one request span more than one fab, or is fab a required single-valued param?
- 유사어: cover multiple fabs (평이), cross fab boundaries (경계 은유), be scoped to several fabs (설정 쪽)
- 반의어: be scoped to a single fab

## "renders as intended"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/bcad2e37 [assistant]
- 맥락: 브라우저 확인 결과 화면이 의도대로 나왔다고 한 줄로 보고할 때
- 한국어: 의도한 대로 렌더링된다.
- 설명: `render` 는 화면에 그려지는 것, `as intended` 는 "의도한 바와 같이". 동사 하나와 부사구로 검증 결과를 끝낸다. 뒤에 `Pushing and tearing down.` 처럼 다음 동작을 붙이는 작업 로그 문체다.
- 예문: Badge renders as intended; pushing and tearing down.
- 유사어: looks right (구어), displays correctly (평이), matches the design (디자인 기준)
- 반의어: renders wrong / is off

## "infer a larger topology from a request"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [herdr skill]
- 맥락: 작은 요청을 큰 구조 변경으로 확대 해석하지 말라고 규칙을 적을 때
- 한국어: 요청 하나에서 더 큰 구조를 추론하지 말라.
- 설명: `infer A from B` 는 B 를 근거로 A 를 끌어낸다. `Do not infer … from …` 은 "그 근거로는 그 결론에 가지 말라". `larger` 비교급이 "요청이 담은 것보다 더 큰"을 뜻한다.
- 예문: Do not infer a larger topology from a request to start an agent or command.
- 반의어: take the request at face value (요청을 액면대로 받다)
- 유사어: read too much into (구어, 과잉 해석), extrapolate from (격식, 통계 어감), assume more than was asked (풀어 말함)

## "labelled as such rather than stated as established fact"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/466cd9af [agent-prompt]
- 맥락: 근거가 약한 주장을 어떻게 표시해야 하는지 보고서 규칙을 줄 때(격식)
- 한국어: 확정 사실로 쓰지 말고 그런 것(추정·인용)이라고 표시하라.
- 설명: `as such` 는 앞에 나열한 종류(스니펫·마케팅·추론)를 받아 "그 종류로". `rather than` 뒤에 금지하는 서술 방식을 둔다. `established fact` 는 "확립된 사실"로, 증거 등급 최상위를 가리킨다.
- 예문: Unverified formulas and the researchers' own inferences must be labelled as such rather than stated as established fact.
- 유사어: flagged as unverified (평이), caveated (한 단어·격식), marked as inference (구체적)
- 반의어: presented as settled

## "build on and assess them rather than repeating them"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/466cd9af [agent-prompt]
- 맥락: 기존 문서가 이미 권고를 담고 있을 때 새 보고서가 취할 태도를 정할 때
- 한국어: 그것들을 되풀이하지 말고 그 위에서 더 나아가며 평가하라.
- 설명: 동사 둘(`build on`, `assess`)이 같은 목적어 `them` 을 받는다. `build on` 은 토대로 삼아 쌓는 것, `assess` 는 가치를 따지는 것. `rather than repeating` 이 금지 행동을 분사로 든다.
- 예문: Where existing documents already make a recommendation, build on and assess them rather than repeating them.
- 유사어: extend and critique (격식), take them further (구어), engage with them (학술적)
- 반의어: restate them

## "grounded in data the notes confirm actually exists"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/466cd9af [agent-prompt]
- 맥락: 권고의 근거 요건을 정할 때(연구 지시문·격식)
- 한국어: 노트가 실재한다고 확인한 데이터에 근거한.
- 설명: `grounded in` 은 "~에 뿌리를 둔". 그 뒤 `data [that] the notes confirm actually exists` 는 관계사가 빠진 접촉절 안에 또 `confirm (that) … exists` 가 들어 있어 두 겹이다. `actually` 는 "추정이 아니라 실제로".
- 예문: Recommendations must be grounded in data the notes confirm actually exists.
- 유사어: based on (평이), anchored in (은유 유지), backed by (증거 쪽)
- 반의어: speculative

## "carry through the notes' own evidence grading"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/466cd9af [agent-prompt]
- 맥락: 원자료가 매긴 신뢰 등급을 보고서까지 그대로 유지하라고 할 때
- 한국어: 노트가 스스로 매긴 증거 등급을 끝까지 이어 가라.
- 설명: `carry through` 는 중간에 떨어뜨리지 않고 끝까지 가져간다. `the notes' own` 의 소유격 + `own` 은 "다른 기준이 아니라 노트 자체의". `evidence grading` 은 증거에 등급을 매기는 행위 자체를 명사화했다.
- 예문: The report must carry through the notes' own evidence grading.
- 유사어: preserve (한 단어), keep intact (평이), propagate (기술적)
- 반의어: flatten (등급 차이를 뭉개다)

## "this kind of thing"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/4921f2b7 [assistant]
- 맥락: 지금 요청과 같은 부류의 작업을 뭉뚱그려 가리킬 때(구어)
- 한국어: 이런 종류의 일.
- 설명: 구체적으로 열거하지 않고 범주를 가리키는 구어. 격식 글에서는 `tasks of this kind` 나 `such operations` 로 바꾼다. `in future`(영국식) / `in the future`(미국식) 와 자주 짝이 된다.
- 예문: If you want me to do this kind of thing in future, grant Accessibility to Claude first.
- 유사어: tasks like this (평이), such operations (격식), stuff like this (더 캐주얼)
- 반의어: (마땅한 대체 표현 없음)

## "Codex is up."
- 레지스터: technical, casual
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [assistant]
- 맥락: 프로세스·서버·에이전트가 떠서 쓸 수 있게 됐다고 두 단어로 알릴 때
- 한국어: Codex 가 떴다.
- 설명: `be up` 은 서비스가 가동 중(`the server is up`), `be down` 은 죽은 상태. 사람이 아니라 프로세스에 쓴다. 작업 로그에서 다음 단계로 넘어가는 신호로 쓰기 좋다.
- 예문: Codex is up. Sending round 1 and waiting for its reply.
- 유사어: is running (중립), is ready (준비 완료 강조), is live (서비스 공개 쪽)
- 반의어: is down

## "Per memory, …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [assistant]
- 맥락: 어떤 기록·규정에 따르면 그렇다고 출처를 앞세울 때(짧은 메모)
- 한국어: 기록에 따르면.
- 설명: `per` 는 "~에 따라"(`per the spec`, `per your request`). 라틴어에서 온 격식 전치사라 짧은 업무 메모에 어울린다. 문두에 두면 뒤 문장 전체의 근거가 된다.
- 예문: Per memory, this Herdr build uses `herdr agent wait` rather than `herdr wait`.
- 유사어: According to (평이), As recorded in (문어), Going by (구어)
- 반의어: Contrary to
