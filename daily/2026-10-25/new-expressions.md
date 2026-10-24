# 2026-10-25 — 새 표현

오늘 배치는 광학 계측(두께·엘립소미터) 조사 문서 4개와 대화 9개다. 조사 노트의 영어는 "위험을 짧은 명사구로 이름 붙이는" 문체가 두드러지고 대화에서는 확인한 것과 안 한 것을 갈라 보고하는 말투가 많았다.

## "showing derived thickness as bare truth"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 계산·추정으로 나온 숫자를 근거 없이 "사실"처럼 내보이는 위험을 지적할 때(설계 문서·리뷰, 격식)
- 한국어: 파생된 두께 값을 맥락 없는 진실처럼 보여 주는 것
- 설명: `bare` 는 "아무것도 걸치지 않은"이다. 숫자에 붙어야 할 신뢰도·출처 정보가 벗겨진 상태를 한 단어로 그린다. 위험 목록의 소제목처럼 동명사구로 쓰면 "무엇이 문제인가"가 바로 보인다.
- 예문: Showing derived thickness as bare truth is the biggest quality trap, because a degenerate fit looks exactly like a good one.
- 유사어: presenting X as fact (중립), passing off X as ground truth (부정적 뉘앙스 더 강함), taking X at face value (받아들이는 쪽 관점)
- 반의어: showing X with its uncertainty (불확도와 함께 보여 주다)

## "the bad numbers will be most convincing exactly when the model is wrong"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 직관과 반대로 움직이는 위험(틀릴수록 그럴듯해짐)을 경고할 때(설계 근거·발표)
- 한국어: 모델이 틀렸을 바로 그때 나쁜 숫자가 가장 그럴듯해 보인다
- 설명: 최상급 `most convincing` 과 `exactly when` 이 맞물려 역설을 만든다. `exactly` 를 빼면 단순한 시점 설명이 되고 넣으면 "하필 그때"라는 강조가 된다.
- 예문: Engineers will trust bad numbers, and the bad numbers will be most convincing exactly when the model is wrong.
- 유사어: look most plausible precisely when (더 격식), seem the most trustworthy right when (구어)
- 반의어: (마땅한 대체 표현 없음 — 반대 상황은 "obviously wrong when it fails" 처럼 풀어 쓴다)

## "designing against guessed data"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 실제 데이터를 보기 전에 추측한 형태에 맞춰 설계하는 위험을 말할 때(위험 목록·리뷰)
- 한국어: 짐작한 데이터를 상대로 설계하기
- 설명: `design against X` 는 "X 를 기준·상대로 삼아 설계한다"이다. 테스트에서 `test against a spec` 처럼 쓰는 `against` 와 같다. `guessed` 하나가 "근거 없음"을 다 말한다.
- 예문: Designing against guessed data is risky, since the real tool's export will contradict most of our mock's choices.
- 유사어: building on assumptions (중립), designing in the dark (구어, 비유)
- 반의어: designing against real exports (실제 수출 파일을 기준으로)

## "limits the damage only if …"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 안전장치가 있긴 하지만 조건부로만 효과가 있다고 짚을 때(리뷰·설계 문서)
- 한국어: ~할 때에만 피해를 줄여 준다
- 설명: `limit the damage` 는 "피해를 막는다"가 아니라 "줄인다"다. 뒤에 `only if` 를 붙여 규칙의 효력 범위를 좁힌다. "규칙이 있으니 괜찮다"는 안심을 조건으로 바꿔 놓는 구조다.
- 예문: The repo's mock rule limits the damage only if the UI is built against the contract shape.
- 유사어: contains the damage (격식, 확산 방지 뉘앙스), keeps the blast radius small (기술 구어), helps only when (평이)
- 반의어: makes things worse (오히려 악화시키다)

## "the contract shape, not the mock's conveniences"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 목(mock) 데이터의 편한 성질에 기대지 말고 계약(API 스키마)에 맞추라고 할 때(설계 리뷰)
- 한국어: 목이 주는 편의가 아니라 계약의 모양
- 설명: `conveniences` 를 복수로 써서 "목이라서 깔끔하게 맞는 여러 편한 점들"을 가리킨다. `X, not Y` 대비로 기준을 하나로 못 박는다.
- 예문: Build the view against the contract shape, not the mock's conveniences, or it will break on the first real file.
- 유사어: the schema, not the sample data (평이), the interface, not the fixture (테스트 맥락)

## "volume hubris"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 데이터량을 얕보는 자만을 위험 항목 이름으로 붙일 때(위험 목록, 문어)
- 한국어: 데이터량에 대한 자만
- 설명: `hubris` 는 그리스 비극에서 신을 얕본 오만이다. 명사 두 개를 붙인 짧은 이름이라 목록 제목으로 기억에 남는다. 일상 대화보다는 글에서 무게를 줄 때 쓴다.
- 예문: Imaging-SE volume hubris is the third risk: raw cubes cannot ride a JSON-over-fetch architecture.
- 유사어: underestimating the data volume (평이), overconfidence about scale (중립)
- 반의어: respecting the data volume (데이터량을 존중하다), sizing it first (먼저 규모를 재다)

## "research-grade eye candy"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 보기엔 멋지지만 실무자에게 쓸모가 적은 기능을 가볍게 깎아내릴 때(리뷰·구어)
- 한국어: 연구용으로나 볼 법한 눈요깃거리
- 설명: `eye candy` 는 "눈에 달콤한 것", 겉보기만 화려한 것이다. `research-grade` 는 원래 칭찬(연구 수준)인데 여기선 "현장에는 과하다"는 뜻으로 비튼다.
- 예문: A raw-cube explorer is research-grade eye candy, not what fab engineers need.
- 유사어: a flashy demo (구어), nice to look at but not useful (평이), a showpiece (중립)
- 반의어: a workhorse view (매일 쓰는 실용 화면)

## "a research question nobody in a fab asks daily"
- 레지스터: conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 기능이 답하는 질문 자체가 현장에서 드물다고 말할 때(표·회의)
- 한국어: 팹에서 누구도 매일 묻지 않는 연구용 질문
- 설명: `nobody … asks daily` 는 "아무도 안 묻는다"가 아니라 "매일 묻지는 않는다"로 범위를 좁힌다. 기능을 버리자는 게 아니라 우선순위를 낮추자는 말이 된다.
- 예문: The hyperspectral explorer answers a research question nobody in a fab asks daily.
- 유사어: an edge case for most users (중립), not an everyday question (평이)
- 반의어: the question they ask every morning (매일 아침 묻는 질문)

## "claims outrun verifiable detail"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 홍보 문구가 확인 가능한 근거보다 앞서 나간다고 평할 때(조사 보고서, 격식)
- 한국어: 주장이 검증 가능한 세부보다 앞서 나간다
- 설명: `outrun` 은 "~보다 빨리 달리다". 주장과 증거를 경주시키는 비유라 "과장"이라는 직설보다 점잖다. 원문은 `product-page claims outrun verifiable UI detail`.
- 예문: Product-page claims outrun verifiable UI detail, so treat the exact competitor layouts as unknown.
- 유사어: claims go beyond the evidence (중립), the marketing is ahead of the docs (구어), overstate (직설)
- 반의어: claims are backed by (근거가 뒷받침하다)

## "never by the metric alone"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/optical_metrology_external_evidence.md
- 맥락: 지표 하나만 보고 판정하면 안 된다고 강하게 못 박을 때(기술 문서)
- 한국어: 지표 하나만으로는 절대 판단하지 않는다
- 설명: 앞 문장 `judged by MSE together with residuals …` 뒤에 대시로 붙인 부정 보충이다. `never` 를 문두가 아니라 끝에 두어 앞 내용을 한 번 더 조인다.
- 예문: Fit quality is judged by MSE together with residuals and correlations — never by the metric alone.
- 유사어: not on its own (평이), in isolation (격식, "단독으로")
- 반의어: taken together with (함께 놓고 보면)

## "under-determined"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 데이터에 비해 풀어야 할 변수가 많아 답이 하나로 안 정해질 때(수학·모델링)
- 한국어: 해가 하나로 정해지지 않는(과소결정된)
- 설명: 방정식보다 미지수가 많은 상태를 가리키는 수학 용어다. 일상에서도 "정보가 모자라 결론이 하나로 안 나온다"는 뜻으로 빌려 쓴다.
- 예문: Strong correlations mean the model is under-determined even when the curve looks fine.
- 유사어: ill-posed (더 넓은 수학 용어), not uniquely solvable (풀어 쓴 말), ambiguous (일상)
- 반의어: well-determined, over-determined (데이터가 남는 쪽)

## "perfectly sane to ship"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 크기·비용이 충분히 감당할 만하다고 가볍게 말할 때(엔지니어끼리 구어)
- 한국어: 보내도 전혀 무리 없는
- 설명: `sane` 은 "정신이 온전한", 여기선 "상식적으로 괜찮은"이다. 바로 앞의 `too big for naive JSON` 과 대비돼 "이건 미친 짓이 아니다"라는 느낌을 준다.
- 예문: A point-SE wafer is about 1–5 MB of JSON, which is perfectly sane to ship per measurement.
- 유사어: reasonable (중립), totally fine (구어), well within budget (격식)
- 반의어: prohibitive (감당 못 할)

## "trivially cheap"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md
- 맥락: 성능 비용이 따질 필요도 없이 작다고 말할 때(설계 논의)
- 한국어: 거의 공짜나 다름없이 싸다
- 설명: `trivially` 가 "생각할 거리도 안 된다"는 정도를 더한다. 단, 이 문서는 실측 없이 쓴 판단이라 뒤에 `(no in-repo benchmark run)` 을 붙였다. 강한 부사를 쓸 때 근거 수준을 함께 밝히는 습관까지 같이 익히면 좋다.
- 예문: A spectra overlay with a few 1000-point lines is trivially cheap in ECharts.
- 유사어: negligible (격식), basically free (구어)
- 반의어: expensive, the bottleneck

## "Both cannot be right; X is better sourced."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/optical_metrology_external_evidence.md
- 맥락: 서로 어긋나는 두 출처 중 어느 쪽을 믿을지 근거로 고를 때(조사 보고서)
- 한국어: 둘 다 맞을 수는 없고 X 쪽이 출처가 더 탄탄하다
- 설명: 먼저 모순을 인정하고(`Both cannot be right`) 판정 기준(`better sourced`)을 댄다. `sourced` 는 "출처가 달린"이라는 형용사로 쓰였다.
- 예문: Both cannot be right; the Cimetrix/SEMI grouping is better sourced.
- 유사어: X has stronger backing (중립), X is the more reliable source (평이)
- 반의어: equally well sourced (출처가 비슷하게 탄탄하다)

## "exists purely to dodge (the rate limit)"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/skewvoir_thickness_local_code.md
- 맥락: 어떤 API·코드가 왜 있는지 그 존재 이유를 한 줄로 말할 때(코드 설명)
- 한국어: 오로지 (요청 제한을) 피하려고 있는
- 설명: `dodge` 는 몸을 피하다, 제약을 요리조리 피하다. `purely` 가 "다른 이유는 없다"를 보탠다. 기능이 아니라 우회책이라는 성격을 드러낸다.
- 예문: The batch endpoint exists purely to dodge the 50-req/5s rate limit.
- 유사어: works around (중립), sidesteps (격식), gets around (구어)
- 반의어: is subject to (제한을 그대로 받다)

## "One thing has to change at the same time, or you'll end up with …"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt fc3f283c (pi-mcp-adapter 제거 질문)
- 맥락: 답은 "예"인데 같이 해야 할 조건 하나를 경고로 붙일 때(동료에게 말·채팅)
- 한국어: 하나는 같이 바꿔야 한다, 안 그러면 결국 ~가 된다
- 설명: `or` 뒤에 나쁜 결과를 두는 경고 구조다. `end up with` 는 의도치 않게 그 상태로 끝나 버리는 것. 원문은 `or you'll end up with no MCP at all`.
- 예문: You can remove the adapter, but one thing has to change at the same time, or you'll end up with no MCP at all.
- 유사어: there's a catch (구어), provided that you also … (격식), as long as you also … (중립)

## "(only matters if you used these)"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt fc3f283c
- 맥락: 손실·주의사항 목록 앞에 "해당 없으면 무시해도 된다"고 범위를 미리 알려 줄 때(안내문·채팅)
- 한국어: (이것들을 썼던 경우에만 해당)
- 설명: 주어 `This` 를 생략한 괄호 메모다. 독자가 목록을 다 읽기 전에 자기와 관계있는지 판단하게 해 준다.
- 예문: What you'd lose (only matters if you used these): the gateway tool and the save-script feature.
- 유사어: if applicable (격식), skip this if … (구어)

## "If you rely on that, test one … after you switch."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt fc3f283c
- 맥락: 확인 못 한 부분을 밝히고 상대가 직접 해 볼 최소 점검을 제안할 때(보고 끝맺음)
- 한국어: 그걸 쓰고 있다면 바꾼 뒤에 하나만 시험해 보세요
- 설명: 앞에서 `I didn't check whether …` 로 미확인을 인정한 뒤 이어지는 문장이다. 조건(`If you rely on that`)으로 대상을 좁히고 점검 크기(`one subagent`)를 구체로 준다.
- 예문: I didn't check the child-agent grant; if you rely on that, test one subagent after you switch.
- 유사어: if that matters to you, try … (구어), it would be worth verifying … (격식)

## "I agree with all six and will fix them now rather than hand them back."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt b4fc9877 (code-review high 결과 수용)
- 맥락: 리뷰 지적을 받아들이고 공을 상대에게 넘기지 않고 바로 처리하겠다고 할 때(업무 보고)
- 한국어: 여섯 개 모두 동의하고 되돌려 드리지 않고 지금 고치겠습니다
- 설명: `rather than` 뒤에는 원형(`hand`)이 온다. `hand back` 은 일을 원래 주인에게 돌려주는 것이다. "결정만 묻고 떠넘기지 않겠다"는 태도를 짧게 담았다.
- 예문: The review returned six findings, all in code I landed today; I agree with all six and will fix them now rather than hand them back.
- 유사어: instead of passing them back to you (평이), rather than kicking them back (구어)
- 반의어: hand them back for a decision (판단을 넘기다)

## "stay exactly as they are"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt b4fc9877 (logging 스크립트 재실행 질문)
- 맥락: 작업을 다시 돌려도 기존 데이터는 하나도 안 바뀐다고 안심시킬 때(구어·채팅)
- 한국어: 지금 그대로 남는다
- 설명: `as they are` 가 "현재 상태 그대로"이고 `exactly` 가 "한 글자도"를 덧붙인다. `No.` 로 답한 뒤 이 문장을 붙이면 걱정을 완전히 덮는다.
- 예문: Previously stored rows, including the visit and page-view rows, stay exactly as they are.
- 유사어: remain untouched (격식), aren't touched at all (구어)
- 반의어: get overwritten (덮어써지다)

## "would be rejected rather than applied"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt b4fc9877
- 맥락: 잘못된 요청이 들어와도 시스템이 조용히 반영하지 않고 거절한다고 설명할 때(기술 설명)
- 한국어: 적용되는 대신 거절된다
- 설명: 수동태 과거분사 두 개를 `rather than` 으로 나란히 놓았다. "실패하면 어떻게 되나"를 묻는 사람에게 "안전한 쪽으로 실패한다"를 보여 준다.
- 예문: If the body tried to change an existing field, the request would be rejected rather than applied.
- 유사어: fails loudly instead of silently (구어 기술), is refused (격식)
- 반의어: is silently applied (조용히 반영된다)

## "Nothing is lost either way."
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt b4fc9877
- 맥락: 두 경우를 설명한 뒤 어느 쪽이든 손해가 없다고 마무리할 때(구어)
- 한국어: 어느 쪽이든 잃는 건 없다
- 설명: 앞에서 두 갈래(매핑 전·후)를 풀어 놓고 `either way` 로 한꺼번에 받는다. 짧은 결론 문장이라 단락 끝에 두면 안심 효과가 크다.
- 예문: Rows written before the update just lack the field; nothing is lost either way.
- 유사어: no data is lost in either case (격식), you're fine both ways (구어)
- 반의어: something gets dropped (뭔가 빠진다)

## "would have charged every … a …"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt b4fc9877 (리뷰 지적 3번)
- 맥락: 코드 하나가 매 요청마다 비용을 물리는 구조였다고 설명할 때(코드 리뷰)
- 한국어: 모든 ~에 ~ 비용을 물렸을 것이다
- 설명: `charge A B` 는 "A 에게 B 를 청구하다"인데, 성능 비용에도 그대로 쓴다. 가정법 과거완료(`would have charged`)는 고치기 전에 그랬을 상황을 말한다.
- 예문: Reading the roster first would have charged every recipe open a parquet load at cold start.
- 유사어: would have cost every … (평이), would have added … to every … (중립)
- 반의어: costs nothing on the common path (흔한 경로에서는 비용 없음)
