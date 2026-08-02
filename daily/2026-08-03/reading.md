# 2026-08-03 — 정독

## 단락 1

live_alarm was built as a writer/reader split: a separate scheduler service polls the in-house alarm API every 15 seconds and writes a Redis board; SKEWNONO only ever reads that board. That design does keep the alarm API safe from page traffic, but it buys the safety at a price: it needs a second deployment; it polls the alarm API 24 hours a day whether or not anyone has the page open; and its office template assumes an interface the office does not have. That last point is what forces the redesign rather than merely motivating it. The interface mismatch and the deployment cost point at the same replacement: let the page request trigger the fetch, and put a short Redis cache with a lock in front of it so that many viewers collapse into one upstream call.

**문법·구조**: 첫 문장은 콜론 뒤에 세미콜론으로 두 주체(스케줄러/SKEWNONO)의 역할을 병렬한다 — 콜론이 "풀어 쓰면 이렇다"를, 세미콜론이 대등한 두 절을 맡는 분업. 둘째 문장의 `does keep` 은 강조의 do 로, 양보("안전하긴 하다")를 먼저 세운 뒤 `but` 으로 비용 목록을 연다. 목록 안 `whether or not anyone has the page open` 은 양보 부사절로 "누가 보든 말든"을 압축한다. 마지막 문장은 명령형 `let ... trigger`, `put ... in front of it` 두 개를 콜론 뒤에 놓아 해법을 지시문처럼 제시하고, `so that ... collapse into` 로 목적을 닫는다.

**핵심 표현**:
- `buys the safety at a price` — 장점을 인정하되 대가를 청구하는 전환부.
- `forces ... rather than merely motivating it` — 여러 근거 중 결정타를 골라내는 문형.
- `point at the same replacement` — 서로 다른 두 문제가 같은 해법을 가리킨다는 수렴 논증.

**격식 짝**:
- refined: That last point is what forces the redesign rather than merely motivating it. ↔ plain: That one isn't just a nice-to-have — it's the reason we have to redo this. (작성)
- refined: It buys the safety at a price. ↔ plain: We get the safety, but it costs us. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md</sub>

---

## 단락 2

A user looking at one parameter on the recipe-open page can see everything about it — the idp_image_info row, AMP, AF/PR, each image and its beam condition — and can take none of it with them. There is no download, and there is no documented way to ask for the same data from a script. Both gaps have a shape the codebase already knows how to fill, and both have a trap in them. The export trap: recipe-compare already exports an .xlsx, and its image handling is a deliberate non-answer. That reasoning is sound for compare, which is N recipes wide. It does not carry over to one parameter, which has at most three image slots. Reusing compare's answer here would ship a filenames-only export for a case whose cost objection does not apply.

**문법·구조**: 첫 문장은 `can see everything ... and can take none of it with them` 의 everything/none 대구가 축이다 — 긴 대시 삽입구로 "everything"의 내용을 다 보여 준 뒤에 none 으로 떨어뜨려 낙차를 키운다. `There is no A, and there is no B` 의 반복은 결핍을 리듬으로 만든다. `a shape the codebase already knows how to fill` 은 관계사 that 이 생략된 접촉절 + `know how to` 로, "전례가 있다"를 의인화해 압축한다. 뒤쪽은 `is sound for A / does not carry over to B` 로 현재형 판정을 잇고, 마지막 문장은 가정법 `would ship` 으로 "그 답을 재사용하면 벌어질 일"을 미리 보여 준다. `whose cost objection does not apply` 의 whose 는 사물(case)에도 자연스럽게 붙는다.

**핵심 표현**:
- `can take none of it with them` — 볼 수는 있으나 가져갈 수 없다는 문제 제기의 낙차.
- `a deliberate non-answer` — 과거의 공백이 판단이었음을 밝히는 이름표.
- `does not carry over to` — 타당한 논리의 적용 범위를 자르는 동사구.

**격식 짝**:
- refined: That reasoning does not carry over to one parameter. ↔ plain: That logic doesn't hold up here — one parameter is a different case. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md</sub>

---

## 단락 3

I fixed this at the copyToClipboard helper rather than in app.config.ts. A global toast override would have silently restyled every toast in the app — including the fifteen other call sites that pass ordinary prose, where break-all is actively wrong. The defect is specific to machine identifiers in a fixed-width box, so the fix belongs where those identifiers are, not in the design system. break-all over wrap-anywhere was a convention call, not a technical one: two sibling components already solve this exact problem with break-all, and matching them beats introducing a second idiom for one shared behavior. Worth noting what did not need touching: shareUrl() was correct the whole time, and the clipboard always received all 367 characters. The bug lived purely in presentation — "the toast looks wrong" and "the feature is broken" are separate claims.

**문법·구조**: 결정을 설명하는 글의 뼈대는 `rather than`(대안 배제) → `would have restyled`(가지 않은 길의 가정법 과거완료) → `so the fix belongs where ...`(귀결) 순서다. `belongs where those identifiers are` 는 장소 관계부사 where 절이 명사 없이 곧바로 보어가 된 형태로, "수정은 제자리가 있다"는 의인화를 만든다. `matching them beats introducing ...` 은 동명사구 둘을 주어·목적어로 세워 비교를 한 문장에 넣는다. `Worth noting what did not need touching:` 은 It is 가 생략된 구어적 도입이며, 마지막 문장의 인용부호 친 두 절을 주어로 쓰는 방식(`"A" and "B" are separate claims`)은 논증을 명제 단위로 다루는 영어 특유의 습관이다.

**핵심 표현**:
- `the fix belongs where the identifiers are` — 수정 위치를 원인의 위치로 정당화.
- `a convention call, not a technical one` — 판단 기준을 밝히는 방어.
- `lived purely in presentation` — 버그의 층위를 한정하는 동사 live.

**격식 짝**:
- refined: "The toast looks wrong" and "the feature is broken" are separate claims. ↔ plain: Just because the toast looks off doesn't mean the feature's actually broken. (작성)

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (Share 토스트 수정 세션)</sub>
