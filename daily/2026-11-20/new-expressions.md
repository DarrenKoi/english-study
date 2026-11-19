# 2026-11-20 — 새 표현

오늘 배치는 대화 네 건인데 둘은 `/clear` 뿐이라 실제 내용은 두 건입니다. auto_recipe_creator 에서는 Radmin·VNC·RFB 구조를 물었고, pm-notes 에서는 pptx 템플릿을 md 로 정리했습니다. 대화 본문은 한국어라서 영어는 세션에 함께 실린 auto_recipe_creator 의 `CLAUDE.md` 와 하네스 안내문에서 골랐습니다. `CLAUDE.md` 는 "A, not B" 로 경계를 긋는 문장이 유난히 많습니다. 어디서 실패하는지, 누가 결정권을 쥐는지, 무엇이 보장하는지를 한 줄로 못박는 방식을 눈여겨보세요.

## "cannot see or drive the actual RCS application"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Development Workflow")
- 맥락: 도구나 에이전트가 어떤 환경에서 무엇을 못 하는지 한계를 밝힐 때(개발 문서, 중립 격식)
- 한국어: 실제 RCS 애플리케이션을 볼 수도, 조작할 수도 없다.
- 설명: `drive` 가 "운전하다"에서 넓어져 프로그램·GUI 를 "조작하다, 구동하다"로 쓰입니다. 브라우저 자동화에서 `drive a browser` 라고 하는 것과 같은 용법입니다. `see or drive` 로 관찰과 조작을 한 쌍으로 묶은 점도 좋습니다.
- 예문: On the build server, the test runner cannot see or drive the actual desktop app, so UI tests are skipped there.
- 유사어: control (가장 평이), operate (기계·장비에 격식 있게), interact with (보기와 조작을 뭉뚱그림)

## "debugging relies on the user reporting console output"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Development Workflow")
- 맥락: 작업이 누구의 어떤 행동에 달려 있는지 설명할 때(절차 문서·보고, 격식)
- 한국어: 디버깅은 사용자가 콘솔 출력을 알려 주는 것에 기댄다.
- 설명: `rely on + 명사 + -ing` 구조입니다. `the user` 가 동명사 `reporting` 의 의미상 주어라서 "사용자가 보고하는 것"이 됩니다. 격식을 더 올리면 `the user's reporting` 이지만 실무 문서에서는 소유격 없이 쓰는 쪽이 흔합니다.
- 예문: Our release process relies on each team updating the changelog before the freeze.
- 유사어: depends on (가장 중립), hinges on (그것 하나에 전부 달렸다는 어감), counts on (사람을 믿고 맡긴다는 구어)

## "git history is the restore path"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Flask Proxy VLM Architecture")
- 맥락: 지운 것을 되살리는 방법이 무엇인지 한 줄로 못박을 때(설계 메모·운영 문서)
- 한국어: 복구 경로는 git 이력이다.
- 설명: `the + 명사 + path` 로 "~하는 길"을 이름 붙이는 조어입니다(`upgrade path`, `rollback path`, `happy path`). 백업 파일을 따로 두지 않았다는 사실까지 이 한 문장이 말해 줍니다.
- 예문: We deleted the old migration scripts, and git history is the restore path if we ever need them again.
- 유사어: you can recover it from git history (풀어 쓴 회화체), the fallback is git history (대비책이라는 어감)

## "fails at slug resolution … not at the proxy"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Flask Proxy VLM Architecture")
- 맥락: 오류가 흐름의 어느 단계에서 나는지 짚을 때(디버깅 설명·장애 보고)
- 한국어: 프록시가 아니라 slug 를 찾는 단계에서 실패한다.
- 설명: `fail at + 단계` 로 실패 지점을 찍고 `not at B` 로 흔한 오해를 막습니다. `resolution` 은 이름을 실제 대상으로 "풀어 찾는" 일입니다(`DNS resolution`, `name resolution`).
- 예문: The request fails at token validation, not at the database, so check the auth header first.
- 유사어: breaks at (구어), errors out during (과정 중이라는 어감), is rejected at (거부라는 뜻이 분명할 때)
- 반의어: gets past, makes it through

## "Never let a VLM answer override a low CV score"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "align-key engine" 설계 규칙)
- 맥락: 두 판단 근거 중 어느 쪽이 우선인지 규칙으로 적을 때(설계 원칙, 단호한 문어)
- 한국어: 낮은 CV 점수를 VLM 답이 뒤집게 두지 마라.
- 설명: `let A override B` = A 가 B 를 누르고 이기게 두다. `Never let …` 은 금지 중에서도 "그런 일이 생기도록 방치하지 마라"는 뜻이라, 코드 한 줄이 아니라 설계 전체에 거는 규칙에 어울립니다.
- 예문: Never let a manager's hunch override a failing test.
- 유사어: take precedence over (격식, 우선순위 표현), overrule (사람·기관의 결정을 뒤집을 때), trump (구어, 카드 게임에서 온 말)
- 반의어: defer to, yield to

## "ECC dominates SEM so mixing dilutes it"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `matching/mind_rerank.py`)
- 맥락: 좋은 신호에 다른 신호를 섞으면 오히려 나빠진다고 설명할 때(실험 결과 해석)
- 한국어: SEM 에서는 ECC 가 압도적이라 섞으면 희석된다.
- 설명: `dominate` 는 "지배하다"보다 "그 영역에서 가장 큰 몫을 차지한다"에 가깝고, `dilute` 는 물을 타서 묽게 한다는 뜻에서 효과·신호를 약하게 만든다는 뜻으로 넓어졌습니다. 둘을 `so` 로 이어 원인과 결과를 일곱 단어에 담았습니다.
- 예문: The first feature dominates the ranking, so adding weaker signals only dilutes it.
- 유사어: waters down (구어), weakens (평이), washes out (신호가 묻혀 사라진다는 어감)
- 반의어: sharpens, reinforces

## "deleting it just falls back to `config.py` defaults"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Local config")
- 맥락: 선택 파일이 없어도 안전하다고 안심시킬 때(설정 문서)
- 한국어: 지워도 `config.py` 기본값으로 돌아갈 뿐이다.
- 설명: `fall back to X` 는 의도한 대비책으로 물러난다는 뜻입니다. `just` 가 "그것 말고 다른 일은 없다"를 더합니다. 동명사 `deleting it` 을 주어로 세워서 "지우는 행위의 결과"를 바로 말했습니다.
- 예문: If the cache is unavailable, the service just falls back to reading from disk.
- 유사어: reverts to (원래 상태로 되돌아감), defaults to (기본값을 쓴다), drops back to (구어)

## "real env still wins"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Bench config")
- 맥락: 설정 값이 여러 곳에서 올 때 어느 쪽이 이기는지 말로 설명할 때(구어, 문서의 괄호 주석)
- 한국어: 그래도 실제 환경 변수가 우선한다.
- 설명: 우선순위를 `win` 한 단어로 말하는 개발자 구어입니다. CSS 의 `the last rule wins` 와 같은 용법이에요. `still` 은 "방금 말한 장치가 있어도"를 뜻합니다. 같은 문서의 격식 버전은 `Precedence: real shell env > …` 입니다.
- 예문: You can set a default in the file, but the command-line flag still wins.
- 유사어: takes precedence (격식), takes priority (중립), overrides the rest (동작을 직접 말함)
- 반의어: loses out, is ignored

## "the two VLMs are not independent votes"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `rcs/`)
- 맥락: 검증이 두 번이라도 서로 독립이 아니면 신뢰도가 안 오른다고 지적할 때(설계 근거·리뷰)
- 한국어: 두 VLM 은 서로 독립된 표가 아니다.
- 설명: 판정을 `vote` 에 빗댄 표현입니다. 뒤 단계가 앞 단계가 고른 crop 만 보기 때문에 둘이 같은 실수를 공유한다는 뜻이고, 그래서 OCR 확인 게이트를 따로 둔다는 근거로 이어집니다. 리뷰어가 둘인데 한 명이 다른 한 명의 요약만 읽었다면 같은 말을 쓰면 됩니다.
- 예문: The two reviewers are not independent votes, because the second one only read the first one's summary.
- 유사어: don't count as separate checks (평이), are correlated (통계 용어), aren't a real second opinion (구어)
- 반의어: independent confirmation

## "lowering only the ratio is a no-op because the two floors dominate"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `rcs/`)
- 맥락: 설정 하나만 바꿔서는 아무 효과가 없다고 경고할 때(튜닝 안내)
- 한국어: 비율만 낮추면 하한 둘이 지배해서 아무 일도 일어나지 않는다.
- 설명: `no-op` (no operation)은 실행해도 결과가 달라지지 않는 것을 가리킵니다. `floor` 는 최솟값(하한)이고 짝은 `ceiling`/`cap` 입니다. 부사 `only` 가 `the ratio` 바로 앞에 놓여 "셋 중 그것만"을 정확히 한정합니다.
- 예문: Raising the timeout alone is a no-op because the retry limit kicks in first.
- 유사어: has no effect (평이), does nothing (구어), is moot (따져 봐야 소용없다는 어감)

## "cleanup … is guaranteed by `try/finally`, not steps"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Running Modules" 끝)
- 맥락: 어떤 성질을 무엇이 보장하는지 책임 소재를 밝힐 때(아키텍처 설명)
- 한국어: 정리 작업은 step 이 아니라 `try/finally` 가 보장한다.
- 설명: 수동태 `is guaranteed by` 로 보장되는 대상(cleanup)을 주어에 두고, 보장하는 주체를 뒤에서 `A, not B` 로 가릅니다. step 목록에 정리 단계를 넣지 말라는 지시가 사실 서술 안에 들어 있습니다.
- 예문: Ordering is guaranteed by the queue, not by the consumers.
- 유사어: is enforced by (규칙을 강제함), is handled by (가볍게), is ensured by (격식)

## "is a library, not an entry point"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Running Modules" 끝)
- 맥락: 파일이나 모듈의 성격을 한마디로 규정해 오해를 막을 때(코드 문서)
- 한국어: 라이브러리이지 실행 진입점이 아니다.
- 설명: `entry point` 는 프로그램 실행이 시작되는 지점입니다. `X is A, not B` 는 이 문서가 가장 자주 쓰는 틀이고, 읽는 사람이 하기 쉬운 오해(직접 실행하려 드는 것)를 먼저 지웁니다.
- 예문: This module is a library, not an entry point, so import it instead of running it directly.
- 유사어: isn't meant to be run directly (풀어 쓴 회화체), is not a standalone script (같은 뜻의 다른 각도)

## "so cost scales with generations, not frames"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `recording_filter/`)
- 맥락: 비용이 무엇에 비례해 늘어나는지 설명할 때(성능 설계 근거)
- 한국어: 그래서 비용은 프레임 수가 아니라 세대 수에 비례한다.
- 설명: `scale with X` = X 가 늘면 같이 늘어난다. 관사 없는 `cost` 를 주어로 삼아 일반 원리처럼 말했습니다. 프레임마다 VLM 을 부르지 않는다는 설계 선택을 숫자 없이 설득합니다.
- 예문: We cache per user, so memory scales with active users, not with requests.
- 유사어: grows with (평이), is proportional to (수학적으로 엄밀), depends on the number of (풀어 쓴 꼴)
- 반의어: stays flat, is constant regardless of

## "Ships notify-only behind a double gate"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `poc/workflow_3e/`)
- 맥락: 위험한 기능을 일단 꺼 둔 채 내보낸다고 알릴 때(릴리스 노트·설계 요약)
- 한국어: 이중 게이트 뒤에 두고 알림만 보내는 상태로 출시한다.
- 설명: 주어를 뺀 메모체입니다(`It ships …`). `ship + 형용사` 는 "어떤 상태로 나간다"는 뜻이고(`ships disabled`, `ships off by default`), `behind a gate/flag` 는 조건을 열어야 동작한다는 말입니다. `X-only` 로 형용사를 만드는 조어도 같이 익혀 두세요.
- 예문: The auto-delete feature ships read-only behind a feature flag until we finish the audit.
- 유사어: is released in dry-run mode (풀어 쓴 꼴), is gated behind two flags (게이트 쪽을 강조), goes out disabled by default (구어)

## "a missing adapter just disables that integration with a warning"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "filesystem contract")
- 맥락: 구성 요소가 없을 때 시스템이 죽지 않고 어떻게 물러나는지 설명할 때(운영 문서)
- 한국어: adapter 가 없으면 경고를 내고 그 연동만 꺼진다.
- 설명: 한국어라면 "없으면 ~된다"로 조건절을 쓸 자리에 영어는 `a missing adapter` 라는 명사구를 주어로 세웁니다. 무생물 주어 + 타동사 구조라 문장이 짧아집니다. `with a warning` 은 "조용히 꺼지지는 않는다"는 정보입니다.
- 예문: A missing API key just disables the export feature with a warning instead of stopping the whole app.
- 유사어: if the adapter is absent, the integration is skipped (조건절로 푼 격식체), degrades gracefully (전체 태도를 이르는 용어)
- 반의어: crashes at startup, fails hard

## "the look-alike that drives the ambiguity"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `diagnostics/feasibility_check.py`)
- 맥락: 혼동의 원인이 되는 닮은 후보를 가리킬 때(분석 보고·리뷰)
- 한국어: 모호함을 일으키는 닮은꼴.
- 설명: `look-alike` 는 "닮은 것"이라는 명사이고, `drive` 는 여기서 "~의 주된 원인이 되다"입니다(`what drives the cost`). 같은 문서에서 `drive the RCS application` 은 "조작하다"였으니 한 단어의 두 용법을 나란히 익힐 기회입니다.
- 예문: The second-best match is the look-alike that drives the ambiguity, so we draw it on the debug image.
- 유사어: the near-duplicate behind the confusion (평이), the decoy (속이는 가짜라는 어감), the main source of ambiguity (원인만 말할 때)

## "to cut payload size without hurting accuracy"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Code Conventions")
- 맥락: 한쪽을 줄이되 다른 쪽은 해치지 않는다는 절충을 밝힐 때(규칙의 근거, 설계 문서)
- 한국어: 정확도를 해치지 않으면서 전송 크기를 줄이려고.
- 설명: `A without hurting B` 는 최적화의 조건을 붙이는 틀입니다. `cut` 은 `reduce` 보다 짧고 과감하며, `hurt` 는 사람이 아닌 지표에도 씁니다(`hurt performance`, `hurt readability`).
- 예문: We compress the screenshots to cut upload time without hurting OCR accuracy.
- 유사어: reduce … without compromising … (격식), shrink … at no cost to … (비용 관점), trim … while preserving … (긍정문으로 뒤집은 꼴)

## "Lead with the result"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (하네스 concise 출력 스타일 안내)
- 맥락: 보고나 답변을 결론부터 시작하라고 조언할 때(글쓰기 지침, 동료 피드백)
- 한국어: 결과부터 말하라.
- 설명: `lead with X` = X 를 맨 앞에 내세우다. 신문 기사 첫 문장을 `lead` 라고 부르는 데서 왔습니다. 같은 안내문의 짝 문장이 `Cut narration, keep substance` 인데, 쉼표 하나로 명령문 둘을 대비시켰습니다.
- 예문: When you write the incident summary, lead with the result and put the timeline below it.
- 유사어: start with the conclusion (평이), put the bottom line up front (군대식 약어 BLUF 로도 씀), open with (글·발표의 첫머리)
- 반의어: bury the lede, save it for the end

## "The choice is yours"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes/5ab92045 (하네스 도구 안내)
- 맥락: 선택지를 설명한 뒤 결정을 상대에게 넘길 때(구어·글 모두, 가벼운 격식)
- 한국어: 고르는 건 네 몫이다.
- 설명: 원문은 `The choice is yours: prefer Edit or Write when a shell edit would be fragile` 입니다. 맡긴다고 말해 놓고 콜론 뒤에 권장 기준을 붙이는 흐름이 실전에서 유용합니다. 재량을 주되 판단 기준은 준다는 형식이에요.
- 예문: We can ship today or wait for the fix; the choice is yours, but I'd wait.
- 유사어: It's up to you (가장 흔한 구어), It's your call (결정권을 강조하는 구어), at your discretion (격식 문어)
