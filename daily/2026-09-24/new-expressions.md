# 2026-09-24 — 새 표현

> 오늘 배치는 repo 문서 2건(equipment-data-map 아키텍처 문서)과 transcript 8건. repo 문서는 본문이 전부 한국어라 영어를 뽑을 데가 없었고 표현 21개는 모두 transcript 의 `[assistant]` 영어에서 나왔다. graphify 도입 검토·가짜 FTP 단계 제거 세션(equipment-data-map)과 pi 오케스트레이션 세션(pm-notes)이 대부분이다. `stand in for`, `reframe`, `first-class`, `no dangling reference` 는 노트에 이미 있어서 뺐다.

## "Short answer: not for X."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: "이거 쓸 수 있을까?" 같은 질문에 결론부터 던질 때(채팅·리뷰 답변, 격식 중간). 뒤에 이유가 길게 온다.
- 한국어: 짧게 답하면, X 에는 안 맞는다.
- 설명: `The short answer is …` 를 줄인 머리말. `not for X` 로 범위를 좁혀 "전부 안 된다"가 아니라 "이 용도로는 아니다"를 전한다. 바로 다음에 `One idea from it is worth borrowing, though.` 처럼 살릴 부분을 붙이면 거절이 덜 딱딱하다.
- 예문: Short answer: not for the equipment file stores themselves.
- 유사어: In a word, no (더 단호함), The quick answer is no (평이), Bottom line: … (결론 강조, 보고체)
- 반의어: It's complicated — let me walk through it. (결론을 미룸)

## "One idea from it is worth borrowing, though."
- 레지스터: professional, conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 외부 도구·라이브러리를 통째로는 안 쓰지만 발상 하나는 가져오자고 할 때(설계 검토, 격식 중간).
- 한국어: 그래도 거기서 가져올 만한 아이디어가 하나 있다.
- 설명: `worth + 동명사` 는 "~할 가치가 있다". `borrow` 는 코드를 복사하는 게 아니라 개념만 빌린다는 뉘앙스라 기술 검토에서 자주 쓴다. 문장 끝 `though` 가 앞 문장의 부정과 대비를 만든다.
- 예문: We won't adopt the tool, but one idea from it is worth borrowing, though: tagging every edge as extracted or inferred.
- 유사어: there's one thing we could take from it (평이), one idea merits adoption (격식↑, 문서체), steal one idea from it (구어, 가벼움)
- 반의어: nothing in it applies to us (가져올 것 없음)

## "leave it out until someone asks for it"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 있으면 좋지만 급하지 않은 기능을 지금 만들지 말자고 할 때(범위 조정 회의·리뷰).
- 한국어: 누가 요청할 때까지 빼 두자.
- 설명: 원문은 `It's a nice-to-have, so leave it out until reviewers ask for it.` `leave out` 은 "빼다, 포함하지 않다". 조건을 "실제 요구"에 걸어 두니 YAGNI 원칙을 한 줄로 말한다.
- 예문: A clickable graph view is a nice-to-have, so leave it out until reviewers ask for it.
- 유사어: park it until there's demand (구어), defer it pending a concrete request (격식↑), hold off on it for now (평이)
- 반의어: build it in up front (미리 넣어 두다)

## "find its way around"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 사람이나 에이전트가 낯선 코드베이스·장소에서 길을 찾아다니는 모습을 말할 때(구어·기술 글 모두).
- 한국어: (어딘가에서) 길을 찾아다니다, 구조를 파악하며 돌아다니다.
- 설명: `find one's way around X` 는 X 의 지리를 익혀 헤매지 않게 된다는 뜻. 소유격이 주어에 맞춰 바뀐다(`find my way around`, `find its way around`).
- 예문: The execution agent could use graphify to find its way around its own build.
- 유사어: get one's bearings in (방향 감각을 잡다), navigate (중립, 문어), learn the lay of the land (관용, 구어)
- 반의어: get lost in (헤매다)

## "worked out by a fixed rule"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 어떤 값이 원문에 적혀 있던 게 아니라 규칙으로 계산·도출됐다고 구분할 때(설계 문서, 격식 중간).
- 한국어: 고정된 규칙으로 도출된.
- 설명: `work out` 은 "계산해 내다, 풀어내다". 원문은 `"worked out by a fixed rule, not written in the source"` 로 `A, not B` 대비와 함께 쓰였다. `derived` 보다 구어적이라 설명할 때 더 부드럽다.
- 예문: graphify's `INFERRED` means worked out by a fixed rule, not written in the source.
- 유사어: derived by rule (격식, 기술 용어), computed deterministically (기술적, 정확), rule-based (형용사형)
- 반의어: read directly from the file (직접 관측한)

## "read X as proof that …"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 사람들이 약한 신호를 확실한 증거로 오해할 위험을 짚을 때(리뷰·설계 논의).
- 한국어: X 를 ~라는 증거로 받아들이다.
- 설명: `read A as B` 는 "A 를 B 로 해석하다". `start reading` 으로 쓰면 "앞으로 그렇게 오해하기 시작하면"이라는 조건이 된다. 대책을 미뤄 두는 조건문에 잘 어울린다.
- 예문: If reviewers start reading `similar_name` as proof that two families are related, the fix would be a third value such as `derived`.
- 유사어: take X as evidence that (중립), treat X as conclusive (격식↑), mistake X for proof (오해를 더 드러냄)
- 반의어: treat X as a hint (단서 정도로 보다)

## "Don't build it until X shows the gap."
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 부족할지도 모르는 기능을 실제 결과로 부족함이 드러날 때까지 미루자고 할 때(설계 권고의 마무리).
- 한국어: X 에서 실제로 빈틈이 보이기 전에는 만들지 마라.
- 설명: `the gap` 은 앞에서 말한 "예상되는 부족분"을 가리킨다. 명령문으로 끝맺어 권고를 단호하게 만든다. 조건절 `If the first real rollout shows …` 와 짝을 이뤄 "증거가 먼저, 구현은 나중"을 말한다.
- 예문: It needs no new dependency. Don't build it until that rollout shows the gap.
- 유사어: wait for evidence before building it (평이), defer it until the need is demonstrated (격식↑), cross that bridge when we come to it (관용, 구어)
- 반의어: build it pre-emptively (미리 만들다)

## "the only takeaway"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 긴 검토 끝에 "건질 건 이것 하나뿐"이라고 정리할 때(회의 마무리·채팅).
- 한국어: 얻어 갈 건 그것 하나뿐.
- 설명: `takeaway` 는 발표·회의에서 가져갈 핵심. `the only` 를 붙여 나머지는 쓸모없었다는 뜻을 담는다. 사용자가 "we only get the concept of extracted, inferred" 라고 하자 `Yes, that's the only takeaway` 로 받았다.
- 예문: Yes, that's the only takeaway, and the spec already has it as `observed_vs_inferred`.
- 유사어: the one thing worth keeping (평이), the sole lesson (격식), the bottom line (결론 강조)

## "That last fact decides the architecture."
- 레지스터: professional, technical
- 출처: transcript:[assistant] pm-notes
- 맥락: 검증한 사실 여러 개 가운데 하나가 설계를 결정짓는다고 짚을 때(기술 보고).
- 한국어: 방금 말한 마지막 사실이 구조를 결정한다.
- 설명: 사물(`fact`)을 주어로 세워 `decides` 를 쓰면 "내가 정했다"가 아니라 "사실이 정했다"가 되어 결정이 객관적으로 들린다. `That last` 는 바로 앞 문장의 마지막 정보를 가리킨다.
- 예문: `agent read` returns raw terminal text, not JSON — that last fact decides the architecture.
- 유사어: that's what drives the design (구어), the architecture hinges on that (격식), that settles it (짧은 구어)

## "said so itself rather than faking it"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] pm-notes
- 맥락: 에이전트·도구가 못 하는 일을 꾸며내지 않고 스스로 보고했을 때 그 태도를 평가하며(버그 보고).
- 한국어: 꾸며내지 않고 스스로 그렇다고 말했다.
- 설명: `say so` 는 "그렇다고 말하다"(so = 앞 내용). `rather than + 동명사` 로 하지 않은 쪽을 대비한다. 에이전트가 거짓 성공을 보고하는 문제가 흔해서 이런 문장이 칭찬이 된다.
- 예문: The reviewer can't write files, and the agent said so itself rather than faking it.
- 유사어: admitted it instead of making something up (평이), reported the limitation honestly (격식), owned up to it (구어)
- 반의어: papered over it (덮어 버리다)

## "Direction change noted"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] pm-notes
- 맥락: 상대가 방향을 바꿨을 때 군말 없이 접수했다고 알리고 바로 다음 행동으로 넘어갈 때(채팅, 짧은 보고).
- 한국어: 방향 바뀐 것 알겠습니다.
- 설명: `(Your) direction change (has been) noted` 에서 주어와 조동사를 떨어뜨린 수동 분사 구문. 대시 뒤에 바뀐 내용을 요약하면(`— dropping herdr, going pi-only`) 오해 없이 확인까지 된다.
- 예문: Direction change noted — dropping herdr, going pi-only.
- 유사어: Got it, switching over (구어), Understood; I'll proceed accordingly (격식↑), Change of plan acknowledged (격식)

## "It would silently not apply."
- 레지스터: technical
- 출처: transcript:[assistant] pm-notes
- 맥락: 설정이 잘못된 자리에 있어서 오류 없이 무시되는 위험을 설명할 때(설정·리뷰).
- 한국어: 오류 없이 조용히 적용되지 않을 것이다.
- 설명: 부사 `silently` 가 `not apply` 앞에 와서 "실패가 눈에 안 띈다"를 강조한다. 원문은 `I put it in the wrong file, where it would silently not apply.` 관계부사 `where` 가 파일을 받아 결과를 이어 준다.
- 예문: `timeoutMs` is a config.json key; in settings.json it would silently not apply.
- 유사어: be ignored without a warning (평이), fail silently (기술 관용), have no effect (중립)
- 반의어: fail loudly (시끄럽게 실패하다)

## "Filesystem as the bus, terminal as the view."
- 레지스터: technical
- 출처: transcript:[assistant] pm-notes
- 맥락: 설계 원칙을 표어처럼 짧게 요약할 때(설계 노트·README).
- 한국어: 파일 시스템이 통신로, 터미널은 보기용.
- 설명: 동사 없이 `A as B, C as D` 두 구를 쉼표로 맞세운 병렬. 앞 문장(`Worker output must go to files, not scrollback`)의 근거를 한 줄로 기억하게 해 준다. `bus` 는 컴포넌트 사이 데이터가 오가는 통로.
- 예문: Worker output must go to files, not scrollback. Filesystem as the bus, terminal as the view.
- 유사어: files carry the data; the terminal just displays it (평이, 풀어쓴 문장), state on disk, view on screen (비슷한 표어)

## "deletes an entire class of X"
- 레지스터: technical, professional
- 출처: transcript:[assistant] pm-notes
- 맥락: 설계 하나로 특정 유형의 코드·버그가 통째로 없어진다고 말할 때(설계 근거).
- 한국어: X 류 전체를 통째로 없앤다.
- 설명: `an entire class of bugs` 는 기술 영어의 단골 표현. 개별 항목이 아니라 "종류 전체"를 없앤다는 게 핵심이라 설계 장점을 설득할 때 힘이 세다.
- 예문: Herdr resolves agents by name, so an orchestrator needs no state file; that deletes an entire class of bookkeeping code.
- 유사어: eliminates a whole category of (격식), gets rid of all that (구어), makes X unnecessary (중립)
- 반의어: adds another layer of (한 겹 더 얹다)

## "It keeps what still passes."
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 재빌드·재실행이 전부를 다시 하는 게 아니라 통과한 부분은 유지한다고 안심시킬 때(작업 안내).
- 한국어: 여전히 통과하는 건 그대로 둔다.
- 설명: 목적어 자리에 `what` 명사절(`what still passes`)이 들어갔다. `still` 이 "바뀐 뒤에도"를 함축한다. 앞에 `That's a CLI and skill rebuild, and` 가 붙어 "재빌드지만 손실은 작다"를 전한다.
- 예문: The agent will redo letters 02, 03, 12 and 14, but it keeps what still passes and rebuilds only the parts that changed.
- 유사어: it only redoes what broke (구어), passing work is preserved (격식, 수동), incremental rebuild (기술 용어)
- 반의어: it starts from scratch (처음부터 다시)

## "Now the riskiest part —"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] pm-notes
- 맥락: 작업 진행 보고 중 가장 위험한 단계에 들어간다고 예고할 때(진행 안내·채팅).
- 한국어: 이제 가장 위험한 부분.
- 설명: 동사를 뺀 명사구 + 대시로 무엇이 위험한지 붙인다. 같은 세션에 `Now the real test —`, `Now the important part —` 도 나와 진행 안내의 틀로 쓸 만하다.
- 예문: Now the riskiest part — parallel fan-out with the `--wait` race.
- 유사어: Here's where it could go wrong (구어), The most delicate step comes next (격식), Next up, the tricky bit (가벼운 구어)

## "irrelevant to X anyway"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 못 한 검사가 있지만 이번 변경과 무관해서 괜찮다고 덧붙일 때(작업 보고 끝).
- 한국어: 어차피 X 와는 상관없다.
- 설명: 원문은 `I didn't run the transport check — irrelevant to a docs-only diff anyway.` 문장 조각으로 이유를 붙여 변명처럼 늘어지지 않는다. `anyway` 가 "안 했지만 결과는 같다"를 담는다.
- 예문: `python` isn't on this shell's PATH, so I didn't run the transport check — irrelevant to a docs-only diff anyway.
- 유사어: which doesn't matter here (평이), not applicable to this change (격식), moot for this diff (간결, 격식)
- 반의어: essential for this change (꼭 필요한)

## "This changes the answer."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] pm-notes
- 맥락: 새로 알게 된 사실 때문에 앞서 한 권고를 뒤집을 때(채팅·리뷰, 솔직한 톤).
- 한국어: 이러면 답이 달라진다.
- 설명: 새 정보를 주어로 세워 "내가 틀렸다" 대신 "상황이 바뀌었다"로 말한다. 뒤에 대시로 무엇이 바뀌었는지 이어야 한다(`— pi-subagents already does most of what I hand-rolled`).
- 예문: This changes the answer — pi-subagents already does most of what I hand-rolled.
- 유사어: That puts things in a different light (격식), Well, that changes things (구어), I'll revise my recommendation (격식, 보고체)
- 반의어: That doesn't change anything (변함없다)

## "What this costs:"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 변경 보고에서 장점을 말한 뒤 대가·부작용을 따로 묶어 보여 줄 때(작업 보고의 소제목).
- 한국어: 이 변경의 대가.
- 설명: `What changed:` → `What this costs:` 로 소제목을 이어 가면 보고가 균형 잡힌다. 대가를 숨기지 않고 제목으로 세우는 게 신뢰를 준다.
- 예문: What this costs: the first time the company LLM interprets anything is on real equipment samples.
- 유사어: Trade-offs: (기술 보고 관용), The downside: (구어), Costs and risks: (격식)
- 반의어: What we gain: (얻는 것)

## "One thing works differently from what I first described"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 작업 전에 설명한 계획과 결과가 한 가지 다를 때 먼저 밝히는 말(완료 보고).
- 한국어: 처음에 설명한 것과 다르게 된 게 하나 있다.
- 설명: `differently from what …` 은 "~와 다르게". 결과가 계획과 어긋났다고 스스로 밝히고 콜론 뒤에서 이유를 설명한다. 보고의 정직성을 보여 주는 틀.
- 예문: One thing works differently from what I first described: the CLI still has `stage 1` and `stage 2` commands.
- 유사어: One deviation from the plan (격식), Heads-up, one thing changed (구어), Contrary to what I said earlier, … (정정 강조)

## "echo (something) back"
- 레지스터: technical
- 출처: transcript:[assistant] pm-notes
- 맥락: 프로그램이 입력받은 값을 출력에 그대로 되돌려 보여 주는 동작을 말할 때(디버깅 설명).
- 한국어: (입력을) 그대로 되돌려 출력하다.
- 설명: `echo back` 은 메아리처럼 받은 걸 되돌려 준다는 동사구. 목적어가 짧으면 가운데(`echoes the query back`)에 넣는다. 이 경우 검색어가 오류 메시지에 되비쳐 grep 이 자기 자신을 찾아낸 버그였다.
- 예문: `pi --list-models` echoes the query back in its "No models matching" message, so the grep matched itself.
- 유사어: repeat back (구어), reflect the input (기술적), include the query verbatim (격식)
