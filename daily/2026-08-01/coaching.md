# 2026-08-01 — 코칭

오늘 배치의 `[user]` 발화는 전부 영어였습니다. `한글→영어` 는 어시스턴트의 고급 한국어를 옮기는 (b) 번역 정독 카드만 싣고, 대신 `영어 다듬기` 를 여덟 장으로 늘렸습니다. 짧은 지시문이 많아 관사·전치사·명사 연쇄에서 배울 게 뚜렷했습니다.

## 한글→영어

### 카드 1 — 재료가 얇았던 날 (고급 한글 · 번역)

- 한글 원문: "오늘 배치는 repo 문서 13건이 거의 다 한국어라 표현 소스로는 얇고, 실제 영어는 plan 문서 안에 박힌 docstring·주석과 트랜스크립트 쪽에 몰려 있었습니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: Almost all thirteen repo documents in today's batch are in Korean, so they are thin as a source of expressions; the real English sits in the docstrings and comments embedded in the plan, and in the transcripts.
- 번역 포인트: "얇다"는 영어에서도 `thin` 이 그대로 통하는 몇 안 되는 비유입니다. 다만 한국어는 그냥 "얇다"로 끝내도 되지만 영어는 무엇에 대해 얇은지를 `as a source of expressions` 로 밝혀 줘야 문장이 서 있습니다. "몰려 있었습니다"를 `were concentrated in` 으로 옮기면 통계 보고서 같아지므로, 자리를 차지한다는 뜻의 `sits in` 이 문서 이야기에 어울립니다. "박힌"은 `embedded in` — 다른 것 안에 끼워져 있다는 그림이 정확히 겹칩니다.

### 카드 2 — 정렬을 건드리지 않고 끼워 넣기 (고급 한글 · 번역)

- 한글 원문: "기존 정렬이 구두점을 무시하는 방식이라, 전체 재정렬 대신 정규화 키로 삽입 위치만 찾는 편이 기존 순서를 건드리지 않아 안전합니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: The existing order ignores punctuation, so finding the insertion point with a normalized key is safer than re-sorting the whole file: it leaves every existing line where it is.
- 번역 포인트: "~하는 편이 안전합니다"는 비교급 `is safer than ~` 으로 바로 받는 편이 낫습니다. `It is safer to ~ rather than to ~` 로 늘리면 원문의 간결함이 사라집니다. "건드리지 않아"라는 부정 표현은 영어에서 긍정문 `leaves every existing line where it is` 로 뒤집으면 더 구체적입니다 — 무엇을 안 하는지보다 무엇이 그대로 남는지를 말해 주기 때문입니다. 이유를 콜론으로 뒤에 매다는 것도 영어 산문의 흔한 리듬입니다.

### 카드 3 — 상한이 지켜 준 몫 (고급 한글 · 번역)

- 한글 원문: "`doc_budget_share` 0.6 상한이 트랜스크립트 몫을 지켜 준 덕에 코칭 카드가 살아남았습니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: The 0.6 cap on `doc_budget_share` held part of the budget open for the transcripts, and that is what kept the coaching cards alive.
- 번역 포인트: "~한 덕에"를 `thanks to` 로 옮기면 감사 인사처럼 가벼워집니다. 인과를 못 박고 싶을 때는 `and that is what kept ~` 처럼 분열문으로 원인을 뒤에서 지목하는 편이 셉니다. "몫을 지켜 주다"는 `protect a share` 보다 `hold part of the budget open` — 자리를 비워 둔다는 그림이 예산 배분에 정확합니다. "살아남았습니다"는 `survived` 도 되지만, 지켜 준 쪽을 주어로 세운 이상 `kept ~ alive` 가 구조에 맞습니다.

## 영어 다듬기

### 카드 1 — 문제 없으면 정리해 달라

- 내가 쓴 영어: "if no problem, clean up worktrees"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 조건절에 주어와 동사가 없습니다 → `if there's no problem`. 그 저장소의 특정 워크트리들을 가리키므로 `the worktrees` 로 관사도 붙습니다.
- 더 나은 표현: If nothing looks off, go ahead and clean up the worktrees.
- 왜: `if no problem` 은 표지판에서나 통하는 메모체라 문장에서는 뼈대가 빠진 느낌을 줍니다. 판단을 상대에게 맡기는 자리이므로 `if nothing looks off`(이상해 보이는 게 없으면)나 `if everything checks out`(다 확인되면)이 어울리고, `go ahead and ~` 가 "확인은 네가 하고 그다음 진행하라"는 위임까지 부드럽게 담습니다.

### 카드 2 — 브랜치 목록을 물을 때

- 내가 쓴 영어: "what is the git branch list currently?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: What branches do I have right now?
- 왜: 문법은 틀리지 않았지만 `the git branch list` 라는 명사 덩어리가 '깃 브랜치 목록'을 그대로 옮긴 모양입니다. 영어는 목록을 명사로 세우기보다 `What branches ~` 로 바로 묻습니다. `currently` 는 문어체라 구어에서는 `right now` 가 자연스럽고, 범위까지 정하고 싶다면 `Can you list the current branches, local and remote?` 처럼 한 번에 말해 주면 되묻지 않아도 됩니다.

### 카드 3 — 아이콘 제거 요청

- 내가 쓴 영어: "remove the icon for color mode in the top nav."   (출처: transcript:[user] flask_modules)
- 더 나은 표현: Remove the color-mode toggle from the top nav.
- 왜: `the icon for color mode` 는 전치사로 이어 붙인 설명형이라 길어집니다. 영어는 `color-mode icon` 처럼 명사를 앞에 붙이고, 하이픈이 두 단어를 한 수식어로 묶어 줍니다. 게다가 그 아이콘은 눌러서 상태를 바꾸는 물건이니 `toggle` 이 제 이름입니다. 위치에는 `in` 보다 `from` 이 맞습니다 — 제거는 어디에서 떼어내는지를 말하는 동사이기 때문입니다.

### 카드 4 — 이유를 붙이는 문장

- 내가 쓴 영어: "As we have app color mode in the settings, we do not need it anymore."   (출처: transcript:[user] flask_modules)
- 정정: `color mode` 는 셀 수 있는 명사라 관사가 필요합니다 → `we have an app color mode in the settings`.
- 더 나은 표현: Now that the app has a color-mode setting, we don't need it anymore.
- 왜: `As` 로 여는 이유절은 격식 있는 글에서는 맞지만, 구어에서는 "~하는 동안"으로도 읽혀 한 박자 걸립니다. 새로 생긴 사정을 근거로 댈 때는 `Now that ~`("이제 ~하니")이 시점까지 함께 담습니다. `we have app color mode` 는 가진 주체가 우리인지 앱인지 흐리므로 주어를 앱으로 넘겨 `the app has a color-mode setting` 이라 하면 분명해지고, 더 격식 있게는 `since that setting now lives in the app's preferences` 입니다.

### 카드 5 — 다른 저장소에도 같은 작업

- 내가 쓴 영어: "do the same in skewnono_v3_nuxt"   (출처: transcript:[user] flask_modules)
- 더 나은 표현: Do the same for `skewnono_v3_nuxt`.
- 왜: `in` 도 통하지만 작업 대상을 가리킬 때는 `for` 가 자연스럽습니다 — `in` 은 그 안에서 벌어지는 일, `for` 는 그 대상을 위해 해 주는 일이라는 결이 있습니다. 무엇을 되풀이하라는 것인지 못 박고 싶다면 목적어를 되살려 `Apply the same .gitignore change to skewnono_v3_nuxt.` 라고 쓰면 됩니다.

### 카드 6 — 문구를 고쳐 달라

- 내가 쓴 영어: "fix the members blocker wording too"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Reword the `members` blocker as well.
- 왜: `fix the members blocker wording` 은 명사를 넷이나 이어 붙인 데다 동사 `fix` 가 약해서 무엇을 어떻게 하라는지 흐려집니다. `reword`(문구를 다시 쓰다) 하나면 목적어가 하나로 줄고 뜻이 또렷해집니다. 문장 끝의 `too` 는 구어에서 흔하지만 지시문에서는 `as well` 이 조금 더 분명하고, 부탁의 자리라면 `Please reword the members blocker as well.` 이 부드럽습니다.

### 카드 7 — 앞선 기록을 가리키며 확인 요청

- 내가 쓴 영어: "now check the plumbing-fixes worktree from the 19:07 note."   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Now look into the plumbing-fixes worktree the 19:07 note mentions.
- 왜: `from the 19:07 note` 는 그 워크트리가 노트에서 나왔다는 뜻으로도 읽혀 잠깐 걸립니다. 목적격 관계대명사를 생략한 관계절 `the 19:07 note mentions` 로 바꾸면 출처가 아니라 언급이라는 게 분명해집니다. `check` 는 있는지 없는지만 보는 느낌이라, 상태를 살펴 달라는 자리에는 `look into`(들여다보다)나 `follow up on`(마무리까지 챙기다)이 어울립니다.

### 카드 8 — 남은 항목을 훑어 달라

- 내가 쓴 영어: "check the rest of open-jobs for stale entries"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Go through the rest of `open-jobs` and flag anything that's gone stale.
- 왜: `check A for B`(A 를 훑어 B 를 찾다)는 정확한 구문이라 그대로 둬도 좋습니다. 다만 `go through ~` 로 바꾸면 처음부터 끝까지 본다는 범위가 살고, `flag ~`(표시해 두다)를 붙이면 찾은 뒤 무엇을 하길 원하는지까지 한 문장에 들어갑니다. 현재완료 `that's gone stale` 은 "그사이 낡아 버린"이라는 변화의 결과를 담아 `stale entries` 보다 한 겹 정확합니다.
