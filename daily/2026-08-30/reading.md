## 단락 1

Objection 1 (worst): V2's flagship rule is structurally anti-correlated with its own success condition. The matcher's confident zone is zoomed-in, scale~1.0 (terminal guard: scale ≥ 0.6 + ORB, live_search.py). Recovery traces exist because the key wasn't matchable — so on exactly the before-frames the classifier must read, the matcher returns unknown → unclassified. And when it does fire, a pan near a spurious best_xy is mislabeled reposition_to_align_key, binding to move_to_point(best_xy) — a fabricated recenter that poisons ticket-04 semantic-key merging. Falsifier (1) isn't a tail risk; it's the expected day-one outcome, and with 0 Episodes, home-only text digests, and no images executable at home, the tolerance can't even be calibrated. The position states the rule but no confidence gate or calibration plan. Cost: digest action column collapses to unclassified, defeating the very motivation cited in ticket 09.

**문법·구조**: "because"(이유절)와 "so"(결과절)가 한 문장 안에서 연쇄로 이어지며 논증을 한 방향으로 밀고 간다 — "생긴 이유 → 그래서 벌어지는 일"의 인과 사슬이다. "isn't a tail risk; it's the expected day-one outcome"는 세미콜론으로 두 절을 대구시켜 부정→긍정으로 판정을 뒤집는 전형적인 반론 구문이다. 마지막 문장의 "Cost:"는 주어 없는 명사구로 시작해 결론을 압축하는 격식체 특유의 생략 서술이고, 뒤이은 "defeating the very motivation"은 결과를 나타내는 분사구문(-ing)으로 문장 전체의 귀결을 짧게 덧붙인다.

**핵심 표현**: "structurally anti-correlated with" — 우연이 아니라 구조적으로 반대 방향인 관계(기술 반론). "a fabricated recenter that poisons X" — 관계절로 원인과 악영향을 한 번에 서술하는 방식.

**격식 짝**: refined — "The position states the rule but articulates no confidence gate or calibration plan." / plain — "They said what the rule is, but never said how sure it needs to be or how to tune it."

<sub>출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-action-vocabulary-debate.md</sub>

---

## 단락 2

Objection 1 (shadow poisons the corpus, worst). C4 keeps `verify:*` reading real observations while `act:*` only logs. During shadow runs the engineer is manually recovering the tool — so `verify` will read the human's post-action state, the evaluator will derive success, and the run terminates `recovered`. C5 then declares every shadow run "a new Recovery Trace attempt" with `playbook_version` + `rule_id` provenance — but provenance has no execution-mode field, so this is indistinguishable from live qualified success evidence for a rule whose actions never executed. Ticket 04 explicitly gates rules/fallbacks on qualified `recovered` provenance; ticket 06's replay gate cannot catch this, because replay re-runs the same evaluator over the same trace and reproduces the same false `recovered`. Cost: the first approved playbook version — and every branch derived from it — rests on fabricated success evidence. Fix is cheap (mode in provenance, shadow attempts excluded from supporting corpus), but as stated the position fails its own falsifier (4).

**문법·구조**: "while"는 두 동작이 동시에 일어나지만 성격이 다름을 대조하는 접속사다("verify는 읽는데 act는 로그만 남긴다"). "will read... will derive... terminates"로 이어지는 현재/미래 시제 연쇄는 지금 설계대로면 앞으로 반드시 이렇게 흘러간다는 예측을 강조한다. "a rule whose actions never executed"의 "whose"는 소유격 관계대명사로, rule이 가진 성질(그 행동이 실행된 적 없음)을 간결히 얹는다.

**핵심 표현**: "poisons the corpus" — 데이터 근거 전체를 오염시킨다는 은유(기술 반론). "indistinguishable from X" — 겉으로 구별할 수 없어 위험한 상황을 짚는 표현.

**격식 짝**: refined — "The fix is inexpensive: tag execution mode in the provenance record and exclude shadow attempts from the supporting corpus." / plain — "Easy fix — just mark whether it was a shadow run, and don't let those count as real evidence."

<sub>출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-workflow4-compiler-debate.md</sub>

