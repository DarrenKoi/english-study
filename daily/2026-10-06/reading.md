# 2026-10-06 — 정독

> 세 단락 모두 배치 원문. 단락 1은 skewnono 서브에이전트에게 준 ALTITUDE 리뷰 지시문에서 첫 문단, 번호 목록을 여는 문장, 1번 항목, 맨 끝 문장을 이었다. 괄호 속 파일 경로는 덜어 냈고 목록을 여는 문장 끝의 콜론은 마침표로 바꿨다. 단락 2는 `/code-review low` 지시문의 "Turn 2 — findings" 규칙으로, 줄바꿈만 이었다. 단락 3은 pm_notes 구현 계획의 Goal, Architecture, Global Constraints 불릿 셋을 라벨과 기호를 떼고 이은 것. 앞의 둘은 "무엇을 봐 달라"는 주문이고 셋째는 "무엇을 만들라"는 주문이라, 명령문과 `must` 와 현재형 서술이 어디서 갈리는지 견줘 읽기 좋다.

## 단락 1

READ-ONLY code-quality review (do not edit, stage or commit anything). Angle: **ALTITUDE** — is each change made at the right depth, or is it a special case / bandaid layered on top of a shared mechanism that should have been changed instead? Specific places I suspect are at the wrong depth — evaluate each and tell me the deeper/more general change if there is one, or say it is fine where it is. Block identity is reconstructed in the frontend (`blockOrdinals`, `blocksOfPoint`, `tagBlocks` infer which Summary block a data row belongs to from row order). The backend knows the block while building rows. Should the contract carry a block index/name per row instead? Weigh against: `backend/afm/MIGRATION.md` treats the payload as office-contract surface, and the office adapter is still a stub. Be decisive and concise; I will apply only the ones that are clearly net simpler and do not change the office contract without the user's say-so.

**문법·구조**: 첫 문장은 동사 없는 표제이고 괄호 속에 명령문 하나를 넣었다. 둘째 문장은 `is each change made …, or is it …` 로 묻는 선택의문문. `layered on top of a shared mechanism` 은 과거분사가 `bandaid` 를 뒤에서 꾸미고 그 `mechanism` 을 다시 `that should have been changed instead` 가 꾸민다. `should have been + p.p.` 는 조동사·완료·수동이 겹친 형태로 "고쳤어야 했는데 고치지 않은"이라는 뜻. 셋째 문장의 `places I suspect are at the wrong depth` 는 관계절 안에 `I suspect` 가 끼어든 꼴이라 `are` 의 주어는 `places` 다. 대시 뒤로는 명령문 셋(`evaluate`, `tell`, `say`)이 이어지고 `if there is one` 의 `one` 은 `change` 를 받는다. 넷째와 다섯째 문장에서 볼 것은 태. 프론트 쪽은 수동(`is reconstructed`)이라 누가 했는지보다 어디서 벌어지는지가 드러나고 백엔드 쪽은 능동(`knows`)이어서 "이미 아는 쪽"이 주어에 선다. 괄호 속 `infer which Summary block a data row belongs to from row order` 는 `infer A from B` 틀인데 A 자리에 간접의문문이 들어가 `to` 와 `from` 이 맞붙었다. `while building rows` 는 주어가 같아서 줄인 동시 표현. 여섯째 문장은 `Should … instead?` 로 제안을 질문에 담았고 일곱째는 `Weigh against:` 한 줄로 반대 근거를 붙였다. 마지막 문장의 관계절 `that are clearly net simpler and do not change …` 에는 서술어가 둘이라 두 조건을 다 채워야 적용 대상이 된다.

**핵심 표현**: `layered on top of a shared mechanism` — 아래를 고치지 않고 위에 덧댔다는 지적. / `say it is fine where it is` — "문제없음"도 답으로 받겠다는 출구. / `without the user's say-so` — 허락 없이는 넘지 않을 선.

**격식 짝**: (작성)
- refined: Please assess whether each change has been made at the appropriate level, or whether it merely works around a shared mechanism that ought to have been modified.
- plain: For each change, tell me whether it's fixed in the right place or it's just a patch on top of something we should've fixed instead.

<sub>출처: transcript:skewnono-v3-nuxt (서브에이전트 ALTITUDE 리뷰 지시문)</sub>

---

## 단락 2

Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong condition, off-by-one, null/undefined deref where adjacent lines show the value can be absent, removed guard, falsy-zero check, missing `await`, wrong-variable copy-paste, error swallowed in a catch that should propagate. Also flag — still from the hunk alone — new code that duplicates an existing helper visible in the diff context, and dead code the diff leaves behind. Do **not** flag style, naming, perf, missing tests, or anything outside the hunk. Output at most **4 findings**, most-severe first, one line each: `path/to/file.ext:123 — what's wrong and the concrete failure`. If nothing qualifies, output exactly `(none)`. Do not call the ReportFindings tool even if it is available.

**문법·구조**: 여섯 문장이 모두 명령문이다(`Flag`, `Also flag`, `Do not flag`, `Output`, `output`, `Do not call`). 규칙을 적는 글은 주어 없이 동사로 시작한다. 첫 문장의 콜론 뒤는 관사 없는 명사구 여덟 개. 버그 유형의 이름표라서 `a` 를 뗐다(`removed guard`, `missing await`). 눈여겨볼 것은 줄인 관계절 셋이다. `bugs (that are) visible from the hunk alone`, `error (that is) swallowed in a catch`, `an existing helper (that is) visible in the diff context`. 그 가운데 `error swallowed in a catch that should propagate` 는 한 번 더 읽어야 한다. `that should propagate` 가 바로 앞의 `catch` 가 아니라 `error` 를 꾸민다. 전파됐어야 할 오류가 catch 에서 삼켜졌다는 말이고 관계절이 선행사에서 떨어진 예. `dead code the diff leaves behind` 는 목적격 관계대명사를 뺀 꼴이다. `where adjacent lines show the value can be absent` 는 `where` 절이 `deref` 를 한정해 "근거가 옆에 있을 때만"으로 좁힌다. 둘째 문장은 대시 사이에 `still from the hunk alone` 을 끼워 조건을 되풀이했다. 부정 명령 뒤의 나열은 `and` 가 아니라 `or` 로 묶는다(`style, naming, perf, missing tests, or anything outside the hunk`). 넷째 문장은 쉼표로 덧말 둘을 붙여 개수(`at most 4`), 순서(`most-severe first`), 길이(`one line each`)를 한꺼번에 정했다. 마지막의 `even if it is available` 은 "쓸 수 있더라도"라는 양보.

**핵심 표현**: `visible from the hunk alone` — 검토 범위를 조각 하나로 묶는 말. / `dead code the diff leaves behind` — 변경이 남기고 간 것. / `If nothing qualifies, output exactly (none).` — 빈 결과에도 정해진 답을 준다.

**격식 짝**: (작성)
- refined: Should no finding meet these criteria, respond with `(none)` and nothing else.
- plain: If there's nothing worth flagging, just write `(none)`.

<sub>출처: transcript:skewnono-v3-nuxt (서브에이전트 `/code-review low` 지시문)</sub>

---

## 단락 3

Convert the 11 Markdown documents in `ai-dt/ai-terms-and-technologies/` into a polished, fully offline HTML learning portal that opens directly from `html/index.html`. A standard-library Python builder parses the repository's current Markdown subset into semantic HTML, rewrites collection links, and generates one checked-in page per source document. Shared CSS provides the editorial, responsive, theme-aware visual system; a small shared JavaScript file adds filtering, mobile navigation, progress, theme persistence, and active-table-of-contents behavior without fetching content. All reading functions must work from `file://` without a server, CDN, package install, or network request. JavaScript is progressive enhancement: article content and basic navigation remain usable when it is disabled. Stage and commit only the files named in each task; preserve unrelated working-tree changes.

**문법·구조**: 문장의 꼴이 세 번 바뀐다. 첫 문장은 목표라서 명령문(`Convert A into B`). 둘째와 셋째는 설계 설명이라 현재형 서술이고 넷째부터는 제약이라 `must`, 현재형 단언, 명령문이 차례로 나온다. 첫 문장의 `a polished, fully offline HTML learning portal` 은 형용사가 평가(`polished`), 성질(`fully offline`), 종류(`HTML learning`) 순으로 쌓였고 `that opens directly from …` 관계절이 뒤를 받친다. 둘째 문장은 주어 하나에 동사 셋을 나란히 걸었다(`parses …, rewrites …, and generates …`). `one checked-in page per source document` 의 `per` 는 "문서 하나에 페이지 하나". 셋째 문장은 세미콜론 양쪽에 CSS 와 JavaScript 의 몫을 나눠 놓았고 끝의 `without fetching content` 가 "하지 않는 일"로 범위를 긋는다. 넷째 문장도 `without` 뒤에 명사 넷을 `or` 로 묶어 없어도 되는 것을 늘어놓았다. 다섯째 문장은 콜론 앞이 정의, 뒤가 그 풀이. `remain usable when it is disabled` 에서 `remain` 은 형용사 보어를 받고 `it` 은 JavaScript 다. 여섯째 문장은 명령문 둘을 세미콜론으로 이었다. `the files named in each task` 는 과거분사가 뒤에서 꾸미는 꼴로 "각 작업에 이름이 적힌 파일".

**핵심 표현**: `opens directly from html/index.html` — 서버 없이 파일을 바로 연다. / `without fetching content` — 기능을 더하되 넘지 않을 선. / `preserve unrelated working-tree changes` — 내 일이 아닌 수정은 건드리지 않는다.

**격식 짝**: (작성)
- refined: JavaScript serves solely as a progressive enhancement; the article content and basic navigation shall remain usable in its absence.
- plain: JavaScript is just a nice extra. You can still read the article and get around with it turned off.

<sub>출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md</sub>
