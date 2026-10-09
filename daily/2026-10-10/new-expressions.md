# 2026-10-10 — 새 표현

> 오늘 배치는 repo 문서 4건과 transcript 6건이다. repo 문서 가운데 성과 보고와 조사 보고서 본문은 한국어여서 표현 재료로 쓰지 않았고, 영어로 쓴 조사 노트 두 편(`skewvoir_current_state.md`, `ebeam_pages_current_state.md`)에서 대부분을 골랐다. 코드를 읽고 쓴 현황 조사라 "어디까지 읽었고 무엇은 추론인가"를 밝히는 표현이 많다. transcript 셋은 `/clear` 만 찍힌 빈 세션이다. 나머지에서는 pm-notes 세션에 딸려 온 Artifact 디자인 지침에서 셋을 골랐다. Herdr·browser-verify 스킬 문서는 예전에 다 골라서 건너뛰었다. 노트에 이미 있어서 뺀 것: `load-bearing claims`, `spot-check`, `the single source of truth`, `by construction`, `end to end`, `a throwaway worktree`, `one-for-one`, `less is more`.

## "is dropped on the floor"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 받아 놓고 쓰지 않는 데이터나 처리되지 않고 사라지는 요청을 가리킬 때(기술 문서·리뷰, 구어에 가까움).
- 한국어: (받아 놓고) 그냥 버려진다
- 설명: 바닥에 떨어뜨린다는 그림 그대로다. 일부러 지운 것이 아니라 아무도 받지 않아 사라진다는 느낌이 있다. 네트워크에서는 패킷이나 메시지가 조용히 유실될 때도 쓴다. 수동태로 쓰면 누가 버렸는지 따지지 않고 사실만 전한다.
- 예문: A meaningful amount of already-delivered data is dropped on the floor.
- 유사어: goes unused (평이·중립), is discarded (격식, 의도적으로 버림), falls through the cracks (구어, 틈새로 빠져 놓침)
- 반의어: is put to use (활용된다)

## "the owner's direction of travel"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 개별 결정을 모아 보면 드러나는 큰 방향을 말할 때(보고서·회의, 격식. 영국식 비즈니스 영어에서 흔함).
- 한국어: (결정들이 가리키는) 나아가는 방향
- 설명: `direction` 하나만 써도 되는데 `of travel` 을 붙이면 "아직 도착하지는 않았고 그쪽으로 움직이는 중"이라는 뜻이 살아난다. 확정된 계획이 아니라 승인·거절 이력에서 읽어 낸 경향을 말할 때 알맞다.
- 예문: The owner's direction of travel is clear from what was accepted vs rejected.
- 유사어: where this is heading (구어), the overall trajectory (격식·분석적), the general thrust (문어, 논지의 방향)

## "is stale against the code"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 문서나 캐시가 코드보다 뒤처져 믿을 수 없다고 경고할 때(코드 리뷰·조사 노트).
- 한국어: 코드에 비해 낡았다(코드와 안 맞는다)
- 설명: `stale` 은 빵이 굳었다는 말에서 온 "갱신 안 된". 전치사 `against` 가 비교 기준을 세운다. `out of date` 보다 "무엇과 견줘 낡았는지"가 또렷하다. 원문은 이 뒤에 `so it should not be used as a source` 를 붙여 결론까지 한 문장에 담았다.
- 예문: The API contract file is stale against the code, so it should not be used as a source.
- 유사어: is out of sync with the code (평이), has drifted from the code (서서히 어긋남), lags behind the implementation (격식)
- 반의어: is up to date with the code (코드와 맞는다)

## "thinner than their single-scope twins"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 짝을 이루는 두 화면·기능 가운데 한쪽이 덜 만들어졌다고 비교할 때(설계 리뷰, 문어).
- 한국어: 단일 범위 쪽 짝보다 내용이 얇다
- 설명: `thin` 은 기능이나 근거가 빈약하다는 뜻으로 자주 쓴다(`a thin wrapper`, `thin evidence`). `twin` 은 같은 틀을 나눠 쓰는 대응물을 가리키는 비유여서 `counterpart` 보다 "원래 같은 모양이어야 한다"는 기대가 실린다.
- 예문: The set-scope views are thinner than their single-scope twins.
- 유사어: less developed than their counterparts (격식), not as fleshed out (구어), lag behind the single-scope versions (평이)
- 반의어: on par with (동등한 수준이다)

## "silent limits"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 사용자에게 알리지 않고 걸리는 상한(잘림·만료)을 UX 문제로 분류할 때(리뷰 소제목·이슈 제목).
- 한국어: 말없이 걸리는 제한
- 설명: `silent` 는 오류도 안내도 없이 일어난다는 뜻으로 `silent failure`, `silently truncated` 처럼 붙는다. 원문은 30건 상한, 60일 검색 창, 61일 보관 기한을 이 제목 아래 묶었다. 형용사 하나로 "제한이 있다"가 아니라 "제한을 알려 주지 않는다"가 문제임을 짚는다.
- 예문: The 30-member cap is one of several silent limits in the workspace.
- 유사어: undisclosed caps (격식), hidden cutoffs (평이), limits the UI never mentions (풀어 쓴 구어)
- 반의어: an explicit limit with a warning (경고가 붙은 명시적 제한)

## "cannot be judged from code"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 조사 방법의 한계 때문에 답할 수 없는 질문을 `Gaps` 로 남길 때(조사 보고, 격식).
- 한국어: 코드만 봐서는 판단할 수 없다
- 설명: `judge A from B` 는 "B 를 근거로 A 를 판단한다". 수동태로 뒤집어 판단 주체를 지우고 "이 자료로는 안 된다"만 남겼다. 주어 자리에 `Whether …` 절이 오는 꼴이 많다.
- 예문: Whether the radial approach matches what engineers actually look for cannot be judged from code.
- 유사어: the code alone can't tell us (구어), is not determinable from the source (격식), you'd have to ask the users (평이, 대안 제시)

## "Anything under "Inferences" is inference, not fact."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 보고서 머리에서 사실 절과 추론 절을 가르는 읽는 법을 알려 줄 때(조사 노트·감사 보고, 격식).
- 한국어: "추론" 아래 적힌 것은 모두 추론이지 사실이 아니다
- 설명: `Anything under X` 로 절 제목 아래의 모든 항목을 한꺼번에 받는다. `A, not B` 로 등급을 못 박는 짧은 문장이다. 독자가 뒤에서 어느 줄을 인용하든 근거 수준을 헷갈리지 않게 한다.
- 예문: Anything under "Inferences" is inference, not fact.
- 유사어: Items in that section are my reading, not verified findings (풀어 씀), Treat that section as conjecture (격식), Take those with a grain of salt (구어)

## "were grepped, not read in full"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 파일을 검색으로만 훑었고 통독하지는 않았다고 조사 깊이를 밝힐 때(코드 조사 보고).
- 한국어: grep 으로만 봤고 끝까지 읽지는 않았다
- 설명: 도구 이름 `grep` 을 동사로 쓰고 과거분사 `grepped` 로 수동태를 만들었다. `in full` 은 "전부, 빠짐없이"(`paid in full`, `quoted in full`). 두 과거분사를 `, not` 으로 맞세워 한 일과 안 한 일을 한 줄에 적는다.
- 예문: `DistributionChart.vue` and `SequenceTrend.vue` were grepped, not read in full.
- 유사어: I only skimmed those files (구어), were searched but not reviewed line by line (격식), I didn't read them end to end (평이)
- 반의어: were read in full (통독했다)

## "X is in; Y is out"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 범위에 넣을 것과 뺄 것을 한 문장으로 가를 때(스코프 정리·회의 요약).
- 한국어: X 는 범위 안, Y 는 범위 밖
- 설명: 부사 `in`/`out` 이 보어로 쓰여 "채택됐다/제외됐다"를 뜻한다. 원문은 주어가 길다. 앞은 `comparisons the user defines by hand and labels as exploratory`, 뒤는 `anything that reads as an official verdict` 이고 `until an office contract exists` 로 제외가 풀리는 조건을 붙였다. 긴 주어 뒤에 한 음절 보어가 와서 끝이 단단하다.
- 예문: Comparisons the user defines by hand are in; anything that reads as an official verdict is out until an office contract exists.
- 유사어: is in scope / is out of scope (격식·문서), made the cut / didn't make the cut (구어), is on the table / is off the table (협상·회의)

## "reads as an official verdict"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/skewvoir_current_state.md
- 맥락: 글이나 화면이 독자에게 어떤 인상으로 받아들여지는지 말할 때(문구 검토·UX 리뷰).
- 한국어: 공식 판정처럼 읽힌다
- 설명: `read as` 는 주어가 글·화면이고 "~로 읽힌다"는 자동사다. 실제로 그런지와 상관없이 받는 쪽 인상을 말하므로 문구를 고칠 때 근거로 쓰기 좋다. `sound like` 는 말소리, `look like` 는 겉모습, `read as` 는 글의 인상.
- 예문: Anything that reads as an official verdict is out until an office contract exists.
- 유사어: comes across as (구어, 사람·말에도), could be taken as (조심스러운 가능성), gives the impression of (격식)

## "Where a claim rests on a grep rather than a full read it says so."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 보고서가 근거 약한 대목을 스스로 표시한다고 방법 주석에서 약속할 때(조사 보고, 격식).
- 한국어: 주장이 통독이 아니라 grep 에 기대는 곳에서는 그렇다고 적어 둔다
- 설명: 문두의 `Where` 는 장소가 아니라 "~인 경우에는"을 뜻하는 접속사로 규정·계약 문체에 흔하다. `rest on` 은 "~에 근거를 둔다". 뒤의 `it says so` 에서 `it` 은 그 주장(문서)이고 `so` 가 앞 절 내용을 받는다.
- 예문: Where a claim rests on a grep rather than a full read it says so.
- 유사어: Claims based only on search results are marked as such (격식), I flag anything I only grepped (구어), Unverified statements are labelled (평이)

## "not proofs of absence"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 검색에 안 걸렸다고 없는 것은 아니라고 선을 그을 때(조사 한계 서술).
- 한국어: 없다는 증명은 아니다
- 설명: "Absence of evidence is not evidence of absence" 라는 격언을 줄인 말이다. 원문은 표의 N 칸을 `"not found by the grep patterns used"` 로 다시 정의하고 이 구를 붙였다. 찾는 방법의 한계와 대상의 부재를 가르는 표현.
- 예문: The cells marked N mean "not found by the grep patterns used"; they are not proofs of absence.
- 유사어: doesn't mean it isn't there (구어), a null result, not a negative finding (연구 문체), I can't rule it out (평이)

## "lean on X for Y"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 한 모듈이 다른 모듈의 데이터에 기대고 있다고 의존 관계를 설명할 때(아키텍처 설명, 구어에 가까움).
- 한국어: Y 를 X 에 기대다
- 설명: `depend on` 과 뜻은 같고 몸을 기댄다는 그림이 남아 있어 "자기 것을 따로 두지 않고 빌려 쓴다"는 어감이 난다. 사람 사이에서는 "의지하다"(`lean on a friend`).
- 예문: pm_planning, storage and tttm lean on sem_list for their roster.
- 유사어: depend on X for Y (중립), piggyback on X (구어, 얹혀 간다), draw Y from X (격식)
- 반의어: keep their own copy of Y (자체 사본을 둔다)

## "the connective tissue between pages"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 부품 자체가 아니라 부품을 잇는 링크·규약을 가리킬 때(설계 문서·에세이, 문어).
- 한국어: 페이지 사이를 잇는 결합 조직(연결 고리)
- 설명: 해부학의 결합 조직에서 온 비유다. 눈에 띄지는 않지만 없으면 전체가 따로 논다는 뜻을 담는다. 조직·문서·코드 어디에나 쓰고 `glue` 보다 격식이 높다.
- 예문: The connective tissue between pages today is recipe-centric and MSR-centric.
- 유사어: the glue between pages (구어), the links that tie pages together (평이), the integration layer (기술·격식)

## "link dead-ends in both directions"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 들어오는 링크도 나가는 링크도 없는 화면을 가리킬 때(내비게이션 분석).
- 한국어: 양방향 모두 링크가 끊긴 막다른 곳
- 설명: `dead end` 는 막다른 길. 명사 앞에 `link` 를 붙여 무엇이 막혔는지 밝혔고 `in both directions` 로 들어오는 쪽과 나가는 쪽을 한꺼번에 말했다. 논의나 조사가 더 나아가지 못할 때도 `hit a dead end` 라고 한다.
- 예문: TTTM, 라이브 알람, 스토리지 and 디바이스 통계 are link dead-ends in both directions under the current policy.
- 유사어: isolated pages (격식), islands (비유·구어), nothing links in or out (풀어 씀)

## "spend its novelty elsewhere"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 이미 준비된 일을 새 제안처럼 포장하지 말고 새로운 내용은 다른 데 쓰라고 조언할 때(보고서 작성 지침, 문어).
- 한국어: 새로움은 다른 곳에 쓰다
- 설명: `spend` 의 목적어로 돈·시간이 아니라 `novelty` 를 둔 표현이다. 보고서가 내놓을 수 있는 새 제안의 양이 한정된 예산이라는 발상이 깔려 있다. `spend your effort on`, `spend political capital` 과 같은 틀.
- 예문: A final report should present them as an existing backlog and spend its novelty elsewhere.
- 유사어: save the new ideas for other areas (평이), focus its originality elsewhere (격식), don't waste fresh proposals on settled items (풀어 씀)

## "The rejections cluster around three reasons"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 흩어진 사례를 몇 가지 원인으로 묶어 정리할 때(분석 보고, 격식).
- 한국어: 거절 사유는 세 가지로 모인다
- 설명: `cluster around` 는 점들이 몇 군데에 뭉친다는 통계 용어에서 온 동사구다. `There are three reasons` 는 처음부터 셋이라고 단정하는 말이고 이쪽은 여러 건을 살펴보니 셋으로 묶이더라는 귀납의 느낌이 있다. 대시를 긋고 세 가지를 나열하는 흐름이 뒤따른다.
- 예문: The rejections cluster around three reasons — new collection state, cross-feature coupling in one component, and claims the data cannot support.
- 유사어: fall into three groups (평이), boil down to three reasons (구어), can be grouped under three headings (격식)

## "noted for completeness"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 범위 밖이지만 빠뜨리지 않으려고 한 줄 적어 둘 때(보고서 소제목·각주).
- 한국어: 빠짐없이 적으려고 덧붙임
- 설명: `for completeness` 는 "핵심은 아니지만 목록을 온전히 하려고"라는 단서다. 원문은 소제목 뒤에 `— outside the listed features, noted for completeness` 로 붙였다. 독자에게 이 대목은 건너뛰어도 된다는 신호를 준다.
- 예문: The Mag/Pixel guide is outside the listed features and is noted for completeness.
- 유사어: mentioned for the record (격식, 기록 목적), just so it's covered (구어), included for reference (평이)

## "must not be re-proposed without new grounds"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 이미 거절된 안을 다시 꺼내려면 새 근거가 있어야 한다고 못 박을 때(의사결정 기록, 격식).
- 한국어: 새 근거 없이 다시 제안해서는 안 된다
- 설명: `grounds` 는 복수로 써서 "근거·사유"(`on what grounds?`, `grounds for appeal`). `re-propose` 는 하이픈으로 "다시 제안하다"를 만들었다. `must not` 은 금지이고 `don't have to`(필요 없다)와 뜻이 다르다.
- 예문: A long explicit "do not build" list exists and must not be re-proposed without new grounds.
- 유사어: shouldn't be reopened unless something changes (구어), is closed absent new evidence (법률·격식), don't bring it up again without a reason (평이)

## "are taken second-hand"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 원문을 직접 읽지 않고 다른 문서의 인용을 거쳐 얻은 정보라고 밝힐 때(조사 한계, 격식).
- 한국어: 직접 본 것이 아니라 건너 들은 것이다
- 설명: `second-hand` 는 중고라는 뜻 말고 "남을 거쳐 얻은"이라는 뜻이 있다(`second-hand information`). 여기서는 부사처럼 쓰여 `take`(받아들이다) 방식을 꾸민다. 원문에서는 디자인 문서를 읽지 않았고 그 문서를 인용한 ADR 에서 제약을 옮겼다는 고백이다.
- 예문: The visual-language constraints are taken second-hand from references in another document.
- 유사어: come from a secondary source (격식), I got that indirectly (구어), are quoted from someone else's summary (풀어 씀)
- 반의어: first-hand (직접 확인한)

## "an unsourced assertion"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 출처 없이 적힌 단언을 근거로 쓰기 어렵다고 지적할 때(문헌 검토·리뷰).
- 한국어: 출처 없는 단언
- 설명: `assertion` 은 근거를 대지 않고 내세운 말이라는 어감이 `claim` 보다 짙다. `unsourced` 가 붙으면 "틀렸다"가 아니라 "확인할 길이 없다"는 평가가 된다. 위키 편집에서 `[citation needed]` 가 붙는 문장이 이것이다.
- 예문: The only usage-related statement about engineers found in the docs is an unsourced assertion.
- 유사어: an unsupported claim (근거 부족), hearsay (전해 들은 말, 구어·법률), an anecdotal remark (일화 수준)
- 반의어: a documented fact (기록으로 확인된 사실)

## "the cheapest available evidence"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 가장 적은 비용으로 얻는 근거부터 확인하자고 권할 때(우선순위 논의).
- 한국어: 지금 구할 수 있는 가장 값싼 근거
- 설명: `cheap` 은 돈만이 아니라 드는 수고가 적다는 뜻으로 엔지니어링 글에 자주 나온다(`a cheap check`). 원문은 뒤에 `and requires no code change` 를 붙여 왜 싼지를 댄다.
- 예문: Reading those numbers there is the cheapest available evidence for prioritising pages and requires no code change.
- 유사어: the lowest-effort way to find out (구어), the most readily available evidence (격식), a quick win (구어·성과 쪽)
- 반의어: evidence that needs a full study (본격 조사가 필요한 근거)

## "cannot be created retroactively"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 지금부터 쌓지 않으면 나중에 만들 수 없는 이력 데이터를 두고 말할 때(수집 설계 논의).
- 한국어: 소급해서 만들 수는 없다
- 설명: `retroactively` 는 "과거 시점으로 거슬러 적용하여". 법률(`apply retroactively`)과 데이터(`backfill retroactively`) 양쪽에서 쓴다. 원문 주어는 `history` 이고 수집을 미루면 그 기간이 영영 빈다는 경고다.
- 예문: The brainstorm itself notes that history cannot be created retroactively.
- 유사어: can't be backfilled (기술·구어), can't be reconstructed after the fact (격식), you can't go back and collect it (평이)

## "rides in the beacon URL"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 값이 별도 필드가 아니라 기존 통로에 실려 간다고 설명할 때(API·로깅 설계).
- 한국어: 비콘 URL 에 실려 간다
- 설명: `ride in/on` 은 탈것에 타고 간다는 말이라 "새 자리를 만들지 않고 얹혀 간다"는 뜻이 된다. 원문은 `and no index field was added` 로 이어져 스키마를 건드리지 않았다는 점을 밝힌다.
- 예문: The tool family rides in the beacon URL and no index field was added.
- 유사어: is carried in the URL (중립), piggybacks on the request (구어), is encoded in the path (기술·격식)

## "fell off before triage finished"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md
- 맥락: 표시 창이 짧아 항목이 처리 전에 화면에서 사라졌다고 원인을 설명할 때(변경 이유 주석).
- 한국어: 분류·대응이 끝나기 전에 (목록에서) 떨어져 나갔다
- 설명: `fall off` 는 목록이나 창의 끝으로 밀려 빠진다는 뜻(`fall off the first page`). `triage` 는 응급실 분류에서 온 말로 들어온 문제의 급한 순서를 가리는 일이다. 원문은 창을 10분에서 20분으로 넓힌 이유를 `because alarms fell off before triage finished` 로 적었다.
- 예문: The window was widened from 10 to 20 minutes because alarms fell off before triage finished.
- 유사어: scrolled out of view (화면 기준), expired too early (만료 기준), aged out of the window (기술·격식)

## "designing is a given"
- 레지스터: conversational, professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 Artifact 디자인 지침)
- 맥락: 할지 말지는 논의 대상이 아니고 어떻게 할지만 정하면 된다고 전제를 깔 때(지침·회의).
- 한국어: 디자인을 한다는 것은 당연한 전제다
- 설명: `a given` 은 과거분사가 명사로 굳은 말로 "따질 필요 없이 주어진 조건"이다. 수학의 `given that` 과 뿌리가 같다. 원문은 `Decide the treatment; designing is a given.` 으로 세미콜론 앞에서 정할 것을, 뒤에서 정할 필요 없는 것을 말한다.
- 예문: Decide the treatment; designing is a given.
- 유사어: goes without saying (구어), is non-negotiable (격식, 협상 불가), is taken for granted (당연시된다, 때로 부정적)
- 반의어: is up for debate (논의 대상이다)

## "used with restraint"
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 Artifact 디자인 지침)
- 맥락: 개성 강한 요소를 아껴 쓰라고 권할 때(디자인·글쓰기 지침, 문어).
- 한국어: 절제해서 쓴
- 설명: `with restraint` 는 "자제하며". `with + 추상명사` 가 부사 노릇을 한다(`with care`, `with confidence`). 원문은 `a characterful display face used with restraint` 로 개성 있는 제목 서체는 조금만 쓰라는 뜻이다. `sparingly` 한 단어로 바꿔도 된다.
- 예문: Pick a characterful display face, but make sure it is used with restraint.
- 유사어: sparingly (한 단어, 중립), in moderation (양을 줄여), in small doses (구어)
- 반의어: liberally (아낌없이), to excess (지나치게)

## "by choice, never by omission"
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 Artifact 디자인 지침)
- 맥락: 무언가를 뺐다면 깜빡한 것이 아니라 결정한 결과여야 한다고 요구할 때(설계 원칙, 격식).
- 한국어: 빠뜨려서가 아니라 선택해서
- 설명: `by choice` 와 `by omission` 을 같은 전치사로 맞세웠다. `omission` 은 해야 할 것을 안 함(법률의 `sin of omission`, 부작위). 원문은 단일 테마로 가는 디자인을 두고 `do this by choice, never by omission` 이라 했다. 결과가 같아도 과정이 다르면 다른 일이라는 말.
- 예문: A page may stay single-theme, but do this by choice, never by omission.
- 유사어: on purpose, not by accident (구어), deliberately rather than by default (격식), as a decision, not an oversight (평이)
