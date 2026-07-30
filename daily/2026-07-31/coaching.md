# 2026-07-31 — 코칭

오늘 배치의 `[user]` 발화는 전부 영어였습니다. 그래서 `한글→영어` 는 어시스턴트의 고급 한국어를 옮기는 (b) 번역 정독 카드만 싣고, 대신 `영어 다듬기` 가 열 장으로 두꺼워졌습니다.

## 한글→영어

### 카드 1 — 예산 상한이 없었다면 (고급 한글 · 번역)

- 한글 원문: "문서 예산 60% 상한이 없었다면 한국어 설계 문서 7건이 예산을 다 먹고 트랜스크립트가 밀려, 코칭 카드가 0장이 됐을 겁니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: Without the 60% cap on the documentation budget, seven Korean design docs would have eaten the whole allowance, pushed the transcripts out, and left the day with zero coaching cards.
- 번역 포인트: "~가 없었다면"을 `If there had been no ~` 로 풀면 무겁습니다. 전치사 `Without` 하나로 가정법 과거완료의 조건절을 대신하고 주절만 `would have p.p.` 로 남기면 문장이 반으로 줍니다. "예산을 다 먹고"의 `eat` 는 영어에서도 자원 소모에 그대로 쓰는 구어라 `consume` 보다 생생합니다. 한국어는 "밀려"로 피동을 썼지만 영어는 `pushed the transcripts out` 능동이 자연스럽고, 세 동사 `eaten / pushed / left` 를 한 조동사 아래 나란히 묶어 인과를 한 호흡에 담았습니다.

### 카드 2 — 잔량은 손실이 아니다 (고급 한글 · 번역)

- 한글 원문: "`collect` 는 상태 추적 없이 매번 다시 훑으므로 이 잔량은 손실이 아니라 다음 실행의 후보로 남습니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: Since `collect` re-scans from scratch every run and keeps no state, the backlog is not lost work — it stays queued as a candidate for the next run.
- 번역 포인트: "상태 추적 없이"를 `without state tracking` 으로 직역하면 명사가 무거워지므로, 동사절 `keeps no state` 로 풀었습니다. 핵심은 "A 가 아니라 B"인데, 영어에서는 `not A but B` 보다 대시로 끊고 다시 시작하는 편이 말맛이 삽니다. "남습니다"의 잔류 어감은 `stays` 가 받고, "후보로"는 `as a candidate` 로 자격을 표시하는 전치사 `as` 를 씁니다.

### 카드 3 — 통짜 인용과 구분하기 (고급 한글 · 번역)

- 한글 원문: "정독 단락은 여러 문단을 한 단락으로 이어 붙였으므로, 출처 줄에 그 사실을 명시해 통짜 인용과 구분했습니다."   (출처: transcript:[assistant] english-study)
- 자연스러운 영어: The reading passages stitch several paragraphs into one, so the source line says as much — that keeps them distinct from a verbatim quotation.
- 번역 포인트: "이어 붙이다"는 `stitch A into B` 가 딱 맞습니다. 천 조각을 꿰맨다는 그림이 살아 있어 `combine` 보다 정확하죠. "그 사실을 명시해"를 `states that fact` 로 옮기면 늘어지는데, 관용구 `say as much`("그렇다고 밝히다")를 쓰면 앞 문장을 대명사 없이 되받습니다. "통짜 인용"은 `a verbatim quotation` — 원문 그대로라는 뜻의 `verbatim` 이 학술·인용 문맥의 표준어입니다.

## 영어 다듬기

### 카드 1 — 스크립트를 만들어 달라는 요청

- 내가 쓴 영어: "can you generate to check the redis keys for device_info_hvm and device_info_rnd in scripts folder?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `generate` 는 타동사라 목적어가 필요합니다 → `generate a script to check ~`. 그리고 `in scripts folder` 는 특정 폴더를 가리키므로 관사가 붙어야 합니다 → `in the scripts folder`.
- 더 나은 표현: Could you add a script under `scripts/` that checks the Redis keys `device_info_hvm` and `device_info_rnd`?
- 왜: 무엇을 만들지(`a script`) 어디에 둘지(`under scripts/`) 무엇을 하는지(`that checks ~`)를 순서대로 놓으면 되묻지 않아도 되는 요청이 됩니다. `generate` 는 데이터·코드를 기계적으로 뽑아낸다는 색이 강해서, 파일 하나 추가하는 일에는 `add` 나 `write` 가 더 자연스럽습니다.

### 카드 2 — 인덱스를 소개하는 문장

- 내가 쓴 영어: "from opensearch we have index "sknn-planstep-r3" that contain steps we are interested in."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 관계절의 선행사가 단수 `an index` 이므로 `that contain` → `that contains`. 가산명사 단수 앞의 관사도 빠졌습니다 → `we have an index`.
- 더 나은 표현: In OpenSearch there's an index, `sknn-planstep-r3`, that holds the steps we care about.
- 왜: `from opensearch we have ~` 는 출처를 문두에 던져 놓은 한국어 어순입니다. 존재를 알리는 문장은 `In X there's ~` 로 시작하면 영어 리듬에 맞습니다. 이름을 쉼표로 감싸 동격으로 두면 뒤 관계절이 `index` 를 가리키는 게 분명해집니다.

### 카드 3 — 명명 규칙 설명

- 내가 쓴 영어: "we tend to add suffix "_BASE" for the product name as BASE is the basic setting for the process integration for the devices"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `add suffix` → `add the suffix`(특정 접미사). 붙이는 대상은 `for` 가 아니라 `to` 를 씁니다 → `add ~ to the product name`. `for the process integration for the devices` 는 `for` 가 연달아 두 번이라 걸리므로 뒤쪽을 `on those devices` 로 바꿉니다.
- 더 나은 표현: We append `_BASE` to the product name, since BASE is the baseline setting for process integration on those devices.
- 왜: 문자열 끝에 붙이는 동작에는 `append` 가 전문어로 정확하고, `add A to B` 는 붙이는 방향을 전치사가 알려 줍니다. `basic` 은 "기초적인·별것 없는"으로 읽힐 수 있어, "기준이 되는"이라는 뜻이면 `baseline` 이 오해가 없습니다.

### 카드 4 — 판단을 밝히는 한 문장

- 내가 쓴 영어: "I think it is find to sort based on the oper_det_desc."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `find` 는 `fine` 의 오타입니다 → `it is fine to sort ~`.
- 더 나은 표현: I think sorting by `oper_det_desc` is fine.
- 왜: 가주어 `it ~ to부정사` 도 맞지만, 화제가 "정렬하는 것"이면 동명사를 그대로 주어 자리에 놓는 편이 짧고 직접적입니다. 정렬 기준은 `based on` 보다 `by` 한 단어로 충분합니다 — `sort by`, `group by`, `filter by` 는 데이터 작업의 고정 짝입니다.

### 카드 5 — 접두사 순서 설명

- 내가 쓴 영어: "But normally, it starts with prefix (ISO, CW, BG, ...) in order (but it differ based on the tool)"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 3인칭 단수 현재의 `-s` 가 빠졌습니다 → `it differs`. 가산명사 앞 관사도 필요합니다 → `starts with a prefix`.
- 더 나은 표현: They normally start with one of these prefixes, in this order — though the actual order varies by tool.
- 왜: 실제 가리키는 것이 여러 값이라면 복수 `They` 로 받는 편이 `it` 보다 헷갈리지 않습니다. 나열한 목록 중 하나라는 뜻은 `one of these prefixes` 가 정확하고, 양보는 `but` 을 또 쓰기보다 `though` 로 받으면 앞의 `but` 과 겹치지 않습니다.

### 카드 6 — 화면에 단서를 남겨 달라는 요구

- 내가 쓴 영어: "You can sort them based on that order but should specify that the we do not consider operation process in the page."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `that the we` 에서 `the` 가 잘못 들어갔습니다 → `that we`. 화면 위에 표시한다는 뜻이면 `in the page` 보다 `on the page` 입니다.
- 더 나은 표현: Sort by that order, but state on the page that it does not reflect the actual process order.
- 왜: `You can ~ but should ~` 는 허락과 의무가 한 문장에서 뒤섞여 지시의 힘이 약합니다. 명령형 두 개를 `but` 으로 이으면 "이렇게 하되 이건 꼭"이 또렷해집니다. "고려하지 않는다"는 화면 문구로는 어색하니, 정렬이 무엇을 뜻하지 *않는지*를 밝히는 `does not reflect ~` 로 뒤집었습니다.

### 카드 7 — 탭이 중복이라는 지적

- 내가 쓴 영어: "개요 seems duplicated info, same as idp_image_info table."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `seem` 뒤에 명사구가 바로 오면 `to be` 가 필요합니다 → `seems to be duplicated info`. 비교 대상에도 관사가 빠졌습니다 → `the same as the idp_image_info table`.
- 더 나은 표현: The 개요 tab looks redundant — it repeats what the `idp_image_info` table already shows.
- 왜: `look` 은 `seem to be` 없이 명사·형용사를 바로 받아 더 간결합니다. `duplicated` 는 "복제된"이라 행위의 결과를 가리키는데, 여기서 하고 싶은 말은 "있어도 그만"이라는 평가이므로 `redundant` 가 맞습니다. 무엇이 왜 중복인지 대시 뒤에 한 절로 붙이면 근거까지 한 문장에 들어갑니다.

### 카드 8 — 탭 교체 지시

- 내가 쓴 영어: "replace 개요 with AMP info table. 개요 -> AMP and move the amp table to there."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `there` 는 그 자체로 "그곳으로"를 뜻해 `to` 가 겹칩니다 → `move the AMP table there`.
- 더 나은 표현: Rename the 개요 tab to AMP and move the AMP table into it.
- 왜: 탭 이름만 바뀌고 자리는 그대로면 `replace A with B` 보다 `rename A to B` 가 실제 작업을 정확히 부릅니다. 목적지가 앞에 나온 탭이라면 `there` 대신 대명사 `into it` 을 써야 어느 곳인지 붙잡힙니다.

### 카드 9 — 탭 분리 요청

- 내가 쓴 영어: "Also in 이미지 + 설정 tab, sequence_addressing & measurement can be in the seperated tab (sequence)"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 철자 `seperated` → `separated`. 다만 여기서 필요한 낱말은 "분리된"이 아니라 "별도의"이므로 `a separate tab` 이 맞습니다.
- 더 나은 표현: Also, pull `sequence_addressing` and `sequence_measurement` out of the 이미지 + 설정 tab into their own Sequence tab.
- 왜: `can be in ~` 은 가능성을 말할 뿐이라 지시로 읽히지 않습니다. `pull A out of B into C` 는 어디서 무엇을 빼 어디에 넣는지를 전치사 세 개로 다 말해 줍니다. `their own ~` 은 "따로 자기 자리를 준다"는 뉘앙스라 `a separate ~` 보다 의도가 잘 드러납니다.

### 카드 10 — 버그 신고와 확인 요청

- 내가 쓴 영어: "can you fix this for me. make sure db connected right."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: be동사가 빠졌습니다 → `make sure the DB is connected`. 동사를 꾸미므로 형용사 `right` 가 아니라 부사가 필요합니다 → `properly`.
- 더 나은 표현: Could you look into this? Please confirm the DB connection is actually working.
- 왜: 원인을 모르는 상태에서 `fix this` 는 진단을 건너뛰고 수정부터 시키는 말이 됩니다. `look into ~` 는 "들여다봐 달라"라서 조사 단계를 열어 둡니다. `make sure` 는 상대에게 책임을 지우는 어감이 있으니, 확인을 부탁하는 자리라면 `confirm` 이 부드럽고 결과도 같습니다.
