# 2026-08-25 — 정독

## 단락 1

The interesting part wasn't adding a spinner — one already existed. It was that `setPending` **cannot see the first half of the wait**. The set is resolved by looking the URL's `msrs` ids up in `meas_hist`, so until that history answers there is no set key, no batch to fire, and `setPending` is *correctly* `false`. A flag that means "the batch is running" was doing duty as "we're waiting", and the two aren't the same interval.

That's why the symptom was worse than a missing spinner: with no pending flag, the panels fell through to their **empty states** — "비교할 측정을 추가하세요.", "이 파라미터의 sequence 데이터가 없습니다." The page wasn't silent during the wait, it was answering the question wrongly. DESIGN.md already names this ("a frozen previous page is not a loading state"); an empty state shown during a fetch is the same failure with more confidence.

**문법·구조**: 일곱 문장이 "예상 답 부정 → 진짜 원인 → 증상 재해석" 순으로 흐른다.
① 첫 두 문장은 분열 구조 `The interesting part wasn't X. It was that Y.` — 누구나 예상하는 답(스피너 추가)을 먼저 지우고, 진짜 발견을 `that` 절로 미룬다. 문장을 둘로 끊은 덕에 부정이 먼저 들리고 발견이 독립된 무게를 얻는다.
② 셋째 문장은 원인을 수동태(`is resolved by looking ... up`)로 두어 행위자를 지우고, 결과를 `there is no A, no B, and C` 세 병렬로 쌓는다. `correctly` 가 이탤릭인 이유가 이 단락의 요점이다 — 플래그 값은 정확하다. 문제는 "플래그가 틀렸다"가 아니라 "플래그의 정의가 좁다"는 것.
③ 넷째 문장 `A flag that means X was doing duty as Y` 는 과거진행형으로 "그동안 대신 일해 왔다"는 지속을 담고, `the two aren't the same interval` 로 앞의 두 인용구를 `the two` 하나로 받아 짧게 닫는다.
④ 둘째 단락은 콜론(`That's why ... :`) 뒤에 구체 증상을 나열한다. `The page wasn't silent during the wait, it was answering the question wrongly.` 는 `not A, but B` 를 쉼표만으로 처리한 구어적 대조 — 격식 문어라면 `was not silent; rather, it was ...` 가 되지만 이 쉼표 대조가 문장을 훨씬 날카롭게 만든다.
⑤ 마지막은 세미콜론으로 "문서가 이미 이름 붙인 원칙"과 "이번 사례는 그 원칙의 더 나쁜 변형"을 붙인다. 세미콜론은 두 절의 관계가 독자에게 자명할 때 접속사를 생략하는 장치다.

**핵심 표현**
- `doing duty as` — 원래 뜻과 다른 역할을 임시로 맡고 있다. 플래그·변수·상수가 이름과 다른 용도로 쓰일 때.
- `fell through to their empty states` — 조건이 하나도 안 맞아 기본 분기로 떨어졌다. UI 에서 "로딩도 데이터도 아닌 빈 화면"이 뜨는 메커니즘을 정확히 말한다.
- `the same failure with more confidence` — 같은 실패의 더 확신에 찬 버전(새 표현 참조).

**격식 짝**
- refined: A flag that means "the batch is running" was doing duty as "we're waiting", and the two aren't the same interval.
- plain: We were using the "batch is running" flag as our "please wait" sign, but those aren't the same thing. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt 3ae7de12</sub>

---

## 단락 2

When a program types for you, it can send a keystroke two ways:

- **"Press physical key number 23"** — like a real keyboard does.
- **"Here, take the letter I as text"** — no key involved, just the character.

The typing library we use picks the first way for small letters, and the second way for anything needing Shift. That's a quirk of the library, not something I chose.

RCS is a window showing a screen far away. It listens for *key presses* and relays them to the machine. When we handed it "take the letter I as text," there was no key press to relay — so it threw it away. Small letters arrived because they came as real key presses.

That's why exactly `I T C !! O S S` vanished and not one small letter did.

**문법·구조**: 사용자가 "explain to me in plain words" 라고 요청해 받은 답이다. 같은 내용을 앞서 `KEYEVENTF_UNICODE`·`VkKeyScan` 으로 설명한 기술 버전이 있으니, 이 단락은 plain 레지스터가 어떻게 만들어지는지 보여 주는 표본이다.
① 법칙과 사건을 시제로 가른다. 시스템이 늘 하는 일은 현재형(`can send`, `picks`, `listens`, `relays`), 그날 일어난 일은 과거형(`handed`, `threw`, `arrived`, `vanished`). 독자는 시제만으로 "원리"와 "그때 벌어진 일"을 구분한다.
② 전문 용어를 인용문으로 바꿨다. 이벤트 플래그 대신 `"Here, take the letter I as text"` — 기계에게 말을 시키는 의인화가 plain 설명의 핵심 장치다.
③ `RCS is a window showing a screen far away.` — 정의문. 관계절 `which shows` 대신 현재분사 후치수식 `showing` 으로 짧게. plain 설명에서는 문장당 개념 하나.
④ `there was no key press to relay — so it threw it away` — 대시 뒤 `so` 로 인과를 구어처럼 잇는다. 격식 문어라면 `; consequently,` 가 올 자리.
⑤ 마지막 문장 `That's why exactly X vanished and not one small letter did.` — `not one` 은 `none` 보다 강한 부정이고, `did` 는 `vanished` 를 받는 대동사. 증거(대문자만 사라짐)와 설명(대문자만 다른 경로)을 한 문장에 맞물린다.

**핵심 표현**
- `a quirk of the library, not something I chose` — 이상한 동작의 출처를 사실 진술로 가르는 말(새 표현 참조).
- `hand it X` / `there was nothing to relay` — "넘겨줬는데 전달할 게 없었다"는 파이프라인 설명의 기본 틀.
- `not one small letter did` — 대동사 `did` 로 반복을 피한 강한 부정.

**격식 짝**
- plain (원문): When we handed it "take the letter I as text," there was no key press to relay — so it threw it away.
- refined: Because the unicode event carried neither a virtual-key nor a scan code, the relay had nothing to forward and silently discarded it. (작성 — 같은 세션의 기술 설명을 문어로 다듬음)

<sub>출처: transcript:[assistant] auto-recipe-creator 6e44bf1a</sub>

---

## 단락 3

**Four I deliberately left alone**, and I want to be straight that this is me narrowing your request:

`PRE_CLICK_SETTLE` (0.6), `CLICK_HOLD` (0.15), `ALT_SETTLE` (0.3), `SHIFT_SETTLE` (0.12).

These aren't pacing — they're the reason a click or keystroke lands at all. Each one came out of an office round: the cursor-arrives-but-nothing-happens problem, and the vanishing-capitals problem. Shaving them risks a demo that doesn't work rather than a demo that's slow, and those aren't comparable outcomes. Together they only account for a couple of seconds anyway; the 12s came from the pauses you were actually watching.

**문법·구조**: "30% 줄여 달라"는 요청에 대해 넷은 안 줄였다고 밝히는 대목. 요청을 좁힌 사실을 숨기지 않으면서 근거를 다섯 문장에 담는다.
① 첫 문장은 목적어 도치 `Four I deliberately left alone` — `I left four alone` 을 뒤집어 숫자를 문두에 놓는다. 바로 앞 표(30% 줄인 항목들)와 대비되는 "안 줄인 넷"을 세는 방식이다. 뒤의 `this is me narrowing your request` 는 `me + -ing` 구문으로 자기 행동을 3인칭처럼 명명한다 — 상대가 이의를 제기할 지점을 먼저 드러내는 셈.
② `These aren't pacing — they're the reason X lands at all.` — `not A — B` 대조에 `at all` 을 붙여 "속도 문제"에서 "성립 문제"로 격을 올린다.
③ `the cursor-arrives-but-nothing-happens problem` — 절 전체를 하이픈으로 묶어 형용사로 쓴 합성어. 이름 없는 현상에 임시 이름을 붙이는 구어 기술 글의 관용 장치다.
④ `Shaving them risks A rather than B, and those aren't comparable outcomes.` — 동명사 주어 `Shaving them` 이 `risks` 를 받는다. `rather than` 으로 두 결과를 나란히 놓은 뒤 `those aren't comparable` 로 저울 자체를 치운다.
⑤ 마지막은 세미콜론 대조. `Together they only account for a couple of seconds anyway; the 12s came from the pauses you were actually watching.` — 숫자를 앞뒤에 놓아 "안 건드린 건 작고, 당신이 느낀 건 이미 줄였다"를 접속사 없이 전한다. `actually` 는 여기서 "실제로 체감한" 쪽이다.

**핵심 표현**
- `I want to be straight that …` — 불리한 사실을 먼저 꺼내는 어투(새 표현 참조).
- `this is me narrowing your request` — 자기 행동을 명명해 상대가 이의를 제기할 지점을 명확히 만드는 표현.
- `account for (a couple of seconds)` — 전체 중 얼마를 차지한다.

**격식 짝**
- refined: Reducing these four intervals would trade a slow demonstration for one that may not function, and the two outcomes are not comparable. (작성)
- plain (원문): Shaving them risks a demo that doesn't work rather than a demo that's slow, and those aren't comparable outcomes.

<sub>출처: transcript:[assistant] auto-recipe-creator 6e44bf1a</sub>
