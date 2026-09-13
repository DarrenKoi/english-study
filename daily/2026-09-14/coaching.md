# 2026-09-14 — 코칭

> 오늘 transcript 의 `[user]` 메시지 대부분은 Codex/Herdr 가 중계한 검토 요청문("사용자가 … 요청했습니다")이라 내가 직접 쓴 글로 보지 않고 제외했다. 아래 (a) 카드는 내가 직접 친 짧은 지시 두 개다.

## 한글→영어

### 카드 1 — 변경 파일 목록 요청   (내가 쓴 한글)
- 내가 쓴 한글: "변경된 파일 리스트 알려주고"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: List the files that changed.
- 왜 이렇게: "리스트 알려주다"를 `tell me the list` 로 옮기면 어색하다. 영어는 `list` 를 동사로 써서 목적어만 붙이면 끝난다. "변경된 파일"은 `changed files` 도 되지만 관계절 `the files that changed` 가 구어에서 더 자연스럽다. 끝의 "~하고"는 뒤에 다른 지시가 이어질 어조인데, 영어 채팅에서는 그냥 명령문 하나로 끊고 다음 문장을 새로 시작한다. 조금 더 부드럽게는 `Can you list what changed?`.

### 카드 2 — 항목 골라서 진행   (내가 쓴 한글)
- 내가 쓴 한글: "3, 4, 2a 진행해줘"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: Go ahead with 3, 4, and 2a.
- 왜 이렇게: "진행해줘"의 짝은 `proceed with` 가 격식, `go ahead with` 가 구어다. 채팅 지시에는 후자가 맞다. 번호 나열 끝에는 `and` 를 넣는 것이 영어 관례라 `3, 4, and 2a` 로 쓴다. 승인의 뜻을 실으려면 `Approved — go ahead with 3, 4, and 2a.` 처럼 앞에 한 단어를 붙이면 된다.

### 카드 3 — 가정이 아니라 적용 대상이 틀렸다   (고급 한글 · 번역)
- 한글 원문: "모순은 실제로 있습니다. 다만 틀린 쪽은 가정 자체가 아니라 가정을 적용한 대상입니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The contradiction is real. What's wrong, though, is not the assumption itself but what it was applied to.
- 번역 포인트: "실제로 있습니다"를 `exists` 로 옮기면 딱딱하다. `is real` 이 "진짜다"의 어감을 살린다. "틀린 쪽은"은 `What's wrong` 이라는 명사절 주어로 세우고, "A 가 아니라 B" 는 `not A but B` 로 그대로 간다. "가정을 적용한 대상"은 수동태 `what it was applied to` 가 가장 짧다. "다만"은 문두 `However` 보다 문중 `though` 가 리뷰 문체에 어울린다.

### 카드 4 — 픽스처가 결함을 가렸다   (고급 한글 · 번역)
- 한글 원문: "사람이 손으로 만든 픽스처가 실제 입력(crop)과 달라 결함을 가린 경우입니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: This is a case where a hand-built fixture differed from the real input, a crop, and masked the defect.
- 번역 포인트: "~한 경우입니다"는 `This is a case where …` 가 정확한 틀이다. "손으로 만든"은 `hand-built` 한 단어로 압축되고, `hand-crafted` 는 정성 들였다는 뉘앙스라 여기엔 맞지 않는다. "결함을 가리다"는 `hide` 보다 `mask` 가 테스트 문맥의 관용어다. 괄호 속 보충 `(crop)` 은 영어에서 동격 `, a crop,` 으로 푸는 편이 읽기 쉽다.

### 카드 5 — 자동 클릭보다 인계   (고급 한글 · 번역)
- 한글 원문: "미검증 물리 가정 위에서 자동 클릭보다 엔지니어 인계가 옳습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: On an unverified physical assumption, handing off to an engineer beats clicking automatically.
- 번역 포인트: "~ 위에서"는 여기서 "그 가정에 기대어"라는 뜻이라 `on` 이 맞고 `above` 는 오역이다. "A 보다 B 가 옳다"는 `B is better than A` 로도 되지만 `B beats A` 가 짧고 판단의 확신이 실린다. "인계"는 `handoff` 명사도 있으나 동명사 `handing off to an engineer` 가 `clicking automatically` 와 병렬을 이룬다.

### 카드 6 — 커밋에 숨기지 말 것   (고급 한글 · 번역)
- 한글 원문: "맞는 수정이지만 'scale' 커밋에 숨기지 말고 커밋 메시지/CLAUDE.md 에 따로 적을 것."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The fix is right, but don't bury it in the "scale" commit; call it out separately in the commit message and CLAUDE.md.
- 번역 포인트: "숨기다"를 `hide` 로 하면 고의성이 강해진다. 다른 변경 사이에 묻힌다는 뜻이라 `bury` 가 정확하다. "따로 적을 것"의 짝은 `call it out separately` — `call out` 은 눈에 띄게 언급한다는 리뷰 관용구다. 문말 "~할 것"의 지시 어조는 영어에서 그냥 명령문으로 옮긴다.

## 영어 다듬기

### 카드 7 — 랜딩 페이지 정렬 요청
- 내가 쓴 영어: "in the landing page, we have to make more balanced and located for the 시스템 상태, 데이터 반출 금지 component."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in the landing page` → `on the landing page` (페이지·화면 위의 요소는 `on`). `make more balanced and located for the … component` → `make the … components more balanced and better positioned` (`make` 는 목적어가 먼저 와야 하고, `located` 는 "위치한"이라는 상태 형용사라 "배치를 손본다"는 뜻으로는 못 쓴다). 두 컴포넌트를 말하므로 `components` 복수.
- 더 나은 표현: On the landing page, the 시스템 상태 card and the 데이터 반출 금지 notice need to be better balanced and positioned.
- 왜: `we have to make X Y` 는 목적어 자리가 비면 문장이 무너진다. 두 요소를 주어로 세우고 `need to be + 과거분사` 로 바꾸면 무엇을 어떻게 할지가 한 번에 보인다. `balanced` 와 `positioned` 를 과거분사로 맞추면 병렬이 깨끗하다. 한글 고유명사는 그대로 두되 종류(`card`, `notice`)를 붙이면 어시스턴트가 대상을 찾기 쉽다.

### 카드 8 — 스킬 제거 요청
- 내가 쓴 영어: "remove the skill caveman"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: 문법 오류는 없다. 다만 영어에서 이름은 보통 종류 명사 앞에 온다: `the caveman skill`.
- 더 나은 표현: Remove the caveman skill, including its files and any settings that reference it.
- 왜: `the skill caveman` 도 뜻은 통하지만 `the caveman skill` 이 훨씬 자연스럽다(`the Python library`, `the main branch` 와 같은 어순). 한 발 더 나가 "완전히 지워라"는 범위를 밝히면(`including its files and any settings that reference it`) 어시스턴트가 되물을 일이 없다.
