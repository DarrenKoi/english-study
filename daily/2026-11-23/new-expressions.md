# 2026-11-23 — 새 표현

오늘 배치는 이 저장소의 야간 실행 기록 두 건(11-21, 11-22)입니다. 사람과 나눈 대화는 없고, 세션에 실린 영어는 하네스가 붙여 준 안내문뿐이에요. 환경 주의사항, MCP 서버 인증 안내, 에이전트·스킬 설명 목록에서 골랐습니다. 스킬 설명은 "이럴 때 써라"를 한두 문장에 눌러 담은 글이라서 `when + -ing`, 따옴표로 든 구어 트리거, `so that` 목적절이 많습니다. 이미 인덱스에 있는 것(`Treat this as a connection failure…`, `stand in for` 등)은 뺐습니다.

## "a planted `json.py` runs on `import json`"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (환경 주의사항)
- 맥락: 공격자가 미리 심어 둔 파일·코드를 가리킬 때(보안 문서·리뷰, 중립 격식)
- 한국어: 심어 둔 `json.py` 가 `import json` 때 실행된다.
- 설명: `plant` 는 "몰래 갖다 놓다"입니다. 증거를 조작할 때도 `plant evidence` 라고 해요. 과거분사 `planted` 가 명사 앞에 붙으면 "누군가 일부러 넣어 둔"이 됩니다. `run on X` 의 `on` 은 "X 가 일어나는 순간에"라는 계기를 가리킵니다(`on startup`, `on save`).
- 예문: A planted `.pth` file in the archive would run on the next interpreter start.
- 유사어: a malicious `json.py` (의도만 말함, 놓인 경위는 없음), a rogue file (제멋대로 끼어든 것, 구어), a booby-trapped archive (건드리면 터지게 꾸민 것, 생생한 구어)
- 반의어: a legitimate module, a vetted dependency

## "Otherwise carry on with the request and do not mention these servers."
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (MCP 인증 안내)
- 맥락: 예외 조건을 먼저 말한 뒤 "해당 없으면 하던 대로"를 붙일 때(지침·인수인계 메모)
- 한국어: 그 밖의 경우에는 요청을 그대로 진행하고 이 서버들은 언급하지 마라.
- 설명: 앞 문장이 `If the request depends on …` 이고, 문두 `Otherwise` 가 "그 조건이 아니면"을 한 단어로 받습니다. `carry on with` 는 "멈추지 않고 계속하다"로 영국식 어감이 조금 있어요. 미국식 문서라면 `go ahead with` 나 `proceed with` 가 더 흔합니다.
- 예문: If the build fails, ping me; otherwise carry on with the deploy and don't wait for my review.
- 유사어: proceed with the request (격식), go ahead with it (회화), keep going as usual (가장 평이)
- 반의어: hold off on the request, stop and flag it

## "a sign-in may still be good"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (MCP 인증 안내)
- 맥락: 토큰·세션·티켓이 아직 유효한지 말할 때(동료와 대화, 가벼운 문서)
- 한국어: 로그인이 아직 살아 있을지도 모른다.
- 설명: 여기서 `good` 은 "좋다"가 아니라 "유효하다"입니다. `This coupon is good until Friday.` 와 같은 쓰임이에요. 격식 문서에서는 `valid` 를 쓰고, 말로 할 때는 `still good` 이 자연스럽습니다. `may` 로 단정을 피했습니다.
- 예문: Try the old API key first; it may still be good until the end of the month.
- 유사어: may still be valid (격식·문서), might not have expired yet (풀어 쓴 말), is probably still live (구어, 세션·연결에)
- 반의어: has expired, has been revoked

## "Try that first, and tell the user only if it is refused."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (MCP 인증 안내)
- 맥락: 먼저 해 볼 일과 보고할 조건을 순서대로 못박을 때(운영 절차·지침)
- 한국어: 그것부터 해 보고, 거부당했을 때만 사용자에게 알려라.
- 설명: `only if` 는 "그 경우에만"으로 조건을 좁힙니다. `if only`(~이기만 하면 좋을 텐데)와 순서가 반대이니 헷갈리지 않게 봐 둡니다. `it is refused` 는 수동태인데, 누가 거부했는지는 중요하지 않고 시도가 막혔다는 사실만 필요해서입니다.
- 예문: Retry the upload once, and page the on-call engineer only if it is rejected again.
- 유사어: escalate only on failure (명사구로 줄인 런북체), let them know if it doesn't go through (회화), report it solely in the event of a refusal (매우 격식)
- 반의어: tell the user up front, report regardless

## "Do not report a capability as unavailable without first searching."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (MCP 서버 연결 안내)
- 맥락: 확인도 안 하고 "안 된다"고 답하지 말라고 할 때(지침·리뷰 코멘트, 격식)
- 한국어: 먼저 찾아보지도 않고 기능이 없다고 보고하지 마라.
- 설명: `report A as B` 는 "A 를 B 라고 보고하다"입니다. `without first -ing` 에서 `first` 가 `without` 과 동명사 사이에 들어가는 어순이 눈에 띄어요. `without searching first` 도 맞지만 앞에 둔 쪽이 글에서 더 단단하게 읽힙니다.
- 예문: Do not mark a test as flaky without first reproducing the failure locally.
- 유사어: check before you say it's not there (회화), don't rule it out until you've looked (구어, `rule out` = 배제하다), verify availability before reporting (격식·명사화)
- 반의어: assume it's missing, take its absence for granted

## "it locates code; it doesn't review or audit it"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (Explore 에이전트 설명)
- 맥락: 도구나 역할이 하는 일과 하지 않는 일의 경계를 그을 때(설계 문서·도구 소개)
- 한국어: 코드를 찾아 줄 뿐, 검토하거나 감사하지는 않는다.
- 설명: 세미콜론이 "하는 일 ; 안 하는 일"을 접속사 없이 맞세웁니다. `locate` 는 `find` 보다 격식 있고 "위치를 짚어 내다"에 가깝습니다. `audit` 은 기준에 맞는지 전수로 따져 보는 것이라 `review` 보다 무겁습니다.
- 예문: The linter flags style issues; it doesn't check whether the logic is correct.
- 유사어: it finds code, nothing more (회화), it's a search tool, not a reviewer (명사로 맞세움), its scope is limited to locating code (격식)

## "a web search result that does not settle the question"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (web-fetch 에이전트 설명)
- 맥락: 찾은 근거가 결론을 내기에 모자랄 때(조사 보고·기술 토론)
- 한국어: 질문에 결론을 내 주지 못하는 웹 검색 결과.
- 설명: `settle` 은 인덱스에 여러 번 올랐지만(`that settles it`, `settle it by running…`) `settle the question` 꼴은 처음입니다. 사람이 아니라 증거가 주어로 와서 "이 자료로는 판가름이 안 난다"가 돼요. 목적어로 `the question`, `the matter`, `the debate` 가 자주 옵니다.
- 예문: The benchmark alone does not settle the question; we still need numbers from production traffic.
- 유사어: is inconclusive (형용사 하나로, 격식), doesn't answer it either way (회화), leaves the question open (열린 채로 둔다는 쪽에 초점)
- 반의어: is conclusive, puts the question to rest

## "Proactively use when Claude Code is stuck"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (codex-rescue 에이전트 설명)
- 맥락: 일이 더 나아가지 않는 상태를 말할 때(스탠드업·페어 작업, 구어)
- 한국어: Claude Code 가 막혔을 때 먼저 나서서 써라.
- 설명: `be stuck` 은 "끼어서 못 움직이다"에서 온 말로, 문제를 못 풀고 있는 상태를 가리킵니다. `I'm stuck on this bug.` 처럼 `on` 으로 대상을 답니다. `Proactively` 는 "시키기 전에 먼저"이고 `actively`(활발하게)와는 다릅니다.
- 예문: I've been stuck on this race condition since Monday, so I'd like a second pair of eyes.
- 유사어: has hit a wall (더 세고 생생함), is blocked (남·외부 요인 때문에 못 나감), isn't making headway (격식 섞인 완곡)
- 반의어: is making progress, is unblocked

## "Do NOT answer from this page alone if the answer may be further in the file."
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (파일 읽기 잘림 안내)
- 맥락: 일부만 보고 판단하지 말라고 경고할 때(도구 메시지·리뷰 지침)
- 한국어: 답이 파일 뒤쪽에 있을지도 모르니 이 페이지만 보고 답하지 마라.
- 설명: `from X alone` 은 "X 하나만 근거로"입니다. `alone` 이 명사 뒤에 붙어 `only` 구실을 해요(`Price alone doesn't decide it.`). `further in the file` 은 "파일 더 안쪽에"로, `further down` 이라고도 합니다.
- 예문: Don't judge the migration from the summary alone if the details may be further down in the PR.
- 유사어: based solely on this page (격식), just going by this page (회화), on the strength of this page alone (근거의 무게를 말하는 문어)

## "picking up where you left off"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (back-to-office 스킬 설명)
- 맥락: 멈췄던 일을 그 자리에서 다시 이어 갈 때(아침 스탠드업·회의 재개, 구어)
- 한국어: 멈춘 데서부터 다시 이어 가기.
- 설명: `pick up` 은 "다시 집어 들다", `leave off` 는 "하다가 멈추다"입니다. 둘이 짝으로 굳어서 회의를 다시 열 때 `Let's pick up where we left off.` 가 정해진 문장처럼 쓰여요. 같은 설명에 나오는 `resume` 이 격식 쪽 짝입니다.
- 예문: I saved my notes last night, so this morning I just picked up where I left off.
- 유사어: resume (격식, 한 단어), get back to it (회화, 어디서부터인지는 말 안 함), continue from the last checkpoint (기술 문서)
- 반의어: start over, start from scratch

## "wants unfinished work recorded so it isn't lost overnight"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (leave-office 스킬 설명)
- 맥락: 남에게 시켜서 어떤 상태로 만들어 두고 싶다고 할 때(요청·요구사항 서술)
- 한국어: 밤사이 사라지지 않도록 못 끝낸 일을 적어 두고 싶어 한다.
- 설명: `want + 목적어 + p.p.` 는 "~가 …된 상태이기를 바라다"입니다. `wants someone to record unfinished work` 보다 짧고, 누가 하는지는 빼 버려요. 뒤의 `so (that) it isn't lost` 가 목적을 답니다. `overnight` 는 부사로 "밤사이에".
- 예문: She wants the rollback steps written down so they aren't forgotten by the next release.
- 유사어: wants a record of what's left (명사로), needs the open items logged (업무 어투), would like outstanding work captured (격식, `outstanding` = 미결)

## "work that has returned half-done"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (unlazy 스킬 설명)
- 맥락: 맡긴 일이 반쯤만 된 채 돌아왔을 때(리뷰·위임 후 피드백)
- 한국어: 하다 만 채로 돌아온 일.
- 설명: `half-done` 은 `half + 과거분사` 복합 형용사입니다(`half-finished`, `half-baked`, `half-written`). `return + 형용사` 는 "~한 상태로 돌아오다"로, `The package returned unopened.` 와 같은 틀이에요. `half-baked` 는 "설익은 생각"이라는 비난이 섞이니 일의 완성도만 말할 때는 `half-done` 이 안전합니다.
- 예문: The refactor came back half-done, with two of the five modules still on the old interface.
- 유사어: half-finished (거의 같음), incomplete (격식·중립), a half-baked job (구어, 깔보는 어감)
- 반의어: fully done, finished end to end

## "turning tribal knowledge into exact step-by-step commands"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (operations:runbook 스킬 설명)
- 맥락: 문서화되지 않고 사람끼리만 전해지는 지식을 말할 때(운영·온보딩 논의)
- 한국어: 구전 지식을 정확한 단계별 명령으로 바꾸기.
- 설명: `tribal knowledge` 는 팀 안에서 입으로만 전해지고 어디에도 적혀 있지 않은 지식입니다. 부족(tribe)의 구전에 빗댄 업계 용어예요. `turn A into B` 가 변환을 맡습니다. 뒤 항목의 `a process that lives in someone's head` 가 같은 뜻을 풀어 쓴 말이니 함께 익힙니다.
- 예문: Half of our deploy process is tribal knowledge, so new hires keep asking the same three people.
- 유사어: undocumented know-how (중립), institutional knowledge (조직에 쌓인 지식, 긍정적), stuff only Dana knows (구어)
- 반의어: documented procedure, written runbook

## "formalizing a process that lives in someone's head"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (operations:process-doc 스킬 설명)
- 맥락: 특정인만 아는 업무 절차를 문서로 옮기자고 할 때(회의·제안서)
- 한국어: 누군가의 머릿속에만 있는 절차를 공식화하기.
- 설명: `live in` 을 지식이나 데이터에 쓰면 "거기에 들어 있다"입니다. `The config lives in the repo root.` 처럼 개발자 말투에 흔해요. `formalize` 는 "정식 문서·규칙으로 만들다". 주어가 사람 머리라서 위험하다는 말(그 사람이 없으면 끝)이 은근히 실립니다.
- 예문: Right now the release checklist lives in Minsu's head, and that's a risk every time he's on leave.
- 유사어: exists only in someone's memory (격식), nobody ever wrote it down (회화), is undocumented (한 단어, 건조)
- 반의어: is written down, is documented

## "the team feels overallocated and you need the numbers"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (operations:capacity-plan 스킬 설명)
- 맥락: 일이 사람보다 많다는 느낌을 수치로 뒷받침해야 할 때(분기 계획·인력 논의)
- 한국어: 팀에 일이 과하게 배정된 것 같은데 수치가 필요하다.
- 설명: `overallocated` 는 가용 시간보다 많은 일이 배정된 상태로, 프로젝트 관리 용어입니다. `overworked`(과로한)가 사람의 피로를 말한다면 이쪽은 배정표의 문제를 말해서 감정이 덜 실려요. `need the numbers` 는 "느낌 말고 근거 수치"라는 뜻으로 정관사가 붙습니다.
- 예문: Everyone says we're overallocated this quarter, but I need the numbers before I ask for another hire.
- 유사어: stretched thin (구어, 얇게 펴졌다는 그림), over capacity (용량 기준), overcommitted (약속을 너무 많이 한 쪽에 초점)
- 반의어: underutilized, has slack

## "Channels a senior dev who has seen everything"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (ponytail 스킬 설명)
- 맥락: 누군가의 태도나 말투를 빌려 그 사람처럼 군다고 할 때(가벼운 글·농담)
- 한국어: 볼 꼴 다 본 시니어 개발자를 빙의한다.
- 설명: 동사 `channel` 은 원래 영매가 영혼을 불러 대신 말하는 것입니다. 거기서 "~의 기운을 받아 그 사람처럼 하다"가 됐어요. `has seen everything` 은 현재완료로 "겪을 만큼 겪어서 이제 놀랄 일이 없다"는 뜻이고, `seen it all` 이 더 흔한 꼴입니다.
- 예문: In code review she channels a QA engineer who has seen everything break at least once.
- 유사어: takes on the mindset of (격식·중립), acts like (가장 평이), does its best impression of (흉내, 농담조)

## "reading legwork delegated to a background agent"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (mattpocock-skills:research 스킬 설명)
- 맥락: 결과를 내기 전에 발로 뛰어야 하는 지루한 사전 작업을 말할 때(업무 분담)
- 한국어: 자료 읽는 품을 백그라운드 에이전트에게 넘기기.
- 설명: `legwork` 는 "다리 품", 곧 돌아다니며 모으고 확인하는 밑작업입니다. 셀 수 없는 명사이고 `do the legwork` 로 가장 많이 써요. 머리 쓰는 일과 대비되는 어감이 있어서 "판단은 내가, 품은 네가"라는 분담을 말하기 좋습니다.
- 예문: I'll make the call on the vendor, but can you do the legwork of collecting the three quotes?
- 유사어: grunt work (더 낮춰 부르는 구어), the groundwork (기초를 닦는 일, 긍정적), preliminary research (격식)

## "I'm torn between X and Y"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (llm-council 스킬 설명)
- 맥락: 두 선택지 사이에서 마음을 못 정했다고 털어놓을 때(회의·1:1, 구어)
- 한국어: X 와 Y 사이에서 갈팡질팡이다.
- 설명: `torn` 은 `tear`(찢다)의 과거분사로, 양쪽에서 잡아당겨 찢기는 그림입니다. 둘 다 끌려서 못 고른다는 뜻이라 `I can't decide` 보다 고민의 무게가 실려요. 선택지가 동사면 `torn between staying and leaving` 처럼 동명사로 맞춥니다.
- 예문: I'm torn between rewriting the parser and patching it one more time.
- 유사어: I can't decide between (가장 평이), I'm on the fence about (어느 쪽으로도 안 기운 상태, 구어), I'm weighing A against B (저울질 중, 격식 섞임)
- 반의어: I've made up my mind, I'm set on X
