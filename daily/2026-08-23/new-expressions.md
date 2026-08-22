# 2026-08-23 — 새 표현

## "Existing drift elsewhere doesn't authorize a new instance."
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-skewvoir-verdict-block-review.md
- 맥락: 코드 리뷰에서 "다른 데도 이렇게 쓰던데요" 라는 반박을 미리 차단할 때(문어·격식). 지적 바로 뒤에 한 문장으로 붙인다.
- 한국어: 다른 데 이미 어긋난 게 있다고 해서 하나 더 만들 권한이 생기지는 않는다.
- 설명: `drift` 는 규칙에서 조금씩 벗어난 기존 코드를 가리킨다. `authorize` 가 핵심인데, 선례를 "허가"라는 법적 어휘로 받아서 "그건 허가가 아니라 부채"라는 뜻을 만든다. 사람을 탓하지 않고 논거만 무효로 만드는 문장이다.
- 예문: I know `text-(--sk-accent)` appears in three other components, but existing drift elsewhere doesn't authorize a new instance.
- 유사어: precedent isn't permission (더 짧고 경구에 가까움), that's a reason to fix those too, not to add a third (구어·설득조), two wrongs don't make a right (일상 회화, 코드 리뷰에는 다소 훈계조)
- 반의어: if that's already the house pattern, follow it

## "it's preservation, not invention"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: "이건 범위 초과 아니냐" 는 지적에 "새로 만든 게 아니라 원래 있던 걸 옮겨온 것" 이라고 답할 때(문어·리뷰 답변).
- 한국어: 새로 만든 게 아니라 (있던 걸) 보존한 것이다.
- 설명: `A, not B` 대구를 두 명사로만 세워 반박을 두 단어로 끝낸다. 리뷰어가 "invention"(없던 걸 지어냄)이라고 규정한 프레임을 그대로 받아 반대말 하나로 뒤집는 게 요령이다. 지운 파일에서 옮겨온 코드를 방어할 때 특히 잘 맞는다.
- 예문: The thumbnails came over from the deleted `StatBar.vue` untouched — it's preservation, not invention.
- 유사어: it was carried over, not added (더 평이하고 사실 위주), that predates this change (시점으로 방어), we inherited this (책임 소재를 앞 커밋으로 넘김)
- 반의어: that's net-new behavior

## "the docstring describes the old bug as the new behavior"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 코드는 고쳤는데 주석·문서만 안 고쳤을 때, 그 상태를 한 문장으로 진단하며(문어·리뷰).
- 한국어: docstring 이 옛날 버그를 새 동작이라고 설명하고 있다.
- 설명: "문서가 낡았다" 를 `describes A as B` 구문으로 바꿔 훨씬 아프게 만든다. 단순히 부정확한 게 아니라 **버그를 사양으로 승격시켜 놓았다**는 뜻이라, 다음 사람이 그 문서를 믿고 버그를 복원할 위험까지 함께 지목한다.
- 예문: We removed the fallback and fixed the tests, but the module docstring describes the old bug as the new behavior.
- 유사어: the comment predates the fix (사실만, 톤이 부드러움), the doc is stale (가장 흔하고 무난), the doc now states the opposite of the code (더 강한 대립 표현)
- 반의어: the docstring tracks the code

## "the fix is at the right altitude"
- 레지스터: technical, professional
- 출처: transcript:[assistant] (align-404 altitude review 결과)
- 맥락: 수정이 올바른 추상 층위에 놓였는지 판정할 때(설계 리뷰·문어). 보통 뒤에 "다만" 이 붙는다.
- 한국어: 수정이 (너무 낮지도 높지도 않은) 알맞은 층위에 있다.
- 설명: `altitude` 는 고도, 곧 추상 수준의 은유다. 호출부마다 땜질하면 too low, 안 그래도 되는 프레임워크를 만들면 too high. `at the right altitude, and it is incompletely applied` 처럼 층위 판정과 적용 범위 판정을 갈라 놓으면 "방향은 맞고 덜 퍼졌다" 를 정확히 말할 수 있다.
- 예문: The fix is at the right altitude, and it is incompletely applied — two of the three name-publishing sites still predate it.
- 유사어: it generalizes correctly (효과 쪽에 초점), the seam is in the right place (경계 은유), it's the right level of abstraction (가장 밋밋한 직역투)
- 반의어: it's a band-aid at the call site

## "a wall of 404s"
- 레지스터: technical, casual
- 출처: transcript:[assistant] (align-404 altitude review 결과)
- 맥락: 실패가 하나가 아니라 화면을 뒤덮는 규모임을 실감나게 말할 때(구어에 가까운 기술 서술).
- 한국어: 404 로 뒤덮인 화면.
- 설명: `a wall of ~` 는 "벽처럼 앞을 막는 양" 이라는 양·시각 은유로, `a wall of text`, `a wall of noise` 처럼 쓴다. 숫자 대신 이 표현을 쓰면 심각도를 사용자가 보는 화면 기준으로 전달한다.
- 예문: A listing hiccup silently converts a working screen into a wall of 404s.
- 유사어: a flood of 404s (양은 같고 시간 흐름 강조), every image on the screen breaks at once (은유 없이 직설), 404s across the board (범위 강조)
- 반의어: a clean load

## "Positives first:"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 리뷰·피드백을 시작하며 지적 전에 잘된 점을 먼저 묶어 말할 때(구어체에 가까운 업무 문어).
- 한국어: 좋은 점부터 말하면,
- 설명: 두 단어에 콜론만 붙인 헤더형 표현이라 문장을 만들 필요가 없다. 상대의 방어를 낮추는 장치인데, 뒤에 반드시 구체적 사실을 붙여야 형식적 칭찬으로 읽히지 않는다.
- 예문: Positives first: both providers now route through one function, and the docs and the mock changed together.
- 유사어: to start with what works (조금 더 부드럽고 길다), credit where it's due (칭찬을 명시적으로 인정하는 톤), let me lead with the good news (회화체)
- 반의어: I'll start with the problems

## "matches existing practice"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-skewvoir-verdict-block-review.md
- 맥락: 규칙을 문자 그대로 어긴 것처럼 보이지만 저장소 관행상 문제없다고 판정할 때(문어·격식).
- 한국어: 기존 관행과 맞는다.
- 설명: `practice` 는 문서에 적힌 규칙(rule)이 아니라 **실제로 굳어진 방식**을 가리킨다. 규칙과 관행이 어긋날 때 이 단어를 고르면 "규칙을 무시하자" 가 아니라 "이 저장소의 실제 기준은 이쪽" 이라는 뜻이 된다.
- 예문: Treating a 6px status dot as outside the `rounded-full` ban matches existing practice.
- 유사어: is consistent with how the repo already does it (풀어 쓴 평이한 판), follows precedent (더 격식·법률투), that's the house style (회화체)
- 반의어: is a departure from existing practice

## "Two files are in play."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] (.claude 설정 질문 답변)
- 맥락: 답을 시작하기 전에 관련된 대상이 몇 개인지 먼저 세워 줄 때(구어·업무 대화).
- 한국어: 관련된 파일은 둘입니다.
- 설명: `in play` 는 원래 스포츠에서 "공이 살아 있는 상태" 를 뜻하고, 일상 업무에서는 "지금 이 문제에 실제로 관여하는" 이라는 뜻으로 쓴다. `involved` 보다 가볍고 `at stake`(걸려 있다)보다 중립적이라, 설명 도입부에 부담 없이 쓴다.
- 예문: Two files are in play — a project-local one and your global one.
- 유사어: there are two files involved (가장 무난한 직역), two files feed into this (흐름 강조), we're looking at two files here (회화체)
- 반의어: only one file matters here

## "two sites I deliberately left alone"
- 레지스터: professional
- 출처: transcript:[assistant] (align-404 마무리 보고)
- 맥락: 알고도 안 고친 부분을 스스로 먼저 밝힐 때(문어·보고). 뒤에 이유가 따라온다.
- 한국어: 일부러 손대지 않은 두 곳.
- 설명: `deliberately` 하나가 "빠뜨린 것" 과 "남겨 둔 것" 을 가른다. 이 단어 없이 그냥 `two sites I didn't fix` 라고 하면 누락으로 읽힌다. 판단이었음을 밝힌 뒤 근거를 대는 게 세트다.
- 예문: The altitude review found the same defect at two sites I deliberately left alone, both written up in the spec.
- 유사어: intentionally out of scope (범위 문서에 기대는 격식체), I chose not to touch (주어를 드러내 책임을 명시), knowingly deferred (더 격식)
- 반의어: swept up while I was in there

## "can contradict its own guard"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-skewvoir-verdict-block-review.md
- 맥락: 조건문 안의 문장이 자기를 통과시킨 조건과 앞뒤가 안 맞는 결함을 지목할 때(문어·리뷰).
- 한국어: 자기를 통과시킨 가드와 모순될 수 있다.
- 설명: `guard` 는 그 분기로 들어가기 전 검사를 가리킨다. `its own` 이 결정적인데, 외부 값이 이상한 게 아니라 **같은 코드 안에서 앞뒤가 어긋난다**는 뜻이라 반박하기 어려운 형태의 지적이 된다.
- 예문: The σ-share clause can contradict its own guard: the guard admits only shares above 0.2, yet the sentence prints a negative percentage.
- 유사어: the branch disagrees with the condition that let it in (풀어 쓴 판), the invariant isn't actually held (더 격식·수학적), it's self-inconsistent (짧지만 근거가 약해 보임)
- 반의어: the guard fully constrains the branch

## "the change makes a documented claim wrong"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: diff 가 건드리지도 않은 줄인데 이번 변경 때문에 거짓이 된 문서를 지적할 때(문어·리뷰).
- 한국어: 이번 변경이 문서에 적힌 주장을 거짓으로 만든다.
- 설명: `make + 목적어 + 형용사` 사역 구문이라 주어(the change)에 책임이 자연스럽게 붙는다. "diff 밖이니 내 소관이 아니다" 라는 반론을 미리 막는 논법이며, 뒤에 `— and it was the claim the fix had to overturn` 처럼 한 겹 더 붙이면 왜 하필 그 문장인지까지 설명된다.
- 예문: The line is untouched by the diff, but the change makes a documented claim wrong.
- 유사어: it invalidates a documented promise (계약 어휘로 격상), that doc is now false (가장 짧고 단정적), the code and the doc now disagree (책임 소재 없이 상태만)
- 반의어: the docs still hold

## "one slot family over"
- 레지스터: technical, casual
- 출처: transcript:[assistant] (align-404 altitude review 결과)
- 맥락: 방금 고친 결함이 바로 옆 형제 구조에도 그대로 있다고 짚을 때(구어에 가까운 기술 서술).
- 한국어: 한 칸 옆 slot 계열에서.
- 설명: `one X over` 는 "한 칸 옆" 을 뜻하는 공간 표현으로, `one street over`, `one desk over` 처럼 쓴다. 기술 문서에서 이걸 코드 구조에 얹으면 "같은 결함이 이웃 모듈에 복제돼 있다" 를 짧고 생생하게 전달한다.
- 예문: That is the same blind spot that hid the align bug, one slot family over.
- 유사어: at the sibling site (중립·격식), next door (더 구어), in the neighbouring module (평이한 직역투)

## "I want evidence before making that trade."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] (align-404 마무리 보고)
- 맥락: 득실이 갈리는 수정을 지금 하지 않겠다고 밝힐 때(구어·업무 대화). 거절이 아니라 보류임을 못 박는다.
- 한국어: 그 맞바꿈을 하기 전에 근거가 있었으면 합니다.
- 설명: `trade` 가 "무언가를 얻고 무언가를 잃는 선택" 을 한 단어로 압축한다. `I don't want to` 대신 `I want evidence before` 를 쓰면 거부가 아니라 조건부 동의가 되어, 상대가 근거를 가져오면 진행된다는 문이 열려 있다.
- 예문: Dropping the fallback would cost CD-SEM users images that currently load — I want evidence before making that trade.
- 유사어: I'd need data first (더 짧고 직설), not without proof (단호하고 다소 거칠다), let's confirm it's live before we pay for it (근거 수집 방법까지 암시)
- 반의어: I'm comfortable making that call now

## "fetch a file it never checked existed"
- 레지스터: technical
- 출처: transcript:[assistant] (align-404 근본 원인)
- 맥락: 404 의 근본 원인을 한 문장으로 요약할 때(문어·보고).
- 한국어: 존재 여부를 확인한 적 없는 파일을 가져오게 시켰다.
- 설명: `checked existed` 는 `checked (that it) existed` 에서 that 이 빠진 형태로, 관계절 안에 또 절이 들어가 있어 처음엔 비문처럼 보인다. `never` 가 검사 자체가 없었음을 못 박아, 버그를 "이름을 잘못 만들었다" 가 아니라 "검증 단계가 통째로 빠져 있었다" 로 재정의한다.
- 예문: Every 404 meant the backend told the browser to fetch a file it never checked existed.
- 유사어: it published a name it never verified (더 격식·수동적), the filename was a guess (원인을 한 단어로), we advertised a path we hadn't confirmed (계약 어휘)
- 반의어: every name it publishes resolves 200

## "reuse over re-derivation"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-skewvoir-verdict-block-review.md
- 맥락: 이미 계산된 값을 다시 계산하지 않고 넘겨 쓰는 설계 원칙을 이름 붙여 부를 때(문어·설계).
- 한국어: 재계산 대신 재사용.
- 설명: `A over B` 는 "B 보다 A 를 택한다" 를 명사 둘로 압축한 원칙 표기법이다(`composition over inheritance` 와 같은 틀). 동명사 두 개를 대비시키면 문장 없이도 방침이 되고, 그대로 리뷰 체크리스트 항목이 된다.
- 예문: Reuse over re-derivation is documented and real here — the metrics come in as an argument instead of being recomputed.
- 유사어: compute it once and pass it down (실행 방법으로 풀어 쓴 판), single source of derivation (원천 강조), don't recompute what the caller already has (지시문형)
- 반의어: recompute at each call site

## "a thin route shell delegating to the view"
- 레지스터: technical
- 출처: transcript:[assistant] (뒤로가기 버튼 작업 insight)
- 맥락: 라우트 파일에 로직이 없고 화면 컴포넌트로 넘기기만 한다고 설명할 때(문어·구조 설명).
- 한국어: 뷰로 넘기기만 하는 얇은 라우트 껍데기.
- 설명: `thin` + `shell` 이 겹쳐 "내용이 없다" 를 두 번 말하고, `delegating to` 가 그 빈 껍데기가 하는 유일한 일을 지목한다. 이 구조를 밝히면 "그래서 이 수정은 라우트가 아니라 뷰에 들어가야 한다" 는 결론이 따라 나오므로, 위치를 정당화하는 문장으로 자주 쓴다.
- 예문: `measurement-rules.vue` is a thin route shell delegating to `EbeamMeasurementRulesView`, so the header lives in the view, not the page.
- 유사어: the page is just a wrapper (가장 평이), it's a pass-through (한 단어로 압축), the route holds no logic of its own (직설적 서술)
- 반의어: the page owns the layout itself
