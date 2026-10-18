# 2026-10-19 — 새 표현

오늘 배치는 문서 30건과 대화 5건이다. 문서는 전부 `bulk_recipe_copy` 저장소에서 왔다. 티켓·스펙·핸드오프는 한국어라 표현 원료가 못 되고, 영어는 `ftp_handler/docs/adr/` 아래 네 편(핸드오프, 용어집 `CONTEXT.md`, `ftp_fleet_downloader.md`, ADR 0001)에 몰려 있다. 결정의 이유를 한 줄씩 붙이는 설계 문서라 `X, not Y` 대비와 조건절이 많다. `blow past`, `black-holed`, `backstop`, `drop-in`, `load-bearing`, `clobber`, `co-resident`, `at the … cliff`, `if X changes materially` 는 이미 노트에 있어 건너뛰었다. 대화 5건 중 4건은 `/clear` 뿐이고, 나머지 하나는 연말 성과 보고서 작성이라 `coaching.md` 로 갔다.

## "a fresh agent picking up the … work"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/handoff_ftp_fleet_downloader.md
- 맥락: 인수인계 문서 첫 줄에서 "이 글은 누가 읽으라고 쓴 것인지"를 밝힐 때(문서·격식)
- 한국어: 이 일을 이어받는 새 에이전트(사람)
- 설명: `pick up` 은 남이 내려놓은 일을 중간부터 집어 드는 그림이다. `take over` 가 책임 이전을 강조한다면 `pick up` 은 "멈춘 지점에서 이어 간다"에 가깝다. `fresh` 는 "앞 맥락을 모르는"이라는 뜻이라 문서가 배경부터 설명할 이유가 된다.
- 예문: This note is context for a fresh agent picking up the equipment-FTP collection work.
- 유사어: take over (책임까지 넘겨받음, 더 공식적), carry on with (같은 사람이 계속할 때도 씀), inherit (원치 않게 떠안은 느낌이 섞임)
- 반의어: hand off (넘겨주는 쪽)

## "Fix direction chosen: …"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/handoff_ftp_fleet_downloader.md
- 맥락: 원인 분석 뒤에 "그래서 어떤 방향으로 고치기로 했나"를 머리말 하나로 붙일 때(보고서·이슈·격식)
- 한국어: 선택한 수정 방향: …
- 설명: `the fix direction that was chosen` 을 줄여 콜론 머리말로 만들었다. 바로 앞의 `Root cause:` 와 짝을 이뤄 "원인 → 방향" 두 줄로 결론을 낸다. `direction` 이라는 단어가 "세부 구현은 아직 열려 있다"는 여지를 남긴다.
- 예문: Root cause: unbounded concurrency. Fix direction chosen: a bounded thread pool with per-host isolation.
- 유사어: Chosen approach: (가장 무난), Resolution: (이미 끝난 수정에 더 맞음), We went with … (구어)

## "fans out hundreds of hosts concurrently with zero extra packages"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 동시 실행 구조의 장점을 말하며 의존성이 늘지 않았다는 점까지 한 문장에 담을 때(설계 문서)
- 한국어: 추가 패키지 하나 없이 수백 대 호스트로 동시에 퍼져 나간다
- 설명: `fan out` 은 부채꼴로 펼쳐지듯 한 작업을 여러 갈래로 나눠 동시에 보낸다는 뜻이고 여기서는 타동사로 썼다. `zero extra packages` 는 `no` 대신 숫자 `zero` 를 써서 "정말 하나도"를 강조한다.
- 예문: A bounded thread pool fans out hundreds of hosts concurrently with zero extra packages.
- 유사어: spread across (평이), parallelize over (더 기술적·딱딱함), scatter (scatter-gather 패턴 문맥)
- 반의어: fan in (결과를 한 곳으로 모으다), run serially

## "failures are collected, not raised"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 일부 실패가 전체를 멈추지 않도록 설계했다는 점을 짧게 못 박을 때(설계·리뷰)
- 한국어: 실패는 예외로 던지지 않고 모아 둔다
- 설명: 수동태 두 개를 `X, not Y` 로 맞세웠다. `raise` 는 파이썬에서 예외를 던진다는 뜻이라 개발자 독자에겐 동사 하나로 동작이 전달된다. 앞 문장의 "죽은 호스트 하나가 나머지를 멈추지 못한다"를 구현 차원에서 받쳐 주는 꼬리 문장이다.
- 예문: One bad host can't abort the run, because failures are collected, not raised.
- 유사어: errors are recorded rather than thrown (같은 뜻, 더 풀어 씀), fail soft (짧은 관용구)
- 반의어: fail fast, fail-on-any (첫 실패에 전체를 멈춤)

## "not inherently riskier than"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 막연한 불안을 짚으며 "그 자체로는 더 위험하지 않다"고 선을 그을 때(설계 논의·격식)
- 한국어: 본질적으로 ~보다 더 위험한 것은 아니다
- 설명: `inherently` 는 "그 성질 자체 때문에"라는 뜻이다. 부정과 붙으면 "조건에 따라 위험할 수는 있지만 원래 그런 건 아니다"가 되어 반론을 열어 둔 채 오해만 걷어 낸다. 바로 뒤에 진짜 위험 요인(`shared mutable state`)을 대야 주장이 선다.
- 예문: In-memory buffering is not inherently riskier than writing to disk; shared state is what causes the mixing.
- 유사어: no riskier in itself than (평이), not intrinsically more dangerous than (더 학술적)
- 반의어: inherently unsafe

## "The fear that X comes from Y, not from Z."
- 레지스터: professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 상대의 걱정을 인정하면서 그 걱정의 진짜 출처를 옮겨 줄 때(설계 설명·회의)
- 한국어: X 라는 걱정은 Z 가 아니라 Y 에서 나온다
- 설명: 걱정 내용을 `that` 절로 통째로 주어에 넣고 `comes from` 으로 원인을 지목한다. 걱정을 무시하지 않고 "맞는 걱정인데 범인을 잘못 짚었다"고 말하는 정중한 반박 틀이다. 원문은 `Y` 와 `Z` 를 기울임으로 강조했다.
- 예문: The fear that async mixes one host's data into another's comes from shared mutable state, not from memory itself.
- 유사어: What actually drives that concern is … (더 부드러움), That worry is really about … (구어)

## "Cross-host contamination"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 동시 처리에서 한 단위의 데이터가 다른 단위로 새어 들어가는 버그를 이름 붙일 때(설계·버그 보고)
- 한국어: 호스트 간 데이터 오염(섞임)
- 설명: `contamination` 은 원래 화학·위생 용어인데 데이터가 섞이는 현상에도 쓴다. `cross-` 접두사가 "단위 경계를 넘어서"를 더한다. `mixing` 보다 "결과를 못 믿게 됐다"는 심각성이 강하다.
- 예문: Cross-host contamination happens only if concurrent units share a destination or a stateful resource.
- 유사어: data bleed (구어, 새어 나옴), cross-talk (신호·채널 간 간섭), mixing (가장 평이)
- 반의어: isolation

## "When X genuinely wins: …"
- 레지스터: professional, conversational
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 한쪽 손을 들어 준 뒤 반대쪽이 실제로 나은 경우를 공정하게 덧붙일 때(비교 글·토론)
- 한국어: X 가 정말로 이기는 경우: …
- 설명: `genuinely` 가 "말뿐인 양보가 아니라 진짜로"를 표시한다. 바로 뒤에 `memory pressure, not correctness` 처럼 이기는 조건을 좁혀 댄다. 비교 글에서 한쪽만 편든다는 인상을 지우는 소제목 틀이다.
- 예문: When disk genuinely wins: memory pressure, not correctness.
- 유사어: Where X does come out ahead: (강조형 do), The case for X: (중립·격식), X makes sense when … (평이)

## "handed to you the moment it downloads, then dropped"
- 레지스터: technical, conversational
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 스트리밍 처리의 생명주기를 "받자마자 넘기고 버린다"로 짧게 설명할 때(문서·구어)
- 한국어: 내려받는 순간 넘겨지고 곧바로 버려진다
- 설명: `the moment (that) S V` 는 접속사처럼 쓰여 `as soon as` 와 같은 뜻이다. 명사구가 시간 접속사로 굳은 경우라 문법상 낯설어도 아주 흔하다. `then dropped` 는 `and is then dropped` 를 줄인 꼴로 메모리를 붙잡지 않는다는 점을 덧붙인다.
- 예문: Each file is handed to your callback the moment it downloads, then dropped.
- 유사어: as soon as it lands (구어), immediately upon download (격식), on arrival (짧은 명사구)

## "lowest common denominator"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/CONTEXT.md
- 맥락: 기능은 가장 적지만 어디서나 통하는 최후의 공통 선택지를 가리킬 때(기술 비교·격식)
- 한국어: 최소 공통분모, 어디서나 되지만 기능은 제일 빈약한 것
- 설명: 수학의 "최소공배수(분모)"에서 온 말로, 모두가 지원하는 최소한이라는 뜻이다. 문화 비평에서는 "수준을 가장 낮은 쪽에 맞춘"이라는 깎아내림이 섞이는데, 기술 문서에서는 대개 중립적으로 "호환성은 최고, 표현력은 최저"를 뜻한다.
- 예문: NLST is the lowest common denominator: every server supports it, but it returns names only.
- 유사어: the bare minimum (평이), the universal fallback (기술 문맥에서 긍정적), least common denominator (미국식 변형)
- 반의어: the richest option, best-in-class

## "in decreasing fidelity / increasing compatibility"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/CONTEXT.md
- 맥락: 선택지를 나열하며 한 축이 줄면 다른 축이 는다는 트레이드오프를 순서로 보여 줄 때(설계 문서)
- 한국어: 정확도는 떨어지고 호환성은 올라가는 순서로
- 설명: `in decreasing/increasing order of X` 를 줄여 두 축을 슬래시로 묶었다. 목록 앞에 이 한 줄을 두면 독자가 순서 자체에서 트레이드오프를 읽는다. `fidelity` 는 "원본을 얼마나 충실하게 담는가"로, 여기서는 타입·시각 정보를 얼마나 주는가다.
- 예문: There are three ways to list a directory, in decreasing fidelity and increasing compatibility.
- 유사어: from richest to most portable (평이), ordered by X, descending (표 머리말 투)

## "rolling back if it lands in the future"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/CONTEXT.md
- 맥락: 날짜 추론 규칙에서 계산 결과가 미래로 나오면 한 단계 되돌린다는 보정을 설명할 때(기술 문서)
- 한국어: (추론한 날짜가) 미래로 떨어지면 한 해 되돌린다
- 설명: `land` 는 계산 결과가 어느 값에 "떨어진다"는 뜻으로 날짜·숫자에 자주 쓴다. 분사구문 `rolling back …` 이 앞 절 `infers the year` 의 보정 동작을 덧붙인다. 연도 없는 `ls -l` 출력에서 올해로 가정했다가 미래가 되면 작년으로 돌리는 규칙이다.
- 예문: The year-less form assumes the current year, rolling back one year if the date lands in the future.
- 유사어: falls in the future (평이), ends up in the future (구어)

## "borrows from that same budget — it does not get a fresh one"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 새 기능이 기존 자원 한도를 나눠 쓴다는 점을 오해 없이 강조할 때(ADR·리뷰)
- 한국어: 같은 예산에서 빌려 쓰며, 새 예산을 따로 받지 않는다
- 설명: 긍정문 뒤에 대시로 같은 내용을 부정문으로 한 번 더 말한다. 중복처럼 보이지만 "따로 받는 줄 알았다"는 흔한 오해를 미리 막는 장치다. `budget` 을 돈이 아니라 메모리·시간 한도에 쓰는 것도 기술 영어의 흔한 비유다.
- 예문: The proxy borrows from the uWSGI worker's memory budget; it does not get a fresh one.
- 유사어: shares the same allowance (평이), eats into the existing headroom (구어, 잠식 뉘앙스)
- 반의어: gets its own (dedicated) budget

## "size the defaults against the shared envelope"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 설정값을 정하는 기준이 "공유 자원의 운영 한계"임을 밝힐 때(ADR·용량 계획)
- 한국어: 공유 자원의 운영 한계에 맞춰 기본값 크기를 정하다
- 설명: `envelope` 는 원래 항공의 `flight envelope`(안전하게 날 수 있는 범위)에서 온 말로, 시스템이 안전하게 버티는 한계 범위를 뜻한다. `size A against B` 는 "B 를 기준으로 A 의 크기를 맞추다"다. 원문은 앞에서 `That app's envelope` 라고 프로세스 수·메모리 한도를 묶어 불렀다.
- 예문: We sized the batch defaults against the shared 8 GiB envelope rather than the proxy alone.
- 유사어: operating limits (평이), headroom (남은 여유 쪽에 초점), within the budget (일반적)

## "returns partial results instead of being killed"
- 레지스터: technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 타임아웃 순서를 조정한 이유를 "통째로 죽느니 일부라도 돌려준다"로 설명할 때(설계·리뷰)
- 한국어: 강제 종료되는 대신 일부 결과라도 돌려준다
- 설명: `instead of being killed` 는 동명사 수동태다. 주어(배치)가 스스로 죽는 게 아니라 uWSGI 에게 죽임을 당한다는 점을 수동으로 보여 준다. 시간 한도를 바깥 한도보다 짧게 잡아야 하는 이유를 결과 하나로 요약한다.
- 예문: With host_timeout under harakiri, the batch returns partial results instead of being killed.
- 유사어: degrades to a partial response (기술적), comes back with whatever it has (구어)
- 반의어: fails wholesale, all-or-nothing

## "a caller who hasn't done this math"
- 레지스터: professional, conversational
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 안전한 기본값을 왜 코드에 박았는지, 계산을 모르는 사용자를 위해서라고 말할 때(설계·구어)
- 한국어: 이 계산을 해 보지 않은 호출자
- 설명: `do the math` 는 "계산해 보다, 따져 보다"라는 구어 관용구다. 관계절로 독자를 가정해 "그런 사람도 안전해야 한다"는 기본값 설계 원칙을 사람 중심으로 말한다. 영국식은 `do the maths`.
- 예문: The defaults exist to give a caller who hasn't done this math a safe result on the shared host.
- 유사어: someone who hasn't worked through the numbers (평이), an uninformed caller (딱딱하고 약간 낮잡음)

## "the rewrite this ADR deliberately defers"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 지금 안 하는 큰 작업을 "잊은 게 아니라 일부러 미룬 것"으로 기록할 때(ADR·결정 기록)
- 한국어: 이 ADR 이 의도적으로 미루는 재작성
- 설명: `deliberately` 가 핵심이다. 빠진 것을 누락이 아닌 결정으로 바꿔 놓는다. 주어를 사람이 아닌 문서(`this ADR`)로 둬서 결정의 주체를 문서에 맡기는 격식체다. 앞에 미룬 조건(`If the file profile changes …`)을 먼저 대고 이 문장으로 닫는다.
- 예문: A streaming transport is the rewrite this ADR deliberately defers.
- 유사어: is explicitly out of scope for now (더 흔한 문서 표현), we're punting on (구어), is parked (구어, 보류)
- 반의어: is addressed here, is in scope

## "Do not 'optimize' X back up without re-checking …"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 일부러 보수적으로 둔 값을 누군가 "성능 개선"이라며 되돌리지 않도록 경고할 때(ADR·코드 주석)
- 한국어: 위 계산을 다시 확인하지 않고 X 를 도로 올리는 "최적화"를 하지 마라
- 설명: `optimize` 를 따옴표에 넣어 "그건 최적화처럼 보이지만 아니다"라는 비꼼을 담았다. `back up` 은 원래 값으로 "도로 올린다"는 방향이다. `without re-checking` 이 금지 조건을 걸어 영구 금지가 아니라 재검토 의무로 만든다.
- 예문: Do not "optimize" request_batch back up without re-checking the memory math above.
- 유사어: Don't bump X without … (구어), Any increase to X must be re-validated against … (격식)

## "deprioritized … during design"
- 레지스터: professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/handoff_ftp_fleet_downloader.md
- 맥락: 어떤 항목을 일부러 뒤로 미뤘다는 사실을 남 탓 없이 기록할 때(인수인계·회의록)
- 한국어: 설계 중에 우선순위를 낮췄다
- 설명: `de-` + `prioritize` 로 "우선순위에서 내리다"다. `ignored` 나 `skipped` 와 달리 판단을 거친 결정이라는 뉘앙스가 있다. 다음 사람이 "왜 이건 비어 있지?"라고 물을 때 답이 되는 문장이다.
- 예문: The user deprioritized storage detail during design, so parse_records is still a stub.
- 유사어: put on the back burner (구어), moved down the list (평이), parked (보류)
- 반의어: prioritized, fast-tracked

## "was offered … — not confirmed"
- 레지스터: professional
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/handoff_ftp_fleet_downloader.md
- 맥락: 제안은 했지만 상대가 아직 결정하지 않은 상태를 인수인계에서 정확히 남길 때(문서·격식)
- 한국어: 제안은 했으나 확정되지 않았다
- 설명: `be offered + 동명사` 꼴(`was offered baking these as defaults`)은 "~하는 안을 제안받았다"다. 대시 뒤 `not confirmed` 두 단어가 상태를 못 박는다. 다음 담당자가 제안을 결정으로 착각하지 않게 하는 장치다.
- 예문: The user was offered baking these values in as defaults — not confirmed.
- 유사어: proposed but not yet agreed (평이), pending the user's call (결정 대기 쪽 강조)
- 반의어: signed off, agreed

## "edit the fleet without a code deploy"
- 레지스터: technical, conversational
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 설정을 코드 밖으로 뺀 이점을 운영 관점에서 한 줄로 말할 때(문서·구어)
- 한국어: 코드 배포 없이 대상 목록을 고칠 수 있다
- 설명: `without a code deploy` 의 `deploy` 는 명사로 쓰였다. 원래 동사지만 개발자 영어에서는 `a deploy` 를 `a deployment` 대신 흔히 쓴다. 대시 뒤에 붙여 앞 설명(매 실행마다 Variable 을 다시 읽는다)의 효과를 짧게 밝힌다.
- 예문: The host list is re-read every run, so you can edit the fleet without a code deploy.
- 유사어: change it at runtime (기술적), no redeploy needed (구어, 짧음)
- 반의어: hard-coded, baked into the build

## "Terms only; no implementation detail (that lives in X)."
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy ftp_handler/docs/adr/CONTEXT.md
- 맥락: 문서 첫머리에서 이 문서가 다루는 범위와 다른 정보가 있는 곳을 함께 밝힐 때(문서·격식)
- 한국어: 용어만 다룬다. 구현 세부는 X 에 있다.
- 설명: `lives in` 은 정보·코드가 "어디에 살고 있다", 즉 그 문서가 정본이라는 뜻의 개발자 관용이다. 범위 선언과 참조를 한 줄에 묶어 중복 서술을 막는다. 명사구만으로 된 머리글이라 동사가 없다.
- 예문: This file defines terms only; the implementation detail lives in the reference doc.
- 유사어: is covered in (평이), see X for … (가장 흔한 참조 표현), is documented in (격식)
