# 2026-10-25 — 정독

## 단락 1

Designing against guessed data. No thickness/SE office source exists yet (`docs/datatables/` has no vendor for it). Every mocked schema decision (site layout, spectra sampling, fit metadata fields) is a guess that the real tool's export will contradict; the repo's own rule (mock must mirror office fidelity, unknowns marked `OFFICE-VERIFY`) limits the damage only if the UI is built against the *contract shape*, not the mock's conveniences. Skewvoir already learned this lesson — its readiness matrix gates whole views when site-layout identity is unknown. Showing derived thickness as bare truth. A thickness number with no MSE/residual/correlation context looks identical whether the fit is excellent or degenerate (thickness↔n correlation). Every serious vendor tool shows fit quality; SKEWNONO must too, or engineers will trust bad numbers — and the bad numbers will be most convincing exactly when the model is wrong.

**문법·구조**: 위험 두 개를 각각 **동명사구 제목**(`Designing against …`, `Showing … as …`)으로 열고 근거 문장을 붙였다. 제목에 주어·동사가 없으니 "이 행위 자체가 위험"이라는 뜻이 된다. `is a guess that the real tool's export will contradict` 의 `that` 절은 목적격 관계절로, `contradict` 의 목적어가 `a guess` 다. 미래 `will` 은 "아마"가 아니라 "반드시 그렇게 된다"는 예측에 가깝고요. 세미콜론(;)이 두 번 나와 "사실 ; 그 사실의 함의"를 한 문장 안에 붙인다. `whether the fit is excellent or degenerate` 는 양보의 `whether A or B` 로 "어느 쪽이든 똑같아 보인다"를 만든다. 마지막 문장은 `must too, or …` 로 의무와 그걸 어겼을 때의 결과를 잇고 대시 뒤 `and` 절에서 역설로 끝맺는다.

**핵심 표현**:
- `limits the damage only if …` — 규칙이 있다는 안심을 조건부로 낮춘다. "효과는 있지만 이 조건에서만"이라는 정밀한 평가다.
- `already learned this lesson` — 같은 저장소의 다른 기능이 먼저 겪은 일을 선례로 끌어온다. 설득할 때 가장 값싼 근거다.
- `looks identical whether … or …` — 겉으로 구별이 안 된다는 점을 들어 "표시가 꼭 필요하다"로 잇는다.

**격식 짝** (작성):
- refined: Unless fit-quality context accompanies every derived value, users cannot distinguish a reliable thickness from a degenerate one.
- plain: If you don't show the fit quality next to the number, nobody can tell a good thickness from a bad one.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-24-optical-metrology-analysis-display-notes/display_approach_tradeoffs.md (Three biggest risks 1·2, 번호 생략)</sub>

---

## 단락 2

No. Re-running it does not touch stored documents. Previously stored rows, including the visit and page-view rows, stay exactly as they are. … OpenSearch mapping updates can only add fields. It cannot change or remove an existing field, and if the body tried to, the request would be rejected rather than applied. Documents are not rewritten, so there is no reindex. The practical effect is that rows written before the update simply have no `referer` field, and rows written after the code deploy but before the mapping update keep it in `_source` only, readable per document but not searchable. Nothing is lost either way.

**문법·구조**: 예/아니오 질문에 답하는 모범 구조. `No.` 한 단어로 결론부터 주고 짧은 평서문으로 이유를 쌓은 뒤 `Nothing is lost either way.` 로 다시 결론을 닫는다(샌드위치). `if the body tried to` 에서 `to` 뒤 동사(`change or remove`)를 생략하는 **대부정사**가 쓰였다. 이 가정법 과거(`tried … would be rejected`)는 실제론 안 일어날 일을 가정해 안전성을 보여 주는 장치. `Documents are not rewritten, so …` 의 수동태는 "누가"보다 "문서에 무슨 일이 생기나"가 중요해서 고른 것이고요. `rows written before …` / `rows written after … but before …` 는 과거분사 후치 수식 두 개를 대구로 놓아 두 경우를 나눈다. `readable per document but not searchable` 은 형용사구를 콤마 뒤에 붙여 상태를 덧붙이는 분사구문식 보충이다.

**핵심 표현**:
- `stay exactly as they are` — 기존 데이터가 그대로라는 안심 문장.
- `would be rejected rather than applied` — 잘못돼도 안전한 쪽으로 실패한다는 설명.
- `The practical effect is that …` — 원리 설명 뒤 "그래서 실제로 보이는 건"으로 넘어가는 다리.

**격식 짝** (작성):
- refined: Re-executing the script leaves all previously indexed documents unaltered.
- plain: Running it again won't touch anything that's already stored.

<sub>출처: transcript:skewnono_v3_nuxt b4fc9877 (본문 + "Additive mapping update" 항목 일부를 이어 붙임, 생략은 …)</sub>

---

## 단락 3

The built-in is turned off right now. Your `~/.pi/agent/settings.json` has `"extensions": ["-builtin:mcp"]`. You didn't add that line: pi-mcp-adapter writes it automatically the first time it starts, so its own `/mcp` takes over. No MCP servers are configured. I didn't find any `mcp.json`, `mcp-adapter.json` or `.mcp.json` for pi under your home directory. The adapter is loaded but has nothing to connect to. Nothing you have installed requires the adapter. pi-subagents mentions it, but only to give MCP tools to child agents, which is optional.

**문법·구조**: 조사 결과를 "주장 한 줄 → 증거 한두 줄" 묶음으로 세 번 반복한 글. 주장 문장(`The built-in is turned off right now.`, `No MCP servers are configured.`, `Nothing you have installed requires the adapter.`)은 모두 현재 시제의 상태 진술이고 증거 문장은 과거(`didn't find`, `didn't add`)로 "내가 확인한 행위"를 말한다. 시제가 "지금 상태 / 내가 한 확인"을 갈라 준다. `You didn't add that line:` 의 콜론은 "왜냐하면" 대신 이유를 바로 붙이는 역할. `the first time it starts` 는 접속사 없이 `the first time` 이 시간 부사절을 이끄는 구조다. 마지막 `but only to …, which is optional` 은 `only` 로 범위를 좁히고 계속적 용법 `which` 로 "그것도 선택 사항"이라는 평가를 덧붙인다.

**핵심 표현**:
- `takes over` — 다른 것의 역할을 넘겨받아 대신 맡다. 기능 충돌을 설명할 때 자주 쓴다.
- `has nothing to connect to` — `nothing to + 동사 + 전치사` 구조. "연결할 대상이 없다"를 짧게.
- `mentions it, but only to …` — 의존성이 있는 듯 보이지만 범위가 좁다고 정정할 때.

**격식 짝** (작성):
- refined: The adapter is currently loaded, although no server configuration exists for it to connect to.
- plain: It's loaded, but there's nothing for it to talk to.

<sub>출처: transcript:skewnono_v3_nuxt fc3f283c (What I found on this machine 목록을 이어 붙임)</sub>
