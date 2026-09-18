# 2026-09-19 — 새 표현

> auto_recipe_creator 설계 문서 3건과 skewnono chat→RAG 계약 편지는 본문이 한국어라 표현을 뽑지 않았다. 19개 모두 transcript 의 어시스턴트 쪽 영어에서 나왔다(skewnono 16, equipment-data-map 2, auto-recipe-creator 1). 그중 2개는 simplify 리뷰 서브에이전트가 보낸 보고문이다. 노트에 이미 있는 `a false alarm`, `the culprit`, `your history moved under me`, `say the word`, `by design` 은 뺐다.

## "a guard doing its job, not a bug"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 에러를 낸 코드가 사실은 일부러 넣은 방어 로직이라 고칠 대상이 아니라고 짚을 때(버그 분석·채팅)
- 한국어: 버그가 아니라 제 할 일을 한 방어 코드다
- 설명: 원문은 `Line 201 of _office_search.py is a guard doing its job, not a bug.` 에러 메시지를 본 사람은 그 줄을 고치고 싶어 한다. 이 문장은 `A, not B` 틀로 그 반응을 먼저 막는다. `doing its job` 은 사물을 일하는 사람처럼 그려 "제대로 작동한 결과"라는 판정을 짧게 전한다.
- 예문: The 409 you got is the lock check doing its job, not a bug — someone else was editing the same row.
- 유사어: working as intended (중립·가장 흔함), a symptom, not the disease (원인은 다른 데 있다는 쪽으로), the check is right to refuse (거절이 옳다는 쪽)
- 반의어: a genuine bug, a false positive

## "hide the evidence"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 에러 메시지나 로그가 원인 진단에 필요한 정보를 버리고 있다고 지적할 때(디버깅·리뷰)
- 한국어: 단서를 감추다
- 설명: 원문은 `The backend is hiding the evidence though.` 앞 문장에서 "백엔드 잘못이 아니다"라고 해 놓고 `though` 로 한 발 물러선다. 백엔드가 범인은 아니지만 수사를 방해하고 있다는 그림이다. 범죄 수사 어휘(`evidence`, `culprit`, `suspect`)는 디버깅 대화에서 자주 빌려 쓴다.
- 예문: The retry wrapper swallows the original exception, so it's hiding the evidence every time the job fails.
- 유사어: swallow the error (예외를 삼킨다, 기술적), throw away the details (평이), obscure the root cause (문어)
- 반의어: surface the cause, preserve the context

## "so the next incident diagnoses itself"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 지금 당장 고치는 게 아니라 다음 장애 때 원인이 바로 보이게 로그·메시지를 보강하자고 제안할 때(설계 제안·리뷰)
- 한국어: 다음에 터지면 원인이 저절로 드러나도록
- 설명: 원문은 `One-line change so the next incident diagnoses itself`. `diagnose` 는 보통 사람이 주어인 타동사인데 여기서는 `itself` 를 목적어로 받아 장애가 스스로를 진단한다고 썼다. 에러 메시지에 원인을 실어 두면 사람이 따로 조사할 필요가 없다는 뜻이 한 동사에 담긴다.
- 예문: Let's log the full request ID and payload size so the next incident diagnoses itself.
- 유사어: make the next failure self-explanatory (조금 더 격식), leave a breadcrumb for next time (구어), make it debuggable (평이)
- 반의어: fail silently, leave us guessing

## "a hygiene step, not a prerequisite"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 해 두면 좋지만 지금 작업을 막는 조건은 아니라고 우선순위를 낮출 때(업그레이드 검토·계획)
- 한국어: 선행 조건이 아니라 해 두면 좋은 정리 작업
- 설명: 원문은 `Bumping to opensearch-py 3.x at some point is a reasonable hygiene step, not a prerequisite.` `hygiene` 은 위생에서 온 말로, 당장 아프진 않지만 꾸준히 챙기면 좋은 관리를 가리킨다. `prerequisite` 은 "먼저 끝내야 다음으로 갈 수 있는 것"이다. 두 단어를 `A, not B` 로 맞세워 "해도 되지만 기다릴 필요는 없다"를 정확히 말한다.
- 예문: Renaming the old config keys is a hygiene step, not a prerequisite for the release.
- 유사어: nice to have, not a blocker (구어), housekeeping (가벼운 명사), a follow-up item (계획 문서체)
- 반의어: a blocker, a hard requirement

## "rediscover each bug one incident at a time"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 이미 쌓인 지식을 버리고 새로 만들면 같은 실수를 장애마다 다시 겪게 된다고 반대할 때(설계 토론)
- 한국어: 버그 하나하나를 장애 때마다 다시 발견하다
- 설명: 원문은 `A fresh text-to-DSL path in _rag/ would rediscover each of those bugs one incident at a time.` 기존 어댑터 16개에 녹아 있는 함정을 새 경로는 모른다는 말이다. `one … at a time` 은 "하나씩 차례로"라서 비용이 한 번에 오지 않고 운영 중에 조금씩 새어 나온다는 느낌을 준다. 가정법 `would` 로 "그렇게 만들면"을 깔았다.
- 예문: If we rewrite the parser from scratch, we'll rediscover every edge case one support ticket at a time.
- 유사어: relearn the same lessons the hard way (구어), reinvent the wheel, bugs included (비꼬는 어감), repeat past mistakes (평이)
- 반의어: build on what we already know, reuse the hardened path

## "a letter, not an edit"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 다른 팀이 소유한 코드는 직접 고치지 말고 요청을 보내라는 경계 규칙을 한 줄로 정할 때(협업 규칙·문서)
- 한국어: 직접 고치지 말고 편지로 요청할 일
- 설명: 원문은 `data_tools.py is chat-side owned, so a field they want added is a letter, not an edit.` 이 프로젝트에서 "편지"는 두 에이전트가 주고받는 계약 문서다. 명사 두 개를 대비시켜 "소유자가 다르면 경로도 다르다"를 규칙으로 만든다. 주어 `a field they want added` 는 `want + 목적어 + 과거분사` 구조다.
- 예문: The schema belongs to the data team, so a column you want added is a ticket, not a commit.
- 유사어: a request, not a change (평이), goes through the owner (격식), ask, don't touch (구어)
- 반의어: just patch it yourself

## "theme-blind"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 어떤 산출물이 앱의 테마·색 토큰을 모르고 만들어진다는 단점을 짚을 때(프런트엔드 설계)
- 한국어: 테마를 모르는
- 설명: 원문은 `Do not have the LLM emit an ECharts option: it is large, theme-blind, easy to get subtly wrong, …` `color-blind` 에서 틀을 빌린 복합 형용사로, `명사-blind` 는 "~를 보지 못하는, ~을 고려하지 않는"이다. 형용사 네 개를 쉼표로 나열해 거절 사유를 한꺼번에 댔다.
- 예문: Hard-coded hex colors are theme-blind, so the chart looks wrong the moment someone switches to dark mode.
- 유사어: unaware of the theme (풀어 쓴 형태), context-blind (더 넓은 뜻), doesn't respect the design tokens (구체적)
- 반의어: theme-aware, token-driven

## "That explains it better than my guess."
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 상대가 내 추측보다 그럴듯한 원인을 댔을 때 순순히 인정하며 받을 때(채팅·회의)
- 한국어: 제 추측보다 그게 더 잘 설명되네요
- 설명: 사용자가 "커서가 버튼 위에 있어서 실패한 것 같다"고 하자 나온 답이다. 틀렸다고 사과하지 않고 두 설명을 비교해 더 나은 쪽을 고르는 말투라 자존심 싸움 없이 방향을 바꾼다. 바로 뒤에 "그래서 코드 주석을 고치겠다"는 행동을 붙였다.
- 예문: Oh, the proxy strips the header? That explains it better than my guess.
- 유사어: That fits better than my theory. (거의 같음), Good call, that makes more sense. (더 구어), That's a more plausible explanation. (격식)
- 반의어: I don't think that's it.

## "a placeholder posed as a pick"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 기본값이 사용자가 실제로 고른 값처럼 취급돼 버그가 났다고 설명할 때(버그 보고)
- 한국어: 자리 표시용 기본값이 사용자 선택인 척했다
- 설명: 원문은 `A placeholder posed as a pick.` 동사 `pose as` 는 "~인 척하다, ~로 행세하다"다. 링크에 기본으로 찍힌 `mp=WAFER` 를 코드가 사용자의 명시적 선택으로 존중했다는 버그를 다섯 단어로 요약했다. `placeholder` 와 `pick` 의 p 두운도 기억을 돕는다.
- 예문: The empty filter wasn't a user choice; it was a placeholder posed as a pick, and the query honored it.
- 유사어: a default mistaken for a choice (풀어 쓴 평이체), a fake selection (구어), an implicit value treated as explicit (문어·기술)
- 반의어: an explicit choice, a real selection

## "keep the honest blank"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 억지로 값을 채워 보여 주느니 "보여 줄 게 없다"는 빈 화면이 정직하다는 선택지를 제시할 때(설계 판단)
- 한국어: 정직한 빈 화면을 유지하다
- 설명: 원문은 `Revert the second commit if you would rather keep the honest blank there.` 빈 화면을 `honest` 로 수식해 "틀린 답보다 나은 무응답"이라는 가치 판단을 실었다. `would rather` 는 사용자의 선호를 묻는 정중한 조건이다. 자기 변경을 되돌릴 방법까지 알려 주며 결정을 넘기는 문형이다.
- 예문: If the fallback value feels misleading, we can keep the honest blank and show "no shared parameter" instead.
- 유사어: show nothing rather than something wrong (풀어 쓴 형태), fail visibly (기술), leave it empty on purpose (평이)
- 반의어: paper over it, show a misleading default

## "caught mid-frame"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 스크린샷의 이상한 모습이 버그가 아니라 애니메이션 도중에 찍혀서라고 설명할 때(UI 검증)
- 한국어: 애니메이션 중간에 찍혔다
- 설명: 원문은 `The band edge is just the ECharts area animation caught mid-frame at 600ms.` `catch` 는 "순간을 포착하다"이고 `mid-` 접두사는 "~의 한가운데"다(`mid-sentence`, `mid-flight`). `just` 로 문제의 크기를 줄이고, 근거로 `the earlier post-hover shot showed it complete` 를 붙였다.
- 예문: The half-drawn bar isn't a rendering bug; the screenshot just caught it mid-frame.
- 유사어: caught mid-animation (거의 같음), a timing artifact (기술 명사), snapped before it finished (구어)
- 반의어: the final rendered state

## "Deferring is defensible; writing it twice in one file is not."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (simplify 리뷰 에이전트 보고)
- 맥락: 리팩터링을 미루는 건 이해하지만 같은 파일에서 중복을 새로 만드는 건 안 된다고 선을 그을 때(코드 리뷰)
- 한국어: 미루는 건 변명이 되지만, 한 파일에 두 번 쓰는 건 아니다
- 설명: 세미콜론 앞뒤로 같은 술어를 긍정과 부정으로 맞세운 대구다. 뒤쪽은 `is not (defensible)` 에서 형용사를 생략했다. 리뷰어가 상대 선택의 일부는 인정하면서 받아들일 수 없는 부분만 정확히 겨냥한다.
- 예문: Skipping the migration for now is defensible; adding a third copy of the same helper is not.
- 유사어: I get postponing it, but not duplicating it. (구어), The delay is acceptable; the duplication isn't. (격식 평서), Fine to wait, not fine to copy. (짧은 구어)
- 반의어: (마땅한 대체 표현 없음)

## "stop being the default move"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (simplify 리뷰 에이전트 보고)
- 맥락: 공용 컴포넌트를 만들어 두면 사람들이 습관처럼 복붙하던 관행이 멈춘다고 설득할 때(리팩터링 제안)
- 한국어: 습관처럼 하던 선택이 아니게 되다
- 설명: 원문은 `the eighth copy stops being the default move`. `move` 는 체스·게임의 "수"로, `the default move` 는 생각 없이 두는 기본 수다. 중복 코드의 진짜 비용이 "다음 사람도 복사하게 된다"는 데 있다는 관점을 담았다.
- 예문: Once there's a shared date formatter, copy-pasting one stops being the default move.
- 유사어: stop being the path of least resistance (조금 더 문어), no longer the go-to (구어), stop being the habit (평이)
- 반의어: become the norm, the path of least resistance

## "has nothing to do with load"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 상대가 의심한 원인과 실제 실패 원인이 무관하다고 분리할 때(장애 분석·질문 답변)
- 한국어: 부하와는 아무 상관이 없다
- 설명: 원문은 `The one way the restart genuinely fails has nothing to do with load.` 사용자는 "사람들이 많이 쓰면 재시작이 실패하느냐"고 물었다. 답은 "실패할 수 있다, 다만 네가 의심한 이유로는 아니다"이다. `genuinely` 가 "진짜로 실패하는 유일한 경우"를 앞선 가벼운 손실들과 가른다.
- 예문: The timeout has nothing to do with the database; the DNS lookup is what's slow.
- 유사어: is unrelated to (격식), isn't about (구어), is independent of (문어·기술)
- 반의어: is caused by, comes down to

## "look fine all day and take the instance down at night"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 문제가 당장은 안 보이다가 특정 시점(재시작·배포)에만 터지는 지연형 위험을 경고할 때(운영 리뷰)
- 한국어: 하루 종일 멀쩡해 보이다가 밤에 인스턴스를 죽이다
- 설명: 원문은 `A daytime overlay that broke one of these would look fine all day and take the instance down at 00:05.` 주어 하나에 동사구 둘을 `and` 로 이어 "멀쩡함 → 붕괴"의 대비를 한 문장에 넣었다. `take … down` 은 서버·서비스를 멈추게 하다. 시각을 구체적으로 적어 위험이 현실로 느껴지게 한다.
- 예문: A bad env var would look fine all day and take the service down at the next deploy.
- 유사어: a time bomb (명사 비유), fail only on restart (기술 평서), bite you later (구어)
- 반의어: fail fast, break immediately

## "To be precise for the record"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 상대가 대화를 끝내려 할 때 오해가 남지 않게 결론을 한 번 더 정확히 적어 둘 때(회의 마무리·기록)
- 한국어: 기록 삼아 정확히 말씀드리면
- 설명: 원문은 `Understood. To be precise for the record: load cannot stop the reload, …` 사용자가 조건을 반대로 말해 모호해진 상황에서 나온 말이다. `for the record` 는 "공식 기록으로 남기자면", `to be precise` 는 "정확히 하자면"이다. 둘을 겹쳐 반박이 아니라 정리라는 어조를 만든다.
- 예문: Understood. To be precise for the record, the backup ran; only the upload step failed.
- 유사어: Just to be clear (구어), For clarity (문어·짧음), Let me state it exactly (격식)
- 반의어: (마땅한 대체 표현 없음)

## "a refresh, not a restart"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 업데이트를 적용하려면 처음부터 다시 할 필요 없이 갱신만 하면 된다고 안심시킬 때(운영 안내)
- 한국어: 재시작이 아니라 새로 고침
- 설명: 원문은 `It's a refresh between sessions, not a restart.` 사용자는 "어떻게 다시 시작하느냐"고 물었는데 답은 질문의 전제(`start`)를 부드럽게 고친다. `between sessions` 가 언제 하는지까지 알려 준다. `A, not B` 틀은 이 대화 전체에 반복되는 핵심 문형이다.
- 예문: You don't need to reinstall anything; it's a refresh between runs, not a restart.
- 유사어: an update in place (기술), just a reload (구어), an incremental update (격식)
- 반의어: a fresh start, a full reset

## "lives in the ledger, not in your memory"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 무엇을 다시 해야 하는지를 사람이 기억할 필요 없이 기록이 판단한다고 설계를 설명할 때(설계 설명)
- 한국어: 판단 근거가 사람 기억이 아니라 장부에 있다
- 설명: 원문은 `Redo detection lives in the ledger, not in your memory.` 기능이나 정보가 어느 계층에 있는지를 `lives in` 으로 말하는 건 개발자 영어의 흔한 비유다. 뒤에 `not in your memory` 를 붙여 사용자에게서 책임을 덜어 준다.
- 예문: The retry state lives in the database, not in the worker, so a crash doesn't lose it.
- 유사어: is tracked by (평이), is recorded in (격식), X keeps track, so you don't have to (구어)
- 반의어: relies on someone remembering

## "grey out / snap back"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: UI 옵션이 조건에 따라 비활성화되고 선택값이 기본으로 돌아가는 동작을 설명할 때(UI 변경 보고)
- 한국어: 회색으로 비활성화되다 / 원래 값으로 되돌아가다
- 설명: 원문은 `95% 신뢰/예측 grey out under 원본만 or an insufficient fit, and snap back to IQR if the fit disappears.` `grey out` 은 자동사·타동사 모두 되는 UI 동사구다(`grey` 영국식, `gray` 미국식). `snap back` 은 고무줄처럼 "탁 원위치로 돌아가다"라 자동 복귀의 순간성이 느껴진다.
- 예문: The Export button greys out while the query runs and snaps back once the results arrive.
- 유사어: be disabled (중립·기술), revert to (격식), reset to (평이)
- 반의어: become enabled, stick (선택이 유지되다)
