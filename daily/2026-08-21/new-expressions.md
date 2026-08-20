# 2026-08-21 — 새 표현

## "buys nothing by itself"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 상대 제안이 기술적으로 가능하다고 먼저 인정한 뒤, 같은 문장 안에서 실익이 0임을 회수할 때(설계 리뷰·문어체)
- 한국어: 그것만으로는 얻는 게 없다
- 설명: 승인과 기각을 대시 하나로 붙여 놓는 형식이다. 앞에서 "가능하다"를 내주고 `and buys nothing by itself` 로 실익을 도로 가져온다. `by itself` 가 "다른 변경이 따라붙지 않는 한" 이라는 조건을 소리 없이 깐다.
- 예문: Yes, purely additive is structurally possible — and buys nothing by itself.
- 유사어: is a no-op in practice (더 차갑고 기술적), doesn't move the needle (회화·경영 어감), is necessary but not sufficient (가장 격식)
- 반의어: pays for itself

## "the real edit surface is elsewhere"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: "여기만 고치면 된다"는 낙관을 꺾고, 실제로 손대야 할 코드가 다른 데 있다고 방향을 돌릴 때
- 한국어: 진짜 손댈 표면은 다른 곳이다
- 설명: `edit surface` 는 변경이 실제로 닿는 코드 면적이다. `real` 이 앞 문단의 "여긴 안전하다"를 인정으로 남긴 채 논점만 옮긴다. 뒤에 `and cannot be additive` 처럼 왜 그쪽은 안전하지 않은지를 바로 붙이는 게 관례다.
- 예문: But the real edit surface is elsewhere, and cannot be additive.
- 유사어: the blast radius is wider than it looks (파급을 강조), that's not where the cost lives (더 구어적)
- 반의어: the change is contained

## "the smallest defensible slice"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 반대 의견을 유지한 채로도 "굳이 한다면 여기까지" 라는 최소안을 제시할 때
- 한국어: 그나마 변호 가능한 최소 조각
- 설명: `defensible` 이 "옳다"가 아니라 "따져 물으면 답할 수 있다"는 수준을 가리킨다. 반대를 접지 않으면서 협조하는 화법이라, 앞에 `If forced anyway,` 같은 조건절을 세우고 뒤에 번호 목록을 다는 게 정석이다.
- 예문: If forced anyway, smallest defensible slice: add the method upstream and to the vendored copy together, cap the sub-batch at five, and put it behind an env flag.
- 유사어: the minimum viable adoption (중립적·제품 어휘), the least-bad version (더 회화적)
- 반의어: the full rollout

## "breach the rule outright"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 해석의 여지 없이 규칙을 정면으로 어겼다고 판정할 때(리뷰 판정문·격식)
- 한국어: 규칙을 대놓고 어기다
- 설명: `outright` 하나가 "회색지대가 아니다"를 담는다. `violate` 보다 `breach` 가 계약·규약 쪽 어휘라 사내 규칙 문서에 잘 맞는다. 뒤에 결과를 세미콜론으로 잇는 리듬이 흔하다.
- 예문: Adding the method there breaches the rule outright; the next upstream sync silently drops it.
- 유사어: violate the convention (더 일반적), fall foul of the rule (영국식·간접적)
- 반의어: stay within the letter of the rule

## "On the merits, I would not overturn it"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 절차상 재검토할 근거가 있어도 내용만 놓고 보면 앞선 결정이 옳다고 말할 때(법정 어투를 빌린 격식)
- 한국어: 내용만 따져도 그 결정을 뒤집지는 않겠다
- 설명: `on the merits` 는 절차·형식이 아니라 사안 자체의 시비를 가리키는 법률 관용구다. `overturn` 도 판결을 뒤집는 말이라 둘이 짝을 이룬다. 조건절 `would` 로 톤을 낮춰 상대 결정을 존중하는 자세를 남긴다.
- 예문: On the merits, I would not overturn it: the conclusion came from candidate-by-candidate elimination, and the error-semantics cost is real.
- 유사어: I'd let it stand (회화체), substantively I agree (덜 형식적)
- 반의어: I would reopen it

## "The decision stands unless ..."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 결론을 닫으면서 재론의 조건을 딱 하나만 열어 둘 때(회의록·의사결정 기록의 마지막 줄)
- 한국어: ~하지 않는 한 이 결정은 유효하다
- 설명: `stands` 는 "그대로 서 있다", 즉 뒤집히지 않고 살아 있다는 뜻이다. `unless` 절이 재론의 문턱을 명시하므로, 나중에 누가 다시 꺼내려면 그 조건부터 충족해야 한다. 결정 기록의 마지막 문장 자리 관례가 있다.
- 예문: The decision stands unless instrumentation later shows a real fan-out cost.
- 유사어: this holds until X (덜 형식적), we revisit only if X (조건을 더 앞세움)
- 반의어: the decision is provisional

## "fatal as specified"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-20-per-take-run-directory-debate.md
- 맥락: 아이디어 자체가 아니라 지금 문서에 적힌 형태가 치명적이라고 범위를 좁혀 지적할 때
- 한국어: 명세된 그대로면 치명적이다
- 설명: `as specified` 가 비판의 사거리를 설계 문서 한 판본으로 묶는다. 방향은 살려 두고 명세만 문제 삼으니, 상대가 설계를 통째로 방어할 필요가 없어진다. 반론 소제목에 그대로 붙여 쓰는 패턴이 흔하다.
- 예문: The tag is not unique per take — worst objection, and it's fatal as specified.
- 유사어: broken as written (더 짧고 구어적), a blocking defect in the current form (중립적)
- 반의어: sound as specified

## "is bigger than it reads"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-20-per-take-run-directory-debate.md
- 맥락: 문서에서 한 줄로 적힌 항목이 실제로는 큰 작업임을 경고할 때(설계 검토·구어에 가까운 격식)
- 한국어: 읽히는 것보다 큰 문제다
- 설명: `read` 를 자동사로 써서 "글이 그렇게 읽힌다"를 뜻한다. 사람의 판단이 아니라 문서의 겉모습을 주어로 세우니 비난이 아니라 관찰이 된다. `hiding` 계열 표현과 붙여 쓰면 강도가 올라간다.
- 예문: The tag-stamping for events.log is bigger than it reads.
- 유사어: a one-line bullet hiding the hardest problem (더 그림이 선명하다), deceptively large (형용사 하나로 압축)
- 반의어: as small as it looks

## "Not worth pressing."
- 레지스터: professional, conversational
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-18-occupied-share-request-debate.md
- 맥락: 자기 반론을 스스로 접고 다음 논점으로 넘어갈 때(토론 기록의 문단 마무리)
- 한국어: 더 밀어붙일 값어치는 없다
- 설명: 주어 없는 단문이라 판정 도장처럼 찍힌다. `press` 가 논점을 계속 밀어붙이는 동작이므로, 진 것이 아니라 "이 갈래는 여기서 닫는다"는 선언이 된다. 앞에 `Objection 3: dropped.` 처럼 라벨을 두고 이 문장으로 닫는 리듬이 있다.
- 예문: Iterative geometry tuning may take two or three round-trips, but each failed round-trip is a non-click — not worth pressing.
- 유사어: I'll let that one go (회화체), I withdraw the objection (가장 격식)
- 반의어: I'll press this one

## "the cost is delay, not harm"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-18-occupied-share-request-debate.md
- 맥락: 실패해도 무엇을 잃는지 종류를 갈라 위험을 재평가할 때(트레이드오프 변론)
- 한국어: 비용은 지연이지 피해가 아니다
- 설명: 크기가 아니라 **종류**를 대비시키는 `X, not Y` 틀이다. 되돌릴 수 있는 손실(지연)과 되돌릴 수 없는 손실(피해)을 갈라 놓으면 같은 확률도 다르게 읽힌다. 안전 설계의 기본값을 옹호할 때 자주 나온다.
- 예문: Each failed round-trip is a non-click — the cost is delay, not harm.
- 유사어: it fails safe (더 기술적), the downside is recoverable (중립적)
- 반의어: the cost is unrecoverable

## "Caveat for precision:"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-bm-pm-anchor-9h.md
- 맥락: 결론에 동의하면서도 근거 한 줄이 과장됐음을 스스로 깎아 낼 때(리뷰·감사 보고의 삽입절)
- 한국어: 정확을 기하자면 단서 하나
- 설명: `caveat` 앞에 관사를 빼고 콜론으로 끊어 소제목처럼 쓴다. 결론을 뒤집지 않고 정밀도만 손보겠다는 신호라, 뒤에는 보통 "문서에 그렇게 적혀 있진 않다" 류의 축소가 따라온다.
- 예문: Caveat for precision: no document mandates that replacement as a blanket rule.
- 유사어: To be precise (가장 흔하고 가볍다), with one sharpening (같은 기능이나 더 협업적)
- 반의어: stated without qualification

## "de facto, not written"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-bm-pm-anchor-9h.md
- 맥락: 코드에 일관되게 나타나는 관행을 성문 규칙으로 승격시키지 않고 그 지위를 정확히 표시할 때
- 한국어: 관행이지 성문 규칙은 아니다
- 설명: 라틴어 `de facto`(사실상)와 영어 `written`(문서화된)을 쉼표 하나로 대치시킨다. 근거의 강도를 미리 낮춰 두는 장치라, "그러니 위반이라고 부를 수는 없다"가 자연스럽게 따라온다.
- 예문: The six-versus-one pattern is de facto, not written.
- 유사어: convention rather than policy (더 사무적), an unwritten rule (일상적)
- 반의어: codified in the standard

## "the payoff is capped"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-opensearch-parallelisation.md
- 맥락: 최적화 제안의 상한을 먼저 계산해 두고 비용과 견줄 때(성능 논의)
- 한국어: 이득에 천장이 있다
- 설명: `cap` 이 "위에서 눌린 한계"라 아무리 잘돼도 그 이상은 없다는 뜻이 된다. 뒤에 검증 불가능한 비용을 붙이면 `capped benefit + untestable cost` 라는 기각 논리가 완성된다.
- 예문: You've argued the payoff is capped and then committed untestable code to capture it anyway.
- 유사어: the upside is bounded (더 수학적), there's a ceiling on the gain (풀어 쓴 형태)
- 반의어: the payoff compounds

## "The honest fix is ..."
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-18-occupied-share-request-debate.md
- 맥락: 값싼 우회책을 하나 제시한 직후 그것이 미봉책임을 인정하고 제대로 된 해법을 내놓을 때
- 한국어: 정직한 해법은 ~다
- 설명: `honest` 가 코드가 아니라 **엔지니어의 자세**를 수식한다. 앞에 `If you keep X: ... — but that's calibrated guessing` 처럼 우회책과 그 흠을 먼저 놓고, 이 문장으로 뒤집는 2단 구성이 관례다.
- 예문: The honest fix is two narrow crops — the extra OCR round-trip is cheaper than breaking the gate every occupied row.
- 유사어: the real fix (더 짧고 흔하다), the principled option (가장 격식)
- 반의어: the expedient workaround

## "funnel through one choke point"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 여러 메서드가 결국 한 함수로 모인다는 구조를 근거로 "여기만 고치면 된다"를 논증할 때
- 한국어: 한 지점으로 수렴하다
- 설명: `funnel` 은 깔때기라 여럿이 하나로 좁아지는 그림이고, `choke point` 는 그 좁은 목이다. 병목(`bottleneck`)이 성능 문제를 함의하는 것과 달리 이 짝은 중립적이라 **변경 지점의 유일성**을 말할 때 쓴다.
- 예문: Every existing method funnels through one choke point, so a sibling method disturbs nothing.
- 유사어: converge on a single entry point (더 형식적), all roads lead to X (비유적·구어)
- 반의어: the logic is scattered across call sites

## "die silently"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 예외도 로그도 없이 처리 경로 전체가 무력화되는 최악의 실패를 이름 붙일 때
- 한국어: 조용히 죽다
- 설명: 주어가 사람이 아니라 `the failure path` 같은 경로라는 점이 요령이다. `silently` 가 "관측 가능한 흔적이 없다"를 담아 심각도를 올린다. 뒤에 콜론을 찍고 죽는 지점을 열거하는 배치가 흔하다.
- 예문: The entire current failure path dies silently: the driver never raises the not-found error at all.
- 유사어: go dead without a trace (더 그림이 선명), be swallowed (예외에 한정)
- 반의어: fail loudly

## "stop firing"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 코드는 그대로 남아 있는데 조건이 바뀌어 가드·핸들러가 더는 발동하지 않게 됨을 말할 때
- 한국어: (검사·가드가) 더는 발동하지 않는다
- 설명: `fire` 는 이벤트·트리거가 터지는 동작이라 핸들러·훅·알림에 붙는다. 삭제된 게 아니라 **살아 있는 채로 잠든다**는 어감이라, 코드 검색으로는 안 보이는 결함을 설명하기에 맞다.
- 예문: The except clause that maps a missing alias to a data error stops firing.
- 유사어: never triggers (더 평이), becomes unreachable (도달 자체가 불가할 때만)
- 반의어: fires on every request

## "reach (something) unannounced"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-msearch-operational-review.md
- 맥락: 배포 절차상 경고가 뜨지 않아 변경이 운영 사본에 조용히 도달하는 위험을 말할 때
- 한국어: 예고 없이 ~에 닿다
- 설명: `unannounced` 는 원래 사람이 예고 없이 찾아올 때 쓰는 말인데, 주어를 변경(change)으로 바꾸면 "알림 없이 퍼진다"가 된다. 사람을 탓하지 않고 절차의 구멍만 짚는 어휘 선택이다.
- 예문: Any behavioural change to those two entry points would reach running office copies unannounced.
- 유사어: propagate without a warning (더 건조), land without anyone noticing (구어)
- 반의어: ship behind an explicit migration notice

## "sneak past"
- 레지스터: technical, conversational
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-18-occupied-share-request-debate.md
- 맥락: 부분 문자열 비교처럼 헐거운 검사를 값이 슬쩍 통과해 버릴 위험을 말할 때
- 한국어: 슬쩍 통과하다
- 설명: 값을 의인화해 검문을 몰래 지나가는 그림을 만든다. `pass` 가 중립적인 반면 `sneak past` 는 "통과하면 안 되는데 통과했다"를 담아, 검사 자체의 설계 결함까지 함께 지적한다.
- 예문: Enumerate every comparison against "corrected", including checks where substring-adjacent statuses could sneak past.
- 유사어: slip through (가장 흔한 짝), evade the check (더 형식적이고 의도적 어감)
- 반의어: be caught by the guard

## "like-for-like"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-bm-pm-anchor-9h.md
- 맥락: 두 값이 같은 기준·단위로 비교되고 있음을 한 단어로 보증할 때(시간대·통화·집계 비교)
- 한국어: 같은 기준끼리
- 설명: 하이픈 셋으로 묶인 부사구라 동사 뒤에 그대로 붙는다. 시간대 논의에서는 "둘 다 UTC 이므로 어긋나지 않는다"는 뜻이 되어, 뒤에 `no omission at all` 같은 결론을 바로 끌어낸다.
- 예문: If the indices store UTC, the naive anchor compares like-for-like against UTC storage — no omission at all.
- 유사어: apples to apples (회화체), on the same basis (가장 중립적)
- 반의어: comparing across mismatched units

## "ungated"
- 레지스터: technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-18-occupied-share-request-debate.md
- 맥락: 다른 동작에는 다 붙은 사전 검사가 유독 한 곳에만 빠져 있음을 지적할 때
- 한국어: 관문 없이 그냥 실행되는
- 설명: `gate`(사전 검사) 에 `un-` 을 붙인 조어다. 명사구 소제목으로 세우면 판정문이 되고, 뒤에 "하필 검증이 방금 실패한 그 순간에"를 붙이면 위험이 극대화된다.
- 예문: The Cancel click is ungated: it is a bare click on the same mislocatable popup.
- 유사어: unguarded (더 일반적), bypasses the check (동사구)
- 반의어: gated on an explicit check

## "lose its click affordance"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: UI 요소가 눌리는 것처럼 보이는 신호 자체를 잃어 사용자가 시도조차 못 하게 됨을 설명할 때(프런트엔드)
- 한국어: 클릭 가능하다는 신호를 잃다
- 설명: `affordance` 는 디자인 용어로 "이렇게 쓰라고 알려 주는 형태"다. `becomes unclickable` 이 동작만 말한다면 이쪽은 **사용자가 인지하는 단서**까지 말하므로, 에러 없이 조용히 죽은 UI 를 설명하기에 정확하다.
- 예문: A renamed field arrives as "No", and every row loses its click affordance.
- 유사어: stop looking interactive (풀어 쓴 회화체), become inert (더 짧고 기술적)
- 반의어: regain its click affordance

## "it degrades, it doesn't crash"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 두 실패 방향을 실측한 뒤 어느 쪽으로 기울어 실패할지 기본값을 고를 때
- 한국어: 성능이 떨어질 뿐 터지지는 않는다
- 설명: 접속사 없이 쉼표만으로 두 절을 이어 판정을 리듬으로 만든다. `degrade` 는 기능이 남은 채 품질만 내려가는 실패이고 `crash` 는 전부 잃는 실패라, 이 대비가 fail-open 기본값의 근거가 된다.
- 예문: Opening a measurement with no raw data renders an empty screen — it degrades, it doesn't crash.
- 유사어: fails soft (가장 압축적), still usable, just worse (회화체)
- 반의어: it takes the whole page down

## "a standing hazard"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-20-bm-pm-anchor-9h.md
- 맥락: 지금 당장 사고는 아니지만 문서가 이미 위험으로 등재해 둔 상태를 가리킬 때
- 한국어: 상존하는 위험
- 설명: `standing` 이 "계속 서 있는", 즉 해소되지 않고 유지되는 상태를 뜻한다(`standing order` 와 같은 용법). 저장소 문서가 스스로 표시해 뒀다는 사실과 붙으면 "몰랐다"는 변명이 막힌다.
- 예문: Not a defensible local choice — the repo's own docs flag it as a standing hazard.
- 유사어: a known trap (더 가볍다), an accepted risk (감수하기로 결정했을 때만)
- 반의어: a one-off slip

## "there's a real fork here"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto_recipe_creator
- 맥락: 구현에 들어가기 전, 되돌리기 어려운 갈림길이 있음을 알리고 판단을 요청할 때
- 한국어: 여기 진짜 갈림길이 있다
- 설명: `fork` 는 길이 갈리는 지점이라 두 방향 모두 유효할 때 쓴다. `real` 이 "형식적인 선택지가 아니다"를 담아 상대가 그냥 넘기지 못하게 잡아 둔다. 뒤에 무엇과 충돌하는지 한 줄로 잇는 게 요령이다.
- 예문: Before I build: there's a real fork here, and it touches the design you wrote this morning.
- 유사어: this is a genuine either-or (더 건조), we need to pick a lane (구어·비유)
- 반의어: there's only one sensible path

## "have a number attached"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto_recipe_creator
- 맥락: 인상·추측으로 오간 이야기를 실측으로 바꾸겠다고 예고할 때
- 한국어: 질문에 숫자를 붙이다
- 설명: `attach` 가 숫자를 질문에 물리적으로 달아 두는 그림을 만든다. `measure it` 이 행동만 말한다면 이쪽은 **질문이 남는다**는 점까지 담아, "그래서 얼마나 빠른데?" 를 정량으로 닫겠다는 뜻이 된다.
- 예문: Let me measure the actual cost per iteration so the "it's too fast" question has a number attached.
- 유사어: put a number on it (가장 흔한 짝), quantify it (가장 격식)
- 반의어: leave it at a hunch

## "a good place to be"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 의도치 않게 얻은 결과가 알고 보니 유리한 위치임을 담담하게 말할 때
- 한국어: 있기 좋은 자리다
- 설명: 성과를 자랑하지 않고 **상태**로만 말하는 완곡 표현이다. 앞에 `That was somewhat accidental, but` 를 두면 겸손과 이점을 동시에 챙길 수 있다. 뒤에는 그래서 무엇이 가능해졌는지가 콜론으로 따라붙는다.
- 예문: That was somewhat accidental, but it's a good place to be: the decision is now yours to make on data-modelling grounds.
- 유사어: we're in decent shape (더 캐주얼), that leaves us well positioned (격식)
- 반의어: we've painted ourselves into a corner
