# 2026-08-13 — 새 표현

## "a request, not a constraint"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 지시만으로는 강제되지 않는다고 못 박을 때. 코드 리뷰·설계 논의에서 "그건 부탁이지 강제가 아니다"라고 선을 긋는 말.
- 한국어: 요청일 뿐 강제 장치는 아니다
- 설명: 프롬프트·문서·컨벤션처럼 지키라고 적어두기만 한 것과, 코드로 막아둔 것을 가르는 표현. 뒤에 보통 "so I added a guard" 같은 대응이 따라온다.
- 예문: Prompt instructions are a request, not a constraint, so the guard enforces the rule geometrically.
- 유사어: advisory, not enforced (더 격식·문서체), a convention rather than a check (풀어쓴 형태)
- 반의어: enforced at the type level

## "a wrong-but-confident signal"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 장애 원인을 설명할 때. "틀렸는데 확신에 차 있어서 더 나쁜" 데이터를 한 덩어리 명사로 부른다.
- 한국어: 틀렸으면서 확신에 찬 신호
- 설명: 하이픈으로 형용사구를 통째 묶는 영어식 조어. `working-but-imperfect`, `cheap-but-fragile`처럼 대비쌍으로 굴리면 문장이 짧아진다.
- 예문: A wrong-but-confident signal is worse than no signal, because nothing downstream knows to distrust it.
- 유사어: a false positive with high confidence (중립·기술적), garbage that looks like data (구어)
- 반의어: a noisy but honest signal

## "silently displace"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 새 코드 경로가 기존 경로를 조용히 밀어냈다고 회귀 원인을 짚을 때.
- 한국어: 소리 없이 밀어내다
- 설명: `replace`는 의도한 교체, `displace`는 밀려남이다. `silently`가 붙으면 로그도 경고도 없었다는 뜻이 따라붙는다.
- 예문: The sidecar path silently displaced the VLM fallback, so the pipeline made zero model calls without ever saying so.
- 유사어: quietly take precedence over (완곡), shadow (덮어 가림), preempt (선점)
- 반의어: fall back to

## "lock onto (something)"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 탐지기·모델이 엉뚱한 대상에 고정돼 버렸을 때. 레이더 은유라 구어에서도 쓴다.
- 한국어: (엉뚱한 대상에) 딱 물려 고정되다
- 설명: 사람이 주어면 "집착하다"에 가깝고, 모델·센서가 주어면 "그 대상만 계속 잡는다"는 뜻.
- 예문: If the model locks onto the palm icon, every frame reports the same coordinate and the track looks perfectly stable.
- 유사어: latch onto (더 구어), fixate on (사람 주어일 때 자연스러움)
- 반의어: lose track of

## "a decoy"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 진짜와 헷갈리게 만드는 방해물을 한 단어로 부를 때. 보안·테스트·UI 탐지 문맥 모두에서 통한다.
- 한국어: 미끼, 헷갈리게 만드는 가짜
- 설명: 원래 사냥용 유인물. 의도적으로 놓은 것이 아니어도 "결과적으로 미끼 노릇을 하는 것"에 쓴다.
- 예문: The open-palm icon is a decoy: it sits where the cursor usually is and never moves.
- 유사어: a distractor (시험·인지 실험 용어라 더 중립), a red herring (논증에서 시선을 돌리는 것)
- 반의어: the ground truth

## "indistinguishable from success"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 실패가 성공처럼 보여 잡히지 않는다고 위험을 강조할 때. 사후 보고서·리뷰에서 강한 문장.
- 한국어: 성공과 구분이 안 되는
- 설명: `indistinguishable from X` 형태로 굳어 있다. 뒤에 `in the artifacts`, `from the outside`처럼 "어디서 봤을 때"를 붙여주면 정확해진다.
- 예문: A consistent, confident, completely wrong track is indistinguishable from success in the artifacts.
- 유사어: looks exactly like a clean run (구어), passes every check we have (구체적)
- 반의어: fails loudly

## "the discriminator is X"
- 레지스터: technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 두 가설을 가르는 결정적 기준 하나를 지목할 때. 디버깅 대화의 전환점에서 자주 나온다.
- 한국어: 둘을 가르는 판별 기준은 X다
- 설명: 통계·ML 용어가 일반 엔지니어링 대화로 넘어온 사례. `the discriminator is free` 처럼 뒤에 비용까지 붙이면 설득력이 커진다.
- 예문: The discriminator is motion: a real cursor moves, and a static icon never does.
- 유사어: the deciding test is (평이), what separates the two is (회화체)
- 반의어: the two are observationally equivalent

## "an audit trail"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 데이터를 지우지 않고 상태만 바꿔 추적 가능성을 남겼다고 설명할 때. 규제·금융 문서에서도 그대로 쓴다.
- 한국어: 감사 추적 기록
- 설명: 삭제 대신 표시(soft delete, re-status)를 택한 이유를 한 단어로 정당화한다.
- 예문: Events are re-statused rather than deleted, so the audit trail keeps them.
- 유사어: a paper trail (더 구어·비유), provenance (출처 추적 쪽에 무게)
- 반의어: a hard delete

## "that's your call"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 내가 정할 문제가 아니라고 결정권을 넘길 때. 회의·슬랙에서 자연스럽고, 격식 문서에는 조금 캐주얼하다.
- 한국어: 그건 당신이 정할 몫입니다
- 설명: `call`이 심판의 판정이라는 데서 왔다. 앞에 `honestly`나 `I shouldn't make this alone`을 붙이면 책임 회피가 아니라 존중으로 읽힌다.
- 예문: Whether to capture the full screen or track multiple windows is a design decision — that's your call.
- 유사어: I'll leave that to you (부드러움), that's a decision for you to make (격식)
- 반의어: I'll go ahead and decide

## "One change, one measurement."
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 변경을 한 번에 하나만 넣자고 짧게 못 박을 때. 표어처럼 던지는 문장이라 회의에서 힘이 있다.
- 한국어: 한 번에 하나만 바꾸고, 그 하나만 재자
- 설명: 관사 없는 대구 구조가 표어 느낌을 만든다. 같은 골격으로 `One owner, one queue.` 같은 문장을 만들 수 있다.
- 예문: Stacking a coordinate fix on an unvalidated prompt change breaks the rule I care about here: one change, one measurement.
- 유사어: change one thing at a time (평이), isolate the variable (실험체)
- 반의어: bundle it all into one commit

## "separately revertible"
- 레지스터: technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 두 변경을 따로 되돌릴 수 있게 나눠 커밋했다고 설명할 때.
- 한국어: 각각 따로 되돌릴 수 있는
- 설명: `revertible`은 git 문맥에서 굳은 형용사. `independent and separately revertible`처럼 짝지어 쓰면 커밋 분리의 근거가 된다.
- 예문: I kept them in two commits so they're independent and separately revertible.
- 유사어: can be rolled back on its own (평이), atomic (커밋 단위가 하나의 의미라는 뜻에 가까움)
- 반의어: baked into one commit

## "stop short of (doing something)"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 일부러 거기까지만 하고 멈췄다고 밝힐 때. 자기 절제를 드러내는 표현이라 보고에 좋다.
- 한국어: 일부러 ~까지는 하지 않았다
- 설명: 실패해서 못 한 게 아니라 판단해서 멈췄다는 뉘앙스가 핵심. 뒤에 이유를 붙이는 게 관례다.
- 예문: I stopped short of changing any thresholds, because I still didn't know which stage had zeroed out.
- 유사어: hold off on (더 구어), refrain from (격식·문어)
- 반의어: go ahead and (do it anyway)

## "flag rather than bury"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 불리한 사실을 본문 아래 묻지 않고 앞으로 끌어올릴 때 쓰는 자기 서술.
- 한국어: 묻어두지 않고 짚어두다
- 설명: `bury`가 "긴 글 속에 파묻다"라는 뜻으로 쓰인다. 나쁜 소식을 전할 때 신뢰를 얻는 상투구.
- 예문: One thing I want to flag rather than bury: this guard could void genuine clicks near the live-image border.
- 유사어: surface (동사·중립), call out up front (구어)
- 반의어: bury it in the appendix

## "a systematic hole"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 무작위가 아니라 특정 구간만 통째로 빠진 결손을 지적할 때. 데이터 품질 논의의 핵심 어휘.
- 한국어: 체계적으로 뚫린 구멍(편향된 결손)
- 설명: `random loss`와 대비시키는 게 관용. 무작위 손실보다 나쁘다는 판단이 이 단어 하나에 담긴다.
- 예문: Discarding those frames deletes edge-region operations preferentially — a systematic hole in the timeline, worse than random loss.
- 유사어: a blind spot (인지 쪽 은유), selection bias (통계 용어)
- 반의어: uniformly sampled

## "X is the dial"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 조절하고 싶으면 이 값 하나를 만지면 된다고 알려줄 때. 설정 설명에서 친근하고 정확하다.
- 한국어: 조절 손잡이는 X다
- 설명: `knob`도 같은 뜻으로 쓰이며, `the dial to turn`처럼 부정사를 붙이기도 한다.
- 예문: If the guard starts eating real clicks, `static_cursor_tolerance_px` is the dial.
- 유사어: the knob to turn (동의), the tuning parameter (격식·문어)
- 반의어: hard-coded

## "premised on a wrong model"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 결론이 아니라 전제 자체가 틀렸다고 스스로 물릴 때. 정정 발화의 격식 있는 형태.
- 한국어: 잘못된 이해를 전제로 삼은
- 설명: `premised on`은 `based on`보다 논리적 무게가 있다. 뒤에 무엇을 잘못 봤는지 한 문장으로 붙이는 게 관례.
- 예문: My last commit is premised on a wrong model: I had treated the drawn cursor and the local pointer as the same object.
- 유사어: built on a false assumption (평이), rests on a premise that doesn't hold (격식)
- 반의어: holds regardless of that assumption

## "from helpful to actively dangerous"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 새 정보 하나로 어떤 변경의 평가가 뒤집혔다고 말할 때.
- 한국어: 도움이 되는 것에서 오히려 해로운 것으로
- 설명: `actively`가 "가만히 두는 것보다 나쁘다"는 뜻을 얹는다. `from X to actively Y` 골격으로 응용된다.
- 예문: That detail moves the prompt change from helpful to actively dangerous.
- 유사어: turns a fix into a liability (구체적), backfires (구어·간결)
- 반의어: from risky to routine

## "no amount of X would have Y"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 어떤 방향의 노력을 아무리 해도 소용없었을 것이라고 단언할 때. 원인을 다른 층으로 옮길 때 쓴다.
- 한국어: X 를 아무리 해도 Y 하지 못했을 것이다
- 설명: 가정법 과거완료(`would have + p.p.`)와 짝을 이룬다. `no amount of tuning`, `no amount of retries` 형태가 흔하다.
- 예문: No amount of gate or threshold work would have recovered this session.
- 유사어: tuning wouldn't have saved it (구어), the fix lies at a different layer (완곡)
- 반의어: a small threshold change would have caught it

## "two honest caveats"
- 레지스터: professional
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 성과를 보고한 직후 한계를 스스로 꺼낼 때 다는 소제목. 숫자를 붙이면 읽는 사람이 범위를 가늠한다.
- 한국어: 솔직히 밝혀둘 단서 두 가지
- 설명: `honest`가 없어도 뜻은 통하지만, 붙이면 "숨기지 않겠다"는 태도가 드러난다. 발표 슬라이드 제목으로도 쓴다.
- 예문: Two honest caveats: the prompt change is unvalidated, and the gate leak is still open.
- 유사어: a couple of things I can't yet vouch for (구어), limitations (격식·논문체)
- 반의어: no known limitations

## "decisive about one thing"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto_recipe_creator b0cef303
- 맥락: 데이터가 전부를 밝히진 않지만 최소한 하나는 확정한다고 범위를 좁힐 때.
- 한국어: 적어도 한 가지는 확실히 못 박는다
- 설명: `decisive`를 사람이 아니라 숫자·증거에 쓰는 용법. 뒤에 `about` + 확정되는 사실이 온다.
- 예문: `roi_p50=0` with `dist_p50=1966` is decisive about one thing: nothing is changing where we think the cursor is.
- 유사어: settles one question (평이), rules out X conclusively (범위 지정형)
- 반의어: consistent with either hypothesis

## "own this signal"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-engineer-done-priority-signals.md
- 맥락: 어느 컴포넌트가 그 판단의 주인인지 정할 때. 중복 검사를 막는 설계 규칙 문장.
- 한국어: 이 신호는 저 쪽이 책임진다
- 설명: 소유권(ownership) 어휘가 데이터·상태·신호로 확장된 예. "다른 데서 또 확인하지 마라"가 함의다.
- 예문: Avoid a second state-changing window check; the recording thread owns this signal.
- 유사어: is the source of truth for (더 격식), is responsible for deciding (풀어쓴 형태)
- 반의어: shared responsibility

## "only vetoes when ..."
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-engineer-done-priority-signals.md
- 맥락: 어떤 조건이 통과에 관여하지 않고 거부에만 관여한다고 비대칭 규칙을 적을 때.
- 한국어: ~일 때만 거부권을 행사한다
- 설명: `veto`를 동사로 굴리는 게 핵심. 승인 권한은 없고 반대 권한만 있는 관계를 한 단어로 표현한다.
- 예문: `Addressing1` is optional and only vetoes when its visible score is red.
- 유사어: can block but not approve (평이), has negative-only authority (격식)
- 반의어: is required for approval

## "strictly increasing"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-engineer-done-priority-signals.md
- 맥락: 같은 값이 반복되면 안 된다는 조건을 수학 용어로 정확히 못 박을 때.
- 한국어: 순증가하는(같은 값 허용 안 됨)
- 설명: `non-decreasing`(같은 값 허용)과 반드시 구분해서 쓴다. 명세에서 이 한 단어 차이가 버그를 가른다.
- 예문: Numerator fallback requires three strictly increasing readings `n1 < n2 < n3`.
- 유사어: monotonically increasing (문맥에 따라 같은 값 허용 여부가 갈리므로 주의)
- 반의어: non-decreasing

## "a regression guard"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-engineer-done-priority-signals.md
- 맥락: 이미 통과하는 테스트를 왜 남겨두는지 설명할 때.
- 한국어: 회귀 방지용 테스트
- 설명: 새 기능을 검증하지 않고 "예전 동작이 깨지지 않았음"만 지키는 테스트를 가리킨다. `retained as a regression guard` 형태가 흔하다.
- 예문: The clipped-header test already passes and is retained as a regression guard for the right-edge behavior.
- 유사어: a pinning test (동작을 고정한다는 뉘앙스), a safety net (구어·비유)
- 반의어: a characterization test (현재 동작을 기술만 하는 것)

## "suppress X while preserving Y"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-engineer-done-priority-signals.md
- 맥락: 어떤 처리가 잡음만 죽이고 신호는 살린다고 한 문장으로 정당화할 때.
- 한국어: X 는 눌러 없애면서 Y 는 살린다
- 설명: 트레이드오프 없는 처리를 주장하는 골격. `while` 분사구가 두 효과를 한 문장에 담는다.
- 예문: Quantizing to 16-level buckets suppresses small remote-render noise while preserving a changed score.
- 유사어: filters noise without losing signal (평이)
- 반의어: throws out the signal with the noise
