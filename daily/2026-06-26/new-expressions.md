# 2026-06-26 — 오늘의 표현

오늘 배치는 거의 전부 사내 프로젝트 설계 문서(영어 prose)였다. 그중 보고서·ADR·설계 스펙에서 바로 꺼내 쓸 만한 표현을 골랐다. (한글→영어·영어 다듬기 코칭은 내가 직접 쓴 글이 없어 오늘은 생략.)

---

## "hit the same wall"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 여러 다른 시도가 *결국 같은 한계*에 부딪혔다고 결론지을 때 (회고·실험 보고서). 한 번이면 "hit a wall".
- 한국어: 같은 벽에 부딪히다, 똑같은 한계에 막히다.
- 설명: 서로 다른 접근들이 약속이나 한 듯 동일한 지점에서 막히는 상황을 한 문장으로 압축한다. "all hit the same wall" 처럼 `all` 과 붙여 "전부 똑같이 막혔다"를 강조하는 게 정석.
- 예문: Three matcher-fusion methods all hit the same wall: they recover the true point but rank it #1 only half the time.
- 유사어: run into the same dead end (회화·구어적), converge on the same limitation (격식·분석적)
- 반의어: break through (돌파하다), clear the hurdle

## "the validated next move"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 추측이 아니라 *검증을 거쳐* 다음에 할 일이 확정됐다고 못 박을 때 (설계 결정문).
- 한국어: 검증된 다음 수순, (근거로) 확정된 다음 행보.
- 설명: `move` 가 체스/전략에서의 "한 수"라는 뉘앙스라 "next step" 보다 결단·전략성이 강하다. `validated` 가 "그냥 다음 단계"가 아니라 "데이터가 가리킨" 단계임을 보증한다.
- 예문: Re-registration onto a more distinctive region is the validated next move.
- 유사어: the confirmed next step (중립), the proven way forward (격식)
- 반의어: an untested gamble, a shot in the dark (요행수)

## "calibration-fragile ↔ calibration-light"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 임계값·설정에 *민감해 쉽게 깨지는* 지표 vs *거의 안 타는* 지표를 대비할 때 (평가·튜닝 설계).
- 한국어: 보정에 취약한 ↔ 보정에 둔감한(튜닝이 거의 필요 없는).
- 설명: `X-fragile` / `X-light` 는 "X 에 얼마나 민감한가"를 형용사로 압축하는 생산적 합성 패턴이다 (cf. `latency-light`, `config-heavy`). 두 단어를 한 쌍으로 제시하면 trade-off 가 또렷해진다.
- 예문: Its tier floors are calibration-fragile, so a cleaner, calibration-light signal is preferred.
- 유사어: (fragile) brittle, threshold-sensitive / (light) robust to tuning, low-maintenance
- 반의어: calibration-fragile ↔ calibration-light (이 쌍 자체가 대비)

## "de-risk (something) first"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md (§10)
- 맥락: 본격 착수 전에 *가장 위험한 부분을 먼저 없애자*고 제안할 때 (계획 회의·태스크 순서 결정).
- 한국어: (착수 전에) 위험을 먼저 걷어내다, 가장 불확실한 곳을 먼저 못 박다.
- 설명: 명사 `risk` 를 동사화한 표현. "Pin the join key (de-risk first)" 처럼 *맨 앞 태스크*에 위험 해소를 배치하라는 전략적 지시로 자주 쓴다. [[front-load]] 와 짝을 이룬다.
- 예문: Pin the join key first to de-risk the rest of the implementation.
- 유사어: take the risk off the table, retire the biggest unknown (둘 다 격식)
- 반의어: leave it to chance, kick the risk down the road (미루다)

## "rank them worst-first"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 작업 목록·트리아지에서 *가장 나쁜 것부터* 정렬해 우선순위를 매긴다고 밝힐 때.
- 한국어: 나쁜 것부터(악화 순으로) 정렬하다.
- 설명: `worst-first` 가 정렬 방향을 부사처럼 한 단어로 못 박는다. 엔지니어가 "어디부터 손대야 하나"에 바로 답하는 실무 지향 표현. 반대 방향은 `best-first`.
- 예문: The worklist ranks recipes worst-first, so the engineer tackles the most broken keys before anything else.
- 유사어: sort by severity (descending), most-broken-first
- 반의어: best-first, in arbitrary order (정렬 없이)

## "float up (the list)"
- 레지스터: conversational, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 가중치·점수를 줘서 *중요한 항목이 위로 떠오르게* 만든다는 비유 (랭킹·우선순위 로직 설명, 약간 구어).
- 한국어: (목록에서) 위로 떠오르다/떠오르게 하다.
- 설명: 액체 위로 뜨는 이미지. 정렬 결과로 "자연히 위에 오게 한다"는 뉘앙스라 능동적 강제(force to top)보다 부드럽다. `so (that) ... float up` 으로 목적을 붙인다.
- 예문: Multiply by a fix-type weight so the harder, higher-value fixes float up the list.
- 유사어: bubble up (더 구어), rise to the top, surface (드러나다)
- 반의어: sink to the bottom, get buried (묻히다)

## "impossible to miss"
- 레지스터: conversational, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md (§5)
- 맥락: 로그·경고·UI 를 *못 보고 지나칠 수 없게* 만들었다고 할 때. 회화·문서 양쪽.
- 한국어: 못 보고 지나칠 수 없는, 눈에 안 띌 수가 없는.
- 설명: `impossible + to부정사` 는 "~하기가 불가능한"을 간결히 표현하는 형용사구. 방어적 설계에서 "조용한 실패(silent failure)"의 반대편으로 자주 등장한다.
- 예문: Emit a loud coverage line so a silent key mismatch is impossible to miss.
- 유사어: hard to overlook (조금 약함), glaringly obvious, it stares you in the face (캐주얼)
- 반의어: easy to overlook, fly under the radar (몰래 지나가다)

## "a hard failure signal, not a quiet X"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md (§5)
- 맥락: 어떤 상태를 *조용히 넘기지 말고 명백한 실패로 다뤄야 한다*고 규정할 때 (방어적 설계 원칙).
- 한국어: (조용한 ~가 아니라) 명백한 실패 신호.
- 설명: `hard` 가 "단호한·명시적"의 뜻(↔ soft). "X, not a quiet Y" 구문으로 "묻고 넘어가는 길"을 먼저 차단한다. fail-fast 철학의 문어체 표현.
- 예문: A near-zero match rate is a hard failure signal, not a quiet fallback.
- 유사어: a loud failure, fail fast and loud (구어적 슬로건)
- 반의어: fail silently, degrade quietly (조용히 강등)

## "the one real implementation hazard"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md (§5 제목)
- 맥락: 나머지는 사소하고 *진짜 위험은 이것 하나*라고 콕 집어 독자의 주의를 모을 때 (스펙 섹션 제목·리뷰).
- 한국어: 진짜 위험 요소는 이거 하나, 유일하게 실질적인 함정.
- 설명: `the one real X` 패턴 — `one` 과 `real` 이 함께 "여럿처럼 보여도 실제로 단 하나"임을 강조한다. `hazard` 는 risk 보다 "사고로 이어질 수 있는" 구체적 위험.
- 예문: Join-key mismatch is the one real implementation hazard here; everything else is mechanical.
- 유사어: the single biggest risk, the only real gotcha (구어)
- 반의어: a minor edge case, a non-issue (별 문제 아님)

## "the payload for (X)"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md (§4.4)
- 맥락: 어떤 경우에 *실어 보내는 핵심 산출물·알맹이*가 무엇인지 지정할 때 (자료구조·출력 설계).
- 한국어: (~행/케이스의) 실질 내용물, 핵심 산출물.
- 설명: 네트워크에서 헤더가 아닌 "본문 데이터"를 뜻하는 `payload` 를 비유로 확장 — "이 행에서 정작 쓸모 있는 알맹이는 이것"이라는 뜻. `the payload for NEW_REGION rows` 처럼 "어느 케이스의 알맹이냐"를 `for` 로 붙인다.
- 예문: The whitebox suggestion is the payload for NEW_REGION rows; FRESH_SNAPSHOT rows don't need one.
- 유사어: the actionable output, the meaningful content (둘 다 격식)
- 반의어: boilerplate, filler (빈 껍데기)

## "ambiguous by construction"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-25-reregister-rank1-distinctiveness-worklist-design.md
- 맥락: 우연이 아니라 *구조상 필연적으로* 모호하다고 근본 원인을 진단할 때. (cf. 이미 정리한 [[safe by construction]] / made structurally impossible 와 같은 `X by construction` 가족.)
- 한국어: 구조적으로/태생적으로 모호한.
- 설명: `by construction` 은 "만들어진 방식 자체가 그렇다 → 검사로 바꿀 수 없다"는 수학·CS 관용구. 형용사 자리에 `ambiguous` 를 넣어 "모호함이 데이터에 박혀 있다"를 단언한다.
- 예문: If the matcher can't rank the true point #1 even on a clean success frame, the key is ambiguous by construction.
- 유사어: inherently ambiguous, ambiguous by design
- 반의어: distinctive, unambiguous (변별력 있는)
