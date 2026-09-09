# 2026-09-10 — 새 표현

## "Three lines earn their place."
- 레지스터: professional, technical
- 출처: transcript:[assistant] llm-serving (common.env 정리)
- 맥락: 리뷰·리팩터링에서 "이 항목들은 남을 자격이 있다"고 판정할 때. 글·구어 다 되고 격식은 중간.
- 한국어: 세 줄은 제 몫을 한다 / 자리값을 한다.
- 설명: `earn one's place` 는 존재 자체가 아니라 **기여로 자격을 얻는다**는 은유. 8줄 중 5줄을 지우고 3줄만 남길 때, "이건 필요하다" 보다 판정의 근거가 선다.
- 예문: Of the eight settings in that file, three lines earn their place and the rest just restate the code's defaults.
- 유사어: pull its weight (제 몫의 짐을 진다, 더 구어), justify its existence (더 딱딱한 격식), pay for itself (비용 대비 이득 쪽)
- 반의어: dead weight (짐만 되는 것), be along for the ride (묻어가다)

## "that's expected noise, not a fault"
- 레지스터: technical, professional
- 출처: transcript:[assistant] llm-serving (check_vlm 이 비활성 인스턴스를 down 으로 표시)
- 맥락: 경고·빨간 줄이 뜨지만 정상인 상황을 동료에게 미리 알려줄 때. 팀 채팅·코드 리뷰 코멘트.
- 한국어: 그건 예상된 잡음이지 결함이 아니다.
- 설명: `noise` 를 신호처리 은유로 써서 "관측되지만 의미 없음"을 한 단어로 처리한다. `not a fault` 를 붙여 대비시키는 X-not-Y 구조가 핵심 — 오해를 미리 지운다.
- 예문: `check_vlm.py` will always list the A/B bench instance as down — that's expected noise, not a fault.
- 유사어: that's benign (더 짧고 격식), it's cosmetic (표시상의 문제일 뿐), a known false positive (더 기술적·정확)
- 반의어: that's a real regression, that's the actual failure

## "held hostage by"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] llm-serving (start_all 가드 설명)
- 맥락: 하나가 막혀서 나머지 전부가 못 나가는 구조적 문제를 강조할 때. 회의·구어에서 강한 비유.
- 한국어: ~에 발목이 잡히다 / 인질로 잡히다.
- 설명: 인질 은유라 감정이 실린다. 단순 blocked 보다 "부당하게, 그것 하나 때문에" 라는 뉘앙스가 붙어 우선순위를 설득할 때 효과가 크다.
- 예문: Catching that exit is precisely when you'd least want the production models held hostage by the general-purpose one.
- 유사어: blocked on (중립·격식), at the mercy of (더 문어적), bottlenecked by (기술적)
- 반의어: fail independently, degrade gracefully

## "it's the shortest path"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] llm-serving (git checkout 으로 복구 권유)
- 맥락: 여러 해법 중 하나를 추천하며 근거를 한 마디로 댈 때. 구어·문어 둘 다.
- 한국어: 그게 제일 빠른 길이다.
- 설명: 최선(best)이 아니라 **최단(shortest)** 이라고 말해 판단 범위를 좁힌다. 완벽하지 않을 수 있음을 인정하면서도 지금 고르라고 미는 표현.
- 예문: Restore it — one command, and it's the shortest path.
- 유사어: it's the cheapest fix (비용 강조), that's the quick win (더 구어), the path of least resistance (마찰이 적다 쪽, 살짝 부정적)
- 반의어: the long way round, the proper fix

## "mixing it in would have muddied this commit"
- 레지스터: technical, professional
- 출처: transcript:[assistant] llm-serving (무관한 문서 수정을 따로 뺀 이유)
- 맥락: 커밋·PR 범위를 좁게 유지한 이유를 설명할 때. 코드 리뷰 코멘트에 그대로 쓸 수 있다.
- 한국어: 같이 넣었으면 이 커밋이 탁해졌을 것이다.
- 설명: `muddy` 는 맑은 물에 흙을 풀어 흐리게 만드는 동사. 커밋을 "읽을 수 있는 것"으로 보는 관점이 담겨 있어 scope creep 을 지적할 때 자연스럽다.
- 예문: That fix predates today, so it's an unrelated change and mixing it in would have muddied this commit.
- 유사어: it would blur the diff (더 평이), that's scope creep (문제 이름을 붙이는 쪽), it would bury the real change (묻힌다는 결과 강조)
- 반의어: keep the commit focused, a single-purpose diff

## "an adapter, not a smell"
- 레지스터: technical
- 출처: transcript:[assistant] llm-serving (`except SystemExit` 변호)
- 맥락: 관행상 나쁜 패턴처럼 보이는 코드를 정당화할 때. 코드 리뷰 서면.
- 한국어: 이건 냄새가 아니라 어댑터다.
- 설명: `code smell` 이라는 기존 용어를 끌어와 **먼저 인정하고 뒤집는다**. 예상되는 반박을 선점하는 X-not-Y 구조라 리뷰에서 방어력이 높다.
- 예문: The `except SystemExit` here is an adapter, not a smell — it converts "abort the program" into "fail this one instance."
- 유사어: it's deliberate, not accidental (의도성 강조), that's a seam, not a hack (설계 용어 쪽)
- 반의어: that's a genuine code smell, this is papering over the problem

## "reuse, not reimplement"
- 레지스터: technical
- 출처: transcript:[assistant] llm-serving (import 옆 주석)
- 맥락: 코드 주석이나 커밋 메시지에서 선택의 근거를 두 단어로 남길 때. 매우 압축된 서면.
- 한국어: 다시 짜지 말고 가져다 쓴다.
- 설명: 동사 두 개를 콤마로 대비시켜 문장 없이 원칙만 남기는 형태. 주석·슬라이드 제목·PR 체크리스트에서 잘 먹힌다.
- 예문: `from start_model import stop_if_already_running`  # reuse, not reimplement
- 유사어: don't roll your own (구어·경고조), lean on the existing helper (풀어 쓴 회화체)
- 반의어: write a second stop-and-wait, roll your own

## "Both resolve on their own."
- 레지스터: conversational, technical
- 출처: transcript:[assistant] llm-serving (D-state 프로세스 설명)
- 맥락: 상대가 걱정하는 현상이 손댈 필요 없이 사라진다고 안심시킬 때. 구어·서면 모두.
- 한국어: 둘 다 알아서 풀린다.
- 설명: `resolve` 를 자동사로 쓰는 게 요령 — 목적어도 행위자도 없어 "누가 고치지 않아도"가 문장 구조 자체에 들어간다. `fix themselves` 보다 한 단계 격식이 높다.
- 예문: Both resolve on their own, typically within seconds, so the warning is worth checking but not worth acting on.
- 유사어: it clears itself (더 구어), it's self-limiting (의학·격식 차용), give it a moment (지시형 구어)
- 반의어: it needs manual intervention, it won't clear until you restart

## "a drift trap"
- 레지스터: technical, professional
- 출처: transcript:[assistant] llm-serving (기본값이 코드와 설정에 두 번 선언된 문제)
- 맥락: 지금은 멀쩡한데 나중에 조용히 어긋날 구조를 지적할 때. 설계 리뷰 서면.
- 한국어: (값이) 어긋나기 딱 좋은 함정.
- 설명: `drift` 는 두 사본이 시간에 따라 서서히 벌어지는 현상. `trap` 을 붙여 "지금은 무해해 보인다"는 함정성을 더한다. 중복 자체가 아니라 **미래 비용**을 지적하는 프레임.
- 예문: It reads as harmless redundancy, but a default declared twice is a drift trap.
- 유사어: a footgun (더 구어·즉각적 사고), a maintenance hazard (더 딱딱), two sources of truth (문제를 이름으로 지목)
- 반의어: a single source of truth

## "fails in a way that looks like success"
- 레지스터: technical, professional
- 출처: transcript:[assistant] llm-serving (start_all 을 실행 중인 스택 위에 다시 돌릴 때)
- 맥락: 가장 위험한 실패 유형을 경고할 때. 사고 보고서·설계 문서에 잘 어울린다.
- 한국어: 성공처럼 보이는 방식으로 실패한다.
- 설명: 관계절 `in a way that ...` 이 실패의 **양상**을 수식한다. 조용한 실패는 시끄러운 실패보다 나쁘다는 엔지니어링 상식을 한 문장에 담는 정형구.
- 예문: Running the launcher on a live stack fails in a way that looks like success — the old instance answers the readiness probe.
- 유사어: it fails silently (더 짧고 흔함), it's a false green (CI 맥락), it degrades without telling you (풀어 쓴 회화체)
- 반의어: it fails loudly, it dies at load

## "decay into wrong instructions"
- 레지스터: professional, technical
- 출처: transcript:[assistant] llm-serving (오래된 docstring 에 대해)
- 맥락: 문서·주석이 방치되면 단순히 낡는 게 아니라 해롭게 변한다고 주장할 때. 서면·격식.
- 한국어: (문서가) 썩어서 틀린 지시가 되어 버린다.
- 설명: `decay` 는 방사성 붕괴·부패의 은유라 **시간이 지나면 저절로** 일어난다는 뜻이 붙는다. `become` 대신 쓰면 관리 부재의 책임까지 함께 지적된다.
- 예문: Docstrings that encode workflow rather than describing signatures decay into wrong instructions the moment the code changes.
- 유사어: go stale (가장 흔한 구어), rot (더 거칠고 강함), drift out of date (중립·완만)
- 반의어: stay in step with the code, remain accurate

## "backwards from the other two"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] llm-serving (site.env 만 override 규칙이 반대)
- 맥락: 세트 안에서 하나만 규칙이 반대라 헷갈린다고 짚을 때. 구어·문서 주석 모두.
- 한국어: 나머지 둘과 정반대다.
- 설명: `backwards` 를 부사로 쓰고 `from + 비교 대상` 을 붙이는 형태. `different from` 이 "다르다"에서 멈추는 데 비해, 방향까지 알려줘 독자가 규칙을 뒤집어 기억하게 만든다.
- 예문: `site.env` is backwards from the other two — it's the only one a shell export can override.
- 유사어: the odd one out (집합에서 튄다는 쪽, 구어), inverted relative to (격식·기술), the exception here is X
- 반의어: consistent with the others, follows the same rule
