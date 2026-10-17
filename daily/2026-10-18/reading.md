# 2026-10-18 — 정독

## 단락 1

Never lazy about understanding the problem. The ladder shortens the solution, never the reading. Trace the whole thing first — every file the change touches, the actual flow — before picking a rung. Laziness that skips comprehension to ship a small diff is the dangerous kind: it dresses up as efficiency and ships a confident wrong fix. Read fully, then be lazy.

**문법·구조**: 첫 문장은 동사 없는 명령문이다. `(Be) never lazy about …` 에서 `be` 를 떨어뜨려 표어처럼 만들었다. 둘째 문장은 `shortens A, never B` 로 목적어 둘을 맞세운다. 같은 동사를 한 번만 쓰고 뒤쪽은 `never` 로 부정만 얹는 압축이다. 셋째 문장은 대시 사이에 동격구 두 개(`every file …`, `the actual flow`)를 끼워 `the whole thing` 이 무엇인지 풀어 준다. 넷째 문장이 이 단락의 핵심이다. 주어가 `Laziness that skips comprehension to ship a small diff` 로 길고, 관계절 안에 목적 부정사(`to ship`)까지 들어 있다. 그 긴 주어를 `is the dangerous kind` 라는 짧은 서술로 받고, 콜론 뒤에 `dresses up … and ships …` 두 동사로 왜 위험한지 설명한다. `ship` 이 같은 문장에 두 번 나오는데 앞쪽은 의도(작은 diff 를 내보내려고), 뒤쪽은 결과(틀린 수정을 내보낸다)다. 마지막 문장은 다섯 단어로 단락 전체를 접는다. 긴 설명 뒤 짧은 명령으로 닫는 지침문의 리듬이다.

**핵심 표현**:
- `shortens the solution, never the reading` — 줄여도 되는 것과 안 되는 것을 한 동사로 가른다.
- `the dangerous kind` — 앞에서 말한 종류 중 "위험한 쪽"을 `kind` 하나로 가리킨다.
- `a confident wrong fix` — 형용사 두 개를 쉼표 없이 겹쳐 "자신만만하지만 틀린"을 만든다.

**격식 짝**:
- refined (작성): Efficiency gained by skipping comprehension is illusory; it produces a fix that is wrong with conviction.
- plain (작성): If you skip the reading to save time, you'll just ship something wrong and feel sure about it.

<sub>출처: transcript:skewnono-v3-nuxt/07a4eb85 (Ponytail 스킬 문서, "When NOT to be lazy")</sub>

---

## 단락 2

Updating only the doc is the failure mode to avoid: the doc is read when someone writes an office adapter, but `mock.py` is what every home session actually runs against. A fact recorded in one and not the other is a fact the next home session will contradict. […] A mock resembles the real thing as closely as what we know allows. Copy every confirmed property — the shape of an identifier, which axes vary independently, how wide the spread is, whether nulls appear — because a mock that is tidier than the office is a mock that hides the office's bugs. Where the real value is genuinely unknown, fabricate a plausible one and mark it `OFFICE-VERIFY`: the provenance marks below are what separate a guess from a confirmed fact, so a guess never has to be avoided, only labelled.

**문법·구조**: 이 단락은 "규칙 → 이유"를 콜론으로 잇는 문장이 반복된다. 첫 문장은 동명사구 주어(`Updating only the doc`)로 금지 행동을 지목하고, 콜론 뒤에 `the doc is read … but mock.py is what … runs against` 로 둘의 역할 차이를 댄다. `is read` 는 수동태로 읽는 사람이 누구든 상관없음을 나타낸다. 둘째 문장은 `A fact … is a fact …` 로 같은 명사를 주어와 보어에 반복해 격언 꼴을 만든다. 뒤쪽 `a fact (that) the next home session will contradict` 에서 관계대명사가 빠졌다. 중략 뒤 첫 문장 `as closely as what we know allows` 는 `as … as` 비교 안에 `what` 명사절이 주어로 들어간 구조다. 직역하면 "우리가 아는 것이 허락하는 만큼 가깝게"가 된다. 다음 문장은 대시 사이에 명사구·간접의문문 네 개를 나열해 `every confirmed property` 의 내용을 채우고, `because` 절에서 다시 `a mock that … is a mock that …` 반복 틀을 쓴다. 마지막 문장은 `Where …` 조건절로 열고, 콜론 뒤에 `what separate A from B` 로 표시의 역할을 정의한 뒤, `so` 로 결론을 받는다. `never … only …` 는 금지가 아니라 조건부 허용이다.

**핵심 표현**:
- `is what every home session actually runs against` — `run against X` 는 X 를 대상으로 실행한다는 뜻. `actually` 가 문서와 코드의 차이를 찌른다.
- `a mock that is tidier than the office` — `tidy` 를 데이터에 써서 "너무 깔끔해서 거짓인" 상태를 만든다.
- `what separate a guess from a confirmed fact` — `separate A from B` 로 두 범주를 가르는 기준을 말한다.

**격식 짝**:
- refined (작성): Any property confirmed against the office data should be reproduced in the mock; a mock that is cleaner than reality conceals the defects reality would expose.
- plain (작성): If we've seen it in the real data, put it in the mock too. A mock that's neater than the real thing just hides the bugs.
- refined (작성): Unknown values may be fabricated, provided they are marked as such.
- plain (작성): It's fine to make a value up, as long as you flag it.

<sub>출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md, "Office DB knowledge lands in TWO places"; 가운데 한 단락 생략)</sub>

---

## 단락 3

Never stage broadly — commit only the files you personally edited. Always pass explicit pathspecs: `git commit -- path/a path/b`, or `git add <exact paths>` followed by `git commit`. `git add -A`, `git add .`, `git commit -a`, and bare `git stash` are banned: I run several agent sessions against this one working tree, so a broad stage sweeps another session's half-finished edits into your commit under an unrelated subject line. Nothing errors — the log just gets corrupted. The same reason bans whole-tree `git checkout` / `git restore` / `git stash pop`.

**문법·구조**: 금지(`Never …`)로 열고 대시 뒤에 허용 행동(`commit only …`)을 붙여 "하지 말 것"과 "대신 할 것"을 한 문장에 넣었다. 둘째 문장은 `Always …: 예시` 로 규칙 뒤에 콜론으로 구체 명령을 보인다. 셋째 문장이 이 단락의 뼈대다. 금지 목록을 주어로 세우고 `are banned` 수동태로 선언한 뒤, 콜론 뒤에서 1인칭 `I run …` 으로 이유를 댄다. 그 이유는 `so` 로 결과까지 이어진다. `sweeps A into B` 는 빗자루질 비유로, 남의 미완성 편집이 내 커밋에 쓸려 들어가는 그림을 만든다. `under an unrelated subject line` 은 커밋 제목이 내용과 안 맞게 된다는 뜻이다. 넷째 문장은 짧다. 긴 설명 뒤에 `Nothing errors` 로 끊어 "조용한 실패"를 강조한다. 마지막 문장은 `The same reason bans …` 로 이유를 주어로 세워 추가 금지 항목을 한 줄에 붙인다. 이유가 동사(`bans`)의 주어가 되는 무생물 주어 구문이다.

**핵심 표현**:
- `stage broadly` — 범위를 좁히지 않고 통째로 스테이징한다. `broadly` 가 경고의 핵심이다.
- `sweeps … into your commit` — 의도치 않은 포함을 빗자루질에 빗댄다.
- `The same reason bans X` — 앞서 댄 이유를 재활용해 금지 목록을 넓힌다.

**격식 짝**:
- refined (작성): Because several sessions share one working tree, any unscoped staging risks incorporating another session's incomplete changes.
- plain (작성): Other sessions are editing the same tree, so if you stage everything you'll grab their half-done work too.

<sub>출처: transcript:skewnono-v3-nuxt/07a4eb85 (프로젝트 CLAUDE.md, "Git Workflow")</sub>

