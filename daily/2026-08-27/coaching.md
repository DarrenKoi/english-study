# 2026-08-27 — 코칭

오늘 내가 쓴 메시지는 전부 영어라 한글→영어 카드는 없습니다. 영어 다듬기 3장만 둡니다.

## 영어 다듬기

### 카드 1 — 기본값과 선택지 지정
- 내가 쓴 영어: "then, keep 2주 as default. and user can decide from 1주|2주|3주|4주"   (출처: transcript:[user] skewnono-v3-nuxt 4a1eae66)
- 정정: `as default` → `as the default` (특정한 하나를 가리키므로 정관사). `user can decide from` → `users can choose from` (총칭 복수 + 선택지 목록엔 `choose from`; `decide` 는 `decide on/between`).
- 더 나은 표현: Then keep 2주 as the default, and let users choose from 1주 | 2주 | 3주 | 4주.
- 왜: 두 문장을 `and` 로 이으면 "기본값 유지 + 선택 허용"이 한 지시가 된다. `let users choose from` 은 UI 명세의 상투구라 읽는 쪽이 바로 알아듣는다. 문두 `then,` 뒤의 쉼표는 영어에선 보통 뺀다.

### 카드 2 — 조건부 머지 지시
- 내가 쓴 영어: "merge and push it once tests pass"   (출처: transcript:[user] skewnono-v3-nuxt 4a1eae66)
- 정정: 오류 없음. `once … pass` 조건절이 정확하다.
- 더 나은 표현: Merge and push once the suite is green. / Merge and push as soon as the tests pass.
- 왜: 이미 자연스러운 문장이다. 한 단계 위로는 `the suite is green` 같은 팀 은어가 "전체 스위트"를 못 박고, `as soon as` 는 `once` 보다 "지체 없이"를 강조한다. 목적어 `it` 은 앞 문맥이 분명하면 빼도 된다.

### 카드 3 — 진단 스크립트 요청
- 내가 쓴 영어: "I want you to create diagnose script for recipe-search. check if we are correctly using redis DBs to get to the idp info or file. make the code in the folder scripts so that I can see the flow of process."   (출처: transcript:[user] skewnono-v3-nuxt 8aed5687)
- 정정: `create diagnose script` → `create a diagnostic script` (관사 + 형용사형 `diagnostic`; `diagnose` 는 동사). `the flow of process` → `the flow of the process` 또는 `the process flow` (관사 누락). `make the code in the folder scripts` → `put the script in the `scripts/` folder`.
- 더 나은 표현: Write a diagnostic script for recipe-search that checks whether we're hitting the right Redis DBs to reach the IDP info or file. Put it under `scripts/` so I can follow the process flow step by step.
- 왜: 세 문장을 관계절 `that checks whether …` 로 묶으면 "무엇을 / 무엇을 확인 / 어디에"가 한 호흡으로 읽힌다. `correctly using redis DBs to get to` 는 뜻은 통하지만 `hitting the right Redis DBs to reach` 가 개발자 어투로 더 정확하다(DB 번호 선택 문제임을 `right` 가 드러낸다). `see the flow` 보다 `follow the flow step by step` 이 "단계별로 출력해 달라"는 요구를 담는다.
