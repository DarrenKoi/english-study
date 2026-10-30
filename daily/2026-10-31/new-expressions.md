# 2026-10-31 — 새 표현

오늘 repo 문서 10개는 거의 다 한국어라 쓸 만한 영어가 적었다. 표현은 대부분 SKEWNONO 세션 트랜스크립트에서 골랐다. 어시스턴트가 AFM 엔드포인트 작업을 보고한 글과 사용자가 붙여 넣은 poteto-mode 스킬 본문이다. 이전 날짜에 이미 수집한 스킬 문구(candor over sycophancy, earn its place 등)는 뺐다.

## "(one thing users) would trip on"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 사용자나 동료가 걸려 넘어질 함정을 미리 짚을 때(보고·구어 모두)
- 한국어: (사용자들이) 걸려 넘어질 만한 것
- 설명: trip on 은 '~에 발이 걸리다'. 비유로 '~ 때문에 실수하다'가 된다. would 를 붙이면 "아직 일어나진 않았지만 그대로 두면 그럴 것"이라는 예측이 된다. 원문은 이 구로 콜론 앞을 열고 뒤에 함정(`#` 가 들어간 파일명)을 댔다.
- 예문: One thing users would trip on: AFM filenames contain `#`, so a script must percent-encode them in the URL path.
- 유사어: trip up (타동사형, "This trips users up"), a gotcha (구어, 함정 자체를 가리키는 명사), a common pitfall (문어)
- 반의어: work out of the box (아무 함정 없이 바로 동작)

## "The real gap is that ..."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 요청받은 것과 실제로 비어 있는 것이 다를 때 진짜 문제를 짚어 줄 때(보고·회의)
- 한국어: 진짜 빠져 있는 건 ~이다
- 설명: 요청은 "엔드포인트를 만들어 달라"였지만 엔드포인트는 이미 있었다. 빠진 것은 문서였다. real 이 "겉으로 보이는 것 말고"라는 대비를 만든다. 앞 문장에서 요청의 전제를 깨고 이 문장으로 진짜 할 일을 세우는 순서가 자연스럽다.
- 예문: The real gap is that the `/endpoints` reference page has no AFM section, so users cannot discover the endpoints or copy a working snippet.
- 유사어: What's actually missing is ... (구어), The underlying issue is ... (문어, 원인 쪽에 무게)
- 반의어: That's already covered. (빈 데가 없음)

## "Both are true but read as a contradiction."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 두 문장이 각각 맞는데 나란히 놓이면 독자가 헷갈릴 때(리뷰·문서 피드백)
- 한국어: 둘 다 사실이지만 서로 모순처럼 읽힌다
- 설명: read 가 자동사로 '~하게 읽히다'. read as 는 "실제로 그렇다는 게 아니라 독자에게 그렇게 보인다"는 뜻이라 사실과 인상을 갈라 준다. 상대 문서를 고쳐 달라고 할 때 공격적으로 들리지 않는다.
- 예문: The general note says the API is rate-limited and the AFM group says AFM is exempt; both are true but read as a contradiction. (작성)
- 유사어: come across as contradictory (구어), appear inconsistent (문어)
- 반의어: read consistently (일관되게 읽히다)

## "Say so if you want it reworded"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 일부러 손대지 않은 부분을 알리면서 원하면 바꾸겠다고 제안할 때(보고 마무리·구어)
- 한국어: 고쳐 쓰길 원하시면 말씀해 주세요
- 설명: `want + 목적어 + 과거분사` 구조다. "그것이 고쳐진 상태를 원한다"로, 누가 고칠지는 숨긴다. say so 는 "그렇다고 말해 달라"는 짧은 구어 청유다. 결정권을 상대에게 넘기면서 기본값(그대로 둠)을 분명히 한다.
- 예문: I left the general note alone. Say so if you want it reworded to name the exempt features.
- 유사어: Let me know if you'd like it changed (더 공손), Happy to reword it if you prefer (구어, 친근)

## "in case you pick it up later"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 중단한 작업을 버리지 않고 보관해 둔 이유를 말할 때(구어·작업 보고)
- 한국어: 나중에 다시 이어서 할 경우를 대비해
- 설명: pick up 은 '멈췄던 일을 다시 집어 들다'. in case 뒤에는 현재형을 쓴다(미래 일이라도 will 을 넣지 않는다). 대비책을 마련했다는 뉘앙스다.
- 예문: I'm removing the worktree and keeping the diff as a patch in case you pick it up later.
- 유사어: in case you come back to it (구어), should you resume it later (문어, 도치 조건)
- 반의어: for good (영영, 완전히 버림)

## "(the server) behaves exactly as before"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 되돌린 뒤 아무것도 바뀌지 않았음을 확인해 줄 때(작업 보고)
- 한국어: (서버가) 전과 똑같이 동작한다
- 설명: as before 는 '이전처럼'. exactly 가 "조금도 다르지 않다"를 못 박는다. 원문은 앞에 "변경이 main 에 없다"를 대고 이 구로 결과를 확인했다. 원인(커밋 없음)과 결과(동작 불변)를 나눠 말하는 습관이 보인다.
- 예문: The rate-limit change is not on `main` and the server behaves exactly as before.
- 유사어: is unchanged (짧고 건조), works the same as it did (구어)
- 반의어: behaves differently now

## "turned X into Y"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 어떤 원칙이 과제를 다른 과제로 바꿔 놓았음을 설명할 때(설계 근거·회고)
- 한국어: X 를 Y 로 바꿔 놓았다
- 설명: 주어 자리에 사람이 아니라 원칙(Laziness Protocol)이 왔다. 무생물 주어 + turn A into B 는 "그 원칙 때문에 일이 이렇게 바뀌었다"를 한 문장에 담는 영어다운 구조다. 따옴표로 과제 이름을 그대로 넣어 대비를 선명하게 했다.
- 예문: Laziness Protocol turned "create endpoints" into "document the ones that exist".
- 유사어: reframed X as Y (문어, 관점 전환 강조), changed the ask from X to Y (구어)

## "(the endpoints) are exempt from the rate limit"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant] / subagent report
- 맥락: 규칙의 적용 대상에서 빠져 있음을 말할 때(기술 문서·정책)
- 한국어: 요청 제한에서 면제된다
- 설명: exempt 는 형용사로 `be exempt from`. 세금·의무 면제에서 온 말이라 규칙이 원래 모두에게 걸린다는 전제가 깔린다. 목록 이름은 exempt list, 동사로는 exempt X from Y.
- 예문: The `afm` blueprint is exempt from the rate limit, so the description says so.
- 유사어: excluded from (중립), not subject to (문어, 법률 느낌), bypasses (구어, 우회 느낌)
- 반의어: subject to the rate limit (제한을 받다)

## "has no design fork"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 설계 검토 단계를 건너뛴 이유를 댈 때(작업 보고)
- 한국어: 설계상 갈림길이 없다
- 설명: fork 는 길이 둘로 갈라지는 지점. 두 가지 이상 그럴듯한 설계가 있어야 비교 검토가 의미가 있다. 원문은 "데이터 항목만 추가하는 변경이라 갈림길이 없어서 how·architect 를 건너뛰었다"고 썼다.
- 예문: I skipped `how` and `architect` because the change adds data entries to an existing typed catalog and has no design fork.
- 유사어: there's only one sensible way to do it (구어), no competing designs (문어)
- 반의어: a contested design (여러 설계가 맞서는 상태)

## "checked by DOM only, not by eye"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 검증을 어디까지 했는지 범위를 정직하게 밝힐 때(QA 보고)
- 한국어: DOM 으로만 확인했고 눈으로는 확인 안 했다
- 설명: `by + 무관사 명사`(by hand, by eye)는 수단을 말한다. only 와 `not by eye` 가 검증의 빈틈을 스스로 드러낸다. 스크린샷 저장이 실패해서 레이아웃은 눈으로 못 봤다는 맥락이다.
- 예문: The screenshot did not save, so layout is checked by DOM only, not by eye.
- 유사어: verified programmatically, not visually (문어), I didn't actually eyeball it (구어)

## "(the behaviour) is inferred from the shared route code"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 직접 실행해 보지 못한 환경의 동작을 추론으로 말할 때(보고서의 근거 표시)
- 한국어: (동작은) 공유 라우트 코드에서 추론한 것이다
- 설명: 앞 문장 "Nothing was run against the office adapter." 와 짝이다. 실측과 추론을 문장 단위로 갈라 독자가 근거의 무게를 알게 한다. 수동태라 "누가 추론했나"보다 "근거가 무엇인가"에 초점이 간다.
- 예문: Nothing was run against the office adapter. The office behaviour is inferred from the shared route code.
- 유사어: is assumed based on (더 약한 근거), follows from (논리적 귀결)
- 반의어: was measured / observed directly

## "It is illustrative, like X elsewhere on the page"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 예시 값이 실제로 존재하지 않을 수 있다고 미리 알려 줄 때(문서·리뷰)
- 한국어: 예시용일 뿐이다, 이 페이지의 다른 X 처럼
- 설명: illustrative 는 '설명을 위한, 예시용'. like X elsewhere on the page 로 이미 있는 관례에 기대면 "왜 진짜 값을 안 썼나"라는 질문을 미리 막는다. 뒤에 "and will not exist on the office server" 로 한계를 덧붙였다.
- 예문: It is illustrative, like `MSR_001` elsewhere on the page, and will not exist on the office server.
- 유사어: just a placeholder (구어), for illustration only (문어)
- 반의어: a real, existing file

## "want X precomputed"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant]
- 맥락: 상대가 원할 수 있는 다른 결과를 조건으로 걸고, 그건 별도 작업이라고 선을 그을 때(범위 협의)
- 한국어: X 가 미리 계산돼 있기를 원하다
- 설명: `want + 목적어 + 과거분사`. 뒤에 "that is a real new endpoint and a separate task" 를 붙여 범위를 분명히 나눴다. a separate task 는 "지금 요청에 몰래 끼워 넣지 않겠다"는 뜻이라 범위 관리에 쓰기 좋다.
- 예문: If users want the tips or usage numbers precomputed instead of deriving them from the rows, that is a real new endpoint and a separate task.
- 유사어: have X calculated in advance (풀어쓴 구어), out of scope for now (범위 밖)

## "Where your brief was off"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 subagent report
- 맥락: 받은 지시서에서 사실과 다른 부분을 정리해 돌려줄 때(보고서 소제목)
- 한국어: 지시서가 틀렸던 부분
- 설명: brief 는 '작업 지시서'. off 는 형용사로 '빗나간, 맞지 않는'. wrong 보다 부드럽고, 조금 어긋났다는 느낌이다. 소제목으로 쓰면 지적이 감정이 아니라 사실 목록이라는 신호가 된다.
- 예문: Where your brief was off: the base note says the API is rate-limited, but this group is exempt. (작성)
- 유사어: Corrections to the brief (문어, 중립), Where the brief didn't match the code (구체적)
- 반의어: as you described (지시서와 일치)

## "the same prompt against a different model"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 교차 검증 방법을 한 문장으로 정의할 때(AI 작업 절차·기술 문서)
- 한국어: 같은 프롬프트를 다른 모델에 돌리는 것
- 설명: run X against Y 는 'Y 를 대상으로 X 를 실행하다'. 동사를 생략해도 against 하나로 그 뜻이 산다. "A second opinion is ..." 로 정의문을 만들어 두 번째 의견이 무엇인지 못 박는다.
- 예문: A second opinion is the same prompt against a different model.
- 유사어: cross-check with another model (구어), an independent replication (문어)

## "Agreement is high-signal."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 독립된 두 판단이 일치할 때 그 결과를 더 믿을 근거가 된다고 말할 때(검토·의사결정)
- 한국어: (독립된 판단끼리) 일치하면 신뢰도가 높다
- 설명: signal 은 잡음(noise)과 대비되는 '의미 있는 정보'. high-signal 은 하이픈으로 묶은 형용사다. 짧은 단언문 하나로 원칙을 세운다.
- 예문: Run the review on two models; agreement is high-signal. (작성)
- 유사어: is a strong indicator (문어), means a lot (구어)
- 반의어: low-signal / noise (의미 없는 정보)

## "with consolidated scope"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 흩어진 지시를 한데 모아 새 담당자에게 넘길 때(업무 인계)
- 한국어: 범위를 한데 모아 정리한 상태로
- 설명: consolidate 는 '흩어진 것을 하나로 합치다'. 원문은 바로 뒤에 meaning 으로 범위의 구성(원래 지시서, 이후 지시, 이전 보고와 브랜치)을 풀었다. 추상어 뒤에 meaning 으로 내용을 대는 방식이 정의할 때 쓸모 있다.
- 예문: Give new work to a fresh subagent with consolidated scope, meaning the original brief, every later directive, and the prior agent's report and branch.
- 유사어: with the full context bundled (구어), with a complete handover (인계 강조)
- 반의어: piecemeal (조각조각)

## "only when the new work strictly needs ..."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 예외를 아주 좁게 허용할 때(규칙·지침 문서)
- 한국어: 새 작업이 꼭 ~을 필요로 할 때에만
- 설명: only when 이 예외를 조건으로 묶고 strictly 가 그 조건을 더 좁힌다. "있으면 좋은" 수준이 아니라 "없으면 안 되는" 수준이어야 한다는 뜻이다. 기본값(새 서브에이전트)을 앞에서 세우고 예외를 뒤에 다는 규칙문 구조다.
- 예문: Resume an existing subagent only when the new work strictly needs state that lives in that agent and is costly to move. (작성)
- 유사어: only if absolutely necessary (구어), solely where (문어)

## "to the letter"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 지시를 한 글자도 어김없이 그대로 따를 때(지침·구어)
- 한국어: 한 치도 어김없이, 글자 그대로
- 설명: letter 는 '글자'. 해석의 여지 없이 문자 그대로 따른다는 관용구다. 원문은 "모호한 의도에 판단이 필요한 일"과 "정확히 정해진 단계를 그대로 실행하는 일"을 대비했다.
- 예문: It can be a precisely specified sequence of steps to execute to the letter. (작성)
- 유사어: exactly as written (중립), by the book (규정대로; 관행 강조)
- 반의어: loosely (느슨하게), in spirit (취지만 따라)

## "gnarly (concurrency)"
- 레지스터: casual, technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 까다롭고 꼬여서 손대기 겁나는 문제를 말할 때(개발자 구어)
- 한국어: 고약한, 꼬일 대로 꼬인(동시성 문제)
- 설명: gnarly 는 원래 나무 옹이(gnarl)처럼 울퉁불퉁하다는 말. 개발자 사이에서는 '골치 아프게 복잡한'이다. 공식 문서에서는 피하고 대화·내부 문서에서 쓴다.
- 예문: The hardest changes, like gnarly concurrency, go to your strongest model. (작성)
- 유사어: hairy (구어, 비슷한 강도), thorny (문어에도 무난), intricate (문어, 중립)
- 반의어: straightforward, trivial

## "Green is not safe."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: CI 가 통과했다는 것만으로 배포해도 된다는 뜻은 아니라고 경고할 때(배포 절차)
- 한국어: 초록불(CI 통과)이 곧 안전은 아니다
- 설명: green 은 CI 결과가 모두 통과한 상태를 색으로 부르는 말이다. 네 단어 단언문이라 규칙으로 기억하기 좋다. 원문은 바로 뒤에 "독립된 PR 별 판정 전에는 아무것도 걸지 않는다"를 붙였다.
- 예문: Green is not safe. Nothing gets armed before an independent per-PR verdict.
- 유사어: Passing CI isn't proof it works (풀어쓴 구어), A green build is necessary but not sufficient (문어)

## "Bias to deletion"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 코드를 고칠 때 추가보다 삭제 쪽을 먼저 고르라는 원칙을 말할 때(설계 원칙)
- 한국어: 삭제 쪽으로 기울어라
- 설명: bias 는 명사로 '편향', 동사로 '한쪽으로 기울게 하다'. bias toward 가 흔하고 bias to 도 쓴다. 명령문 하나로 판단 기본값을 정한다.
- 예문: Bias to deletion and the smallest change that solves the problem.
- 유사어: lean toward removing code (구어), prefer subtraction (문어)
- 반의어: add another layer (계층 추가)

## "No is an acceptable answer."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 제안을 거절하거나 반대해도 괜찮다고 미리 허락할 때(협업 규범)
- 한국어: 아니라고 답해도 된다
- 설명: No 를 명사처럼 주어 자리에 썼다. 그래서 대문자로 시작하고 관사가 없다. 짧은 규범 문장이라 팀 문화 문서에 잘 맞는다.
- 예문: No is an acceptable answer. Asked whether to do something, reply with your real judgment. (작성)
- 유사어: Feel free to say no (구어, 친근), Declining is a valid outcome (문어)

## "Never hand the human a check you could run. (작성)"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문
- 맥락: 직접 확인할 수 있는 일을 남에게 미루지 말라고 할 때(작업 원칙)
- 한국어: 직접 돌려 볼 수 있는 확인을 사람에게 떠넘기지 마라
- 설명: `hand + 사람 + 사물`(이중 목적어). a check you could run 은 관계대명사가 생략된 관계절이다. could 는 "할 수 있었는데 안 한" 가능성을 암시한다.
- 예문: Every claim carries its evidence or its label, and you should never hand the human a check you could run.
- 유사어: Don't make the user verify what you can verify yourself (풀어쓴 구어), don't offload checks (짧은 구어)
