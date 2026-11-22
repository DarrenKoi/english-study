# 2026-11-23 — 정독

두 단락 모두 하네스가 세션에 붙인 안내문입니다. 단락 1은 도구를 언제 어떻게 쓰는지 설명하는 글이고, 단락 2는 인증이 안 된 서버를 어떻게 다룰지 정한 절차예요. 둘 다 명령문이 뼈대인데, 명령마다 이유나 조건을 어떤 문장부호와 접속사로 붙였는지 봅니다.

## 단락 1

Use this to fetch and read web pages / URLs when you do not have a direct WebFetch tool of your own (if you do, just call it). Without one, this agent stands in for that tool: calling it to read a page is ordinary tool use, so the Agent tool's own advice on when to spawn does not apply. Reach for it whenever a public page holds the answer: a URL you were given, or a web search result that does not settle the question. Read the page rather than answer from memory. Put the full URL(s) in the prompt along with the question or task itself — a summary is a task, so ask it for the summary, not for the page's contents to summarize yourself; its report is what enters your context, so it should already be the answer. It runs in the foreground and its report comes back as this tool's result; send `run_in_background: true` (where available) only when you have independent work to do meanwhile.

**문법·구조**: 여섯 문장 가운데 넷이 명령문(`Use`, `Reach for`, `Read`, `Put`)으로 시작합니다. 그 사이에 평서문이 끼어서 이유를 댑니다. 콜론은 두 번 나오는데 쓰임이 달라요. 첫 번째(`stands in for that tool: calling it …`)는 앞말의 귀결을 풀고, 두 번째(`holds the answer: a URL …, or a web search result …`)는 예를 늘어놓습니다. `calling it to read a page is ordinary tool use` 는 동명사구가 주어이고, 뒤의 `so` 절이 거기서 나온 결론입니다. `Read the page rather than answer from memory` 는 `rather than` 뒤에 원형 동사가 와서 두 명령을 맞세워요. `a URL you were given` 은 관계대명사가 빠진 수동 관계절인데, 누가 줬는지는 몰라도 되기 때문에 수동입니다. 다섯째 문장은 대시와 세미콜론으로 세 토막이 이어지고 토막마다 `so` 가 들어갑니다. "사실, 그러니 이렇게 하라"가 두 번 반복되는 꼴이에요. `its report is what enters your context` 에서 `what` 절은 보어로, "네 맥락에 들어오는 것은 바로 그 보고서다"라고 초점을 줍니다. 마지막 `only when` 은 기본값이 "하지 않는다"임을 알립니다.

**핵심 표현**: `stand in for` 는 "대역을 서다"로, 여기서는 없는 도구의 빈자리를 메운다는 뜻입니다. `Reach for it` 은 손을 뻗어 집는 그림이라 "필요하면 주저 없이 써라"로 읽혀요. `settle the question` 은 증거가 주어일 때 "판가름을 내다". `of your own` 은 "네 몫으로 따로 있는"이고 `a room of my own` 과 같은 틀입니다.

**격식 짝** (작성):
- refined: Consult the source directly rather than relying on recollection.
- plain: Go read the page. Don't answer off the top of your head.
- refined: Where the search results prove inconclusive, retrieve the underlying page.
- plain: If the search doesn't settle it, just open the page.

<sub>출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (web-fetch 에이전트 설명)</sub>

---

## 단락 2

This session is non-interactive, so Claude cannot run the OAuth flow here. If the user's request depends on one of these servers (even if they didn't name it explicitly), or they ask about it, tell them that it needs to be authorized — for claude.ai connectors, via their claude.ai connector settings; for other servers, via `claude mcp` or /mcp in an interactive session — and that the capability is unavailable until they do. Otherwise carry on with the request and do not mention these servers. Do not ask the user for authorization codes, tokens, or callback URLs. For claude.ai Google Calendar, claude.ai Gmail, a sign-in may still be good: calling one of a server's tools by name (mcp__<server>__<tool>), or a ToolSearch query that contains the server's name, connects to it again, with the sign-in already held. Try that first, and tell the user only if it is refused.

**문법·구조**: 첫 문장이 사실과 그 결과를 `so` 로 잇고, 나머지는 그 사실 위에서 갈라지는 경우를 하나씩 처리합니다. 순서는 `If …`(해당하면), `Otherwise`(아니면), `Do not …`(어느 쪽이든 금지), `For …`(특정 서버의 예외), `Try that first`(예외의 절차)입니다. 둘째 문장이 가장 길어요. `tell them that A — … — and that B` 에서 `that` 을 두 번 써서 전할 내용이 둘임을 분명히 했고, 대시 한 쌍 사이에 "어디서 인증하는지"를 끼웠습니다. 그 안에서는 세미콜론이 두 경우를 가르고 `via` 가 수단을 댑니다. `until they do` 의 `do` 는 `authorize it` 을 받는 대동사예요. `they` 는 단수 `the user` 를 받는 단수 they 이고, 성별을 모를 때 쓰는 기본값입니다. 다섯째 문장은 주어가 `calling …, or a ToolSearch query that …` 로 길고 동사 `connects` 가 한참 뒤에 옵니다. `or` 로 묶인 주어는 가까운 쪽(단수 `query`)에 수를 맞춥니다. 끝의 `with the sign-in already held` 는 `with + 명사 + p.p.` 부대상황으로 "로그인이 이미 잡혀 있는 채로"라는 뜻입니다.

**핵심 표현**: `carry on with` 는 "하던 대로 계속하다". `may still be good` 의 `good` 은 "유효한"입니다. `by name` 은 관사 없이 "이름을 대서"이고 `call someone by name`, `mention it by name` 처럼 씁니다.

**격식 짝** (작성):
- refined: In all other cases, proceed with the request without reference to these servers.
- plain: If not, just keep going and don't bring the servers up.
- refined: The existing credentials may remain valid; attempt a connection before notifying the user.
- plain: The old login might still work, so try it before you say anything.

<sub>출처: transcript:-Users-daeyoung-Codes-english-study/821cb368 (MCP 인증 안내)</sub>
