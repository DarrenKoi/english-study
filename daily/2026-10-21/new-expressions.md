# 2026-10-21 — 새 표현

오늘 배치는 문서 1건과 대화 6건이다. 문서(스큐노노 연말 성과 보고)는 전부 한국어라 표현 원료가 되지 못했고, 대신 `reading.md` 의 모범 단락으로 영어판 요약을 지어 두었다. 영어 표현은 대부분 AFM 사용 현황(`/afm/<tool>/usage`) 작업을 세 라운드에 걸쳐 보고한 어시스턴트 답변에서 왔다. 이 보고들은 "확인한 것 / 확인 안 한 것 / 판단을 맡길 것"을 칸칸이 나눠 말하는 글이라 작업 보고를 영어로 쓸 때 문형째 빌려 쓰기 좋다. `falls back to`, `for good`, `a one-line change`, `silently dropped`, `as intended`, `untouched`, `neither … nor` 는 이미 노트에 있어 건너뛰었다.

## "Things you may want to rule on"
- 레지스터: professional
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 보고 끝에서 상대가 결정해 줘야 할 항목을 따로 묶을 때(작업 보고·문어/구어 모두)
- 한국어: 판단해 주셨으면 하는 것들
- 설명: `rule on X` 는 원래 판사가 "X 에 판결을 내리다"라는 뜻이다. 업무에서는 "이건 내가 정할 일이 아니라 당신이 정할 일"이라는 권한 경계를 공손하게 긋는다. `may want to` 가 강요를 빼 준다.
- 예문: Things you may want to rule on: the default date range and whether hidden recipes should stay hidden after a reload.
- 유사어: open questions for you (중립적, 가장 흔함), decisions I need from you (더 직접적), up to you (구어, 한 항목에 붙일 때)
- 반의어: already settled (이미 정해진 것)

## "I followed the code."
- 레지스터: technical, professional
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 문서 지시끼리 충돌할 때 실제 코드를 기준으로 삼았다고 밝힐 때(리뷰·보고)
- 한국어: 코드를 따랐습니다.
- 설명: 브리프의 두 지시가 서로 어긋나자 "문서 말고 지금 돌아가는 코드가 기준"이라고 한 문장으로 선택 근거를 밝힌다. 짧아서 더 단호하게 들린다. 앞 문장에 충돌 내용을 먼저 적고 이 문장으로 닫는 배치가 핵심이다.
- 예문: The spec and the existing charts disagreed on where the selection lives, so I followed the code.
- 유사어: I went with what the code does (구어), I treated the code as the source of truth (격식, 원칙 강조), I matched the existing behaviour (기존 동작 유지 강조)
- 반의어: I followed the spec (문서를 따름)

## "it comes back if you widen the window again"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 사라졌던 상태가 조건이 돌아오면 되살아나는 동작을 설명할 때(UI 동작 보고)
- 한국어: 기간을 다시 넓히면 되돌아온다
- 설명: 앞 절 `it falls back to … when it leaves the window` 와 짝을 이룬다. 선택한 날이 사라지는 게 아니라 숨었다가 돌아온다는 걸 `come back` 한 동사로 보여 준다. `widen the window` 는 조회 기간을 늘린다는 뜻이다.
- 예문: The filter disappears when you switch tools, but it comes back if you return to the first one.
- 유사어: it's restored when … (격식, 수동), it reappears once … (중립), it sticks around (구어, 유지된다는 쪽)
- 반의어: it's cleared for good (영구 삭제)

## "picked up by the bundle scan, so no substitute was needed"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 도구가 자동으로 감지해 주니 대체 작업이 필요 없었다고 밝힐 때(빌드·설정 보고)
- 한국어: 번들 스캔이 잡아내서 대체품이 필요 없었다
- 설명: `be picked up by X` 는 "X 가 알아서 감지·포함하다"는 기술 영어의 단골 동사구다. 뒤의 `so no substitute was needed` 는 걱정하던 대안 작업을 안 해도 됐다는 결론을 수동태로 담담하게 적는다.
- 예문: The new route is picked up by the file-based router, so no manual registration was needed.
- 유사어: detected by (중립), included automatically by (풀어 쓴 표현), caught by (오류·변경을 잡아낼 때)
- 반의어: missed by (놓치다)

## "I checked this by reading the config, not by building the offline bundle."
- 레지스터: professional, technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 무엇을 확인했는지와 함께 *어떻게* 확인했는지(그리고 어떤 방법은 안 썼는지)를 밝힐 때(검증 보고)
- 한국어: 설정을 읽어서 확인했지, 오프라인 번들을 직접 빌드해 본 건 아닙니다.
- 설명: `by A, not by B` 구조가 검증의 강도를 정직하게 알린다. 듣는 쪽은 "확인됨"이 어느 수준인지 알고, 더 강한 검증이 필요하면 B 를 요청할 수 있다.
- 예문: I confirmed the fix by reading the logs, not by reproducing the crash.
- 유사어: I only checked X, not Y (구어, 범위 축소를 더 드러냄), verified on paper rather than in practice (격식, 비유), based on X alone (짧은 단서)
- 반의어: verified end to end (끝까지 직접 검증)

## "Not verified: real office data."
- 레지스터: professional, technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 보고서에서 검증하지 못한 범위를 머리말 하나로 분리할 때(보고서·체크리스트)
- 한국어: 검증 안 함: 실제 사무실 데이터.
- 설명: `Not verified:` 라는 콜론 머리말이 이 줄의 성격을 먼저 선언한다. 문장을 다 쓰지 않아도 "이건 남은 위험"이라는 게 분명하다. 공들인 결과 사이에 이런 줄을 꼭 끼워 두는 게 신뢰를 산다.
- 예문: Not verified: the Windows build and anything behind the company proxy.
- 유사어: Untested: (더 짧음), Out of scope this round: (의도적으로 뺀 경우), Still open: (남은 일 전체)
- 반의어: Verified: (확인됨)

## "were exercised by the node tests"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 어떤 코드 경로·입력을 테스트가 실제로 거쳐 갔다고 말할 때(테스트 보고)
- 한국어: 노드 테스트가 그 경로를 실제로 돌려 봤다
- 설명: `exercise` 는 "운동하다"가 아니라 "코드 경로를 실제로 실행해 보다"라는 테스트 용어다. `tested` 보다 "그 분기를 밟고 지나갔다"는 구체적인 느낌이 있다.
- 예문: The empty-list branch is exercised by two unit tests and one browser replay.
- 유사어: covered by (커버리지 관점, 가장 흔함), hit by (구어), run through (구어)
- 반의어: unexercised / never hit (한 번도 실행 안 됨)

## "an office-shaped response"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 실제 데이터는 아니지만 그 모양(필드·형식)을 흉내 낸 가짜 입력을 말할 때(테스트·목업)
- 한국어: 사무실 응답 모양을 한 응답
- 설명: `X-shaped` 는 "X 처럼 생긴"이라는 복합 형용사다. 내용은 가짜여도 구조는 진짜와 같다는 뜻을 하이픈 하나로 담는다. `production-shaped data`, `user-shaped input` 처럼 넓게 쓴다.
- 예문: I tested the parser against a production-shaped payload with every optional field missing.
- 유사어: realistic (덜 구체적), mirrors the real format (풀어 쓴 표현), a stand-in for (대역)
- 반의어: the real thing (진짜 데이터)

## "were not looked at"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 검토·확인하지 않은 항목을 담담하게 나열할 때(보고 끝머리)
- 한국어: 살펴보지 않았다
- 설명: 구동사 `look at` 을 수동태로 돌린 형태다. 전치사 `at` 이 문장 끝에 남는 게 영어에서는 자연스럽다. `not checked` 보다 덜 딱딱하고, "아예 열어 보지도 않았다"는 솔직함이 있다.
- 예문: Light theme and the mobile layout were not looked at this round.
- 유사어: weren't checked (중립), went unexamined (격식), I didn't get to (구어, 시간이 없었다는 뉘앙스)
- 반의어: were reviewed (검토됨)

## "only exists once the sibling branch merges"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 다른 브랜치가 머지돼야 의미가 생기는 의존 관계를 경고할 때(브랜치 작업 보고)
- 한국어: 형제 브랜치가 머지되어야 비로소 존재한다
- 설명: `only … once` 가 "그때가 되어야 비로소"를 만든다. `sibling branch` 는 같은 기준에서 갈라져 나란히 진행 중인 다른 브랜치를 가리킨다. 지금 링크가 깨져 보여도 버그가 아니라는 걸 미리 알려 준다.
- 예문: The settings link only works once the auth branch merges.
- 유사어: depends on X landing (구어, 개발자 은어), blocked until (차단 강조), won't resolve until (링크·경로에)
- 반의어: works on its own (독립적으로 동작)

## "it reads `기타` but is its own legend entry"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 겉보기에는 같지만 내부적으로는 별개인 것을 설명할 때(UI·데이터 설명)
- 한국어: `기타` 로 읽히지만 별도의 범례 항목이다
- 설명: `read X` 는 "X 라고 쓰여 보이다"라는 자동사 용법이다. `its own` 은 "독자적인, 따로인"이다. 겉(`reads`)과 속(`is`)을 동사 둘로 대비시킨 문장이다.
- 예문: The label reads "Other" but is its own category in the database.
- 유사어: looks like X but is actually Y (구어), appears as X while being distinct (격식), displays as (UI 맥락)
- 반의어: is the same entry (같은 항목)

## "differ by colour only"
- 레지스터: technical, professional
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 두 항목을 구분하는 단서가 하나뿐이라는 한계를 지적할 때(UI·접근성 검토)
- 한국어: 색으로만 다르다
- 설명: `differ by X` 는 "X 만큼/X 로 차이 나다". 끝의 `only` 가 "그것 말고는 구분할 길이 없다"는 약점을 드러낸다. 색맹 접근성 검토에서 자주 나오는 지적이다. 영국식 철자 `colour` 이다.
- 예문: If two recipes share a name, their legend entries differ by colour only.
- 유사어: are told apart only by (풀어 쓴 표현), the only cue is colour (명사 구문), are indistinguishable except for (격식)
- 반의어: are clearly distinct (확실히 구별됨)

## "That held in every screenshot, but adding X later would make it drift."
- 레지스터: technical, professional
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 지금은 가정이 맞지만 어떤 변경이 들어오면 깨질 수 있다고 경고할 때(한계 보고)
- 한국어: 모든 스크린숏에서는 그 가정이 맞았지만, 나중에 X 를 추가하면 어긋날 것이다
- 설명: `hold` 는 "(가정·규칙이) 유효하다". 과거 `held` 로 확인한 사실을, `would make it drift` 로 가정의 미래 위험을 말한다. 시제 대비가 "지금은 OK, 조건부로 위험"을 정확히 나눈다. `drift` 는 위치가 조금씩 어긋나는 걸 말한다.
- 예문: The offset held at every zoom level, but a sticky header would make it drift.
- 유사어: works for now, but … (구어), is fragile against (격식), would break if (더 직설적)
- 반의어: is robust to (~에도 끄떡없다)

## "is not part of the PNG export, since it sits above the canvas"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 구현 방식 때문에 생기는 부수 효과를 원인과 함께 밝힐 때(기술 설명)
- 한국어: 캔버스 위에 떠 있어서 PNG 내보내기에는 포함되지 않는다
- 설명: `since` 가 이유를 덧붙이되 `because` 보다 가볍다(이미 납득할 만한 이유라는 뉘앙스). `sit above` 는 레이어가 위에 "얹혀 있다"는 공간 동사다. 결과 → 원인 순서라 독자가 먼저 알아야 할 것을 앞에 둔다.
- 예문: The watermark is not part of the printout, since it lives in a separate overlay.
- 유사어: is left out of (중립), won't show up in (구어), is excluded from (격식)
- 반의어: is baked into (~에 박혀 들어가다)

## "only the legend case was reproduced"
- 레지스터: technical, professional
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 원인은 고쳤지만 직접 재현해 본 건 일부뿐이라고 정직하게 구분할 때(버그 수정 보고)
- 한국어: 직접 재현한 건 범례 케이스뿐이다
- 설명: 앞 절 `the cause is removed from both charts` 와 `but` 으로 묶여 "고친 범위"와 "확인한 범위"를 갈라 준다. 수동태라 누가 재현했는지보다 무엇이 재현됐는지에 초점이 간다.
- 예문: Both crashes share the same root cause, but only the first one was reproduced.
- 유사어: I only reproduced X (능동, 구어), X is the only case confirmed (격식), the rest is inferred (나머지는 추론)
- 반의어: all cases were reproduced (전부 재현함)

## "I pinned the grid rather than reading the chart instance"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 두 가지 해결책 중 하나를 골랐다고 첫 문장에서 밝힐 때(설계 선택 보고)
- 한국어: 차트 인스턴스를 읽는 대신 격자를 고정했다
- 설명: `pin` 은 "값·위치를 못 박아 고정하다". `rather than + -ing` 로 고르지 않은 쪽을 바로 옆에 둬서 선택의 의미가 드러난다. 뒤에 콜론으로 이유를 붙이는 게 이 문장의 리듬이다.
- 예문: I pinned the dependency version rather than chasing the latest release.
- 유사어: fixed X in place (중립), hard-coded X (부정적 뉘앙스 가능), locked X down (구어)
- 반의어: computed X dynamically (동적으로 계산)

## "so a four-digit tick fits"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 수치를 바꾼 목적을 짧게 붙일 때(UI 수정 보고)
- 한국어: 네 자리 눈금이 들어가도록
- 설명: 목적의 `so (that)` 뒤에 현재형 `fits` 를 쓴다. `so that … can fit` 보다 짧고, "이제 들어간다"는 결과처럼 읽힌다. `four-digit` 처럼 수사+명사 복합 형용사는 단수(`digit`)로 쓴다.
- 예문: I widened the column to 120px so a full date fits.
- 유사어: to make room for (풀어 쓴 표현), so there's space for (구어), to accommodate (격식)
- 반의어: gets clipped (잘린다)

## "needed nothing, as you decided"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 상대가 이미 정한 대로 손대지 않았다고 짧게 확인할 때(라운드 보고)
- 한국어: 결정하신 대로 손댈 게 없었다
- 설명: `as you decided` 가 "내 판단이 아니라 당신 결정을 따랐다"는 근거를 문장 끝에 붙인다. 리뷰 라운드마다 항목별로 처리 결과를 말할 때 빠뜨리기 쉬운 "안 한 것"도 이렇게 명시한다.
- 예문: The retry logic needed nothing, as you decided in the last review.
- 유사어: left as is, per your call (구어), unchanged, as agreed (격식), no action needed (체크리스트)
- 반의어: needed rework (다시 손봐야 했다)

## "Noticed, not changed:"
- 레지스터: professional, technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 범위 밖이라 고치지 않았지만 발견한 문제를 기록해 둘 때(보고서 머리말)
- 한국어: 발견했지만 고치지 않음:
- 설명: 과거분사 두 개를 `not` 으로 대비시킨 초압축 머리말이다. "봤다 / 안 고쳤다"를 한 번에 말해서, 범위를 지킨 것과 정보를 숨기지 않은 것을 동시에 보여 준다.
- 예문: Noticed, not changed: the export button has no loading state.
- 유사어: Out of scope, but worth noting: (풀어 쓴 표현), Side finding: (짧음), For a follow-up: (후속 작업 제안)
- 반의어: Fixed along the way: (하는 김에 고침)

## "would have its axis label clipped at the left edge"
- 레지스터: technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 극단적인 입력에서 생길 화면 결함을 미리 짚을 때(한계 보고)
- 한국어: 축 라벨이 왼쪽 끝에서 잘릴 것이다
- 설명: `have + 목적어 + 과거분사` 는 "목적어가 ~ 당하다"는 경험 구문이다. 주어(`a day`)가 피해를 입는 쪽이라 수동태보다 자연스럽다. 앞의 `would` 가 "그런 날이 온다면"이라는 가정을 깐다.
- 예문: A user with a very long name would have it truncated in the header.
- 유사어: would get cut off (구어), would overflow (레이아웃 용어), would be truncated (격식)
- 반의어: would fit (들어간다)

## "it scrolled fine"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-afm-usage [assistant]
- 맥락: 우려되는 점을 말하면서도 실제 체감은 문제없었다고 덧붙일 때(괄호 속 구어)
- 한국어: 스크롤은 잘 됐다
- 설명: `scroll` 을 자동사로, 대상(표)을 주어로 쓴다. `fine` 은 "문제없이"라는 부사적 형용사다. 가상화를 안 한 위험을 말한 뒤 이 짧은 말로 "지금 당장은 괜찮다"는 균형을 잡는다.
- 예문: The table has no virtualisation, but it scrolled fine with two thousand rows.
- 유사어: it ran smoothly (조금 격식), no lag that I could see (구어, 관찰 강조), it held up (부하에도 버텼다)
- 반의어: it stuttered / it lagged (버벅였다)

## "the scan never got past it"
- 레지스터: technical, conversational
- 출처: transcript:english-study [assistant]
- 맥락: 루프나 검색이 어떤 지점에서 멈춰 그 뒤를 처리하지 못한 원인을 설명할 때(버그 설명)
- 한국어: 스캔이 그 지점을 넘어가지 못했다
- 설명: `get past X` 는 "X 를 지나가다". `never` 로 "한 번도"를 강조해 버그의 본질(그 뒤로 아예 못 감)을 생생하게 보여 준다. 원인이 된 항목을 `it` 으로 받아 앞 문장과 이어 준다.
- 예문: The parser hit a malformed row, and the import never got past it.
- 유사어: got stuck on (구어), stopped at (중립), never made it beyond (조금 더 문어)
- 반의어: ran to the end (끝까지 돌았다)

## "sits between its correct alphabetical neighbours"
- 레지스터: technical, professional
- 출처: transcript:english-study [assistant]
- 맥락: 정렬된 목록에서 항목이 제자리에 들어갔다고 확인할 때(수정 결과 보고)
- 한국어: 알파벳 순으로 올바른 이웃 사이에 있다
- 설명: 목록을 동네처럼, 앞뒤 항목을 `neighbours` 로 표현한 비유다. `sit` 이 "자리 잡고 있다"는 정적인 상태를 말한다. "정렬이 맞다"를 항목 하나하나의 관점에서 확인하는 느낌이다.
- 예문: After the fix, each new entry sits between its correct alphabetical neighbours.
- 유사어: is in the right place (구어), slots in correctly (구어, 끼워 넣기 강조), is correctly ordered (격식)
- 반의어: is out of order (순서가 틀림)

## "write them out as full sentences"
- 레지스터: professional, conversational
- 출처: transcript:english-study [assistant]
- 맥락: 압축된 메모·지시문을 사람에게 보낼 때 풀어 쓰라고 조언할 때(글쓰기 조언)
- 한국어: 완전한 문장으로 풀어 쓰다
- 설명: `write out` 은 "생략 없이 다 써 내다"라는 구동사다. 목적어가 대명사면 `write them out` 처럼 가운데로 들어간다(`write out them` 은 틀림). 앞 문장 "프롬프트나 체크리스트에서는 압축해도 명확하다"와 대비된다.
- 예문: Bullet fragments are fine in a checklist, but in an email you should write them out as full sentences.
- 유사어: spell them out (구어, 명확히 말하다 쪽), expand them (중립), flesh them out (내용까지 보탤 때)
- 반의어: boil them down (요약해 줄이다)

## "has R&D causing the harm when it's the one being harmed"
- 레지스터: professional, conversational
- 출처: transcript:english-study [assistant]
- 맥락: 문장의 주어·목적어가 뒤바뀐 실수를 짚어 줄 때(글 첨삭)
- 한국어: 피해를 입는 쪽인 R&D 를 피해를 주는 쪽으로 쓰고 있다
- 설명: `have + 목적어 + -ing` 는 "(문장이) 목적어가 ~하게 그려 놓다". `when` 은 시간이 아니라 "실제로는 ~인데"라는 대조다. `the one being harmed` 는 현재분사 수동으로 "당하는 쪽"을 명사처럼 쓴다.
- 예문: Your draft has the customer approving the change when they're the one asking for it.
- 유사어: makes X the doer instead of the target (풀어 쓴 표현), gets the roles backwards (구어), reverses subject and object (문법 용어)
- 반의어: gets the roles right (역할을 맞게 씀)
