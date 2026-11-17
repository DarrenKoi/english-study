# 2026-11-18 — 코칭

오늘 내가 쓴 한국어는 기능 구현을 맡기는 긴 지시 하나와 짧은 후속 지시 넷입니다. "어디까지 해 달라", "일단 ~로 가정하고", "~에게도 맡겨 줘" 같은 위임 표현이 중심입니다.

## 한글→영어

### 카드 1 — 정보 출처 밝히기   (내가 쓴 한글)
- 내가 쓴 한글: "@docs/office-migration/veritysem_provision_recipe_list.txt 그리고 recipe_usage.txt 파일 정보는 office agent가 알려준거야."   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: The information in @docs/office-migration/veritysem_provision_recipe_list.txt and recipe_usage.txt came from the office agent.
- 왜 이렇게: "~가 알려준 거야"를 `The office agent told me …` 로 옮겨도 되지만, 주어가 긴 파일 이름일 때는 `X came from Y` 가 깔끔합니다. 출처를 말하는 가장 흔한 틀입니다. 한 번 더 격식을 올리면 `was provided by the office agent`.

### 카드 2 — 할 수 있는 데까지   (내가 쓴 한글)
- 내가 쓴 한글: "이 데이터 내용을 토대로 Verity, Provision에 recipe 기능 (CD-SEM, HV-SEM처럼)구현할 수 있는데 까지 진행해줘."   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: Based on this data, build out the recipe features for Verity and Provision, like the ones CD-SEM and HV-SEM have, as far as the data allows.
- 왜 이렇게: "~할 수 있는 데까지"는 `as far as you can` 이 기본입니다. 여기서는 한계가 데이터에 있으니 `as far as the data allows` 가 더 정확합니다. "토대로"는 `based on`, "CD-SEM처럼"은 `like the ones CD-SEM has` 로 풀어야 "같은 종류의 기능"이라는 뜻이 삽니다. `build out` 은 뼈대에 살을 붙여 넓혀 간다는 어감입니다.

### 카드 3 — "~정도 되지 않을까"   (내가 쓴 한글)
- 내가 쓴 한글: "아마도 recipe 검색 기능 (includig skewvoir)과 recipe 현황 일부 테이블 정도 되지 않을까."   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: My guess is that it'll come down to recipe search (including in Skewvoir) and a few of the recipe status tables.
- 왜 이렇게: "~정도 되지 않을까"는 확신 없는 예상입니다. `I'd guess …`, `My guess is …`, `Probably something like …` 가 그 말투에 맞습니다. `come down to` 는 "결국 ~정도로 좁혀지다". "일부 테이블"은 `some of the tables` 나 `a few of the tables`. `maybe` 를 문장 앞에 두고 평서문으로 끝내면 한국어보다 훨씬 단정적으로 들립니다.

### 카드 4 — 활성화해야 해   (내가 쓴 한글)
- 내가 쓴 한글: "해당 top nav는 활성화 해야해."   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: The matching top-nav tabs need to be enabled.
- 왜 이렇게: "해당"은 `the corresponding` 이나 `the matching` 입니다. 구어에서는 `those` 하나로 충분할 때도 많습니다. 꺼져 있던 메뉴를 켜는 일은 `activate` 보다 `enable` 이 UI 용어로 자연스럽습니다. 주어를 사물로 두고 `need to be + 과거분사` 를 쓰면 누가 하는지 말하지 않고도 요구 사항이 됩니다.

### 카드 5 — 일단 가정하고 진행   (내가 쓴 한글)
- 내가 쓴 한글: "Provision도 VeritySE로의 Key 3/4 유사한 형태로 만들었어. (일단 동일한 스키마로 가정하고 진행)"   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: I've set up Key 3/4 for Provision in a similar form to VeritySEM's. (For now, go ahead and assume the same schema.)
- 왜 이렇게: 방금 만들어서 지금 쓸 수 있다는 뜻이라 현재완료 `I've set up` 이 맞습니다. "일단"은 `for now` 입니다. 나중에 바뀔 수 있다는 단서가 그 안에 들어 있습니다. "~로 가정하고 진행"은 `go ahead and assume …` 또는 `proceed on the assumption that the schema is the same`(격식). 원문의 "VeritySE로의"는 "VeritySEM의"를 잘못 친 것으로 보고 옮겼습니다.

### 카드 6 — 점검도 맡겨 줘   (내가 쓴 한글)
- 내가 쓴 한글: "작업 다 마친 뒤에 codex (via herdr)에게도 점검 맞겨줘. 그리고 문제 없으면 commit and push"   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: Once everything's done, have Codex review it too (via Herdr). Then, if nothing comes up, commit and push.
- 왜 이렇게: "~에게 맡겨 줘"는 사역 `have + 사람 + 동사원형` 이 딱 맞습니다(`have Codex review it`). `ask Codex to review it` 도 됩니다. "다 마친 뒤에"는 `after` 보다 `once` 가 "끝나는 대로 곧"의 느낌을 줍니다. "문제 없으면"은 어제 배운 `if everything looks good` 말고도, 리뷰 결과를 두고 말할 때는 `if nothing comes up` 이 잘 어울립니다. 한글 맞춤법은 "맞겨줘"가 아니라 "맡겨 줘"입니다.

### 카드 7 — 오래된 건 검증된 것들   (내가 쓴 한글)
- 내가 쓴 한글: "오래된 것들은 검증이 된 것들. 정리해줘"   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: The old ones have already been verified. Go ahead and clear them out.
- 왜 이렇게: "검증이 된 것들"은 이미 끝난 상태라 현재완료 수동 `have been verified` 를 씁니다. `already` 를 넣으면 "그러니 더 볼 필요 없다"는 뜻이 됩니다. "정리해 줘"는 여기서 목록에서 지우라는 뜻이라 `organize` 가 아니라 `clear out` 이나 `clean up` 입니다. 한국어 "정리"는 `organize / tidy up / clear out / wrap up` 중 문맥에 맞는 걸 골라야 합니다.

### 카드 8 — 칸별로, 정렬할 수 있게   (내가 쓴 한글)
- 내가 쓴 한글: "product/layer/ 칸별로 비워주세요. 나눠서 소팅할 수 있게."   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: Please fill in the product and layer columns separately, so I can sort by each one.
- 왜 이렇게: 어시스턴트가 읽은 대로 "비워주세요"를 "채워주세요"로 보고 옮겼습니다. 칸을 채우는 건 `fill in`, 비우는 건 `leave blank` / `clear` 라서 영어에서도 한 낱말 차이로 뜻이 뒤집힙니다. "나눠서 소팅할 수 있게"는 목적절 `so (that) I can sort by each one` 입니다. `sort by + 기준` 형태를 기억해 두세요. "칸별로"는 `per column` 이나 `separately`.

### 카드 9 — 보여 줄 데이터가 없다   (고급 한글 · 번역)
- 한글 원문: "스큐보아는 측정값(CD, 이미지)을 분석하는 화면인데, 이번 키는 MES 작업 집계라 보여 줄 데이터가 없습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: Skewvoir is built for analyzing measurements (CD values and images), but these keys only hold MES job aggregates, so there is nothing for it to show.
- 번역 포인트: "~인데, ~라, ~없습니다"가 한 문장에 이어진 구조입니다. 영어에서는 `but` 으로 대비를, `so` 로 결론을 나눠 받습니다. "보여 줄 데이터가 없다"는 `there is no data to show` 도 되지만 `nothing for it to show` 처럼 `for + 의미상 주어 + to 부정사` 를 쓰면 "스큐보아 입장에서 보여 줄 게 없다"가 살아납니다. "분석하는 화면"은 `a screen that analyzes` 보다 `is built for analyzing` 이 용도를 말하기에 자연스럽습니다.

### 카드 10 — 더 쪼개지 않은 이유   (고급 한글 · 번역)
- 한글 원문: "더 쪼개지 않은 이유는 각 절반이 내부적으로 강하게 결합되어 있기 때문입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: I didn't split the work any further because each half is tightly coupled internally.
- 번역 포인트: "이유는 ~ 때문입니다"를 `The reason … is because …` 로 옮기면 중복이 됩니다. 영어는 `I didn't … because …` 로 행동을 주어에 세우는 쪽이 짧습니다. "강하게 결합"은 소프트웨어 용어 `tightly coupled` 가 정해진 짝이고(`strongly coupled` 는 드뭅니다) 반대는 `loosely coupled`. "더"는 부정문이라 `any further`.

### 카드 11 — 한 번도 실행되지 않았다   (고급 한글 · 번역)
- 한글 원문: "이 어댑터는 실제 Redis에서 한 번도 실행되지 않았습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: This adapter has never been run against a real Redis instance.
- 번역 포인트: "한 번도 ~않았다"는 지금까지의 경험이라 현재완료 `has never been run` 입니다. 과거형 `was never run` 은 "그때는 안 돌렸다"로 끝난 이야기처럼 들립니다. "Redis에서"는 `on` 이 아니라 `against` 를 씁니다. 코드를 어떤 대상에 대고 돌려 본다는 뜻의 전치사입니다. 검증 안 된 부분을 숨기지 않고 밝히는 문장으로, 보고서 끝에 그대로 쓸 만합니다.

### 카드 12 — 오타로 읽었습니다   (고급 한글 · 번역)
- 한글 원문: "'비워주세요'는 '채워주세요'의 오타로 읽었습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 444fbcbd)
- 자연스러운 영어: I read "비워주세요" as a typo for "채워주세요".
- 번역 포인트: `read A as B`(A 를 B 로 해석하다)와 `a typo for X`(X 를 잘못 친 것)를 이으면 됩니다. 오늘 표현 `which I treated as a typo` 와 같은 틀입니다. 내 해석을 먼저 밝히고 일을 진행하면, 틀렸을 때 상대가 바로 고쳐 줍니다. 더 조심스럽게는 `I'm assuming you meant "채워주세요"`.

## 영어 다듬기

### 카드 1 — including 철자와 위치
- 내가 쓴 영어: "recipe 검색 기능 (includig skewvoir)"   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 정정: includig → including. 철자에서 `n` 이 빠졌습니다.
- 더 나은 표현: recipe search (including in Skewvoir) / recipe search, Skewvoir included
- 왜: `including Skewvoir` 라고만 쓰면 "스큐보아를 포함한 검색 기능"으로도, "스큐보아 안의 검색까지"로도 읽힙니다. 화면 안의 검색을 말한다면 `including in Skewvoir` 처럼 전치사를 하나 더 넣어야 분명합니다. `X included` 를 뒤에 붙이는 꼴은 괄호 없이 쓸 수 있어 문장에 넣기 편합니다.

### 카드 2 — commit and push 앞에 조건 붙이기
- 내가 쓴 영어: "commit and push" (한국어 문장 끝에 붙여 씀), "(via herdr)"   (출처: transcript:[user] skewnono-v3-nuxt 444fbcbd)
- 더 나은 표현: If the review comes back clean, commit and push. / Have Codex look it over via Herdr.
- 왜: `commit and push` 와 `via` 는 그대로 맞는 영어입니다. 문장 전체를 영어로 쓸 때는 조건을 `If the review comes back clean` 처럼 붙이면 한 단계 자연스럽습니다. `come back clean` 은 검사·리뷰 결과에 문제가 없다는 뜻의 관용 표현입니다. `via` 는 경로·수단을 말하는 조금 격식 있는 전치사이고, 구어에서는 `through` 로 바꿔도 됩니다.
