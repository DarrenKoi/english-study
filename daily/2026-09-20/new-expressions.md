# 2026-09-20 — 새 표현

> repo 문서 10건(equipment-data-map 아키텍처 4건, auto_recipe_creator 기능 메모 5건, skewnono chat→RAG 계약)은 본문이 한국어라 표현을 뽑지 않았다. 20개 모두 transcript 에서 나왔다. 어시스턴트 영어가 17개(equipment-data-map 6, auto-recipe-creator 6, skewnono 5)다. 나머지 3개는 세션에 주입된 스킬 본문(diagnosing-bugs 2, leave-office 1)이다. 노트에 이미 있는 `load-bearing`, `go stale`, `be level with`, `I left it alone.`, `say the word`, `by design`, `tell A from B`, `keyed on X`, `re-litigate` 는 뺐다.

## "If you catch yourself (doing X), stop"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator (diagnosing-bugs 스킬 본문)
- 맥락: 자기도 모르게 나쁜 습관으로 빠지는 순간을 짚어 멈추라고 할 때(가이드·코칭·회고)
- 한국어: 문득 ~하고 있는 자신을 발견하면 멈춰라
- 설명: 원문은 `If you catch yourself reading code to build a theory before this command exists, stop`. `catch + 목적어 + -ing` 는 "~하는 현장을 잡다"이다. 목적어가 `yourself` 면 무심코 하던 행동을 스스로 알아챈다는 뜻이 된다. `find yourself -ing` 보다 "하면 안 되는 걸 하다 들켰다"는 어감이 짙다.
- 예문: If you catch yourself adding a third flag to the same function, stop and split it.
- 유사어: if you find yourself -ing (중립, 잘못이라는 어감이 약함), the moment you notice you're -ing (풀어 쓴 구어), should you be inclined to (격식 문어)

## "Don't block on it"
- 레지스터: conversational, technical
- 출처: transcript:auto-recipe-creator (diagnosing-bugs 스킬 본문)
- 맥락: 상대 답을 기다리느라 멈추지 말고 하던 일을 계속하라고 할 때(비동기 협업·채팅)
- 한국어: 그것 때문에 멈춰 서 있지 마라
- 설명: 원문은 `Don't block on it — proceed with your ranking if the user is AFK.` 스레드가 I/O 를 기다리며 멈추는 `block on` 을 사람의 일하는 방식에 빌려 왔다. 확인은 요청하되 답이 올 때까지 손 놓고 있지는 말라는 뜻이다. `AFK` 는 away from keyboard 의 줄임말.
- 예문: I've asked the infra team about the quota, but don't block on it — start with the default and we'll adjust later.
- 유사어: don't wait on it (평이), keep moving in the meantime (구어), proceed without waiting for confirmation (격식)
- 반의어: hold off until you hear back, wait for sign-off

## "where my head was"
- 레지스터: conversational
- 출처: transcript:auto-recipe-creator (leave-office 스킬 본문)
- 맥락: 작업을 멈추던 시점에 무슨 생각을 하고 있었는지 메모로 남기거나 물을 때(인수인계·퇴근 메모)
- 한국어: 그때 내 생각이 어디쯤 가 있었는지
- 설명: 원문은 `a decision made mid-session, or "where my head was" that the next session would otherwise have to rediscover`. `head` 는 머릿속 생각의 상태를 가리킨다. `Where's your head at?` 은 "지금 무슨 생각이야?"라는 구어다. 코드에도 커밋에도 남지 않는 사고의 맥락을 가리킬 때 딱 맞는다.
- 예문: I left a note in the PR about where my head was, so you won't have to guess why the cache is disabled.
- 유사어: my train of thought (조금 더 중립), what I was thinking at the time (풀어 쓴 말), my mental state (같은 스킬의 템플릿에 나온 말, 딱딱함)

## "give the heading the stack it promises"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 제목·이름이 예고한 내용이 실제로는 비어 있어 채워 넣는다고 설명할 때(문서 리뷰·diff 설명)
- 한국어: 제목이 약속한 스택을 실제로 넣어 주다
- 설명: 원문은 `The third gives the heading the stack it promises`. `## Tech Stack` 이라는 제목 아래 정작 스택이 없던 걸 고치는 diff 를 한 줄로 소개한다. `the stack (that) it promises` 는 관계대명사가 생략된 절이다. 제목을 주어로 세워 "제목이 약속했다"고 의인화하니 "있어야 할 게 없었다"는 지적이 부드럽게 들어간다.
- 예문: This commit finally gives the "Quick Start" section the commands it promises.
- 유사어: make the section live up to its title (관용, 조금 길다), fill in what the heading implies (평이), deliver on the heading (짧은 비즈니스 어투)
- 반의어: a heading with nothing under it

## "Apply all four, or only some?"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 여러 제안을 내놓은 뒤 전부 할지 일부만 할지 상대에게 짧게 결정을 넘길 때(리뷰 끝·채팅)
- 한국어: 네 개 다 적용할까요, 일부만 할까요?
- 설명: 주어와 조동사(`Should I`)를 뺀 생략 의문문이다. 긴 보고 끝에 선택지 둘만 남겨 상대가 한마디로 답하게 만든다. 실제로 사용자는 `apply all four` 세 단어로 답했다. 질문이 답의 문형까지 미리 정해 준 셈이다.
- 예문: I found six unused imports. Remove all six, or only the ones in this file?
- 유사어: Want me to apply all of them, or just a few? (더 구어), Shall I proceed with all four? (격식, 선택지를 하나만 제시), All or some? (극단적으로 짧음)

## "end up (somewhere)"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 누가 의도하지 않았는데 결과적으로 엉뚱한 자리·상태에 가 있다고 말할 때(버그·문서 정리 보고)
- 한국어: (어쩌다 보니) 결국 ~에 가 있다
- 설명: 원문은 `The focus-ring bullet had ended up inside the Dark Field section and is back under Semantic.` 누가 옮겼는지는 묻지 않고 결과만 말한다. 과거완료 `had ended up` 이 고치기 전 상태를, 현재 `is back` 이 고친 뒤 상태를 가리켜 한 문장에 전후가 담긴다. 뒤에는 장소 부사구나 `-ing` 가 온다(`ended up rewriting it`).
- 예문: The retry config had ended up in the test folder, so production never read it.
- 유사어: wind up (같은 뜻, 더 구어), land in (장소에 한정), find its way into (의도 없이 섞여 들어갔다는 어감)
- 반의어: stay put, be where it belongs

## "in the meantime"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 근본 수정이 나오기 전까지의 기간에 할 일·하지 말 일을 덧붙일 때(보고·계획)
- 한국어: 그사이에는, 그때까지는
- 설명: 원문은 `Fixing it means changing one function, and teammates shouldn't copy that chip in the meantime.` 고칠 방법을 말한 뒤 "고쳐지기 전까지는"의 행동 지침을 붙인다. 문두에 두면 쉼표를 찍는다(`In the meantime, …`). `meanwhile` 은 "같은 시각 다른 곳에서"라는 동시 진행의 뜻도 있어 쓰임이 조금 넓다.
- 예문: The proper fix needs a schema change; in the meantime, please don't rely on that column.
- 유사어: for now (더 짧고 가벼움), until then (기한이 분명할 때), in the interim (격식 문어)
- 반의어: once it's fixed, from then on

## "without an explicit agreement from you"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 허락받지 않고 내 판단으로 넣은 변경을 자진해서 밝힐 때(완료 보고·PR 설명)
- 한국어: 당신의 명시적 동의 없이
- 설명: 원문은 `One thing I added without an explicit agreement from you: … Remove it from that list if the width wasn't agreed.` 자진 신고와 되돌리는 방법을 한 쌍으로 준다. `One thing I added …:` 는 동사 없는 명사구 머리말이고 콜론 뒤에 내용이 온다. `explicit` 한 단어가 "암묵적으로는 괜찮다고 봤다"는 여지를 남긴다.
- 예문: One change I made without an explicit agreement from you: the default timeout is now 30 seconds. Revert it if that wasn't the plan.
- 유사어: without checking with you first (구어), on my own judgment (내 판단 쪽을 강조), without your sign-off (결재 어감)
- 반의어: as we agreed, per your request

## "only proves the map matches itself"
- 레지스터: technical, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 검증이 자기 자신과 비교하는 순환 구조라 아무것도 보증하지 못한다고 지적할 때(설계 리뷰)
- 한국어: 지도가 자기 자신과 일치한다는 것만 증명할 뿐이다
- 설명: 원문은 `Checking hashes against index.json only proves the map matches itself.` 해시 목록이 검사 대상과 같은 곳에서 나왔다면 통과는 당연하다. `only proves` 가 검증의 효력 범위를 좁히고 `matches itself` 가 순환을 드러낸다. 주어는 동명사구 `Checking hashes against …` 다. `check A against B` 는 "A 를 B 에 대조하다"이다.
- 예문: Comparing the output to a snapshot we just generated only proves the code matches itself.
- 유사어: a circular check (명사로 짧게), self-consistent but unverified (형용사 대비), grading your own homework (비유, 구어)
- 반의어: verified against an independent source

## "each one reproduces"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 찾은 결함이 추측이 아니라 실제로 재현된다고 보고할 때(코드 리뷰·버그 보고)
- 한국어: 하나하나 다 재현된다
- 설명: 원문은 `I found three blocking defects, and each one reproduces.` `reproduce` 는 보통 타동사(`reproduce the bug`)지만 개발자 영어에서는 버그를 주어로 한 자동사로도 쓴다. 같은 대화의 `Three blocking defects still reproduce` 도 같은 용법이다. 한국어 "재현된다"를 굳이 `is reproduced` 로 옮기지 않아도 된다.
- 예문: The crash only reproduces on Windows when the path contains a space.
- 유사어: I can reproduce each one (사람을 주어로), each has a repro (명사 repro, 구어), is reproducible (형용사, 조금 더 격식)
- 반의어: can't reproduce it, works on my machine

## "the test locks the defect in"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 테스트가 잘못된 동작을 기대값으로 단언하고 있어 버그를 고치면 테스트가 깨진다고 짚을 때(코드 리뷰)
- 한국어: 테스트가 결함을 굳혀 버린다
- 설명: 원문은 `test_folder_request_… asserts that pending, so the test locks the defect in.` `lock in` 은 원래 "확정해 못 바꾸게 하다"라는 좋은 뜻으로 쓰는데, 여기서는 목적어가 `the defect` 라 나쁜 쪽으로 뒤집혔다. 목적어가 `lock` 과 `in` 사이에 끼는 분리형 구동사다(대명사면 반드시 `lock it in`).
- 예문: That snapshot was recorded while the bug was live, so the test locks the defect in.
- 유사어: the test enshrines the bug (격식, 비꼬는 어감), the test asserts the wrong behavior (평이하고 정확), bake the bug in (구어)
- 반의어: the test catches the defect

## "fail partway through"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 작업이 시작은 했지만 중간에 실패해 어중간한 상태가 남는 위험을 말할 때(리뷰·장애 분석)
- 한국어: 도중에 실패하다
- 설명: 원문은 `A deep --output can fail partway through writing and leave a partial folder that blocks a rerun.` `partway through + 명사/-ing` 는 "~의 중간쯤에서"다. 뒤의 `leave a partial folder that blocks a rerun` 까지가 한 세트로, 중간 실패가 왜 문제인지(찌꺼기가 재실행을 막는다)를 이어 말한다.
- 예문: If the migration fails partway through, half the tables will have the new column and half won't.
- 유사어: fail midway (같은 뜻), die halfway through (구어), abort mid-write (더 기술적)
- 반의어: fail up front, complete atomically

## "hold up"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대가 고쳤다고 한 것을 직접 확인해 보니 대부분 맞더라고 인정하면서 남은 문제를 꺼낼 때(재리뷰)
- 한국어: (따져 봐도) 버티다, 유효하다
- 설명: 원문은 `Most of the fixes hold up, but one contradiction remains`. 주장·수정·논리가 검증을 받고도 무너지지 않는다는 자동사다. `Most … hold up, but one … remains` 는 인정을 먼저 하고 `but` 뒤에 본론을 두는 재리뷰의 기본 틀이다. 바로 아래 소제목 `Checked and holding:` 도 같은 동사의 변주다.
- 예문: Your benchmark numbers hold up, but the memory claim doesn't match what I measured.
- 유사어: check out (구어, "확인해 보니 맞다"), stand up to scrutiny (격식), be sound (형용사로 짧게)
- 반의어: fall apart, not survive a closer look

## "out of line with"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 구현이 기준 문서·규격과 어긋나 있다고 지적할 때(리뷰 보고서)
- 한국어: ~와 맞지 않는, 어긋난
- 설명: 원문은 `The reserved-name list is out of line with implementation-reference §7`. `in line with`(~에 부합하는)의 반대말이다. 조심할 점이 하나 있다. `with` 없이 사람에게 `out of line` 이라고 하면 "선을 넘었다, 무례했다"는 전혀 다른 뜻이 된다.
- 예문: The retry count in the client is out of line with the limit documented in the API guide.
- 유사어: inconsistent with (가장 중립), at odds with (충돌의 어감이 더 강함), doesn't match (평이한 구어)
- 반의어: in line with, consistent with

## "Found the shape of it."
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 원인을 다 밝히진 못했지만 문제의 윤곽은 잡았다고 중간 보고할 때(디버깅 채팅)
- 한국어: 윤곽은 잡았다
- 설명: 원문은 `Found the shape of it. Two things, one certain, one needing your console line.` 주어 `I` 를 뺀 메모체다. `the shape of it` 은 세부는 아직이어도 전체 모양은 보인다는 뜻이라 `found the cause` 보다 한 발 물러선 정직한 표현이다. 뒤 문장이 확실한 것 하나와 확인이 필요한 것 하나로 곧바로 나눈다.
- 예문: Found the shape of it: the cache is fine, but something upstream is sending duplicate keys.
- 유사어: I have a rough picture (평이), I've narrowed it down (후보를 좁혔다는 쪽), I see the outline of the problem (조금 더 격식)
- 반의어: I'm still in the dark, nailed it

## "overshoot"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 조정이 목표 지점을 지나쳐 너무 많이 가 버렸다고 말할 때(제어·튜닝·디버깅)
- 한국어: (목표를) 지나치다, 과하게 가다
- 설명: 원문은 표 안의 `Zoom-out overshot.` 두 단어짜리 진단이다. 배율을 너무 낮춘 탓에 한 화면이 탐색 범위를 다 덮어 훑을 셀이 0개가 됐다. 과거형은 `overshot`(shoot-shot-shot). 제어 공학의 overshoot 와 같은 말이고 예산·일정에도 쓴다.
- 예문: The auto-scaler overshot and spun up twice as many workers as the queue needed.
- 유사어: go too far (평이), overcorrect (바로잡으려다 반대로 지나침), overdo it (구어)
- 반의어: undershoot, fall short

## "came back clean"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 검사·리뷰·스캔을 돌렸더니 지적 사항이 없었다고 알릴 때(채팅 보고)
- 한국어: (검사 결과가) 깨끗하게 나왔다
- 설명: 원문은 `Review came back clean — (none), no findings at low effort.` `come back + 형용사` 는 맡긴 검사가 결과를 들고 돌아오는 그림이다. 병원 검사 결과(`the test came back negative`)에서 온 말투다. 관사 없는 `Review` 로 시작하는 메모체이고 `at low effort` 로 검사 강도의 한계까지 함께 밝힌다. 노트에 있는 `come back empty` 와 같은 틀이다.
- 예문: The security scan came back clean, so I'm merging.
- 유사어: no findings (보고서 말투), nothing flagged (수동, 짧음), it passed (가장 평이)
- 반의어: came back with findings, turned up issues

## "Taking that as: …"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 애매한 지시를 받았을 때 내가 어떻게 해석했는지 먼저 밝히고 진행할 때(채팅·업무 메신저)
- 한국어: ~라는 뜻으로 받아들이고 진행합니다
- 설명: 원문은 `Taking that as: commit and push the pending edits.` 사용자의 `fix the uncommited changes` 가 "고쳐라"인지 "커밋해라"인지 애매하자, 되묻지 않고 해석을 한 줄로 선언한 뒤 움직였다. 틀렸으면 상대가 바로 정정하면 된다. `I'm` 을 뺀 현재분사 머리말이다. `take A as B` 는 "A 를 B 로 받아들이다"이다.
- 예문: Taking that as: keep the old endpoint alive until the mobile app updates. Shout if you meant something else.
- 유사어: I'll read that as … (같은 뜻, 동사만 `read`), Assuming you mean … (가정임을 더 드러냄), To confirm my understanding, … (격식, 답을 기다리는 쪽)
- 반의어: Could you clarify what you mean?

## "One thing worth repeating, since it affects how you read the numbers"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 이미 한 말이지만 상대가 결과를 오해할 수 있어 보고 끝에 한 번 더 못 박을 때(데이터·지표 전달)
- 한국어: 수치를 읽는 방식에 영향을 주니 다시 말해 둘 것 하나
- 설명: 원문은 `One thing worth repeating, since it affects how you read the numbers: correction_finished_at is when the agent finished clicking, not confirmation that the align is right.` 반복하는 이유를 `since` 절로 먼저 대서 잔소리로 들리지 않는다. 콜론 뒤에서는 `A is X, not Y` 로 오해하기 쉬운 해석(Y)을 명시적으로 지운다. `worth + -ing` 구조라 `worth to repeat` 는 틀린다.
- 예문: One thing worth repeating, since it affects how you read the chart: the y-axis is cumulative, not per day.
- 유사어: Just to reiterate (짧은 격식), One caveat before you read the numbers (처음 꺼내는 주의사항일 때), Again, keep in mind that … (구어)

## "apart from"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 전체가 어떻다고 말하면서 예외 하나를 떼어 놓을 때(상태 보고)
- 한국어: ~을 빼면, ~ 말고는
- 설명: 원문은 `The working tree is clean apart from the untracked docs/research/, which isn't mine and which I left alone.` "깨끗하다"는 단언에 예외를 붙인 뒤 계속적 관계절 `which … and which …` 두 개로 그 예외를 왜 건드리지 않았는지까지 설명한다. 영국식에서 더 흔하고 미국식은 `aside from` 을 많이 쓴다. 문맥에 따라 "~외에도"(추가)의 뜻도 되니 앞뒤를 봐야 한다.
- 예문: All the tests pass apart from the two that need a live database.
- 유사어: except for (가장 흔함, 예외만 뜻함), aside from (미국식), other than (부정문·의문문과 잘 어울림)
- 반의어: including, along with
