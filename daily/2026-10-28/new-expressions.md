# 2026-10-28 — 새 표현

## "a retried run is harmless"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 작업을 다시 돌려도 부작용이 없다고 보증할 때(설계 문서·격식)
- 한국어: 다시 돌린 실행은 해가 없다
- 설명: 멱등성을 '재실행해도 안전하다'는 결과로 풀어 쓴 문장이다. retried 는 과거분사 형용사로 run 을 꾸민다. harmless 가 '무해하다'를 한 단어로 닫아서 idempotent 라는 용어를 모르는 독자도 바로 이해한다.
- 예문: A path already gone is a success, so a retried run is harmless.
- 유사어: safe to re-run (구어·가장 흔함), has no side effects on retry (기술적·정확)
- 반의어: a retry can do damage (재시도가 피해를 낼 수 있음)

## "proves nothing about (the path)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 어떤 신호가 판단 근거가 못 된다고 선을 그을 때(리뷰·설계 근거, 격식~중립)
- 한국어: (그 경로가 있는지 없는지) 아무것도 증명하지 못한다
- 설명: '550 이 아닌 다른 거절 코드'는 경로가 있다는 뜻도 없다는 뜻도 아니라는 말이다. 증거로서의 자격을 통째로 부정하는 표현이라 '애매하다'보다 단호하다. 뒤에 so it keeps the failure too 처럼 '그래서 보수적으로 처리한다'가 자연스럽게 이어진다.
- 예문: A probe refused with anything but 550 proves nothing about the path, so it keeps the failure too.
- 유사어: is not evidence of (중립·짧음), tells us nothing about (구어), is inconclusive (격식, 한 단어)
- 반의어: confirms (확증한다)

## "(a host) given up on at (host_timeout)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 중간에 포기한 대상을 짧게 가리킬 때(기술 글, 문법 포인트)
- 한국어: (host_timeout 시점에) 포기된 호스트
- 설명: give up on (~을 포기하다)은 전치사까지 한 덩어리인 구동사라서, 수동이 되어도 on 이 끝에 남는다. a host (that is) given up on 처럼 관계대명사와 be 동사를 줄인 후치 수식이다. on 을 빼면 문법이 깨진다.
- 예문: A host given up on at `host_timeout` keeps its thread, and `delete` sets that host's stop flag.
- 유사어: an abandoned host (원문 제목에 쓴 형용사형, 더 짧음), a host we have written off (구어, 손절 느낌)

## "The command already in flight cannot be recalled."
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 이미 출발한 요청은 되돌릴 수 없다고 한계를 밝힐 때(장애 설명·격식)
- 한국어: 이미 나간 명령은 회수할 수 없다
- 설명: recall 은 '불러들이다, 회수하다'. 리콜(제품 회수)과 같은 말이다. 원문은 뒤에 세미콜론으로 its outcome is unknown 을 붙여 '회수 불가 → 결과 모름'을 한 호흡에 적었다. 할 수 있는 일과 없는 일을 정직하게 나누는 문장이다.
- 예문: The command already in flight cannot be recalled; its outcome is unknown.
- 유사어: can't be taken back (구어), cannot be undone (결과 되돌리기 쪽에 초점), is past the point of no return (비유적)
- 반의어: can still be cancelled (아직 취소 가능)

## "That needs (the 550) settled again."
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 앞에서 한 판정 절차를 다른 경우에도 다시 해야 한다고 이어 말할 때(기술 글·구어)
- 한국어: 그러려면 (550 을) 다시 판가름해야 한다
- 설명: need + 목적어 + 과거분사 구조로 '~이 처리된 상태가 필요하다'는 뜻이다. needs to be settled 보다 짧고 말맛이 있다. settled 는 앞 절(mkdir)에서 쓴 'is settled by CWD'를 받아 again 으로 연결한다.
- 예문: That needs the 550 settled again: after a refused DELE the path counts as gone only if `SIZE` answers 550.
- 유사어: That calls for the same check again (중립), We have to resolve the 550 again (능동, 직설)

## "match it method by method"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 두 구현이 인터페이스를 하나하나 빠짐없이 따르는지 말할 때(테스트·설계 글)
- 한국어: 메서드 하나하나까지 일치하다
- 설명: 명사 by 명사(step by step, line by line)는 '하나씩 차례로 빠짐없이'를 뜻한다. 대략 비슷한 게 아니라 전수 대조라는 점을 짧게 전한다.
- 예문: A conformance test asserts both adapters match `FleetTransport` method by method.
- 유사어: one-to-one (대응 관계에 초점), item by item (일반 목록), exhaustively (격식)
- 반의어: roughly match (대충 맞음)

## "(a field missing from the wire) falls back alone"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 여러 값 중 빠진 것만 따로 기본값으로 돌아간다고 설명할 때(설계 글)
- 한국어: (전송에서 빠진 필드는) 혼자서 기본값으로 넘어간다
- 설명: alone 이 핵심이다. user 가 없을 때 password 까지 같이 바꾸지 않고 빠진 그 필드만 대체한다는 뜻이다. the wire 는 '네트워크로 오가는 실제 데이터'를 가리키는 개발자 관용어다(over the wire).
- 예문: `user` and `password` resolve independently, and a field missing from the wire falls back alone.
- 유사어: defaults on its own (중립), is filled in independently (격식)
- 반의어: falls back together (함께 대체됨)

## "cross the HTTP hop"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 데이터가 중간 경유 구간을 지나간다고 특히 보안 위험을 짚을 때(기술 글)
- 한국어: HTTP 경유 구간을 건너가다
- 설명: hop 은 네트워크에서 한 번 건너뛰는 구간이다. cross 와 짝지으면 '그 구간을 실제로 지나간다'가 되어 노출 지점을 떠올리게 한다. 원문은 바로 뒤에 HTTPS 와 토큰을 요구한다.
- 예문: Bytes and credentials both cross the HTTP hop: serve it behind HTTPS and set `FTP_PROXY_TOKEN`.
- 유사어: travel over HTTP (중립), pass through the proxy (경유지에 초점)

## "marks every host in it failed"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 한 번의 실패가 묶음 전체의 상태를 바꾼다고 설명할 때(기술 글)
- 한국어: 그 안의 모든 호스트를 실패로 표시한다
- 설명: mark + 목적어 + 보어(형용사·과거분사). mark it done, mark it read 와 같은 틀이다. as 없이 바로 failed 를 붙이는 게 개발 문서에서 흔하고 간결하다.
- 예문: A whole-batch transport failure marks every host in it failed.
- 유사어: flags every host as failed (as 를 쓴 형태), fails the whole batch (구어, 더 짧음)
- 반의어: marks it succeeded/ok (성공으로 표시)

## "(PASV) is right behind NAT"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 특정 환경에서는 그 기본값이 맞는 선택이라고 말할 때(구어·기술 글)
- 한국어: (NAT 뒤에서는) 그게 맞다
- 설명: right 는 '옳다'보다 '그 상황에 맞는 선택이다'에 가깝다. 뒤에 behind NAT 같은 조건을 붙여 '언제 맞는지'를 한정한다. 바로 다음 문장에서 그 조건이 깨지는 경우(다른 서브넷)를 다룬다.
- 예문: `ftplib` defaults to PASV, which is right behind NAT.
- 유사어: is the correct choice when (격식), works well (when) (중립·구어)
- 반의어: is the wrong default for (그 환경에는 틀린 기본값)

## "if login works but every RETR hangs only from the server"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 증상을 정확히 짚어 '이럴 때 이걸 해 보라'고 안내할 때(트러블슈팅 글·구어)
- 한국어: 로그인은 되는데 서버에서만 RETR 이 전부 멈춘다면
- 설명: but 으로 '되는 것'과 '안 되는 것'을 대비시키고 only from the server 로 재현 조건을 좁힌다. 증상 기술은 이렇게 '어디까지 되고 어디서부터 안 되는지'를 함께 적어야 쓸모가 있다. 뒤에는 명령문 try ... 가 온다.
- 예문: If login works but every `RETR` hangs only from the server, try `passive=False`.
- 유사어: it connects fine but downloads stall (구어), authentication succeeds while data transfers time out (격식)

## "Disk wins only on memory pressure."
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 대안이 나은 경우를 딱 하나로 좁혀 말할 때(설계 비교·회의)
- 한국어: 디스크가 나은 건 메모리가 빠듯할 때뿐이다
- 설명: win 은 '비교에서 이기다, 더 낫다'. 설계 비교에서 자주 쓴다. only on 이 이기는 조건을 한 가지로 묶어 '그 밖에는 기본값이 낫다'를 함축한다.
- 예문: Disk wins only on memory pressure; files here are KB–few MB, so the default is in-memory.
- 유사어: is only better when (중립), only pays off under (격식, 비용 대비 효과)
- 반의어: loses everywhere else (나머지에선 진다)

## "the original "works locally, fails on the server" bug"
- 레지스터: conversational
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 환경 차이로 생기는 버그를 따옴표 한 줄로 이름 붙일 때(구어·회고 글)
- 한국어: 처음의 '로컬에선 되는데 서버에선 안 되는' 버그
- 설명: 증상 문장을 통째로 따옴표에 넣어 형용사처럼 bug 앞에 붙였다. 영어에서 흔한 즉석 복합 수식어다(a 'not my problem' attitude). original 이 '이 설계를 하게 만든 첫 사건'이라는 뜻을 준다.
- 예문: Unpinned `aioftp` installed at task runtime was the original "works locally, fails on the server" bug.
- 유사어: a works-on-my-machine bug (가장 흔한 관용어), an environment-drift bug (기술적·격식)

## "Both paths are in use."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/CONTEXT.md
- 맥락: 두 방식 모두 실제로 운영 중이라 어느 쪽도 버릴 수 없다고 밝힐 때(문서·격식)
- 한국어: 두 경로 모두 실제로 쓰이고 있다
- 설명: in use 는 '사용 중'. 짧은 단언이라 '하나는 레거시 아니냐'는 질문을 미리 막는다. 용어집 정의 끝에 붙여 두 경로를 동등하게 유지해야 하는 이유가 된다.
- 예문: The proxy does the real FTP and returns file bytes. Both paths are in use.
- 유사어: Both are live (구어, 운영 맥락), Both remain in production (격식)
- 반의어: deprecated / no longer used (더 이상 안 씀)

## "tolerates (large files) easily; (the other) is sensitive to them"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/CONTEXT.md
- 맥락: 같은 조건에 두 대상이 다르게 반응한다고 대비할 때(설계 문서)
- 한국어: (큰 파일을) 쉽게 견딘다 / (그것에) 민감하다
- 설명: tolerate(견디다)와 be sensitive to(민감하다)를 세미콜론 앞뒤에 놓아 대구를 만든다. them 이 large files 를 받아 반복을 줄인다. 위험 분석에서 '어느 쪽이 약한가'를 한 문장으로 보여 주는 틀이다.
- 예문: The direct path tolerates large files easily; the proxy path is sensitive to them.
- 유사어: handles X fine / struggles with X (구어), is robust to X / is vulnerable to X (격식)

## "asserts neither drifts"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/CONTEXT.md
- 맥락: 테스트가 두 구현이 서로 어긋나지 않게 지켜 준다고 말할 때(테스트·설계 글)
- 한국어: 어느 쪽도 어긋나지 않는지 단언한다
- 설명: drift 는 '조금씩 떠내려가다'. 두 구현이 시간이 지나며 슬그머니 달라지는 현상을 가리킨다. neither 는 단수 취급이라 drift 에 -s 가 붙는다.
- 예문: Both classes satisfy the seam structurally, and a conformance test asserts neither drifts.
- 유사어: keeps them in sync (구어), guards against divergence (격식)
- 반의어: the two drift apart (서로 멀어짐)

## "real at that scale"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 리뷰를 맡길 때 실제 규모에서 의미 있는 문제만 올리라고 범위를 정할 때(위임·격식~중립)
- 한국어: 그 규모에서 실제로 문제가 되는
- 설명: real 은 '이론상 말고 실제로 비용이 생기는'. at that scale 이 판단 기준을 '최대 20개'라는 앞의 맥락에 묶는다. 사소한 지적으로 목록을 채우는 걸 막는 위임 문장이다.
- 예문: Only report something that is real at that scale.
- 유사어: that actually matters at this size (구어), material at the expected volume (격식)
- 반의어: theoretical (이론상만의)

## "keep (large payloads) alive"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 참조가 남아 메모리가 풀리지 않는 상황을 말할 때(코드 리뷰·기술)
- 한국어: (큰 데이터를) 계속 살려 두다
- 설명: keep + 목적어 + alive 는 '살아 있는 상태로 유지하다'. GC 언어에서 참조가 남아 메모리가 해제되지 않는 상황을 생생하게 표현한다. 원문은 closures that keep large payloads alive 로 리뷰 관점 목록에 넣었다.
- 예문: Flag closures that keep large payloads alive after the page no longer needs them.
- 유사어: hold a reference to (중립·정확), retain (격식, 한 단어)
- 반의어: let it be garbage-collected (해제되게 두다)

## "Context that bounds the cost:"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 리뷰어에게 비용 판단의 상한이 되는 사실을 먼저 알려 줄 때(위임 프롬프트·격식)
- 한국어: 비용의 상한을 정하는 맥락:
- 설명: bound 는 동사로 '한계를 정하다'. 콜론 뒤에 '최대 20개' 같은 사실을 늘어놓아 리뷰어가 과장된 지적을 하지 않게 한다. 관계절 that bounds the cost 가 어떤 맥락인지를 한정한다.
- 예문: Context that bounds the cost: the group holds at most 20 measurements.
- 유사어: What limits the cost here: (구어), Scale constraints: (짧은 제목형)

## "I would not change it, but (X) would be cleaner if the file is touched again."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 지금 고칠 필요는 없지만 다음에 손댈 때 개선하라고 부드럽게 권할 때(코드 리뷰·구어)
- 한국어: 지금 바꾸진 않겠지만 그 파일을 다시 손댈 때는 X 가 더 깔끔하다
- 설명: would 두 번으로 의견임을 드러내 강요하지 않는다. if the file is touched again 은 '따로 수정 PR 을 만들 정도는 아니고 다음 기회에'라는 리뷰 관용 틀이다.
- 예문: I would not change it, but a plain `push` would be cleaner if the file is touched again.
- 유사어: Not blocking, but next time you're in there, ... (구어), Non-blocking nit: ... (짧은 리뷰 태그)
- 반의어: This must be fixed before merge. (머지 전 필수 수정)

## "That is inherent to (the highlight)."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 비용이 기능 자체에서 오는 것이라 줄일 대상이 아니라고 설명할 때(리뷰·격식)
- 한국어: 그건 (하이라이트 기능에) 본래 따르는 것이다
- 설명: inherent to 는 '~에 본래 내재된'. 피할 수 없는 비용이라 결함이 아니라는 판정이다. 리뷰에서 '이건 낭비가 아니라 기능의 대가'라고 짧게 정리한다.
- 예문: The row list re-renders on each click, but that is inherent to the highlight.
- 유사어: comes with the territory (구어 관용구), is the price of (the feature) (중립)
- 반의어: avoidable overhead (피할 수 있는 낭비)

## "not worth hoisting"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt subagent(efficiency review) — agent-prompt / [assistant]
- 맥락: 반복 계산을 밖으로 빼는 최적화가 이득이 없다고 말할 때(코드 리뷰)
- 한국어: 밖으로 빼낼 가치가 없다
- 설명: hoist 는 원래 '끌어올리다'. 코드에서는 반복되는 계산을 루프나 템플릿 밖으로 꺼내는 것을 말한다. not worth + 동명사로 '해 봐야 이득이 없다'를 짧게 전한다.
- 예문: The key compare appears three times per row, but it is a string compare and not worth hoisting.
- 유사어: not worth caching (계산 결과 저장 쪽), not worth pulling out (구어)
