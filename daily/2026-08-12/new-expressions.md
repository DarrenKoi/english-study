# 2026-08-12 — 새 표현

## "a band-aid"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator d5dd7c25 (Stage 2a 커서 오탐 진단)
- 맥락: 증상만 덮는 처치와 진짜 원인 수리를 갈라 말할 때(동료 사이 구어, 리뷰 코멘트에도 그대로 쓴다)
- 한국어: 미봉책, 반창고 처방
- 설명: 상처에 붙이는 밴드에서 온 비유라, "당장은 피가 멎지만 원인은 그대로"라는 판단이 단어 하나에 들어간다. 보통 `X is a band-aid` 로 단정하거나 `a band-aid over Y` 로 무엇을 덮고 있는지까지 밝힌다. 회의에서 대안을 깎아내릴 때 가장 짧게 쓰는 무기다.
- 예문: The sidecar join is the real fix — hardening the prompt is a band-aid.
- 유사어: a stopgap (중립적이고 격식 있다 — "임시로 세워 둔 것"이라 비난이 덜하다), paper over the cracks (덮어 감춘다는 부정이 더 강하다), a patch (기술 문맥에서 가벼운 임시 수정)
- 반의어: a root-cause fix (원인 자체를 없애는 수리)

## "lopsided"

- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator abd41f20 (GPU 재배치 논의)
- 맥락: 자원·부하·인원이 한쪽으로만 쏠린 현재 상태를 지적할 때(보고·설계 문서 둘 다)
- 한국어: 한쪽으로 기운, 균형이 깨진
- 설명: `lop`(잘라 내다) + `sided` 라서 한쪽 면이 잘려 나간 그림이다. 통계의 `skewed` 와 달리 분포가 아니라 **배치**를 두고 쓰며, 사람·GPU·업무량처럼 나눠 담을 수 있는 것에 붙는다. 서술 형용사로도 한정 형용사로도 쓴다.
- 예문: Here's what's actually running today and why it's now lopsided.
- 유사어: unbalanced (가장 무색투명하다), skewed (분포·통계 쪽), top-heavy (위쪽·상위 계층에만 몰렸을 때)
- 반의어: evenly split (고르게 나뉜)

## "still cramped"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator abd41f20 (GPU 1 에 모델 3개가 몰린 상태)
- 맥락: 옮기거나 줄여 봤지만 여전히 자리가 빠듯하다고 말할 때(구어, 표의 셀 안 한 마디로도 자주 쓴다)
- 한국어: 그래도 여전히 비좁은
- 설명: 사람이 좁은 방에 낀 감각을 그대로 자원에 옮겨 쓴다. `full` 이 "다 찼다"라면 `cramped` 는 "들어가긴 했는데 움직일 여유가 없다"를 담아, 지금 당장 터지지는 않지만 손대기 겁나는 상태를 그린다. `still` 을 앞에 붙이면 개선을 시도했음이 함께 읽힌다.
- 예문: Everything moved to GPU 1, still cramped.
- 유사어: tight (여유가 없다 — 일정·예산에도 두루 쓴다), squeezed (밖에서 눌려 좁아진 느낌), no headroom left (여유분이 0 이라고 수치로 말하는 쪽)
- 반의어: roomy (여유 있는)

## "the binding constraint"

- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator abd41f20 (호스트 RAM 16GB 제약)
- 맥락: 여러 제약 중 실제로 발목을 잡는 하나를 지목할 때(설계 근거·의사결정 문서에서 격식 있게)
- 한국어: 실제로 걸리는 제약, 발목을 잡는 조건
- 설명: 최적화·경제학에서 온 말이라 "여러 부등식 중 등호로 걸린 것"이라는 뜻이 그대로 살아 있다. `bottleneck` 이 흐름의 좁은 목이라면 이쪽은 **결정을 좌우하는 한 줄**이라, "GPU 는 남는데 호스트 RAM 이 문제다"처럼 엉뚱한 데를 만지지 말라는 말을 정중하게 한다.
- 예문: With 16 GB of system RAM, the binding constraint is per-process host memory, not GPU memory.
- 유사어: the limiting factor (더 일상적이고 범위가 넓다), the real bottleneck (구어 — 흐름·처리량 문맥), what actually gates this (구어체로 풀어쓴 형태)
- 반의어: slack (아직 여유가 남은 축)

## "a bug factory"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt d5b1f8a7 (인덱스 대신 접미사를 기억하기로 한 결정)
- 맥락: 어떤 설계가 지금 한 번이 아니라 두고두고 버그를 낳을 구조라고 반대할 때(동료 사이 구어)
- 한국어: 버그 공장, 두고두고 사고 날 설계
- 설명: `would be a bug factory` 처럼 가정법과 붙어 "그렇게 갔으면 어떻게 됐을지"를 말하는 자리에 잘 온다. 한 건의 결함이 아니라 **결함이 계속 생산되는 구조**를 겨눈다는 점에서 `a bug` 와 무게가 다르다.
- 예문: Remembering the index instead of the label would have been a bug factory.
- 유사어: an accident waiting to happen (사고가 예정돼 있다는 쪽), a footgun (쓰는 사람이 제 발을 쏘게 만드는 API)
- 반의어: safe by construction (구조 자체가 그 실수를 못 하게 막는)

## "have it backwards"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator abd41f20 (`--swap-space` 버전 오판 정정)
- 맥락: 앞서 한 말의 방향이 반대였다고 스스로 정정할 때(구어지만 보고에도 그대로 쓸 만큼 담백하다)
- 한국어: 거꾸로 알고 있었다
- 설명: `I had X backwards` 로 목적어를 끼워 넣으면 "무엇을" 거꾸로 알았는지까지 한 문장에 담긴다. 사과 없이 사실만 뒤집는 어투라, 길게 변명하지 않고 정정하기 좋다. 상대에게 쓸 때는 `I think you have it backwards` 처럼 완충어를 앞에 붙인다.
- 예문: I had the version risk backwards — the flag that broke was the old one, not the new one.
- 유사어: get it the wrong way round (영국식 구어), the direction is inverted (기계적·격식)
- 반의어: read it right (제대로 짚었다)

## "the tempting fix"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (`pack.py` 의 `Path.cwd()` 계약)
- 맥락: 누구나 먼저 떠올릴 해법을 굳이 언급한 뒤 왜 안 골랐는지 밝힐 때(설계 근거·PR 설명)
- 한국어: 솔깃한 해법, 손이 먼저 가는 수정
- 설명: 보통 `The tempting fix here was X — but that would have been wrong` 꼴로 쓴다. 기각한 대안을 먼저 세워 두면 읽는 사람이 "왜 쉬운 길을 두고?"라고 되묻지 않게 되어, 리뷰 왕복이 한 번 줄어든다. `tempting` 은 유혹의 주체를 상황에 두므로 누구를 탓하는 말이 아니다.
- 예문: The tempting fix here was to derive the repo root from `__file__` like the other scripts do — but that would have been wrong.
- 유사어: the obvious-looking fix (겉보기에 명백한 쪽), the intuitive move (직관이 가리키는 수), what you'd reach for first (구어로 풀어쓴 형태)
- 반의어: the fix that actually holds (실제로 버티는 수정)

## "X is the contract, not an oversight"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (`Path.cwd()` 를 그대로 둔 이유)
- 맥락: 어설퍼 보이는 코드가 사실은 지켜야 할 약속임을 밝힐 때(코드 리뷰·설계 문서)
- 한국어: 그건 빠뜨린 게 아니라 지켜야 할 계약이다
- 설명: `not an oversight` 가 "실수로 남겨진 것"이라는 기본 해석을 미리 차단한다. 뒤에 근거(테스트가 그 동작에 기대고 있다, 문서가 그렇게 약속한다)를 붙여야 성립하며, 근거 없이 쓰면 그냥 우기는 말이 된다. 정리하는 사람이 무심코 지우는 사고를 막는 데 특히 쓸모 있다.
- 예문: The script reads the working tree on purpose — `Path.cwd()` is the contract, not an oversight.
- 유사어: by design, not by accident (가장 흔한 대구 형태), load-bearing (그 코드가 하중을 받고 있다는 비유)
- 반의어: an accident of implementation (구현 과정에서 우연히 그렇게 된 것)

## "silently degrade into a guess"

- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 2f1bb741 (fab 태그를 잃은 경로)
- 맥락: 값이 빠졌을 때 에러 대신 기본값으로 넘어가는 경로의 위험을 지적할 때(설계 리뷰·버그 보고)
- 한국어: 아무 소리 없이 추측으로 주저앉다
- 설명: `degrade into` 는 등급이 한 단 내려앉는 그림이고, 앞의 `silently` 가 "그 사실을 아무도 모른다"를 맡는다. 실패가 눈에 보이면 고칠 수 있지만 추측은 그럴듯한 답을 내놓아 더 오래 살아남는다는 판단까지 한 구에 담긴다.
- 예문: Every path that loses the tag silently degrades into a guess.
- 유사어: quietly fall back to a default (같은 구조를 평이하게 쓴 형태), fail open (막지 않고 통과시키는 실패 — 보안 문맥)
- 반의어: fail loudly (막고 소리 내어 실패하다)

## "actively point at the wrong file"

- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (EPIPE 빌드 실패)
- 맥락: 에러 메시지가 도움이 안 되는 정도가 아니라 사람을 엉뚱한 데로 끌고 갔다고 말할 때(사후 정리·구어)
- 한국어: (에러가) 엉뚱한 파일을 대놓고 가리킨다
- 설명: `actively` 하나가 "정보가 없었다"와 "틀린 정보를 줬다"를 가른다. 시간을 잡아먹은 원인이 무지가 아니라 오도였음을 짚는 자리에 쓰고, 그래서 기록해 둘 값어치가 있다는 말과 잘 붙는다.
- 예문: This one is worth remembering — it cost real time, and the error message actively points at the wrong file.
- 유사어: send you down the wrong path (사람 쪽으로 시선을 옮긴 표현), misattribute the failure (원인 귀속이 틀렸다는 기술적 서술)
- 반의어: name the real culprit (진짜 원인을 지목하다)

## "deserve real suspicion"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 68159d16 (R3 는 되고 M fab 은 안 되는 원인 후보)
- 맥락: 여러 가설 중 하나에 무게를 실으면서도 단정은 피할 때(진단 보고·설계 검토)
- 한국어: 진짜로 의심해 볼 만하다
- 설명: `deserve` 를 쓰면 의심의 근거가 사람의 직감이 아니라 **대상이 갖춘 조건**에서 나온 것이 된다. `real` 은 "형식적으로 목록에 올린 후보 말고"를 뜻해, 후보들을 나란히 나열한 뒤 하나를 앞으로 끌어낼 때 유용하다.
- 예문: Cause B deserves real suspicion, because the two join claims are not equally solid.
- 유사어: warrant a closer look (더 부드럽고 중립적), be the prime suspect (수사 비유가 강해 구어에 가깝다)
- 반의어: can be safely ruled out (안심하고 배제해도 되는)

## "the vintage of X"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt 9d946c68 (오래된 `office.py` 복사본)
- 맥락: 복사본·배포본이 언제 적 판인지 따질 때(디버깅 대화, 문서에도 무리 없다)
- 한국어: (그 물건이) 몇 년도 판인지, 언제 적 것인지
- 설명: 포도주의 생산 연도에서 온 말이라 "품질"이 아니라 **시점**을 묻는다. 버전 번호가 없는 파일에 특히 편해서, `it tells you the vintage of what you last copied` 처럼 간접 증거로 시점을 추정하는 문장에 잘 어울린다.
- 예문: This copy can't even import, but it tells you the vintage of what you last cp'd.
- 유사어: which build it is (버전이 붙어 있을 때), how old the copy is (가장 평이한 직설)

## "dead leftover"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 9d946c68 (import 조차 안 되는 옛 어댑터)
- 맥락: 지금은 아무도 안 쓰지만 지워지지 않고 남은 파일을 가리킬 때(코드 정리·리뷰)
- 한국어: 죽은 잔재
- 설명: `leftover` 는 먹다 남은 음식에서 온 명사라 "남은 것"에 이미 약간의 홀대가 섞여 있고, `dead` 가 "실행 경로에 없다"를 못 박는다. 아직 살아 있는 코드에 붙이면 사실이 틀리므로, 임포트조차 안 되는 상태처럼 근거를 함께 대는 편이 안전하다.
- 예문: `back_dev_home/ebeam/hitachi/` no longer exists, so this copy is dead leftover here.
- 유사어: cruft (오래 쌓인 잡동사니 전반), a stale artifact (격식 있고 중립적), dead code (실행되지 않는 코드라는 정확한 기술 용어)
- 반의어: live code (실제로 실행되는 코드)

## "theirs to commit"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator abd41f20 (병렬 세션이 남긴 변경분)
- 맥락: 내가 손대지 않고 남겨 둔 남의 작업물을 짚을 때(협업 보고, 커밋 범위 설명)
- 한국어: 그건 그쪽이 커밋할 몫이다
- 설명: `X is yours to decide` 계열의 소유격 + to부정사 구문이다. "권한이 저쪽에 있다"와 "그래서 나는 안 건드렸다"를 한 번에 말해서, 경계를 지켰다는 사실을 자랑하지 않고 알린다. `mine to fix`, `hers to approve` 처럼 자유롭게 바꿔 쓴다.
- 예문: The parallel session's edits are still uncommitted in your tree — untouched, and theirs to commit.
- 유사어: their call (결정권이 저쪽이라는 쪽에 무게), not mine to touch (내 권한 밖임을 강조)
- 반의어: mine to land (내가 머지까지 책임질 몫)

## "it cost real time"

- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (EPIPE 사건을 기록해 두자는 말)
- 맥락: 이 일을 기록해 둘 값어치가 있다고 설득할 때(회고·메모, 구어)
- 한국어: 시간을 적잖이 잡아먹었다
- 설명: `real` 이 "말로만 번거로운 게 아니라 진짜로"를 맡아, 숫자 없이도 비용을 실감 나게 만든다. 다음에 같은 함정을 다시 밟지 않게 하려는 제안과 붙어 다닌다.
- 예문: This one is worth remembering; it cost real time.
- 유사어: it burned an afternoon (반나절을 태웠다 — 더 구체적이고 구어적), it wasn't cheap (비용 은유를 그대로 밀고 간 형태)
- 반의어: it was a quick one (금방 끝난 건)

## "keyed on X"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 2f1bb741 (Redis 와 meas_hist 가 둘 다 fab 을 키로 쓴다)
- 맥락: 조회·캐시·인덱스가 무엇을 키로 삼는지 밝힐 때(설계 문서·디버깅 설명)
- 한국어: X 를 키로 삼는
- 설명: `keyed on` 과 `keyed by` 둘 다 쓰이며, 앞의 것이 조회 조건 쪽에 조금 더 기운다. 이 표현이 힘을 얻는 자리는 "두 소스가 같은 키를 쓴다"를 밝히는 순간이다 — 그 키가 틀리면 폴백이 폴백 구실을 못 한다는 결론이 바로 따라 나온다.
- 예문: Both sources are keyed on `fab_name`, so a wrong fab kills them at once.
- 유사어: indexed by (저장 구조 쪽), looked up by (조회 동작 쪽)
- 반의어: fab-agnostic (그 축과 무관한)

## "a granularity mismatch"

- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 2f1bb741 (`m16` 대 `M16B`)
- 맥락: 양쪽이 같은 것을 가리키는데 잘게 쪼갠 정도가 달라 조인이 깨질 때(스키마 논의·장애 분석)
- 한국어: 세분화 단위가 어긋난 것
- 설명: 대소문자나 오타와 달리 **양쪽 다 자기 기준으로는 맞는데** 안 맞는 종류의 불일치라, 눈으로 훑어서는 안 잡힌다. `a case mismatch`(대소문자) 와 나란히 놓고 "이건 그쪽이 아니라 이쪽"이라고 구분해 말하면 진단이 빨라진다.
- 예문: If Redis catalogs by `m16` but meas_hist stores `M16B`, every recipe of that fab fails identically — that's a granularity mismatch, not a typo.
- 유사어: a level-of-detail mismatch (풀어쓴 형태), coarse vs fine keys (두 축을 대비시켜 부르는 방식)
- 반의어: same grain on both sides (양쪽 단위가 일치하는)

## "hold in context at once"

- 레지스터: professional, technical
- 출처: transcript:[user] auto-recipe-creator d5dd7c25 (brainstorming 스킬 문서)
- 맥락: 파일·모듈을 작게 유지해야 하는 이유를 댈 때(설계 지침·리뷰 근거)
- 한국어: 한 번에 머릿속에 담아 두다
- 설명: `hold` 가 "손에 쥐고 있다"에서 "인지적으로 붙들고 있다"로 넘어간 용법이고, `at once` 가 "쪼개지 않고 통째로"를 맡는다. 사람에게도 LLM 에게도 같은 논리로 쓰여, 요즘 설계 문서에서 파일 크기를 논할 때 표준 어구가 됐다.
- 예문: You reason better about code you can hold in context at once, and your edits are more reliable when files are focused.
- 유사어: keep in your head (더 구어적), take in at a single sitting (한 번 앉아서 다 읽는다는 쪽)
- 반의어: too big to hold at once (한 번에 안 잡히는 크기)

## "YAGNI ruthlessly"

- 레지스터: technical, conversational
- 출처: transcript:[user] auto-recipe-creator d5dd7c25 (brainstorming 스킬 문서)
- 맥락: 설계 단계에서 "지금 필요 없는 건 다 빼라"고 지시할 때(팀 규약·스킬 문서)
- 한국어: 필요 없는 건 가차 없이 쳐낼 것
- 설명: You Aren't Gonna Need It 의 약자를 **동사로** 굴린 개발자 은어다. 원래 원칙 이름이라 명사·형용사로 쓰는 게 보통인데, 동사로 세우고 `ruthlessly` 를 붙이면 "원칙에 동의한다"가 아니라 "지금 이 문서에서 실행하라"가 된다. 사내 문서에서는 통하지만 사외 문서에서는 풀어쓰는 편이 안전하다.
- 예문: YAGNI ruthlessly — remove unnecessary features from every approach and design.
- 유사어: cut it to the bone (뼈만 남기고 깎다), strip it back to what's needed today (오늘 필요한 것까지 되돌린다는 평이한 형태)
- 반의어: build for the future (올지 안 올지 모를 요구를 미리 짓는)

## "a latent trap, not a current break"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (Nuxt 컴포넌트 이름 충돌)
- 맥락: 지금 고칠 필요는 없지만 알고는 있어야 할 위험을 보고할 때(리뷰 말미·인수인계)
- 한국어: 지금 깨진 건 아니고, 나중에 걸릴 함정
- 설명: 두 명사구를 `not` 으로 맞세워 긴급도와 중요도를 한 줄에 분리한다. 이 대구가 없으면 읽는 사람이 "그래서 지금 장애냐"를 되묻게 되고, 반대로 위험을 아예 안 적으면 다음 사람이 그대로 밟는다.
- 예문: Worth consolidating the three `Fdc*.vue` files at some point, but it's a latent trap, not a current break.
- 유사어: a hazard waiting for the right conditions (조건이 맞을 때 터진다는 그림), non-blocking but worth recording (진행은 막지 않는다는 쪽)
- 반의어: a live failure (지금 터져 있는 장애)
