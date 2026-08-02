# 2026-08-03 — 새 표현

## "buys the safety at a price"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 기존 설계의 장점을 인정하면서 그 대가를 짚을 때(설계 문서·리뷰, 격식)
- 한국어: 그 안전을 대가를 치르고 산다 — 공짜가 아니다
- 설명: `buy X at a price` 는 "X 를 얻긴 하는데 값을 치른다"는 관용 구조. 앞에 `does keep ... safe` 처럼 상대 설계의 장점을 강조 조동사 `does` 로 인정해 두고, `but it buys the safety at a price:` 로 비용 목록을 여는 흐름이 정중한 반박의 정석이다.
- 예문: That design does keep the alarm API safe from page traffic, but it buys the safety at a price.
- 유사어: comes at a cost (더 평이·중립), trades simplicity for safety (무엇을 내줬는지 명시)
- 반의어: comes for free (비용 없이 따라온다)

## "forces X rather than merely motivating it"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 여러 근거 중 하나가 "결정타"임을 구분해 줄 때(설계 근거 서술, 격식)
- 한국어: X 를 단순히 뒷받침하는 게 아니라 강제한다
- 설명: motivate(하고 싶게 만드는 이유)와 force(안 할 수 없게 만드는 이유)를 대비시키는 문형. `rather than merely -ing` 가 두 동사의 급 차이를 한 문장에 눌러 담는다. 근거 나열 뒤에 "이 중 이것 때문에 반드시 해야 한다"를 짚을 때 쓴다.
- 예문: That last point is what forces the redesign rather than merely motivating it.
- 유사어: necessitates (격식·건조), leaves no choice but to (구어에 가까움)
- 반의어: merely motivates (하고 싶은 이유일 뿐 강제는 아니다)

## "collapse into (one call)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 여러 요청·이벤트가 하나로 합쳐지는 동작을 설명할 때(기술 문서)
- 한국어: (여럿이) 하나로 접히다/합쳐지다
- 설명: N 개의 입력이 시스템을 거치며 1개의 실질 동작으로 줄어드는 것을 collapse 로 그린다. 캐시·디바운스·락 설명에 딱 맞는 동사로, `any number of X collapse into at most one Y` 꼴로 상한을 함께 말할 수 있다.
- 예문: Any number of viewers collapse into at most one call to the office alarm API per facility per 20 seconds.
- 유사어: coalesce into (격식·물리적 합쳐짐), be deduplicated into (기계적)
- 반의어: fan out into (하나가 여럿으로 퍼지다)

## "carry over to"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 한 상황에서 타당했던 논리가 다른 상황에도 적용되는지 따질 때
- 한국어: (논리·결론이) 그대로 옮겨 적용되다
- 설명: "저기서 맞았다고 여기서도 맞는 건 아니다"를 말하는 표준 동사구. `That reasoning is sound for A. It does not carry over to B.` 두 문장 패턴으로 쓰면, 원 결정을 존중하면서 재사용을 거부할 수 있다.
- 예문: That reasoning is sound for compare, which is N recipes wide; it does not carry over to one parameter.
- 유사어: transfer to (일반어), generalize to (학술 어감), hold for (수학·논리 어감)
- 반의어: be confined to (그 상황에만 갇혀 있다)

## "(a distinction that) has teeth"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 규칙·구분이 장식이 아니라 어기면 실제로 문제가 생긴다고 강조할 때(구어 기운이 있는 문서체)
- 한국어: 이빨이 있다 — 실제 물리력(결과)이 따르는
- 설명: 법·규칙이 "물 수 있다", 즉 위반 시 실제 대가가 있다는 관용구. 코드 문서에서 "이 구분을 무시하면 진짜 사고가 난다"를 한 단어로 전달한다. 원문은 fac_id/fab_name 구분이 과거 장애를 낸 이력을 가리키며 썼다.
- 예문: See roster.py and _tool_specs.py for why that distinction has teeth.
- 유사어: has real consequences (평이·격식), is enforced (규정 어감)
- 반의어: toothless (있으나 마나 한)

## "a deliberate non-answer"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: "안 하기로 한 것"이 게으름이 아니라 판단의 결과였음을 밝힐 때(설계 문서)
- 한국어: 의도된 무응답 — 일부러 답하지 않기로 한 선택
- 설명: non-answer 는 "답이 아닌 답". 앞에 deliberate 를 붙이면 "그 공백 자체가 결정이었다"가 된다. 과거 결정을 소개할 때 이렇게 이름 붙여 두면, 뒤에서 그 전제가 지금도 유효한지 따지는 흐름이 자연스럽다.
- 예문: Its image handling is a deliberate non-answer: the filenames let a reader find the images without pulling them off the tool.
- 유사어: a conscious punt (구어·미식축구 은유), an intentional omission (건조한 격식)
- 반의어: an oversight (몰라서 빠뜨린 것)

## "dig X out of Y"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 데이터를 힘들게 파내야 하는 번거로움을 불평 섞어 묘사할 때
- 한국어: Y 를 뒤져서 X 를 파내다
- 설명: extract 의 구어 버전. "그냥 주어지는 게 아니라 파야 나온다"는 수고가 담겨 있어, API 가 불친절하다는 논지를 세울 때 효과적이다. 원문도 스크립트 사용자가 겪을 번거로움을 나열하며 썼다.
- 예문: A script must call recipe-detail, dig the locator out of the payload, and post it back.
- 유사어: fish X out of (더 캐주얼), extract X from (중립·격식 — 격식 문서에서는 이쪽)

## "green for the wrong reason"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 테스트가 통과하긴 하는데 그 통과를 믿으면 안 되는 상황(테스트 리뷰)
- 한국어: 엉뚱한 이유로 초록불인 — 통과가 무의미한
- 설명: CI 의 green(통과)을 빌려, "결과는 pass 지만 검증 대상이 실제로 검증되지 않았다"를 말한다. 원문은 가짜 Redis 가 NX/TTL 을 속이면 그 위의 락 테스트 전부가 이렇게 된다고 경고했다.
- 예문: A double that lies about NX or TTL would make every lock test below it green for the wrong reason.
- 유사어: a false green (명사형, 기존 노트), passing vacuously (논리학 어감)
- 반의어: failing honestly (실패가 진짜 신호인 상태)

## "hide behind"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 하나의 이름 아래 성격이 다른 것들이 숨어 있음을 드러낼 때(분석 글의 도입)
- 한국어: (한 표현) 뒤에 숨어 있다
- 설명: 사람이 핑계 뒤에 숨는 hide behind 를 사물에 쓰면, "겉보기 하나, 실체 여럿"을 여는 문장이 된다. 이어서 차이(비용·성격)를 표로 가르는 전개와 짝이 좋다.
- 예문: Two data sources hide behind "parameter info", and they differ by orders of magnitude.
- 유사어: lurk behind (더 불길한 어감), sit behind (중립)
- 반의어: be spelled out (겉으로 다 드러나 있다)

## "harmless while X, actively misleading now that Y"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 전제가 바뀌어 무해하던 것이 해로워졌음을 설명할 때(회고·결정 번복의 근거)
- 한국어: X 일 때는 무해했지만, Y 가 된 지금은 적극적으로 오도한다
- 설명: 시점 대비 구문. `while`(그때) ↔ `now that`(전제가 바뀐 지금)이 축이고, misleading 앞의 actively 가 "가만히 있어도 해를 끼친다"로 수위를 올린다. 과거 결정을 비난하지 않으면서 지금 바꿔야 하는 이유를 만든다.
- 예문: The fake SEM texture was harmless while every other column was fabricated too, and actively misleading now that they are real tool data.
- 유사어: benign then, harmful now (평이), no longer defensible (더 강한 판정)
- 반의어: still holds (전제가 안 바뀌어 여전히 유효하다)

## "self-heal"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 장애 후 사람 개입 없이 시스템이 스스로 복구되는 성질(신뢰성 논의)
- 한국어: 스스로 치유되다 — 자동 복구되다
- 설명: 장애(outage) 뒤 상태가 저절로 정상으로 수렴하는 성질. 원문은 상류 API 가 이력을 충분히 돌려주면 보드가 self-heal 하고, 아니면 "구멍이 영구히 남는다"(a permanent hole)고 두 경우를 갈랐다 — 반대 상황까지 짝으로 익혀 두면 좋다.
- 예문: If it returns ten minutes of history, the board self-heals after any outage.
- 유사어: self-correct (판단·수치의 수렴), recover on its own (평이)
- 반의어: leave a permanent hole (복구 불가능한 공백이 남다)

## "strictly better than"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 트레이드오프가 아니라 모든 면에서 우위라고 단언할 때(설계 비교)
- 한국어: 어느 면에서도 밀리지 않고 낫다 — 순수 우위
- 설명: 게임이론의 strict dominance 에서 온 어법. "장단이 있다"가 아니라 "잃는 게 없다"는 강한 주장이므로, 원문처럼 바로 뒤에 `because ...` 로 근거를 대는 게 관례다.
- 예문: Caching at fac granularity is strictly better than caching per fab, because the coarse key is the one the upstream call is actually parameterized by.
- 유사어: dominates (게임이론 그대로), wins on every axis (구어)
- 반의어: a trade-off (얻는 만큼 잃는 관계)

## "wedge (the feature)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 시스템이 죽지도 살지도 못하고 끼어 버린 상태를 말할 때(장애 논의, 구어 기운)
- 한국어: (쐐기가 박힌 듯) 꽉 끼어 멈추다
- 설명: crash(죽음)와 다르게 wedge 는 "멈췄는데 에러도 안 나는" 상태. 원문은 배포 결함이 실패에 더해 락까지 물고 있어 기능 전체를 LOCK_TTL_SEC 동안 끼워 버리면 안 된다고 썼다. 곁들여진 `on top of failing`(실패한 것도 모자라)도 같이 쓸 만하다.
- 예문: A deployment fault must not wedge the feature for twenty seconds on top of failing.
- 유사어: jam (물리적 어감), deadlock (원인이 상호 대기일 때), brick (아예 벽돌이 되다, 더 강함)
- 반의어: degrade gracefully (기능을 줄이며 살아남다)

## "a convention call, not a technical one"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (Share 토스트 수정)
- 맥락: 선택의 근거가 기술 우열이 아니라 코드베이스 관례였음을 밝힐 때(리뷰 답변)
- 한국어: 기술 판단이 아니라 관례 판단이었다
- 설명: `a ~ call` 은 judgment call 의 틀을 빌린 것으로, 무엇을 기준으로 내린 결정인지 call 앞의 명사가 말해 준다. `not a technical one` 을 붙이면 "더 나은 속성이 있다는 건 알지만 기존 관례를 따랐다"는 방어가 된다.
- 예문: break-all over wrap-anywhere was a convention call, not a technical one.
- 유사어: a judgment call (기준을 밝히지 않는 상위어), a style choice (가벼움)
- 반의어: a technical necessity (기술적으로 그래야만 하는 것)

## ""A" and "B" are separate claims"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (Share 토스트 수정)
- 맥락: 뭉뚱그려진 두 진술을 분리해 각각 따로 검증하자고 할 때(디버깅·논증)
- 한국어: A 와 B 는 별개의 주장이다
- 설명: 증상("토스트가 이상해 보인다")과 결론("기능이 고장났다")을 claim 이라는 단어로 같은 급에 올려놓고 separate 로 가른다. 하나가 참이어도 다른 하나는 검증 전이라는 규율을 문장 하나로 세운다.
- 예문: "The toast looks wrong" and "the feature is broken" are separate claims.
- 유사어: distinct questions (중립), orthogonal issues (수학 은유, 남용 주의)
- 반의어: one and the same (사실상 같은 이야기)

## "a cue to X, not a Y in its own right"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 신호의 성격을 규정할 때 — 행동을 촉구하는 실마리이지 그 자체가 사건은 아니다(UI·알림 설계)
- 한국어: X 하라는 신호이지, 그 자체로 Y 는 아니다
- 설명: cue 는 "다음 행동을 부르는 신호". `in its own right`(그 자체로서)와 짝지으면 표시 수위를 정하는 근거가 된다 — 원문은 unmatched_count 를 배지·에러가 아니라 조용한 한 줄로 그리는 이유로 썼다.
- 예문: A non-zero count is an operator's cue to check the tool list, not an alarm in its own right.
- 유사어: a prompt to (더 직접적), a signal to (중립)
- 반의어: an event in its own right (그 자체가 독립된 사건)

## "mock fodder, not classifiers"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 데이터의 용도를 오해해 생긴 버그를 경고할 때 — 이건 테스트 재료지 판별 기준이 아니다
- 한국어: 목(mock) 채우기용 재료일 뿐, 분류기가 아니다
- 설명: fodder 는 원래 가축 사료로, `X fodder` 꼴로 "X 에 쓰라고 만든 소모성 재료"를 뜻한다(cannon fodder, tabloid fodder). `A, not B` 로 용도를 못박아, prefix 목록을 분류 로직에 쓰다 장애를 낸 전례를 한 줄로 봉인한다.
- 예문: eqp_prefixes and eqp_models are mock fodder, not classifiers.
- 유사어: grist for X (X 의 재료, 관용구 grist for the mill), test scaffolding (구조물 은유)
- 반의어: the source of truth (판단의 근거로 삼아도 되는 것)
