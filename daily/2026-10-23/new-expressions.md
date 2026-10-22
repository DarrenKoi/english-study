# 2026-10-23 — 새 표현

## "the group's presence is the flag"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/office-migration/office-replies-recipe-formula-261022.md
- 맥락: 별도 boolean 없이 "있느냐 없느냐" 자체가 신호라고 설계를 설명할 때(기술 문서·리뷰)
- 한국어: 그 group 이 있다는 사실 자체가 표지다.
- 설명: `presence` 를 주어로, `flag` 를 보어로 놓아 "존재 = 신호"를 한 줄로 정의한다. 반대 경우는 `its absence means …` 로 받는다.
- 예문: Empty values set nothing, so the field's presence is the flag.
- 유사어: the mere presence of X signals Y (조금 더 문어), if X is there, it's a Y (회화)
- 반의어: its absence means … (부재 쪽에서 정의)

## "Zero regressions."
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/office-migration/office-replies-recipe-formula-261022.md
- 맥락: 변경 전후 테스트 결과가 같다고 보고를 닫을 때(짧은 상태 보고)
- 한국어: 회귀 없음.
- 설명: 실패 수가 0 이라는 뜻이 아니다. 원문은 "32 failed / 370 passed - identical with … reverted" 다음에 이 말을 붙였다. 원래 깨져 있던 것 외에 새로 깨진 게 없다는 뜻이다.
- 예문: The failure count is identical with and without the patch — zero regressions.
- 유사어: no new failures (더 풀어 쓴 말), nothing broke that wasn't already broken (회화)
- 반의어: this introduces a regression

## "harmless for (substitution)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/office-migration/office-replies-recipe-formula-261022.md
- 맥락: 이상해 보이는 입력이 특정 처리에는 문제가 안 된다고 범위를 그을 때
- 한국어: (치환)에는 해가 없다.
- 설명: `harmless` 뒤에 `for + 처리` 를 붙여 "다른 데서는 몰라도 이 처리에는 괜찮다"로 한정한다. 원문: "Duplicate refs are legal (max($5,$6,$6,$7)) - harmless for substitution."
- 예문: Trailing spaces in the name are harmless for lookup because we strip them first.
- 유사어: doesn't affect X (평이), is a no-op for X (기술 구어)
- 반의어: breaks X

## "do NOT assume (parens or a function context)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/office-migration/office-replies-recipe-formula-261022.md
- 맥락: 구현자가 빠지기 쉬운 가정을 미리 금지할 때(명세·인수인계 메모)
- 한국어: (괄호나 함수 안에 있다고) 가정하지 마라.
- 설명: 대문자 `NOT` 은 글에서 목소리를 높이는 장치다. 앞 문장 "must be a plain token replace anywhere in the string" 이 해야 할 일, 이 문장이 하지 말 것을 맡는다.
- 예문: The ID can appear anywhere in the line, so do not assume it follows a colon.
- 유사어: don't rely on X (평이), make no assumption about X (격식)

## "I've mapped the flow"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 8a530136
- 맥락: 조사 단계를 끝내고 구현으로 넘어간다고 알릴 때(진행 보고)
- 한국어: 흐름을 파악(정리)했다.
- 설명: `map` 은 "지도를 그리듯 단계를 하나하나 짚었다"는 뉘앙스다. 원문은 괄호 안에 `A → B → C` 로 그 지도를 바로 보여 준다.
- 예문: I've mapped the flow from login to checkout, and the token is refreshed twice.
- 유사어: I've traced the path (코드 추적 뉘앙스), I've worked out how it goes (회화)

## "wiring it into (HardwareView)"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 만든 helper 를 실제 화면·모듈에 연결하는 단계를 말할 때(개발자 구어)
- 한국어: (HardwareView 에) 연결해 넣다.
- 설명: 부품은 만들었고 이제 전선을 잇는다는 비유다. "writing the helper and wiring it into X" 처럼 만들기→연결 두 단계를 한 문장에 담는다.
- 예문: The parser works on its own; next I'm wiring it into the upload handler.
- 유사어: hook it up to (회화), integrate it into (격식)
- 반의어: unhook / decouple it from

## "The card fix holds everywhere."
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 8a530136
- 맥락: 고친 것이 다른 조건에서도 깨지지 않았다고 확인 결과를 요약할 때
- 한국어: 카드 수정이 어디서나 유지된다(다 잘 된다).
- 설명: `hold` 는 "버티다·유효하다". 테스트 범위(9개 탭 × 3개 폭)를 앞 문장에 두고 이 짧은 문장으로 결론만 낸다.
- 예문: I tried it on Safari and Firefox too, and the fix holds.
- 유사어: the fix works across the board (회화), the fix is robust to X (격식)
- 반의어: the fix breaks down at …

## "I found one problem my fix didn't cause"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 8a530136
- 맥락: 작업 중 발견한 별개 문제를 보고하면서 내 변경 탓이 아님을 먼저 밝힐 때
- 한국어: 제 수정 때문은 아닌 문제를 하나 찾았습니다.
- 설명: 관계절 `(that) my fix didn't cause` 가 책임 범위를 문장 안에서 정리한다. 뒤에 위치와 판단(left it alone), 질문(Want me to …?)이 이어진다.
- 예문: I found one problem my change didn't cause: the footer overlaps the menu on small screens.
- 유사어: unrelated to my change, I noticed … (조금 격식), separately, … (짧게)

## "Want me to fix it anyway?"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 8a530136
- 맥락: 손대지 않은 이유를 말한 뒤 그래도 할지 결정을 넘길 때(가벼운 업무 대화)
- 한국어: 그래도 고칠까요?
- 설명: `Do you want me to …` 에서 `Do you` 를 뺀 구어 축약이다. `anyway` 가 "위 이유가 있어도"를 받는다.
- 예문: It only shows up on phones, so I left it — want me to fix it anyway?
- 유사어: Should I fix it regardless? (조금 격식), Shall I go ahead and fix it? (공손)

## "leave it as it is"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 8a530136 ([user])
- 맥락: 제안받은 변경을 하지 말라고 짧게 답할 때(구어·채팅)
- 한국어: 그냥 그대로 둬.
- 설명: 첫 `it` 은 대상, 뒤 `as it is` 는 "지금 상태대로". `leave it` 만으로도 통하지만 `as it is` 가 "바꾸지 마"를 분명히 한다.
- 예문: The header looks fine on desktop, so let's leave it as it is.
- 유사어: leave it alone (회화), keep it as is (짧게), no change needed there (업무 문어)
- 반의어: go ahead and change it

## "(the cards) drop below (the description)"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 8a530136
- 맥락: 반응형 레이아웃에서 요소가 다음 줄로 내려가는 모습을 묘사할 때
- 한국어: (카드가 설명 글) 아래로 내려간다.
- 설명: 좁은 화면에서 옆에 있던 것이 밑으로 떨어지는 그림을 `drop below` 가 그대로 담는다. `wrap to the next line` 보다 구체적이다.
- 예문: On narrow screens the sidebar drops below the main content.
- 유사어: wrap onto the next line (텍스트에 자주), stack under (세로 배치 강조)
- 반의어: sit beside / sit side by side

## "One number to explain before pushing"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 결과에서 이상해 보일 수치를 먼저 해명하겠다고 예고할 때(리뷰·보고)
- 한국어: 푸시하기 전에 설명할 숫자가 하나 있습니다.
- 설명: 주어·동사 없이 `명사 + to-부정사` 로 머리말을 만든다. 상대가 "왜 4가 아니라 3이냐"고 묻기 전에 막는다.
- 예문: One thing to flag before we merge: the build time went up by about 20%.
- 유사어: One thing to flag (흔한 업무 구어), A note on the numbers (문어 헤딩)

## "Pushing and tearing down."
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 마무리 단계(푸시, 서버·환경 정리)를 진행 중이라고 짧게 알릴 때
- 한국어: 푸시하고 정리하는 중.
- 설명: `tear down` 은 테스트용으로 띄운 서버·worktree·브라우저를 걷어 내는 일이다. 주어를 생략한 진행 보고체.
- 예문: Tests are green; merging and tearing down the preview environment.
- 유사어: cleaning up (평이), shutting everything down (회화)
- 반의어: spin up / set up

## "reads off (Down order)"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 어떤 값이 어느 기준에서 읽혀 나오는지 설명할 때
- 한국어: (Down 순서)를 기준으로 읽어 낸다.
- 설명: `read off X` 는 "X 에서 값을 바로 읽어 내다". 계기판 눈금을 읽는 그림이다. 원문: "it is computed in the provider before the re-sort, so it still reads off Down order."
- 예문: The badge reads off the cached count, so it lags behind by a minute.
- 유사어: is derived from (격식), takes its value from (평이)

## "closer to the real thing rather than a regression"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 커진 수치·바뀐 동작이 퇴보가 아니라 실제 환경에 가까워진 결과라고 해석할 때
- 한국어: 회귀라기보다 실제에 더 가까워진 것이다.
- 설명: `closer to X rather than Y` 로 같은 현상에 두 해석을 놓고 하나를 고른다. 원문은 mock 응답이 70 KB→526 KB 로 커진 것을 이렇게 풀었다.
- 예문: The test data is slower to load now, but that is closer to the real thing rather than a regression.
- 유사어: more realistic, not worse (회화), a more faithful approximation (격식)
- 반의어: a step backwards

## "(such a row) may land out of place"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 정렬·배치 결과에서 일부 항목이 엉뚱한 자리에 갈 수 있다고 경고할 때
- 한국어: (그런 행은) 엉뚱한 자리에 들어갈 수 있다.
- 설명: `land` 는 "결과적으로 어딘가에 떨어지다". 정렬은 의도와 무관하게 결과가 정해지므로 `be placed` 보다 이 동사가 어울린다.
- 예문: Rows with a blank date may land out of place at the top of the list.
- 유사어: end up in the wrong spot (회화), be misordered (기술 문어)
- 반의어: land where it belongs

## "one look at a few real rows would settle it"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 미해결 질문을 간단한 확인 한 번이면 정리된다고 제안할 때
- 한국어: 실제 행 몇 개만 보면 결론이 난다.
- 설명: 주어 자리에 `one look` 을 놓아 "확인 비용이 작다"를 강조한다. `settle` 은 논쟁·의문을 끝내다.
- 예문: We keep guessing about the timezone; one look at the raw log would settle it.
- 유사어: a quick check would answer that (평이), that can be resolved by inspecting … (격식)

## "one is a judgement call for you"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 사실로 정할 수 없고 상대가 판단해야 하는 항목을 구분해 넘길 때
- 한국어: 하나는 당신이 판단할 문제다.
- 설명: `judgement call` 은 정답이 데이터로 안 나오는 판단. 원문은 "Two things are worth knowing, and one is a judgement call for you." 로 정보와 결정을 나눠 예고한다. 영국식 `judgement`, 미국식 `judgment`.
- 예문: Both options work; which one to ship is a judgement call for you.
- 유사어: that's your call (회화), that's a decision for you (평이)

## "paints over the next item"
- 레지스터: technical
- 출처: transcript:skewnono-s3 283e893e
- 맥락: UI 요소가 넘쳐서 옆 요소를 덮어 그리는 버그를 묘사할 때
- 한국어: 다음 항목 위에 덧그려진다.
- 설명: 브라우저가 화면을 "칠한다(paint)"는 렌더링 용어를 그대로 동사로 쓴다. `overlap` 보다 "덮어서 가린다"가 분명하다.
- 예문: A long filename overflows the cell and paints over the next column.
- 유사어: overlaps (중립), bleeds into (비유적)

## "clip instead of overflow"
- 레지스터: technical
- 출처: transcript:skewnono-s3 283e893e ([user] 붙여 넣은 지시)
- 맥락: 넘치는 내용을 잘라서 처리하라고 방식을 정할 때(UI 지시·리뷰)
- 한국어: 넘치게 두지 말고 잘라라.
- 설명: `X instead of Y` 로 두 처리 방식 중 하나를 고른다. 뒤 보고문은 "clipped with an ellipsis instead of painting over the next item" 으로 같은 틀을 받았다.
- 예문: Long titles should clip instead of overflow, with the full text in a tooltip.
- 유사어: truncate rather than spill over (조금 문어), cut it off with an ellipsis (회화)
- 반의어: let it overflow / let it wrap

## "One change beyond the manager's decision."
- 레지스터: professional
- 출처: transcript:skewnono-s3 283e893e
- 맥락: 지시받은 것 외에 내가 추가로 바꾼 것을 따로 밝히는 보고 머리말
- 한국어: 매니저 결정 외에 바꾼 것 하나.
- 설명: `beyond` 는 "범위를 넘어선". 지시 밖 변경을 숨기지 않고 헤딩처럼 앞세운 뒤 이유를 댄다.
- 예문: One change beyond the spec: I also renamed the column so the export matches.
- 유사어: One deviation from the plan (격식), I also changed … (평이)

## "if it turns out to be common"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-s3 283e893e
- 맥락: 지금은 드문 경우라 두되 자주 생기면 대응하겠다고 조건을 걸 때
- 한국어: 그게 흔한 걸로 드러나면.
- 설명: `turn out to be` 는 "나중에 알고 보니 ~이다". 아직 모른다는 전제가 들어 있다. 원문: "widening min-w-36 is the fix if it turns out to be common."
- 예문: We can add a cache later if slow lookups turn out to be common.
- 유사어: if it proves (to be) common (격식), if it keeps happening (회화)

## "verified by reading only"
- 레지스터: professional, technical
- 출처: transcript:skewnono-s3 283e893e
- 맥락: 실행해 보지 않고 코드만 읽어 확인했다고 검증 수준을 밝힐 때
- 한국어: 코드를 읽어서만 확인했다.
- 설명: 수동태 + `by -ing only` 로 확인 방법과 한계를 한 번에 적는다. 실행 확인과 읽기 확인을 섞어 보고하지 않는 습관이 담겼다.
- 예문: The retry path was verified by reading only; I couldn't trigger a timeout locally.
- 유사어: checked by inspection (격식), I only eyeballed the code (회화)
- 반의어: verified end to end / exercised in the browser

## "nothing was merged or pushed"
- 레지스터: professional
- 출처: transcript:skewnono-s3 283e893e
- 맥락: 작업 결과를 보고하며 공유 브랜치에는 영향이 없다고 못 박을 때
- 한국어: merge 나 push 는 하지 않았다.
- 설명: 부정 주어 `nothing` + 수동태로 행위자보다 "상태"를 강조한다. 병렬 작업 보고 끝에 자주 붙는다.
- 예문: The branch is ready for review; nothing was merged or pushed.
- 유사어: it's all local (회화), no changes have reached main (격식)

## "say so if you'd rather I (review that range directly)"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 008466b8
- 맥락: 내가 다른 방식을 해도 된다고 공손하게 선택지를 열어 둘 때
- 한국어: 제가 (그 범위를 직접 리뷰하길) 원하시면 말씀하세요.
- 설명: `would rather + 주어 + 과거형` 구조라서 `I reviewed` 가 문법상 맞지만, 구어에서는 원형 `I review` 도 흔하다. `say so` 는 "그렇다고 말해 달라".
- 예문: I've left the old endpoint in place — say so if you'd rather I remove it.
- 유사어: let me know if you'd prefer that I … (격식), just tell me if you want me to … (회화)
