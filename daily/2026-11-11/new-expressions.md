# 2026-11-11 — 새 표현

출처는 두 대화 기록입니다. 대부분 skewnono_v3_nuxt 세션(d0eba2c5)에서 나왔습니다. 이 세션에서 CLAUDE.md·AGENTS.md를 점검하고 CI에 lint를 넣었고, werkzeug 버전 차이로 깨진 테스트도 고쳤습니다. 세션에 함께 실린 CLAUDE.md 본문과 `diagnosing-bugs`·`ponytail` 스킬 지침에서도 골랐습니다.

## "all there and all checked out"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 ([assistant] CLAUDE.md Quality Report)
- 맥락: 점검 결과를 보고하면서 "빠진 것도 없고 확인해 보니 다 맞다"고 할 때(보고서·구어 모두)
- 한국어: 빠짐없이 다 있고, 확인해 보니 모두 맞다
- 설명: `check out` 을 자동사로 쓰면 "조사해 보니 사실로 드러나다"가 됩니다. `all there` 는 누락이 없다는 뜻이고, 둘을 `and` 로 이어 존재와 정확성을 한 번에 보고합니다.
- 예문: Backend, frontend and markdown-lint commands are all there and all checked out.
- 유사어: all present and verified (문어, 건조함), everything lines up (구어), all accounted for (빠짐없음 쪽에 무게)
- 반의어: doesn't hold up (확인해 보니 틀리다)

## "with the details pushed out to linked docs"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 ([assistant] Quality Report, Conciseness 항목)
- 맥락: 문서 구조를 평가하면서 "세부는 다른 문서로 빼 뒀다"고 할 때(리뷰·글)
- 한국어: 세부 내용은 링크한 문서로 밀어내 두고
- 설명: `push out to` 는 본문에서 바깥으로 밀어낸다는 그림입니다. `with + 명사 + 과거분사` 부대상황 구문이라 앞 문장("Dense")에 이유를 짧게 덧붙입니다.
- 예문: The README stays short, with the details pushed out to linked docs.
- 유사어: with the details moved into separate pages (평이), deferring the specifics to linked docs (격식), linking out for the details (구어)
- 반의어: with everything inlined (모두 본문에 넣음)

## "Nothing points to them, so …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 ([assistant] Quality Report, Issue 2)
- 맥락: 좋은 코드·문서가 있는데 아무 데서도 안내하지 않아 묻혀 있다고 지적할 때(리뷰)
- 한국어: 그걸 가리키는 곳이 아무 데도 없어서 …
- 설명: 무생물 `Nothing` 을 주어로 세워 "아무도 안 알려 준다"를 간결하게 만듭니다. 뒤의 `so` 절에서 그 결과(중복 구현)를 바로 이어 문제의 무게를 보여 줍니다.
- 예문: The shared helpers are solid, but nothing points to them, so a new adapter could rebuild code that already exists.
- 유사어: they aren't referenced anywhere (격식), no one would know they're there (구어), they're undiscoverable (기술 문어)
- 반의어: they're linked from the main guide

## "I'm leaving out X because …"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 ([assistant] Proposed updates 끝부분)
- 맥락: 제안 범위를 밝히면서 일부러 손대지 않는 부분과 그 이유를 말할 때(회의·리뷰 코멘트)
- 한국어: X는 일부러 뺍니다, 왜냐하면 …
- 설명: 현재진행형 `I'm leaving out` 이 "지금 이 제안에서 빼는 중"이라는 의도를 드러냅니다. 빠뜨린 게 아니라 고른 것이라는 점이 분명해집니다.
- 예문: I'm leaving out the Git Workflow rationale paragraphs because they're long on purpose.
- 유사어: I've deliberately skipped X (의도 강조), X is out of scope here (격식), I'm not touching X (구어)
- 반의어: I'm folding X in as well

## "the only carrier of what we know about X"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md "Office DB knowledge lands in TWO places")
- 맥락: 어떤 산출물이 지식을 담아 나르는 유일한 통로라서 소홀히 하면 안 된다고 강조할 때(설계 문서·격식)
- 한국어: X에 관해 우리가 아는 것을 실어 나르는 유일한 수단
- 설명: `carrier` 는 정보·병원체를 옮기는 매개체입니다. `what we know` 명사절을 목적어로 두어 데이터가 아니라 "지식"을 나른다는 점을 짚습니다.
- 예문: The office databases are unreachable from home, so mock data is the only carrier of what we know about them.
- 유사어: the sole record of (격식, 기록 쪽), the only place that knowledge lives (구어), our single source of truth for (기술 관용)
- 반의어: a throwaway placeholder

## "a fact the next session will contradict"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md, 같은 절)
- 맥락: 한쪽에만 기록된 사실은 결국 다른 쪽에 의해 뒤집힌다고 경고할 때(규칙 문서)
- 한국어: 다음 세션이 거스르게 될 사실
- 설명: `A fact … is a fact …` 반복 구조로 문장을 경구처럼 만듭니다. 미래 `will` 이라 "그럴 수도"가 아니라 "반드시 그렇게 된다"는 단정입니다.
- 예문: A fact recorded in one and not the other is a fact the next home session will contradict.
- 유사어: a fact bound to be overwritten (격식), something the next person will undo without knowing (구어)
- 반의어: a fact that sticks

## "Use judgement"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md Git Workflow)
- 맥락: 규칙을 다 정하지 않고 판단을 맡기되, 바로 뒤 콜론으로 기준을 줄 때(지침·위임)
- 한국어: 알아서 판단해라(다만 기준은 이렇다)
- 설명: 관사 없이 `judgement` 만 씁니다. 영국식 철자이고 미국식은 `judgment` 입니다. 단독으로 쓰면 무책임하게 들리니 이 문장처럼 콜론 뒤에 기준을 붙이는 게 정석입니다.
- 예문: Use judgement: commit at coherent stopping points, not mid-edit.
- 유사어: use your discretion (격식), it's your call (구어), go with your gut (가벼움)
- 반의어: follow the checklist exactly

## "at coherent stopping points, not mid-edit"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md Git Workflow)
- 맥락: 커밋·저장·인계 타이밍을 "의미 있게 끝난 지점"으로 정할 때(개발 지침·구어)
- 한국어: 앞뒤가 맞게 일단락된 지점에서, 편집 도중이 아니라
- 설명: `coherent` 는 "그 자체로 말이 되는". `mid-edit` 은 `mid-` 접두사로 "~하는 도중"을 한 단어로 만듭니다. mid-flight, mid-sentence, mid-refactor 처럼 응용이 넓습니다.
- 예문: Commit at coherent stopping points, like a passing test suite, not mid-edit.
- 유사어: at a natural breakpoint (구어), once the change stands on its own (격식)
- 반의어: halfway through a change

## "hold onto merged branches"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md, worktree 정리 규칙)
- 맥락: 치우지 않은 자원이 필요 없어진 것을 계속 붙잡고 있다고 설명할 때(기술 문서)
- 한국어: 이미 병합된 브랜치를 계속 붙들고 있다
- 설명: `hold onto` 는 놓아야 할 것을 붙잡고 있다는 뉘앙스입니다. 무생물 주어(Leftover worktrees)에 동사 세 개(accumulate, hold onto, mislead)를 나란히 붙여 피해를 쌓아 올립니다.
- 예문: Leftover worktrees accumulate stale checkouts, hold onto merged branches, and mislead the next session about what work is still open.
- 유사어: keep merged branches alive (중립), pin merged branches in place (기술), cling to (감정적)
- 반의어: release, let go of

## "under an unrelated subject line"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md "Never stage broadly")
- 맥락: 엉뚱한 변경이 관계없는 커밋 제목 아래 섞여 들어가는 사고를 설명할 때(Git 규칙)
- 한국어: 관계없는 커밋 제목 아래에(섞여서)
- 설명: `under` 가 "~라는 이름표 아래"를 뜻합니다. under a different name, under the heading of 과 같은 쓰임입니다. 커밋 로그가 오염되는 모습을 구체적으로 보여 줍니다.
- 예문: A broad stage sweeps another session's half-finished edits into your commit under an unrelated subject line.
- 유사어: mislabeled as part of another change (평이), filed under the wrong heading (비유)
- 반의어: in its own commit

## "Wrong bug = wrong fix."
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (diagnosing-bugs 스킬 Phase 2)
- 맥락: 재현한 실패가 사용자가 말한 그 버그인지 먼저 확인하자고 짧게 못 박을 때(구어·체크리스트)
- 한국어: 버그를 잘못 잡으면 고치는 것도 틀린다
- 설명: 등호를 써서 동사 없이 인과를 표현하는 슬로건형 문장입니다. 말할 때는 "If it's the wrong bug, it's the wrong fix."로 풀어 씁니다.
- 예문: Make sure the test fails the way the user described; wrong bug = wrong fix.
- 유사어: garbage in, garbage out (더 일반적), fix the wrong thing and you've fixed nothing (구어)
- 반의어: (마땅한 대체 표현 없음)

## "a different failure that happens to be nearby"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (diagnosing-bugs 스킬 Phase 2)
- 맥락: 근처에서 우연히 난 다른 오류를 진짜 원인으로 착각하지 말라고 할 때(디버깅)
- 한국어: 마침 근처에서 난 다른 실패
- 설명: `happen to + 동사` 는 "우연히 ~하다". 관계절 속에 넣어 그 실패가 원인과 무관하게 위치만 가깝다는 점을 드러냅니다.
- 예문: The loop must produce the failure the user described, not a different failure that happens to be nearby.
- 유사어: an unrelated error in the same area (평이), a red herring (관용, 주의를 흩뜨리는 미끼)
- 반의어: the exact symptom

## "jumping straight to a hypothesis"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (diagnosing-bugs 스킬 Phase 1)
- 맥락: 증거를 모으기 전에 결론부터 세우는 습관을 경계할 때(회의·코칭)
- 한국어: 곧장 가설로 뛰어드는 것
- 설명: `jump straight to` 는 중간 단계를 건너뛴다는 뜻입니다. 동명사구가 주어가 되어 "그 행동 자체가 실패"라고 판정합니다.
- 예문: Jumping straight to a hypothesis is the exact failure this skill prevents.
- 유사어: jumping to conclusions (관용), theorizing before the evidence is in (격식), shooting from the hip (구어)
- 반의어: letting the evidence lead

## "is isolated to X"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (CLAUDE.md Feature-sliced Backend Layout)
- 맥락: 변경·영향 범위가 한 파일이나 모듈 안에 갇혀 있다고 할 때(설계 문서)
- 한국어: (영향이) X 안에만 국한된다
- 설명: `isolate` 의 수동형에 `to` 를 붙이면 "~로 한정되다"가 됩니다. 버그 보고에서도 "The issue is isolated to Safari."처럼 자주 씁니다.
- 예문: Handlers never touch DB drivers directly, so the home↔office swap is isolated to `providers/office.py`.
- 유사어: is confined to (격식), only touches (구어), is scoped to (기술)
- 반의어: leaks into, spreads across

## "measurably falls short"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt d0eba2c5 (ponytail 스킬 Intensity 예시)
- 맥락: 감이 아니라 측정으로 부족함이 드러날 때만 더 큰 해법을 쓰자고 할 때(설계 판단·글)
- 한국어: 측정해 보니 확실히 모자라다
- 설명: `fall short` 는 기대에 못 미치다. 부사 `measurably` 가 "숫자로 확인될 만큼"이라는 조건을 붙여 섣부른 최적화를 막습니다.
- 예문: Skipped the custom cache class; add it when lru_cache measurably falls short.
- 유사어: proves inadequate in practice (격식), actually isn't enough (구어)
- 반의어: holds up, does the job
