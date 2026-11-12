# 2026-11-13 — 코칭

출처는 `transcript:` 세 세션입니다. pm-notes 6a5d0980(REA 문서 사실 확인, 설치 절 보강, deck 넘침 확인), pm-notes 0270bee8(deck 수정, em dash 제거), skewnono-v3-nuxt d0eba2c5(opencode 기록과 스킬 삭제). 직접 쓴 한국어 9건을 먼저 다루고 어시스턴트 문장 4개를 뒤에 붙였습니다.

## 한글→영어

### 카드 1 — 사실 확인 요청, ~는 안 되는 건가?   (내가 쓴 한글)
- 내가 쓴 한글: "fact check 필요. Ghidra 함수 이름 달기 (찾아내기), 주석 붙이기는 Windows에서 안되는건가?"   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: This needs a fact check. Is it true that naming functions and adding comments in Ghidra doesn't work on Windows?
- 왜 이렇게: "~는 안 되는 건가?"는 들은 말을 의심하며 확인하는 질문이라 `Is it true that …?` 이 어울립니다. 가볍게는 `So you can't … on Windows?` 도 됩니다. "함수 이름 달기"는 `name functions`, 이미 있는 이름을 바꾸는 것이면 `rename` 입니다. "주석 붙이기"는 `add comments` 또는 `annotate` 를 씁니다. 동명사 두 개를 `and` 로 묶어도 하나의 기능으로 보면 동사는 단수(`doesn't work`)로 받습니다. 운영체제 앞 전치사는 `on Windows` 입니다. 직접 쓴 `fact check` 는 명사로 맞게 썼고, 동사로 쓸 때는 `Can you fact-check this?` 처럼 하이픈을 넣습니다.

### 카드 2 — ~하고 ~까지 해줘   (내가 쓴 한글)
- 내가 쓴 한글: "응 두 줄 수정하고 재게시까지 해줘"   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: Yes, fix those two lines and go ahead and republish too.
- 왜 이렇게: "~까지"는 "거기서 멈추지 말고 그 단계도"라는 뜻입니다. `too` 로 충분하고, 범위를 강조하려면 `fix the two lines, republish and all` 이나 `all the way through republishing` 을 씁니다. `go ahead and` 는 상대가 "수정할까요?"라고 물었을 때 허락을 주는 말입니다. "두 줄"은 방금 상대가 짚은 줄이라 `those two lines` 로 지시어를 붙입니다.

### 카드 3 — 같은 문구가 있는지 확인하고 고쳐줘   (내가 쓴 한글)
- 내가 쓴 한글: "slides deck도 같은 문구 있는지 확인하고 고쳐줘. 그리고 pi coding agent 설치 과정 맞는 지 다시 확인해주고, claude code에도 설치하는 방법 추가."   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: Check whether the slide deck has the same wording and fix it there too. Also, double-check that the pi coding agent install steps are correct, and add instructions for installing it in Claude Code as well.
- 왜 이렇게: "있는지 확인"은 `check whether/if` 입니다. "맞는지 다시 확인"은 `double-check that … are correct` 로, 사실이 맞다고 기대할 때는 `that` 을 씁니다. "문구"는 `wording` 이 가장 가깝고 `phrase` 는 특정 구절 하나를 가리킵니다. `slides deck` 은 `slide deck` 이 맞습니다. 명사가 명사를 꾸밀 때는 단수형을 씁니다. "설치 과정"은 `install steps` 나 `installation procedure`, "설치하는 방법"은 `instructions for installing` 입니다.

### 카드 4 — ~도 추가   (내가 쓴 한글)
- 내가 쓴 한글: "Hermes도 추가."   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: Add Hermes too.
- 왜 이렇게: 작업 도중에 끼워 넣는 짧은 지시입니다. 영어도 세 단어면 됩니다. 앞 요청에 덧붙인다는 뜻을 살리려면 `Oh, and add Hermes as well.` 이라고 하면 "아, 그리고"라는 느낌이 납니다. `Also add Hermes.` 도 같은 뜻인데 `also` 는 동사 앞에, `too` 와 `as well` 은 문장 끝에 둡니다.

### 카드 5 — ~이 없는 게 의문   (내가 쓴 한글)
- 내가 쓴 한글: "npm install --global rea-agents와 npx rea-agents@latest setup 과 같은 내용이 없는게 의문."   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: I'm surprised there's nothing about `npm install --global rea-agents` or `npx rea-agents@latest setup`.
- 왜 이렇게: "의문"을 `question` 이나 `doubt` 로 옮기면 뜻이 어긋납니다. `I doubt …` 는 "아닐 거라고 생각한다"입니다. 빠진 것을 지적하는 말은 `I'm surprised there's nothing about …`, 조금 더 따지는 투로는 `Why isn't there anything about …?` 입니다. 격식 있게 쓰려면 `I notice the docs don't mention …` 이 무난합니다. "~과 같은 내용"은 `anything like …` 나 `nothing about …` 으로 받고, 부정문 안에서 둘을 이을 때는 `and` 가 아니라 `or` 를 씁니다.

### 카드 6 — 열어서 넘치는지 확인   (내가 쓴 한글)
- 내가 쓴 한글: "deck 17번 슬라이드 브라우저로 열어서 넘치는지 확인해줘"   (출처: transcript:[user] pm-notes 6a5d0980)
- 자연스러운 영어: Open slide 17 of the deck in a browser and check whether anything overflows.
- 왜 이렇게: "17번 슬라이드"는 `slide 17` 로, 번호가 뒤에 오고 관사가 없습니다(`the 17th slide` 도 되지만 덜 씁니다). "브라우저로"는 수단이지만 영어에서는 `in a browser` 입니다. "넘치다"는 UI 용어로 `overflow` 이며, 주어를 정하기 어려우면 `anything` 을 세우면 됩니다. 더 구체적으로는 `check that the text fits inside its box` 라고 반대쪽에서 말할 수도 있습니다.

### 카드 7 — 삭제. 이제 전혀 안 씀   (내가 쓴 한글)
- 내가 쓴 한글: "oc-review, oc-discuss 스킬 삭제" / "이제 전혀 사용 안함"   (출처: transcript:[user] skewnono-v3-nuxt d0eba2c5)
- 자연스러운 영어: Delete the oc-review and oc-discuss skills. I don't use them at all anymore.
- 왜 이렇게: "이제 … 안 함"은 `not … anymore`, "전혀"는 `at all` 입니다. 둘을 함께 쓸 때 순서는 `at all anymore` 가 자연스럽습니다. 한 문장으로 묶으면 `Delete the oc-review and oc-discuss skills; I no longer use them.` 이 되고, `no longer` 는 글에 어울리는 격식형입니다. "스킬" 앞에 이름 둘이 오므로 복수 `skills` 로 받고 정관사를 붙입니다.

### 카드 8 — ~도 맞춰서 고쳐줘   (내가 쓴 한글)
- 내가 쓴 한글: "발표 deck 슬라이드도 맞춰서 고쳐줘"   (출처: transcript:[user] pm-notes 0270bee8)
- 자연스러운 영어: Update the presentation slides to match as well.
- 왜 이렇게: "맞춰서"는 기준(방금 고친 문서)에 일치시킨다는 뜻이라 `to match` 가 맞습니다. 기준을 밝히려면 `to match the docs`, 격식 있게는 `Bring the slide deck in line with the updated docs.` 입니다. "고쳐줘"는 틀린 것을 바로잡는 `fix` 보다 최신 내용을 반영하는 `update` 가 상황에 어울립니다. "발표 deck 슬라이드"는 `presentation slides` 나 `slide deck` 중 하나만 써도 됩니다.

### 카드 9 — 최대한 줄여줘, 잘 쓰이지 않음   (내가 쓴 한글)
- 내가 쓴 한글: "em dash 가운데 점 최대한 줄여줘. em dash는 한국 문서에 잘 쓰이지 않음."   (출처: transcript:[user] pm-notes 0270bee8)
- 자연스러운 영어: Cut down on em dashes and middle dots as much as you can. Em dashes aren't commonly used in Korean documents.
- 왜 이렇게: "줄이다"는 사용 빈도를 낮추는 것이라 `cut down on` 이 맞고, 글에서는 `minimize the use of` 를 씁니다. `reduce em dashes` 는 어색합니다. "최대한"은 `as much as you can/possible` 입니다. "잘 쓰이지 않음"은 수동태 `aren't commonly used` 가 그대로 대응하며, 능동으로 바꾸면 `Korean writing rarely uses em dashes.` 가 됩니다. "가운데 점"은 `middle dot` 이고 유니코드 이름으로는 `interpunct` 라고도 부릅니다. 가산명사라 복수형으로 씁니다.

### 카드 10 — 요청받지 않은 일을 했다고 밝히기   (고급 한글 · 번역)
- 한글 원문: "커밋과 push는 따로 요청받지 않았지만 앞 작업과 같은 방식으로 진행했으니, 원치 않으셨다면 알려 주세요."   (출처: transcript:[assistant] pm-notes 0270bee8)
- 자연스러운 영어: You didn't ask me to commit and push, but I went ahead and did so the same way as before. If that wasn't what you wanted, let me know.
- 번역 포인트: "요청받지 않았지만"을 수동태 `I wasn't asked to` 로 옮겨도 되지만, 영어 대화에서는 상대를 주어로 한 능동(`You didn't ask me to`)이 더 흔합니다. "진행했으니"의 "-으니"는 이유보다 상황 설명에 가까워서 `so` 로 잇지 않고 문장을 나눕니다. `went ahead and did so` 는 허락 없이 먼저 했다는 느낌을 담습니다. "원치 않으셨다면"은 이미 한 일이므로 과거형 `wasn't what you wanted` 입니다.

### 카드 11 — 제한의 주체는 A가 아니라 B   (고급 한글 · 번역)
- 한글 원문: "제한의 주체는 Ghidra가 아니라 REA의 Windows 연동(P0, 실험 단계)입니다."   (출처: transcript:[assistant] pm-notes 6a5d0980)
- 자연스러운 영어: The restriction comes from REA's Windows integration (P0, still experimental), not from Ghidra itself.
- 번역 포인트: "주체"를 `subject` 나 `agent` 로 옮기면 뜻이 흐려집니다. "어디서 오는 제한인가"로 풀어 `comes from A, not from B` 로 씁니다. 한국어는 "A가 아니라 B" 순서지만 영어는 긍정 쪽을 먼저 말하고 `not` 을 뒤에 두는 편이 읽기 쉽습니다. `Ghidra itself` 의 재귀대명사가 "Ghidra 자체는"이라는 대비를 살립니다. 강조하려면 분열문 `It's REA's Windows integration, not Ghidra, that imposes the limit.` 을 씁니다.

### 카드 12 — 지우면 출처만 사라진다   (고급 한글 · 번역)
- 한글 원문: "아래는 지난 작업을 적은 기록이라 지우면 출처만 사라집니다."   (출처: transcript:[assistant] skewnono-v3-nuxt d0eba2c5)
- 자연스러운 영어: The items below are records of past work, so deleting them would only erase where things came from.
- 번역 포인트: "출처만 사라집니다"의 "만"은 "얻는 것 없이 잃기만 한다"는 뜻입니다. `would only erase` 의 `only` 가 그 역할을 맡습니다. "출처"는 `source` 한 단어보다 `where things came from` 이나 `the provenance` 가 문맥에 맞습니다. "지우면"은 아직 하지 않은 일이라 가정의 `would` 를 쓰고, 조건절 대신 동명사 주어(`deleting them`)로 줄였습니다.

### 카드 13 — 알림이 뜬 이유 설명   (고급 한글 · 번역)
- 한글 원문: "방금 뜬 백그라운드 작업 실패 알림은 그 서버를 제가 종료해서 나온 것입니다."   (출처: transcript:[assistant] pm-notes 6a5d0980)
- 자연스러운 영어: The background-task failure notice that just popped up is from me shutting down that server.
- 번역 포인트: "방금 뜬"은 `that just popped up` 으로 관계절에 넣습니다. "~해서 나온 것입니다"는 원인을 밝히는 말이라 `is from me shutting down …` 또는 `was caused by my stopping the server` 로 옮깁니다. 앞쪽이 구어, 뒤쪽이 글투입니다. 동명사의 의미상 주어는 구어에서 목적격(`me`), 격식 있는 글에서 소유격(`my`)을 씁니다. 걱정할 일이 아니라는 뜻을 더하려면 `so it's expected` 를 붙입니다.

## 영어 다듬기

### 카드 14 — commit 철자
- 내가 쓴 영어: "commmit and push"   (출처: transcript:[user] pm-notes 0270bee8)
- 정정: commit and push — `commmit` 은 m 이 하나 많습니다. `commit` 은 m 둘, t 하나입니다(과거형과 -ing 에서만 t 가 겹칩니다: `committed`, `committing`).
- 더 나은 표현: Commit and push, please. / Go ahead and commit and push.
- 왜: 명령문 자체는 맞는 표현이고 개발자끼리는 이대로 씁니다. 대상을 밝히려면 `Commit these changes and push to main.` 처럼 목적어와 목적지를 넣습니다. 이 세션에서는 이미 다 올라가 있었으니 `Is everything committed and pushed?` 로 물었으면 답이 한 번에 나왔을 겁니다.

### 카드 15 — delete + 경로
- 내가 쓴 영어: "delete @docs/opencode/"   (출처: transcript:[user] skewnono-v3-nuxt d0eba2c5)
- 더 나은 표현: Delete the docs/opencode/ folder and anything that still points to it.
- 왜: 문법 오류는 없습니다. 다만 폴더만 지우면 그 경로를 적어 둔 곳(`CLAUDE.md`, 설정 파일)이 남아서, 실제로 어시스턴트가 "이 두 줄도 고칠까요"라고 되물었습니다. `anything that still points to it` 을 붙이면 범위가 한 번에 정해집니다. `point to` 는 경로나 링크가 무언가를 가리킬 때 쓰는 동사구입니다. 기록까지 남기고 싶지 않다는 의도라면 `We're not using opencode anymore, so remove the folder and its references.` 처럼 이유를 먼저 말하는 것도 방법입니다.
