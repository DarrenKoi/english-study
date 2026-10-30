# 2026-10-31 — 코칭

오늘 배치에는 내가 쓴 한국어가 없어 한글→영어 카드는 없다. 어시스턴트 발화도 영어뿐이라 번역 정독 카드도 뺐다.

## 영어 다듬기

### 카드 1 — 엔드포인트 요청
- 내가 쓴 영어: "for afm page, I want to service with endpoint. create api endpoint for the afm features to the users so that they can use them in the script in their local PC."   (출처: transcript:[user] skewnono-v3-nuxt d5f5ede9, `/poteto-mode` 인자)
- 정정: "For the AFM page, I want to **expose** its features **through** API endpoints. **Create** API **endpoints** for the AFM features so that users can call them from scripts **on** their local PCs."
  - `service` 는 이 뜻의 동사가 아니다. 동사 service 는 '정비하다'(service a car)라서 "엔드포인트로 제공하다"는 `expose` 나 `serve` 를 쓴다.
  - 셀 수 있는 명사는 관사나 복수가 필요하다. `with endpoint` → `through endpoints`, `create api endpoint` → `create API endpoints`, `afm page` → `the AFM page`.
  - PC '위에서' 돌리는 것이라 `in their local PC` 가 아니라 `on their local PCs`.
  - `to the users` 는 앞 동사(create)와 맞지 않는다. 받는 사람은 `for users` 로 쓰거나 아예 so that 절에 넘긴다.
- 더 나은 표현: "Let's make the AFM features available as an API, so users can call them from scripts on their own PCs." 또는 지시문으로: "Expose the AFM page's features as API endpoints that users can call from local scripts."
- 왜: 요청의 핵심은 "로컬 스크립트에서 AFM 기능을 쓸 수 있게"다. `make X available as an API` 는 엔드포인트를 새로 만들지, 있는 걸 문서화할지를 열어 둔다. 실제로 이번엔 엔드포인트가 이미 있어서 문서화로 끝났다. 목표(무엇을 가능하게)를 말하고 수단(endpoint 를 만들어라)은 빼는 편이 오해가 적다. 첫 글자 대문자, 고유명사 대문자(AFM, API)도 챙기면 문장이 한결 단정해진다.

### 카드 2 — 요청 제한도 걸어라
- 내가 쓴 영어: "API rate-limited is also applied to the AFM too."   (출처: transcript:[user] skewnono-v3-nuxt d5f5ede9)
- 정정: "**API rate limiting** should apply to AFM too." (또는 "Apply the API rate limit to AFM too.")
  - `rate-limited` 는 형용사(제한이 걸린)라 주어 자리에 못 온다. 명사로 `rate limiting` 이나 `the rate limit` 을 쓴다.
  - `also … too` 는 같은 뜻을 두 번 말한 중복이다. 하나만 남긴다.
  - `is … applied` 는 "이미 적용돼 있다"는 사실 진술로 읽힌다. 원한 게 지시라면 `should apply` 나 명령문을 쓴다.
- 더 나은 표현: "Please put AFM under the same rate limit as the rest of the API." / 사실을 알리려는 뜻이었다면: "The rate limit already applies to AFM as well."
- 왜: 이 문장은 지시로도 사실 진술로도 읽혀서 어시스턴트가 작업을 시작했다가 멈췄다. 영어에서 지시는 명령문이나 `should` 로, 사실은 현재형 + `already` 로 갈라 쓰면 오해가 없다. `the same … as the rest of the API` 는 "예외 없이 나머지와 똑같이"라는 의도를 정확히 전한다.

### 카드 3 — 파일 지우기
- 내가 쓴 영어: "delete the patch file"   (출처: transcript:[user] skewnono-v3-nuxt d5f5ede9)
- 더 나은 표현: "Go ahead and delete the patch file; I won't need it."
- 왜: 문법 오류는 없고 짧은 지시로 충분히 통한다. `Go ahead and …` 는 상대가 방금 제안한 일을 승인하는 구어 표현이다. 어시스턴트가 "필요 없으면 지워도 된다"고 제안했으니 딱 맞는다. 뒤에 `I won't need it` 처럼 이유를 반 문장 붙이면 같은 일이 다시 생겨도 상대가 기준을 안다.
