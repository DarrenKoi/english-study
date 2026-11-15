# 2026-11-16 — 새 표현

오늘 원문은 skewnono-v3-nuxt 세션 한 건이다. llm-council 스킬을 설치하고 고쳐 쓴 다음 두 번 시험 실행한 대화라서, 조언자 다섯과 검토자, 의장이 서로의 주장을 따지는 영어가 많다. 남의 논리를 반박하고 근거가 약하다고 짚고 소수 의견 편을 드는 말을 주로 골랐다. 스킬 문서(skill-creator)에서도 하나 넣었다.

## "before calling it installed"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 설치 보고)
- 맥락: 확인을 마치기 전에는 "끝났다"고 말하지 않겠다고 밝힐 때(업무 구어·진행 보고)
- 한국어: 설치됐다고 말하기 전에
- 설명: `call it + 형용사/과거분사` 는 "그것을 ~라고 부르다, ~로 치다"이다. 원문은 `so I'm reading it before calling it installed` 로, 파일을 받아 놓은 것만으로는 설치라고 하지 않겠다는 태도가 담겼다. `call it done`, `call it fixed` 로 바꿔 쓰기 좋다.
- 예문: I want to run the migration on a copy of the database before calling it done.
- 유사어: before signing off on it (승인·확정의 느낌, 격식), before I declare it finished (선언하다, 약간 무겁다), before marking it complete (티켓·체크리스트 맥락)
- 반의어: call it a day (이쯤에서 끝내다; 확인 없이 접는 쪽)

## "Nothing runs on its own"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 설치 보고)
- 맥락: 받은 파일에 자동 실행되는 코드가 없다고 안심시킬 때(구어·보안 점검 보고)
- 한국어: 저절로 실행되는 것은 없다.
- 설명: `on its own` 은 "누가 시키지 않아도 혼자서"이다. 원문은 `Nothing runs on its own, so it's only text instructions for the agent.` 로 이어진다. 부정 주어 `Nothing` 으로 시작해서 `not … anything` 보다 단호하게 들린다.
- 예문: Nothing runs on its own in this repo; every script has to be started by hand.
- 유사어: nothing executes automatically (문서용, 격식), there are no hooks or background jobs (구체적으로 풀어 쓴 말), it's inert (한 단어, 엔지니어 구어)
- 반의어: it fires automatically (자동으로 발동한다)

## "they add cost without adding perspective"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] Insight)
- 맥락: 어떤 단계가 비용만 들고 얻는 게 없다고 지적할 때(설계 리뷰·문어)
- 한국어: 비용만 늘리고 관점은 늘리지 못한다.
- 설명: 같은 동사 `add` 를 두 번 써서 "늘어난 것"과 "안 늘어난 것"을 맞세운다. `without + -ing` 가 뒤쪽을 부정한다. 검토자 다섯이 같은 모델, 같은 프롬프트라는 사정을 한 줄로 정리한 문장이다.
- 예문: Two more approval steps would add delay without adding safety.
- 유사어: it's all cost and no benefit (구어, 더 세다), they are redundant (한 단어, 건조하다), it doesn't pay for itself (들인 값을 못 한다)
- 반의어: it earns its keep (들인 값을 한다)

## "That cancels the one thing this advisor is for"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] Insight)
- 맥락: 어떤 처리가 그 부품의 존재 이유를 없앤다고 짚을 때(리뷰 코멘트·구어)
- 한국어: 그러면 이 조언자가 있는 단 하나의 이유가 사라진다.
- 설명: `the one thing X is for` 는 "X가 존재하는 유일한 용도"이고 전치사 `for` 가 문장 끝에 남는다. `That` 은 앞 문장 전체(외부인에게도 같은 브리프를 준다)를 받는다. 길게 설명하지 않고 결함의 무게를 전한다.
- 예문: Caching the health check cancels the one thing a health check is for.
- 유사어: that defeats the purpose (가장 흔한 구어), that undermines its whole point (조금 부드럽다), that negates its function (격식 문어)
- 반의어: that plays to its strength (강점을 살린다)

## "so it isn't anchored on our conversation"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 재작성 보고)
- 맥락: 판단하는 쪽이 앞선 정보에 끌려가지 않게 분리했다고 설명할 때(설계 근거·준격식)
- 한국어: 우리 대화에 끌려가지 않도록
- 설명: `be anchored on` 은 처음 본 정보에 닻을 내린 듯 판단이 묶이는 것으로, 심리학의 anchoring bias 에서 왔다. 원문은 `has the chairman run as a fresh subagent so it isn't anchored on our conversation` 이고, `have + 목적어 + 동사원형` 사역 구문이 함께 쓰였다.
- 예문: Ask a second reviewer who hasn't seen the ticket, so they aren't anchored on my explanation.
- 유사어: biased by (일반적인 말), primed by (미리 자극받은, 심리학 용어), influenced by (가장 중립)
- 반의어: comes to it fresh (선입견 없이 본다)

## "An advisor slot is load-bearing"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Executor 답변)
- 맥락: 빠지면 전체가 흔들리는 자리라고 말할 때(아키텍처 토론·구어)
- 한국어: 조언자 자리는 하중을 받는 자리다.
- 설명: `load-bearing` 은 건축의 내력벽에서 온 말로, 치우면 무너지는 부분을 가리킨다. 원문은 콜론 뒤에 이유를 붙인다. `if Codex fails there, you lose one of five lenses and the chairman has to reason about a hole.` 맞은편 표현은 같은 답변에 나온 `redundant by design` 이다.
- 예문: That retry wrapper looks like boilerplate, but it is load-bearing; remove it and the nightly job fails.
- 유사어: critical-path (일정·흐름에서 빠질 수 없는), essential (평범한 말), a single point of failure (명사구, 위험을 강조)
- 반의어: redundant by design (일부러 여분을 둔), optional

## "Then measure instead of debating"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Executor 답변)
- 맥락: 논쟁을 접고 작은 실험으로 정하자고 제안할 때(회의·구어)
- 한국어: 그다음에는 말로 다투지 말고 재 보라.
- 설명: `instead of + -ing` 로 그만둘 행동을 뒤에 둔다. 주어 없는 명령문이라 회의에서 결론을 재촉하는 말투다. 원문은 바로 뒤에 무엇을 셀지 정해 준다. `For the next five council runs, note one thing.`
- 예문: We've argued about the cache size for a week; let's measure instead of debating.
- 유사어: let the data decide (데이터에 맡기자), run the experiment (실험하자), stop guessing and check (더 구어)
- 반의어: keep going back and forth (말만 주고받다)

## "one person wearing five hats"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Outsider 답변)
- 맥락: 여럿처럼 보여도 실은 한 주체가 역할만 바꿔 맡았다고 꼬집을 때(구어·비유)
- 한국어: 모자 다섯 개를 번갈아 쓴 한 사람
- 설명: `wear many hats` 는 한 사람이 여러 역할을 맡는다는 관용구다. 보통은 바쁘다는 뜻으로 쓰지만 여기서는 "독립된 다섯이 아니다"라는 비판으로 돌려 썼다. 원문은 `"five advisors on the same Claude model with different thinking styles" describes one person wearing five hats.`
- 예문: At a startup that size, the CTO is one person wearing five hats.
- 유사어: playing multiple roles (평이하게), the same voice in different costumes (원문에 가까운 비유), a one-man band (혼자 다 한다, 구어)
- 반의어: independent minds (서로 독립된 판단 주체)

## "grading your own homework"
- 레지스터: conversational, casual
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Outsider 답변)
- 맥락: 만든 쪽이 검증까지 하면 의미가 없다고 지적할 때(구어·비유)
- 한국어: 자기 숙제를 자기가 채점하기
- 설명: 원문은 `That is grading your own homework five times and calling it consensus.` 다. 영국식은 `marking your own homework`. 동명사 두 개(`grading`, `calling`)를 `and` 로 이어 "하고서는 ~라고 부른다"는 비꼼을 만든다.
- 예문: Letting the team that wrote the feature approve its own release is grading your own homework.
- 유사어: marking your own homework (영국식), a rubber stamp (형식적인 승인), self-certification (격식, 규정 문서)
- 반의어: independent review (독립 검토), a second pair of eyes (다른 사람의 눈)

## "Reading this cold"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Outsider 답변)
- 맥락: 사전 지식 없이 처음 본 인상이라고 전제할 때(리뷰 코멘트·구어)
- 한국어: 아무 배경 없이 읽어 보면
- 설명: `cold` 가 부사처럼 쓰여 "준비나 맥락 없이"를 뜻한다. `cold call`, `cold start`, `go in cold` 와 같은 계열이다. 분사구문이라 주어는 뒤 절과 맞아야 하는데 원문은 주어가 인용구라서 엄밀히는 어긋난다. 구어에서는 흔히 넘어간다.
- 예문: Reading this cold, I couldn't tell which of the three services owns the retry logic.
- 유사어: coming to this fresh (선입견 없이), with no context (풀어서), as an outsider (외부인으로서)
- 반의어: knowing the backstory (사정을 아는 채로)

## "degrades cleanly to two reviewers"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 First Principles 답변)
- 맥락: 일부가 빠져도 전체가 덜 좋은 상태로 무리 없이 돌아간다고 설명할 때(설계 문서·토론)
- 한국어: 검토자 둘인 상태로 깔끔하게 내려앉는다.
- 설명: `degrade` 는 고장 나지 않고 성능만 낮아지는 것이고 `degrade gracefully` 가 표준 표현이다. `cleanly` 를 쓰면 "뒤탈 없이"가 강조된다. 원문은 `while a missing advisor leaves a hole in the lens set` 으로 반대 경우를 붙여 대비했다.
- 예문: If the cache server is down, the page degrades cleanly to a slower direct query.
- 유사어: degrades gracefully (가장 흔한 표준 표현), falls back to (대체 경로로 넘어간다), fails soft (부드럽게 실패한다)
- 반의어: fails hard (통째로 죽는다), leaves a hole (구멍이 난다)

## "want dissent shown rather than averaged away"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (의장 판결문)
- 맥락: 이견을 요약 과정에서 뭉개지 말고 드러내자고 할 때(보고서·회의록, 격식)
- 한국어: 이견이 평균에 묻히지 않고 드러나기를 바란다.
- 설명: `want + 목적어 + 과거분사` 구조다. `average away` 의 `away` 는 "닳아 없어지게"라는 뜻을 더한다(`explain away`, `smooth away`). `dissent` 는 다수와 다른 의견을 가리키는 격식 명사다.
- 예문: In the summary, I want the two objections shown rather than averaged away into "mostly positive".
- 유사어: smoothed over (대충 덮다, 구어), glossed over (얼버무리다), flattened (같은 원문에 나온 `flattening dissent`)
- 반의어: surfaced (겉으로 드러낸), called out (콕 집어 밝힌)

## "The peer review took that apart"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (의장 판결문)
- 맥락: 누군가의 주장이 조목조목 반박당했다고 전할 때(구어·준격식 보고)
- 한국어: 상호 검토가 그 주장을 조목조목 깼다.
- 설명: `take apart` 는 기계를 분해하듯 주장을 하나씩 뜯어 무너뜨리는 것이다. 원문은 콜론 뒤에 반박 세 가지를 나열한다. `the wrapper can read beyond the brief, the trial has no noise baseline, and five occasional runs take months.`
- 예문: I thought my estimate was solid until the review took it apart in ten minutes.
- 유사어: picked it apart (흠을 하나하나 잡다), dismantled (격식), poked holes in (허점을 찔렀다, 덜 세다)
- 반의어: backed it up (뒷받침했다), held up (검증을 버텼다; `the claim held up`)

## "I am siding with the minority"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (의장 판결문)
- 맥락: 다수결과 다른 쪽을 택한다고 분명히 밝힐 때(결정문·회의)
- 한국어: 나는 소수 의견 편에 선다.
- 설명: `side with` 는 "~편을 들다"이고 `side` 가 동사다. 원문은 `over the three votes for C` 를 붙여 무엇을 제치고 택했는지까지 밝힌다. 줄임말 없는 `I am` 이 결정문다운 무게를 준다.
- 예문: I am siding with the two engineers who want to delay the release, even though most of the team disagrees.
- 유사어: I'm going with (구어), I come down on the side of (고민 끝에 기울다), I agree with the dissenters (평이하게)
- 반의어: side against (반대편에 서다; 원문에도 `the peer review sided against "one line"`), go with the majority

## "rests on evidence that does not transfer"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (조언자 Contrarian 답변)
- 맥락: 다른 분야에서 통한 근거를 여기에 그대로 쓸 수 없다고 반박할 때(논증·문어)
- 한국어: 여기로 옮겨 올 수 없는 근거에 기대고 있다.
- 설명: `rest on` 은 "~을 토대로 삼다"이고, `transfer` 는 자동사로 "다른 상황에도 통하다"이다. 코드 리뷰에는 정답이 있지만 의사 결정에는 없다는 이유가 뒤따른다. 의장도 같은 틀을 썼다. `The case for C rests on Executor's claim.`
- 예문: The plan rests on benchmarks from a much smaller dataset, and those results do not transfer.
- 유사어: is built on (평이하게), hinges on (그것 하나에 달려 있다), doesn't carry over (구어로 "안 넘어온다")
- 반의어: holds across contexts (어디서나 성립한다), generalizes

## "only the Contrarian is still outstanding"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 진행 보고)
- 맥락: 아직 안 들어온 항목이 무엇인지 보고할 때(업무 메일·진행 보고)
- 한국어: 반대론자 것만 아직 안 왔다.
- 설명: `outstanding` 은 "뛰어난" 말고 "아직 처리되지 않은"이라는 뜻이 있다. 미결 청구서(`outstanding invoice`), 남은 작업(`outstanding items`)에 쓴다. 같은 대화에서 도착한 쪽은 `are in` 으로 말한다. `Four of five advisors are in.`
- 예문: Three of the four approvals are in; only the security review is still outstanding.
- 유사어: pending (대기 중, 시스템 용어), yet to come in (구어), still to be done (할 일 쪽)
- 반의어: in (도착한), settled / closed out (마무리된)

## "Yes, modestly."
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 최종 보고)
- 맥락: "효과가 있나?"는 물음에 있긴 하되 크지 않다고 답할 때(보고·회의)
- 한국어: 네, 조금은요.
- 설명: 두 단어로 답과 크기를 함께 말한다. `modestly` 는 "소폭으로"이고 숫자에도 쓴다(`grew modestly`). 원문은 `Does Codex add anything?` 이라는 제목 밑에 이 답을 먼저 놓고 근거를 이었다. 뒤에 `the same modest gain` 으로 다시 받는다.
- 예문: Does the new index speed things up? Yes, modestly: about eight percent on the slowest queries.
- 유사어: Somewhat. (어느 정도), A little, yes. (구어), Marginally. (아주 조금, 더 낮춰 말한다)
- 반의어: Yes, substantially. (네, 크게요), Not at all.

## "folding what the run taught into the skill"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt ([assistant] 진행 보고)
- 맥락: 시험에서 배운 점을 본문에 반영하겠다고 할 때(진행 보고·구어)
- 한국어: 이번 실행에서 배운 것을 스킬에 녹여 넣는 중
- 설명: `fold A into B` 는 반죽에 재료를 섞듯 A를 B에 자연스럽게 합치는 것이다. 목적어 자리에 `what the run taught` 라는 명사절이 왔고 사물 주어 `the run` 이 "가르쳤다". 한국어라면 "실행에서 배운 것"이라고 사람을 주어로 삼을 자리다.
- 예문: I'm folding the review comments into the design doc before I send it around again.
- 유사어: incorporate (격식, 문서용), work A into B (손봐서 끼워 넣다), bake in (처음부터 박아 넣다, 구어)
- 반의어: leave out (빼다), keep separate

## "just vibe with me"
- 레지스터: casual
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (skill-creator 스킬 본문)
- 맥락: 격식 차린 절차 없이 편하게 같이 해 보자고 할 때(친한 동료 사이, 아주 구어)
- 한국어: 그냥 편하게 나랑 맞춰 가자.
- 설명: `vibe with` 는 "분위기를 맞추다"라는 최근 속어다. 원문은 `if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.` 이고, `is like` 도 "~라고 말한다면"을 뜻하는 구어 인용 표현이다. 회의록이나 메일에는 쓰지 않는다.
- 예문: We don't need a spec for this prototype; just vibe with me for an hour and we'll see what works.
- 유사어: let's just wing it (준비 없이 해 보자), keep it loose (느슨하게 가자), let's play it by ear (상황 봐 가며 하자, 덜 속어)
- 반의어: do it by the book (절차대로 하다)
