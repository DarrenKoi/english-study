# 2026-10-06 — 새 표현

> 오늘 배치는 repo 문서 15건과 transcript 15건이다. transcript 일곱은 `/clear`·`/model`·`/plugin` 만 찍힌 빈 세션, 둘은 이 학습 파이프라인의 실행 기록이라 재료에서 뺐다. 내용이 있는 네 세션(auto-recipe-creator 자원 누수 검토, skewnono 페이지 가치 브레인스토밍·테스트 정리 검토·AFM 적재 명세)은 대화가 거의 한국어여서 코칭 쪽 재료가 됐다. repo 문서도 pm_notes 의 `ai-terms-html-reader` 구현 계획 하나를 빼면 전부 한국어. 영어는 세 군데서 나왔다. skewnono 서브에이전트 두 건의 지시문(수정 층위를 묻는 ALTITUDE 리뷰, `/code-review low` 규칙), 브레인스토밍 세션에 딸려 온 Herdr 스킬 문서, 그리고 위 구현 계획. 계획 문서는 어제 배치에도 있었으므로 그때 고르지 않은 것만 골랐다. 목록 항목은 도입 문장과 이어 붙였고 원문이 명사구뿐인 것은 문장으로 고쳐 `(작성)` 을 달았다. 노트에 이미 있어서 뺀 것: `when the layout calls for it`, `honor (a filter)`, `swallow an exception`, `on purpose`, `off-by-one`, `in scope / out of scope`, `checked-in`, `progressive enhancement`, `treat every ID as an opaque string`, `Inspect before waiting.`, `do not infer a larger topology from X`.

## "layered on top of a shared mechanism"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 리뷰에서 "밑의 공용 장치를 고쳤어야 하는데 위에 덧댔다"고 지적할 때(코드 리뷰·설계 검토, 문어).
- 한국어: 공용 메커니즘 위에 덧씌운
- 설명: `layer A on top of B` 는 B 를 그대로 둔 채 A 를 한 겹 얹는다는 말. 여기서는 과거분사 `layered` 가 `a special case / bandaid` 를 뒤에서 꾸민다. 뒤따르는 `that should have been changed instead` 가 "고쳤어야 할 것은 아래쪽"이라고 못 박는다. `should have + p.p.` 는 하지 않은 일을 아쉬워하는 형태.
- 예문: Angle: ALTITUDE — is each change made at the right depth, or is it a special case / bandaid layered on top of a shared mechanism that should have been changed instead?
- 유사어: bolted on (나중에 억지로 붙였다는 어감), papered over (문제를 가렸다는 쪽), patched at the call site (호출부에서 땜질)
- 반의어: fixed at the source (원인 자리에서 고친), built into the mechanism (장치 안에 넣은)

## "say it is fine where it is"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 검토를 맡기면서 "안 옮겨도 되면 그렇다고 말해 달라"고 출구를 열어 줄 때(리뷰 요청, 구어에 가까운 지시).
- 한국어: 지금 자리에 둬도 괜찮다고 말해 줘
- 설명: `where it is` 는 "지금 있는 그 자리에". `fine as it is`(지금 상태 그대로)와 비슷하지만 `where` 를 쓰면 위치, 곧 코드가 놓인 층을 가리킨다. "문제없음"도 답으로 받겠다는 말이라 리뷰어가 억지 지적을 지어낼 까닭이 없어진다.
- 예문: For each item, tell me the deeper change if there is one, or say it is fine where it is. (작성)
- 유사어: leave it where it is (그대로 두라는 지시), it's fine as is (상태 쪽), no need to move it (평이)
- 반의어: it belongs somewhere deeper (더 아래로 가야 한다)

## "Weigh against: …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 제안을 내놓은 바로 뒤에 반대편 사정을 붙여 "이것과 견줘 판단하라"고 할 때(리뷰 지시문·설계 메모).
- 한국어: 다만 이것과 견줘 볼 것
- 설명: `weigh A against B` 는 저울 양쪽에 올려 견준다는 뜻. 여기서는 A 를 생략하고 명령문에 콜론을 붙여 반대 근거를 곧바로 늘어놓았다. 질문(`Should the contract carry …?`)만 던지면 답이 "그렇다"로 기울기 쉬운데, 이 한 줄이 반대쪽 무게를 미리 올려 둔다.
- 예문: Weigh against: `backend/afm/MIGRATION.md` treats the payload as office-contract surface, and the office adapter (`providers/office_example.py`) is still a stub.
- 유사어: On the other hand, … (평이한 연결어), Counterpoint: … (메모체), Bear in mind that … (주의 환기)

## "Should the contract carry … instead?"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 프론트가 추측하는 값을 백엔드 응답에 실어 보내자고 제안할 때(API 설계 논의).
- 한국어: 계약(응답)에 ~를 실어 보내야 하지 않나?
- 설명: `carry` 는 payload·row·contract 가 필드를 "싣고 다닌다"는 뜻으로 쓴다. `include` 보다 데이터가 그 값을 달고 이동한다는 그림이 선다. `Should … instead?` 는 단정 대신 질문으로 대안을 내미는 틀이고 `instead` 가 "지금 방식 말고"를 맡는다. `per row` 는 "행마다".
- 예문: Should the contract carry a block index/name per row instead?
- 유사어: include (중립), expose (바깥에 내보인다는 쪽), ship … in the payload (구어)
- 반의어: reconstruct it on the client (클라이언트에서 다시 짜 맞추다), infer it from row order (행 순서로 추측하다)

## "normalising once where rows enter the app"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 방어 코드를 곳곳에 두지 말고 데이터가 들어오는 입구 한 곳에서 정리하자고 할 때(코드 리뷰).
- 한국어: 행이 앱에 들어오는 자리에서 한 번만 정규화하기
- 설명: `where rows enter the app` 은 장소를 나타내는 부사절이고 "경계에서"를 풀어 썼다. 핵심은 `once`. 뒤의 `so every consumer gets clean strings` 가 이득을 댄다. 철자는 영국식 `normalising`(미국식 `normalizing`).
- 예문: Normalise the rows once where they enter the app, so every consumer gets clean strings. (작성)
- 유사어: validate at the boundary (경계 검증, 격식), sanitize on the way in (구어), parse, don't validate (격언)
- 반의어: null-check at every call site (호출부마다 방어), scatter the call (호출을 흩뿌리다)

## "take its clock from one injectable place"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 코드가 "지금 시각"을 직접 읽지 말고 주입받게 하자고 할 때(테스트 설계).
- 한국어: 시계를 주입 가능한 한 곳에서 받아 오다
- 설명: `clock` 은 시계 자체가 아니라 현재 시각을 얻는 출처. `take X from Y` 로 출처를 밝히고 `injectable` 로 테스트가 갈아 끼울 자리임을 말한다. 원문은 저장소 전체 fixture 로 날짜를 고정하는 안과 이 안을 `versus` 로 맞세웠다.
- 예문: It would be cleaner for the mock to take its clock from one injectable place than to pin the date in a repo-wide fixture. (작성)
- 유사어: accept a `now` parameter (가장 평이), go through a clock seam (seam 은 갈아 끼울 자리), read time from a single source (출처 하나)
- 반의어: call `date.today()` inline (그 자리에서 직접 읽다), hard-code the date (날짜를 박아 넣다)

## "a hand-measured sum"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 레이아웃의 숫자가 계산이 아니라 손으로 재서 더한 값임을 밝힐 때(코드 리뷰, 스스로 약점을 적을 때).
- 한국어: 손으로 재서 더한 값
- 설명: `hand-` + 과거분사는 "자동이 아니라 사람이 직접"이라는 형용사를 만든다(`hand-tuned`, `hand-rolled`). 앞에 나온 `a magic clamp(...)` 의 `magic` 은 근거가 코드에 없는 숫자를 부르는 `magic number` 에서 왔다. 둘을 나란히 쓰면 "이 28rem 은 카드의 다른 부분이 바뀌면 틀린다"는 고백이 된다.
- 예문: The sticky rail height is handled by a magic `clamp(6rem, calc(100dvh - 28rem), 16rem)` in PointRail, where 28rem is a hand-measured sum of the card's other parts. (작성)
- 유사어: a hard-coded offset (박아 넣은 값), an eyeballed number (눈대중, 구어), a hand-tuned constant (손으로 맞춘 상수)
- 반의어: a computed value (계산한 값), measured at runtime (실행 중에 잰)

## "know about (a key that only the page adds)"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 한 모듈이 다른 모듈의 사정을 알고 있어 결합이 생겼다고 지적할 때(설계 리뷰).
- 한국어: ~의 존재를 알고 있다(거기에 묶여 있다)
- 설명: 코드 리뷰에서 `A knows about B` 는 "A 가 B 에 의존한다"의 구어다. 사람처럼 "안다"고 말하지만 실은 결합을 탓한다. 여기서는 표 유틸이 페이지에서만 붙이는 키를 알고 있다는 점이 문제. 거꾸로 `A doesn't need to know about B` 는 칭찬으로 쓴다.
- 예문: `ID_COLUMN_KEYS` in `afmPointsTable.ts` knows about a key that only the page adds. (작성)
- 유사어: be coupled to (격식), depend on (중립), reach into (남의 속을 들여다본다는 어감)
- 반의어: be agnostic of (모른다, 그래서 독립적이다), be unaware of

## "a more direct formulation"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 지금 로직이 돌아가긴 하지만 더 곧게 쓰는 길이 있는지 물을 때(리뷰 질문).
- 한국어: 더 직접적인 식 세우기
- 설명: `formulation` 은 문제를 식이나 절차로 세우는 방식. `that would not need the patches` 의 `would` 는 "그렇게 썼다면"이라는 가정을 품는다. 음수 인덱스를 살리려고 덧댄 보정 둘을 `the patches` 라고 불렀고 괄호 속 `e.g. generating per calendar day` 로 스스로 후보 하나를 내놓았다.
- 예문: Is there a more direct formulation (e.g. generating per calendar day) that would not need the patches?
- 유사어: a simpler way to express it (평이), a cleaner approach (구어), a more natural framing (관점 쪽)
- 반의어: a roundabout way (에두른 방식), a workaround (우회책)

## "Be decisive and concise"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 검토자에게 "얼버무리지 말고 짧게 결론을 내라"고 주문할 때(리뷰 요청의 마지막 줄).
- 한국어: 분명하게, 짧게 답해 달라
- 설명: `decisive` 는 결정을 미루지 않는 태도. `Be + 형용사` 명령문 뒤에 세미콜론으로 이유를 댔다. 어떤 것만 적용할지 미리 밝혀 두었으니 리뷰어는 판정 기준을 알고 답한다.
- 예문: Be decisive and concise; I will apply only the ones that are clearly net simpler and do not change the office contract without the user's say-so.
- 유사어: Give me a clear verdict (판정 요구), Don't hedge (얼버무리지 마라, 구어), Keep it short and commit to an answer (평이)
- 반의어: hedge (얼버무리다), sit on the fence (어느 편도 들지 않다)

## "clearly net simpler"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 변경을 받아들일 기준이 "더한 것과 뺀 것을 셈해도 더 단순한가"일 때(리팩토링 판단).
- 한국어: 셈해 봐도 분명히 더 단순한
- 설명: `net` 은 "더하고 빼고 남은". `net simpler` 라고 하면 새 필드나 테스트가 늘더라도 전체로는 단순해진다. `clearly` 를 얹어 "애매하면 안 한다"는 문턱을 세웠다. `net positive`, `a net win` 과 같은 계열.
- 예문: I'd take the second option — it is clearly net simpler, even after adding the test. (작성)
- 유사어: simpler on balance (격식), a net win (구어), simpler overall (평이)
- 반의어: net more complex (셈하면 더 복잡한), a wash (득실이 같은)

## "without the user's say-so"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 허락 없이는 하지 않을 일의 선을 그을 때(작업 지시, 구어).
- 한국어: 사용자의 허락 없이는
- 설명: `say-so` 는 "그렇게 하라는 말 한마디", 곧 허락이나 승인. `on someone's say-so` 는 "그 사람 말만 믿고"라는 다른 뜻이 되니 전치사를 가려 쓴다. 문서에서는 `approval` 이 무난하다.
- 예문: Don't change the office contract without the user's say-so. (작성)
- 유사어: without the user's approval (격식), without sign-off (업무 구어), unless the user OKs it (평이)
- 반의어: with the user's blessing (기꺼이 승인받고)

## "places I suspect are at the wrong depth"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)
- 맥락: 내 의심을 먼저 밝히고 확인을 맡길 때(리뷰 요청).
- 한국어: 내가 보기에 층위가 잘못된 것 같은 곳들
- 설명: `places (that) I suspect are …` 는 관계절 안에 `I suspect` 가 끼어든 꼴. `places that are at the wrong depth` 에 "내 생각엔"을 넣은 것이라 `are` 의 주어는 `places` 다. `I think`, `I believe` 가 이렇게 끼면 주격 관계대명사도 뺀다. `suspect` 는 `think` 보다 "증거는 없지만 그럴 것 같다"는 수위.
- 예문: Specific places I suspect are at the wrong depth — evaluate each and tell me the deeper/more general change if there is one, or say it is fine where it is.
- 유사어: places I think are … (평이), places that look … to me (구어), places that may be … (추측을 조동사로)

## "visible from the hunk alone"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: 검토 범위를 "diff 조각만 보고 알 수 있는 것"으로 한정할 때(코드 리뷰 규칙).
- 한국어: 그 hunk 만 보고도 드러나는
- 설명: `hunk` 는 diff 에서 `@@` 로 시작하는 변경 조각 하나. `from X alone` 은 "X 만으로". 파일 전체나 호출 관계를 읽지 않아도 보이는 결함만 잡으라는 요구. 같은 글이 `still from the hunk alone` 으로 한 번 더 못 박는다.
- 예문: Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong condition, off-by-one, … error swallowed in a catch that should propagate.
- 유사어: evident from the diff itself (격식), without leaving the hunk (평이), on the face of the diff (문어)
- 반의어: only visible with full-file context (파일 전체를 봐야 드러나는)

## "where adjacent lines show the value can be absent"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: 지적의 조건을 "근거가 바로 옆에 있을 때만"으로 좁힐 때(리뷰 규칙).
- 한국어: 바로 옆 줄들이 그 값이 없을 수 있음을 보여 주는 곳에서
- 설명: `where` 절이 `null/undefined deref` 를 한정한다. null 접근을 전부 잡으라는 말이 아니라 근처 코드가 "없을 수 있다"고 증언할 때만 잡으라는 조건. `show (that) the value can be absent` 에서 `absent` 는 `null`, `undefined`, 누락을 한데 부른다.
- 예문: Flag a null deref only where adjacent lines show the value can be absent. (작성)
- 유사어: when the surrounding code proves it can be null (평이), where the context shows it is optional (타입 쪽), if nearby lines guard against it (가드가 근거)
- 반의어: on suspicion alone (의심만으로)

## "dead code the diff leaves behind"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: 변경 때문에 쓸모없어졌는데 지워지지 않은 코드를 가리킬 때(코드 리뷰).
- 한국어: diff 가 남기고 간 죽은 코드
- 설명: `dead code (that) the diff leaves behind` 는 목적격 관계대명사를 뺀 관계절. `leave behind` 는 떠나면서 두고 가는 것이라 "호출부는 지웠는데 함수는 남았다" 같은 상황에 맞는다. diff 를 주어로 세워 사람을 탓하지 않는다.
- 예문: Also flag — still from the hunk alone — new code that duplicates an existing helper visible in the diff context, and dead code the diff leaves behind.
- 유사어: orphaned code (부를 곳을 잃은 코드), leftover code (평이), now-unused helpers (구체적)
- 반의어: code the diff cleans up (diff 가 치운 코드)

## "most-severe first, one line each"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: 결과 목록의 순서와 분량을 못 박을 때(보고 형식 지시).
- 한국어: 심각한 것부터, 하나에 한 줄씩
- 설명: 동사 없는 덧말 둘. `X first` 는 정렬 기준이고 `one line each` 의 `each` 는 뒤에 붙어 "각각 한 줄"이 된다(`two dollars each`). 앞의 `at most 4 findings` 까지 합치면 개수, 순서, 길이가 한 문장에 다 들어간다.
- 예문: Output at most 4 findings, most-severe first, one line each: `path/to/file.ext:123 — what's wrong and the concrete failure`.
- 유사어: worst first (구어), ranked by severity (격식), a line apiece (`apiece` 는 `each` 의 문어)
- 반의어: in no particular order (순서 없이)

## "If nothing qualifies, output exactly `(none)`."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: 해당 사항이 없을 때의 출력을 정해 줄 때(프롬프트·명세).
- 한국어: 해당하는 것이 없으면 정확히 `(none)` 만 출력하라
- 설명: `qualify` 는 "기준을 충족하다". 목적어 없이 `nothing qualifies` 로 쓴다. `exactly` 는 글자 그대로라는 뜻이어서 설명이나 사과를 덧붙이지 말라는 요구가 된다. 빈 결과에 이름을 붙여 두면 "못 찾음"과 "실행 실패"가 갈린다.
- 예문: If nothing qualifies, output exactly `(none)`.
- 유사어: If nothing meets the bar (구어), If there are no findings (평이), Should none apply (격식, 도치)

## "a falsy-zero check"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)
- 맥락: `if (!x)` 가 0 을 "없음"으로 잘못 걸러 내는 버그를 부를 때(JS/TS 코드 리뷰).
- 한국어: 0 을 거짓으로 취급해 버리는 검사
- 설명: `falsy` 는 불리언 문맥에서 거짓으로 평가되는 값(`0`, `''`, `null`, `undefined`, `NaN`). 값이 있는지 보려던 검사가 정상값 0 까지 버리는 실수에 붙인 이름이다. 원문에는 버그 유형 목록 속 명사구로만 나온다.
- 예문: `if (!count)` is a falsy-zero check: it treats a legitimate 0 as missing. (작성)
- 유사어: a truthiness check (참·거짓 평가에 기댄 검사), treating 0 as missing (풀어 쓴 말)
- 반의어: an explicit null check (`x == null`), a nullish check (`??`)

## "instead of predicting either one"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (Herdr 스킬 문서)
- 맥락: 값을 짐작하지 말고 응답에서 읽으라고 할 때(도구 문서·운영 지침).
- 한국어: 둘 중 어느 것도 짐작하지 말고
- 설명: 앞의 `identifiers and state` 둘을 `either one` 으로 받았다. `predict` 는 보통 앞일을 예측한다는 말인데 여기서는 "보지 않고 지어낸다"는 뜻. 에이전트가 ID 를 추측해 쓰는 일을 막는 문장이다.
- 예문: Read identifiers and state from those responses instead of predicting either one.
- 유사어: rather than guessing (평이), don't assume them (명령), never make them up (구어, 강함)
- 반의어: read it back from the response (응답에서 다시 읽다)

## "do not retarget later resources"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (Herdr 스킬 문서)
- 맥락: 한 번 쓴 식별자가 나중에 다른 대상을 가리키게 되지 않는다고 보장할 때(API·ID 설계 문서).
- 한국어: 나중에 생긴 자원을 가리키게 바뀌지 않는다
- 설명: `retarget` 은 "겨냥하는 대상을 바꾸다". 닫힌 창의 ID 가 재사용돼 새 창을 가리키면 옛 ID 로 보낸 명령이 엉뚱한 곳에 떨어진다. `are not reused and do not retarget` 로 수동과 능동을 나란히 써서 같은 보장을 두 번 말했다.
- 예문: Closed tab and pane IDs are not reused and do not retarget later resources.
- 유사어: are never recycled (재활용되지 않는다), never point at a different resource later (풀어 쓴 말), stay bound to the original (원래 대상에 묶여 있다)
- 반의어: be reused, be recycled (재사용되다)

## "unusably narrow columns"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (Herdr 스킬 문서)
- 맥락: 정도가 지나쳐 쓰지 못하게 된 상태를 한 단어로 말할 때(UI·레이아웃 설명).
- 한국어: 못 쓸 만큼 좁은 열
- 설명: `unusable` 에 `-ly` 를 붙여 형용사 `narrow` 를 꾸몄다. `too narrow to use` 를 부사 하나로 접은 꼴. `painfully slow`, `impossibly small` 처럼 "부사 + 형용사"로 정도와 결과를 함께 말한다. `that would create` 의 `would` 는 "그렇게 나누면"이라는 가정.
- 예문: Avoid repeated same-direction splits that would create unusably narrow columns or short rows.
- 유사어: too narrow to be useful (평이), impractically narrow (격식), cramped (구어, 답답한)
- 반의어: comfortably wide (넉넉히 넓은)

## "preserve unrelated working-tree changes"
- 레지스터: technical, professional
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 커밋할 때 내 작업과 무관한 수정은 건드리지 말라고 할 때(작업 계획·에이전트 지시).
- 한국어: 관련 없는 작업 트리 변경은 그대로 둔다
- 설명: `working tree` 는 아직 커밋하지 않은 파일 상태. 명사 앞에서 꾸밀 때는 하이픈을 넣어 `working-tree changes`. 앞 절 `Stage and commit only the files named in each task` 와 세미콜론으로 이어 "이것만 올리고 나머지는 보존"을 한 문장에 담았다.
- 예문: Stage and commit only the files named in each task; preserve unrelated working-tree changes.
- 유사어: leave other local changes untouched (평이), don't sweep up unrelated edits (구어), keep the rest of the tree as is (평이)
- 반의어: stage everything (전부 쓸어 담다), discard local changes (버리다)

## "parse every document before rendering any output"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: "전부 검증한 뒤에야 쓰기 시작한다"는 순서를 명세할 때(빌드·배치 설계).
- 한국어: 출력을 하나라도 만들기 전에 문서를 전부 파싱한다
- 설명: `every` 와 `any` 의 대비가 요점. "모든 문서를 먼저, 어떤 출력보다도 앞서"가 되어 파싱 오류가 하나라도 있으면 반쯤 쓰인 결과물이 남지 않는다. `before + -ing` 는 주어가 같을 때 쓰는 축약.
- 예문: `build_site()` must parse every document before rendering any output.
- 유사어: validate everything up front (구어), fail before writing anything (실패 시점 쪽), an all-or-nothing build (결과 쪽)
- 반의어: render as you go (읽는 대로 바로 출력하다)

## "aggregate every failure and raise one ValueError"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 첫 오류에서 멈추지 말고 다 모아 한 번에 보고하라고 할 때(검증기 설계).
- 한국어: 실패를 전부 모아 예외 하나로 올린다
- 설명: `aggregate` 는 흩어진 것을 한데 모으다. 짝을 이루는 말은 `every failure` 와 `one ValueError`. `listing source page and broken target` 은 `ValueError` 를 꾸미는 현재분사구로 예외에 무엇이 담기는지 말한다. 깨진 링크가 열 개여도 한 번 돌려 다 본다.
- 예문: `validate_local_references()` must aggregate every failure and raise one `ValueError` listing source page and broken target.
- 유사어: collect all errors and report them together (평이), batch up the failures (구어), accumulate errors (격식)
- 반의어: fail fast (첫 오류에서 멈추다), bail on the first error (구어)

## "If no final changes remain after validation, do not create an empty commit."
- 레지스터: professional, technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 절차의 마지막 단계에서 "할 게 없으면 하지 마라"를 명시할 때(작업 계획).
- 한국어: 검증 뒤에 남은 변경이 없으면 빈 커밋을 만들지 않는다
- 설명: 주어를 `no final changes` 로 잡아 부정을 앞에 세웠다. `If there are no changes left` 보다 문어답다. `remain` 은 "아직 남아 있다". 체크리스트를 기계처럼 따르다 의미 없는 커밋을 남기는 일을 막는 한 줄.
- 예문: If no final changes remain after validation, do not create an empty commit.
- 유사어: If there's nothing left to commit, skip the commit (구어), Commit only if something changed (평이)

## "Run the tests and verify they fail"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: TDD 에서 구현 전에 테스트가 실패하는지 먼저 확인하는 단계(작업 계획·TDD 절차).
- 한국어: 테스트를 돌려 실패하는지 확인한다
- 설명: 실패를 "확인"한다는 점이 눈에 띈다. 구현이 없는데도 통과하는 테스트는 아무것도 검증하지 않으므로 먼저 빨간불을 본다. `verify (that) they fail` 은 `that` 이 빠진 꼴. 계획서는 바로 아래에 `Expected: ERROR because build.py does not exist.` 로 실패 이유까지 적어 둔다.
- 예문: Run the tests and verify they fail.
- 유사어: watch it fail first (구어), confirm the test is red (TDD 용어), see the test fail for the right reason (이유까지 확인)
- 반의어: verify they pass (통과를 확인하다)

## "with a scroll-position fallback when unavailable"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 기능이 없는 환경에서 쓸 대체 수단을 한 구로 붙일 때(구현 명세).
- 한국어: 지원되지 않으면 스크롤 위치로 대신한다
- 설명: `when unavailable` 은 `when it is unavailable` 에서 주어와 be 동사를 뺀 축약. 명세와 문서에 흔하다(`if needed`, `when possible`, `where applicable`). `with a … fallback` 은 "대체 수단을 갖춘".
- 예문: Use `IntersectionObserver` for heading anchors, with a scroll-position fallback when unavailable. (작성)
- 유사어: falling back to scroll position if it isn't supported (풀어 쓴 말), degrading to scroll position (격식), or scroll position as a backup (구어)
- 반의어: with no fallback (대체 수단 없이)

## "changes and persists after reload"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 설정이 바뀌고 새로고침 뒤에도 유지되는지를 확인 항목으로 적을 때(검증 체크리스트).
- 한국어: 바뀌고 새로고침해도 유지된다
- 설명: `persist` 는 자동사로 "사라지지 않고 남다". 저장 방식(`localStorage`)은 말하지 않고 눈에 보이는 결과만 적었다. 동사 둘이 확인할 일 둘이다. 바뀌는가, 그리고 남는가.
- 예문: Verify at desktop width: light/dark theme changes and persists after reload.
- 유사어: survives a reload (구어), is remembered across reloads (수동), sticks after a refresh (구어)
- 반의어: resets on reload (새로고침하면 초기화된다)
