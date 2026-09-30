# 2026-10-01 — 새 표현

> 오늘 배치는 repo 문서 4건과 transcript 19건이다. 영어 문서는 `hardware_fdc_fleet_verification.md` 한 편인데 어제 거의 다 뽑아 써서 표현 소스로는 쉬게 했다. 나머지 문서(MDC·FDC 데이터 표 메모, equipment-data-map 인계 문서)는 한국어 위주다. 오늘 표현은 대부분 transcript 의 어시스턴트 답변에서 나왔다. RCS headless 제어 검토, 사무실 LLM 과 병렬로 일하는 방법, NCC 예외 규칙을 모든 레시피에 써도 되는지 따진 답이 특히 알찼다. `last resort`, `fail open / fail closed`, `tear down`, `momentum is cheapest there`, `Red for the right reason.`, `kill switch`, `in the meantime`, `on purpose` 는 노트에 이미 있어서 뺐다.

## "Where it could quietly break"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator (RCS headless 제어 검토)
- 맥락: 새 방식을 도입할 때 겉으로는 멀쩡한데 속으로 틀어질 수 있는 지점을 꼽는 소제목(설계 검토 글, 기술).
- 한국어: 조용히 망가질 수 있는 곳
- 설명: `quietly` 가 핵심이다. 에러를 내며 멈추는 게 아니라 결과만 슬쩍 틀리는 실패를 가리킨다. 원문은 "지금 무엇이 나아지나" 표 바로 뒤에 이 제목을 두어 장점과 위험을 짝지었다. 제목이라 주어 없이 `Where` 절만 쓴다.
- 예문: Before we switch to posted messages, let's list where it could quietly break, starting with modifier keys.
- 유사어: failure modes (기술 용어, 더 딱딱함), what could go wrong (구어), silent failure points (명사구, 문서체)
- 반의어: fail loudly (요란하게 실패해 바로 드러나다)

## "A stale frame is worse than a slow one."
- 레지스터: technical
- 출처: transcript:auto-recipe-creator (RCS headless 제어 검토)
- 맥락: 느린 것과 틀린 것 중 무엇이 더 나쁜지 한 문장으로 못 박을 때(기술 판단, 구어·문어 겸용).
- 한국어: 낡은 프레임이 느린 프레임보다 더 나쁘다.
- 설명: `one` 이 앞의 `frame` 을 받아 반복을 피한다. `stale` 은 "시간이 지나 신선하지 않은", 곧 지금 상태를 반영하지 않는 데이터다. 클릭할 때마다 화면을 다시 찍어 확인하는 루프에서는 느린 캡처는 기다리면 되지만 낡은 캡처는 잘못된 판단으로 이어진다는 논리다.
- 예문: The whole loop re-captures after each click, so a stale frame is worse than a slow one.
- 유사어: Wrong data is worse than late data. (일반화한 문장), Better late than wrong. (속담 비틀기, 구어)
- 반의어: Any frame is better than none. (없는 것보다는 뭐라도 낫다)

## "lose sight of what it's doing"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (RCS headless 제어 검토)
- 맥락: 자동화가 눈에 안 보이게 되면서 사람이 감독하지 못하게 되는 위험을 말할 때(검토·회의, 중립).
- 한국어: 그것이 무엇을 하는지 놓치다, 시야에서 잃다
- 설명: `lose sight of` 는 원래 "시야에서 놓치다"이고 비유로 "목표·상황을 잊다"에도 쓴다. 원문은 `Losing sight of what it's doing.` 을 굵은 글씨 항목 제목으로 썼다. 바로 뒤에 "지금은 엔지니어가 자동화가 생산 장비를 클릭하는 걸 볼 수 있다"로 무엇을 잃는지 구체적으로 댄다.
- 예문: Invisible clicks mean the engineer loses sight of what the automation is doing on production equipment.
- 유사어: lose track of (진행 상황을 놓치다, 더 일상적), lose visibility into (업무 보고서체), fly blind (감 없이 진행하다, 구어)
- 반의어: keep an eye on (계속 지켜보다)

## "until you trust it"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (RCS headless 제어 검토)
- 맥락: 새 기능을 바로 믿지 말고 안전장치를 켠 채 쓰다가 믿음이 생기면 풀라고 권할 때(조언, 구어).
- 한국어: 믿을 만해질 때까지
- 설명: 기간을 날짜가 아니라 신뢰라는 조건으로 정한다. `until it's proven` 보다 사람 쪽 판단을 강조한다. 원문은 "알림을 켜 두거나 기본으로 보이게 실행하라"는 지시 끝에 이 구를 붙였다.
- 예문: Keep a notification, or run visibly by default, until you trust it.
- 유사어: until it has earned your trust (조금 더 격식), until you're comfortable with it (구어), until it's proven in practice (문어)

## "I wouldn't go there."
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (RCS headless 제어 검토)
- 맥락: 선택지 중 하나를 짧고 단호하게 권하지 않을 때(구어, 동료 사이).
- 한국어: 거기까지는 안 가겠다, 그건 권하지 않는다
- 설명: 직역하면 "나라면 그쪽으로 안 간다". `would` 가 "내가 너라면"을 깔고 있어서 명령이 아니라 조언이 된다. 원문은 headless 방식 세 가지를 설명한 뒤 "세 번째(RCS 프로토콜 직접 제어)는 벤더에 달린 별개 프로젝트"라고 하고 이 말로 닫았다.
- 예문: The third option would be a different, vendor-dependent project; I wouldn't go there.
- 유사어: I'd steer clear of that. (구어), I wouldn't recommend it. (격식 중간), That's a rabbit hole. (끝없이 빠져드는 일, 구어)
- 반의어: I'd go for it. (해 볼 만하다)

## "won't work the way you expect"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator (사무실 LLM 병렬 작업)
- 맥락: 상대가 제안한 방법이 겉보기와 달리 동작한다는 걸 부드럽게 알릴 때(기술 상담, 중립).
- 한국어: 생각하는 대로 동작하지 않는다
- 설명: "안 된다"고 잘라 말하지 않고 "기대와 다르게 된다"로 돌려 말해 상대 체면을 지킨다. 뒤에 반드시 이유가 와야 자연스럽다. 원문은 폴더를 복사해도 import 가 원본을 불러와 사무실 LLM 의 수정이 아무 효과가 없다는 설명을 이어 붙였다.
- 예문: Copying the folder won't work the way you expect, because every import still points at the original package.
- 유사어: won't do what you think (구어), doesn't behave as you'd assume (격식 중간), there's a catch (구어, 짧게)
- 반의어: works out of the box (손대지 않아도 바로 된다)

## "Which fits depends on one thing: …"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (사무실 LLM 병렬 작업)
- 맥락: 선택지 두세 개를 설명한 뒤 결정 기준을 질문 하나로 좁힐 때(제안·상담, 중립).
- 한국어: 어느 쪽이 맞는지는 한 가지에 달려 있다: …
- 설명: 주어 `Which fits` 는 간접의문절(어느 것이 맞는지)이다. 콜론 뒤에 질문을 그대로 두면 상대가 바로 답할 수 있다. 원문은 `can the office PC push to GitHub?` 를 붙이고 "yes 면 Option 1, pull 만 되면 Option 2"로 분기를 끝냈다.
- 예문: Which fits depends on one thing: can the office PC push to GitHub?
- 유사어: It all comes down to … (구어), The deciding factor is … (격식), It hinges on … (문어, 약간 격식)

## "the break shows up right away instead of failing silently"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator (사무실 LLM 병렬 작업)
- 맥락: 테스트나 검사를 두는 이유를 "문제가 즉시 드러나게"로 설명할 때(기술 문서).
- 한국어: 조용히 실패하는 대신 깨진 게 바로 드러난다
- 설명: `break` 가 명사로 "깨진 곳, 파손"이다. `show up` 은 "나타나다"의 구어형. `instead of failing silently` 가 막으려는 대안을 명시해 테스트의 가치를 대비로 보여 준다. 원문은 Mac 에서 함수 이름을 바꾸면 사무실 폴더의 작은 테스트가 곧바로 깨지게 해 두었다는 설명이다.
- 예문: If I rename a function on the Mac, the break shows up right away instead of failing silently at the office.
- 유사어: it fails fast (기술 관용구), it surfaces immediately (문어), you find out on the spot (구어)
- 반의어: goes unnoticed (눈치채지 못하고 지나가다)

## "This is the real danger."
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 위험 목록 중 진짜 신경 써야 할 하나를 골라 강조할 때(위험 평가 표·보고서).
- 한국어: 이게 진짜 위험이다.
- 설명: 다른 행은 "낮음: 안전하게 멈춘다"라고 적은 뒤 이 행만 굵게 이 말을 달았다. `real` 이 "나머지는 이름만 위험"이라는 대비를 만든다. 짧은 문장이라 표 안에서 더 눈에 띈다.
- 예문: If the matcher picks the wrong neighbour and NCC still favours it, the rule approves the wrong spot. This is the real danger.
- 유사어: This is the one that matters. (구어), This is the critical risk. (보고서체), That's where it bites. (구어, 비유)
- 반의어: This is harmless. (문제될 게 없다)

## "backed by a count rather than a hunch"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 조건을 하나 더할 때 감이 아니라 측정한 숫자를 근거로 삼겠다고 할 때(설계 판단, 격식 중간).
- 한국어: 짐작이 아니라 센 숫자로 뒷받침되는
- 설명: `backed by` 는 "~로 뒷받침되는". `hunch` 는 근거 없는 감이다. `count` 는 여기서 "실제로 센 건수"라서 `data` 보다 구체적이다. 원문은 "데이터가 갈라지는 곳에만 분기를 넣고 그 분기는 모두 이렇게 숫자로 뒷받침한다"는 권고였다.
- 예문: Each of those would be one condition inside the gate, backed by a count rather than a hunch.
- 유사어: grounded in data (격식), based on numbers, not gut feel (구어), evidence-based (보고서체)
- 반의어: a shot in the dark (어림짐작)

## "by guesswork"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 근거 없이 짐작으로 무언가를 추가·결정하는 방식을 거절할 때(상담·리뷰).
- 한국어: 짐작으로, 감으로 때려 맞춰서
- 설명: `guesswork` 는 셀 수 없는 명사로 "짐작으로 하는 작업"이다. 원문 `Not yet for all recipes, and not by adding branches by guesswork either.` 는 질문 두 개(모든 레시피에 써도 되나? 분기를 넣어야 하나?)에 `not … either` 로 한 번에 "둘 다 아니다"라고 답한다.
- 예문: Not yet for all recipes, and not by adding branches by guesswork either.
- 유사어: by trial and error (시행착오로, 뉘앙스가 조금 다름), on a hunch (감으로), off the cuff (즉석에서, 구어)
- 반의어: by measurement (측정해서)

## "The rescue rate doesn't offset them."
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 좋은 효과가 있어도 나쁜 효과를 상쇄하지 못한다고 비용·편익을 따질 때(분석 보고, 격식).
- 한국어: 구해 낸 비율이 그것들을 상쇄하지 못한다.
- 설명: 동사 `offset` 은 "상쇄하다, 벌충하다". `them` 은 앞 문장의 false accepts(잘못 통과시킨 건)다. 원문은 이 규칙이 "멈추고 묻기"를 "실행하기"로만 바꾸므로 비용은 전부 잘못 통과시킨 건이고 구해 낸 건이 많아도 그걸 메우지 못한다고 설명했다.
- 예문: Its cost is entirely false accepts, and the rescue rate doesn't offset them.
- 유사어: cancel out (구어), make up for (구어, "벌충하다"), compensate for (격식)
- 반의어: compound (악화시키다, 더하다)

## "a mitigation, not a guarantee"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 어떤 조치가 위험을 줄일 뿐 없애지는 못한다고 선을 그을 때(위험 분석, 격식).
- 한국어: 완화책이지 보장은 아니다
- 설명: `A, not B` 구조로 독자가 과신하지 않게 한다. `mitigation` 은 위험을 "줄이는" 조치라는 뜻의 격식어다. 원문은 같은 프레임 안에서 NCC 를 비교하면 프레임 전체에 고르게 걸린 drift 는 상쇄되지만 부분 음영·차징은 못 없앤다고 설명한 뒤 이 구로 정리했다.
- 예문: That's why "same frame" is a mitigation, not a guarantee.
- 유사어: it reduces the risk, it doesn't remove it (평이), a safeguard, not a cure (비유), a partial fix (구어)
- 반의어: a guarantee (보장), foolproof (절대 실패하지 않는)

## "was held back by … (by 0.001)"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator (office 판정 결과 해석)
- 맥락: 결과는 좋았는데 어떤 검사가 막아 세웠다고 얼마 차이로 막혔는지까지 보고할 때(분석 보고).
- 한국어: …에 발목이 잡혔다 (0.001 차이로)
- 설명: `hold back` 은 "붙잡아 두다, 진행을 막다". 수동태로 쓰면 "좋은 결과인데 억울하게 막혔다"는 뉘앙스가 난다. 뒤의 `by 0.001` 에서 `by` 는 차이의 크기를 나타낸다(win by two points 와 같은 쓰임).
- 예문: The numbers show a correct, strong match that was held back by a chamfer ambiguity check, by 0.001.
- 유사어: was blocked by (평이), was stopped short by (조금 문어), was tripped up by (걸려 넘어지다, 구어)
- 반의어: sailed through (거침없이 통과했다)

## "instead of racing the hotkey"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (Ctrl+Alt+Q 로 멈춘 뒤 판정 해석)
- 맥락: 타이밍 맞춰 버튼을 누르는 번거로운 방법 대신 더 깔끔한 방법을 제안할 때(구어, 동료 사이).
- 한국어: 단축키로 타이밍 싸움을 하는 대신
- 설명: `race` 가 타동사로 "~와 경주하다", 곧 시간 싸움을 하다. 사용자가 search-around 가 시작되기 전에 Ctrl+Alt+Q 를 누르려고 서두르던 상황을 한 단어로 그렸다. 제안은 `ALIGN_FAIL_FALLBACK_SEARCH=0` 으로 처음부터 검색을 끄는 것.
- 예문: A cleaner way to run this: instead of racing the hotkey, run with the search turned off.
- 유사어: instead of trying to beat the timing (평이), rather than a race against the clock (구어)
- 반의어: take your time (서두르지 않다)

## "This last line tells you nothing."
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (Ctrl+Alt+Q 로 멈춘 뒤 판정 해석)
- 맥락: 로그·보고서의 특정 줄이 정보 가치가 없다고 딱 잘라 알려 줄 때(구어, 설명).
- 한국어: 이 마지막 줄은 아무것도 알려 주지 않는다.
- 설명: 무생물 주어 + `tell you` 는 영어에서 아주 흔한 설명 방식이다. 한국어로는 "이 줄로는 알 수 있는 게 없다"가 자연스럽다. 원문은 굵게 쓰고 바로 뒤에 "멈췄다는 사실만 말한다"고 이유를 붙였다.
- 예문: This last line tells you nothing: it only says you stopped the search.
- 유사어: This line is noise. (구어), This line carries no information. (문어), You can ignore this line. (평이)
- 반의어: This line tells you everything. (이 줄이 핵심이다)

## "The charts follow the chips."
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt (FDC fab 전체 모델 필터)
- 맥락: 한 UI 요소를 바꾸면 다른 요소가 따라 바뀐다는 연동을 짧게 설명할 때(변경 요약).
- 한국어: 차트가 칩(선택)을 따라간다.
- 설명: `follow` 가 "~에 따라 바뀌다, 연동되다"로 쓰였다. `are synchronized with` 보다 훨씬 짧고 생생하다. 원문은 굵은 소제목으로 쓰고 "모델을 바꾸면 다시 불러오지 않고 바로 갱신된다"를 덧붙였다. 바로 앞의 원인 설명 `Nothing connected them to the Fab 전체 charts.` 와 짝을 이룬다.
- 예문: The charts follow the chips: switching models updates them right away, with no refetch.
- 유사어: X tracks Y (기술, 조금 격식), X reacts to Y (평이), X is driven by Y (기술 문서체)
- 반의어: X ignores Y (연동되지 않다)

## "It isn't interfering with our work."
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (Orca 스킬·훅 점검)
- 맥락: 무언가가 방해하느냐는 질문에 아니라고 답할 때(점검 결과 보고, 중립).
- 한국어: 우리 작업을 방해하고 있지 않다.
- 설명: `interfere with` 는 "간섭하다, 방해하다"로 `interrupt`(흐름을 끊다)보다 넓다. 사용자가 `Is that skill inturrupt our work?` 라고 물은 데 대한 답이라 비교해 두면 좋다. 무언가가 계속 옆에서 영향을 주는지 물을 때는 `interfere with` 가 맞다.
- 예문: No, the Orca hooks aren't interfering with our work; outside Orca they exit right away.
- 유사어: get in the way of (구어), affect (평이, 중립), disrupt (격식, 더 강함)
- 반의어: stay out of the way (방해하지 않고 비켜 있다)

## "the lasting fix"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (Orca 스킬·훅 점검)
- 맥락: 임시 조치와 근본 해결을 구분해 "오래가는 해결책은 이것"이라고 짚을 때(조언, 중립).
- 한국어: 오래가는 해결책, 근본 해결
- 설명: `lasting` 은 "지속되는". 원문은 훅 13개를 지울 수는 있지만 Orca 앱을 켜면 다시 추가되니 앱 삭제가 `the lasting fix` 라고 했다. `permanent` 보다 부드럽고 "다시 되돌아오지 않는"이라는 느낌이 있다.
- 예문: While Orca.app is still installed, it will add the hooks back, so uninstalling the app is the lasting fix.
- 유사어: the permanent fix (평이), the root-cause fix (기술), a proper fix (구어)
- 반의어: a stopgap (임시방편), a band-aid (땜질)

## "Read aloud, …"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (영상 카드 문구 조사 선택)
- 맥락: 글자로 볼 때와 소리 내어 읽을 때가 다르다는 점을 짚을 때(문구 검토, 격식 중간).
- 한국어: 소리 내어 읽으면, …
- 설명: 분사구문이다. `When it is read aloud` 에서 접속사와 주어·be 동사를 줄였다. 문두 분사구의 의미상 주어가 주절 주어("디에프티")와 같아야 한다. 원문은 DFT 뒤 조사를 "가"로 할지 "이"로 할지를 이 구로 풀었다.
- 예문: Read aloud, "디에프티" ends in a vowel, so "가" is correct.
- 유사어: When spoken, … (조금 격식), Out loud, … (구어), Pronounced, … (문어)
- 반의어: On paper, … (글자로 보면)

## "as many times as you like"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (영상 원본 보존 확인)
- 맥락: 반복해도 손해가 없으니 마음껏 다시 해도 된다고 안심시킬 때(구어, 안내).
- 한국어: 원하는 만큼 몇 번이든
- 설명: `as many … as` 원급 비교 구조로 "원하는 만큼 많이". 원문은 스크립트가 원본을 읽기만 하고 매번 새 파일을 쓰니 자막·순서를 고쳐 몇 번이든 다시 돌려도 된다고 답했다. 뒤에 "반복 편집해도 화질이 떨어지지 않는다"가 이어져 안심의 근거가 된다.
- 예문: You can edit the captions or order and re-run as many times as you like.
- 유사어: as often as you want (구어), freely (짧게), without limit (조금 격식)
- 반의어: only once (한 번만)

## "I took this to mean …"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (semiauto 스크립트 생성)
- 맥락: 모호한 요청을 어떻게 해석했는지 밝히고 다르면 고치겠다고 할 때(업무 소통, 중립).
- 한국어: 이것을 …라는 뜻으로 받아들였다
- 설명: `take A to mean B` 는 "A 를 B 라는 뜻으로 해석하다". 과거형이라 "이미 이렇게 가정하고 진행했다"는 보고가 된다. 원문은 "Semi-auto" 를 "수동 시작 + 자동 접속"으로 해석했다고 밝힌 뒤, 코드베이스식 반자동(OK 는 엔지니어가 누름)이라면 `OK_CLICK=0` 으로 바꾸겠다고 대안을 붙였다.
- 예문: I took "semi-auto" to mean a manual trigger with an automatic connection.
- 유사어: I read this as … (구어), I interpreted this as … (격식), My assumption was … (평이)
- 반의어: I wasn't sure what you meant by … (해석을 확정하지 못했다)

## "the one to watch"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator (NCC 예외 규칙 검토)
- 맥락: 여러 항목 중 앞으로 특히 지켜봐야 할 하나를 가리킬 때(위험 목록·리뷰).
- 한국어: 지켜봐야 할 것
- 설명: `the one` 이 앞의 명사(row)를 받는다. to부정사가 형용사처럼 뒤에서 꾸며 "지켜볼 대상"이 된다. 스포츠·주식에서 "주목할 선수·종목"을 말할 때도 쓰는 친숙한 표현이다.
- 예문: That's why the periodic-wrong-neighbour row is the one to watch.
- 유사어: the one to keep an eye on (구어), the key risk (보고서체), the case that matters most (평이)
- 반의어: the one you can ignore (무시해도 되는 것)

## "a flat ridge rather than a peak"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator (office 판정 결과 해석)
- 맥락: 점수 곡면 모양을 지형에 빗대 매칭이 왜 애매해지는지 설명할 때(기술 설명).
- 한국어: 봉우리가 아니라 평평한 능선
- 설명: `ridge` 는 "능선", `peak` 는 "봉우리". 긴 수평선은 수평으로 어디에 놓아도 가장자리가 맞아서 chamfer 점수가 한 점에서 솟지 않고 길게 이어진다. `rather than` 이 `not` 보다 부드럽게 대비를 준다.
- 예문: A long horizontal line lines up at every horizontal offset, so the score surface forms a flat ridge rather than a peak.
- 유사어: a plateau (고원, 수치가 멈춘 구간), a broad maximum (수학적 표현)
- 반의어: a sharp peak (뾰족한 봉우리)
