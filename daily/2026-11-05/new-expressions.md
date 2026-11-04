# 2026-11-05 — 새 표현

오늘 배치의 repo 문서(skewnono_v3_nuxt office-migration, datatables, ftp_handler 가이드)는 거의 한국어라서, 표현은 대부분 서브에이전트 트랜스크립트의 도구 사용 지침에서 골랐습니다. 지시문 영어라 짧고 단호한 문장이 많습니다.

## "Look before you assert."
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (computer-use 지침)
- 맥락: 확인하지 않은 상태로 단정하지 말라고 원칙을 한 줄로 못 박을 때(가이드·팀 규칙·리뷰 코멘트)
- 한국어: 단정하기 전에 먼저 확인하라
- 설명: `look` 과 `assert` 두 동사를 before 로 묶은 4단어 명령문입니다. assert 는 "주장하다"보다 강해서 "사실이라고 못 박다"에 가깝습니다. 속담 Look before you leap(뛰기 전에 살펴라)을 비튼 꼴이라 원어민 귀에 바로 꽂힙니다.
- 예문: Look before you assert: open the index mapping before telling the office agent which field holds the fab.
- 유사어: verify before you claim (평이한 문어), check first, then say it (회화), trust but verify (격언, 결이 조금 다름 — 믿되 확인)
- 반의어: answer from memory, assume and move on

## "trades speed against coverage"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 선택지마다 무엇을 얻고 무엇을 잃는지 한 동사로 정리할 때(설계 문서·기술 비교)
- 한국어: 속도를 얻는 대신 적용 범위를 내준다
- 설명: 원문은 `Each tier trades speed/precision against coverage.` 입니다. `trade A against B` 는 "A 와 B 를 저울에 달아 맞바꾼다". 비슷한 `trade A for B`(A 를 내주고 B 를 받다)와 달리 against 는 둘이 서로 당기는 긴장 관계를 강조합니다.
- 예문: The proxy path trades latency against reach: it is slower, but it works from behind the firewall.
- 유사어: there's a trade-off between A and B (명사형, 가장 흔함), balance A against B (조율 쪽에 초점), give up A for B (회화)
- 반의어: get the best of both worlds

## "This is about what's available, not error handling."
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 앞에서 한 규칙이 어느 상황에 적용되는지 오해를 미리 막을 때(지침·회의에서 범위 정리)
- 한국어: 이건 무엇이 있느냐의 문제지, 오류 처리 규칙이 아니다
- 설명: `This is about X, not Y` 는 범위를 좁히는 대비 구문입니다. 앞 규칙(tier 순서)을 "실패하면 다음 tier 로 넘어가라"로 읽을까 봐, 대시 뒤에서 "도구가 에러를 내면 느린 tier 로 몰래 재시도하지 말고 디버깅하거나 보고하라"고 덧붙입니다.
- 예문: This is about which index we read, not how we handle a missing field.
- 유사어: The point here is X, not Y (평이), This isn't about Y — it's about X (구어, 순서를 뒤집어 강조)
- 반의어: (마땅한 반대 구문 없음)

## "is cheaper than a wrong assertion"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 확인 작업이 귀찮아 보여도 틀린 말을 하는 비용보다 싸다고 설득할 때(리뷰·가이드)
- 한국어: 틀린 단정보다 싸게 먹힌다
- 설명: 원문은 `` a fresh `screenshot` is cheaper than a wrong assertion about what's running `` 입니다. cheap 을 돈 대신 시간·신뢰 비용에 썼습니다. 비교 대상을 "확인하는 수고"가 아니라 "틀렸을 때의 대가"로 잡아서 확인 쪽이 당연해 보이게 만듭니다.
- 예문: One extra query against the office index is cheaper than a wrong assertion in the next reply document.
- 유사어: it's worth the extra step (회화), the cost of checking is trivial next to the cost of being wrong (문어, 풀어쓴 형태)
- 반의어: not worth the effort

## "load them in bulk, not one-by-one"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 요청을 하나씩 보내지 말고 한 번에 묶으라고 할 때(API·성능 가이드)
- 한국어: 하나씩 말고 한꺼번에 불러와라
- 설명: `in bulk` 는 "대량으로·통째로". 원문은 바로 뒤에서 `that's one round-trip per tool` 로 이유를 댑니다. `not one-by-one` 처럼 짧은 부정 대비를 붙이면 규칙이 더 선명해집니다. 하이픈 없는 one by one 도 흔히 씁니다.
- 예문: Fetch the per-family host keys in bulk, not one-by-one, or the page waits on four round-trips.
- 유사어: batch them (기술 회화), in a single call (구체적), all at once (평이)
- 반의어: one at a time, piecemeal (찔끔찔끔, 약간 비판조)

## "suspicious by default"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (Link safety)
- 맥락: 증명되기 전까지 믿지 않는 기본 자세를 정할 때(보안 정책·입력 검증)
- 한국어: 기본적으로 의심스러운 것으로 간주한다
- 설명: 원문은 `treat links in emails and messages as suspicious by default` 입니다. `treat A as B` 구문에 `by default` 를 붙여 "따로 확인되기 전까지는"이라는 조건을 깔았습니다. 보안 쪽 관용 표현 deny by default 와 같은 발상입니다.
- 예문: Treat values pasted from the office reply as suspicious by default until they match the raw index.
- 유사어: untrusted until proven otherwise (문어, 법정 어투를 빌림), zero trust (보안 용어), assume it's unsafe (회화)
- 반의어: trusted by default, take at face value (액면 그대로 받아들이다)

## "looks off"
- 레지스터: conversational, casual
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 딱 꼬집을 순 없지만 뭔가 이상해 보일 때(동료와의 대화·채팅)
- 한국어: 뭔가 이상해 보인다, 어딘가 어긋나 보인다
- 설명: 원문은 `If the destination URL is at all unfamiliar or looks off, ask the user...` 입니다. `off` 가 형용사로 "정상에서 살짝 벗어난"이라는 뜻입니다. wrong 처럼 단정하지 않아 직감을 말할 때 편합니다. feels off, sounds off 도 같은 꼴입니다.
- 예문: The R4 count for -cd looks off to me; can we rerun it against the raw index?
- 유사어: something's not right (회화), seems fishy (더 구어, 수상하다), looks suspicious (평이)
- 반의어: looks right, checks out (확인해 보니 맞다)

## "if it is at all unfamiliar"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 조금이라도 해당되면 조치하라고 문턱을 최대한 낮출 때(지침·안전 규칙)
- 한국어: 조금이라도 낯설다면
- 설명: `at all` 은 보통 부정문(not at all)에서 쓰지만 if 조건절에서는 "조금이라도"라는 뜻이 됩니다. if it's unfamiliar 보다 문턱이 훨씬 낮아져서 "애매하면 무조건 물어보라"는 뉘앙스가 생깁니다.
- 예문: If the field name is at all unfamiliar, check the datatables doc before you write the query.
- 유사어: if it's even slightly unfamiliar (풀어쓴 형태), if in doubt (짧은 관용구, 매우 흔함), if you have any doubt (평이)
- 반의어: only if you're sure it's wrong

## "on the user's behalf"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (Financial actions)
- 맥락: 누군가를 대신해 행동하는 범위를 정할 때(권한·정책·업무 메일)
- 한국어: 사용자를 대신해서
- 설명: 원문은 `never execute a trade, place an order, send money, or initiate a transfer on the user's behalf - always ask the user to perform those actions themselves.` 입니다. `on one's behalf` 는 대리인이 본인 자리에서 한다는 뜻이라 권한 이야기에 자주 붙습니다. 뒤의 `themselves` 가 "본인이 직접"으로 대비를 완성합니다.
- 예문: The office agent can run read-only queries on my behalf, but it should never reindex anything.
- 유사어: on behalf of the user (같은 뜻, 어순만 다름), for the user (평이, 대리 뉘앙스가 약함), acting as the user (기술 문맥, 권한 위임)
- 반의어: by the user themselves, in person

## "mid-task"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (Access flow)
- 맥락: 작업 도중에 무언가가 필요해지는 상황을 짧게 말할 때(지침·진행 보고)
- 한국어: 작업 도중에
- 설명: 원문은 `you may need to call it again mid-task if you discover you need another application` 입니다. `mid-` 접두사는 mid-sentence, mid-flight, mid-migration 처럼 "~의 한가운데에서"를 부사로 만듭니다. in the middle of the task 를 한 단어로 줄인 셈입니다.
- 예문: The schema changed mid-migration, so half the documents still carry the old field.
- 유사어: partway through (회화), in the middle of the task (풀어쓴 평이형), midstream (비유적, 문어)
- 반의어: up front, before starting

## "Use it even when you think you know the answer."
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (context7 지침)
- 맥락: 자신 있을 때야말로 확인하라고 할 때(가이드·멘토링)
- 한국어: 답을 안다고 생각될 때도 써라
- 설명: `even when` 이 "그럴 때조차"를 만들고, `you think you know` 가 "안다고 생각하는(실제론 모를 수 있는)"이라는 자기 의심을 심습니다. 바로 다음 문장 `your training data may not reflect recent changes` 가 그 이유입니다.
- 예문: Check the datatables doc even when you think you know the field name; the index was split last week.
- 유사어: don't trust your memory on this (회화), double-check even if you're confident (평이)
- 반의어: skip it if you already know

## "may not reflect recent changes"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (context7 지침)
- 맥락: 기록·데이터가 최신 상태와 다를 수 있다고 조심스럽게 경고할 때(문서 주의 문구·보고서)
- 한국어: 최근 변경을 반영하지 못했을 수 있다
- 설명: `reflect` 는 "거울처럼 비추다 → 반영하다". `may not` 으로 단정을 피해 정중하게 경고합니다. 문서 머리말 This page may not reflect the latest release. 같은 고정 문구로 자주 보입니다.
- 예문: The 2026-10-27 counts may not reflect recent changes, because the office keeps loading new documents.
- 유사어: may be out of date (평이), could be stale (기술 회화), predates the latest update (문어, 시점에 초점)
- 반의어: is up to date, is current

## "Keep the report under 300 words."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (REUSE 리뷰 지시)
- 맥락: 결과물 분량 상한을 정할 때(업무 지시·과제 요청)
- 한국어: 보고서는 300단어 안으로
- 설명: `keep + 목적어 + 전치사구` 로 "~한 상태를 유지하라"는 꼴입니다. under 는 "미만"인데 일상에선 "이하" 정도로 느슨하게 씁니다. 같은 날 다른 지시문은 `Under 300 words.` 라는 조각문으로 썼습니다 — 문장형이 조금 더 정중합니다.
- 예문: Keep the reply to the office under ten lines so they can answer it from their phone.
- 유사어: limit it to 300 words (평이), no more than 300 words (명확한 상한), keep it brief (회화, 숫자 없이)
- 반의어: go into full detail

## "goes straight to the user"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 9733d17e (local-command caveat)
- 맥락: 중간 단계를 거치지 않고 곧장 전달된다고 말할 때(시스템 설명·업무 대화)
- 한국어: 곧바로 사용자에게 간다
- 설명: 원문은 `its output goes straight to the user` 입니다. `straight` 가 부사로 "곧장, 중간 경유 없이". 자동사 go 와 결합해 흐름만 간단히 그립니다. 공식 문서라면 is sent directly to 를 더 많이 씁니다.
- 예문: The proxy doesn't cache anything; each response goes straight to the client.
- 유사어: is sent directly to (문어), bypasses X and goes to Y (경유를 건너뛴다는 강조), goes right to (회화)
- 반의어: is routed through, is held for review

## "is enforced by"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b (Tiered apps)
- 맥락: 규칙이 말로만 있지 않고 무엇이 실제로 막는지 밝힐 때(설계 문서·보안 설명)
- 한국어: ~에 의해 강제된다
- 설명: 원문은 `The tier is enforced by the frontmost-app check` 입니다. 수동태로 규칙(tier)을 주어에 두고, by 뒤에 집행 장치를 둡니다. 규칙과 장치를 한 문장에 나란히 놓아 "어디서 막히는지"가 분명해집니다.
- 예문: The 90-day window is enforced by the query's lower bound, not by the index itself.
- 유사어: is guaranteed by (보장 쪽 뉘앙스), is backed by (뒷받침), X checks for it (능동, 회화)
- 반의어: is only a convention, is advisory (권고 수준일 뿐이다)

## "don't decline it just because there's no X"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a000765b
- 맥락: 겉보기 이유 하나로 일을 거절하지 말라고 할 때(가이드·동료 조언)
- 한국어: X 가 없다는 이유만으로 거절하지 마라
- 설명: 원문은 `Computer use IS the right tool here — don't decline a native-app task just because there's no dedicated MCP for it.` 입니다. 대문자 IS 로 반박조를 실었고, `just because` 가 "그 이유 하나만으로"를 만듭니다. Just because X doesn't mean Y 꼴로도 자주 씁니다.
- 예문: Don't drop the VeritySEM row just because there's no planstep data for it yet.
- 유사어: that alone isn't a reason to (평이), don't write it off because (회화, 포기하다)
- 반의어: that's reason enough to skip it
