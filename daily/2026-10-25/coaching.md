# 2026-10-25 — 코칭

## 한글→영어

오늘 내가 쓴 한국어는 사무실 회신 정리(번호 매긴 12개 항목 + 핵심 결론)와 로깅 요청 한 줄이다. 메모체("~함", "~불가")가 많아서 영어로는 완전한 문장과 메모체를 어떻게 갈라 쓰는지가 연습 포인트다.

### 카드 1 — 회신 머리말   (내가 쓴 한글)
- 내가 쓴 한글: "회신은 다음과 같다."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: Here's what came back from the office. / Here are the answers.
- 왜 이렇게: "다음과 같다"를 `as follows` 로 직역하면(`The replies are as follows.`) 공문서처럼 딱딱하다. 채팅에서는 `Here's …` / `Here are …` 가 기본이다. "회신"은 `the reply` 도 되지만 질문지에 대한 답이면 `the answers`, 누가 보냈는지 살리려면 `what came back from …` 이 자연스럽다.

### 카드 2 — 오류 0건 보고   (내가 쓴 한글)
- 내가 쓴 한글: "B - recipe 목록 오류 0 건."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: B — no errors on the recipe list. (메모체) / There were no errors on the recipe list. (문장)
- 왜 이렇게: 영어는 `0 errors` 보다 `no errors` 가 훨씬 자연스럽다. 숫자 0 은 표·로그에서나 쓴다. 메모체라면 `be` 동사를 빼도 되지만 관사·`no` 는 남긴다.

### 카드 3 — 표본이 없어 확인 불가   (내가 쓴 한글)
- 내가 쓴 한글: "이 레시피의 meas_hist 표본이 0 건( 어느 ㅍfab에도 문서 없음)이라 확인 불가."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: Can't confirm — this recipe has no samples in meas_hist (no documents in any fab).
- 왜 이렇게: 한국어는 이유 → 결론("~라 확인 불가") 순서지만 영어 메모는 결론(`Can't confirm`)을 앞에 두고 대시 뒤에 이유를 단다. "확인 불가"는 `unverifiable` 보다 `Can't confirm` / `Couldn't check` 가 구어에 맞다. "어느 fab 에도"는 `in any fab` (부정문 속 `any`).

### 카드 4 — 로그에 안 남는다   (내가 쓴 한글)
- 내가 쓴 한글: "원 요청의 화면 경로는 로그에 남지 않음. 재현 경로는 H->A"   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: The logs don't record which screen the original request came from. The repro path was H → A.
- 왜 이렇게: "로그에 남지 않는다"는 사물 주어 `The logs don't record …` 로 뒤집으면 영어답다(`is not left in the log` 는 어색). "원 요청의 화면 경로"는 명사를 쌓기보다 `which screen … came from` 간접의문절로 푼다. "재현"은 개발자끼리 `repro` 로 줄여 쓴다.

### 카드 5 — 무엇 기준으로 적재되나   (내가 쓴 한글)
- 내가 쓴 한글: "C 현재 장비 위치 기준 적재."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: C — it's stored based on where the tool is now. / C — loaded by the tool's current location.
- 왜 이렇게: "~기준"은 `based on` 이 무난하고 `by` 가 더 짧다. "적재"는 문맥 따라 `stored`, `loaded`, `written` 중에서 고르는데, DB 에 쌓이는 거면 `stored`/`written` 이 가장 흔하고요. "현재 위치"는 `where the tool is now` 처럼 절로 풀면 말로 할 때 편하다.

### 카드 6 — URL 에 이미 있었다   (내가 쓴 한글)
- 내가 쓴 한글: "A 처음 여는 주소창 URL에 &fab_name=M16B 있었음."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: A — `&fab_name=M16B` was already in the address bar when the page first opened.
- 왜 이렇게: "처음 여는 주소창 URL"처럼 수식어를 명사 앞에 쌓는 구조는 영어에서 `when the page first opened` 시간절로 뒤에 뺀다. "있었다"는 `was there` / `was in` 이면 충분하고 `already` 를 넣으면 "누가 넣은 게 아니라 처음부터"라는 회신의 요점이 산다.

### 카드 7 — 출처는 데이터 자체   (내가 쓴 한글)
- 내가 쓴 한글: "M16B의 출는 데이터 자체. 재현에서도 검색표 행 링크가 fab_name=M16B를 어 보냈습니다."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: M16B comes from the data itself. In the repro, the link on the search-table row also sent `fab_name=M16B`.
- 왜 이렇게: "~의 출처는 X 다"는 `X is the source of …` 보다 `… comes from X` 가 짧고 자연스럽게 들린다. `itself` 는 "다른 데가 아니라 바로 그것"이라는 강조. "실어 보냈다"는 `sent` 또는 `passed along` 이면 된다. "검색표 행 링크"는 `the link on the search-table row` 처럼 전치사로 풀어 명사 세 개 연달아 붙이는 걸 피한다.

### 카드 8 — 세 갈래 원인을 한 문장에   (내가 쓴 한글)
- 내가 쓴 한글: "세 레시피 모두 m16 카탈로그, tools_in_rcp_m16b에 등재되어 있으나, rcp_loc_m16b에만 항목이 없고, meas_hist어느 fab에도 0건이라 열지 못합니다."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: All three recipes are listed in the m16 catalog and in `tools_in_rcp_m16b`, but they have no entry in `rcp_loc_m16b` and no rows in meas_hist for any fab, so they can't be opened.
- 왜 이렇게: 한국어 "~있으나, ~없고, ~이라 ~못한다"는 연결어미 사슬이다. 영어로는 `A, but B and C, so D` 로 역접·병렬·결과를 접속사 하나씩 맡긴다. "~에만 항목이 없다"의 `만` 은 대비를 뜻하는데, 영어에선 앞의 `but` 이 그 대비를 맡으니 `only` 를 넣지 않는다(`only … no entry` 는 오히려 헷갈린다).

### 카드 9 — 묻지 않은 부수 발견   (내가 쓴 한글)
- 내가 쓴 한글: "참고: 묻지 않은 유형으로 param-detail 503이 65건 있었습니다. (원 오의 43%)"   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: FYI, there were also 65 param-detail 503s, which you didn't ask about (43% of the original errors).
- 왜 이렇게: "참고:"는 `FYI,` 또는 `Side note:`. "묻지 않은 유형으로"는 관계절 `which you didn't ask about` 로 뒤에 붙이면 자연스럽다. 상태 코드는 `503s` 처럼 복수형으로 센다. `also` 를 넣으면 "이건 별건"이라는 느낌이 산다.

### 카드 10 — 로그를 더 자세히   (내가 쓴 한글)
- 내가 쓴 한글: "일단 skewnono logging에 자세한 내역이 적재될 수 있게 만들어야 함. opensearch를 통해서 debuging 하는 수밖에."   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: For now, we need skewnono's logging to record the details. Debugging through OpenSearch is the only option we have.
- 왜 이렇게: "일단"은 `For now` / `First`. "~수 있게 만들어야 한다"는 `make it possible for … to be stored` 로 직역하면 길다. `need X to do Y` 사역 구조가 짧다. "~하는 수밖에 (없다)"는 `the only option` / `the only way` 가 정석이며 구어로는 `We'll just have to debug it through OpenSearch.` 도 좋다.

### 카드 11 — 진짜 원인은 어긋남   (고급 한글 · 번역)
- 한글 원문: "진짜 원인은 등록부 두 hash 의 어긋남입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: The real cause is a mismatch between two hashes in the registry.
- 번역 포인트: "어긋남"은 `mismatch` 가 가장 정확하고 시간이 지나며 생긴 차이를 강조하려면 `drift` 도 된다. "A 의 B 의 어긋남"처럼 소유격이 겹치면 영어에선 `a mismatch between X and Y` / `between two …` 로 관계를 전치사에 맡긴다.

### 카드 12 — 조용해지지 않는다   (고급 한글 · 번역)
- 한글 원문: "틀리면 FTP 단계에서 \"Could not download\" 502 가 나므로 지금보다 조용해지지는 않습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: If that's wrong, the FTP step returns a "Could not download" 502, so it fails no more quietly than it does today.
- 번역 포인트: "조용해지지는 않는다"는 "실패가 숨겨지지 않는다"는 뜻이다. `no more quietly than` 비교 부정이 원문 구조와 가장 가깝고 풀어서 `so the failure won't be any harder to notice` 라고 해도 된다. "~가 나다"는 오류가 주어일 때 `returns` / `throws` / `you get a 502` 중 골라 쓴다.

### 카드 13 — 기준을 먼저 밝히기   (고급 한글 · 번역)
- 한글 원문: "이번 추적에서 로그만으로 알 수 없었던 두 정보가 기준입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt b4fc9877)
- 자연스러운 영어: I picked these based on the two things this investigation couldn't learn from the logs alone.
- 번역 포인트: "~가 기준이다"를 `X is the criterion` 으로 옮기면 무엇의 기준인지가 빠진다. 영어는 행위자를 살려 `I picked these based on …` 으로 쓴다. "로그만으로"는 `from the logs alone`. `alone` 을 명사 뒤에 두는 게 핵심이다.

## 영어 다듬기

### 카드 14 — 새 버전이 대신해 주나
- 내가 쓴 영어: "now pi supports mcp in the latest version, so now I do not need the pi-mcp-adapter package?"   (출처: transcript:[user] skewnono_v3_nuxt fc3f283c)
- 정정: 문장 첫 글자는 대문자(`Now`), 고유명·약어는 표기대로(`MCP`). `now` 가 두 번 나와 군더더기다.
- 더 나은 표현: Now that the latest pi supports MCP natively, do I still need the pi-mcp-adapter package?
- 왜: `Now that …` 은 "이제 ~하니까"라는 이유 접속사다. 첫 `now` 의 뜻은 살리고 두 번째 `now` 는 없애는 셈. 평서문 끝에 물음표만 다는 질문은 말로는 되지만 글에서는 의문문 어순(`do I still need`)이 또렷하다. `still` 이 "예전엔 필요했는데"라는 맥락까지 담는다.

### 카드 15 — 기존 로그에 영향이 있나
- 내가 쓴 영어: "if I re-run skewnono_logging.py, does it affect the previously stored logging like user visit?"   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 정정: 쌓인 데이터는 `logging`(행위)이 아니라 `logs`(기록). 예시는 복수로 `user visits`. 문장 첫 글자 대문자(`If`).
- 더 나은 표현: If I re-run skewnono_logging.py, will it affect logs that are already stored, like user visits?
- 왜: 조건절 뒤 결과를 묻을 때는 `will it affect` 가 자연스럽다(`does` 는 일반적 사실을 묻는 느낌). `previously stored` 도 맞지만 `already stored` 가 구어에 더 가깝다. `like` 는 구어 예시, 글에서는 `such as`.

### 카드 16 — 명령을 돌려 달라고 할 때
- 내가 쓴 영어: "and then do /code-review high"   (출처: transcript:[user] skewnono_v3_nuxt b4fc9877)
- 더 나은 표현: After that, run `/code-review high`.
- 왜: 문법 오류는 없다. 다만 명령어·스크립트는 `do` 보다 `run` 이 정확한 동사다. `and then` 으로 시작하면 앞 문장에 매달린 조각처럼 읽히니, 따로 보낼 때는 `After that,` / `Then` 으로 독립시킨다.
