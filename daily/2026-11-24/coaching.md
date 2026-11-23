# 2026-11-24 — 코칭

오늘 직접 쓴 한국어는 ARC TF 피드백 장표를 고치면서 남긴 짧은 지시들입니다. 메모처럼 주어와 조사를 뺀 문장이 많아서, 영어로 옮길 때는 누가 무엇을 하는지를 다시 세워야 합니다. 영어로는 두 가지 꼴을 같이 적었어요. 동료에게 채팅으로 보내는 한 줄, 그리고 장표에 들어가는 개조식 문구입니다. 어제 실행 기록에 `[user]` 로 찍힌 파이프라인 지침문은 어제 카드로 다뤘으므로 뺐습니다. 내가 쓴 영어 문장은 없어서 영어 다듬기는 건너뜁니다.

## 한글→영어

### 카드 1 — 올라가 있으면 안 남겨도 됨   (내가 쓴 한글)
- 내가 쓴 한글: "정리되어 올라가 있으면 남기지 않아도 됌. .scratch는 local에만 보존."   (출처: transcript:[user] skewnono_v3_nuxt 8c14fe26, 이전 대화 인용)
- 자연스러운 영어: If it's already been cleaned up and pushed, there's no need to keep a copy. Keep `.scratch` local only.
- 왜 이렇게: "올라가 있으면"은 원격에 올라간 상태이므로 `pushed` 나 `it's already up` 으로 받습니다. "남기지 않아도 됨"은 금지가 아니라 불필요이니 `don't have to` 나 `there's no need to` 를 써요. `must not` 으로 옮기면 뜻이 바뀝니다. "local에만 보존"은 `local only` 가 굳은 말이고, 풀어 쓰면 `Don't commit .scratch; keep it on this machine.` 입니다. 한글 맞춤법은 "됌"이 아니라 "됨"입니다.

### 카드 2 — 반영보다는 피드백 내용으로 시작   (내가 쓴 한글)
- 내가 쓴 한글: "기획안 피드백 반영보다는 피드백 내용으로 시작하고."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Open with the feedback itself rather than with how we've incorporated it into the proposal.
- 왜 이렇게: "A 보다는 B 로 시작"은 `open with B rather than A` 로 순서를 뒤집어 긍정 쪽을 먼저 냅니다. "반영"은 `reflect` 로 직역하기 쉬운데, 피드백을 문서에 넣었다는 뜻이면 `incorporate` 나 `address` 가 맞아요. `reflect` 는 "문서가 피드백을 반영하고 있다"처럼 문서가 주어일 때 씁니다. `the feedback itself` 의 `itself` 가 "내용 그 자체"를 살립니다.

### 카드 3 — 질문마다 논의, 검토, 답변을 담는 형식   (내가 쓴 한글)
- 내가 쓴 한글: "팀장님의 각 질문에 대해서 논의 , 검토, 답변등을 담는 형식으로 pptx를 만들어줘."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Build the deck so that each of the team lead's questions gets its own slide covering the discussion, our review, and the answer.
- 왜 이렇게: "~을 담는 형식으로"를 `in a format that contains` 로 옮기면 뜻은 통해도 딱딱합니다. `so that each question gets its own slide covering …` 처럼 결과를 그려 주는 쪽이 자연스러워요. "팀장님"은 직함을 그대로 부르는 영어 습관이 없어서 `the team lead` 나 `my manager` 로 받습니다. "등"은 `etc.` 를 붙이지 않고 셋을 나열하는 것으로 충분합니다. "pptx"는 말할 때 `the deck`, `the slides` 입니다.

### 카드 4 — 위치 안내는 최종 수정 때   (내가 쓴 한글)
- 내가 쓴 한글: "장표 어느 위치에 뭐를 추가하거나 있다는 것은 나중에 피드백을 마치고 최종 수정할 때 넣으면 돼"   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Notes on where things were added or already sit in the deck can wait until the final revision, once we've finished going through the feedback.
- 왜 이렇게: "나중에 ~할 때 넣으면 돼"는 `can wait until …` 가 딱 맞습니다. "지금은 안 해도 된다"와 "그때 한다"를 한꺼번에 말해요. "어느 위치에 뭐를 추가하거나 있다는 것"은 `where things were added or already sit` 로, 간접의문문 하나에 동사 둘을 걸었습니다. `sit` 은 내용이 문서 어디에 자리 잡고 있다는 뜻으로 흔히 씁니다. "피드백을 마치고"는 `once we've finished going through the feedback` 로, `once + 현재완료` 가 "끝난 다음에"입니다.

### 카드 5 — 커밋하고 push 해줘   (내가 쓴 한글)
- 내가 쓴 한글: "커밋하고 push 해줘"   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Go ahead and commit and push.
- 왜 이렇게: `Commit and push.` 만으로도 되지만, 앞에서 "커밋은 하지 않았습니다"라는 보고를 받고 허락하는 상황이라 `Go ahead and …` 가 어울립니다. "이제 해도 된다"는 승인이 실려요. 더 정중하게는 `Please commit and push when you're ready.`, 채팅에서는 `Ship it.` 도 씁니다.

### 카드 6 — 누가 실익이 낮은지 안 밝혔네   (내가 쓴 한글)
- 내가 쓴 한글: "누가 실익이 낮음? 명시 안했네."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Low benefit for whom? It doesn't say.
- 왜 이렇게: 한국어 "누가"는 주어처럼 보여도 영어에서는 "누구에게 이득이 적은가"이므로 `for whom` 입니다. 말로는 `Who's it low-value for?` 도 좋아요. "명시 안 했네"는 `It doesn't say.` 가 가장 가볍고, 리뷰 코멘트로는 `The slide doesn't specify who.` 나 `This needs a subject.` 로 씁니다. "실익"은 `practical benefit`, 사업 문맥에서는 `upside` 나 `payoff` 도 됩니다.

### 카드 7 — BP사가 움직일 인센티브가 없음   (내가 쓴 한글)
- 내가 쓴 한글: "BP사가 움직일만한 인센티브가 부재."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: The vendor has no incentive to act. (장표 문구: No incentive for the vendor to act)
- 왜 이렇게: "인센티브가 부재"를 `absence of incentive` 로 옮기면 명사만 쌓여 무겁습니다. `have no incentive to + 동사` 가 영어에서 굳은 틀이에요. "움직일 만한"은 `to act` 나 `to move on this` 로 받고, "움직이다"를 `move` 하나로 쓰면 이사하다로 읽힐 수 있습니다. "BP사"는 사내 용어이니 밖에서는 `the vendor`, `the equipment supplier`, `our partner company` 가운데 관계에 맞는 것을 고릅니다. 개조식 장표에서는 동사를 빼고 `No incentive for A to B` 로 적습니다.

### 카드 8 — 현업이 투자한 시간을 인정받지 못함   (내가 쓴 한글)
- 내가 쓴 한글: "현업 투자 시간 인정 받지 못함. (공식 이런 표현 없이)"   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: The time field engineers put in goes unrecognized. (Leave out the word "officially.")
- 왜 이렇게: "인정받지 못함"은 `is not recognized` 도 되지만 `go unrecognized` 가 "아무도 알아주지 않은 채 지나간다"는 상태를 더 잘 담습니다(`go unnoticed`, `go unanswered` 와 같은 틀). "투자한 시간"은 `the time they put in` 이 구어이고 격식으로는 `the time they invest` 입니다. "현업"은 맞는 한 단어가 없어서 하는 일로 풀어요. 여기서는 `field engineers`, 넓게는 `the operating teams` 나 `people on the floor` 입니다. 괄호 속 지시는 `Leave out …` 또는 `Drop the word …` 로 옮깁니다.

### 카드 9 — 겸직이란 표현 안 씀   (내가 쓴 한글)
- 내가 쓴 한글: "겸직이란 표현 안씀. 정규 조직 신설 불가능 (삭제)"   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Don't use the term "dual role." And delete the line saying a permanent team can't be set up.
- 왜 이렇게: "겸직"은 본업과 TF 를 같이 맡는다는 뜻이라 `dual role` 이나 `a part-time assignment` 가 가깝습니다. `concurrent position` 은 사전에는 나오지만 임원 겸임 같은 공식 발령에 씁니다. "표현"은 낱말 하나를 가리키므로 `expression` 보다 `term` 이나 `wording` 이에요. "정규 조직"은 `a permanent team`(TF 의 반대말은 `permanent`), "신설"은 `set up` 이나 `establish` 입니다. 삭제 지시에서는 `the line saying …` 으로 무엇을 지울지 짚어 줍니다.

### 카드 10 — 현업 수고 → 현업 과제 인정   (내가 쓴 한글)
- 내가 쓴 한글: "현업 수고 -> 현업 과제 인정."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Change "the field teams' hard work" to "recognition of this as an official assignment for the field teams."
- 왜 이렇게: 화살표는 `Change A to B` 나 `Replace A with B` 로 풉니다. 두 틀은 전치사가 달라요(`change … to`, `replace … with`). "수고"는 `effort`, `hard work` 인데 고마움의 말이라 평가 항목으로는 약합니다. 고친 쪽 "과제 인정"은 그 일이 정식 업무로 잡힌다는 뜻이어서 `counts as an official assignment` 나 `is credited as project work` 처럼 `count as`, `credit` 을 쓰면 인사 평가에 들어간다는 뜻이 전해집니다.

### 카드 11 — 다른 장표에도 수정 적용   (내가 쓴 한글)
- 내가 쓴 한글: "다른 장표에도 수정 적용."   (출처: transcript:[user] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: Apply the same edits to the other decks too.
- 왜 이렇게: "수정"은 글자를 고친 것이므로 `edits` 나 `changes` 이고 `fix` 는 버그에 씁니다. `the same` 을 넣어야 "방금 그 수정을"이 살아요. "장표"가 발표 자료 한 벌이면 `deck`, 낱장이면 `slide` 입니다. 여기서는 rev2, 팀원용처럼 자료 단위라 `decks` 입니다. 같은 뜻으로 `Carry these changes over to the other decks.` 도 자주 씁니다.

### 카드 12 — 지운 게 아니라 되돌릴 수 있음   (고급 한글 · 번역)
- 한글 원문: "완전히 지운 것이 아니라서 필요하면 되돌릴 수 있습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 8c14fe26)
- 자연스러운 영어: They haven't been permanently deleted, so you can restore them if you need to.
- 번역 포인트: 한국어는 "~아니라서"로 이유를 앞에 두는데, 영어는 사실을 먼저 말하고 `so` 로 귀결을 붙이는 쪽이 읽기 편합니다. "완전히 지우다"는 `completely` 보다 `permanently delete` 가 파일에 쓰는 짝이에요. "되돌리다"는 휴지통에서 꺼내는 것이면 `restore`, 변경을 무르는 것이면 `undo` 나 `revert` 입니다. 주어 없는 문장이라 `they`(메모 두 개)를 세웠습니다.

### 카드 13 — 실수로 커밋된 파일 삭제도 같이   (고급 한글 · 번역)
- 한글 원문: "예전에 실수로 커밋된 LibreOffice lock 파일 삭제도 이 커밋에 넣었습니다."   (출처: transcript:[assistant] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: This commit also removes a LibreOffice lock file that had been committed by mistake earlier.
- 번역 포인트: "삭제도 넣었습니다"를 `I included the deletion` 으로 옮기면 명사가 무거워집니다. 커밋을 주어로 세워 `This commit also removes …` 라고 하면 동사 하나로 끝나요. "예전에 실수로 커밋된"은 이번 커밋보다 앞선 일이라 과거완료 수동 `had been committed` 가 맞습니다. `by mistake` 와 `accidentally` 는 바꿔 써도 됩니다.

### 카드 14 — 최종 수정 때 맞출 것으로 보고 손대지 않음   (고급 한글 · 번역)
- 한글 원문: "최종 수정 때 맞추는 것으로 보고 손대지 않았습니다."   (출처: transcript:[assistant] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: I left those untouched, on the assumption that they'll be brought in line during the final revision.
- 번역 포인트: "~으로 보고"는 판단의 근거이므로 `on the assumption that` 이나 `assuming` 으로 받습니다. 추측임을 밝혀 두는 말이라 보고문에서 쓸모가 커요. "손대지 않다"는 `leave A untouched` 또는 `leave A as is`. "맞추다"는 여기서 표현을 통일한다는 뜻이라 `bring in line` 이나 `align` 을 씁니다. `match` 는 색·값이 같다는 쪽입니다.

### 카드 15 — 렌더링해서 보지는 않았는데   (고급 한글 · 번역)
- 한글 원문: "rev2와 팀원용은 렌더링해서 보지는 않았는데, 바뀐 장이 피드백 장표에서 확인한 것과 같은 슬라이드입니다."   (출처: transcript:[assistant] pm_notes arc-tf 77eb8e9c)
- 자연스러운 영어: I didn't render rev2 or the team deck to check them visually, but the slides that changed are the same ones I verified in the feedback deck.
- 번역 포인트: "~지는 않았는데"는 하지 않은 일을 먼저 털어놓고 그래도 괜찮은 이유를 대는 구조라 `I didn't …, but …` 로 그대로 갑니다. 부정문 안의 "A 와 B"는 `and` 가 아니라 `or` 예요(`didn't render A or B`). "렌더링해서 보다"는 `render … to check them visually` 로 목적을 풀었습니다. "확인한 것과 같은"은 `the same ones I verified` 로, `ones` 가 `slides` 를 대신합니다.
