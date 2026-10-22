# 2026-10-23 — 정독

## 단락 1

**Your call.** What `hub_load_tm` really means. The Uploaded column is `hub_load_tm`. If that is the time the engineer wrote the note, the new order is what you asked for. If it is the time the data hub loaded the row, a bulk reload would give many rows the same stamp, and those would fall back to Down order among themselves. I can't check this from home; one look at a few real rows at the office would settle it.

**문법·구조**: 두 개의 `If` 문이 같은 틀(If it is the time …)로 나란히 서서 해석 A·B 를 비교한다. 첫 조건문은 현재형 결론(`is what you asked for`)으로 "그렇다면 이미 맞다"를 단언하고, 두 번째는 `would give … would fall back` 으로 가정 결과를 말한다. 한쪽은 사실, 다른 쪽은 가능성이라는 확신의 차이가 시제 선택에 드러난다. `the time the engineer wrote the note` 는 관계부사 `when` 이 생략된 명사절이다. 마지막 문장은 세미콜론으로 "확인 못 함"과 "확인 방법"을 붙여 문제 제기를 해결책으로 닫는다.

**핵심 표현**:
- `what you asked for` — "요청하신 그대로". 결과가 요구와 맞는지 확인할 때.
- `fall back to X among themselves` — 같은 값끼리는 2차 기준으로 정렬된다. `among themselves` 가 범위를 동률 그룹 안으로 묶는다.
- `one look at … would settle it` — 확인 비용이 작다는 걸 주어로 강조.

**격식 짝** (작성):
- refined: This ambiguity can be resolved by inspecting a small sample of production rows on site.
- plain: If someone just looks at a few real rows at the office, we'll know.

<sub>출처: transcript:skewnono_v3_nuxt 008466b8 (BM/PM·비교 장비 리뷰 보고)</sub>

---

## 단락 2

One change beyond the manager's decision. `w-0 min-w-full truncate` with `min-w-36` was not enough on its own: the line spanned only the label and value (98 px for Distinct recipes), so ordinary deltas would have been clipped. I changed the grid's second column from `auto` to `1fr` so the line spans the whole item. Known limit: 144 px holds 20 characters. A delta of 21 or more, such as `+10h 07m 51s (+16.7%)`, is clipped and readable only in the tooltip. That is plausible on long windows or multi-fab selections; widening `min-w-36` is the fix if it turns out to be common.

**문법·구조**: 시제가 이야기 순서를 따라간다. 지시대로 했을 때의 결과는 과거(`was not enough`, `spanned`), 막아 낸 일은 과거 가정(`would have been clipped`), 내가 한 일은 과거(`I changed`), 지금 상태는 현재(`spans`, `holds`, `is clipped`)다. 콜론은 "주장 → 근거"(`not enough on its own: the line spanned …`)로 쓰였다. `so the line spans` 의 `so` 는 목적(그래서 ~하도록)이다. 마지막 문장은 위험의 크기(`plausible`)와 대응책(`the fix`)을 세미콜론 하나로 짝짓는다.

**핵심 표현**:
- `not enough on its own` — 그것만으로는 부족하다. 지시를 따랐지만 보완이 필요했다는 근거를 깔 때.
- `Known limit:` — 남은 한계를 숨기지 않고 헤딩처럼 앞세운다.
- `if it turns out to be common` — 지금은 드물다는 판단과 대응 조건을 함께.

**격식 짝** (작성):
- refined: The prescribed classes were insufficient in isolation; an additional change to the grid template was required.
- plain: Doing just what you said wasn't enough, so I also tweaked the grid.

<sub>출처: transcript:skewnono-s3 283e893e (Round 3 수정 보고)</sub>

---

## 단락 3

Cause: the cohort came from the payload's `settings` map, which the office adapter cuts to the tool family (CD-SEM vs HV-SEM) but not to the model. Fix: `HardwareView` now narrows that map to the picked models before passing it to the panels. This is frontend-only, so the office needs just a `git pull` and a rebuild — no `office.py` re-copy. The mock's comparison tools were made-up ids that aren't in the equipment list, so the model filter would have emptied the picker at home. The mock now returns the tool's real same-fab, same-family tools with models mixed, as the office does. Home MDC/SCE comparison data therefore shows different tool ids than before.

**문법·구조**: `Cause:` / `Fix:` 라벨로 원인과 처치를 나눈 전형적인 버그 보고 단락이다. 첫 문장의 `which the office adapter cuts to … but not to …` 는 계속적 관계절로, `but not` 이 빠진 한 단계를 정확히 짚는다. `would have emptied` 는 "mock 을 안 고쳤다면 생겼을 일"을 과거 가정으로 보여 준다. `as the office does` 의 `as` 는 "~처럼"이고 `does` 가 앞 동사구를 받는다. 마지막 `therefore` 는 문장 가운데 들어가 결과(달라 보이는 id)를 미리 알린다.

**핵심 표현**:
- `cut X to Y` — X 를 Y 범위로 줄이다(필터링).
- `narrow X to Y` — 후보를 Y 로 좁히다.
- `no X re-copy` — 대시 뒤에 명사구로 "X 다시 복사할 필요 없음"을 덧붙이는 보고체.

**격식 짝** (작성):
- refined: Because the change is confined to the frontend, deployment requires only a pull and a rebuild.
- plain: It's frontend-only, so just pull and rebuild.

<sub>출처: transcript:skewnono_v3_nuxt 008466b8 (비교 장비 모델 범위 수정 보고)</sub>
