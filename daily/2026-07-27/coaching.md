# 2026-07-27 — 코칭

> 오늘 배치에는 직접 쓴 한국어 문장이 없었습니다. 트랜스크립트의 한글은 `셋업 미리보기`·`라이브 알람` 같은 UI 이름뿐이고, 어시스턴트 발화도 전부 영어였습니다(`repo:` 문서의 한국어는 코칭 대상 밖). 그래서 한글→영어 섹션은 비우고, 영어로 지시한 다섯 건을 다뤘습니다. 오늘은 실제 문법 오류가 여럿 나와서 정정할 것이 많습니다.

## 영어 다듬기

### 카드 1 — 채팅 페이지에서 상단 탭이 사라진 문제

- 내가 쓴 영어: "in the chat page, you lost the top nav buttons. other pages keep them. fix it when you entering the chatpage"   (출처: transcript:[user] skewnono_v3_nuxt, 99399c55)
- 정정: 세 군데입니다.
  1. `in the chat page` → **`on the chat page`**. 영어는 웹 페이지를 **평평한 면**으로 봅니다. 그래서 on 이에요 — `on this page`, `on the home page`, `on screen`. in 을 쓰면 문서 안쪽 어딘가라는 뜻이 되어 URL 단위를 가리키지 못합니다. 예외는 `in the modal`, `in the sidebar` 처럼 실제로 테두리가 있는 상자입니다.
  2. `when you entering` → **`when you enter`** 또는 **`when entering`**. 접속사 `when` 뒤에 주어(`you`)를 세웠으면 반드시 정동사가 와야 합니다. -ing 만 쓰려면 주어를 지워야 해요. 둘을 섞은 `when you entering` 은 흔한 실수인데, "주어를 남기면 동사도 시제를 갖는다"만 기억하면 안 틀립니다.
  3. `chatpage` → **`chat page`**. 두 단어입니다. `homepage` 는 붙여 쓰지만 `chat page`, `login page`, `settings page` 는 띄어 씁니다.
- 더 나은 표현: "The top nav buttons disappear on the chat page — every other page keeps them. Please make them render on `/chat` too."
- 왜: 문법보다 **주어 선택**이 더 큽니다. `you lost the top nav buttons` 는 상대를 주어로 세워 "네가 잃어버렸다"가 되어, 버그 신고가 책임 추궁처럼 읽힙니다. 증상을 주어로 올려 `The buttons disappear` 라고 하면 같은 사실이 관찰 보고가 돼요. 상대가 정말 만든 문제일 때도 이렇게 씁니다 — 영어권 버그 리포트의 기본값입니다.

  뒷문장의 `fix it when you entering the chatpage` 는 시제를 고쳐도 여전히 애매합니다. 문자 그대로는 "들어갈 때 고쳐라"가 되어 **고치는 시점**을 지정한 말로 읽히거든요. 의도는 "들어갔을 때 보이도록 고쳐라"이니, 목적을 `so that` 이나 `make … render` 로 붙여야 뜻이 닫힙니다. 지시문에서 `when` 은 조건인지 시점인지 자주 헷갈리는 자리라, 결과를 원할 때는 `so (that)` 쪽으로 가는 게 안전합니다.

### 카드 2 — fab 폴백 규칙 선언

- 내가 쓴 영어: "if no fab is remembered (empty or no memory from user side) we fall back to \"R3\". that is the rule."   (출처: transcript:[user] skewnono_v3_nuxt, 99399c55)
- 정정: `from user side` → **`on the user's side`** 또는 **`from the user side`**. 관사가 빠졌습니다. `side` 는 셀 수 있는 명사라 맨몸으로 못 씁니다. 다만 이 자리라면 `nothing stored on the user's side` 처럼 소유격이 자연스럽습니다. (조건절과 종결부의 문법은 정확합니다.)
- 더 나은 표현: "If no fab is remembered — empty, or nothing stored on the user's side — we fall back to R3. That's the rule, not a special case for this one page."
- 왜: 이 문장은 **실제로 효과를 봤습니다.** `that is the rule` 이라는 한마디 덕분에 상대가 한 곳만 고치지 않고 같은 규칙이 흩어져 있는 여섯 군데를 전부 찾아 하나로 모았어요. 규칙을 선언하는 문장은 이렇게 짧고 단정할수록 힘이 셉니다.

  다만 두 가지를 올릴 수 있습니다. 먼저 `that is` → `That's`. 규칙을 못 박는 자리에서는 축약형이 오히려 단호하게 들립니다. `that is the rule` 은 한 박자 늘어져 설명조가 돼요. 그리고 괄호 대신 대시입니다. 괄호는 "곁다리 정보"라는 신호라 조건의 정의가 부차적으로 밀리는데, 대시로 감싸면 같은 내용이 문장의 본류에 남습니다.

  뒤에 `not a special case for this one page` 를 붙인 것도 의도가 있습니다. 이 대화에서 상대가 처음엔 한 군데만 고쳤고, 그다음에야 여섯 군데를 찾았거든요. `X, not Y` 로 범위를 미리 잘라 두면 그 왕복이 줄어듭니다.

### 카드 3 — 여백 정리 요청

- 내가 쓴 영어: "can you organize the empty spaces in mag-pixel 셋업 미리보기?"   (출처: transcript:[user] skewnono_v3_nuxt, fe1dc34e)
- 정정: `the empty spaces` → **`the empty space`**. 여백을 뜻하는 space 는 불가산입니다. `spaces` 로 복수를 만들면 "구획된 공간들"(주차 공간, 사무 공간)이 되어 버려요. `there's not enough space`, `a lot of empty space` 처럼 단수로 씁니다. 문두 대문자 `Can` 도 함께.
- 더 나은 표현: "Can you tighten up the empty space in the mag-pixel 셋업 미리보기 card?"
  격식을 올리면: "Could you reclaim the dead space in the 셋업 미리보기 card?"
- 왜: `organize` 가 자리를 못 찾습니다. 이 동사는 흩어진 것을 분류하고 정돈한다는 뜻이라 파일·일정·서랍에 붙지, 비어 있는 면적에는 안 붙어요. 여백에 쓰는 동사는 따로 있습니다 — `tighten up`(조이다), `close up`(붙이다), `reclaim`(되찾다), `trim`(잘라 내다).

  실제로 상대가 이 요청을 받아 쓴 말이 **`dead space`** 였습니다. 의도 없이 생긴 죽은 여백을 가리키는 현장 용어이고, 의도된 여백인 `whitespace` 와 정반대 평가를 담습니다. 앞으로 이 요청을 할 때 `dead space` 를 먼저 꺼내면 "여백이 많다"가 아니라 "이 여백은 잘못이다"라는 판정이 첫마디에 실립니다.

### 카드 4 — 아이콘 교체 요청

- 내가 쓴 영어: "and Also find any better icon thana current ruler icon to describe the mag-pixel in the top nav. replace it"   (출처: transcript:[user] skewnono_v3_nuxt, fe1dc34e)
- 정정: 세 군데입니다.
  1. `thana` → **`than a`** (오타). 그리고 이 자리는 `than **the** current ruler icon` 입니다. 헤더에 지금 박혀 있는 그 아이콘 하나를 가리키므로 정관사예요.
  2. `any better icon` → **`a better icon`**. `any` 는 "아무거나"라는 뜻이 실려서, 기준 없이 조금이라도 나으면 된다는 말로 들립니다. 실제 의도는 그 반대였고요.
  3. `and Also` → **`Also,`** 하나만. 둘 다 "추가"를 뜻해 겹칩니다. 문중에 온 `Also` 가 대문자인 것도 정리 대상입니다.
- 더 나은 표현: "Also, find a better icon than the current ruler for mag-pixel in the top nav, and swap it in."
  격식을 올리면: "Please replace the ruler icon for mag-pixel in the top nav with one that describes the page better."
- 왜: `replace it` 을 별도 문장으로 떼면 무엇을 무엇으로 바꾸는지가 흐려집니다. 영어의 replace 는 **`replace A with B`** 로 한 몸이라, 짝을 잃으면 대상이 붕 떠요. 앞 문장에 `and swap it in` 으로 이어 붙이거나 `replace A with B` 한 문장으로 묶는 편이 낫습니다. `swap in` 은 "이미 있는 것을 빼고 새것을 끼워 넣다"라 교체 요청에 정확히 맞는 구동사입니다.

  하나 더. `to describe the mag-pixel` 의 정관사도 빼는 게 자연스럽습니다. 기능 이름은 무관사로 씁니다 — `the icon for mag-pixel`, `the mag-pixel page`.

### 카드 5 — 시작 시각을 건 작업 지시

- 내가 쓴 영어: "Implement: apply 2a style to the mag-pixel page. Start the tasks at 10:40am."   (출처: transcript:[user] skewnono_v3_nuxt, `/goal` 인자)
- 정정: (문법 오류 없음.)
- 더 나은 표현: "Implement the 2a style on the mag-pixel page. Don't start before 10:40 KST."
- 왜: 두 군데가 한 단계 올라갑니다.

  먼저 `Implement:` 라벨과 뒤의 명령문 `apply` 가 겹칩니다. 라벨을 세웠으면 뒤는 목적어(명사구)로 받는 게 깔끔하고, 문장으로 쓸 거면 라벨을 빼고 동사 하나만 남기면 됩니다. `Implement the 2a style on …` 처럼요. 참고로 스타일·디자인은 페이지 **위에** 얹는 것이라 `on the page` 가 `to the page` 보다 자연스럽습니다.

  더 중요한 건 두 번째 문장입니다. `Start the tasks at 10:40am` 은 "10:40에 시작하라"라서, 문자 그대로는 **더 일찍 시작하는 것을 막지 못합니다.** 실제 의도는 "그 전엔 손대지 마라"였고요. 금지가 목적이면 `Don't start before …` 로 방향을 뒤집어야 합니다. 시간대도 붙이세요 — `10:40am` 만으로는 어느 시간대인지 알 수 없어서, 자리를 비운 사이 도는 작업일수록 `KST` 한 단어가 값을 합니다.

  덧붙이면 `the tasks` 의 정관사도 어색합니다. 아직 존재하지 않는 작업을 가리키니까요. 아예 목적어를 빼고 `Don't start before 10:40 KST` 로 두면 시작 대상이 앞 문장의 구현 작업으로 자연스럽게 이어집니다.
