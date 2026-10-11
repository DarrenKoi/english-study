# 2026-10-12 — 새 표현

> 오늘 배치는 repo 문서 4건과 transcript 9건이다. `ebeam_pages_current_state.md` 는 그제(10-10)에 한 번 훑은 문서라 그때 안 고른 것만 일곱을 집었고, FDC/SCE 조사 브리프(`hardware_fdc_sce_characterization.md`)도 9월 29일에 다룬 적이 있어 남은 여섯만 골랐다. AFM 현황 노트와 FDC 데이터 메모는 본문이 한국어여서 표현 재료로 쓰지 않았다. transcript 에서는 skewnono 문서 정리 세션의 영어 보고에서 아홉, 히트맵 수정 보고에서 둘, auto-recipe-creator 세션의 코드 리뷰 결과에서 다섯을 골랐다. Herdr·leave-office·browser-verify 스킬 문서와 이 저장소의 지난 배치 프롬프트는 예전에 다 다뤄서 건너뛰었다. 노트에 이미 있어서 뺀 것: `not proofs of absence`, `the connective tissue between pages`, `fell off before triage finished`, `rides in the beacon URL`, `a guess dressed as a finding`, `be silently dropped`, `in flight`.

## "has so far declined"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 결정권자가 지금까지는 거절해 왔다고, 앞으로 바뀔 여지를 남기며 적을 때(보고서·문어, 격식).
- 한국어: 지금까지는 (하지 않기로) 거절해 왔다
- 설명: `so far` 가 현재완료 사이에 끼어 "아직까지는"이라는 단서를 단다. `refused` 는 딱 잘라 거부했다는 느낌이고 `declined` 는 정중하게 사양했다는 쪽이다. 원문은 `which the owner has so far declined for storage` 로, 스토리지에 한해 그렇다는 범위까지 `for` 로 붙였다.
- 예문: Adding a trend to those pages needs new collection, which the owner has so far declined for storage.
- 유사어: has not yet agreed to (중립, 거절보다 보류에 가까움), has ruled out for now (구어~중립, 더 단정적), has turned down (구어)
- 반의어: has signed off on (승인했다)

## "is waiting on (X)"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 어떤 일이 다른 일이 끝나기를 기다리며 멈춰 있다고 말할 때(스탠드업·상태 보고, 구어~중립).
- 한국어: ~이 끝나기를 기다리는 중이다, ~에 걸려 있다
- 설명: `wait for` 는 그저 기다린다는 말이고 `wait on` 은 "그게 와야 내가 움직인다"는 의존 관계를 담는다. 업무 영어에서 막힌 이유를 한 단어로 댈 때 흔하다. 원문은 `should note it is waiting on VeritySEM/Provision onboarding`.
- 예문: The navigation regrouping is waiting on VeritySEM and Provision onboarding.
- 유사어: is blocked on (개발자 구어, 막혔다는 뜻이 더 강함), is pending (격식, 무엇을 기다리는지는 뒤에 따로), depends on (의존만 말하고 지금 멈췄는지는 안 말함)
- 반의어: is unblocked (막힌 게 풀렸다)

## "designed down to file and function names"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 설계가 얼마나 구체적인지를 "어느 수준까지 내려갔다"로 알릴 때(설계 리뷰·보고).
- 한국어: 파일명과 함수명 수준까지 설계가 끝난
- 설명: `down to X` 는 "가장 잔 단위인 X 까지"다. `accurate down to the millisecond`, `planned down to the last detail` 과 같은 틀이다. 원문은 그래서 이 항목들이 새 아이디어가 아니라 `"ready work"` 라고 잇는다.
- 예문: The unshipped items are already designed down to file and function names, so they are ready work, not new ideas.
- 유사어: specified in full detail (격식, 수준을 짚지는 않음), spelled out to the last function (구어), fully scoped (범위가 정해졌다는 쪽)
- 반의어: only sketched out (윤곽만 잡힌)

## "claims the data cannot support"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 데이터가 뒷받침하지 못하는 주장이라서 제안을 기각한다고 적을 때(리뷰·보고서, 격식).
- 한국어: 데이터로 뒷받침할 수 없는 주장
- 설명: `support a claim` 은 근거가 주장을 떠받친다는 연어다. 관계대명사를 생략한 `claims (that) the data cannot support` 꼴로 명사 뒤에 붙였다. 원문은 기각 사유 셋을 대시 뒤에 나란히 놓았다(`new collection state, cross-feature coupling in one component, and claims the data cannot support`).
- 예문: We dropped the utilisation figure because it was a claim the data cannot support.
- 유사어: unsupported claims (짧고 격식), claims that go beyond the data (얼마나 넘었는지를 강조), overreach (구어, 명사 하나로)
- 반의어: a well-supported claim (근거가 충분한 주장)

## "has to argue against the first reason explicitly"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 이미 기각된 사유가 있으니 새 제안은 그 사유를 정면으로 반박해야 한다고 조건을 달 때(제안서 심사·설계 논의).
- 한국어: 첫 번째 사유를 명시적으로 반박해야 한다
- 설명: `argue against` 는 "~에 반대 논거를 편다"이다. `explicitly` 가 끝에 와서 "슬쩍 넘어가지 말고 글로 적어서"를 요구한다. 주어가 사람이 아니라 `Any new opportunity that needs history` 인 점도 눈여겨볼 만하다. 영어는 제안 자체가 논증한다고 쓴다.
- 예문: Any proposal that needs stored history has to argue against the first reason explicitly.
- 유사어: has to address the objection head-on (구어~중립), must rebut (격식, 법률·학술 느낌), needs to make the case for (찬성 쪽 논거를 세운다는 방향)
- 반의어: can take it as given (전제로 받아들여도 된다)

## "deep at 'showing' and shallow at 'questioning'"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 제품이나 화면의 강점과 약점을 한 문장에 대칭으로 진단할 때(리뷰·회고, 중립).
- 한국어: "보여주기"는 깊고 "묻기"는 얕다
- 설명: `good at / bad at` 의 `at` 을 `deep / shallow` 에 그대로 붙였다. 반대말 한 쌍을 같은 틀에 넣으면 긴 진단이 한 줄로 줄어든다. 따옴표 친 동명사는 "이른바 ~하는 일"이라는 라벨 구실을 한다.
- 예문: The pages are deep at "showing" and shallow at "questioning": there is no baseline to compare against.
- 유사어: strong on display, weak on analysis (같은 대칭, 더 흔한 형용사), long on data and short on insight (관용적 대칭 `long on / short on`), shows a lot but asks little (구어)

## "(X) is the wrong tool"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 방법 선택이 문제의 성격과 안 맞는다고 잘라 말할 때(기술 논의, 구어~중립).
- 한국어: ~은 이 문제에 맞는 도구가 아니다
- 설명: 방법이 나쁘다는 말이 아니라 "이 일에는" 안 맞는다는 판정이다. 원문은 괄호로 이유를 붙였다(`the question is variance decomposition/state-space estimation, no labels exist`). `the right tool for the job` 의 반대편에 있는 말이다.
- 예문: Machine learning is the wrong tool here, because the question is variance decomposition and no labels exist.
- 유사어: is not a good fit for (부드러움), is overkill for (과하다는 쪽), doesn't apply here (적용 자체가 안 된다)
- 반의어: is the right tool for the job

## "several of their display choices are guesses"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 우리가 만든 것의 일부가 근거 없이 정한 것임을 숨기지 않고 밝힐 때(브리프·인계 문서).
- 한국어: 화면 표시 방식 가운데 몇몇은 짐작으로 정한 것이다
- 설명: `are guesses` 처럼 명사 보어로 닫으면 `were guessed` 보다 단정하고 짧다. 앞 문장 `The FDC and SCE panels were built on a mock, so …` 가 이유를 대고 이 절이 결과를 받는다. `several of` 가 "전부는 아니다"를 지킨다.
- 예문: The panels were built on a mock, so several of their display choices are guesses.
- 유사어: are educated guesses (근거가 조금은 있다는 쪽), are placeholders (나중에 바꿀 자리 표시), are unverified assumptions (격식)
- 반의어: are backed by measurements (실측에 근거한다)

## "exists to settle (a display decision)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 질문이나 작업의 존재 이유가 결정 하나를 끝내는 데 있다고 못 박을 때(조사 지시·브리프).
- 한국어: (화면 결정 하나를) 매듭짓기 위해 있다
- 설명: `settle` 은 논쟁이나 미결 사항을 끝낸다는 동사다(`settle a debate`, `settle the question`). `exists to` 는 목적을 주어의 존재 이유로 올려 말한다. 원문은 굵은 글씨로 `Every question below exists to settle a display decision.` 이라 쓰고 답하는 방식까지 지정한다.
- 예문: Every question below exists to settle a display decision, so answer with numbers.
- 유사어: is there to decide (구어), serves to resolve (격식), is meant to answer (목적만 말함)

## "need a longer baseline to show up"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 변화가 짧은 창에서는 안 보이고 긴 기준 구간이 있어야 드러난다고 설명할 때(데이터 분석).
- 한국어: 기준 구간이 더 길어야 드러난다
- 설명: `show up` 은 "나타나다, 눈에 띄다"이고 사람에게 쓰면 "모습을 보이다"다. 데이터에서는 신호가 그래프에 보이기 시작한다는 뜻으로 쓴다. `baseline` 은 비교의 바탕이 되는 구간이다.
- 예문: The page shows 30 days, but PM steps and re-tunes need a longer baseline to show up.
- 유사어: become visible only over a longer window (풀어 쓴 문어), don't stand out in a short window (부정으로 뒤집음), emerge over time (격식)
- 반의어: is washed out (묻혀서 안 보인다)

## "whether the (10,000) cap holds"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 정해 둔 상한이나 가정이 실제 데이터에서도 유지되는지 확인할 때(성능·용량 검토).
- 한국어: 상한이 (실제로도) 버티는지
- 설명: 자동사 `hold` 는 "성립한다, 유지된다"이다. `the assumption holds`, `the 30-min cycle split holds` 처럼 가정·규칙·한도를 주어로 받는다. 같은 문서가 `whether the 30-min cycle split holds` 로 한 번 더 쓴다.
- 예문: Count docs per tool per 30 days to see whether the 10,000 cap holds.
- 유사어: is enough (구어), is sufficient in practice (격식), stands up to real data (검증을 견딘다는 그림)
- 반의어: breaks down (무너진다), is exceeded (넘는다)

## "must not read as pass/fail"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 화면 요소나 문장이 사용자에게 다른 뜻으로 읽히면 안 된다고 요구할 때(UI 리뷰·카피 리뷰).
- 한국어: 합격/불합격으로 읽히면 안 된다
- 설명: 자동사 `read as` 는 "~로 읽힌다"이다. 글·표시가 주어가 되고 읽는 사람은 문장에 안 나온다. 원문은 `If it is the fit model, the badge must not read as pass/fail` 로, 피팅 모델 이름을 판정처럼 보이게 하지 말라는 조건문이다.
- 예문: If the token is the name of the fitted model, the badge must not read as pass/fail.
- 유사어: must not look like (보이는 쪽), must not be taken as (받아들이는 쪽, 수동), shouldn't come across as (구어, 인상)

## "a bare verdict"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 근거나 여유값 없이 판정 결과만 달랑 보여 주는 것을 가리킬 때(UI·리포트 설계).
- 한국어: (근거 없이) 판정만 달랑
- 설명: `bare` 는 "덧붙은 것이 없는"이다. `a bare number`, `the bare minimum`, `bare fields` 처럼 쓴다. 원문은 `show the margin to the threshold instead of a bare verdict` 로 대안을 함께 낸다. 판정 대신 임계까지 남은 여유를 보여 주자는 말이다.
- 예문: We can show the margin to the threshold instead of a bare verdict.
- 유사어: a verdict with no context (풀어 씀), just a pass/fail flag (구어), an unexplained result (설명이 없다는 쪽)
- 반의어: a verdict with its reasoning (근거가 딸린 판정)

## "separates jitter from real re-tunes"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md
- 맥락: 잡음과 실제 변화를 가르는 허용 오차나 기준을 정할 때(신호 분석·데이터 품질).
- 한국어: 잔떨림과 실제 재튜닝을 가른다
- 설명: `separate A from B` 는 둘을 구분해 낸다는 뜻이고 주어는 기준(`a tolerance`)이다. `jitter` 는 의미 없는 미세한 흔들림이다. 원문은 `name a tolerance that separates jitter from real re-tunes` 로, 그 기준값을 숫자로 대라고 요구한다.
- 예문: If unchanged days differ by about 1e-9, name a tolerance that separates jitter from real re-tunes.
- 유사어: tells noise apart from signal (구어), distinguishes A from B (격식), draws the line between (경계를 긋는다는 그림)
- 반의어: lumps them together (한데 뭉뚱그린다)

## "rewritten rather than left dangling"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 지운 것을 가리키던 참조를 끊긴 채 두지 않고 고쳐 썼다고 보고할 때(정리 작업 보고).
- 한국어: 끊긴 채 두지 않고 고쳐 썼다
- 설명: `dangling` 은 한쪽 끝이 어디에도 안 붙고 매달린 상태다. `a dangling pointer`, `a dangling reference` 에서 온 말을 문서 인용에 옮겨 썼다. `A rather than B` 는 과거분사 둘을 나란히 놓아 "B 하지 않고 A 했다"를 만든다.
- 예문: Six files that cited the deleted tickets were rewritten rather than left dangling.
- 유사어: repointed instead of left broken (새 대상을 가리키게 했다는 쪽), fixed up so nothing points nowhere (구어), updated rather than orphaned (`orphaned` 는 주인 잃은)

## "stands as is"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 이미 한 커밋이나 결정을 고칠 필요가 없다고 확인해 줄 때(리뷰 답변, 중립).
- 한국어: 지금 그대로 유효하다
- 설명: `stand` 는 결정·기록이 "효력을 유지한다"는 자동사다(`the ruling stands`). `as is` 는 "손대지 않은 그대로". 원문은 `so af8a5719 stands as is and nothing needs amending` 으로, 뒤 절에서 같은 말을 한 번 더 풀어 준다.
- 예문: That matches the commit message, so the commit stands as is and nothing needs amending.
- 유사어: is fine as it is (구어), needs no changes (결과만), can stay (가장 짧음)
- 반의어: needs amending (고쳐야 한다), has to be reverted

## "(the reasons) are my inference"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 내가 적은 설명이 확인된 사실이 아니라 추론임을 밝힐 때(커밋·보고, 중립).
- 한국어: (그 이유는) 제 추론입니다
- 설명: `I inferred the reasons` 보다 `the reasons are my inference` 가 "사실이 아니라 추론"이라는 지위를 더 또렷이 한다. 앞에 `I had no context on why these were removed, so …` 를 두어 왜 추론할 수밖에 없었는지부터 댄다. 바로 뒤 `Say so if they are wrong` 이 정정 길을 열어 둔다.
- 예문: I had no context on why these were removed, so the commit message's reasons are my inference.
- 유사어: are my best guess (구어, 확신이 더 낮음), are my reading of it (해석이라는 쪽), are an assumption on my part (격식)
- 반의어: are confirmed (확인된 것이다)

## "two more turned up in (X)"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 찾던 중에 예상 밖의 것이 더 나왔다고 알릴 때(진행 보고, 구어).
- 한국어: ~에서 두 건이 더 나왔다
- 설명: `turn up` 은 찾던 것이든 아니든 "불쑥 나타나다"이다. 내가 찾아냈다는 `I found` 와 달리 주어가 발견된 쪽이라 "나올 줄 몰랐는데 나왔다"는 느낌이 산다. 잃어버린 물건이 나올 때도 쓴다(`My keys turned up in the car`).
- 예문: Citations are stripped in 18 files; two more turned up in `.scratch/` tickets, so I'm clearing those too.
- 유사어: surfaced (조금 격식), showed up (구어, 거의 같은 뜻), came to light (문어, 숨어 있던 것이 드러남)

## "the sentence that existed only to carry it"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 링크나 인용을 담으려고만 있던 문장이라 함께 지웠다고 설명할 때(문서 정리 보고).
- 한국어: 그것을 싣기 위해서만 있던 문장
- 설명: `carry` 는 문장이 정보를 "싣고 있다"는 그림이다. `existed only to` 가 "다른 쓸모는 없었다"를 말해 지운 이유가 된다. 원문은 `Most edits just drop the pointer, or the sentence that existed only to carry it.` 로, 대부분의 수정이 단순 삭제였음을 한 문장에 정리한다.
- 예문: Most edits just drop the pointer, or the sentence that existed only to carry it.
- 유사어: a sentence that was just a wrapper for the link (개발자 구어), filler around the citation (낮춰 부름), a sentence with no other purpose (풀어 씀)

## "Three went further than a deletion"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 대부분은 단순 작업이었지만 몇 건은 그 이상을 했다고 예외를 따로 꺼낼 때(변경 요약).
- 한국어: 세 건은 삭제에 그치지 않았다
- 설명: `go further than X` 는 "X 에서 멈추지 않고 더 나아가다"이다. 앞 문장이 일반 규칙(`Most edits just drop …`)을 말하고 이 문장이 콜론 뒤에 예외 목록을 연다. 리뷰어가 어디를 자세히 봐야 하는지 알려 주는 구조다.
- 예문: Most edits just drop the pointer; three went further than a deletion.
- 유사어: Three needed more than a deletion (필요가 있었다는 쪽), Three were more involved (구어, `involved` 는 손이 많이 가는), In three cases I did more than delete (주어를 나로)

## "rather than lose them"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 버리는 대신 옮겨 적어 살렸다고 선택의 이유를 붙일 때(변경 설명).
- 한국어: 잃어버리느니 (차라리)
- 설명: `rather than` 뒤에 동사원형이 온다. 주절 동사가 과거(`inlined`)여도 `lose` 는 원형으로 둔다. `instead of losing them` 과 뜻은 같고 `rather than lose` 쪽이 "그 편을 택했다"는 의지가 더 묻어난다. `in condensed form` 은 "줄인 꼴로".
- 예문: I inlined three of its four checks in condensed form rather than lose them.
- 유사어: instead of losing them (동명사, 중립), so they aren't lost (목적절로 풀어 씀), to keep them from disappearing (구어)

## "Say if you want that pass."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 추가 작업 한 바퀴를 할지 상대 결정에 맡기며 보고를 닫을 때(채팅·리뷰 답변, 구어).
- 한국어: 그 작업도 한 번 돌릴지 말씀해 주세요
- 설명: `pass` 는 전체를 한 차례 훑는 작업 단위다(`a cleanup pass`, `a second pass`). `Say if …` 는 `Let me know if …` 보다 짧고 건조하다. `Say so if …` 는 앞말이 맞다면 그렇다고 해 달라는 뜻이라 쓰임이 조금 다르다.
- 예문: Each mention would need checking by hand. Say if you want that pass.
- 유사어: Let me know if you'd like me to go through them (정중), Want me to do that sweep? (구어 의문형), I can do that pass on request (문어)

## "Fix is in"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 수정을 코드에 넣었고 이제 검증으로 넘어간다고 짧게 알릴 때(진행 메모, 구어).
- 한국어: 수정 넣었음
- 설명: 관사를 뗀 메모 문체다. 온전히 쓰면 `The fix is in.` 이고 `in` 은 "코드에 들어갔다"이다. 원문은 세미콜론 뒤에 `now selecting models in the browser to confirm …` 을 이어 다음 단계를 말한다. 일상 영어에서 `the fix is in` 은 "짜고 치는 판이다"라는 숙어이기도 해서 개발 맥락 밖에서는 조심한다.
- 예문: Fix is in; now checking in the browser that every tool name shows on the heatmap.
- 유사어: The fix has landed (병합까지 됐다는 쪽), Patched (한 단어 메모), I've applied the fix (온전한 문장, 격식)

## "inferred from the code rather than observed"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [assistant]
- 맥락: 원인을 재현으로 본 것이 아니라 코드를 읽고 추정했다고 근거의 세기를 밝힐 때(버그 수정 보고).
- 한국어: 직접 본 것이 아니라 코드에서 추론한
- 설명: `inferred` 와 `observed` 는 근거의 등급을 가르는 한 쌍이다. 앞 절 `I did not reproduce the missing label before the change` 가 사실을 말하고 `so` 뒤가 그 결과로 근거가 약하다는 점을 적는다. 고쳤다는 보고에 이 한 줄이 붙으면 읽는 사람이 재발 가능성을 스스로 가늠한다.
- 예문: I did not reproduce the missing label before the change, so the cause is inferred from the code rather than observed.
- 유사어: is my reading of the code, not a repro (구어, `repro` 는 재현), is a deduction, not a measurement (대구), has not been confirmed empirically (격식)
- 반의어: reproduced and confirmed (재현해서 확인한)

## "(64 sender threads) pile up"
- 레지스터: technical, conversational
- 출처: transcript:auto-recipe-creator (code-review 결과)
- 맥락: 처리되지 못한 요청·스레드·일이 차곡차곡 쌓여 간다고 장애 시나리오를 묘사할 때.
- 한국어: (스레드가) 쌓인다, 밀린다
- 설명: `pile up` 은 치우는 속도보다 들어오는 속도가 빨라 더미가 되는 그림이다. 일감(`work piles up`), 요청, 미결 티켓에 두루 쓴다. 원문은 `Office cube I/O hangs and 64 sender threads pile up.` 으로 현재형 두 동사만으로 장애 장면을 세운다.
- 예문: Office cube I/O hangs and 64 sender threads pile up.
- 유사어: back up (흐름이 막혀 뒤로 밀림), accumulate (격식), queue up (줄을 선다는 쪽, 순서가 있음)
- 반의어: drain (빠져나가 비워진다)

## "the graph view just goes dark"
- 레지스터: technical, conversational
- 출처: transcript:auto-recipe-creator (code-review 결과)
- 맥락: 기능이 에러 없이 조용히 꺼져 아무것도 안 나오게 된다고 말할 때(장애 묘사, 구어).
- 한국어: 그래프 화면이 (소리 없이) 꺼진다
- 설명: `go dark` 는 불이 꺼지듯 신호·출력이 끊기는 것이다. 모니터링, 로그, 연락이 끊길 때 쓴다(`the sensor went dark`). `just` 가 "그 밖에 아무 일도 없이"를 더해 조용한 실패임을 강조한다.
- 예문: The TypeError is swallowed as a one-time warning, so the graph view just goes dark.
- 유사어: silently stops working (풀어 씀), goes blank (화면이 빈다는 쪽), drops off the radar (추적에서 사라짐)
- 반의어: comes back up (다시 살아난다)

## "the situation the raise was meant to surface"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator (code-review 결과)
- 맥락: 어떤 장치가 드러내려던 바로 그 상황이 여전히 묻힌다고 지적할 때(코드 리뷰).
- 한국어: 그 raise 가 드러내려던 바로 그 상황
- 설명: 타동사 `surface` 는 "숨은 것을 수면 위로 올리다"이다(`surface the error to the user`). `was meant to` 는 "그러라고 넣은 것인데"라는 뜻이어서 의도와 결과가 어긋났음을 한 구로 말한다. 관계대명사 `that` 이 생략된 꼴이다.
- 예문: The next alarm connects with the stale window still open, which is the situation the raise was meant to surface.
- 유사어: the very case it was supposed to catch (구어), the problem it was designed to expose (격식), exactly what the check was for (가장 평이)
- 반의어: bury (묻어 버린다), mask (가린다)

## "removes the trap"
- 레지스터: technical, conversational
- 출처: transcript:auto-recipe-creator (code-review 결과)
- 맥락: 지금은 버그가 아니지만 나중에 누군가 걸려 넘어질 코드를 고치자고 권할 때(코드 리뷰).
- 한국어: 함정을 없앤다
- 설명: 코드 리뷰에서 `trap` 은 당장은 멀쩡하지만 다음 사람이 밟을 덫이다. 비슷한 말로 `footgun`, `pitfall` 이 있다. 원문은 `a plain truthiness check with updated stubs removes the trap` 으로 해법을 주어에 세웠다.
- 예문: A plain truthiness check with updated stubs removes the trap.
- 유사어: closes the pitfall (문어), defuses the footgun (개발자 속어), makes it harder to get wrong (풀어 씀)
- 반의어: sets a trap for the next reader (다음 사람에게 덫을 놓는다)

## "statistics move with the selection"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 기준이 되어야 할 통계가 필터를 바꿀 때마다 같이 바뀐다고 문제를 짚을 때(대시보드 설계 리뷰).
- 한국어: 통계가 선택한 범위를 따라 움직인다
- 설명: `move with X` 는 "X 가 바뀌면 같이 바뀐다"이다. 원문은 괄호 안에서 `no comparison baseline` 의 이유로 썼다. 비교 기준이 고정되어 있지 않아 "평소보다 나쁜가"를 답하지 못한다는 진단이다.
- 예문: There is no comparison baseline, because the statistics move with the selection.
- 유사어: shift with the filter (구어), are relative to the current query (격식), have no fixed reference (기준이 없다는 쪽)
- 반의어: are pinned to a fixed baseline (고정 기준에 묶여 있다)
