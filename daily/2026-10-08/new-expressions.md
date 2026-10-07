# 2026-10-08 — 새 표현

> 오늘 배치는 repo 문서 10건과 transcript 14건이다. repo 문서는 skewnono_v3_nuxt 의 AFM 적재 명세·회신 기록·질문서·사무실 확인서인데 본문이 한국어여서 표현 재료가 나오지 않았다. transcript 여섯은 `/clear` 나 `/model` 만 찍힌 빈 세션. 영어는 다섯 군데서 나왔다. 세션에 딸려 온 스킬 문서 둘(`herdr`, `grilling`), AFM API 문서화를 하위 에이전트에게 맡긴 영어 지시문, orca 를 지운 뒤의 영어 결과 보고, 그리고 작업 중간에 찍힌 한두 줄짜리 영어 진행 보고. `browser-verify` 스킬은 어제까지 다 골랐으므로 건너뛰었다. 노트에 이미 있어서 뺀 것: `is the authority for`, `treat every ID as an opaque string`, `instead of predicting either one`, `when the layout calls for it`, `unusably narrow`, `Inspect before waiting`, `infer a larger topology`, `is considered seen`, `control surface`, `hang off`, `Don't block on it`, `The frontier is X.`, `take effect`, `say so`.

## "Do not probe a mutating nested command by omitting arguments"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 herdr 스킬 문서)
- 맥락: CLI 사용법을 알아보려고 인자를 빼고 실행해 보는 버릇을 막을 때(도구 문서의 경고문, 격식).
- 한국어: 상태를 바꾸는 하위 명령을 인자 없이 찔러 보지 말 것
- 설명: `probe` 는 탐침으로 찔러 보듯 "어떻게 반응하나 떠본다"는 동사. `mutating` 은 상태를 바꾼다는 뜻의 형용사로 `read-only` 의 반대편에 선다. `by omitting arguments` 가 수단이고, 바로 뒤 문장이 이유를 댄다(`some commands … are valid with defaults and will execute`).
- 예문: Do not probe a mutating nested command by omitting arguments; some commands are valid with defaults and will execute.
- 유사어: Don't run a write command just to see its usage (평이), Don't poke at it to see what happens (구어)
- 반의어: Run it with `--help` first (도움말부터 보기)

## "Honor a direction requested by the user."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 herdr 스킬 문서)
- 맥락: 기본 규칙보다 사용자의 요청이 먼저라고 한 줄로 못 박을 때(지침·규정 문서, 격식).
- 한국어: 사용자가 요청한 방향이 있으면 그대로 따를 것
- 설명: `honor` 는 약속·요청·설정을 "존중해서 그대로 지킨다"는 격식 동사(`honor a request`, `honor the config`). `follow` 보다 "내 판단보다 앞세운다"는 느낌이 짙다. `requested by the user` 는 과거분사가 뒤에서 `a direction` 을 꾸민다. 다음 문장이 `Otherwise` 로 시작해서 "요청이 없을 때만 직접 고른다"가 이어진다.
- 예문: Honor a direction requested by the user; otherwise inspect the caller pane's current rectangle.
- 유사어: Respect the user's choice (평이), Go with whatever the user asked for (구어), Defer to the user's stated preference (더 격식)
- 반의어: override the user's choice (사용자의 선택을 무시하고 덮어쓰다)

## "unless the user explicitly intends to …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 herdr 스킬 문서)
- 맥락: 위험한 동작을 금지하면서 예외 하나만 열어 둘 때(안전 규칙, 격식).
- 한국어: 사용자가 분명히 그럴 의도일 때가 아니면
- 설명: `Never … unless …` 는 금지와 예외를 한 문장에 담는 틀. `explicitly` 가 "짐작이 아니라 말로 밝힌"을 맡고, `intends to` 는 `wants to` 보다 결과까지 알고 하는 선택이라는 뜻이 실린다. 같은 문서에 `unless the user explicitly asked`, `unless the user explicitly requests` 도 나와서 동사만 바꿔 쓰는 연습이 된다.
- 예문: Never run `herdr server stop` from an active session unless the user explicitly intends to stop the server and its pane processes.
- 유사어: unless the user explicitly asks for it (요청 기준), only if the user really means to (구어), absent explicit instruction (법률·규정 투)
- 반의어: by default (따로 말이 없으면 늘)

## "Interview the user relentlessly until you reach a shared understanding."
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 설계나 계획을 확정하기 전에 빈틈이 없어질 때까지 묻겠다고 선언할 때(지침 문서, 회의 진행 규칙).
- 한국어: 서로 같은 그림을 그릴 때까지 사용자를 집요하게 인터뷰할 것
- 설명: `relentlessly` 는 "늦추지 않고, 봐주지 않고". 사람에게 쓰면 조금 센 말인데 여기서는 묻는 쪽의 태도를 일부러 세게 잡았다. `reach a shared understanding` 은 "합의"(`agreement`)보다 한 발 앞 단계, 같은 것을 같은 뜻으로 알고 있는 상태를 말한다. `until` 절은 미래 일이라도 현재형.
- 예문: Interview the user relentlessly until you reach a shared understanding.
- 유사어: keep asking until we're on the same page (구어), probe until the requirements are unambiguous (문어), drill down until nothing is unclear (구어·업무)
- 반의어: take the request at face value (요청을 적힌 그대로만 받아들이다)

## "without guessing at answers you haven't heard yet"
- 레지스터: professional, conversational
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 아직 답을 듣지 못한 것을 넘겨짚지 않겠다고 할 때(회의·인터뷰 진행, 구어와 문어 모두).
- 한국어: 아직 듣지 못한 답을 넘겨짚지 않고
- 설명: `guess at X` 의 `at` 은 과녁을 겨누는 전치사. `guess the answer` 가 "맞혔다"까지 품는다면 `guess at the answer` 는 "맞는지 모르고 찍어 본다"에 머문다. `you haven't heard yet` 은 목적격 관계대명사를 뺀 관계절이고 현재완료 부정에 `yet` 이 붙어 "앞으로 들을 것"임을 남긴다.
- 예문: The frontier is the set of questions you can ask now without guessing at answers you haven't heard yet.
- 유사어: without assuming the answer (평이), without jumping ahead (구어), without presupposing the outcome (격식)
- 반의어: fill in the blanks yourself (빈칸을 제멋대로 채우다)

## "push the frontier outward"
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 결정 하나가 내려지면서 다음에 다룰 범위가 넓어진다고 말할 때(설계 논의, 문어).
- 한국어: 경계선을 바깥으로 밀어내다
- 설명: `frontier` 는 개척지의 맨 끝 선. 연구·탐색 문맥에서 "지금 손이 닿는 가장 바깥"을 뜻한다. `settled decisions push the frontier outward` 는 사람이 아니라 결정이 주어인 무생물 주어 문장이고 뒤에 `and unblock questions that depended on them` 이 이어져 "밀어내고, 풀어 준다"가 한 호흡에 읽힌다.
- 예문: Settled decisions push the frontier outward and unblock questions that depended on them.
- 유사어: open up the next set of questions (평이), move the boundary forward (평이), expand what we can decide next (풀어 쓴 구어)
- 반의어: narrow the scope (범위를 좁히다)

## "Finding facts is your job, never the user's."
- 레지스터: professional, conversational
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 누가 무엇을 맡는지 한 문장으로 가를 때(역할 분담을 적는 지침, 팀 규칙).
- 한국어: 사실을 찾는 일은 네 몫이고 사용자 몫이 아니다
- 설명: 동명사 주어 `Finding facts` 에 단수 동사 `is`. 쉼표 뒤의 `never the user's` 는 `never the user's job` 에서 `job` 을 뺀 소유격이다. `not` 대신 `never` 를 써서 "예외 없이"가 된다. 몇 줄 아래의 `The decisions are the user's` 와 짝을 이뤄 사실은 내가, 결정은 사용자가 맡는 구도가 완성된다.
- 예문: Finding facts is your job, never the user's.
- 유사어: Look it up yourself; don't ask the user (평이한 명령), The legwork is on you (구어), Fact-finding rests with the agent, not the user (격식)
- 반의어: Ask the user for it (사용자에게 물어서 얻다)

## "put each to them and wait"
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 결정할 사항을 상대에게 넘기고 답을 기다리라고 할 때(지침·회의 진행, 약간 격식).
- 한국어: 하나하나 그들에게 내놓고 기다릴 것
- 설명: `put a question to someone` 은 "누구에게 질문을 내놓다"는 격식 있는 연어. `ask them each one` 보다 "결정권이 저쪽에 있다"는 뜻이 선명하다. `each` 는 앞의 `The decisions` 를 받는 대명사이고, `them` 은 `the user` 를 단수 they 로 받았다.
- 예문: The decisions are the user's — put each to them and wait.
- 유사어: ask them one by one and wait (평이), run each one by them (구어), submit each for their decision (격식)
- 반의어: decide on their behalf (대신 정해 버리다)

## "nothing left silently assumed"
- 레지스터: professional
- 출처: transcript:pm-notes [user] (세션에 딸려 온 grilling 스킬 문서)
- 맥락: 논의가 끝났다는 기준을 "말없이 넘어간 가정이 없음"으로 잡을 때(설계 리뷰·요구사항 정리, 문어).
- 한국어: 말없이 가정해 둔 채 남은 것이 없다
- 설명: 콜론 뒤에 동사 없이 놓인 명사구 둘(`every branch of the design tree visited, nothing left silently assumed`)이 "끝난 상태"를 그린다. `left + 과거분사` 는 "~된 채로 남겨진". `silently` 가 요점인데, 가정 자체가 아니라 말하지 않은 가정이 문제라는 뜻이다.
- 예문: The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed.
- 유사어: no unstated assumptions (명사구, 문서용), nothing taken for granted (평이), every assumption spelled out (뒤집어 말하기)
- 반의어: taken as read (말 안 해도 그런 것으로 치다, 영국식)

## "own the diff directly"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 일을 맡기면서 "네가 직접 고치고 그 변경을 책임져라"고 범위를 정할 때(업무 위임, 코드 리뷰).
- 한국어: 변경분을 직접 책임지고 맡아라
- 설명: `own` 은 소유가 아니라 책임을 뜻한다(`Who owns this service?`). `the diff` 는 이번에 바뀌는 코드 전체. `directly` 뒤에 `do not spawn agents, do not commit` 이 이어져서 "남에게 넘기지 말고 네 손으로"가 구체화된다. 콜론 앞의 `You are a code-writing delegate` 가 역할, 뒤가 그 역할의 경계.
- 예문: You are a code-writing delegate: own the diff directly, do not spawn agents, do not commit.
- 유사어: make the change yourself (평이), you're responsible for the change end to end (풀어 쓴 문어), it's your change to land (구어)
- 반의어: hand it off (남에게 넘기다), delegate it further (다시 위임하다)

## "What is missing is that …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 이미 된 것을 먼저 말한 뒤 빠진 한 가지를 짚을 때(작업 지시·이슈 설명, 문어와 구어 모두).
- 한국어: 빠져 있는 것은 ~라는 점이다
- 설명: `What is missing` 이 주어인 의사분열문(pseudo-cleft). 앞 문장 둘이 "엔드포인트는 이미 있다, 토큰 요청에도 답한다"를 깔고, 이 문장이 빠진 것 하나에 초점을 모은다. `The reference page does not list them` 이라고만 써도 뜻은 같지만 "문제는 이것 하나"라는 무게가 실리지 않는다.
- 예문: What is missing is that the `/endpoints` API reference page does not list them.
- 유사어: The only gap is that … (더 짧게), The catch is that … (구어, 함정의 느낌), What remains is … (남은 일을 말할 때)
- 반의어: What is already in place is … (이미 갖춰진 것은)

## "it MUST be percent-encoded"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: URL 에 넣을 수 없는 문자를 `%XX` 꼴로 바꿔야 한다고 못 박을 때(API 문서, 명세).
- 한국어: 반드시 퍼센트 인코딩해야 한다
- 설명: `percent-encode` 는 `#` 을 `%23` 으로 바꾸는 방식의 정식 이름이다. 흔히 `URL-encode` 라고도 한다. 대문자 `MUST` 는 RFC 문서에서 온 관습으로, "권장이 아니라 필수"를 표시한다. `so it MUST be …, otherwise …` 는 이유, 의무, 어겼을 때의 결과를 한 문장에 세운 구조.
- 예문: It contains `#`, so it MUST be percent-encoded in the URL path, otherwise the HTTP client drops everything after it as a fragment.
- 유사어: must be URL-encoded (더 흔한 말), needs to be escaped (넓은 뜻), has to be quoted (Python `urllib.parse.quote` 에서 온 말)
- 반의어: can be passed as-is (그대로 넘겨도 된다)

## "drops everything after it as a fragment"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 어떤 문자 때문에 그 뒤가 통째로 버려진다고 설명할 때(버그 원인 설명, 기술 문서).
- 한국어: 그 뒤를 전부 프래그먼트로 보고 떼어 버린다
- 설명: `drop` 은 "말없이 빼 버리다". 오류를 내지 않는다는 뜻이 함께 실린다. `as a fragment` 의 `as` 는 "~로 취급해서". URL 에서 `#` 뒤는 서버로 가지 않는 fragment 라는 규칙을 한 구절로 요약했다. `everything after it` 의 `it` 은 앞의 `#`.
- 예문: Unless the filename is encoded, the HTTP client drops everything after the `#` as a fragment. (작성)
- 유사어: cuts off the rest of the path (평이), treats the rest as a fragment and never sends it (풀어 쓰기), truncates the URL at the `#` (격식)
- 반의어: sends the path intact (경로를 온전히 보낸다)

## "work as pasted"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 예제를 복사해 붙이면 손대지 않고 돌아가야 한다고 요구할 때(문서 작성 기준, 리뷰 코멘트).
- 한국어: 붙여 넣은 그대로 동작하다
- 설명: `as + 과거분사` 는 "~된 그 상태로"(`as written`, `as shipped`, `as is`). 예제 코드의 품질 기준을 두 낱말로 말한다. 원문에서는 `so both the curl and the Python snippet … work as pasted` 로, 목적을 나타내는 `so` 절 안에 들어 있다.
- 예문: Write every example path with the encoded literal so both the curl and the Python snippet work as pasted.
- 유사어: work out of the box (설치 직후 바로), run without edits (평이), be copy-paste ready (형용사로)
- 반의어: need tweaking first (먼저 손을 봐야 한다)

## "is thinned for display"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 화면에 그리려고 데이터 점을 솎아 냈다고 말할 때(API 문서, 데이터 설명).
- 한국어: 표시용으로 솎아 낸다
- 설명: `thin` 은 동사로 "솎다, 묽게 하다"(`thin the seedlings`, `thin the paint`). `downsample` 이 정식 용어라면 `thin` 은 그림이 떠오르는 일상어다. `for display` 가 목적을 밝혀 "원본이 줄어든 게 아니라 보여 주는 쪽만"임을 알린다.
- 예문: Without `full=1`, a dense scan is thinned for display, and comparing `count` with `total` tells you whether that happened. (작성)
- 유사어: is downsampled (정식 용어), is decimated (신호 처리 용어), is trimmed down for the chart (구어)
- 반의어: is returned in full (전부 돌려준다)

## "the untouched original"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 변환·압축을 거치지 않은 원본 파일을 가리킬 때(파일 형식 설명, 문서).
- 한국어: 손대지 않은 원본
- 설명: `untouched` 는 "아무도 건드리지 않은". `raw` 가 가공 전 데이터라는 뜻이라면 `untouched` 는 "받은 그대로 한 바이트도 안 바꿨다"는 보증에 가깝다. 원문은 `the untouched original; path says tiff but align is .bmp` 로, 경로 이름과 실제 형식이 다르다는 주의를 바로 붙였다.
- 예문: This route returns the untouched original, so an align image comes back as `.bmp` even though the path says `tiff`. (작성)
- 유사어: the raw file (가공 전), the source file as stored (풀어 쓰기), the pristine copy (문어, 깨끗함 강조)
- 반의어: the converted copy (변환본), a derived thumbnail (파생 썸네일)

## "drop the sentence if false"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 확인해 보고 사실이 아니면 그 내용을 빼라고 조건부로 지시할 때(문서 작성 위임, 편집 지시).
- 한국어: 사실이 아니면 그 문장은 뺄 것
- 설명: `if false` 는 `if it is false` 를 줄인 꼴. 지시문에서 흔한 생략이다(`if needed`, `if any`, `if so`). `drop` 은 "빼다"의 가장 가벼운 동사. 괄호 안에서 `confirm by reading … ; drop the sentence if false` 로 "확인 방법 + 틀렸을 때의 처리"를 한꺼번에 준 점이 배울 만하다.
- 예문: Confirm that the pages call no other endpoint, and drop the sentence if false.
- 유사어: leave it out if it doesn't hold (구어), omit it if it turns out to be untrue (격식), cut it if you can't confirm it (조건을 "확인 불가"로)
- 반의어: keep it as is (그대로 둘 것)

## "No new comments except a non-obvious why."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 코드 주석 기준을 한 줄로 정할 때(코딩 규칙, 리뷰 기준).
- 한국어: 뻔하지 않은 "왜"가 아니면 주석을 새로 달지 말 것
- 설명: 의문사 `why` 를 명사로 썼다. `a why` 는 "이유 하나"이고 `the what and the why` 같은 꼴로도 자주 나온다. `non-obvious` 가 붙어 "코드만 봐서는 알 수 없는 이유"로 좁혀진다. 동사가 없는 명사구 문장이라 체크리스트 항목으로 읽힌다.
- 예문: Our rule for this repo is simple: no new comments except a non-obvious why. (작성)
- 유사어: Comment only the reasoning that isn't obvious from the code (풀어 쓰기), Explain why, not what (표어)
- 반의어: comment every line (줄마다 주석을 달다)

## "anything in my brief you found wrong"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [agent-prompt] (AFM API 문서화 위임 지시문)
- 맥락: 내가 준 지시나 전제에 틀린 데가 있으면 알려 달라고 미리 청할 때(업무 위임, 리뷰 요청).
- 한국어: 내 지시문에서 틀렸다고 본 곳이 있으면 무엇이든
- 설명: `brief` 는 명사로 "일을 맡기며 건네는 지시·배경 설명". `find + 목적어 + 형용사`(`found it wrong`)에서 목적어가 앞으로 나가 관계절이 됐다. 보고서에 넣을 항목으로 이것을 요구하면 맡은 쪽이 틀린 전제를 그대로 따르지 않고 되짚을 길이 열린다.
- 예문: In your report, include anything in my brief you found wrong and which endpoints you left out.
- 유사어: anything I got wrong (구어), any errors in my instructions (평이), any inaccuracies in the brief (격식)

## "Everything orca-related is gone from …"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (orca 제거 결과 보고)
- 맥락: 지워 달라는 요청을 끝내고 결과를 한 줄로 알릴 때(메신저·구두 보고).
- 한국어: orca 와 관련된 것은 ~에서 전부 없어졌다
- 설명: `X-related` 는 명사 뒤에 붙여 "X 와 관련된"을 만드는 손쉬운 조어. `everything` 뒤에 형용사가 오는 어순(`everything orca-related`)에 주의한다. `is gone` 은 동작(`has been removed`)이 아니라 지금 상태를 말해서 "확인해 보면 없다"로 들린다.
- 예문: Done. Everything orca-related is gone from the Claude Code config.
- 유사어: I've removed all the orca bits (구어, 동작 중심), All orca-related entries have been removed (격식, 수동), It's all cleaned out (더 가볍게)
- 반의어: is still in there (아직 안에 있다)

## "it was wired into"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (orca 제거 결과 보고)
- 맥락: 어떤 것이 시스템의 여러 지점에 물려 있었다고 말할 때(설정·훅·이벤트 설명).
- 한국어: 그것이 연결돼 있던
- 설명: `wire A into B` 는 전선을 잇듯 A 를 B 에 물린다는 뜻. 훅·콜백·이벤트처럼 "어딘가에 걸어 두는" 것에 잘 붙는다. 원문의 `all 13 hook events it was wired into` 는 관계대명사를 뺀 관계절이고 전치사 `into` 가 끝에 남았다.
- 예문: I removed the Orca agent hook command from all 13 hook events it was wired into. (작성)
- 유사어: it was hooked into (훅 문맥), it was registered on (이벤트 등록), it was attached to (평이)
- 반의어: was detached from (떼어 냈다), was never hooked up (애초에 연결된 적 없다)

## "which is just a catalogue"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (orca 제거 결과 보고)
- 맥락: 검색에 걸린 것이 실제 설치물이 아니라 목록일 뿐이라고 가볍게 일축할 때(결과 보고, 구어).
- 한국어: 그건 그냥 목록일 뿐이다
- 설명: 쉼표 뒤의 `which` 는 앞 명사(`the public plugin directory cache`)를 덧붙여 설명하는 계속적 용법. `just` 가 "신경 쓸 것 없다"를 맡는다. `catalogue` 는 영국식 철자이고 미국식은 `catalog`. 앞의 `The only "plugin" hit was …` 에서 `hit` 은 검색에 걸린 결과를 뜻한다.
- 예문: The only "plugin" hit was the public plugin directory cache, which is just a catalogue.
- 유사어: which is only a listing (평이), which is nothing more than an index (조금 격식), that's just a list of what's available (구어)

## "The Orca app itself stays"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (orca 제거 결과 보고)
- 맥락: 지운 범위와 남긴 범위를 가를 때(결과 보고, 구어와 문어 모두).
- 한국어: Orca 앱 자체는 그대로 둔다
- 설명: `itself` 가 "딸린 것들 말고 본체"를 강조한다. `stay` 는 자동사로 "남는다". `I left the app` 보다 짧고 주어가 대상이라 무엇이 남았는지가 먼저 들린다. 콜론 뒤에 남은 경로 둘을 나열했고, 다음 문장 `Say so if you want those gone too.` 로 선택을 넘긴다.
- 예문: The Orca app itself stays: `/usr/local/bin/orca` and `~/.orca/`.
- 유사어: I left the app itself alone (구어, 내가 주어), The app proper is untouched (문어, `proper` 는 "본체"), The app is still installed (상태 서술)
- 반의어: The app goes too (앱도 같이 없앤다)

## "Say so if you want those gone too."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (orca 제거 결과 보고)
- 맥락: 범위 밖이라 남겨 둔 것을 원하면 마저 하겠다고 열어 둘 때(메신저·구두).
- 한국어: 그것들도 없애고 싶으면 말해 줘
- 설명: `want + 목적어 + gone` 은 "~가 없어지기를 바란다"는 5형식. `want me to remove those` 보다 짧고 결과 상태를 말한다. `those` 는 앞 문장의 경로 둘, `too` 는 "이미 지운 것에 더해". `Say so` 가 문두에 와서 요청 방법이 먼저 들린다.
- 예문: The Orca app itself stays; say so if you want those gone too.
- 유사어: Let me know if you'd like those removed as well (공손), Just tell me if those should go too (구어), Shout if you want those out as well (아주 가볍게, 영국식)

## "Backend green (76 passed, ruff clean)."
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 테스트와 린트가 통과했다고 한 줄로 찍을 때(진행 보고·커밋 사이 메모, 구어).
- 한국어: 백엔드 통과(76건 통과, ruff 지적 없음)
- 설명: be 동사를 뺀 메모체. `green` 은 CI 의 초록불에서 온 말로 "전부 통과". `clean` 은 린터가 지적한 것이 없다는 뜻이다(`lint clean`, `typecheck clean`). 괄호 안에 근거 숫자를 붙이면 "통과"라는 주장이 검증 가능한 말이 된다.
- 예문: Backend green (76 passed, ruff clean). Now the frontend logic.
- 유사어: Backend tests all pass (평이), The backend suite is passing and lint is clean (완전한 문장), All good on the backend (구어, 근거 없음)
- 반의어: Backend red (실패), one test is failing (하나가 실패 중)

## "Now the frontend logic."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 한 단계를 끝내고 다음 단계로 넘어간다고 알릴 때(작업하며 중얼거리듯 남기는 보고, 구어).
- 한국어: 이제 프런트 로직 차례
- 설명: `Now + 명사구` 만으로 "다음은 이것"이 된다. 동사(`I'll do`, `let's move on to`)를 빼서 속도감이 난다. 같은 세션에 `Now the schema docs and the reply record.`, `Now the docs for the 8th reply, while tests run.`, `Now the edit.` 이 잇달아 나온다. `while tests run` 처럼 뒤에 절을 붙여 "기다리는 동안"을 더할 수도 있다.
- 예문: Now the docs for the 8th reply, while tests run.
- 유사어: Next up: the frontend logic (구어), Moving on to the frontend logic (조금 더 문장답게), On to the frontend (가장 짧게)

## "Teardown as its own step."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 정리 작업을 앞 단계와 묶지 않고 따로 하겠다고 밝힐 때(배포·작업 절차 메모).
- 한국어: 정리는 별도 단계로
- 설명: `teardown` 은 세워 둔 환경(worktree, 임시 서버)을 걷어 내는 일이고 `setup` 의 짝이다. 동사는 띄어서 `tear down`. `as its own step` 은 "남의 단계에 끼워 넣지 않고 제 단계로". 푸시가 확인된 뒤에만 지우겠다는 순서가 이 네 낱말에 담겼다.
- 예문: Pushed and verified. Teardown as its own step.
- 유사어: Cleanup comes separately (평이), I'll tear down in a separate step (완전한 문장), Cleanup is a step of its own (어순을 바꿔)
- 반의어: all in one go (한 번에 몰아서)

## "broke the string; fixing"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 방금 낸 사소한 실수와 조치를 한 줄로 알릴 때(작업 중 보고, 구어).
- 한국어: 문자열이 깨졌고, 고치는 중
- 설명: 원인(주어) + `broke` + 결과, 세미콜론 뒤에 `fixing` 한 낱말. 관사와 주어를 뺀 전보체지만 누가 무엇을 망가뜨렸는지는 빠지지 않는다. `my test title` 의 `my` 가 책임 소재를 밝힌다. `fixing` 은 `I'm fixing it` 의 줄임.
- 예문: Apostrophe in my test title broke the string; fixing.
- 유사어: An apostrophe in the test title ended the string early; I'm fixing it now (완전한 문장), My bad — unescaped quote; on it (더 구어)

## "Those are charts, not fetchers; the claim holds."
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (하위 에이전트의 확인 메모)
- 맥락: 의심스러운 곳을 들여다본 뒤 앞서 한 주장이 여전히 맞다고 결론 낼 때(검증 메모, 리뷰 답변).
- 한국어: 그건 차트지 데이터를 가져오는 코드가 아니다. 그러니 주장은 유효하다
- 설명: `A, not B` 로 헷갈린 것을 가르고 세미콜론 뒤에 결론을 붙였다. `hold` 는 자동사로 "성립한다, 무너지지 않는다"(`the assumption holds`). `the claim` 은 지시문이 확인하라고 한 문장("그 페이지들은 다른 엔드포인트를 부르지 않는다")을 가리킨다. `fetcher` 는 `fetch` 에 `-er` 을 붙인 개발자 말.
- 예문: Those are charts, not fetchers; the claim holds.
- 유사어: so the statement is still true (평이), so the assumption stands (같은 무게, `stand`), which confirms the claim (격식)
- 반의어: the claim falls apart (주장이 무너진다), that doesn't hold up (성립하지 않는다)
