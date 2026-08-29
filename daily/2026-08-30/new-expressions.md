# 2026-08-30 — 신규 표현

## "the expected day-one outcome"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-action-vocabulary-debate.md
- 맥락: 어떤 실패가 드문 예외가 아니라 설계상 첫날부터 뻔히 일어날 결과임을 강조할 때(기술 반론·격식)
- 한국어: 처음부터 뻔히 예견되는 결과
- 설명: "tail risk"(확률 낮은 극단 사례)와 짝지어 대비시키는 표현이다. 문제를 드문 사고가 아니라 설계 즉시 나타날 필연적 결과로 못박아 반론의 무게를 높인다.
- 예문: Falsifier (1) isn't a tail risk; it's the expected day-one outcome, and with 0 Episodes, home-only text digests, and no images executable at home, the tolerance can't even be calibrated.
- 유사어: baked in from the start (더 캐주얼), a foregone conclusion (문어)
- 반의어: a tail risk, an edge case

## "a genuine pressure valve"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-action-vocabulary-debate.md
- 맥락: 규칙에 정당한 도피 경로를 남겨 둬야 시스템이 막다른 골목에 몰리지 않는다고 옹호할 때(설계 논의)
- 한국어: 진짜 숨통 역할을 하는 안전장치
- 설명: 압력을 빼주는 밸브에서 온 은유로, 억지로 막지 않고 예외를 정당하게 흘려보내는 장치·절차를 가리킨다.
- 예문: The append-only `unresolved` proposal path is a genuine pressure valve; premature vocab growth is the bigger danger with 0 Episodes.
- 유사어: a safety valve, breathing room (더 일반적)
- 반의어: a bottleneck, a chokepoint

## "if nothing lands, say converged"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-action-vocabulary-debate.md
- 맥락: 토론·리뷰에서 반론이 더 이상 상대에게 먹히지 않으면 논의를 종료하라고 지시할 때(격식)
- 한국어: (반론이) 하나도 먹히지 않으면 합의됐다고 해라
- 설명: "land"는 주먹이 "맞다"는 뜻에서 확장돼, 주장·반론이 상대에게 실제로 타격을 주며 통했다는 뜻으로 쓰인다. 부정형 "nothing lands"는 더는 유효한 반박이 없다는 신호다.
- 예문: Raise a new objection only if it is genuinely stronger. Under 250 words; if nothing lands, say converged.
- 유사어: doesn't stick, fails to persuade
- 반의어: lands hard, hits the mark

## "press (someone), with a concrete failure case, on X"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-action-vocabulary-debate.md
- 맥락: 토론·코드 리뷰에서 특정 쟁점 하나를 구체적 실패 사례로 계속 파고들라고 지시할 때(격식)
- 한국어: (한 쟁점을) 구체적 실패 사례로 계속 물고 늘어지다
- 설명: "press on"은 물리적으로 누르는 이미지에서 확장되어, 논쟁에서 한 지점을 집요하게 추궁한다는 뜻이 된다. "with a concrete failure case"를 붙이면 추상적 반박이 아니라 실제 사례를 요구한다는 조건이 선다.
- 예문: Press, with a concrete failure case, only on the corrected classification rule (sequence role + after-frame corroboration).
- 유사어: push on, drill into, bear down on
- 반의어: let it go, drop the point

## "close out with what's confirmed rather than continue stalling"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/9eb9c743-9a6b-419b-8942-e35030598f05.jsonl
- 맥락: 응답 없는 하위 작업을 무기한 기다리지 않고 확보된 결과로 마무리할 때(업무 보고)
- 한국어: 하염없이 지연시키지 않고 확보된 것으로 마무리하다
- 설명: "stall"은 엔진이 멎듯 일이 진행되다 멈추는 것을 가리키고, "indefinitely"가 붙으면 끝을 알 수 없이 무기한 멈춰 있다는 뉘앙스가 강해진다.
- 예문: I'll close out with what's confirmed rather than continue stalling indefinitely.
- 유사어: wrap up with what we have, cut losses and move on
- 반의어: wait indefinitely, leave it open-ended

## "distinct enough (from X) to justify Y"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/9eb9c743-9a6b-419b-8942-e35030598f05.jsonl
- 맥락: 비슷해 보이는 두 대상을 정말 별도로 다룰 만큼 다른지 판단할 때(코드 리뷰·설계 논의)
- 한국어: 별도로 취급할 만큼 충분히 다른가
- 설명: "형용사 + enough to + 동사" 구문으로 "그 정도로 충분한가"를 묻는 표준 패턴이다. 여기서는 두 모듈이 합칠 수 없을 만큼 다른지를 따진다.
- 예문: If you want that folder covered, it should be re-run as its own audit rather than waited on further here — it's the largest remaining unaudited surface in scope, and worth specific attention to `_siblings.py`, `spec_range_mock.py`/`pm_gate_bsm_mock.py` (whether they're distinct enough from `providers/mock.py` to justify separate files), and `bm_pm/_shared.py`'s actual caller count.
- 유사어: different enough to warrant, sufficiently distinct to keep separate
- 반의어: close enough to merge, redundant with

## "repo-scoped, not global"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/df74b5af-62cf-4b5d-93f8-ca9965748f15.jsonl
- 맥락: 설정·권한의 적용 범위가 저장소 하나에 한정되고 전역에는 영향이 없음을 밝힐 때(기술 설명)
- 한국어: (전역이 아니라) 이 저장소에만 적용되는
- 설명: "X-scoped"는 "X 범위로 한정된"이라는 뜻의 형용사 패턴으로, scope를 명시할 때 명사에 -scoped를 붙이는 개발자 관용 표현이다.
- 예문: The gate is repo-scoped, not global — enabling it here doesn't affect your other checkouts, and each `git worktree` you spin up under `../skewnono-<task>/` is a different path, so it may not inherit the gate.
- 유사어: scoped to this repo, local to this checkout
- 반의어: global, applies everywhere

## "composes with (rather than replaces) X"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/df74b5af-62cf-4b5d-93f8-ca9965748f15.jsonl
- 맥락: 새 기능이 기존 것을 덮어쓰지 않고 나란히 함께 작동함을 설명할 때(기술 설명)
- 한국어: (기존 것을) 대체하는 게 아니라 함께 맞물려 작동하다
- 설명: "compose with"는 함수형 프로그래밍에서 "조합하다"라는 뜻이 일상 설명으로 넘어온 표현으로, 두 장치가 서로 대체 관계가 아니라 보완·결합 관계임을 짚을 때 쓴다.
- 예문: It fires at *stop time*: Claude Code will hand the pending diff to Codex for a fresh review before the turn ends, which composes with (rather than replaces) your `oc-*` opencode skills — those run read-only via `--agent plan`, this one runs through Codex's own runtime.
- 유사어: works alongside, layers on top of
- 반의어: replaces, supersedes

## "rests on fabricated success evidence"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-workflow4-compiler-debate.md
- 맥락: 결론·승인이 조작되거나 오염된 근거 위에 서 있음을 신랄하게 지적할 때(기술 반론)
- 한국어: 조작된 성공 근거 위에 서 있다
- 설명: "rest on X"는 물리적으로 "X 위에 놓여 있다"에서 "X에 의존한다"로 확장된 관용 표현이다. 근거가 무너지면 그 위의 결론도 함께 무너진다는 뉘앙스를 전달한다.
- 예문: Cost: the first approved playbook version — and every branch derived from it — rests on fabricated success evidence.
- 유사어: is built on, hinges on (더 중립적)
- 반의어: rests on solid evidence, is independently verified

## "at the system's least-tested moment"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-promotion-gate-debate.md
- 맥락: 검증이 가장 부족한 시점에 중요한 결정이 내려진다는 위험을 지적할 때(격식·기술 반론)
- 한국어: 시스템이 가장 덜 검증된 시점에
- 설명: "least-tested"처럼 최상급을 하이픈 복합 형용사로 만들어 명사를 수식하는 패턴은 기술 문서에서 흔하다. 시점을 콕 짚어 위험이 몰린 순간을 부각한다.
- 예문: The first real approvals — at the system's least-tested moment (G9) — will be single-Episode, maximally circular rules carrying a `replay_report.json` that reads as "path reproduced" evidence.
- 유사어: at the weakest point, at the most fragile stage
- 반의어: once things are battle-tested, at a mature, well-validated stage

## "signs it (off) to unblock"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-promotion-gate-debate.md
- 맥락: 절차가 막혀 있을 때 내용을 제대로 못 보고도 진행을 위해 승인 서명을 해버리는 부정적 상황을 지적할 때(격식)
- 한국어: (제대로 못 보고) 진행시키려고 서명하다
- 설명: "unblock"은 IT·프로젝트 관리에서 "막힌 것을 뚫어주다"라는 뜻으로 흔히 쓰이는 동사다. "sign (it) to unblock"은 절차상 어쩔 수 없이 도장을 찍는다는 부정적 뉘앙스를 담는다.
- 예문: Concrete failure: a guard reading is ambiguous, the packet question requires contract interpretation, nobody at the office owns the contract — approval either stalls across day/night cycles or an unqualified engineer signs it to unblock.
- 유사어: rubber-stamp it (더 부정적), sign off just to keep things moving
- 반의어: hold the line, refuse to sign

## "become in-sample"
- 레지스터: technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-promotion-gate-debate.md
- 맥락: 검증에 쓴 데이터가 사실은 학습·튜닝에 이미 쓰인 데이터라서 평가가 무의미해질 때(통계·머신러닝, 격식)
- 한국어: (검증 데이터가 학습 데이터와 겹쳐) 표본 안에 들어가 버리다, 즉 검증이 무의미해지다
- 설명: 통계·ML에서 모델은 학습에 쓰지 않은 새 데이터(out-of-sample)로 검증해야 일반화 성능을 믿을 수 있다. 검증셋이 학습에 이미 노출됐다면 "in-sample"이 되어 결과가 부풀려진다.
- 예문: Prediction-match statistics become in-sample.
- 유사어: overfit to the training data, tainted by leakage
- 반의어: stay out-of-sample, held-out

## "systematically overstate generalization"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-29-recovery-playbook-promotion-gate-debate.md
- 맥락: 통계적 편향 때문에 결과가 구조적으로, 우연이 아니라 늘 실제보다 과장돼 보일 때(격식·기술 문서)
- 한국어: 일반화 성능을 구조적으로 과장하다
- 설명: "systematically"는 우연이 아니라 매번 같은 방향으로 어긋난다는 뜻이다. "overstate"는 실제보다 부풀려 말한다는 뜻으로, 통계 편향을 짚을 때 자주 쓰인다.
- 예문: The split blocks temporal leakage but not serial correlation; the statistic will systematically overstate generalization, and a later production gate citing it inherits that inflation.
- 유사어: inflate the numbers, paint too rosy a picture
- 반의어: understate, undersell

## "disregard it, no action needed"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/9eb9c743-9a6b-419b-8942-e35030598f05.jsonl
- 맥락: 방금 한 행동이나 나온 결과가 불필요했으니 신경 쓰지 말고 넘어가라고 알릴 때(업무 대화, 중립~약간 격식)
- 한국어: 그건 무시해라, 신경 안 써도 된다
- 설명: "disregard"는 "ignore"보다 다소 격식 있는 동의어로, 특정 정보·결과를 의도적으로 배제하라고 지시할 때 쓴다.
- 예문: That last tool call was unnecessary — disregard it, no action needed there.
- 유사어: ignore it, never mind that, scratch that (더 캐주얼)
- 반의어: flag it, take note of it
