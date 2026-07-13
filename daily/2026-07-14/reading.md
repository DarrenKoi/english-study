# 2026-07-14 — 정독

## 단락 1

Part A — rebuild the MDC hardware tab around a per-tool timestamped history (시계열 sub-tab: 0°/90° x-y trajectory + per-axis trends; 비교 sub-tab: fleet boxplot replacing the matrix table). Part B — overlay BM/PM maintenance events as colored vertical markLines on every time-axis hardware chart, behind one page-level toggle (default ON). The Phase-1 Flask mock gains `build_mdc_history()` and re-anchors `bm_pm_mock` to the requested window `end` so markers land inside chart ranges. The frontend adds three pure utils, rebuilds `MdcPanel.vue` with 시계열/비교 sub-tabs, and threads a `maintenance-events` prop from `HardwareView` into the five chart panels. Response contracts keep the `docs`/`settings` shapes, so the office provider swap stays confined to the provider layer. MDC values sit at 1.0 ±0.55%, so `stableYRange` would flatten them — MDC charts use tight scaling.

**문법·구조**: 아직 만들지 않은 기능인데 gains / adds / rebuilds / threads / keeps 가 모두 **현재시제** — 설계 문서는 "완성된 세계"를 현재형으로 기술하는 관례를 따릅니다. 설계 결정 뒤에 그 효과를 붙이는 **so-결과절**이 세 번 반복되고("so markers land…", "so the swap stays confined…", "so `stableYRange` would flatten…"), 마지막 so-절 안의 **would flatten** 은 "만약 그걸 썼다면 뭉개졌을 것"이라는 반사실 가정입니다. 주어가 전부 무생물(The mock, The frontend, Response contracts)인 것도 영어 기술 문서의 전형입니다.
**핵심 표현**: *land inside chart ranges* (마커가 범위 안에 떨어진다), *stay confined to* (변경이 그 층 밖으로 안 번진다), *behind one page-level toggle (default ON)* (스위치 뒤에 배포), *thread a prop into* (값을 컴포넌트 사이로 꿰어 전달 — 기존 수집어 thread through 의 변형).
**격식 짝**: refined "The office provider swap **stays confined to** the provider layer." ↔ plain "Swapping in the office provider **only touches** the provider code." (작성) / refined "…**behind one page-level toggle (default ON)**." ↔ plain "There's **one switch for the whole page, and it starts out on**." (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-13-hardware-mdc-timeseries-and-bmpm-overlay.md (Goal·Architecture 발췌)</sub>

---

## 단락 2

Conversation memory does not survive compaction. In real sessions, controllers that lost their place have re-dispatched entire completed task sequences — the single most expensive failure observed. Track progress in a ledger file, not only in todos. Tasks listed there as complete are DONE — do not re-dispatch them; resume at the first task not marked complete. The ledger is your recovery map: the commits it names exist in git even when your context no longer remembers creating them. After compaction, trust the ledger and git log over your own recollection.

**문법·구조**: 둘째 문장의 **현재완료 have re-dispatched** 는 "과거 여러 세션에서 실제로 벌어졌고 지금 교훈으로 남았다"는 경험·결과의 완료입니다. 이어지는 동격구 "— the single most expensive failure **observed**"에서 observed 는 명사 뒤에 붙은 **후치 과거분사**(= that has been observed). 지침의 골격은 **명령문 연쇄**(Track / do not re-dispatch / resume / trust)이고, "the commits **it names**"는 관계대명사가 생략된 **접촉절**입니다. "not only in todos"처럼 not only 가 전치사구 하나만 부정해 대비를 만드는 용법도 눈여겨볼 만합니다.
**핵심 표현**: *survive* (does not survive compaction — 압축을 '살아남지' 못한다, 지속성의 동사), *lose one's place* (읽던·하던 자리를 놓치다), *trust X over Y* (충돌 시 신뢰 서열).
**격식 짝**: refined "After compaction, **trust the ledger and git log over your own recollection**." ↔ plain "Once things get squashed, **don't go by memory — check the ledger and the git log**." (작성)

<sub>출처: transcript:auto_recipe_creator 8909999c… (subagent-driven-development 지침 "Durable Progress" 발췌)</sub>

---

## 단락 3

Turn count beats token price. Wall-clock and context cost scale with how many turns a subagent takes, and the cheapest models routinely take 2-3× the turns on multi-step work — costing more overall. Use a mid-tier model as the floor for reviewers and for implementers working from prose descriptions. When the task's plan text contains the complete code to write, the implementation is transcription plus testing: use the cheapest tier for that implementer. Single-file mechanical fixes also take the cheapest tier.

**문법·구조**: 첫 문장 "**Turn count beats token price.**"는 관사 없는 명사구 둘을 beats 로 이은 **격언형 헤드라인** — 규칙을 먼저 못 박고 뒤에서 근거를 풉니다. "scale with **how many turns a subagent takes**"는 전치사 with 의 목적어 자리에 **간접의문 명사절**이 온 구조("~에 비례한다"). "— **costing** more overall"은 앞 절 전체의 귀결을 받는 **분사구문**이고, "use a mid-tier model **as the floor**"의 floor 는 '하한선' 비유입니다. take 가 두 용법으로 나옵니다: take 2-3× the turns(턴이 그만큼 든다) / take the cheapest tier(가장 싼 등급을 받는다).
**핵심 표현**: *X beats Y* (우선순위 격언), *scale with* (~에 비례해 커지다), *as the floor* (최소 기준선으로), *routinely* (예외가 아니라 으레).
**격식 짝**: plain(격언) "**Turn count beats token price.**" ↔ refined "**The number of turns a model takes is a stronger cost driver than its per-token price.**" (작성)

<sub>출처: transcript:auto_recipe_creator 8909999c… (subagent-driven-development 지침 "Model Selection" 발췌)</sub>
