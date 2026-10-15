# 2026-10-16 — 코칭

## 한글→영어

### 카드 1 — 남이 보낸 검토 요청을 넘기기   (내가 쓴 한글)
- 내가 쓴 한글: "office agent가 몇 가지 수정사항 검토를 요청해왔어."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: The office agent sent over a few fixes it wants us to look at.
- 왜 이렇게: "요청해왔어"의 "-왔어"는 저쪽에서 이쪽으로 온 방향이라 `sent over` 가 딱 맞다. "수정사항 검토를 요청"을 명사로 직역하면(`requested a review of some modifications`) 무겁다. `fixes … it wants us to look at` 처럼 동사로 풀면 말이 된다.

### 카드 2 — 발견 경위를 머리말로   (내가 쓴 한글)
- 내가 쓴 한글: "device-statistics를 검토하다가 발견한 사항"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Issues found while reviewing device-statistics
- 왜 이렇게: 머리말은 명사구로 두면 된다. "~하다가"는 `while + -ing`. `found` 는 과거분사로 `Issues` 를 뒤에서 꾸민다(`Issues that were found` 의 축약).

### 카드 3 — 개선 요청의 제목   (내가 쓴 한글)
- 내가 쓴 한글: "하사정자 저장 필터가 원인인 '디바이스 안 보임' 진단성 개선 요청"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Request: make it easier to tell when a saved user filter is why a device isn't showing up
- 왜 이렇게: "진단성"은 영어에 딱 맞는 명사가 없다(`diagnosability` 는 어색하다). `make it easier to tell when …`(언제 그런지 알아보기 쉽게)로 풀면 뜻이 산다. "안 보임"은 `isn't showing up` 이 화면 맥락에서 가장 흔하다. 참고로 "하사정자"는 "사용자"의 오타로 보인다.

### 카드 4 — 데이터는 정상, 원인은 따로   (내가 쓴 한글)
- 내가 쓴 한글: "RX1A는 정상 데이터 확인. 하지만 안 보였던 원인은 useDeviceStatisticsPreference가 localStorage에 저장하는 필터였음."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: The RX1A data itself checks out. It was hidden by the filter that `useDeviceStatisticsPreference` saves to localStorage.
- 왜 이렇게: "정상 데이터 확인"은 `checks out`(확인해 보니 맞다)이 짧고 자연스럽다. "안 보였던 원인은 ~였음"은 `The reason it didn't show was …` 도 되지만, 수동태 `It was hidden by …` 로 쓰면 원인이 바로 행위자 자리에 온다.

### 카드 5 — 세션을 넘어 남는 필터   (내가 쓴 한글)
- 내가 쓴 한글: "selectedProdCategories RX1A는 prod_catg_cd="Advanced" 인데 DRAM/NAND 등을 골라두면 숨음 (세션 넘어 지속)."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: RX1A's `prod_catg_cd` is "Advanced", so if `selectedProdCategories` has DRAM/NAND picked, it gets hidden — and that sticks across sessions.
- 왜 이렇게: "골라두면"의 "-두면"은 선택이 남아 있는 상태라 `has … picked` 로 상태를 말한다. "세션 넘어 지속"은 구어로 `sticks across sessions`, 글로는 `persists across sessions` 다.

### 카드 6 — 순위가 밀려 경계에 걸림   (내가 쓴 한글)
- 내가 쓴 한글: "selectedLots 측정 상위 N - RX1A가 11->12위로 내려와 상위 10에 정확히 걸림."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: For the top-N-by-measurements filter, RX1A slipped from 11th to 12th, so it falls just outside the top 10.
- 왜 이렇게: 순위가 "내려오다"는 `slip` 이나 `drop` 이 자연스럽다. "정확히 걸림"은 경계 바로 밖이라는 뜻이니 `falls just outside the top 10` 으로 위치를 밝혀야 오해가 없다(`is caught by the top 10` 은 안에 든다는 뜻으로 읽힌다).

### 카드 7 — 표시 요청과 그 목적   (내가 쓴 한글)
- 내가 쓴 한글: "요청 - 필터가 저장되어 있을 때 저장된 필터 적용 중 표시 (배지) - 데이터 문제와 필터 문제 구분해야함."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Request: when a saved filter is active, show a "saved filter applied" badge, so users can tell a filter problem from a data problem.
- 왜 이렇게: "구분해야함"은 목적이라 `so users can tell A from B` 로 붙인다. `tell A from B` 는 "A 와 B 를 구별하다"의 구어 표준형이다. 문어라면 `distinguish A from B`.

### 카드 8 — 옵션 추가를 검토해 달라   (내가 쓴 한글)
- 내가 쓴 한글: "topN 옵션 (10/25/50)에 15 또는 20 추가 검토."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Consider adding 15 or 20 to the top-N options (10/25/50).
- 왜 이렇게: "추가 검토"는 `consider adding` 한 단어로 끝난다. `consider` 뒤에는 동명사(-ing)가 온다(`consider to add` 는 틀린다).

### 카드 9 — 잠복 버그를 한 줄로   (내가 쓴 한글)
- 내가 쓴 한글: "backend _lot_meta의 M-fab 우선 정책이 R3 lot의 prod_catg_cd를 마스킹 (잠복 버그성)"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: The M-fab-first rule in backend `_lot_meta` masks `prod_catg_cd` for R3 lots — a latent bug.
- 왜 이렇게: "잠복 버그"는 `latent bug` 가 정확한 짝이다. "~성"(그런 성격)은 굳이 옮기지 않거나 `a latent bug, more or less` 정도로 흐린다. "우선 정책"은 `X-first rule` 로 압축된다.

### 카드 10 — 덮어쓰는 동작을 설명   (내가 쓴 한글)
- 내가 쓴 한글: "office_example.py (office.py)의 _lot_meta는 겹치는 lot_cd에서 M-fab (device_desc) 행이 이겨 prod_catg_cd를 ""로 덮음. 두 카탈로그 교집합은 458개 lot."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: In `_lot_meta` (`office_example.py`, deployed as `office.py`), when a `lot_cd` appears in both catalogs, the M-fab (`device_desc`) row wins and overwrites `prod_catg_cd` with an empty string. The two catalogs overlap on 458 lots.
- 왜 이렇게: "행이 이겨"는 영어에서도 `wins` 를 그대로 쓴다(우선순위 충돌을 말할 때 흔하다). "교집합은 458개"는 `overlap on 458 lots` 가 수학 용어(`intersection`)보다 말로 자연스럽다.

### 카드 11 — 지금은 괜찮지만 위험한 경우   (내가 쓴 한글)
- 내가 쓴 한글: "현재 확인된 RX1A 원본 값도 "Advanced"라 피해가 없지만, DRAM/NAND 값을 가진 겹친 lot은 memory_class_auto가 unknow으로 떨어져 룰 셀이 미매칭 (Gray-A) 될 수 있음."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: RX1A's source value is "Advanced" anyway, so no harm done there. But for overlapping lots whose value is DRAM or NAND, `memory_class_auto` can fall back to `unknown`, leaving the rule cell unmatched (Gray-A).
- 왜 이렇게: "피해가 없지만"은 관용구 `no harm done` 이 딱 맞다. "~로 떨어져"는 기본값으로 빠진다는 뜻이라 `fall back to`. 뒤의 결과는 오늘 정독의 `leaving …` 분사구로 붙이면 한 문장에 담긴다. `unknow` 는 `unknown` 의 오타.

### 카드 12 — 우선순위 조정을 요청   (내가 쓴 한글)
- 내가 쓴 한글: "요청: fac_id가 R 계열인 lot은 R3 카탈로그 행이 이기도록 우선순위를 검토."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Request: please revisit the precedence so that for lots with an R-series `fac_id`, the R3 catalog row wins.
- 왜 이렇게: 이미 있는 규칙을 다시 보는 것이라 `review` 보다 `revisit` 이 정확하다. "우선순위"는 규칙 간 충돌이면 `precedence`, 작업 순서면 `priority` 다.

### 카드 13 — 빈 표 대신 이유를 보여 달라   (내가 쓴 한글)
- 내가 쓴 한글: "스텝 0건인 디바이스를 빈 표 대신 "planstep 자료 없음"으로 명시 - 원인이 파이프라인인지 원본 데이터인지 사용자가 구분 가능해야 함."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: For devices with zero steps, show "no planstep data" instead of an empty table, so users can tell whether the problem is in the pipeline or in the source data.
- 왜 이렇게: "명시"는 `explicitly state` 로 직역하기보다 `show "…"` 처럼 무엇을 보여 줄지 적는 편이 구체적이다. "~인지 ~인지 구분"은 `tell whether A or B`. 카드 7의 `tell A from B` 와 짝으로 익혀 두면 좋다.

### 카드 14 — 시간대 문제를 설명하고 감사를 부탁   (내가 쓴 한글)
- 내가 쓴 한글: "meas_hist 계열 timestamp는 kst 실제 시각이 naive로 적재돼 opensearch가 UTC로 해석. date-math now를 쓰는 코드가 있는 지 한번 감사해주세요."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: The `meas_hist` timestamps are stored as naive KST wall-clock times, so OpenSearch reads them as UTC. Could you audit whether any code uses date-math `now`?
- 왜 이렇게: "실제 시각"은 시계에 보이는 현지 시각이라 `wall-clock time` 이 정확한 용어다. "적재돼"는 `loaded` 보다 `stored`·`indexed` 가 OpenSearch 맥락에 맞다. "한번 ~해주세요"의 "한번"은 부드럽게 하는 말이라 `Could you …?` 로 충분하다.

### 카드 15 — 섞인 형식에 주의   (내가 쓴 한글)
- 내가 쓴 한글: "OS의 os_inserted도 naive(KST)와 +09:00 포멧이 섞여 있으니 이 필드로 정렬/필터한다면 주의해야함."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: `os_inserted` in OpenSearch also mixes naive (KST) values with `+09:00` ones, so be careful if anything sorts or filters on that field.
- 왜 이렇게: "~가 섞여 있다"는 필드를 주어로 `mixes A with B` 로 쓰면 짧다. "~로 정렬하다"는 `sort on a field`, `filter on a field` 처럼 전치사 `on` 을 쓴다. "포멧"은 "포맷"이 맞는 표기다.

### 카드 16 — 검토 후 바로 진행   (내가 쓴 한글)
- 내가 쓴 한글: "위 내용 검토해서 코드 수정 진행."   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Review the above and go ahead with the code changes.
- 왜 이렇게: "~해서 진행"은 `… and go ahead with …` 로 두 동작을 잇는다. `the above` 는 "위 내용"의 표준 표현이다.

### 카드 17 — 대신 해 달라, 나중에 다시   (내가 쓴 한글)
- 내가 쓴 한글: "그냥 너가 진행해줘. pi 문제 해결하고 나중에 해볼게"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Just go ahead and do it yourself. I'll sort out pi and try it later.
- 왜 이렇게: "너가 진행해줘"는 "pi 대신 네가"라는 뜻이라 `yourself` 가 그 대비를 살린다(실제로 어시스턴트도 이 문장을 "직접 리뷰하라"로 해석했다). "문제 해결하고"는 구어로 `sort out` 이 `fix` 보다 가볍다. 참고로 표준 표기는 "네가"다.

### 카드 18 — 짧은 지시 두 개   (내가 쓴 한글)
- 내가 쓴 한글: "개발 서버 두개 띄워" / "pi에게 다시 리뷰 요청해줘"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Bring both dev servers back up. / Ask pi for the review again.
- 왜 이렇게: "띄우다"는 `start` 도 되지만, 내려갔던 서버를 다시 올리는 상황이라 `bring … back up` 이 정확하다. "~에게 리뷰 요청"은 `ask X for a review`. `request a review to pi` 는 틀린 전치사다(`request … from`).

### 카드 19 — 정리해서 공지로   (내가 쓴 한글)
- 내가 쓴 한글: "이번 버그/수정 사항들을 정리해서 공지사항에 작성해줘"   (출처: transcript:[user] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Write up these bugs and fixes as a post on the notices page.
- 왜 이렇게: "정리해서 작성"은 `write up` 하나로 된다(어제의 `write up the changes` 와 같은 동사). "공지사항"은 페이지면 `the notices page`, 글 한 편이면 `an announcement`. 오늘 정독 단락 3이 이 공지를 영어로 옮긴 모범 단락이다.

### 카드 20 — 셀프 리뷰의 한계   (고급 한글 · 번역)
- 한글 원문: "다만 작성자가 자기 코드를 본 것이라 독립적인 리뷰는 아닙니다 — pi 리뷰는 여전히 받아볼 가치가 있습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: That said, this was the author reviewing their own code, so it isn't an independent review — a review from pi is still worth getting.
- 번역 포인트: "다만"은 앞 결론을 인정하고 단서를 다는 말이라 `That said,` 가 정확하다(`However` 보다 부드럽다). "~할 가치가 있다"는 `be worth + -ing`. 어제 코칭의 `worth of fixing` 같은 실수를 피하는 형태다.

### 카드 21 — 버그가 숨어 있던 이유   (고급 한글 · 번역)
- 한글 원문: "결과가 같아서 드러나지 않았고, DRAM/NAND 값을 가진 겹침 lot에서만 차이가 납니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: Because the outcome was the same either way, the bug never surfaced; it only makes a difference for overlapping lots whose value is DRAM or NAND.
- 번역 포인트: "드러나다"는 버그·문제에 쓰는 `surface`(수면 위로 올라오다)가 제격이다. "차이가 난다"는 `make a difference`. 두 절의 시점이 달라(과거 vs 지금도) 세미콜론으로 나누고 시제를 갈랐다.

### 카드 22 — 공지와 배포가 어긋나는 위험   (고급 한글 · 번역)
- 한글 원문: "이 파일의 원칙이 '공지는 설명하는 코드와 같은 배포에 나간다'이므로, 배포 전에 cp가 빠지면 5번 항목만 공지와 실제 동작이 어긋납니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/da5cd7a3)
- 자연스러운 영어: This file's rule is that a notice ships in the same release as the code it describes, so if the `cp` is skipped before deployment, item 5 will be the one place where the notice and the actual behaviour disagree.
- 번역 포인트: "배포에 나가다"는 `ship in a release` 가 개발 현장 말이다. "어긋나다"는 사람끼리 의견이 다를 때 쓰는 `disagree` 를 문서와 동작에 써서 생생하게 만든다(`be out of sync` 도 된다). "~만"은 `the one place where …` 로 범위를 좁혔다.
