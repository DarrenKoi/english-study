# 2026-10-17 — 코칭

## 한글→영어

### 카드 1 — 배포 후 에러와 빈 화면   (내가 쓴 한글)
- 내가 쓴 한글: "최근 변경 사항을 업데이트 했는데, 이런 에러 로깅이 발견되었고, 여러 페이지에서 데이터가 안보여지고 있어."   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: I deployed the latest changes, and now I'm seeing errors like this in the logs, and several pages aren't showing any data.
- 왜 이렇게: "변경 사항을 업데이트했다"는 서버에 반영했다는 뜻이라 `deployed` 가 정확하다(`updated the changes` 는 어색하다). "에러 로깅이 발견되었고"는 수동태 직역(`error logging was found`) 대신 `I'm seeing errors … in the logs` 로 사람을 주어로 세운다. 참고로 "안보여지고"는 이중 피동이라 한국어로도 "안 보이고"가 맞다.

### 카드 2 — 캐시에 lock 이 필요할까   (내가 쓴 한글)
- 내가 쓴 한글: "ttl_cache에 lock도 추가해야 하나?"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: Should we add a lock to `ttl_cache` as well?
- 왜 이렇게: "~해야 하나?"는 스스로 묻는 혼잣말 같은 질문이라 `Do we need to …` 나 `Should we …` 로 연다. "도"는 문장 끝 `as well`/`too` 로 옮긴다. 동사 앞에 `also` 를 두면 무엇에 "도"가 걸리는지 흐려진다.

### 카드 3 — 예전에 저절로 풀렸던 일   (내가 쓴 한글)
- 내가 쓴 한글: "예전에도 비슷하게 데이터가 안불러와지는 일이 있었던 것 같은데, 시간이 지나서 해결됬던 것 같은데 이거는 thread가 새로 바뀌면서 가능했던건가?"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: I think we had something similar before where the data wouldn't load, and it seemed to fix itself after a while. Was that because the threads got replaced?
- 왜 이렇게: "~것 같은데"가 두 번 이어지는 긴 문장은 영어에서 두 문장으로 끊는다. "안 불러와지는"은 반복된 실패라 `wouldn't load`(고집스레 안 되던 과거)가 맞다. "시간이 지나서 해결됐다"는 `fixed itself after a while` 이 구어로 가장 자연스럽다. "가능했던 건가"는 그대로 옮기지 말고 원인을 묻는 `Was that because …?` 로 바꾼다. (한국어 맞춤법: "해결됬던" → "해결됐던")

### 카드 4 — 배포하니 정상   (내가 쓴 한글)
- 내가 쓴 한글: "일단 배포를 했더니 문제 없이 데이터가 불러와지기 시작했어"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: I went ahead and deployed it, and the data started loading without any problems.
- 왜 이렇게: "일단 ~했더니"의 "일단"은 확신 없이 먼저 해 봤다는 뉘앙스라 `went ahead and` 가 잘 맞는다. "-했더니"는 결과가 뒤따르는 연결이라 `and` 로 이으면 된다.

### 카드 5 — 섞여 든 두 번째 증상   (내가 쓴 한글)
- 내가 쓴 한글: "uwsgi_response_write_headers_do(): Broke pip … duringGET /_nuxt/.. 이런 부분에서도 보이네"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: I'm also seeing it on `/_nuxt/` requests, like this: …
- 왜 이렇게: "~에서도 보이네"는 새로 알아챈 사실을 덧붙이는 말이라 `I'm also seeing it on …` 이 정확하다. 로그를 붙일 때는 `like this:` 뒤에 콜론으로 이어 붙이면 깔끔하다.

### 카드 6 — 변경으로 생긴 차이를 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "scroll -> search_after 로 인해 어떤 변경점이 있었던 거지?"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: What actually changed when we switched from scroll to search_after?
- 왜 이렇게: "~로 인해"를 `due to` 로 직역하면 딱딱하다. `when we switched from A to B` 로 사건을 시점절로 바꾸면 말이 된다. "변경점이 있었던 거지?"는 `What actually changed` 로 짧게. `actually` 가 "정확히 뭐가"라는 궁금함을 살린다.

### 카드 7 — 다른 저장소도 봐 달라   (내가 쓴 한글)
- 내가 쓴 한글: "flask modules도 확인해줘"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: Can you check `flask_modules` too?
- 왜 이렇게: 짧은 부탁은 `Can you … too?` 로 충분하다. 명령형 `Check flask_modules too.` 도 되지만 동료에게는 의문형이 부드럽다.

### 카드 8 — 둘을 같게 맞추기   (내가 쓴 한글)
- 내가 쓴 한글: "맞춰줘"   (출처: transcript:[user] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: Yes, please sync them up.
- 왜 이렇게: "맞추다"는 두 사본을 같게 만든다는 뜻이라 `sync them up` 이나 `bring them in line` 이 맞다. 앞 질문("복사해 맞출까요?")에 대한 답이니 `Yes, please` 로 시작하면 자연스럽다.

### 카드 9 — 조용히 사라지는 문서   (내가 쓴 한글)
- 내가 쓴 한글: "ops_store 수정이 필요해. opensearch 3.7 클러스터에서 scroll 방식으로 문서를 가져오면 결과가 클 때 문서가 조용히 사라진다."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: `ops_store` needs a fix. On the OpenSearch 3.7 cluster, fetching documents with scroll silently drops some of them when the result set is large.
- 왜 이렇게: "문서가 조용히 사라진다"는 주어를 바꿔 `scroll … silently drops documents` 로 쓰면 원인이 주어 자리에 온다. `disappear quietly` 보다 기술 글에서 흔하다. "결과가 클 때"는 `when the result set is large`.

### 카드 10 — 다른 방식으로는 전량 확인   (내가 쓴 한글)
- 내가 쓴 한글: "search_after 방식으로 페이지를 나눠 가져오면 전량 들어오는 거 확인했다."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: I've confirmed that paging through with search_after brings back every document.
- 왜 이렇게: "페이지를 나눠 가져오다"는 `page through` 한 동사구로 된다. "전량 들어온다"는 `brings back every document` 나 `returns the full set`. 확인한 사실이 지금도 유효하니 현재완료 `I've confirmed` 가 맞다.

### 카드 11 — 시그니처는 그대로   (내가 쓴 한글)
- 내가 쓴 한글: "함수 시그니처는 그대로"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Keep the function signature as is.
- 왜 이렇게: "그대로"는 `as is` 나 `unchanged`. 지시문이므로 명령형 `Keep …` 로 연다. `The signature stays the same.` 처럼 평서문으로 써도 된다.

### 카드 12 — 전체 개수를 셀 필요가 없다   (내가 쓴 한글)
- 내가 쓴 한글: "track_total_hits를 False로 끝는 것 (전제 개수를 세는 비용이 필요 없어짐)"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Set `track_total_hits` to False, since we no longer need to pay for counting the total.
- 왜 이렇게: "~를 False 로 끄다"는 `set … to False` 나 `turn off`. "비용이 필요 없어짐"은 `we no longer need to pay for …` 로 옮기면 "비용"이 동사 `pay for` 에 녹는다. (오타: "끝는"→"끄는", "전제"→"전체")

### 카드 13 — 루프를 언제 멈출지   (내가 쓴 한글)
- 내가 쓴 한글: "받은 페이지 크기가 요청한 페이지보다 작으면 그만두고, 아니면 마지막 문서의 sort 값을 다음 커서로 저장."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: If the page comes back smaller than requested, stop; otherwise, save the last document's sort value as the next cursor.
- 왜 이렇게: "~면 A, 아니면 B"는 `If …, A; otherwise, B.` 가 정석이다. 세미콜론이 두 갈래를 깔끔하게 나눈다. "받은 페이지 크기가 요청보다 작으면"은 `comes back smaller than requested` 로 줄인다. 반복되는 `page size` 를 빼도 뜻이 산다.

### 카드 14 — 진단이 맞으면 고쳐라   (내가 쓴 한글)
- 내가 쓴 한글: "위가 진단 내용인데, 그게 맞으면 수정해줘. 어쨌던 search_after 방식으로 교체하는거야"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: That's my diagnosis. If it holds up, go ahead and fix it. Either way, the goal is to switch to search_after.
- 왜 이렇게: "그게 맞으면"은 검증을 거쳐도 버틴다는 뜻의 `If it holds up` 이 좋다. "어쨌든"은 `Either way`(맞든 틀리든)가 문맥에 정확하다. `Anyway` 는 화제를 돌리는 느낌이 있다.

### 카드 15 — 원본 저장소도 같이   (내가 쓴 한글)
- 내가 쓴 한글: "upstream flask_modules도 같이 고쳐줘"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Please apply the same fix to upstream `flask_modules` as well.
- 왜 이렇게: "같이 고쳐 줘"는 같은 수정을 거기에도 적용하라는 뜻이라 `apply the same fix to …` 가 정확하다. `fix it together` 로 옮기면 "함께 고치자"로 읽힌다.

### 카드 16 — 상대 에이전트의 확인을 전하기   (내가 쓴 한글)
- 내가 쓴 한글: "upstream도 push 해줘. office agent가 너의 지적이 맞다고 해서 시간 내림차순 + _id asc 조합으로 search_after 전량 수집 확인, 정확하다고 피드백을 줬어."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Push upstream too. The office agent agreed with your point: with time descending plus `_id` ascending, search_after collected every document, and it confirmed the results are correct.
- 왜 이렇게: "너의 지적이 맞다고 해서"는 `agreed with your point` 가 자연스럽다(`said your point was right` 보다 짧다). 콜론 뒤에 확인 내용을 붙이면 "무엇을 확인했는지"가 한눈에 보인다. "피드백을 줬어"를 `gave feedback` 으로 따로 쓰면 군더더기다. `confirmed` 하나로 충분하다.

### 카드 17 — 9시간 스큐의 원인   (내가 쓴 한글)
- 내가 쓴 한글: "meas_hist의 timestamp는 KST 실제 시각으로 찍혀있는데 opensearch가 naive 값을 UTC로 해석해서 지금 9시간분 데이터 차이가 발생하고 있어."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: The `meas_hist` timestamps are stored as actual KST times, but OpenSearch reads those naive values as UTC, so we're currently missing nine hours of data.
- 왜 이렇게: "찍혀 있는데"는 대조라 `but` 으로 잇는다. "~로 해석한다"는 `reads A as B`(`interprets A as B` 는 더 격식). "9시간분 데이터 차이가 발생"은 명사구 직역(`a 9-hour data difference occurs`)보다 `we're missing nine hours of data` 로 결과를 말하는 편이 또렷하다.

### 카드 18 — 공지가 필요할까   (내가 쓴 한글)
- 내가 쓴 한글: "위 버그를 수정했다고 공지사항에 올릴 필요가 있을까?"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Is it worth posting a notice that we fixed this bug?
- 왜 이렇게: "~할 필요가 있을까?"는 해 볼 가치를 묻는 말이라 `Is it worth -ing?` 가 딱이다. `Do we need to …` 는 의무를 묻는 느낌이 더 강하다. "공지사항에 올리다"는 `post a notice` 또는 `put up an announcement`.

### 카드 19 — 어느 화면이 쓰는지 추적   (내가 쓴 한글)
- 내가 쓴 한글: "브리지를 어느 화면이 쓰는지 추적해줘"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Can you trace which screens use the bridge?
- 왜 이렇게: 간접의문문 `which screens use the bridge` 는 평서문 어순(주어+동사)을 지킨다. `which screens does the bridge use` 로 쓰면 틀린다. "추적하다"는 코드 경로라면 `trace` 가 정확하다.

### 카드 20 — 확인할 것과 고칠 것   (내가 쓴 한글)
- 내가 쓴 한글: "어떤 것을 확인하고 수정해야 하는 지 알려줘"   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: Tell me what I need to check and what needs fixing.
- 왜 이렇게: 확인은 내가 하고 수정은 코드에 필요하니 주어를 달리해 `what I need to check and what needs fixing` 으로 나눈다. `need + -ing` 는 수동 뜻("고쳐질 필요가 있다")이 된다.

### 카드 21 — 사본 갱신은 끝, 문서 차례   (내가 쓴 한글)
- 내가 쓴 한글: "ops_store 는 다른 repo 전부 갱신했어. 스키마 문서 업데이트 해줘."   (출처: transcript:[user] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: I've updated `ops_store` in all the other repos. Now please update the schema docs.
- 왜 이렇게: "다른 repo 전부"는 `in all the other repos` 로 장소 전치사 `in` 이 필요하다(`updated all the other repos' ops_store` 는 무겁다). 두 문장 사이에 `Now` 를 넣으면 "그건 끝났고 다음은 이것"이라는 순서가 산다.

### 카드 22 — 결론부터   (고급 한글 · 번역)
- 한글 원문: "결론부터 말하면, 지금은 추가하지 않는 게 낫습니다. lock을 넣어도 이번 증상인 워커 포화는 풀리지 않습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: The short answer is no, not right now. A lock wouldn't relieve the worker saturation we're seeing.
- 번역 포인트: "결론부터 말하면"은 `To put it simply` 나 `In short` 도 되지만, 질문에 대한 답이라 `The short answer is …` 가 가장 영어답다. 뒤에 `The longer answer is …` 를 이어 붙일 수도 있다. "넣어도 풀리지 않는다"는 가정이라 `wouldn't` 를 쓴다. "이번 증상인 워커 포화"는 동격 구조를 `the worker saturation we're seeing` 처럼 관계절로 풀면 자연스럽다.

### 카드 23 — 조용히 적게 보이는 버그   (고급 한글 · 번역)
- 한글 원문: "이 버그가 \"조용히 적게 보이는\" 종류였기 때문입니다. 에러가 난 적이 없어서 사용자는 문제가 있었는지 모르고, 수정 후에는 설명 없이 숫자만 달라집니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: This was the kind of bug that quietly under-reports. It never threw an error, so users had no idea anything was wrong, and after the fix the numbers simply change with no explanation.
- 번역 포인트: "조용히 적게 보이는"을 `quietly under-reports` 한 동사로 줄였다. `under-` 접두사가 "덜, 모자라게"를 맡는다(`underestimate`, `undercount`). "모르고"는 `had no idea` 가 구어로 더 생생하다. "숫자만 달라진다"의 "만"은 `simply` 로 옮긴다. 다른 설명 없이 숫자만 바뀐다는 허전함이 산다.

### 카드 24 — 공지에 쓸 것과 뺄 것   (고급 한글 · 번역)
- 한글 원문: "공지에는 원인(scroll, UTC 해석)을 쓰지 말고 증상과 영향만 쓰는 게 낫습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/547d3d09)
- 자연스러운 영어: In the notice, stick to the symptoms and their impact, and leave out the cause (scroll, the UTC interpretation).
- 번역 포인트: "A 는 쓰지 말고 B 만 쓰라"를 영어에서는 긍정을 앞세워 `stick to B, and leave out A` 로 뒤집는다. 무엇을 할지 먼저 말해야 지침이 또렷하다. "~하는 게 낫다"는 조언이지만, 지침 맥락이면 명령형으로 써도 무례하지 않다.

### 카드 25 — 이번 일의 교훈   (고급 한글 · 번역)
- 한글 원문: "데이터 누락을 고치는 변경은 받는 양을 늘려서 조회를 느리게 만들 수 있으니, 행 수뿐 아니라 걸리는 시간도 확인해야 한다"   (출처: transcript:[assistant] skewnono-v3-nuxt/290c8938)
- 자연스러운 영어: A fix for missing data can slow a query down by increasing how much it fetches, so check how long it takes, not just how many rows come back.
- 번역 포인트: "데이터 누락을 고치는 변경"은 `A fix for missing data` 로 명사구 하나에 담는다. "행 수뿐 아니라 걸리는 시간도"는 `not only A but also B` 보다 `B, not just A` 순서가 구어로 가볍다. 새로 강조할 것(시간)이 앞에 온다.

## 영어 다듬기

### 카드 26 — 지시서대로 끝까지   
- 내가 쓴 영어: "Read ./ROUND2-afm-recipes.md and do everything it says, without asking me questions."   (출처: transcript:[user] skewnono-afm-recipes/4e1c4ef9)
- 더 나은 표현: Follow everything in ./ROUND2-afm-recipes.md end to end — no need to check in with me along the way.
- 왜: 원문에 오류는 없다(같은 틀은 10-05 에 다뤘다). `without asking me questions` 는 질문 자체를 막는 말이라 조금 딱딱하다. `no need to check in with me` 는 "중간에 확인받지 않아도 된다"는 허락으로 읽혀 부드럽다. `end to end` 를 넣으면 "중간에 멈추지 말고 끝까지"가 분명해진다. 첫 지시문의 `Stop when ./REPORT-afm-recipes.md is written.` 처럼 종료 조건을 하나 더 붙이면 이번 라운드도 언제 끝내야 하는지 모호하지 않다.
