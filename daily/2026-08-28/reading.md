# 2026-08-28 — 정독

## 단락 1

Your two cases bifurcate for **different reasons**, and naming them separately is what stops "we're growing" from becoming a valid argument for any feature. The distinction has teeth: Skewvoir needs to hand off — a wafer → its recipe → its equipment → Recipe 현황. AFM genuinely doesn't. So Skewvoir gets a different shell but must **not** get a different vocabulary or a walled route namespace; AFM gets both. If someone later argues Recipe 검색 should go standalone, the test answers it: it shares the vocabulary *and* fits the page shell. It's growing, not bifurcating. "Different style" is the symptom, not the criterion. Every big feature eventually wants its own style. What actually distinguishes AFM is that its data has almost no join with e-beam data — you can't route from an AFM scan to a CD-SEM recipe. Bifurcate on the **join**, not on the visual ambition.

**문법·구조**: 기준 하나를 세우고, 그 기준으로 미래의 요청까지 미리 판결해 두는 논증문이다.
① 첫 문장의 주어가 동명사구 `naming them separately` 다. "이름을 따로 붙이는 행위"를 통째로 주어 자리에 넣었기에 뒤의 `is what stops A from becoming B` 가 성립한다. `what` 절이 보어로 오는 의사분열문(pseudo-cleft)이라 "이게 바로 그 역할을 한다"는 강조가 붙는다.
② `stop X from -ing` 은 전치사 `from` 이 필수다. 인용부호 안의 구어 `"we're growing"` 을 그대로 목적어로 쓴 것도 요령 — 앞으로 누가 할 말을 미리 따다 붙여 반박 대상을 눈에 보이게 만든다.
③ `The distinction has teeth:` 뒤는 콜론으로 근거를 잇는다. `Skewvoir needs to hand off … AFM genuinely doesn't.` — 대동사 `doesn't` 가 `need to hand off` 를 통째로 받아 반복을 지운다. 부사 `genuinely` 가 "형식적으로가 아니라 진짜로"를 얹어 예외 취급이 아님을 표시한다.
④ `gets a different shell but must not get a different vocabulary` — `must not` 은 금지이지 불필요가 아니다. `doesn't have to get` 으로 바꾸면 "안 가져도 된다"가 되어 뜻이 무너진다. 이 자리에서 조동사 선택이 규칙의 강도를 결정한다.
⑤ 조건절 `If someone later argues …, the test answers it` 은 가정법이 아니라 직설법 현재다. 실제로 일어날 일로 보기 때문이며, 그래서 뒤의 `the test answers it` 이 "그때 가서 논쟁하지 않는다"는 약속이 된다. 이탤릭 `*and*` 가 두 조건이 모두 충족돼야 함을 한 글자로 표시한다.
⑥ `X is the symptom, not the criterion.` — 증상과 기준을 가르는 명사 대비. 바로 뒤 `Every big feature eventually wants its own style.` 이 일반 현재시제로 "그건 누구나 그렇다"를 깔아, 증상이 변별력이 없음을 증명한다.
⑦ 마지막은 명령형 `Bifurcate on the join, not on the visual ambition.` 이다. 앞의 서술을 규칙으로 바꿔 문단을 닫는 형태이고, 전치사 `on` 이 "무엇을 근거로 가르는가"를 가리킨다.

**핵심 표현**
- `It's growing, not bifurcating.` — 규모와 종류를 가르는 판결문. 기준을 먼저 세운 뒤라야 힘이 있다.
- `must not get a different vocabulary` — 허용이 아니라 금지. 조동사 하나로 규칙의 등급을 정한다.
- `Bifurcate on the join, not on the visual ambition.` — 판단 근거를 눈에 보이는 것(스타일)에서 구조적인 것(데이터 조인)으로 옮긴다.

**격식 짝**
- refined: The criterion is whether the data joins, not whether the feature has outgrown its visual language.
- plain: Ask if you can actually click through from one to the other. If you can't, split it — otherwise it just wants a new coat of paint. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt f0e35121</sub>

---

## 단락 2

**`back_dev_home/ebeam/recipe_search/MIGRATION.md` not updated.** Its endpoint table still reads `/align-images | Redis recipe registry (fallback: meas_hist) — resolution only, no FTP | wired` and its narrative says "No FTP happens in this endpoint. Align image names are computable … so the tool is only dialed when `/recipe-image` is asked for the bytes." The change makes `/align-images` perform an NLST round trip via `_list_raw_dirs`. CLAUDE.md defers per-feature specifics to MIGRATION.md; it now states the opposite of the code. `recipe_idp.txt` was rewritten but this doc was left contradicting it. **Stale contract comment** — contracts.py:203 still says `optic: str  # "OM" (P.No 1) or "SEM" (P.No 2)`, but the change introduces `optic: ""` for unknown points. The contract now misdescribes its own value domain.

**문법·구조**: "문서가 코드와 어긋났다"는 지적 하나를 증거 → 원인 → 판정 → 책임 순으로 세우는 리뷰 문단이다.
① 제목 행이 완전한 문장이 아니라 `X not updated.` 라는 무동사 명사구다. 리뷰 항목의 헤더는 이렇게 압축하고 본문에서 문장으로 푸는 게 관례.
② `Its endpoint table still reads …` 의 `read` 는 "읽다"가 아니라 **문서에 그렇게 적혀 있다**는 자동사 용법이다. 주어가 사람이 아니라 표라는 점이 핵심 — `says` 와 나란히 써서 문서 두 곳(표와 산문)을 각각 인용한다. 부사 `still` 이 "코드는 바뀌었는데 여기만"을 한 단어로 전한다.
③ 인용은 원문 그대로 두고 생략은 `…` 로 표시한다. 인용 안의 수동태 `is only dialed when /recipe-image is asked for the bytes` 는 행위자를 감춘 게 아니라 불필요해서 지운 경우다 — 누가 부르든 상관없고 "언제 걸리는가"만이 쟁점이다.
④ `The change makes /align-images perform an NLST round trip` — 사역동사 `make + 목적어 + 원형부정사`. `to perform` 이 아니라 원형인 것이 문법 포인트이며, 주어를 `The change` 로 둬서 책임이 이번 변경에 있음을 문장 구조로 못 박는다.
⑤ 세미콜론이 두 절을 잇는다. 앞은 규칙(`CLAUDE.md defers … to MIGRATION.md`), 뒤는 그 규칙에 비춘 판정(`it now states the opposite of the code`). 마침표로 끊으면 규칙과 판정이 따로 놀고, `because` 를 넣으면 장황해진다 — 세미콜론이 정확히 이 간격을 맡는다.
⑥ `was rewritten but this doc was left contradicting it` — 수동태 두 개를 `but` 으로 맞세워 "한쪽은 손댔고 한쪽은 안 댔다"를 대칭으로 보인다. `was left + 현재분사` 는 방치의 결과를 그리되 방치한 사람을 지목하지 않는 완충 구문이다.
⑦ 마지막 문장의 `misdescribes its own value domain` 에서 소유격 `its own` 이 아이러니를 만든다. 남의 것도 아니고 자기가 정의한 값 범위를 자기 주석이 틀리게 적고 있다는 뜻.

**핵심 표현**
- `its endpoint table still reads …` — 문서를 주어로 삼아 "이렇게 적혀 있다"를 서술한다.
- `it now states the opposite of the code` — 불일치가 아니라 정반대임을 명시해 등급을 올린다.
- `was left contradicting it` — 누락을 사람이 아니라 파일의 상태로 서술한다.

**격식 짝**
- refined: The document was left contradicting the implementation it is meant to describe.
- plain: The code moved and this doc didn't — it now says the exact opposite. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md</sub>

---

## 단락 3

The nav refactor is a deletion, not an addition. Right now a new page has to be registered in six hand-maintained lists, and the compiler catches none of it — miss one and the page ships without its tabs. This is already costing you: two parallel route trees exist for the same feature set, and two more are stubbed out waiting for the same copy. The earlier fix, deriving three consumers from one array, was right, and it stopped one file short. Every later step raises the stakes on finishing it rather than lowering them, so it belongs first in the plan. Maturity, meanwhile, stops being a place — it becomes a badge on the row, since hiding unfinished pages in production was never the drawer's job. One consequence falls out of that move: the drawer empties, and the freed menu slot can carry the domain switcher instead.

**문법·구조**: 오늘 배운 표현들을 하나의 제안문으로 엮은 모범 단락이다. 제안 → 현재 비용 → 과거 평가 → 순서 근거 → 부수 효과의 흐름을 따른다.
① 첫 문장 `A, not B` 가 문단 전체의 논지다. 리팩터링 제안은 "일이 늘어난다"는 반사적 저항을 받으므로, 그 전제를 첫 줄에서 뒤집고 시작한다.
② `miss one and the page ships without its tabs` — 명령형 + `and` 가 조건문을 대신한다. `If you miss one, the page will ship …` 보다 짧고 경고의 톤이 살아난다. 구어와 문어 양쪽에서 통하는 압축형이다.
③ 콜론 뒤에 증거 두 개를 `and` 로 병렬한다. `two parallel route trees exist … and two more are stubbed out` — 능동과 수동을 섞었지만 어색하지 않은 이유는 주체가 다르기 때문이다. 앞은 트리가 존재한다는 사실, 뒤는 누군가 스텁을 만들어 두었다는 사실.
④ `The earlier fix, deriving three consumers from one array, was right` — 쉼표 두 개 사이에 동격 동명사구를 끼워 넣어 무슨 수정인지 밝힌다. 주어와 동사(`fix … was`)가 멀어지지만, 삽입구가 짧아 읽는 데 걸리지 않는다.
⑤ `raises the stakes on finishing it rather than lowering them` — `rather than -ing` 이 예상되는 반대 해석을 미리 부정한다. 대명사 `them` 이 `the stakes` 를 받아 명사 반복을 피한다.
⑥ `Maturity, meanwhile, stops being a place` — 문중 삽입 부사 `meanwhile` 이 화제 전환을 알린다. 문두에 놓아도 되지만 주어 뒤로 넣으면 전환이 부드럽고, 앞 문장과의 연결이 끊기지 않는다.
⑦ 마지막 문장의 `falls out of` 는 의도한 결과가 아니라 구조상 딸려 나온 결과를 뜻한다. 그래서 `so we can also …` 처럼 공을 주장하지 않고도 이득 하나를 더 얹을 수 있다.

**핵심 표현**
- `the compiler catches none of it` — 실수해도 조용히 통과한다는 최악의 실패 양상.
- `it stopped one file short` — 과거의 개선을 인정하면서 모자란 거리를 수치로 준다.
- `stops being a place` — 분류 축을 위치에서 속성으로 옮기자는 제안을 세 단어로.

**격식 짝**
- refined: Registration is currently distributed across six hand-maintained lists with no compile-time verification.
- plain: Add a page and you've got six files to remember — and nothing yells at you if you forget one. (작성)

<sub>출처: 모범 단락(작성) — 오늘 수집한 표현을 엮음</sub>

