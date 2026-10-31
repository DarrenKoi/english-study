# 2026-11-01 — 코칭

오늘 내가 쓴 글은 영어 세 문장뿐이라 (a) 내가 쓴 한글 카드는 없다. 어시스턴트의 한국어 답변에서 고급 문장 네 개를 골라 번역 정독 카드로 만들었다.

## 한글→영어

### 카드 1 — 직접 만들 필요 없다   (고급 한글 · 번역)
- 한글 원문: "아니요, 직접 만들 필요는 없습니다. 오늘 아침에 올린 `/admin/announcements` 페이지가 키를 대신 만들어 줍니다."   (출처: transcript:[assistant] skewnono-v3-nuxt fdff92d0)
- 자연스러운 영어: "No, you don't need to create it yourself. The `/admin/announcements` page I pushed this morning creates the key for you."
- 번역 포인트: "대신 만들어 준다"는 `instead` 보다 `for you` 가 자연스럽다. 영어의 `do X for you` 가 "수고를 대신 덜어 준다"는 뜻을 그대로 담는다. "오늘 아침에 올린 페이지"는 관계대명사 없이 `the page I pushed this morning` 으로 명사 뒤에 붙인다. "직접"은 `yourself` 로 옮기면 강조가 정확히 산다.

### 카드 2 — 읽기와 쓰기의 다른 실패   (고급 한글 · 번역)
- 한글 원문: "배너 하나 때문에 랜딩 페이지가 깨지면 안 되지만, 저장이 실패했는데 성공한 것처럼 보이면 안 되기 때문입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt fdff92d0, Insight)
- 자연스러운 영어: "A single banner should never be able to break the landing page, but a failed save must never look like a success."
- 번역 포인트: 한국어는 "~면 안 된다"를 두 번 반복하지만 영어는 `should never` / `must never` 로 강도를 조금 달리하면 대비가 선다. "배너 하나 때문에"는 `because of one banner` 로 직역하기보다 `A single banner` 를 주어로 세우는 편이 영어답다(무생물 주어). "실패했는데 성공한 것처럼"은 `a failed save … look like a success` 로 명사화해 짧게 줄인다.

### 카드 3 — 첫 쓰기가 곧 초기화   (고급 한글 · 번역)
- 한글 원문: "\"키 없음 = 빈 목록\"으로 정해 두었기 때문에 첫 쓰기가 곧 초기화입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt fdff92d0, Insight)
- 자연스러운 영어: "Because a missing key is treated as an empty list, the first write doubles as initialization."
- 번역 포인트: "A가 곧 B다"는 `A is B` 로 끝내면 밋밋하다. `double as`(~의 역할을 겸하다)를 쓰면 "따로 하지 않아도 같이 된다"는 뉘앙스가 산다. "정해 두었다"는 사람(we decided)보다 규칙 자체를 주어로 한 수동태 `is treated as` 가 설계 설명에 맞다.

### 카드 4 — 먼저 만든 복사본   (고급 한글 · 번역)
- 한글 원문: "지금 클라우드에 있는 `office.py`는 관리자 페이지보다 먼저 만든 복사본이라 add/remove 함수가 없습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt fdff92d0)
- 자연스러운 영어: "The `office.py` currently on the cloud predates the admin page, so it has no add/remove functions."
- 번역 포인트: "~보다 먼저 만든"은 동사 `predate` 하나로 줄어든다(post-date 의 반대). "복사본이라"를 굳이 `is a copy made before` 로 풀지 않아도 문맥에서 복사본임은 드러난다. "지금 클라우드에 있는"은 `currently on the cloud` 처럼 부사+전치사구로 명사 뒤에 붙인다.

## 영어 다듬기

### 카드 1 — 디자인 다 가져왔나
- 내가 쓴 영어: "have you extract all the things that are needed for the design from skewnono_v3_nuxt?"   (출처: transcript:[user] bulk-recipe-copy 87a47375)
- 정정: "**Have** you **extracted** everything the design needs from skewnono_v3_nuxt?"
  - 현재완료는 `have + 과거분사` 라서 `extract` → `extracted`.
  - 문장 첫 글자는 대문자.
- 더 나은 표현: "Have we brought over everything the design needs from skewnono_v3_nuxt?" 또는 빠진 것을 묻는 쪽으로: "Is anything design-related from skewnono_v3_nuxt still missing here?"
- 왜: `all the things that are needed for` 는 길게 돌아간다. `everything the design needs` 로 관계절을 줄이면 같은 뜻이 반으로 줄어든다. 동사도 `extract`(추출하다)보다 `bring over`(옮겨 오다)가 저장소 간 복사 상황에 맞는다. 정말 알고 싶은 것이 "빠진 게 있나"라면 그걸 직접 묻는 편이 답도 바로 나온다. 실제로 어시스턴트는 "다 됐다, 빠진 건 이것들"이라고 답했다.

### 카드 2 — 둘 다 해 줘
- 내가 쓴 영어: "copy the favicon and resync DESIGN.md"   (출처: transcript:[user] bulk-recipe-copy 87a47375)
- 더 나은 표현: "Let's do both: copy the favicon and resync DESIGN.md."
- 왜: 문법 오류는 없다. 어시스턴트가 "favicon 이냐 DESIGN.md 냐" 하고 선택지를 줬으니 `Let's do both:` 를 앞에 붙이면 질문에 대한 답이라는 게 분명해진다. 콜론 뒤에 구체 지시를 두는 형식은 업무 메시지에서 흔하다. 첫 글자 대문자와 마침표만 챙겨도 지시문이 단정해진다.

### 카드 3 — Redis 키를 만들어야 하나
- 내가 쓴 영어: "for banner announcement in the landing page, should I create redis key for that?"   (출처: transcript:[user] skewnono-v3-nuxt fdff92d0)
- 정정: "For **the** banner announcement **on** the landing page, should I create **a** Redis key for **it**?"
  - 셀 수 있는 단수 명사에는 관사가 필요하다: `banner announcement` → `the banner announcement`, `redis key` → `a Redis key`.
  - 웹 페이지 '위에' 보이는 것은 `on the page`. `in the page` 는 HTML 소스 안을 말할 때 쓴다.
  - 앞에서 `For …` 로 대상을 이미 말했으니 끝의 `for that` 은 중복이다. 지우거나 `for it` 으로.
  - 고유명사 Redis 는 대문자.
- 더 나은 표현: "Do I need to create a Redis key for the landing-page banner, or does something already handle that?"
- 왜: 실제 답은 "관리자 페이지가 알아서 만든다"였다. `or does something already handle that?` 을 붙이면 "내가 해야 하나, 이미 되어 있나"를 한 번에 물어 상대가 바로 핵심을 답한다. `landing-page banner` 처럼 명사를 형용사로 앞에 세우면 전치사구가 줄어 문장이 짧아진다.
