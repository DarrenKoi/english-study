# 2026-09-01 — 새 표현

## "Everything else survived scrutiny."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt fdbfe0cc (scripts/ 정리 보고)
- 맥락: 삭제 후보를 하나씩 검토한 뒤 "지워도 되는 건 이것뿐"이라고 결론지을 때(글로 쓰는 작업 보고, 격식)
- 한국어: 나머지는 전부 (따져 보니) 살아남았다.
- 설명: `scrutiny` 는 그냥 보는 게 아니라 "지울 근거를 찾으려고 캐묻는 검토"다. 주어를 사람이 아니라 대상(`everything else`)으로 두면 "내가 봐줬다"가 아니라 "대상이 스스로 정당화됐다"로 읽힌다. 삭제·축소 작업 보고의 표준 마무리.
- 예문: I only removed one file — everything else survived scrutiny.
- 유사어: everything else held up (더 평이), each of the others still earns its place (근거를 앞세운 표현)
- 반의어: it didn't hold up under scrutiny

## "not mine to fix here"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt fdbfe0cc
- 맥락: 내 변경과 무관한 기존 실패를 발견했을 때, 책임 밖임을 밝히면서도 숨기지 않을 때(구어·PR 코멘트 모두)
- 한국어: 이건 여기서 내가 고칠 몫이 아니다.
- 설명: `mine to fix` 는 "내가 고칠 자격/책임이 있는"이라는 명사+to부정사 구문이다. `here` 가 붙으면 "영원히 안 고친다"가 아니라 "이 작업 범위에서는 아니다"로 좁혀져서 회피처럼 들리지 않는다.
- 예문: That failure exists on main too — not mine to fix here, but worth a ticket.
- 유사어: out of scope for this change (더 격식), I'll leave that one alone (더 평이)
- 반의어: I'll pick that up while I'm in here

## "a design call that's genuinely yours"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt dc332be2 (tttm 배치도 진단)
- 맥락: 기술적으로 다 조사해 놓고 마지막 선택은 상대에게 넘길 때(협업·구두 보고)
- 한국어: 이건 정말로 당신이 내려야 할 설계 판단입니다.
- 설명: `call` 은 심판의 판정에서 온 말로 "정답이 없어 누군가 정해야 하는 결정"을 뜻한다. `genuinely` 가 사교적 양보와 진짜 위임을 가른다 — 뒤에 "the options aren't equivalent"처럼 왜 위임인지를 붙이는 게 관용적이다.
- 예문: I've narrowed it to three options, but which one ships is a design call that's genuinely yours.
- 유사어: your judgment call (더 평이), this one's above my pay grade (농담조)
- 반의어: there's only one defensible option here

## "if the itch is X, the cheaper fix is Y"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt f2d1927f (`_` 폴더 리팩터링 논의)
- 맥락: 상대가 요청한 큰 작업을 거절하면서 진짜 불만만 싼값에 해소해 줄 때(리뷰·설계 논의)
- 한국어: 가려운 데가 X라면, 더 싸게 먹히는 해법은 Y다.
- 설명: `itch` 는 "요청 뒤에 깔린 진짜 불편함"을 가리키는 은유다. 요청의 형태(폴더를 합치자)와 동기(플러밍인지 한눈에 안 보인다)를 갈라놓아서, 거절이 아니라 재조준으로 들린다.
- 예문: If the itch is that you can't tell these are plumbing at a glance, the cheaper fix is a one-line README.
- 유사어: what you're actually after is (직설적), the underlying need here is (격식)
- 반의어: taking the request at face value

## "shrink the hypothesis space"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator aeec243f (`diagnosing-bugs` 스킬 본문)
- 맥락: 재현 조건을 최소화해야 하는 이유를 설명할 때(디버깅 문서·기술 토론)
- 한국어: 가설 공간을 좁힌다.
- 설명: 후보 원인의 집합을 공간으로 보고 그 부피를 줄인다는 비유다. `narrow down the cause` 가 하나로 좁히는 그림이라면 이쪽은 "아직 여럿이지만 훨씬 적다"라서 중간 단계 보고에 맞는다.
- 예문: A minimal repro shrinks the hypothesis space — there are simply fewer moving parts left to suspect.
- 유사어: rule out whole classes of cause (제거를 강조), narrow the search (평이)
- 반의어: everything is still on the table

## "Spend disproportionate effort here."
- 레지스터: professional
- 출처: transcript:auto-recipe-creator aeec243f (`diagnosing-bugs` 스킬 본문)
- 맥락: 여러 단계 중 하나에 시간을 몰아 쓰라고 지시할 때(가이드·문서, 명령형)
- 한국어: 여기에는 (다른 데와 비교가 안 되게) 과할 만큼 시간을 써라.
- 설명: `disproportionate` 는 보통 부정적인 단어인데 여기서는 일부러 긍정으로 뒤집어 쓴다. "균형 있게 배분하지 말라"는 지시라 우선순위 문서에서 힘이 세다.
- 예문: Spend disproportionate effort on the feedback loop; everything after it is mechanical.
- 유사어: this is where the leverage is (성과 관점), front-load the effort (시점 관점)
- 반의어: timebox it and move on

## "riskier than its diff size suggests"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt f2d1927f
- 맥락: 변경 줄 수가 적다고 안심하는 상대에게 숨은 위험을 알릴 때(코드 리뷰·설계 반대)
- 한국어: diff 크기가 말해 주는 것보다 위험하다.
- 설명: `X-er than Y suggests` 는 "겉으로 드러난 지표와 실제가 어긋난다"를 한 구로 압축한 틀이다. `suggests` 가 지표를 의인화해서, 지표를 믿은 상대를 탓하지 않고도 반박이 된다.
- 예문: The untracked `office.py` copies are what make this rename riskier than its diff size suggests.
- 유사어: the diff undersells the risk (더 구어), small change, wide blast radius (대구)
- 반의어: exactly as small as it looks

## "The letter below is kept as received."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/chat/chat_office_adapter_handoff.txt
- 맥락: 남이 보낸 원문을 손대지 않고 그대로 보존한다고 밝힐 때(문서 머리말, 격식)
- 한국어: 아래 편지는 받은 그대로 둡니다.
- 설명: `as received` 는 `as-is` 보다 좁아서 "수신 시점 상태 그대로"를 뜻한다. 오타·부정확한 내용이 있어도 편집하지 않았음을 미리 밝혀 두는 장치라, 인수인계 문서의 관례적 한 줄이다.
- 예문: The current contract lives elsewhere; the letter below is kept as received.
- 유사어: reproduced verbatim (더 격식), quoted unedited (평이)
- 반의어: lightly edited for clarity

## "no amount of staring at code will save you"
- 레지스터: conversational, technical
- 출처: transcript:auto-recipe-creator aeec243f (`diagnosing-bugs` 스킬 본문)
- 맥락: 재현 수단 없이 코드만 읽는 디버깅을 말릴 때(멘토링·구어체 지침)
- 한국어: 코드를 아무리 노려봐도 소용없다.
- 설명: `no amount of X will Y` 는 "양으로는 절대 안 된다"는 강한 부정 틀이다. `save you` 가 노력이 아니라 구원의 문제로 프레임을 바꿔서, 접근법 자체가 틀렸다는 뜻이 된다.
- 예문: Without a failing test, no amount of staring at code will save you.
- 유사어: you can't read your way out of this (같은 강도, 더 구어), reading code won't get you there (완화)
- 반의어: a careful read of the diff is enough here

## "removes the whole failure class"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt dc332be2
- 맥락: 개별 버그를 막는 가드 대신 기능을 삭제한 선택을 정당화할 때(설계 근거·커밋 본문)
- 한국어: 실패 유형 자체를 통째로 없앤다.
- 설명: `failure class` 는 한 건의 버그가 아니라 "같은 원리로 계속 생길 버그들"을 묶은 단위다. 이 말이 붙으면 회귀 테스트를 안 쓴 이유까지 자동으로 설명된다 — 없앤 코드에는 회귀할 것이 없으니까.
- 예문: Removing the region removes the whole failure class, which is why there's no regression test to write.
- 유사어: designs the bug out (더 짧음), makes the state unrepresentable (타입 설계 문맥)
- 반의어: patches this one instance

## "which is worse than never"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt dc332be2
- 맥락: "가끔 맞는" 절충안을 반대할 때(설계 토론·리뷰)
- 한국어: 그건 아예 안 하느니만 못하다.
- 설명: 앞에 `sometimes` 를 강조해 두고 뒤에서 `worse than never` 로 받는 대구다. 신뢰의 문제라 절반의 정확성이 0의 정확성보다 나쁘다는 논리를 한 줄로 세운다.
- 예문: A containment check would have made the circle sometimes honest, which is worse than never.
- 유사어: intermittently correct is the worst kind (풀어쓴 형태), a half-right signal trains the wrong habit (근거 제시형)
- 반의어: partial coverage still beats none

## "it just needed to stop being the only signal"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt dc332be2
- 맥락: 기존 설계를 부정하지 않으면서 무엇이 부족했는지만 짚을 때(리뷰 답변·회고)
- 한국어: 그게 틀린 게 아니라, 유일한 신호이기를 그만두면 됐다.
- 설명: `just needed to stop -ing` 은 "고칠 게 이것 하나뿐"이라는 최소 진단이다. 앞 문장에서 기존 선택을 먼저 옹호(`It's the right encoding for ...`)한 뒤 이 문장으로 넘어가는 순서가 관용적이다.
- 예문: The red/blue rule is the right encoding — it just needed to stop being the only signal on a card about groups.
- 유사어: it was necessary but not sufficient (격식), nothing wrong with it, it was just carrying too much (구어)
- 반의어: the encoding itself was wrong

## "your history moved under me"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt dc332be2
- 맥락: 작업 도중 다른 세션·동료가 같은 브랜치에 커밋해서 기준점이 바뀐 걸 알릴 때(구어·짧은 보고)
- 한국어: 작업하는 사이에 (당신 쪽) 히스토리가 발밑에서 움직였다.
- 설명: `move under someone` 은 발판이 밟고 선 채로 움직이는 그림이라 "내 잘못도 당신 잘못도 아닌 타이밍"이라는 뉘앙스가 생긴다. 뒤에 병합이 깨끗했다는 사실을 붙여야 경고가 아니라 참고가 된다.
- 예문: Heads-up: your history moved under me — another session landed a commit between my two, but the merge was clean.
- 유사어: main moved while I was working (평범·안전), I rebased onto newer main midway (사실 위주)
- 반의어: the branch was untouched the whole time

## "X buys A and costs B"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt f2d1927f
- 맥락: 제안을 거절하면서 득실을 같은 문장에 나란히 놓을 때(설계 판단·리뷰)
- 한국어: X는 A를 얻어 주고 B를 치르게 한다.
- 설명: `buy` 와 `cost` 를 한 주어에 걸어 대구로 만드는 게 핵심이다. 이득을 일부러 사소하게(`a shorter ls`), 비용을 구체적으로 적으면 판정이 문장 안에서 저절로 난다.
- 예문: Moving them under one folder buys a shorter `ls` and costs a repo-wide rename plus an office boot break.
- 유사어: the trade isn't worth it (결론만), you'd pay X for Y (순서 반대)
- 반의어: it pays for itself

## "died with ModuleNotFoundError"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt fdbfe0cc
- 맥락: 실행이 특정 예외로 즉시 종료됐다고 보고할 때(버그 리포트·구두 설명)
- 한국어: ModuleNotFoundError를 내며 죽었다.
- 설명: `die with <예외>` 는 `fail with` 보다 구어적이고, 프로세스가 살아서 잘못된 값을 내는 게 아니라 그 자리에서 끝났음을 강조한다. 예외 이름은 관사 없이 그대로 넣는다.
- 예문: The path-form invocation died with ModuleNotFoundError because the sys.path bootstrap was missing.
- 유사어: blew up with (더 구어), exits non-zero with (중립·격식)
- 반의어: silently returned an empty list

## "Treat the loop as a product."
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator aeec243f (`diagnosing-bugs` 스킬 본문)
- 맥락: 임시로 만든 도구를 계속 다듬으라고 지시할 때(방법론 문서, 명령형)
- 한국어: 그 루프를 (일회용이 아니라) 제품처럼 다뤄라.
- 설명: `treat X as Y` 는 대상의 지위를 바꾸는 지시 틀이다. `product` 라는 단어 하나로 "속도·정확도·재현성을 계속 개선한다"는 기대치가 따라붙어서, 설명을 길게 안 해도 된다.
- 예문: Treat the loop as a product: make it faster, sharper, and more deterministic before you use it.
- 유사어: invest in your tooling (일반적), the harness deserves the same care as the fix (풀어쓴 형태)
- 반의어: throw it away once it goes green

## "keep raising the rate until it's debuggable"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator aeec243f (`diagnosing-bugs` 스킬 본문)
- 맥락: 간헐적 버그를 다룰 때 목표를 "완벽 재현"이 아니라 "재현률 상승"으로 다시 잡을 때
- 한국어: 디버깅이 될 만해질 때까지 재현률을 계속 올려라.
- 설명: `debuggable` 은 사전보다 현장에서 굳은 형용사로 "작업이 가능한 상태"를 뜻한다. 50%는 되고 1%는 안 된다는 식으로 숫자를 옆에 붙여 주는 게 이 표현의 관용적 쓰임이다.
- 예문: A 50%-flake bug is debuggable and a 1% one isn't — keep raising the rate until it's debuggable.
- 유사어: get the repro rate up (평이), make it fail on demand (이상적 목표)
- 반의어: chase a clean, one-shot repro

## "time it to land right before ~"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt f2d1927f
- 맥락: 위험한 변경을 언제 머지할지 상대의 일정에 맞춰 제안할 때(계획 논의)
- 한국어: ~하기 바로 전에 떨어지도록 시점을 맞춘다.
- 설명: `land` 는 변경이 main 에 안착하는 순간을 가리키는 표준 동사고, `time X to ~` 가 그 시점을 의도적으로 고른다는 뜻을 얹는다. 뒤처리가 필요한 변경일수록 이 조합이 자연스럽다.
- 예문: I'd do it in a worktree and time it to land right before you're at the office.
- 유사어: schedule the merge for when you can babysit it (풀어쓴 형태), hold it until you're on site (보류 강조)
- 반의어: land it whenever it's ready

## "it names the misreading directly rather than leaving it to be inferred"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt dc332be2 (범례 추가 보고)
- 맥락: UI 문구·문서에서 오해를 암시가 아니라 명시로 막았다고 설명할 때(디자인 근거)
- 한국어: 오해를 암시로 남기지 않고 곧장 이름 붙여 준다.
- 설명: `name X` 는 "말로 정확히 지목한다"는 뜻이고, `leave it to be inferred` 는 "독자가 알아서 유추하게 둔다"는 반대편이다. 라벨 세 개를 늘어놓는 대신 오해 자체를 문장으로 쓰라는 원칙을 이 대비 하나로 표현한다.
- 예문: The trailing note says the color is a tolerance verdict, not group membership — it names the misreading directly rather than leaving it to be inferred.
- 유사어: says the quiet part out loud (구어·농담기), states the exclusion explicitly (격식)
- 반의어: leaves the reader to connect the dots
