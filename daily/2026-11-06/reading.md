# 2026-11-06 — 정독

## 단락 1

One requested extension beyond the plan, and only this one: when a baseline is set, 위치 비교 (Position view) in set scope should be able to show a **baseline-versus-target delta map** — per site, target-group value minus baseline-group value — as a layer beside the existing set mean / σ maps. Site pairing must use the site key the set-scope position code already uses; a site present in only one group shows as no-data, never as zero. The delta colour scale is diverging and centred on zero; if no suitable `--sk-*` diverging tokens exist, reuse whatever the existing residual/centered layers use (see `components/ebeam/skewvoir/position/SpatialLayerMap.vue`) rather than inventing colours. If this extension turns out to need more than a modest addition, build S7 as planned, skip the extension, and say so in your report.

**문법·구조**: 첫 문장은 동사 없는 명사구 `One requested extension ..., and only this one` 을 콜론 앞에 세워 제목처럼 씁니다. 콜론 뒤 `when a baseline is set` 은 수동태 조건절입니다. 누가 설정하든 상관없고 "설정된 상태"만 중요하니 수동이 맞습니다. 대시 사이 `per site, target-group value minus baseline-group value` 는 delta map 을 수식처럼 풀어 주는 **동격 삽입구**입니다. 둘째 문장은 세미콜론으로 규칙 둘을 잇는데, `the site key the set-scope position code already uses` 는 관계대명사 that 이 빠진 목적격 관계절이고, `a site present in only one group` 은 형용사구 `present in ...` 이 뒤에서 명사를 꾸밉니다. 셋째 문장의 `whatever the existing ... layers use` 는 "기존 레이어가 쓰는 것이 무엇이든"이라는 복합관계대명사절이라 reuse 의 목적어가 됩니다. 마지막 문장은 조건 `If ... turns out to need` 뒤에 명령 세 개(build, skip, say so)를 순서대로 늘어놓아 **대안 경로**를 미리 정해 둡니다. 실패해도 할 일이 분명합니다.

**핵심 표현**:
- `shows as no-data, never as zero` — 결측과 0을 구분하라. `never` 가 `not` 보다 한 단계 강합니다.
- `reuse whatever ... use rather than inventing colours` — 새로 만들지 말고 있는 걸 써라. `rather than + -ing` 로 금지할 쪽을 동명사로 붙입니다.
- `turns out to need more than a modest addition` — 해 보니 생각보다 커지면. `turn out to` 는 "결과적으로 ~로 드러나다"입니다.

**격식 짝**:
- refined: "Should this extension prove to require more than a modest addition, it should be deferred and the omission noted in the report." (작성 — should 도치 조건문)
- plain: "If it gets big, skip it and just tell me." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96 (S7 지시서, 위치 비교 확장 단락)</sub>

---

## 단락 2

A suspect is exactly what the screen already marks: a target measurement outside its recipe's band (`TrendRow.out`), or a measurement with at least one FAILED / STOPPED point (the page already counts these for its `FAILED · STOPPED` KPI — reuse that definition). Do not add a new detection rule, threshold or score. A baseline measurement is never a suspect for being out of band (it is not judged against itself) but is still listed if it has FAILED / STOPPED points. Mixed-recipe groups: follow the screen — μ and band are per recipe; never pool recipes into one reference; say so in 요약.

**문법·구조**: 정의문은 `A suspect is exactly what the screen already marks` 로 시작합니다. `what` 이 이끄는 명사절이 보어이고, `exactly` 가 "더도 덜도 아니고 딱 그만큼"을 보장합니다. 콜론 뒤 `a ... measurement outside ..., or a measurement with ...` 는 전치사구가 명사를 뒤에서 꾸미는 꼴로 정의를 두 갈래로 나눕니다. 셋째 문장의 `is never a suspect for being out of band` 에서 `for + 동명사` 는 "~라는 이유로"입니다. 괄호 속 `it is not judged against itself` 는 수동태로 그 이유를 댑니다(기준 측정을 자기 자신과 비교할 수는 없으니까요). 이어지는 `but is still listed if ...` 는 주어를 반복하지 않고 동사구만 but 으로 붙였습니다. 마지막 문장은 명사구 + 콜론으로 상황을 먼저 띄우고, 세미콜론으로 짧은 명령 세 개를 연달아 놓습니다.

**핵심 표현**:
- `exactly what the screen already marks` — 화면이 이미 표시하는 바로 그것. 새 규칙을 만들지 말라는 뜻이 `exactly ... already` 에 담겨 있습니다.
- `is never a suspect for being out of band` — `for + -ing` 로 판정 이유를 콕 집어 제외합니다.
- `never pool recipes into one reference` — 서로 다른 레시피를 한 기준으로 섞지 마라.

**격식 짝**:
- refined: "Measurements are classified as suspect solely on the basis of criteria already displayed on screen; no additional detection rule is introduced." (작성)
- plain: "If the screen flags it, it's a suspect. Don't make up new rules." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (AFM 조사 묶음 지시서, Scope 2–3)</sub>

---

## 단락 3

The office's sixth reply settled the last open question about table A. In the planstep index, `det_fac_id` is not a fac-level code; it is the location of the tool that measured the step, so a step measured on an R4 tool inside the R3 fac shows as `R4`. There is no separate `fab_name` field, and none is needed: we join A to B on `det_fac_id` as it is, with no sem_list lookup. This also explains the R7QA / R7QC mismatch from the fourth reply. Table D reports a fac-level `fab_id`, so the two values were never comparable, and we never pool them into one key — A and D stay joined by `lot_cd` alone. All of this is as of 2026-11-05; if a later index splits the field again, we will say so in the next reply rather than patch the mock silently.

**문법·구조**: 첫 문장은 과거시제 `settled` 로 "6차 회신이 결론을 냈다"는 사건을 말하고, 이후는 지금도 참인 사실이라 현재시제로 바뀝니다. 둘째 문장은 `is not X; it is Y` 로 **부정 → 정정**을 세미콜론으로 붙이고, `the tool that measured the step` 이라는 주격 관계절로 위치의 정체를 밝힙니다. `so` 뒤의 `a step measured on an R4 tool` 은 과거분사가 명사를 뒤에서 꾸밉니다. 셋째 문장의 `and none is needed` 는 `no separate field` 를 대명사 none 으로 받아 "없고, 필요도 없다"를 짧게 이었습니다. 다섯째 문장은 `were never comparable`(과거부터 줄곧 비교 불가였다)과 `we never pool`(지금의 방침)을 나란히 둬 시제 차이로 원인과 대응을 가릅니다. 마지막 문장의 `as of 2026-11-05` 는 사실의 유효 시점을 못 박고, `rather than patch the mock silently` 는 하지 않을 행동을 원형으로 붙입니다(`will say ... rather than patch`).

**핵심 표현**:
- `shows as R4` — (값이) R4 로 나온다. 오늘 표현 `shows as no-data` 와 같은 자동사 용법입니다.
- `as it is` — 손대지 않고 그대로. `as is` 로 줄여 쓰기도 합니다.
- `as of 2026-11-05` — 이 날짜 기준. 나중에 바뀔 수 있다는 단서를 함께 답니다.

**격식 짝**:
- refined: "The field may be used without transformation; no join against sem_list is required." (작성)
- plain: "Just use det_fac_id straight — no need to look anything up." (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/office-migration/reply-device-statistics-families-261105-r2.md 내용을 오늘 표현으로 다시 씀</sub>
