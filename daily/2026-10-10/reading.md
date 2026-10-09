# 2026-10-10 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 e-beam 페이지 현황 조사 노트의 머리에 붙은 방법 주석을 그대로 옮겼다. 단락 2는 AFM 구조 검토 세션에 딸려 온 Herdr 스킬 문서에서 에이전트 상태 `idle`·`done` 을 설명하는 이어진 두 문단이다. 단락 3은 pm-notes 세션에 딸려 온 Artifact 디자인 지침의 `Read the request first` 절에서 이어진 세 문단을 붙였다. 1은 수동태로 "어디까지 읽었나"를 밝히는 글, 2는 시간·조건절로 상태 규칙을 적는 글, 3은 명령문으로 판단 기준을 주는 글이어서 문체가 서로 다르다.

## 단락 1

**Method note for the report writer.** Source is the local repo at `main` `8d176861` (2026-10-09). Backend `contracts.py` files and mock module docstrings **were read directly**. The two page-value research docs **were read in full**. Frontend views **were NOT read line by line**: chart types, column names and labels below come from targeted greps over each view (ECharts `type: '…'`, `accessorKey`, label strings, download helpers, `route.query`). **Where a claim rests on a grep rather than a full read it says so.** **Nothing was run**; no browser, no office data. All paths are repo-relative.

**문법·구조**: 여덟 문장 가운데 넷이 수동태다. `were read directly`, `were read in full`, `were NOT read line by line`, `Nothing was run`. 읽은 사람이 누구인지는 중요하지 않고 "무엇이 어떤 깊이로 읽혔는가"가 정보라서 대상을 주어로 세웠다. 수동태 뒤에 붙는 부사구가 매번 달라지는 점을 본다. `directly`(직접), `in full`(전부), `line by line`(한 줄씩)이 읽기의 깊이를 세 단계로 가른다. 넷째 문장은 `NOT` 을 대문자로 써서 앞 두 문장과 반대임을 알리고 콜론 뒤에서 그 대신 무엇을 했는지 능동 현재 `come from` 으로 푼다. 여섯째 문장의 `Where` 는 "~인 곳에서는, ~인 경우에는"이라는 조건 접속사이고 `rather than` 이 두 명사구 `a grep` 과 `a full read` 를 맞세운다. `it says so` 의 `so` 는 앞 절 전체를 받는다. 첫 문장과 일곱째 문장 뒷부분(`no browser, no office data`)은 동사 없는 명사구 조각인데 메모 문체에서는 이렇게 끊어 써도 된다. 시제는 조사 행위가 과거(`were read`), 문서가 지금 담고 있는 성질이 현재(`come from`, `rests on`, `are`)다.

**핵심 표현**: `were read in full` / `were NOT read line by line` — 읽은 깊이를 부사구로 가르기. / `Where a claim rests on a grep rather than a full read it says so.` — 근거가 약한 대목은 스스로 표시한다는 약속. / `Nothing was run; no browser, no office data.` — 실행 검증이 없었다는 한계를 가장 짧게.

**격식 짝**: (작성)
- refined: The frontend views were characterised by targeted searches rather than a complete reading; any claim that depends solely on such a search is identified as such.
- plain: I didn't read the frontend files all the way through. I grepped them, and I say so wherever that's all I did.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md</sub>

---

## 단락 2

An agent **that first opens at its prompt** reports `idle`, including in a background pane. **After** a working or blocked agent completes, it reports `done` **when** its tab or workspace is in the background. It reports `idle` when it completes in the active tab **while** the foreground client is focused. **If** the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus **marks the visible tab as seen**, so `done` becomes `idle`. Switching away **does not turn** an existing `idle` status **into** `done`; `done` is created by a later completion while the pane is unseen.

**문법·구조**: 규칙을 적는 글이라 동사가 모두 단순현재다. 볼 것은 접속사 넷의 분업이다. `After` 는 순서(끝난 다음), `when` 은 그 시점의 조건(탭이 뒤에 있을 때), `while` 은 동시에 이어지는 상태(포커스가 있는 동안), `If` 는 예외 가정을 맡는다. 둘째 문장은 `After … , it reports … when …` 으로 앞뒤에 부사절을 하나씩 달았고, 셋째 문장은 `when … while …` 로 부사절 안에 부사절을 넣었다. 시간·조건 부사절 안에서는 미래 일이어도 현재형을 쓴다는 규칙이 문장마다 지켜진다(`completes`, `is`). 첫 문장의 `that first opens at its prompt` 는 주격 관계절로 어떤 에이전트인지 좁힌다. 넷째 문장의 `can become` 은 "늘 그런 것은 아니고 그럴 수 있다"는 가능성 표시여서 다른 문장의 단정과 구별된다. 다섯째 문장은 동명사 셋(`Focusing`, `switching`, `regaining`)을 `or` 로 묶은 주어에 단수 동사 `marks` 를 썼다. `or` 로 이으면 동사는 가까운 쪽에 맞춘다. 마지막 문장은 세미콜론 앞이 능동 부정(`does not turn A into B`), 뒤가 수동(`is created by`)이다. "이렇게는 안 생기고 저렇게 생긴다"를 태를 바꿔 대비했다.

**핵심 표현**: `reports idle` / `reports done` — 상태 값을 목적어로 받는 `report`. / `marks the visible tab as seen` — `mark A as B` 로 상태를 바꾼다는 말. / `does not turn an existing idle status into done` — `turn A into B` 의 부정으로 오해를 미리 막기.

**격식 짝**: (작성)
- refined: Completion is reported as `done` only if the pane is not visible at the time; otherwise the result is deemed to have been seen and the status reverts to `idle`.
- plain: If you weren't looking at the pane when it finished, it shows `done`. If you were, it just goes back to `idle`.

<sub>출처: transcript:skewnono-v3-nuxt [user] (세션에 딸려 온 Herdr 스킬 문서)</sub>

---

## 단락 3

Many requests **call for** a more utilitarian treatment: a plan, a memo, a demo. Make it polished, with real typographic hierarchy, considered spacing, and a proper palette, **but avoid over-designing**. Most pages don't need a flashy, gigantic hero. Keep flourishes tasteful and limited. Some requests call for an editorial treatment: a landing page, a game, an app or tool **they'll keep or share**. **If unsure**: a well-composed page is always acceptable; an over-designed visual identity **sometimes isn't**.

**문법·구조**: 서술문과 명령문이 번갈아 나온다. 첫 문장과 다섯째 문장은 `Many requests call for …`, `Some requests call for …` 로 틀이 같고 콜론 뒤에 예시 셋을 명사구로 늘어놓는다. `Many` 와 `Some` 의 대비만으로 어느 쪽이 기본값인지 드러난다. 둘째 문장은 명령문 `Make it polished` 에 `with` 구로 구체 조건 셋을 달고 `but avoid` 로 한계를 긋는다. `make + 목적어 + 형용사` 5형식이다. `considered spacing` 의 `considered` 는 "깊이 생각한"이라는 형용사로 쓰인 과거분사다. 셋째 문장은 평서 부정 `don't need` 로 한 박자 쉬고 넷째 문장이 다시 명령문 `Keep + 목적어 + 형용사`. `tasteful and limited` 두 형용사가 보어다. 다섯째 문장 끝의 `they'll keep or share` 는 목적격 관계대명사를 뺀 관계절이다. 마지막 문장의 `If unsure` 는 `If you are unsure` 에서 주어와 be 동사를 줄였다. 세미콜론 양쪽은 `always acceptable` 과 `sometimes isn't` 로 빈도 부사가 맞서고 뒤쪽은 `acceptable` 을 되풀이하지 않고 `isn't` 에서 끊었다.

**핵심 표현**: `call for` — 상황이 무엇을 요구한다는 뜻(`This calls for a different approach`). / `Make it polished, … but avoid over-designing.` — 하라는 것과 넘지 말 선을 한 문장에. / `If unsure: A is always acceptable; B sometimes isn't.` — 망설일 때 고를 기본값을 주는 틀.

**격식 짝**: (작성)
- refined: Where the appropriate treatment is unclear, a restrained, well-composed page is the safer default, since an elaborate visual identity may not suit the request.
- plain: Not sure how fancy to go? Keep it clean. A tidy page never hurts, but an overdone one sometimes does.

<sub>출처: transcript:pm-notes [user] (세션에 딸려 온 Artifact 디자인 지침)</sub>
