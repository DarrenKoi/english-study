# 2026-09-30 — 새 표현

> 오늘 배치는 repo 문서 7건과 transcript 3건이다. 영어 문서는 skewnono 의 사무실 LLM 용 브리프 두 편(`hardware_field_usage.md`, `hardware_fdc_fleet_verification.md`)뿐이고 나머지는 한국어 인계 문서·데이터 표 메모·Codex 협의 brief 라 표현 소스에서 뺐다. transcript 는 CEO 시연 영상(RCS 순찰 데모, Align Fail 녹화, 영상 다듬기) 세션이 거의 전부이고, equipment-data-map 의 사무실 인계 문서 작성이 짧게 붙었다. `A gap is useful; a guess dressed as a finding is not.`, `Report numbers, not rows.`, `character for character`, `It shows as an empty chart, not an error.`, `One catch: …`, `disregard it, no action needed` 는 노트에 이미 있어서 제외.

## "Where this brief and those files disagree, report it."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 문서 여러 개를 함께 넘기면서 서로 어긋나는 곳을 찾으면 알려 달라고 할 때(작업 지시서, 격식).
- 한국어: 이 브리프와 그 파일들이 서로 다른 곳이 있으면 보고하라.
- 설명: 문두의 `Where` 는 장소가 아니라 "~하는 경우에는(in cases where)"이다. `If` 보다 "그런 지점이 여러 군데일 수 있다"는 느낌이 강하다. 뒤의 `it` 은 어긋남 자체를 받는다. 두 출처 중 어느 쪽이 옳은지 판정하라는 게 아니라 차이를 드러내라는 지시라서 짧게 끝난다.
- 예문: The schema background lives in the `hardware_*.txt` files. Where this brief and those files disagree, report it.
- 유사어: Flag any discrepancies between the two. (격식, `flag` = 표시해 알리다), If they don't match, tell me. (구어), Note any inconsistencies you find. (보고서체)
- 반의어: treat this brief as authoritative (이 브리프를 기준으로 삼아라)

## "The only trace is …"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 조용히 일어나는 문제의 흔적이 거의 없다는 걸 알려 줄 때(장애 진단 문서, 기술).
- 한국어: 남는 흔적이라고는 … 뿐이다.
- 설명: `trace` 는 "지나간 자국". `the only` 를 붙여 "그것 말고는 알아챌 길이 없다"를 강조한다. 원문은 `office.py` 가 없으면 mock 데이터를 조용히 내보내는데, 서버 로그의 INFO 한 줄 외엔 아무 표시가 없다는 경고였다.
- 예문: A tab without `office.py` silently serves mock data. The only trace is one INFO line in the server log.
- 유사어: The only sign of it is … (평이), All it leaves behind is … (구어, 약간 문학적), The sole indication is … (격식)
- 반의어: It fails loudly. (요란하게 실패해서 바로 보인다)

## "Keep these two apart when you diagnose."
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 비슷해 보이지만 원인이 다른 두 증상을 섞지 말라고 당부할 때(진단 가이드, 격식 중간).
- 한국어: 진단할 때 이 둘을 구분해서 다뤄라.
- 설명: `keep A and B apart` 는 "둘을 떼어 두다", 곧 혼동하지 말라는 뜻이다. `distinguish` 보다 손에 잡히는 표현이다. 원문은 이 문장 아래에 **Raise**(탭 전체가 빨간 오류)와 **Silent**(빈 차트) 두 실패 모양을 나란히 적었다.
- 예문: Failure styles come in two kinds. Keep these two apart when you diagnose.
- 유사어: don't mix these up (구어), tell these two apart (구분해 내다, 평이), treat these as distinct cases (격식)
- 반의어: lump them together (한데 뭉뚱그리다)

## "Hitting the cap raises instead of truncating."
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 한도에 닿았을 때 결과를 몰래 자르지 않고 오류를 낸다는 설계를 설명할 때(기술 문서).
- 한국어: 상한에 닿으면 잘라 내지 않고 예외를 던진다.
- 설명: 동명사 주어 `Hitting the cap` 이 조건 역할을 한다(= If a query hits the cap). `raise` 는 Python 에서 예외를 던지는 동사를 그대로 자동사로 썼다. `instead of truncating` 이 "조용히 잘라서 부분 결과를 주는" 대안을 명시적으로 부정한다. 부분 결과가 틀린 차트로 이어지느니 실패가 낫다는 설계 판단이 담겼다.
- 예문: Every OpenSearch pull is one request capped at 10,000 docs. Hitting the cap raises instead of truncating.
- 유사어: It errors out rather than returning partial results. (구어·기술), fail loudly instead of silently dropping data (설계 원칙), It refuses to truncate. (간결)
- 반의어: silently truncate (조용히 잘라 내다)

## "built from what the code accepts, not copied from real data"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 문서에 넣은 예시 데이터가 실제 값이 아니라고 미리 밝힐 때(기술 문서 주석).
- 한국어: 실제 데이터를 복사한 게 아니라 코드가 받아들이는 형태로 만든 것
- 설명: 과거분사 두 개 `built from` ↔ `copied from` 을 `not` 으로 대비했다. 예시를 곧이곧대로 믿지 말라는 경고다. 원문은 이어서 `IPs, ids and note text are illustrative.` 라고 덧붙였다. `illustrative` 는 "설명용, 예시일 뿐"이라는 격식 형용사다.
- 예문: The samples are built from what the code accepts, not copied from real data.
- 유사어: synthetic, not sampled from production (기술), made up to match the schema (구어), for illustration only (격식)
- 반의어: taken verbatim from production (운영 데이터 그대로)

## "That is the fastest way to …"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 방법을 지시한 뒤 왜 그 방법인지 한 줄로 설득할 때(문서·회의 모두).
- 한국어: 그게 …하는 가장 빠른 길이다.
- 설명: 명령문 다음에 `That is the fastest way to …` 를 붙이면 지시가 설득으로 바뀐다. `That` 은 바로 앞 문장 전체를 받는다. 단순하지만 지시문에 이유를 다는 습관을 들이기 좋은 틀이다.
- 예문: Put one real sample next to each block and diff them. That is the fastest way to find a `NAME`, `TYPE` or `VALUE` mismatch.
- 유사어: That's the quickest route to … (구어), This is the most efficient way to … (격식), Nothing beats it for … (구어, 강조)
- 반의어: That's the long way round. (돌아가는 길이다)

## "fetched, never read"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md
- 맥락: 가져오긴 하지만 실제로 쓰지 않는 필드를 표에서 짧게 표시할 때(기술 문서, 표 셀).
- 한국어: 가져오기만 하고 읽지는 않음
- 설명: 과거분사 둘을 쉼표로 이어 `A, never B` 로 대비했다. `not` 대신 `never` 를 써서 "어느 경로에서도 안 쓴다"로 강하다. 그래서 이 필드가 틀려도 화면에 영향이 없다는 결론이 따라 나온다(원문 표의 다음 칸이 `—`).
- 예문: `eqp_model_cd`, `fab_name` and `eqp_ip` are fetched, never read, so a mismatch there changes nothing on the page.
- 유사어: loaded but unused (평이), pulled in but ignored (구어), retrieved but not consumed (격식·기술)
- 반의어: load-bearing (결과를 좌우하는)

## "at the edge of"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 수치가 한계치에 거의 닿아 있어 조치가 필요하다고 말할 때(보고서, 격식 중간).
- 한국어: …의 한계선에 걸려 있는, 경계에 아슬아슬한
- 설명: 넘지는 않았지만 여유가 없다는 뜻. `close to` 보다 긴장감이 있다. 원문은 가장 바쁜 장비가 30일에 약 2.7k 건이라 기본값 약 3000 의 가장자리에 있으니 `precision_threshold` 를 40000 으로 올렸다는 문맥이다.
- 예문: Busiest tools log ~2.7k Contactpin docs per 30 days, at the edge of the ~3000 default, so the query now sets `precision_threshold` 40000.
- 유사어: right up against (구어), close to the limit (평이), bordering on (격식)
- 반의어: well within (한참 안쪽인)

## "stay … for good"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 어떤 상태가 일시적이지 않고 영영 그대로라고 말할 때(보고·구어 모두).
- 한국어: 영영 …인 채로 남다
- 설명: `for good` 은 "영구히(permanently)"의 구어적 표현. `good` 에 "좋은"이라는 뜻은 없다. 원문은 과도기에 쓰인 문서 약 6.8% 가 옛 코드로 먼저 기록돼 `_id` 가 잠긴 탓에 새 필드를 끝내 갖지 못한다는 설명이다. 곧바로 `no action needed` 로 이어 "영구적이지만 괜찮다"고 정리한다.
- 예문: About 6.8% of docs written during the transition stay fieldless for good: an old-code twin task wrote them first.
- 유사어: permanently (격식), for keeps (구어), once and for all (결단의 뉘앙스, 주로 해결에)
- 반의어: for now / for the time being (당분간만)

## "Not X, same trip."
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 주제는 다르지만 가는 김에 같이 처리해 달라고 할 때(체크리스트 소제목, 구어적 격식).
- 한국어: X 는 아니지만 간 김에
- 설명: 동사 없는 명사구 두 개로 된 소제목이다. `same trip` 은 "같은 걸음·같은 방문"이라 "~하는 김에"를 살려 준다. 원문 C 절은 FDC 가 아니라 proxy 자격 증명 확인인데, 사무실 LLM 이 어차피 그 자리에 있으니 한 번에 하자는 뜻이다.
- 예문: Section C isn't about FDC, but it's the same trip, so check the proxy credentials while you're there. (작성)
- 유사어: while you're at it (구어, 가장 흔함), while you're there (구어), in the same pass (기술 문서)
- 반의어: in a separate run (따로 돌려서)

## "Start here."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 긴 문서에서 읽는 사람이 어디부터 손대야 하는지 못 박을 때(가이드·브리프 머리, 간결).
- 한국어: 여기서 시작하라.
- 설명: 굵게 쓴 두 단어로 문서 전체의 입구를 정한다. 원문은 바로 뒤에 `Run this section, not the whole brief.` 를 붙여 범위까지 좁혔다. 긴 지시서일수록 이런 진입점 한 줄이 읽는 쪽(사람이든 LLM 이든)의 시간을 아껴 준다.
- 예문: **Start here.** Run this section, not the whole brief.
- 유사어: Begin with this section. (평이), If you read one thing, read this. (구어, 강조), TL;DR (요약 표기)
- 반의어: Read from the top. (처음부터 읽어라)

## "merge them by hand instead of overwriting"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 로컬 수정본이 있을 수 있으니 통째로 덮지 말라고 할 때(운영 절차서, 기술).
- 한국어: 덮어쓰지 말고 손으로 합쳐라
- 설명: `by hand` 는 관사 없이 "수작업으로". `instead of + -ing` 로 하지 말아야 할 쉬운 길(`cp` 로 덮기)을 명시한다. 조건절 `If your office.py carries local edits` 와 한 문장을 이룬다. `carry edits` 는 "수정 사항을 지니고 있다"는 뜻이다.
- 예문: If your `office.py` carries local edits, merge them by hand instead of overwriting.
- 유사어: reconcile them manually (격식), hand-merge them (기술 구어), don't just clobber them (구어, `clobber` = 덮어써 망가뜨리다)
- 반의어: overwrite blindly (무작정 덮어쓰다)

## "must be explainable"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 빠진 항목이 있어도 되지만 그 이유를 댈 수 있어야 한다고 기준을 세울 때(검증 기준, 격식).
- 한국어: 설명이 되어야 한다
- 설명: `missing` 자체를 금지하지 않고 `explainable` 로 기준을 옮겼다. 이유가 설명되면 정상, 설명이 안 되면 결함이라는 판정 규칙이다. 원문은 허용되는 이유(`no FDC, or no side-fields yet`)를 콜론 뒤에 나열하고 설명이 안 되는 경우를 굵게 따로 적었다.
- 예문: Missing tools must be explainable: no FDC, or no side-fields yet.
- 유사어: must have a known cause (평이), must be accounted for (격식), there has to be a reason (구어)
- 반의어: unexplained (설명되지 않은)

## "while the window is only partly filled"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 집계 기간이 아직 다 차지 않아 수치가 모자라 보이는 시기를 가리킬 때(데이터 보고, 기술).
- 한국어: 기간이 아직 일부만 채워진 동안
- 설명: `window` 는 조회 기간(30일)이다. `partly filled` 로 배포 뒤 며칠치만 쌓인 상태를 그렸다. `while` 절이라 "그 기간 동안에는 따로 안내가 필요하다"는 한시성이 드러난다.
- 예문: The page may need a "집계 시작일" note while the 30-day window is only partly filled.
- 유사어: until the window fills up (구어), during the ramp-up period (격식·운영), before we have a full 30 days of data (평이)
- 반의어: once the window is full (기간이 다 찬 뒤)

## "that count undercounts"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 집계 방식 때문에 실제보다 적게 세어진다고 지적할 때(데이터 검증, 기술).
- 한국어: 그 집계는 실제보다 적게 센다
- 설명: `undercount` 는 동사와 명사를 겸한다. 짝은 `overcount`, 넓게 쓰면 `understate` ↔ `overstate`. 원문은 `cardinality(timestamp)` 가 같은 시각의 서로 다른 문서 두 건을 한 건으로 세기 때문에 적게 나온다는 논리다. 같은 문서의 V2.4 에서는 카운터 리셋이 있으면 `(max - min) then overstates` 라고 반대 방향을 짚었다.
- 예문: `pin_counts` uses `cardinality(timestamp)`, which counts such a pair once. If it happens, that count undercounts.
- 유사어: comes in low (구어), underreports (보고서), is biased low (통계, 격식)
- 반의어: overcounts / overstates (실제보다 많게 잡다)

## "mean nothing on an older build"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_fleet_verification.md
- 맥락: 전제 조건이 안 맞으면 검사 결과가 무의미하다고 경고할 때(검증 절차서).
- 한국어: 옛 빌드에서는 아무 의미가 없다
- 설명: `mean nothing` 은 "의미가 없다(meaningless)"를 동사로 푼 말이다. 결과가 틀린 게 아니라 판단 근거가 되지 못한다는 뉘앙스. 원문은 `Report the deployed commit first;` 와 세미콜론으로 이어, 먼저 할 일과 그 이유를 한 문장에 담았다.
- 예문: Report the deployed commit first; A1 and A2 below mean nothing on an older build.
- 유사어: are meaningless on (평이), prove nothing on (논증 뉘앙스), are invalid against (격식)
- 반의어: hold regardless of the build (빌드와 상관없이 유효하다)

## "guess at a fix"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 원인을 모른 채 짐작으로 고치고 싶지 않다고 선을 그을 때(리뷰·보고, 구어).
- 한국어: 짐작으로 고칠 방법을 찍다
- 설명: `guess` 는 타동사로 "답을 맞히다", `guess at` 은 "확신 없이 대충 짐작해 보다"로 헛짚는 뉘앙스가 있다. 원문은 실제 장비에서 클릭하는 코드라서 다섯 갈래 중 어느 게이트가 막는지 모르면 고치지 않겠다는 판단이다. 이어서 로그의 어느 줄이 필요한지 정확히 요청한다.
- 예문: From the code alone I can't tell which of five gates stops it, and I don't want to guess at a fix for a real click.
- 유사어: take a stab at a fix (구어, 시도해 보다에 가까움), fix it blind (구어), speculate about a remedy (격식)
- 반의어: fix it from evidence (근거를 보고 고치다)

## "take your hands off"
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 자동화가 도는 동안 입력 장치에서 손을 떼라고 안내할 때(사용 안내, 구어).
- 한국어: 손을 떼다
- 설명: `take one's hands off (something)` 은 물리적으로 손을 뗀다는 뜻이다. 목적어 없이도 쓴다. 원문은 녹화 시작 전 5초 카운트다운을 넣은 이유로 이 말을 썼다. 비유로 쓰면 "관여를 끊다(hands-off)"가 된다.
- 예문: I added a countdown so you can take your hands off before recording starts.
- 유사어: let go of the mouse and keyboard (구체적, 평이), step away from the keyboard (구어), refrain from any input (격식)
- 반의어: take over (조작을 넘겨받다)

## "I pushed the wrong fix first"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 잘못된 수정을 먼저 반영했다가 되돌렸다고 솔직하게 보고할 때(작업 보고, 격식 중간).
- 한국어: 제가 틀린 수정을 먼저 push 했습니다
- 설명: 주어 `I` 를 앞에 두고 잘못을 직접 인정한다. 수동태(`A wrong fix was pushed`)로 흐리지 않는 게 신뢰를 얻는 보고 방식이다. 원문은 이어서 `so I reverted it (also pushed). The code is back to where it was, the tool-close failure is still unfixed` 로 현재 상태를 빠짐없이 적었다.
- 예문: I pushed the wrong fix first; Codex's review showed it can't work, so I reverted it.
- 유사어: My first fix was wrong. (평이), I made a bad call on the first fix. (구어), The initial change was incorrect and has been reverted. (격식, 수동)
- 반의어: got it right the first time (한 번에 맞게 고치다)

## "keeps it from becoming a second rulebook that drifts"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 요약 문서가 원본과 어긋나는 또 하나의 규칙서가 되지 않게 설계했다고 설명할 때(문서 설계, 격식).
- 한국어: 그게 이 문서가 따로 어긋나 가는 두 번째 규칙서가 되는 걸 막는다
- 설명: `keep A from -ing` 은 "A 가 ~하지 못하게 막다". `prevent A from -ing` 보다 부드럽다. `that drifts` 는 관계절로, 원본이 바뀌어도 요약은 그대로라 점점 벌어지는 모습을 `drift`(표류하다) 한 단어로 그렸다. 앞 문장 `the spec … win if they disagree with it` 이 그 장치다.
- 예문: Its opening says the spec wins if they disagree. That keeps it from becoming a second rulebook that drifts.
- 유사어: stops it turning into a competing source of truth (구어), prevents it from diverging into a parallel spec (격식), so it doesn't go stale on its own (구어)
- 반의어: a single source of truth (유일한 기준 문서)

## "This comes from last time, when …"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 지금의 방식이 지난번 실수에서 배운 것이라고 밝힐 때(회고·보고, 구어적 격식).
- 한국어: 이건 지난번에 …했던 일에서 나온 거예요
- 설명: `come from` 은 "~에서 비롯되다". `last time` 뒤에 쉼표 + `when` 계속적 관계부사절을 붙여 그때 무슨 일이 있었는지 풀어 준다. 원문은 `when I predicted from the latest commit and was wrong` 으로 자기 실수를 짧게 인정한다.
- 예문: I compared the letters with the last commit the office pulled. This comes from last time, when I predicted from the latest commit and was wrong.
- 유사어: I learned this the hard way last time. (구어), This is a lesson from last time. (평이), This reflects a mistake made previously. (격식)

## "the test fails without it"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 회귀 테스트가 진짜로 그 수정을 검사한다는 걸 증명했다고 말할 때(개발 보고, 기술).
- 한국어: 그 수정이 없으면 테스트가 실패한다
- 설명: 괄호 안에 넣어 `verified` 의 근거를 댔다. 수정을 빼고 돌려 실패(red)를 확인해야 그 테스트가 쓸모 있다는 TDD 관행을 네 단어로 요약한다. `without it` 의 `it` 은 수정(fix)이다.
- 예문: The stale-frame fix is verified (the test fails without it).
- 유사어: the test goes red if I revert the fix (구어·기술), the test catches the regression (평이), the test is sensitive to the change (격식)
- 반의어: the test passes either way (수정 여부와 상관없이 통과한다 — 쓸모없는 테스트)
