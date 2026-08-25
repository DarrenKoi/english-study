# 2026-08-26 — 정독

## 단락 1

**JUDGEMENT** — Scope-bar gating rule (DESIGN.md:177): the diff enrolls this page in "the scope-bar layout" (DESIGN.md:174) but not its gate — "the results area carries an explicit `AppEmptyState` naming the missing choice." The empty-scope state is still a plain `<span>…</span>`, and the empty-search state a `sk-body` `<p>`. Mitigating: `selectedTool` auto-falls-back to the first row (`HardwareView.vue:142-147`) and the watch at :169-179 re-seeds it, so an unscoped results pane is nearly unreachable in practice — the rule's substance (no zeroed card masquerading as a verdict) holds. Worth either an `AppEmptyState` for the zero-rows case or a one-line doc note that H/W gates by auto-selection.

**문법·구조**: 리뷰 finding 한 건이 "규칙 → 위반 사실 → 정상 참작 → 권고" 네 단계로 짜여 있다.
① 첫 문장은 `enrolls this page in A but not its gate` — 같은 동사에 목적어 둘을 `but not` 으로 걸어 "절반만 가입했다"를 만든다. 대시 뒤 인용은 규칙 본문을 그대로 붙여 리뷰어의 해석이 아님을 보인다.
② 둘째 문장은 `The empty-scope state is still a plain <span>, and the empty-search state a sk-body <p>.` — 뒤 절에서 동사 `is` 를 생략한 병렬(gapping). 같은 구조가 반복될 때 두 번째 동사를 지우면 두 사실이 한 쌍으로 묶여 읽힌다.
③ `Mitigating:` 한 단어 + 콜론이 방향을 튼다. 이어지는 문장은 `auto-falls-back … and … re-seeds it, so … is nearly unreachable` 처럼 사실 두 개를 `and` 로 쌓고 `so` 로 결론을 뽑는 구조다. `nearly` 와 `in practice` 가 각각 "완전히는 아님"과 "이론 말고 실제"를 맡아 과장을 막는다.
④ 대시 뒤 `the rule's substance (…) holds` 는 자구와 취지를 가르는 판정문. 괄호 속 `no zeroed card masquerading as a verdict` 는 규칙의 취지를 한 구로 요약한 명사구다 — `masquerading` 현재분사가 `card` 를 뒤에서 수식한다.
⑤ 마지막 문장은 주어 없이 `Worth either A or B.` 로 시작한다. 리뷰 코멘트 특유의 생략문으로, `It would be worth` 를 지운 형태. `either … or` 가 두 처방(코드 수정 / 문서 한 줄)의 무게를 같게 놓아, 구현자에게 선택을 넘긴다.

**핵심 표현**
- `enrolls this page in X but not its gate` — 어떤 계열에 넣으면서 그 계열의 의무는 빠뜨렸다.
- `nearly unreachable in practice` — 이론상 가능하지만 실제로는 거의 도달하지 않는 상태.
- `the rule's substance holds` — 자구는 어겼어도 규칙의 본뜻은 지켜진다(새 표현 참조).

**격식 짝**
- refined: An unscoped results pane is nearly unreachable in practice, so the rule's substance holds.
- plain: You basically can't get to an empty results pane, so we're still doing what the rule is actually for. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md</sub>

---

## 단락 2

**The old "1주 윈도우" was only a label.** The office adapters looked back 60 d (tttm) / 30 d (pm_planning) but capped at the **10 / 8 most recent runs per tool**, so the real window was "the last ten runs" and widening the lookback alone would not have gathered more evidence. Office adapters: lookback **and** run cap now move together — `window_days(weeks)` + `runs_per_tool(weeks) = 10×weeks` (tttm) / `8×weeks` (pm). `load_points` LRU raised 768→2048 so a 3-week pm-tune page (~970 pickles) doesn't evict itself. Default is 3주 per your first message; at the office that is ~3× the MinIO GETs of before on a cold load (cached after). If you'd rather default to 1주 and let users widen, it's a one-line change in `_analysis_window.py` + `utils/analysisWindow.ts`.

**문법·구조**: 요청("1주는 짧으니 3주로")을 받아 "전제가 틀렸다 → 그래서 이렇게 고쳤다 → 비용과 대안"으로 답하는 보고문이다.
① 첫 문장은 굵은 단정 `X was only a label.` 한 줄이다. 그다음 문장이 `looked back … but capped at …, so the real window was …` 로 근거를 대고, `would not have gathered` 가정법 과거완료로 "요청대로만 했다면 헛수고였을 것"을 말한다. 결론을 먼저, 근거를 뒤에 — 영어 기술 보고의 기본 순서다.
② `lookback and run cap now move together` 에서 `and` 를 굵게 친 이유는 그 접속사가 변경의 핵심이기 때문이다. 앞 문장에서 두 값이 따로 놀았다는 사실을 세운 뒤라, `now` 하나로 "전과 달리"가 전해진다.
③ `raised 768→2048 so a 3-week page doesn't evict itself` — `so (that)` 목적절에 재귀대명사 `itself` 를 써서 캐시가 제 항목을 밀어내는 자해적 상황을 그린다. 숫자와 화살표를 문장 안에 그대로 넣는 것도 변경 요약의 관례다.
④ 마지막 두 문장은 사용자에게 돌아온다. `per your first message` 로 기본값의 출처를 사용자에게 두고, `If you'd rather … , it's a one-line change` 로 대안의 비용을 미리 계산해 준다. `would rather` 가 상대의 선호를, `one-line` 이 비용을 각각 담아 결정을 쉽게 만든다.

**핵심 표현**
- `was only a label` — 이름표일 뿐 동작과 무관했다(새 표현 참조).
- `move together` — 두 값이 한 축으로 연동된다(새 표현 참조).
- `if you'd rather …, it's a one-line change` — 대안 제시와 비용 견적을 한 문장에.

**격식 짝**
- refined: Widening the lookback alone would not have gathered more evidence.
- plain: Just stretching the date range wouldn't have given us any more data. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66</sub>

---

## 단락 3

**The gap:** that's a property of the *current rule data*, not an *invariant of the engine*. `selectorMatches` (`ruleEngine.ts:283`) only skips a phase check when `s.phase_in` is absent — a cell with no `family` and `phase_in: ['PV']` would happily claim a Pool recipe. Since rule editing is open to users, that cell is authorable. Also, the mock builds `ctn_desc` from `family` and `phase` jointly, so it **never generates a Pool+PV string** — home development has never once seen this case. This is the classic "the data happens to be right, so the code was never asked to be" bug. The invariant lives in a comment in `rules.py` and in the shape of hand-written seed cells, not in the engine — so it survives exactly until someone edits a rule.

**문법·구조**: "지금은 맞게 동작한다"는 관찰에서 "그래도 고쳐야 한다"는 결론으로 가는 논증이다.
① 첫 문장은 `a property of A, not an invariant of B` — 명사구 둘을 `not` 으로 대비시켜 "우연 vs 보장"을 가른다. 이탤릭이 대비의 두 축을 짚는다.
② 둘째 문장은 현재형 사실(`only skips … when … is absent`) 뒤에 대시를 두고 가정법 `would happily claim` 으로 넘어간다. 시제 전환이 "지금 코드가 하는 일"과 "데이터만 바뀌면 벌어질 일"을 가른다.
③ `Since rule editing is open to users, that cell is authorable.` — `since` 이유절이 앞서고 주절은 형용사 하나(`authorable`)로 끝난다. `-able` 신조어는 기술 영어에서 "누군가 만들 수 있다"를 한 단어로 줄이는 흔한 장치다.
④ `Also, … jointly, so it never generates …` 는 두 번째 근거. `never once` 가 부정을 한 단계 더 세게 만들고, `home development has … seen` 처럼 환경을 주어로 세워 "집 환경에서는 재현 자체가 불가능했다"를 말한다.
⑤ 마지막 두 문장이 일반화다. 따옴표로 묶은 긴 절을 `the classic "…" bug` 의 수식어로 쓴 뒤, `lives in A and in B, not in C` 로 불변식의 소재지를 짚고 `so it survives exactly until` 로 수명을 못 박는다. `lives` 와 `survives` 라는 생존 동사 두 개가 코드를 시한부 생명체처럼 그려 위험을 실감나게 한다.

**핵심 표현**
- `a property of the data, not an invariant of the engine` — 우연한 데이터 모양과 코드 보장의 대비.
- `authorable` — 사용자가 만들어 낼 수 있는(따라서 언젠가 나타날) 상태.
- `survives exactly until` — 바로 그 사건까지만 살아남는다(새 표현 참조).

**격식 짝**
- refined: The invariant lives in a comment and in hand-written seed cells, not in the engine.
- plain: The only thing keeping this right is a comment and the way someone typed the seed data — the code itself doesn't check it. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87</sub>
