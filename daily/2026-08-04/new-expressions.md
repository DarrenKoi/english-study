# 2026-08-04 — 새 표현

## "silent-wrong instead of loud-broken"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/585e2b32
- 맥락: 실패가 "조용히 틀린 값"으로 나는지 "요란하게 터지는지"를 가를 때(설계 근거·리뷰)
- 한국어: 요란하게 깨지는 대신 조용히 틀린다
- 설명: 형용사 둘을 하이픈으로 묶어 명사처럼 쓴 조어. silent-wrong 은 오류 없이 잘못된 값을 내는 상태, loud-broken 은 즉시 눈에 띄게 터지는 상태다. 소프트웨어에서는 전자가 훨씬 위험하다는 판단이 `A instead of B` 한 구에 들어 있다.
- 예문: A pre-today office copy keeps answering with the old key, so the failure is silent-wrong instead of loud-broken.
- 유사어: fail silently (동사구·중립), a silent regression (명사형), degrade quietly (완만한 열화 쪽)
- 반의어: fail loudly (즉시 눈에 띄게 터지다)

## "a live foot-gun"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/1c134071
- 맥락: 사소한 개선처럼 보이던 것을 "지금 사고가 나는 구조"로 격상할 때(버그 보고·기술 대화)
- 한국어: 장전된 채 놓인 자해 장치
- 설명: shoot yourself in the foot(제 발등 찍다)에서 나온 개발자 은어로, 쓰는 사람이 스스로 사고를 내게 만드는 설계를 뜻한다. live 는 총알이 들어 있다는 뜻이라 "이론상 위험"이 아니라 "당장 터진다"를 얹는다. `isn't just X; it's Y` 로 등급을 올리는 문형과 짝을 이룬다.
- 예문: Two fields you'd naturally compare sit nine hours apart in one record — this isn't just readability, it's a live foot-gun.
- 유사어: an accident waiting to happen (일상 관용구), a trap waiting to be sprung (서술적), a sharp edge (더 온건)
- 반의어: safe by construction (구조상 그럴 수 없음)

## "request-order luck"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/4eb3da27
- 맥락: 동작 여부가 설계가 아니라 우연한 순서에 달려 있었다고 지적할 때(원인 서술)
- 한국어: 요청이 어느 쪽이 먼저 도착하느냐 하는 운
- 설명: `X was Y luck` 은 "X 가 Y 라는 우연에 달려 있었다"를 명사 하나로 눌러 담는 틀이다. 앞자리를 갈아 끼워 timing luck, ordering luck, cache luck 처럼 쓴다. 경쟁 상태를 비난조 없이 정확히 묘사한다.
- 예문: Whether an MSR got warmed was request-order luck, not design.
- 유사어: a race condition (엄밀·중립), it depended on which resolved first (풀어쓴 형태)
- 반의어: deterministic (매번 같은 결과)

## "didn't survive checking"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/585e2b32
- 맥락: 리뷰에서 주장 하나가 검증에 걸려 탈락했음을 알릴 때(격식)
- 한국어: 확인해 보니 살아남지 못했다
- 설명: survive 를 "검증을 통과하다"로 쓰는 용법. 죽는 주체가 사람이 아니라 주장이라 지적이 인신공격으로 들리지 않는다. 리뷰 결과를 뒤집는 문단의 첫 줄로 관례처럼 붙는다.
- 예문: One spec claim didn't survive checking: there is an app-wide error handler after all.
- 유사어: didn't hold up (더 평이), failed verification (건조·격식), turned out to be wrong (직설)
- 반의어: held up under scrutiny (따져 봐도 버텼다)

## "the error you see is the error path, not the cause"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/585e2b32
- 맥락: 사용자가 본 예외가 원인이 아니라 원인을 설명하려다 죽은 코드임을 짚을 때(진단 보고 첫 줄)
- 한국어: 지금 보이는 에러는 원인이 아니라 에러 처리 경로다
- 설명: error path 는 예외를 잡아 메시지를 만드는 쪽 코드를 가리키는 기술 용어다. 그 안에서 2차 예외가 나면 원래 원인이 통째로 가려지는데, 그 사정을 `X is A, not B` 대비 하나로 정리한다.
- 예문: `sorted(frames)` crashed while writing the message that would have explained the failure — the error you see is the error path, not the cause.
- 유사어: a secondary failure masking the first (풀어쓴 형태), the diagnostic died, not the code under test
- 반의어: the traceback points straight at the cause

## "lying about its age"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/585e2b32
- 맥락: 최신인 척하는 낡은 사본·캐시를 두고 말할 때(운영 대화, 반쯤 구어)
- 한국어: 나이를 속이고 있다 — 최신인 척하는 낡은 사본
- 설명: 무생물을 거짓말하는 주체로 세우는 의인화다. `X is lying about Y` 는 "X 가 Y 에 대해 잘못된 인상을 준다"를 짧고 세게 말한다. 파일이 자기 버전을 겉으로 드러내지 않을 때 꼭 맞는다.
- 예문: `sync_office_adapters --diff` is the only thing that tells you which copies are lying about their age.
- 유사어: silently out of date (건조·중립), stale without saying so
- 반의어: self-describing (자기 판을 스스로 밝히는)

## "an assumption with no mechanism behind it"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/910b1dcc
- 맥락: 어떤 기대가 강제 장치 없는 믿음일 뿐임을 짚을 때(설계 근거·리뷰, 격식)
- 한국어: 그것을 강제할 장치가 하나도 없는 가정
- 설명: assumption 과 mechanism 을 맞세워 "그렇게 되겠지"와 "그렇게 되도록 만들어 뒀다"를 가른다. 문제의 가정을 큰따옴표로 그대로 인용해 주어 자리에 앉히는 배치가 관례다.
- 예문: On a host where the baseline is someone else's image, "pandas will bring a good numpy" is an assumption with no mechanism behind it.
- 유사어: wishful thinking (구어·비판적), unenforced (형용사·건조), it relies on convention alone
- 반의어: enforced by the tooling (도구가 강제한다)

## "import success proves presence, never version"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/910b1dcc
- 맥락: 점검 코드가 어디까지 증명하는지 사정거리를 못 박을 때(기술 근거 서술)
- 한국어: import 가 됐다는 건 있다는 증명일 뿐, 어느 판인지는 증명하지 못한다
- 설명: `X proves A, never B` 는 증거의 한계를 잘라 말하는 틀이다. not 대신 never 를 써서 "어떤 경우에도 아니다"까지 담는다. 검사 방식을 왜 바꿨는지 한 문장으로 정당화할 때 쓴다.
- 예문: Why this rather than the numpy-specific check I added earlier: import success proves presence, never version.
- 유사어: presence is not proof of version (평이한 환언), necessary but not sufficient (더 일반적)
- 반의어: it pins the exact version

## "the corollary is counter-intuitive"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/910b1dcc
- 맥락: 앞 설명에서 따라 나오는 결론이 상식과 어긋날 때 미리 예고하며(문어·격식)
- 한국어: 여기서 따라 나오는 결론이 직관과 어긋난다
- 설명: corollary 는 수학의 "따름정리"에서 온 말이라, 새 주장이 아니라 앞 문단의 논리적 귀결임을 알린다. 상식에 반하는 조언을 낼 때 방어막 노릇을 한다. 뒤에 콜론을 찍고 결론을 굵게 붙이는 배치가 흔하다.
- 예문: The corollary is counter-intuitive for a requirements file: declare transitive dependencies whose version matters.
- 유사어: it follows, oddly, that … (문장형), the surprising consequence is …
- 반의어: as you would expect

## "sidestep"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/acabd470
- 맥락: 문제를 푸는 대신 그 상황 자체가 생기지 않게 비껴갈 때(설계 선택 설명)
- 한국어: 정면으로 풀지 않고 비껴가다
- 설명: solve 가 맞붙어 푸는 것이라면 sidestep 은 링에 아예 오르지 않는 쪽이다. 뒤에 `having to -ing` 를 붙여 "그 일을 해야 할 필요 자체를 없앤다"로 잇는 형태가 잦다. avoid 보다 능동적이고 영리하다는 결이라 설계 근거로 쓸 수 있다.
- 예문: A `data:` URI sidesteps having to get cache headers right in three different serving layers.
- 유사어: obviate the need for (격식·문어), work around (임시방편 느낌), avoid (중립)
- 반의어: tackle head-on (정면으로 붙다)

## "it's yours to delete"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/585e2b32
- 맥락: 내가 못 하는 마지막 한 단계를 상대에게 넘길 때(협업 구어, 정중하되 격식은 낮음)
- 한국어: 지우는 건 그쪽 몫입니다
- 설명: `it's yours to V` 는 그 동사를 할 권한과 책임이 상대에게 있다고 부드럽게 넘기는 틀이다. 명령형보다 압박이 덜하면서 누가 해야 하는지는 흐려지지 않는다. yours 자리를 mine/theirs 로 바꿔 주체만 갈아 끼운다.
- 예문: My `rm -rf` was blocked by the permission classifier, so it's yours to delete.
- 유사어: I'll leave that to you (더 부드러움), that one's on you (casual, 책임을 강조)
- 반의어: I've taken care of it

## "a two-minute check on your side"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/7b3f8feb
- 맥락: 상대에게 일을 넘기면서 부담이 작다는 걸 수치로 못 박을 때(업무 대화)
- 한국어: 그쪽에서 2분이면 끝나는 확인
- 설명: `a <시간> check/fix/change` 는 시간을 형용사처럼 명사 앞에 붙여 규모를 미리 밝힌다. 하이픈이 필수이고 minute 은 복수가 되지 않는다. `on your side` 가 "내 환경이 아니라 그쪽 환경에서"를 뜻해, 책임 떠넘기기가 아니라 접근 권한 문제임을 드러낸다.
- 예문: Nothing is broken at home, so pinpointing it is a two-minute check on your side.
- 유사어: a quick one on your end (구어), it's a one-line change (다른 척도로 크기 표시)
- 반의어: a day's work

## "come along (with a change)"
- 레지스터: technical, casual
- 출처: transcript:skewnono-v3-nuxt/1c134071
- 맥락: 의도한 수정에 딸려 같이 바뀐 부분을 가볍게 밝힐 때(커밋 설명·구어)
- 한국어: 손대려던 건 아닌데 같이 딸려 왔다
- 설명: 공유 헬퍼를 고치면 그 호출부가 자동으로 따라 바뀌는 상황을 한 마디로 설명한다. 변경 범위를 숨기지도, 크게 다루지도 않는 어조라 커밋 메시지에 잘 맞는다.
- 예문: `locks.py` shares the same helper, so it came along.
- 유사어: it was swept in (범위를 넓게 잡았다는 뉘앙스), it fell out of the same change (더 기술적)
- 반의어: left untouched

## "nobody was listening"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/4eb3da27
- 맥락: 정보는 이미 있었는데 받아 쓰는 쪽이 없었다고 짚을 때(원인 설명)
- 한국어: 알려 주고 있었는데 듣는 쪽이 없었다
- 설명: 이벤트·폴링 구조를 사람의 대화로 은유한다. 세미콜론 앞은 "신호는 있었다", 뒤는 "소비자가 없었다"로 대비시키는 배치가 핵심. 없던 기능을 만든 게 아니라 있던 것을 연결했다는 뜻이라 수정 규모까지 정확히 전달한다.
- 예문: The warm job already knows when the cache is ready; nobody was listening.
- 유사어: it was fire-and-forget (원인 쪽에서 본 같은 사실), the signal existed but went unread
- 반의어: wired end to end

## "a prime suspect"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt/4eb3da27
- 맥락: 아직 확인 전이지만 가장 유력한 원인을 지목할 때(디버깅 대화)
- 한국어: 가장 유력한 용의자
- 설명: 수사 은유다. culprit(범인)은 확정된 뒤에 쓰지만 suspect 는 미확정이라 성급한 단정을 피한다. prime 이 "여럿 중 첫 번째로 의심스러운"을 얹고, 뒤에 `for <증상>` 을 붙여 무엇의 용의자인지 밝힌다.
- 예문: Flask isn't listening on :5050 — that's a prime suspect for the 502.
- 유사어: the most likely culprit (확신이 한 단계 위), my money is on X (구어·베팅조)
- 반의어: ruled out (용의선상에서 제외됨)

## "the asymmetry matters"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/910b1dcc
- 맥락: 두 방향이 대칭이 아니라는 사실이 결론을 좌우할 때(기술 설명, 격식)
- 한국어: 여기서 비대칭이 중요하다
- 설명: 짧은 문장을 콜론 앞에 세워 "지금부터 할 말이 결론을 바꾼다"고 예고하는 신호 문장이다. asymmetry 는 A→B 는 되는데 B→A 는 안 되는 관계를 가리키고, 끝을 `— but not the reverse` 로 닫는 짝이 굳어져 있다.
- 예문: The asymmetry matters: numpy-1 pickles load fine under numpy 2, but not the reverse.
- 유사어: this only works in one direction (평이), it is not symmetric (건조)
- 반의어: it cuts both ways (양쪽 다 성립한다)
