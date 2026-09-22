# 2026-09-23 — 새 표현

> 오늘 배치는 repo 문서 3건(equipment-data-map 2, auto_recipe_creator 1)과 transcript 18건. repo 문서는 본문이 전부 한국어라 표현 추출에 쓸 영어가 없었고 표현 20개는 모두 transcript 의 `[assistant]` 영어에서 골랐다. 대부분 equipment-data-map 세션(`init` 기본값·`engineer.toml`·proxy 토큰 버그)에서 나왔고 auto-recipe-creator 의 Scope/brightness 세션과 skewnono 의 recipe 검색 세션에서 몇 개를 보탰다. `for no gain`, `a no-op`, `leave it as is`, `get swept into` 처럼 이미 노트에 있는 표현은 뺐다.

## "This one I want to push back on before touching anything"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 요청을 그대로 실행하기 전에 반대 의견부터 내겠다고 예고할 때(회의·채팅, 격식 중간). 뒤에 `because …` 로 이유가 온다.
- 한국어: 이건 손대기 전에 먼저 반대 의견을 내고 싶다.
- 설명: `push back on X` 는 X 에 이의를 제기한다는 뜻. 목적어 `this one` 을 문두로 끌어내 "다른 건 다 했지만 이것만은" 이라는 대비를 만든다. `before touching anything` 은 "아직 아무것도 안 바꿨다"는 안심을 함께 준다.
- 예문: This one I want to push back on before touching anything, because it reverses the one rule the whole safety design hangs on.
- 유사어: I'd like to challenge this before we proceed (격식↑, 문서체), I'm not sure about this one (부드럽고 약함), Let me flag a concern first (중립)
- 반의어: Consider it done. (군말 없이 실행)

## "the one rule the whole design hangs on"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 설계 전체가 기대고 있는 단 하나의 규칙을 가리킬 때(설계 논의·문서, 격식).
- 한국어: 설계 전체가 걸려 있는 그 규칙 하나.
- 설명: `hang on X` 는 "X 에 달려 있다, X 가 무너지면 같이 무너진다". 관계대명사가 빠진 접촉절이라 `the rule (that) the design hangs on` 으로 읽으면 된다. `the one` 이 "유일한"을 강조한다.
- 예문: Letting the agent run `init` reverses the one rule the whole safety design hangs on.
- 유사어: the linchpin of the design (격식, 명사형), everything depends on this rule (평이), the load-bearing rule (건축 은유, 기술 글)
- 반의어: a nice-to-have (없어도 되는 것)

## "The reason isn't ceremony"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 어떤 규칙이 형식 절차가 아니라 실질적 이유에서 나온 것임을 밝힐 때(설계 근거 설명, 격식).
- 한국어: 이 규칙은 형식 때문에 있는 게 아니다.
- 설명: 개발 문맥에서 `ceremony` 는 승인·서식·TTY 확인 같은 "절차를 위한 절차"를 뜻한다. 부정문으로 먼저 오해를 걷어내고 콜론 뒤에 진짜 이유를 붙이는 구조.
- 예문: The reason isn't ceremony: an IP that reaches the agent sits in its transcript forever.
- 유사어: This isn't red tape (구어, 관료주의 뉘앙스), It's not a formality (평이), This rule is substantive, not procedural (격식↑)
- 반의어: pure ceremony (형식뿐인 절차)

## "a design change, not a convenience"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대가 "편의 개선"으로 여기는 요청이 실은 설계 변경임을 분류해 줄 때(리뷰·협의, 격식).
- 한국어: 편의 기능이 아니라 설계 변경이다.
- 설명: `A, not B` 로 요청의 등급을 다시 매긴다. `convenience` 는 "있으면 편한 것", `design change` 는 "보장이 바뀌는 것". 이렇게 이름을 바꿔 부르면 "그래도 하겠나"를 묻는 근거가 된다.
- 예문: If you still want the agent to drive it, that is a design change, not a convenience.
- 유사어: this changes the contract (기술 문서), this is a bigger ask than it looks (구어), this alters the guarantees (격식)
- 반의어: a quality-of-life tweak (사소한 편의 개선)

## "take (someone) at their word"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대 말을 검증하지 않고 그대로 믿고 진행했음을 밝힐 때(보고, 격식 중간). 원문은 `taken at your word that the harness owns it`.
- 한국어: 당신 말을 그대로 믿고 진행했다.
- 설명: 관용구 `take X at X's word` = X 의 말을 액면 그대로 받아들이다. 보고문에서 과거분사 `taken at your word that …` 로 줄여 쓰면 "이 부분은 확인 안 했다, 당신 말이 근거다"라는 책임 소재가 분명해진다.
- 예문: I've taken you at your word that the harness owns the LLM config, so `init` never prompts for it.
- 유사어: going by what you said (구어), per your statement (격식, 딱딱함), assuming X as you described (중립)
- 반의어: verify independently (따로 검증하다)

## "knobs with one sensible value"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 설정 항목이 많아 보이지만 실제로는 정답이 하나뿐인 값들이라고 설명할 때(설정 설계 논의).
- 한국어: 사실상 값이 하나로 정해진 조절 항목들.
- 설명: `knob` 은 돌려서 맞추는 손잡이, 곧 조정 가능한 설정값. `with one sensible value` 가 "돌릴 이유가 없다"를 함축한다. 그래서 다음 문장의 "묻지 말고 기본값으로 써라"가 자연스럽게 따라온다.
- 예문: Most of those aren't per-equipment decisions; they're knobs with one sensible value.
- 유사어: settings that only have one right answer (평이), tunables nobody tunes (구어·자조), parameters with a fixed default (격식)
- 반의어: a genuine per-site decision (현장마다 달라지는 판단)

## "X it is."
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대가 선택지를 고른 직후 "그걸로 가자"고 짧게 확정할 때(채팅·회의, 구어). 원문은 `Defaults approach it is.`
- 한국어: 그럼 X 로 하자.
- 설명: `Then it is X` 의 도치. 이미 결정된 것을 되풀이해 확정하는 관용 어순이라 `it is` 를 앞으로 옮기면 뜻이 사라진다. 다음 문장에서 바로 행동(`Let me read …`)으로 넘어가는 게 전형이다.
- 예문: Defaults approach it is. Let me read the spots that define what `init` asks.
- 유사어: Going with X, then. (구어), Understood, we'll take X. (격식↑), X, then. (더 짧음)
- 반의어: Let's keep both options open. (결정 유보)

## "make it sound like a step"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 문서 표현이 실제와 다른 인상을 준다고 인정할 때(문서 수정 사유, 격식 중간). 원문은 `the wording I left makes it sound like a step`.
- 한국어: 그 문구가 마치 해야 할 단계처럼 들리게 한다.
- 설명: `make X sound like Y` = X 를 Y 처럼 들리게 하다. 잘못이 사실이 아니라 "말투"에 있었다고 좁혀 주므로, "기능은 이미 맞고 문장만 고친다"는 다음 행동이 따라온다.
- 예문: You don't. Every one of those is a default already; the wording I left makes it sound like a step.
- 유사어: gives the wrong impression (중립), reads as if it were required (문어), comes across as a to-do (구어)
- 반의어: states it plainly (있는 그대로 말하다)

## "The two sides disagreed on what "" means."
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 클라이언트와 서버처럼 짝을 이루는 두 코드가 같은 값을 다르게 해석해 생긴 버그를 한 줄로 요약할 때(버그 설명·포스트모템).
- 한국어: 양쪽이 빈 문자열의 뜻을 다르게 봤다.
- 설명: `disagree on X` 는 사람이 아니라 프로그램 두 편에도 쓴다. `what "" means` 처럼 값 자체를 인용부호로 주어 삼는 것도 기술 글의 관례. 버그를 "누가 틀렸다"가 아니라 "합의가 없었다"로 프레이밍한다.
- 예문: The two sides disagreed on what "" means; the client sent no header while the server switched auth on.
- 유사어: the client and server were out of sync on X (평이), had different readings of X (문어), interpreted X differently (격식)
- 반의어: agree on a single meaning (한 가지 해석을 공유하다)

## "the classic 'is it set?' vs 'is it non-empty?' split"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 잘 알려진 버그 유형에 이름을 붙여 분류할 때(코드 리뷰·설명). `os.getenv` 가 `None` 과 `""` 를 구분하는 문제.
- 한국어: 전형적인 "설정됐나" 대 "비어 있지 않나" 혼동.
- 설명: `the classic X` 는 "다들 한 번씩 겪는 그 문제"라는 뉘앙스. 두 질문을 따옴표로 세워 `vs` 로 맞붙이고 `split`(갈림) 으로 묶는다. 이름을 붙이면 수정 방법(`or None`, `if token:`)도 정석으로 따라온다.
- 예문: This is the classic "is it set?" vs "is it non-empty?" split, and only the client author knew about it.
- 유사어: the usual None-versus-empty confusion (구어), a presence/emptiness ambiguity (격식), the old set-but-blank trap (구어)
- 반의어: (마땅한 대체 표현 없음)

## "Two things to know:"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 완료 보고 끝에 상대가 알아야 할 부수 사실 두 가지를 묶어 낼 때(보고서·PR 설명, 격식 중간).
- 한국어: 알아 둘 것 두 가지.
- 설명: `There are two things you should know` 를 명사구로 압축한 소제목. 숫자를 먼저 밝혀 독자가 분량을 가늠하게 하고 콜론 뒤 불릿으로 잇는다. `Two things to note:` 와 거의 같고 `know` 쪽이 "행동에 영향 있다"는 무게가 조금 더 있다.
- 예문: Two things to know: letter 02's hash changed, and nothing is staged or committed yet.
- 유사어: Two things to note: (조금 가벼움), A couple of caveats: (주의 사항 강조), Heads-up on two points: (구어)
- 반의어: Nothing else to report. (더 알릴 것 없음)

## "Say so when you get there and I'll do it."
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 지금은 때가 아닌 후속 작업을 상대의 신호에 맡기며 마무리할 때(채팅, 구어).
- 한국어: 거기까지 가면 말해 줘, 그때 할게.
- 설명: `say so` 는 "그렇다고 말하다", `get there` 는 진행 단계상 "그 지점에 이르다". 명령문 + `and` + 미래로 조건을 만든다(`If you say so, I'll do it`). 할 일을 잊지 않되 지금 하지는 않겠다는 선을 긋는다.
- 예문: Once letter 18 proves the CLI on real equipment, the spike files can go together. Say so when you get there and I'll do it.
- 유사어: Ping me when you're ready (구어), Let me know at that point (중립), Flag it when the time comes (약간 격식)
- 반의어: I'll go ahead and do it now. (지금 바로 처리)

## "the point of X is proving A, not tuning B"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 어떤 단계의 목적을 다시 세워 상대가 엉뚱한 데 공을 들이지 않게 할 때(설명·코칭, 격식 중간).
- 한국어: 1단계의 목적은 CLI 검증이지 한도 튜닝이 아니다.
- 설명: `the point of X is …` 가 목적을 정의하고 `A, not B` 가 흔한 오해를 걷어낸다. 동명사(`proving`, `tuning`)를 짝지어 두 활동을 같은 무게로 세운다.
- 예문: Use any budgets big enough to cover the fixture; the point of stage 1 is proving the CLI, not tuning limits.
- 유사어: stage 1 exists to prove the CLI (평이), the goal here is A rather than B (중립), A is the objective; B is out of scope (격식)
- 반의어: (마땅한 대체 표현 없음)

## "keep the tool from noticing you"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 속도 제한(rate limit)의 목적을 비유로 설명할 때(구어 섞인 기술 설명).
- 한국어: 장비가 눈치채지 못하게 한다.
- 설명: `keep X from -ing` = X 가 …하지 못하게 막다. 장비를 사람처럼 세워 `noticing you` 라고 하면 "부하를 느끼지 않을 만큼 조용히 접근한다"가 한 구절로 전달된다. 격식 문서라면 `avoid putting load on the tool` 로 바꾼다.
- 예문: Pace limits never end a run; they just keep the tool from noticing you.
- 유사어: stay under the radar (구어 관용구), avoid loading the equipment (격식·직설), throttle politely (기술 구어)
- 반의어: hammer the tool (마구 두드리다)

## "Worth confirming X before building either."
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 두 가지 구현 후보를 두고 먼저 가설부터 확인하자고 권할 때(설계 논의, 격식 중간).
- 한국어: 둘 중 뭘 만들든 그 전에 X 부터 확인할 가치가 있다.
- 설명: `It is` 를 떨어뜨린 `Worth -ing` 은 권고를 부드럽게 시작하는 관용 어순. `either` 가 앞에서 말한 두 후보를 한 단어로 받는다. 순서를 정하는 말이지 반대하는 말이 아니다.
- 예문: Worth confirming the mode-mismatch theory on one real fail before building either actuator.
- 유사어: I'd verify X first (구어), X should be confirmed before either path is built (격식↑, 수동), Let's check X before we commit to one (중립)
- 반의어: build both and see which sticks (일단 둘 다 만들어 보기)

## "Same point — already implementing it."
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 상대가 이어서 한 말이 방금 지적과 같은 내용이고 이미 반영 중임을 알릴 때(채팅, 구어).
- 한국어: 같은 얘기예요. 이미 반영하는 중.
- 설명: 주어와 동사를 모두 떨어뜨린 두 조각. `Same point` 는 "당신 말이 내가 잡은 그 지점과 같다", `already implementing it` 은 진행형으로 "말하는 동안 손이 가 있다". 상대 말을 자르지 않고 중복을 줄인다.
- 예문: Same point — already implementing it. Adding the regression tests for exactly that confusion.
- 유사어: Yes, that's the fix I'm on (구어), Agreed, and it's in progress (중립), That's covered by the change underway (격식)
- 반의어: That's a separate issue. (다른 문제다)

## "a stale belief in the code"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 코드 주석이나 분기가 이제는 틀린 전제를 그대로 품고 있음을 짚을 때(코드 리뷰·수정 보고).
- 한국어: 코드에 남아 있던 낡은 전제.
- 설명: `stale` 은 캐시·데이터가 "오래돼 현실과 어긋난" 상태. 이를 `belief` 에 붙이면 코드가 어떤 사실을 "믿고" 짜였는데 그 사실이 바뀌었다는 뜻이 된다. 사람을 탓하지 않고 시점 문제로 만드는 말.
- 예문: Your correction also fixed a stale belief in the code: a comment said msr cond has no Scope, so the parser never checked it.
- 유사어: an outdated assumption (평이·격식), a leftover premise (문어), a comment that no longer holds (직설)
- 반의어: a current, verified assumption (검증된 현재 전제)

## "The safety story moved rather than vanished."
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 규칙을 완화한 뒤 "그래도 안전 보장은 남아 있다"고 설득할 때(설계 변경 보고, 격식).
- 한국어: 안전 장치는 사라진 게 아니라 자리를 옮겼다.
- 설명: `the X story` 는 "X 에 관한 설명·논리 전체". `moved rather than vanished` 는 두 자동사를 `rather than` 으로 대비시켜 "변했지만 없어지지 않았다"를 한 줄에 담는다. 다음 문장에서 옮겨 간 위치를 반드시 설명해야 빈말이 안 된다.
- 예문: The safety story moved rather than vanished: the only facts the agent may carry are exactly the `init` flags.
- 유사어: the guarantee is narrower but intact (격식), we didn't lose the guard, we relocated it (구어), the invariant survives in a different form (기술·격식)
- 반의어: the guarantee is gone (보장이 사라졌다)

## "You don't."
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: "왜 내가 X 를 해야 하나" 라는 물음에 "안 해도 된다"고 두 단어로 답할 때(채팅, 구어).
- 한국어: 안 해도 됩니다.
- 설명: 질문 `why do I need to …?` 의 조동사를 그대로 받아 `You don't (need to).` 로 줄인 응답. 전제 자체를 부정하는 가장 짧은 방법이라 질문의 이유를 설명하기 전에 결론을 먼저 준다.
- 예문: "Why do I need to fill in the budgets by hand?" "You don't. Every one of those is a default already."
- 유사어: There's no need. (중립), That step isn't required. (격식), You can skip that. (구어)
- 반의어: You do, and here's why. (해야 하고 이유는 이렇다)

## "is precisely the flow the spec forbids"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대의 제안이 명세가 금지하는 바로 그 동작임을 못 박을 때(설계 검토, 격식).
- 한국어: 그게 바로 명세가 금지하는 흐름이다.
- 설명: `precisely` 가 "비슷한 게 아니라 정확히 그것"을 강조하고 관계대명사가 빠진 `the flow (that) the spec forbids` 가 뒤따른다. 인용부호로 제안을 먼저 세운 뒤 이 술어를 붙이면 반박이 감정 없이 규칙 대조로 읽힌다.
- 예문: "Let the LLM ask me for the IP and fill it in" is precisely the flow the spec forbids.
- 유사어: runs directly against the spec (평이), is exactly what the contract rules out (중립), is the one path the design excludes by construction (격식↑)
- 반의어: is squarely within the spec (명세 안에 든다)
