# 2026-10-17 — 정독

## 단락 1

Write the regression test before the fix — but only if there is a correct seam for it. A correct seam is one where the test exercises the real bug pattern as it occurs at the call site. If the only available seam is too shallow (single-caller test when the bug needs multiple callers, unit test that can't replicate the chain that triggered the bug), a regression test there gives false confidence. If no correct seam exists, that itself is the finding. Note it. The codebase architecture is preventing the bug from being locked down. Flag this for the next phase.

**문법·구조**: 명령문으로 시작해서 대시 뒤 `but only if …` 로 조건을 단다. "하라, 단 이럴 때만"이라는 지침 글의 기본 틀이다. 둘째 문장 `A correct seam is one where …` 은 정의문이다. `one` 이 앞의 `seam` 을 받고 `where` 관계부사절이 그 조건을 채운다. 셋째 문장은 괄호 안에 예시 두 개를 관사 없이 나열했다. 문장 흐름을 끊지 않으려고 명사구를 압축한 것이다. 넷째부터는 길이가 확 줄어든다(`Note it.` 두 단어). 긴 조건 설명 끝에 짧은 명령을 연달아 놓아 행동 지시가 또렷해진다. `is preventing … from being locked down` 은 `prevent A from -ing` 에 수동 동명사(`being locked`)를 넣은 형태다. 현재진행형이라 "지금 이 구조가 막고 있다"는 진단이 된다.

**핵심 표현**:
- `that itself is the finding` — 할 수 없다는 사실 자체가 보고할 결과라는 뒤집기.
- `gives false confidence` — 통과는 하지만 실제로는 아무것도 보장하지 않는 테스트를 가리킨다.
- `preventing the bug from being locked down` — 테스트로 버그를 묶어 두지 못하게 막는다.

**격식 짝**:
- refined (작성): Where no suitable seam exists, its absence should be recorded as a finding in its own right.
- plain (작성): If there's nowhere good to put the test, that's worth writing down too.

<sub>출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서, Phase 5)</sub>

---

## 단락 2

Generate 3–5 ranked hypotheses before testing any of them. Single-hypothesis generation anchors on the first plausible idea. Each hypothesis must be falsifiable: state the prediction it makes. If you cannot state the prediction, the hypothesis is a vibe — discard or sharpen it. Show the ranked list to the user before testing. They often have domain knowledge that re-ranks instantly ("we just deployed a change to #3"), or know hypotheses they've already ruled out. Cheap checkpoint, big time saver. Don't block on it — proceed with your ranking if the user is AFK.

**문법·구조**: 명령문과 이유문이 번갈아 나온다. 첫 문장(명령) 뒤에 둘째 문장(이유)이 와서 왜 여러 개를 세워야 하는지 받친다. 이 이유문은 동명사구 `Single-hypothesis generation` 을 주어로 세웠다. 사람이 아니라 "방법"이 첫 생각에 묶인다고 써서 독자를 탓하지 않는다. 셋째 문장의 콜론은 앞말(`falsifiable`)을 구체적인 행동(`state the prediction`)으로 풀어 주는 역할이다. `the prediction it makes` 는 목적격 관계대명사 `that` 이 빠진 꼴이다. 여섯째 문장의 `they've already ruled out` 은 현재완료로 "지금 시점에 이미 배제가 끝나 있다"를 나타낸다. 끝의 `Cheap checkpoint, big time saver.` 는 동사 없는 슬로건이다. 그 뒤 대시는 `Don't block on it` 이라는 단서를 붙인다. 앞에서 "보여 주라"고 했지만 기다리지는 말라고 균형을 잡는다.

**핵심 표현**:
- `anchors on the first plausible idea` — 첫 그럴듯한 생각에 판단이 닻을 내리는 편향.
- `the hypothesis is a vibe` — 예측 없는 가설은 그냥 느낌이라는 구어 비판.
- `re-ranks instantly` — 사용자가 아는 사실 하나로 순위가 즉시 뒤집힌다.

**격식 짝**:
- refined (작성): Share the ranked hypotheses with the user before testing; their domain knowledge may reorder the list immediately.
- plain (작성): Run the list by the user first — they might know right away which one it is.
- refined (작성): A hypothesis that yields no testable prediction should be discarded or refined.
- plain (작성): If you can't say what it predicts, it's just a hunch. Drop it or tighten it up.

<sub>출처: transcript:skewnono-v3-nuxt/290c8938 (diagnosing-bugs 스킬 문서, Phase 3)</sub>

---

## 단락 3

Gates are clean (the 2 lint warnings are pre-existing, in `ImageViewer.vue`). Both server exits are my own shutdown. The row-open check ended with the page navigating away mid-eval, so the destination wasn't read back; restarting briefly to confirm it properly. The mock never emits null dates or empty recipe names, so the "제외" subtitle clauses, the hidden `사용한 팁` block and the no-date chart fallback are covered by node tests only. Both read 0 on both tools (the mock spans 12 days with at least 3 measurements per recipe), so those filters were only seen producing the empty state. [There are] 6 recipes per tool, so list scroll and name truncation were not exercised; the fresh profile rendered dark only.

**문법·구조**: 여러 진행 보고와 보고서의 "브라우저로 확인 못 한 것" 절을 이어 붙였다. 문장마다 `X, so Y` 가 반복된다. 앞에는 원인(목 데이터의 한계), 뒤에는 결과(확인 범위가 좁아짐)가 온다. 독자가 "왜 못 봤는지"를 바로 납득한다. 확인 못 한 것은 수동태로 썼다(`wasn't read back`, `are covered by … only`, `were not exercised`). 행위자를 빼고 "확인이라는 일이 일어나지 않았다"는 사실만 남긴 것이다. 세미콜론은 밀접한 두 절을 마침표보다 가깝게 묶는다. `restarting briefly to confirm it properly` 는 주어·동사가 없는 진행 보고체다(`I'm` 생략). `only` 의 위치도 볼 만하다. `covered by node tests only`, `seen producing the empty state only` 처럼 끝에 두면 한정 범위가 또렷하다. `rendered dark only` 도 같다.

**핵심 표현**:
- `navigating away mid-eval` — `mid-` + 명사로 "~하는 도중"을 짧게 넣는다.
- `wasn't read back` — 결과를 되읽어 확인하지 못했다는 정직한 보고.
- `were not exercised` — 그 코드 경로를 실제로 밟아 보지 못했다.

**격식 짝**:
- refined (작성): Because the mock data contains no null dates, these code paths were verified by unit tests alone.
- plain (작성): The mock never has empty dates, so I only checked those parts in tests, not in the browser.

<sub>출처: transcript:skewnono-afm-recipes/4e1c4ef9 (진행 보고·완료 보고, 문장을 이어 붙이고 굵은 소제목은 덜어 냄. [ ] 안은 이어 읽히도록 보탠 말)</sub>
