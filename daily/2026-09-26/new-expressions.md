# 2026-09-26 — 새 표현

> 오늘 배치에는 transcript 9건만 있었고 repo 문서와 spool 노트는 없었다. 표현 22개는 전부 `[assistant]` 영어에서 뽑았다. 세션별로는 equipment-data-map 둘(해시 폴더와 위키 가독성, ftp_handler 포팅), auto-recipe-creator 넷(배포 전 점검 반영, search-around 트리거, align point 보정, glide·녹화·가림 감지), skewnono 하나(즐겨찾기 장비 grilling)다. `a coin flip`, `the crux`, `the odd one out`, `just say the word`, `earn its keep`, `worth knowing` 는 노트에 이미 있어서 제외했다.

## "It's by design."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 이상해 보이는 동작을 두고 "버그가 아니라 설계가 그렇다"고 첫마디부터 정리할 때(질문 답변·리뷰, 격식 중간).
- 한국어: 의도된 설계입니다.
- 설명: `by design` 은 "설계상, 일부러 그렇게 만든"이라는 부사구다. 원문은 바로 뒤에 `The spec and letters require it; the agent didn't choose it.` 을 붙여 누가 정했는지까지 밝힌다. 이렇게 근거를 이어 줘야 변명이 아니라 설명으로 들린다.
- 예문: It's by design. The spec and letters require it; the agent didn't choose it.
- 유사어: That's intentional. (평이), It's working as intended. (고객 응대·이슈 트래커 정형구), on purpose (구어)
- 반의어: It's a bug. / an oversight (놓친 것)

## "Mostly yes, with two catches."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대 이해가 대체로 맞다고 인정하면서 예외 몇 가지를 붙일 때(채팅·회의 답변, 구어).
- 한국어: 대체로 맞아요, 단서가 두 개 있긴 하지만.
- 설명: `catch` 는 "숨은 함정·단서"다. 숫자를 먼저 밝혀 두면 듣는 쪽이 예외가 몇 개 나올지 알고 따라온다. 원문도 `Catch 1: …`, `Catch 2: …` 로 번호를 붙여 이어 간다.
- 예문: Mostly yes, with two catches. Once stage 4 has run, the wiki is the place to read.
- 유사어: Yes, with a couple of caveats. (격식 조금 위), Broadly, yes — but … (문어), Pretty much, except … (캐주얼)
- 반의어: Yes, no strings attached. (단서 없음)

## "Next to these, X is negligible."
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 진짜 병목을 먼저 늘어놓고 상대가 걱정한 비용이 그에 비하면 미미하다고 정리할 때(성능 분석·보고서).
- 한국어: 이것들에 비하면 X 는 무시해도 될 정도다.
- 설명: 여기서 `next to` 는 "옆에"가 아니라 "~와 나란히 놓고 보면"이라는 비교 표현이다. 원문은 `Where the time really goes` 로 FTP·LLM 비용을 먼저 보이고 이 한 문장으로 해싱 걱정을 접는다.
- 예문: Next to these, hashing time is negligible.
- 유사어: Compared with these, … (평이), By comparison, … (문어), … is a rounding error next to … (구어·과장)
- 반의어: X dominates the runtime. (X 가 시간을 대부분 잡아먹는다)

## "Where the time really goes"
- 레지스터: technical, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 성능 걱정에 답하면서 실제 시간이 드는 곳을 소제목처럼 짚을 때(성능 분석 글).
- 한국어: 시간이 실제로 드는 곳
- 설명: `go` 가 "(시간·돈이) 쓰이다, 나가다". `Where does the money go?` 의 `go` 와 같다. `really` 가 붙어서 "당신이 걱정한 곳 말고 진짜로는"이라는 대비가 생긴다.
- 예문: Where the time really goes is FTP listing and the LLM calls, not hashing.
- 유사어: the real bottleneck (기술 용어), what actually eats the time (구어), the dominant cost (격식)
- 반의어: a negligible cost

## "X now costs almost nothing"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 아직 확정되지 않은 결정이라 지금 바꾸면 비용이 거의 없다고 알릴 때(설계 검토, 격식 중간).
- 한국어: 지금 X 하면 비용이 거의 들지 않는다
- 설명: 주어 자리에 동명사(`switching to OKF`)를 세우고 `costs` 로 받는다. 시점 부사 `now` 가 핵심이다. "나중이면 비싸진다"는 뜻을 굳이 말하지 않아도 전달한다.
- 예문: So the format is still open, and switching to OKF now costs almost nothing.
- 유사어: it's cheap to change at this point (평이), the switching cost is minimal (문어), now's the time to change it (구어)
- 반의어: it'd be expensive to change later

## "a stray keystroke"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 편집 가능한 상태로 열린 파일이 실수 한 번에 바뀔 위험을 말할 때(도구 사용 주의, 구어·문어 모두).
- 한국어: 무심코 잘못 누른 키 하나
- 설명: `stray` 는 "제자리를 벗어나 헤매는"이다. `a stray bullet`(유탄), `a stray cat` 처럼 "의도 없이 튀어나온"이라는 느낌이다. 노트에 있는 `no stray staged files` 와 같은 형용사지만 여기선 사람의 실수를 가리킨다.
- 예문: Obsidian also opens notes ready for editing, so a stray keystroke changes a page.
- 유사어: an accidental keypress (평이), a slip of the finger (구어), a fat-finger edit (개발자 속어)
- 반의어: a deliberate edit

## "The bug was treating X and Y as one thing."
- 레지스터: technical, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 버그의 근원이 서로 다른 두 개념을 하나로 묶은 데 있다고 짚을 때(원인 분석·Insight).
- 한국어: 버그의 원인은 X 와 Y 를 같은 것으로 취급한 데 있었다.
- 설명: `The bug was + 동명사` 는 버그를 "잘못된 행동"으로 규정하는 구조다. `treat A as B` 는 "A 를 B 로 다루다". 해시용 표현 형식과 파일로 쓰는 형식을 한 규칙으로 묶은 게 문제였다는 요약이다.
- 예문: The bug was treating the hash form and the file form as one thing.
- 유사어: conflating X and Y (문어), mixing up X and Y (구어), X and Y got lumped together (구어, 수동)
- 반의어: keeping X and Y separate

## "can go stale by the time X happens"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 미리 해 둔 검사가 실제 동작 시점에는 이미 낡은 정보일 수 있다고 경고할 때(동시성·안전 리뷰).
- 한국어: X 가 일어날 즈음엔 이미 낡은 정보가 되어 있을 수 있다
- 설명: `go stale` 은 "상하다, 쉬다"에서 온 말로 정보가 시간이 지나 맞지 않게 된 상태다. `by the time + 현재시제` 는 "~할 즈음엔". 검사 시점(time-of-check)과 사용 시점(time-of-use) 사이 틈을 쉬운 말로 풀었다.
- 예문: A check that runs once can go stale by the time the action happens.
- 유사어: be out of date by then (평이), a time-of-check/time-of-use gap (보안 용어, TOCTOU), be overtaken by events (문어)
- 반의어: still hold at the moment of use

## "X is a policy decision"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 기술적으로는 할 수 있지만 무엇을 지울지·남길지는 사람이 정해야 할 규칙이라고 넘길 때(보고·회의).
- 한국어: X 는 정책으로 정할 문제다
- 설명: 동명사 주어(`deleting recordings`)에 `is a policy decision` 을 붙이면 "코드가 아니라 운영 규칙의 영역"이라고 선을 긋게 된다. 원문은 이유(`because they're also training data`)와 요청(`Tell me how much to keep`)을 이어 붙여 결정을 넘긴다.
- 예문: But deleting recordings is a policy decision because they're also training data.
- 유사어: that's a judgment call for the team (구어), a business decision, not a technical one (회의체), falls under policy (문어)
- 반의어: a purely technical call

## "too minor to churn a commit over"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 발견한 작은 흠을 밝히되 그것만으로 커밋을 새로 만들 가치는 없다고 할 때(작업 보고, 구어).
- 한국어: 커밋을 하나 더 만들 만큼 큰 문제는 아니다
- 설명: `too A to B` 구조 끝에 전치사 `over` 가 남는다(`churn a commit over it`). 노트의 명사 `churn`(공회전 변경)을 동사로 썼다. 원문은 뒤에 `Say the word and I'll fix the wording.` 을 붙여 결정을 상대에게 넘긴다.
- 예문: One imprecision I found in my own code, too minor to churn a commit over: the message misleads when you hit the abort.
- 유사어: not worth its own commit (평이), too small to bother with right now (구어), below the threshold for a fix (격식)
- 반의어: worth a follow-up commit

## "load-bearing"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 없애도 될 것처럼 보이는 장치가 실은 무언가를 떠받치고 있다고 경고할 때(리팩터 논의·리뷰).
- 한국어: (없애면 무너지는) 하중을 받치는, 실제로 제 역할을 하는
- 설명: 건축의 `load-bearing wall`(내력벽)에서 왔다. `still` 과 함께 쓰면 "클릭 경로에선 필요 없어졌어도 휠 경로에선 여전히"라는 대비가 생긴다. 노트에는 유사어로만 있었고 표제어로는 처음이다.
- 예문: Scroll never got that treatment, so glide is still load-bearing for the wheel.
- 유사어: doing real work (구어), essential (평이), not just decorative (대비형)
- 반의어: vestigial (흔적만 남은), dead weight

## "real but second-order"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 개선 효과가 있긴 하지만 더 큰 비용에 비하면 부차적이라고 크기를 매길 때(성능 논의).
- 한국어: 실제로 있긴 하지만 부차적인
- 설명: `second-order` 는 수학의 2차 항에서 온 말로 "주된 효과 다음 순위"다. `real but` 으로 먼저 인정해서 상대 제안을 깎아내리지 않는다. 원문은 이어서 `measure … rather than guessing` 으로 측정을 권한다.
- 예문: Against VLM locate calls of seconds each, it's real but second-order.
- 유사어: a minor factor (평이), not the main lever (구어), of secondary importance (문어)
- 반의어: first-order, the dominant factor

## "the wrong rung to stop at"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 단계적으로 시험해 볼 사다리 중 지금 멈추기엔 이르거나 틀린 단계라고 말할 때(실험 계획 논의).
- 한국어: 지금 멈춰 설 단계가 아니다
- 설명: `rung` 은 사다리의 가로대다. 원문은 앞서 `Suggested ladder at the office` 로 시험 순서를 사다리로 세웠고 여기서 같은 은유를 이어 받는다. `stop at` 의 `at` 이 문장 끝에 남는 to부정사 구조다.
- 예문: It's 3 lines, so no — but it's still the wrong rung to stop at right now.
- 유사어: premature at this stage (격식), not the step to settle on yet (평이), jumping ahead (구어)
- 반의어: the right place to start

## "collapse X and Y into one"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 구별해야 할 두 상황을 코드가 한 경우로 처리해 버린 실수를 스스로 인정할 때(버그 사후 설명).
- 한국어: X 와 Y 를 하나로 뭉뚱그리다
- 설명: 노트의 `collapse to` 는 "작은 해법으로 접히다"였고 여기선 타동사로 "두 경우를 하나로 합쳐 버리다"다. 원문은 과거완료 `I'd collapsed` 를 써서 고치기 전 이미 저질러 둔 실수라는 시간 순서를 드러낸다.
- 예문: Losing the detector and the screen becoming clear are different events, and I'd collapsed them into one.
- 유사어: conflate (문어), lump together (구어), treat as the same case (평이)
- 반의어: tell X apart, keep the cases distinct

## "held its position"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 리뷰·토론에서 상대가 반박을 받고도 입장을 굽히지 않았다고 전할 때(리뷰 결과 보고).
- 한국어: 입장을 굽히지 않았다
- 설명: 원문은 같은 단락에서 `Codex conceded …`(양보했다), `sharpened it`(더 날카롭게 다듬었다), `held its position`(버텼다)을 나란히 써서 쟁점마다 결말을 구분한다. 리뷰 논쟁을 보고할 때 이 세 동사를 묶어 알아 두면 좋다.
- 예문: Codex held its position: a tooling failure isn't evidence of occlusion, but it isn't evidence of clearance either.
- 유사어: stood its ground (구어·약간 극적), maintained its view (격식), didn't budge (캐주얼)
- 반의어: conceded the point, backed down

## "the gating question, not a nice-to-have"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 선택 사항처럼 보이던 확인이 다음 단계를 막는 필수 관문이 되었다고 격상할 때(계획·보고).
- 한국어: 있으면 좋은 게 아니라 다음으로 가려면 먼저 풀어야 할 질문
- 설명: `gating` 은 게이트처럼 "통과해야 다음으로 가는"이다. `a nice-to-have` 는 `nice to have` 를 하이픈으로 묶어 명사로 쓴 말(있으면 좋은 것). `X, not Y` 대비로 중요도를 한 단계 끌어올린다.
- 예문: So the office check is now the gating question, not a nice-to-have.
- 유사어: a blocker (구어), a prerequisite (격식), the question everything hinges on (평이)
- 반의어: a nice-to-have, optional

## "it cuts harder than I said"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 상대 지적이 내가 앞서 인정한 것보다 더 아프게 들어맞는다고 솔직히 인정할 때(리뷰 대화).
- 한국어: 제가 말한 것보다 더 크게 걸리는 문제다
- 설명: `cut` 은 자동사로 "(논점이) 파고들다, 효과를 내다"다. `cut both ways`(양날의 검)와 같은 쓰임. 앞서 자기가 한 말을 기준으로 삼아(`than I said`) 스스로 과소평가했음을 인정한다.
- 예문: That's the same uncertainty I flagged, but Codex is right that it cuts harder than I said.
- 유사어: it's more serious than I made it sound (평이), I understated it (격식), it bites harder than I thought (구어)
- 반의어: it's less of an issue than it looks

## "measure X before and after rather than guessing"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 개선 효과를 추정으로 다투지 말고 전후 수치로 확인하자고 권할 때(성능 개선 논의).
- 한국어: 짐작하지 말고 전후로 X 를 재 보자
- 설명: `rather than + 동명사` 는 "~하는 대신". 명령문 `measure` 에 비교 대상 `guessing` 을 붙여 태도를 권한다. 원문 앞에는 `it's real but second-order —` 가 있어 크기를 매긴 뒤 측정으로 마무리한다.
- 예문: Measure `correction_sec` in `align_fail_timing.csv` before and after rather than guessing.
- 유사어: let the numbers decide (구어), verify empirically (격식), benchmark it first (기술)
- 반의어: eyeball it (눈대중으로 보다)

## "I'd rather confirm that than build X speculatively."
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 증거 없이 미리 만들기보다 먼저 사실을 확인하겠다고 우선순위를 밝힐 때(설계 판단·보고).
- 한국어: X 를 짐작으로 만들기보다 먼저 그걸 확인하고 싶다
- 설명: `would rather A than B` 에서 A, B 는 둘 다 동사원형이다(`confirm`, `build`). `speculatively` 는 "근거 없이 추측으로, 혹시 몰라서". YAGNI 를 정중하게 말하는 문장이다.
- 예문: I'd rather confirm that than build the second detector speculatively.
- 유사어: Let's verify first before building anything. (평이), I'd hold off until we know. (구어), building it now would be premature (격식)
- 반의어: build it just in case

## "the request nobody actually maintains"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 그럴듯하지만 실제로는 사용자가 관리하지 않게 되는 기능 요청을 짚을 때(기획·요구사항 논의).
- 한국어: 막상 아무도 관리하지 않는 요청
- 설명: 관계절 `nobody actually maintains` 가 `the request` 를 꾸민다. `actually` 가 "말로는 원하지만 실제로는"이라는 대비를 만든다. 경험에서 나온 판단을 일반론처럼 말하는 화법이다.
- 예문: Per-page sets are the request nobody actually maintains.
- 유사어: sounds good on paper (구어), rarely used in practice (평이), a feature that ends up abandoned (설명적)
- 반의어: a feature people actually use

## "distinguishable after the fact"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 지금 막을 순 없어도 나중에 로그로 원인을 구별할 수 있다고 안심시킬 때(운영·장애 대응).
- 한국어: 사후에 (로그로) 구별할 수 있다
- 설명: `after the fact` 는 "일이 벌어진 뒤에"라는 관용구다. 원문은 콜론 뒤에서 무엇으로 구별하는지(`stop_reason=max_sec`)를 바로 대 준다.
- 예문: It's distinguishable after the fact: the manifest shows `stop_reason=max_sec` instead of `window_gone` or a done-detection.
- 유사어: you can tell from the logs afterward (평이), identifiable in hindsight (격식), shows up in the post-mortem (구어·기술)
- 반의어: indistinguishable, silent

## "the single chokepoint every frame goes through"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 검사를 넣을 위치로 모든 흐름이 반드시 지나는 한 지점을 골랐다고 설명할 때(설계 설명).
- 한국어: 모든 프레임이 반드시 거쳐 가는 단 하나의 길목
- 설명: `chokepoint` 는 원래 군사·교통 용어로 "좁은 병목 통로"다. 코드에선 "모든 호출이 모이는 지점이라 여기 하나만 막으면 된다"는 뜻으로 긍정적으로 쓴다. `every frame goes through` 는 관계대명사가 빠진 접촉절.
- 예문: The gate sits in `_capture_full_gray()`, the single chokepoint every frame goes through.
- 유사어: a single choke point (띄어 쓰는 표기), the one path everything funnels through (구어), a central gate (평이)
- 반의어: scattered call sites
