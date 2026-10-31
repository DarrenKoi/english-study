# 2026-11-01 — 새 표현

## "a few small items that may be worth a decision"
- 레지스터: professional, conversational
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] 디자인 복사 점검 보고)
- 맥락: 점검 결과를 보고하면서 "큰 문제는 없고 정할 거리 몇 개만 남았다"고 상대에게 공을 넘길 때(업무 보고·구어/문어 겸용)
- 한국어: 정해 둘 만한 자잘한 항목 몇 개
- 설명: `be worth + 명사/동명사` 는 "~할 가치가 있다". `may` 를 붙여 "결정까지 할지는 당신 판단"이라는 여지를 남긴다. 보고 첫 줄에 두면 읽는 사람이 남은 일의 크기를 바로 가늠한다.
- 예문: The migration is done; the only gaps are a few small items that may be worth a decision.
- 유사어: a few open questions (더 중립적), a couple of loose ends (구어, '마무리 안 된 끝'), a few judgment calls (판단이 필요한 것임을 강조)
- 반의어: a blocker (진행을 막는 문제)

## "line for line"
- 레지스터: technical, professional
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "matches the 2026-10-18 copy line for line")
- 맥락: 두 문서·코드가 줄 단위로 똑같다고 말할 때(코드 리뷰·동기화 보고)
- 한국어: 한 줄 한 줄 그대로, 줄 단위로 똑같이
- 설명: `word for word`(한 단어씩), `byte-for-byte`(바이트 단위)와 같은 `X for X` 꼴. 동사 match/copy 뒤 부사구로 붙는다.
- 예문: The vendored copy matches upstream line for line, so we can drop the local patch.
- 유사어: word for word (글·인용에 더 흔함), verbatim (격식, 문어), byte-for-byte (파일 비교에서 더 엄격)

## "trimmed on purpose"
- 레지스터: technical, conversational
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "`nuxt.config.ts`: trimmed on purpose.")
- 맥락: 원본과 다른 부분이 실수가 아니라 의도적으로 줄인 것임을 짚어 둘 때(diff 설명·리뷰 답변)
- 한국어: 일부러 덜어 냈다
- 설명: 생략된 주어·be동사(`It was trimmed on purpose`)를 뺀 메모체. 차이를 먼저 해명해 두면 리뷰어가 "빠졌다"고 지적할 일이 없다.
- 예문: The config looks shorter than the original because it was trimmed on purpose.
- 유사어: deliberately pared down (격식), cut down intentionally (평이), stripped back (구어, 과감히 덜어 냄)
- 반의어: dropped by accident (실수로 빠진)

## "folded into flat files"
- 레지스터: technical
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "They're folded into flat files rather than copied as the original folders.")
- 맥락: 여러 폴더·모듈을 한 파일로 합쳐 구조를 납작하게 만들었다고 설명할 때(설계·리팩터 보고)
- 한국어: 평평한(하위 폴더 없는) 파일들로 접어 넣었다
- 설명: `fold A into B` 는 반죽에 재료를 섞어 넣듯 "A를 B 안으로 합쳐 넣다". `rather than` 으로 버린 대안(원래 폴더째 복사)을 같은 문장에서 대비시킨다.
- 예문: We folded the helper modules into a single flat file rather than keeping the original package layout.
- 유사어: merged into (가장 평이), consolidated into (격식), inlined (코드를 호출부에 직접 박을 때)
- 반의어: split out into (따로 떼어 내다)

## "more about identity than the shared design"
- 레지스터: professional, conversational
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] 파비콘 항목 설명)
- 맥락: 어떤 것이 겉보기 범주와 달리 사실은 다른 성격의 문제라고 재분류할 때(의견 제시·구어)
- 한국어: 공용 디자인이라기보다 정체성(브랜드) 문제에 가깝다
- 설명: `be more about A than B` 는 "B라기보다 A의 문제다". 결정을 어느 기준으로 내려야 하는지를 바꿔 준다.
- 예문: The favicon question is more about identity than the shared design, so it's your call.
- 유사어: less a matter of B than of A (문어·격식), it's really about A, not B (구어, 단정적)

## "Copy them when one does."
- 레지스터: conversational, technical
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "No current screen uses them. Copy them when one does.")
- 맥락: 지금 필요 없는 것을 "필요해지는 시점에" 하라고 짧게 미룰 때(YAGNI 식 권고·구어)
- 한국어: 쓰는 화면이 생기면 그때 복사하라
- 설명: `one does` 의 `one` 은 앞 문장의 screen, `does` 는 `uses them` 을 대신하는 대동사. 반복을 지우는 영어다운 생략이다.
- 예문: No test needs the fixture yet, so add it when one does.
- 유사어: Add it once something needs it (평이), Defer until there's a real need (격식), Cross that bridge when we come to it (관용, 구어)

## "the whole visual contract"
- 레지스터: technical, professional
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "the stylesheet is the whole visual contract")
- 맥락: 어떤 파일 하나가 화면 모양에 대한 약속 전체를 떠맡고 있다고 강조할 때(설계 근거 글)
- 한국어: 시각적 약속(계약)의 전부
- 설명: API 에 쓰던 `contract`(지켜야 할 인터페이스 약속)를 디자인에 빌려 쓴 비유. `whole` 이 "그 밖에는 없다"는 범위를 못 박는다.
- 예문: Because colours come from tokens only, the stylesheet is the whole visual contract.
- 유사어: the single source of truth (더 흔한 업계 표현), the entire visual spec (평이)

## "back in sync with"
- 레지스터: technical, conversational
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "`DESIGN.md` is back in sync with SKEWNONO")
- 맥락: 한동안 어긋났던 사본을 원본과 다시 맞췄다고 보고할 때(동기화 작업 완료 보고)
- 한국어: (원본과) 다시 맞춰졌다
- 설명: `in sync with` 는 "~와 일치한 상태". `back` 이 "원래 맞았다가 어긋났고, 이제 복구됐다"는 시간 흐름을 한 단어로 담는다.
- 예문: After the resync, our copy of the design doc is back in sync with the original.
- 유사어: realigned with (격식), caught up with (뒤처졌다가 따라잡음), matches again (평이)
- 반의어: out of sync with / drifted from (어긋난)

## "If you're fine publishing them, it's one small commit to add them."
- 레지스터: conversational, professional
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] 로고 이미지 제외 설명)
- 맥락: 결정권은 상대에게 두되 그 결정을 따를 때 드는 비용이 작다고 알려 줄 때(제안·구어)
- 한국어: 공개해도 괜찮다면 추가는 작은 커밋 하나면 된다
- 설명: `be fine + -ing` 는 "~해도 괜찮다". 뒤 절 `it's one small commit to …` 는 비용을 구체 단위로 말해 선택을 가볍게 만든다.
- 예문: If you're fine waiting a day, it's one small change to switch the job to nightly.
- 유사어: If you're okay with publishing them (더 구어), Should you wish to publish them (격식), Say the word and I'll add them (구어, 적극적)

## "with no backend change"
- 레지스터: technical
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] "`/favicon/*` will work with no backend change")
- 맥락: 프런트 쪽 변경만으로 끝나 서버는 손대지 않아도 된다고 알릴 때(작업 범위 설명)
- 한국어: 백엔드를 고치지 않고도
- 설명: `with no + 명사` 는 `without + 명사` 와 같은 뜻이지만 `no` 가 강세를 받아 "하나도 없이"가 더 또렷해진다.
- 예문: The new route works with no backend change because Flask already serves everything in dist/.
- 유사어: without touching the backend (구어), requiring no server-side changes (격식)

## "the next sync can be a plain diff"
- 레지스터: technical
- 출처: transcript:bulk-recipe-copy 87a47375 ([assistant] Insight 블록)
- 맥락: 지금 정리해 둔 덕에 다음 작업이 단순해진다고 효과를 설명할 때(작업 보고 말미)
- 한국어: 다음 동기화는 그냥 diff 한 번이면 된다
- 설명: `plain` 은 "꾸밈없는, 특별한 처리 없는". 두 파일이 완전히 같아졌으니 다음엔 수작업 대조 없이 기계적 비교로 충분하다는 뜻이다.
- 예문: Now that both files are identical, the next sync can be a plain diff.
- 유사어: a straight diff (구어), a mechanical comparison (격식)

## "The suite has not rotted — that is where the seconds go."
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt fdff92d0 (CLAUDE.md Commands 절)
- 맥락: 느린 테스트가 고장 난 것이 아니라 시간이 드는 곳이 정해져 있다고 오해를 미리 막을 때(개발 문서)
- 한국어: 테스트가 망가진 게 아니라 시간이 거기서 드는 것이다
- 설명: `rot` 은 원래 "썩다". 소프트웨어에선 방치돼 서서히 망가지는 것(code rot, bit rot)을 가리킨다. `where the seconds go` 는 "시간이 어디로 새는지"를 돈 쓰듯 표현했다.
- 예문: The build isn't broken; the image step is just where the minutes go.
- 유사어: it hasn't gone stale (구어), this is not a regression (격식·기술), it's slow by design (의도된 느림)

## "a mock that is tidier than the office is a mock that hides the office's bugs"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt fdff92d0 (CLAUDE.md "Office DB knowledge" 절)
- 맥락: 가짜 데이터를 실제보다 깔끔하게 만들면 안 되는 이유를 경구처럼 박아 둘 때(설계 원칙 글)
- 한국어: 실제보다 깔끔한 mock 은 실제 버그를 감추는 mock 이다
- 설명: `a X that … is a X that …` 반복 구문으로 두 성질을 등호처럼 묶는다. 비교급 `tidier than` 이 "정돈된 게 장점이 아니라 위험"이라는 역설을 만든다.
- 예문: Keep the nulls in the fixture; a fixture that is tidier than production is a fixture that hides production's bugs.
- 유사어: a sanitized mock gives false confidence (평이·격식), clean test data lies (구어, 단정)

## "legitimately exceeds the budget"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt fdff92d0 (CLAUDE.md Runtime gotchas — rate limit 예외)
- 맥락: 한도를 넘는 것이 남용이 아니라 정상 사용이라서 예외를 둔다고 정당화할 때(설계 문서)
- 한국어: 정당하게(정상 사용으로도) 예산을 넘는다
- 설명: `legitimately` 는 "합당하게, 정상적인 이유로". 예외 규칙을 둘 때 그 근거가 '봐주기'가 아님을 한 단어로 밝힌다.
- 예문: One gallery view legitimately exceeds the request budget, so its blueprint is exempt.
- 유사어: genuinely needs more than the limit (평이), has a valid reason to exceed (격식)
- 반의어: abuses the limit (한도를 악용하다)

## "a stale overlay sends a delegated reviewer at the wrong surfaces"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt fdff92d0 (CLAUDE.md Agent skills 절)
- 맥락: 문서를 최신으로 유지해야 하는 이유를 "낡으면 어떤 일이 벌어지는지"로 보여 줄 때(운영 문서)
- 한국어: 낡은 오버레이는 위임받은 리뷰어를 엉뚱한 곳으로 보낸다
- 설명: 무생물 주어(`a stale overlay`)가 사람을 움직이는 영어식 인과 구문. 한국어 "~하면 ~하게 된다"를 주어+동사 하나로 압축한다. `send A at B` 는 "A를 B 쪽으로 겨눠 보내다".
- 예문: An outdated runbook sends the on-call engineer at the wrong dashboard.
- 유사어: points the reviewer in the wrong direction (평이), misdirects the reviewer (격식, 간결)

## "later can scaffold for itself"
- 레지스터: conversational, technical
- 출처: transcript:bulk-recipe-copy 87a47375 (Ponytail 스킬 지침 Rules)
- 맥락: "나중을 위한" 뼈대 코드를 미리 만들지 말자고 재치 있게 말할 때(코드 리뷰·구어)
- 한국어: 나중 일은 나중이 알아서 뼈대를 세운다
- 설명: `later` 를 사람처럼 주어로 세운 의인화. "for later"라는 변명을 그대로 뒤집어 받아치는 말장난이다.
- 예문: Don't add a plugin system for later; later can scaffold for itself.
- 유사어: we'll build it when we need it (평이), YAGNI (개발 은어), don't build for hypotheticals (격식)

## "Never simplify away"
- 레지스터: technical, professional
- 출처: transcript:bulk-recipe-copy 87a47375 (Ponytail "When NOT to be lazy")
- 맥락: 단순화하더라도 절대 빼면 안 되는 것의 목록을 앞세울 때(가이드라인·체크리스트)
- 한국어: 단순화한답시고 없애 버리지 마라
- 설명: 동사 + `away` 는 "~해서 없애 버리다"(explain away, optimize away). `simplify away X` 는 단순화 과정에서 X가 사라지게 만든다는 뜻이다.
- 예문: Never simplify away input validation at a trust boundary.
- 유사어: don't cut (평이), never trade away (가치 있는 걸 맞바꿔 버리다), must survive any simplification (격식)

## "no re-arguing"
- 레지스터: conversational, professional
- 출처: transcript:bulk-recipe-copy 87a47375 (Ponytail "User insists on the full version → build it, no re-arguing.")
- 맥락: 상대가 이미 결정했으면 다시 따지지 말고 따르라고 할 때(협업 규칙·구어)
- 한국어: 다시 따지지 말고
- 설명: `re-` 접두사로 "한 번 한 논쟁을 또" 하는 걸 막는다. 명사구 하나로 끝나는 지침체라 규칙 목록 끝에 붙이기 좋다.
- 예문: Once the team picks an option, we go with it, no re-arguing.
- 유사어: no relitigating (격식·비즈니스 은어), don't reopen the debate (평이), the decision stands (단정)

## "Hardware is never the ideal on paper"
- 레지스터: technical, professional
- 출처: transcript:bulk-recipe-copy 87a47375 (Ponytail "When NOT to be lazy")
- 맥락: 이론값과 실물은 늘 다르니 보정 여지를 남기라고 할 때(장비·센서·계측 관련 설계)
- 한국어: 하드웨어는 결코 종이 위의 이상과 같지 않다
- 설명: `on paper` 는 "서류상·이론상". `the ideal on paper` 로 "계산상으로만 완벽한 모습"을 한 덩어리 명사로 만든다. 계측 장비를 다루는 일에 바로 쓸 만하다.
- 예문: Leave a calibration offset in the config; hardware is never the ideal on paper.
- 유사어: looks good on paper (이론상 좋아 보인다, 관용), the real world doesn't match the spec (평이)
- 반의어: works as specified (명세대로 동작한다)

## "YAGNI applies to tests too"
- 레지스터: technical, conversational
- 출처: transcript:bulk-recipe-copy 87a47375 (Ponytail "Trivial one-liners need no test, YAGNI applies to tests too.")
- 맥락: 원칙을 예외 없이 다른 영역까지 넓힐 때(리뷰 코멘트·구어)
- 한국어: YAGNI 는 테스트에도 적용된다
- 설명: `X applies to Y too` 는 원칙의 범위를 넓히는 가장 짧은 틀이다. YAGNI(You Aren't Gonna Need It)는 "필요 없을 기능은 만들지 마라"는 개발 격언.
- 예문: You don't need a fixture for a one-liner; YAGNI applies to tests too.
- 유사어: the same rule holds for tests (평이), this principle extends to tests (격식)

## "Rank by payoff; cap at the 10 best."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt a809dbc8 ([agent-prompt] 단순화 리뷰 지시)
- 맥락: 결과 목록을 받을 때 정렬 기준과 개수 상한을 한 줄로 지정할 때(업무 지시·위임)
- 한국어: 효과가 큰 순으로 정렬하고 상위 10개까지만
- 설명: `payoff` 는 "들인 노력 대비 돌아오는 이득". `cap at` 은 "~에서 상한을 두다". 명령문 두 개를 세미콜론으로 이어 지시를 압축했다.
- 예문: List the refactor candidates, rank them by payoff, and cap the list at the five best.
- 유사어: prioritize by impact (평이·업무), limit it to the top 10 (평이)

## "Only report what you verified."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt a809dbc8 ([agent-prompt])
- 맥락: 추측과 확인된 사실을 섞지 말라고 보고 기준을 못 박을 때(조사 위임·리뷰 지시)
- 한국어: 직접 확인한 것만 보고하라
- 설명: `what you verified` 는 명사절 목적어. `Only` 를 맨 앞에 둬 동사 전체를 한정한다. 짧지만 보고 품질을 크게 바꾸는 지시문이다.
- 예문: Please only report what you verified; mark anything else as a guess.
- 유사어: Stick to confirmed findings (평이), Report verified findings only (격식, 문서체)

## "Project facts so you don't raise false positives"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt a809dbc8 ([agent-prompt] "Project facts so you don't raise false positives: …")
- 맥락: 리뷰어에게 오탐을 막으려고 배경 사실을 먼저 건넬 때(리뷰 위임 프롬프트·문서)
- 한국어: 오탐을 내지 않도록 미리 알려 두는 프로젝트 사실
- 설명: `raise` 는 "(문제·이슈를) 제기하다". `false positive` 는 실제 문제가 아닌데 문제라고 잡는 것. `so (that) you don't …` 로 목적을 붙인다.
- 예문: Here are a few project conventions so you don't raise false positives about unused imports.
- 유사어: so you don't flag non-issues (구어), to avoid spurious findings (격식)
- 반의어: false negative (실제 문제를 놓침)
