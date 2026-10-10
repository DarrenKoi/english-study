# 2026-10-11 — 새 표현

> 오늘 배치는 repo 문서 3건과 transcript 7건이다. Windows 업그레이드 절차서는 본문이 한국어여서 표현 재료로 쓰지 않았고, 영어로 쓴 외부 근거 조사 노트 두 편(`ebeam_metrology_analytics_external.md`, `analytics_ux_patterns_external.md`)에서 스물하나를 골랐다. 둘 다 "무엇을 확인했고 무엇은 못 찾았나"를 등급까지 매겨 적는 글이라 근거의 세기를 조절하는 말이 많다. transcript 에서는 pm-notes 세션의 서브에이전트 조사 보고에서 여섯, skewnono 리뷰 서브에이전트에게 준 프롬프트에서 셋을 골랐다. `/clear`·`/skill-doctor` 만 찍힌 세션 셋은 재료가 없다. grilling·Herdr·research 스킬 문서는 예전에 다 골라서 건너뛰었다. 노트에 이미 있어서 뺀 것: `hold up`, `first-class`, `a head-to-head comparison`, `have no counterpart`, `the lever is X`, `understate`.

## "was not pinned down"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 조사는 했지만 정확히 어느 것인지 끝내 특정하지 못했다고 밝힐 때(조사 노트·보고, 격식~중립).
- 한국어: (정확히) 특정하지 못했다
- 설명: `pin down` 은 핀으로 꽂아 움직이지 못하게 고정한다는 그림이다. 후보는 좁혔는데 하나로 못 박지는 못했을 때 쓴다. 원문은 바로 뒤에 `candidates are …` 를 붙여 어디까지 좁혔는지 알려 준다. 수동태라서 "내가 못 찾았다"보다 변명처럼 덜 들린다.
- 예문: The exact patent in the family carrying this claim was not pinned down.
- 유사어: could not be identified (격식, 중립), I couldn't nail it down (구어), remains unconfirmed (보고서체, 결과만 말함)
- 반의어: was confirmed (확인됐다)

## "both sides carry uncertainty"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 비교하는 두 값 모두 오차가 있어서 한쪽을 기준으로 삼지 못한다고 설명할 때(통계·계측 문서).
- 한국어: 양쪽 다 불확도를 안고 있다
- 설명: `carry` 는 "지니고 다닌다"는 동사여서 오차·위험·비용 같은 추상명사와 잘 붙는다(`carry risk`, `carry a cost`). `have uncertainty` 보다 "떼어 낼 수 없이 딸려 온다"는 느낌이 난다. 원문은 이 이유를 대고 일반 최소제곱법이 기울기를 왜곡한다고 이어 간다.
- 예문: The same Mandel/TMU machinery is the right method for CD-SEM vs reference comparison, since both sides carry uncertainty.
- 유사어: both are subject to error (격식), neither side is exact (평이), both come with error bars (구어·기술)

## "doubles as"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 한 가지가 본래 용도 말고 다른 구실도 겸한다고 말할 때(설명·제안, 구어~중립).
- 한국어: ~을 겸한다, ~ 구실도 한다
- 설명: `double as B` 는 "A 이면서 B 로도 쓰인다"는 뜻이다. 따로 만들지 않아도 덤으로 얻는다는 느낌이 깔려 있어서 원문도 `a free … monitor` 라고 `free` 를 붙였다. 주어로는 사물이 온다(`The sofa doubles as a bed`).
- 예문: The PSD noise floor doubles as a free per-image tool-noise monitor.
- 유사어: also serves as (격식), works as … too (구어), does double duty as (구어, 한 번에 두 몫)

## "falls out of (the computation)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 따로 계산하지 않아도 다른 계산의 부산물로 저절로 나온다고 할 때(수학·공학 설명).
- 한국어: (계산에서) 덤으로 나온다
- 설명: `fall out of` 는 주머니에서 물건이 굴러 떨어지듯 애쓰지 않아도 나온다는 말이다. 수학·물리 글에서는 "이 결과는 정의에서 바로 따라 나온다"를 `it falls out of the definition` 이라고 쓴다. `drop out`(항이 소거되어 사라진다)과는 방향이 반대다.
- 예문: It falls out of the roughness computation and trends by tool.
- 유사어: comes for free (구어), is a by-product of (격식), follows directly from (수학·논증)

## "match or beat"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 새 방식이 기존 기준과 같거나 더 낫다고 성능을 요약할 때(보고·비교, 중립).
- 한국어: ~와 맞먹거나 앞선다
- 설명: 동사 둘을 `or` 로 묶어 "최소한 동급"이라는 뜻을 두 단어로 끝낸다. `is as good as or better than` 보다 훨씬 짧다. 원문은 `is reported to` 를 앞에 둬서 직접 확인한 수치가 아니라 문헌이 그렇게 보고했다는 거리를 뒀다.
- 예문: Design-based offline creation is reported to match or beat expert on-tool recipes.
- 유사어: is on par with or better than (격식), is at least as good as (평이), holds its own against (구어, 밀리지 않는다)
- 반의어: falls short of (못 미친다)

## "Evidence here is thinner"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 이 대목은 앞 대목보다 근거가 약하다고 미리 알릴 때(조사 보고서·리뷰).
- 한국어: 이쪽은 근거가 더 얇다
- 설명: 근거를 두께로 말한다. `thin evidence` 는 양이 적거나 출처가 약한 근거이고 반대말은 `solid`, `strong` 이다. 원문은 `and mostly patent-level` 을 이어 붙여 얇은 까닭까지 한 문장에 넣었다. 같은 배치의 서브에이전트 보고에도 `Where the evidence is thin` 이라는 소제목이 나온다.
- 예문: Evidence here is thinner and mostly patent-level.
- 유사어: the support is weaker (중립), there is less to go on (구어), the evidence base is limited (격식)
- 반의어: the evidence is solid (근거가 탄탄하다)

## "siloed by owner"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 도구·데이터·조직이 담당 주체별로 갈라져 서로 이어지지 않는다고 지적할 때(분석 보고·회의).
- 한국어: 주인별로 칸막이가 쳐져 있다
- 설명: `silo` 는 곡물 저장탑이다. 탑마다 따로 쌓여 섞이지 않는 모습에서 "부서·시스템 사이의 단절"을 뜻하게 됐고 `siloed` 는 그 분사형이다. `by owner` 가 갈리는 기준을 알려 준다(`siloed by team`, `siloed by region`).
- 예문: The vendor tools are siloed by owner: a tool vendor's offline station covers its own tools and recipes.
- 유사어: fragmented across vendors (중립), walled off from each other (구어), compartmentalised (격식)
- 반의어: integrated across (두루 통합되어 있다)

## "The common thread in X is Y"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 여러 사례를 훑은 뒤 공통점 하나를 뽑아 말할 때(보고서 결론·발표).
- 한국어: X 를 꿰는 공통점은 Y 다
- 설명: 구슬 여럿을 꿰는 실 한 가닥이라는 그림이다. 원문은 `in the credible results` 로 범위를 "믿을 만한 결과"에 한정해서 모든 결과가 그렇다는 과장을 피했다. 콜론 뒤에서 공통점을 풀어 쓰는 구조도 같이 익혀 둔다.
- 예문: The common thread in the credible results is reuse.
- 유사어: what these have in common is (평이), the recurring theme is (문어), they all come down to (구어)

## "with unstated baselines"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: "몇 배 개선" 같은 수치가 무엇 대비인지 밝히지 않았다고 짚을 때(벤더 자료 검토·리뷰).
- 한국어: 기준점을 밝히지 않은 (수치)
- 설명: `baseline` 은 비교의 출발점이다. 그것이 `unstated` 면 "20배"가 무엇의 20배인지 알 길이 없다. 원문은 벤더 수치를 `marketing claims with unstated baselines` 로 보고하라고 권한다. 수치를 버리지는 않되 무게를 낮추는 표현이다.
- 예문: Vendor multipliers should be reported as marketing claims with unstated baselines.
- 유사어: with no stated point of comparison (풀어 쓴 격식), compared to what? (구어, 되묻는 말투), unbenchmarked (기술, 한 단어)

## "did not surface in any result"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md
- 맥락: 찾아봤지만 검색 결과에 아예 나오지 않았다고 조사의 빈 곳을 적을 때(조사 노트).
- 한국어: 어느 결과에도 나타나지 않았다
- 설명: `surface` 는 자동사로 "수면 위로 떠오른다"이고 검색 맥락에서는 "결과에 잡힌다"는 뜻이다. `was not found` 는 없다는 쪽으로 들리는데 `did not surface` 는 내 검색에 안 걸렸을 뿐이라는 여지를 남긴다. 같은 문서에 `surfaced by title only`(제목만 걸렸다)도 나온다.
- 예문: AFM as a reference for CD-SEM did not surface in any result.
- 유사어: did not turn up (구어), was not retrieved (격식·조사 문체), the search came up empty (구어, 주어가 검색 쪽)
- 반의어: surfaced repeatedly (거듭 나왔다)

## "we are only just scratching the surface"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 아직 겉만 건드렸고 본격적인 부분은 손도 못 댔다고 할 때(발표·토론, 구어~중립).
- 한국어: 이제 겨우 겉만 긁었다
- 설명: 표면을 긁기만 하고 속은 못 팠다는 관용구다. `only just` 가 "이제 막, 간신히"를 더한다. 원문은 `a solved problem`(다 풀린 문제)과 맞세워 학계 의견이 갈린다는 것을 보여 준다.
- 예문: Some may say that it is a solved problem, while others argue that we are only just scratching the surface.
- 유사어: we've barely begun (평이), there is much left to explore (격식), this is the tip of the iceberg (구어, 숨은 부분이 크다는 쪽)
- 반의어: it is a solved problem (다 풀린 문제다)

## "the safest reading"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 근거가 엇갈릴 때 가장 무리 없는 해석을 내놓을 때(보고서 결론·리뷰, 격식).
- 한국어: 가장 무리 없는 해석
- 설명: `reading` 은 "읽기"가 아니라 "해석"이다(`my reading of the data`). `safest` 를 붙이면 근거가 허락하는 선을 넘지 않는 해석이 된다. 원문은 뒤에 콜론을 찍고 곧바로 권고를 적는다. 같은 배치의 `my reading of each licence` 와 쓰임이 같다.
- 예문: The safest reading for an expert tool: support overview → filter → detail and the reverse path, and make every cross-view link visibly obvious.
- 유사어: the most cautious interpretation (격식), the conservative takeaway (보고서체), to be safe, assume … (구어)

## "work outward"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 아는 지점 하나에서 출발해 주변으로 넓혀 가며 조사한다고 할 때(디버깅·분석 설명).
- 한국어: (한 점에서) 바깥으로 넓혀 간다
- 설명: `work + 방향 부사` 는 "그 방향으로 차근차근 해 나간다"는 뜻이다(`work backward`, `work down the list`). 원문은 전체에서 좁혀 들어가는 길의 반대, 곧 이미 아는 lot 이나 장비에서 시작하는 길을 가리킨다.
- 예문: Start from a known lot or tool and work outward.
- 유사어: expand from there (평이), branch out from (구어), trace outward from (기술, 따라가며)
- 반의어: drill down (파고 내려간다)

## "alert liberally; page judiciously"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 경보는 넉넉히 걸되 사람을 깨우는 호출은 아껴야 한다는 운영 원칙을 말할 때(온콜·모니터링 설계).
- 한국어: 경보는 넉넉히, 호출은 가려서
- 설명: 부사 둘이 맞선다. `liberally` 는 "아끼지 않고", `judiciously` 는 "잘 가려서". `page` 는 담당자를 호출한다는 동사로 삐삐(pager) 시절에 생겼다. 세미콜론으로 명령문 둘을 붙인 구조여서 구호처럼 외우기 좋다.
- 예문: Datadog's advice is to alert liberally; page judiciously.
- 유사어: record broadly, interrupt rarely (풀어 쓴 말), sparingly (liberally 의 반대쪽 부사), with discretion (judiciously 의 격식 대체)

## "under another name"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 이름만 다르고 실제로는 같은 것이라고 이어 줄 때(비교 설명·보고서).
- 한국어: 이름만 다른 (같은 것)
- 설명: 문장 끝에 붙여 "A 는 사실 B 다, 부르는 이름이 다를 뿐"이라고 말한다. 독자가 아는 개념에 새 개념을 얹을 때 쓴다. 원문은 다른 업계의 BubbleUp 패턴이 반도체 수율 도구의 commonality analysis 와 같다고 잇는다.
- 예문: The pattern is the commercial yield tools' "commonality analysis" under another name.
- 유사어: by a different name (같은 뜻, 평이), in all but name (이름만 아닐 뿐 사실상), essentially the same thing as (풀어 쓴 구어)

## "available off the shelf"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 새로 만들 필요 없이 기성 기능·제품으로 이미 있다고 할 때(기술 선택·견적).
- 한국어: 기성품으로 바로 쓴다
- 설명: 가게 선반에서 집어 오면 된다는 말이다. 명사 앞에서는 하이픈을 넣어 `off-the-shelf components` 라고 쓴다. 맞춤 제작은 `custom-built`, `bespoke`.
- 예문: LTTB downsampling, shared cursors and cross-chart zoom/brush are all available off the shelf in ECharts.
- 유사어: built in (내장, 더 좁은 뜻), out of the box (설치하자마자 되는), ready-made (평이)
- 반의어: custom-built (맞춤 제작한)

## "Correlation is not agreement"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 두 장비 값이 같이 움직인다고 해서 값이 같은 것은 아니라고 못 박을 때(계측·통계 리뷰).
- 한국어: 상관이 높다고 일치하는 것은 아니다
- 설명: `Correlation is not causation` 을 본뜬 문장이다. r 이 1 에 가까워도 한쪽이 늘 2 nm 높게 나오면 `agreement` 는 없다. `A is not B` 로 흔한 오해를 한 줄에 끊는 형식이라 발표 슬라이드 제목으로도 좋다.
- 예문: Correlation is not agreement — a worked example shows near-perfect r with a systematic bias.
- 유사어: moving together is not the same as matching (풀어 쓴 구어), high r does not rule out bias (기술), tracking is not matching (메모체)

## "X, not Y, is the bottleneck"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 막히는 곳이 사람들이 짐작하는 데가 아니라 다른 데라고 바로잡을 때(발표 첫 문장·보고서 결론).
- 한국어: 병목은 Y 가 아니라 X 다
- 설명: 주어와 동사 사이에 `, not Y,` 를 끼워 넣어 예상을 뒤집는다. `The bottleneck is X, not Y` 로 써도 뜻은 같지만 끼워 넣은 쪽이 X 를 문장 맨 앞에 세워서 더 세다. `bottleneck` 은 병의 좁은 목이다.
- 예문: Verification, not generation, is the bottleneck.
- 유사어: the limiting factor is X rather than Y (격식), what slows us down is X (구어), X is the constraint (공정 관리 용어)

## "far below headline numbers"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 널리 인용되는 대표 수치와 실제 조건의 성적이 크게 다르다고 할 때(벤치마크 검토).
- 한국어: 내세우는 수치에 한참 못 미친다
- 설명: `headline number` 는 기사 제목에 실릴 만한 대표 수치다. 가장 유리한 조건에서 나온 값인 경우가 많아서 "실제는 다르다"는 문맥에 자주 나온다. `headline figure`, `headline claim` 도 같은 식으로 쓴다.
- 예문: Benchmarks on realistic enterprise schemas and on chart reading show accuracy far below headline numbers.
- 유사어: well short of the advertised figures (격식), nowhere near the numbers people quote (구어), below the top-line result (보고서체)
- 반의어: in line with headline numbers (대표 수치와 맞는다)

## "satisfice"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 사용자가 최선을 찾지 않고 처음 통한 방법에 머문다고 설명할 때(UX·의사결정 글, 학술어).
- 한국어: 그럭저럭 되는 것에서 멈춘다
- 설명: `satisfy` 와 `suffice` 를 합친 말로 허버트 사이먼이 만들었다. 최적(`optimise`)을 찾는 대신 "충분히 괜찮은" 첫 답에서 탐색을 끝낸다는 뜻이다. 일상 대화에서는 드물고 UX·경제학 글에서 본다. 원문은 그래서 불만 표시가 아니라 관찰된 비효율을 봐야 한다고 잇는다.
- 예문: Users prefer to learn by doing and satisfice with the first method that works.
- 유사어: settle for good enough (구어), make do with (구어, 아쉬운 대로), stop at the first workable option (풀어 쓴 말)
- 반의어: optimise (최선을 찾는다)

## "pointed the same way"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md
- 맥락: 다른 검증도 같은 결론 쪽이었다고 가볍게 덧붙일 때(연구 요약·보고).
- 한국어: 같은 쪽을 가리켰다
- 설명: 증거를 화살표처럼 말한다. `confirmed` 라 하기에는 표본이 작거나 예비 결과일 때 한 단계 낮춰 쓰기 좋다. 원문 주어가 `preliminary validation` 인 것도 그래서다. `point to` 는 "~을 시사한다".
- 예문: Preliminary validation with physicians pointed the same way.
- 유사어: was consistent with this (격식), told the same story (구어), supported the same conclusion (중립)
- 반의어: pointed the other way (반대쪽을 가리켰다)

## "has to be assembled from analogues"
- 레지스터: professional
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 딱 맞는 선례가 없어서 비슷한 사례 여럿을 조합해 만들어야 한다고 보고할 때(벤치마크 조사·기획).
- 한국어: 유사 사례를 엮어서 만들어야 한다
- 설명: `analogue`(미국식 `analog`)는 "성격이 비슷한 다른 분야의 사례"다. `assemble from` 은 부품을 모아 조립한다는 그림이다. 통째로 가져올 본보기가 없다는 사실을 불평 없이 전한다. e-beam 문서의 `nearest analogues` 도 같은 낱말이다.
- 예문: Guide has to be assembled from analogues.
- 유사어: must be pieced together from similar schemes (구어), has no direct precedent (격식, 선례 없음만 말함), we'll have to borrow from adjacent fields (회의 말투)

## "is light by comparison"
- 레지스터: professional, conversational
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 남의 기준과 견줘 우리 쪽이 느슨하다고 부드럽게 지적할 때(리뷰·벤치마크).
- 한국어: 그에 비하면 가벼운 편이다
- 설명: `by comparison` 은 문장 끝에 붙어 "앞에 든 것과 견주면"이라는 뜻이 된다. `light` 는 요건이 적다는 말로 `weak` 나 `insufficient` 보다 덜 공격적이다. 원문은 Kubernetes 의 리뷰 5건·PR 20건 요건을 먼저 적고 이 말을 붙였다.
- 예문: Our "3 substantive reviews" before granting approval rights is light by comparison.
- 유사어: is lenient next to that (구어), is modest in comparison (격식), sets a lower bar (기준이 낮다는 쪽)
- 반의어: is strict by comparison (그에 비하면 엄격하다)

## "is ours to design from scratch"
- 레지스터: conversational, professional
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 참고할 데가 없어서 우리가 처음부터 직접 정해야 하는 부분이라고 할 때(기획 논의).
- 한국어: 우리가 맨바닥에서 설계할 몫이다
- 설명: `be + 소유대명사 + to 부정사` 는 "그 일은 ~의 몫"이라는 구문이다(`It's yours to keep`, `The decision is theirs to make`). `from scratch` 는 출발선에서, 곧 아무것도 없는 데서. 책임이 누구에게 있는지와 일이 얼마나 큰지를 한 번에 전한다.
- 예문: No scheme I checked requires it; that requirement is ours to design from scratch.
- 유사어: we'll have to define it ourselves (평이), there is no template to follow (선례 없음), it falls to us to (격식)

## "this is directional only"
- 레지스터: professional
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 수치를 방향만 보라고, 값 자체는 믿지 말라고 단서를 달 때(분석 보고·회의).
- 한국어: 방향만 참고할 것
- 설명: `directional` 은 "늘려야 하나 줄여야 하나"는 알려 주지만 얼마만큼인지는 못 알려 준다는 뜻의 업계 말이다. 원문은 시험 출제 비중과 교육 시간이 같은 척도가 아니라는 이유를 앞에 대고 이 말로 닫는다. 같은 보고의 `used as a direction, not a number to copy` 가 풀어 쓴 형태다.
- 예문: Exam-question weight and teaching hours are not the same scale, so this is directional only.
- 유사어: treat it as a rough guide (평이), indicative, not definitive (격식 짝말), take the number with a grain of salt (구어)
- 반의어: this is exact (정확한 값이다)

## "my reading of X, not a legal review"
- 레지스터: professional
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 내 해석일 뿐 전문가 검토가 아니라고 판단의 무게를 스스로 낮출 때(조사 보고).
- 한국어: 내가 읽은 바일 뿐 법률 검토가 아니다
- 설명: `my reading of` 는 "내가 해석하기로는"이다. 뒤에 `not a legal review` 를 붙여 책임 범위를 긋는다. `not legal advice` 라는 굳은 면책 문구와 같은 계열이다. `A, not B` 로 무엇이 아닌지까지 말해야 독자가 과신하지 않는다.
- 예문: The copy/adapt columns are my reading of each licence, not a legal review.
- 유사어: as I understand it (구어), my interpretation, which a lawyer should confirm (풀어 쓴 격식), a layperson's read (스스로 낮추는 말)

## "is back to what it was"
- 레지스터: conversational, technical
- 출처: transcript:pm-notes (서브에이전트 조사 보고)
- 맥락: 내가 건드린 것을 치워서 원래 상태로 돌아왔다고 보고할 때(작업 보고, 구어).
- 한국어: 원래대로 돌아왔다
- 설명: `what it was` 는 "전에 그러했던 상태"다. `be back to` 뒤에 명사절을 둬서 `restored to its original state` 를 쉬운 말로 한다. 원문은 부작용(브라우저가 폴더를 떨궈 놓음)을 먼저 털어놓고 이 말로 마무리한다.
- 예문: I deleted it; `git status` is back to what it was.
- 유사어: is back to normal (평이), has been restored (격식), is clean again (git 맥락 구어)

## "Your angle: EFFICIENCY ONLY."
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 프롬프트)
- 맥락: 여러 리뷰어에게 관점을 하나씩 나눠 줄 때(리뷰 분업 지시·프롬프트).
- 한국어: 네가 볼 관점은 효율 하나다
- 설명: `angle` 은 "사안을 보는 각도"다. 기자에게 `What's your angle?` 이라고 물으면 어떤 관점으로 쓸 거냐는 뜻이다. 콜론 뒤에 명사만 두고 `ONLY` 를 대문자로 써서 범위 밖 지적을 막는다. 원문은 뒤에 `Not in scope:` 목록까지 따로 준다.
- 예문: Your angle is efficiency only: flag wasted work the diff introduces.
- 유사어: your focus is (평이), look at this purely from the efficiency side (풀어 쓴 구어), your remit is limited to (격식·영국식)

## "(a Map keyed once) would do"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 프롬프트)
- 맥락: 더 간단한 것으로 충분하다고 대안을 낮춰 제시할 때(코드 리뷰·일상).
- 한국어: ~면 충분하다
- 설명: 이때 `do` 는 "충분하다, 쓸 만하다"는 자동사다(`That will do`, `Any pen will do`). `would` 를 쓰면 "그렇게 했더라면 됐을 텐데"라는 가정이 실려서 리뷰 지적에 어울린다.
- 예문: The code scans the array inside a loop where a Map keyed once would do.
- 유사어: would be enough (평이), would suffice (격식), is all you need (구어)
- 반의어: won't cut it (그걸로는 안 된다)

## "judge fan-out accordingly"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 프롬프트)
- 맥락: 방금 준 조건을 감안해서 판단하라고 맡길 때(지시·가이드, 중립~격식).
- 한국어: 그 점을 감안해 (동시 요청 수를) 판단하라
- 설명: `accordingly` 는 "앞에 말한 사정에 맞게"다. 세부 기준을 일일이 적지 않고 판단을 넘길 때 문장 끝에 붙인다(`Plan accordingly`, `Adjust accordingly`). `fan-out` 은 요청 하나가 여러 갈래로 퍼지는 것.
- 예문: The `afm` blueprint is exempt from the rate limit, so judge fan-out accordingly.
- 유사어: with that in mind (구어), take that into account when … (풀어 쓴 말), in light of this (격식, 문두)
