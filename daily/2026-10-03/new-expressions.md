# 2026-10-03 — 새 표현

> 오늘 배치는 repo 문서 14건과 transcript 3건이다(1건은 `/clear` 만 찍힌 빈 세션). repo 문서는 AFM 질문서·스키마, 장비 계열 온보딩 규약, DL 학습 계획으로 거의 전부 한국어라 표현은 transcript 에서만 골랐다. 재료가 가장 많은 곳은 auto_recipe_creator 세션의 리뷰 보고서들이다. `/simplify` 관점별 보고 넷, Codex 설계 리뷰, Codex 코드 리뷰 두 차례가 영어로 돌아와 "고칠 것 / 미룰 것 / 안 고칠 것"을 가르는 말이 많았다. 세션에 딸려 온 스킬 문서(browser-verify, tdd)에서도 몇 개 골랐다. `one-for-one`, `reach for`, `not retroactive`, `treat every ID as an opaque string`, `Inspect before waiting.`, `tracer bullet`, `reads like a specification`, `X beats Y`, `the same class of bug as X`, `a fragile bandaid` 는 노트에 이미 있어서 뺐다.

## "Nothing worth fixing on the efficiency angle"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (simplify 리뷰, efficiency 보고서)
- 맥락: 맡은 관점에서 봤지만 고칠 게 없다고 첫 줄에 결론부터 보고할 때(리뷰 보고, 중립).
- 한국어: 효율 관점에서는 고칠 만한 게 없다
- 설명: `nothing worth -ing` 는 "~할 만한 게 없다". `worth` 뒤에는 동명사가 바로 온다. `on the X angle` 은 리뷰를 관점별로 나눴을 때 자기 몫을 가리키는 말. 원문은 세미콜론 뒤에 근거를 붙여 한 줄로 끝냈다.
- 예문: Nothing worth fixing on the efficiency angle; the diff adds no wasted work.
- 유사어: No findings from an efficiency standpoint (격식), Efficiency-wise, it's clean (구어), Nothing to flag here (관점을 안 밝힐 때)
- 반의어: Three findings on the efficiency angle (지적이 있을 때)

## "noise next to the VLM/OCR calls"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator (simplify 리뷰, efficiency 보고서)
- 맥락: 비용이 있긴 해도 옆의 큰 비용에 견주면 무시해도 된다고 할 때(성능 리뷰, 구어 섞인 기술 글).
- 한국어: VLM/OCR 호출 옆에서는 잡음 수준
- 설명: `noise` 는 측정에서 의미 없는 흔들림이다. `next to` 는 여기서 "~에 비하면"으로, `compared with` 의 구어판. 원문은 비용을 먼저 인정한 뒤 쉼표 하나로 크기를 매겼다.
- 예문: Cost is env parsing plus a millisecond-scale window enumeration, noise next to the VLM/OCR calls.
- 유사어: negligible compared with X (격식), a rounding error next to X (구어), dwarfed by X (큰 쪽을 강조)
- 반의어: the dominant cost (지배적인 비용)

## "a separate refactor, not this diff"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (simplify 리뷰, reuse 보고서)
- 맥락: 맞는 개선이지만 이번 변경에 넣을 일은 아니라고 선을 그을 때(코드 리뷰).
- 한국어: 별도 리팩터 거리이지 이번 diff 가 아니다
- 설명: `A, not B` 로 범위를 가른다. 원문 주어 `Promoting an env_str` 의 `promote` 는 한 파일 안에 숨은 헬퍼를 공용으로 올린다는 뜻. 같은 관용구가 17곳에 있다는 숫자를 먼저 대고 이 문장으로 닫았다.
- 예문: Promoting an `env_str` is a separate refactor, not this diff.
- 유사어: out of scope for this PR (가장 흔한 말), belongs in its own change (따로 하자는 쪽을 강조), a follow-up, not a blocker (우선순위로 말하기)
- 반의어: fold it into this diff (이번에 같이 넣다)

## "none blocking"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (simplify 리뷰, simplification 보고서)
- 맥락: 지적은 있지만 머지를 막을 정도는 아니라고 요약 첫 줄에서 알릴 때(리뷰 보고).
- 한국어: 막을 만한 건 없음
- 설명: `none (of them is) blocking` 을 줄인 말이다. `blocking` 은 "이게 풀려야 다음으로 간다"는 리뷰 용어. 세미콜론 뒤의 `otherwise` 는 "그 밖에는"이다. 개수, 심각도, 나머지 상태를 한 줄에 담았다.
- 예문: Three small findings, none blocking; otherwise the diff is clean.
- 유사어: no blockers (명사형), all non-blocking (형용사형), nothing that should hold up the merge (풀어 쓴 말)
- 반의어: one blocker, a must-fix (꼭 고쳐야 할 것)

## "not made worse by the diff"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (simplify 리뷰, simplification 보고서의 "Checked and clean")
- 맥락: 문제는 있지만 이번 변경이 키운 건 아니라서 손대지 않는다고 할 때(코드 리뷰).
- 한국어: 이번 diff 때문에 나빠진 건 아니다
- 설명: 수동태 `made worse by` 로 책임 소재를 가린다. 원문은 바로 뒤에 `not trivially removable`(간단히 뺄 수도 없다)을 `and` 로 이어 "이번엔 안 건드린다"의 근거를 둘 댔다. `since` 절이 그 이유.
- 예문: Double window lookup (`:249`): not made worse by the diff and not trivially removable, since `manual_click_button.main` returns only an int.
- 유사어: pre-existing (한 단어로), not a regression (회귀가 아니다), no worse than before (비교급으로)
- 반의어: introduced by this diff, a regression

## "no longer advertised"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (simplify 리뷰, simplification 보고서의 "Checked and clean")
- 맥락: 기능은 살아 있는데 문서에서 더는 안내하지 않는다고 구분할 때(코드·문서 리뷰).
- 한국어: 더는 안내하지 않는
- 설명: `advertise` 는 광고에서 넓어져 문서나 도움말이 "이런 게 있다"고 알리는 일을 가리킨다. 원문의 `knob` 은 조절 손잡이, 곧 설정값. `still live, not dead` 로 죽은 코드가 아님을 먼저 못 박았다.
- 예문: `SAFE_MODE` handling (`:230`, `:283`) and the `[dry-run]` suffix (`:298`) are still live, not dead — the knob still works and is just no longer advertised in this file.
- 유사어: undocumented (문서에 없다), soft-deprecated (쓰지 말라고 권하는 단계), hidden but supported (숨겼지만 지원)
- 반의어: documented, removed

## "go one step further"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)
- 맥락: 방향은 맞으니 한 걸음만 더 가자고 권할 때(리뷰 판정, 회의).
- 한국어: 한 걸음 더 나아가다
- 설명: 정도를 말할 때는 `further` 를 쓴다(`farther` 는 실제 거리). 원문은 `to (c)` 를 붙여 어디까지 가라는지 밝혔다. `Verdict:` 라벨 덕에 첫 줄에서 결론이 난다.
- 예문: Verdict: go one step further to (c).
- 유사어: take it a step further (흔한 변형), finish the job (구어, 더 세다), extend the fix to X (격식)
- 반의어: stop here, dial it back (되돌리다)

## "half-applied"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)
- 맥락: 고친 방식은 옳은데 절반만 적용됐다고 지적할 때(코드 리뷰).
- 한국어: 반만 적용된
- 설명: `half-` 에 과거분사를 붙이는 틀이다. `half-done`, `half-baked`, `half-migrated` 가 같은 식. 원문은 `is the right mechanism, but` 으로 칭찬을 먼저 두고 한계를 뒤에 붙였다.
- 예문: The optional-arg fix is the right mechanism, but it is half-applied.
- 유사어: only partly applied (풀어 쓴 말), applied to one of two cases (구체적으로), incomplete (범용)
- 반의어: applied across the board (전부에 적용된)

## "net about zero lines"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)
- 맥락: 제안한 수정이 코드 양을 늘리지 않는다고 덧붙일 때(리뷰 제안).
- 한국어: 줄 수 증감이 거의 0
- 설명: `net` 은 더하고 뺀 뒤 남는 순(純) 양이다. `net +3 lines`, `net negative` 처럼 쓴다. 원문은 소제목 `Change (c) — net about zero lines, backward compatible:` 로, 변경의 비용과 안전성을 두 마디로 요약했다.
- 예문: The change is net about zero lines and stays backward compatible. (작성)
- 유사어: roughly line-neutral (형용사로), adds as many lines as it removes (풀어 쓴 말), no net increase in code (격식)
- 반의어: net +40 lines, a net increase

## "Defer it."
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)
- 맥락: 근본 원인은 맞지만 이번에 하기엔 크니 미루자고 짧게 결정할 때(리뷰, 회의).
- 한국어: 미루자
- 설명: `defer` 는 판단해서 뒤로 넘긴다는 말이다. `postpone` 은 일정을 늦추는 쪽, `put off` 는 구어. 원문은 `(d) is the real root` 라고 인정한 다음 `too large for this diff. Defer it.` 두 단어로 끊었다.
- 예문: The real fix needs a 170-line refactor, so defer it to a follow-up. (작성)
- 유사어: Park it for now (구어), Leave it for a follow-up (다음 작업을 명시), Punt on it (미국 구어)
- 반의어: Fix it in this diff

## "got the … treatment and these did not"
- 레지스터: conversational, technical
- 출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)
- 맥락: 한 곳만 고치고 같은 종류의 다른 곳은 빠뜨렸다고 짚을 때(리뷰, 구어).
- 한국어: 저긴 그 처리를 받았는데 여긴 안 받았다
- 설명: `get the X treatment` 는 "X 식 처리를 받다"다. 원문은 `treatment` 앞에 코드 조각을 그대로 넣었다. `and these did not` 은 `did not get it` 을 줄인 꼴. 일관성 지적을 탓하는 기색 없이 한다.
- 예문: `manual_open_recipe.py:237` got the `or '(열린 tool 창)'` treatment and these did not.
- 유사어: was given the same fix (평이), was handled the same way (중립), got the same fallback (구체적으로)
- 반의어: was left untouched

## "a hypothesis, not something I tested"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Codex 설계 리뷰 Q1)
- 맥락: 주장을 내놓으면서 실제로 돌려 본 건 아니라고 스스로 밝힐 때(리뷰, 보고).
- 한국어: 가설이지 내가 시험해 본 게 아니다
- 설명: `something I tested` 는 관계사 `that` 이 빠진 꼴이다. 노트의 `a hypothesis, not a verdict` 가 결과의 지위를 말한다면 이 문장은 내가 한 일의 범위를 말한다. 권고 바로 뒤에 붙어 독자가 무게를 조절하게 한다.
- 예문: This is a hypothesis, not something I tested.
- 유사어: untested, reasoning only (짧게), I haven't verified this (직설), speculative on my part (격식)
- 반의어: reproduced, confirmed by a test

## "closeness in time does not prove that the earlier action caused the change"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (Codex 설계 리뷰 Q2)
- 맥락: 시간상 가깝다는 것만으로 원인이라 볼 수 없다고 반박할 때(설계 리뷰, 분석 글).
- 한국어: 시간상 가깝다고 앞선 동작이 그 변화를 일으켰다는 증거는 아니다
- 설명: "상관은 인과가 아니다"를 이 사례에 맞춰 풀어 쓴 문장이다. `closeness` 는 `close` 의 명사형. 무생물을 주어로 세우고 `does not prove that` 을 붙이면 상대의 추론만 겨냥하게 된다.
- 예문: The transitive chain can suppress indefinitely while changes keep arriving, and closeness in time does not prove that the earlier action caused the change.
- 유사어: correlation is not causation (격언), just because B followed A doesn't mean A caused it (구어), temporal proximity is not evidence of causation (격식)
- 반의어: X directly caused Y (인과를 단언)

## "fix the bookkeeping"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Codex 설계 리뷰 Q3)
- 맥락: 핵심 설계는 동의하지만 건수·기간·참조 번호 같은 부수 기록이 틀렸다고 할 때(리뷰).
- 한국어: 부기(장부)를 바로잡아라
- 설명: `bookkeeping` 은 원래 회계 장부 정리다. 코드에서는 카운터, 합계, 순번처럼 본 로직 옆에서 맞춰 줘야 하는 기록을 가리킨다. 원문 소제목은 `agree with X, but …` 로 동의와 조건을 한 줄에 실었다.
- 예문: Q3: agree with interleave-after, but fix the bookkeeping.
- 유사어: fix the counters and totals (구체적으로), tidy up the accounting (같은 은유), housekeeping (더 가벼운 정리)
- 반의어: rework the core logic (본 로직을 다시 짜다)

## "aborts the whole run"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차)
- 맥락: 부가 기능 하나의 실패가 실행 전체를 끝내 버린다고 결함을 보고할 때(버그 리포트).
- 한국어: 실행 전체를 중단시킨다
- 설명: `abort` 는 도중에 끝내 버린다는 뜻. `whole` 이 피해 범위를 키워 보여 준다. 무생물 주어에 현재시제라 한 번 일어난 일이 아니라 코드의 성질로 읽힌다.
- 예문: An overlay failure aborts the whole run.
- 유사어: kills the entire run (구어), takes down the whole pipeline (비유), is fatal to the run (격식)
- 반의어: is logged as a warning and the run continues

## "failure isolation"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차)
- 맥락: 한 부분의 실패가 다른 부분으로 번지지 않게 가둔다는 성질을 말할 때(설계·테스트).
- 한국어: 실패 격리
- 설명: 명사 둘을 붙인 용어다. 원문은 고친 뒤 그 성질을 지키는 회귀 테스트를 요구했다. 같은 보고서의 `Stage 2a absorbs the failure`(실패를 받아 삼킨다)가 격리가 된 쪽의 예.
- 예문: Add a regression test for this failure isolation.
- 유사어: fault containment (격식), graceful degradation (기능을 줄여서 계속 간다), blast-radius control (피해 반경 관리)
- 반의어: cascading failure (연쇄 실패)

## "sorts before"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차)
- 맥락: 문자열 정렬에서 어느 값이 어느 값 앞에 놓이는지 말할 때(버그 설명).
- 한국어: 정렬하면 ~앞에 온다
- 설명: `sort` 를 자동사로 쓴 꼴이다. 값이 주어가 되어 "정렬되면 어디에 선다"를 말한다. `Once` 는 "일단 ~하면"으로 버그가 드러나는 문턱을 가리킨다.
- 예문: Once a recording holds more than 9,999 frames, `10000` sorts before `1000`.
- 유사어: comes before X in lexical order (풀어 쓴 말), is ordered ahead of X (수동), collates before X (격식, 드묾)
- 반의어: sorts after

## "I did not verify that coverage myself."
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차, 중계 에이전트의 덧붙임)
- 맥락: 남의 결과를 전하면서 내가 직접 확인한 범위가 아니라고 밝힐 때(보고, 격식).
- 한국어: 그 범위는 제가 직접 확인하지 않았습니다
- 설명: `that coverage` 는 방금 말한 "Codex 가 본 범위"를 받는다. 문장 끝의 `myself` 가 "직접"이다. 중계자가 전달과 검증을 섞지 않으려고 넣는 한 줄.
- 예문: I did not verify that coverage myself.
- 유사어: I'm relaying this unverified (전달만 한다), I haven't checked this independently (격식), take this as reported (구어)
- 반의어: I confirmed this myself

## "Nothing further to report."
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차)
- 맥락: 보고서의 한 칸에 더 적을 게 없다고 명시할 때(보고서, 격식).
- 한국어: 더 보고할 것 없음
- 설명: 앞에 `There is` 가 빠진 정형구다. `further` 는 "추가의". 칸을 비워 두면 안 본 건지 없는 건지 모르니 "없음"을 적는다. 원문은 `PLAUSIBLE` 칸 아래 이 한 줄만 두었다.
- 예문: I have nothing further to report on the remaining items. (작성)
- 유사어: No further findings (격식), Nothing else to flag (구어), That's all from my side (회의)
- 반의어: One more thing: (더 있을 때)

## "admits the same noise"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (Codex 설계 리뷰 Q1)
- 맥락: 좁게 잡은 규칙도 결국 같은 잡음을 통과시킨다고 지적할 때(설계 리뷰).
- 한국어: 같은 잡음을 들여보낸다
- 설명: `admit` 의 "인정하다"가 아닌 "들여보내다" 쪽 뜻이다(입장 허가의 admission). 규칙이나 필터가 주어일 때 이 뜻으로 읽는다. 노트의 `The comment admits …` 와 같은 동사, 다른 뜻.
- 예문: The narrow rule admits the same noise whenever cursor detection fails.
- 유사어: lets in the same noise (구어), doesn't keep out X (부정으로), is open to the same noise (상태로)
- 반의어: filters out, rejects

## "hijack the tab"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 병렬로 도는 다른 에이전트·프로세스가 내가 쓰던 자원을 가로챈다고 할 때(작업 규칙, 구어 섞인 기술 글).
- 한국어: 탭을 가로채다
- 설명: `hijack` 은 납치에서 넓어져 남이 쓰던 것을 중간에 빼앗아 쓴다는 뜻이다. `so (that) … cannot` 은 목적절로, 규칙 뒤에 이유를 바로 붙이는 틀.
- 예문: Always work in a named session so a parallel agent cannot hijack the tab.
- 유사어: take over the tab (중립), steal focus (포커스만 뺏을 때), clobber the session (덮어써 망가뜨릴 때)
- 반의어: leave the tab alone

## "Gotchas seen so far:"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 써 보다가 걸려든 함정을 목록으로 남길 때(문서 소제목, 구어).
- 한국어: 지금까지 겪은 함정:
- 설명: `gotcha` 는 `got you` 에서 왔고 모르면 당하는 함정을 가리킨다. `seen so far` 는 과거분사가 뒤에서 꾸미는 꼴. "지금까지"라는 말이 목록이 더 늘어날 수 있다는 뜻까지 전한다.
- 예문: Gotchas seen so far: `wait --text` times out at 25 s with no partial output, so wait on a string the mock is guaranteed to emit, not on one branch of it.
- 유사어: Known pitfalls: (격식), Caveats: (중립), Things that have bitten us: (구어)

## "is guaranteed to emit"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 어떤 출력이 반드시 나온다는 보장을 근거로 삼을 때(테스트 작성 지침).
- 한국어: 반드시 내보내게 돼 있는
- 설명: `be guaranteed to + 동사` 는 "~하게 보장돼 있다". 원문은 `a string (that) the mock is guaranteed to emit` 으로 관계절 안에 넣고, `not on one branch of it` 으로 분기 한쪽에서만 나오는 문자열을 기다리지 말라고 대비했다.
- 예문: The handler is guaranteed to emit a `done` event, so the test waits on that. (작성)
- 유사어: always emits (평이), is certain to produce (격식), will emit no matter what (구어)
- 반의어: may or may not emit

## "compare structure, not colour"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 환경마다 달라지는 겉모습 말고 구조를 비교하라고 지시할 때(검증 지침).
- 한국어: 색 말고 구조를 비교해라
- 설명: 명령문에 `A, not B` 를 넣고 `unless` 로 예외를 달았다. 예외까지 한 문장에 넣어야 규칙이 과하게 적용되지 않는다. `colour` 는 영국식 철자.
- 예문: A fresh profile has no persisted chart theme, so ECharts may render with a different theme than your own browser shows — compare structure, not colour, unless the theme is what you are checking.
- 유사어: check the layout rather than the palette (풀어 쓴 말), ignore cosmetic differences (부정으로), focus on shape over styling (대비)

## "is a fine answer"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 최선은 아니어도 그렇게 대처하면 된다고 허용할 때(작업 지침, 구어).
- 한국어: 그렇게 해도 괜찮다
- 설명: `fine` 은 "훌륭한"이 아니라 "그 정도면 된다"다. 주어는 동명사 `switching to Playwright`. 대시 뒤 `just say which one is being used` 가 허용에 붙는 조건이다.
- 예문: If the extension reports "Browser extension is not connected", switching to Playwright is a fine answer — just say which one is being used.
- 유사어: is perfectly acceptable (격식), is a reasonable fallback (대안임을 밝힘), works too (구어)
- 반의어: is a last resort (최후 수단일 뿐)

## "rather than assuming"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 짐작하지 말고 실제 출력을 확인하라고 할 때(작업 지침).
- 한국어: 짐작하지 말고
- 설명: `rather than + -ing` 로 하지 말아야 할 쪽을 뒤에 둔다. `assume` 을 목적어 없이 끝내 "뭘 가정하든"으로 넓혔다. 앞 절이 포트가 바뀔 수 있다는 이유를 댄다.
- 예문: Nuxt takes the next free port when 3000 is busy — read the dev-server log rather than assuming.
- 유사어: instead of guessing (구어), verify, don't assume (명령 둘로), don't take it for granted (당연시 금지)
- 반의어: take it on faith (그냥 믿다)

## "pick by situation"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt (browser-verify 스킬 문서)
- 맥락: 선택지 여럿을 두고 상황 보고 고르라고 할 때(지침, 구어).
- 한국어: 상황 보고 골라라
- 설명: `by` 는 기준을 나타낸다(`sort by date` 와 같은 쓰임). 관사 없이 `by situation` 이라고 쓰면 표 제목처럼 간결해진다. 원문은 바로 아래에 상황별 표를 붙였다.
- 예문: The other two remain available — pick by situation.
- 유사어: choose case by case (건별로), use whichever fits (구어), depending on the context (격식)
- 반의어: always use the default

## "a reference to consult, not a session to run"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (tdd 스킬 문서)
- 맥락: 문서나 도구의 쓰임새를 "찾아보는 것이지 돌리는 것이 아니다"로 규정할 때(문서, 격식).
- 한국어: 찾아보는 참고서이지 실행하는 세션이 아니다
- 설명: 명사 뒤에 to부정사를 붙여 "~할 것"으로 꾸미는 꼴을 두 번 겹쳤다(`a reference to consult`, `a session to run`). `consult` 는 사전이나 지도를 찾아본다는 동사. 쓰임새를 오해할 여지를 `A, not B` 로 막았다.
- 예문: It is the shared source of the module, interface, depth, seam, adapter, leverage and locality terms, and it is a reference to consult, not a session to run.
- 유사어: a glossary, not a procedure (명사 대비), for lookup only (짧게), something to look things up in (구어)
- 반의어: a step-by-step procedure (따라 하는 절차)
