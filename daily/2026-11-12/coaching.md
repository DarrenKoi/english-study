# 2026-11-12 — 코칭

출처는 모두 `transcript:` pm-notes 0270bee8 세션입니다(REA 문서 최신화 → Codex에게 herdr로 조사 위임 → 프롬프트 완성형으로 교체 → 커밋·푸시·Artifact 재게시). 카드 9는 english-study f02163d6 세션에서 가져왔습니다. 직접 쓴 영어는 `commit and push`, `via herdr`, `republish` 같은 조각뿐이고 완결된 문장이 없어서 영어 다듬기는 생략하고, 해당 조각은 카드 2와 5에서 함께 다룹니다.

## 한글→영어

### 카드 1 — 조사하고, 있으면 추가   (내가 쓴 한글)
- 내가 쓴 한글: "최신 REA 기법 조사하고 혹시 추가할 내용과 지식이 있으면 추가해줘."   (출처: transcript:[user])
- 자연스러운 영어: Look into the latest REA techniques and add anything worth including.
- 왜 이렇게: "혹시 ~이 있으면 추가해줘"를 `if there is anything to add, add it` 로 옮기면 `add` 가 두 번 나옵니다. `add anything worth including` 처럼 `anything + 형용사구` 로 묶으면 조건이 목적어 안에 들어갑니다. "조사하다"는 가볍게 `look into`, 자료를 찾아 정리하는 일이면 `research` 를 씁니다. "내용과 지식"은 영어에서 하나로 합쳐도 뜻이 빠지지 않습니다. 대상을 밝히려면 끝에 `to the reverse_engineering docs` 를 붙입니다.

### 카드 2 — ~에게도 시켜서 같이   (내가 쓴 한글)
- 내가 쓴 한글: "최신 REA 노하우는 codex에게도 시켜서 같이 작성 (via herdr)"   (출처: transcript:[user])
- 자연스러운 영어: Have Codex work on the latest REA know-how as well, through herdr, and write it up together.
- 왜 이렇게: "~에게 시키다"는 사역동사 `have + 사람 + 동사원형` 이 가장 가볍습니다. `make` 는 억지로 시키는 느낌이고 `get Codex to …` 는 구어입니다. "~도"는 `as well` 이나 `too` 로 받습니다. 직접 쓴 `via herdr` 는 문법상 맞고 메모에서는 그대로 써도 됩니다. 말로 할 때는 `through herdr` 나 `using herdr` 가 더 흔합니다. "작성"은 조사한 것을 문서로 정리한다는 뜻이라 `write` 보다 `write it up` 이 맞습니다.

### 카드 3 — ~도 넣어줬어?   (내가 쓴 한글)
- 내가 쓴 한글: "예시로 던질 수 있는 프롬프트들도 넣어줬어?"   (출처: transcript:[user])
- 자연스러운 영어: Did you also include example prompts I can try out?
- 왜 이렇게: "넣어줬어?"는 끝난 일을 확인하는 질문이라 `Did you include …?` 입니다. "~도"는 `also` 를 동사 앞에 둡니다. "예시로 던질 수 있는"은 `prompts I can throw` 로 직역하면 어색합니다. 영어에서는 `example prompts I can try out` 이나 `sample prompts I could use` 라고 합니다. 한국어의 "던지다" 비유를 살리고 싶으면 `prompts I can throw at it` 처럼 `at it` 을 붙여야 자연스럽습니다.

### 카드 4 — 응, ~로 바꿔줘   (내가 쓴 한글)
- 내가 쓴 한글: "응 완성형으로 바꿔줘"   (출처: transcript:[user])
- 자연스러운 영어: Yes, make them ready to use as-is.
- 왜 이렇게: "완성형"은 한 단어로 옮기기 어렵습니다. 여기서는 "빈칸 없이 그대로 붙여 넣어 쓸 수 있는"이라는 뜻이라 `ready to use as-is` 나 `copy-paste ready` 가 맞습니다. `complete` 만 쓰면 "빠진 항목이 없는" 정도로 약하게 들립니다. "바꿔줘"는 `change them to` 보다 `make them + 형용사` 가 짧습니다. 글로 쓴다면 `Yes, please turn them into fully specified prompts.`

### 카드 5 — 완료 후 커밋, 재게시도   (내가 쓴 한글)
- 내가 쓴 한글: "완료 후 commit and push. claude artifact에 republish도 진행."   (출처: transcript:[user])
- 자연스러운 영어: Once that's done, commit and push, and republish the Claude artifact too.
- 왜 이렇게: "완료 후"는 `After completion` 도 되지만 딱딱합니다. 대화에서는 `Once that's done` 이나 `When you're done` 이 자연스럽습니다. 직접 쓴 `commit and push` 는 그대로 맞는 표현입니다. `republish` 는 타동사라 `republish to the artifact` 가 아니라 `republish the artifact` 로 목적어를 바로 받습니다. 같은 링크를 유지한다는 뜻까지 넣으려면 `republish it to the same link` 라고 합니다(이때 `it` 은 페이지). "~도 진행"의 "진행"은 영어로 옮길 필요가 없고 `too` 하나로 충분합니다.

### 카드 6 — 어디까지 확인했는지 밝히기   (고급 한글 · 번역)
- 한글 원문: "모든 내용은 upstream 문서와 릴리스 노트 대조까지만 했습니다. 회사 Windows PC, pi, 사내 모델에서 실제로 돌려 보지는 않았습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: Everything here has only been checked against the upstream docs and release notes. I haven't actually run any of it on the office Windows PC, with pi, or against the in-house models.
- 번역 포인트: "~까지만 했습니다"의 한계 표시는 `only` 를 과거분사 앞에 두어 `has only been checked against` 로 옮깁니다. "대조"는 `check against` 가 검증의 뜻을 살립니다. 둘째 문장의 "~지는 않았습니다"는 대조의 보조사 "는"이 핵심인데, 영어에서는 `actually` 가 그 역할을 합니다. 환경 세 개는 전치사를 각각 맞춰(`on` 기기, `with` 도구, `against` 모델) 나열하면 원어민 글처럼 읽힙니다.

### 카드 7 — 있긴 한데, 다만   (고급 한글 · 번역)
- 한글 원문: "네, 들어 있습니다. 다만 대부분 그대로 붙여 넣을 완성형은 아닙니다."   (출처: transcript:[assistant])
- 자연스러운 영어: Yes, they're in there. Most of them aren't ready to paste in as-is, though.
- 번역 포인트: "다만"을 문두 `However` 로 옮기면 글투가 됩니다. 대화에서는 문장 끝 `though` 가 같은 일을 가볍게 합니다. "들어 있습니다"는 `they are included` 보다 `they're in there` 가 구어에 맞습니다. "대부분 ~은 아닙니다"는 부분 부정이라 `Most of them aren't …` 로 주어에 수량을 둡니다. `Not all of them are …` 로 쓰면 "일부만 아니다"로 뜻이 약해집니다.

### 카드 8 — 원인과 결과를 한 문장에   (고급 한글 · 번역)
- 한글 원문: "main 브랜치는 매일 바뀌어서 upstream 문서가 배포본에 없는 기능까지 설명합니다."   (출처: transcript:[assistant])
- 자연스러운 영어: The main branch changes daily, so the upstream docs describe features that haven't shipped in a release yet.
- 번역 포인트: "~어서"는 `because` 로 앞세우기보다 `A, so B` 로 한국어 어순을 그대로 따르는 편이 읽기 쉽습니다. "배포본에 없는 기능"은 `features not in the release` 보다 `features that haven't shipped yet` 이 개발자 영어답습니다. `ship` 을 자동사로 쓰면 "출시되다"입니다. "~까지"의 뉘앙스(거기까지 나아가)는 `even` 을 넣어 `even describe features …` 로 살려도 됩니다.

### 카드 9 — 실수와 수습을 담담하게   (고급 한글 · 번역)
- 한글 원문: "처음에 전체를 다시 정렬했더니 기존 항목 수백 줄의 순서가 바뀌어서, 파일을 되돌리고 새 줄만 제자리에 끼워 넣었습니다."   (출처: transcript:[assistant], english-study f02163d6)
- 자연스러운 영어: I first re-sorted the whole file, which reordered hundreds of existing lines, so I restored it and inserted only the new lines in their proper places.
- 번역 포인트: "~했더니 ~해서 ~했습니다"의 세 단계는 `, which …` 계속적 관계절과 `, so …` 로 이으면 한 문장에 담깁니다. `which` 가 앞 절 전체(다시 정렬한 일)를 받는 용법입니다. "제자리에"는 `in their proper places` 이고 줄이 여러 개라 복수로 맞춥니다. 같은 세션의 영어 원문 `My sort reordered existing index lines. I'll restore the file and insert only the new lines.` 와 견주어 보면, 계획(`I'll`)과 사후 보고(과거형)의 시제 차이가 보입니다.
