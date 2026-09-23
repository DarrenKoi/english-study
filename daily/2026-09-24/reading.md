# 2026-09-24 — 정독

> repo 문서 2건은 본문이 한국어라 세 단락 모두 equipment-data-map 세션의 `[assistant]` 영어 원문에서 골랐다. 굵은 소제목은 풀어서 본문에 이었고 중간에 뺀 문장은 `…` 로 표시했다. 단락 1은 외부 도구 대신 기존 파이프라인을 권하는 글, 단락 2는 "이미 있다"고 답하면서 남은 차이 하나를 짚는 글, 단락 3은 계획과 달라진 점과 변경의 대가를 밝히는 완료 보고. 셋 다 결론을 먼저 말하고 조건절로 "언제 다시 볼지"를 정해 둔다.

## 단락 1

Better fit: the pipeline we already have. Grouping will put the `.sh` files into their own file family. When Sampling downloads a few of them, the `references_file` relationship (§4.7.1) already turns an explicit path in one sample into an `observed` edge. That edge points from the script to the family of files it names, with the evidence cited. Scripts only get sampled, not fully covered, but those sampled edges are the ones that matter here. … If the first real rollout shows that `.sh` samples produce too few `references_file` edges, the fix is a shell extractor in Extraction. It would pull redirect targets and `cp`/`mv` paths into features, which would then feed `references_file` like any other path. It needs no new dependency. Don't build it until that rollout shows the gap.

**문법·구조**: 첫 문장 `Better fit: the pipeline we already have.` 는 동사 없이 콜론으로 결론부터 던진다. `the pipeline we already have` 는 관계대명사가 빠진 접촉절. 이어지는 세 문장은 시제가 정확히 나뉜다. 앞으로 일어날 단계는 `will put`, 조건이 갖춰지면 늘 일어나는 일은 현재형 `When Sampling downloads …, … already turns` 로 쓴다. `the family of files it names` 도 접촉절(`that` 생략). `Scripts only get sampled, not fully covered` 는 `get + 과거분사` 수동태에 `A, not B` 를 얹어 한계를 먼저 인정하고 `but` 뒤에서 "그래도 중요한 건 그 부분"으로 뒤집는다. 후반부는 조건문 `If … shows …, the fix is …` 로 "지금은 안 만들지만 언제 만들지"를 정한다. 가상의 도구를 설명하는 문장은 `It would pull …, which would then feed …` 처럼 `would` 로 일관해 아직 없는 물건임을 드러내는 방식. 계속적 용법 `, which` 는 앞 절 전체(추출된 경로)를 받는다. 마지막 두 문장은 짧게 끊어 권고를 못 박는다.

**핵심 표현**: `those sampled edges are the ones that matter here` — 범위는 좁아도 중요한 부분은 잡는다는 방어. / `the fix is X` — 문제가 생기면 무엇으로 고칠지 미리 정해 두는 말. / `Don't build it until that rollout shows the gap.` — 증거가 먼저, 구현은 나중.

**격식 짝**: (작성)
- refined: Should the initial rollout reveal an insufficient number of `references_file` edges, a dedicated shell extractor may be introduced at that stage.
- plain: If the first rollout doesn't give us enough edges, we'll add a shell extractor then.
- refined: Development of this component should be deferred until the deficiency is demonstrated in practice.
- plain: Don't build it until we actually see the gap.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 2

Our version is stricter than graphify's in three ways. Every tag has to point to a SHA that the checker re-hashes, there's a separate `confidence` score, and a claim can't move from inferred to observed without an engineer confirming it. In graphify, the tag is just a label. One real difference. graphify's `INFERRED` means "worked out by a fixed rule, not written in the source". Our relationship rules `similar_name` and `same_directory` are also worked out by a fixed rule, but we label them `observed`. `rule_version` and `support_scope: metadata` already show what produced each one, so I'd leave it as is. If reviewers start reading `similar_name` as proof that two families are related, the fix would be a third value such as `derived`.

**문법·구조**: 주장(`stricter … in three ways`) → 근거 셋 → 대비 한 문장의 순서. 근거 셋은 `A, B, and C` 로 한 문장에 묶었는데 구조가 서로 다르다. `has to point to a SHA that the checker re-hashes`(관계절), `there's a separate … score`(존재문), `can't move … without an engineer confirming it`(동명사의 의미상 주어 `an engineer`). `without + 명사 + -ing` 는 "누가 ~하지 않으면"을 간결하게 말하는 틀이다. `In graphify, the tag is just a label.` 은 짧은 문장으로 대비를 끝낸다. `One real difference.` 는 명사구만으로 화제를 바꾸는 신호. `are also worked out by a fixed rule, but we label them observed` 는 "같은 방식인데 이름은 다르게 붙였다"를 `also … but` 으로 맞세운다. `I'd leave it as is` 의 `would` 는 권고를 부드럽게 만들고 마지막 문장의 `the fix would be` 는 가정 조건(`If reviewers start reading …`)에 맞춘 `would` 다. 단락 1의 `the fix is` 와 비교하면 이쪽이 한 단계 더 조심스럽다.

**핵심 표현**: `stricter than X's in three ways` — 비교 우위를 개수로 예고. / `worked out by a fixed rule, not written in the source` — 도출값과 원문값을 가르는 정의. / `read X as proof that …` — 약한 신호를 증거로 오해하는 위험.

**격식 짝**: (작성)
- refined: Our implementation imposes stricter requirements than graphify's in three respects.
- plain: Ours is stricter than graphify's in three ways.
- refined: Should reviewers come to interpret `similar_name` as evidence of a relationship, a third classification would be warranted.
- plain: If people start treating `similar_name` as proof, we'll add a third tag.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 3

One thing works differently from what I first described: the CLI still has `stage 1` and `stage 2` commands. Letters 09–13 build and test those commands on test-only rollouts marked `fixture = true`, created in temp folders. Removing them would have meant rewriting those letters too. What this costs: the first time the company LLM interprets anything is on real equipment samples. Letter 18 has you check one measurement family and one log family before you approve the stage 3 result. The office will redo letters 02, 03, 12 and 14 (their file hashes changed). That's a CLI and skill rebuild, and it keeps what still passes. A rollout created under the old rules may already contain an `adopt` record. The new code accepts that record and ignores it, so an in-progress rollout keeps working.

**문법·구조**: 완료 보고에서 "계획과 다른 점"과 "대가"를 두 소제목으로 세웠다. 원문의 굵은 소제목을 콜론으로 이어 본문에 넣었다. 둘째 문장 `test-only rollouts marked fixture = true, created in temp folders` 는 과거분사 두 개(`marked`, `created`)가 명사를 뒤에서 꾸민다. 관계절 `that are marked …, that were created …` 를 줄인 형태로 기술 글에서 흔한 방식. 셋째 문장 `Removing them would have meant rewriting …` 은 가정법 과거완료로 "그 길을 택했다면 이런 대가가 있었다"를 말해 선택의 이유를 댄다. 동명사 주어(`Removing them`)와 동명사 목적어(`rewriting`)가 대칭을 이루는 점도 눈여겨볼 것. `Letter 18 has you check …` 는 사역 `have + 목적어 + 동사원형`으로 "문서가 당신에게 확인을 시킨다". `The office will redo …` 는 확정된 미래라 `will`. 마지막 두 문장은 `may already contain` 으로 가능성을 인정한 뒤 `accepts … and ignores it, so … keeps working` 으로 안심을 준다. 위험을 먼저 말하고 대책을 곧바로 붙이는 순서가 보고의 신뢰를 만든다.

**핵심 표현**: `One thing works differently from what I first described:` — 계획과의 차이를 스스로 먼저 밝힘. / `What this costs:` — 대가를 소제목으로 세워 숨기지 않음. / `it keeps what still passes` — 재작업 범위가 작다는 안심.

**격식 짝**: (작성)
- refined: Retaining these commands was preferable, as their removal would have necessitated revising letters 09 through 13.
- plain: I kept them, because taking them out meant rewriting letters 09–13 too.
- refined: Rollouts initiated under the previous rules will continue to function without intervention.
- plain: Rollouts you already started will keep working.

<sub>출처: transcript:[assistant] equipment-data-map</sub>
