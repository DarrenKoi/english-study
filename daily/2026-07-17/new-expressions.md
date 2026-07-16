# 2026-07-17 — 새 표현

오늘 배치는 전부 `skewnono_v3_nuxt` 프로젝트의 설계·계획 문서(영어)였습니다. spool 노트·대화 코칭 소재는 없어, 표현 추출과 정독 단락만 다룹니다.

## "read as (visually) identical / distinct"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: UI·디자인·글에서 "결과적으로 ~처럼 보인다/받아들여진다"고 말할 때(설계 근거·리뷰, 격식)
- 한국어: (결과적으로) ~처럼 보이다/읽히다.
- 설명: `read as X` 는 "실제로 그렇다"가 아니라 "보는 사람에게 X 로 **읽힌다/느껴진다**"는 지각(perception)의 뉘앙스. 주어는 사물(차트·문장)이고 사람이 아님에 주의.
- 예문: The two charts share the same layout, so they read as visually identical even though they show different data.
- 유사어: come across as (인상·느낌 강조, 회화), appear (중립·격식), look like (평이)
- 반의어: read as distinct (뚜렷이 구별되어 보이다)

## "opt out (of X) / opted out"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: 기본은 켜져 있고 특정 대상만 **명시적으로 제외**할 때(정책·설정, 격식)
- 한국어: (기본 적용에서) 빠지다/제외를 선택하다.
- 설명: 기본값이 "포함(opt-in)"일 때, 예외적으로 빠지는 것이 `opt out`. "unless explicitly opted out"처럼 수동태로 자주 쓰며, 명사·형용사형은 `opt-out`.
- 예문: All charts get the download button unless a component explicitly opts out with `disableDownload`.
- 유사어: exclude oneself (격식·중립), turn off / disable (기능 자체를 끄다, 기술), bow out (구어, 참여에서 빠지다)
- 반의어: opt in (스스로 포함을 선택하다)

## "bake in (a solid background)"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-chart-image-download-and-tat-colors.md
- 맥락: 나중에 바꿀 수 없게 **결과물에 붙박이로 넣을** 때(엔지니어링 구어)
- 한국어: (빼낼 수 없게) 굽듯이 고정해 넣다, 붙박이로 심다.
- 설명: 빵을 구우면 재료가 분리되지 않듯, 산출물에 값·설정을 영구히 포함시키는 비유. 투명 배경 대신 불투명 배경을 "구워 넣는다"처럼.
- 예문: Exported PNGs must bake in a solid theme background, or they come out transparent and look broken.
- 유사어: hardcode (값을 코드에 박다, 기술), embed (끼워 넣다, 중립), lock in (되돌릴 수 없게 확정하다)
- 반의어: keep configurable / leave dynamic (바꿀 수 있게 두다)

## "an acceptable trade-off"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: 단점을 알지만 **감수할 만한 절충**이라 판단할 때(설계 결정 근거, 격식)
- 한국어: 감수할 만한 절충/맞바꿈.
- 설명: `trade-off` 는 하나를 얻기 위해 다른 하나를 내주는 교환. `acceptable` 로 "그 손해는 받아들일 만하다"는 판단을 덧붙인 리뷰·설계 상용구.
- 예문: The overlay button covers a small corner of the chart — an acceptable trade-off for auto-injecting it everywhere.
- 유사어: a reasonable compromise (타협, 격식), a fair price to pay (구어), a worthwhile trade (가치 있는 맞바꿈)
- 반의어: a dealbreaker (받아들일 수 없는 결점), a non-starter (시작조차 못 할 안)

## "funnel (everything) through (a single X)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: 여러 경로를 **하나의 통로로 모아** 한곳에서 처리·통제할 때(아키텍처 설명)
- 한국어: 하나의 통로로 모으다/집중시키다.
- 설명: 깔때기(funnel)처럼 흩어진 것을 한 지점으로 모으는 비유. "모두 한곳을 거치니, 고치면 전부에 적용된다"는 단일 지점(single choke point) 논리를 표현.
- 예문: Because all charts funnel through `useEchart`, the download feature is added in one place and reaches every chart.
- 유사어: route through (경로를 통과시키다, 중립), channel through (통로로 흘려보내다), go through a single entry point (기술)
- 반의어: scatter across / duplicate everywhere (여러 곳에 흩뿌리다)

## "be torn down (together with X) / teardown"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: 리소스·리스너·DOM 을 생성 역순으로 **깔끔히 해체**할 때(수명주기 설명, 기술)
- 한국어: (자원을) 해체하다/정리하다. (명사) teardown = 정리 과정.
- 설명: `set up ↔ tear down` 짝. 버튼·이벤트 리스너를 차트와 "함께 tear down" 해 누수(leak)·중복을 막는다. 명사 `teardown` 은 셋업의 반대 단계.
- 예문: The button, its listener, and the style mutation are torn down together with the chart, so there are no leaked listeners.
- 유사어: dispose (of) (폐기, 기술), clean up (정리, 중립·구어), dismantle (해체, 격식)
- 반의어: set up / spin up (구성하다, 띄우다)

## "each hop / hop(ping) among (screens)"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-recipe-detail-header-and-parameter-sorting-design.md
- 맥락: 화면·페이지·상태를 짧게 **건너뛰며 오갈** 때(네비게이션 설명, 가벼운 기술 구어)
- 한국어: (한 번의) 이동/건너뜀. 이 화면 저 화면 옮겨 다니기.
- 설명: `hop` 은 "폴짝 뛰다"에서 온 가벼운 이동. `each hop preserves ...`처럼 "매 이동마다 ~를 유지한다"로 상태 보존을 말할 때 자연스럽다.
- 예문: Each hop among the three detail screens preserves the current `recipe_name` and the optional `set=1` query.
- 유사어: each navigation / transition (격식·중립), jump between (뛰어 오가다), switch between (전환)
- 반의어: (마땅한 대체 표현 없음)

## "a single source of truth"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-recipe-detail-header-and-parameter-sorting-design.md
- 맥락: 같은 데이터·정의가 **한 곳에만** 존재해 불일치를 막는다고 설계 원칙을 말할 때(격식)
- 한국어: 단일 진실 원천(정보가 한 곳에만 있어 그것이 유일한 기준).
- 설명: 라벨·경로·정의를 여러 곳에 복사하지 않고 한 정의(SSOT)를 재사용해, 한 번 고치면 전부 반영되게 하는 원칙. 소프트웨어 설계 상용구.
- 예문: The three destinations reuse `RECIPE_ROW_ACTIONS` so labels, icons, and paths have one source of truth.
- 유사어: a canonical definition (정본, 격식), the authoritative copy (권위 있는 원본), SSOT (약어, 기술)
- 반의어: duplicated / scattered definitions (곳곳에 복제된 정의)

## "collide with"
- 레지스터: professional, technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-chart-image-download-and-tat-colors-design.md
- 맥락: 두 요소·이름·일정이 같은 자리를 놓고 **부딪쳐 충돌**할 때(폭넓게)
- 한국어: 충돌하다, 겹쳐 부딪치다.
- 설명: 물리적 충돌뿐 아니라 UI 겹침·이름 중복·일정 겹침 등 은유로 널리 쓴다. `collide with the chart's own controls`처럼.
- 예문: An overlay button would collide with the chart's own corner controls, so those charts opt out.
- 유사어: clash with (부딪치다·안 어울리다, 구어·중립), conflict with (충돌, 격식), overlap with (겹치다, 중립)
- 반의어: coexist with (충돌 없이 공존하다), sit alongside (나란히 놓이다)

## "a singleton, injected once"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-chart-image-download-and-tat-colors.md
- 맥락: 앱 전체에서 **딱 한 번만** 만들어 공유하는 인스턴스를 말할 때(구현 설명, 기술)
- 한국어: 싱글턴(단 하나만 존재하는 인스턴스); 한 번만 주입되는.
- 설명: `singleton` 은 "전체에서 하나뿐"인 것. `injected once`, `guarded by an id`, `exactly once` 등과 짝지어 "중복 생성 방지"를 표현한다.
- 예문: A singleton `<style>` element is injected into the head exactly once, guarded by an id.
- 유사어: a shared instance (공유 인스턴스), one global copy (전역 단일본), created once and reused (한 번 만들어 재사용)
- 반의어: per-instance / one-per-X (인스턴스마다 하나씩)

## "unit-testable in isolation / test X in isolation"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-chart-image-download-and-tat-colors.md
- 맥락: 의존성을 떼어내 **다른 것과 분리한 채** 검증·검토할 때(테스트·분석, 격식)
- 한국어: 따로 떼어(고립시켜) 단위 테스트할 수 있는; ~을 독립적으로.
- 설명: `in isolation` = "다른 것에 얽매이지 않고 그 자체만". 순수 로직을 DOM/프레임워크에서 떼어 두면 `testable in isolation` 이 된다. 넓게는 "한 요인만 따로 보다"에도 쓴다.
- 예문: The filename logic is kept free of DOM and framework imports so it stays unit-testable in isolation.
- 유사어: on its own (그 자체로, 구어·중립), standalone (독립형, 기술), independently (독립적으로)
- 반의어: coupled to / entangled with (~에 얽혀 있는), only testable end-to-end (전체를 띄워야만 검증되는)

## "retain source order (for stable, predictable results)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-recipe-detail-header-and-parameter-sorting-design.md
- 맥락: 정렬 시 **값이 같은 항목은 원래 순서를 유지**한다고 명세할 때(안정 정렬, 기술)
- 한국어: (동순위는) 원래 순서를 유지하다 — 안정적이고 예측 가능한 결과를 위해.
- 설명: 안정 정렬(stable sort)의 정의. `retain/preserve source order`, `equal values keep their original order` 로 표현하며, 결과가 매번 같아 `predictable` 하다는 점을 강조한다.
- 예문: Equal values retain their source order, so the sort is stable and predictable.
- 유사어: preserve the original order (원 순서 보존), keep ties in place (동순위를 제자리에), a stable sort (안정 정렬)
- 반의어: reorder arbitrarily / an unstable sort (동순위를 뒤섞는 불안정 정렬)
