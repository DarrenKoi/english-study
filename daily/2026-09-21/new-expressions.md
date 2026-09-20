# 2026-09-21 — 새 표현

> repo 문서 2건(equipment-data-map 성능 개선안, skewnono chat→RAG 계약 편지)은 본문이 한국어라 표현을 뽑지 않았다. 23개 모두 transcript 의 어시스턴트 영어에서 나왔다(skewnono 16, equipment-data-map 6, auto-recipe-creator 1). 노트에 이미 있는 `rule out`, `in flight`, `tear down`, `on purpose`, `fold in`, `verbatim`, `on demand`, `say so`, `One catch: …`, `that is a one-line change in X`, `moved under me`, `a job that has been rotting` 은 뺐다. 세션에 주입된 herdr·tdd·writing-for-agents 스킬 본문도 앞선 날에 다룬 글이라 건너뛰었다.

## "pull (something) together"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 흩어진 자료를 모아 한 덩어리로 정리해 두었다고 중간 보고할 때(업무 채팅·메일)
- 한국어: (자료를) 한데 끌어모아 정리하다
- 설명: 원문은 `I've pulled the update history together, but I haven't built the UI yet.` `collect` 가 모으는 데서 끝난다면 `pull together` 는 여기저기서 끌어와 쓸 만한 꼴로 묶는 데까지 간다. 목적어가 사이에 끼는 분리형이라 대명사면 반드시 가운데 둔다(`pull it together`). 사람에게 `Pull yourself together` 라고 하면 "정신 차려"라는 전혀 다른 말이 된다.
- 예문: I've pulled the incident timeline together from Slack and the deploy logs, and it's in the shared doc.
- 유사어: put together (가장 평이, 새로 만든다는 어감), compile (격식, 목록·보고서), gather up (구어, 모으기만 한다)
- 반의어: leave scattered across (several places)

## "hand (something) back to you"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 내 선에서 끝낼 수 없는 부분을 상대에게 돌려주겠다고 미리 알릴 때(작업 중간 안내)
- 한국어: 그 부분은 당신에게 다시 넘기다
- 설명: 원문은 `The design import is blocked on authorization, so I'll hand that part back to you at the end.` `hand off` 가 다음 사람에게 넘기는 것이라면 `hand back` 은 원래 주인에게 되돌려 준다. 막힌 이유(`blocked on authorization`)를 앞에 대고 `so` 로 이으니 책임을 떠넘기는 말로 들리지 않는다. `at the end` 로 돌려줄 시점까지 알렸다.
- 예문: I can draft the migration, but the production credentials are yours, so I'll hand the final run back to you.
- 유사어: leave that part to you (평이), pass it back to you (구어), return it to you for action (격식 메일)
- 반의어: take it off your hands

## "in shorthand"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 지금 보여 주는 초안이 줄여 쓴 메모체라고 양해를 구할 때(초안 공유)
- 한국어: 줄여 쓴 메모체로
- 설명: 원문은 `The draft lists changes in shorthand. When I add them to notices.ts I'll write them as full sentences in the same polite style as the 09-18 entry.` `shorthand` 는 원래 속기술이다. 남에게 보이기 전 단계의 약식 표기를 가리킬 때 쓴다. `X is shorthand for Y`(X 는 Y 를 줄여 부르는 말) 틀도 흔하다.
- 예문: My notes are in shorthand, so let me write them up properly before I share them with the team.
- 유사어: in note form (영국식, 평이), in abbreviated form (격식), as rough notes (구어)
- 반의어: in full sentences

## "Say if you want that gone too."
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 일부러 남겨 둔 것을 알리면서 원하면 그것도 지우겠다고 가볍게 제안할 때(채팅)
- 한국어: 그것도 없애길 원하면 말해 주세요
- 설명: `Say if …` 는 `Let me know if …` 보다 더 짧은 구어형이다. `want + 목적어 + gone` 은 `want it to be gone` 을 줄인 꼴로, 목적어 뒤에 원하는 상태를 바로 붙인다(`want it fixed`, `want it done by Friday`). 원문은 "데이터 반출 금지" 카드는 공지가 아니라서 건드리지 않았다고 밝힌 뒤 이 문장으로 닫았다.
- 예문: I kept the old export button for now. Say if you want that gone too.
- 유사어: Let me know if you'd like that removed as well (정중), Just say the word and I'll drop it too (구어), Should you wish it removed, please advise (격식 메일)

## "(X) is the whole change"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 조사해 보니 고칠 곳이 한 군데뿐이라고 작업 범위를 못 박을 때(착수 전 보고·PR 설명)
- 한국어: ~하는 것이 변경의 전부다
- 설명: 원문은 `So emptying the JSON is the whole change.` 앞 문장에서 fixture 와 문서를 확인한 근거를 대고 `So` 로 결론을 냈다. 동명사 주어(`emptying the JSON`)와 `the whole + 명사`("그게 전부")의 조합이다. 작은 변경임을 강조해 상대를 안심시키는 효과가 있다.
- 예문: The flag is only read in one place, so flipping its default is the whole change.
- 유사어: that's all there is to it (구어), the change is limited to X (격식), nothing else needs touching (평이)
- 반의어: that's only the first step

## "be due to (expire)"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 일정상 ~하기로 되어 있다고 말할 때(공지·일정 안내, 중립~격식)
- 한국어: ~할 예정이다
- 설명: 원문은 `(was due to expire 9/30)`. `due to + 동사원형` 은 예정이고 `due to + 명사` 는 원인("~때문에")이다. 모양이 같아서 헷갈리는데 뒤에 동사가 오면 예정으로 읽으면 된다. 과거형 `was due to` 는 "그럴 예정이었는데 그 전에 다른 일이 생겼다"는 어감. 여기서는 만료일 전에 공지를 내렸다.
- 예문: The certificate is due to expire next month, so let's renew it this week.
- 유사어: be set to (뉴스·보고체), be scheduled to (격식, 일정표에 올라 있음), be supposed to (구어, 어긋날지도 모른다는 어감)

## "hand-rolled"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 공용 유틸이나 라이브러리가 있는데도 직접 짠 구현을 가리킬 때(코드 리뷰·설계 설명)
- 한국어: 손수 짠, 자체 구현한
- 설명: 원문은 `The composable goes through usePersistedState, as CLAUDE.md requires, so there's no hand-rolled localStorage`. 담배를 손으로 말아 피우는 데서 온 말이다. 기성품을 두고 굳이 직접 만들었다는 가벼운 부정이 깔려 있고 `roll your own` 과 뿌리가 같다.
- 예문: We replaced the hand-rolled retry loop with the library's built-in backoff.
- 유사어: homegrown (중립, 사내에서 만든), roll-your-own (구어), bespoke (영국식, 맞춤 제작이라는 긍정적 어감)
- 반의어: off-the-shelf, built-in

## "throwaway"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 쓰고 버릴 작정으로 만든 브랜치·스크립트·프로토타입을 가리킬 때(개발 대화)
- 한국어: 쓰고 버릴, 일회용
- 설명: 원문은 `This change spans about 8 files, so per the repo rules I'm doing it in a throwaway worktree.` 동사 `throw away` 가 한 단어 형용사로 굳어 명사 앞에 온다(`a throwaway script / branch / account`). 품질을 따지지 말라는 신호로도 쓴다.
- 예문: I wrote a throwaway script to backfill the column, so don't bother reviewing its style.
- 유사어: disposable (중립·격식), scratch (개발 구어, `a scratch branch`), one-off (한 번 쓰고 끝, 버린다는 어감은 약함)
- 반의어: long-lived, permanent

## "give (it) a moment"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 재시작·빌드·캐시가 자리 잡을 때까지 잠깐 기다리겠다고 할 때(작업 중계)
- 한국어: 잠깐 시간을 주다
- 설명: 원문은 `I'll give the restart a moment and re-run the full flow in the browser`. 사물에게 시간을 "준다"고 말하는 것이 영어답다. `give it a minute`, `give it a second` 도 같은 틀이다. 한국어 "좀 기다렸다가"를 `wait` 없이 옮길 때 쓸모가 있다.
- 예문: The cache takes a while to warm up, so give it a moment before you run the benchmark.
- 유사어: wait a bit for it (평이), let it settle (기술 구어), allow some time for (격식)

## "Point by point:"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 상대가 한꺼번에 던진 여러 항목에 하나씩 답하겠다고 예고할 때(메일·리뷰 답글)
- 한국어: 항목별로 보면:
- 설명: 원문은 `Your answers are recorded as a postscript on the letter and pushed as 701298a0. Point by point:` 뒤에 굵은 소제목 여섯 개가 사용자 메시지의 문장 순서대로 이어진다. 결과를 한 줄로 먼저 말하고 이 말로 넘어가면 긴 답도 길을 잃지 않는다. `step by step`, `line by line` 과 같은 `A by A` 틀이다.
- 예문: Thanks for the detailed review. Point by point: the naming is fixed, the test is added, and I disagree on the third item.
- 유사어: Taking these in turn (격식), One by one (구어), To address each in order (격식 문어)
- 반의어: In short, Overall

## "go live"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 기능·서비스가 실사용자에게 열리는 시점을 말할 때(배포 계획·공지)
- 한국어: 실서비스에 올라가다, 공개되다
- 설명: 원문은 `that chat-side step has to land before the tools go live`. 같은 메시지에 `since the service is live` 처럼 형용사 `live` 도 나온다. 다른 세션에는 `It goes live with that deploy` 가 있다. `launch` 와 달리 주어가 사람이 아니라 기능인 점도 봐 두자. `land`(코드가 main 에 들어가다)와 `go live`(사용자에게 열리다)를 한 문장에서 구별해 쓴 것도 눈여겨볼 만하다.
- 예문: The new billing page goes live on Monday, so the copy has to be final by Friday.
- 유사어: launch (제품 단위, 주어가 주로 사람·회사), ship (개발 구어), be rolled out (격식, 단계적 배포)
- 반의어: be taken offline, be pulled

## "that is the discussion to have then"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 지금 결정하지 않고 조건이 닥쳤을 때 논의하자고 선을 그을 때(설계 논의·회의)
- 한국어: 그건 그때 가서 할 논의다
- 설명: 원문은 `If real reports need more, a separate "report turn" budget is the discussion to have then, not a raise today.` `the discussion to have` 는 to부정사가 명사를 뒤에서 꾸미는 꼴("해야 할 논의")로, `have a discussion` 의 목적어가 앞으로 나왔다. `then` 과 `today` 가 짝을 이루고 `A, not B` 틀로 지금은 올리지 않는다는 결론을 분명히 했다.
- 예문: If traffic doubles, sharding is the discussion to have then, not something to build now.
- 유사어: we'll cross that bridge when we come to it (관용, 구어), let's revisit it when the need arises (격식), that's a problem for later (캐주얼)
- 반의어: let's settle it now

## "one-for-one"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 새 도구가 옛 도구의 역할을 빠짐없이 그대로 대신했다고 말할 때(도구 교체 보고)
- 한국어: 하나를 하나로, 그대로 맞바꿔
- 설명: 원문은 `Agent-browser replaced the Playwright run one-for-one on the same check`. `one-to-one` 은 1:1 대응 관계를 말하고 `one-for-one` 은 교환·대체를 말한다. 전치사 `for` 에 "~의 대가로, ~대신"이라는 뜻이 살아 있다. 부사 자리에 그대로 쓴다.
- 예문: The new SDK replaces the old client one-for-one, so none of the call sites need to change.
- 유사어: like for like (영국식, 동급 교체), as a drop-in replacement (개발 관용), one-to-one (대응 관계를 말할 때, 교체의 뜻은 약함)

## "scrub (the URL)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 쓸모를 다했거나 남으면 곤란한 정보를 지워 없앤다고 할 때(보안·상태 관리 설명)
- 한국어: (흔적을) 말끔히 지우다
- 설명: 원문은 `Apply-once, then scrub the URL.` 검색 페이지가 쿼리 파라미터를 한 번 적용한 뒤 `router.replace` 로 주소에서 지운다는 설명이다. 솔로 문질러 닦는 그림이라 `remove` 보다 "남김없이"라는 어감이 짙다. 로그에서 개인 정보를 지울 때도 `scrub PII from the logs` 라고 한다.
- 예문: After reading the token from the query string, the page scrubs it from the URL so it never ends up in a screenshot.
- 유사어: strip (떼어 낸다, 가장 흔함), sanitize (위험 요소 제거, 보안 맥락), redact (문서에서 가린다, 격식)

## "Append, never interleave."
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 기존 데이터 순서를 건드리지 않으려고 새 것은 뒤에만 붙인다는 원칙을 말할 때(데이터·fixture 설계)
- 한국어: 뒤에 붙여라, 사이에 끼워 넣지 마라
- 설명: `interleave` 는 두 흐름을 번갈아 끼워 넣는 동작이다. 원문은 시드 고정 난수로 만든 mock 600행을 그대로 두고 새 블록을 별도 시드로 뒤에 붙인 이유를 설명한다. 뒤따르는 문장은 `so not one existing value moved`. 명령문 둘을 쉼표로 이은 표어체라 원칙을 한 줄로 남길 때 흉내 내기 좋다.
- 예문: Log lines from the two workers interleave, so add a worker id before you try to read them.
- 유사어: intersperse (격식, 띄엄띄엄 섞다), weave in (비유적, 글·이야기), alternate (번갈아 나오다)
- 반의어: append, keep in separate blocks

## "legitimately empty"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 빈 결과가 버그가 아니라 데이터 사정상 맞는 결과라고 설명할 때(검증 보고)
- 한국어: 정당하게 비어 있는
- 설명: 원문은 `the mock recipe-search catalogue has no meas_hist rows, so the result list there is legitimately empty at home`. 검증 보고에서 빈 목록은 실패로 읽히기 쉽다. `legitimately` 한 단어가 "비어 있는 게 맞다"는 판단을 실어 준다. 이유를 앞에 대고 `so` 로 이은 것도 같은 목적이다.
- 예문: The report is legitimately empty for new accounts, so show a hint instead of an error.
- 유사어: genuinely (가짜가 아니라 정말로), rightly (판단이 옳다, 격식), as expected (예상대로, 평이)
- 반의어: spuriously, by mistake

## "spell out"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 암묵적으로 넘어간 조건을 문서에 빠짐없이 명시하라고 요구할 때(설계 리뷰)
- 한국어: 하나하나 명시하다
- 설명: 원문은 `v2 must spell out its own set of reuse-key inputs.` 철자를 한 글자씩 불러 주듯 빠짐없이 적으라는 말이다. 리뷰에서 "정의가 없다"를 부드럽게 지적하는 동사로 자주 나온다. 구어에서 `Do I have to spell it out for you?` 라고 하면 "꼭 말로 해야 알아?"라는 짜증이 된다.
- 예문: The contract should spell out what happens when the upstream returns a partial page.
- 유사어: make explicit (격식), state outright (단언), lay out (차례로 펼쳐 설명)
- 반의어: leave implicit, gloss over

## "work against"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대의 제안이 상대 자신이 세운 목표와 어긋난다고 정중히 반대할 때(리뷰·설계 논의)
- 한국어: ~에 역행하다, ~와 어긋나다
- 설명: 원문은 `That works against the simplicity you asked for.` 토큰을 정확히 세려면 tokenizer 의존성이 새로 생긴다는 근거를 댄 다음에 나온 문장이다. "당신이 틀렸다"가 아니라 "당신이 원한 단순함에 어긋난다"고 말해 기준을 상대의 말에서 가져왔다. `the simplicity you asked for` 는 관계대명사가 생략된 절이다.
- 예문: Adding a second cache works against the goal of making this service easier to debug.
- 유사어: undermine (격식, 더 세다), run counter to (문어), cut against (구어·미국식)
- 반의어: work in favor of, serve

## "hang together"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 여러 군데 고친 문서·설계가 서로 모순 없이 맞물리는지 말할 때(최종 점검)
- 한국어: 앞뒤가 맞아떨어지다
- 설명: 원문은 `One last full read of the index.md diff to check that the agent contract hangs together.` 이고 다음 메시지가 `The contract hangs together.` 다. 부분이 각각 맞는 것과 전체가 하나로 서는 것은 다른데 이 표현은 뒤쪽을 말한다. 글·논리·계획에 두루 쓴다.
- 예문: Each section reads fine alone, but the proposal doesn't hang together once you compare the budget with the timeline.
- 유사어: be coherent (격식), add up (구어, 앞뒤가 맞다), hold together (거의 같은 뜻)
- 반의어: fall apart

## "(X) can then go"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 다른 변경이 들어가면 필요 없어지는 규칙·코드를 지워도 된다고 할 때(리뷰)
- 한국어: 그러면 ~는 없애도 된다
- 설명: 원문은 `The partial-object salvage rules (lines 161–162) can then go.` 여기서 `go` 는 "가다"가 아니라 "없어지다, 빠지다"이다. `This has to go`(이건 없애야 해)의 그 `go` 다. `then` 이 앞 제안을 조건으로 받아 "그렇게 하면"을 한 단어로 처리했다.
- 예문: Once every caller passes the new flag, the compatibility shim can go.
- 유사어: can be dropped (평이), can be removed (중립), becomes unnecessary (격식, 지운다는 행동은 말하지 않는다)
- 반의어: has to stay

## "Where I disagree:"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 대부분 동의한 뒤 반대하는 지점 하나를 따로 세워 말할 때(리뷰·설계 답변)
- 한국어: 제가 동의하지 않는 부분:
- 설명: 원문은 소제목 `Where I disagree: make one family per request the default` 다. `where` 절이 통째로 명사 노릇을 해 "내가 동의하지 않는 지점"이 된다. 콜론 뒤에는 대안을 명령문으로 바로 붙인 꼴. 같은 세션의 마무리는 `I have no other disagreement.` 와 `Two objections, both small.` 이다. 반대의 범위를 좁혀 말하는 습관이 일관된다.
- 예문: Most of the plan looks right. Where I disagree: the rollout should start with one region, not all three.
- 유사어: My one objection is … (조금 딱딱), The part I'd push back on is … (구어), I take a different view on … (격식)
- 반의어: Where we agree:

## "dominate"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 전체 시간·비용에서 어느 구간이 가장 큰 몫인지 말할 때(성능 분석)
- 한국어: (시간·비용의) 대부분을 차지하다
- 설명: 원문은 `The 8-worker pool with the combined reply comes second, and only once llm-attempts.jsonl shows LLM time dominates.` 목적어 없이 자동사로 썼다. 측정으로 확인되기 전에는 최적화하지 말라는 문맥에서 단골로 나온다. `only once` 가 "그때가 되어서야"라는 조건을 건다.
- 예문: Profile first, because there's no point optimizing the parser if network time dominates.
- 유사어: account for most of (풀어 쓴 말), be the bottleneck (병목이라는 진단까지 담는다), outweigh (둘을 견줄 때)
- 반의어: be negligible

## "dilute attention"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 양이 많아져 정작 중요한 것에 눈이 덜 간다고 지적할 때(문서·알림·회의 설계)
- 한국어: 주의를 흐트러뜨리다, 희석하다
- 설명: 원문은 `A long file also dilutes attention on the short rules that matter in every session`. 물을 타서 묽게 만드는 `dilute` 를 집중·메시지·효과에 빌려 쓴다. 무생물 주어 `A long file` 이 동사를 받는 구성이라 "파일이 길어서 ~하게 된다"를 부사절 없이 한 절로 끝냈다.
- 예문: Ten alerts a day dilute attention, and the one that matters gets ignored.
- 유사어: water down (구어, 내용을 약하게 만들다), spread thin (주의·자원이 넓게 퍼져 얇아지다), weaken (평이)
- 반의어: sharpen the focus, concentrate
