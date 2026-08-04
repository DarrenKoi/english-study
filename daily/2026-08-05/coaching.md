# 2026-08-05 — 코칭

## 한글→영어

### 카드 1 — 굳이 Redis 여야 하나   (내가 쓴 한글)
- 내가 쓴 한글: "rules는 여기에서 만들어도 될 것 같은데, 굳이 redis를 이용해야 하는 이유가 있을까?"   (출처: transcript:[user] e0858fc1)
- 자연스러운 영어: It seems like we could just build the rules in the app — is there a real reason we have to go through Redis?
- 왜 이렇게: "~해도 될 것 같은데" 는 `It seems like we could just …` — could + just 가 제안의 부담을 낮춘다. "굳이 ~해야 하는 이유가 있을까?" 의 "굳이" 는 단어 하나로 옮기기보다 `a real reason we have to` 의 real 이 진다. 더 짧은 회화체로는 `Do we really need Redis here?` 도 같은 뜻이다. 경유한다는 뜻의 동사는 use 보다 `go through` 가 "굳이 거친다"는 뉘앙스까지 싣는다.

### 카드 2 — 그대로 반환해 달라   (내가 쓴 한글)
- 내가 쓴 한글: "편집 저장하는 일은 없을 것 같아. rules.py를 그대로 반환해줘"   (출처: transcript:[user] e0858fc1)
- 자연스러운 영어: I don't think we'll ever be saving edits — just return rules.py as-is.
- 왜 이렇게: "~하는 일은 없을 것 같아" 는 미래에 대한 부정 예측이므로 `I don't think we'll ever …` 가 정확하다(ever 가 "일은 없다"의 단정을 싣는다). "그대로" 는 기술 문맥의 표준어 `as-is`. 말로 하면 `just serve it straight from rules.py` 도 자연스럽다.

### 카드 3 — 안 쓰는 함수가 남는 경로   (고급 한글 · 번역)
- 한글 원문: "안 쓰는 판정 함수를 남겨두는 것이 두 정의가 다시 갈라지는 경로입니다."   (출처: transcript:[assistant] edde6893)
- 자연스러운 영어: Leaving an unused predicate around is exactly how the two definitions end up diverging again.
- 번역 포인트: "~하는 것" 명사절은 동명사 주어(`Leaving … around`)로 세운다. "경로입니다" 를 path 로 직역하면 어색하다 — 인과의 통로라는 뜻이므로 `is (exactly) how …` 가 관용이다. "갈라지다" 는 diverge / drift apart 중 고르는데, 서서히 어긋나는 뉘앙스면 drift apart, 결과적으로 딴 것이 된다는 단정이면 diverge.

### 카드 4 — Redis 가 사 주는 것   (고급 한글 · 번역)
- 한글 원문: "지금 상태에서는 Redis가 사 주는 게 없습니다."   (출처: transcript:[assistant] e0858fc1)
- 자연스러운 영어: As things stand, Redis buys us nothing.
- 번역 포인트: "사 주다" 은유가 영어 buy 와 정확히 겹친다 — What does this abstraction buy us? 는 설계 리뷰의 상투 질문이다. "지금 상태에서는" 은 `as things stand` (현 상황이 유지되는 한) 가 right now 보다 격에 맞는다.

### 카드 5 — 없는 것과 못 읽은 것   (고급 한글 · 번역)
- 한글 원문: "없는 것과 못 읽은 것은 다른 사실" (Redis 가 죽은 경우는 폴백하지 않고 에러를 낸다는 근거)   (출처: transcript:[assistant] e0858fc1)
- 자연스러운 영어: "Not there" and "couldn't read it" are two different facts.
- 번역 포인트: 한국어의 명사형("없는 것/못 읽은 것")을 영어에서는 짧은 인용구로 그대로 세우면 대비가 산다. absence 와 read failure 같은 추상명사로도 가능하지만 무거워진다. `two different facts` 의 two 가 "각각 따로 다뤄야 한다"는 함의를 만든다.

### 카드 6 — 걷어냈다 다시 깔기   (고급 한글 · 번역)
- 한글 원문: "편집기가 로드맵에 있는 이상 걷어냈다가 다시 까는 것보다 fallback이 쌉니다."   (출처: transcript:[assistant] e0858fc1)
- 자연스러운 영어: As long as the editor is still on the roadmap, a fallback is cheaper than ripping Redis out and putting it back later.
- 번역 포인트: "~하는 이상" 은 `as long as` 가 정확한 짝이다. "걷어내다/다시 깔다" 의 설비 은유는 `rip out / put back` 으로 유지된다(rip 이 "과감히 뜯어낸다"까지 싣는다). "쌉니다" 는 cost 은유 그대로 `cheaper` — 기술 판단을 비용 비교로 말하는 영어의 습관과 맞물린다.

## 영어 다듬기

### 카드 1 — bucket 별 Lot 요약
- 내가 쓴 영어: "Only Normal and Mother Normal is the same way to filter (Only CD extraction from oper_desc). Mother Normal goes deeper! it only handles mother_para true."   (출처: transcript:[user] edde6893)
- 정정: Only Normal and Mother Normal **is** → **are** — A and B 는 복수 주어다. (같은 메시지의 "copmarison" 은 comparison 오타.)
- 더 나은 표현: Only Normal and Mother Normal share the same step filter; Mother Normal goes one level deeper and keeps only parameters whose mother_para is true.
- 왜: "the same way to filter" 는 `share the same filter` 로 — 같음을 동사(share)에 실으면 주어-동사 수 일치 문제도 사라진다. "goes deeper" 는 그대로 살릴 만큼 좋은 표현이라, 실제로 어시스턴트도 설계 문서에서 `goes one level deeper` 로 받았다. "handles mother_para true" 는 `keeps only parameters whose mother_para is true` 로 풀어야 필터링이라는 뜻이 살아난다.

### 카드 2 — 고칠 게 많다
- 내가 쓴 영어: "we have lots of things to be fixed. … if suffix is one of them (_WCUD, _FCDU, _FULL), them they are not considered for the 판정 범위."   (출처: transcript:[user] e0858fc1)
- 정정: "them they" → "**then** they" (오타). "if suffix is" → "if **the** suffix is" — 특정 recipe 의 접미사이므로 정관사가 필요하다.
- 더 나은 표현: We have a lot to fix. … If a recipe name ends with _WCDU, _FCDU, or _FULL, it should be excluded from the judgment scope.
- 왜: "things to be fixed" 는 문법상 가능하지만 수동 부정사가 무겁다 — `a lot to fix` 가 관용이다. "not considered for X" 보다 `excluded from X` 가 분자·분모 양쪽에서 빠진다는 이번 요구사항의 뜻을 정확히 전달한다.

### 카드 3 — 이미 필터링하지 않았나
- 내가 쓴 영어: "Have we filter the lot_cd based on the recent measurement history from ebeam_tas_lot_hist? right, we should do the same thing for the device-statistics in terms of listing up the lot_cd (device codes)."   (출처: transcript:[user] e0858fc1)
- 정정: "Have we **filter**" → "Have we **filtered**" — 현재완료는 have + 과거분사. "listing **up**" → "listing" — list up 은 콩글리시로, list 자체가 "목록에 올리다"다.
- 더 나은 표현: Didn't we already filter lot_cds by recent measurement history from ebeam_tas_lot_hist? Right — we should do the same for the device-statistics device list.
- 왜: "우리 이미 ~하지 않았나?" 라는 확인 질문은 `Didn't we already …?` 가 가장 자연스럽다. "in terms of listing up the lot_cd" 처럼 in terms of 로 끌고 가는 대신 `for the device list` 한 구로 줄인다 — in terms of 는 남발하면 문장이 늘어진다.

### 카드 4 — 어느 것을 지켜봐야 할지
- 내가 쓴 영어: "Since we have so many lot_cd list, hard to track down on which one to watch."   (출처: transcript:[user] e0858fc1)
- 정정: 주어 누락 — "**it's** hard". "so many lot_cd list" → "so many lot_cd**s**" (many 뒤는 복수형). "track down **on** which" → "track down which" (track down 은 전치사 없이 목적어를 받는다).
- 더 나은 표현: With so many lot_cds, it's hard to know which ones to keep an eye on.
- 왜: `With so many X` 도입이 Since 절보다 가볍고 회화적이다. track down 은 "추적 끝에 찾아내다"라서 계속 지켜본다는 이 문맥에는 `keep an eye on` 이 맞는 동사다.

### 카드 5 — 404 보고
- 내가 쓴 영어: "also error when I try to get the device-staistics/rules?fac_id=R3 404 NOT FOUND in the web console."   (출처: transcript:[user] e0858fc1)
- 정정: 동사 누락 — "also **I get an** error when …". "staistics" → statistics 오타.
- 더 나은 표현: Also, the web console shows a 404 NOT FOUND when I hit device-statistics/rules?fac_id=R3.
- 왜: 오류 보고는 "콘솔이 무엇을 보여준다" 를 주어-동사로 세우면 문장이 저절로 갖춰진다. API 를 호출해 본다는 구어 동사는 `hit` — try to get 보다 짧고 개발자 사이 표준이다.

### 카드 6 — 조사 방법 질문
- 내가 쓴 영어: "what should I do to check about read_idp_info issue in the cloud"   (출처: transcript:[user] bdade38d — /back-to-office 인자)
- 정정: "check **about**" → "check **on**" 또는 "look into" — check 는 about 을 받지 않는다. "read_idp_info issue" → "**the** read_idp_info issue" (특정 이슈이므로 정관사).
- 더 나은 표현: How should I go about investigating the read_idp_info issue in the cloud?
- 왜: 절차를 묻는 질문은 `What should I do to …?` 보다 `How should I go about …-ing?` 이 관용형이다. 참고로 "in the cloud" 자체는 자연스러운 표현이고, 특정 호스트를 가리킬 때만 `on the cloud host` 로 좁힌다 — 어시스턴트 답변이 정확히 그렇게 구분했다.

### 카드 7 — 툴팁·팝업 요청
- 내가 쓴 영어: "In the device-statistics page, enhance the visibility of tooltips in the bar charts. (not able to see the description). Also increase the popup window size in both ways (width and height)"   (출처: transcript:[user] 3043a732)
- 정정: "**In** the device-statistics page" → "**On** the … page" — 페이지·화면 위의 요소는 on 이다.
- 더 나은 표현: On the device-statistics page, make the bar-chart tooltips easier to read — the description is barely legible. Also make the popup bigger in both dimensions (width and height).
- 왜: "enhance the visibility of" 는 틀리지 않지만 명사화가 무겁다 — 요청은 `make … easier to read` 처럼 동사로 하는 편이 자연스럽다. "in both ways" 는 "두 가지 방법으로"로 읽히므로 크기의 두 축은 `in both dimensions` 또는 그냥 `wider and taller` 로 말한다.
