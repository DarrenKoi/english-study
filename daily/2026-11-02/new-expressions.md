# 2026-11-02 — 새 표현

## "ranked by payoff"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (altitude review 보고)
- 맥락: 검토 결과나 할 일 목록을 "고쳤을 때 얻는 효과" 순으로 늘어놓았다고 밝힐 때(보고서·문어)
- 한국어: 효과(이득)가 큰 순으로
- 설명: payoff 는 투자 대비 돌아오는 보상. severity(심각도)순과 달리 "고치면 얼마나 좋아지나"가 기준이라는 점을 드러냅니다.
- 예문: Here are eight findings, ranked by payoff, so you can stop after the first three if time is short.
- 유사어: ordered by value (더 평이), in order of impact (격식), biggest wins first (회화)
- 반의어: in no particular order (순서 없이)

## "stated twice, differently"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (altitude review 보고)
- 맥락: 같은 규칙이 두 곳에 서로 다르게 적혀 있다는 코드 리뷰 지적(문어)
- 한국어: 두 번, 그것도 서로 다르게 적혀 있다
- 설명: 부사 differently 를 쉼표 뒤에 덧붙여 "중복"에 "불일치"까지 얹습니다. 짧지만 문제의 핵심을 다 담는 구조입니다.
- 예문: The "not recorded" rule is stated twice, differently, so the two pages already disagree on blank values.
- 유사어: duplicated and out of sync (풀어 쓴 판), defined in two places that disagree (설명적)
- 반의어: defined in one place (단일 정의)

## "on top of (X)"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 이미 있는 비용·일에 무언가가 더 얹힌다고 말할 때(구어·문어 모두)
- 한국어: ~에 더해, ~ 위에 또
- 설명: 원문은 "two teardowns plus two inits per point, on top of the setOption". 기본 비용 위에 추가 비용이 쌓인다는 그림이 그려집니다.
- 예문: Each point change costs two re-initialisations on top of the normal redraw.
- 유사어: in addition to (격식), besides (평이), not to mention (강조·회화)

## "that is the worst case, not X"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 상대가 과장해서 잡은 최악 수치를 실제 상한으로 바로잡을 때(기술 문서)
- 한국어: 최악이어도 그 정도지, X 까지는 아니다
- 설명: 원문 "Server caps a profile at 65,536 samples, so that is the client's worst case, not 260k." 앞에서 근거(cap)를 대고 so 로 결론을 붙입니다.
- 예문: The API pages at 500 rows, so that is the worst case for one request, not the full table.
- 유사어: at most (간결), the upper bound is (격식), it never gets worse than (회화)
- 반의어: the best case (최선의 경우)

## "at true scale"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af 서브에이전트 브리프
- 맥락: 그래프나 도면을 축 비율을 왜곡하지 않고 실제 크기 그대로 그리라고 할 때(사양서)
- 한국어: 실제 축척 그대로
- 설명: 정규화·리샘플링 없이 원래 단위와 크기를 지킨다는 뜻. 비교 차트 요구사항에 자주 붙습니다.
- 예문: Overlay the line profiles of the same point across measurements, at true scale.
- 유사어: to scale (더 짧고 흔함), without normalisation (기술적 풀이)
- 반의어: normalised (정규화한), not to scale (축척 무시)

## "do not leave hooks for them"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af 서브에이전트 브리프
- 맥락: 이번 범위 밖 기능을 위해 미리 확장 지점을 심어 두지 말라고 못 박을 때(작업 지시)
- 한국어: 나중을 위한 연결 고리도 남기지 마라
- 설명: hook 은 나중에 기능을 끼울 자리. "만들지 마라"에 이어 "만들 준비도 하지 마라"까지 막아 YAGNI 를 분명히 합니다.
- 예문: These are non-goals; do not build them and do not leave hooks for them.
- 유사어: don't add extension points (기술적), don't design for them yet (평이)
- 반의어: leave room for (나중을 위해 여지를 두다)

## "Verify each of these against the code and docs before relying on it."
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af 서브에이전트 브리프
- 맥락: 넘겨준 정보를 그대로 믿지 말고 원본과 대조하라고 위임할 때(지시문)
- 한국어: 기대기 전에 하나하나 코드와 문서에 대조해 확인하라
- 설명: verify A against B = A 를 B 에 맞춰 대조하다. before relying on it 이 "왜 지금 확인해야 하는지"를 붙여 줍니다.
- 예문: The figures below come from last month's notes; verify each of them against the dashboard before relying on it.
- 유사어: double-check X against Y (회화), cross-check (격식), don't take my word for it (구어)

## "testing effort lands on the critical paths"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af (tdd 스킬 문서)
- 맥락: 노력·자원이 어디에 쓰이게 되는지 결과 중심으로 말할 때(문어)
- 한국어: 테스트 노력이 핵심 경로에 쏠리게 된다
- 설명: land on 은 "떨어져 닿다". 의도적으로 배분한 결과가 그곳에 도착한다는 그림입니다.
- 예문: Agreeing the seams up front is how testing effort lands on the critical paths instead of every edge case.
- 유사어: goes where it matters (회화), is concentrated on (격식), is spent on (평이)
- 반의어: is spread thin (얇게 흩어지다)

## "a retune"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (altitude review 보고)
- 맥락: 디자인 토큰·파라미터를 다시 조정하는 일을 명사 하나로 부를 때(기술·구어)
- 한국어: 재조정
- 설명: 원문 "Cost: a retune of a role class skips these." 동사 retune 을 관사와 함께 명사로 써서 문장을 짧게 만듭니다.
- 예문: A retune of the spacing scale will miss any component that hard-codes its own padding.
- 유사어: an adjustment (평이), a recalibration (격식·측정 맥락)

## "it matters past roughly 5k rows"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 어떤 비용이 일정 규모를 넘어서야 의미가 생긴다고 선을 그을 때(리뷰·구어)
- 한국어: 대략 5천 행을 넘어서야 문제가 된다
- 설명: past 를 전치사로 써서 "그 지점을 지나면"이라는 문턱을 짧게 표현합니다.
- 예문: The scan is linear, so it only matters past roughly ten thousand items.
- 유사어: only above (평이), beyond (격식), once you hit (회화)

## "Checked, nothing to fix."
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 검토했지만 손볼 것이 없었던 항목을 보고에 명시할 때(보고서 소제목·메모)
- 한국어: 확인함, 고칠 것 없음
- 설명: 주어·동사를 생략한 메모체. "안 봤다"와 "봤는데 괜찮다"를 구분해 주는 한 줄이라 리뷰 보고에서 값어치가 큽니다.
- 예문: Listener cleanup: checked, nothing to fix.
- 유사어: No issues found (격식), All good here (회화)

## "tell the next reader something false"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (simplification review 보고)
- 맥락: 낡은 주석·문서가 해로운 이유를 미래의 독자 관점에서 지적할 때(리뷰)
- 한국어: 다음에 읽는 사람에게 틀린 사실을 알려 준다
- 설명: 주석을 "말하는 주체"로 세운 무생물 주어 구문. 한국어로는 "읽는 사람이 오해하게 된다"로 옮기면 자연스럽습니다.
- 예문: Delete the comment; it is eleven lines that tell the next reader something false about the office adapter.
- 유사어: mislead future readers (평이), give a wrong picture (회화)

## "its correction lands in a .vue"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (altitude review 보고)
- 맥락: 수정이 엉뚱한(테스트하기 어려운) 파일에 들어가게 된다고 지적할 때(리뷰)
- 한국어: 그 수정이 .vue 파일 안에 떨어지게 된다
- 설명: land in 은 "결국 ~에 들어가게 되다". 원하지 않는 위치라는 뉘앙스가 실립니다.
- 예문: If the regex stays in the page, its correction lands in a component that has no tests.
- 유사어: ends up in (회화), gets made in (평이)

## "I did not observe a 429."
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 추론으로 위험을 지적하되 실제로 관측하지는 않았다고 선을 그을 때(정직한 보고)
- 한국어: 429(요청 과다)를 실제로 본 것은 아니다
- 설명: 앞 문장의 추정("can exceed")과 뒤의 관측 여부를 분리해 신뢰도를 정확히 전달합니다.
- 예문: One open can exceed the rate limit in theory, but I did not observe a 429.
- 유사어: I haven't actually seen it happen (회화), this has not been reproduced (격식·수동)

## "two rules for one job"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (reuse review 보고)
- 맥락: 같은 역할을 하는 구현이 둘이라는 문제를 짧게 요약할 때(리뷰·구어)
- 한국어: 한 가지 일에 규칙이 둘
- 설명: 대구(two/one)로 리듬을 만든 명사구. 뒤에 괄호로 구체 차이를 붙이면 설득력이 생깁니다.
- 예문: We have two sanitisers for file names, which is two rules for one job.
- 유사어: duplicated logic (기술적), reinventing the wheel (관용·회화)
- 반의어: a single source of truth (하나의 기준)

## "Expected values must be hand-worked literals."
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af 서브에이전트 브리프
- 맥락: 테스트 기대값을 코드로 계산하지 말고 손으로 푼 값을 적으라고 할 때(지시문)
- 한국어: 기대값은 손으로 계산해 둔 상수여야 한다
- 설명: hand-worked 는 "손으로 풀어 본". 같은 로직으로 기대값을 만들면 테스트가 항상 통과하는(tautological) 문제를 막는 규칙입니다.
- 예문: For the line-removal test, the expected values must be hand-worked literals from a four-point example.
- 유사어: worked out by hand (평이), computed independently (격식)

## "Nil at X; noticeable only on Y"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (efficiency review 보고)
- 맥락: 비용이 규모에 따라 0에서 체감 수준까지 달라진다고 압축해 말할 때(메모체 리뷰)
- 한국어: X 에서는 사실상 0, Y 에서만 체감된다
- 설명: nil 은 "없음, 0". 세미콜론으로 두 조건을 나란히 놓아 대비를 만듭니다.
- 예문: The extra allocation is nil for a single line; noticeable only on dense grids.
- 유사어: negligible (격식), barely matters (회화)
- 반의어: significant (상당한)

## "No shared helper exists yet."
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (reuse review 보고)
- 맥락: 재사용할 대상이 아직 없다는 사실을 밝히며 새로 만들 근거를 깔 때(리뷰)
- 한국어: 아직 공용 도우미 함수가 없다
- 설명: yet 이 "앞으로 만들 만하다"는 여지를 남깁니다. 단정적인 "There is no..."보다 부드럽습니다.
- 예문: No shared helper exists yet, so the copy toast is written out three times.
- 유사어: There's nothing to reuse here (회화), nothing common has been extracted (격식)

## "against DESIGN.md"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d (altitude review 보고)
- 맥락: 결정이 지침서와 어긋난다고 지적할 때(리뷰). against = "~에 반하여"
- 한국어: DESIGN.md 에 어긋나게
- 설명: 원문 "Colour and type decisions made at call sites, against DESIGN.md." against 는 "대조하여"도 되고 "거슬러"도 되므로 문맥으로 구분합니다.
- 예문: Several components pick their own red, against the design guide.
- 유사어: contrary to (격식), in breach of (규정 위반 뉘앙스), not following (평이)
- 반의어: in line with (부합하여)

## "Prefer no backend change."
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af 서브에이전트 브리프
- 맥락: 금지까지는 아니지만 기본값으로 피하라고 우선순위를 줄 때(작업 지시)
- 한국어: 가능하면 백엔드는 건드리지 마라
- 설명: Prefer no X 는 "X 를 하지 않는 쪽을 택하라". 뒤에 "If ... truly required, stop and report"를 붙여 예외 경로를 열어 둡니다.
- 예문: Prefer no schema change; if one is truly required, stop and report instead of making it.
- 유사어: Avoid X if you can (회화), X should be a last resort (격식)

## "a reference to consult, not a session to run"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af (tdd 스킬 문서)
- 맥락: 문서나 도구의 쓰임새를 대비로 정의할 때(문어)
- 한국어: 실행할 절차가 아니라 펼쳐 볼 참고서
- 설명: "a N to V, not a N to V" 대구. to 부정사가 명사를 꾸며 "~할 대상"을 만듭니다.
- 예문: The style guide is a reference to consult, not a checklist to run through every time.
- 유사어: something to look things up in (회화), a resource, not a procedure (격식)
