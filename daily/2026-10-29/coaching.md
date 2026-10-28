# 2026-10-29 — 코칭

## 한글→영어

### 카드 1 — 최근 변경분 기준으로 정리하고 리뷰 맡기기   (내가 쓴 한글)
- 내가 쓴 한글: "skewvoir, afm page에 대해서 최근 변경점을 기준으로 simplify 진행 하고 codex (via herdr)와 함께 code review 진행해줘"   (출처: transcript:[user] skewnono-v3-nuxt d2f430dc)
- 자연스러운 영어: Run a simplify pass on the recent changes to the skewvoir and AFM pages, then do a code review together with Codex via herdr.
- 왜 이렇게:
  - '~에 대해서 … 기준으로'는 영어에서 전치사 하나로 줄어든다. on the recent changes to (the pages) 면 대상과 범위가 한 번에 들어간다. about 을 쓰면 '그 페이지에 관해 이야기하다'처럼 들려서 어색하다.
  - '진행하다'를 proceed 로 옮기지 않는다. 영어는 구체 동사를 쓴다. 정리는 run a pass, 리뷰는 do a review.
  - '진행하고 … 진행해줘'처럼 같은 동사를 두 번 쓰면 영어에서는 then 으로 순서만 보여 주면 된다.
  - 더 짧게 말할 때(구어): Simplify the recent skewvoir and AFM changes, then review them with Codex in herdr.

### 카드 2 — 줄 수보다 규칙의 단일화   (고급 한글 · 번역)
- 한글 원문: "이번 simplify는 줄 수가 거의 줄지 않았습니다(+97 −96). 얻은 것은 같은 규칙을 한 곳에서만 계산하게 된 점입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt d2f430dc)
- 자연스러운 영어: This simplify pass barely changed the line count (+97 −96). What it bought us is that each rule is now computed in exactly one place.
- 번역 포인트: '줄 수가 줄지 않았다'는 barely changed the line count 로 옮겨 '줄'이 두 번 겹치는 걸 피한다. '얻은 것은 ~점입니다'는 What it bought us is that … 처럼 what 절 주어로 받으면 한국어의 '것은 … 점' 구조가 그대로 살아난다. buy 는 '대가를 치르고 얻다'라서 '줄 수는 못 줄였지만'이라는 맥락과 맞는다.

### 카드 3 — fix 커밋이 쌓인 원인   (고급 한글 · 번역)
- 한글 원문: "오늘 fix 커밋이 20개 쌓인 것도 대부분 같은 규칙을 화면·영수증·상관에서 따로 고쳤기 때문입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt d2f430dc)
- 자연스러운 영어: Most of today's twenty fix commits piled up for the same reason: the same rule was fixed separately in the screen, the receipt, and the correlation view.
- 번역 포인트: '~한 것도 … 때문입니다'를 because 로 길게 잇는 대신 for the same reason: 으로 끊고 콜론 뒤에 이유를 둔다. '쌓이다'는 piled up 이 커밋이 하나씩 늘어나는 모습을 잘 살린다. '따로'는 separately 로, 고친 장소 셋은 in A, B, and C 로 나열한다.

### 카드 4 — 지금은 두고 신호가 오면 손보기   (고급 한글 · 번역)
- 한글 원문: "실제 지연이나 메모리 압박이 보이면 그때 손보면 됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt d2f430dc)
- 자연스러운 영어: If we see real latency or memory pressure, we can deal with it then.
- 번역 포인트: '~면 됩니다'는 허락·충분함의 뉘앙스라 we can … then 이 맞는다. we should 는 의무처럼 들린다. '손보다'는 fix 보다 deal with 가 가볍고 자연스럽다. 격식 문서라면 This can be revisited if real latency or memory pressure is observed.
