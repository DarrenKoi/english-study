# 2026-07-04 — 코칭

오늘 배치에는 내가 직접 쓴 한국어가 없어(모든 메시지가 영어), 한글→영어는 (b) 고급 번역 정독만 싣는다.
대신 zoom-ladder 디버깅 대화에서 내가 쓴 영어가 많아 영어 다듬기가 풍성하다.

## 한글→영어

### 카드 1 — AI 티 제거 지시문   (고급 한글 · 번역)
- 한글 원문: "AI가 쓴 듯한 티(번역투, 기계적 병렬 구조, 균일한 문장 리듬, 과한 불릿·굵은 글씨 남발, 상투적 접속)를 제거해 사람이 쓴 자연스러운 보고서로 윤문하세요."   (출처: transcript:[assistant] 윤문 에이전트 지시)
- 자연스러운 영어: "Remove the telltale signs of AI writing — translationese, mechanical parallelism, uniform sentence rhythm, overused bullets and bold, formulaic connectives — and polish it into a report that reads as if a person wrote it."
- 번역 포인트: "티"는 `telltale signs`(정체를 드러내는 흔적)가 정확한 짝. "남발"은 `overused` 한 단어로 흡수하고, "사람이 쓴 듯한"은 `reads as if a person wrote it`(read 자동사 + as if 가정법)로 옮기면 자연스럽다. 긴 괄호 나열은 영어에서 대시(—)로 감싸는 편이 읽기 좋다.

### 카드 2 — 윤문 결과 보고   (고급 한글 · 번역)
- 한글 원문: "번역투와 기계적 병렬을 자연스럽게 풀되 수치와 고유명사는 한 글자도 건드리지 않았습니다."   (출처: transcript:[assistant] 윤문 완료 보고)
- 자연스러운 영어: "I smoothed out the translationese and mechanical parallelism while leaving every figure and proper noun untouched — not a single character changed."
- 번역 포인트: "풀되"의 양보·대조는 `while + -ing` 로 한 문장에 담는다. "한 글자도 건드리지 않다"는 `not a single character changed` 를 대시 뒤에 얹어 강조 — 영어도 부정 강조는 뒤로 뺄 때 힘이 실린다. `smooth out`(매끄럽게 펴다)은 윤문에 딱 맞는 구동사.

### 카드 3 — 뉘앙스 보존 보고   (고급 한글 · 번역)
- 한글 원문: "CCTV의 '가능성만 확인한 채 추가 평가는 중단' 한계 뉘앙스와 의미·순서·인과관계를 그대로 보존했습니다."   (출처: transcript:[assistant] 윤문 완료 보고)
- 자연스러운 영어: "I preserved the meaning, ordering, and causal links intact, including the nuanced caveat that the CCTV work only confirmed feasibility and was then set aside without further evaluation."
- 번역 포인트: "~한 채 중단"은 영어에서 `only confirmed X and was then set aside`(확인만 하고 이후 보류됨)처럼 시간 순서를 풀어 쓰는 게 자연스럽다. "한계 뉘앙스"는 `the nuanced caveat that ...` 동격절로 — caveat(단서·유보)이 "한계 서술"의 격식 있는 대응어다.

## 영어 다듬기

### 카드 1 — align point 불확실 상황 질문
- 내가 쓴 영어: "When align fail occurs and download rcp/msr images and consensus images, we do not sure which one is align point (= low score), in that case, can we do go furture?"   (출처: transcript:[user])
- 정정: ① `we do not sure` → **`we are not sure`** (sure 는 형용사라 be 동사 필요; do 부정은 동사에만). ② `can we do go furture` → **`can we go further`** (조동사 뒤 동사원형 하나만; further 철자). ③ `When align fail occurs and download ...` — 주어가 사라진 병렬: **`When an align fail occurs and we've downloaded ...`**.
- 더 나은 표현: "When an align fail occurs and we've already downloaded the rcp/msr and consensus images but still can't tell which point is the align point (the score is low), can we go a step further?"
- 왜: `can't tell which ...`(구별이 안 된다)이 `not sure` 보다 상황을 정확히 말하고, `go a step further` 는 "한 단계 더 나아가다"로 자연스러운 요청 어투가 된다. 괄호 `(= low score)` 는 영어에선 절로 풀어주는 게 읽기 좋다.

### 카드 2 — pm_crop 이미지 불필요 통보
- 내가 쓴 영어: "Now I do not need the pm_crop image as I found that the function works well. I do not need to see the result of the image anymore."   (출처: transcript:[user])
- 정정: 문법 오류 없음.
- 더 나은 표현: "I no longer need the pm_crop image — I've confirmed the function works well, so there's no need to inspect its output anymore."
- 왜: `no longer need` 가 `now I do not need` 보다 간결한 격식 표현. "확인했다"는 발견(found)보다 검증(confirmed)이 맥락에 맞고, 두 문장의 중복(`do not need` 반복)을 대시 + `so` 인과로 묶으면 한 호흡이 된다.

### 카드 3 — 휠 동작 불능 보고
- 내가 쓴 영어: "I think still the wheel action is not working (I do not see any images in captured_img_from_rcs."   (출처: transcript:[user])
- 정정: ① 부사 위치 — `I think still the wheel action is not working` → **`I think the wheel action is still not working`** (still 은 be/조동사 뒤, 일반동사 앞). ② 여는 괄호만 있고 닫는 괄호가 없음.
- 더 나은 표현: "The wheel action still doesn't seem to be working — I don't see any images in captured_img_from_rcs."
- 왜: `doesn't seem to be working` 은 단정 대신 관찰 기반 추정으로, `I think` 를 문법적으로 흡수한다. 증거(이미지 없음)는 괄호보다 대시로 잇는 편이 보고 문장답다.

### 카드 4 — 줌 인·아웃 필요성 주장
- 내가 쓴 영어: "we have to zoom in and out to find the align key and its correct point. (only zoom out method is not enough eventaully)"   (출처: transcript:[user])
- 정정: ① `eventaully` → **`eventually`** (철자). ② `only zoom out method` → **`the zoom-out method alone`** (only 를 명사구 앞에 두면 "유일한 방법"으로 오독됨; alone 후치가 "그것만으로는"을 정확히 표현).
- 더 나은 표현: "We need to zoom both in and out to find the align key and pin down its exact point — zooming out alone won't be enough in the end."
- 왜: `both in and out` 이 양방향을 명시하고, `pin down`(정확히 짚어내다)이 "correct point 찾기"의 관용 짝이다. `won't be enough in the end` 는 "eventually not enough"의 자연스러운 어순.

### 카드 5 — 커서 위치 보장 요구
- 내가 쓴 영어: "make sure move mouse cursor inside the live sem box and apply wheel action."   (출처: transcript:[user])
- 정정: `make sure move ...` → **`make sure to move ...`** 또는 **`make sure the cursor is inside ...`** (make sure 뒤에는 to부정사나 that절; 동사원형 직결 불가).
- 더 나은 표현: "Make sure the mouse cursor is actually inside the live SEM box before applying the wheel action."
- 왜: `make sure + that절` 이 "상태 보장"을 가장 정확히 요구하고, `actually` 가 "겉보기만 말고 실제로"라는 이번 버그의 핵심을 살린다. `before -ing` 로 순서 제약(이동 → 휠)을 문법으로 고정.

### 카드 6 — RCS 마우스 추적 가설
- 내가 쓴 영어: "maybe you have to move around the mouse pointer so that RCS can follow your mouse movement."   (출처: transcript:[user])
- 정정: 문법 오류 없음 (`move around the mouse pointer` 는 `move the mouse pointer around` 가 더 자연스러운 어순).
- 더 나은 표현: "You may need to move the pointer around gradually so that RCS can track the motion."
- 왜: `may need to` 가 `maybe you have to` 보다 부드러운 추정 제안. 짧은 대명사 목적어는 구동사 사이에 넣는 게 원어민 어순(`move it around`)이고, follow 보다 `track`(연속적으로 추적)이 이 기술 맥락의 정확한 동사다. 참고로 이 가설이 그대로 root cause 였다 — 표현만 다듬으면 완벽한 버그 리포트.

### 카드 7 — 마우스는 움직이는데 휠이 안 됨
- 내가 쓴 영어: "now I see mouse is moving! but the wheel up/down seems not working. no PM changes."   (출처: transcript:[user])
- 정정: ① `I see mouse is moving` → **`I see the mouse moving`** (관사 + 지각동사 see + 목적어 + -ing). ② `seems not working` → **`doesn't seem to be working`** (seem 의 부정은 조동사 쪽으로).
- 더 나은 표현: "The mouse is moving now! But wheel up/down doesn't seem to have any effect — the PM value never changes."
- 왜: `have any effect` 가 "동작은 가는데 결과가 없다"는 이 상황을 정확히 구별해 준다(작동 자체가 아니라 효과의 문제). `never changes` 는 반복 관찰을 담아 `no PM changes` 보다 증거력이 세다.

### 카드 8 — 휠 대신 더블클릭 의심
- 내가 쓴 영어: "instead of zoom out, it rather goes double click different posision? (maybe by accident?)"   (출처: transcript:[user])
- 정정: ① `instead of zoom out` → **`instead of zooming out`** (전치사 of 뒤 동명사). ② `goes double click different posision` → **`it double-clicks at a different position`** (double-click 을 동사로; 장소 전치사 at; position 철자).
- 더 나은 표현: "Instead of zooming out, it seems to double-click at a different position — possibly by accident?"
- 왜: `seems to` 로 관찰 불확실성을 담고, `possibly by accident?` 가 `maybe by accident?` 보다 문어에서 자연스럽다. 이런 "예상 동작 대신 실제 동작" 보고는 `Instead of X-ing, it Y-s` 프레임을 그대로 외워두면 좋다.

### 카드 9 — 드롭다운 위치 + 2단계 VLM 요구
- 내가 쓴 영어: "the drop down will be show up right beneath the PM button. Also we have to use two steps (what we have done with the vlms) to get the right pm button position. the one vlm method is not working well."   (출처: transcript:[user])
- 정정: ① `will be show up` → **`will show up`** (show up 은 자동사; be 불필요). ② `(what we have done with the vlms)` → **`(the two-stage approach we've been using with the VLMs)`** (what 절보다 명사구 동격이 명확). ③ `the one vlm method` → **`the single-VLM method`**.
- 더 나은 표현: "The dropdown shows up right beneath the PM button. Also, we should locate the PM button with the two-stage VLM approach we've been using — the single-pass method isn't working well."
- 왜: UI 의 일반적 동작은 미래형보다 현재형(shows up)이 관례. `two-stage` / `single-pass` 는 이 코드베이스가 실제로 쓰는 용어라(coarse→refine), 내 문장에 그대로 얹으면 의사소통 비용이 준다.
