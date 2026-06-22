# 2026-06-23 — 정독

## 단락 1

A recipe comparison service at `/ebeam/{cd-sem,hv-sem}/<fab>/recipe-search/compare`. Engineers multi-select recipes on the existing search page (a persistent "working set"), then compare them: an **overlap grid** (which parameters exist in which recipes) drilling into a **parameter attribute matrix** with **slot tabs**, **image thumbnails + lightbox**, a **나란히 (side-by-side) ⇄ 분포 (value-grouping/outlier)** view toggle, a **차이만 보기** (differences-only) filter, and **client-side Excel export**. Targets ~100 recipes via one batch backend request plus pure client-side derivations.

**문법·구조**: 이 단락의 첫 문장은 **동사가 없는 명사구**("A recipe comparison service at ...")입니다. 기능 명세서·요약에서 흔한 *headline 문체* — "이것이 무엇인가"를 동사 없이 명사로 못 박습니다. 두 번째 문장이 진짜 주어-동사 골격을 끌고 가는데, **현재시제 present simple**("multi-select ... then compare ... Targets ...")로 일상적·반복적 동작을 서술합니다(설명문의 기본 시제). 콜론(`:`) 뒤는 "compare 가 구체적으로 무엇인지"를 **목록으로 펼친 동격 구조**이고, 그 안에서 `drilling into ...` 는 앞 명사(overlap grid)를 꾸미는 **현재분사 후치수식**("~로 파고드는")입니다. 마지막 문장의 주어 생략("Targets ~100 recipes ...")도 명세서 특유의 *telegraphic style* — 주어 The service 를 생략해 밀도를 높입니다.

**핵심 표현**:
- **working set** — 사용자가 모아 둔, 작업 대상 묶음. "a persistent working set"처럼 *persistent*(새로고침·페이지 이동에도 살아남는)와 자주 붙습니다.
- **drill into** — 요약에서 세부로 파고들다. UI 에서 "상위 표 → 클릭 → 하위 상세"의 그 동작.
- **via ... plus ...** — "~을 통해, 그리고 ~로". 수단을 압축해 나열할 때.

**격식 짝**:
- refined: *The service targets roughly one hundred recipes through a single batch request and purely client-side derivations.* (작성)
- plain: *It handles about 100 recipes — one backend call, the rest done in the browser.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-14-recipe-comparison-build.md</sub>

---

## 단락 2

A new Flask feature folder serves a raw 3-tier skew contract from deterministic JSON fixtures (no real statistics — office swaps `data.py` later). The Nuxt page fetches that raw payload once and does **all grouping on the client**: a pure TS util computes maximal cliques at the current tolerance, picks the primary answer by the tiebreakers, and the UI redraws instantly when the tolerance knob moves — no refetch. Phase-1 proves **contract + UX only**; correctness of recommendations is verified later with office data.

**문법·구조**: 세 문장 모두 **현재시제**로 시스템의 *항구적 동작*을 적습니다("serves / fetches / computes / redraws"). 시스템 설명을 미래("will serve")가 아니라 현재로 쓰는 게 영어 기술문서의 관례입니다. 두 번째 문장의 콜론(`:`)은 앞의 추상("all grouping on the client")을 뒤에서 **세 동작으로 구체화**하는데, `computes ... , picks ... , and ... redraws` 로 **동사 병렬(parallelism)**을 맞춰 리듬을 줍니다. 대시(`—`) 뒤의 "no refetch"는 **결과를 한 마디로 못 박는 강조** 삽입구입니다. 마지막 문장의 세미콜론(`;`)은 "이건 증명하고 / 저건 나중에"라는 **대비된 두 절을 한 문장에** 묶고, 뒷절은 **수동태**("correctness ... is verified later")로 행위자(office)보다 *대상(정확성)*에 초점을 둡니다.

**핵심 표현**:
- **deterministic fixtures** — 매번 같은 값을 주는 (랜덤이 아닌) 고정 테스트 데이터.
- **redraw instantly — no refetch** — 서버 재요청 없이 화면만 즉시 다시 그린다. 클라이언트 계산의 장점을 압축한 표현.
- **prove X only** — "X 까지만 증명한다(그 이상은 아직 아니다)"라고 범위를 좁히는 겸손한 한정.

**격식 짝**:
- refined: *Phase-1 establishes only the contract and the user experience; the correctness of the recommendations is validated subsequently against office data.* (작성)
- plain: *Phase-1 just nails down the contract and the UX — we'll check if the picks are right later, with real data.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-05-31-tool-skew-mgmt.md</sub>
