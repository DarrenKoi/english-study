# 2026-06-22 — 새 표현

## "fast-follow"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-14-recipe-comparison-design.md
- 맥락: 기능 설계에서 "이번엔 범위 밖이지만 출시 직후 곧바로 이어서 할 후속 작업"을 가리킬 때(기획·설계 문서, 격식)
- 한국어: 곧바로 뒤따르는 후속 작업
- 설명: 어떤 것을 내보낸 직후 "빠르게 이어서" 하기로 예정해 둔 후속 항목. 보통 명사로 쓰며, 지금 당장은 아니지만 곧 한다는 뉘앙스.
- 예문: The in-page recipe switcher across those three views is the documented fast-follow.
- 유사어: follow-up (더 일반적·격식 중립), next iteration (다음 반복 주기에서 처리), quick win (가치 대비 빠르게 끝나는 일이라는 뉘앙스)
- 반의어: out of scope (아예 범위 밖으로 빼 둔 것)

## "well-established"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 어떤 기법·관행이 "이미 학계·업계에서 충분히 정립·검증되어 표준이 되었다"고 평가할 때(기술 리뷰, 격식)
- 한국어: 충분히 정립된, 널리 인정받는
- 설명: 새로 지어낸 게 아니라 오랜 검증을 거쳐 표준으로 자리 잡았다는 뜻. 주로 method/technique/pattern 과 함께 쓴다.
- 예문: The overall pattern is well-established and sound.
- 유사어: well-recognized (널리 알려진), standard/canonical (표준으로 굳은), battle-tested (실전에서 검증된, 더 구어)
- 반의어: ad hoc (임시변통의), experimental (아직 실험적인)

## "hand-tuned"
- 레지스터: technical
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 파라미터·임계값을 이론에서 유도하지 않고 사람이 경험으로 손수 맞췄다고 짚을 때(기술 비평)
- 한국어: 사람이 손으로 맞춘, 수동 튜닝한
- 설명: 자동 보정이나 원리적 유도가 아니라 손으로 조정했다는 의미. 흔히 "rather than derived" 와 대비시켜 약점을 지적할 때 쓴다.
- 예문: The individual score components are reasonable but hand-tuned rather than derived from a published metric.
- 유사어: hand-built (직접 만든), hand-crafted (정성껏 손으로), heuristic (휴리스틱한)
- 반의어: derived / principled (원리에서 유도된), calibrated (데이터로 보정된)

## "cold-start values"
- 레지스터: technical
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 아직 실데이터로 보정하기 전의 "초기 가동 기본값"을 가리킬 때(기술)
- 한국어: 초기 가동값, 보정 전 기본값
- 설명: 시스템이 데이터를 쌓기 전 시작 시점에 쓰는 임시 상수. 나중에 calibrate 되면 대체된다.
- 예문: The 0.50 accept threshold and scorer weights are cold-start constants, not calibrated decision boundaries.
- 유사어: default values (기본값), placeholder values (자리만 채운 값), pre-calibration values (보정 전 값)
- 반의어: calibrated values (데이터로 보정된 값)

## "ad hoc"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 일반 원칙이 아니라 그 경우 하나만을 위한 임시 처방임을 짚을 때(격식·기술 글)
- 한국어: 임시변통의, 그때그때 둘러댄
- 설명: 라틴어에서 온 표현. 체계적 근거 없이 특정 상황에 맞춰 급조했다는 뜻으로, 약간 부정적 뉘앙스를 띨 수 있다.
- 예문: The best-3-plus-worst weighting is explicitly ad hoc tolerance for one broken side.
- 유사어: improvised (즉흥적인), one-off (일회성의), makeshift (임시방편의, 더 구어)
- 반의어: principled (원칙에 기반한), systematic (체계적인)

## "the main fragility is X"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 분석 결론에서 "가장 깨지기 쉬운 약점"을 한 문장으로 지목할 때(기술 리뷰, 결론부)
- 한국어: 가장 큰 취약점은 X 이다
- 설명: fragility 는 "깨지기 쉬움". 여러 우려 중 핵심 약점을 요약해 제시하는 결론 문형이다.
- 예문: The main fragility is the outermost-wall selection and the area-first pruning, both of which can discard the correct candidate.
- 유사어: the main weakness is, the weak point is, the Achilles' heel is (관용·약간 구어)
- 반의어: the main strength is (가장 큰 강점은)

## "ordered by severity"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator (codex 평가)
- 맥락: 이슈·우려 목록을 심각도 순으로 정렬했다고 헤더에서 밝힐 때(기술 문서, 격식)
- 한국어: 심각도 순으로 정렬됨
- 설명: 리스트 제목 옆 괄호로 자주 쓴다. `by` 뒤에 정렬 기준을 넣어 "~순으로"를 표현한다.
- 예문: The concerns below are ordered by severity, with the most damaging one first.
- 유사어: sorted by severity, in order of priority (우선순위 순으로), ranked by impact (영향도 순으로)
- 반의어: in no particular order (특별한 순서 없이)

## "quarantined"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto_recipe_creator (모듈 분리 설명)
- 맥락: 위험하거나 플랫폼에 종속된 코드를 "한곳에 격리해 전파를 막는다"고 비유할 때(아키텍처 설명)
- 한국어: 격리된, 한곳에 가둬 둔
- 설명: 원래는 검역·격리. 코드 맥락에서는 의존성이나 위험을 한 모듈에 가둬 다른 곳으로 번지지 않게 한다는 뜻.
- 예문: The `rcs/` package (Windows-only, pywinauto/pynput) is quarantined, so nothing in `vision` drags in a Windows dependency.
- 유사어: isolated (분리된), sandboxed (샌드박스에 가둔), walled off (벽을 쳐 막은)
- 반의어: entangled / intertwined (서로 얽힌)

## "transitively pull in"
- 레지스터: technical
- 출처: transcript:[assistant] auto_recipe_creator (모듈 분리 설명)
- 맥락: 한 모듈을 import 하면 그 의존성이 줄줄이 따라 들어옴을 설명할 때(기술)
- 한국어: (의존성을) 간접적으로 줄줄이 끌어오다
- 설명: transitively 는 "추이적으로"(A가 B를, B가 C를 의존하면 A도 C에 의존). pull in 은 "끌어들이다".
- 예문: Importing the CV matcher would transitively pull in `pywinauto`, and nothing would run on your Mac.
- 유사어: drag in (더 구어; 같은 글에 함께 등장), bring along (딸려 오게 하다)

## "drill into / drill down"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-14-recipe-comparison-design.md
- 맥락: 요약·상위 뷰에서 세부 항목으로 파고들어 살필 때(UI·데이터 분석, 격식 중립)
- 한국어: (세부로) 파고들다, 드릴다운하다
- 설명: 데이터나 UI에서 개요→상세로 들어가는 동작. `into` 뒤에 대상을 쓰고, `down` 은 자동사적으로 쓴다.
- 예문: Show the overlap grid first, then let the user drill into a parameter's attribute matrix.
- 유사어: zoom in on (~을 확대해 보다), dig into (파고들다), expand (펼치다)
- 반의어: zoom out / roll up (상위 집계로 다시 올라가다)

## "reads like the README"
- 레지스터: conversational
- 출처: transcript:[assistant] auto_recipe_creator (모듈 분리 설명)
- 맥락: 코드나 문서가 군더더기 없이 의도가 술술 읽힌다고 칭찬할 때(구어, 동료에게 설명)
- 한국어: README 처럼 술술 읽힌다
- 설명: "X reads like Y" 는 "X가 Y처럼 읽힌다"는 가독성 비유. 코드가 설명문처럼 명료하다는 칭찬으로 쓴다.
- 예문: Read `monitor/cycle.py` and it reads like the README: detect, connect, correct, notify, record.
- 유사어: reads like prose (산문처럼 읽힌다), is self-documenting (코드가 곧 설명서), reads top-to-bottom (위에서 아래로 막힘없이)
- 반의어: reads like spaghetti (뒤엉켜 읽기 힘들다)

## "nudge (someone) toward"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-14-recipe-comparison-design.md
- 맥락: 강제하지 않고 슬쩍 어떤 선택으로 유도할 때(UX·제품 논의)
- 한국어: ~쪽으로 슬쩍 유도하다
- 설명: nudge 는 팔꿈치로 살짝 미는 동작. force(강제)와 달리 부드럽게 권유한다는 뉘앙스를 살린다.
- 예문: The UI nudges the user toward the distribution view once the count passes a threshold.
- 유사어: steer toward (~로 방향을 틀다), guide toward (이끌다), encourage (권장하다)
- 반의어: force / require (강제하다)

## "seeded from"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-14-recipe-comparison-design.md
- 맥락: 초기 상태를 다른 출처의 값으로 "씨앗처럼 미리 채워" 시작할 때(기술)
- 한국어: ~에서 초기값을 받아 채워진
- 설명: seed 는 "초기 데이터를 심다". `seeded from X` 는 X에서 가져온 값으로 시작 상태를 미리 채운다는 뜻.
- 예문: It is a persistent multi-select working set, seeded from the search page.
- 유사어: initialized from (~로 초기화된), populated from (~에서 채워진), pre-filled from (~로 미리 채운)
- 반의어: empty by default (기본적으로 비어 있는)
