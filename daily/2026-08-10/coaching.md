# 2026-08-10 — 코칭

## 한글→영어

### 카드 1 — 지금 적용 가능한 것부터   (내가 쓴 한글)

- 내가 쓴 한글: "지금 시점에서 적용 가능한 것들 (특히 현재 코드에 더 좋은 이점으로 작용한다면) 적용해보자"   (출처: transcript:[user] 2fc9f8aa)
- 자연스러운 영어: Let's apply whatever we can land right now — especially the items that actually make the current code better.
- 왜 이렇게: "지금 시점에서 적용 가능한"을 `applicable at this point in time` 으로 옮기면 번역투가 됩니다. `what we can land right now` 처럼 **동사로 풀면** 훨씬 자연스럽습니다(`land` 는 "변경을 실제로 머지해 넣다"는 개발 현장 동사). 괄호 안의 단서는 영어에서 괄호보다 대시가 잘 어울리고, "더 좋은 이점으로 작용한다"는 `make the current code better` 로 줄이는 편이 낫습니다 — `act as a better benefit` 은 영어로 성립하지 않습니다.

### 카드 2 — 항목 골라서 적용   (내가 쓴 한글)

- 내가 쓴 한글: "A, C, D 적용"   (출처: transcript:[user] 2fc9f8aa)
- 자연스러운 영어: Go ahead with A, C, and D. / Apply A, C, D — skip B.
- 왜 이렇게: 목록에서 일부만 고르는 지시는 `Go ahead with …` 가 가장 짧고 자연스럽습니다. 명사만 던지는 한국어 지시("적용")를 영어로 그대로 옮기면 무례하게 들리므로, 동사 하나만 앞에 붙이면 됩니다. **뺀 것을 명시**하는 `skip B` 한마디가 오해를 막아 주니 습관으로 붙일 만합니다.

### 카드 3 — 최적화 여부 확인 요청   (내가 쓴 한글)

- 내가 쓴 한글: "msr image를 호출할 때 (장비로부터 받거나, minIO upload/download) 우리는 async 방식으로 최고 속도와 최적화를 진행하고 있는 지 확인 해줘"   (출처: transcript:[user] 70b03c04)
- 자연스러운 영어: Check whether the MSR image path — fetching from the tool, and uploading to and downloading from MinIO — is actually async and as fast as it could be.
- 왜 이렇게: "확인해줘"는 `Check whether …` 로 시작하는 게 정석입니다(`Confirm` 은 이미 답을 정해 두고 도장 찍으라는 뉘앙스라 여기엔 안 맞습니다). "최고 속도와 최적화를 진행하고 있는지"는 명사 두 개를 나열했지만 영어에서는 형용사로 푸는 편이 자연스러워 `as fast as it could be` 로 옮겼습니다. `upload/download` 처럼 슬래시로 묶은 것은 영어에서 전치사가 갈리므로(`upload to` / `download from`) 풀어 써야 문장이 맞습니다.

### 카드 4 — 캐시 활용 여부 질문   (내가 쓴 한글)

- 내가 쓴 한글: "tiff의 경우도 webp 전환 후 image_cache (minIO)에 저장해 cache로 활용하나?"   (출처: transcript:[user] 70b03c04)
- 자연스러운 영어: For TIFFs, do we store the converted WebP back into the MinIO image cache and serve it from there?
- 왜 이렇게: "~의 경우도"는 `in the case of …` 로 옮기기 쉽지만 영어에서는 `For TIFFs,` 로 시작하는 게 훨씬 가볍습니다. "cache로 활용하나"는 캐시라는 명사를 다시 쓰기보다 **동사 `serve it from there`** 로 옮겨야 "그 캐시에서 꺼내 응답하느냐"는 진짜 질문이 드러납니다. `back into` 의 `back` 이 "왔던 곳으로 되돌려 넣는다"를 한 단어로 처리합니다.

### 카드 5 — 더 안전한 쪽 선택   (내가 쓴 한글)

- 내가 쓴 한글: "webp 더 안전한 방식으로 가자. 진행해줘"   (출처: transcript:[user] 70b03c04)
- 자연스러운 영어: Let's go with the safer WebP option. Go ahead.
- 왜 이렇게: "~로 가자"는 `go with X` 가 정확한 대응입니다(`go to` 가 아닙니다). 비교 대상이 둘일 때는 `safest` 가 아니라 **`the safer`** 로 비교급을 쓰고 정관사를 붙입니다. 마지막의 "진행해줘"는 `Please proceed with the work` 처럼 늘리지 말고 `Go ahead.` 두 단어면 충분합니다.

### 카드 6 — 검토 요청 + 제약 설명   (내가 쓴 한글)

- 내가 쓴 한글: "vendored folder: ftp_handler 검토해볼 수 있어? 구조는 가능하면 변경하고 office에서 테스트하면 되니까."   (출처: transcript:[user] 70b03c04)
- 자연스러운 영어: Can you review the vendored `ftp_handler`? Feel free to restructure it where it helps — we can test it at the office anyway.
- 왜 이렇게: "~하면 되니까"는 한국어 특유의 허락·안심 어미인데, 영어에서는 문장 끝의 **`anyway`** 가 그 몫을 합니다("어차피 그렇게 하면 되니까"). "가능하면 변경하고"를 `change it if possible` 로 옮기면 소극적으로 들려서, 허가의 뉘앙스를 살리려면 `Feel free to …` 가 맞습니다. `where it helps` 는 "도움이 되는 곳에 한해"라는 조건을 두 단어로 붙인 것입니다.

### 카드 7 — 두 저장소 동시 변경 승인   (내가 쓴 한글)

- 내가 쓴 한글: "좋아 두 ftp_handler를 동시에 바꾸자. 작업 진행해줘"   (출처: transcript:[user] 70b03c04)
- 자연스러운 영어: Good — let's change both copies of `ftp_handler` together. Go ahead and do it.
- 왜 이렇게: "두 ftp_handler"는 영어로 `two ftp_handlers` 보다 **`both copies of ftp_handler`** 가 정확합니다(같은 라이브러리의 사본 둘이니까요). "동시에"는 `simultaneously` 가 아니라 `together`/`in one go` 가 자연스럽습니다 — 시각적 동시성이 아니라 "한 묶음으로"라는 뜻이니까요.

### 카드 8 — 실패가 무작위처럼 보였다   (고급 한글 · 번역)

- 한글 원문: "이 버그가 위험했던 이유는 실패가 무작위처럼 보였다는 점입니다. 같은 파라미터도 장비 부하에 따라 45초를 넘기도 안 넘기도 하고, 넘었을 때의 증상은 '장비가 느렸다'와 구분되지 않습니다."   (출처: transcript:[assistant] 70b03c04)
- 자연스러운 영어: What made this bug dangerous is that the failures looked random. The same parameter could cross the 45-second line or stay under it depending on tool load, and when it did cross, the symptom was indistinguishable from "the tool was just slow."
- 번역 포인트: "~했던 이유는 ~라는 점입니다"를 `The reason … is that …` 으로 옮기면 무겁습니다. **`What made X dangerous is that …`** 라는 what-분열문이 같은 강조를 훨씬 가볍게 냅니다. "넘기도 안 넘기도 하고"는 반복 어미라 영어에 대응이 없으니 `could … or …` 의 조동사 하나로 가능성을 표현했습니다. "구분되지 않는다"는 `cannot be distinguished` 보다 형용사 `indistinguishable from` 이 압축적입니다.

### 카드 9 — 측정 대상이 측정을 오염시킨다   (고급 한글 · 번역)

- 한글 원문: "계측 중에는 host_timeout을 1시간으로 강제합니다. 이걸 안 하면 측정 대상이 측정을 오염시킵니다 — 포기된 호스트는 소요시간이 아니라 실패를 돌려주므로, 느린 파일만 조용히 사라지고 평균이 빠른 쪽으로 편향됩니다."   (출처: transcript:[assistant] 70b03c04)
- 자연스러운 영어: While measuring, the script forces `host_timeout` to an hour. Without that, the thing being measured corrupts the measurement: an abandoned host returns a failure rather than a duration, so the slow files quietly drop out and the average skews fast.
- 번역 포인트: "측정 대상"은 `the target` 이 아니라 **`the thing being measured`** 로 진행 수동을 써야 "지금 재고 있는 그것"이라는 관계가 삽니다. "~므로"는 인과라 `so` 로 충분하고, 앞에 콜론을 두면 "이제 그 이유를 설명한다"는 신호가 됩니다. "평균이 빠른 쪽으로 편향된다"는 `skew` 뒤에 형용사를 부사처럼 붙이는 통계 관용(`skews fast`, `skews high`)이 있어 그대로 쓸 수 있습니다.

### 카드 10 — 기계 한 대에만 존재하는 규칙   (고급 한글 · 번역)

- 한글 원문: "규칙이 adapter가 아니라 이 표에 있는 이유는 `office.py`가 gitignore 대상이기 때문입니다. adapter 안에만 있는 규칙은 기계 한 대에만 존재하는 규칙입니다."   (출처: transcript:[assistant] 2fc9f8aa)
- 자연스러운 영어: The rule lives in this table rather than in the adapter because `office.py` is gitignored. A rule that exists only inside the adapter is a rule that exists on exactly one machine.
- 번역 포인트: 소재를 말할 때 `is in` 보다 **`lives in`** 이 문서·코드베이스 영어에서 훨씬 자연스럽습니다. 둘째 문장은 원문이 "A는 B다" 형태의 정의문이라 영어에서도 `A rule that … is a rule that …` 로 **같은 명사를 두 번 써서 대구**를 만드는 편이 낫습니다 — `is only on one machine` 으로 줄이면 경구 같은 맛이 사라집니다. `exactly one` 의 `exactly` 가 "고작 한 대"라는 어이없음을 얹습니다.

## 영어 다듬기

### 카드 11 — 남은 작업 묻기

- 내가 쓴 영어: "what else do we have onen tasks?"   (출처: transcript:[user] 2fc9f8aa)
- 정정: `onen` → `on` (오타). 그리고 `what else do we have on` 뒤에 명사를 겹쳐 쓸 수 없습니다 — `have X on` 어순이라 `what else do we have on?` 으로 끝나야 합니다.
- 더 나은 표현: What else is on the list? / What else have we got open?
- 왜: `have something on` 은 "예정된 일이 있다"는 뜻이라 그 자체로 완결됩니다. 여기서 진짜 묻고 싶은 건 **미완 작업**이므로 `open` 을 쓰는 쪽이 정확합니다(`open jobs`, `still open`). 회의체로는 `What's still open?` 세 단어면 충분합니다.

### 카드 12 — 방법 묻기

- 내가 쓴 영어: "how can we give a pane name?"   (출처: transcript:[user] 9cb33a18)
- 정정: 관사 누락. `give a pane a name` 또는 `give a pane name` 이 아니라 **`name a pane`** 이 맞습니다. 지금 문장은 "pane name 이라는 것을 준다"로 읽힙니다.
- 더 나은 표현: How do we name a pane? / How do I label a pane?
- 왜: `can we` 는 가능 여부를 묻는 뉘앙스라, 방법을 물을 때는 `How do we …?` 가 자연스럽습니다. 또 이 도구에서는 사용자가 붙이는 이름을 `label` 이라 부르므로, **도메인 용어를 그대로 쓰면** 답이 정확해집니다 — `How do I set a pane's label?`

### 카드 13 — 개선 효과 묻기

- 내가 쓴 영어: "so now what benefits can we expect from ftp handler improvement?"   (출처: transcript:[user] 70b03c04)
- 정정: 관사 누락 — `from the ftp handler improvement` 또는 `from the ftp_handler changes`. 특정 작업을 가리키므로 정관사가 필요합니다.
- 더 나은 표현: So what do we actually get out of the `ftp_handler` work?
- 왜: `what benefits can we expect from X` 는 문법적으로 맞지만 제안서 문체라 대화에서는 딱딱합니다. `what do we get out of X` 가 같은 뜻의 구어체이고, `actually` 한 단어가 **"홍보 말고 실제로"** 라는 압박을 자연스럽게 얹습니다. 실제로 돌아온 답도 "속도 개선은 거의 없다"였으니 그 압박이 유효했던 질문입니다.

### 카드 14 — 승인하기

- 내가 쓴 영어: "yes  please do it"   (출처: transcript:[user] 70b03c04)
- 정정: (문법 오류 없음 — 이중 공백만 정리)
- 더 나은 표현: Yes, please — go ahead. / Yes, let's do it.
- 왜: `please do it` 은 문법은 맞지만 명령에 `please` 만 붙인 형태라 다소 뚝뚝합니다. 콤마로 `Yes, please` 를 끊고 `go ahead` 를 붙이면 **동의 + 착수 허가**가 자연스럽게 나뉩니다. 조금 더 방향을 얹고 싶으면 `Yes — start with the measurement script.` 처럼 첫 항목을 지정하는 편이 좋습니다.
