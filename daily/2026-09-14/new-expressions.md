# 2026-09-14 — 새 표현

## "a shared, scarce resource"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 왜 어떤 자원을 아껴 써야 하는지 설계 근거를 한 구로 못 박을 때(문서·격식)
- 한국어: 여럿이 같이 쓰는데 양은 적은 자원
- 설명: `shared` 와 `scarce` 두 형용사를 쉼표로 나란히 두면 "공유된다 + 부족하다"가 각각 독립된 근거로 읽힌다. 둘 중 하나만으로는 문제가 안 되지만 합쳐지면 경합이 생긴다는 논리를 형용사 배치만으로 전달한다.
- 예문: The FTP server caps concurrent sessions and engineers use it too, so a session is a shared, scarce resource.
- 유사어: a contended resource (경합이 이미 일어나고 있음을 강조·기술), a bottleneck (자원보다 병목 지점 자체를 가리킴)
- 반의어: an abundant resource / cheap to open

## "A waiter blocking IS the intent"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 리뷰어가 버그로 오해할 만한 동작을 "의도한 것"이라고 선제 방어할 때(코드 주석·docstring)
- 한국어: 대기자가 멈춰 있는 것이 바로 의도다
- 설명: 동사 `IS` 를 대문자로 쓰는 것은 코드 주석에서 강세를 주는 관용 표기다(굵은 글씨를 못 쓰는 환경). 주어 `A waiter blocking` 은 명사 + 동명사로 "대기자가 블로킹하는 상황"을 한 덩어리로 만든다. 보통 `is intended` 같은 수동태로 흐르기 쉬운데, `the intent` 라는 명사를 보어로 세워 단정 강도를 높였다.
- 예문: There is no timeout because a waiter blocking IS the intent.
- 유사어: that's by design (구어·짧음), this is deliberate (격식 중간), working as intended (버그 리포트 답변 정형구)
- 반의어: an unintended side effect

## "release and clean up on the way out"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 컨텍스트 매니저·finally 블록처럼 "빠져나갈 때 정리한다"를 설명하는 docstring
- 한국어: 나가는 길에 해제하고 정리한다
- 설명: `on the way out` 은 "나가는 길에"라는 일상 표현인데, 함수·with 블록의 종료 시점을 가리키는 은유로 자연스럽게 쓰인다. 정확한 `at exit` 보다 사람 냄새가 나면서도 뜻이 흐려지지 않는다.
- 예문: The gate serialises callers sharing the key, then releases and cleans up on the way out.
- 유사어: on exit (더 건조·정확), in the teardown (테스트 문맥), when the block exits (풀어쓴 설명)
- 반의어: on the way in / on entry

## "hand the next arrival a different lock object"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 동시성 버그가 어떻게 생기는지 시나리오로 설명할 때(주석·설계 문서)
- 한국어: 다음에 오는 쪽에 다른 락 객체를 쥐여 주다
- 설명: `hand A B` 는 "A 에게 B 를 건네다"의 이중 목적어 구문이다. `the next arrival` 은 "다음 도착자"를 명사 하나로 의인화해, 스레드 이름을 붙이지 않고도 순서를 서술한다. 버그 설명에서 이런 의인화는 독자가 타임라인을 머릿속에 그리게 돕는다.
- 예문: Dropping the entry while someone still waits would hand the next arrival a different lock object, and the exclusion would be lost.
- 유사어: give the next caller a fresh lock (평이), the next caller would see a different lock (수동적 관점)

## "Whoever went first, no interleaving"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 순서는 상관없고 겹치지만 않으면 된다는 테스트 단언을 설명할 때(테스트 주석)
- 한국어: 누가 먼저 갔든 상관없다, 끼어들기만 없으면 된다
- 설명: `Whoever went first` 는 "누가 먼저였든"의 양보절이고, 뒤에 동사 없이 `no interleaving` 만 붙였다. 주석에서 허용되는 생략 문장으로, 두 조건을 콜론 없이 대비시킨다. `interleave` 는 두 실행이 번갈아 끼어드는 것을 뜻하는 동시성 용어다.
- 예문: Whoever went first, no interleaving: an "in" is always followed by its own "out".
- 유사어: order doesn't matter, only exclusivity does (풀어쓴 격식), regardless of who wins the race (경쟁 조건 문맥)
- 반의어: interleaved / racy

## "Provable by the next acquisition succeeding"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 테스트가 "어떻게 그 성질을 증명하는지"를 한 줄로 밝힐 때(주석)
- 한국어: 다음 획득이 막히지 않고 성공하는 것으로 증명된다
- 설명: `provable by + 동명사절` 은 증명 수단을 압축하는 형식이다. `the next acquisition succeeding` 은 명사 + 동명사 구조라 "다음 획득이 성공한다는 사실"이 통째로 증거가 된다. 락이 풀렸음을 직접 검사할 수 없을 때 "다시 잡혀야 풀린 것"이라는 논법을 표현한다.
- 예문: Provable by the next acquisition succeeding without blocking.
- 유사어: which we can verify by … (풀어쓴 문장), the proof is that … (구어에 가까움)

## "Same status, opposite response"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 겉보기에 같은 신호에 정반대로 대응해야 하는 함정을 경고할 때(주석·리뷰)
- 한국어: 상태 코드는 같은데 대응은 정반대
- 설명: 명사구 둘을 쉼표로 붙인 대구법이다. `same`/`opposite` 의 대비가 문장 구조 자체에 들어가 있어 "왜 두 429 를 구분해야 하는가"를 설명 없이도 각인시킨다. 뒤에 콜론이나 설명 문장이 따라오는 도입부로 쓴다.
- 예문: Same status, opposite response: retrying a throttled client sends more.
- 유사어: looks identical but calls for the opposite handling (풀어쓴 격식), don't treat these two alike (구어)

## "does not improve by waiting"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 재시도·대기가 소용없는 경우를 골라낼 때(설계 근거·리뷰)
- 한국어: 기다린다고 나아지지 않는다
- 설명: `improve by + 동명사` 로 "무엇을 해서 나아지는가"를 붙인다. 부정하면 그 수단이 무의미하다는 뜻이 된다. 죽은 서버·만료된 작업처럼 시간이 해결하지 못하는 실패를 가려낼 때 정확하다.
- 예문: A dead tool or an expired job does not improve by waiting.
- 유사어: waiting won't help (구어), is not transient (기술·상태 분류), retrying is pointless here (직설)
- 반의어: is transient / will clear on its own

## "jitter cancels and the base shows through"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 무작위 요소를 중립값으로 고정해 테스트 기대값을 설명할 때(주석)
- 한국어: 지터가 상쇄되어 기본값이 그대로 드러난다
- 설명: `show through` 는 얇은 천 아래 무늬가 비쳐 보이듯 "가려졌던 것이 드러난다"는 구동사다. 무작위 항이 0 이 되는 순간 밑에 있던 base 값이 그대로 보인다는 그림을 정확히 전달한다. `cancel` 은 자동사로 "상쇄되다".
- 예문: rand = 0.5 is the midpoint, so jitter cancels and the base shows through.
- 유사어: the noise drops out and you see the baseline (풀어쓴 구어), reduces to the base value (수학·건조)

## "only to then give up"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 헛수고가 되는 순서를 비꼬듯 지적할 때(주석·리뷰·구어)
- 한국어: 그러고 나서 결국 포기할 거면서
- 설명: `only to + 동사` 는 "결국 ~하고 말았다"는 허무한 결말을 붙이는 부정사 용법이다. 가운데 `then` 이 들어가 시간 순서가 더 또렷해진다. 앞에 동명사 주어(`Sleeping 4s`)를 두면 "그럴 거면 왜 했나"의 어조가 완성된다.
- 예문: Sleeping 4s only to then give up would hold the panel for nothing.
- 유사어: and then bail anyway (구어·강함), before ultimately giving up (격식·중립)

## "used to double as"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-09-ebeam-phase0-flattening.md
- 맥락: 한 값이 예전에 두 가지 의미를 겸했음을 밝히고 그 겸직을 없앴다고 설명할 때(docstring·변경 이력)
- 한국어: 예전에는 ~의 역할도 겸했다
- 설명: `double as` 는 "겸하다"의 구동사이고 `used to` 가 붙어 "지금은 아니다"를 함께 말한다. `None` 같은 값이 "모름"과 "AMAT 장비" 두 뜻을 동시에 가졌던 과거를 한 줄로 요약한다.
- 예문: None now means genuinely unknown. It used to double as "an AMAT tool".
- 유사어: also served as (격식), was overloaded to mean (기술·타입 문맥), did double duty as (구어)
- 반의어: now means one thing only

## "each carrying their own sizing rule"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 레이아웃이 어긋난 원인을 "규칙이 분산돼 있었다"로 진단할 때(설명·리뷰)
- 한국어: 각자 자기만의 크기 규칙을 안고 있는
- 설명: `carry` 를 "규칙을 지니고 있다"에 쓰면 그 규칙이 짐처럼 따라다닌다는 뉘앙스가 생긴다. `each … their own` 이 분산의 문제를 드러낸다. 분사구문이라 앞 명사 `two cards` 에 바로 붙는다.
- 예문: The earlier imbalance came from two cards each carrying their own sizing rule.
- 유사어: each with its own width logic (평이), with sizing decided in two places (원인을 장소로 표현)
- 반의어: sharing one sizing rule / sized by the parent

## "neither card needs to know how wide it is"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 책임을 상위로 올려 하위가 몰라도 되게 만든 설계를 설명할 때
- 한국어: 어느 카드도 자기 폭을 알 필요가 없다
- 설명: `needs to know` 의 부정은 "몰라도 된다"이며, 캡슐화·관심사 분리를 말하는 표준 어법이다. `how wide it is` 같은 간접의문절이 목적어로 온다. 주어 `neither card` 로 둘 모두를 한 번에 부정한다.
- 예문: Moving the width decision to a parent grid means neither card needs to know how wide it is.
- 유사어: the cards stay width-agnostic (기술 조어), the parent owns the width (책임 소재 표현)
- 반의어: each card sizes itself

## "pre-existing warnings in an unrelated file"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 검증 결과를 보고하면서 남은 경고가 내 변경 탓이 아님을 밝힐 때
- 한국어: 무관한 파일에 원래부터 있던 경고
- 설명: `pre-existing` 은 "이 변경 이전부터 있던"을 한 단어로 말하고, `unrelated` 가 책임 범위를 다시 한 번 좁힌다. 둘을 같이 쓰면 "내 diff 는 깨끗하다"를 변명처럼 들리지 않게 전달한다.
- 예문: Typecheck passes, and lint shows only two pre-existing warnings in an unrelated skewvoir file.
- 유사어: not introduced by this change (격식·직설), already there before I touched it (구어)
- 반의어: a new warning this diff introduces

## "there's nothing left for it to switch off"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 설정 항목을 지운 이유를 설명할 때, 대상이 사라져 설정이 무의미해졌다는 논리
- 한국어: 그 설정이 꺼 줄 대상이 이제 없다
- 설명: `there's nothing left for X to do` 구조다. `for it` 이 부정사의 의미상 주어이고, `switch off` 의 목적어가 `nothing` 으로 앞에 나갔다. 잔여 설정·죽은 코드를 정리할 때 근거를 대는 자연스러운 문장이다.
- 예문: I removed the "caveman": "off" line from skillOverrides, since there's nothing left for it to switch off.
- 유사어: the setting no longer has a target (격식), it would be a dangling override (기술)

## "Deliberately per-process"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 한계처럼 보이는 설계 선택이 의도였다고 문두에서 선언할 때(docstring·ADR)
- 한국어: 일부러 프로세스 단위로 둔 것이다
- 설명: 부사 `Deliberately` 를 문두에 두고 주어·동사를 생략한 조각 문장이다. "이건 실수가 아니라 선택"임을 먼저 박고, 콜론 뒤에서 근거를 편다. 리뷰어의 "왜 Redis 안 썼나" 질문을 미리 막는 배치다.
- 예문: Deliberately per-process and lock-free of any store: with one worker it is exact.
- 유사어: This is intentional (평이), by design (짧음), a conscious trade-off (격식)
- 반의어: an oversight / accidentally

## "rejected, not widened"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-09-ebeam-phase0-flattening.md
- 맥락: 잘못된 입력을 "거절"해야지 "전체로 넓혀" 처리하면 안 된다는 테스트 이름·커밋 메시지
- 한국어: 거절하지, 범위를 넓히지 않는다
- 설명: `A, not B` 대비 구조를 과거분사 둘로 만든 압축형이다. `widen` 은 필터를 풀어 "전체"로 떨어지는 조용한 실패를 뜻하는 동사로, 이 문맥에서 `reject` 의 정확한 반대말이 된다. 테스트 함수 이름에 그대로 들어가는 문장이다.
- 예문: An unknown tool_type is rejected with 400, not widened to "everything".
- 유사어: fail closed, not open (보안 관용구), a hard error rather than a silent fallback (풀어쓴 격식)
- 반의어: silently falls back to all
