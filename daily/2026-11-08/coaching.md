# 2026-11-08 — 코칭

오늘 한국어 메시지는 대부분 사무실 에이전트 회신을 메모처럼 줄여 옮긴 글입니다. 명사형 종결("누락됨", "고치기 쉬움")이 많은데, 영어로 옮길 때는 주어와 동사를 되살려 완전한 문장으로 쓰는 연습을 합니다. 어시스턴트 메시지는 모두 영어라 오늘은 고급 한글 번역 카드가 없습니다.

## 한글→영어

### 카드 1 — 규칙에서 빠진 항목   (내가 쓴 한글)
- 내가 쓴 한글: "R1: A 단 CD_HV/CD2_HV/CD3_HV 53이 규칙 F에서 누락됨."   (출처: transcript:[user] skewnono e6aa6018, 2차 회신)
- 자연스러운 영어: R1: A, except that rule F misses the 53 steps named CD_HV, CD2_HV or CD3_HV.
- 왜 이렇게: "단"은 `except that` 이나 `but` 으로 받습니다. "누락됨"은 수동 `are missing from rule F` 도 되지만, 규칙을 주어로 세운 `rule F misses` 가 더 짧고 능동입니다. 숫자 뒤에는 무엇을 셌는지(`steps`)를 꼭 붙입니다.

### 카드 2 — 대표를 고르면 안 되는 이유   (내가 쓴 한글)
- 내가 쓴 한글: "R2: B 같은 recipe, version에 파라미터 다른 경우 40건. 33건은 fab마다 하나로 정해짐. eqp_id로 대표 고르면 안됨. 배열이고 94.5%가 IP 주소."   (출처: transcript:[user] skewnono e6aa6018, 2차 회신)
- 자연스러운 영어: R2: B. There are 40 cases where the same recipe and version have different parameters. In 33 of them, each fab has exactly one set. Don't pick the representative by `eqp_id`: it's an array, and 94.5% of its values are IP addresses.
- 왜 이렇게: "~인 경우 N건"은 `There are N cases where ...` 가 정석입니다. "하나로 정해짐"은 `is settled` 보다 `each fab has exactly one set` 처럼 구체적으로 풀면 오해가 없습니다. 금지 이유는 콜론 뒤에 붙여 한 문장으로 묶습니다.

### 카드 3 — 덮는 비율 비교   (내가 쓴 한글)
- 내가 쓴 한글: "R4: B. CD-SEM 접두사 규칙은 5.68%만 덮음. 이름 안 토큰(EX>ED/EDGE>WF>LV)으로 41.1%. EDGE_EX를 EDGE보다 먼저 판정해야함."   (출처: transcript:[user] skewnono e6aa6018, 2차 회신)
- 자연스러운 영어: R4: B. The CD-SEM prefix rule covers only 5.68%. Matching tokens inside the name (EX > ED/EDGE > WF > LV) covers 41.1%. EDGE_EX has to be checked before EDGE.
- 왜 이렇게: "덮다"는 `cover` 가 그대로 통합니다. "~만"은 `only` 를 동사 앞에 둡니다. "판정하다"는 `judge` 가 아니라 `check`/`test` 가 코드 맥락에 맞습니다.

### 카드 4 — 같은 버그, 쉬운 수정   (내가 쓴 한글)
- 내가 쓴 한글: "CD-SEM 경로 3곳이 같은 버그. LOT_HIST_TIME_F, PROD_ID_SUFFIX, skip_yn "세 값' 주석. office.py 상수 하나씩이라 고치기 쉬움."   (출처: transcript:[user] skewnono e6aa6018, 2차 회신)
- 자연스러운 영어: Three places in the CD-SEM path have the same kind of bug: `LOT_HIST_TIME_F`, `PROD_ID_SUFFIX`, and the "three values" comment on skip_yn. Each is a single constant in office.py, so they're easy to fix.
- 왜 이렇게: "~라서 쉬움"은 `Each is ..., so they're easy to fix.` 로 이유 → 결과 순서를 지킵니다. 목록은 콜론으로 이어 붙이면 됩니다. 원문 따옴표("세 값')의 짝이 안 맞는 것도 함께 고칩니다.

### 카드 5 — 섞여 있어서 사라진다   (내가 쓴 한글)
- 내가 쓴 한글: "R4 device가 계열 index에 섞여 있음. fac_id로 R3만 고르면 R7QA/R7QC 두 device가 표 A에서 사라짐."   (출처: transcript:[user] skewnono e6aa6018, 2차 회신)
- 자연스러운 영어: The family indexes also contain R4 devices. If you filter to R3 by `fac_id`, two devices, R7QA and R7QC, drop out of table A.
- 왜 이렇게: "섞여 있다"를 `are mixed in` 으로 직역해도 되지만 `also contain` 이 더 담백합니다. "사라지다"는 `disappear` 보다 `drop out of` 가 필터링 결과에 잘 맞는 구동사입니다.

### 카드 6 — 에러 없이 전 기간이 통과   (내가 쓴 한글)
- 내가 쓴 한글: "S1. dt.keyword 하한 "2026-11-04"는 dt 값 (20260518)보다 작아서 매칭이 안됩니다. … 에러 없이 전 기간이 통과합니다. lte로는 반대로 0건. 90일 창을 걸었다고 믿으면서 2022년까지 읽는 상태라 옛 oper_det_desc가 섞입니다."   (출처: transcript:[user] skewnono e6aa6018, 3차 회신)
- 자연스러운 영어: S1: The `dt.keyword` lower bound "2026-11-04" sorts below every `dt` value (e.g. 20260518), so it doesn't filter anything. Every period passes, with no error. With `lte` it's the opposite: zero hits. We think a 90-day window is in place, but we're actually reading back to 2022, so old `oper_det_desc` values get mixed in.
- 왜 이렇게: 문자열 비교에서 "작다"는 `sorts below` 가 정확합니다(`is smaller` 는 숫자처럼 들림). "매칭이 안 된다"는 실제 결과가 "아무것도 거르지 못한다"이므로 `doesn't filter anything` 으로 뜻을 살립니다. "~라고 믿으면서 실은 ~"는 `We think ..., but we're actually ...` 대비 구문으로 받습니다.

### 카드 7 — 해결책 지시   (내가 쓴 한글)
- 내가 쓴 한글: "하한을 strftime("%Y%m%d")로. 지금은 창이 사라져 전 기간을 읽습니다."   (출처: transcript:[user] skewnono e6aa6018, 3차 회신)
- 자연스러운 영어: Format the lower bound with `strftime("%Y%m%d")`. Right now the window is gone, so it reads the whole history.
- 왜 이렇게: "~로."로 끝나는 지시는 동사 명령문(`Format ...`, `Use ...`)으로 완성합니다. "전 기간"은 `the whole period` 보다 `the whole history` 가 인덱스 맥락에 자연스럽습니다.

### 카드 8 — 날짜 계산을 직접   (내가 쓴 한글)
- 내가 쓴 한글: "S12 _office_meas_hist.py 60일 창. now-60d date math 못 쓰니 날짜 계산해 %Y%m%d."   (출처: transcript:[user] skewnono e6aa6018, 3차 회신)
- 자연스러운 영어: S12: `_office_meas_hist.py` uses a 60-day window. Since `now-60d` date math doesn't work on this field, compute the date yourself and format it as `%Y%m%d`.
- 왜 이렇게: "못 쓰니"는 이유 `Since ...` 로 앞에 둡니다. 왜 못 쓰는지(text 필드라서)를 `on this field` 로 살짝 넣으면 읽는 사람이 덜 헷갈립니다.

### 카드 9 — 회신 전달   (내가 쓴 한글)
- 내가 쓴 한글: "여기 회신." / "회신이 왔다."   (출처: transcript:[user] skewnono e6aa6018, 4차·5차 회신)
- 자연스러운 영어: Here's the reply. / The reply is in.
- 왜 이렇게: `The reply came.` 은 어색합니다. 결과물이 도착했다는 말은 `is in`(`The results are in.`)이 관용입니다. `Here's the office's reply.` 처럼 누구 회신인지 붙이면 더 분명합니다.

### 카드 10 — 정정과 확인   (내가 쓴 한글)
- 내가 쓴 한글: "T4가 틀렸습니다. 3차 S3의 가장 최근 문서는 version이 아니라 modified 였습니다. T2는 A가 맞습니다. V4는 두 기준으로 답했습니다. R3 all이 모호했습니다."   (출처: transcript:[user] skewnono e6aa6018, 4차 회신)
- 자연스러운 영어: T4 was wrong: in round 3's S3, "newest document" meant newest `modified`, not highest `version`. A is correct for T2. I answered V4 two ways because "R3 all" was ambiguous.
- 왜 이렇게: "A가 아니라 B"는 `B, not A` 순서로 뒤집는 게 영어답습니다. 마지막 두 문장은 원인-결과 관계라 `because` 로 한 문장에 묶었습니다.

### 카드 11 — 서술 정정과 새 발견   (내가 쓴 한글)
- 내가 쓴 한글: "3차 서술 정정 -cd의 R4 전용 device는 0개입니다. 새 발견 R7QA/R7QC의 fab이 두 index에서 어긋납니다. 표 A det_fac_id는 R4, 표 D fac_id는 R3, fac_id료 A <->D를 조인하면 같은 device가 두 fab으로 갈립니다."   (출처: transcript:[user] skewnono e6aa6018, 4차 회신)
- 자연스러운 영어: Correction to round 3: `-cd` has no R4-only devices. New finding: R7QA and R7QC have different fabs in the two indexes. Table A's `det_fac_id` is R4, but table D's `fac_id` is R3, so joining A and D on `fac_id` splits the same device across two fabs.
- 왜 이렇게: "어긋나다"는 `mismatch` 도 되지만 `have different fabs` 처럼 무엇이 다른지 풀어 주면 더 정확합니다. "갈리다"는 `splits ... across` 가 딱 맞습니다. 오타 "fac_id료"는 "fac_id로"입니다.

### 카드 12 — 정확 일치는 일부만   (내가 쓴 한글)
- 내가 쓴 한글: "U1: A (HV-SEM 한정 - -hv recipe 1449 중 575 exact. Verity/Provision은 hvsem_idp_ver 매칭 0. Verity/Provision은 별도 만들어야 함."   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: U1: A, but only for HV-SEM: 575 of the 1,449 `-hv` recipes match exactly. Verity and Provision have zero matches in `hvsem_idp_ver`, so they need their own source.
- 왜 이렇게: "~ 한정"은 `only for ...` 로 받습니다. "N 중 M"은 `M of the N ...` 입니다. "별도 만들어야 함"은 무엇을 만드는지 밝혀 `need their own source` 로 씁니다.

### 카드 13 — 9시간 밀린다   (내가 쓴 한글)
- 내가 쓴 한글: "U3: A (단 modified는 mapping data라 range 질의가 9시간 밀림)"   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: U3: A, but `modified` is stored as mapping data, so range queries are off by nine hours.
- 왜 이렇게: 시간 차이로 "밀린다"는 `are off by N hours` 가 관용입니다. `shift` 도 되지만 `off by` 가 "어긋났다"를 더 정확히 말합니다.

### 카드 14 — 원인과 범위 넓히기   (내가 쓴 한글)
- 내가 쓴 한글: "U4: B - 같은 (recipe,fac_id,modified) 그룹 5614 / 문서 11228. 원인은 fab_name 누락, writer doc_id키로 넓히면 8그룹만 남음"   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: U4: B. There are 5,614 groups with the same (recipe, fac_id, modified), covering 11,228 documents. The cause is the missing `fab_name`: if you widen the key to the writer's doc_id, only 8 groups remain.
- 왜 이렇게: "원인은 ~ 누락"은 `The cause is the missing X` 로 형용사 `missing` 을 앞에 붙입니다. "키로 넓히면"은 `widen the key to ...` 가 자연스럽습니다.

### 카드 15 — 가정과 크게 어긋남   (내가 쓴 한글)
- 내가 쓴 한글: "W1: Y 86.98 / 71.52 / 93.56% (mock 15% 가정과 크게 어긋남)"   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: W1: Y is 86.98% / 71.52% / 93.56%, far from the mock's assumed 15%.
- 왜 이렇게: "~와 크게 어긋남"은 `far from ...` 두 단어면 충분합니다. 격식을 높이면 `well off the mock's 15% assumption` 입니다.

### 카드 16 — 계약에 단위를 고정   (내가 쓴 한글)
- 내가 쓴 한글: "표 B에 fab_name을 넣을 것 (full_name, fac_id)로 묶으면 5606그룹이 ite 만 다른 채 뭉침. total_recipe 단위를 계약 주석에 고정 : device 행 단위 (합계 17974), 화면 합계 18794 아님."   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: Add `fab_name` to table B. Grouping by (full_name, fac_id) lumps 5,606 groups together that differ only in `ite`. Pin the unit of `total_recipe` in the contract comment: it's per device row (sum 17,974), not the on-screen total of 18,794.
- 왜 이렇게: "~할 것"은 명령문으로 바꿉니다. "~만 다른 채 뭉침"은 `lumps ... together that differ only in ...` 로 관계절을 뒤에 붙입니다. "고정하다"는 `fix` 보다 `pin` 이 문서·버전 맥락에서 자연스럽습니다.

### 카드 17 — lot_cd 로만 이어진다   (내가 쓴 한글)
- 내가 쓴 한글: "M fab 장비는 어떤 planstep 계열 index에도 없음. 그래서 표 A <-> 표 D는 device로 안 이어지고 lot_cd 로만 이어짐 - 4차 결졍 재확인"   (출처: transcript:[user] skewnono e6aa6018, 5차 회신)
- 자연스러운 영어: M-fab tools aren't in any planstep family index, so tables A and D can't be linked by device, only by `lot_cd`. This reconfirms the round-4 decision.
- 왜 이렇게: "어떤 ~에도 없다"는 `aren't in any ...` 입니다. "A가 아니라 B로만"은 `not by A, only by B` 또는 `can't ... by A, only by B` 로 대비시킵니다. 오타 "결졍"은 "결정"입니다.

### 카드 18 — 합성 불필요   (내가 쓴 한글)
- 내가 쓴 한글: "1. Table A의 fab은 det_fac_id이고, 그 값은 sem_list.fab_name (툴의 위치)입니다. planstep index에는 fab_name 필드가 없습니다. … sem_list 조인 없이 det_fac_id 그대로 써도 됨."   (출처: transcript:[user] skewnono e6aa6018, 6차 회신)
- 자연스러운 영어: 1. Table A's fab is `det_fac_id`, and its value is `sem_list.fab_name`, the tool's location. The planstep index has no `fab_name` field. … You can use `det_fac_id` directly, with no join to sem_list.
- 왜 이렇게: 괄호 설명 "(툴의 위치)"는 영어에서 쉼표 뒤 **동격** `, the tool's location` 으로 넣는 게 자연스럽습니다. "그대로 써도 됨"은 `You can use ... directly` 또는 `as-is` 로 받습니다.

## 영어 다듬기

### 카드 1 — 질문지 요청
- 내가 쓴 영어: "give me the question sheet that I can hand to the office agent."   (출처: transcript:[user] skewnono e6aa6018)
- 더 나은 표현: "Can you write up a question sheet I can hand to the office agent?"
- 왜: 문법 오류는 없습니다. `that` 은 목적격 관계대명사라 빼면 구어답게 가벼워집니다. 아직 없는 질문지를 만들어 달라는 뜻이라 `give me` 보다 `write up` 이 정확하고, `the` 대신 `a` 가 맞습니다(특정한 기존 질문지가 아님). 문장 첫 글자는 대문자로 씁니다.

### 카드 2 — 몇 번째 질문지
- 내가 쓴 영어: "give me the 4th question sheet for the office agent" / "give me the 5th question sheet for the office agent"   (출처: transcript:[user] skewnono e6aa6018)
- 더 나은 표현: "Next, the fourth question sheet for the office agent, please."
- 왜: 오류는 없습니다. 반복 요청이라면 `Next,` 로 흐름을 잇고 명령문을 명사구 + `please` 로 줄여도 자연스럽습니다. 글에서는 `4th` 보다 `fourth` 처럼 서수를 풀어 쓰는 편이 깔끔합니다.

### 카드 3 — 회신 전달
- 내가 쓴 영어: "here is the reply from the office agent."   (출처: transcript:[user] skewnono e6aa6018)
- 더 나은 표현: "Here's the office agent's reply."
- 왜: 오류는 없습니다. `the reply from X` 를 소유격 `X's reply` 로 바꾸면 짧아지고, 구어에서는 `Here's` 축약이 자연스럽습니다. 첫 글자는 대문자로 씁니다.

### 카드 4 — 무엇을 쓰고 무엇을 안 쓰는지
- 내가 쓴 영어: "we do not use fac_id mostly, fab_name or det_fac_id from the datatables."   (출처: transcript:[user] skewnono e6aa6018)
- 정정: `mostly` 가 `not` 뒤에 붙어 "대체로 안 쓴다"인지 "주로 쓰는 건 다른 것"인지 흐립니다. 부정 범위를 분명히 하려면 대비 구문을 씁니다. 쉼표 하나로 "안 쓰는 것"과 "쓰는 것"을 잇는 것도 콤마 스플라이스에 가깝습니다.
- 더 나은 표현: "We mostly don't use `fac_id`; we use `fab_name` or `det_fac_id` from the datatables instead."
- 왜: `mostly` 를 `don't` 앞에 두면 "대체로 쓰지 않는다"로 뜻이 고정됩니다. 세미콜론과 `instead` 로 대안을 따로 세우면 읽는 사람이 어느 쪽이 쓰는 필드인지 바로 압니다. 더 짧게는 "We use `fab_name` or `det_fac_id`, not `fac_id`." 도 좋습니다.
