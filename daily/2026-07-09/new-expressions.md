# 2026-07-09 — 새 표현

오늘 배치는 auto_recipe_creator 트랜스크립트(코드리뷰 서브에이전트·A/B 평가 감사·데몬 디버깅 세션)에서 수집했습니다.

## "fire-and-forget"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 결과를 기다리지 않고 백그라운드로 던져두는 비동기 호출을 설명할 때(기술 문서·구어 모두)
- 한국어: 쏘고 잊는 방식 — 발사 후 결과를 기다리지 않는 비동기 실행
- 설명: 미사일 용어에서 온 관용구. 스레드/메시지/요청을 "던져놓고 신경 끄는" 패턴을 한 단어처럼 압축합니다. 하이픈으로 묶어 형용사처럼 씁니다(a fire-and-forget call). 오늘 배치에는 변형 "fire early, join late"(일찍 쏘고 늦게 회수)도 등장 — 시작과 회수 시점을 분리하는 설계를 대구로 표현.
- 예문: The consensus gather is fired off as a fire-and-forget daemon thread immediately after the alarm is detected.
- 유사어: non-blocking (형식적·중립), kick off in the background (구어적 풀어쓰기), best-effort (실패해도 무방하다는 뉘앙스가 추가됨)
- 반의어: a blocking / synchronous call (완료까지 기다림)

## "nail down (the ordering)"
- 레지스터: conversational, technical
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 애매하던 사실을 확실하게 못 박아 확정할 때(구어·작업 로그)
- 한국어: (사실·순서·원인을) 확실히 못 박다, 확정하다
- 설명: nail(못질)에서 온 구동사. "대충 아는" 상태에서 "확실히 아는" 상태로 만드는 행위. 조사·디버깅 서사에서 "지금부터 이걸 확정하겠다"는 신호로 자주 씁니다.
- 예문: Let me read the main monitor loop around the gather call to nail down the ordering.
- 유사어: pin down (거의 동의어 — 이미 노트에 있음), lock down (합의·설정을 고정하는 쪽), establish (격식·문어)
- 반의어: leave (it) open / up in the air (미확정 상태로 두다)

## "the (single most likely) culprit"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 여러 용의 원인 중 "범인"을 지목할 때(디버깅 보고·구어)
- 한국어: (문제의) 주범, 범인
- 설명: 원래 "범죄자"라는 뜻이지만 기술 영어에서는 버그 원인을 의인화하는 표준 어휘입니다. "the most likely culprit", "the usual culprit(단골 범인)" 같은 콜로케이션으로 외워두면 좋습니다.
- 예문: The single most likely culprit given "harness works, loop empty" is the recipe_id format mismatch.
- 유사어: the (root) cause (중립·격식), the offender (파일·코드 줄을 지목할 때 익살스럽게), the prime suspect (아직 확정 전 단계)
- 반의어: red herring (범인처럼 보이지만 아닌 것)

## "That rules out X — and it sharpens the diagnosis"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 새 정보로 가설 하나를 소거하면서 남은 가설이 더 또렷해졌다고 말할 때(진단·분석 보고)
- 한국어: 그걸로 X는 배제되고, 진단이 더 날카로워진다
- 설명: rule out(배제)과 sharpen(날카롭게 하다)의 결합. 소거가 손실이 아니라 전진임을 강조하는 프레임 — "가능성이 줄었다"가 아니라 "초점이 좁혀졌다"로 들리게 합니다. sharpen은 diagnosis, question, hypothesis 등과 잘 붙습니다.
- 예문: Good — that rules out the path mismatch, and it actually sharpens the diagnosis.
- 유사어: narrow it down (구어), that eliminates X (중립), that leaves only Y (결과 쪽 강조)
- 반의어: that muddies the picture (상황을 더 흐리게 만든다)

## "the classic signature of X"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 증상 조합이 특정 원인의 전형적 패턴임을 지목할 때(진단 보고·격식)
- 한국어: X의 전형적인 징후(서명처럼 남는 흔적)
- 설명: signature는 "원인이 남기는 고유한 흔적"이라는 은유. "이 증상 세트를 보면 십중팔구 이 원인"이라고 경험칙을 압축해 전달합니다. classic이 "교과서적"의 뉘앙스를 더합니다.
- 예문: "Works in the test, empty in the loop" is the classic signature of cross-thread connection reuse.
- 유사어: the telltale sign of (숨길 수 없는 단서 — 약간 문학적), the hallmark of (품질보증 마크 은유·격식), textbook X (형용사적: a textbook race condition)
- 반의어: an atypical presentation (전형에서 벗어난 증상 — 의학 어투)

## "parameter creep"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (코드리뷰 서브에이전트)
- 맥락: 함수 인자가 조금씩 늘어 비대해지는 현상을 지적할 때(코드리뷰)
- 한국어: 파라미터가 슬금슬금 늘어나는 현상
- 설명: scope creep(범위 증식)의 함수 버전. creep은 "눈치채지 못하게 기어 늘어난다"는 핵심 이미지 — 한 번에 나빠지는 게 아니라 리뷰마다 하나씩 늘어서 나중에 문제가 됩니다. "slight parameter creep but reasonable"처럼 정도를 달아 균형 있게 지적하는 게 리뷰 관례.
- 예문: _finalize_match now takes four optional kwargs — slight parameter creep, but acceptable given the None defaults.
- 유사어: scope creep (일·범위가 대상 — 이미 노트에 있음), feature creep (제품 기능이 대상), bloat (이미 비대해진 결과 상태)
- 반의어: a lean interface (군더더기 없는 인터페이스)

## "no copy-paste drift"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (코드리뷰 서브에이전트)
- 맥락: 코드를 옮기면서 미세하게 달라진 부분이 없음을 보증할 때(리팩터 리뷰)
- 한국어: 복붙 과정에서 생긴 미세한 어긋남 없음
- 설명: 코드를 verbatim(글자 그대로) 이동했는지가 리팩터 검증의 핵심인데, 옮기다 살짝 바뀌는 사고를 drift(표류) 한 단어로 명명합니다. "moved verbatim with no copy-paste drift"가 한 세트.
- 예문: The multi-scale NMS body was moved verbatim to _collect_candidates with no copy-paste drift.
- 유사어: byte-identical / bit-for-bit identical (결과 동일성 — 이미 노트에 있음), a faithful move (충실한 이동), no transcription errors (필사 오류 없음)
- 반의어: silent divergence (조용히 갈라짐)

## "swamped by"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (A/B 평가 감사)
- 맥락: 작은 신호가 큰 물량에 묻혀 안 보이게 될 때(통계·평가 보고)
- 한국어: (다수·큰 값에) 잠겨 묻히다
- 설명: swamp(늪)가 동사로 쓰이면 "물에 잠기게 하다". 집계 수치의 함정을 지적할 때 강력합니다 — 평균이 좋아 보여도 소수의 심각한 악화가 다수의 미미한 개선에 "잠겨" 있을 수 있다는 경고.
- 예문: A 20% regression in five recipes could be swamped by fifty small gains elsewhere.
- 유사어: drowned out by (소리 은유 — 신호/피드백에), dwarfed by (크기 대비가 초점), masked by (가려짐 — 중립)
- 반의어: stand out (도드라지다)

## "understate / overstate (the gain)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (A/B 평가 감사)
- 맥락: 측정 설계 때문에 효과가 실제보다 작게/크게 보고될 때(평가·통계 문서, 격식)
- 한국어: (효과를) 실제보다 축소해서 / 부풀려서 말하다
- 설명: state(진술하다)에 under/over를 붙인 대칭쌍. 거짓말이 아니라 "구조적으로 눈금이 어긋난 보고"라는 뉘앙스가 핵심 — 편향 논의에 정확히 맞는 동사입니다. It is no understatement to say...(결코 과장이 아니다) 같은 파생 표현도 유용.
- 예문: Restricting the eval to easy frames will systematically understate the true gain.
- 유사어: undersell / oversell (설득·영업 뉘앙스), downplay / talk up (의도적 축소·부풀림), inflate (수치를 부풀리다 — overstate 쪽)
- 반의어: 서로가 서로의 반의어 (understate ↔ overstate)

## "headroom"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (A/B 평가 감사)
- 맥락: 아직 남아 있는 개선 여지·여유 용량을 말할 때(성능 논의·격식/기술 모두)
- 한국어: (천장까지의) 여유 공간, 개선 여지
- 설명: 원래 "머리 위 공간"(차·터널). 성능 논의에서는 "현재 수치와 이론적 상한 사이의 남은 여지"를 뜻합니다. 오늘 문맥은 특히 좋았습니다 — 쉬운 케이스만 평가하면 "앙상블이 실제로 도울 수 있는 headroom"을 놓친다는 지적.
- 예문: Scoring only the easy frames under-counts the headroom where the ensemble actually helps.
- 유사어: room for improvement (평이·중립), upside (투자 어휘 — 잠재 이득), slack (여유분 — 자원 쪽)
- 반의어: a ceiling (상한 — headroom이 0인 상태)

## "guess-and-check thrashing"
- 레지스터: conversational, technical
- 출처: transcript:auto_recipe_creator (systematic-debugging 스킬 문서)
- 맥락: 원인 분석 없이 이것저것 바꿔보며 허우적대는 디버깅을 낮잡아 부를 때(구어·설득)
- 한국어: 찍고-확인하기를 반복하며 제자리에서 허우적대기
- 설명: thrash는 "몸부림치다" — OS 용어 thrashing(페이지 교체만 반복하며 일을 못 하는 상태)과 겹쳐 들려 개발자에게 특히 와닿습니다. "Systematic debugging is FASTER than guess-and-check thrashing"처럼 대비 구도로 쓰면 설득력이 셉니다.
- 예문: Two hours of guess-and-check thrashing would have been fifteen minutes with a systematic approach.
- 유사어: flailing (허우적댐 — 더 구어적), trial and error (중립 — 부정적 뉘앙스 없음), shotgun debugging (산탄총식 — 무차별 수정)
- 반의어: a systematic / disciplined approach

## "untested fixes don't stick"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (systematic-debugging 스킬 문서)
- 맥락: 테스트 없는 수정은 결국 되돌아온다고 짧게 원칙을 박을 때(구어·리뷰 코멘트)
- 한국어: 테스트 없는 수정은 오래 못 간다(다시 떨어져 나간다)
- 설명: stick은 "붙어 있다 → 정착하다". 접착 은유로 "고쳤다는 상태가 유지되지 않는다"를 4단어로 압축합니다. make it stick(확실히 정착시키다), the lesson didn't stick(교훈이 몸에 안 배었다)처럼 확장 가능.
- 예문: Untested fixes don't stick — write the failing test first, then fix.
- 유사어: won't hold (버티지 못한다), will regress (다시 무너진다 — 기술적), come undone (풀려버린다 — 문학적)
- 반의어: a durable fix (오래가는 수정)

## "Standing by."
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (문서 개정 세션)
- 맥락: 다음 입력·완료 신호를 기다리며 대기 중임을 알릴 때(짧은 상태 보고, 무전 어투)
- 한국어: 대기 중입니다.
- 설명: 군·무전 용어에서 온 stand by(대기하다)의 진행형을 한 문장으로 끊어 쓰는 상태 보고. "아무것도 안 하는 게 아니라 준비된 채 기다린다"는 뉘앙스. 이메일/채팅 끝에 붙이면 간결하고 프로페셔널합니다.
- 예문: The two remaining agents are still running — standing by for their completion notifications.
- 유사어: on standby (형용사구), awaiting your go-ahead (격식 — 승인 대기), holding (무전 어투 — 더 짧음)
- 반의어: proceeding (진행에 들어감)

## "the disciplined move is to X"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (align-fail 디버깅 세션)
- 맥락: 유혹(찍기)을 물리치고 원칙적 선택을 선언할 때(작업 보고·격식)
- 한국어: 절제된(원칙에 맞는) 수는 X다
- 설명: 체스의 "the right move" 어법에 disciplined를 얹은 형태. "쉬운 길이 있지만 훈련된 사람은 이렇게 한다"는 자기 절제의 선언으로, 뒤에 오는 행동에 권위를 실어줍니다. 원문: "I won't guess which one — the disciplined move is to make that silent gate speak."
- 예문: I won't guess which gate fires — the disciplined move is to instrument it and let one run tell us.
- 유사어: the principled choice (원칙 강조·격식), the textbook play (교과서적 수), the prudent thing to do (신중함 강조)
- 반의어: the tempting shortcut (유혹적인 지름길)

## "audience calibration"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (문서 개정 세션)
- 맥락: 글의 수준·용어를 독자에 맞게 조정하는 작업을 명명할 때(문서 작업·격식)
- 한국어: 독자 눈높이 보정
- 설명: calibration(계측기 눈금 맞추기)을 글쓰기에 전용한 표현. "쉽게 쓰기"가 아니라 "측정기처럼 독자에 맞춰 눈금을 다시 잡는다"는 정밀한 은유라 보고서 개정 작업을 품위 있게 지칭합니다.
- 예문: The review's real theme is audience calibration — strip the package names that mean nothing to executives.
- 유사어: pitching it at the right level (구어), tailoring to the reader (중립), know your audience (관용 명령형)
- 반의어: a one-size-fits-all draft (독자 구분 없는 원고)

## "the throughline"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (문서 개정 세션)
- 맥락: 여러 지적·장면을 관통하는 하나의 주제를 짚을 때(리뷰 요약·격식)
- 한국어: 전체를 관통하는 한 줄기(일관된 주제)
- 설명: 연극·시나리오 용어(스타니슬랍스키의 through-line of action)에서 온 말. 흩어진 리뷰 코멘트들이 사실 하나의 요구라는 것을 "the review's throughline is X"로 묶으면 요약이 한 단계 고급스러워집니다.
- 예문: The review's throughline is audience calibration: every comment asks the same question — does an executive need this?
- 유사어: the common thread (실 은유·평이), the unifying theme (격식), the red thread (유럽식 표현)
- 반의어: scattered, unrelated notes (관통 주제가 없는 상태)
