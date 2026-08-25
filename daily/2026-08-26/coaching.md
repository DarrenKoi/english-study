# 2026-08-26 — 코칭

## 한글→영어

### 카드 1 — 우선순위 규칙과 사본 정리 지시   (내가 쓴 한글)
- 내가 쓴 한글: "1. VT RTC Cubic은 pool과 함께 있을 때 pool보다 우선해. 2. 사본 어긋남도 고치자. 나중에 잘못될 수 있으니."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: 1. When VT/RTC/Cubic appears together with Pool, it takes precedence over Pool. 2. Let's fix the drifted copy too — it could bite us later.
- 왜 이렇게: "~보다 우선해"는 `takes precedence over` 가 룰 엔진 맥락에 맞는 정확한 동사구다(`wins over` 는 더 구어). "함께 있을 때"는 `co-occurs with` 도 되지만 `appears together with` 가 평이하다. "사본 어긋남"은 명사 그대로 옮기면 어색하니 `the drifted copy`(어긋난 사본) 로 사물을 주어에 두고, "나중에 잘못될 수 있으니"는 이유 접속사 없이 대시 뒤 `it could bite us later` 로 붙이면 지시문의 리듬이 산다.

### 카드 2 — 표기가 여러 가지라는 사실 전달   (내가 쓴 한글)
- 내가 쓴 한글: "VG는 여러가지 의미로 사용되고 있어. desc에 Vertical, VG, Vertical Gate 등등이 쓰일거야."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: "VG" shows up in several forms — the desc will use Vertical, VG, Vertical Gate, and so on.
- 왜 이렇게: 문맥상 "여러 의미"가 아니라 "여러 표기"라서 `several forms`/`several spellings` 로 옮겨야 뜻이 산다(`several meanings` 로 직역하면 어시스턴트가 실제로 그랬듯 "단독 VG 가 다른 뜻일 수 있다"로 읽는다). "쓰일 거야"는 추측이 아니라 예고라 `will use` 가 맞고, "등등"은 `and so on` 또는 `among others`.

### 카드 3 — 현행 유지 후 사무실에서 확인   (내가 쓴 한글)
- 내가 쓴 한글: "단독 VG 도 그대로 두고, 사무실에서 확인할게"   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: Leave bare "VG" as is too — I'll verify at the office.
- 왜 이렇게: "단독 VG"는 `bare VG`/`standalone VG`. "그대로 두고"는 `leave … as is` 가 관용구이고, "도"는 `too` 를 문장 끝에 둔다. "확인할게"는 약속이라 `I'll verify`/`I'll check` — 화자의 의지를 담는 `will` 축약형이 자연스럽다. 두 절은 쉼표 대신 대시로 끊으면 지시와 약속이 분리된다.

### 카드 4 — 순서 의존은 불변식이 아니다   (고급 한글 · 번역)
- 한글 원문: "그래서 지금까지 Pool cell 이 이겼던 건 로직이 아니라 `rules.py` 가 cell 을 꽂아 넣은 순서였습니다. 판정이 데이터 순서에 의존하면 그건 불변식이 아니라 우연입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: So what made the Pool cell win until now wasn't logic — it was the order in which `rules.py` inserted the cells. A verdict that depends on data order isn't an invariant; it's a coincidence.
- 번역 포인트: "이겼던 건 ~였습니다"는 분열문 `what made X win … wasn't A — it was B` 로 옮기면 한국어의 초점이 그대로 산다. "꽂아 넣은 순서"는 관계절 `the order in which … inserted` — `the inserting order` 같은 명사 압축은 부자연스럽다. 둘째 문장은 조건절 대신 관계절 주어 `A verdict that depends on …` 으로 세우고, `isn't A; it's B` 세미콜론 대비로 단정을 살린다.

### 카드 5 — 같은 이름, 두 가지 뜻   (고급 한글 · 번역)
- 한글 원문: "같은 이름의 필드가 두 뜻을 가지면 어떤 동기화도 안전하지 않습니다. 사본을 맞추는 게 아니라 지운 게 맞았던 이유입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: When one field name carries two meanings, no amount of syncing is safe. That's why deleting the copy — rather than reconciling it — was the right call.
- 번역 포인트: "어떤 동기화도 안전하지 않다"는 `no amount of syncing is safe` — `no amount of` 가 "아무리 해도"의 전면 부정을 맡는다. "맞추는 게 아니라 지운 게 맞았다"는 동명사 주어 `deleting the copy` 에 삽입구 `rather than reconciling it` 을 끼우고 `was the right call` 로 닫으면 판단의 무게가 실린다.

### 카드 6 — 실행 0회의 경고   (고급 한글 · 번역)
- 한글 원문: "테스트가 3500개 통과해도, 겹치는 문자열이 생성되지 않으면 그 코드 경로는 집에서 0회 실행됩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87)
- 자연스러운 영어: Even with 3,500 tests passing, if the overlapping string is never generated, that code path runs zero times at home.
- 번역 포인트: "~해도"는 `even with + 명사구` 로 절을 줄이면 영어가 가볍다. "0회 실행됩니다"는 수동 `is executed zero times` 보다 자동사 `runs zero times` 가 자연스럽고, `zero` 를 숫자 그대로 두는 것이 `never runs` 보다 앞의 3,500 과 대구를 이룬다.

## 영어 다듬기

### 카드 7 — 데이터 수집 윈도 확대 요청
- 내가 쓴 영어: "in tttm, pm-tune pages, we have to enlarge the data gathering. 1 week window is too short. let's enlarge it to be 3 weeks."   (출처: transcript:[user] skewnono-v3-nuxt 4a1eae66)
- 정정: `1 week window` → `the 1-week window` (관사 + 복합 형용사 하이픈). `enlarge it to be 3 weeks` → `to be` 불필요: `widen it to 3 weeks`.
- 더 나은 표현: On the TTTM and PM-tune pages, we need to gather more data — a 1-week window is too short. Let's widen it to 3 weeks.
- 왜: 시간 범위에는 `enlarge`(면적·크기) 보다 `widen`/`extend` 를 쓴다. "data gathering 을 키운다"는 동사 명사화라 `gather more data` 로 풀면 바로 읽힌다. 세 문장을 대시로 묶으면 "요청 → 이유 → 수치"가 한 호흡이 된다.

### 카드 8 — 다중 선택 요청
- 내가 쓴 영어: "in hardware page, the 장비 선택 (models) should be multi-selectible. now only single select."   (출처: transcript:[user] skewnono-v3-nuxt 88abf698)
- 정정: `multi-selectible` → `multi-selectable` (철자: select + -able). `in hardware page` → `on the hardware page`.
- 더 나은 표현: On the hardware page, the model chips in 장비 선택 should allow multi-select — right now it's single-select only.
- 왜: UI 요소는 `on the page`. 형용사 `selectable` 보다 `allow multi-select`/`support multi-select` 가 UI 명세에서 더 흔하다. "now only single select" 는 동사가 없으니 `right now it's single-select only` 로 채운다.

### 카드 9 — 컴포넌트 배치 변경 제안
- 내가 쓴 영어: "In the hardware page, we have tool selector in the left side. I think we have to move this component to be in the top component right below H/W 관리 status component so that we have more space to display 데일리 / 분기 component and data display. Can you manage the placement of components? as we move the tool selector component to the top and change the shape from vertical to the horizontal), we can show the models and based on the model selections, we may well see the tool lists."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 정정: `in the left side` → `on the left`. `we have tool selector` → `we have a tool selector` (관사). `from vertical to the horizontal)` → 닫는 괄호 짝이 없고 관사 불일치: `from vertical to horizontal`. `we may well see the tool lists` — `may well` 은 "아마 그럴 것이다"라는 추측이라 의도(보여 주자)와 다르다: `we can then show the tool list`.
- 더 나은 표현: On the hardware page, the tool selector sits on the left. I'd like to move it to the top, directly below the H/W 관리 status bar, so the 데일리/분기 tabs and the data area get more room. Could you rework the layout? Once the selector moves to the top and turns horizontal, it can show the models first, and the tool list can follow from the model selection.
- 왜: "have to" 는 의무라 제안에는 `I'd like to`/`let's` 가 맞다. `manage the placement` 는 어색해 `rework the layout`/`rearrange the components`. 조건은 `as we move` 보다 `once the selector moves` 가 "그렇게 한 뒤"의 순서를 살린다. "based on the model selections, we may well see" 는 `the tool list can follow from the model selection` — `follow from` 이 "선택에 따라 결정된다"를 담는다.

### 카드 10 — 모델을 고를 때까지 숨기기
- 내가 쓴 영어: "yes. until a model is picked. by doing so users are sure what models they are working on."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 정정: 첫 조각은 앞 질문("모델을 고르기 전에는 장비를 숨긴다?")의 답이라 동사가 생략됐는데, 문장으로 세우려면 `Yes — hide the tools until a model is picked.` `by doing so users are sure` → `that way, users know for sure`.
- 더 나은 표현: Yes — hide the tools until a model is picked. That way users always know which model they're working with.
- 왜: `by doing so` 는 격식 문어체라 짧은 채팅 답변엔 `that way` 가 자연스럽다. `are sure what models` 는 `know which model` 이 정확하다(`sure` 는 확신, `know` 는 인지). "working on" 은 작업 대상(문제·과제), 장비·모델을 다룰 땐 `working with`.

### 카드 11 — HV-SEM 도 같은 경로
- 내가 쓴 영어: "yes. HV-SEM also experience the same path."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 정정: `HV-SEM also experience` → 3인칭 단수: `experiences`. 다만 `experience a path` 는 연어가 어색하다: `goes through the same path` / `follows the same path`.
- 더 나은 표현: Yes — HV-SEM goes through the same path too.
- 왜: 경로·흐름은 `go through`/`follow`, `experience` 는 감정·사건에 쓴다. `also` 를 문장 끝 `too` 로 옮기면 구어 답변의 리듬이 된다.

### 카드 12 — 이미지 2×2 배치 요청
- 내가 쓴 영어: "in recipe-search/open, for the hv-sem case, we tend to display more images for the Measurement component. Right now, we may display 4 images in a row while Addresing image comes with only one. Since we display all four images in a single row, they look so compact. Can we display two images in a row so that we have 2 by 2 image intead of 1 by 4 images."   (출처: transcript:[user] skewnono-v3-nuxt a101dd54)
- 정정: `Addresing` → `Addressing`, `intead` → `instead` 오타. `we tend to display` — `tend to` 는 경향이고 여기선 사실이라 `we display`. `they look so compact` — `compact` 는 긍정적 어감(알차게 작은)이라 불만에는 `cramped`/`squeezed`. 물음표 누락.
- 더 나은 표현: In recipe-search/open, the HV-SEM case shows more images for the Measurement slot — four in a row, while Addressing has just one. With all four in a single row they look cramped. Could we show two per row, so we get a 2×2 grid instead of 1×4?
- 왜: "N images in a row" 를 두 번 반복하지 않고 `four in a row … two per row` 로 줄이면 대비가 선명하다. `2 by 2 image` 는 `a 2×2 grid` 처럼 격자 명사를 붙여야 한다. `so that we have` 는 `so we get` 이 회화체.

### 카드 13 — 다른 파일도 고칠 가치가 있는지 묻기
- 내가 쓴 영어: "worth fixing ImgThumb for CompareMatix.vuew too?"   (출처: transcript:[user] skewnono-v3-nuxt a101dd54)
- 정정: `CompareMatix.vuew` → `CompareMatrix.vue` 오타. 문장 구조 자체는 구어 생략문(`(Is it) worth fixing …?`)으로 자연스럽다.
- 더 나은 표현: Worth applying the same fix to `ImgThumb` in `CompareMatrix.vue` too?
- 왜: 원문의 `fixing ImgThumb for X` 는 "X 를 위해 ImgThumb 을 고친다"로 읽히는데, 뜻은 "X 안의 ImgThumb 에도 같은 수정을 적용한다"이다. `apply the same fix to A in B` 가 그 관계를 정확히 놓는다.

### 카드 14 — Pool 과 PV 가 함께 나올 때의 규칙
- 내가 쓴 영어: "for device-statistics, we have set the rules like TV, PV, Pool제. However, we have found that some special cases from the description like DRAM Pool제 (@Spica PV). In this case, we have both Pool and PV. In this case we have to follow Pool and ignore PV."   (출처: transcript:[user] skewnono-v3-nuxt a8bc1b87)
- 정정: `we have found that some special cases … like …` — `that` 절에 동사가 없다: `we've found some special cases in the description, like …` (`that` 삭제). `In this case` 가 연속 두 문장에 반복된다.
- 더 나은 표현: In device-statistics, we set rules by stage — TV, PV, Pool제. But some descriptions carry both, e.g. "DRAM Pool제 (@Spica PV)". When Pool and PV co-occur like that, Pool should win and PV should be ignored.
- 왜: `the rules like TV, PV` 는 무엇의 예시인지 불명해 `rules by stage — TV, PV, Pool제` 로 범주를 준다. 두 번의 `In this case` 는 `When … co-occur like that` 하나로 접는다. "follow Pool" 은 `Pool should win`/`Pool takes precedence` 가 룰 우선순위의 관용 표현이다.
