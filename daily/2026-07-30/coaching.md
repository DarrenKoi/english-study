# 2026-07-30 — 코칭

> 오늘 배치에는 내가 한국어로 쓴 문장이 없고(질문·지시를 전부 영어로 함), 어시스턴트 발화도 영어여서
> `한글→영어` 섹션은 두지 않았습니다. 대신 내가 쓴 영어 9건을 다듬습니다.

## 영어 다듬기

### 카드 1 — 마무리 확인

- 내가 쓴 영어: "are we done? clean up the worktrees?"   (출처: transcript:[user] 134c9baf)
- 더 나은 표현: Are we done here? Shall I clean up the worktrees?
- 왜: 문법 오류는 없다. 다만 동사 없는 `clean up the worktrees?` 는 명령인지 제안인지 상대가 고르게 만든다. `Shall I …?` 를 붙이면 "네가 해라"가 아니라 "내가 할까?"가 되고, 더 짧게 가려면 `Worktrees cleaned up?` 처럼 완료 확인으로 바꾸는 편이 낫다. 두 뜻이 다르니 의도한 쪽을 고르는 게 핵심.

### 카드 2 — 남은 일이 있는 곳 묻기

- 내가 쓴 영어: "check other worktrees that we can do the rest of jobs"   (출처: transcript:[user] 134c9baf)
- 정정: `worktrees that we can do the rest of jobs` → `worktrees where we can do the rest of the jobs`. 관계절 안에서 worktree 가 "장소"라 `that` 이 아니라 `where` 가 필요하고(또는 `that we can work in` 처럼 전치사를 살려야 함), 특정된 명사 앞의 `the` 도 빠졌다.
- 더 나은 표현: Check whether any other worktrees still have work left in them.
- 왜: 원문은 "worktree 를 확인해 달라"인지 "남은 일이 어디 있는지 알려 달라"인지 갈린다. `whether … still have work left` 로 바꾸면 묻는 대상이 worktree 가 아니라 *남은 일의 유무* 로 분명해진다. 더 격식 있게는 `Which worktrees, if any, still hold unfinished work?`

### 카드 3 — 스크립트 수정 요청

- 내가 쓴 영어: "I want you to know the details of recipe info from the recipe raw data for each parameter … can you modify the code to download parameter's related data (img_add1, img_add2,..) and read them?"   (출처: transcript:[user] 0ff1832b)
- 정정: `I want you to know the details` → `I want to know the details`(정보를 원하는 쪽은 나다). `parameter's related data` → `the data related to each parameter` 또는 `each parameter's related files`(무생물 소유격 `parameter's` 는 어색하고, 관사도 없다).
- 더 나은 표현: I want to see the full recipe detail behind each parameter. Could you extend the script to download that parameter's related files (img_add1, img_add2, …) and parse them?
- 왜: `I want you to know` 는 "너에게 알려 주고 싶다"로 읽혀 요청이 뒤집힌다. `modify the code` 보다 `extend the script` 가 "기존 것을 살리고 덧붙여 달라"는 의도를 더 정확히 전한다. `read them` 은 파일을 열기만 한다는 뜻이라, 내용을 구조화해 달라는 요청이면 `parse` 가 맞다.

### 카드 4 — 하드코딩 요청

- 내가 쓴 영어: "I can control the parameter in the code (hard code please and i can edit myself). the default parameter is 'WAFER'."   (출처: transcript:[user] 0ff1832b)
- 정정: `hard code` → `hard-code`(동사일 때 하이픈). `i` → `I`. `I can edit myself` 는 "내가 나 자신을 편집한다"로도 읽히므로 `I can edit it myself`.
- 더 나은 표현: Hard-code the parameter near the top of the file so I can edit it myself; default it to "WAFER".
- 왜: "왜 하드코딩을 원하는지"를 `so I can edit it myself` 로 붙이면 상대가 CLI 인자 같은 대안을 제안하며 겉돌지 않는다. `near the top of the file` 처럼 위치를 지정하면 한 번에 원하는 모양이 나온다.

### 카드 5 — 수정 여부 확인

- 내가 쓴 영어: "you fixed .jpg.jpeg thing?"   (출처: transcript:[user] 0ff1832b)
- 정정: `you fixed …?` → `Did you fix …?`(조동사 없는 평서문 억양 의문은 격식 대화에서 어색하다). `.jpg.jpeg thing` → `the .jpg.jpeg thing`.
- 더 나은 표현: Did you actually fix the .jpg.jpeg problem, or just report it?
- 왜: 실제 상황이 "보고만 하고 안 고침"이었다. `or just report it?` 처럼 대안을 함께 주면 상대가 애매하게 얼버무리지 못하고 둘 중 하나로 답한다. 확인 질문에서 아주 실용적인 장치.

### 카드 6 — API 계약 알려 주기

- 내가 쓴 영어: "from idp_amp_reader, you can use functions: read_amp_info(img_meas2), …"   (출처: transcript:[user] 0ff1832b)
- 정정: `you can use functions:` → `you can use these functions:` 또는 `the following functions:`(가산명사 복수 앞에 한정사가 필요하다).
- 더 나은 표현: `idp_amp_reader` exposes five functions — use them as follows: …
- 왜: `expose` 는 모듈이 공개하는 API 를 가리키는 표준 동사라 `you can use` 보다 계약 문서처럼 읽힌다. 개수(`five`)를 앞에 박아 두면 상대가 하나를 빠뜨렸는지 스스로 검산한다.

### 카드 7 — 관행 설명

- 내가 쓴 영어: "we tend to have P.No with two numbers 1 and 2. 1 is OM, and 2 is SEM. sometimes we only have 1, but mostly 1, 2."   (출처: transcript:[user] 0ff1832b)
- 정정: `P.No with two numbers 1 and 2` → `P.No values of 1 and 2`(with 이 아니라 값 자체를 말하는 자리). 문장 첫 글자 대문자, `mostly 1, 2` → `most of the time we have both`.
- 더 나은 표현: Align points normally come in a pair — P.No 1 is OM and P.No 2 is SEM. Occasionally only 1 exists, but both are the usual case.
- 왜: `tend to` 는 맞지만 `normally come in a pair` 가 규칙성을 더 또렷하게 만든다. 예외를 `Occasionally … but … the usual case` 로 감싸면 상대가 예외를 기본값으로 오해하지 않는다. 상대가 이 문장 하나로 코드를 쓰기 때문에 예외의 비중을 말로 못 박아 두는 게 중요하다.

### 카드 8 — 버그 신고

- 내가 쓴 영어: "in recipe-seaerch/open page, when I click Align 정보, I see the images of align with the popup window. but I cannot close it. can you fix this bug? I want to close with ESC or x button in the window."   (출처: transcript:[user] c3d8d75e)
- 정정: `in recipe-search/open page` → `on the recipe-search/open page`(페이지 위치는 `on`). `the images of align` → `the align images`(of 로 늘리지 않고 명사를 형용사처럼 앞에 둔다). `with the popup window` → `in a popup`. `I want to close with ESC` → `I want to close it with ESC or an X button`(타동사 close 에 목적어가 빠졌다).
- 더 나은 표현: On the recipe-search/open page, clicking 「Align 정보」 opens the align images in a popup that I can't dismiss. Could you add a close path — ESC or an X button in the window?
- 왜: 버그 신고는 "행동 → 결과 → 기대"가 한 흐름이면 재현이 빨라진다. `clicking …` 동명사 주어로 조건절을 없애 한 문장에 담고, 관계절 `that I can't dismiss` 로 증상을 붙였다. `dismiss` 는 모달·알림을 닫는다는 뜻의 UI 전문어라 `close` 보다 정확하다.

### 카드 9 — 슬라이드 개선 요청

- 내가 쓴 영어: "update the contents. I intent to show my knowhow to build this project, hop between home and office. It is good to show the skills that I often use. Add some of file structure that help the smooth transition."   (출처: transcript:[user] 5b5f25b7)
- 정정: `I intent to` → `I intend to`(intent 는 명사). `my knowhow to build` → `my know-how for building`(know-how 뒤에는 to부정사가 아니라 for + 동명사). `hop` → `hopping`(앞 구와 병렬이 아니라 방식을 덧붙이는 분사구). `some of file structure that help` → `some of the file structure that helps`(관사 + 단수 주어에 맞춘 3인칭 단수 동사).
- 더 나은 표현: Update the deck. I want it to show the know-how behind building this project while hopping between home and office — the skills I lean on, plus enough of the file structure to make the hand-off legible.
- 왜: `It is good to show …` 는 일반론이라 요청으로 약하다. `I want it to show …` 로 주어를 세우면 지시가 된다. `the skills I lean on`(자주 기대는 기술)은 `the skills that I often use` 보다 짧고 태도가 드러나고, `enough of X to Y` 는 "얼마나 넣을지"까지 함께 정해 준다.
