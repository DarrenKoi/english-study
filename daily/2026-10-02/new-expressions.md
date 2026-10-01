# 2026-10-02 — 새 표현

> 오늘 배치는 transcript 11건이고 repo 문서와 spool 노트는 없다. 그중 4건은 `/clear` 만 찍힌 빈 세션이라 실제 재료는 7건이다. 표현이 가장 많이 나온 곳은 skewnono 하드웨어 페이지 작업 두 세션(FDC·MDC). 코드 리뷰와 `/simplify` 보고서가 길게 이어져 "받아들일 지적과 물릴 지적을 가르는 말"이 풍성했다. 세션에 딸려 온 스킬 문서(unlazy, code-review, simplify)에서도 몇 개 골랐다. `carry over to`, `just say the word`, `hold up`, `earn its place`, `exercise (a code path)`, `blast radius`, `heads up`, `one-line change`, `byte-identical` 은 노트에 이미 있어서 뺐다.

## "extract it when a third appears"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (FDC 코드 리뷰 요약)
- 맥락: 중복 코드를 지금 뽑지 않고 세 번째가 나올 때까지 미루자고 할 때(코드 리뷰, 기술).
- 한국어: 세 번째가 나오면 그때 뽑아낸다
- 설명: 흔히 rule of three 라고 부르는 관행이다. 두 번까지는 두고 세 번째에 공통 코드로 뽑는다. 원문은 세미콜론 앞에 지금 상태를, 뒤에 조건 달린 지시를 두었다. `a third` 뒤에 생략된 말은 `copy`. 리뷰어 보고서에는 더 줄인 `Extract it on a third.` 도 나온다.
- 예문: This is the second copy; extract it when a third appears.
- 유사어: wait for the rule of three (관행 이름으로 말하기), factor it out once it repeats again (풀어 쓴 말), leave the duplication for now (미루는 쪽만 말함)
- 반의어: extract it now (지금 바로 뽑다)

## "at a verified stopping point"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt (FDC 코드 리뷰 시작)
- 맥락: 검증까지 끝낸 매듭에서 커밋하거나 보고한다고 말할 때(작업 규칙 설명, 중립).
- 한국어: 검증을 마친 매듭 지점에서
- 설명: `stopping point` 는 일을 끊어도 되는 지점이다. `verified` 가 붙어 "테스트로 확인된"이라는 조건이 더해진다. 원문 `the project rules have me commit` 의 `have + 사람 + 동사원형` 은 사역으로, 규칙이 나에게 그렇게 시킨다는 말이다.
- 예문: Heads-up first: the change is already committed and pushed to `main` (59d1c388), because the project rules have me commit at a verified stopping point.
- 유사어: at a natural breakpoint (검증 여부는 말하지 않음), once the tests are green (조건을 구체적으로), at a good place to pause (구어)
- 반의어: mid-change (변경 도중에)

## "which is exactly the bug X was meant to fix"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (Spec 리뷰 보고서)
- 맥락: 고치려고 넣은 장치가 도리어 그 버그를 다시 부른다고 지적할 때(리뷰, 기술).
- 한국어: 그게 바로 X 가 고치려던 버그다
- 설명: `, which` 가 앞 절 전체를 받는다. `be meant to` 는 "~하라고 만든"이다. 원문은 툴팁 고정 장치(pin)가 점이 촘촘한 차트에서는 풀려 버려 툴팁이 커서보다 앞서 달아난다고 짚었다.
- 예문: The tooltip then re-pins and runs 6 px ahead of the cursor, which is exactly the bug the pin was meant to fix.
- 유사어: which defeats the purpose of X (목적을 무너뜨린다, 더 일반적), the very problem X was supposed to solve (`very` 로 강조), which brings the original bug back (평이)

## "I'm dismissing this one."
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt (FDC 코드 리뷰 요약)
- 맥락: 리뷰 지적 하나를 직접 확인한 뒤 받아들이지 않겠다고 밝힐 때(리뷰 응답, 중립).
- 한국어: 이 지적은 기각합니다
- 설명: `dismiss` 는 주장이나 우려를 따져 본 뒤 물리는 동사다. 보지도 않고 넘기는 `ignore` 와는 결이 다른 말. 원문은 바로 앞에 `I tested this in the browser and it doesn't happen.` 을 두어 근거부터 댔다. `this one` 은 여러 지적 가운데 하나를 짚는다.
- 예문: I tested this in the browser and it doesn't happen, so I'm dismissing this one. (작성)
- 유사어: I'm ruling this out (가능성을 배제), I'll set this one aside (보류에 가깝고 부드러움), not a real issue (구어, 단정)
- 반의어: this one holds up (지적이 타당하다)

## "unless you say otherwise"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt (FDC 코드 리뷰 요약)
- 맥락: 기본 방침을 알리고 상대가 반대하면 바꾸겠다는 여지를 둘 때(보고·메신저, 구어~중립).
- 한국어: 달리 말씀이 없으면
- 설명: 원문은 `Leaving alone unless you say otherwise:` 로 손대지 않을 항목 목록을 열었다. 허락을 묻지 않고 기본값을 정해 둔 채 거부권만 준다. 격식을 올리면 `unless you object` 다.
- 예문: I'm leaving the toggle markup alone unless you say otherwise. (작성)
- 유사어: unless you tell me differently (같은 뜻, 조금 길다), unless you object (격식), by default (기본값만 말함)
- 반의어: only if you say so (말씀하실 때만)

## "along the way"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt (남은 세 항목 완료 보고)
- 맥락: 본래 작업을 하다가 덤으로 찾았거나 한 일을 덧붙일 때(작업 보고, 구어~중립).
- 한국어: 하는 도중에, 하는 김에
- 설명: 원문은 `Bug found along the way:` 라는 굵은 소제목이다. 요청받은 범위 밖에서 나온 발견임을 구 하나로 알린다. 여정 비유라서 "가는 길에 주웠다"는 느낌이 난다.
- 예문: I found a blank-icon bug along the way and fixed it in the same commit. (작성)
- 유사어: in passing (지나가다, 더 가볍게), while I was at it (하는 김에, 구어), incidentally (격식 부사)
- 반의어: on purpose (일부러)

## "cancel out"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt (/simplify 적용 중)
- 맥락: 더한 것과 뺀 것이 맞먹어 합계가 그대로라고 설명할 때(수치 보고, 중립).
- 한국어: 서로 상쇄되다
- 설명: 자동사로는 `A and B cancel out`, 타동사로는 `A cancels out B` 로 쓴다. 원문은 테스트 수가 왜 그대로인지 콜론 뒤에서 풀었다.
- 예문: The test count stays 1839: the removed `wallClockIso` test and the new icon test cancel out.
- 유사어: offset each other (격식, 회계·통계), balance out (균형이 맞다), net out to zero (순합계 0, 업무 구어)
- 반의어: add up (쌓이다)

## "take on"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt (/simplify 완료 보고)
- 맥락: 일을 맡겠느냐고 묻거나 맡으라고 할 때(업무 대화, 구어~중립).
- 한국어: (일을) 맡다
- 설명: 원문 `Want me to take on either of these?` 는 `Do you` 를 뗀 구어 의문문이다. 나는 이 말을 `take on the two fixes` 로 받아 썼고 어시스턴트는 `Taking both on.` 으로 답했다. 대명사나 짧은 목적어는 가운데(`take both on`), 긴 명사구는 뒤에 둔다.
- 예문: Want me to take on either of these?
- 유사어: pick up (일을 집어 들다, 더 가볍다), tackle (어려운 일에 달려들다), handle (처리하다, 중립)
- 반의어: pass on (사양하다), hand off (넘기다)

## "a near-miss hover"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (추세선 툴팁 수정)
- 맥락: 대상에서 살짝 빗나간 입력으로 허용 반경을 시험할 때(UI 테스트, 기술).
- 한국어: 살짝 빗나간 호버
- 설명: `near miss` 는 "아슬아슬하게 빗나감"이다. 명사 앞에서 꾸밀 때는 하이픈 필수. 원문은 점에서 13px 떨어진 곳을 가리켜 22px 반경 안이면 잡히는지 확인했다. 뒤에는 `Correct now: the near-miss picks the 09-25 dot.` 처럼 명사로도 썼다.
- 예문: Re-testing in the browser with a near-miss hover, about 13px off the dot.
- 유사어: an off-target hover (과녁을 벗어난), a slightly-off click (구어), an edge-case input (경계 입력, 더 넓은 말)
- 반의어: a direct hit (정확히 맞힘)

## "positive control"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (Codex 리뷰 반영)
- 맥락: 테스트가 정말 실패할 줄 아는지 일부러 고장 내 확인할 때(테스트 검증, 실험 용어).
- 한국어: 양성 대조
- 설명: 실험에서 온 말로 결과가 나와야 하는 조건에서 정말 나오는지 보는 대조군을 가리킨다. 테스트에서는 "버그를 일부러 넣으면 빨갛게 되는가"가 된다. 같은 배치의 unlazy 스킬에도 `Exercise a negative check against a known positive control before trusting absence.` 가 있다.
- 예문: Positive control: temporarily making `gridDetail` return the snapped `x` should fail Codex's test.
- 유사어: a check that the test can fail (풀어 쓴 말), a mutation check (코드를 바꿔 보는 검증), a known-bad case (실패해야 맞는 사례)
- 반의어: negative control (안 나와야 할 때 안 나오는지 보는 대조)

## "a test that guards nothing"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (Simplification 리뷰 보고서)
- 맥락: 호출자가 사라진 함수의 테스트처럼 지킬 대상이 없는 테스트를 지적할 때(코드 리뷰, 기술).
- 한국어: 아무것도 지키지 않는 테스트
- 설명: `guard` 는 회귀를 막는다는 뜻의 동사다. `nothing` 을 목적어로 두어 부정문 없이 부정한다. 원문은 죽은 코드를 남겨 둘 때 드는 비용을 명사구 하나로 셈했다.
- 예문: Cost: 5 lines plus a test that guards nothing.
- 유사어: a test with nothing left to protect (풀어 쓴 말), a vacuous test (늘 통과하는 빈 테스트, 격식), dead test code (죽은 코드 쪽에 초점)
- 반의어: a regression guard (회귀를 막는 테스트)

## "The comment admits …"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (Altitude 리뷰 보고서)
- 맥락: 코드 주석 스스로 적어 둔 한계를 근거로 삼을 때(리뷰, 기술).
- 한국어: 주석도 …라고 인정한다
- 설명: 무생물 주어에 `admit` 을 붙여 주석을 증인처럼 세운다. 한국어로는 "주석에 ~라고 적혀 있다"가 자연스럽지만 영어는 주석이 직접 말하게 한다. 원문은 `that` 없이 절을 바로 이었다.
- 예문: The comment admits data spanning under a day still repeats.
- 유사어: The comment concedes that … (더 격식), The comment itself says … (평이), By its own account, … (문어)
- 반의어: The comment claims … (근거 없이 주장한다는 뉘앙스)

## "always travel together"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (Altitude 리뷰 보고서)
- 맥락: 늘 붙어 다니는 인자나 필드를 하나로 묶자고 할 때(코드 리뷰, 기술).
- 한국어: 늘 함께 다닌다
- 설명: 리팩터링에서 Data Clumps 냄새를 설명할 때 쓰는 말이다. 배치에 실린 code-review 스킬에도 `the same few fields or params keep travelling together` 가 나온다. 값이 호출 경로를 따라 "이동한다"고 보는 비유다. 영국식 철자는 `travelling`.
- 예문: `step` and `dateOnly` are two props that always travel together.
- 유사어: always come as a pair (짝으로 온다, 구어), are always passed together (평이), go hand in hand (비유, 일반 글)
- 반의어: vary independently (따로 변한다)

## "different notions of "same""
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (Altitude 리뷰 보고서)
- 맥락: 같은 로직이 여러 곳에 있는데 판정 기준이 서로 다르다고 지적할 때(리뷰, 기술).
- 한국어: "같다"의 기준이 서로 다르다
- 설명: `notion` 은 `definition` 보다 느슨한 말이라 정식으로 정한 적 없이 코드마다 암묵적으로 품은 기준을 가리키기에 알맞다. 원문은 한 곳이 `===` 로, 다른 곳이 허용 오차로 비교한다고 짚었다. 수정 계획은 이를 `One notion of "unchanged."` 로 받았다.
- 예문: "Collapse repeated snapshots" is implemented three times, with different notions of "same".
- 유사어: different definitions of "same" (더 딱 떨어지는 말), each has its own idea of what counts as equal (구어로 풀기), inconsistent equality rules (문서체)
- 반의어: a single definition (정의 하나)

## "sit clear of"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt (MDC 시계열 탭 확인)
- 맥락: 화면 요소가 다른 요소와 겹치지 않고 떨어져 있다고 설명할 때(UI 확인 보고, 중립).
- 한국어: ~와 겹치지 않게 떨어져 있다
- 설명: `clear of` 는 "~에 닿지 않게 비켜난"이다. `sit` 은 화면 요소가 놓인 위치를 말할 때 쓰는 동사다. 같은 세션에 `the "nm" axis name stays clear` 도 나온다.
- 예문: The trajectory has its own row, its axis names sit clear of the tick labels, and the trends show only `MM/DD`.
- 유사어: don't overlap (평이), are well separated from (문서체), have room to breathe (여백이 넉넉하다, 디자인 구어)
- 반의어: print over (위에 덮어 찍히다), overlap (겹치다)

## "an oracle that cannot fail"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (unlazy 스킬 본문)
- 맥락: 어떤 경우에도 통과해 버려 검증 구실을 못 하는 검사를 가리킬 때(테스트 설계, 기술).
- 한국어: 실패할 수 없는 판정 기준
- 설명: `oracle` 은 테스트에서 맞고 틀림을 판정하는 기준이다. 실패할 수 없는 기준은 통과해도 알려 주는 게 없다. 원문은 `caught at authoring time rather than certified at report time` 으로 과거분사 둘을 맞세웠다. 쓸 때 잡느냐, 보고할 때 도장을 찍어 주느냐의 대비.
- 예문: Lint the ledger before working it, so an oracle that cannot fail is caught at authoring time rather than certified at report time.
- 유사어: a check that always passes (평이), a vacuous assertion (격식), a rubber stamp (비유)
- 반의어: a gate that can fail honestly (정직하게 실패할 수 있는 관문)

## "Open decision:"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (MDC 변경 완료 보고)
- 맥락: 보고 끝에 상대가 정해 줘야 할 사항을 따로 떼어 알릴 때(작업 보고, 중립~격식).
- 한국어: 남은 결정 사항
- 설명: 명사구 라벨이다. `open` 은 "아직 닫히지 않은"이다. 원문은 뒤에 지금 동작을 적고 바꾸는 비용(`that's a one-line change`)까지 붙여 상대가 바로 고르게 했다.
- 예문: Open decision: the table waits for a click rather than opening on the first condition.
- 유사어: Still to decide: (평이), Pending your call: (상대의 결정임을 강조), Open question: (결정보다 물음에 가깝다)
- 반의어: Decisions locked in: (확정된 결정)

## "which I reproduced before fixing"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt (Codex 리뷰 반영 보고)
- 맥락: 남이 지적한 문제를 곧이듣지 않고 재현부터 했다고 밝힐 때(리뷰 반영 보고, 중립).
- 한국어: 고치기 전에 직접 재현했다
- 설명: 계속적 용법 `, which` 가 `three real problems` 를 받는다. `before fixing` 은 주어가 같아서 `before I fixed them` 을 줄인 꼴이다. 지적 → 재현 → 수정 순서를 관계절 하나에 담았다.
- 예문: It flagged three real problems in my change, which I reproduced before fixing.
- 유사어: which I confirmed first (확인했다, 더 넓은 말), I verified each one before touching the code (풀어 쓴 문장), I didn't take them on faith (곧이곧대로 믿지 않았다, 구어)
- 반의어: which I fixed on trust (믿고 바로 고친)

## "Likely causes, most likely first"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (OpenSearch 이름 해석 오류 진단)
- 맥락: 원인 후보를 가능성 높은 순으로 늘어놓는 목록의 제목(장애 분석 글, 중립).
- 한국어: 가능한 원인, 가능성 높은 순
- 설명: 쉼표 뒤의 `most likely first` 가 정렬 기준이다. 제목에서 순서의 뜻을 밝혀 두면 읽는 사람이 1번부터 확인하면 된다는 걸 안다. 앞의 `likely` 는 원급, 뒤는 최상급이다.
- 예문: Likely causes, most likely first: the PC is off the internal network, company DNS is having trouble, or the host was renamed. (작성)
- 유사어: Possible causes, in order of likelihood (격식), Probable causes, ranked (짧은 문서체), What's probably going on (구어)

## "map straight onto"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (FDC·SCE 특성 조사 brief 설명)
- 맥락: 조사 결과가 따로 해석할 것 없이 곧바로 할 일로 이어진다고 말할 때(계획 설명, 중립).
- 한국어: 곧바로 ~에 대응되다
- 설명: `map onto` 는 "하나씩 대응되다"이고 `straight` 가 "중간 단계 없이"를 더한다. 원문의 `should` 는 의무가 아니라 예상이다.
- 예문: Once the report comes back, the decision table in it should map straight onto concrete panel changes.
- 유사어: translate directly into (곧장 ~로 바뀌다), correspond one-to-one with (격식), line up with (구어)
- 반의어: need interpreting first (해석부터 거쳐야 한다)

## "a confident done report"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (unlazy 스킬 본문)
- 맥락: 근거 없이 "다 됐습니다"만 자신 있게 말하는 보고를 경계할 때(작업 방식 문서, 중립).
- 한국어: 자신만만한 완료 보고
- 설명: `done` 이 명사 `report` 를 꾸며 "끝났다는 보고"가 된다. 여기서 `confident` 는 칭찬이 아니다. 말투만 확신에 차 있고 증거는 없는 상태를 꼬집는다.
- 예문: Prove outcomes against a ledger instead of relying on a confident done report.
- 유사어: an unverified completion claim (격식), a "looks good to me" with no evidence (구어로 풀기), taking "it's done" at face value (액면 그대로 믿기)
- 반의어: a verified result (검증된 결과)

## "note the skip rather than arguing with it"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (/simplify 지침 본문)
- 맥락: 받아들이지 않을 리뷰 지적은 반박하지 말고 건너뛰었다고만 적으라고 지시할 때(리뷰 절차 문서, 중립).
- 한국어: 반박하지 말고 건너뛰었다고만 적는다
- 설명: `skip` 이 명사로 쓰였다. `rather than + -ing` 는 하지 말 쪽을 뒤에 둔다. `it` 이 가리키는 것은 그 지적(finding). 리뷰어와 논쟁하느라 시간을 쓰지 말라는 실무 지침이다.
- 예문: Skip any finding you judge to be a false positive, and note the skip rather than arguing with it. (작성)
- 유사어: just record that you skipped it (평이), log it and move on (구어), decline without debate (격식)
- 반의어: push back on it (반박하다)

## "Two changes you didn't ask for:"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (FDC 여섯 항목 완료 보고)
- 맥락: 요청 범위 밖에서 손댄 것을 숨기지 않고 따로 묶어 알릴 때(작업 보고 소제목, 중립).
- 한국어: 요청하지 않으셨지만 바꾼 것 두 가지
- 설명: `changes (that) you didn't ask for` 는 목적격 관계대명사를 생략한 꼴이라 전치사 `for` 가 끝에 남는다. 요청한 일의 목록과 분리해 두면 상대가 범위를 넘은 부분만 골라 검토하기 쉽다.
- 예문: Two changes you didn't ask for: the LaserPower mock data and the shared tooltip code. (작성)
- 유사어: Beyond the request: (문서체), Unrequested changes: (딱딱함), Also, while I was in there … (구어)
- 반의어: Exactly as requested (요청한 그대로)

## "My mistake:"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt (Codex 리뷰 반영 중)
- 맥락: 자기 실수를 짧게 인정하고 곧바로 경위를 설명할 때(작업 보고, 구어).
- 한국어: 제 실수입니다
- 설명: `I made a mistake` 보다 짧고 `Sorry` 보다 담백하다. 콜론 뒤에 무슨 일이 있었는지 바로 붙인다. 원문은 실수(`git checkout --` 로 커밋 안 한 수정까지 날림)와 복구 방법(직전에 떠 둔 백업)을 연달아 말했다.
- 예문: My mistake: I restored with `git checkout --`, which reset `chartNearest.ts` to the last commit and wiped the uncommitted `gridDetail` edit.
- 유사어: My bad. (더 가벼운 속어), That one's on me. (책임이 내게 있다, 구어), I got that wrong. (판단이 틀렸음을 인정)

## "sort out"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt (OpenSearch 이름 해석 오류 진단)
- 맥락: 꼬인 문제를 풀어 정리한다고 말할 때(업무 대화, 구어).
- 한국어: 해결하다, 정리하다
- 설명: `fix` 보다 "엉킨 것을 풀어 제자리에 둔다"는 느낌이 짙다. `while you sort out X` 는 "X 를 해결하는 동안 임시로"라는 틀이다. 대명사는 가운데에 둔다(`sort it out`).
- 예문: To silence only the log shipping while you sort out the network, set `OPENSEARCH_LOGGING_DISABLED=1`.
- 유사어: straighten out (바로잡다), resolve (격식), figure out (원인을 알아내는 쪽)
- 반의어: mess up (엉망으로 만들다)

## "Spend attention where it compounds"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt (unlazy 스킬 본문)
- 맥락: 한정된 집중력을 나중에 몇 배로 돌아오는 곳에 쓰라고 권할 때(작업 원칙 제목, 중립).
- 한국어: 복리로 불어나는 곳에 주의를 써라
- 설명: `compound` 는 "복리로 불어나다"이다. 주의력을 돈처럼 `spend` 한다고 표현해 비유가 끝까지 이어진다. 원문은 이 제목 아래에서 설계·통합·검증에는 강한 추론을, 기계적인 일에는 값싼 실행을 쓰라고 적었다.
- 예문: Spend attention where it compounds: use stronger reasoning for design, integration, and verification. (작성)
- 유사어: Put your effort where it pays off most (평이), Focus on high-leverage work (업무 용어), Pick your battles (비유, 구어)
- 반의어: spread yourself thin (힘을 여기저기 흩다)
