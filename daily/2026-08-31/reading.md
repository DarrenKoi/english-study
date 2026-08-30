# 2026-08-31 — 정독

## 단락 1

`FeatureTabs.vue` decided the active tab with its own `path.includes()` if-chain ending in an unconditional fallback. `/pm-planning` had no branch, so it fell through to the default and lit 장비 상태. `/tttm` *did* have a branch — which is exactly why you only saw it on pm-planning. The if-chain was a recurring bug, not a one-off. Its own comments record the previous two rounds — `live-alarm` got a line "so no tab highlights on that page", `tttm` got another. Each new page paid the same tax, and `pm-planning` was the first one to forget. A fallback that means 장비 상태 makes silence the failure mode: forget a branch and you don't get a blank tab bar, you get a confidently wrong one.

**문법·구조**: 원인 보고문의 표준 골격이다. 첫 문장은 단순과거 `decided` 로 버그가 있던 코드의 동작을 사실로 서술하고, 현재분사구 `ending in an unconditional fallback` 이 관계절(`which ends in…`)을 대신해 문장 끝에 결정적 조건을 얹는다. 둘째 문장의 `so` 는 앞 문장 전체를 원인으로 받아 결과를 잇고, `fell through` 와 `lit` 이 같은 주어의 연속 동작으로 병렬을 이룬다. 셋째 문장 `/tttm` **did** have a branch 의 `did` 는 강조 조동사다 — 상대가 "왜 tttm 은 멀쩡하냐"를 묻기 전에 그 예외를 먼저 인정하고, 대시 뒤 `which is exactly why…` 로 그 예외를 오히려 증거로 되돌린다. 넷째 문장의 `A, not B` 는 이 단락의 논지이고 이후 문장들이 그 근거다. 다섯째 문장에서 주어를 코드가 아니라 `Its own comments` 로 옮긴 덕에 "코드가 스스로 증언한다"는 그림이 서고, 마지막 문장은 콜론 뒤에 명령형 `forget a branch and…` 를 놓아 조건절 없이 조건을 만든다(= if you forget a branch). `you don't get X, you get Y` 대구가 마지막 판정을 만든다.

**핵심 표현**: `fall through to the default` — 어느 분기에도 걸리지 않아 기본값으로 흘러가다. `a recurring bug, not a one-off` — 재발하는 구조적 결함이지 한 번의 실수가 아니다. `a confidently wrong one` — 자신 있게 틀린 답(빈 화면보다 나쁘다).

**격식 짝**:
- refined: *The absence of a matching branch caused the path to resolve to the default, which the tab bar renders as an active state.* (작성)
- plain: *There was no branch for it, so it just fell through and lit the wrong tab.* (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl</sub>

---

## 단락 2

The cleanup itself is sound — the hoists into `_core/timefmt.py` and `_shared.py` all landed correctly, and mock and office_example both call the shared forms. What it missed: contract drift. The backend half of three payloads was deleted, the frontend types weren't. Verified by grep: no runtime reads of any of these, so removal is type-only, no behaviour change. This comment now *lies* — "The backend still ships `defaults.focus_n`" was the documented reason to leave the contract alone, and the same change-series removed it. Rewrite or delete; leaving it invites someone to "restore" the field. Not swap-safe: `_format_iso` takes KST-aware inputs, so the existing `.replace("+00:00","Z")` is a no-op and `iso_z` would silently convert to UTC.

**문법·구조**: 남의 작업을 리뷰할 때의 순서가 그대로 드러난다. 잘된 점을 먼저 완결된 문장으로 인정하고(`is sound`), 그다음 `What it missed:` 라는 명사절 하나로 방향을 튼다 — 의문사절을 주어 자리에 세우면 "무엇을 놓쳤는가"가 제목이 되어 뒤 내용이 목록처럼 읽힌다. 셋째 문장의 `the frontend types weren't` 은 반복을 피한 생략(`weren't deleted`)이고, 이 비대칭이 곧 지적 내용이다. `Verified by grep:` 은 주어와 동사를 지운 과거분사 머리로, 판정 앞에 확인 방법을 먼저 대는 리뷰 관례다. `Rewrite or delete;` 는 명령형 두 개를 세미콜론으로 근거와 이어 붙였다 — 세미콜론 뒤가 마침표였다면 "왜"가 별개 주장이 되지만 이렇게 붙이면 지시와 근거가 한 판정이 된다. 마지막 문장의 `so … and …` 는 원인 하나에서 결과 둘이 갈라져 나오는 구조인데, `would silently convert` 의 would 가 "아직 안 일어났지만 바꾸면 일어날 일"이라는 가정을 담는다.

**핵심 표현**: `the hoists … all landed correctly` — 위 계층으로 끌어올린 코드가 제자리를 잡았다. `Verified by grep:` — grep 으로 확인함(근거 표기). `a no-op` — 실행돼도 아무 효과가 없는 코드.

**격식 짝**:
- refined: *Removing these fields is type-only; no runtime consumer reads them.* (작성)
- plain: *Nothing actually reads them, so ripping them out changes nothing.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md</sub>

---

## 단락 3

18 of about 30 top-level consts are the same name computing the same thing — the entire analysis pipeline. Four of the six bars are the same components fed from the same `useTttmScope` entry, and five of the empty states are the same. `PmPlanningView.vue` carries eight comments saying "same as TttmView" — duplication documented in prose rather than removed. The route is not the page; routes here are identity, not just navigation. My recommendation is to keep both URLs and merge the implementation — one view component with a `view` prop, plus a sub-tab bar copied from the 장비 상태 pattern. Both slugs survive, so no backend, logging or nav churn, one request serves both views, and the tolerance knob becomes a real shared control instead of an instruction to go elsewhere.

**문법·구조**: 수치를 앞세워 판단을 뒤로 미루는 설득 순서다. 앞 세 문장은 전부 `N of M are the same` 꼴로 같은 틀을 반복하는데, 문장마다 세는 대상만 바꿔(consts → bars/empty states → comments) 근거가 쌓이는 느낌을 만든다. 셋째 문장의 대시 뒤 `duplication documented in prose rather than removed` 는 동사 없는 명사구 판정 — 앞 사실에 이름을 붙여 주는 자리라 문장으로 늘리지 않는 편이 강하다. 넷째 문장 `The route is not the page; routes here are identity, not just navigation` 은 세미콜론으로 두 격언을 붙인 형태이고, `not just` 가 "그것도 맞지만 그게 다가 아니다"를 담아 반박을 미리 흡수한다. 다섯째 문장은 `My recommendation is to…` 로 권고를 명시적으로 표지한다(앞의 사실 진술과 섞이지 않게 하는 장치다). 마지막 문장의 `so` 뒤에는 결과 세 개가 콤마로 늘어서는데, 끝을 `instead of an instruction to go elsewhere` 로 닫아 개선 전 상태를 한 번 더 대비시킨다.

**핵심 표현**: `computing the same thing` — 이름도 계산 내용도 같다. `fed from the same entry` — 같은 진입점에서 데이터를 받는. `an instruction to go elsewhere` — 다른 화면으로 가라는 안내(기능 대신 놓인 문구를 비꼬는 말).

**격식 짝**:
- refined: *I would retain both URLs and consolidate the implementation behind a single view component.* (작성)
- plain: *Keep both links, but make them one page underneath.* (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl</sub>

