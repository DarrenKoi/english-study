# 2026-08-19 — 정독

## 단락 1

The gated page fetches 44 KB to use 1.2 KB. Measured against the running mock: the full `tttm/check` payload is 44,053 bytes, and while gated the only part rendered is `tools` at 1,182 bytes — the roster feeding the model-group dropdowns. The other 97% (matrices, trend, mdc_history, occupied_cells) is fetched and discarded on every cold load. The fetch is still necessary — gating it leaves nothing to pick from — but "necessary" only covers the roster, not the rest. A roster-only endpoint would fix it properly; I didn't invent one, and it's not free at the office where this becomes a real Redis read.

**문법·구조**: 첫 문장이 결론이고 나머지가 근거다. `Measured against the running mock:` 는 주어 없는 과거분사구로 시작해 콜론으로 수치를 쏟는데, 격식 있는 보고문이 "제가 측정해 보니"를 지우는 방식이다. 3문장의 `is fetched and discarded` 는 수동태 — 누가 버리는지가 아니라 데이터가 어떻게 되는지가 요점이라 행위자를 지웠다. 4문장은 `still necessary ... but "necessary" only covers` 로 자기가 방금 쓴 단어에 따옴표를 씌워 되받는다. 상대의 예상 반론("그래도 필요하잖아")을 먼저 꺼내 범위를 좁히는 수법이다. 마지막 문장의 세미콜론은 "제대로 된 해법은 이것 / 다만 내가 한 건 아님"을 한 호흡에 붙여, 변명이 아니라 인계로 읽히게 한다.

**핵심 표현**: `fetches 44 KB to use 1.2 KB` — 숫자 두 개의 대비만으로 낭비를 증명하는 제목형 문장. `on every cold load` — 한 번이 아니라 매번임을 못박는 부사구. `it's not free at the office` — 비용을 "돈"이 아니라 `free/not free` 로 말하는 개발 관용.

**격식 짝**: (작성)
- refined: The payload is fetched in full and largely discarded while the view remains gated.
- plain: We pull the whole thing and throw almost all of it away until you pick something.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (assistant)</sub>

---

## 단락 2

DESIGN.md §Layout documented the rail as an agreed pattern, "do not revert." I added a scope-bar rule beside the rail rule rather than silently contradicting it — code-only would have left the next session reading the doc as source of truth and railing it back. The rule states the two conditions that make a bar right over a rail (results are gated; scope fits ~3 cells), so it's a decision procedure, not a description of these two pages. 1440px is kept but on a new justification. The old one was "list-plus-detail"; that's gone. It now rests on the results themselves — four rows of paired cards, and 1280px pushes the pairwise matrix off a 1080px screen. I confirmed that visually.

**문법·구조**: 시제가 세 층으로 갈린다. 과거(`documented`, `added`)는 이미 벌어진 일, 가정법 과거완료(`would have left`)는 하지 않은 선택의 결과, 현재(`states`, `rests`)는 지금 유효한 규칙. 안 한 선택을 가정법으로 말하는 이 층위 덕분에 "왜 문서까지 고쳤나"가 설득된다. `rather than silently contradicting it` 은 전치사 뒤 동명사로 대안을 붙이는 정형구다. `railing it back` 은 명사 `rail` 을 동사로 굴린 즉석 조어인데, 앞에서 명사로 정의해 뒀기에 통한다. 마지막 네 문장은 짧게 끊으며 리듬을 바꾼다 — 긴 논증 뒤 짧은 확인문(`I confirmed that visually.`)이 마침표 역할을 한다.

**핵심 표현**: `a decision procedure, not a description` — `A, not B` 대구로 규칙의 성격을 규정. `on a new justification` — 결론은 그대로 두고 근거만 갈아 끼웠음을 밝히는 전치사구. `pushes X off a 1080px screen` — 추상적 "안 맞는다" 대신 물리적 동사로 증상을 말한다.

**격식 짝**: (작성)
- refined: The documented rule and the shipped code must not diverge; I amended the former alongside the latter.
- plain: If I change the code and leave the doc alone, someone will just put it back.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (assistant)</sub>

---

## 단락 3

Two findings share one shape. `recent_runs` detects truncation via `doc_count > len(hits)` and surfaces it; `_bsm_by_tool` caps its hits at forty and says nothing. Same smell, lower risk applies to the third case, where the cap is unlikely to bite — but the pattern was not applied there either. What checks out is the harder half: every exact-match field uses its `.keyword` sub-field, and archive dates are discovered rather than computed. The gap is not knowledge, then, but reach: a convention the author clearly holds was carried into one function and not the next two. That is the cheapest kind of defect to fix and the easiest to miss, because each site reads fine on its own.

**문법·구조**: 첫 문장이 논지고, 세미콜론으로 이은 두 절이 대조 증거다 — `detects ... and surfaces it` 대 `caps ... and says nothing`. 동사 구조를 일부러 평행하게 맞춰 차이가 마지막 동사 하나에 몰리게 했다. `The gap is not knowledge, then, but reach` 는 `not A but B` 구문 가운데에 `then`(그렇다면)을 끼워 결론을 늦추는 문어체 리듬이다. 관계절 `a convention the author clearly holds` 는 목적격 관계대명사를 생략했다 — 격식체에서도 목적격은 흔히 지운다. 마지막 문장의 `the cheapest ... and the easiest ...` 최상급 두 개를 붙인 대구는 판정을 기억에 남기는 마무리 장치다.

**핵심 표현**: `two findings share one shape` — 개별 지적을 한 패턴으로 묶는 도입. `unlikely to bite` — 결함이 실제로 문제를 일으키는 것을 `bite` 로 말하는 구어적 비유. `reads fine on its own` — 개별로는 멀쩡한데 모아 보면 어긋난다는 뜻.

**격식 짝**: (작성)
- refined: The convention was established but not propagated to every call site.
- plain: They knew the rule — they just didn't carry it to the other two spots.

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/opencode/2026-08-18-office-tttm-pm-adapters-review.md 의 지적들을 재구성</sub>
