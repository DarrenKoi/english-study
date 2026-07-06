# 2026-07-07 — 정독

## 단락 1

The 'orb_flip' category was introduced specifically to prove ORB was harmful (27% flip rate) and justify replacing it with NCC. Now that NCC selection is production code, this category diagnoses a code path that no longer exists in the ensemble entrypoint. Re-running this diagnostic will produce 'orb_flip' counts against a reconstructed-ORB pool that diverges from production — an engineer interpreting those counts as evidence about the current system will draw incorrect conclusions, incorrectly attributing regressions to ORB when the production function no longer uses ORB for selection. The diagnostic runner was designed as evidence for removing ORB; now that ORB selection is gone from production, its output measures the ghost of the old system.

**문법·구조**: 첫 문장은 수동태 `was introduced ... to prove ... and justify`(도입 목적을 to-부정사 두 개 병렬로). `Now that + 절`이 두 번 반복되며 "상황이 바뀐 지금은"이라는 전환 프레임을 만든다. `an engineer interpreting those counts ...`는 관계절 대신 **현재분사 후치수식**으로 주어를 압축한 뒤, 문장 끝에 분사구문 `incorrectly attributing ...`을 얹어 결과를 이어붙였다 — 격식 리뷰 문체의 전형. 세미콜론은 "설계 의도 ; 현재의 무의미함"의 대비를 한 문장에 담는다.
**핵심 표현**: `diagnose a code path that no longer exists`(사라진 코드 경로를 진단하다 — 무의미해진 계측), `draw incorrect conclusions`(잘못된 결론을 끌어내다), `measures the ghost of the old system`(옛 시스템의 유령을 측정하다).
**격식 짝**: refined "its output measures the ghost of the old system" ↔ plain "it's still measuring how the old code behaved" (작성). refined "will draw incorrect conclusions" ↔ plain "will get the wrong idea" (작성).

<sub>출처: transcript:auto_recipe_creator (cross-file impact 감사 subagent)</sub>

---

## 단락 2

The A/B runner explicitly passes the compare scales, so the office A/B itself is correct. But any future caller that uses the ensemble function without the keyword argument — a downstream production integration, a notebook experiment, or a new test — will silently run on the wrong scale band. The mismatch is also an API surprise: the natural expected default for an ensemble proposer used in the static-compare path is the compare band, not the default band. Change the default in the public function, and in its helper for consistency. This makes the API safe-by-default without touching the test, which relies on the default — the test passes a synthetic frame that works at any scale anyway.

**문법·구조**: `so`(그러므로) → `But`(그러나) → 콜론(부연) → 명령문(처방) → `This makes ...`(효과)로 이어지는 **리뷰 지적의 표준 5단 흐름**. `any future caller that uses X without Y will silently run ...`은 "조건을 안 지키는 미래의 누군가"를 관계절 + 미래시제로 그리는 경고 문형. 대시 쌍(— ... —)은 예시 삽입, 콜론은 "surprise"의 내용 풀이. `without touching the test`는 전치사 + 동명사로 "부작용 없음"을 간결하게 처리한다.
**핵심 표현**: `silently run on the wrong scale band`(경고 없이 잘못된 설정으로 돌다 — silently 가 위험의 핵심), `an API surprise`(사용자의 자연스러운 기대를 배반하는 API), `safe-by-default`.
**격식 짝**: refined "The mismatch is also an API surprise." ↔ plain "The default just isn't what you'd expect." (작성)

<sub>출처: transcript:auto_recipe_creator (holistic 통합 리뷰 subagent)</sub>

---

## 단락 3

The runner's experimental mechanics — pairing, geometry, counting, normalization, logging — are correct. The only validity problem is in the upstream ensemble implementation: scale metadata is dropped at RRF fusion, so the chamfer rescore and ORB rerank both operate at a fixed scale of 1.0, regardless of which scale band each proposal actually came from. The runner will produce a number, but it measures a scale-broken ensemble finalizer, not the intended three-channel design. Any measured accuracy gain (or loss) is confounded by this bug; it cannot be cleanly compared to the earlier recall gain. Fix the fusion step to propagate the source candidate's scale field, then re-run the A/B; until then the localization numbers should not be compared against the recall figures.

**문법·구조**: 첫 문장에서 대시 나열로 "정상인 것들"을 묶어 치운 뒤, `The only validity problem is ...` 콜론으로 초점을 좁힌다. `X is dropped ... so Y operate ...`는 수동태(책임 주체 생략) + so 인과. `regardless of which ... came from`은 의문사절을 전치사 목적어로 쓰는 고급 패턴. `it measures X, not Y` 대비 구문과, 마지막 문장의 **명령문 → then → until then** 시퀀스(고쳐라 → 재실행하라 → 그 전까지는 비교 금지)가 처방을 시간 순으로 배열한다. `should not be compared`는 수동태 권고로 어조를 눌렀다.
**핵심 표현**: `is confounded by this bug`(이 버그로 교란되다 — 실험 무효화 어휘), `cannot be cleanly compared`(깔끔하게 비교 불가), `until then`(그 전까지는).
**격식 짝**: refined "Any measured accuracy gain is confounded by this bug." ↔ plain "The bug muddies whatever number we get." (작성). refined "the numbers should not be compared against the recall figures" ↔ plain "don't line these numbers up against the recall ones yet" (작성).

<sub>출처: transcript:auto_recipe_creator (Codex localization A/B 리뷰)</sub>
