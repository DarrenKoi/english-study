# 2026-11-13 — 새 표현

오늘 배치는 skewnono_v3_nuxt 문서 7건과 대화 기록 5개입니다. 문서는 전부 한국어라 표현 출처가 되지 못했습니다. 영어는 pm-notes 세션(6a5d0980)에 실린 ponytail 지침과 computer-use 지침, 하니스가 끼워 넣는 안내 문구에서 골랐습니다. ponytail 문서는 10-18, 11-01 배치에서 이미 많이 다뤄서 그때 빠진 문장만 가져왔습니다.

## "Two rungs work → take the higher one and move on."
- 레지스터: conversational, technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, The ladder)
- 맥락: 선택지 둘이 다 될 때 오래 재지 말고 고르라고 할 때(팀 규칙·구어)
- 한국어: 두 칸 다 되면 위 칸을 택하고 넘어가라
- 설명: `Two rungs work` 는 `If two rungs work` 에서 `if` 를 뺀 메모투 조건절입니다. `move on` 은 "그 문제는 접고 다음으로 간다"는 뜻이라 고민을 끊는 말로 자주 붙습니다.
- 예문: Both libraries would do the job, so take the smaller one and move on.
- 유사어: pick one and keep going (구어), go with the simpler option and proceed (격식), don't overthink it (캐주얼)
- 반의어: keep weighing the options (계속 재다)

## "clever is what someone decodes at 3am"
- 레지스터: conversational, technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Rules)
- 맥락: 기교 부린 코드를 말릴 때(코드 리뷰·구어)
- 한국어: 기발한 코드는 누군가 새벽 3시에 해독해야 하는 코드다
- 설명: 형용사 `clever` 를 그대로 주어로 세웠습니다. 앞 문장 `Boring over clever` 의 마지막 단어를 받아 정의를 내리는 꼴입니다. `what someone decodes` 는 선행사를 품은 관계절로 "누군가 해독하는 것"이고, `at 3am` 이 장애 호출이라는 상황을 불러옵니다.
- 예문: Keep the query plain, because clever is what someone decodes at 3am.
- 유사어: clever code is a maintenance burden (격식), write it so the on-call can read it (구어), don't be cute (캐주얼)
- 반의어: boring code reads itself (작성)

## "The smallest change in the wrong place isn't lazy, it's a second bug."
- 레지스터: professional, technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Rules)
- 맥락: 작은 diff 를 자랑하는 수정이 엉뚱한 곳을 고쳤을 때(리뷰·설계 근거)
- 한국어: 엉뚱한 자리에 넣은 최소 수정은 게으름이 아니라 두 번째 버그다
- 설명: `isn't A, it's B` 로 이름표를 바꿔 붙입니다. 접속사 없이 쉼표만으로 두 절을 이어 말하듯 들립니다. 격식 있는 글이라면 세미콜론이나 `but rather` 를 씁니다. `a second bug` 의 부정관사는 "하나 더"라는 뜻입니다.
- 예문: Patching the template would hide the symptom, but the smallest change in the wrong place isn't lazy, it's a second bug.
- 유사어: a quick fix in the wrong layer just moves the problem (구어), a minimal patch at the wrong level introduces a new defect (격식)
- 반의어: the right fix in the right place (작성)

## "Take the one that's correct on edge cases."
- 레지스터: technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Rules)
- 맥락: 크기가 같은 두 구현 중 하나를 고르는 기준을 줄 때(리뷰·문서)
- 한국어: 경계 사례에서 맞게 동작하는 쪽을 골라라
- 설명: `the one that's …` 의 `one` 이 앞의 `option` 을 받습니다. `correct on edge cases` 에서 전치사가 `on` 인 점을 눈여겨봅니다. 입력 종류를 말할 때 `on` 을 씁니다(`fails on empty input`). 바로 뒤 문장이 `not picking the flimsier algorithm` 으로 반대쪽을 짚습니다.
- 예문: Both parsers are ten lines long, so take the one that's correct on edge cases.
- 유사어: prefer the one that handles corner cases (비슷한 격식), go with whichever doesn't break on weird input (구어)
- 반의어: pick the flimsier algorithm (허술한 쪽을 고르다)

## "patching only the path the ticket names leaves every sibling caller still broken"
- 레지스터: technical, professional
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Bug fix = root cause)
- 맥락: 신고된 경로만 고친 수정이 왜 부족한지 설명할 때(리뷰·사후 분석)
- 한국어: 티켓에 적힌 경로만 고치면 같은 함수를 부르는 다른 호출자는 모두 고장 난 채 남는다
- 설명: 동명사구가 주어이고 동사는 `leaves` 입니다. `leave + 목적어 + 형용사` 는 "~을 어떤 상태로 남겨 두다"입니다. `the path the ticket names` 는 목적격 관계대명사가 빠진 꼴이고 `names` 는 동사("지목하다")입니다. `sibling caller` 는 같은 함수를 부르는 형제 호출자입니다.
- 예문: Patching only the path the ticket names leaves every sibling caller still broken, so the guard belongs in the shared helper.
- 유사어: fixing just the reported case leaves the others exposed (구어), a point fix does not address the remaining call sites (격식)
- 반의어: fix it once, where all callers route through (한 곳에서 한 번에 고치다)

## "Lazy code without its check is unfinished."
- 레지스터: professional, technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, When NOT to be lazy)
- 맥락: 코드만 내고 검증을 안 붙인 작업을 미완성으로 규정할 때(팀 규칙·리뷰)
- 한국어: 확인 코드가 없는 간결한 코드는 끝난 게 아니다
- 설명: `without its check` 가 주어를 뒤에서 좁히고 보어는 형용사 `unfinished` 하나입니다. 금지문이 아니라 정의문으로 규칙을 말하는 방식입니다. `its` 가 "그 코드에 딸린"이라는 소유를 만들어 확인이 코드의 일부라는 뜻이 됩니다.
- 예문: The parser looks fine, but lazy code without its check is unfinished, so add one assert before you merge.
- 유사어: it's not done until it's tested (구어), untested code should not be considered complete (격식), no test, no merge (캐주얼)

## "The ladder shortens the solution, never the reading."
- 레지스터: professional
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, When NOT to be lazy)
- 맥락: 줄여도 되는 것과 줄이면 안 되는 것을 한 문장으로 가를 때(원칙 문서)
- 한국어: 사다리는 풀이를 줄일 뿐 읽는 일을 줄여 주지는 않는다
- 설명: 쉼표 뒤에서 동사를 생략하고 `never + 목적어` 만 남겼습니다. `shortens A, never B` 는 `A, not B` 보다 단호합니다. `the reading` 은 동명사에 정관사를 붙여 "(문제와 코드를) 읽는 그 일"로 명사화했습니다.
- 예문: A template shortens the writing, never the thinking.
- 유사어: it saves you code, not comprehension (구어), this reduces implementation effort but not the need to understand the problem (격식)

## "Ponytail governs what you build, not how you talk"
- 레지스터: professional, technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Boundaries)
- 맥락: 규칙이 적용되는 범위와 적용되지 않는 범위를 나눌 때(지침·정책 문서)
- 한국어: ponytail 이 정하는 것은 무엇을 만드느냐이지 어떻게 말하느냐가 아니다
- 설명: `govern` 은 "규율하다, 적용 대상으로 삼다"로, 법 조문이나 정책 문서에서 범위를 말할 때 씁니다. 목적어 자리에 의문사절 두 개(`what you build` / `how you talk`)를 `A, not B` 로 나란히 놓았습니다.
- 예문: This policy governs what gets deployed, not how teams organize their branches.
- 유사어: applies to (가장 평이), covers (구어), is scoped to (기술 문서)
- 반의어: is out of scope for (범위 밖이다)

## "Do NOT interpret this as user acknowledgement, confirmation, or response to any pending question."
- 레지스터: professional, technical
- 출처: transcript:pm-notes 6a5d0980 (하니스 백그라운드 작업 알림)
- 맥락: 자동 알림을 사람의 답으로 오해하지 말라고 못 박을 때(시스템 안내문·격식)
- 한국어: 이것을 사용자의 확인, 승인, 또는 대기 중인 질문의 답으로 해석하지 말 것
- 설명: `interpret A as B` 의 B 자리에 명사 셋을 나열했습니다. `acknowledgement` 는 "받았다는 표시", `confirmation` 은 "맞다는 확인"으로 무게가 다릅니다. `pending question` 은 아직 답을 못 받은 질문입니다. `any` 가 "어느 것이든"으로 예외를 막습니다.
- 예문: Do not interpret the automated receipt as acknowledgement, confirmation, or response to any pending question.
- 유사어: don't take this as a yes (구어), this does not constitute approval (격식·법률), this isn't a reply from the user (평이)
- 반의어: treat this as explicit confirmation (명시적 확인으로 보다)

## "must NOT be treated as approval or consent"
- 레지스터: professional
- 출처: transcript:pm-notes 6a5d0980 (하니스 백그라운드 작업 알림)
- 맥락: 어떤 진술이 동의의 근거가 될 수 없다고 규정할 때(정책·안내문·격식)
- 한국어: 승인이나 동의로 취급해서는 안 된다
- 설명: 수동태 `be treated as` 로 행위자를 지우고 규칙만 남겼습니다. 원문 주어는 `Any statement that the user said, approved, or confirmed something` 으로 길어서, 수동태가 아니면 문장이 무거워집니다. `approval` 은 허가, `consent` 는 당사자의 동의라 둘을 함께 적어 빈틈을 없앱니다.
- 예문: Silence from the reviewer must not be treated as approval or consent.
- 유사어: doesn't count as a go-ahead (구어), shall not be construed as consent (법률 문체), is not a sign-off (업무 구어)

## "debug or report it rather than silently retrying via a slower tier"
- 레지스터: technical
- 출처: transcript:pm-notes 6a5d0980 (computer-use 지침, Pick the right tool for the app)
- 맥락: 실패를 느린 우회로로 덮지 말라고 할 때(도구 지침·운영 문서)
- 한국어: 더 느린 단계로 말없이 다시 시도하지 말고 원인을 찾거나 보고하라
- 설명: `A rather than B-ing` 에서 A 는 명령문 동사 원형, B 는 동명사입니다. 형태가 달라도 자연스러운 구문입니다. `silently` 가 핵심으로, 재시도 자체보다 "알리지 않고" 하는 것을 문제 삼습니다. `tier` 는 속도와 정밀도로 나눈 도구 등급입니다.
- 예문: If the API call fails, debug or report it rather than silently retrying via a slower tier.
- 유사어: don't quietly fall back to the slow path (구어), surface the failure instead of masking it with a fallback (격식)
- 반의어: fall back silently (말없이 대체 경로로 넘어가다)

## "Treat this as a connection failure, not a missing capability"
- 레지스터: technical, professional
- 출처: transcript:pm-notes 6a5d0980 (하니스 MCP 서버 연결 실패 안내)
- 맥락: 장애의 종류를 잘못 분류하지 않게 선을 그을 때(운영 안내·보고)
- 한국어: 기능이 없는 게 아니라 연결이 실패한 것으로 다뤄라
- 설명: `treat A as B, not C` 로 분류를 지정합니다. 뒤에 `do not conclude the server is unconfigured or that access does not exist` 가 이어져 성급한 결론 두 가지를 막습니다. `missing capability` 는 "원래 없는 기능"이라 재시도해도 소용없지만 `connection failure` 는 다시 붙으면 해결됩니다.
- 예문: Treat this as a connection failure, not a missing capability, and ask the user to retry the server.
- 유사어: it's down, not gone (캐주얼), this is an outage rather than an unsupported feature (격식)

## "No need to announce the new date — the user's own clock shows it."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (하니스 날짜 변경 안내)
- 맥락: 상대가 이미 아는 사실을 굳이 말하지 말라고 할 때(구어·메모)
- 한국어: 새 날짜를 알릴 필요는 없다. 사용자 시계에 이미 나와 있다
- 설명: `There is` 를 뺀 `No need to + 동사원형` 은 메모와 대화에서 흔한 생략형입니다. 대시 뒤에 이유를 접속사 없이 붙였습니다. `the user's own clock` 의 `own` 이 "남이 알려 줄 것 없이 자기 것으로"라는 느낌을 더합니다.
- 예문: No need to announce the deploy time — the dashboard already shows it.
- 유사어: you don't have to mention it (평이), it goes without saying (관용), there is no need to state the obvious (격식)

## "no interface with one implementation, no factory for one product"
- 레지스터: technical
- 출처: transcript:pm-notes 6a5d0980 (ponytail 지침, Rules)
- 맥락: 쓸 곳이 하나뿐인 추상화를 금지할 때(코딩 규칙·리뷰)
- 한국어: 구현이 하나뿐인 인터페이스도, 제품이 하나뿐인 팩토리도 만들지 않는다
- 설명: 동사 없이 `no + 명사구` 를 나열한 규칙문입니다. 원문은 `No unrequested abstractions:` 뒤 콜론으로 세 가지 예(`no config for a value that never changes` 까지)를 풉니다. 전치사가 `with`(딸린 것)와 `for`(대상)로 갈리는 점도 봐 둡니다.
- 예문: Keep the module flat: no interface with one implementation, no factory for one product.
- 유사어: don't abstract until you have two users (구어), avoid premature abstraction (격식), YAGNI (약어)
