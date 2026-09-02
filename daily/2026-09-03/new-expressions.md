# 2026-09-03 — 새 표현

## "not retroactive"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt df4b4762 (Chrome 확장으로 앱 검증)
- 맥락: 로그·계측 도구가 "켜기 전 일은 못 본다"는 성질을 알릴 때. 코드 리뷰·디버깅 메모에서 자주 쓴다.
- 한국어: 소급되지 않는, 켠 시점부터만 기록되는
- 설명: 켠 뒤부터만 수집한다는 뜻. Playwright 트레이스처럼 상시 기록하는 도구와 대비할 때 이 한 단어가 차이를 다 설명한다.
- 예문: Network tracking is not retroactive, so call the reader before the click you want to observe.
- 유사어: only records from the first call (직설·풀어쓰기), forward-only (더 짧고 딱딱함)
- 반의어: persistent trace, always-on capture

## "arm (the reader) first"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 관찰 도구를 미리 무장·대기시켜 놓고 그다음에 행동을 일으키겠다고 절차를 밝힐 때.
- 한국어: (계측기를) 먼저 걸어 두다
- 설명: arm 은 폭약·경보를 "격발 대기 상태로 만들다". 계측에 쓰면 "관찰을 준비시킨 뒤 트리거한다"는 순서가 한 동사에 들어간다.
- 예문: I'd arm the network reader first, then force a failing download and confirm the toast actually fires.
- 유사어: start capturing before (평이), set up the listener first (중립)
- 반의어: read the log afterwards

## "re-derived every session"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt df4b4762 (verify 스킬 설명)
- 맥락: 문서로 굳혀 두지 않으면 매번 처음부터 다시 알아내야 한다는, 문서화의 존재 이유를 대는 자리.
- 한국어: 세션마다 매번 다시 알아내야 하는
- 설명: derive 는 "추론해서 얻다". re- 가 붙어 "같은 추론을 반복한다"는 낭비를 지적한다. 문서·스킬의 정당화 문장으로 정형화돼 있다.
- 예문: It exists because "did this actually work?" is a manual procedure that would otherwise be re-derived every session.
- 유사어: rediscovered from scratch (더 구어), reinvented each time (약간 비아냥)
- 반의어: written down once

## "a memory of traps, not a wrapper"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 도구·문서의 성격을 한 줄로 규정할 때. "X 가 아니라 Y" 대비 틀이 핵심.
- 한국어: 감싸는 도구가 아니라 함정의 기록
- 설명: 각 항목이 "누가 한 번 밟은 실수"라는 뜻을 담는다. 자동화(wrapper)와 경험 축적(memory)을 가르는 표현이라 스킬·런북 설명에 잘 맞는다.
- 예문: The skill is a memory of traps, not a wrapper — each gotcha is a mistake someone made once.
- 유사어: a record of hard-won lessons (더 격식), a list of things that bit us (회화)
- 반의어: an abstraction layer

## "Rough rule:"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 정밀한 기준 대신 실용적 어림 기준을 내놓을 때. 예외를 인정하면서 판단을 넘겨주는 어감.
- 한국어: 대충의 기준은 이렇다
- 설명: rule of thumb 을 문장 첫머리에 압축해 쓴 형태. 뒤에 조건절 한 줄이 붙는 게 보통이다.
- 예문: Rough rule: if the bug could be described without mentioning pixels, events, or the URL bar, it isn't a browser job.
- 유사어: as a rule of thumb (더 격식), the quick test is (구어)
- 반의어: the precise criterion is

## "it isn't a <tool> job"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 어떤 도구를 꺼낼지 말지를 한 문장으로 자를 때. 도구 선택 가이드의 마침표.
- 한국어: 그건 그 도구가 할 일이 아니다
- 설명: 능력 부족을 말하는 게 아니라 담당이 아니라는 판정이다. 사람을 탓하지 않고 경계만 긋는 어감이라 리뷰에서 부드럽게 먹힌다.
- 예문: If a curl through the proxy answers the question, it isn't a browser job.
- 유사어: that's out of scope for X (더 격식), X is the wrong tool here (직설)
- 반의어: that's exactly what X is for

## "silently skips"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 실패가 아니라 조용한 누락이라 더 위험하다고 경고할 때.
- 한국어: 아무 말 없이 건너뛴다
- 설명: 초록불이 뜨는데 실제로는 절반만 돌았다는 상황을 가리킨다. loudly 와 짝으로 쓰면 대비가 선명해진다.
- 예문: Running `pytest tests` alone silently skips the provider-contract half, so the green is only half true.
- 유사어: quietly drops (더 구어), no-ops without warning (기술 문서)
- 반의어: fails loudly

## "a deliberate blank"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15 (mother/son 라벨)
- 맥락: 빈칸이 버그가 아니라 결정이었음을 보고서에서 밝힐 때.
- 한국어: 일부러 비워 둔 자리
- 설명: 빠뜨림(oversight)과 선택을 가르는 이름표. 뒤에 "왜 채우지 않았는지" 한 문장을 붙여야 방어가 완성된다.
- 예문: A deliberate blank for parameters whose region has no mother — labelling them son would contradict the toggle.
- 유사어: an intentional gap (중립), left empty on purpose (회화)
- 반의어: an oversight

## "that is a one-line change in X"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 상대가 다른 결정을 원할 때 되돌리는 비용이 싸다고 알려 주며 선택권을 넘길 때.
- 한국어: 그건 X 에서 한 줄만 고치면 된다
- 설명: 결정을 강요하지 않으면서 "언제든 바꿔도 된다"는 안전판을 깔아 준다. 실제로 한 줄일 때만 써야 신뢰가 남는다.
- 예문: If you would rather those read as son, that is a one-line change in `paramRole`.
- 유사어: it's a cheap reversal (더 격식), we can flip that any time (회화)
- 반의어: that would mean reworking the whole engine

## "keeping them apart"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 비슷해 보이는 두 개념을 굳이 나눠 둔 설계 의도를 설명할 때.
- 한국어: 둘을 따로 두는 것
- 설명: 합치면 편해 보이는 두 술어를 분리해 둔 이유를 밝히는 문장에서 쓴다. 뒤에 "그래서 무엇이 안 움직였는지"를 붙이면 근거가 된다.
- 예문: Keeping them apart means the toggle's numbers did not move at all with this change.
- 유사어: drawing the line between them (비유적), treating them as two concepts (평이)
- 반의어: collapsing them into one

## "one caveat to be aware of"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 작업을 끝내 보고하면서 사후에 물릴 수 있는 조건 하나를 미리 얹을 때(격식).
- 한국어: 알아 두셔야 할 단서가 하나 있습니다
- 설명: 결함 고백이 아니라 정보 제공의 틀이다. 뒤에 "동작은 그대로고 라벨만 넓어졌다"처럼 영향 범위를 함께 못박는다.
- 예문: One caveat to be aware of: a row can now read `son` while its note has no exclusion mark.
- 유사어: with one caveat (더 짧음), worth flagging (회화)
- 반의어: no strings attached

## "X is the equivalent"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 어떤 기능을 못 주는 대신 같은 목적을 이루는 다른 수단을 제시할 때.
- 한국어: X 가 그 자리를 대신한다
- 설명: 거절 뒤에 곧바로 대체안을 붙이는 구조라, 못 한다는 말이 막다른 길로 끝나지 않는다.
- 예문: CSV has no formatting, so highlighting is not possible there — Excel's autofilter on the `mother/son` column is the equivalent.
- 유사어: serves the same purpose (평이), stands in for it (회화)
- 반의어: there's no substitute for it

## "beats round-tripping each click"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 여러 호출을 한 번에 묶는 편이 왕복 대기보다 낫다고 도구 사용법을 조정할 때.
- 한국어: 클릭마다 왕복하는 것보다 낫다
- 설명: round-trip 이 동사로 쓰인 형태. 성능 얘기 같지만 실제로는 "호출을 어떻게 묶을지"라는 사용 습관 조언이다.
- 예문: With this extension, `browser_batch` beats round-tripping each click.
- 유사어: batching wins over one call at a time (평이)
- 반의어: one round trip per action

## "side-effect-runs"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt df4b4762
- 맥락: 명령이 의도한 일 대신 엉뚱한 파일까지 실행해 버리는 함정을 경고할 때.
- 한국어: 부수효과로 (엉뚱한 것까지) 실행해 버린다
- 설명: 명사 side effect 를 하이픈으로 묶어 동사로 만든 즉석 조어. 기술 메모에서 이런 조어는 자연스럽게 통한다.
- 예문: `npx playwright test` finds nothing here and side-effect-runs your `node:test` files.
- 유사어: accidentally executes (평이), picks up and runs (완곡)
- 반의어: exits cleanly with no matches

## "stands out against"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 많은 것들 사이에서 하나가 눈에 띄게 만든 UI·문서 설계 의도를 말할 때.
- 한국어: ~들 사이에서 도드라지다
- 설명: against 가 "배경 대비"를 만든다. 대비 대상을 반드시 뒤에 붙여야 뜻이 산다.
- 예문: Only `mother` carries the accent colour so it stands out against the many sons.
- 유사어: reads at a glance (기능 중심), pops (구어·가벼움)
- 반의어: blends in with the rest

## "the behaviour is unchanged, only the label is broader"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt ad54ba15
- 맥락: 겉보기 변화가 큰 커밋에서 "실제 로직은 안 건드렸다"를 못박아 리뷰 부담을 줄일 때.
- 한국어: 동작은 그대로고 이름표만 넓어졌다
- 설명: 무엇이 안 바뀌었는지를 먼저 말하는 보고 습관. 리뷰어가 어디를 볼지 바로 정할 수 있다.
- 예문: The behaviour is unchanged, only the label is broader, and the docstrings say so.
- 유사어: cosmetic on the surface, identical underneath (더 길고 구어)
- 반의어: this changes what the toggle actually excludes
