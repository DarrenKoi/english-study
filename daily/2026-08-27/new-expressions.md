# 2026-08-27 — 새 표현

## "the two places that must agree"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 같은 값을 두 파일(백엔드·프런트 상수 등)에 나눠 두었고 그 둘이 어긋나면 안 된다고 변경 보고에서 말할 때(격식)
- 한국어: 서로 값이 맞아야 하는 두 자리
- 설명: "중복"을 결함이 아니라 관리 대상으로 부르는 표현이다. `must agree` 는 사람의 합의가 아니라 값의 일치를 뜻하며, 관계절로 붙여 "고칠 곳은 여기 둘뿐"을 함께 전한다. 변경 요약 첫 줄에 두면 뒤의 "나머지는 여기서 읽어 온다"가 자연스럽게 이어진다.
- 예문: The default is set in the two places that must agree, and everything else reads from those.
- 유사어: kept in sync (동작 서술, 더 평이), a twin constant (한쪽에서 다른 쪽을 부를 때)
- 반의어: a single source of truth

## "recorded as your decision"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 설계 문서에 어떤 값을 정한 근거를 적을 때, 그것이 구현자의 판단이 아니라 요청자의 결정임을 날짜와 함께 남긴다고 보고할 때(격식·문어)
- 한국어: 당신의 결정으로 기록해 두었다
- 설명: 나중에 "왜 2주냐"가 나왔을 때 답이 문서에 있게 하는 관행. `recorded as` 뒤에 결정의 주체를 명시해 책임 소재를 분명히 하고, 괄호 속 날짜가 provenance 를 완성한다. 비난이 아니라 기록의 언어라 어조가 중립적이다.
- 예문: The rationale was rewritten for the 2-week default (recorded as your decision, 2026-08-26).
- 유사어: per your call (구어, 짧음), attributed to (출처를 밝히는 문어체)
- 반의어: an implementer's assumption

## "(main) moved under this change"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 작업하는 동안 다른 세션의 커밋으로 base 브랜치가 앞서 나가 rebase 가 필요했다고 알릴 때(개발 보고)
- 한국어: 이 변경을 만드는 동안 main 이 (밑에서) 움직였다
- 설명: `under` 가 "발밑에서"의 그림을 준다 — 내가 서 있던 땅이 움직였으니 다시 맞춰야 했다는 뜻. 횟수(`twice`)를 넣으면 rebase 가 두 번이었음이 한 단어로 전해진다. 남 탓 없이 상황만 서술하는 어투다.
- 예문: `main` moved twice under this change, so the branch was rebased and re-gated before the fast-forward.
- 유사어: the base advanced (중립·건조), upstream got ahead of us (구어)
- 반의어: a clean fast-forward

## "the reminder from yesterday still stands"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 이전에 알린 할 일이 아직 유효하다고 보고 말미에 다시 짚을 때(회의·채팅·문서 모두)
- 한국어: 어제 말한 주의사항은 여전히 유효하다
- 설명: `stand` 는 "효력이 살아 있다"의 뜻으로, 판정·제안·경고에 두루 쓴다(`the offer stands`). `still` 을 붙이면 "그 사이 아무것도 바뀌지 않았다"가 얹힌다. 새 정보가 없어도 잊히지 않게 붙드는 문장.
- 예문: And the office reminder from yesterday still stands — `office.py` needs re-copying before the window axis works there.
- 유사어: remains open (할 일 목록의 어투), is still on the table (제안에 한정)
- 반의어: is now moot / no longer applies

## "conceded, and it's the finding that mattered"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 외부 리뷰 결과를 판정할 때, 지적을 받아들이면서 그것이 이번 리뷰의 핵심이었다고 등급을 매길 때(격식)
- 한국어: 수용 — 그리고 이게 중요한 발견이었다
- 설명: 앞의 한 단어 `conceded` 로 판정을 끝내고, 뒤의 절이 무게를 준다. `the finding that mattered` 는 다른 finding 들을 부드럽게 내리누르는 최상급 없는 최상급이다. 수용 목록에서 하나만 이렇게 표시하면 읽는 이가 어디부터 볼지 안다.
- 예문: Spec (c)1 — conceded, and it's the finding that mattered.
- 유사어: the one that counts (구어), the substantive finding (문어)
- 반의어: a nit / noting for the record

## "rationalising a widening"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 내가 문서에 적어 둔 그럴듯한 근거가 실은 범위 확대를 사후 정당화한 것이었다고 스스로 인정할 때(격식·자기비판)
- 한국어: 범위가 넓어진 걸 그럴듯하게 둘러댄 것
- 설명: `rationalise` 는 "합리적으로 만들다"가 아니라 "이미 한 일에 이유를 갖다 붙이다"의 뜻이라 자기비판에 딱 맞는다. 목적어를 명사화한 `a widening` 으로 두면 "무엇을" 둘러댔는지가 한 단어에 담긴다. 영국식 철자(`-ising`)는 미국식 `-izing` 과 뜻 차이가 없다.
- 예문: My "one span, one label" note in MIGRATION was rationalising a widening nobody asked for.
- 유사어: dressing up (구어, "포장하다"), post-hoc justification (명사형, 더 학술적)
- 반의어: a stated, up-front reason

## "more build than it buys"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 제안된 안전장치가 그것이 막아 줄 위험보다 만드는 비용이 크다고 거절할 때(리뷰 답변·설계 논의)
- 한국어: 얻는 것보다 만드는 게 더 크다
- 설명: `build`(구축 비용)와 `buy`(얻는 효용)를 두운으로 맞춘 압축형. `it's not worth it` 보다 이유가 들어 있어 거절이 설득이 된다. 명사 `build` 가 "빌드 단계"와 "만드는 수고" 둘 다로 읽히는 것이 이 문맥에선 장점.
- 예문: A shared-source test across Python and TS for one constant is more build than it buys.
- 유사어: not worth the machinery (문어), the juice isn't worth the squeeze (관용·구어)
- 반의어: pays for itself

## "half wrong"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 상대 지적이 절반은 맞고 절반은 틀렸다고 판정 제목에 붙일 때(리뷰 판정·토론)
- 한국어: 절반은 틀림
- 설명: `partly wrong` 보다 각이 서 있다 — 어느 절반이 틀렸는지 곧바로 설명하겠다는 예고다. 판정표의 셀에 쓰면 "기각/수용" 이분법을 벗어나면서도 애매하지 않다. 뒤에는 반드시 맞은 절반과 틀린 절반을 갈라 써야 한다.
- 예문: Spec (b)1 — half wrong: the old office trend never spanned 30 days in the first place.
- 유사어: partly right (긍정 쪽에 무게), true but beside the point (사실은 맞는데 논점이 아닐 때)
- 반의어: dead on / entirely correct

## "read the constant, not the data flow"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 리뷰어가 코드의 숫자(상수)만 보고 실제 실행 경로에서 그 값이 작동하는지는 안 봤다고 반박할 때(기술 논쟁)
- 한국어: 상수만 읽고 데이터 흐름은 안 읽었다
- 설명: `A, not B` 대비로 상대의 조사 깊이를 한 줄에 그린다. `TREND_DAYS = 30` 이라는 선언과 "실제로 30일치가 흐르는가"는 다른 질문이고, 그 차이를 짚는 말이 이 문장이다. 비난보다는 진단 어투라 반박에 써도 거칠지 않다.
- 예문: The model read the constant, not the data flow — with ten runs per tool, the trend never reached 30 days.
- 유사어: took the code at face value (더 일반적), looked at the declaration, not the behaviour (풀어쓴 형태)
- 반의어: traced it end to end

## "Missed by both:"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 두 독립 리뷰 축이 모두 놓친 항목을 내가 덧붙일 때의 소제목(리뷰 보고·격식)
- 한국어: 양쪽 다 놓친 것:
- 설명: 주어와 동사를 지운 콜론 소제목. 앞에 두 리뷰가 있었다는 맥락이 있어야 `both` 가 산다. 리뷰를 종합하는 사람만 쓸 수 있는 자리이며, 그 뒤 항목은 "그러니 내 몫"이라는 뜻을 품는다.
- 예문: Missed by both: the stored `windowWeeks: 3` from yesterday's default silently stays 3 for anyone who already opened the page.
- 유사어: neither axis caught (완전한 절), what both overlooked (명사절, 문장 안에 넣을 때)
- 반의어: flagged on both axes

## "One hitch on the way"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 완료 보고 끝에, 결과엔 영향이 없었던 작은 걸림돌 하나를 덧붙일 때(구어·채팅)
- 한국어: 오는 길에 걸린 게 하나
- 설명: `hitch` 는 크지 않은 일시적 차질이다(`without a hitch` = 아무 문제 없이). `on the way` 가 "결과가 아니라 과정에서"를 한정해 읽는 이를 안심시킨다. 콜론 없이 문장으로 이어 가면 자연스럽다.
- 예문: One hitch on the way: the fast-forward first refused because my untracked spec copy collided with the now-tracked file.
- 유사어: a small snag (같은 크기의 차질), a bump along the way (더 구어)
- 반의어: went through without a hitch

## "(the boot log) will flag both STALE until then"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 어떤 작업을 마치기 전까지 시스템이 경고를 계속 띄울 것이라고 미리 알릴 때(운영 안내)
- 한국어: 그때까지는 부팅 로그가 둘 다 STALE 로 표시할 것이다
- 설명: `flag X (as) Y` 는 "Y 라고 표시해 눈에 띄게 하다". `until then` 이 조건("복사하기 전까지")을 앞 문장에서 받아 온다. 경고가 버그가 아니라 예상된 상태임을 미리 말해 주는 문장이라, 사무실에서 로그를 보고 놀라지 않게 한다.
- 예문: The boot log will flag both adapters STALE until then — that's expected, not a regression.
- 유사어: will keep warning (더 평이), will show up as STALE (표시 결과 중심)
- 반의어: will go quiet once copied

## "arming a waiter on it"
- 레지스터: technical, casual
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 오래 걸리는 백그라운드 작업(테스트 스위트)의 완료를 알릴 감시 장치를 걸어 두겠다고 짧게 말할 때(개발 채팅)
- 한국어: 거기에 대기 장치를 걸어 둔다
- 설명: `arm` 은 알람·트랩·폭탄을 "작동 대기 상태로 만들다". 감시 스크립트를 세운다는 뜻으로 옮겨 오면 "걸어 두고 기다린다"가 한 단어가 된다. `on it` 이 감시 대상. 격식 문서엔 `set up a watcher` 가 안전하다.
- 예문: Only the full-suite result gates the merge; arming a waiter on it.
- 유사어: setting up a watcher (중립·문어), keeping an eye on it (구어, 사람이 볼 때)
- 반의어: polling it by hand

## "X gates the merge"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 머지 전에 남은 유일한 조건이 무엇인지 말할 때(CI·릴리스 대화)
- 한국어: X 가 머지의 관문이다 / X 만 통과하면 머지한다
- 설명: 명사 `gate`(관문)를 동사로 쓴 형태. `Only … gates` 로 쓰면 "다른 건 다 끝났다"가 덤으로 전해진다. `blocks` 는 부정적(막힘)이고 `gates` 는 절차적(통과 조건)이라 뉘앙스가 다르다.
- 예문: Only the full-suite result gates the merge; everything else is staged.
- 유사어: is the last blocker (구어, 장애물 느낌), is a precondition for (문어)
- 반의어: is advisory only

## "fails here, not inside two paid model calls"
- 레지스터: professional, technical
- 출처: transcript:[user] skewnono-v3-nuxt 4a1eae66 (oc-review 스킬 본문)
- 맥락: 비싼 단계 앞에 값싼 검증을 두는 이유를 설명할 때(절차 문서·설계 근거)
- 한국어: 여기서 실패하지, 유료 모델 호출 두 번 안에서 실패하지 않는다
- 설명: `A, not B` 대비에 비용(`paid`)을 박아 넣어 "빨리 실패하기"의 이유를 돈으로 보여 준다. `here` 가 검증 위치를 가리키는 지시어라 앞에 실제 명령이 있어야 한다. 절차 문서에서 "왜 이 순서냐"를 한 줄로 끝내는 방식.
- 예문: A bad ref or an empty diff fails here, not inside two paid model calls.
- 유사어: fail fast, before the expensive step (일반 원칙형), catches it up front (구어)
- 반의어: surfaces only after the spend

## "defaulting up costs little"
- 레지스터: professional
- 출처: transcript:[user] skewnono-v3-nuxt 4a1eae66 (oc-review 스킬 본문)
- 맥락: 더 비싼 선택지를 기본값으로 두어도 추가 비용이 적다고 정당화할 때(도구 설정·정책 문서)
- 한국어: 상위 등급을 기본으로 잡아도 비용이 거의 안 든다
- 설명: `default up`(더 높은 쪽을 기본으로 삼다)은 `default to X` 를 방향 부사로 줄인 형태다. 뒤의 `costs little` 이 그 결정의 근거. "왜 heavy 가 기본이냐"에 대한 답으로, 성능이 좋아서가 아니라 싸서라는 점이 핵심이다.
- 예문: It was also the fastest verified reviewer, so defaulting up costs little.
- 유사어: erring on the heavier side (더 풀어쓴 형태), a cheap upgrade (명사형)
- 반의어: start light and escalate

## "where this skill earns its keep"
- 레지스터: conversational, professional
- 출처: transcript:[user] skewnono-v3-nuxt 4a1eae66 (oc-review 스킬 본문)
- 맥락: 도구·절차의 여러 단계 중 진짜 가치가 나오는 한 곳을 가리킬 때(문서·설명)
- 한국어: 이 스킬이 제 밥값을 하는 자리
- 설명: `earn one's keep` 은 "숙식비를 벌다", 곧 존재 이유를 증명하다. 사람·개·도구 모두에 쓴다. 관계부사 `where` 로 앞 명사(third section)를 받아 "다른 데는 부수적"이라는 함의를 만든다.
- 예문: Rules for the third section, which is where this skill earns its keep: name disagreements explicitly.
- 유사어: pulls its weight (같은 뜻, 조금 더 구어), justifies its existence (문어·딱딱)
- 반의어: is dead weight

## "turns a plausible finding into a quotable one"
- 레지스터: professional
- 출처: transcript:[user] skewnono-v3-nuxt 4a1eae66 (oc-review 스킬 본문)
- 맥락: 인용 출처를 직접 열어 확인하는 수고가 왜 값어치 있는지 설명할 때(리뷰 절차·문서)
- 한국어: 그럴듯한 발견을 인용 가능한 발견으로 바꾼다
- 설명: `plausible`(그럴듯함)과 `quotable`(남 앞에 내놓을 수 있음)의 대비가 문장의 전부다. `turn A into B` 로 검증 행위의 효과를 변환으로 그린다. 두 형용사 뒤에 `one` 을 두어 `finding` 반복을 피했다.
- 예문: Opening the cited line also turns a plausible finding into a quotable one.
- 유사어: makes it defensible (방어 가능성에 초점), upgrades it from hunch to evidence (구어)
- 반의어: leaves it as hearsay

## "reads the diff cold"
- 레지스터: professional
- 출처: transcript:[user] skewnono-v3-nuxt 4a1eae66 (oc-review 스킬 본문)
- 맥락: 사전 맥락이 전혀 없는 검토자의 장점을 말할 때(리뷰 위임의 근거)
- 한국어: 사전 지식 없이 diff 를 읽는다
- 설명: 부사 `cold` 는 "준비·예열 없이"(`cold read`, `go in cold`). 여기서는 대화 이력이 없다는 뜻이며, 그것이 단점이 아니라 "가정에 물들지 않았다"는 장점으로 뒤집힌다. 앞 문장 `carries every assumption that produced it` 과 짝을 이룬다.
- 예문: A model with no such history reads the diff cold — that is the entire value here.
- 유사어: with fresh eyes (더 부드러움), without prior context (문어·중립)
- 반의어: carries every assumption that produced it

## "going direct after reading"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt 8aed5687
- 맥락: 정식 절차(스킬·템플릿)를 건너뛰고 바로 작업에 들어가겠다고 짧게 선언할 때(개발 채팅)
- 한국어: 읽고 나서 바로 진행한다
- 설명: `go direct` 는 중간 단계 없이 곧장 간다는 구어. 앞에 "맞는 절차가 없다"는 이유를 붙여야 게으름이 아니라 판단으로 읽힌다. `after reading` 이 "읽는 건 건너뛰지 않는다"는 최소 조건을 남긴다.
- 예문: No process skill fits a one-file diagnostic script; going direct after reading.
- 유사어: skipping the ceremony (구어·약간 냉소), proceeding without a plan doc (문어)
- 반의어: going through the full process

## "fails cleanly at each stage instead of tracebacking"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 8aed5687
- 맥락: 진단 스크립트가 예외 덤프 대신 단계 이름과 원인을 찍고 멈춘다고 검증 결과를 보고할 때
- 한국어: 각 단계에서 깔끔하게 실패한다, 트레이스백을 뿜지 않고
- 설명: `fail cleanly` 는 "의도된 방식으로 실패"다. `traceback` 을 동사로 쓴 `tracebacking` 은 사전엔 없는 개발자 조어지만 파이썬 팀에선 바로 통한다. 격식 문서엔 `instead of raising an unhandled exception` 이 안전하다.
- 예문: A real run at home fails cleanly at each stage instead of tracebacking.
- 유사어: degrades gracefully (시스템 전체에 대해), reports cause and next action (실패 시 출력 내용에 초점)
- 반의어: blows up with a stack trace

## "silently falls through to (a fallback)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 8aed5687
- 맥락: 조건이 안 맞을 때 오류 없이 다음 분기로 조용히 흘러가 잘못된 결과를 정상처럼 보여 주는 버그를 설명할 때
- 한국어: 소리 없이 다음 경로로 떨어진다
- 설명: `fall through` 는 switch 문의 관통에서 온 은유로, "잡히지 않고 아래로 빠진다". `silently` 가 이 동작이 위험한 이유(경고 없음)를 담는다. 그 결과가 무엇처럼 보이는지(`the browser shows "never measured"`)를 이어 쓰면 버그 보고가 완성된다.
- 예문: A loader writing to db1 produces a nil, not an error, and the adapter's `_bail` silently falls through to meas_hist.
- 유사어: quietly degrades to (더 부드러움), defaults to X without warning (풀어쓴 형태)
- 반의어: fails loudly

## "Fixture diffs are key re-sorting; skipping those."
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 리뷰 첫 줄에서 내용 없는 변경(정렬 순서만 바뀐 픽스처)을 검토 대상에서 뺀다고 선언할 때
- 한국어: 픽스처 diff 는 키 재정렬뿐이라 건너뛴다
- 설명: 세미콜론으로 사실과 결정을 붙였다. `X are Y` 로 diff 의 정체를 규정한 뒤 주어 없는 `skipping those` 로 행동을 적는 리뷰어 특유의 생략문. 무엇을 안 봤는지를 먼저 밝히면 나머지 finding 의 범위가 분명해진다.
- 예문: Fixture diffs are key re-sorting; skipping those and reading the code hunks.
- 유사어: generated churn, not complexity (기존 노트; 판단 근거 쪽), noise, not signal (구어)
- 반의어: a substantive hunk

## "consequence is mild since it's a cap, not a formula"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 지적을 하되 그 심각도가 낮은 이유를 값의 역할(상한 vs 계산식)로 설명할 때(리뷰 finding 의 꼬리)
- 한국어: 상한값이지 계산식이 아니라서 영향은 가볍다
- 설명: 리뷰어가 스스로 finding 의 등급을 내리는 문장. `cap`(넘지 못하는 선)이 틀리면 조금 덜 모으는 데서 끝나지만 `formula` 가 틀리면 모든 결과가 어긋난다 — 그 차이가 `mild` 의 근거다. `A, not B` 로 값의 성격을 규정한 뒤 결과를 붙이는 구조.
- 예문: Mark the daily-frequency assumption OFFICE-VERIFY; consequence is mild since it's a cap, not a formula.
- 유사어: low blast radius (구어·기술), bounded impact (문어)
- 반의어: propagates into every result

## "Commit 2 itself demonstrates the hazard"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 지적하려는 위험이 가설이 아니라 검토 대상 안에서 이미 한 번 일어났다고 증거를 댈 때(리뷰)
- 한국어: 두 번째 커밋이 그 위험을 몸소 보여 준다
- 설명: 재귀대명사 `itself` 가 "다른 데서 찾을 것도 없이 바로 이 diff 가" 를 강조한다. `demonstrate` 는 "보여 주다"보다 "입증하다"에 가깝다. 이어서 커밋 메시지를 인용하면 finding 이 반박하기 어려워진다.
- 예문: Commit 2 itself demonstrates the hazard — "두 곳이 같은 값을 들어야 하므로 함께 바꿉니다."
- 유사어: is a case in point (관용, 같은 뜻), proves the point (구어)
- 반의어: is hypothetical so far

## "nothing ties them, so drift surfaces only as (runtime 400s)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 두 값을 묶는 검증이 없어서 어긋남이 늦게, 나쁜 형태로만 드러난다고 설명할 때
- 한국어: 둘을 묶는 게 없어 어긋남은 런타임 400 으로만 드러난다
- 설명: `ties` 는 두 값을 기계적으로 결합하는 테스트·빌드를 뜻한다. `surfaces only as` 가 핵심 — 문제가 "없다"가 아니라 "가장 늦은 곳에서만 보인다"는 진단이다. `only as` 뒤에 증상을 넣으면 위험의 형태가 구체화된다.
- 예문: Each suite pins its own side; nothing ties them, so drift surfaces only as runtime 400s or a silent normalize-to-default.
- 유사어: caught only in production (더 일반적), no test spans the two (풀어쓴 형태)
- 반의어: pinned by a shared-source test

## "the repo's rationale overrides the baseline smell"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 일반 규칙상 냄새지만 저장소가 그 이유를 문서화해 두었으니 지적을 접는다고 밝힐 때(리뷰)
- 한국어: 저장소가 밝힌 근거가 일반 기준의 냄새보다 우선한다
- 설명: 우선순위 규칙을 문장으로 적용한 것. `override` 는 상위 규칙이 하위 규칙을 무효로 한다는 뜻이며, 여기서는 "문서화된 의도 > 범용 체크리스트". 리뷰어가 스스로 finding 을 억제할 때 그 근거를 남기는 방식이다.
- 예문: It is explicitly documented as deliberate, so the repo's rationale overrides the baseline smell.
- 유사어: a documented exception (명사형), design intent wins here (구어)
- 반의어: no rationale on record

## "unusually thorough"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 리뷰를 마치며 테스트 범위 같은 강점을 짧게 칭찬할 때(격식)
- 한국어: 보기 드물게 꼼꼼한
- 설명: `very thorough` 는 밋밋하고 `unusually` 는 비교 기준(보통의 PR)을 암시해 칭찬에 무게가 실린다. 괄호 안에 무엇이 꼼꼼했는지 셋쯤 나열하면 빈말이 아니게 된다. 부정 finding 뒤에 두면 리뷰 전체의 균형이 잡힌다.
- 예문: Otherwise clean; the test coverage (route refusal, lookback and cap moving together, echo on every unavailable branch) is unusually thorough.
- 유사어: exhaustive (빠짐없음에 초점), meticulous (사람의 태도에 초점)
- 반의어: thin coverage

## "This deserves at least a (spec line or) note"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-26-window-weeks-two-axis-review.md
- 맥락: 동작 변경을 되돌리라고까지는 안 하되 문서 한 줄은 있어야 한다고 최소 요구를 낼 때(리뷰)
- 한국어: 최소한 스펙 한 줄이나 메모는 있어야 한다
- 설명: `deserve` 로 "받아 마땅하다"를 말하고 `at least` 로 요구의 하한을 정한다. 뒤에 `or` 로 두 선택지를 주면 구현자가 고를 수 있어 지적이 명령이 아니라 제안이 된다. 되돌리기와 방치 사이의 제3안을 제시하는 문형.
- 예문: This deserves at least a spec line or an OFFICE-VERIFY note — MDC epochs got exactly such a carve-out, BSM/PM did not.
- 유사어: warrants a mention (문어), at minimum, document it (직설)
- 반의어: can go unremarked

## "that duplication is deliberate and ends in Task 7"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 계획 문서에서 일시적으로 생기는 중복이 실수가 아니며 언제 사라지는지 미리 알릴 때
- 한국어: 그 중복은 의도된 것이고 Task 7 에서 끝난다
- 설명: 리뷰어가 "중복이네요" 하기 전에 선수를 치는 문장. `deliberate` 가 의도를, `ends in` 이 수명을 말해 두 질문("왜?", "언제까지?")을 한 번에 닫는다. 지시대명사 `that` 이 바로 앞 문장의 상황을 가리킨다.
- 예문: Task 4 creates `normalize.py` while `writer/normalize.py` still exists; that duplication is deliberate and ends in Task 7.
- 유사어: temporary by design (명사구), a stepping stone, not the end state (구어)
- 반의어: an accidental copy

## "Compare X totals, not X alone"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 환경에 따라 숫자가 달리 보이므로 어떤 값을 비교해야 하는지 지침으로 줄 때
- 한국어: 합계를 비교하라, 그 값 하나만 보지 말고
- 설명: 명령문 + `not … alone` 꼬리. `alone` 이 "그것만으로는 오해한다"를 담는다. 앞 문장에 왜 숫자가 다른지(worktree 엔 office 파일이 없어 skip 이 늘어남) 이유가 있어야 지침이 산다.
- 예문: Provider tests that skip without office files show different skip counts in a worktree — compare `passed + skipped` totals, not `passed` alone.
- 유사어: look at the sum, not one column (풀어쓴 형태), judge by the aggregate (문어)
- 반의어: eyeball the raw count

## "refusing to start would cost more than one bad value"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 잘못된 설정값을 만났을 때 예외 대신 기본값으로 넘어가는 설계를 정당화할 때(docstring·설계 근거)
- 한국어: 기동을 거부하는 쪽이 잘못된 값 하나보다 비싸다
- 설명: 두 실패의 비용을 저울에 올린 문장. 동명사 주어 `refusing to start` 와 명사구 `one bad value` 를 `cost more than` 으로 잇는다. 앞에 `it is plumbing` 같은 성격 규정이 있어야 "왜 관대해도 되는지"가 완성된다.
- 예문: A typo'd env var must not take the scheduler down at boot — it is plumbing, and refusing to start would cost more than one bad value.
- 유사어: fail open here (기술 은어), tolerate rather than abort (문어)
- 반의어: fail fast on bad config

## "an orphan-clear window, NOT a runtime budget"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 설정값이 흔히 오해되는 뜻이 아니라 다른 뜻임을 주석에서 못 박을 때
- 한국어: 고아 락을 치우는 시간 창이지, 실행 시간 예산이 아니다
- 설명: `A, NOT B` 에서 B 가 바로 "흔한 오해"다. 대문자 `NOT` 은 코드 주석에서 강조를 얻는 관행. 뒤에 "왜 오해하기 쉬운지"(`Do NOT reason "weekly job, weekly TTL"`)까지 적어 두면 미래의 수정자가 같은 실수를 안 한다.
- 예문: `lock_ttl` is an orphan-clear window, NOT a runtime budget — a live run re-arms its own TTL.
- 유사어: a cleanup horizon (명사 대체), bounds the orphan, not the run (풀어쓴 형태)
- 반의어: a hard deadline for the job

## "Tuning must not require a deploy."
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 값을 상수가 아니라 환경변수로 두는 이유를 제약 조건으로 적을 때(설계 제약·계획 문서)
- 한국어: 값을 조정하는 데 배포가 필요해선 안 된다
- 설명: 다섯 단어짜리 제약. `must not require` 가 설계 요구사항의 어투이고, `a deploy`(명사화된 배포)가 비용을 대표한다. 이유 문장이라기보다 규칙 문장이라 근거 없이도 서며, 앞에 "무엇을 env 로 뺐는지"가 온다.
- 예문: Retention and paths are env vars, not constants — tuning must not require a deploy.
- 유사어: configurable at runtime (형용사형), no redeploy to change it (구어)
- 반의어: baked in at build time

## "the one that is broken today"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 여러 경우 중 지금 실제로 고장 나 있는 하나를 지목해 우선순위를 줄 때
- 한국어: 지금 당장 고장 나 있는 그 경우
- 설명: `the one` 이 앞의 목록(세 경우) 중 하나를 골라내고, `today` 가 "이론상 위험"과 "현재 결함"을 가른다. 계획 문서에서 이 한 구가 "왜 이 태스크가 있는지"를 대신한다.
- 예문: Three cases in order: uWSGI, the Werkzeug reloader, otherwise this process. The reloader case is the one that is broken today.
- 유사어: the live bug (구어), the case currently misbehaving (문어)
- 반의어: a theoretical edge case

## "(a roster gap) cannot look like (a quiet fab)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md
- 맥락: 데이터 누락이 "이상 없음"으로 오인되지 않도록 설계했다고 커밋 메시지·문서에 적을 때
- 한국어: 명단 누락이 조용한 fab 처럼 보일 수 없다
- 설명: 같은 화면(빈 보드)이 두 원인(진짜 조용함 / 매핑 실패)에서 나올 때, 그 둘을 구분되게 만드는 것이 설계의 핵심이다. `cannot look like` 가 "구별 불가능한 상태를 없앴다"를 한 구로 말한다. 앞의 `counted into … rather than dropped silently` 가 그 수단.
- 예문: Alarms from equipment the roster does not carry are counted into `unmatched_count` rather than dropped silently, so a roster gap cannot look like a quiet fab.
- 유사어: is distinguishable from (문어·중립), can't masquerade as (기존 노트 `masquerading` 계열, 더 강함)
- 반의어: is indistinguishable from

## "The accepted loss:"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 설계 선택의 단점을 숨기지 않고 "알고도 감수한다"고 docstring 끝에 명시할 때
- 한국어: 감수하기로 한 손실:
- 설명: 콜론 소제목. `accepted` 가 "몰랐다"를 미리 차단하고, `loss` 가 미화를 거부한다. 뒤에는 무엇을 잃는지(`a run missed while the process is down is skipped rather than detected`)를 한 문장으로 적는다. 트레이드오프 문서의 결말 관용구.
- 예문: The accepted loss: a run missed while the process is down is skipped rather than detected as missed.
- 유사어: the trade-off we take (구어), known limitation (문서 항목명)
- 반의어: an unintended side effect

## "routine here, not rare"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 드물어 보이는 상황이 이 환경에서는 일상이라서 대비가 필요하다고 근거를 댈 때
- 한국어: 여기서는 일상이지, 드문 일이 아니다
- 설명: `X, not Y` 대비의 짧은 꼬리형. `here` 가 "일반론과 달리 이 환경에선"을 한정한다. 앞에 수치(`max-requests = 1000`)가 있어야 `routine` 이 주장이 아니라 사실이 된다. 예외 처리 코드에 왜 정성을 들였는지 설명하는 자리.
- 예문: With `max-requests = 1000` in wsgi.ini, worker recycles are routine here, not rare.
- 유사어: the common case, not the edge (풀어쓴 형태), happens all the time (구어)
- 반의어: a once-in-a-blue-moon event

## "Why X exists at all:"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md
- 맥락: 코드·데이터 구조의 존재 이유부터 설명해야 뒤의 결정이 이해될 때 docstring 을 여는 소제목
- 한국어: 애초에 X 가 왜 있는가:
- 설명: `at all` 이 "왜 이렇게"가 아니라 "왜 있기나 한지"로 질문의 층을 한 단계 올린다. 뒤에 `cannot be recovered by query` 같은 불가능성이 오면 존재 이유가 증명된다. 미래의 "이거 지워도 되나"를 막는 한 줄.
- 예문: Why the snapshot exists at all: the process-step source is a current-state index, so "how many steps three weeks ago" cannot be recovered by query.
- 유사어: the reason this is here (평이), raison d'être (차용어·문어)
- 반의어: (마땅한 대체 표현 없음)
