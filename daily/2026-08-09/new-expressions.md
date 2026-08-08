# 2026-08-09 — 새 표현

## "smuggled in by implementation fiat"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 논의 없이 코드로 밀어 넣은 결정을 지적할 때. 리뷰 코멘트·설계 문서(격식).
- 한국어: 구현자 재량으로 슬쩍 밀어 넣은
- 설명: `fiat` 는 라틴어 "그렇게 되게 하라"에서 온 말로, 근거 없이 권한만으로 내리는 결정을 뜻한다. `smuggle`(밀수하다)과 붙으면 "몰래 들여왔다"가 되어, 결정 자체가 틀렸다고는 하지 않으면서 절차를 문제 삼는다. 사람을 비난하지 않고 경로를 비난하는 어법이라 리뷰에 얹기 좋다.
- 예문: Suppressing the badge may well be the right product call, but that call belongs in the spec — not smuggled in by implementation fiat.
- 유사어: slipped in without review (평이하고 직접적), decided by default (더 완곡, 아무도 안 정해서 그렇게 됐다는 뜻), by executive fiat (조직 결정에 쓰는 더 센 표현)
- 반의어: recorded with its reasoning

## "de-facto (threshold)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/03-fab-checkbox-picker-extraction.md
- 맥락: 문서에 없지만 팀이 실제로 지켜 온 기준을 가리킬 때. 코드 리뷰·회고(격식과 구어 양쪽).
- 한국어: 사실상의 (기준)
- 설명: 법률 라틴어 `de facto`(사실상) ↔ `de jure`(법적으로)의 짝에서 왔다. 규칙집에는 없어도 관행으로 굳은 선을 가리키므로, "규칙 위반"이라고 말하지 않고도 "우리는 늘 이 선에서 뽑아냈다"는 근거를 만들어 준다.
- 예문: Three copies is this codebase's de-facto extract threshold, so the third copy is where we pull the pattern out.
- 유사어: our working rule (회화체), the unwritten rule (관행임을 더 강조), established practice (더 격식)
- 반의어: de jure / codified in the style guide

## "a guaranteed recurring tax"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/02-shared-table-ui-map.md
- 맥락: 중복·부채를 방치하면 앞으로 계속 물게 될 비용이라고 설득할 때. 리팩터링 제안(격식).
- 한국어: 앞으로도 반드시 반복해서 낼 세금
- 설명: 유지보수 비용을 세금에 비유하는 어법으로, 한 번의 실수가 아니라 **주기적 지출**이라는 점을 강조한다. `guaranteed` 가 확률 논쟁을 미리 차단해서, "그럴 수도 있다"가 아니라 "이미 한 번 냈고 또 낸다"로 논지를 옮긴다.
- 예문: DESIGN.md sweeps are a recurring event in this repo, so the triplication is a guaranteed recurring tax.
- 유사어: an ongoing maintenance cost (중립적·격식), it keeps billing you (회화체·비유 유지), death by a thousand cuts (누적 피해를 강조하지만 원인이 흩어진 경우)
- 반의어: a one-time cost

## "it reads as precedent for X"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/design-tokens/02-recipe-tat-count-chip-off-zinc.md
- 맥락: 예외를 남겨 두면 다음 사람이 그걸 근거로 삼는다고 경고할 때. 규범 논쟁(격식).
- 한국어: 그게 다음 사례의 선례처럼 읽힌다
- 설명: `read as` 는 "그렇게 읽힌다 = 의도와 무관하게 그런 뜻으로 받아들여진다"는 뜻이다. 여기에 `precedent` 를 붙이면, 미룬 것을 허용으로 오해할 사람을 지목하지 않고도 방치의 비용을 말할 수 있다. `every day it stands` 처럼 시간 표현과 함께 쓰면 압박이 붙는다.
- 예문: The deferral is acknowledged, but every day it stands it reads as precedent for the next zinc usage.
- 유사어: sets a precedent (더 단정적·능동), sends the signal that … (의도 없는 메시지 전달을 강조), opens the door to (결과 쪽에 초점)
- 반의어: is clearly marked as an exception

## "a live risk, not a corner case"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/multi-fab/01-promote-redis-pair-exact-fab.md
- 맥락: "그건 극단적 상황 아니냐"는 반론을 미리 막을 때. 버그 우선순위 논쟁(격식·구어 모두).
- 한국어: 예외적 상황이 아니라 실제로 살아 있는 위험
- 설명: `corner case` 는 "이론상 가능하지만 현실에선 거의 없는 경우"를 뜻하고, 흔히 우선순위를 낮추는 근거로 쓰인다. `live` 를 앞세워 그 프레임을 뒤집는데, 보통 앞에 수치를 붙여야 힘이 실린다(여기서는 이름 겹침 20%).
- 예문: The ~20% cross-fab name overlap documented in the Phase B spec makes this a live risk, not a corner case.
- 유사어: this happens in production today (수치 없이도 강한 평서문), not hypothetical (짧고 회화적)
- 반의어: a theoretical edge case

## "without spec sanction"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/01-decide-mixed-fab-badge-suppression.md
- 맥락: 명세가 허락하지 않은 동작 변경을 지적할 때. 스펙 리뷰(격식).
- 한국어: 명세의 승인 없이
- 설명: `sanction` 은 명사로 "제재"와 "승인" 두 뜻을 다 갖는 특이한 단어인데, `without ... sanction` 형태에서는 늘 "승인" 쪽이다. 주어를 사람이 아니라 구현(the implementation)으로 두면, 누가 잘못했는지 따지지 않고 코드와 문서의 불일치만 남는다.
- 예문: The implementation narrows a shipped signal's behavior without spec sanction.
- 유사어: with no basis in the spec (더 평이), unsanctioned (한 단어, 더 딱딱함), off-spec (기술 구어)
- 반의어: as the spec mandates

## "a sound rejection"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/design-tokens/03-timeseries-lens-tabs-role-class.md
- 맥락: 남의 판단을 먼저 인정하고 나서 다른 문제를 짚을 때. 리뷰 코멘트(격식).
- 한국어: 타당한 거절(판단)
- 설명: 형용사 `sound` 는 "소리"와 무관하게 "논리에 빈틈이 없는"이라는 뜻이다(`a sound argument`, `sound reasoning`). 이 구를 양보절 앞에 세우면 상대의 결정을 존중한 채로 부작용만 문제 삼게 되어, 리뷰가 반박이 아니라 후속 조치 제안으로 읽힌다.
- 예문: `SkNavPill` was rejected for aria reasons — a sound rejection, but the geometry is now a second copy that drifts silently on any pill retone.
- 유사어: the right call (회화체), well-founded (더 격식), defensible (약한 인정 — "옹호할 수는 있다"는 뉘앙스)
- 반의어: a rejection that doesn't hold up

## "acknowledged intent, not accident"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/03-fab-checkbox-picker-extraction.md
- 맥락: 중복이 실수가 아니라 의도된 복제였음을 근거(커밋 메시지 등)로 확정할 때. 리뷰·감사 기록(격식).
- 한국어: 실수가 아니라 스스로 인정한 의도
- 설명: 두 명사를 `not` 으로 대비시켜 판정을 한 구에 담는 영어의 상투적 리듬이다(`X, not Y`). 여기서는 "몰라서 그런 게 아니다"를 증거와 함께 못 박아, 다음 문장의 요구(추출하자)에 정당성을 만들어 준다.
- 예문: The landing-page copy's own commit comment cites the pattern source — the duplication is acknowledged intent, not accident.
- 유사어: a deliberate copy (평이), done with eyes open (회화체), by design (중립적이라 비판 어조가 약함)
- 반의어: an oversight

## "a hand-maintained invariant"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/05-backend-shape-cleanups.md
- 맥락: 사람이 기억으로만 지키는 규칙이라 언젠가 깨진다고 말할 때. 코드 리뷰(격식·기술).
- 한국어: 사람 손으로 유지되는 불변식
- 설명: `invariant` 는 항상 참이어야 하는 조건이고, `hand-maintained` 는 그것을 강제하는 장치가 코드에 없다는 뜻이다. 뒤에 `holds only until …` 을 붙이는 게 이 표현의 짝인데, 깨지는 시점을 미래의 특정 사건으로 지목해 추상적 우려를 구체적 예측으로 바꾼다.
- 예문: A hand-maintained `image === images[0]` invariant holds only until the first consumer that forgets it.
- 유사어: enforced by convention only (더 격식), kept in sync by hand (평이), an unenforced contract (계약 어휘 쪽)
- 반의어: enforced at the type level

## "colocated per repo convention"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/02-equipment-endpoints-400-tests.md
- 맥락: 새 파일을 어디에 둘지 지시하면서 근거를 관례에 넘길 때. 티켓·작업 지시(격식·기술).
- 한국어: 저장소 관례대로 같은 자리에 두어
- 설명: `colocate` 는 "관련된 것을 물리적으로 같은 위치에 둔다"는 뜻으로, 테스트를 대상 코드 옆에 두는 관행을 가리킬 때 특히 자주 쓴다. `per` 는 "~에 따라"를 뜻하는 격식체 전치사라 `according to` 보다 짧고 지시문에 어울린다.
- 예문: Add the bad-`tool_slug` → 400 coverage for both equipment endpoints, colocated per repo convention.
- 유사어: keep it next to the code it tests (평이·회화), following the existing layout (더 완곡)
- 반의어: kept in a separate top-level test tree

## "shotgun across (two components)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/design-tokens/01-chip-dark-override-uses-token.md
- 맥락: 한 번의 변경이 여러 파일을 동시에 건드려야 한다고 말할 때. 리팩터링 논의(기술).
- 한국어: 한 번 고치려면 여러 곳에 흩어져 번진다
- 설명: 리팩터링 냄새 이름 `Shotgun Surgery`(산탄총 수술)를 동사로 쓴 용법이다. 산탄이 퍼지듯 수정이 흩어진다는 그림이 그대로 살아 있어, "중복이 있다"는 정적 서술을 "다음 작업이 비싸진다"는 동적 예측으로 바꿔 준다.
- 예문: The byte-identical pair in `NavPill.vue` means that retone already shotguns across two design-system components.
- 유사어: touch N files for one change (수치로 말하는 평이한 방식), ripple through (범위가 넓지만 비유는 더 약함)
- 반의어: land in one file

## "actively teaches the next session wrong"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/tiff-preview/03-preview-route-cleanups.md
- 맥락: 낡은 주석·문서를 "없는 것보다 나쁘다"고 판정할 때. 문서 품질 리뷰(격식).
- 한국어: 다음 세션에게 틀린 것을 적극적으로 가르친다
- 설명: `actively` 가 이 표현의 핵심으로, 방치(수동)와 오정보(능동)를 가른다. `teach ... wrong` 은 `teach someone wrongly` 가 아니라 목적어 뒤에 형용사를 붙인 구어적 결합인데, 문서가 사람처럼 행동한다고 두는 의인화가 지적의 날을 세운다.
- 예문: A docstring describing a removed fallback path actively teaches the next session wrong.
- 유사어: worse than no comment at all (평이하고 강함), misinforms whoever reads it next (더 중립적·격식)
- 반의어: correctly discloses what it does

## "the whole plumbing already exists"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (랜딩 페이지 다중 fab 선택)
- 맥락: 큰 기능처럼 보이는 요청이 실은 배선 한 줄이면 된다고 알릴 때. 작업 착수 보고(구어에 가까운 기술 어투).
- 한국어: 배관(하부 배선)은 이미 다 깔려 있다
- 설명: `plumbing` 은 눈에 보이지 않는 하부 연결 전체를 뜻하는 비유로, 배관처럼 "이미 벽 안에 있어서 새로 뚫을 필요가 없다"는 그림을 준다. 견적을 낮출 때 특히 유용한데, 남은 일이 무엇인지(여기서는 쓰기 쪽 연결)를 곧바로 지목하게 해 준다.
- 예문: `toolTypeHref()` already builds its URL from `buildFabSegment(store.fabs)` — the whole multi-fab plumbing exists, the landing page just writes to it through the single-fab shim.
- 유사어: the wiring is already there (더 평이한 같은 비유), it's all there under the hood (회화체), the substrate exists (격식이 과함)
- 반의어: this needs to be built from scratch

## "a poor carrier for X"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (사이드바 fab 색 통일)
- 맥락: 어떤 수단이 그 의미를 전달하기에 부적합하다고 설명할 때. 디자인 근거·기술 판단(격식).
- 한국어: X를 실어 나르기에 부적합한 수단
- 설명: `carrier` 는 신호를 실어 보내는 매체를 뜻해서, 판단의 초점을 "예쁘다/안 예쁘다"에서 "무엇을 전달하는가"로 옮긴다. 그래서 취향 논쟁을 피하면서 대안을 요구하기 좋고, 뒤에 이유(색조가 함께 변한다)를 붙이면 그대로 설계 원칙이 된다.
- 예문: Opacity is a poor carrier for "secondary" state on filled surfaces — it blends the row toward the background, changing perceived hue, not just intensity.
- 유사어: the wrong signal to use for … (평이), doesn't survive on a filled surface (구체적 조건을 앞세운 변형)
- 반의어: the right cue for X

## "the on-system move"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (사이드바 fab 색 통일)
- 맥락: 디자인 시스템·규약에 맞는 선택지를 가리킬 때. 디자인 리뷰(격식·구어 중간).
- 한국어: 시스템 안에서 정석인 방식
- 설명: `on-system` 은 `off-brand`(브랜드에서 벗어난)의 반대 방향 조어로, "우리가 이미 정한 어휘 안에 있다"는 뜻이다. `move`(수, 선택)와 붙어 "정석 수"라는 바둑·체스식 그림이 되니, 개인 취향이 아니라 규약을 근거로 대안을 권할 때 쓴다.
- 예문: If you ever do want the routed fab distinguished again, an edge/weight cue is the on-system move, not transparency.
- 유사어: the idiomatic choice here (기술 문서 쪽), what the design system already gives you (평이하고 길게 풀어쓴 형태)
- 반의어: off-system / ad-hoc

## "invent a second look"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (체크박스 드롭다운)
- 맥락: 기존 사례를 따르겠다고 밝히며 새로 만들지 않는 이유를 댈 때. 착수 보고(구어).
- 한국어: 두 번째 스타일을 새로 만들어 내다
- 설명: `look` 이 명사로 "겉모습·스타일"을 뜻하는 패션 어휘이고, `a second` 가 붙어 "같은 목적에 두 가지 모양"이라는 문제를 이름 붙인다. `rather than invent …` 형태로 쓰면 결정의 근거가 게으름이 아니라 일관성이라는 게 분명해진다.
- 예문: The repo already has a checkbox-dropdown precedent in `CompareToolPicker.vue`, so I'll follow that rather than invent a second look.
- 유사어: reuse the existing pattern (중립적·격식), roll our own (반대 방향의 관용구 — 직접 만든다는 뜻)
- 반의어: follow the existing precedent

## "poison (a stored value)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (M16 버그 수정)
- 맥락: 잘못된 값이 저장소에 남아 이후 세션까지 오염시킬 때. 버그 사후 보고(기술).
- 한국어: (저장된 값을) 오염시키다
- 설명: 캐시·localStorage처럼 다음 실행까지 살아남는 저장소에 잘못된 값이 들어간 상황을 가리킨다. 한 번의 실수가 아니라 **지속되는 상태**라는 점이 핵심이라, 뒤에 `permanently` 나 `until the user changes it` 같은 지속 표현이 자연히 따라붙는다. 조치 쪽은 `purge`(싹 비우다)와 짝을 이룬다.
- 예문: One visit to device-statistics poisoned the app-wide fab selection permanently, surfacing as a pre-selected M16 on the landing page.
- 유사어: corrupt the stored state (더 격식·중립), leave a bad value behind (평이), taint (더 격식이고 보안 문맥에서 흔함)
- 반의어: purge / clear the stored value

## "that write bought nothing"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (M16 버그 수정)
- 맥락: 문제를 일으킨 코드가 대가로 얻은 것도 없다고 결론 내릴 때. 원인 보고의 마지막 문장(구어에 가까움).
- 한국어: 그 쓰기는 아무것도 얻어 주지 못했다
- 설명: `buy` 를 "비용을 내고 무엇을 얻다"의 은유로 쓰는 어법이다(`what does this buy us?`). 부정형으로 쓰면 "위험만 있고 이득은 0"이라는 판정이 되어, 대안을 검토할 필요 없이 그냥 지우면 된다는 결론까지 한 문장에 담긴다.
- 예문: The page keeps its own fab in `useDeviceStatisticsPreferences`, so that global write bought nothing.
- 유사어: it served no purpose (더 격식·평이), all cost, no benefit (대비를 드러낸 변형)
- 반의어: that's what the write buys you

## "no orphaned wrapper is left holding the port"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (3000·5050 포트 종료)
- 맥락: 프로세스를 죽인 뒤 잔여물이 없음을 확인해 줄 때. 운영 보고(기술).
- 한국어: 포트를 붙잡고 남은 고아 프로세스가 없다
- 설명: `hold a port` 는 소켓을 계속 점유해 재시작을 막는 상태를 가리키는 관용구다. `orphaned`(부모가 먼저 죽어 홀로 남은)와 `wrapper`(npm 같은 껍데기 프로세스)가 합쳐져, "죽였다"가 아니라 "다시 켤 수 있다"까지 보증한다.
- 예문: Its npm parent also exited cleanly, so no orphaned wrapper is left holding the port.
- 유사어: nothing is still listening on that port (가장 평이하고 검증 가능한 표현), no stray processes remain (범위가 더 넓음)
- 반의어: something is still bound to the port

## "by the litmus test"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (FDC 탭 배치)
- 맥락: 미리 정해 둔 판별 기준을 적용해 분류를 정당화할 때. 디자인·설계 판단(격식).
- 한국어: (문서에 정해 둔) 판별 기준에 따르면
- 설명: `litmus test` 는 리트머스 시험지처럼 결과가 즉시 둘로 갈리는 단일 판별 기준을 뜻한다. `by the litmus test` 로 시작하면 판단의 주체가 내가 아니라 문서가 되어, 취향 논쟁 없이 분류를 확정할 수 있다.
- 예문: By the litmus test this is a NAVIGATE control — pressing it swaps the entire panel stack, not a filter.
- 유사어: the deciding question is whether … (기준을 문장으로 펼친 형태), the acid test (거의 같지만 "가혹한 시험"이라는 뉘앙스가 섞임)
- 반의어: it's a judgement call either way

## "One consequence worth stating plainly"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (M16 버그 수정)
- 맥락: 고쳤지만 사용자가 감수해야 할 부작용을 자진 신고할 때. 완료 보고 끝 문단(격식과 구어 중간).
- 한국어: 분명히 말해 둘 결과가 하나 있습니다
- 설명: `worth + -ing` 구문에 `plainly`(에두르지 않고)를 얹어, 나쁜 소식을 축소하지 않겠다는 태도를 문장 형식으로 표시한다. 완료 보고의 맨 끝에 두는 자리 관례가 있어서, 상대가 "숨긴 게 있나" 하고 되묻는 일을 미리 막는다.
- 예문: One consequence worth stating plainly: the key bump means everyone's remembered fab selection is cleared once on next load.
- 유사어: to be upfront about the trade-off (더 회화적), one caveat (짧지만 무게가 가벼움), for full disclosure (격식이 세고 다소 법률투)
- 반의어: (부작용을 언급하지 않고) it's fully fixed

## "that's the price of X"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (M16 버그 수정)
- 맥락: 선택한 해법의 대가를 인정하고 결정권을 넘길 때. 트레이드오프 설명(구어에 가까움).
- 한국어: 그게 X의 대가입니다
- 설명: 부작용을 변명하지 않고 값으로 환산해 제시하는 어법이다. 뒤에 `say the word if you'd rather …` 같은 선택지를 붙이는 게 정석인데, 그러면 "감수하자"는 통보가 아니라 두 안 중 하나를 고르라는 제안이 된다.
- 예문: That's the price of purging the bad values — say the word if you'd rather keep existing selections.
- 유사어: the trade-off is … (중립적·격식), you don't get one without the other (회화체)
- 반의어: there's no downside to this
