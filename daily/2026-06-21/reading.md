# 2026-06-21 — 정독

오늘 배치는 대부분 한국어 명세였지만, production-trust 플랜에 **양질의 영어 단락**이 하나 있어 정독 1로 인용합니다.
정독 2는 오늘의 표현(escape hatch / best-effort / abstain / trade-off)을 자연스럽게 엮은 **모범 단락(작성)** 입니다.

---

## 단락 1 — 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/plans/2026-06-10-production-trust-consensus-cache-and-decision-layer.md

> Many cycles raised the matcher score (ensemble C1/C2/C3 RRF + NCC rerank; consensus re-registration +0.442 in_topk in lab). Scores are high but **not enough for production**. Exploration found two structural gaps. The consensus cache is gathered but never consumed. The consensus build lives only in `poc/workflow_2/consensus_template.py` and is never imported by workflow_3. The biggest lab win is structurally disconnected from the production loop — likely *the* reason "high scores aren't enough": the office matches against drift-stale templates.

**문법·구조**:
- **현재완료 vs 단순과거의 대비**: 첫 문장 `Many cycles **raised** the score` 는 단순과거(완료된 일련의 사이클). 반면 `The cache **is gathered** but never **consumed**` 는 **현재시제 수동태**로 "지금도 계속 그런 상태"라는 *지속되는 사실*을 말합니다. 시제만으로 "한 번 일어난 일"과 "여전히 그런 구조"를 구분하고 있어요.
- **수동태로 책임자 숨기기**: `is gathered`, `is never imported`, `is structurally disconnected` — 누가 했느냐보다 **상태 자체**가 중요할 때 영어는 수동태를 씁니다. 기술 문서에서 "주어를 굳이 안 밝히는" 전형.
- **대시(—)로 결론 붙이기**: `...production loop **—** likely *the* reason...` 대시 뒤에 앞 문장의 **귀결·해석**을 답니다. 한국어의 "즉/다시 말해"에 해당. `*the* reason` 처럼 정관사 the 를 이탤릭으로 강조해 "바로 그 이유"라는 어감을 줍니다.
- **명사구 압축**: `drift-stale templates`(드리프트로 낡아버린 템플릿)처럼 명사 앞에 하이픈 복합어를 쌓아 한 덩어리로 만드는 건 영어 기술문의 핵심 압축 기법.

**핵심 표현**:
- *not enough for production* — "점수는 높지만 실전엔 부족하다". `good/high but not enough for X` 패턴은 "조건은 충족했으나 목적엔 모자라다"를 말할 때 매우 유용.
- *gathered but never consumed* — "모으기만 하고 쓰지는 않는다". 데이터·자원이 수집되되 활용 안 되는 상황의 정석 표현.
- *structurally disconnected from* — "구조적으로 ~와 단절돼 있다". 단순히 "안 쓴다"가 아니라 "설계상 연결 자체가 없다"는 더 강한 진단.

**격식 짝**:
- *The biggest lab win is structurally disconnected from the production loop.* (refined·문어)
  ↔ *The best thing we built in the lab just isn't wired into the real system.* (plain·회화, "wire into" = 배선처럼 연결하다)
- *Scores are high but not enough for production.* (refined)
  ↔ *The numbers look great, but they won't cut it in production.* (plain; "won't cut it" = 성에 안 찬다/기준 미달)

---

## 단락 2 — 모범 단락(작성)

> When a system can't be sure, the safest move is often to do nothing at all. Rather than click the wrong point, our gate will **abstain** and hand the case to an engineer. We keep one **escape hatch**, though: an operator can override the gate when they trust the match. Gathering fresh templates runs as a **best-effort** step — if it fails, the loop keeps the old cache and moves on, instead of crashing. None of this is free, so the office digest must report the full **trade-off curve**: every point we automate safely is weighed against every point we get wrong. Only once that curve looks healthy will we **green-light** the rollout.

**문법·구조**:
- **부정 주어 + 도치**: `**None of this is free**` 는 "이 중 어느 것도 공짜가 아니다". 부정어를 주어로 앞세워 단정적인 어조를 만듭니다.
- **`Rather than + 동명사`**: `Rather than **click**(ing) the wrong point` — "~하느니 차라리". 뒤 주절(will abstain)과 대비시켜 선택을 부각.
- **`Only once ... will we ~` 도치**: 문두에 제한 부사구(Only once that curve looks healthy)가 오면 주절이 **의문문 어순으로 도치**(will we green-light)됩니다. 격식 있는 영어의 강조 도치. = "그 곡선이 건강해 보여야 비로소 우리는 승인한다."
- **대시 + 콜론으로 부연**: best-effort 뒤 대시로 조건절을, trade-off curve 뒤 콜론으로 정의를 답니다. 둘 다 "한 호흡 멈추고 풀어 설명"하는 장치.

**핵심 표현**:
- *the safest move is to do nothing* — "가장 안전한 수는 아무것도 안 하는 것". 보류·기권의 가치를 설명할 때.
- *weighed against* — "~와 견주어 저울질되다". 득과 실을 대비하는 trade-off 의 단골 동사.

**격식 짝**:
- *Our gate will abstain and hand the case to an engineer.* (refined)
  ↔ *When it's not sure, the system just backs off and lets a person decide.* (plain; "back off" = 물러서다/손 떼다)
