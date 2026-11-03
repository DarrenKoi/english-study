# 2026-11-04 — 새 표현

## "a special case layered on shared infrastructure"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a3c93e7c (ALTITUDE 리뷰 지시)
- 맥락: 공통 구조를 고치지 않고 그 위에 예외 분기를 얹은 변경을 지적할 때(코드 리뷰·설계 글)
- 한국어: 공통 기반 위에 덧댄 특수 처리
- 설명: `layered on` 은 과거분사가 뒤에서 명사를 꾸미는 꼴로, which is layered on 이 줄었습니다. "덧붙였다"는 행위보다 "겹겹이 얹혀 있다"는 상태를 그려서 구조 문제라는 인상이 강합니다. 원문은 `sits at the right depth` 와 짝을 지어 "제 깊이에 있나, 아니면 위에 얹은 예외인가"를 묻습니다.
- 예문: Check whether the new branch in ToolInventoryView is a special case layered on shared infrastructure.
- 유사어: bolted on (더 구어적, 억지로 붙였다는 비판조), a one-off exception (범위가 좁다는 쪽에 초점), a patch over the abstraction (추상화를 덮었다는 뉘앙스)
- 반의어: built into the shared layer, a general change

## "within the diff's scope"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a3c93e7c
- 맥락: 리뷰 제안을 이번 변경 범위 안으로 묶어 둘 때(리뷰 지시·PR 코멘트)
- 한국어: 이번 diff 가 다루는 범위 안에서
- 설명: 원문은 `Name the more general change only if it is clearly simpler and within the diff's scope.` 입니다. only if 뒤에 조건 두 개를 and 로 묶어 "더 간단하고, 범위 안일 때만" 제안하라고 문을 좁힙니다. 소유격 `the diff's` 로 범위의 주인을 diff 로 정했습니다.
- 예문: Moving the registry is a good idea, but it is not within the diff's scope, so leave it for a follow-up.
- 유사어: in scope for this change (더 평이), part of this PR (회화)
- 반의어: out of scope, scope creep (범위가 슬금슬금 커지는 현상)

## "Name the cheaper alternative concretely."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d (EFFICIENCY 리뷰 지시)
- 맥락: "느리다"는 지적만 하지 말고 대안을 구체적으로 적으라고 요구할 때(리뷰 지시·피드백 가이드)
- 한국어: 더 싼 대안을 구체적으로 짚어라
- 설명: `name` 을 동사로 써서 "이름을 대다 → 콕 집어 말하다"라는 뜻입니다. cheaper 는 돈이 아니라 연산 비용입니다. 부사 concretely 를 문장 끝에 둬서 요구의 무게가 거기 실립니다.
- 예문: If a computed re-runs on every hover, name the cheaper alternative concretely, such as memoizing it by point ID.
- 유사어: spell out the fix (회화), propose a specific alternative (평이한 문어)
- 반의어: hand-wave (얼버무리다)

## "Flag wasted work"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 성능 리뷰에서 무엇을 찾으라는지 한마디로 정할 때(리뷰 지시)
- 한국어: 헛도는 연산을 짚어 내라
- 설명: `flag` 는 "깃발을 꽂다 → 문제로 표시하다". wasted work 는 결과에 기여하지 않는 계산을 통칭합니다. 원문은 콜론 뒤로 예시(같은 계산을 여러 컴포넌트가 반복, O(n²) 스캔 등)를 줄줄이 붙여 이 짧은 명령을 풀어 갑니다.
- 예문: Flag wasted work: the same histogram is binned in three components from the same props.
- 유사어: point out redundant computation (평이), call out needless work (회화)
- 반의어: necessary work, load-bearing computation

## "depend on more than they need"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 반응형 값(computed)이 필요 없는 상태까지 구독해 쓸데없이 다시 돈다고 설명할 때(프론트엔드 리뷰)
- 한국어: 필요한 것보다 많은 것에 의존한다
- 설명: 원문은 `computeds that re-run because they depend on more than they need` 입니다. `more than they need` 뒤에 to depend on 이 생략돼 있습니다. 비교 구문을 의존성 크기에 쓴 깔끔한 예입니다.
- 예문: The heatmap option re-runs on every point click because it depends on more than it needs.
- 유사어: over-subscribed (기술 은어), has too wide a dependency set (문어)
- 반의어: depends only on what it reads

## "created and not released"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 리소스(object URL·리스너·옵저버) 누수를 짧게 지적할 때(코드 리뷰)
- 한국어: 만들어 놓고 해제하지 않은
- 설명: 과거분사 두 개를 and not 으로 묶어 "만들기만 하고 풀지 않음"을 대비시킵니다. 행위자를 빼고 리소스의 처지만 남기는 수동형이라 리뷰 문장이 건조하고 객관적으로 들립니다.
- 예문: Object URLs for the profile images are created and not released when the page unmounts.
- 유사어: leaked (짧고 직접적), never cleaned up (회화)
- 반의어: disposed of, torn down

## "depending on something volatile"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 자주 바뀌는 값에 기대는 바람에 비싼 재계산이 일어난다고 설명할 때(기술 문서)
- 한국어: 자주 바뀌는 무언가에 기대는
- 설명: 원문은 `so a chart option depending on something volatile is a full rebuild` 입니다. 현재분사구 depending on ... 이 명사 option 을 뒤에서 꾸밉니다. volatile 은 "변덕스러운, 자주 바뀌는"이고, `is a full rebuild` 는 "= 전체 재구성이다"라고 결과를 등식으로 못 박는 말투입니다.
- 예문: Keep the selected point out of the option computed; anything depending on something volatile pays for a full rebuild.
- 유사어: tied to fast-changing state (평이), reactive to every change (기술)
- 반의어: depending only on stable inputs

## "say what size makes it matter"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 사소한 최적화를 늘어놓지 말고 "어느 규모부터 문제가 되는지"를 밝히라고 할 때(리뷰 지시)
- 한국어: 어느 크기부터 의미가 생기는지 밝혀라
- 설명: 앞 문장 `Do not report micro-optimisations with no measurable effect at these sizes;` 와 세미콜론으로 이어집니다. `make it matter` 는 사역동사 make + 원형동사로 "그것을 중요하게 만들다". 간접의문문 what size ... 가 say 의 목적어입니다.
- 예문: An O(n²) scan over 17 columns is harmless, so say what size makes it matter before you flag it.
- 유사어: state the threshold where it starts to hurt (문어), tell me when it'd actually bite (회화)
- 반의어: (마땅한 대체 표현 없음)

## "Not hunting for correctness bugs — skip those."
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 리뷰 범위에서 버그 찾기를 빼라고 짧게 선을 그을 때(지시문·구두 요청)
- 한국어: 정확성 버그를 찾는 게 아니다, 그건 건너뛰어라
- 설명: 주어와 be동사(We're / You're)를 떼어 낸 조각문입니다. 지시문에서는 이렇게 줄이면 단호하면서도 가볍게 들립니다. 대시 뒤 명령문이 앞의 사실을 행동으로 바꿉니다.
- 예문: Not hunting for correctness bugs — skip those and stick to wasted renders.
- 유사어: Bugs are out of scope for this pass. (격식), Leave bugs aside. (평이)
- 반의어: Report every bug you find.

## "be judged by X instead of Y"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 71930ffc subagent a3c93e7c
- 맥락: 판정 기준이 바뀌었다고 설명할 때(설계 메모·변경 설명)
- 한국어: Y 대신 X 로 판정된다
- 설명: 원문은 `Provision and VeritySEM ... are now judged by per-family Redis host keys instead of v3_df_sem_avail.` 입니다. 사람이 아니라 장비군을 주어로 한 수동태라 "무엇이 판정 기준인가"에 초점이 갑니다. now 가 변경 시점을 알립니다.
- 예문: Tool availability is now judged by the host keys instead of the old availability table.
- 유사어: be determined by (더 격식), go by (회화: "we go by the host keys now")
- 반의어: (마땅한 대체 표현 없음)

## "Users are on FHD desktops."
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d
- 맥락: 사용자 환경(기기·화면·OS)을 한 줄로 알려 줄 때(지시문·회의)
- 한국어: 사용자는 FHD 데스크톱을 쓴다
- 설명: `be on + 기기/플랫폼` 은 "그걸 쓰고 있다"는 구어 표현입니다(I'm on Windows, She's on the old version). use 보다 짧고 자연스럽습니다.
- 예문: Most of our users are on FHD desktops, so don't optimise for phones.
- 유사어: use (평이), run (OS·버전에), work on (조금 길게)
- 반의어: (마땅한 대체 표현 없음)

## "Start-of-day ritual"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (/back-to-office 스킬 본문)
- 맥락: 하루를 여는 고정 절차를 이름 붙여 부를 때(도구 설명·팀 문화 이야기)
- 한국어: 하루를 여는 의례, 출근 루틴
- 설명: `start-of-day` 처럼 하이픈으로 묶은 구가 명사 앞에서 형용사 역할을 합니다(end-of-day report 도 같은 꼴). ritual 은 routine 보다 "의식처럼 꼭 치르는" 느낌이 있어 도구 소개 첫 줄에 어울립니다.
- 예문: Reading the open-jobs file is my start-of-day ritual before I touch any code.
- 유사어: morning routine (평이), daily kickoff (업무 회화)
- 반의어: end-of-day wrap-up

## "Call out anything whose since date is several days old"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (/back-to-office 스킬 본문)
- 맥락: 오래 묵은 항목을 따로 눈에 띄게 알리라고 할 때(지시문·회의)
- 한국어: since 날짜가 며칠 지난 항목은 따로 짚어라
- 설명: `call out` 은 "공개적으로 지적하다·눈에 띄게 언급하다". `anything whose ...` 는 소유격 관계대명사 whose 가 사물에도 쓰인다는 좋은 예입니다(of which 보다 훨씬 자연스럽습니다).
- 예문: In the standup, call out anything whose deadline has already slipped.
- 유사어: flag (더 짧음), highlight (문어), point out (평이)
- 반의어: gloss over (대충 넘어가다)

## "The carryover tells you where the user stopped; only the user knows where they want to start."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (/back-to-office 스킬 본문)
- 맥락: 기록은 과거를 말할 뿐 다음 결정은 사람이 한다고 선을 그을 때(설계 원칙·지시문)
- 한국어: 이월 기록은 어디서 멈췄는지를 알려 줄 뿐, 어디서 시작할지는 사용자만 안다
- 설명: 세미콜론 앞뒤가 stopped ↔ start, carryover ↔ only the user 로 대구를 이룹니다. `where the user stopped` 는 간접의문문이 tells 의 목적어 자리에 들어간 꼴이고, they 는 성별을 정하지 않는 단수 대명사입니다.
- 예문: The log tells you where the build stopped; only you know where you want to pick up.
- 유사어: The notes show where you left off, not where to go next. (평이), History informs the choice; it does not make it. (격식)
- 반의어: (마땅한 대체 표현 없음)

## "check whether the blocker cleared"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 0028e27e (/back-to-office 스킬 본문)
- 맥락: 막혀 있던 작업을 다시 볼 때 막던 원인이 풀렸는지 먼저 확인하라고 할 때(업무 회화)
- 한국어: 막던 원인이 풀렸는지 확인하다
- 설명: `clear` 를 자동사로 써서 "(장애물·막힘이) 걷히다"라는 뜻입니다. The road cleared, The fog cleared 와 같은 쓰임입니다. whether 절이 check 의 목적어입니다.
- 예문: Before you restart the migration ticket, check whether the blocker cleared overnight.
- 유사어: see if it's unblocked (회화), confirm the dependency is resolved (격식)
- 반의어: still blocked

## "doesn't exist anywhere in the raw data"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md (1차 회신 원문)
- 맥락: 원천 데이터를 다 뒤졌지만 그 필드가 없다고 단정할 때(데이터 회신·회의)
- 한국어: 원본 데이터 어디에도 없다
- 설명: `not ... anywhere` 가 "어디에도 ~없다"는 전면 부정입니다. `isn't in the raw data` 보다 "찾아봤다"는 뉘앙스가 강해 확인 결과를 보고할 때 믿음이 갑니다.
- 예문: The Fab field doesn't exist anywhere in the raw data, so we can't derive it at ETL time.
- 유사어: is nowhere to be found in (조금 문어적·강조), is missing from (평이)
- 반의어: is present throughout

## "the primary extraction method"
- 레지스터: technical, professional
- 출처: transcript:pm_notes 65f7b337 (프로젝트 CLAUDE.md 영어 규칙)
- 맥락: 여러 방법 중 기본으로 쓰는 경로를 밝힐 때(설계 문서·기술 결정)
- 한국어: 주된(기본) 추출 방법
- 설명: 원문은 `99% of company docs are DRM-protected → screenshot + VLM pipeline is the primary extraction method` 입니다. primary 는 "첫째·기본"이라 다른 방법(fallback)이 있다는 전제가 깔립니다. main 보다 문어적입니다.
- 예문: Because most files are DRM-protected, screenshot-plus-VLM is the primary extraction method and text parsing is the fallback.
- 유사어: the default approach (평이), the main path (회화)
- 반의어: the fallback, a secondary method
