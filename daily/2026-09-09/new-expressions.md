# 2026-09-09 — 새 표현

오늘 재료는 트랜스크립트 10개. repo 문서도 spool 노트도 없다. 영어는 두 갈래에서 나왔다.
하나는 `llm-serving` 의 긴 GPU 디버깅 세션이고, 다른 하나는 `skewnono` FTP 감사 보고문이다.
둘 다 "무엇이 원인이 아닌지"를 지워 나가는 글이라, 소거·판정 어휘가 유난히 많다.

## "so the diagnosis held"
- 레지스터: technical, professional
- 출처: transcript:llm-serving 842f4019 (tool call parser 교체)
- 맥락: 고친 뒤 결과가 예측대로 나왔다고 확인 도장을 찍을 때(디버깅 보고·구어에 가까운 격식)
- 한국어: 그래서 진단이 맞았다 / 진단이 버텼다
- 설명: `hold` 를 자동사로 써서 "가설이 반증되지 않고 살아남았다"는 뜻을 만든다. `was correct`
  가 결과만 말한다면 `held` 는 *검증을 통과했다*는 과정을 함께 담아, 앞에 놓인 RED→GREEN
  기록과 한 덩어리로 읽힌다. 과거형인 게 중요하다 — 이 사건 하나에 대한 판정이지 영구 선언이 아니다.
- 예문: RED on hermes, GREEN on `qwen3_xml`, so the diagnosis held.
- 유사어: the theory checked out (더 구어), that confirms the root cause (더 단정적), the hypothesis survived (실험 문맥·격식)
- 반의어: the diagnosis fell apart

## "So this is not a stale note."
- 레지스터: professional, technical
- 출처: transcript:llm-serving 5565b9d0 (MTP 활성화 검토)
- 맥락: 오래된 경고를 인용한 뒤 "지금도 유효하다"고 못 박을 때(조사 보고·격식)
- 한국어: 그러니 이건 철 지난 메모가 아니다
- 설명: 상대가 속으로 할 반론("옛날 이슈 아냐?")을 먼저 꺼내 닫는 선제 방어 문장이다.
  `stale` 은 원래 빵이 굳었다는 뜻인데 정보에 붙으면 "사실이었지만 지금은 아닌"이 된다.
  바로 앞에 이슈의 최종 활동 날짜와 댓글 수를 놓았기 때문에 이 한 줄이 근거를 갖는다.
- 예문: The issue is still open, last activity 2026-08-31, so this is not a stale note.
- 유사어: this is still live (짧고 구어), the warning still applies (건조·중립), that has not been fixed since (사실만)
- 반의어: this has since been resolved

## "Accepted guesses are free tokens."
- 레지스터: technical
- 출처: transcript:llm-serving 5565b9d0 (MTP 설명)
- 맥락: 최적화 기법의 이득을 한 줄로 압축해 보여줄 때(설명·강의체)
- 한국어: 채택된 추측은 공짜 토큰이다
- 설명: 주어·보어 모두 두 단어인 최소 문장이라, 앞의 긴 설명 뒤에 놓이면 요약 망치처럼 떨어진다.
  `free` 가 "무료"와 "추가 비용 없이 얻는"을 겹쳐 담는 게 핵심이고, 기술 글에서 `free` 는
  대체로 후자다(`you get it for free`).
- 예문: The draft head guesses ahead and the big model verifies in one pass, so accepted guesses are free tokens.
- 유사어: you get those tokens for free, the win is pure upside (더 구어·과장), those come at no extra cost (격식·건조)
- 반의어: every token costs a full forward pass

## "The only thing you buy is speed."
- 레지스터: technical, conversational
- 출처: transcript:llm-serving 5565b9d0
- 맥락: 어떤 기법이 주는 이득의 범위를 좁혀 못 박을 때(설명·상담)
- 한국어: 이걸로 사는 건 속도 하나뿐이다
- 설명: `buy` 를 "돈을 내고 산다"가 아니라 "무언가를 내주고 얻는다"로 쓴다. 비용을 이미
  말한 뒤에 놓아야 대구가 성립한다. `The only thing` 이 앞에 서면서 뒤에 오는 명사 하나를
  제외한 전부를 배제해, "품질은 안 달라진다"는 직전 문장을 되받는다.
- 예문: Output is mathematically identical, so the only thing you buy is speed.
- 유사어: all you get out of it is speed (더 구어·약간 시큰둥), the sole benefit is latency (격식·문어)
- 반의어: it buys you nothing you don't already have

## "a blunt heuristic"
- 레지스터: technical
- 출처: transcript:llm-serving 5565b9d0 (FLA 커널 경고 해석)
- 맥락: 경고나 검사가 거칠어서 오탐이 난다고 설명할 때(디버깅·중립)
- 한국어: 무딘 어림짐작 / 거친 판정 규칙
- 설명: `blunt` 는 칼이 무디다는 뜻에서 와서 "정밀하지 못하다"로 확장된다. 검사 로직을
  깎아내리되 *틀렸다*고는 하지 않는 지점이 좋다 — 규칙 자체는 합리적인데 해상도가 낮을 뿐이라는
  뉘앙스라, 경고를 무시해도 되는 이유로 그대로 쓸 수 있다.
- 예문: That warning is a blunt heuristic in the kernel wrapper, not a real format problem.
- 유사어: a crude check (더 부정적), an approximation (중립·격식), a rule of thumb (사람이 쓰는 경험칙 쪽)
- 반의어: a precise check

## "your inputs trip it for a benign reason"
- 레지스터: technical
- 출처: transcript:llm-serving 5565b9d0
- 맥락: 경보가 울렸지만 실제 문제는 없다고 정리할 때(진단 결론·중립)
- 한국어: 네 입력이 해가 없는 이유로 그걸 건드린 것뿐이다
- 설명: `trip` 은 발이 걸려 넘어지다에서 와 "센서·차단기를 작동시키다"가 된다. 주어가 사람이
  아니라 입력값이라, 누구의 실수도 아니라는 함의가 자연히 붙는다. `benign` 은 의학의 양성종양에서
  온 말로, 기술 글에서 "존재하지만 해롭지 않은"에 정확히 들어맞는다.
- 예문: No issue — the check is a blunt heuristic and your inputs trip it for a benign reason.
- 유사어: it's a false positive (더 짧고 흔함), that fires harmlessly here (구어), it's tripped by design in this shape (더 길고 조심스러움)
- 반의어: that warning is pointing at a real bug

## "Permission problems look different."
- 레지스터: technical
- 출처: transcript:llm-serving b0fb3a9d (모델 경로 진단)
- 맥락: 남이 의심하는 원인을 증상 모양만으로 배제할 때(진단·구어에 가까운 격식)
- 한국어: 권한 문제라면 증상이 이렇게 안 생긴다
- 설명: `look different` 세 단어로 가설 하나를 통째로 버리는 문장이다. 뒤에 콜론을 찍고
  "그랬다면 무엇이 보였을 것인가"를 가정법 과거완료(`would have thrown`)로 붙여 근거를
  세운다. 이 순서 — 판정 먼저, 반사실 근거 나중 — 가 진단 보고문의 기본 리듬이다.
- 예문: Permission problems look different: `Path.is_dir()` would have thrown a traceback, not this clean message.
- 유사어: that's not the signature of a permission error (더 격식·전문), if it were permissions you'd see something else (구어·풀어씀)
- 반의어: that's exactly what a permission error looks like

## "Only the downloader class discriminates."
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt 6702b593 (FTP transport 감사)
- 맥락: 여러 후보 중 실제로 판별력이 있는 하나만 남기라고 지시할 때(감사 보고·격식)
- 한국어: 갈라 보여 주는 건 다운로더 클래스뿐이다
- 설명: `discriminate` 를 목적어 없이 자동사로 쓰면 "차별하다"가 아니라 **"둘을 구분해 낸다"**가
  된다. 통계·측정 문맥의 용법이고, `Only` 를 문두에 놓아 나머지 지표는 전부 무용하다는 앞 문단의
  결론을 한 문장으로 봉인한다.
- 예문: `HostSpec` is the same object under both transports, so only the downloader class discriminates.
- 유사어: only X tells the two apart (구어·쉬움), only X is diagnostic (더 짧고 임상적)
- 반의어: that probe reports the same thing either way

## "That kills a whole class of misconfiguration."
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt 6702b593
- 맥락: 설계 선택 하나가 버그 유형 전체를 없앴다고 평가할 때(설계 리뷰·격식)
- 한국어: 그 선택이 오설정이라는 부류 자체를 통째로 없앤다
- 설명: `a whole class of X` 는 개별 버그가 아니라 **범주**를 셌다는 신호다. 이 표현을 쓰면
  "이 버그를 고쳤다"가 "이 버그가 생길 자리를 없앴다"로 격상된다. `kill` 은 세지만 설계 평가에서는
  흔하고 감정적으로 읽히지 않는다.
- 예문: The swap is an import at the call site rather than a runtime lookup, which kills a whole class of misconfiguration.
- 유사어: rules out an entire failure mode (더 건조), makes that mistake unwriteable (더 강함·조어에 가까움)
- 반의어: that leaves the failure mode wide open

## "the bug is hard to write"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt 6702b593
- 맥락: 코드 구조 덕에 실수하기 어렵다고 칭찬할 때(감사·설계 리뷰)
- 한국어: 그 버그는 쓰기가 어렵게 되어 있다
- 설명: 관점을 뒤집은 게 재미있는 지점이다. 보통은 "이 코드는 안전하다"라고 쓰는데, 여기서는
  버그를 주어 삼아 *작성 난이도*를 말한다. `hard to write` 라는 평범한 구가 안전성 평가로
  승격되는 순간이고, 사람의 부주의를 탓하지 않고 구조만 칭찬하게 된다.
- 예문: The vendored package is structured so the wrong-transport bug is hard to write.
- 유사어: you'd have to go out of your way to break it (구어·과장), the mistake is not reachable from here (더 정밀)
- 반의어: the bug writes itself

## "The residual risk is exactly one shape."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt 6702b593 (감사 결론)
- 맥락: 조사를 마치고 남은 위험을 하나로 좁혀 넘길 때(감사 보고 결론·격식)
- 한국어: 남은 위험은 정확히 한 가지 모양이다
- 설명: `residual` 은 조치를 다 하고도 남는 잔여분을 가리키는 리스크 관리 용어다. 여기에
  `exactly one shape` 를 붙여 "여러 개가 아니라 딱 하나이며, 그 하나의 생김새를 내가 말할 수
  있다"는 두 가지를 동시에 주장한다. 뒤에 이탤릭으로 그 모양을 한 문장으로 그려 주면 완성된다.
- 예문: The residual risk is exactly one shape: a hand-edited file on the office PC, shipped intact.
- 유사어: only one scenario survives the audit (더 절차적), what's left is a single case (평이)
- 반의어: the remaining risk is diffuse

## "That settles the design."
- 레지스터: professional, conversational
- 출처: transcript:llm-serving b0fb3a9d (배포 방식 확정)
- 맥락: 새 사실 하나가 나와 미결이던 설계 논쟁이 끝났을 때(회의·구어에 가까운 실무)
- 한국어: 그걸로 설계가 정해졌다
- 설명: `settle` 은 흔들리던 것이 가라앉는다는 그림이라, 결정을 *내렸다*기보다 **저절로 정해졌다**는
  쪽에 선다. 사실이 결론을 강제했다는 뉘앙스라 상대의 정보 제공을 공로로 돌리는 효과가 있다.
  콜론을 붙여 곧바로 정해진 내용을 이어 쓰는 게 정석이다.
- 예문: That settles the design: only those two folders travel, so the site values have to live inside one of them.
- 유사어: that decides it (짧고 구어), that answers the open question (더 중립), that's dispositive (법률투·매우 격식)
- 반의어: that reopens the question

## "give this module a voice"
- 레지스터: professional, casual
- 출처: transcript:skewnono-v3-nuxt 6702b593 (로깅 추가)
- 맥락: 로그가 아예 없던 코드에 처음으로 로깅을 넣는 작업을 부를 때(설계 노트·비유적)
- 한국어: 이 모듈에 말할 입을 만들어 준다
- 설명: 의인화로 작업 범위를 다시 정의하는 문장이다. "로그 한 줄 추가"가 아니라 "지금까지
  침묵하던 모듈이 처음 말하게 만드는 일"이라고 규정하면, 왜 이게 한 줄짜리가 아닌지가 저절로 설명된다.
  `at all` 을 뒤에 붙이면 "그런 게 하나도 없었다"는 강조가 더해진다.
- 예문: This isn't "add a log line" — it's giving this module a voice at all.
- 유사어: make it observable (관측가능성 용어·격식), wire up logging (평이·기술적), stop it from failing silently (효과 쪽에서 서술)
- 반의어: leave it silent

## "It is long on purpose."
- 레지스터: conversational, professional
- 출처: transcript:llm-serving b0fb3a9d (진단 스크립트 안내)
- 맥락: 출력이 길다고 상대가 놀라기 전에 의도임을 밝힐 때(안내·구어)
- 한국어: 일부러 길게 만든 거다
- 설명: 짧은 문장 하나로 상대의 판단을 미리 교정한다. `on purpose` 는 `deliberately` 보다
  훨씬 구어적이고, 변명이 아니라 설계 의도로 들린다. 지시문 뒤 별도 문장으로 떼어 놓아야
  효과가 산다 — 앞 문장에 쉼표로 붙이면 묻힌다.
- 예문: Paste the whole output. It is long on purpose.
- 유사어: that's deliberate (더 격식·건조), by design (가장 짧고 기술적), I know it's verbose, and that's the point (풀어쓴 구어)
- 반의어: that's just noise you can ignore

## "Rather than another guessing round"
- 레지스터: professional
- 출처: transcript:llm-serving b0fb3a9d (진단 방식 전환)
- 맥락: 추측을 반복하다 멈추고 측정으로 방법을 바꿀 때(디버깅 보고·격식)
- 한국어: 또 한 번 넘겨짚는 대신
- 설명: `round` 가 권투·협상의 라운드에서 와 "같은 일의 n번째 반복"을 센다. `another` 와
  붙으면 앞선 시도들이 이미 실패했다는 사실을 말하지 않고도 전달한다. 자기 방법을 비판하는
  문장이라 상대를 탓하지 않고 방향을 트는 데 쓰기 좋다.
- 예문: Rather than another guessing round, I'm making the diagnostic run the launcher itself.
- 유사어: instead of guessing again (평이·구어), to stop trading hypotheses (더 문어적)
- 반의어: one more hypothesis and we'll have it

## "per your standing rule"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt 6702b593 (작업 범위 보고)
- 맥락: 예전에 받은 지시를 이번에도 지켰다고 밝힐 때(보고·격식)
- 한국어: 전부터 세워 두신 원칙대로
- 설명: `standing` 은 "계속 서 있는", 즉 한 번 정해진 뒤 매번 재확인하지 않아도 유효한 것을
  가리킨다(`a standing order`, `a standing invitation`). 지시를 다시 묻지 않은 이유까지
  이 한 단어가 설명해 준다. `per` 는 짧고 사무적이라 보고문에 잘 맞는다.
- 예문: I only edited the templates, per your standing rule.
- 유사어: as you've asked before (구어·풀어씀), in line with the convention we set (더 길고 부드러움), as previously agreed (계약투)
- 반의어: this one time I made an exception

## "Two things go missing when a repo is copied by hand."
- 레지스터: technical, professional
- 출처: transcript:llm-serving b0fb3a9d (git 없는 서버 진단)
- 맥락: 어떤 조건이 성립하면 늘 같은 것들이 빠진다고 일반화할 때(진단 도입·설명)
- 한국어: 저장소를 손으로 복사하면 두 가지가 사라진다
- 설명: `go missing` 은 "없어지다"인데 *누가 없앴는지를 말하지 않는* 자동사구다. 수동태
  `are lost` 보다 가볍고, 사람을 탓하지 않으면서 결과만 짚는다. 숫자를 먼저 던지고(`Two things`)
  뒤에 목록을 다는 구조는 상대가 몇 개를 기다리면 되는지 알려 줘서 긴 진단문의 길잡이가 된다.
- 예문: Two things go missing when a repo is copied by hand: the gitignored `.env`, and any file changed after the copy.
- 유사어: two things don't survive the copy (더 구체적), you silently lose two things (독자를 주어로)
- 반의어: everything travels intact
