# 2026-10-22 — 정독

## 단락 1
S5 is built, committed as `7f96e1d4` on `work/s5-rule-explain`, and `REPORT-S5.md` is written at the worktree root. `npm test` passes (1922), typecheck is clean, and lint shows 0 errors (2 warnings in an untouched file). The browser check passed with no console errors, and both servers are stopped. In the drill slideover each recipe now has a collapsed "판정 근거" fold with the sentence, the inputs and the applied cell id. The parameter rows gain a 출처 column and `+N` beside the cap.

**문법·구조**: 완료 보고의 정석 순서다. ① 산출물 → ② 자동 검증 → ③ 수동 검증 → ④ 사용자가 보게 될 변화. 첫 문장은 `is built`, `(is) committed`, `is written` 세 수동태를 쉼표와 `and` 로 묶는다. 누가 했는지보다 "지금 어떤 상태인가"가 중요해서 현재형 수동(상태 수동)을 썼다. 둘째 문장은 주어 세 개(`npm test`, `typecheck`, `lint`)가 각각 짧은 술어를 받는 병렬 구조이고, 괄호로 숫자와 예외(건드리지 않은 파일의 경고 2건)를 덧붙여 본문 흐름을 끊지 않는다. 셋째 문장에서 시제가 갈린다. `passed` 는 과거형으로 끝난 사건이고, `are stopped` 는 현재 상태다. 넷째·다섯째 문장은 현재형 `has`, `gain` 으로 바뀐 화면을 묘사한다. `now` 하나가 "이전엔 없었다"는 대비를 만들고, 동사 `gain` 은 "기존 행에 열이 더해졌다"를 `add` 보다 짧게 말한다.

**핵심 표현**:
- `committed as <hash> on <branch>` — 커밋 해시와 브랜치를 전치사 `as`·`on` 으로 한 번에 붙인다.
- `2 warnings in an untouched file` — 경고가 있지만 내 변경과 무관하다고 괄호 안에서 미리 해명한다.
- `The parameter rows gain a … column` — 무생물 주어 + `gain` 으로 UI 변화를 묘사한다.

**격식 짝**:
- refined (작성): All automated checks pass; the two remaining lint warnings predate this change and are confined to a file it does not touch.
- plain (작성): Tests and typecheck are fine. Lint has two warnings, but they're in a file I didn't touch.

<sub>출처: transcript:skewnono-s5 [assistant] (S5 1차 완료 보고)</sub>

---

## 단락 2
`idle` and `done` are the same underlying semantic state with different attention state. An agent that first opens at its prompt reports `idle`, including in a background pane. After a working or blocked agent completes, it reports `done` when its tab or workspace is in the background. It reports `idle` when it completes in the active tab while the foreground client is focused. If the foreground client is explicitly unfocused, completion can become `done` even in the active tab. Focusing a pane, switching to its tab, or regaining outer terminal focus marks the visible tab as seen, so `done` becomes `idle`. Switching away does not turn an existing `idle` status into `done`; `done` is created by a later completion while the pane is unseen.

**문법·구조**: 상태 기계를 산문으로 풀어 쓴 단락이다(원문은 첫 문장 뒤에 두 줄짜리 불릿이 있어 그 부분만 뺐다). 첫 문장이 정의를 내리고 나머지 여섯 문장이 "언제 어느 쪽이 되는가"를 조건별로 나열한다. 시간·조건 접속사가 전부 다르다는 점을 보자. `After … completes`(시간 순서), `when … is in the background`(상황), `while … is focused`(동시 조건), `If … is explicitly unfocused`(예외 조건). 같은 동사 `reports` 를 반복하고 접속사만 바꿔 독자가 조건 차이에만 집중하게 했다. 모든 문장이 현재형인데, 매번 그렇게 동작하는 규칙(일반 사실)이라서다. 여섯째 문장은 동명사 주어 세 개(`Focusing …, switching …, or regaining …`)를 `or` 로 묶어 "이 중 무엇이든"을 표현한다. 마지막 문장은 세미콜론 앞에서 흔한 오해(떠나면 done 이 된다)를 부정하고, 뒤에서 수동 `is created by` 로 유일한 발생 경로를 밝힌다. "아닌 것 → 맞는 것" 순서라 오해가 정정된 채로 기억에 남는다.

**핵심 표현**:
- `the same underlying … state with different … state` — 실체는 하나, 부가 속성만 다르다고 정리하는 틀.
- `including in a background pane` — `including` 뒤에 전치사구를 바로 붙여 "그 경우도 예외 없이"를 덧붙인다.
- `does not turn an existing X into Y; Y is created by …` — 상태 전이를 부정한 뒤 진짜 경로를 밝힌다.

**격식 짝**:
- refined (작성): The two statuses denote the same state and differ only in whether the result has been acknowledged.
- plain (작성): `idle` and `done` mean the same thing — `done` just means you haven't looked yet.

<sub>출처: transcript:skewnono_v3_nuxt (herdr 스킬 문서, Control agents through panes)</sub>

---

## 단락 3
Round 3 is done: finding 2 is fixed and committed as `a66e7761`. `npm test` passes (1925), typecheck is clean, and lint shows 0 errors (the same 2 warnings in an untouched file). The browser check was not re-run, since only sentence text in a pure function changed. The sentence says `면제` only when every uncapped judged parameter is `exempt`, and `cap 없음·면제` only when exempt rows are actually mixed with others. Everything else, including a son that inherited a mother with no cap, counts as `cap 없음`. I counted inherited-null as `cap 없음` rather than listing each source, because the per-row 출처 column already shows `mother 상속`.

**문법·구조**: 원문은 `**Fix:**`, `**My call:**` 머리말이 달린 불릿인데, 머리말을 빼고 이으면 리뷰 대응 보고의 모범 단락이 된다. 첫 문장은 콜론으로 "라운드 완료"와 "무엇을 했나"를 이었다. 셋째 문장은 단락 1과 달리 건너뛴 검증을 수동 `was not re-run` 으로 밝히고 `since` 로 근거를 붙인다. 넷째 문장의 핵심은 `only when` 두 번이다. "이럴 때만 이 단어를 쓴다"는 조건을 좁혀 리뷰어가 지적한 과잉 단언을 막았음을 보여 준다. `actually mixed` 의 `actually` 는 "겉보기가 아니라 실제로"라는 강조다. 다섯째 문장은 `Everything else` 로 나머지 전부를 한 범주로 묶고 `including …` 으로 리뷰어가 지적한 바로 그 경우를 지목한다. 마지막 문장은 `rather than + -ing` 로 고르지 않은 대안을 옆에 두고 `because` 로 근거를 단다. 선택 → 대안 → 이유가 한 문장에 들어간다.

**핵심 표현**:
- `only when … , and … only when …` — 단어를 쓰는 조건을 둘 다 좁혀 과잉 단언을 막는다.
- `Everything else, including X, counts as Y` — 기본값 범주를 정하고 논란이 된 사례를 명시적으로 넣는다.
- `I counted X as Y rather than Z-ing, because …` — 재량 판단 보고의 정형.

**격식 짝**:
- refined (작성): Parameters whose cap is inherited but null are classified as "cap 없음"; listing each source individually would duplicate the per-row 출처 column.
- plain (작성): I just called those "cap 없음" — the 출처 column already says where each one came from.

<sub>출처: transcript:skewnono-s5 [assistant] (Round 3 보고)</sub>
