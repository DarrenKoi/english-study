# 2026-10-15 — 새 표현

오늘 영어는 대부분 AFM 계측 외부 조사 보고서(`afm_metrology_analytics_external.md`) 한 편에서 나왔다. 근거 수준을 태그로 달고, 확인한 것과 추론한 것과 못 찾은 것을 칸을 나눠 적는 글이라 "얼마나 확실한가"를 말하는 표현이 많다. 나머지는 diff 리뷰를 맡긴 하위 에이전트 지시문과 FTP 인코딩 세션의 짧은 영어 몇 줄이다.

## "Coverage is uneven."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 조사·리뷰 보고서 서두에서 어느 부분은 근거가 두껍고 어느 부분은 얇은지 미리 밝힐 때(문어·보고)
- 한국어: 조사한 범위가 고르지 않다.
- 설명: `coverage` 는 "얼마나 덮었는가". `uneven` 을 붙이면 "다 못 봤다"는 고백이 아니라 "깊이가 영역마다 다르다"는 지도가 된다. 바로 뒤에 `Strongest: … Weakest: …` 로 어디가 강하고 약한지 나열하는 짝이 자연스럽다.
- 예문: Coverage is uneven: the CMP section is well sourced, but tool matching rests on vendor pages alone.
- 유사어: The depth varies by section (중립), Some areas are thinner than others (구어)
- 반의어: Coverage is comprehensive (전 영역을 고르게 다뤘다)

## "should be treated as unverified"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 검색 요약만 보고 쓴 수치나 문구를 독자가 확정 사실로 받지 않게 경고할 때(문어·조사 보고)
- 한국어: 검증되지 않은 것으로 다뤄야 한다.
- 설명: `treat A as B` 는 "A 를 B 로 취급하다". 주어를 독자로 두지 않고 수동태(`should be treated`)로 써서 "누가 읽든 이렇게 다뤄라"는 규칙처럼 읽힌다. 남을 탓하지 않고 자기 근거의 한계를 밝히는 문장이다.
- 예문: The page itself was not opened, so wording and numbers should be treated as unverified.
- 유사어: should be taken with caution (중립), are provisional (격식, 짧음), don't lean on these yet (구어)
- 반의어: can be taken as confirmed (확인된 것으로 봐도 된다)

## "follow from (the applications)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 앞에서 정한 전제에서 결론이 자연스럽게 나온다고 말할 때(문어·설계 근거)
- 한국어: (용도에서) 자연히 따라 나온다.
- 설명: `A follows from B` 는 "B 가 원인·전제이고 A 가 그 귀결". 방향을 헷갈리기 쉽다. `from` 뒤에 오는 쪽이 출발점이다. `It follows that …`(그러므로 ~이다) 형태로도 자주 쓴다.
- 예문: The questions engineers ask of the data follow from the applications.
- 유사어: stem from (원인 쪽을 강조), are driven by (중립), come straight out of (구어)
- 반의어: are unrelated to (~와 무관하다)

## "a natural cross-check"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 이미 있는 데이터를 엇갈려 비교하면 따로 일을 벌이지 않고도 검증이 된다고 제안할 때(설계·분석)
- 한국어: 자연스럽게 따라오는 교차 검증 수단.
- 설명: `cross-check` 는 서로 다른 출처로 같은 값을 맞춰 보는 검증. `natural` 을 붙이면 "억지로 만든 지표가 아니라 구조상 당연히 해 볼 비교"라는 뜻이 실린다. 제안을 부드럽게 정당화한다.
- 예문: Depth measurements are bounded by tip geometry, so "depth versus tip age" is a natural cross-check.
- 유사어: an obvious sanity check (구어), a built-in consistency check (중립·기술)
- 반의어: an independent validation (별도로 공들인 검증)

## "runs the other way"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 사람들이 흔히 예상하는 방향과 실제 관계가 반대라고 짚을 때(보고·구어 모두)
- 한국어: 방향이 거꾸로다.
- 설명: 흐름이나 인과의 "방향"을 `run` 으로 말한다. 원문은 "AFM 위에 ML 을 얹는" 그림을 기대한 독자에게 "실제로는 AFM 이 ML 의 정답 레이블을 대는 쪽"이라고 뒤집는다.
- 예문: The most mature "ML on AFM" pattern in fabs runs the other way: AFM as label source for optical models.
- 유사어: is the reverse (중립), is flipped (구어), is inverted (격식·기술)
- 반의어: runs the same way (같은 방향이다)

## "the central weakness vendors compete on"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 시장·기술 동향을 요약하며 업계 전체가 붙잡고 있는 약점을 짚을 때(보고·분석)
- 한국어: 업체들이 서로 앞서려고 경쟁하는 핵심 약점.
- 설명: `compete on X` 는 "X 를 무기로 경쟁하다". 약점이 곧 경쟁 지점이라는 역설을 관계절 하나(`vendors compete on`)로 담았다. 목적격 관계대명사 `that` 이 빠지고 전치사 `on` 이 끝에 남은 구조를 눈여겨볼 것.
- 예문: Throughput is the central weakness vendors compete on.
- 유사어: the main battleground (구어·비유), the key differentiator (격식, 약점 뉘앙스는 빠짐)
- 반의어: a solved problem (이미 해결돼 경쟁 거리가 아닌 것)

## "is hindered by"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 어떤 기술·방법이 퍼지지 못하는 원인을 짚을 때(문어·논문 요약)
- 한국어: ~때문에 (보급·진행이) 막혀 있다.
- 설명: `hinder` 는 완전히 막는(`prevent`) 게 아니라 "더디게 하다, 발목을 잡다". 수동태로 쓰면 막히는 대상(uptake)이 주어가 되어 원인 쪽에 초점이 간다.
- 예문: BTR uptake is hindered by uncertainty over tip matrix size and threshold.
- 유사어: is held back by (구어), is impeded by (더 격식), is slowed by (중립)
- 반의어: is driven by, is accelerated by (~덕분에 앞당겨진다)

## "offered as proof that"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 업체·상대가 어떤 자료를 근거로 내세우는지 거리를 두고 소개할 때(보고·비평)
- 한국어: ~의 증거로 내세워진.
- 설명: `offer` 는 "내놓다". 증거라고 단정하지 않고 "증거로 제시됐다"고만 적어서 판단을 독자에게 남긴다. 업체 마케팅 자료를 인용할 때 중립을 지키는 장치다.
- 예문: The repeat-test numbers are offered as proof that True Non-Contact mode preserves the tip.
- 유사어: presented as evidence that (중립·격식), held up as proof (살짝 비판적), they point to this to show (구어)
- 반의어: shown to be (실제로 입증된)

## "is not directly comparable"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 측정 조건이 다른 두 수치를 나란히 놓지 말라고 경고할 때(분석·리뷰)
- 한국어: 그대로 맞대어 비교할 수 없다.
- 설명: `directly` 가 핵심이다. "아예 비교 불가"가 아니라 "변환·보정 없이 그대로는 안 된다"는 뜻이라, 뒤에 "어떻게 하면 비교할 수 있는지"가 이어지기 좋다(원문은 PSD 로 비교하라고 이어 간다).
- 예문: Rq from instruments with different bandwidths is not directly comparable.
- 유사어: isn't apples to apples (구어), cannot be compared like for like (영국식·격식)
- 반의어: is directly comparable, is on the same footing (같은 기준 위에 있다)

## "an estimate of unknown bias"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 계산은 되지만 그 값이 얼마나 치우쳤는지 알 길이 없다고 경고할 때(분석·계측)
- 한국어: 치우침의 크기를 알 수 없는 추정치.
- 설명: `of` 가 성질을 붙이는 용법(`a man of courage` 와 같은 꼴)이다. 오차(`error`)가 아니라 `bias` 라서 "무작위로 흔들리는" 게 아니라 "한쪽으로 쏠렸을 수 있는데 그 양을 모른다"는 말이 된다.
- 예문: Any roughness or step value computed from a rendered image would be an estimate of unknown bias.
- 유사어: a number you can't calibrate (구어), an uncalibrated estimate (기술·중립)
- 반의어: a traceable measurement (기준에 소급되는 측정값)

## "provided (that)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 결론이 성립하는 조건을 문장 안에 못 박을 때(문어·계약서·논문)
- 한국어: ~라는 조건에서만, ~하기만 하면.
- 설명: `if` 보다 조건이 엄격하게 읽힌다. "그 조건이 지켜질 때에 한해서"라는 단서 조항 느낌이다. `that` 은 흔히 생략된다.
- 예문: Tool-to-tool matching can use the same Mandel machinery, provided the same wafers and sites are measured on both tools.
- 유사어: as long as (구어), on condition that (더 격식), only if (단순)
- 반의어: regardless of whether (조건과 무관하게)

## "on the order of"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 정확한 값이 아니라 자릿수 수준의 크기를 말할 때(기술 문서·회의)
- 한국어: 대략 ~ 정도(자릿수가 그쯤).
- 설명: `order` 는 여기서 "순서"가 아니라 "크기의 자릿수(order of magnitude)". `about` 보다 범위가 넓어서 "몇 배 차이는 있어도 그 단위대"라는 느슨한 어림이다.
- 예문: Interaction distance for Cu is on the order of 50 to 100 µm.
- 유사어: roughly, in the ballpark of (구어), of the order of (영국식)
- 반의어: exactly, precisely (정확히)

## "a selling point"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 제품·제안에서 상대가 내세우는 장점을 말할 때. 살짝 거리를 두는 뉘앙스(회의·리뷰)
- 한국어: 판매 포인트, 내세우는 장점.
- 설명: 장점이라고 동의하는 말이 아니라 "그들이 팔 때 앞세우는 점"이다. 원문은 이 점을 역이용해 "업체가 평탄한 프로파일을 자랑한다면 평탄화 설정이 숨은 변수라는 뜻"이라고 추론한다.
- 예문: Vendor text treats flat, background-free profiles as a selling point.
- 유사어: a headline feature (중립), a draw (구어), a value proposition (격식·비즈니스)
- 반의어: a drawback, a dealbreaker (단점, 결정적 결함)

## "a hidden parameter"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 결과에 영향을 주는데 기록되지 않아 아무도 의식하지 못하는 설정을 지적할 때(분석·설계 리뷰)
- 한국어: 드러나지 않은 숨은 변수.
- 설명: 보이는 입력 말고 결과를 바꾸는 요인이 따로 있다는 경고. 원문에서는 곧바로 "그러니 그 필드를 기록하지 않으면 추세를 같이 그리지 말라"는 규칙으로 이어진다.
- 예문: Levelling choice is a hidden parameter for step height and dishing.
- 유사어: a confounder (통계·격식), an unrecorded setting (중립), a silent knob (구어)
- 반의어: a controlled variable (통제된 변수)

## "a distinct quantity from"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 비슷해 보여 섞기 쉬운 두 지표를 갈라 둘 때(설계·분석)
- 한국어: ~와는 별개의 양.
- 설명: `distinct from` 은 `different from` 보다 "본질이 다르다, 따로 다뤄야 한다"는 무게가 있다. 원문은 이 선언 뒤에 둘을 구별하는 시그니처(계단 vs 기울기)를 바로 준다.
- 예문: Probe-to-probe offset is a distinct quantity from within-tip wear.
- 유사어: separate from (중립), not the same thing as (구어)
- 반의어: equivalent to, the same as (동등한, 같은)

## "more than an order of magnitude above"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 두 값이 열 배 넘게 차이 난다는 것을 수치 없이 크기로 말할 때(기술 보고)
- 한국어: 열 배를 넘게 웃도는.
- 설명: `an order of magnitude` 는 10배. `above/below` 를 붙여 방향을, `more than` 으로 하한을 정한다. "두 측정은 같은 물건을 재는 게 아니다"라는 경고를 숫자 감각으로 전한다.
- 예문: Integrating a PSD over the optical-profiler band can give an rms roughness more than an order of magnitude above a 1 µm AFM scan.
- 유사어: over ten times higher (구어), vastly larger than (모호·과장)
- 반의어: within the same order of magnitude (같은 자릿수 안)

## "sold and used for"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 업체가 내세우는 용도와 실제 쓰임을 한꺼번에 요약할 때(시장 조사·보고)
- 한국어: ~용으로 팔리고 실제로도 쓰인다.
- 설명: 동사 두 개를 `and` 로 묶어 전치사 하나(`for`)를 공유한다. 마케팅(`sold`)과 현장(`used`)이 일치한다는 걸 짧게 확인해 준다.
- 예문: Inline AFM is sold and used for four families of measurement.
- 유사어: marketed and deployed for (격식), pitched and actually run for (구어)
- 반의어: marketed for X but used for Y (팔리는 용도와 쓰임이 다르다)

## "should not be trended together"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 조건이 다른 데이터를 한 추세 그래프에 섞지 말라고 할 때(데이터 분석·대시보드 설계)
- 한국어: 한 추세로 함께 그리면 안 된다.
- 설명: `trend` 를 동사로 쓴다(시계열로 추적해 그리다). 계측·제조 현장 영어에서 흔한 용법이다. 수동태라 "누가 그리든"의 규칙으로 읽힌다.
- 예문: Results from recipes with different flattening orders should not be trended together without that field recorded.
- 유사어: shouldn't share a chart (구어), should not be pooled (통계·격식)
- 반의어: can be trended on one chart (한 차트에 같이 그려도 된다)

## "a weak tip-wear detector"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 어떤 지표가 특정 문제를 잡아내는 능력이 약하다고 평가할 때(분석·모니터링 설계)
- 한국어: 팁 마모를 잘 못 잡아내는 지표.
- 설명: 데이터 자체를 `detector`(탐지기)로 의인화해 "이 숫자로는 그 문제가 안 보인다"를 한 명사구로 끝낸다. 형용사만 바꿔 `a strong / noisy / lagging indicator` 로 응용하기 좋다.
- 예문: Product results alone are a weak tip-wear detector; a dedicated monitor-site series is required.
- 유사어: a poor signal for (중립), a lagging indicator of (늦게 반응하는 지표)
- 반의어: a sensitive indicator (민감한 지표)

## "low-value to rebuild"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 이미 시중 제품에 있는 기능을 사내에서 다시 만들 가치가 낮다고 판단할 때(기획·build vs buy)
- 한국어: 다시 만들어 봐야 얻는 게 적다.
- 설명: `low-value` 를 형용사로 앞에 두고 `to + 동사` 를 붙여 "~하기에 가치가 낮다". `not worth rebuilding` 보다 단정 정도가 약하고 판단 기준(가치)을 드러낸다.
- 예문: Features vendors already advertise on-tool are low-value to rebuild.
- 유사어: not worth rebuilding (구어), offer little return if rebuilt (격식)
- 반의어: worth building in-house (사내에서 만들 만하다)

## "without numbers"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 근거 수치 없이 주장만 하는 홍보 문구를 담담하게 짚을 때(리뷰·조사)
- 한국어: 수치는 밝히지 않고.
- 설명: 비판 형용사 없이 사실만 적어도 "근거가 없다"가 전달된다. 같은 글에서 `a "Longest Tip Life" heading with no number` 처럼 `with no number` 로도 변주한다.
- 예문: It also advertises "superior tool-to-tool matching" without numbers.
- 유사어: with no figures given (중립), unquantified (격식), they don't say how much (구어)
- 반의어: with published figures (수치를 공개하며)

## "in what I found"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: "없다"고 말할 때 그 범위가 내가 찾아본 자료에 한정된다고 단서를 달 때(조사 보고)
- 한국어: 내가 찾은 자료 안에서는.
- 설명: 부재 주장을 세계 전체가 아니라 탐색 범위로 묶어 둔다. 같은 글의 "an absence of evidence in public pages, not a confirmed absence" 와 같은 정신이다.
- 예문: Not demonstrated in what I found: a production-grade tip-condition classifier.
- 유사어: as far as I could find (구어), within the sources reviewed (격식)
- 반의어: across the field, in general (분야 전반에서)

## "positions X as Y"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 회사·제품이 스스로를 어떤 자리에 놓는지(마케팅 포지셔닝) 설명할 때(비즈니스·보고)
- 한국어: X 를 Y 로 내세우다(자리매김하다).
- 설명: `position` 을 동사로 쓴다. 실제로 그렇다는 판정이 아니라 "그렇게 보이게 자리를 잡는다"는 의도를 말한다. 원문은 바로 뒤에 "결국 AFM 을 기준으로 두는 셈"이라는 해석을 붙인다.
- 예문: Onto Innovation positions OCD as the high-throughput inline Cu-recess method.
- 유사어: pitches X as Y (구어), presents X as Y (중립), markets X as Y (판매 맥락)
- 반의어: (마땅한 대체 표현 없음)

## "a fast initial phase followed by a slower steady phase"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 시간에 따라 두 구간으로 나뉘는 거동(초기 길들이기 → 안정)을 한 명사구로 묘사할 때(기술 보고)
- 한국어: 처음엔 빠르다가 이후 느리고 안정된 구간으로 넘어가는.
- 설명: `A followed by B` 는 순서를 명사구 하나로 압축한다. 절을 두 개 쓰는 것(`It is fast at first, and then it slows`)보다 문어에서 훨씬 단단하다.
- 예문: Wear shows a fast initial phase followed by a slower steady phase.
- 유사어: a run-in period and then a steady state (기술·중립), it starts fast and then levels off (구어)
- 반의어: a constant rate throughout (처음부터 끝까지 일정한 속도)

## "the slope of X against Y"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md
- 맥락: 그래프의 y 축과 x 축을 말로 정의할 때(분석·보고)
- 한국어: Y 에 대한 X 의 기울기(X 를 Y 에 대해 그렸을 때의 기울기).
- 설명: `X against Y` 는 "X 를 세로축, Y 를 가로축으로". 순서가 한국어("Y 에 따른 X")와 반대라 헷갈리기 쉽다. `plot X against Y`, `X versus Y` 도 같은 축 배치다.
- 예문: Wear rate is then the slope of qualifier width against the usage counter.
- 유사어: X versus Y (중립), X as a function of Y (격식·수학)
- 반의어: (마땅한 대체 표현 없음)

## "at the root-cause depth rather than a bandaid"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [agent-prompt]
- 맥락: 리뷰어에게 증상만 덮은 수정인지, 원인 층에서 고친 수정인지 판정해 달라고 할 때(코드 리뷰)
- 한국어: 임시방편이 아니라 근본 원인 깊이에서 고쳤는가.
- 설명: `bandaid`(반창고)는 겉만 덮는 땜질의 대명사다. `depth` 를 써서 수정이 놓인 "층"을 공간 은유로 말한다. 같은 지시문의 `ALTITUDE` 와 짝을 이룬다.
- 예문: Check whether each fix is at the root-cause depth rather than a bandaid.
- 유사어: a proper fix vs. a patch-over (구어), addresses the cause, not the symptom (중립)
- 반의어: a stopgap, a band-aid fix (임시방편)

## "say when the cost is negligible so it is not changed needlessly"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [agent-prompt]
- 맥락: 리뷰어에게 "문제없음"도 명시적으로 보고하게 해 과잉 수정을 막을 때(리뷰 지시)
- 한국어: 비용이 무시할 만하면 그렇다고 말해, 괜히 고치지 않게 하라.
- 설명: `negligible`(무시해도 될 만큼 작은)과 `needlessly`(쓸데없이)가 짝을 이룬다. 결과 절을 `so (that)` 로 붙여 지시의 이유까지 문장 안에 넣었다.
- 예문: Name the cheaper alternative, and say when the cost is negligible so it is not changed needlessly.
- 유사어: flag what's fine so we leave it alone (구어), note where no change is warranted (격식)
- 반의어: flag everything (전부 지적하라)

## "Name the simpler form that does the same job."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/b4fc9877 [agent-prompt]
- 맥락: 막연한 "더 단순하게"가 아니라 구체적 대안까지 요구할 때(리뷰 지시·피드백)
- 한국어: 같은 일을 하는 더 단순한 형태를 구체적으로 적어라.
- 설명: `name` 을 동사로 써서 "이름을 대라 → 구체적으로 짚어라". `does the same job` 은 동작이 같다는 구어적 표현으로, 리팩터링 제안이 기능을 바꾸지 않는다는 전제를 깐다.
- 예문: Flag awkward control flow and name the simpler form that does the same job.
- 유사어: spell out the simpler version (구어), propose a behaviour-preserving simplification (격식)
- 반의어: just say it's too complex (대안 없이 지적만)

## "Now the fix — fleet downloader first."
- 레지스터: casual
- 출처: transcript:skewnono-v3-nuxt/e3eac2d8 [assistant]
- 맥락: 작업 중 다음 단계와 순서를 짧게 알릴 때(구어·진행 안내)
- 한국어: 이제 수정 차례다. fleet downloader 부터.
- 설명: 동사를 다 빼고 명사구와 대시만으로 진행을 알린다. 글보다 말에 가까운 리듬이다. `X first` 로 우선순위를 붙이는 꼴은 매우 흔하다.
- 예문: Now the fix — fleet downloader first, then the proxy client.
- 유사어: On to the fix, starting with … (중립), Next up: … (구어)
- 반의어: (마땅한 대체 표현 없음)
