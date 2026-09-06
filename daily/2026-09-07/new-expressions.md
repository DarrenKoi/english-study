# 2026-09-07 — 새 표현

## "Tolerable but real."
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-09-03-model-upload-review.md
- 맥락: 리뷰에서 결함 하나의 심각도를 두 단어로 못 박을 때(문어·격식). 지적은 남기되 릴리스를 막지는 않는다는 신호.
- 한국어: 참을 만하지만 실재하는 문제다.
- 설명: `tolerable` 이 먼저 와서 상대를 안심시키고, `but real` 이 "그래도 없던 일로 하지는 말라"를 붙인다. 순서가 반대면(`Real but tolerable`) 무게가 심각도 쪽으로 쏠린다. 리뷰 항목 끝에 한 줄로 던지는 판정구.
- 예문: The loser's `os.replace` hits a missing file and churns out a spurious 500 — tolerable but real.
- 유사어: minor but genuine (더 평이), not a blocker (막지 않는다는 쪽만 강조), worth noting (가장 약함)
- 반의어: a hard blocker

## "X stands on its own"
- 레지스터: professional
- 출처: transcript:llm_serving (altitude 리뷰 결과)
- 맥락: 어떤 설명에 딸린 참조·부연을 지워도 되는 근거를 댈 때(코드 리뷰·문서 정리, 격식).
- 한국어: 그것만으로도 말이 된다 / 혼자 서 있다.
- 설명: 삭제 제안의 정당화 공식이다. "지우면 뭔가 빠지지 않나"라는 반문을 미리 막는다. 앞에 무엇을 떼는지, 뒤에 남는 것이 자립한다는 판단을 놓는다.
- 예문: Drop the "same pattern as `serve_vlm.detect_gpu_total_memory_gib`" clause in both places — the csv,noheader,nounits description stands on its own.
- 유사어: is self-contained (더 기술적), needs no further context, speaks for itself (더 구어적이고 "설명이 필요 없다"에 가깝다)
- 반의어: only makes sense alongside X

## "left over from X"
- 레지스터: technical, conversational
- 출처: transcript:llm_serving (repo 전체 over-engineering 감사)
- 맥락: 지금은 쓰이지 않는 코드·설정이 왜 아직 있는지 한 구로 설명할 때(구어·문어 공용).
- 한국어: X 시절의 잔재 / X 때 쓰다 남은 것.
- 설명: `leftover` 를 한 단어 명사로 쓰면 "남은 음식"이 먼저 떠오르지만, `left over from` 으로 풀면 중립적인 유래 설명이 된다. 비난 없이 "이건 과거 사정 때문"이라고 알려 주므로 삭제 제안이 부드러워진다.
- 예문: The `<family> <size>` argv form is left over from `ui-venus 30b`, which no longer exists on this server.
- 유사어: a holdover from (더 격식), a relic of (과장·비유), vestigial (의학 은유, 기술 문서에서만)
- 반의어: newly introduced for X

## "It doesn't stand up to light scrutiny."
- 레지스터: professional
- 출처: transcript:llm_serving (code-review 신뢰도 채점 루브릭)
- 맥락: 남의 지적을 오탐으로 기각할 때, 세게 반박하지 않고 등급만 매기듯 말할 때(리뷰·격식).
- 한국어: 조금만 따져 봐도 무너진다.
- 설명: 핵심은 `light` 다. "깊이 파야 무너진다"가 아니라 "가볍게 봐도 무너진다"라 기각의 강도가 세지는데, 정작 문장 자체는 평온하다. 사람을 치지 않고 주장만 치는 어법.
- 예문: This is a false positive that doesn't stand up to light scrutiny — the same line exists on `main`.
- 유사어: falls apart on a second read (더 구어적), doesn't survive checking (평이)
- 반의어: it held up under scrutiny

## "Applies nothing. One-shot."
- 레지스터: technical, professional
- 출처: transcript:llm_serving (ponytail-audit 스킬 정의)
- 맥락: 도구·에이전트의 동작 범위를 문서 맨 끝에 짧게 못 박을 때(사양서·격식). 동사구를 주어 없이 끊어 쓰는 문체.
- 한국어: 아무것도 적용하지 않는다. 한 번만 돈다.
- 설명: `one-shot` 은 형용사로 "한 번 실행하고 끝, 상태를 남기지 않는" 을 뜻한다. 앞의 `Applies nothing.` 과 짝지어 "읽기 전용에 일회성"이라는 계약 두 개를 다섯 단어로 끝낸다. 사양서에서 주어를 생략하는 이 압축 문체는 표·각주·`Boundaries` 절에서 표준이다.
- 예문: Lists findings, applies nothing. One-shot.
- 유사어: read-only, non-persistent (상태 쪽만), fire-and-forget (실행 후 결과를 안 본다는 쪽)
- 반의어: applies fixes in place / stateful

## "Lean already. Ship."
- 레지스터: casual, technical
- 출처: transcript:llm_serving (ponytail-audit 스킬 정의)
- 맥락: 감사·리뷰 결과 지적할 게 없을 때 던지는 두 단어 결론(동료 사이 구어에 가까운 개발자 말투).
- 한국어: 이미 군더더기 없다. 내보내라.
- 설명: `lean` 은 "살이 없는" — 코드에 쓰면 불필요한 추상·의존이 없다는 칭찬이다. 완전한 문장이 아닌데도 통하는 이유는 개발자 대화에서 판정이 문장보다 짧을수록 신뢰가 가기 때문이다. 격식 문서라면 "No findings; the module is already minimal."
- 예문: Nothing to cut here — lean already. Ship.
- 유사어: nothing to cut, good to go (더 일반적), LGTM (약어, 가장 캐주얼)
- 반의어: this needs a diet / there is fat to trim

## "in principle"
- 레지스터: professional, technical
- 출처: transcript:llm_serving (git 이력 리뷰 결과)
- 맥락: 이론상 가능하지만 실제로는 안 일어난다고 선을 그을 때(리뷰·설계 논의, 격식).
- 한국어: 원리상은 / 이론적으로는.
- 설명: 지적을 완전히 버리지 않으면서 심각도만 낮추는 장치다. 뒤에 보통 "no current config triggers it" 같은 실측이 따라붙어, 인정과 기각을 한 문장에 담는다. `in theory` 보다 딱딱하고 중립적이다.
- 예문: `upstream_port` can still be `None` in principle, so this is a small loss of accuracy in the payload — not safety-relevant.
- 유사어: in theory (더 평이·회화), strictly speaking (규칙 문언에 기댈 때), on paper (실제와의 괴리를 더 강조)
- 반의어: in practice / as actually configured

## "two spellings of one action"
- 레지스터: technical
- 출처: transcript:llm_serving (altitude 리뷰 결과)
- 맥락: 같은 일을 하는 인터페이스가 둘이라 지우자고 할 때(코드 리뷰, 격식).
- 한국어: 한 동작을 적는 방식이 둘.
- 설명: `spelling` 을 "철자"가 아니라 "표기 방식"으로 확장해 쓴 비유다. 두 CLI 형식·두 설정 키처럼 동작은 하나인데 입구가 둘일 때 딱 맞는다. 비용까지 함께 적는 게 관용 — 여기서는 분기 하나와 문서 두 줄.
- 예문: `stop_model.py --port 8006` and `stop_model.py 8006` are two spellings of one action, one extra branch, two doc lines.
- 유사어: a second way to say the same thing, redundant surface (더 추상적)
- 반의어: exactly one way to spell it

## "X is history and can stay"
- 레지스터: professional
- 출처: transcript:llm_serving (reuse 리뷰 결과)
- 맥락: 낡은 문서를 고칠지 말지 정할 때, 안 고치는 쪽을 정당화하며(리뷰·문어).
- 한국어: 그건 기록물이니 그대로 둬도 된다.
- 설명: `history` 를 "지나간 일"이 아니라 "일부러 남기는 기록"으로 쓴다. 코드는 현재를 주장하니 고쳐야 하고 문서는 당시를 적은 것이니 둬도 된다는 구분을 한 단어로 세운다. `can stay` 가 "고쳐도 되지만 안 고쳐도 된다"는 허가의 뉘앙스.
- 예문: Trim the two code and CLAUDE.md lines; the docs are history and can stay.
- 유사어: it is a record of the time (풀어쓴 격식), leave it as an archive
- 반의어: it still claims to be current

## "It's six lines to restore if you want it back."
- 레지스터: conversational, professional
- 출처: transcript:llm_serving (작업 완료 보고)
- 맥락: 상대가 원하지 않았을 수도 있는 삭제를 보고하며 되돌리는 비용을 미리 제시할 때(구어에 가까운 업무 보고).
- 한국어: 되돌리려면 여섯 줄이면 됩니다.
- 설명: 사과하지 않고 되돌림 비용을 숫자로 준다. 상대가 "그럼 되돌려"라고 말하기 쉬워지므로 결정권이 실제로 넘어간다. `It's N lines to X` 는 작업량을 줄 수로 견적 내는 개발자 관용 틀.
- 예문: I also removed `stop_model.py --port N`; the bare positional does the same thing, and it's six lines to restore if you want it back.
- 유사어: easy to put back, a one-line revert (더 짧을 때), the revert is cheap
- 반의어: that one would be painful to undo

## "microseconds, not a real cost"
- 레지스터: technical
- 출처: transcript:llm_serving (efficiency 리뷰 결과)
- 맥락: 성능 지적을 스스로 발견해 놓고 고치지 않겠다고 할 때(리뷰·기술 문서).
- 한국어: 마이크로초 단위라 실제 비용이 아니다.
- 설명: 문제를 인정한 뒤 크기로 기각한다. `not a real cost` 가 "비용이 없다"가 아니라 "비용이라 부를 만하지 않다"라 정직함을 잃지 않는다. 앞에 왜 작은지(일회성 기동 출력)를 붙여야 설득력이 산다.
- 예문: It is a one-shot startup print, so this is microseconds, not a real cost.
- 유사어: in the noise (측정 오차에 묻힌다), not worth optimizing, negligible (가장 격식)
- 반의어: it is on the hot path

## "Numbers in the same diff disagree with the code they document."
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-09-03-model-upload-review.md
- 맥락: 문서와 코드가 어긋난 결함을 한 문장으로 요약할 때(리뷰 보고, 격식).
- 한국어: 같은 diff 안의 숫자가 그것이 설명하는 코드와 어긋난다.
- 설명: `the code they document` 라는 관계절이 문서와 코드의 관계를 명시해, "문서가 낡았다"가 아니라 "같은 커밋 안에서 이미 어긋났다"까지 짚는다. `in the same diff` 가 변명의 여지를 없앤다.
- 예문: The spec says 33 tests but pytest collects 34 — numbers in the same diff disagree with the code they document.
- 유사어: the docs have drifted (시간이 지나 벌어졌을 때), stale by the time it landed
- 반의어: the doc and the code agree

## "pull in X at the checkpoints"
- 레지스터: professional
- 출처: transcript:llm_serving (작업 착수 선언)
- 맥락: 작업 계획을 밝히며 외부 리뷰어·도구를 언제 부를지 정할 때(회의·업무 보고, 준격식).
- 한국어: 중간 점검 지점마다 X 를 끌어들이겠다.
- 설명: `pull in` 은 "필요할 때 불러 참여시키다"로, `ask` 보다 능동적이고 `involve` 보다 구어적이다. `at the checkpoints` 가 "상시가 아니라 정해진 지점에서만"이라는 빈도를 함께 정해 준다.
- 예문: I'll work the agreed order directly, running `pytest` after each step, and pull in Codex and `/code-review` at the checkpoints.
- 유사어: loop X in (더 캐주얼), bring X in, involve X (가장 격식)
- 반의어: work it end to end on my own

## "cut at the right depth"
- 레지스터: technical, professional
- 출처: transcript:llm_serving (altitude 리뷰 결론)
- 맥락: 삭제·리팩터링이 증상이 아니라 메커니즘을 건드렸다고 인정할 때(코드 리뷰, 격식).
- 한국어: 알맞은 깊이에서 잘라 냈다.
- 설명: 뒤에 `the mechanism is gone, not just its callers` 같은 근거를 붙이는 게 정형이다. 이미 아는 `the fix is at the right altitude` 가 "층위"를 보는 데 비해, 이쪽은 "얼마나 깊이 파고들어 잘랐나"를 본다 — 삭제 작업의 승인 도장.
- 예문: Everything else in the diff is cut at the right depth: the mechanism is gone, not just its callers, and no orphaned parameter or test remains.
- 유사어: fixed at the root, removed the mechanism, not the symptom
- 반의어: it only deletes the callers
