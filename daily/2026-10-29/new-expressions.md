# 2026-10-29 — 새 표현

## "Why (X) is shaped the way it is"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 설계 근거 문서의 첫 줄에서 이 글이 무엇을 다루는지 밝힐 때(문어·격식)
- 한국어: X 가 왜 지금 같은 모양이 되었는가
- 설명: 사용법(how to call)이 아니라 이유(why)를 다루는 문서라는 걸 한 줄로 알린다. the way it is 가 '지금의 그 모습'을 가리켜서 구조·인터페이스·기본값을 한꺼번에 묶는다. 원문은 주어가 둘이라 the way they are 로 썼다.
- 예문: Why `direct_downloader.FtpFleetDownloader` and its proxy twin are shaped the way they are.
- 유사어: the rationale behind (X) (격식, 명사형), why we built (X) this way (구어·주어 we 가 드러남)

## "(an offline tool) is abandoned in seconds"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 응답 없는 대상을 빨리 포기하는 타임아웃 설계를 설명할 때(기술 문서)
- 한국어: (꺼진 장비는) 몇 초 만에 포기된다
- 설명: abandon 은 '하던 일을 중간에 버리다'라서 timeout 보다 결과가 선명하다. in seconds 는 '몇 초 안에', 즉 아주 빨리. 수동태라서 누가 포기하는지보다 장비가 어떻게 되는지에 초점이 간다.
- 예문: `connect_timeout` bounds every blocking socket op, so an offline tool is abandoned in seconds.
- 유사어: is given up on quickly (구어, 구동사), times out fast (기술 구어, 짧음)
- 반의어: hangs indefinitely (무한정 매달려 있다)

## "(the sets) agree today only because (three different inputs) happen to coincide"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — altitude 리뷰 보고)
- 맥락: 지금 결과가 맞는 건 설계 덕이 아니라 우연이라고 경고할 때(리뷰·격식)
- 한국어: (세 집합이) 지금 일치하는 건 서로 다른 입력 셋이 우연히 겹쳤기 때문일 뿐이다
- 설명: today 와 only because 가 '지금은 맞지만 보장은 없다'를 만든다. happen to + 동사원형은 '우연히 ~하다'. 'by construction(구조상 반드시)'의 정반대 말이라 리팩터링 제안의 근거로 자주 쓴다.
- 예문: The sets agree today only because three different inputs happen to coincide.
- 유사어: line up by accident (구어), agree by coincidence rather than by design (격식, 대비 명시)
- 반의어: coincide by construction (구조상 반드시 일치한다)

## "a deliberate-scope call"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — simplification 리뷰 보고)
- 맥락: 기계적으로 고칠 일이 아니라 범위를 사람이 정해야 하는 결정이라고 넘길 때(리뷰 보고)
- 한국어: 범위를 의도적으로 정해야 하는 판단
- 설명: call 은 '판정·결정'(judgment call 의 그 call)이다. deliberate-scope 를 하이픈으로 묶어 형용사로 썼다. 이 수정은 테스트 두 개가 고정해 둔 동작을 바꾸니 의도하고 하라는 뜻이다.
- 예문: Two tests in `scaleLabel.test.ts` pin those cases, so it is a deliberate-scope call.
- 유사어: a judgment call (가장 흔함), a decision for the owner (격식, 결정권자 강조)

## "hand-threaded through four layers"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — altitude 리뷰 보고)
- 맥락: 값 하나를 여러 계층에 손으로 일일이 전달하는 배관 코드를 지적할 때(코드 리뷰)
- 한국어: 네 계층에 걸쳐 손으로 꿰어 전달된
- 설명: thread (a value) through 는 실을 꿰듯 값을 계층마다 넘긴다는 뜻이다. 앞에 hand- 를 붙여 자동화 없이 수작업이라는 비용을 강조한다. 이어서 '파라미터 하나 추가에 9군데를 손대야 한다'는 숫자로 근거를 댄다.
- 예문: A new URL param is hand-threaded through four layers.
- 유사어: plumbed by hand through (구어·기술), manually propagated across (격식)
- 반의어: derived from one table (테이블 하나에서 파생된)

## "high on (the duplication), low on (value)"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — reuse 리뷰 보고)
- 맥락: 사실 판단은 확실하지만 고칠 가치는 낮다고 확신도를 두 축으로 나눌 때(리뷰·구어 겸용)
- 한국어: (중복이라는 점은) 확실하지만 (고칠 가치는) 낮다
- 설명: Confidence 를 하나로 뭉뚱그리지 않고 '사실'과 '가치'로 쪼갰다. high on X, low on Y 의 on 은 '~ 면에서'. 리뷰어가 과장하지 않는다는 신호라 듣는 쪽이 판단하기 쉽다.
- 예문: Confidence: high on the duplication, low on value.
- 유사어: certain it's there, unsure it matters (구어, 풀어 쓴 형태), real but minor (짧은 판정)

## "treat it as a question rather than a mechanical cleanup"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — altitude 리뷰 보고)
- 맥락: 정리처럼 보이지만 사실은 의도 확인이 먼저인 항목을 넘길 때(리뷰·격식)
- 한국어: 기계적인 정리가 아니라 질문으로 다뤄라
- 설명: 두 화면의 규칙이 다른데 어느 쪽이 의도인지 모르면 하나로 합치는 것 자체가 결정이 된다. treat A as B rather than C 틀로 '어떻게 분류해서 다룰지'를 지시한다.
- 예문: It needs a decision on which is intended, so treat it as a question rather than a mechanical cleanup.
- 유사어: raise it rather than fix it (구어, 행동 대비), flag it for a decision (기술 구어)

## "Each comment documents its own rule; neither mentions the other."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — altitude 리뷰 보고)
- 맥락: 두 곳이 각자 옳게 문서화돼 있지만 서로를 모른다는 점을 짚을 때(리뷰·문어)
- 한국어: 주석마다 자기 규칙을 적어 두었고, 어느 쪽도 다른 쪽을 언급하지 않는다
- 설명: 세미콜론 앞은 각자의 사정, 뒤는 둘 사이의 공백이다. each … its own 과 neither … the other 가 짝을 이뤄 '따로따로'를 문법으로 보여 준다. 누구 잘못도 아니라는 중립적인 어조가 있다.
- 예문: Each comment documents its own rule; neither mentions the other.
- 유사어: they are documented in isolation (격식, 짧음), neither knows about the other (구어)

## "(X) that (msrRows.ts) says lives in one place"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — reuse 리뷰 보고)
- 맥락: 코드가 스스로 선언한 규칙을 근거로 중복을 지적할 때(리뷰, 문법 포인트)
- 한국어: msrRows.ts 가 한 곳에만 있다고 밝힌 (규칙)
- 설명: the rule that msrRows.ts says (it) lives in one place 에서 관계대명사 that 이 says 뒤 절의 주어 자리를 대신한다. 그래서 says 뒤에 바로 lives 가 온다. 리뷰어 의견이 아니라 파일 자신의 약속을 들이대니 반박하기 어렵다.
- 예문: It is a second copy of the "measured values of a parameter" rule that `msrRows.ts` says lives in one place.
- 유사어: the rule (X) claims to own (구어, 짧음), the single source of truth declared in (X) (격식)

## "only worth it if (X) moves somewhere neutral"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt d2f430dc (simplify — reuse 리뷰 보고)
- 맥락: 제안에 조건을 걸어 가치를 낮춰 말할 때(리뷰·구어 겸용)
- 한국어: X 가 중립적인 곳으로 옮겨질 때만 할 가치가 있다
- 설명: AFM 모듈의 함수를 skewvoir 가 import 하면 도메인 경계가 섞인다는 뜻이다. only worth it if 가 '그 조건이 없으면 하지 마라'를 부드럽게 말한다. somewhere neutral 은 특정 도메인에 속하지 않는 공용 위치.
- 예문: It is a cross-domain import from an AFM module; only worth it if `summaryNumber` moves somewhere neutral.
- 유사어: not worth it unless (같은 뜻, 부정형), worth doing once (X) lives in a shared module (구체형)

## "The output feeds the decision (X)."
- 레지스터: professional
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 조사·분석을 맡기면서 결과물이 어떤 결정에 쓰이는지 밝힐 때(업무 지시·격식)
- 한국어: 이 결과물은 (X 라는) 결정의 입력이 된다
- 설명: feed 는 '먹이다'에서 '입력으로 넣다'로 넓어진 동사다. 목적을 먼저 알리면 받는 사람이 무엇을 깊게 파고 무엇을 건너뛸지 스스로 정한다. 원문은 결정을 따옴표로 그대로 박았다.
- 예문: The output feeds the decision "what do we teach in Builder and in Guide".
- 유사어: This will inform (X) (격식, 가장 흔함), We'll use this to decide (X) (구어)

## "how much of it survives when you strip out (X)"
- 레지스터: professional
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 특정 조건을 걷어 낸 뒤에도 쓸모가 남는지 평가 기준을 줄 때(분석 지시)
- 한국어: X 를 걷어 내면 그중 얼마나 살아남는가
- 설명: strip out 은 '벗겨 내다·빼 버리다'. survive 를 쓰니 '남는 가치'가 생존 문제처럼 또렷해진다. 콜론 뒤에서 무엇이 넘어가고 무엇이 안 넘어가는지 바로 예를 든다.
- 예문: For each source, judge how much of it survives when you strip out the vendor's own product.
- 유사어: what's left once you remove (X) (구어), how much remains usable without (X) (격식)

## "Follow each claim to the page that owns it."
- 레지스터: professional
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 2차 요약 말고 원출처까지 거슬러 확인하라고 할 때(리서치 지시·격식)
- 한국어: 주장마다 그것을 책임지는 원래 페이지까지 따라가라
- 설명: own 을 '소유하다'에서 '책임지고 관리하다'로 썼다. 블로그 요약은 그 주장을 '빌려 온' 것이고, 주인은 공식 강의 페이지·라이선스 파일이다. 코드 리뷰의 'X owns this rule' 과 같은 쓰임이다.
- 예문: Not blog summaries or listicles. Follow each claim to the page that owns it.
- 유사어: trace every claim back to its primary source (격식, 표준 표현), check where it actually comes from (구어)

## "Mark your own judgments clearly as judgment, separate from what the source states."
- 레지스터: professional
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 보고서에서 사실과 의견을 섞지 말라고 할 때(리서치·감사 문서)
- 한국어: 자기 판단은 판단이라고 분명히 표시하고, 출처가 말한 것과 분리하라
- 설명: mark A as B 는 'A 에 B 라는 꼬리표를 붙이다'. separate from 은 앞 구 전체를 꾸미는 형용사구다. judgments 와 judgment 를 일부러 반복해 '판단은 판단일 뿐'이라는 리듬을 만든다.
- 예문: Mark your own judgments clearly as judgment, separate from what the source states.
- 유사어: label opinions as opinions (구어, 짧음), distinguish findings from interpretation (격식, 학술)

## "If a number is not stated, write (X) — do not estimate."
- 레지스터: professional
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 빈칸을 추정치로 메우지 말라고 못 박을 때(지시·격식)
- 한국어: 숫자가 명시돼 있지 않으면 X 라고 적어라. 추정하지 마라
- 설명: 해야 할 일(write X)과 하지 말 일(do not estimate)을 대시로 붙였다. 빈칸에 무엇을 쓸지까지 정해 주니 '모르면 그럴듯하게 채우는' 실수가 막힌다. 원문 X 자리에는 "명시 없음"이 들어갔다.
- 예문: If a number is not stated on the source page, write "not stated" — do not estimate.
- 유사어: leave it blank rather than guess (구어), report it as unavailable (격식)

## "where the evidence was thin"
- 레지스터: professional, conversational
- 출처: transcript:pm-notes subagent a730d3ef (리서치 지시문)
- 맥락: 근거가 약했던 부분을 따로 보고하라고 할 때(리서치·회의)
- 한국어: 근거가 빈약했던 곳
- 설명: thin 은 '얇다'에서 '빈약하다'로 쓰인다. weak evidence 보다 '양이 모자라다'는 느낌이 강하다. 보고 마지막에 이 항목을 두면 독자가 어디를 의심할지 안다.
- 예문: Report anything where the evidence was thin.
- 유사어: where support was weak (중립), where you're least sure (구어, 확신도로 바꿈)
- 반의어: well-supported (근거가 탄탄한)

## "label it so it cannot be read as the same quantity"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt subagent a676af14 (결함 수정 지시문)
- 맥락: 다른 값을 같은 이름으로 오해하지 않게 화면 표기를 바꾸라고 할 때(UI·기술 지시)
- 한국어: 같은 양으로 읽히지 않도록 이름을 붙여라
- 설명: so (that) it cannot be read as 가 목적을 나타낸다. read as 는 '~로 읽히다'. 값을 없애라는 게 아니라 오독을 막으라는 요구라서 수정 폭이 작아진다.
- 예문: Where a backend summary value must still be shown, label it so it cannot be read as the same quantity.
- 유사어: label it unambiguously (격식, 짧음), make it obvious it's a different number (구어)

## "If you find yourself wanting one, stop and report."
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt subagent a676af14 (결함 수정 지시문)
- 맥락: 금지 범위를 넘고 싶어지면 멈추고 알리라고 할 때(위임·지시)
- 한국어: 그게 필요해진다 싶으면 멈추고 보고해라
- 설명: find yourself -ing 는 '어느새 ~하고 있다'. 금지 규칙을 어길 상황을 미리 예상하고 대응까지 정해 둔다. stop and report 는 두 동사만으로 행동을 끝낸다.
- 예문: No backend, contract or provider change. If you find yourself wanting one, stop and report.
- 유사어: check with me first (구어), escalate before proceeding (격식)

## "Write as little as possible"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt subagent a676af14 (결함 수정 지시문)
- 맥락: 최소 변경 원칙을 짧게 지시할 때(코드 작업 지시)
- 한국어: 가능한 한 적게 써라
- 설명: as little as possible 은 양을 최소로. 뒤에 콜론으로 방법을 붙였다(reuse existing helpers; no speculative options). 원칙 한 줄과 실천 두 개라 지키기 쉽다.
- 예문: Write as little as possible: reuse existing helpers; no speculative options.
- 유사어: keep the diff minimal (기술 구어), make the smallest change that works (중립)
- 반의어: build it out generously (넉넉하게 만들다)

## "every ambiguity and how you resolve(d) it"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent a676af14 (결함 수정 지시문)
- 맥락: 보고서에 애매했던 지점과 거기서 고른 해석을 함께 적으라고 할 때(위임 보고 요구)
- 한국어: 애매했던 모든 점과 그것을 어떻게 정리했는지
- 설명: 무엇이 애매했는지만이 아니라 '어떻게 결정했는지'까지 묻는다. 그래야 검토자가 그 선택만 골라 다시 볼 수 있다. 원문은 문장 끝이 잘려 resolve 로 끝난다.
- 예문: Report every ambiguity and how you resolved it.
- 유사어: any judgment calls you made (구어), assumptions and their rationale (격식)

## "(exactly the one file) the brief named"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d2f430dc ([assistant] 승인 메모)
- 맥락: 요청이 지시서 범위 안에 있는지 확인하고 승인할 때(구어·짧은 메모)
- 한국어: 지시서(brief)에 적힌 바로 그 파일 하나
- 설명: brief 는 명사로 '작업 지시서'. the brief named 는 that 이 생략된 관계절로 file 을 꾸민다. exactly 가 '범위를 벗어나지 않았다'를 확인해 준다.
- 예문: The approval is exactly the one file the brief named; approving.
- 유사어: within the scope of the brief (격식), what we agreed on (구어)
- 반의어: out of scope (범위 밖)

## "(the file check) just raced the write"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt d2f430dc ([assistant] 메모)
- 맥락: 실패처럼 보였던 것이 타이밍 경합이었다고 설명할 때(기술 구어)
- 한국어: (파일 확인이) 쓰기와 경합했을 뿐이다
- 설명: race 를 타동사로 써서 'A 가 B 와 경주했다', 즉 순서가 꼬였다는 뜻이다. just 가 '진짜 문제는 아니다'를 붙인다. 앞 문장 It was written 이 결과를 먼저 말해서 안심시킨다.
- 예문: It was written; the file check just raced the write.
- 유사어: ran before the write finished (풀어 쓴 형태), was a timing fluke (구어)
