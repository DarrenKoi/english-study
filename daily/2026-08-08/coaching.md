# 2026-08-08 — 코칭

## 한글→영어

### 카드 1 — 버튼이 무슨 일을 하는지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "in activity, 관리자 기능, 관리자 초기화누르면 어떤 결과?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: On the activity page, under 관리자 기능 — what actually happens when I hit the 초기화 button?
- 왜 이렇게: 페이지는 `on the … page`, 그 안의 구역은 `under`. "어떤 결과?"를 `what is the result?` 로 옮기면 시험 문제처럼 들리고, 실제 동작을 묻는 말은 `what actually happens when…` 입니다. `actually` 한 단어가 "문서 말고 진짜로"라는 뉘앙스를 얹어, 상대가 코드를 열어보게 만듭니다.

### 카드 2 — 라벨을 바꿔달라고 하기   (내가 쓴 한글)
- 내가 쓴 한글: "그럼 단순히 새로고침으로 바꿔주세요. 초기화 sounds horrible"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: Then let's just relabel it 새로고침 — 초기화 sounds alarming for a button that only clears filters.
- 왜 이렇게: "단순히 ~로 바꿔주세요"는 명령형보다 `let's just …` 가 부드럽고, 라벨 변경에는 `change` 보다 `relabel` 이 정확합니다. `horrible` 은 감정이 세서 취향 문제로 들리는데, `alarming` 은 "사용자가 겁먹는다"는 이유를 품고 있어 판단으로 읽힙니다. 뒤에 `for a button that only …` 를 붙이면 요청이 아니라 근거 제시가 됩니다.

### 카드 3 — 아이콘까지 맞추고 올려달라고 하기   (내가 쓴 한글)
- 내가 쓴 한글: "refresh까지 하고 commit and push"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: Swap the icon to refresh as well, then commit and push.
- 왜 이렇게: "~까지"는 `even` 이 아니라 `as well` / `too` 입니다. 여기서는 앞 작업 위에 하나 더 얹는 뜻이라 `as well` 이 맞고, `even` 을 쓰면 "그것마저"라는 놀라움이 섞입니다. 지시가 이어질 때는 `and` 보다 `then` 이 순서를 분명히 합니다.

### 카드 4 — 원인과 조치를 함께 보고하기   (내가 쓴 한글)
- 내가 쓴 한글: "소문자였구나. 대문자여서 검색이 안되는거였어. 소문자로 다시 redis DB 생성해서 문제 해결했어"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: Lowercase — that was it. The search was coming back empty because we'd loaded the fields in uppercase. I rebuilt the Redis hashes in lowercase and it works now.
- 왜 이렇게: "~였구나"의 깨달음은 감탄사보다 `— that was it` 이 담백합니다. "검색이 안되는거였어"를 `didn't work` 로 옮기면 에러가 난 것처럼 들리는데, 실제 증상은 빈 결과였으므로 `was coming back empty` 로 특정해야 상대가 같은 함정을 알아봅니다. 과거완료 `we'd loaded` 가 "적재가 먼저, 증상이 나중"이라는 순서를 표시합니다.

### 카드 5 — 추가 질문에 답하기   (내가 쓴 한글)
- 내가 쓴 한글: "rcp_loc과 tools_in_rcp 도 전부 소문자화 되어 있어"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: `rcp_loc` and `tools_in_rcp` are lowercase too — all of them.
- 왜 이렇게: "~화 되어 있어"를 `have been lowercased` 로 옮기면 누가 언제 했는지가 앞으로 나오는데, 확인 답변에서 상대가 알고 싶은 건 지금 상태뿐이라 `are lowercase` 가 맞습니다. "전부"를 문장 안에 넣지 않고 `— all of them` 으로 떼어 붙이면 구어의 리듬이 삽니다.

### 카드 6 — 조용한 실패가 정상 응답으로 위장된다   (고급 한글 · 번역)
- 한글 원문: "그 구분(field 없음 = 빈 결과 / key 없음 = 502)이 의도된 것이라, 대문자 적재는 인프라 장애가 아니라 합법적 empty로 위장됩니다."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: Because that distinction is deliberate — a missing field means an empty result, a missing key means a 502 — an uppercase load never surfaces as an outage. It disguises itself as a legitimate empty answer.
- 번역 포인트: "의도된 것이라"의 이유절을 `Because …` 로 앞세우고 괄호는 대시로 풀어야 영어 리듬이 삽니다. "위장됩니다"는 한국어에선 피동이지만 영어는 `disguises itself` 로 능동이 자연스럽습니다 — 주어가 사물이어도 영어는 능동을 선호합니다. "인프라 장애가 아니라"의 부정+대조까지 한 문장에 넣으면 무거워져 둘로 끊었습니다.

### 카드 7 — mock 이 보증하는 것과 못 하는 것   (고급 한글 · 번역)
- 한글 원문: "mock은 모양은 보장하지만 사무실 데이터의 표기 규칙 위반은 재현할 수 없습니다"   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: The mock guarantees the shape of the data but not its conventions, so it can never reproduce a casing violation from the office.
- 번역 포인트: "모양은 ~하지만"의 대조 조사 '은'을 `guarantees X but not Y` 로 옮기면 동사를 반복하지 않고도 대비가 섭니다. "표기 규칙 위반"을 `notation rule violation` 으로 직역하면 뜻이 흐려지므로, 실제 위반 내용을 담아 `a casing violation` 으로 좁힙니다. "재현할 수 없습니다"에 `can never` 를 써야 일시적 한계가 아니라 구조적 불가능이 됩니다.

### 카드 8 — 관대한 수정이 왜 나쁜 수정인가   (고급 한글 · 번역)
- 한글 원문: "어댑터를 '대문자도 받아주게' 관대하게 만드는 건 오히려 나쁜 수정입니다: 적재 job의 계약 위반을 숨겨서 다음 소비자가 같은 함정에 빠집니다."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: Making the adapter lenient enough to accept uppercase would be the wrong fix: it hides the loader's contract violation, and the next consumer walks straight into the same trap.
- 번역 포인트: '오히려'를 부사로 옮기려 하지 말고 가정법 `would be the wrong fix` 에 흡수시킵니다 — 하지 않은 일을 현재형으로 단정하면 어색합니다. 콜론 뒤가 근거라는 신호는 한국어와 영어가 같으니 그대로 살릴 수 있습니다. "함정에 빠집니다"는 `falls into` 보다 `walks into` 가 관용적입니다 — 밀려서가 아니라 제 발로 걸어 들어간다는 어감이 붙습니다.

## 영어 다듬기

### 카드 9 — 이슈 목록 열기
- 내가 쓴 영어: "There are bunch of things to be fixed in the device-statistics page."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `a bunch of` — `bunch` 는 가산 단수 명사라 관사가 필요합니다. 그리고 페이지는 `on the … page` 입니다(`in` 은 페이지 *안의* 요소를 가리킬 때).
- 더 나은 표현: A few things need fixing on the device-statistics page.
- 왜: `there are … to be fixed` 는 수동 부정사라 문장이 무거워집니다. `need fixing` 은 형태는 능동인데 뜻은 수동인 관용 구문이라 짧고 자연스럽습니다. 번호를 매겨 항목을 나열하는 글머리에는 `a bunch of`(뭉텅이) 보다 `a few` 가 어울립니다.

### 카드 10 — 증상 보고하기
- 내가 쓴 영어: "we are not able to see the data in Mother Normal tab for the M-fabs."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `in the Mother Normal tab` — 화면 요소 이름 앞에는 정관사가 붙습니다.
- 더 나은 표현: The Mother Normal tab shows no data for the M-fabs.
- 왜: `we are not able to see` 는 사람을 주어로 삼아 "내 환경 문제일 수도 있다"는 여지를 남깁니다. 화면을 주어로 올리면 재현 가능한 사실 보고가 되어 상대가 곧장 조사에 들어갑니다. 사람 주어를 유지하더라도 `are not able to` 보다 `can't` 가 자연스럽습니다.

### 카드 11 — 무엇이 더 중요한지 설명하기
- 내가 쓴 영어: "They are more focued on recipe name (recipe_id or full_name) but here, oper_desc is the foremost important and order should be based on the oper_seq."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `focued` → `focused` 오타. `the foremost important` → `foremost` 는 그 자체가 최상급이라 `most` 와 겹칠 수 없습니다(`the most important` 또는 `foremost` 중 하나). `based on the oper_seq` → 컬럼명 앞에는 정관사를 붙이지 않습니다. 쉼표는 `here` 뒤가 아니라 `but` 앞에 옵니다.
- 더 나은 표현: The cards lead with the recipe name (`recipe_id` or `full_name`), but here `oper_desc` matters most and the default order should follow `oper_seq`.
- 왜: `be focused on` 은 사람이 무언가에 집중한다는 뜻이라 UI 를 주어로 두면 어긋납니다. 요점은 카드가 무엇을 맨 앞에 내세우느냐이므로 `lead with` 가 정확합니다. `is the most important` 를 `matters most` 로 바꾸면 형용사 대신 동사가 무게를 져서 문장이 한 뼘 짧아집니다.

### 카드 12 — 대안 제안하기
- 내가 쓴 영어: "It will be better to sort based on recipe name instead."   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: It would also help to offer recipe name as an alternative sort.
- 왜: 아직 결정 전인 제안에는 `will` 보다 가정법 `would` 가 맞고, 그쪽이 더 정중합니다. `instead` 는 앞의 요구를 취소하라는 말로 읽히는데 의도는 "옵션 추가"였으므로, 그대로 두면 상대가 기본 정렬을 통째로 바꿀 위험이 있습니다. `as an alternative` 가 그 오해를 막습니다.

### 카드 13 — 감사 인사
- 내가 쓴 영어: "very thanks"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `very` 는 형용사·부사만 꾸미므로 명사 `thanks` 를 받을 수 없습니다. `thanks a lot`, `many thanks`, `thank you very much` 중 하나를 씁니다.
- 더 나은 표현: Thanks — that's exactly what I needed.
- 왜: 감사만 있는 한 줄은 상대가 다음 행동을 정하지 못합니다. 무엇이 도움이 됐는지 반 마디만 붙이면 대화가 닫히면서도 다음 요청의 기준이 함께 남습니다.

### 카드 14 — 사실 확인 질문하기
- 내가 쓴 영어: "for recipe-search, what is the hash name in redis for the search?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `Redis` 는 제품명이라 대문자로 씁니다. 문장 첫 글자 `For` 도 마찬가지입니다.
- 더 나은 표현: For recipe-search, which Redis hash does the search actually read from?
- 왜: `what is the name` 은 이름표 하나만 요구하는데, 정작 알고 싶은 건 "검색이 실제로 훑는 대상"이었습니다. `which hash does it read from` 으로 물으면 답에 용도와 경계까지 딸려 옵니다. 원문에 두 번 나오던 `for` 도 `read from` 으로 옮기면서 정리됩니다.
