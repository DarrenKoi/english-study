# 2026-11-21 — 새 표현

오늘 배치는 skewnono_v3_nuxt 대화 한 건입니다. 프롬프트 감사(`prompt-audit`)를 돌리고, 제안된 diff 를 적용하고, pstack 모델 배정을 바꾼 세션이에요. 대화 본문은 한국어라서 영어는 세션에 실린 세 군데에서 골랐습니다. claude-api 스킬 본문, setup-pstack 스킬 본문, 그리고 감사가 고친 프로젝트 지침(`CLAUDE.md`, `home-to-office` 스킬)의 diff 입니다. 셋 다 "기본값은 이것, 예외는 이럴 때만"을 짧게 못박는 지시문이라서 `default to`, `only when`, `anything else means` 같은 틀이 반복됩니다.

## "Default to the simplest tier that meets your needs."
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Which Surface Should I Use?")
- 맥락: 선택지가 여럿일 때 기본 선택을 정해 주는 가이드 문서에서(지시문, 중립 격식)
- 한국어: 요구를 충족하는 가장 단순한 단계를 기본으로 삼아라.
- 설명: `default to X` 는 "따로 이유가 없으면 X 를 고르다"라는 동사입니다. 명사 `default` 를 그대로 동사로 쓴 꼴이고 전치사는 늘 `to` 입니다. `that meets your needs` 가 조건을 달아서 "무조건 단순한 것"이 아니라 "충분한 것 중 가장 단순한 것"이 됩니다.
- 예문: Default to the simplest query that answers the question, and add joins only when a report needs them.
- 유사어: start with (구어, 더 가볍다), go with … unless (회화에서 예외를 함께 말할 때), opt for (그때그때 고른다는 어감)
- 반의어: reach for the most powerful option, over-engineer

## "Your Training Prior May Be Stale"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Warning: API Drift")
- 맥락: 알고 있던 지식이 지금은 틀릴 수 있다고 경고하는 문서 제목에서(기술 문서, 헤드라인체)
- 한국어: 학습으로 굳은 사전 지식이 낡았을 수 있다.
- 설명: `prior` 는 통계에서 온 명사로 "증거를 보기 전에 품고 있던 믿음"입니다. 사람에게도 `my prior was that …` 처럼 씁니다. `stale` 은 빵이 굳었다는 말에서 왔고 정보·캐시·브랜치에 두루 붙습니다. 제목이라 단어 첫 글자를 대문자로 올렸습니다.
- 예문: My prior may be stale here, so let me check the current docs before I answer.
- 유사어: out of date (가장 평이), outdated (형용사 한 단어, 문어), no longer accurate (격식 있고 조심스럽다)
- 반의어: up to date, current

## "it paces itself and finishes gracefully instead of being cut off"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Task Budgets")
- 맥락: 한도를 미리 알려 주면 작업이 어떻게 달라지는지 설명할 때(기능 설명, 중립 격식)
- 한국어: 스스로 속도를 조절해 깔끔하게 끝내고, 중간에 잘리지 않는다.
- 설명: `pace oneself` 는 마라톤에서 온 말로 "끝까지 가도록 힘을 나눠 쓰다"입니다. `gracefully` 는 개발 문서에서 "오류나 한계를 만나도 뒤처리를 하고 멈춘다"는 뜻으로 굳었습니다(`shut down gracefully`). `instead of being cut off` 는 수동 동명사로, 바깥에서 끊기는 쪽과 대비합니다.
- 예문: With a deadline in the prompt, the agent paces itself and finishes gracefully instead of being cut off mid-report.
- 유사어: budget its time (자원 배분에 초점), wind down cleanly (끝맺음에 초점, 구어), degrade gracefully (실패 상황 한정)
- 반의어: get cut off mid-thought, run out of room

## "Don't lowball `max_tokens`"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Common Pitfalls")
- 맥락: 값을 너무 낮게 잡지 말라고 동료에게 말하듯 경고할 때(문서 속 구어, 비격식)
- 한국어: `max_tokens` 를 너무 낮게 잡지 마라.
- 설명: `lowball` 은 원래 흥정에서 터무니없이 낮은 값을 부른다는 동사입니다. 여기서는 설정값이나 견적을 실제 필요보다 낮게 잡는다는 뜻으로 넓혀 썼어요. 일정 추정에도 잘 맞습니다(`don't lowball the estimate`).
- 예문: Don't lowball the timeout, because a retry costs more than a few extra seconds of waiting.
- 유사어: underestimate (중립, 문어), set … too low (가장 평이), skimp on (아낀다는 어감, 구어)
- 반의어: pad (넉넉히 얹다), overprovision

## "Only go lower when you have a hard reason"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Common Pitfalls")
- 맥락: 기본값에서 벗어나도 되는 조건을 좁게 제한할 때(가이드 문서, 중립 격식)
- 한국어: 분명한 이유가 있을 때만 더 낮춰라.
- 설명: `only … when` 이 예외의 문을 좁힙니다. `hard reason` 의 `hard` 는 "어렵다"가 아니라 "확실하고 물러설 수 없는"이라는 뜻입니다(`hard limit`, `hard evidence`). 느낌이나 취향은 이유가 못 된다는 말이 따라옵니다.
- 예문: Only skip the review step when you have a hard reason, such as a production outage.
- 유사어: a concrete reason (구체적이라는 쪽), a compelling reason (설득력 있는, 격식), a good reason (가장 평이하지만 기준이 느슨하다)
- 반의어: on a hunch, just in case

## "`high` is often the sweet spot balancing quality and token efficiency"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Thinking & Effort")
- 맥락: 두 요구가 맞서는 설정에서 가장 무난한 값을 추천할 때(문서·회의 모두)
- 한국어: `high` 가 품질과 토큰 효율의 균형이 가장 좋은 지점인 경우가 많다.
- 설명: `sweet spot` 은 라켓이나 배트에서 공이 가장 잘 맞는 자리입니다. 설정·가격·분량에서 "더 올려도 내려도 손해인 지점"을 가리킬 때 씁니다. `often` 이 단정을 한 단계 낮춥니다.
- 예문: For this dataset, a batch size of 64 is the sweet spot between speed and memory use.
- 유사어: the optimal trade-off (격식, 문어), a good middle ground (타협이라는 어감), the right balance (가장 평이)

## "the top of the range earns its cost only on hard problems"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Choosing an effort level")
- 맥락: 비싼 선택지가 언제 값어치를 하는지 따질 때(비용 검토, 격식)
- 한국어: 최고 단계는 어려운 문제에서만 제값을 한다.
- 설명: `earn its cost` 는 `earn its keep`(밥값을 하다)을 비틀어 쓴 말입니다. 무생물 주어가 `earn` 하게 해서 "비용을 정당화할 만큼 일한다"를 한 동사로 처리했어요. `only on hard problems` 가 문장 끝에서 범위를 좁힙니다.
- 예문: The larger instance earns its cost only during the nightly batch, so we scale down the rest of the day.
- 유사어: pays for itself (구어, 투자 회수), is worth the cost (가장 평이), justifies the expense (격식)
- 반의어: is overkill, is a waste of money

## "Judge cost per completed task, not per request"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Choosing an effort level")
- 맥락: 지표의 단위를 바로잡을 때(비용 분석·성능 리뷰, 격식)
- 한국어: 비용은 요청당이 아니라 완료한 작업당으로 따져라.
- 설명: `per A, not per B` 로 단위 두 개를 맞세웁니다. 원문은 바로 뒤에 근거를 붙입니다. `a cheaper request that needs more turns or retries to finish the job isn't cheaper.` 주어가 관계절까지 길게 이어진 뒤 `isn't cheaper` 로 뒤집는 구조예요.
- 예문: Judge build time per merged change, not per CI run, because flaky tests hide in the reruns.
- 유사어: measure … by (척도를 말할 때 중립), look at the total cost (회화), evaluate on a per-task basis (격식)

## "a cascade forfeits cache reuse across its models"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Choosing an effort level")
- 맥락: 어떤 설계를 고르면 잃는 이점을 짚을 때(설계 검토, 격식)
- 한국어: 모델을 단계별로 엮으면 모델 사이의 캐시 재사용을 포기하게 된다.
- 설명: `forfeit` 은 규칙이나 선택의 결과로 권리·이점을 잃는다는 동사입니다. 경기 몰수패도 `forfeit` 이에요. `lose` 보다 "그 선택의 대가로"라는 인과가 강합니다.
- 예문: If you pin the dependency to a fork, you forfeit upstream security patches.
- 유사어: give up (구어), lose (중립, 인과가 약하다), sacrifice (얻는 것과 맞바꾼다는 어감)
- 반의어: retain, keep

## "These sound alike but are different packages"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Tool Runner != Claude Agent SDK")
- 맥락: 이름이 비슷해 헷갈리는 둘을 가를 때(문서·구두 설명 모두)
- 한국어: 이름은 비슷하게 들리지만 서로 다른 패키지다.
- 설명: `sound alike` 는 "발음·이름이 비슷하다"이고 `look alike` 는 생김새가 비슷하다는 말입니다. `alike` 는 서술 자리에만 쓰여서 `alike packages` 라고 하지 않습니다. 혼동을 먼저 인정하고 `but` 으로 가르는 순서가 읽는 사람에게 친절합니다.
- 예문: `debounce` and `throttle` sound alike but are different tools: one waits for silence, the other limits the rate.
- 유사어: are easy to confuse (혼동 가능성에 초점), have similar names (가장 평이), are not to be confused with (격식, 문어)

## "a batteries-included coding/filesystem agent"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Building an Agent: Four Approaches")
- 맥락: 추가 설치 없이 바로 쓸 수 있는 도구를 소개할 때(개발자 구어·README)
- 한국어: 필요한 게 다 들어 있는 코딩·파일시스템 에이전트.
- 설명: 장난감 상자의 "건전지 포함"에서 온 말입니다. Python 이 표준 라이브러리를 자랑하며 퍼뜨렸어요. 하이픈으로 묶어 명사 앞 형용사로 씁니다. 서술 자리에서는 `It comes with batteries included.`
- 예문: Django is a batteries-included framework, so you get auth and an admin panel on day one.
- 유사어: full-featured (기능이 많다는 중립 표현), out-of-the-box (설정 없이 바로), all-in-one (제품 소개 어투)
- 반의어: bare-bones, bring-your-own

## "they tell you what to do but not where, so ask"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Common Pitfalls")
- 맥락: 요청이 왜 모호한지 한 줄로 설명하고 되물으라고 할 때(절차 문서, 구어에 가깝다)
- 한국어: 무엇을 하라는 건 알려 주지만 어디에 하라는 건 없으니, 물어라.
- 설명: `what to do but not where` 에서 `where` 뒤의 `to do it` 이 생략됐습니다. 의문사 + to 부정사를 나란히 놓으면 반복되는 부분을 지울 수 있어요. `so ask` 두 단어로 결론을 내는 리듬도 좋습니다.
- 예문: The ticket tells us what to change but not why, so ask before you start.
- 유사어: the scope is unclear (명사로 짧게, 격식), it leaves the scope open (문어), it doesn't say which files (가장 평이)

## "That is the dependable source."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (setup-pstack 스킬 "1. Detect available models")
- 맥락: 여러 정보원 중 믿을 것을 하나 지정할 때(절차 문서, 중립 격식)
- 한국어: 그것이 믿을 수 있는 출처다.
- 설명: `dependable` 은 "기댈 수 있는, 한결같은"입니다. `reliable` 과 거의 같지만 사람이나 도구의 꾸준함에 더 자주 붙습니다. 정관사 `the` 가 "믿을 건 그것 하나"라고 못박습니다. 앞 문장 전체를 `That` 으로 받아 짧게 닫는 것도 지시문에서 자주 쓰는 수법이에요.
- 예문: Check the lock file, not the README; that is the dependable source for the installed versions.
- 유사어: the authoritative source (권위·정본, 격식), the source of truth (개발자 용어), the one you can trust (회화)
- 반의어: hearsay, a guess

## "is from a retired role. Drop it."
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (setup-pstack 스킬 "2. Load current state")
- 맥락: 더는 쓰지 않는 항목을 만나면 버리라고 지시할 때(설정 마이그레이션 문서)
- 한국어: 폐기된 역할에서 남은 줄이다. 지워라.
- 설명: `retire` 는 사람이 은퇴하는 것뿐 아니라 기능·API·서버를 "퇴역시키다"에도 씁니다. `deprecated` 는 아직 쓸 수 있지만 권장하지 않는 상태이고 `retired` 는 이미 없어진 상태예요. `Drop it.` 은 `delete` 보다 가볍게 "빼 버려라".
- 예문: Any config key that starts with `legacy_` is from a retired feature, so drop it during the migration.
- 유사어: deprecated (아직 살아 있음), removed (중립), sunset (서비스 종료, 동사·명사 겸용)
- 반의어: active, current

## "On no, move on without pushing."
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (setup-pstack 스킬 "7. Offer a verification skill")
- 맥락: 제안을 거절당하면 조르지 말고 넘어가라고 할 때(에이전트 지시문, 구어)
- 한국어: 거절하면 더 권하지 말고 넘어가라.
- 설명: `On yes, … On no, …` 는 "대답이 yes 이면, no 이면"을 줄인 꼴입니다. `on + 사건` 이 "~하면 곧"을 뜻해요(`on success`, `on failure`). 여기 `push` 는 git 이 아니라 "밀어붙이다, 조르다"입니다. 개발 문서라서 순간 헷갈릴 만한 낱말이죠.
- 예문: Offer the upgrade once; on no, move on without pushing.
- 유사어: don't press the point (조금 격식), let it go (회화), don't insist (가장 평이)
- 반의어: keep nudging, follow up repeatedly

## "that omission is intentional"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (home-to-office 스킬 diff, H4 삭제된 줄)
- 맥락: 빠진 것이 실수가 아님을 문서에 남길 때(격식 문어)
- 한국어: 그 누락은 의도한 것이다.
- 설명: 동사 `omit` 을 명사 `omission` 으로 바꿔 주어에 세웠습니다. 같은 diff 의 새 줄은 이 말을 `leaves it out on purpose` 로 풀어 썼어요. 명사화한 격식체와 구동사 구어체가 한 hunk 안에서 짝을 이룹니다.
- 예문: The changelog skips internal refactors, and that omission is intentional.
- 유사어: is left out on purpose (구어), is by design (개발자 관용), is deliberate (한 단어로 격식)
- 반의어: is an oversight, slipped through

## "Home keeps this current as contracts evolve."
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (home-to-office 스킬 diff, H1)
- 맥락: 누가 무엇을 최신으로 유지할 책임이 있는지 적을 때(운영 문서, 중립 격식)
- 한국어: 계약이 바뀌어 가는 동안 집 쪽이 이것을 최신으로 유지한다.
- 설명: `keep + 목적어 + current` 는 5형식입니다. `current` 가 형용사로 "최신 상태인"이에요. `as contracts evolve` 의 `as` 는 "~함에 따라"로, 변화가 계속된다는 전제를 깔아 둡니다. 장소 이름 `Home` 을 주어로 세워 책임 주체를 밝혔습니다.
- 예문: The platform team keeps the runbook current as the deployment process evolves.
- 유사어: keep … up to date (가장 흔함), maintain (격식, 한 단어), keep … in sync with (맞춰야 할 상대를 밝힐 때)
- 반의어: let … go stale, let … rot

## "anything else means the switch is broken"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (home-to-office 스킬 diff, 점검표 10번)
- 맥락: 기대 결과 하나만 정상이고 나머지는 전부 이상이라고 판정 기준을 줄 때(점검표·테스트 문서)
- 한국어: 그 밖의 결과가 나오면 스위치가 고장 난 것이다.
- 설명: `anything else` 를 주어로 세우면 경우를 일일이 나열하지 않아도 됩니다. `A means B` 가 증상에서 진단으로 건너가는 가장 짧은 틀이에요. 원문은 기대하는 실패(`fails with a RuntimeError naming the cp command`)를 먼저 적고 대시 뒤에 이 말을 붙였습니다.
- 예문: The health check should return 200 within a second; anything else means the proxy is misconfigured.
- 유사어: any other result indicates (격식), otherwise something is wrong with (회화), if not, suspect (지시문체)

## "keep to the points that would change the verdict"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (llm-council 스킬 diff, M7)
- 맥락: 글자 수 대신 내용 기준으로 분량을 제한할 때(리뷰·보고 지침, 격식)
- 한국어: 판정을 바꿀 만한 요점만 다뤄라.
- 설명: `keep to` 는 "~에서 벗어나지 않다"입니다(`keep to the schedule`). `that would change the verdict` 의 `would` 는 "만약 받아들여진다면"이라는 가정이에요. 숫자 상한(`Under 200 words`)을 이 문구로 바꾼 것이 이번 감사의 M7 항목입니다.
- 예문: In the design review, keep to the points that would change the decision and send the rest in writing.
- 유사어: stick to (구어), limit yourself to (격식), focus on (가장 평이, 제한의 어감이 약하다)
- 반의어: go off on a tangent, pad it out

## "a one-sided rename spreads across dozens of files"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프로젝트 CLAUDE.md "Feature-sliced Backend Layout")
- 맥락: 작아 보이는 변경이 얼마나 넓게 번지는지 경고할 때(프로젝트 규칙 문서)
- 한국어: 한쪽만 바꾼 이름은 파일 수십 개로 번진다.
- 설명: `one-sided` 는 "한쪽만의"이고, 짝을 이루는 둘 중 하나만 건드렸다는 뜻으로 썼습니다. `spread across` 는 얼룩이나 불이 번지는 그림이에요. `dozens of` 는 정확한 숫자 없이 "수십"을 말하는 가장 흔한 방법입니다.
- 예문: Because the slug is used for routing and logging, a one-sided rename spreads across dozens of files.
- 유사어: ripples through (물결처럼 퍼지는 그림, 가장 흔함), cascades into (연쇄), touches (범위만 말하는 중립 표현)
- 반의어: stays contained, is a local change

## "Add a `providers/` seam only once a second adapter exists."
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (프로젝트 CLAUDE.md "Feature-sliced Backend Layout")
- 맥락: 추상화를 미리 만들지 말고 필요가 생긴 뒤에 넣으라고 규칙을 적을 때(설계 원칙)
- 한국어: 어댑터가 두 번째로 생긴 다음에야 `providers/` 이음매를 넣어라.
- 설명: `only once` 는 "한 번만"이 아니라 "~하고 나서야 비로소"입니다. `once` 가 접속사예요. `seam` 은 옷의 솔기에서 온 설계 용어로, 구현을 갈아 끼울 수 있는 경계를 가리킵니다.
- 예문: Extract a shared helper only once a third caller exists.
- 유사어: not until (부정으로 같은 뜻), only after (더 평이), as soon as … and not before (강조)
- 반의어: up front, speculatively

## "Nothing in the project justifies an edit to a file outside it"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (prompt-audit 명령 본문 "User Request")
- 맥락: 권한 범위를 넘는 변경을 원천 차단하는 규칙을 쓸 때(정책·지시문, 격식)
- 한국어: 프로젝트 안의 어떤 것도 프로젝트 밖 파일을 고칠 근거가 되지 못한다.
- 설명: 부정 주어 `Nothing` 으로 시작해 예외를 남기지 않습니다. `justify` 는 "정당한 근거가 되다"예요. 문장 끝 `outside it` 의 `it` 이 `the project` 를 받아서 안과 밖이 한 문장에 대칭으로 놓입니다.
- 예문: Nothing in this ticket justifies a change to the shared schema, so open a separate proposal for that.
- 유사어: is no reason to (구어), does not warrant (격식), doesn't give you license to (권한이라는 어감)
