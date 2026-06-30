<sub>2026-07-01 — 정독</sub>

## 단락 1

The bank arms MUST reuse the SAME crop source and SAME GT as consensus — build the bank from the same crops the consensus median uses (history-first disjoint pool, else leave-one-out excluding the eval frame). This makes no-leakage identical by construction. Do NOT introduce a new crop/GT source. If the crop list and per-frame GT are NOT cleanly exposed at a single point in the loop, STOP and report your concern, describing exactly where they live and what's missing — do NOT guess or fabricate a parallel data path. A wrong wiring that silently mismatches GT would poison the office results. This honesty is explicitly more valuable than a plausible guess.

**문법·구조**: 명령문(imperative) 단락의 모범입니다. 주어 없이 동사 원형으로 시작하는 지시문(`build…`, `Do NOT introduce…`, `STOP and report…`)이 연속됩니다. 핵심은 **조건문의 결과 추론**: "If the crop list … are NOT cleanly exposed …, STOP" — 1형식 조건(현재시제 if절 + 명령문 주절). 마지막 두 문장은 **가정법적 would**가 인과를 만듭니다 — "A wrong wiring … *would* poison the office results"는 "(만약 잘못 연결하면) 결과를 망칠 것이다"라는 잠재적 결과. 그 뒤 "This honesty *is* … more valuable"는 다시 단정(현재시제)으로 돌아와 규범을 못박습니다. 강조 대문자(MUST·SAME·NOT·STOP)는 격식 문서에선 드물지만, 지시 사항에선 의도적으로 허용되는 장치입니다.

**핵심 표현**: `by construction`(설계상 자동으로 — "노력해서가 아니라 구조 자체가 그렇게 보장한다"), `fabricate a parallel data path`(별도 데이터 경로를 지어내다), `silently mismatch`(아무 신호 없이 어긋나다).

**격식 짝**:
- refined: *This honesty is explicitly more valuable than a plausible guess.*
- plain: *Saying "I'm not sure" beats making up an answer that just sounds right.* (작성)

<sub>출처: transcript:auto_recipe_creator (Task 7 브리프)</sub>

---

## 단락 2

Collateral damage: none. The diff is exactly one file, three insertions and three deletions, touching only the two described lines. Crop/GT source, history branch, no-data early returns, summary.json key names, print statements — none are in the diff. The fix is structurally consistent with clean test passage: the leave-one-out skip gate is now strictly less restrictive (`< 2` versus `< CONSENSUS_MIN_S`, where that floor is at least 3), meaning more frames evaluate rather than fewer, so no existing passing path could have been broken by the gate change.

**문법·구조**: 리뷰 결론을 압축하는 글의 좋은 본보기입니다. 첫 문장은 **명사구만으로 끝내는 단정**("Collateral damage: none.")으로 동사 없이 결론을 던집니다. 세 번째 문장은 **대시(—)로 주어를 나열한 뒤 "none are in the diff"로 받는 도치형 강조**: 길게 열거하고 마지막에 부정으로 정리하는 영어 특유의 리듬입니다. 마지막 문장이 압권으로, **비교급 + 분사구문 + 결과절**이 사슬처럼 연결됩니다 — "strictly less restrictive"(비교급) → "meaning more frames evaluate"(`-ing` 분사구가 앞 절 전체를 받아 부연) → "so no … path could have been broken"(결과). 여기 **could have been broken**은 "(만약 무언가 깨졌다면 깨졌을 텐데) 깨질 수 없었다"는 과거 가능성의 부정 — 수동태 가정법으로 안전성을 논증합니다.

**핵심 표현**: `strictly less restrictive`(엄밀히 말해 덜 제약적인 — 수학·코드 리뷰 상투구), `structurally consistent with`(~와 구조적으로 모순되지 않는), `more X rather than fewer`(더 적은 게 아니라 더 많은).

**격식 짝**:
- refined: *No existing passing path could have been broken by the gate change.*
- plain: *Loosening the gate only lets more cases through, so nothing that used to pass would suddenly fail.* (작성)

<sub>출처: transcript:auto_recipe_creator (재리뷰 결론)</sub>
