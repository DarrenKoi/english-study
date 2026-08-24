# 2026-08-25 — 새 표현

## "make X actually mean something"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 이름만 있고 효과가 없던 옵션·규칙에 실제 힘을 실어 줄 때(코드 리뷰·설계 논의, 구어~중간 격식)
- 한국어: X가 실제로 뭔가를 뜻하게 만들다 — 허울뿐이던 설정을 진짜로 작동시키다
- 설명: `actually` 가 핵심이다. "지금까지는 strict 로 놓아도 아무 차이가 없었다"는 전제를 한 단어에 담고, 그걸 고치는 변경을 정당화한다. 새 기능을 더했다는 말이 아니라 있던 스위치가 비로소 켜졌다는 말이라, 변경 규모는 작아 보이고 가치는 커 보인다.
- 예문: Giving the step a real needle costs nothing under the default `lenient` and makes `strict` actually mean something.
- 유사어: give X teeth (더 구어적·비유적; 기존 표현 `has teeth` 참고), put X into effect (격식·행정 어투의 "시행하다")
- 반의어: X is still decoration / only nominally kept (이름만 남은 상태)

## "Red for the right reason."
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: TDD 에서 새 테스트가 실패했을 때, 그 실패가 의도한 원인 때문인지 확인하고 보고할 때(커밋 메시지·페어 프로그래밍, 짧은 구어)
- 한국어: 제대로 된 이유로 빨간불 — 테스트가 실패하긴 하는데, 우리가 잡으려던 바로 그 결함 때문에 실패한다
- 설명: 실패 자체는 쉽다. 오타나 import 에러로도 빨개진다. 이 문장은 "실패했다"에 "왜 실패했는지 봤다"를 덧붙여, 다음 단계(구현)로 넘어가도 된다는 판정을 다섯 단어로 낸다. 노트에 이미 있는 `green for the wrong reason` 의 정확한 짝 — 통과도 실패도 이유를 봐야 한다.
- 예문: Red for the right reason: the test fails on the missing Caps toggle, not on an import error, so I can implement now.
- 유사어: Red confirmed. (이유 확인까지는 담지 않은 더 짧은 판), the failure is the one we expected (풀어쓴 격식체)
- 반의어: green for the wrong reason (틀린 이유로 통과), a false red (엉뚱한 이유로 실패)

## "harden (a gate / a check)"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 이미 있던 검사·보호 장치를 더 엄격하고 뚫기 어렵게 고쳤다고 말할 때(커밋 요약·변경 설명, 중간 격식)
- 한국어: (검사·게이트를) 강화하다, 단단하게 만들다
- 설명: 보안 분야의 "hardening" 이 일반 코드 검사에도 그대로 쓰인다. `fix` 는 틀린 걸 고쳤다는 뜻이고 `harden` 은 틀리진 않았지만 느슨했던 걸 조였다는 뜻이라, 리뷰어가 "뭐가 버그였느냐"고 되묻지 않게 한다. 목적어로 gate·check·validation·boundary 가 잘 붙는다.
- 예문: I hardened the typing gate so the editor step confirms on the popup title before it types anything.
- 유사어: tighten (a check) (더 평이하고 정도가 약함), lock down (범위·권한을 잠근다는 뉘앙스)
- 반의어: loosen / relax (a check), be silently loosened

## "whose entire job is X"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 어떤 책임이 왜 그 함수·모듈에 있어야 하는지 근거를 댈 때(설계 근거·코드 리뷰, 문어)
- 한국어: 그것의 일이 오로지 X인 — X만을 위해 존재하는
- 설명: 관계절 `whose ... is` 에 `entire` 를 넣어 "다른 일은 안 한다"를 강조한다. 책임 배치 논증에 쓰면 "여기가 자연스러운 자리"라는 주장이 한 구절로 끝난다. 뒤에 `the one function that owns X` 처럼 바꿔 말해도 무게가 같다.
- 예문: The Alt hold belongs inside `perform_remote_click`, whose entire job is owning that ordering.
- 유사어: the one function that owns X (같은 뜻, 명사구), X is its only responsibility (더 평이함)
- 반의어: a function that wears two hats (역할이 둘인 함수; 기존 표현 `wear two hats`)

## "different failures, different budgets"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 두 재시도·예산·한도를 왜 합치지 않았는지 짧게 설명할 때(설계 근거·회의 발언)
- 한국어: 실패가 다르니 예산도 따로 — 성격이 다른 문제에 같은 한도를 쓰지 않는다
- 설명: 동사 없는 `different X, different Y` 대구는 규칙을 격언처럼 못 박는 장치다. 앞에 긴 설명을 하고 이 네 단어로 닫으면 근거가 끝났다는 신호가 된다. X·Y 자리는 자유롭다 — `different inputs, different outputs`, `different audience, different tone`.
- 예문: Pushing back two stacked windows shouldn't consume the click-retry budget — different failures, different budgets.
- 유사어: keep the two budgets separate (평이한 서술형), one budget per failure mode (규칙 문장으로)
- 반의어: lumped together / one budget for everything

## "land off-target"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 클릭·요청·추정이 의도한 지점에서 벗어났다고 말할 때(장애 보고·현장 대화)
- 한국어: 빗나가다, 엉뚱한 곳에 떨어지다
- 설명: 사격 은유. `miss` 와 달리 "어디엔가 떨어지긴 했다"는 그림이 살아 있어, 좌표 기반 자동화나 추정치 오차에 잘 맞는다. `on-target` 이 반대말이고, `wide of the mark` 는 같은 은유의 오래된 판이다.
- 예문: If the reveal click lands off-target at the office, tell me what it hit and I'll move the ratio.
- 유사어: miss (짧고 결과만), go wide (구어), be off by N px (수치로)
- 반의어: land on target / hit the mark

## "dwell"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 자동화·계측에서 어떤 동작 뒤 일부러 머무는 짧은 시간을 가리킬 때(코드 주석·타이밍 설명, 전문)
- 한국어: 체류 (시간) — 입력이 등록되도록 일부러 두는 짧은 정지
- 설명: 명사로도 동사로도 쓴다(`a 0.6 s dwell`, `dwell for a tick`). `wait` 는 "무언가를 기다린다", `delay` 는 "늦춘다"인데 `dwell` 은 "그 자리에 머문다"라, 마우스·키·프로브가 위치에 도착한 뒤 등록될 때까지 두는 시간을 정확히 가리킨다. 레이저·CNC·SEM 분야의 dwell time 과 같은 단어다.
- 예문: Alt needs its own dwell after the cursor has arrived, or the modifier and the click land in the same tick.
- 유사어: settle time (시스템이 안정될 때까지의 대기; 뉘앙스가 가장 가깝다), hold (버튼을 누른 채 유지), pause (가장 일반적)
- 반의어: fire immediately

## "Now that's genuinely diagnostic."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 상대의 관찰이 원인을 좁혀 주는 진짜 단서일 때 반응으로(디버깅 대화, 구어)
- 한국어: 이제야 진짜 단서가 나왔다 — 그 관찰은 원인을 가려 준다
- 설명: `diagnostic` 을 형용사로 써서 "증상이 아니라 진단에 쓸 정보"라는 뜻을 만든다. `Now that's ...` 은 앞선 보고들과 대비시키는 어투라, 상대를 칭찬하면서 "이전 보고는 애매했다"는 말을 부드럽게 덧붙인다. `genuinely` 가 붙으면 의례적 칭찬이 아니라는 표시.
- 예문: "You typed NFRA. ECH…" — now that's genuinely diagnostic: exactly the Shift characters are missing.
- 유사어: that narrows it down (평이함), that's the tell (기존 표현; 결정적 단서 쪽)
- 반의어: that tells me nothing / a poor diagnostic surface

## "on both counts"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 두 가지 점을 한꺼번에 판정할 때(검증 결과 보고·논쟁 정리, 문어·구어 모두)
- 한국어: 두 가지 점 모두에서 — 두 항목 다
- 설명: `count` 는 법정 용어(공소 사실 하나하나)에서 왔다. `confirmed / wrong / guilty on both counts` 처럼 판정 동사 뒤에 붙어 "항목별로 따져 봤고 둘 다 같은 결론"이라는 뜻을 준다. 셋 이상이면 `on all counts`, 하나만이면 `on one count`.
- 예문: Hypothesis confirmed on both counts: the dropped characters are exactly the Shift ones, and the File failure is my label gate.
- 유사어: in both respects (더 격식), both ways (구어)
- 반의어: on neither count

## "a clean control group"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 디버깅에서 "달라지지 않은 쪽"이 원인을 증명해 줄 때(원인 분석 보고, 중간 격식)
- 한국어: 깨끗한 대조군 — 조건 하나만 다르고 나머지가 같아서 비교 근거가 되는 집단
- 설명: 실험 과학 어휘를 디버깅에 옮겨 쓴다. 소문자는 하나도 안 사라졌다는 사실이 "대문자만 다른 경로를 탄다"는 가설의 대조군 역할을 한다는 논리. `clean` 은 교란 변수가 없다는 뜻이라, 이 말을 쓰면 "우연이 아니라 통제된 비교"라는 주장이 된다.
- 예문: Lowercase letters take the other branch, and that's precisely why not one of them was lost — a clean control group.
- 유사어: a baseline (비교 기준선; 더 넓음), the unchanged half (평이한 풀어쓰기)
- 반의어: a confound (기존 표현; 교란 변수)

## "Here's what happened, without the jargon."
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 기술 설명을 비전문가나 바쁜 상대에게 다시 풀어 줄 때 첫 문장으로(구어·메시지)
- 한국어: 전문 용어 빼고 무슨 일이었는지 설명하면 이렇다
- 설명: `without the jargon` 이 "쉽게 말하면"의 자연스러운 영어다. `in simple terms` 보다 상대를 낮추는 느낌이 적고, "앞선 설명이 어려웠다"는 걸 화자가 먼저 인정하는 어투다. 뒤에는 은유·일상 비유가 이어지는 게 보통이다.
- 예문: Here's what happened, without the jargon: the remote relays key presses one at a time and never says "Shift was down."
- 유사어: in plain terms / in plain English (짧고 흔함), let me put it another way (설명을 바꿔 보겠다는 완곡한 판)
- 반의어: (마땅한 대체 표현 없음)

## "a quirk of X, not something I chose"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 이상한 동작의 출처가 라이브러리·플랫폼이지 내 결정이 아님을 밝힐 때(장애 설명, 구어)
- 한국어: 그건 X의 특이한 버릇이지 내가 고른 게 아니다
- 설명: `quirk` 는 버그라고 부르기엔 의도된 동작이고 정상이라고 부르기엔 이상한 것을 가리킨다. 뒤의 `not something I chose` 는 책임 소재를 정리하되 변명처럼 들리지 않게 하는 장치 — 사실 진술의 형태이기 때문이다. 설계 결정과 환경 제약을 구분할 때 쓸모가 크다.
- 예문: The typing library picks the unicode path for anything needing Shift — that's a quirk of the library, not something I chose.
- 유사어: an idiosyncrasy of X (더 격식·학술), that's just how X behaves (평이함)
- 반의어: a deliberate act (기존 표현; 의도한 선택)

## "be straight that …"
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 상대가 싫어할 수 있는 사실(요청 일부를 안 했다 등)을 숨기지 않고 먼저 밝힐 때(구어·메시지)
- 한국어: ~라는 점을 솔직히 말해 두다
- 설명: `be straight with someone` 은 "숨기지 않고 말하다"이고, `that` 절을 붙이면 무엇을 숨기지 않는지 바로 잇는다. `to be honest` 보다 능동적이다 — 상대가 묻기 전에 먼저 꺼낸다는 뜻이 있다. 요청을 좁혔거나 일부를 거절했을 때 이 어투로 꺼내면 신뢰가 깎이지 않는다.
- 예문: Four I deliberately left alone, and I want to be straight that this is me narrowing your request.
- 유사어: I'll be upfront: … (같은 무게), in the interest of full disclosure (격식·약간 유머러스)
- 반의어: bury (the real fixes) / gloss over (기존 표현)

## "those aren't comparable outcomes"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 두 위험을 같은 저울에 올리면 안 된다고 잘라 말할 때(트레이드오프 논증, 문어·구어)
- 한국어: 그 둘은 견줄 수 있는 결과가 아니다 — 하나는 훨씬 나쁘다
- 설명: "느린 데모"와 "안 되는 데모"처럼 표면상 둘 다 단점인 것을 놓고, 정도 차이가 아니라 종류 차이라고 선언한다. `comparable` 을 부정하면 "비교 자체가 잘못됐다"는 뜻이라, 상대가 "그래도 30% 는 크다"고 되받기 어려워진다.
- 예문: Shaving those waits risks a demo that doesn't work rather than a demo that's slow, and those aren't comparable outcomes.
- 유사어: that's not a fair trade (구어), the two aren't in the same league (관용구)
- 반의어: a wash (기존 표현; 어느 쪽이든 비슷함)

## "shave (a wait)"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 시간·크기를 조금씩 깎아 줄일 때(성능 튜닝 대화, 구어)
- 한국어: (대기 시간을) 깎다, 조금 줄이다
- 설명: 면도 은유라 크게 잘라내는 `cut` 과 달리 표면을 얇게 밀어내는 느낌이다. `shave 200 ms off the startup` 처럼 `off` 와 수치를 함께 쓰면 가장 자연스럽고, 목적어로 직접 받으면(`shaving them`) "이미 얇은 걸 더 깎는다"는 위험 뉘앙스가 살아난다.
- 예문: Shaving the modifier settle windows saves a couple of seconds at most, and it's the one place a cut can break the demo.
- 유사어: trim (비슷하게 소폭), cut (더 큼·중립), squeeze (짜내듯 줄임)
- 반의어: pad (a wait) / add breathing room

## "a structural weakness, not a tuning problem"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 상수를 조정해서 풀릴 문제가 아니라 방식 자체가 취약하다고 판정할 때(원인 분석·설계 검토, 문어)
- 한국어: 구조적 약점이지 조정 문제가 아니다 — 값을 바꿔선 안 풀린다
- 설명: 디버깅에서 가장 중요한 분기 하나를 한 줄에 담는다. `tuning` 은 파라미터를 만지는 일이고 `structural` 은 접근법 자체다. 이 판정을 먼저 내려 두면 "대기 시간을 더 늘려 보자"는 제안이 논리적으로 막힌다. `not a tuning problem` 대신 `not a timing problem` 으로도 자주 쓴다.
- 예문: Fast Caps toggling breaking the memo points at a structural weakness in the approach, not a tuning problem.
- 유사어: a design flaw, not a parameter issue (같은 대비, 더 평이함), the approach is wrong, not the numbers (구어)
- 반의어: a matter of tuning / the operating point (기존 표현)

## "off the table"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 어떤 선택지를 더는 고려하지 않기로 했다고 밝힐 때(협상·설계 논의, 구어~중간 격식)
- 한국어: 선택지에서 빠졌다, 더는 고려 대상이 아니다
- 설명: 협상 테이블 은유. 물건을 테이블에서 치우면 거래 대상이 아니듯, 어떤 방법이 `off the table` 이면 이유가 확정돼 논의 자체를 끝낸다는 뜻이다. `on the table` 이 반대. 증거를 댄 뒤 결론으로 쓰면 강하고, 증거 없이 쓰면 독단으로 들린다.
- 예문: The equipment ignored a real left-Shift scan code, so held modifiers are off the table.
- 유사어: ruled out (기존 표현; 근거로 배제), not an option (평이함)
- 반의어: on the table / still in play

## "stub (a fake X)"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 실제 장치·서비스 대신 관찰된 동작만 흉내내는 대역을 코드로 만들 때(테스트 설명, 전문)
- 한국어: (가짜 X를) 스텁으로 세우다 — 최소 동작만 흉내내는 대역을 만들다
- 설명: 명사 `stub` 을 동사로 쓴다. `mock` 이 호출 여부까지 검증하는 대역이라면 `stub` 은 정해진 응답만 돌려주는 더 단순한 대역이다. 이 문장의 핵심은 뒤에 붙은 `the way we've observed RCS behaving` — 지어낸 동작이 아니라 실측한 동작을 흉내냈다는 근거를 함께 적어야 스텁 테스트가 신뢰를 얻는다.
- 예문: To sanity-check it without the equipment, I stubbed a fake keyboard that remembers Caps state and ignores held modifiers.
- 유사어: mock out (검증까지 포함, 더 넓게 쓰임), fake (명사·동사 모두; 가장 느슨함)
- 반의어: run it against the real thing

## "honest but partial"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 3ae7de12
- 맥락: 기존 신호·플래그가 틀리진 않지만 일부만 본다고 평가할 때(원인 분석, 문어)
- 한국어: 거짓은 아니지만 부분적이다 — 맞는 말만 하는데 전부를 말하지는 않는다
- 설명: 두 형용사를 `but` 으로 묶어 평가를 한 번에 끝낸다. 기존 코드를 비난하지 않으면서("honest") 왜 부족한지("partial")를 같이 말하므로, 리팩터링 근거를 댈 때 저항이 적다. 뒤에 "무엇을 못 보는지"가 반드시 따라와야 한다.
- 예문: The existing `setPending` flag is honest but partial: it only covers the file batch, not the history lookup before it.
- 유사어: correct as far as it goes (관용구, 같은 뜻), incomplete rather than wrong (평이함)
- 반의어: a wrong-but-confident signal (기존 표현)

## "the same failure with more confidence"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 3ae7de12
- 맥락: 새 증상이 이미 문서화된 실패의 더 나쁜 변형임을 짚을 때(설계 문서 인용·버그 분류, 문어)
- 한국어: 같은 실패인데 더 자신 있게 틀린 것 — 빈 상태를 확신에 차서 보여 주는 셈
- 설명: 로딩 중에 이전 화면을 그대로 두는 것과 빈 상태를 보여 주는 것을 같은 실패로 묶고, 후자가 더 나쁜 이유를 `with more confidence` 한 구절로 말한다. "틀린 답을 자신 있게 낸다"는 틀은 모니터링·UI·통계 어디서나 통한다.
- 예문: A frozen page isn't a loading state, and an empty state shown during a fetch is the same failure with more confidence.
- 유사어: a louder version of the same bug (구어), the same class of error, stated more assertively (격식·장황)
- 반의어: an honest stale marker

## "safe for X, wrong for Y"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 3ae7de12
- 맥락: 같은 함수·값이 한 용도엔 맞고 다른 용도엔 틀린다고 구분할 때(코드 리뷰·재사용 판단, 문어)
- 한국어: X에는 안전하고 Y에는 틀리다 — 용도에 따라 판정이 갈린다
- 설명: 재사용하려던 도구를 기각하는 정확한 방식이다. "그 함수는 나쁘다"가 아니라 "그 함수의 질문과 내 질문이 다르다"고 말하므로, 원작자를 공격하지 않으면서 새 함수를 만들 근거가 선다. X·Y 자리에 따옴표로 묶은 질문 문장을 넣으면 특히 선명하다.
- 예문: `isSetPoolComplete` returns true vacuously on an empty key — safe for "may I rewrite the URL param", wrong for "may I show this number".
- 유사어: fit for one purpose, not the other (평이함), right tool, wrong question (구어)
- 반의어: fit for both purposes

## "under-report"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 3ae7de12
- 맥락: 계기·집계가 실제보다 낮은 값을 보인다고 말할 때(데이터·모니터링, 중간 격식)
- 한국어: 실제보다 적게 보고하다, 낮게 잡히다
- 설명: 접두사 `under-` 로 방향까지 담는 동사다. `is wrong` 은 방향을 말하지 않지만 `under-reports` 는 "진짜 값은 이보다 크다"까지 전달한다. 통계·의료·품질 보고의 표준 어휘이며 반대는 `over-report`. 명사형은 `under-reporting`.
- 예문: The rail's 호환 count reads the same `setFiles` map, so it under-reports for the same window.
- 유사어: understate (기존 표현; 서술·주장 쪽), read low (계기 어휘, 구어)
- 반의어: over-report / overstate

## "A/B (동사)"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator 6e44bf1a
- 맥락: 두 방식을 같은 조건에서 번갈아 시험해 보라고 할 때(현장 검증 지시, 구어)
- 한국어: 두 안을 번갈아 시험하다, A/B 로 비교하다
- 설명: 명사 `A/B test` 를 동사로 줄여 쓴다. `so you can A/B at the office without me pushing anything` 처럼 "코드 변경 없이 현장에서 고를 수 있게 해 뒀다"는 맥락에 특히 잘 맞는다. 명사로 쓸 때는 `an A/B`, 동사로는 `A/B it`.
- 예문: The mode switch keeps all three typing paths available, so you can A/B them at the office without a new push.
- 유사어: try both side by side (평이함), compare head-to-head (기존 표현 `a head-to-head` 참고)
- 반의어: (마땅한 대체 표현 없음)

## "control plane"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/orchestration/2026-08-24-herdr-orchestration_v1.md
- 맥락: 시스템에서 "무엇을 할지 결정·조정하는 층"과 "실제 일을 하는 층"을 구분할 때(아키텍처 문서, 전문)
- 한국어: 제어 평면 — 스케줄링·조정·상태 관리를 맡는 층(실제 데이터 처리는 data plane)
- 설명: 네트워크 장비에서 온 용어가 Kubernetes 를 거쳐 일반 아키텍처 어휘가 됐다. Herdr 문서는 "planner 나 scheduler 가 아니라 control plane" 이라고 못 박아, 작업 분해와 판단은 Manager 몫이고 Herdr 는 실행 표면만 제공한다는 경계를 그린다. 이 한 단어로 "그 도구에 기대하면 안 되는 것"이 정해진다.
- 예문: Herdr is an agent-aware terminal runtime and automation API — a control plane — so task decomposition and verification stay with the Manager.
- 유사어: orchestration layer (더 넓고 느슨함), the coordination layer (평이함)
- 반의어: data plane / the workers
