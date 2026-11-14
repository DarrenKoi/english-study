# 2026-11-15 — 정독

## 단락 1

**Build for how it will be used.** A live deck gets narration and possibly discussion; a pre-read has to **carry the whole narrative itself**. An executive audience in a live meeting needs few words and highly visual slides. Detailed, word-heavy slides are sometimes right for subject-matter experts or for a deck read offline. Analytical reports **lean on** charts and tables. **Size a live deck to the talk**: about 1.5 to 2 minutes per slide, with time left for questions if there will be any.

**문법·구조**: 명령문 두 개(`Build for…`, `Size…`)가 앞뒤를 감싸고 그 사이를 현재시제 평서문이 채운다. 가운데 문장들은 주어만 바꿔 가며(a live deck, a pre-read, an executive audience, detailed slides, analytical reports) 같은 틀을 반복하는데, 이렇게 주어를 줄 세우면 연결어 없이도 비교가 된다. `how it will be used` 는 전치사 `for` 의 목적어로 온 명사절이고 미래 수동태다. 세미콜론은 `gets narration` 과 `has to carry` 를 대등하게 맞세운다. `a deck read offline` 의 `read` 는 과거분사라 [red]로 읽고 "오프라인에서 읽히는 deck"이다. `few words` 는 `a` 가 없어 "거의 없는"이라는 부정에 가깝다. 마지막의 `with time left for questions` 는 `with + 명사 + 과거분사` 로 부대 상황을 덧붙이고, `if there will be any` 는 "질문이 있을 예정이라면"이라는 계획을 말하므로 조건절인데도 `will` 이 들어갔다.

**핵심 표현**:
- `Build for how it will be used` — 용도에 맞춰 만들어라. `build for + 명사절` 은 "~을 염두에 두고 만들다".
- `are sometimes right for` — "~에게는 맞을 때도 있다". 단정하지 않고 예외를 인정하는 부사 `sometimes` 의 위치(be동사 뒤)를 봐 둔다.
- `lean on charts and tables` — 차트와 표에 기댄다. `rely on` 보다 그림이 살아 있다.

**격식 짝** (작성):
- refined: A document circulated in advance must be fully self-explanatory, as no presenter will be available to supply context.
- plain: If people read it before the meeting, it has to make sense without you there.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes (pptx 스킬 본문 "Deck content and flow", 연속된 항목 두 개)</sub>

---

## 단락 2

**If the deck came from a template, always pass `--original`.** A template may itself contain parts the XSD rejects, so a bare run can report failures you never caused — and **a genuine regression can hide among them**. `--original` baselines the schema and slide checks against the template, suppressing errors it already had. The structural checks — relationships, content types, charts — ignore `--original` and report template-inherited problems either way, so **read those on their own merits**. pptxgenjs emits chart XML PowerPoint refuses to open, and every other tool accepts: python-pptx opens those decks, LibreOffice renders them, the XSD passes them. **Every failure names its fix.** Fix it in the generator and rebuild.

**문법·구조**: 첫 문장은 조건절이 과거(`came`)이고 주절이 명령문이다. deck이 만들어진 것은 이미 끝난 일이고 지시는 지금부터라서 시제가 갈린다. 둘째 문장의 `may itself contain` 에서 `itself` 는 "템플릿 자체가 이미"라는 강조이고, `parts the XSD rejects` 와 `failures you never caused` 는 둘 다 목적격 관계대명사가 빠진 관계절이다. `so` 로 결과를 잇고 대시 뒤 `and` 로 더 나쁜 결과를 하나 얹는 순서가 깔끔하다. `suppressing errors it already had` 는 결과를 나타내는 분사구문이고 `had` 가 과거인 이유는 "고치기 전부터 있던"이기 때문이다. `chart XML PowerPoint refuses to open, and every other tool accepts` 는 관계절 두 개가 한 명사 `chart XML` 에 걸린 구조인데, 뒤쪽 `accepts` 가 타동사인데도 목적어가 없는 것으로 알아볼 수 있다. 콜론 뒤의 세 절은 접속사 없이 쉼표로만 나열해(asyndeton) "하나같이 통과시킨다"는 속도감을 준다. 마지막 두 문장은 네 단어, 일곱 단어로 짧게 끊어 지시를 못박는다.

**핵심 표현**:
- `a bare run` — 옵션 없이 그냥 돌린 실행. `bare` 는 "아무것도 안 붙인".
- `baselines A against B` — B를 기준선으로 삼아 A를 잰다. `baseline` 을 동사로 썼다.
- `report … either way` — 옵션이 있든 없든 보고한다. `either way` 는 "어느 쪽이든".

**격식 짝** (작성):
- refined: Pre-existing failures should be evaluated independently, since they are unaffected by the baseline option.
- plain: Those errors were already there, so look at each one separately.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes (pptx 스킬 본문 "File QA", 이어진 두 단락)</sub>

---

## 단락 3

An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus **marks the visible tab as seen**, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion **while the pane is unseen**.

**문법·구조**: 상태 전이 규칙을 적은 글이라 전부 현재시제이고, 문장마다 "언제"를 정하는 부사절이 붙는다. `after`(순서), `when`(시점), `while`(동시에 유지되는 상태), `if`(조건)가 각각 다른 일을 하므로 바꿔 쓰면 뜻이 달라진다. 셋째 문장은 `when` 절 안에 `while` 절이 들어 있어 "활성 탭에서 끝나는 순간, 그리고 그동안 클라이언트에 포커스가 있을 것"이라는 두 조건을 한 번에 건다. 다섯째 문장은 동명사 세 개(`Focusing…, switching…, or regaining…`)가 주어인데 `or` 로 묶였으므로 동사는 단수 `marks` 다. 여섯째 문장은 세미콜론 앞이 "이건 아니다", 뒤가 "실제로는 이렇다"로 나뉘고, 뒤 절만 수동태(`is created by`)다. 초점이 `done` 이라는 상태에 있고 만드는 주체는 덜 중요해서 수동을 골랐다. `can become` 의 `can` 은 능력이 아니라 "그런 경우가 생긴다"는 가능성이다.

**핵심 표현**:
- `reports idle` — `report` 뒤에 상태값을 바로 붙여 "idle 이라고 보고한다".
- `marks A as seen` — A를 본 것으로 표시한다. `mark A as + 형용사/분사`.
- `turn A into B` — A를 B로 바꾸다. 부정문에서는 "~한다고 B가 되지는 않는다".

**격식 짝** (작성):
- refined: A completed task is flagged as unread until the user brings its tab into focus.
- plain: It stays marked "done" until you actually look at it.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes (herdr 스킬 본문, 이어진 두 단락에서 앞 여섯 문장)</sub>
