# 2026-08-25 — 코칭

## 한글→영어

오늘 배치에는 내가 한국어로 쓴 메시지와 spool 노트가 없어, 어시스턴트의 고급 한국어 번역 정독 3장만 둡니다.

### 카드 1 — 삭제 기준을 밝히고 부수 효과까지   (고급 한글 · 번역)
- 한글 원문: "삭제 기준이 파일명 날짜가 아니라 mtime입니다. `uwsgi-2026-08-03.log` 는 그 날이 끝나면 더 이상 쓰이지 않으니 mtime이 곧 그 날짜이고, 동시에 날짜가 이름에 없는 회전 파일(`*.log.1`)도 같은 규칙 하나로 처리됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a3157a56)
- 자연스러운 영어: Deletion is keyed on mtime, not on the date in the filename. Once a day ends, `uwsgi-2026-08-03.log` is never written again, so its mtime *is* that date — and the same single rule also covers rotated files like `*.log.1` that carry no date in their name.
- 번역 포인트: "삭제 기준이 X입니다"는 `deletion is keyed on X` 나 `the cutoff is X` — `the deletion criterion is` 는 딱딱하다. "mtime이 곧 그 날짜"의 "곧"은 강조 이탤릭 `*is*` 가 맡는다. "동시에 ~도 같은 규칙 하나로"는 `and the same single rule also covers ...` — `same`·`single`·`also` 셋이 각각 "같은"·"하나"·"도"를 받는다.

### 카드 2 — 오차의 방향이 안전함을 말하기   (고급 한글 · 번역)
- 한글 원문: "파일을 복사/복원해 넣으면 mtime이 갱신돼 일주일 더 남는데, 이건 '너무 오래 남는' 쪽 오차라 안전한 방향입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a3157a56)
- 자연스러운 영어: If you copy or restore a file into the directory, its mtime resets and it survives another week — but that error is on the "kept too long" side, which is the safe direction.
- 번역 포인트: "일주일 더 남는다"는 `survives another week` 가 `remains for one more week` 보다 생생하다. "~쪽 오차"는 관용구 `err on the side of X` 와 통하는데, 여기선 명사형 `on the "kept too long" side` 로 두고 `which is the safe direction` 을 뒤에 붙여 판단을 분리한다. "~인데"는 대시와 `but` 으로 잇는 게 자연스럽다.

### 카드 3 — 순서가 곧 설계라는 논증   (고급 한글 · 번역)
- 한글 원문: "스윕이 그 뒤에 오기 때문에, 지금 쓰이고 있는 파일은 항상 디렉터리에서 가장 새 파일 — 스윕 후보가 될 수 없습니다. 순서를 뒤집으면 열려 있는 파일을 건드릴 여지가 생깁니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a3157a56)
- 자연스러운 영어: Because the sweep runs after that, the file currently being written is always the newest one in the directory — it can never be a sweep candidate. Reverse the order and you open a window in which the live file could be touched.
- 번역 포인트: "지금 쓰이고 있는 파일"은 수동 진행형 `the file currently being written` 이 `the file in use` 보다 정확하다. "될 수 없습니다"는 `can never be` — `never` 가 있어야 한국어의 단정이 산다. "순서를 뒤집으면 ~여지가 생깁니다"는 `if` 절 대신 명령형+`and`(`Reverse the order and you ...`)로 옮기면 영어 기술 문서의 리듬이 되고, "여지"는 `a window in which ...` 가 맞는다.

## 영어 다듬기

### 카드 4 — 절차를 단계별로 지시하기
- 내가 쓴 영어: "I want to add more steps @poc/workflow_3/monitor/demonstration_rcs_control.py . in the tool MCD019, You click the button "Utility" and you'll see the dropbox (opening upward) and click "Memo Print" and you will see the popup window "MemoPrint". go to the window and type "Infra. Tech Center!! \n(hit enter), One Stop Solution" Let's test with MCD019 for this procedure"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `dropbox` → `dropdown` (Dropbox 는 서비스 이름이고, 펼쳐지는 메뉴는 `dropdown (menu)`). `in the tool MCD019, You click` — 문장 중간이라 `you` 는 소문자. `and ... and ... and` 로 이어진 다섯 동작은 단계마다 끊는다.
- 더 나은 표현: I want to add a few more steps to `demonstration_rcs_control.py`. On MCD019: click the **Utility** button — a dropdown opens upward — then choose **Memo Print**, and a **MemoPrint** popup appears. Click into that window and type "Infra. Tech Center!!", press Enter, then "One Stop Solution". Let's test this flow on MCD019.
- 왜: 절차 지시는 한 문장에 동작 하나가 원칙이다. `and` 로 잇는 대신 `then` 과 대시로 순서와 부수 설명을 분리하면 읽는 쪽이 단계를 셀 수 있다. "(hit enter)" 같은 괄호 지시는 `press Enter` 로 동작 문장에 편입한다. `in the tool MCD019` 는 `on MCD019` — 장비·화면 위의 조작은 `on`.

### 카드 5 — 가려진 버튼과 복구 절차 설명
- 내가 쓴 영어: "one thing to note. the button for Utility placed in the right bottom in the tool monitor. Sometimes it is hidden by other windows. In that case, you can do Alt + click to push back the clicked windows so that you will recover the "Utility". We need this process if Utility is not seen via VLM. (note that it is placed in the right botton side)"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `the button for Utility placed in` → 동사 누락: `the Utility button is placed in` / `sits in`. `right bottom` → `bottom right` (영어는 세로축 먼저: bottom-right, top-left). `botton` → `bottom` 오타. `recover the "Utility"` → `recover` 는 "되찾다·복구하다"라, 화면에 다시 드러난다는 뜻으로는 `uncover` / `reveal`.
- 더 나은 표현: One thing to note: the Utility button sits in the bottom-right corner of the tool monitor, and other windows sometimes cover it. When that happens, Alt+click sends the covering window to the back and uncovers Utility. We need that step whenever the VLM can't see Utility.
- 왜: "push back the clicked windows" 는 창 관리의 표준 어휘 `send the window to the back` 으로. `so that you will recover` 처럼 결과절에 `will` 을 넣으면 어색하다 — `so that` 절은 현재형이거나, 아예 동사로 결과를 말한다(`and uncovers Utility`). 괄호로 반복한 "(note that it is placed in the right botton side)" 는 첫 문장에 위치를 정확히 적으면 필요 없다.

### 카드 6 — 동작 순서 정정하기
- 내가 쓴 영어: "you have to move the mouse to the right side of bottom to do Alt + click."   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `the right side of bottom` → `the bottom right` (또는 `the bottom-right corner`).
- 더 나은 표현: You need to move the mouse to the bottom right first, and *then* Alt+click.
- 왜: 이 메시지의 요점은 순서다("먼저 이동, 그다음 Alt+클릭"). `to do Alt + click` 은 목적을 말할 뿐 순서를 못 박지 않는다. `first ... and then` 이 순서를 명시하고, `then` 에 강조를 두면 "지금 순서가 틀렸다"는 정정의 뜻까지 전해진다. `have to` 도 틀리진 않지만 `need to` 가 지시보다 설명에 가까워 부드럽다.

### 카드 7 — 현장 실행 결과 보고와 다음 단계 지시
- 내가 쓴 영어: "good. you have done almost. one thing to note. in MemoPrint, you typed NFRA. ECH ENTER \n NE TOP OLUTION maybe there is some missing point when you start typing and adding space.. After you type the letters, wait 2 seconds, and click "Close" button in MemoPrint window. then move to the MCDC22. You click worksheet but fail to close the Work Sheet window. the File is near the tile of Windows "Work Sheet" but it is small. and click to see the drop down and click Exit."   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `you have done almost` → `you're almost there` / `it's almost done` (`almost` 는 동사 뒤에 단독으로 못 온다). `click "Close" button` → `click the Close button` (관사). `the tile` → `the title` 오타. `You click worksheet but fail to close` → 지난 실행의 보고이므로 과거형: `it clicked Work Sheet but failed to close`.
- 더 나은 표현: Good — almost there. One thing: in MemoPrint the text came out as "NFRA. ECH ENTER / NE TOP OLUTION", so some characters are being dropped, maybe at the start of typing or around the spaces. After typing, wait two seconds and click the Close button in the MemoPrint window, then move on to MCDC22. There it clicked Work Sheet but failed to close it: the File menu is a small label just under the "Work Sheet" window title — click it to open the dropdown, then click Exit.
- 왜: 현상 보고("이렇게 찍혔다")와 지시("이렇게 해라")가 섞인 메시지는 시제로 갈라 준다 — 보고는 과거(`came out as`, `clicked`, `failed`), 지시는 명령형. "some missing point" 는 무엇이 빠졌는지 불분명한데 실제로 빠진 건 글자이므로 `characters are being dropped` 가 정확하다. `the File is near the title but it is small` 은 두 정보를 한 명사구 `a small label just under the title` 로 합치면 찾는 쪽이 바로 그림을 그린다.

### 카드 8 — 부분 개선을 보고하기
- 내가 쓴 영어: "the first letter of the words now all small letters. but now I can see them."   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: 동사 누락 — `the first letters of the words are now all lowercase`. `small letters` 는 통하지만 표준 용어는 `lowercase` / `capitals` (`uppercase`).
- 더 나은 표현: The first letter of each word now comes out lowercase — but at least the characters show up now.
- 왜: `now ... but now` 처럼 `now` 가 두 번 오면 대비가 흐려진다. 나빠진 점과 좋아진 점을 `— but at least` 로 잇고 `at least` 를 넣으면 "완전하진 않지만 진전"이라는 평가가 실린다. `come out` 은 타이핑·인쇄 결과가 "그렇게 나온다"의 관용 동사.

### 카드 9 — 쉬운 말로 설명 요청
- 내가 쓴 영어: "explain to me in plan words."   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `plan` → `plain` (plain words = 쉬운 말; plan 은 계획).
- 더 나은 표현: Can you explain that in plain terms? / Put that in plain English for me.
- 왜: `in plain words` 도 통하지만 관용구는 `in plain terms` 나 `in plain English` 다. 명령형 `explain to me` 는 짧은 채팅에선 괜찮고, 조금 부드럽게 하려면 `Can you ...?`. 참고로 상대는 이 요청에 `Here's what happened, without the jargon.` 으로 답했다 — 그 첫 문장이 이 요청을 받는 가장 자연스러운 공식이다.

### 카드 10 — 대기 시간을 더 줄여 달라기
- 내가 쓴 영어: "also for each step, you can reduce the time waiting more. can you reduce 30% more than now?"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `the time waiting` → `the wait time` / `the waiting time` (명사+분사 어순이 아니라 복합명사). `reduce 30% more than now` → `reduce it by another 30%` (줄이는 양은 `by`, "지금보다 더"는 `another`).
- 더 나은 표현: Also, the per-step waits can come down further — can you cut them by another 30%?
- 왜: 줄이는 양은 `by` 로 표시한다(`cut by 30%`). `another 30%` 는 "이미 한 번 줄였고 거기서 또"라는 맥락을 정확히 담는다. `you can reduce` 는 허락처럼 들리므로 실제 의도(요청)에 맞게 `can you cut ...?` 하나로 합친다. `per-step` 은 "각 단계의"를 형용사 하나로 만드는 편리한 접두 표현.

### 카드 11 — 이상 현상 보고와 원인 질문
- 내가 쓴 영어: "wait, I found that capslock on and off switching fast and not able to write properly in the memo. why is it so? or not possible to hold shift key inside the sem monitor?"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `I found that capslock on and off switching fast and not able to write` — `that` 절에 동사가 없다: `Caps Lock is toggling on and off quickly and the memo isn't being typed properly`. `why is it so?` → `why is that?`. `or not possible to hold shift key` → 의문문이면 주어·동사·관사가 필요: `or is it not possible to hold the Shift key`.
- 더 나은 표현: Wait — Caps Lock is toggling on and off so fast that the memo doesn't type properly. Why is that? Or is it just not possible to hold Shift inside the SEM monitor?
- 왜: 현상은 `so ... that` 으로 원인·결과를 한 문장에 묶으면 명료하다. "왜 그런가"는 `Why is that?` 이 표준. 대안 질문은 `Or is it just not possible to ...?` — `just` 가 "혹시 아예 안 되는 것이냐"의 뉘앙스를 준다. 상대는 이 질문을 "구조적 약점이지 조정 문제가 아니다"라는 판정으로 받았으니, 잘 던진 질문이었다.

### 카드 12 — 계획 변경 통보
- 내가 쓴 영어: "change the plan. instead of MCDC22, we try go with MCDC10. memo_print works fine for MCD019. No need to try the same for MCDC10. just try to do "file" thing"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 정정: `we try go with` → 동사 두 개가 붙었다: `let's go with` / `we'll try MCDC10`. `do "file" thing` → 관사: `do the File part` / `the File flow`.
- 더 나은 표현: Change of plan: let's use MCDC10 instead of MCDC22. memo_print already works on MCD019, so there's no need to repeat it on MCDC10 — just run the File flow there.
- 왜: "계획 변경"의 관용 표현은 명사구+콜론 `Change of plan:` 이다. `try go` 는 한국어 "해 보자"의 직역이 남은 형태 — 영어는 `let's go with X` 하나로 충분하다. `works fine for MCD019` 의 `for` 는 `on` — 장비 위에서 도는 흐름이기 때문. `the same` 뒤에는 무엇의 same 인지 밝히거나 `repeat it` 으로 동사화한다.

### 카드 13 — 로딩 표시 추가 요청
- 내가 쓴 영어: "In skewvoir/analysis, we have multi msr selection case to analyze in time-series. Since they are many msr file loading, it takes time to display the chart. can you add spinner or waiting motion like we have done for recipe 현황 page?"   (출처: transcript:[user] skewnono-v3-nuxt 3ae7de12)
- 정정: `we have multi msr selection case` → 관사·하이픈: `there's a multi-MSR selection case`. `Since they are many msr file loading` → `Since it loads many MSR files` (`they are ... loading` 은 주어가 비어 있다). `add spinner` → `add a spinner`.
- 더 나은 표현: In skewvoir/analysis, the Time-Series view can take a while to render when several MSRs are selected, since it has to load many MSR files. Can you add a spinner or loading state like the one on the Recipe 현황 page?
- 왜: `waiting motion` 은 통하지만 UI 용어는 `loading indicator` / `loading state` 다. "~처럼 우리가 했던"은 `like we have done for` 보다 `like the one on X` 가 짧고 자연스럽다 — 이미 있는 화면 요소를 가리키니 명사 `the one` 으로 받는다. `it takes time` 은 회화에서 `it can take a while` 이 부드럽다.

### 카드 14 — 기존 설정 여부 확인 질문
- 내가 쓴 영어: "in scheduler running in the flask server, have we set the scheduler to trim down the log files in the cloud? in /project/workSpace/logs/uwsgi-yyyy-mm-dd.log. I want to keep the only 7 days of logs"   (출처: transcript:[user] skewnono-v3-nuxt a3157a56)
- 정정: `in scheduler running in the flask server` → `in the scheduler that runs inside the Flask server` (관사·관계절). `keep the only 7 days` → `keep only the last 7 days` (`only` 의 위치와 `last`).
- 더 나은 표현: Does the scheduler in the Flask server already trim the cloud log files (`/project/workSpace/logs/uwsgi-yyyy-mm-dd.log`)? I want to keep only the last 7 days.
- 왜: "이미 되어 있느냐"는 질문은 `have we set ... to` 보다 `Does X already ...?` 가 짧고 요점이 분명하다. `trim down` 도 좋지만 로그 정리의 표준 어휘는 `trim`, `prune`, `rotate`, `purge` — 실제 코드도 `purge_old_logs` 였다. `the only 7 days` 는 "유일한 7일"이 되어 뜻이 바뀌니 `only the last 7 days` 어순을 지킨다.

### 카드 15 — 승인과 후속 지시를 한 줄로
- 내가 쓴 영어: "yes, remove the "!!" and quotes from the memo text and commit and push"   (출처: transcript:[user] auto-recipe-creator 6e44bf1a)
- 더 나은 표현: Yes — drop the "!!" and the quotes from the memo text, then commit and push.
- 왜: 문법 오류는 없다. `and ... and ... and` 를 `, then` 으로 한 번 끊으면 "수정 → 커밋" 순서가 살고, `remove` 대신 `drop` 을 쓰면 텍스트 편집 지시의 관용 어휘가 된다. `the quotes` 처럼 관사를 붙이면 앞의 `the "!!"` 와 균형이 맞는다.
