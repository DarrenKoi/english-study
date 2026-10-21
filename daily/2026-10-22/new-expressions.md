# 2026-10-22 — 새 표현

오늘 배치는 문서 2건과 대화 10건이다. 문서 두 개(Hitachi MSR pickle 구조 메모, 스큐노노 연말 성과 보고)는 거의 한국어라 표현 원료로 쓰지 않았다. 영어 표현은 주로 두 곳에서 왔다. 하나는 S5 작업(판정 근거 설명 기능)을 세 라운드에 걸쳐 보고한 어시스턴트 답변이고, 다른 하나는 AFM 작업 중 불러온 Herdr 스킬 문서다. Herdr 문서는 이전에 이미 상당 부분 수집해서(`treat every ID as an opaque string`, `Inspect before waiting.`, `hijack the tab`, `reach for`, `X is the authority for Y` 등) 새 문장만 골랐다. 브리프·리뷰 지시문(사용자 쪽 영어)에서도 몇 개를 건졌다.

## "make the call and record it"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-s5 [user]
- 맥락: 일을 맡기면서 "묻지 말고 직접 정한 뒤 기록만 남겨라"라고 권한을 넘길 때(업무 지시·구어/문어)
- 한국어: 직접 판단하고 그 판단을 기록해 둬라
- 설명: `make the call` 은 심판이 판정을 내리는 데서 온 말로 "결정을 내리다"이다. `decide` 보다 "책임지고 정한다"는 느낌이 세다. 뒤에 `and record it` 을 붙여 "결정권은 주되 근거는 남겨라"라는 위임의 조건까지 한 줄에 담았다.
- 예문: If the spec is unclear, make the call and record it in the report so I can review it later.
- 유사어: use your judgment (더 부드럽고 일반적), decide and note it down (평이), it's your call (상대에게 권한이 있다고 말할 때, 명령형이 아님)
- 반의어: check with me first (먼저 확인받아라)

## "Calls I made that differ from the brief"
- 레지스터: professional
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 작업 보고에서 지시서와 다르게 처리한 부분을 따로 묶는 소제목(작업 보고·문어)
- 한국어: 브리프와 다르게 내린 판단들
- 설명: 위 지시의 `make the call` 을 받아 명사 `call`(판단)로 돌려준 머리말이다. `that differ from` 관계절로 "다르게 한 것만" 거른다. 지시와 어긋난 부분을 숨기지 않고 먼저 꺼내 놓으면 리뷰어가 볼 곳이 좁아진다.
- 예문: Calls I made that differ from the brief: I kept the old endpoint, and I skipped the dark-theme check.
- 유사어: Deviations from the brief (격식, 짧음), Where I went off-script (구어), Judgment calls (판단 항목 전체를 말할 때)
- 반의어: Done as briefed (지시대로 한 것)

## "regardless of the toggle"
- 레지스터: technical
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 어떤 동작이 설정·스위치 값과 상관없이 똑같이 일어난다고 밝힐 때(코드 설명·문어)
- 한국어: 토글 값과 상관없이
- 설명: `regardless of + 명사` 는 "~에 관계없이"다. 원문은 "엔진은 토글과 관계없이 mother 의 cap 을 상속한다"로, 토글이 바꾸는 범위를 먼저 지운 뒤 "토글이 실제로 바꾸는 건 화면의 접미사뿐"이라고 이어 간다. 기대와 다른 동작을 설명할 때 앞세우기 좋다.
- 예문: The cache is cleared on every deploy, regardless of the feature flag.
- 유사어: no matter how the toggle is set (구어, 더 길다), irrespective of the toggle (격식), whatever the toggle says (구어)
- 반의어: depending on the toggle (토글에 따라)

## "I did not read or act on it."
- 레지스터: professional
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 작업 중 범위 밖의 파일·메시지를 봤지만 손대지 않았다고 분명히 해 둘 때(보고·문어)
- 한국어: 읽지도, 그에 따라 움직이지도 않았습니다.
- 설명: 작업 도중 워크트리에 `BRIEF-review.md` 가 새로 생겼다는 보고의 마지막 문장이다. `read` 와 `act on`(~를 근거로 행동하다)을 `or` 로 묶어 부정하면 "보지도 않았고 반영도 안 했다"가 된다. 다른 에이전트의 지시가 섞여 들어올 수 있는 병렬 작업에서 오염이 없다고 알리는 문장이다.
- 예문: A second config file showed up in the repo during the run; I did not read or act on it.
- 유사어: I left it alone (구어), I ignored it (짧지만 무시했다는 인상이 강함), I didn't touch it (구어)
- 반의어: I picked it up and applied it (가져와 반영했다)

## "the sentence must not claim every parameter is within cap"
- 레지스터: technical, professional
- 출처: transcript:skewnono-s5 [user] (Round 2 지시)
- 맥락: 화면 문구·문서가 사실보다 더 많이 단언하면 안 된다고 지적할 때(리뷰·문어)
- 한국어: 그 문장이 모든 파라미터가 cap 이내라고 주장해서는 안 된다
- 설명: 주어가 사람이 아니라 `the sentence` 이고 동사가 `claim` 이다. 출력 문구도 "주장"을 한다고 보고, 데이터가 뒷받침하지 않는 단언을 금지한다. `must not claim` 은 "틀렸다"보다 정확하다. 일부는 맞지만 범위를 넘어 말한다는 지적이기 때문이다.
- 예문: The summary must not claim the migration is complete while two tables are still pending.
- 유사어: must not overstate (격식, 과장 일반), shouldn't say that every … (구어), must not imply (명시하지 않아도 그렇게 읽히는 경우)
- 반의어: must say exactly what was checked (확인한 만큼만 말하다)

## "it must be true to cap_source"
- 레지스터: technical, professional
- 출처: transcript:skewnono-s5 [user] (Round 3 지시)
- 맥락: 표시·설명이 원천 데이터와 어긋나지 않아야 한다고 요구할 때(리뷰·문어)
- 한국어: cap_source 에 충실해야 한다(그 값과 어긋나면 안 된다)
- 설명: `be true to X` 는 "X 에 충실하다, X 를 그대로 반영하다"이다. 원문은 `your call, but it must be true to cap_source` 로, 표현 방식은 맡기되 사실과의 일치는 양보하지 않는다는 구조다. `your call, but …` 이 재량과 제약의 경계를 한 줄에 긋는다.
- 예문: Pick whatever label reads best, but it must be true to the status the API returns.
- 유사어: must match (평이), must reflect (격식), must stay faithful to (격식, 번역·인용에 자주)
- 반의어: misrepresents (사실을 잘못 전하다)

## "This wording is mine; your example covered only the mixed case."
- 레지스터: professional
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 지시에 없던 부분을 내가 채웠다고 밝히고 그 이유를 붙일 때(보고·문어)
- 한국어: 이 문구는 제가 정했습니다. 주신 예시는 섞인 경우만 다뤘습니다.
- 설명: `This wording is mine` 은 "이건 내 판단"이라고 출처를 밝혀 리뷰어가 확인할 지점을 짚어 준다. 세미콜론 뒤에는 왜 스스로 정해야 했는지(지시가 그 경우를 덮지 않았다)를 붙였다. 자기 몫을 숨기지도 변명하지도 않는 짧은 형식이다.
- 예문: The error message for the empty case is mine; the spec only described the partial failure.
- 유사어: I wrote this part myself (구어), this is my own wording, not from the spec (명시적), I filled this gap (구어)
- 반의어: This is taken verbatim from the spec (지시서 그대로다)

## "sons that ride on a mother"
- 레지스터: technical
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 하위 항목이 상위 항목의 설정에 얹혀 동작한다고 설명할 때(설계 설명·구어/문어)
- 한국어: mother 에 얹혀 가는 son 들
- 설명: `ride on X` 는 "X 에 얹혀 가다, X 에 의존해 움직이다"이다. 상속(`inherit`)보다 가볍고 그림이 잘 그려진다. 원문에서는 토글이 꺼지면 이런 son 뒤에 ` · 제외` 접미사가 붙는다고 설명한다.
- 예문: Child jobs that ride on the parent's schedule are skipped when the parent is paused.
- 유사어: piggyback on (구어, 남의 것에 편승), inherit from (기술 용어, 격식), depend on (일반)
- 반의어: stand on their own (독립적으로 동작하다)

## "Paperwork:"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 본 작업이 아니라 보고서·리뷰 파일 갱신 같은 기록 작업을 따로 묶는 머리말(작업 보고·구어)
- 한국어: 서류 작업(기록 정리):
- 설명: 원래 "서류 업무"지만 개발 보고에서는 코드 외의 기록 갱신(REPORT 에 섹션 추가, REVIEW 에 Author 메모)을 가볍게 부르는 말이다. 살짝 자조적인 어감이 있어 본론과 부수 작업을 구분해 준다.
- 예문: Paperwork: the changelog and the ticket are both updated.
- 유사어: Bookkeeping: (비슷하게 가벼움), Housekeeping: (정리 작업 전반), Records updated: (평이·격식)
- 반의어: (마땅한 반의어 없음 — 본론 쪽은 그냥 "Fix:" 로 쓴다)

## "I did not re-run the browser check, since the change is sentence text in a pure function."
- 레지스터: professional, technical
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 검증 하나를 건너뛰었다고 밝히면서 그게 왜 안전한지 근거를 붙일 때(보고·문어)
- 한국어: 바뀐 게 순수 함수 안의 문장 텍스트뿐이라 브라우저 확인은 다시 돌리지 않았습니다.
- 설명: 건너뛴 사실(`did not re-run`)을 먼저 말하고 `since` 로 근거를 단다. `since` 는 상대도 쉽게 납득할 이유에 붙는다. 근거가 "순수 함수"라서 단위 테스트로 충분하다는 기술적 판단이다. 안 한 일을 숨기지 않으면서 왜 괜찮은지까지 보여 준다.
- 예문: I did not redeploy staging, since the change only touches a test fixture.
- 유사어: I skipped X because … (구어), X wasn't re-run; the change is limited to … (수동, 격식), no need to re-run X, since … (구어, 판단을 더 단정)
- 반의어: I re-ran the full check to be safe (안전을 위해 다시 돌렸다)

## "that is listed under Open questions"
- 레지스터: professional
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 지금 정하지 않은 대안을 보고서의 미결 항목으로 넘겨 두었다고 알릴 때(보고·문어)
- 한국어: 그건 '미결 질문' 항목에 적어 두었습니다
- 설명: 원문은 "대안은 `ComplianceTable.vue` 를 조금 고치는 것이고, 그건 Open questions 에 적어 두었다"이다. `be listed under + 섹션명` 으로 어디를 보면 되는지 위치까지 알려 준다. 결정을 미룬 것이 아니라 결정권자에게 넘긴 것으로 읽힌다.
- 예문: Moving the job to a queue is another option; that is listed under Open questions.
- 유사어: I've parked that under … (구어), see Open questions (짧은 상호 참조), flagged for your decision (명시적)
- 반의어: already decided (이미 정한 것)

## "Status: X are read; now Y-ing"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-s5 [assistant]
- 맥락: 긴 작업 도중 한 줄로 진척을 알릴 때 — 끝난 것과 지금 하는 것을 나란히(진행 보고·구어/문어)
- 한국어: 상황: X 는 읽었고, 지금은 Y 하는 중
- 설명: 원문은 `Status: briefs, spec and the engine/slideover code are read; now widening the engine types, then ruleExplain.ts, UI, tests and the browser check.` 이다. 완료는 수동 `are read`, 진행은 주어 없는 `now -ing`, 다음 순서는 `then …` 으로 이어 한 문장에 과거·현재·다음이 다 들어간다.
- 예문: Status: the logs are pulled; now matching them against the deploy times, then writing up the timeline.
- 유사어: Quick update: … (구어), Progress so far: … (평이), Where I am: … (구어)
- 반의어: (마땅한 반의어 없음)

## "the same underlying state with different attention state"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (herdr 스킬 문서)
- 맥락: 이름이 다른 두 값이 실제로는 같은 상태이고 부가 속성만 다르다고 정리할 때(기술 문서·문어)
- 한국어: 바탕 상태는 같고 '확인했는지' 여부만 다른 것
- 설명: 원문은 "`idle` 과 `done` 은 같은 의미 상태에 주의(attention) 상태만 다르다"이다. `underlying` 은 "겉 이름 아래 깔린 실체"라는 뜻이다. 두 개념을 하나의 축(실체)과 다른 축(부가 속성)으로 나눠 설명하는 틀로 쓴다.
- 예문: `archived` and `hidden` are the same underlying record with different visibility settings.
- 유사어: essentially the same, differing only in … (평이), two names for one state (구어), the same thing under a different flag (구어)
- 반의어: fundamentally different states (근본적으로 다른 상태)

## "the difference is whether the result has been seen"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt (herdr 스킬 문서)
- 맥락: 비슷한 두 값의 차이를 기준 하나로 압축해 말할 때(설명·문어/구어)
- 한국어: 차이는 결과를 봤느냐 안 봤느냐뿐이다
- 설명: `the difference is whether …` 은 차이를 예/아니오로 갈리는 질문 하나로 줄인다. 현재완료 수동 `has been seen` 이 "지금 시점까지 확인됐는가"라는 상태를 말한다. 긴 비교 설명 끝에 이 문장 하나로 정리하면 기억에 남는다.
- 예문: Both endpoints return the same data; the difference is whether the response is cached.
- 유사어: what sets them apart is whether … (격식), the only thing that differs is … (평이), it comes down to whether … (구어)
- 반의어: they differ in many ways (여러 면에서 다르다)

## "turn an existing X into Y"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (herdr 스킬 문서)
- 맥락: 어떤 동작이 이미 있는 상태를 다른 상태로 바꾸지 않는다고 범위를 그을 때(기술 문서·문어)
- 한국어: 이미 있는 X 를 Y 로 바꾸다
- 설명: 원문은 `Switching away does not turn an existing idle status into done; done is created by a later completion while the pane is unseen.` 이다. `turn A into B` 로 상태 전이를 말하고, `existing` 으로 "이미 있던 것"과 "나중에 생기는 것"을 갈랐다. 세미콜론 뒤 수동 `is created by …` 가 그 상태가 생기는 유일한 길을 밝힌다.
- 예문: Re-running the import does not turn an existing draft into a published post.
- 유사어: convert X to Y (격식, 기술), change X to Y (평이), flip X to Y (구어, 이진 상태)
- 반의어: leave X as it is (그대로 두다)

## "Finding 1 is valid"
- 레지스터: professional
- 출처: transcript:skewnono-s5 [user] (Round 2 지시)
- 맥락: 리뷰 지적 중 어느 것이 맞는지 먼저 판정해 주고 처리 방향을 지시할 때(코드 리뷰·문어)
- 한국어: 지적 1은 타당하다
- 설명: 리뷰 라운드를 운영하는 쪽이 지적을 받아들일지 먼저 판정하는 문장이다. `valid` 는 "옳다"보다 "근거가 있어 받아들일 만하다"에 가깝다. 짧게 판정하고 콜론 뒤에 고칠 방향을 바로 적는 배치가 효율적이다.
- 예문: Finding 1 is valid: the retry loop can run forever if the server keeps returning 503.
- 유사어: Finding 1 holds (격식, 간결), the reviewer is right about 1 (구어), I agree with finding 1 (주관적)
- 반의어: Finding 1 doesn't hold (지적이 성립하지 않는다)

## "write a rebuttal directly under the finding"
- 레지스터: professional
- 출처: transcript:skewnono-s5 [user] (Round 2 지시)
- 맥락: 리뷰 지적에 동의하지 않으면 그 자리에 반박을 적으라고 할 때(리뷰 절차·문어)
- 한국어: 지적 바로 아래에 반박을 적어라
- 설명: `rebuttal` 은 "반박, 반론"으로 논쟁·법정에서 온 격식어다. 원문은 `fix it, or write a rebuttal …` 으로 지적마다 두 선택지 중 하나를 반드시 고르게 한다. `directly under` 로 위치까지 정해 기록이 흩어지지 않게 했다.
- 예문: If you disagree with a comment, write a rebuttal directly under it instead of resolving it silently.
- 유사어: push back on it in writing (구어), reply with your reasoning (평이), contest the finding (격식)
- 반의어: accept the finding (지적을 받아들이다)
