# 2026-10-27 — 새 표현

## "the dead-host detector"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 설정값 하나가 시스템에서 맡는 역할에 이름을 붙여 설명할 때(설계 문서·격식)
- 한국어: 죽은 호스트 감지기
- 설명: `connect_timeout` 을 '타임아웃 값'이 아니라 '죽은 장비를 걸러 내는 장치'로 부른다. 숫자 설정을 역할 명사로 바꾸면 왜 그 값이 있는지가 한 번에 전달된다. dead-host 는 하이픈으로 묶은 복합 수식어다.
- 예문: `connect_timeout` (default 8 s) is the dead-host detector: it bounds every blocking socket op, so an offline tool is abandoned in seconds.
- 유사어: liveness check (더 일반적인 기술 용어), a fail-fast timeout (동작 방식에 초점)

## "a host that connects and then stalls"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 연결은 됐는데 그 뒤로 응답이 멈추는 고장 유형을 짚을 때(장애 설명·구어도 가능)
- 한국어: 연결은 되고 나서 멈춰 버리는 호스트
- 설명: stall 은 '진행하다 멈추다'. 엔진이 꺼지는 그림이라 '아예 안 붙는' 고장과 구분된다. and then 이 두 단계(연결 성공 → 정지)의 순서를 보여 줘서 타임아웃이 왜 둘로 나뉘는지 설명이 된다.
- 예문: `host_timeout` is the whole-host backstop for a host that connects and then stalls.
- 유사어: hangs after connecting (구어, 가장 흔함), stops responding mid-session (중립)
- 반의어: fails fast (바로 실패해 금방 드러남)

## "blows past (a limit)"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 한도를 훌쩍 넘겨 버린다고 생생하게 말할 때(구어·기술 글 모두)
- 한국어: (한도를) 훌쩍 넘어서다
- 설명: blow past 는 '쌩 지나쳐 가다'. exceed 보다 넘는 폭이 크고 통제가 안 된다는 느낌이 있다. 원문은 동시 접속 ~200개가 파일 디스크립터 한도와 장비 접속 상한을 함께 넘는 상황.
- 예문: Opening ~200 connections at once blows past `ulimit -n` and the equipment's connection caps.
- 유사어: exceeds (격식, 중립), goes way over (구어), overshoots (목표를 지나침)
- 반의어: stays within (한도 안에 머묾)

## "is not tied to (CPU count)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 흔히 연결 짓는 기준과 이 값은 상관없다고 바로잡을 때(설계 근거·격식)
- 한국어: (CPU 수에) 묶여 있지 않다, 연동되지 않는다
- 설명: be tied to 는 '~에 묶이다/연동되다'. 스레드 수는 CPU 코어 수로 정한다는 통념을 부정하고, 뒤 문장에서 진짜 기준을 댄다. I/O-bound 작업이라 CPU 가 병목이 아니기 때문이다.
- 예문: The threads are I/O-bound, so the cap is not tied to CPU count.
- 유사어: is independent of (격식), doesn't depend on (평이)
- 반의어: scales with / is pegged to (그 값에 맞춰 함께 변함)

## "the real limits are (X), (Y), and (Z)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 잘못 짚은 제약을 걷어 내고 진짜 제약을 나열할 때(설계 문서·리뷰)
- 한국어: 진짜 제약은 X, Y, Z 다
- 설명: 바로 앞의 'not tied to CPU count' 와 짝을 이룬다. 부정(이게 아니다) 뒤에 the real ~ 로 긍정(이게 맞다)을 세우는 흐름. 세미콜론으로 앞 절과 붙여 한 호흡으로 읽힌다.
- 예문: The cap is not tied to CPU count; the real limits are file descriptors, peak RAM, and the servers.
- 유사어: what actually constrains it is (평이), the binding constraints are (격식, 경제·최적화 용어)

## "measured from when (X), not from (Y)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 시간 제한의 기준 시점을 오해 없게 못 박을 때(설정 설명·격식)
- 한국어: X 한 시점부터 잰다, Y 부터가 아니라
- 설명: from 뒤에 when 절이 통째로 와서 '그 일이 일어난 시점'을 가리킨다. not from submit 처럼 대비를 붙여 두면 읽는 사람이 흔히 하는 오해(제출 시점 기준)를 미리 막는다.
- 예문: It is measured from when that host's worker starts, not from submit.
- 유사어: the clock starts when (구어), counted from (중립)

## "Keep it above (X)."
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 설정값이 지켜야 할 하한을 짧은 명령문으로 남길 때(문서·설정 주석)
- 한국어: X 보다 크게 유지하라
- 설명: keep + 목적어 + 전치사구로 '그 상태를 유지하라'. 설명 끝에 붙는 한 줄 규칙이라 주어를 생략한 명령문이 자연스럽다. 원문은 호스트 전체 타임아웃이 '연결 타임아웃 × 파일 수'보다 짧으면 정상 호스트도 잘린다는 경고다.
- 예문: Keep `host_timeout` above `connect_timeout × files-per-host`.
- 유사어: make sure it exceeds (평이), it must not fall below (격식, 규정 문체)
- 반의어: let it drop below (하한 아래로 떨어지게 둠)

## "(tools) go offline routinely"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 장애가 예외가 아니라 일상이라는 운영 현실을 짚을 때(업무 대화·설계 근거)
- 한국어: (장비가) 일상적으로 꺼진다
- 설명: routinely 는 '늘 있는 일로'. 이 한마디가 실패 격리를 기본 설계로 삼은 이유가 된다. go offline 은 상태 변화를 나타내는 go + 형용사 꼴(go missing, go dark 와 같은 계열).
- 예문: Callers gate on `failure_ratio` — tools go offline routinely.
- 유사어: drop off regularly (구어), are frequently unavailable (격식)
- 반의어: stay up / are always reachable (늘 켜져 있음)

## "counts as success"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 어떤 경우를 성공으로 간주한다는 판정 규칙을 밝힐 때(API 문서·구어)
- 한국어: 성공으로 친다
- 설명: count as 는 '~로 간주되다'. 능동형인데 뜻은 수동에 가깝다. 이미 있는 폴더를 실패가 아니라 성공으로 쳐서 mkdir 을 멱등(idempotent)하게 만든다는 규칙.
- 예문: An existing directory counts as success, so the call is safe to repeat.
- 유사어: is treated as success (중립, 문서체), is considered a success (격식)
- 반의어: counts as a failure

## "without looking first"
- 레지스터: conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 미리 확인하는 단계 없이 바로 실행해도 된다고 말할 때(구어·문서)
- 한국어: 먼저 살펴보지 않고
- 설명: look 은 여기서 '존재 여부를 확인하다'. 멱등 설계 덕분에 호출자가 확인 단계를 건너뛸 수 있다는 장점을 평이하게 전한다.
- 예문: Callers run `mkdir` before an upload without looking first.
- 유사어: without checking (평이), blindly (부정적 뉘앙스가 섞임)
- 반의어: look before you leap (실행 전에 확인하라, 속담)

## "is settled by (doing X)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 모호한 결과를 다른 수단으로 판가름한다고 쓸 때(설계 문서·격식)
- 한국어: (X 를 해서) 판가름한다, 결론을 낸다
- 설명: settle 은 논쟁이나 의문을 '매듭짓다'. FTP 가 '이미 있음'과 '권한 없음'에 같은 550 을 돌려줘서, CWD 로 들어가 보는 방법으로 둘을 가른다. 수동태라 '누가'보다 '무엇으로' 결론 나는지에 초점이 간다.
- 예문: A refused MKD is settled by CWD into that path.
- 유사어: is resolved by (중립), is disambiguated by (격식, 정확함)
- 반의어: is left ambiguous (모호한 채로 둠)

## "sits in an unknown (directory)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 시스템이 알 수 없는 상태에 머물러 있다고 묘사할 때(장애 분석·기술 글)
- 한국어: 알 수 없는 (디렉터리에) 머물러 있다
- 설명: sit 은 '그 자리에 가만히 있다'. 움직이지 않고 그 상태가 계속된다는 그림이라 세션 상태를 말할 때 잘 맞는다. sits in an unknown state 로도 쓴다.
- 예문: If that CWD back fails, the session sits in an unknown directory.
- 유사어: is left in an unknown state (중립), is stuck in (구어, 벗어나지 못함)

## "reported failed rather than (created) in the wrong place"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 틀린 성공보다 정직한 실패를 고른 설계를 설명할 때(설계 근거·격식)
- 한국어: 엉뚱한 곳에 만들어지느니 실패로 보고된다
- 설명: report + 목적어 + 형용사(failed) 구조의 수동형이다. rather than 이 두 결과를 저울질해 실패 쪽을 고른 이유를 드러낸다. 데이터를 엉뚱한 위치에 쓰는 것이 실패보다 해롭다는 판단이 깔려 있다.
- 예문: The host's remaining dirs are all reported failed rather than created in the wrong place.
- 유사어: fail safe rather than succeed wrongly (작성, 원칙 표현), better to fail than to guess (구어)

## "Credentials travel with the spec."
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 설정·인증 정보가 요청 데이터에 실려 함께 간다고 설명할 때(기술 문서)
- 한국어: 인증 정보는 spec 에 실려 함께 간다
- 설명: travel with 는 사람이 아닌 데이터에도 쓰는 '~와 함께 이동하다'. 서버 설정이 아니라 요청마다 계정이 따라간다는 구조를 짧게 그린다. 소제목처럼 쓰인 완결문이다.
- 예문: Credentials travel with the spec, so each host can log in with its own account.
- 유사어: are carried in the request (중립, 문서체), ride along with (구어)
- 반의어: live on the server (서버 쪽에 고정됨)

## "roughly triples it"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 크기·비용이 대략 몇 배로 불어나는지 말할 때(구어·기술 글)
- 한국어: 대략 세 배로 불린다
- 설명: triple 은 동사로 '세 배로 만들다'. double·triple·quadruple 이 모두 동사로 쓰인다. 원문은 base64 와 jsonify 가 메모리 사용량을 세 배쯤 불린다는 뜻.
- 예문: The proxy holds a whole batch in memory, and base64 + jsonify roughly triples it.
- 유사어: about 3× (기호, 메모체), inflates it threefold (격식)
- 반의어: roughly halves it (대략 절반으로 줄임)

## "The design exists — do not redesign it."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 이미 정해진 설계를 따르라고 작업 범위를 선 그을 때(작업 지시·리뷰)
- 한국어: 설계는 이미 있다. 다시 설계하지 마라
- 설명: 앞 절에서 사실(exists)을 말하고 대시 뒤 명령으로 결론을 낸다. design 과 redesign 을 바로 붙여 써서 리듬이 짧고 단호하다. 위임할 때 작업자가 범위를 넓히지 않게 막는 문장이다.
- 예문: The design exists — do not redesign it; follow the S6 section of the plans doc.
- 유사어: Build to the existing design (중립), Don't reinvent it (구어)

## "(a stated precondition) no longer holds"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 예전에 걸어 둔 전제 조건이 이제는 성립하지 않는다고 알릴 때(설계·계획 문서)
- 한국어: (명시된 전제가) 더는 성립하지 않는다
- 설명: hold 는 자동사로 '(주장·조건이) 유효하다'. 대시 사이에 근거(어댑터가 사무실에서 돌았다)를 끼우고 so 로 결론(이제 막혀 있지 않다)을 잇는다.
- 예문: One of its stated preconditions no longer holds — the adapter ran at the office on 2026-10-07 — so the feature is unblocked.
- 유사어: no longer applies (평이), is now moot (격식, 의미 없어짐)
- 반의어: still holds / still stands (여전히 유효함)

## "exactly this, nothing more"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 맡긴 범위를 넘지 말라고 강조할 때(작업 지시·구어)
- 한국어: 딱 이것만, 더도 말고
- 설명: 원문은 소제목 'Scope (exactly this, nothing more)'. 긍정(exactly this)과 부정(nothing more)을 나란히 둬서 범위의 위쪽 경계를 못 박는다. 뒤에 Out of scope 목록이 이어진다.
- 예문: Scope: exactly this, nothing more — no backend changes and no new endpoints.
- 유사어: strictly limited to (격식), just this and no extras (구어)
- 반의어: and anything else you think of (범위를 열어 둠)

## "hand-worked literals, not recomputed with the same formula"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 테스트 기댓값을 손으로 계산한 상수로 적으라고 할 때(테스트 작성 지침)
- 한국어: 손으로 계산한 리터럴 값, 같은 공식으로 다시 계산한 값이 아니라
- 설명: hand-worked 는 '손으로 풀어 낸'. 구현과 같은 공식으로 기댓값을 만들면 공식이 틀려도 테스트가 통과하는 함정을 짚는다. 'A, not B' 대비가 지침의 핵심을 한 줄에 담는다.
- 예문: Expected values must be hand-worked literals, not recomputed with the same formula.
- 유사어: hard-coded expected values worked out by hand (평이), independently derived expectations (격식)
- 반의어: expectations computed by the code under test (검사 대상이 계산한 기댓값)

## "leave the branch for review"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 작업을 머지하지 말고 검토용으로 남겨 두라고 할 때(위임·협업)
- 한국어: 브랜치를 리뷰용으로 남겨 두다
- 설명: leave + 목적어 + for 목적. 금지 목록(merge·push·remove 하지 마라) 뒤에 대시로 '대신 이렇게 하라'를 덧붙인 꼴이다. 위임한 작업의 마지막 상태를 정해 준다.
- 예문: Do not merge, push, or remove the worktree — leave the branch for review.
- 유사어: hand it over for review (중립), park it for review (구어)
- 반의어: merge it straight in (바로 합침)

## "wins over (X) instead of falling back to it"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (admin_logs 코드 리뷰 결과)
- 맥락: 우선순위 로직에서 엉뚱한 값이 이겨 버리는 버그를 설명할 때(코드 리뷰)
- 한국어: (X 로) 넘어가는 대신 X 를 이겨 버린다
- 설명: win over 는 '~보다 우선하다'. `a or b` 처럼 앞 값이 참이면 뒤 값이 무시되는 코드에서, 쓸모없는 문자열 ": " 가 참으로 판정돼 기본 문구를 밀어내는 상황이다. instead of falling back to it 이 원래 의도를 대비시킨다.
- 예문: An `error` dict without code or message yields the truthy string ": ", which wins over the reason phrase instead of falling back to it.
- 유사어: takes precedence over (격식), beats (구어)
- 반의어: falls back to (기본값으로 넘어감)

## "the suite stays green"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (admin_logs 코드 리뷰 결과)
- 맥락: 회귀가 생겨도 테스트가 못 잡는다는 공백을 짚을 때(코드 리뷰·구어)
- 한국어: 테스트가 계속 통과한다
- 설명: green 은 CI 통과 색. stays 가 '바뀌었는데도 그대로'라는 뉘앙스를 줘서, 칭찬이 아니라 테스트 공백에 대한 경고가 된다.
- 예문: Someone later drops the fallback, and the suite stays green because no route returns that shape.
- 유사어: CI still passes (평이), the tests don't notice (구어)
- 반의어: the suite goes red (테스트가 깨짐)

## "pins what (the docs) now document"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (admin_logs 코드 리뷰 결과)
- 맥락: 문서에 적은 동작을 테스트로 고정하자고 할 때(코드 리뷰)
- 한국어: (문서가) 이제 적어 둔 내용을 (테스트로) 고정한다
- 설명: pin 은 '핀으로 꽂아 고정하다'. 테스트가 동작을 움직이지 못하게 붙잡는다는 그림이다. what 절이 목적어 자리에 와서 '문서에 적힌 것'을 통째로 받는다.
- 예문: One test per branch pins what the logging doc now documents.
- 유사어: locks in (구어), codifies (격식)

## "is reported identically to (a missing one)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (admin_logs 코드 리뷰 결과)
- 맥락: 서로 다른 두 경우가 같은 메시지로 뭉개져 구분이 안 된다고 지적할 때(리뷰·장애 분석)
- 한국어: (없는 경우와) 똑같이 보고된다
- 설명: identically to 는 '~와 똑같이'. 짧게 잘린 값과 아예 없는 값이 같은 오류 문구로 나와서, 운영자가 원인을 가를 수 없다는 지적이다. 부사 하나로 '정보가 사라졌다'는 문제를 말한다.
- 예문: A one-sided own-fab entry is now reported identically to a missing one.
- 유사어: looks the same as (평이), is indistinguishable from (격식)
- 반의어: is reported distinctly (따로 구분돼 보고됨)

## "in one sitting"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (코드 리뷰 에이전트 지침)
- 맥락: 한자리에서 한 번에 끝낸다고 말할 때(일상·업무 구어)
- 한국어: 한자리에서, 한 번에 앉은 김에
- 설명: sitting 은 명사로 '한 번 앉아 있는 동안'. 책을 한 번에 다 읽을 때도 read it in one sitting 이라고 한다. 원문은 꼼꼼한 리뷰어가 한 번 앉아서 잡을 버그를 다 잡으라는 지침.
- 예문: Catch every real bug a careful reviewer would catch in one sitting.
- 유사어: in one go (구어, 가장 흔함), at a stretch (약간 문어)
- 반의어: over several sessions (여러 번에 나눠서)

## "be judged against a reference that does not move"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시)
- 맥락: 판단 기준을 고정해야 비교가 의미 있다고 설명할 때(분석·설계 문서)
- 한국어: 움직이지 않는 기준에 비추어 판단되다
- 설명: judge against 는 '~에 비추어 평가하다'. 관계절 that does not move 가 기준이 고정됐다는 조건을 붙인다. 앞에서 지적한 문제(기준이 선택과 함께 움직인다)를 정반대로 뒤집는 표현이다.
- 예문: Pin earlier measurements as a fixed baseline, so later measurements are judged against a reference that does not move.
- 유사어: be compared with a fixed baseline (평이), be evaluated against a stable reference (격식)
- 반의어: a reference that moves with the selection (선택에 따라 흔들리는 기준)
