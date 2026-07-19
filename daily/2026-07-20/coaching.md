# 2026-07-20 — 코칭

## 한글→영어

### 카드 1 — finalize 는 파이프라인 몫   (고급 한글 · 번역)
- 한글 원문: "커밋·아카이브는 파이프라인 finalize 단계 몫이라 건드리지 않았습니다."   (출처: transcript:[assistant] english-study 55faedeb)
- 자연스러운 영어: I left commit and archive untouched — those belong to the pipeline's finalize step.
- 번역 포인트: "~몫이다"는 소유의 belong to 로 옮기면 책임 경계가 선명해집니다. "건드리지 않았다"는 didn't touch 보다 left X untouched 가 "의도적으로 놔뒀다"는 뉘앙스를 살립니다. 대시로 이유를 뒤에 붙이는 배치도 한국어 어순("~라서 ~했다")을 뒤집는 영어다운 선택입니다.

### 카드 2 — 중복 대조 후 제외   (고급 한글 · 번역)
- 한글 원문: "중복 후보는 기존 notes 대조 후 제외했습니다."   (출처: transcript:[assistant] english-study 55faedeb)
- 자연스러운 영어: I checked the duplicate candidates against the existing notes and dropped them.
- 번역 포인트: "대조하다"는 check A against B 가 정확한 짝입니다(compare with 보다 검증 뉘앙스). "제외했다"는 exclude 도 되지만 목록 정리 문맥에선 drop 이 가볍고 자연스럽습니다. 한국어의 명사 나열("대조 후 제외")을 영어에선 동사 두 개의 and 연결로 풉니다.

## 영어 다듬기

### 카드 1 — how vs what do you call
- 내가 쓴 영어: "how do you call the code base that is poised to make smooth transition between home and office."   (출처: transcript:[user] skewnono 81e82c59)
- 정정: how → **what** do you call ... — call 은 "X를 Y라고 부르다"의 명칭을 묻는 동사라 의문사는 what. 또 "make **a** smooth transition"(가산 단수엔 관사).
- 더 나은 표현: What do you call a codebase that's set up to switch smoothly between home and office?
- 왜: "How do you call"은 한국어 "어떻게 불러요?"의 직역으로 가장 흔한 오류 중 하나입니다. poised to 는 좋은 어휘지만 "임박했다"는 뉘앙스라, 설계된 상태를 말할 땐 set up to / built to 가 맞습니다.

### 카드 2 — do I only have to
- 내가 쓴 영어: "once I start to wright the code in my office, do i have to only fill in the data.py files? to resemble mock.py?"   (출처: transcript:[user] skewnono 66803736)
- 정정: wright → **write**. "have to only fill in" → "**only have to** fill in" — only 는 조동사 앞에 둬야 "그것만 하면 된다"는 뜻이 됩니다.
- 더 나은 표현: Once I start writing code at the office, is filling in data.py all I need to do — mirroring mock.py?
- 왜: "all I need to do" 의사분열문이 "그게 전부인가?"라는 질문 의도를 정확히 전달합니다. 장소는 in my office 보다 at the office 가 관용적입니다.

### 카드 3 — if there are any
- 내가 쓴 영어: "check those importing issues from dead pycaches if there are, clean up"   (출처: transcript:[user] skewnono 81e82c59)
- 정정: "if there are" → "if there are **any**" — there are 는 보어 없이 문장을 닫을 수 없어 any 로 받아야 합니다. importing issues → **import** issues(명사 수식은 원형).
- 더 나은 표현: Check for import issues from the dead pycache files, and clean up any you find.
- 왜: check for 는 "있는지 탐색"이고 check 는 "이미 아는 대상 점검"입니다. 아직 있는지 모르는 문제라 check for 가 맞고, "any you find"가 조건절을 통째로 대체해 명령문이 매끈해집니다.

### 카드 4 — object to / after consensus is reached
- 내가 쓴 영어: "give your opinions and if you object them, then discuss with /codex:rescue and update to the three files after consensus made."   (출처: transcript:[user] skewnono b7df6a67)
- 정정: object **to** them(자동사+전치사), update ~~to~~ the three files(update 는 타동사), after consensus **is reached**(절에는 동사 필요).
- 더 나은 표현: Give me your opinions; if you object to any of them, hash it out with /codex:rescue and update the three files once you've reached consensus.
- 왜: hash it out 은 "이견을 끝까지 논의해 결론 내다"의 관용구로 discuss 보다 합의 지향이 분명합니다. once you've reached consensus 는 완료를 전제한 시점 표현이라 after 절보다 절차가 또렷합니다.

### 카드 5 — an English version
- 내가 쓴 영어: "As we need to implement plan, make a english version for the plan so that I can implmenet with the english version later on."   (출처: transcript:[user] skewnono b7df6a67)
- 정정: a english → **an English**(모음 발음 앞 an, 언어명 대문자). implement **the** plan(특정 플랜엔 관사). implmenet → implement.
- 더 나은 표현: Since we'll be implementing this plan, make an English version of it so I can work from that later.
- 왜: "version **of** it"이 소속 관계의 표준 전치사입니다(for 는 용도). "work from the English version"의 from 은 "그걸 기준 삼아 작업한다"는 관용 용법으로, implement with 보다 자연스럽습니다.

### 카드 6 — two decimal places
- 내가 쓴 영어: "x axis is good to have integer style. but for y axis, limit to be the 2 digit to the decimal."   (출처: transcript:[user] skewnono 92aa3491)
- 정정: "limit to be the 2 digit to the decimal" → "limit it to **two decimal places**" — 소수 둘째 자리는 two decimal places 가 고정 표현입니다.
- 더 나은 표현: Integers are fine for the x-axis; for the y-axis, cap the values at two decimal places.
- 왜: "X is good to have Y" 구문은 영어에 없습니다 — "Y is fine for X" 로 뒤집어야 합니다. cap at 은 "상한을 ~로 잡다"로 limit to 의 한 단계 위 실무 표현입니다.

### 카드 7 — so (that) 결과절
- 내가 쓴 영어: "돌아가기 means to go back to the previous page so that we fail to go back to the recipe-search page.."   (출처: transcript:[user] skewnono 7112bc25)
- 정정: so that 은 목적("~하도록")의 접속사라 나쁜 결과엔 못 씁니다. 결과는 "**so** we can't ..." 또는 "which means we can't ..." 로.
- 더 나은 표현: "돌아가기" takes us to the previous page in history, so we can't reliably get back to the recipe-search page.
- 왜: fail to 는 "시도했으나 실패"의 뉘앙스라, 구조적으로 불가능한 상황엔 can't reliably 가 정확합니다. takes us to 는 버튼·링크의 동작 주어화로 UI 설명의 표준 어법입니다.

### 카드 8 — 간접의문문 어순
- 내가 쓴 영어: "it is possible how many tokens are consumed in context for the current session?"   (출처: transcript:[user] skewnono e77685e7)
- 정정: 의문문이므로 "**Is it** possible ..." 도치가 필요하고, possible 뒤에는 to 부정사가 와야 합니다: "Is it possible **to see** how many tokens ...".
- 더 나은 표현: Is there a way to see how many context tokens the current session is using?
- 왜: "Is there a way to ..." 가 기능 존재 여부를 묻는 가장 관용적인 틀입니다. are consumed 수동보다 the session is using 능동이 가볍고, context tokens 처럼 명사를 앞에 붙이면 전치사구(in context for ...)가 사라져 문장이 짧아집니다.
