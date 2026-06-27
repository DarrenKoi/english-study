<sub>2026-06-28 · 정독 — 흐름·문법·격식을 단락으로</sub>

## 단락 1

It's complementary, not a replacement. PixelRAG is a retrieval technique — it gives recall on layout and tables and charts that text-chunking flattens. But it produces no structured evidence, provenance, confidence, or roundtrip artifacts — exactly the things the existing plan exists to preserve. So the right shape is a hybrid two-arm retriever, which happens to be your home turf.

**문법·구조**: 짧은 단정문(`It's complementary, not a replacement.`)으로 결론을 먼저 던지고, 이어 근거를 푸는 *두괄식* 구성입니다. `X — it gives …`, `Y — exactly the things …`처럼 **대시(em dash)**로 부연을 붙여 문장을 끊지 않고 호흡을 이어갑니다. 핵심 연결어 **`But`**가 장점(recall)에서 한계(no provenance)로 방향을 틀고, **`So`**가 그 둘을 종합해 결론(hybrid)으로 데려갑니다 — *주장 → 그러나 한계 → 그래서 결론*의 3박자. 관계절 `that text-chunking flattens`는 앞의 layout/tables/charts를 한정해 "텍스트 청킹이 뭉개버리는 바로 그것들"로 좁힙니다.

**핵심 표현**: `the right shape is X`(올바른 형태·구조는 X다 — 설계 권고의 정석 문형), `which happens to be your home turf`(마침 그게 네 전문 분야다 — `happen to`로 "공교롭게도"의 뉘앙스).

**격식 짝**:
- refined: *It is complementary rather than a substitute; the appropriate architecture is therefore a hybrid two-arm retriever.* (작성)
- plain: *It's not a replacement — it works alongside what you have. So go with a two-arm setup; that's right up your alley.* (작성)

<sub>출처: transcript:[assistant] auto-recipe-creator (PixelRAG 적용 분석)</sub>

---

## 단락 2

Phase 1 shipped the contract, the two scoring methods, the combine step, and the visual layer, all stable. Phase 2 adds comparison bases — detectors — only; the scoring and rendering are reused unchanged. A detector takes domain items, computes a leave-one-out center per item, and bands the distance with the active method, returning a list of verdicts. Because the combine step already does worst-of severity with insufficient preserved, a point carrying peer, sibling, and shift verdicts becomes one badge with several reason lines for free — no new combine logic needed.

**문법·구조**: 인수인계(handoff) 글답게 **과거형(`shipped`)으로 끝난 일**, **현재형(`adds`, `takes`, `becomes`)으로 지금/앞으로의 일**을 시제로 또렷이 나눕니다. `comparison bases — detectors — only`는 대시 한 쌍으로 동격(=detectors)을 끼워 넣고 `only`로 범위를 좁힌, 압축된 영어. `takes … , computes … , and bands …`는 동사 3개를 **병렬**로 늘어놓아 한 동작의 절차를 한 문장에 담습니다. 마지막 문장은 **`Because …`** 종속절을 앞세워 원인을 먼저 깔고("이미 combine이 다 해주니까") 결과("배지 하나로 공짜")를 뒤에 둡니다.

**핵심 표현**: `reused unchanged`(고치지 않고 그대로 재사용 — 분사 두 개로 군더더기 없이), `for free`([[for free]] — 추가 작업 없이 거저 따라온다), `no new combine logic needed`(필요 없다를 명사구로 끝맺는 노트체).

**격식 짝**:
- refined: *Because the combine step already aggregates by worst-of severity, no additional logic is required.* (작성)
- plain: *The combine step already handles all that, so you get it for free — nothing new to write.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-27-anomaly-convention-phase2-handoff.md</sub>

---

## 단락 3

The methodological lesson is simple: compare rank-1, not in_topk. in_topk is a recall ceiling; rank-1 is what production actually ships, because the system repositions to one point. A high-in_topk, low-rank-1 result is a recall illusion — it is why the template-bank approach looked like a win until rank-1 was measured. This is exactly why the work pivoted to re-registration: the eval concluded that the remaining failures cannot be fixed in the matcher, so the ambiguous keys must be flagged instead.

**문법·구조**: 콜론(`:`)으로 교훈의 *결론*을 앞세우고, 세미콜론(`;`)으로 **대비되는 두 절**(ceiling ↔ what ships)을 한 문장에 균형 있게 묶었습니다 — 문장부호만으로 논리 구조를 보여주는 좋은 예. `it is why …`, `This is exactly why …`가 **인과를 가리키는 반복 패턴**으로, 앞 문장 전체를 받아 "그래서 ~한 것"이라 매듭짓습니다. 수동태 `until rank-1 was measured`는 *누가* 쟀는지보다 *언제까지 안 보였는지*에 초점을 둬 의도적으로 행위자를 흐립니다.

**핵심 표현**: `X is what production actually ships`([[X is what ships]] — 실전이 실제로 내보내는 건 X), `a recall illusion`([[a recall illusion]]), `looked like a win until …`(~하기 전까진 성공처럼 보였다 — 반전 서술의 정형).

**격식 짝**:
- refined: *The figure that governs production is rank-1, not in_topk; the latter is merely a recall ceiling.* (작성)
- plain: *Don't trust in_topk — rank-1 is what actually goes live. The rest just looks good on paper.* (작성)

<sub>출처: transcript:[assistant] auto-recipe-creator (golden_consensus_eval 결론)</sub>
