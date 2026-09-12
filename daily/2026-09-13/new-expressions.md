# 2026-09-13 — 새 표현

## "have a shape the codebase already knows how to fill"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 설계 문서에서 "새로 만들 게 아니라 이미 있는 틀에 끼우면 된다"를 밝힐 때(격식·문어)
- 한국어: 이미 코드베이스가 채울 줄 아는 모양을 하고 있다
- 설명: 결함(gap)을 "구멍"이 아니라 "규격이 정해진 빈칸"으로 다시 정의하는 비유. 뒤에 보통 `but both have a trap in them` 같은 반전이 따라붙어, 쉬워 보이는 일의 함정을 소개하는 도입부로 쓴다.
- 예문: Both gaps have a shape the codebase already knows how to fill, and both have a trap in them.
- 유사어: fit an existing pattern (밋밋하고 중립적), be a solved problem here (더 단정적·구어에 가까움)
- 반의어: call for something we have never built

## "both have a trap in them"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md
- 맥락: 쉬워 보이는 두 선택지의 숨은 위험을 예고할 때(설계 리뷰·문어와 구어 모두)
- 한국어: 둘 다 함정이 하나씩 들어 있다
- 설명: `a trap` 을 셀 수 있는 명사로 쓰면 "어딘가에 하나 박혀 있다"는 구체성이 살아난다. 이어지는 소제목이 `The export trap` / `The API trap` 처럼 그 함정에 이름을 붙이는 식으로 전개된다.
- 예문: Both gaps have a trap in them, and the second one has already caused a silent wrong-answer bug.
- 유사어: there's a catch (구어·가벼움), come with a caveat (완곡·격식)
- 반의어: it's as simple as it looks

## "point at the same replacement"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 서로 다른 두 근거가 결국 한 결론으로 수렴한다고 못 박을 때(설계 근거·격식)
- 한국어: 서로 다른 문제가 같은 해법을 가리킨다
- 설명: `point at/to` 는 증거가 결론을 "가리킨다"는 뜻. 주어 자리에 근거 둘을 나란히 세우고 술어에 `the same` 을 두면, 결론이 저자의 취향이 아니라 증거의 수렴으로 읽힌다.
- 예문: The interface mismatch and the deployment cost point at the same replacement.
- 유사어: converge on the same answer (더 격식), both push us the same way (구어)
- 반의어: pull in opposite directions

## "collapse into one upstream call"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 동시 요청 여럿이 하나로 합쳐지는 캐시·락 설계를 설명할 때(기술 문서)
- 한국어: 여러 요청이 상위 호출 하나로 합쳐지다
- 설명: 자동사 `collapse into` 는 "무너져 하나가 되다" — 요청 병합(request coalescing)을 한 단어로 압축한다. 주어는 보통 사람·요청이고, 목적지가 `one …` 이라 절약이 곧바로 드러난다.
- 예문: Put a short Redis cache with a lock in front of it so that many viewers collapse into one upstream call.
- 유사어: coalesce into a single request (더 격식·정확), dedupe the fan-out (구어·엔지니어링 은어)
- 반의어: fan out into one call per viewer

## "is bounded at"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 최악의 경우 상한을 숫자로 약속할 때(성능·용량 설계, 격식)
- 한국어: (최대) 얼마로 상한이 걸려 있다
- 설명: `bounded at N` 은 "N 을 넘지 않는다"를 수학 어휘로 말한다. `limited to` 보다 단단하게 들리고, 뒤에 `regardless of …` 를 붙이면 "무엇이 변해도 이 상한은 유지된다"는 불변식 선언이 된다.
- 예문: Office API load is bounded at three calls per minute per facility, regardless of how many viewers there are.
- 유사어: is capped at (일상적·계약 문구에도 흔함), never exceeds (서술적)
- 반의어: grows with the number of viewers

## "the lone-visitor case reads well"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 설계가 극단 상황에서도 어색하지 않음을 밝힐 때(설계 리뷰·문어)
- 한국어: 방문자가 한 명뿐인 경우도 말이 된다
- 설명: `read well` 은 "읽어 보면 자연스럽다" — 코드·설계를 글처럼 다루는 비유다. 벤치마크가 아니라 납득 가능성을 근거로 삼는 자리에 쓴다.
- 예문: The lone-visitor case reads well: a single viewer arriving after an idle night wins the lock and receives a fresh board on that same request.
- 유사어: holds up under the edge case (검증 뉘앙스), makes sense on paper (구어·유보적)
- 반의어: the edge case reads badly

## "turns the parity suite red"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md
- 맥락: 순서를 어기면 CI 가 깨진다고 경고할 때(구현 지시·기술 문서)
- 한국어: (그 테스트) 스위트를 빨갛게 만든다 = 깨뜨린다
- 설명: CI 의 초록/빨강 색을 그대로 동사구로 쓴다. `break the suite` 보다 구체적이고, 실패를 화면에 보이는 사건으로 만들어 경고가 선명해진다.
- 예문: Deleting the writer package while the office template still imports it turns the parity suite red.
- 유사어: breaks the build (가장 흔함), takes CI down (과장된 구어)
- 반의어: keeps the suite green

## "the catalog just doesn't show it well"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73
- 맥락: 요청받은 기능이 이미 있고 문제는 노출뿐이라고 정정할 때(동료에게·반격식)
- 한국어: 목록이 그걸 제대로 보여 주지 못할 뿐이다
- 설명: `just` 가 문제의 크기를 깎는다 — "없는 게 아니라 안 보일 뿐". 앞에 `most of it is already built` 같은 인정을 세우고 `just` 로 잔여 과제를 축소하는 2단 구성이 요청 거절이 아닌 재조준으로 들리게 한다.
- 예문: Yes, and most of it is already built — the catalog just doesn't show it well, and one of its examples is broken.
- 유사어: it's a discoverability problem, not a feature gap (더 분석적·격식)
- 반의어: we'd have to build it from scratch

## "don't fail the rest"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73
- 맥락: 일괄 처리에서 일부 실패를 전체 실패로 번지지 않게 했다고 설명할 때(API 설계·기술 문서)
- 한국어: 일부가 실패해도 나머지까지 실패시키지는 않는다
- 설명: `fail` 을 타동사로 써서 "무엇이 무엇을 실패시킨다"는 인과를 한 단어에 담는다. 부분 실패(partial failure) 정책을 한 줄로 요약할 때의 정형구.
- 예문: Missing MSRs are left out and listed in `_skipped.json`, so a few deleted pickles don't fail the rest.
- 유사어: degrade gracefully (더 격식·일반론), the batch is best-effort (정책 용어)
- 반의어: one bad item fails the whole request

## "silently overwrite"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73
- 맥락: 경고 없이 데이터가 덮어써지는 위험을 테스트로 막았다고 말할 때(코드 리뷰·기술 문서)
- 한국어: 아무 말 없이 덮어쓰다
- 설명: `silently` 는 버그 어휘에서 "실패했는데 아무도 모른다"를 뜻한다. `silently overwrite` / `silent wrong-answer bug` 처럼 부사와 형용사 양쪽으로 쓰이며, 둘 다 "조용해서 더 위험하다"는 평가를 품는다.
- 예문: The test checks that one file doesn't silently overwrite the other when two MSRs return the same filename.
- 유사어: clobber (구어·강함), shadow (가리기만 할 때)
- 반의어: raise a conflict error

## "reading X as Y"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73
- 맥락: 짧은 대답을 어떻게 해석했는지 밝히고 작업에 들어갈 때(동료 간·반격식)
- 한국어: X 를 Y 로 받아들이고 (진행하겠다)
- 설명: 분사구문 `Reading … as …,` 를 문두에 두면 "이렇게 해석했다"를 선언한 뒤 곧바로 행동으로 넘어간다. 되묻지 않고도 오해의 책임 소재를 미리 정리하는 실무 화법.
- 예문: Reading "yes" as yes to both questions, I'll fix the example and build the bulk zip endpoint.
- 유사어: I'll take that as a yes (더 구어), on the assumption that … (더 격식)
- 반의어: just to be sure, which one did you mean?

## "the tail is just hook noise"
- 레지스터: technical, casual
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73
- 맥락: 로그 끝부분에 의미 있는 정보가 없다고 판단할 때(디버깅 중 구어)
- 한국어: 끝부분은 그냥 훅이 뱉은 잡음이다
- 설명: `noise` 는 신호(signal)의 반대말로 "봐도 소용없는 출력". `hook noise`, `log noise`, `CI noise` 처럼 앞에 출처를 붙여 조어하며, 불가산명사라 관사를 붙이지 않는다.
- 예문: I need to find what the review agent actually said, since the tail is just hook noise.
- 유사어: boilerplate output (중립·격식), chatter (구어)
- 반의어: the signal is in the tail

## "that only holds for …"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/7a2f8d37
- 맥락: 자기가 앞서 한 주장의 적용 범위를 스스로 좁힐 때(정정·격식 있는 구어)
- 한국어: 그건 ~인 경우에만 성립한다
- 설명: `hold` 는 "명제가 참으로 유지되다". 사과 없이 조건을 덧붙이는 방식이라 정정이 방어적으로 들리지 않는다. 뒤에 `because …` 로 왜 그 조건이 필요한지 잇는 게 관례.
- 예문: My earlier comment claimed the random stream stays stable, but that only holds for a fixed "today".
- 유사어: is true only under (더 문어적), breaks down once (반대 방향에서 같은 말)
- 반의어: that holds in general

## "deploy skew, not a contract state"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/7a2f8d37
- 맥락: 방어 코드가 실제로 막는 게 무엇인지 이름 붙여 구분할 때(코드 리뷰)
- 한국어: 계약상 있을 수 있는 상태가 아니라 배포 시차일 뿐이다
- 설명: `skew` 는 "서로 어긋난 상태" — `clock skew`, `deploy skew`, `version skew` 로 굳어졌다. `A, not B` 대조가 "그럼 다르게 대응해야 한다"는 결론을 자동으로 끌고 온다.
- 예문: The `?? []` covers only a stale office deployment; that is deploy skew, not a contract state.
- 유사어: a rollout artifact (완곡), version drift (장기간 어긋남)
- 반의어: a state the contract actually allows

## "not worth a diff"
- 레지스터: technical, casual
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/7a2f8d37
- 맥락: 지적은 맞지만 고칠 값어치는 없다고 닫을 때(리뷰 결론·구어)
- 한국어: 고쳐서 diff 를 남길 값어치는 없다
- 설명: 비용 단위를 "시간"이 아니라 "diff 한 줄"로 잡는 엔지니어 특유의 환유. `worth + 명사` 라 `worth to fix` 로 쓰면 틀린다.
- 예문: Every item is trivial at 90 cells; two are readability wins, and the rest is not worth a diff.
- 유사어: below the noise floor (성능 맥락), I wouldn't touch it (구어)
- 반의어: worth fixing now
