# 2026-10-31 — 정독

오늘은 repo 문서가 한국어뿐이었지만 트랜스크립트에 잘 쓴 영어 보고문이 있었다. 셋 다 원문 그대로 인용한다.

## 단락 1
The AFM endpoints already exist and already accept API tokens, so no new routes are needed. I measured this at home with a temporary token: `/api/afm/tools`, `/files`, file detail, profile (with `full=1`), image lists, `tiff.zip` and `images.zip` all returned 200, and the token returned 401 after I revoked it. The real gap is that the `/endpoints` reference page has no AFM section, so users cannot discover the endpoints or copy a working snippet. A delegate is adding an `AFM` group to `frontend/app/data/apiCatalog.ts` now. It is still running. One thing users would trip on: AFM filenames contain `#`, so a script must percent-encode them in the URL path. The new section will say so and ship pre-encoded examples. When the delegate returns I will review its diff, run the generated Python and curl snippets against the home server, check the page in a browser, then commit and push.

**문법·구조**: 시제가 단락의 뼈대다. 현재형(`exist`, `accept`, `has no`)은 지금의 사실, 과거형(`measured`, `returned`, `revoked`)은 직접 해 본 실측, 현재진행(`is adding`, `is still running`)은 지금 돌고 있는 작업, `will`(`will say so`, `will review`)은 다음 계획이다. 시제만 따라가도 "사실 → 근거 → 진행 중 → 계획" 순서가 보인다. 첫 문장은 요청의 전제("새 엔드포인트가 필요하다")를 `so no new routes are needed` 로 바로 뒤집고, 셋째 문장 `The real gap is that …` 이 진짜 할 일을 세운다. `When the delegate returns` 는 시간 부사절이라 미래 일인데도 현재형을 쓴다. 마지막 문장의 동사 넷(review, run, check, commit and push)은 순서대로 늘어놓고 `then` 하나로 마지막 단계를 끊었다.
**핵심 표현**: `The real gap is that …`(진짜 빠진 건 ~다), `would trip on`(걸려 넘어질 법한), `ship pre-encoded examples`(미리 인코딩한 예시를 함께 내놓다; ship 은 '출시하다'에서 '함께 내보내다'로 넓어진 뜻).
**격식 짝**:
- refined: The existing endpoints already support token authentication; what is missing is discoverable documentation. (작성)
- plain: The endpoints are already there and take tokens. What's missing is a docs page that shows them. (작성)

<sub>출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant] AFM 엔드포인트 중간 보고</sub>

---

## 단락 2
The page's general note says the API is rate-limited to 50 calls per 5 seconds, and the AFM group says AFM is exempt. Both are true but read as a contradiction. I left the general note alone. Say so if you want it reworded to name the exempt features. The example filename is today's mock file (`#261007#...`). It is illustrative, like `MSR_001` elsewhere on the page, and will not exist on the office server. If users want the tips or usage numbers precomputed instead of deriving them from the rows, that is a real new endpoint and a separate task.

**문법·구조**: "남은 결정" 목록에서 뽑은 문장들이라 하나하나가 짧다. 첫 문장은 `A says …, and B says …` 로 두 문서를 나란히 세우고, 둘째 문장 `Both are true but read as a contradiction` 이 사실(true)과 인상(read as)을 갈라 판정한다. 셋째·넷째 문장은 "내가 한 일(left alone) → 상대가 할 수 있는 일(say so)"로 결정권을 넘긴다. `want it reworded`, `want the numbers precomputed` 는 같은 `want + 목적어 + 과거분사` 구조가 두 번 나온다. 누가 할지는 빼고 결과 상태만 말하는 틀이다. 마지막 문장은 `If …, that is …` 로 조건이 성립하면 그건 별개 작업이라고 범위를 자른다. `instead of deriving` 은 전치사 뒤 동명사.
**핵심 표현**: `read as a contradiction`(모순처럼 읽히다), `leave X alone`(X 를 건드리지 않다), `a separate task`(별개 작업; 범위 밖이라는 선언).
**격식 짝**:
- refined: The two statements are individually accurate but may appear inconsistent to readers. (작성)
- plain: Both are right, but side by side they look like they disagree. (작성)

<sub>출처: transcript:skewnono-v3-nuxt d5f5ede9 [assistant] AFM 엔드포인트 최종 보고 "Open decisions"</sub>

---

## 단락 3
You own every subagent's work. Review the diff and write your own summary, don't pass through what it said. A second opinion is the same prompt against a different model. Agreement is high-signal. **Fresh subagents by default.** Give new work to a fresh subagent with consolidated scope, meaning the original brief, every later directive, and the prior agent's report and branch. This holds for a fix round, a follow-up, a retry, and the next queue item. Resume, message, or queue a follow-up on an existing subagent only when the new work strictly needs state that lives in that agent and is costly to move: its local checkout, its uncommitted changes, or a process it still runs, such as a dev server, a simulator, or a babysit watcher. A stop or hold order to a running agent is not reuse. A role such as a PR owner outlives its agent.

**문법·구조**: 지침문이라 명령문(`Review`, `write`, `Give`)과 짧은 정의문(`A second opinion is …`, `Agreement is …`)이 번갈아 나온다. 둘째 문장은 쉼표로 두 절을 이었는데(comma splice) 격식 문서라면 세미콜론이나 `rather than` 이 맞다. 리듬을 위해 일부러 끊은 문체다. `meaning …` 은 분사구문으로 앞의 추상어 `consolidated scope` 를 구체 목록으로 풀었다. `This holds for …` 는 "이 규칙은 ~에도 적용된다"로, 규칙의 적용 범위를 넓히는 데 자주 쓴다. `only when … strictly needs` 는 예외를 아주 좁게 허용하는 조건이고, 콜론 뒤에 그 상태의 예를 늘어놓았다. 끝 두 문장은 예외처럼 보이는 경우(정지 명령, 역할)를 정의로 정리한다. `outlive` 는 '~보다 오래 살다'에서 '수명이 ~보다 길다'로 쓰였다.
**핵심 표현**: `pass through what it said`(받은 말을 그대로 넘기다), `This holds for …`(이 규칙은 ~에도 해당한다), `outlives its agent`(그 에이전트보다 오래 남는다).
**격식 짝**:
- refined: Independent agreement between two models constitutes strong evidence. (작성)
- plain: If two different models say the same thing, you can trust it more. (작성)

<sub>출처: transcript:skewnono-v3-nuxt d5f5ede9 [user] poteto-mode 스킬 본문(붙여 넣은 스킬 텍스트, Subagents 절의 이웃한 두 단락)</sub>
