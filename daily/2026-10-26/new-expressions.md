# 2026-10-26 — 새 표현

## "one flip opens both the invitation and the door"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 설정 하나가 여러 곳을 함께 바꾼다는 구조를 비유로 설명할 때(기술 글·구어)
- 한국어: 스위치 한 번에 초대장과 문이 같이 열린다
- 설명: 랜딩 카드 노출을 '초대장', 라우트 차단 해제를 '문'에 빗댔다. 두 곳이 같은 상수를 읽어서 한 번 바꾸면 둘 다 열린다. flip 은 불리언 값을 뒤집는 동사로 개발자 영어에 자주 나온다.
- 예문: The landing card and the route middleware both read the same constant, so one flip opens both the invitation and the door.
- 유사어: one change covers both (평이), a single toggle controls both (기술 문서, 중립)
- 반의어: flip one without the other (하나만 바뀌어 둘이 어긋남)

## "behind a normal 200"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 겉으로는 정상 응답인데 속 데이터가 틀린 위험을 짚을 때(코드 리뷰·장애 보고)
- 한국어: 평범한 200 응답 뒤에 숨어서(정상인 척하면서)
- 설명: 200 은 HTTP 성공 코드. behind 가 '그 뒤에 가려져서'라는 그림을 줘서, 오류가 겉으로 드러나지 않는다는 경고가 된다.
- 예문: With no `office.py`, the next office build serves the mock measurements behind a normal 200.
- 유사어: under a success status (중립), while looking perfectly healthy (구어)
- 반의어: fail loudly (요란하게 실패해 바로 드러남)

## "hold (X) back"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 기능·카드 공개를 당분간 보류하자고 제안할 때(업무 대화·회의)
- 한국어: (X를) 내보내지 않고 붙잡아 두다, 보류하다
- 설명: 원문은 'or the card held back on cloud'. 'needs the adapter written' 과 나란히 놓인 'have/need + 목적어 + 과거분사' 구조라 held 가 과거분사로 쓰였다.
- 예문: It needs the adapter written (or the card held back on cloud) before this build is packed.
- 유사어: hold off on (일정을 미룸, 구어), withhold (격식, 다소 딱딱), keep (X) out of the release (구체적)
- 반의어: roll out, ship (내보내다)

## "a one-word change"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 수정 범위가 아주 작다는 걸 알릴 때(코드 리뷰·구어)
- 한국어: 단어 하나만 바꾸면 되는 수정
- 설명: one-line change 의 변형. 명사 앞에서 하이픈으로 묶인 복합 형용사라 word 에 -s 를 붙이지 않는다.
- 예문: `visibleSections` in `intro.vue` omits `'afm'`; adding it is a one-word change.
- 유사어: a one-line fix (가장 흔함), a trivial change (평가가 섞임)
- 반의어: a sweeping change (대규모 수정)

## "You didn't ask for this one; it follows from (X)."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 요청 범위 밖의 작업을 했다고 먼저 밝히며 이유를 댈 때(업무 보고)
- 한국어: 이건 요청하지 않으셨지만 (X)에서 자연히 따라 나온 일입니다
- 설명: 범위 밖 변경을 숨기지 않고 보고하는 문장. follow from 은 '~의 논리적 결과다'. 세미콜론으로 사실과 이유를 한 호흡에 잇는다.
- 예문: The `home-to-office` skill no longer skips afm. You didn't ask for this one; it follows from the reveal.
- 유사어: This goes slightly beyond what you asked, but ... (정중), I also went ahead and ... (구어)

## "Two things remain open:"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 보고 끝에 아직 해결 안 된 일을 정리할 때(업무 보고·이메일)
- 한국어: 아직 남은(미해결) 일이 두 가지 있습니다
- 설명: open 은 이슈 트래커의 open/closed 감각 그대로 '해결되지 않은'. remain 이 '아직도'라는 시간감을 준다.
- 예문: Two things remain open: the AFM office adapter and the tttm row in STATUS.md.
- 유사어: Two items are still outstanding (격식), There are two loose ends (구어)
- 반의어: be resolved / be closed

## "I can't tell (from home) whether it should read A or B"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 판단할 정보가 없어 결정을 상대에게 넘길 때(업무)
- 한국어: (집에서는) A로 적어야 할지 B로 적어야 할지 알 수 없다
- 설명: can't tell 은 '판별할 수 없다'. read 는 자동사로 '(문서에) ~라고 적혀 있다'라서 should read 는 '문구가 ~가 되어야 한다'.
- 예문: I left it because I can't tell from home whether it should read 구현완료 or office.
- 유사어: I have no way of knowing whether ... (더 단정적), I'm not in a position to judge whether ... (격식)

## "(N) lines lighter"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 리팩터링으로 코드가 줄었다고 말할 때(보고·구어)
- 한국어: N줄 가벼워진
- 설명: lighter 로 코드 양을 무게처럼 말한다. 앞에 about 을 붙여 어림수임을 밝혔다.
- 예문: The AFM pages are now aligned to `DESIGN.md` and about 825 lines lighter.
- 유사어: N lines shorter (평이), a net reduction of N lines (격식·수치 보고)

## "reconcile (the three)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 여러 리뷰·출처의 결과를 대조해 하나로 맞출 때(격식·업무)
- 한국어: (세 결과를) 대조해 하나로 정리하다
- 설명: reconcile 은 서로 다른 기록을 맞춰 보는 동사(회계의 '대사'와 같은 말). 숫자 명사 the three 가 '세 리뷰'를 대신한다.
- 예문: I read the same code in parallel and reconciled the three.
- 유사어: merge (단순히 합침), cross-check (대조에 초점), square A with B (구어·관용)

## "(a failed request) looked like "no data""
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 오류가 다른 정상 상태로 오인되던 버그를 설명할 때(버그 리포트)
- 한국어: 실패한 요청이 '데이터 없음'처럼 보였다
- 설명: look like + 명사로 '겉보기에 ~로 보였다'. 사용자 입장에서 두 상태가 구별되지 않았다는 점이 버그의 핵심.
- 예문: Loading and error states never rendered on the list, detail and comparison pages; a failed request looked like "no data".
- 유사어: was indistinguishable from (격식), passed for (문어·관용)

## "did not exercise (X) by hand"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 무엇을 직접 테스트하지 않았는지 정직하게 밝힐 때(테스트 보고)
- 한국어: (그 부분은) 손으로 직접 돌려 보지 않았다
- 설명: exercise 는 테스트 맥락에서 '코드 경로를 실제로 실행시키다'. 원문은 목적어를 문두로 뺀 도치형이라 '이것만은 안 했다'는 대비가 선다.
- 예문: Pure display changes such as tooltip escaping I did not exercise by hand.
- 유사어: test (X) manually (평이), click through (X) (UI를 직접 눌러 봄, 구어)

## "that (the cache keys) already cover"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 다른 장치가 이미 처리해서 중복 코드를 지웠다고 설명할 때(코드 리뷰)
- 한국어: (캐시 키가) 이미 처리해 주는
- 설명: cover 는 '범위 안에 넣어 처리하다'. 관계절로 지운 이유를 명사 바로 뒤에 붙였다.
- 예문: The API composable lost five request-dedupe maps that the cache keys already cover.
- 유사어: already handled by (중립), redundant with (격식)

## "only showed up in (X), not in (Y)"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 문제가 어떤 방법으로만 드러났는지 대비할 때(리뷰 회고)
- 한국어: X에서만 드러났고 Y에서는 보이지 않았다
- 설명: show up 은 '나타나다, 드러나다'. only … not … 짝으로 두 확인 방법을 맞세운다.
- 예문: The xs badge size renders below the 12px floor; this only showed up in the screenshot, not in the code read.
- 유사어: only surfaced in (조금 격식), was only visible in (평이)

## "fits naturally with (X)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 어떤 작업을 다른 작업과 묶어서 하자고 제안할 때(설계·계획)
- 한국어: X와 자연스럽게 맞물린다(같이 하기 좋다)
- 설명: 지금 하지 않는 이유와 나중에 할 시점을 한 번에 말해 준다.
- 예문: Switching to the API makes the landing page async; it fits naturally with writing the office adapter.
- 유사어: goes hand in hand with (관용), pairs well with (구어), is best bundled with (계획 문서)

## "X works; Y does not exist, because ..."
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 두 갈래 질문에 결론부터 하나씩 답할 때(질의응답)
- 한국어: X는 된다. Y는 아예 없다, 왜냐하면…
- 설명: 세미콜론으로 두 답을 나란히 놓고, Y 쪽은 does not work 가 아니라 does not exist 라고 정확히 말한다. 고장이 아니라 애초에 없는 기능이라는 구분이 중요하다.
- 예문: Lot ID search works; lot code search does not exist, because AFM rows carry no lot code field at all.
- 유사어: Yes for X, no for Y (구어)

## "only hits if it happens to be (X)"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 우연히 조건이 맞을 때만 검색에 걸린다고 설명할 때
- 한국어: 마침 X일 때만 (검색에) 걸린다
- 설명: hit 은 검색·캐시에서 '걸리다, 적중하다'. happen to 는 '우연히 ~하다'라서 의도된 동작이 아님을 드러낸다.
- 예문: Typing a lot code only hits if it happens to be a substring of the lot ID or the filename.
- 유사어: only matches by coincidence (평이)
- 반의어: match by design (의도대로 일치)

## "which will matter once (X)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 지금은 괜찮지만 나중에 문제가 될 조건을 미리 짚을 때(설계 리뷰)
- 한국어: X하게 되면 그때 문제가 될
- 설명: 앞 문장 전체를 받는 계속적 관계대명사 which. once 는 접속사로 '일단 ~하면'.
- 예문: So a lot that isn't in that returned list can't be found, which will matter once the office adapter returns a bounded window of files.
- 유사어: which becomes an issue when (중립), this will bite us once (구어)

## "If you want X, I need to know one thing:"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 다음 작업 전에 필요한 정보를 질문 하나로 좁힐 때
- 한국어: X를 원하시면 하나만 알려 주세요
- 설명: 조건절로 상대의 선택을 먼저 세우고 질문을 하나로 압축한다. 콜론 뒤에 바로 질문을 붙인다.
- 예문: If you want lot code search, I need to know one thing about the office AFM data: is the lot code a separate field, or derivable from the lot ID?
- 유사어: Before I start on X, one question: (구어), To proceed, I would need to confirm ... (격식)

## "which is why (X) didn't cover it"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 앞의 사실이 왜 문제로 이어졌는지 바로 이어 설명할 때
- 한국어: 그래서 X로는 처리되지 않았던 것
- 설명: which is why 는 앞 절 전체를 원인으로 받아 결과를 잇는 구어적 연결.
- 예문: The intro page kept its own hide separate from `AFM_ENABLED`, which is why the first flip didn't cover it.
- 유사어: That's why ... (새 문장, 구어), hence ... (격식·문어)

## "A is what forces B, not C"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 진짜 원인을 짚으면서 흔한 오해를 부정할 때(분석·설명문)
- 한국어: B를 일으키는 건 A이지 C가 아니다
- 설명: 'A is what ~' 강조 구문 뒤에 not C 를 붙여 대비한다. 같은 날 'Dropping the await is what made the loading states real.' 도 같은 틀.
- 예문: Revealing the page is what forces the status change, not any adapter progress.
- 유사어: It is A, not C, that forces B (It-cleft, 더 문어), A drives B, not C (간결)

## "that isn't mine; I left it untouched"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 남이 만든 파일·변경을 건드리지 않았다고 밝힐 때(작업 보고)
- 한국어: 제가 만든 게 아니라서 손대지 않았습니다
- 설명: 소유를 먼저 밝히고 조치를 붙인다. untouched 는 left 의 목적격 보어.
- 예문: There is an untracked `docs/afm/to-questionnaire-afm.md` in the main tree that isn't mine; I left it untouched.
- 유사어: I didn't touch it (구어), I've left it as is (중립)

## "a bounded window of (files)"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (AFM 작업 대화)
- 맥락: 전체가 아니라 범위가 잘린 일부만 돌려주는 API를 설명할 때
- 한국어: 범위가 제한된 일부 구간(의 파일)
- 설명: bounded 는 '상한이 있는', window 는 시간·개수로 잘라 낸 구간. '최근 N개' 같은 목록을 가리킨다.
- 예문: The search can't find older lots once the office adapter returns a bounded window of files.
- 유사어: a capped page of results (중립), a sliding window (시간 축으로 이동하는 구간)
- 반의어: the full history (전체 기록)
