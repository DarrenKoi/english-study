# 2026-09-18 — 새 표현

> equipment-data-map 문서 3건과 skewnono Phase 1 계획은 본문이 한국어라 표현을 뽑지 않았다. 18개 가운데 6개는 영어로 쓰인 skewnono Phase B 계획과 계획 속 코드 주석에서, 12개는 transcript 의 `[assistant]` 영어에서 나왔다. 노트에 이미 있는 `funnel through`, `clobber`, `be level with`, `X is the authority for Y`, `predate the diff`, `trace to`, `exercise (a code path)`, `say so`, `One catch: …` 는 뺐다.

## "map the blast radius"
- 레지스터: technical, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 고치기 전에 변경이 어디까지 번지는지 조사 중이라고 중간 보고할 때(작업 채팅·스탠드업)
- 한국어: 영향 범위를 파악하다
- 설명: 원문은 `Still mapping the blast radius`. `blast radius` 는 폭발 반경에서 온 말로 장애나 변경이 닿는 범위를 가리킨다. 동사로 `map` 을 고르면 "아직 지도를 그리는 중"이라 범위가 확정되지 않았다는 뜻까지 실린다. `still` 을 앞에 두면 "시간이 걸리는 이유가 이것"이라는 해명이 된다.
- 예문: I'm still mapping the blast radius of the schema change, so I haven't touched any code yet.
- 유사어: scope out the impact (평이한 회화), assess the impact (격식 있는 보고서), see what else this touches (가장 구어)
- 반의어: a contained change, an isolated fix

## "quietly bring back"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 한쪽만 고치면 나중에 복사·병합 과정에서 옛 버그가 소리 없이 되살아난다고 경고할 때(설계 근거·리뷰)
- 한국어: (고친 문제를) 아무도 모르게 되살리다
- 설명: 원문은 `a later re-copy … would quietly bring back the ZoneInfo import, and Windows would break again`. `quietly` 는 오류도 경고도 없이 일어난다는 버그 어휘고, `bring back` 은 없앤 것을 다시 들여온다는 뜻이다. 가정법 `would` 가 두 번 이어져 "그렇게 하면 → 이렇게 되고 → 결국 또 깨진다"는 연쇄를 그린다.
- 예문: Re-vendoring from the old fork would quietly bring back the bug we fixed last week.
- 유사어: silently reintroduce (문어·격식), regress (한 단어, 테스트 문맥), undo the fix (평이)
- 반의어: fix it for good, keep it fixed

## "let (something) through"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 검사·필터·정책이 막아야 할 것을 통과시킨다고 설명할 때(코드 리뷰·버그 설명)
- 한국어: ~을 그냥 통과시키다
- 설명: 원문은 `the default lenient policy lets the click through`. 주어가 사람이 아니라 정책이다. 관문을 지키는 문지기가 눈감아 주는 그림이라 "허용한다"보다 "막지 않았다"에 가깝다. 목적어는 `let` 과 `through` 사이에 넣는다.
- 예문: The validator lets empty strings through, so the crash only shows up downstream.
- 유사어: wave through (더 무신경한 통과), allow (중립·격식), not catch (놓쳤다는 쪽에 초점)
- 반의어: block, refuse, reject

## "it just adds noise"
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 거슬리는 출력·경고가 실행 결과에는 영향이 없다고 안심시킬 때(구어·채팅)
- 한국어: 시끄럽기만 할 뿐이다
- 설명: 원문은 `Your run isn't affected; it just adds noise and a query at every start`. 먼저 "영향 없다"를 단언하고 세미콜론 뒤에 실제 비용을 작게 적었다. `just` 가 피해의 크기를 줄이고, `noise` 는 로그에서 정보 가치가 없는 줄을 통칭한다.
- 예문: The deprecation warning doesn't break anything; it just adds noise to the build log.
- 유사어: it's harmless clutter (조금 더 가벼움), it's cosmetic (외관 문제일 뿐), it buries the real signal (해가 있다는 쪽으로 기울 때)
- 반의어: it's a real signal, it matters

## "wait for (someone) who isn't coming"
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 시스템이 오지 않을 응답·사람을 기다리며 멈춰 있는 상황을 설명할 때(버그 설명·구어)
- 한국어: 오지도 않을 사람을 기다리다
- 설명: 원문은 `That still sends a cube notification and waits for an engineer who isn't coming`. 현재진행형 `isn't coming` 이 "올 예정이 없다"는 확정된 미래를 나타낸다. 프로그램을 사람처럼 그려서 타임아웃 없는 대기가 왜 문제인지 한 줄로 와닿게 한다.
- 예문: Without a timeout, the worker just waits for a reply that isn't coming.
- 유사어: hang forever (기술적·직설), block indefinitely (문어), wait on nothing (구어)
- 반의어: time out, give up and move on

## "pin the details (someone) had to guess"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 스펙이 모호해 구현자가 임의로 정했던 부분을 문서에 확정해 넣었다고 보고할 때(변경 보고·문어)
- 한국어: 추측에 맡겨졌던 세부를 못 박다
- 설명: 원문은 `I also pinned the details the office LLM had to guess`. `pin` 은 압정으로 고정한다는 동사로, 버전이나 값을 움직이지 못하게 박아 둘 때 쓴다. 뒤의 접촉 관계절 `(that) the office LLM had to guess` 가 "왜 고정해야 했는지"를 설명한다. 같은 대화에서 덜 고정됐다는 뜻으로 `under-pinned` 도 나왔는데, 사전에 있는 `underpin`(떠받치다)과 뜻이 다르니 대화 안에서만 통하는 임시 조어로 본다.
- 예문: I pinned the retry count in the spec so implementers no longer have to guess.
- 유사어: pin down (구동사, 더 흔함), spell out (풀어서 명시하다), nail down (구어, 최종 확정)
- 반의어: leave it open, leave it to interpretation

## "stop assuming X"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-phase-b.md
- 맥락: 코드가 암묵적으로 깔고 있던 전제를 걷어 낸다고 설계 문서에 적을 때(문어·기술)
- 한국어: X 라고 넘겨짚던 것을 그만두다
- 설명: 원문은 `Ranking rows … gain contributing fab_names so their detail links stop assuming fabs[0]`. 주어가 `links` 다. 코드가 "가정한다"고 의인화하면 버그의 원인이 값이 아니라 전제라는 점이 드러난다. `gain` 도 같은 식으로 필드가 새로 생긴다는 뜻이다.
- 예문: Once the API returns the owner, the client can stop assuming the first item is the right one.
- 유사어: no longer hard-code (구현 쪽 표현), drop the assumption that (문어), stop taking X for granted (일반 회화)
- 반의어: bake in the assumption, hard-code

## "orphaned, not migrated"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-phase-b.md
- 맥락: 옛 저장 키·데이터를 옮기지 않고 그냥 버려 둔다는 결정을 제약 목록에 적을 때(설계 문서)
- 한국어: 옮기지 않고 주인 없이 남겨 둔다
- 설명: 원문은 `Old keys are orphaned, not migrated`. `A, not B` 대구로 독자가 기대할 법한 선택(마이그레이션)을 명시적으로 부정한다. `orphaned` 는 참조하는 코드가 사라져 아무도 읽지 않는 상태다. 지우지도 않는다는 뜻이 함께 실린다.
- 예문: The v1 cache entries are orphaned, not migrated, so users will see an empty list once.
- 유사어: left behind (평이), abandoned in place (더 직설), deprecated without a migration path (격식)
- 반의어: migrated, carried over

## "hide behind a fresher sibling"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-phase-b.md
- 맥락: 여러 소스를 합칠 때 나쁜 상태 하나가 좋은 상태에 가려지면 안 된다고 설계 의도를 적을 때(docstring·주석)
- 한국어: 더 최신인 옆 항목 뒤에 숨다
- 설명: 원문은 `so one stale fac makes the merged board stale rather than hiding behind a fresher sibling`. `hide behind` 는 문제가 집계 뒤에 가려지는 현상이고, `sibling` 은 같은 층위의 이웃 항목을 부르는 기술 어휘다. `rather than -ing` 가 택하지 않은 설계를 짧게 보여 준다.
- 예문: A failing shard should turn the whole dashboard red rather than hiding behind its healthy siblings.
- 유사어: get masked by (문어·중립), be averaged away (수치 집계일 때), get lost in the aggregate (평이)
- 반의어: surface, show through

## "worst-of merge"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-phase-b.md
- 맥락: 여러 상태를 합칠 때 가장 나쁜 값을 대표값으로 삼는 규칙에 이름을 붙일 때(설계 문서·docstring)
- 한국어: 최악값 기준 병합
- 설명: 원문은 `Worst-of merge across facilities`. `best-of-three` 처럼 `-of` 복합어를 형용사로 앞에 세웠다. 규칙에 이름이 생기면 뒤 문서에서 `merged_meta worst-of semantics` 식으로 한 단어처럼 다시 부른다.
- 예문: Health status uses a worst-of merge, so one degraded node marks the cluster degraded.
- 유사어: pessimistic merge (같은 뜻, 더 일반적), take the minimum (구현 설명), fail-closed aggregation (안전 쪽에 초점)
- 반의어: best-of merge, optimistic merge

## "drop alone instead of resetting the whole selection"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-selection.md
- 맥락: 검증을 항목 단위로 하는 이유를 주석으로 남길 때(코드 주석)
- 한국어: 전체를 초기화하지 않고 그 하나만 떨어져 나가다
- 설명: 원문은 `Validated per token so one stale entry drops alone instead of resetting the whole selection`. 주어가 생략된 과거분사 `Validated` 로 시작하는 주석체 문장이다. `drop` 은 자동사로 "목록에서 빠지다", `alone` 은 "다른 것을 끌고 가지 않고"다. `instead of -ing` 가 피한 나쁜 결과를 보여 준다.
- 예문: Each row is parsed separately so a malformed line drops alone instead of failing the whole import.
- 유사어: fail in isolation (문어), get skipped individually (평이), degrade gracefully (더 넓은 개념)
- 반의어: all-or-nothing, take everything down with it

## "pass through untouched"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-selection.md
- 맥락: 값이 어떤 계층을 가공 없이 그대로 지나간다고 설명할 때(코드 주석·설계 문서)
- 한국어: 손대지 않은 채로 통과하다
- 설명: 원문은 `it may be a multi-fab list ("r3,m16b"), which passes through untouched so feature switches keep the whole selection`. `untouched` 는 동사 뒤에 붙은 보어로 "통과할 때의 상태"를 말한다. 계획 본문에서는 같은 뜻을 명사로 써서 `pass-through` 라고도 했다.
- 예문: Unknown query params pass through untouched, so existing bookmarks keep working.
- 유사어: is forwarded as-is (격식·명시적), goes straight through (구어), is left alone (더 일반적)
- 반의어: get normalized, get rewritten

## "stage only my hunk"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 같은 파일에 다른 사람 변경이 섞여 있어 내 부분만 골라 커밋한다고 알릴 때(git 작업 보고)
- 한국어: 내 변경 조각만 스테이징하다
- 설명: 원문은 `Another session also changed CLAUDE.md …, so I'll stage only my hunk`. `hunk` 는 diff 에서 연속된 변경 한 덩어리를 부르는 git 용어다(`git add -p` 가 묻는 단위). `only` 가 목적어 바로 앞에 있어 "내 것만"이 정확히 걸린다.
- 예문: The file has someone else's edits too, so I'll stage only my hunk and leave the rest.
- 유사어: commit just my part (평이), do a partial add (구어), cherry-pick my changes (엄밀히는 다른 명령이지만 회화에서 혼용)
- 반의어: stage everything, git add -A

## "lock in (the approved result)"
- 레지스터: professional, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 뒤 단계가 앞 단계의 승인된 결과를 고정해 받아 쓴다고 규칙을 설명할 때(스펙 요약)
- 한국어: (승인된 결과를) 확정해 묶어 두다
- 설명: 원문은 `stages 2, 4 and 5 lock in the approved result of the stage before them`. `lock in` 은 이후에 바뀌지 않게 잠근다는 뜻으로 가격·일정·결정에 두루 쓴다. `the stage before them` 은 `the previous stage` 를 풀어 쓴 평이한 표현이다.
- 예문: Once the plan is approved, the CLI locks in its hash and refuses any later edit.
- 유사어: freeze (더 짧고 기술적), commit to (결정 쪽 어감), bind to (스펙 문체)
- 반의어: leave open, keep flexible

## "pick up the fix"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대 환경이 별도 조치 없이 다음 갱신 때 수정분을 받게 된다고 알릴 때(배포 안내·구어)
- 한국어: 수정분을 (자연히) 받아 가다
- 설명: 원문은 `the office picks up the fix when the engineer copies the repo over`. `pick up` 은 지나가는 길에 집어 든다는 그림이라 "따로 할 일은 없다"가 함축된다. `copy … over` 의 `over` 는 이쪽에서 저쪽으로 건너간다는 방향을 보탠다.
- 예문: You don't need to do anything; the staging server picks up the fix on the next deploy.
- 유사어: get the fix (가장 평이), inherit the fix (상속·의존 관계일 때), the fix rolls out to (배포 주체 쪽 시점)
- 반의어: miss the fix, stay on the old version

## "I read X as Y"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 모호한 지시를 내가 어떻게 해석했는지 먼저 밝히고 작업에 들어갈 때(협업 채팅)
- 한국어: X 를 Y 라는 뜻으로 받아들였다
- 설명: 원문은 `I read "unnecessary files" as whatever my test runs left behind`. 노트에 있는 `read as`(사물 주어, ~처럼 읽히다)와 달리 주어가 사람이고 타동사다. 해석을 공개하면 틀렸을 때 상대가 바로 바로잡는다. `whatever + 절` 이 "~한 것은 무엇이든"으로 범위를 정한다.
- 예문: I read "clean up the branch" as deleting only the merged ones, so I left the rest.
- 유사어: I took X to mean Y (같은 격식), I understood X as Y (조금 딱딱함), I'm assuming you mean Y (진행형, 확인을 구하는 어감)

## "go away with (the new version)"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 새 버전을 받으면 문제가 저절로 없어진다고 안심시킬 때(구어·배포 안내)
- 한국어: ~와 함께 (문제가) 사라지다
- 설명: 원문은 `letter 01's import problem goes away with the new ftp_handler`. 문제를 주어로 두고 `go away` 를 쓰면 누가 고쳤는지보다 "이제 없다"는 결과가 앞선다. `with` 는 조건이자 동반이다.
- 예문: The flicker goes away with the latest driver, so there's nothing to patch on our side.
- 유사어: is resolved by (격식·수동), disappears once you (조건절로 풀기), is fixed in (릴리스 노트 문체)
- 반의어: come back, persist

## "If you'd rather not …, (I can …)"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 내가 한 선택이 마음에 안 들면 되돌릴 길이 있다고 정중히 열어 둘 때(협업 채팅)
- 한국어: 그렇게 하고 싶지 않으시다면 (~해 드릴 수 있다)
- 설명: 원문은 `If you'd rather not keep it in sync, the commit there is local and unpushed, so I can undo it with git revert`. `would rather not + 동사원형` 은 `don't want to` 보다 부드럽게 선호를 묻는다. 뒤에 되돌리는 비용이 작다는 근거(`local and unpushed`)를 붙여 선택을 쉽게 만들었다.
- 예문: If you'd rather not merge today, I can keep the branch open until Monday.
- 유사어: If you'd prefer not to (조금 더 격식), If that's not what you want (평이), Should you prefer otherwise (문어·매우 격식)
