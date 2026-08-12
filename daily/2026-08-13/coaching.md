# 2026-08-13 — 코칭

## 한글→영어

### 카드 1 — 알람 보드 시간 지평 늘리기   (내가 쓴 한글)
- 내가 쓴 한글: "live-alarm 시간을 20분으로 증가시켜야 해. (10분은 너무 짧다는 feedback을 받음)"   (출처: transcript:[user] skewnono_v3_nuxt 2421c16a)
- 자연스러운 영어: We need to extend the live-alarm window from 10 to 20 minutes — users told us 10 was too short.
- 왜 이렇게: "증가시켜야 해"를 `increase`로 직역하면 숫자가 커진다는 사실만 남습니다. 시간 범위에는 `extend`(늘리다)가 붙고, "10분 → 20분"을 `from A to B`로 함께 적어야 상대가 현재 값을 되묻지 않습니다. 괄호 안 근거는 영어에서 괄호보다 대시 뒤에 문장으로 붙이는 편이 자연스럽고, `feedback을 받음`은 `received feedback that…`보다 `users told us…`가 짧고 구체적입니다. `live-alarm 시간`은 그대로 옮기면 모호하니 `window`(집계 구간)로 특정합니다.

### 카드 2 — 보관 상한과 화면 지평의 관계   (고급 한글 · 번역)
- 한글 원문: "보관 상한이 화면 지평보다 짧으면 reader가 보여줘야 할 이벤트를 refresh가 먼저 지웁니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 2421c16a)
- 자연스러운 영어: If the retention limit is shorter than the display window, refresh deletes events out from under the reader before it can show them.
- 번역 포인트: "먼저 지웁니다"의 '먼저'는 시간 순서가 아니라 **다른 쪽이 쓰기도 전에 치워버린다**는 뜻입니다. 영어에는 이 관계에 딱 맞는 관용구 `out from under someone`이 있어서, `deletes … first`보다 훨씬 정확합니다. "보여줘야 할"은 의무가 아니라 예정이므로 `should show`가 아니라 `before it can show them`으로 시점을 옮깁니다. `보관 상한`은 `retention limit`, `화면 지평`은 `display window` — 둘 다 업계에 굳은 짝이 있어 새로 지어내지 않는 게 안전합니다.

### 카드 3 — 상류 조회가 아니라 누적으로 채워진다   (고급 한글 · 번역)
- 한글 원문: "20분 보드는 상류 조회를 늘려서가 아니라 ZSET이 폴링마다 스냅샷을 누적하기 때문에 채워집니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 2421c16a)
- 자연스러운 영어: The 20-minute board fills up not because we widened the upstream query, but because the ZSET accumulates a snapshot on every poll.
- 번역 포인트: "A 가 아니라 B 때문에"는 영어에서 `not because A, but because B` 로 **접속사를 두 번 반복**해야 대구가 섭니다. `not because A but B`처럼 뒤쪽 because를 빼면 문장이 무너집니다. "상류 조회를 늘려서"는 조회 횟수가 아니라 범위를 넓힌 것이므로 `widen the query`, "폴링마다"는 `on every poll`이 자연스럽습니다. `채워집니다`는 수동태 `is filled`보다 자동사 `fills up`이 짧고, 주어가 보드 자신이라는 감각도 살아납니다.

### 카드 4 — 문구가 조용히 어긋난다   (고급 한글 · 번역)
- 한글 원문: "payload가 `board_window_sec`를 이미 싣고 있는데 화면 문구는 별도 상수라, 이번처럼 서버 값만 바꾸면 문구가 조용히 어긋납니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 2421c16a)
- 자연스러운 영어: The payload already carries `board_window_sec`, but the on-screen copy lives in its own constant — so changing the server value alone, as we just did, silently puts the two out of sync.
- 번역 포인트: "조용히 어긋납니다"가 이 문장의 급소입니다. `silently` + `out of sync` 조합이 "경고 없이 불일치가 생긴다"를 그대로 담고, `drift apart`도 대안입니다. `문구`는 UI 텍스트를 가리키는 업계 단어 `copy`가 정확합니다(`text`는 너무 넓고 `phrase`는 어색). "별도 상수라"의 '~라'는 원인 표시인데 영어에서 `because`를 쓰면 무거워지므로 대시로 근거를 잇는 게 이 길이에 맞습니다. `이번처럼`은 `as we just did`로 삽입구 처리했습니다.

## 영어 다듬기

### 카드 1 — 산출물이 안 나온다고 신고하기
- 내가 쓴 영어: "@poc/workflow_3/recording_filter/filter_recording.py is not working. click_events and element_crops, no files"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: `click_events and element_crops, no files` 는 동사가 없는 조각입니다. 명사만 나열하면 "그 폴더가 없다"인지 "안이 비었다"인지 갈립니다 → `there are no files in click_events or element_crops`. 부정문에서 A·B를 묶을 때는 `and`가 아니라 `or`를 씁니다.
- 더 나은 표현: `filter_recording.py runs but produces nothing — click_events/ and element_crops/ both come out empty.`
- 왜: `is not working`은 범위가 너무 넓어 상대가 "크래시했나?"부터 다시 묻게 됩니다. `runs but produces nothing`으로 **어디까지 됐고 무엇이 안 됐는지**를 한 번에 주면 진단이 한 단계 앞에서 시작됩니다. 폴더 이름 뒤 슬래시(`click_events/`)는 파일이 아니라 디렉터리라는 표시라 관례상 유용합니다.

### 카드 2 — 결과물이 안 보인다고 말하기
- 내가 쓴 영어: "I do not see diag_cursor"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 더 나은 표현: `I don't see a diag_cursor folder anywhere — where should it be written?`
- 왜: 문법 오류는 없습니다. 다만 `do not`은 구어에서 강조나 격식일 때 쓰고, 평범한 진술은 `don't`가 기본입니다. 그리고 대상이 폴더인지 파일인지 밝혀주면(`a diag_cursor folder`) 상대가 엉뚱한 경로를 뒤지지 않습니다. 뒤에 질문 하나를 붙이면 "없다"로 끝나지 않고 다음 행동이 정해집니다.

### 카드 3 — 실행 결과 숫자 전달하기
- 내가 쓴 영어: "I ran diagnose_cursor and got this. mapped=237 out of from 237, cursor in live=0, overlap50=163 contained=24, in_window=0/410"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: `out of from` — 전치사가 겹쳤습니다. `out of` 하나면 충분합니다(`237 out of 237`). 둘 다 "~중에서"라 함께 쓸 수 없습니다.
- 더 나은 표현: `Here's the output from diagnose_cursor: mapped=237/237, cursor_in_live=0, overlap50=163, contained=24, in_window=0/410.`
- 왜: `I ran X and got this.` 는 문장 두 개를 쓰지만, 숫자를 붙여 넘길 때는 `Here's the output from X:` 한 줄이 더 자연스럽습니다. 콜론 뒤에 붙이면 "여기부터가 붙여넣기"라는 신호가 되고, `237 out of 237`은 로그 형식 `237/237`로 통일하는 편이 읽기 쉽습니다.

### 카드 4 — 남의 진단을 정정하기
- 내가 쓴 영어: "no issue on manual_record.py and filter_recording is the issue. Yesterday, it worked 50/50 (due to hand-shaped icon in the tool). The recoding is done perfectly and there is mouse cursor in the images."   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: ① `no issue on` → `no issue with`(`issue`는 `with`를 취합니다). ② `recoding` → `recording` (오타지만 `recoding`은 "재코딩"이라는 다른 뜻이 되어 오해를 부릅니다). ③ `there is mouse cursor` → `there is a mouse cursor` (셀 수 있는 단수 명사에 관사 필수). ④ `due to hand-shaped icon` → `due to a hand-shaped icon`.
- 더 나은 표현: `manual_record.py is fine — the problem is in filter_recording. Yesterday it got about half of them right, and the hand-shaped icon in the tool is why. The recording itself is clean: the cursor is clearly visible in the frames.`
- 왜: `no issue on A and B is the issue` 는 `issue`가 두 번 나와 대비가 흐려집니다. `A is fine — the problem is in B` 로 바꾸면 부정과 지목이 대시 하나로 갈립니다. `it worked 50/50` 은 원어민에게는 "반반 확률"로 읽혀 성공률과 헷갈리니 `got about half of them right`이 안전합니다. 마지막은 콜론으로 근거를 붙여 "깨끗하다 → 그 증거"의 순서를 만들었습니다.

### 카드 5 — 위치를 되묻기
- 내가 쓴 영어: "the hand cursor icon is in between where? do you know it?"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: ① `in between where?` — 의문사를 문미에 두는 건 되묻기(echo question)에서만 자연스럽고, 새 질문이면 `Where is …?`로 앞에 둡니다. `in between`은 두 대상을 밝혀야 하므로 `between what and what?`. ② `do you know it?` — `it`이 무엇인지 불명확합니다. `do you know where it is?`
- 더 나은 표현: `Where exactly does the hand cursor icon sit — between what and what? Do you know?`
- 왜: `sit`은 UI 요소의 위치를 말할 때 `is`보다 자연스러운 동사입니다(`the button sits above the table`). `exactly`가 "대충 말고 정확히"를 담당하고, 짧은 `Do you know?`를 뒤에 따로 두면 재촉이 아니라 확인으로 읽힙니다.

### 카드 6 — 범위를 좁히고 단서를 주기
- 내가 쓴 영어: "no I won't come back to the previous git history. recording is good. only filter is the matter now. mouse cursor tend to be black outside of the sembox. and you can find handpalm that is placed in between Full Size button and live SEM Box that might interfere the mouse cursor detection."   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: ① `come back to the previous git history` → `go back to`. 되돌아가는 것은 `go back`이고, `come back`은 화자 쪽으로 오는 움직임입니다. ② `only filter is the matter` → `the filter is the only problem`. `the matter`는 `What's the matter?` 같은 굳은 표현에서만 이렇게 쓰입니다. ③ `mouse cursor tend to` → `the mouse cursor tends to` (단수 주어 + 관사). ④ `interfere the` → `interfere with` (자동사라 전치사 필수). ⑤ `that is placed in between … that might …` — 관계절 `that`이 연달아 둘이라 무엇을 받는지 흐려집니다.
- 더 나은 표현: `I don't want to roll back to the earlier commits. The recording is fine; the filter is the only thing at issue. The cursor tends to render black outside the SEM box, and there's a hand-palm icon between the Full Size button and the live SEM box that may be throwing off cursor detection.`
- 왜: `roll back to the earlier commits`는 git 문맥에서 굳은 표현이라 `previous git history`보다 정확합니다. `throw off`(어긋나게 하다)는 `interfere with`보다 구어적이면서도 "탐지를 헷갈리게 한다"는 뜻이 더 좁게 잡힙니다. 관계절은 하나만 남기고 위치는 전치사구 `between …`로 처리하면 문장이 곧게 펴집니다.

### 카드 7 — 상수를 파일에 박아달라고 요청하기
- 내가 쓴 영어: "recording filter max vlm calss 300, you can apply in the filter_recording.py"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: ① `calss` → `calls` (오타). ② `apply in` → `apply it in` 또는 `set it in`. `apply`는 타동사라 목적어가 필요합니다. ③ `you can ...` 은 문자 그대로 "해도 된다"는 허가라, 요청 의도가 흐려집니다.
- 더 나은 표현: Let's hard-code `MAX_VLM_CALLS = 300` in filter_recording.py instead of passing it as an env var.
- 왜: `hard-code`는 "값을 소스에 직접 박다"라는 뜻의 정확한 동사이고, `Let's …`는 지시를 명령처럼 들리지 않게 하는 가장 짧은 장치입니다. `instead of …`로 대안을 함께 밝히면 상대가 기존 방식을 지울지 남길지 되묻지 않습니다.

### 카드 8 — 개선 요청하기
- 내가 쓴 영어: "now you get to find the almost all of mouse cursor. However when the mouse cursor is in the place of edge of the windows, the mouse cursor turns in to the shape (X), in that case, you fall back to pick the hand palm ... Can you improve this point?"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 정정: ① `you get to find` → `you now find` / `you're now finding`. `get to do`는 "~할 기회를 얻다"라는 다른 뜻입니다. ② `the almost all of mouse cursor` → `almost all of the cursors`. `almost all` 앞에는 관사가 붙지 않고, of 뒤 명사에 `the`가 갑니다. ③ `in the place of edge of the windows` → `at the edge of the window`. `in the place of`는 "~대신에"라는 전혀 다른 뜻입니다. ④ `turns in to` → `turns into` (붙여 씁니다. `turn in to`는 "제출하다"). ⑤ `..., in that case, you fall back ...` 은 쉼표만으로 두 문장을 이은 comma splice → `and in that case` 로 접속사를 넣습니다.
- 더 나은 표현: `You're now catching almost every cursor. But when the cursor sits at the window edge it changes to an X shape, and in that case you fall back to the hand-palm icon instead. Can you tighten that up?`
- 왜: `Can you improve this point?` 는 문법은 맞지만 `point`가 무엇을 가리키는지 넓습니다. `tighten that up`(정밀도를 높이다)이 개선 방향까지 담습니다. `catching`은 탐지 성공을 말할 때 `finding`보다 자연스럽고, `instead`를 끝에 두면 "진짜 대신 저것을 고른다"는 문제의 핵심이 마지막에 남습니다.

### 카드 9 — 실행할 파일 묻기
- 내가 쓴 영어: "what file should I run?"   (출처: transcript:[user] auto_recipe_creator b0cef303)
- 더 나은 표현: `Which file should I run?`
- 왜: 오류는 아닙니다. 다만 선택지가 **몇 개로 한정된 상황**에서는 `what`보다 `which`가 정확합니다. 방금 세 개의 스크립트가 언급된 뒤라 상대도 "그중 어느 것"으로 답할 준비가 돼 있고, `which`가 그 범위를 명시합니다. `what`은 후보가 열려 있을 때(`What language should I learn?`) 쓰입니다.
