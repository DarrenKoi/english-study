# 2026-10-17 — 새 표현

오늘 배치는 문서 없이 대화 6건이었다. 영어는 세 군데서 나왔다. 가장 많은 건 버그 진단 세션에 딸려 온 `diagnosing-bugs` 스킬 문서다. 짧은 명령문과 대구 격언(`One breakpoint beats ten logs.`)이 많아 지침 글의 리듬을 배우기 좋다. 다음은 AFM Recipe 현황 페이지를 만든 에이전트의 영어 보고로, 확인한 것과 못 한 것을 갈라 적는 표현이 모여 있다. 리뷰 하위 에이전트에게 준 지시문에서 한 줄을 더 골랐다. `browser-verify` 스킬 문서는 예전에 다 골라 건너뛰었다.

## "Refuse to give up."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 막힌 일을 끝까지 밀어붙이라고 독려할 때(지침·구어 모두)
- 한국어: 포기하지 마라.
- 설명: 원문은 `Be aggressive. Be creative. Refuse to give up.` 세 단어짜리 명령문을 연달아 놓아 리듬을 만든다. `Don't give up` 보다 `refuse` 가 의지를 더 세게 드러낸다. 포기가 선택지로 다가와도 거절하라는 뉘앙스다.
- 예문: Spend disproportionate effort here: be aggressive, be creative, and refuse to give up.
- 유사어: Don't give up. (가장 평이), Keep at it. (구어, 꾸준히 하라), Leave no stone unturned. (관용구, 샅샅이 뒤져라)
- 반의어: throw in the towel (손들다, 포기하다)

## "a debugging superpower"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 어떤 도구·습관이 디버깅을 압도적으로 쉽게 만든다고 추켜세울 때(구어·블로그체)
- 한국어: 디버깅의 비장의 무기.
- 설명: `superpower` 는 "초능력"이지만 기술 글에서는 "남들보다 확 앞서게 해 주는 능력"이라는 가벼운 과장으로 쓴다. 원문은 앞 문장의 대비(30초짜리 불안정한 루프 vs 2초짜리 결정적 루프) 끝에 대시로 붙여 결론을 한마디로 찍는다.
- 예문: A 2-second deterministic loop is tight — a debugging superpower.
- 유사어: a game changer (더 흔하고 상투적), a secret weapon (남이 모르는 무기라는 뉘앙스)
- 반의어: a liability (짐, 오히려 해가 되는 것)

## "Stop and say so explicitly."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 할 수 없는 상황이면 얼버무리지 말고 멈춰서 분명히 밝히라고 지시할 때(지침·문어)
- 한국어: 멈추고, 그렇다고 분명히 말하라.
- 설명: `say so` 의 `so` 는 앞 내용(루프를 만들 수 없다는 사실)을 받는 대용어다. `say that you can't` 를 다시 쓰지 않아도 된다. `explicitly` 가 붙어 "돌려 말하지 말고"가 된다.
- 예문: If you genuinely cannot build a loop, stop and say so explicitly.
- 유사어: Flag it and stop. (짧은 업무 지시), Be upfront about it. (구어, 숨기지 말라)
- 반의어: quietly work around it (말없이 우회하다)

## "the hypothesis is a vibe"
- 레지스터: casual, conversational
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 근거·예측 없이 "느낌"만 있는 주장을 깎아내릴 때(구어·인터넷체)
- 한국어: 그 가설은 그냥 느낌일 뿐이다.
- 설명: `vibe` 는 원래 분위기·느낌을 뜻하는 구어다. `X is a vibe` 는 요즘 칭찬("분위기 좋다")으로도 쓰지만 여기서는 "검증할 수 없는 감"이라는 비판이다. 격식 있는 글이라면 `speculation` 이나 `a hunch` 로 바꾼다.
- 예문: If you cannot state the prediction, the hypothesis is a vibe — discard or sharpen it.
- 유사어: it's just a hunch (구어, 직감), it's pure speculation (격식, 순전한 추측)
- 반의어: a falsifiable hypothesis (반증 가능한 가설)

## "re-ranks instantly"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 상대가 아는 한 가지 사실이 우선순위를 단번에 뒤집는다고 말할 때(업무·문어)
- 한국어: 순위를 즉시 다시 매긴다.
- 설명: 접두사 `re-` 를 동사에 붙여 "다시 ~하다"를 한 단어로 만든다(`re-rank`, `re-run`, `re-check`). 주어가 사람이 아니라 `domain knowledge` 라서 "지식이 순위를 바꾼다"는 무생물 주어 구문이 된다.
- 예문: The user often has domain knowledge that re-ranks the list instantly.
- 유사어: reshuffles the priorities (구어), reorders the list on the spot (중립)
- 반의어: leaves the ranking untouched (순위를 그대로 둔다)

## "Cheap checkpoint, big time saver."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 잠깐 확인받는 비용은 작고 아끼는 시간은 크다고 권할 때(구어·지침)
- 한국어: 확인 비용은 싸고, 아끼는 시간은 크다.
- 설명: 동사 없이 `형용사+명사, 형용사+명사` 두 덩어리를 대구로 놓은 슬로건형 문장이다. 앞뒤 대비(cheap ↔ big)가 리듬을 만든다. 글 중간에 짧게 끼워 강조할 때 효과가 크다.
- 예문: Show the ranked list to the user before testing — cheap checkpoint, big time saver.
- 유사어: It costs little and saves a lot. (풀어 쓴 평서문), A quick check now saves hours later. (구어)
- 반의어: a costly detour (비싼 우회로)

## "One breakpoint beats ten logs."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 디버거 한 번이 로그 여러 줄보다 낫다고 도구 선택을 권할 때(기술·격언)
- 한국어: 중단점 하나가 로그 열 줄보다 낫다.
- 설명: 노트에 있는 `X beats Y` 틀에 숫자 대비(one ↔ ten)를 더했다. 숫자를 붙이면 "하나로 열 개를 이긴다"는 효율 차이가 바로 보인다. cf. `A picture is worth a thousand words.`
- 예문: Use the debugger if the environment supports it — one breakpoint beats ten logs.
- 유사어: A debugger tells you more than a pile of print statements. (풀어 쓴 문장), Inspect, don't spray logs. (구어 명령)

## "Untagged logs survive; tagged logs die."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 임시 디버그 로그에 꼬리표를 달아야 나중에 확실히 지운다고 설명할 때(기술·격언)
- 한국어: 꼬리표 없는 로그는 살아남고, 꼬리표 단 로그는 지워진다.
- 설명: 세미콜론으로 정반대 두 절을 잇는 대구다. `survive`/`die` 를 로그에 써서 의인화했다. 꼬리표가 없으면 정리할 때 못 찾아 코드에 남는다는 경고를 두 단어 대비로 압축했다.
- 예문: Tag every debug log with a unique prefix: untagged logs survive; tagged logs die.
- 유사어: If you can't grep for it, you won't clean it up. (풀어 쓴 구어), Label your temporary logs so they're easy to remove. (평이)

## "lock down (a bug)"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 회귀 테스트로 버그가 다시 못 나오게 붙잡아 둔다고 말할 때(기술·문어)
- 한국어: (테스트로) 버그를 단단히 묶어 두다, 재발을 막다.
- 설명: `lock down` 은 "봉쇄하다, 단단히 고정하다"다. 버그에 쓰면 "테스트로 그 동작을 고정해 다시 깨지지 않게 한다"가 된다. 원문은 수동 동명사 `from being locked down` 으로 "묶이지 못하게 막는다"를 썼다. 노트의 `a locked-down PC`(제한된 PC)와는 뜻이 다르다.
- 예문: The codebase architecture is preventing the bug from being locked down.
- 유사어: pin down (정확히 잡아 두다, 비슷하지만 원인 파악 쪽에 가깝다), guard against a regression (격식)
- 반의어: let it slip back in (다시 슬그머니 들어오게 두다)

## "so the next debugger learns"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 기록을 남기는 목적을 뒤에 올 사람의 학습으로 밝힐 때(문어·지침)
- 한국어: 다음에 디버깅할 사람이 배울 수 있도록.
- 설명: 목적의 `so (that)` 뒤에 현재형 `learns` 를 썼다. 미래 일이지만 목적절에서는 `will learn` 대신 현재형이 자연스럽다. `the next debugger` 는 사람을 역할명으로 부르는 방식이다(`the next reader`, `the next maintainer`).
- 예문: State the hypothesis that turned out correct in the commit message, so the next debugger learns.
- 유사어: for whoever touches this next (구어), for future maintainers (격식)

## "anchors on the first plausible idea"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 첫 그럴듯한 생각에 사고가 묶이는 편향을 경고할 때(문어·분석)
- 한국어: 처음 떠오른 그럴듯한 생각에 고정된다.
- 설명: `anchor on` 은 심리학의 앵커링 효과에서 온 말이다. 처음 본 값이나 생각에 판단이 닻처럼 걸려 움직이지 않는 현상을 가리킨다. 원문의 주어는 `Single-hypothesis generation`(가설을 하나만 세우기)이다. 사람이 아니라 방법이 고정된다고 쓴 셈이다.
- 예문: Single-hypothesis generation anchors on the first plausible idea.
- 유사어: fixate on (구어에 가깝고 더 강함), get tunnel vision (구어, 시야가 좁아지다)
- 반의어: keep an open mind (열어 두다)

## "hidden coupling"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 겉으로 안 보이는데 실은 서로 얽혀 있는 코드 의존을 지적할 때(기술·설계)
- 한국어: 숨은 결합(눈에 안 띄는 의존 관계).
- 설명: `coupling` 은 모듈 사이 의존의 정도다. `hidden` 이 붙으면 import 나 인자로 드러나지 않고 전역 상태·공유 캐시·암묵적 순서로 엮인 경우를 말한다. `no good test seam`, `tangled callers` 와 함께 나열돼 구조 문제의 대표 증상으로 쓰였다.
- 예문: If the answer involves architectural change, such as hidden coupling, hand it off with the specifics.
- 유사어: implicit dependency (격식, 같은 뜻), spooky action at a distance (구어·비유)
- 반의어: loose coupling (느슨한 결합)

## "if the user is AFK"
- 레지스터: casual, conversational
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 사용자가 자리를 비웠을 때를 가정할 때(채팅·개발자 구어)
- 한국어: 사용자가 자리에 없으면.
- 설명: `AFK` 는 away from keyboard 의 약자다. 게임·채팅에서 온 말인데 개발자 사이에서는 지침 글에도 그대로 쓴다. 공식 문서라면 `unavailable` 이나 `not around` 로 바꾸는 편이 안전하다.
- 예문: Don't block on it — proceed with your ranking if the user is AFK.
- 유사어: if the user isn't around (구어), if the user is unavailable (격식)

## "red-capable"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 그 테스트가 이 버그에서 실제로 실패할 수 있는지를 따질 때(기술·TDD)
- 한국어: 빨간불(실패)을 낼 수 있는.
- 설명: `X-capable` 은 "X 할 능력이 있는"이라는 합성 형용사다(`GPU-capable`, `5G-capable`). TDD 의 red/green 에 붙여 "이 버그를 잡아 실패로 보여 줄 수 있는"을 한 단어로 만들었다. 그냥 돌아가기만 하는 테스트와 갈라 말할 때 쓴다.
- 예문: Phase 1 is done when the loop is tight and red-capable.
- 유사어: able to catch this bug (풀어 쓴 표현), a test that actually fails on it (구어)
- 반의어: a test that always passes (늘 통과하는, 쓸모없는 테스트)

## "run it unattended"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 사람이 지켜보거나 손대지 않아도 혼자 돌아가야 한다고 말할 때(기술·운영)
- 한국어: 사람 없이 돌리다, 무인으로 실행하다.
- 설명: `unattended` 는 "돌보는 사람이 없는"이다. 공항 안내의 `Do not leave bags unattended` 와 같은 단어다. 자동화 맥락에서는 `run unattended` 가 "클릭이나 확인 없이 끝까지 간다"는 요건이 된다.
- 예문: The loop must be agent-runnable: you can run it unattended.
- 유사어: run hands-off (구어), run without supervision (격식)
- 반의어: run it with a human in the loop (사람이 끼어 돌리다)

## "shrink the repro"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서)
- 맥락: 재현 시나리오에서 필요 없는 부분을 하나씩 걷어 낼 때(기술·디버깅)
- 한국어: 재현 사례를 줄이다(최소화하다).
- 설명: `repro` 는 reproduction(재현 사례)의 줄임말로 개발자 구어에서 아주 흔하다. `shrink` 는 "작게 만들다"라 `minimise` 보다 손에 잡히는 느낌이다. 원문은 `shrink the repro to the smallest scenario that still goes red` 처럼 목표 상태를 `to` 로 붙였다.
- 예문: Once it's red, shrink the repro to the smallest scenario that still goes red.
- 유사어: minimise the reproduction (격식), boil it down (구어, 핵심만 남기다)

## "Gates are clean."
- 레지스터: technical
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 테스트·타입검사·린트 같은 통과 관문이 모두 문제없다고 보고할 때(기술·보고)
- 한국어: 검사 관문이 모두 깨끗하다(통과했다).
- 설명: `gates` 는 머지 전에 통과해야 하는 자동 검사 묶음이다. `clean` 은 "오류·경고 없이 통과"를 뜻하는 개발자 구어다(`a clean build`, `typecheck: clean`). 원문은 괄호로 예외(기존 경고 2개)를 곧바로 밝혀 정직하게 보고했다.
- 예문: Gates are clean (the 2 lint warnings are pre-existing, in `ImageViewer.vue`).
- 유사어: All checks pass. (평이), Everything's green. (구어)
- 반의어: The build is red. (검사가 깨졌다)

## "navigating away mid-eval"
- 레지스터: technical
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 스크립트가 값을 읽는 도중 페이지가 다른 곳으로 넘어가 버렸다고 설명할 때(기술)
- 한국어: 평가(eval) 도중에 페이지가 다른 곳으로 이동해 버림.
- 설명: `navigate away` 는 "현재 페이지를 떠나다"다(`Are you sure you want to navigate away from this page?`). `mid-` 를 명사 앞에 붙이면 "~하는 도중"이 된다(`mid-flight`, `mid-sentence`, `mid-eval`). 하이픈 하나로 시점을 짧게 넣는다.
- 예문: The row-open check ended with the page navigating away mid-eval.
- 유사어: leaving the page partway through (풀어 쓴 표현), the page changed under the script (구어)

## "wasn't read back"
- 레지스터: technical
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 값을 썼거나 이동했지만 결과를 다시 읽어 확인하지 못했다고 밝힐 때(기술·보고)
- 한국어: (결과를) 다시 읽어 확인하지 못했다.
- 설명: `read back` 은 "써 넣은 것을 되읽어 확인하다"다. 무전·전화에서 숫자를 복창하는 것도 `read back` 이라 한다. 원문은 수동태로 "누가"는 빼고 확인이 빠졌다는 사실만 보고한다.
- 예문: The page navigated away mid-eval, so the destination wasn't read back.
- 유사어: wasn't confirmed (평이), I didn't get to verify it (구어, 1인칭)
- 반의어: was read back and matched (되읽어 일치함을 확인했다)

## "Decisions the manager should know about"
- 레지스터: professional
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 보고서에서 윗사람이 꼭 알아야 할 판단만 따로 모아 머리말을 달 때(업무·문어)
- 한국어: 관리자가 알아야 할 결정 사항.
- 설명: 명사 뒤에 관계절을 바로 붙인 머리말이다(`Decisions [that] the manager should know about`). 목적격 관계대명사 `that` 이 빠지고 전치사 `about` 이 끝에 남는다. 영어 구어·보고서에서 아주 자연스러운 어순이다. 뒤에 `(all 14 are in the report)` 처럼 전체 위치를 밝혀 두면 요약이 빠짐없다는 오해를 막는다.
- 예문: Decisions the manager should know about (all 14 are in the report): the subtitle gains a third clause.
- 유사어: Heads-up items (구어, 미리 알림), Judgment calls worth flagging (격식, 짚어 둘 판단)

## "has no slot for it"
- 레지스터: professional
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 정해진 형식에 넣을 자리가 없어서 손을 댔다고 이유를 댈 때(업무·문어)
- 한국어: 그걸 넣을 자리가 없다.
- 설명: `slot` 은 틀 안의 빈칸이다. 템플릿·문자열·일정에 두루 쓴다(`a free slot`, `no slot in the schedule`). 원문은 "공통 지침은 넣으라는데 항목 지침의 문구에는 자리가 없다"는 두 요구의 충돌을 이 한마디로 설명한다.
- 예문: The common brief asks for undated rows to be counted there, and the item brief's string has no slot for it.
- 유사어: doesn't leave room for it (구어), makes no provision for it (격식)
- 반의어: has a placeholder for it (자리가 마련돼 있다)

## "behave as the brief describes"
- 레지스터: professional
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 만든 것이 지시서대로 동작함을 확인했다고 보고할 때(업무·보고)
- 한국어: 지시서에 적힌 대로 동작한다.
- 설명: `as + 주어 + 동사` 는 "~하는 대로"다. `brief` 는 작업 지시서(요약 지침)다. `as described in the brief` 로도 쓰지만, 원문처럼 `the brief describes` 로 지시서를 주어로 세우면 문장이 능동이 되고 짧아진다.
- 예문: Tile filters, sorting and both empty states all behave as the brief describes.
- 유사어: work as specified (격식), do what the brief says (구어)
- 반의어: deviate from the brief (지시서와 어긋나다)

## "nothing amended, not pushed"
- 레지스터: technical
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 기존 커밋을 고쳐 쓰지 않고 새 커밋을 얹었으며 원격에도 안 올렸다고 상태를 밝힐 때(기술·git)
- 한국어: 기존 커밋은 수정하지 않았고, 푸시도 안 했다.
- 설명: `amend` 는 "수정하다"인데 git 에서는 `git commit --amend`, 즉 마지막 커밋을 고쳐 쓰는 것을 가리킨다. 리뷰 반영을 새 커밋으로 쌓았다는 사실은 리뷰어에게 중요한 정보라 괄호로 짧게 덧붙였다. 동사 없이 과거분사만 둔 축약 보고체다.
- 예문: All five findings are fixed in a second commit on `work/afm-recipes` (nothing amended, not pushed).
- 유사어: added as a new commit, nothing rewritten (풀어 쓴 표현), history untouched (구어)
- 반의어: force-pushed over the old commit (기존 커밋을 덮어 강제 푸시했다)

## "Both server exits are my own shutdown."
- 레지스터: conversational, technical
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 로그에 찍힌 종료가 사고가 아니라 내가 한 일이라고 미리 해명할 때(보고·구어)
- 한국어: 서버 두 개가 꺼진 건 둘 다 내가 내린 것이다.
- 설명: `my own` 이 "남 탓이 아니라 내 것"을 강조한다. 이상해 보이는 로그를 먼저 짚고 원인을 자기에게 돌려 걱정을 막는 보고 습관이다. 구어로는 `That's on me.` 나 `That was me.` 가 같은 기능을 한다.
- 예문: Both server exits are my own shutdown, not crashes.
- 유사어: That was me, not a crash. (구어), Both were deliberate shutdowns. (격식)
- 반의어: an unexpected crash (예상 못 한 충돌)

## "in neither X nor Y"
- 레지스터: professional
- 출처: transcript:skewnono-afm-recipes/4e1c4ef9 (작업 보고)
- 맥락: 어떤 항목이 두 분류 어디에도 들지 않는 경계 사례를 밝힐 때(문어·명세)
- 한국어: X 에도 Y 에도 들지 않는다.
- 설명: `neither … nor` 는 둘 다 부정이다. 동사를 긍정형(`is`)으로 두고 전치사구 안에서 부정하므로 `is not in the recent or the stale tile` 보다 짧고 단정적이다. 경계 사례를 명세에 적을 때 즐겨 쓴다.
- 예문: A recipe with no dated row is in neither the recent nor the stale tile.
- 유사어: falls into neither group (구어에 가까움), belongs to neither category (격식)
- 반의어: in both X and Y (양쪽에 다 든다)

## "Known and intentional, do not report:"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/cf201adc subagent agent-a49adc4c (리뷰 지시문)
- 맥락: 리뷰어에게 이미 알고 일부러 둔 것은 지적하지 말라고 범위를 미리 자를 때(지시문·문어)
- 한국어: 알고 있고 의도한 것이니 보고하지 말 것:
- 설명: 형용사 두 개 + 명령문을 쉼표로 이은 머리말이다. 리뷰어가 의도된 설계를 버그로 올리는 헛수고를 막는다. 뒤에 콜론으로 목록을 붙인다. 노트의 `Not in scope:` 와 짝을 이루는 지시문 장치다.
- 예문: Known and intentional, do not report: the parser accepts only `YYYY.MM.DD HH:mm:ss` read as KST.
- 유사어: By design — skip these: (구어), The following are intentional and out of scope: (격식)
