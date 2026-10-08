# 2026-10-09 — 새 표현

> 오늘 배치는 repo 문서 7건과 transcript 17건이다. repo 문서는 skewnono_v3_nuxt 의 AFM 적재 명세·기능 요약·회신 기록·배포 문서인데 본문이 한국어이고 영어는 회신을 옮겨 적은 메모 몇 줄뿐이어서 표현 재료로 쓰지 않았다. transcript 다섯은 `/clear`·`/model`·`/login` 만 찍힌 빈 세션이고 하나는 작업 알림만 담겼다. 영어는 세 군데서 나왔다. AFM 상세 화면의 포인트 정렬을 고친 세션의 영어 보고(가장 많다), 그 세션에 딸려 온 `poteto-mode` 스킬 문서, 하위 에이전트에게 리뷰를 맡긴 지시문 둘. `browser-verify` 스킬 문서는 예전에 다 골라서 건너뛰었다. 노트에 이미 있어서 뺀 것: `I left it alone.`, `re-roll`, `this class of bug`, `earn its place`, `If nothing qualifies, output exactly (none).`, `layered on top of a shared mechanism`.

## "it is not the human's to answer"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 돌려 보면 알 일을 사람에게 묻지 말라고 선을 그을 때(작업 지침, 격식).
- 한국어: 그건 사람이 답할 몫이 아니다
- 설명: `be + 소유격 + to 부정사` 는 "~할 몫·권한이 누구에게 있다"를 말하는 틀이다(`It's not mine to decide`, `That's yours to keep`). 소유격 뒤에 명사가 없다는 점이 눈에 띈다. `the human's job` 이라고 쓰면 업무 분담처럼 들리는데 이 꼴은 "그 사람 소관이 아니다"에 가깝다.
- 예문: If the answer is a fact you could observe by running something, it is not the human's to answer.
- 유사어: that's not a question for the user (평이), it isn't the user's call (구어·결정권), it falls outside the user's remit (격식·영국식)
- 반의어: it's yours to decide (네가 정할 일이다)

## "Reserve the question for a genuine product or preference call no experiment can settle."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 질문은 실험으로 못 가리는 판단에만 쓰라고 범위를 좁힐 때(지침·규정, 격식).
- 한국어: 질문은 어떤 실험으로도 가릴 수 없는 제품·취향 판단을 위해 아껴 둘 것
- 설명: `reserve A for B` 는 "A 를 B 에만 쓰려고 남겨 둔다". `call` 은 여기서 전화가 아니라 판단·결정(`a judgment call`, `your call`). 뒤의 `no experiment can settle` 은 목적격 관계대명사를 뺀 관계절인데 부정어 `no` 가 주어에 붙어서 "어떤 실험도 ~못 한다"가 된다. `settle` 은 다툼이나 물음을 끝낸다는 동사.
- 예문: Reserve the question for a genuine product or preference call no experiment can settle.
- 유사어: Only ask when it's truly a matter of taste (평이), Save your questions for decisions that can't be tested (구어), Limit queries to matters of judgment (격식)
- 반의어: ask about everything up front (처음부터 다 물어보다)

## "let the result decide"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 의견으로 다투지 말고 해 본 결과에 맡기자고 할 때(회의·구어, 지침에도 쓴다).
- 한국어: 결과가 정하게 두다
- 설명: `let + 목적어 + 동사원형` 의 사역 구문. 사람이 아니라 `the result` 가 결정의 주어가 되어서 "내 취향이 아니라 증거가 고른다"는 태도가 실린다. 원문은 `Sketch it … and let the result decide.` 로 명령문 둘을 `and` 로 이었다.
- 예문: Sketch both layouts and let the result decide.
- 유사어: let the data speak for itself (데이터가 말하게, 조금 상투적), go with whatever the test shows (구어), defer to the evidence (격식)
- 반의어: go with your gut (감으로 정하다)

## "assess each on its merits"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 자동 리뷰 지적이나 제안을 뭉뚱그려 받지도 버리지도 말고 하나씩 따지라고 할 때(리뷰·심사, 격식).
- 한국어: 하나하나를 그 자체의 타당성으로 따져 보다
- 설명: `on its merits` 는 법률에서 온 말로 "절차나 출처가 아니라 내용 자체로". 누가 한 말인지, 몇 번째 지적인지는 치우고 그 건이 옳은지만 본다. 원문은 `They catch real bugs and also file non-issues and nitpicks, so assess each on its merits` 로 이유를 먼저 댄다.
- 예문: The bots also file non-issues and nitpicks, so assess each on its merits.
- 유사어: judge each one on its own (평이), take them case by case (구어), evaluate each individually (격식·건조)
- 반의어: accept them wholesale (통째로 받아들이다), dismiss them out of hand (따져 보지도 않고 물리치다)

## "dismiss noise with a concrete reason instead of churning code"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 근거 없는 리뷰 지적 때문에 코드를 이리저리 고치지 말라고 할 때(코드 리뷰 지침).
- 한국어: 잡음은 구체적인 이유를 대고 물리치되 코드를 괜히 뒤집지 말 것
- 설명: `churn` 은 원래 버터를 만들려고 우유를 휘젓는 동작. 코드에 쓰면 "나아지는 것 없이 자꾸 바뀐다"는 뜻이 된다(`code churn`). `noise` 는 신호가 아닌 것, 여기서는 실익 없는 지적. `with a concrete reason` 이 붙어서 그냥 무시하는 것과 갈린다.
- 예문: Dismiss noise with a concrete reason instead of churning code.
- 유사어: don't rewrite code just to quiet a reviewer (평이), push back with specifics rather than thrash the code (구어·개발자)
- 반의어: address every comment (모든 지적을 반영하다)

## "candor over sycophancy"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 듣기 좋은 말보다 솔직한 판단을 앞세우겠다고 원칙을 적을 때(가치 선언, 문어).
- 한국어: 아첨보다 솔직함
- 설명: `A over B` 는 "B 보다 A 를 고른다"는 가치 선언의 틀(`clarity over cleverness`). `candor` 는 불편해도 숨기지 않는 솔직함이고 `sycophancy` 는 윗사람 비위를 맞추는 아첨. 원문에서는 `Agreement is not the default,` 뒤에 쉼표로 붙어 표어처럼 닫는다.
- 예문: Agreement is not the default, candor over sycophancy.
- 유사어: honesty over flattery (평이), straight talk, not yes-man answers (구어), frankness rather than deference (격식)
- 반의어: telling people what they want to hear (듣고 싶은 말만 해 주기)

## "Terse is not an excuse to drop content."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 짧게 쓰라는 규칙이 내용을 빼도 된다는 뜻은 아니라고 못 박을 때(글쓰기 지침).
- 한국어: 간결하게 쓴다는 것이 내용을 빼도 된다는 핑계는 아니다
- 설명: 형용사 `Terse` 가 그대로 주어 자리에 섰다(`Being terse` 의 줄임). `an excuse to + 동사` 는 "~해도 되는 구실". `terse` 는 `concise` 보다 한 발 더 나가 퉁명스러울 만큼 짧다는 뜻이라 여기서 일부러 골랐다. 바로 뒤가 `Short sentences, but every section … stays` 로 받는다.
- 예문: Terse is not an excuse to drop content.
- 유사어: Short doesn't mean incomplete (평이), Keep it brief, but don't leave anything out (구어), Brevity must not come at the expense of completeness (격식)

## "Never hand the human a check you could run."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: "이거 확인해 보세요"로 일을 넘기지 말라고 할 때(보고 지침, 격식).
- 한국어: 네가 돌려 볼 수 있는 확인을 사람에게 떠넘기지 말 것
- 설명: `hand A B` 는 "A 에게 B 를 건네다"의 4형식. `a check` 는 수표가 아니라 확인 작업. `you could run` 의 `could` 는 가정이 아니라 "마음만 먹으면 할 수 있는"이라는 능력이고 관계대명사가 빠졌다. 금지문이지만 뒤집으면 "확인은 끝내고 결과만 건넨다"는 보고 원칙이 된다.
- 예문: Never hand the human a check you could run.
- 유사어: Don't ask the user to verify what you can verify yourself (평이), Don't punt the testing to them (구어), Do not delegate verification you are able to perform (격식)

## "The deliverable is a diagnosis, not a fix."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 이번 일의 결과물이 수정이 아니라 원인 진단까지라고 범위를 정할 때(작업 정의, 격식).
- 한국어: 결과물은 진단이지 수정이 아니다
- 설명: `deliverable` 은 형용사처럼 생겼지만 명사로 "넘겨줘야 할 결과물". `A, not B` 로 범위의 안쪽과 바깥쪽을 한 문장에 가른다. 일을 맡길 때 이 한 줄이 있으면 받는 쪽이 고치려 들지 않는다.
- 예문: The deliverable is a diagnosis, not a fix.
- 유사어: I just need the root cause, not a patch (구어), The expected output is an analysis rather than a remedy (격식), Diagnose only; don't fix (메모체)

## "Make illegal states unrepresentable"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 poteto-mode 스킬 문서)
- 맥락: 잘못된 상태를 검사로 막지 말고 타입 설계로 아예 못 만들게 하라고 할 때(타입 설계 원칙).
- 한국어: 있어서는 안 될 상태를 표현 자체가 불가능하게 만들 것
- 설명: `make + 목적어 + 형용사` 의 5형식. `illegal` 은 법이 아니라 규칙에 어긋난다는 뜻이고 `unrepresentable` 은 "타입으로 적을 수조차 없는". Yaron Minsky 가 한 말로 타입 언어 쪽에서는 표어처럼 통한다. 원문에서는 `brand primitives`, `parse external data at boundaries` 와 나란히 나온다.
- 예문: Make illegal states unrepresentable, and parse external data at boundaries.
- 유사어: encode the invariant in the type (같은 뜻, 더 구체적), rule it out at compile time (구어), don't validate what you can prevent (대구형)
- 반의어: check for bad states at runtime (실행 중에 잘못된 상태를 검사하다)

## "sits at the right depth instead of patching a symptom"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (altitude 리뷰를 맡긴 지시문)
- 맥락: 수정이 원인이 있는 층에서 이뤄졌는지 봐 달라고 리뷰어에게 관점을 줄 때(리뷰 지시문).
- 한국어: 증상을 땜질하지 않고 알맞은 깊이에 놓여 있다
- 설명: `sit at` 은 변경이 놓인 위치를 말한다. 코드를 층으로 보고 "어느 층에서 고쳤나"를 묻는 표현이다. `patch a symptom` 은 원인은 두고 겉으로 드러난 증상만 덧대는 것. `instead of + 동명사` 로 둘을 맞세웠다. 노트에 있는 `cut at the right depth` 가 리뷰 결과를 말한다면 이쪽은 리뷰를 맡기는 물음이다.
- 예문: Check that each change sits at the right depth instead of patching a symptom.
- 유사어: fixes the cause, not the symptom (평이), goes to the root rather than papering over it (구어), is applied at the appropriate layer (격식)
- 반의어: a band-aid fix (임시 땜질)

## "Do not pad; "leave it" is a valid answer."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (altitude 리뷰를 맡긴 지시문)
- 맥락: 지적할 것이 없으면 없다고 답해도 된다고 미리 허락할 때(리뷰·조사 지시문).
- 한국어: 분량을 부풀리지 말 것. "그대로 두라"도 유효한 답이다
- 설명: `pad` 는 솜을 채워 넣듯 글이나 목록을 쓸데없이 늘린다는 자동사. 세미콜론 뒤는 인용구 `"leave it"` 이 통째로 주어가 된 문장이다. 리뷰를 맡길 때 이 말이 없으면 받는 쪽이 뭐라도 찾아내려고 약한 지적을 끼워 넣는다.
- 예문: Do not pad; "leave it" is a valid answer.
- 유사어: Don't invent findings just to fill the list (평이), "Nothing to change" is fine (구어), An empty result is acceptable (격식)

## "Reproducing the order against the running mock before touching anything."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 고치기 전에 증상부터 눈으로 본다고 한 줄로 알릴 때(작업 중 진행 보고, 메모체).
- 한국어: 손대기 전에 돌고 있는 mock 을 상대로 그 순서를 재현하는 중
- 설명: 주어와 be 동사를 뺀 `-ing` 한 문장(`I am` 생략)이 진행 보고의 기본 꼴이다. `reproduce … against X` 의 `against` 는 맞선다는 뜻이 아니라 "X 를 대상으로 돌려 본다"(`run the tests against staging`). `before touching anything` 이 순서를 못 박는다.
- 예문: Reproducing the order against the running mock before touching anything.
- 유사어: Let me see the bug first before I change anything (구어), Confirming the repro before making changes (메모체)

## "Main moved while I worked"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 내가 작업하는 동안 다른 커밋이 main 에 들어왔다고 알릴 때(git 작업 중, 구어·메모).
- 한국어: 내가 작업하는 사이에 main 이 앞으로 나갔다
- 설명: 브랜치가 `move` 한다는 말은 새 커밋이 붙어 끝이 옮겨 갔다는 뜻. `while I worked` 는 단순과거로 "그동안"을 말한다. 원문은 괄호로 원인을 붙이고(`another session's docs commit`) 다음 문장 `Rebasing my two commits onto it.` 으로 대응을 잇는다. 탓하는 말이 없다는 점을 본다.
- 예문: Main moved while I worked, so I am rebasing my two commits onto it.
- 유사어: main got ahead of me (구어), my branch fell behind main (주어를 내 브랜치로), upstream has new commits (건조)

## "rendered them as received"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 받은 데이터를 가공 없이 그 순서대로 그렸다고 원인을 설명할 때(버그 보고, 문어).
- 한국어: 받은 그대로 그렸다
- 설명: `as received` 는 `as they were received` 의 줄임. `as + 과거분사` 꼴(`as written`, `as pasted`)이 "그 상태 그대로"를 맡는다. 원문 문장은 `The office returns … in stored order, and the page rendered them as received.` 인데 앞 절은 늘 그렇다는 현재형, 뒤 절은 고치기 전의 일이라 과거형이다.
- 예문: The office returns rows in stored order, and the page rendered them as received.
- 유사어: showed them in whatever order they came in (구어), displayed them unsorted (평이), passed them through unchanged (기술)
- 반의어: sorted them on arrival (받자마자 정렬했다)

## "so this never showed at home"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 왜 지금까지 버그를 못 봤는지 한 문장으로 설명할 때(버그 보고, 구어에 가까운 문어).
- 한국어: 그래서 집에서는 이게 한 번도 드러나지 않았다
- 설명: `show` 를 목적어 없이 쓰면 "눈에 띄다, 드러나다"(`It doesn't show`). `show up` 과 거의 같고 조금 더 짧다. `never` + 단순과거는 "그 기간 내내 한 번도". 앞 절 `The home mock already returns point order` 가 원인이고 `so` 가 결과를 잇는다.
- 예문: The home mock already returns point order, so this never showed at home.
- 유사어: so we never saw it locally (주어를 사람으로), so it never surfaced in dev (조금 격식), so it went unnoticed at home (수동적 뉘앙스)
- 반의어: it showed up right away (바로 드러났다)

## "where the payload enters the page, so every card inherits the order"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 정렬이나 정규화를 입구 한 곳에서만 하고 아래는 그대로 물려받게 했다고 설명할 때(설계 설명).
- 한국어: 데이터가 페이지로 들어오는 자리에서 (한 번 정렬해) 모든 카드가 그 순서를 물려받게
- 설명: `where` 절이 장소 부사절로 "어디서 정렬하나"를 말한다. `payload` 는 응답에 실려 온 본문 데이터, `enter` 는 경계를 넘는 순간. `inherit` 는 상속 문법이 아니라 "위에서 정한 것을 아래가 그대로 받는다"는 비유다. 원문에는 `once` 가 있어서 "한 번만"이 강조된다.
- 예문: The page sorts the data once where the payload enters the page, so every card inherits the order.
- 유사어: sorts at the boundary so nothing downstream has to (기술), sorts it up front and everything below just uses it (구어)
- 반의어: each card sorts its own copy (카드마다 따로 정렬한다)

## "The sort is stable"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 정렬을 넣어도 같은 키끼리의 원래 순서는 안 바뀐다고 보증할 때(변경 설명).
- 한국어: 이 정렬은 안정 정렬이다
- 설명: `stable` 은 "튼튼하다"가 아니라 정렬 용어로 "키가 같은 원소끼리는 들어온 순서를 지킨다". 원문은 `so a repeat recipe's 회차 numbering is unchanged` 로 그 성질이 사용자에게 무슨 뜻인지 바로 풀어 준다. 용어 하나, 결과 하나를 `so` 로 잇는 짜임을 그대로 가져다 쓸 만하다.
- 예문: The sort is stable, so the lap numbering of a repeated recipe is unchanged.
- 유사어: ties keep their original order (풀어 쓴 말), equal keys stay in input order (기술)
- 반의어: an unstable sort (불안정 정렬)

## "a throwaway Flask and Nuxt pair"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 확인만 하고 버릴 임시 서버를 띄웠다고 말할 때(검증 방법 설명).
- 한국어: 쓰고 버릴 Flask·Nuxt 한 쌍
- 설명: `throwaway` 는 명사 앞에서 "한 번 쓰고 버리는"(`a throwaway script`, `a throwaway branch`). `pair` 가 백엔드와 프런트를 한 묶음으로 센다. 원문은 `with the API order reversed` 를 붙여(`with + 목적어 + 과거분사`) 어떤 조건으로 돌렸는지까지 한 문장에 담았다.
- 예문: I ran a throwaway Flask and Nuxt pair with the API order reversed and read the rendered page.
- 유사어: a scratch server (기술·구어), a temporary dev setup (평이), a disposable instance (격식)
- 반의어: the normal dev servers (평소 쓰는 개발 서버)

## "I am holding the merge to `main` until the review comes back."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 할 수 있는데도 일부러 멈춰 두고 있다고 알릴 때(진행 보고, 문어).
- 한국어: 리뷰 결과가 돌아올 때까지 `main` 병합은 잡아 두고 있습니다
- 설명: `hold` 는 "안 한다"가 아니라 "할 준비는 됐는데 붙들고 있다". 현재진행형이 "지금 이 상태"를 말한다. `until the review comes back` 은 미래 일이지만 시간 부사절이라 현재형이고 `come back` 은 보낸 것이 결과를 들고 돌아온다는 그림이다.
- 예문: I am holding the merge to `main` until the review comes back.
- 유사어: I'll merge once the review is in (구어), The merge is pending review (건조·수동), I'm waiting on the review before I merge (평이)
- 반의어: I went ahead and merged (기다리지 않고 병합했다)

## "predates the final zip-test fix"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 보고하는 테스트 결과가 마지막 수정보다 앞선 것이라고 밝힐 때(검증 보고, 문어).
- 한국어: 마지막 zip 테스트 수정보다 앞선 것이다
- 설명: `predate` 는 "~보다 날짜가 앞서다"는 타동사로 전치사 없이 목적어를 바로 받는다. 원문은 `The one full-suite run (3935 passed, 1 failed) predates the final zip-test fix. After it I reran only the AFM tests.` 실패 1건이 왜 남아 있는지, 그 뒤에 무엇을 다시 돌렸는지를 숨기지 않고 적는 문장이다.
- 예문: The one full-suite run predates the final zip-test fix.
- 유사어: was from before the last fix (구어), was taken prior to the final fix (격식), is stale relative to the last commit (기술)
- 반의어: postdates the fix (수정보다 뒤의 것이다)

## "I left the route alone and relaxed the test."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 코드와 테스트가 어긋났을 때 테스트 쪽 기준을 풀었다고 밝힐 때(변경 보고).
- 한국어: 라우트는 그대로 두고 테스트 쪽을 느슨하게 했습니다
- 설명: `relax a test` 는 단언을 덜 엄격하게 바꾼다는 뜻(`relax a constraint`, `relax the check`). 여기서는 순서까지 비교하던 것을 이름만 비교하게 푼 일이다. `leave A alone` 과 짝을 지어 "무엇을 건드리지 않았고 무엇을 바꿨나"를 한 문장에 넣었다. 테스트를 푼 사실은 숨기기 쉬운 것이라 따로 적는 편이 믿음직하다.
- 예문: I left the route alone and relaxed the test.
- 유사어: I loosened the assertion instead of changing the code (풀어 쓴 말), I made the test less strict (평이)
- 반의어: tightened the test (테스트를 더 엄격하게 했다)

## "Treat it as "nothing obvious", not as a deep read."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 통과한 검토가 얕았으니 그만큼만 믿으라고 알릴 때(리뷰 결과 보고, 문어).
- 한국어: "눈에 띄는 문제는 없다" 정도로 받아들이고 깊이 읽은 결과로 보지는 말 것
- 설명: `treat A as B, not as C` 로 결과를 어느 무게로 읽을지 정해 준다. 바로 앞 문장이 `It was a thin pass: one tool call in about 14 seconds.` 인데 `thin` 이 "얇은, 건성인"을 맡고 콜론 뒤에 근거 수치가 온다. "문제 없음"이라는 보고에 그 보고의 한계를 같이 붙이는 법이다.
- 예문: The review found nothing, but treat it as "nothing obvious", not as a deep read.
- 유사어: It's a quick sanity check, not a full review (구어), Read it as a smoke test (기술), This should not be taken as a thorough audit (격식)
- 반의어: a line-by-line review (한 줄씩 본 검토)

## "did not land on disk"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 저장했다고 생각한 파일이 실제로는 남지 않았다고 말할 때(검증의 한계 보고).
- 한국어: 디스크에 남지 않았다
- 설명: `land` 는 "도착해서 자리를 잡다". 코드가 `land on main` 하듯 파일은 `land on disk` 한다. 원문은 `The two screenshots I tried to save did not land on disk, so there is no image evidence.` 로 `I tried to save` 가 시도였음을, `so` 뒤가 그 결과로 빠진 증거를 말한다.
- 예문: The two screenshots I tried to save did not land on disk, so there is no image evidence.
- 유사어: never got written (구어), weren't saved (평이), failed to persist (격식·기술)

## "The check left one thing behind"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 확인 작업이 환경에 남긴 흔적을 스스로 알릴 때(검증 보고, 문어).
- 한국어: 이번 확인이 흔적 하나를 남겼습니다
- 설명: `leave A behind` 는 떠나면서 뒤에 남긴다는 뜻. 주어가 `I` 가 아니라 `The check` 여서 변명 없이 사실만 전한다. 콜론 뒤에 무엇이 어디에 남았는지를 적고 다음 문장 `Your own browser's group is untouched.` 로 영향이 닿지 않은 범위를 긋는다.
- 예문: The check left one thing behind: three grouped measurements in the automation browser's profile.
- 유사어: One side effect to mention (구어), The test did leave some state around (구어·기술), One artifact remains from the verification (격식)
- 반의어: cleaned up after itself (뒷정리까지 했다)

## "If you would prefer it last, say so."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 내가 고른 기본값을 알리고 반대쪽을 원하면 말하라고 문을 열어 둘 때(보고의 끝, 정중한 구어).
- 한국어: 맨 뒤에 두는 편이 좋으면 말씀해 주세요
- 설명: `prefer + 목적어 + 보어` 로 "그것이 ~한 상태이기를 더 바란다". `last` 가 부사 한 낱말로 위치를 맡는다. `would prefer` 는 `want` 보다 한 단계 공손하고 `say so` 의 `so` 는 앞 절 전체를 받는다. 앞 문장이 현재 동작(`so it sorts first, ahead of 0001`)을 먼저 알려 준다.
- 예문: The image belongs to no point, so it sorts first; if you would prefer it last, say so.
- 유사어: Let me know if you'd rather have it at the end (평이), Happy to move it to the end if you like (구어), Should you prefer it last, I can change it (격식)

## "Nothing to re-copy."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (AFM 상세 화면 정렬 수정 보고)
- 맥락: 상대가 해야 할 뒷일이 없다고 짧게 알릴 때(보고의 끝, 구어·메모).
- 한국어: 다시 복사할 것은 없습니다
- 설명: `There is` 를 뺀 조각문. `Nothing to + 동사` 는 "~할 것이 없다"를 두세 낱말로 끝낸다(`Nothing to add`, `Nothing to worry about`). 원문은 소제목 `For the office.` 바로 뒤에 놓였고 이어서 `The fix is frontend-only` 가 이유를 댄다.
- 예문: Nothing to re-copy; the fix is frontend-only.
- 유사어: No need to copy anything again (평이), You don't have to redo the copy (구어), No further action is required on your side (격식)
