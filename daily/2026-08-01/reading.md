# 2026-08-01 — 정독

## 단락 1

Does the name this person typed match the one the directory holds? Deliberately pure — no Flask, no Redis, no request. Home fabricates member rows, so verification would never execute here if it lived in the route, and would meet a real `members` hash for the first time on the cloud. This is the mock blind spot `CLAUDE.md` warns about, closed by making the logic testable without the thing that is missing. The table below is the spec's §6.2. Exactly one cell rejects. "Cannot check" and "checked and wrong" are opposite answers. Only the second rejects; the first accepts and flags, because refusing a person the directory simply could not tell us about would deny access on the strength of our own outage.

**문법·구조**: 가정법이 단락의 논증을 끌고 갑니다. `verification would never execute here if it lived in the route` 는 가정법 과거로 **지금 그렇게 하지 않았다**는 사실을 뒤집어 보여 주고, 이어지는 `and would meet ~` 는 같은 `if` 절 아래 두 번째 귀결절로 매달려 조건을 되풀이하지 않습니다. 그다음 문장의 `closed by making ~` 은 앞의 명사 `blind spot` 을 뒤에서 받는 과거분사구인데, 관계절 `which is closed by ~` 를 두 단어 줄인 형태입니다. 짧은 단문 `Exactly one cell rejects.` 가 규칙 하나를 못 박고 나면, 마지막 문장이 그 규칙의 이유를 길게 펼칩니다 — 긴 문장 앞에 짧은 문장을 세우는 이 리듬이 규정과 근거를 눈으로 갈라 줍니다. `refusing a person the directory simply could not tell us about` 은 목적격 관계대명사가 생략되고 전치사 `about` 이 문미에 남은 구조라, 앞에서부터 읽으면 "거절한다 / 어떤 사람을 / 디렉터리가 알려 주지 못한" 순으로 풀립니다. 인용부호로 감싼 `"Cannot check"` 와 `"checked and wrong"` 은 절을 통째로 명사 자리에 앉힌 것이고, 시제를 서로 다르게(현재/과거분사) 둔 덕에 "확인 못 함"과 "확인해 보니 틀림"의 차이가 형태로 드러납니다.

**핵심 표현**: `deliberately pure`(일부러 순수하게 — 의존성을 뺀 것이 실수가 아니라 설계임을 밝힘) · `the mock blind spot`(mock 때문에 생긴 사각지대 — 집에서는 아예 실행되지 않는 경로) · `on the strength of ~`(~을 근거로 — 그 근거가 결정의 무게를 감당 못 한다는 평가를 함께 담음).

**격식 짝**: refined — *Refusing a caller the directory could not describe would deny access on the strength of our own outage.* / plain — *If the directory can't tell us anything, that's our outage, not their problem — we shouldn't shut them out for it.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-31-anonymous-self-identification.md — `verify.py` 의 모듈 docstring 과 `decide()` docstring 을 한 단락으로 이어 붙임</sub>

---

## 단락 2

The declared identity (`self_id.py`) rides in a signed session cookie, and its `verified` flag is only a claim the signature makes credible. A default key is a public constant in this repository, so on the cloud a missing value is not a weak configuration — it is an unsigned session that still looks signed. Refuse to start instead: the failure then appears once, at deploy, rather than never. The gate asks whether a value was CHOSEN, not whether it is strong. `SKEWNONO_SECRET_KEY` is required on the cloud: it signs the self-identification session, whose `verified` flag is forgeable without it. Set any non-empty value in `/project/workSpace/back_dev_home/.env` and restart.

**문법·구조**: 첫 문장의 `a claim the signature makes credible` 이 이 단락에서 가장 배울 만한 자리입니다. 목적격 관계대명사가 생략되었고, 그 안이 `make + 목적어 + 형용사`(5형식)라 "서명이 그 주장을 믿을 만하게 만든다"가 명사구 하나로 압축됩니다. 두 번째 문장은 `so` 로 결론을 끌고 온 뒤 대시로 방향을 틀어 **부정과 정정**을 나란히 놓습니다 — `not a weak configuration — it is an unsigned session that still looks signed`. 여기서 `still` 이 없으면 위험이 절반만 전달됩니다. 서명이 없다는 사실보다 **없는데 있는 것처럼 보인다**가 요점이기 때문입니다. `Refuse to start instead:` 는 주어 없는 명령문으로 판단을 지시처럼 던지고, 콜론이 그 뒤에 근거를 붙입니다. `appears once, at deploy, rather than never` 는 쉼표로 시점을 끼워 넣은 뒤 `rather than` 으로 대비를 닫는 3단 구성이라 리듬이 살아 있습니다. 마지막 두 문장에서는 소유격 관계대명사 `whose` 가 사물(session)을 받고 있는데, 사람에게만 쓴다고 오해하기 쉬운 자리입니다. 명령문 두 개(`Set ~ and restart`)로 끝맺는 것도 오류 메시지의 정석입니다 — 무엇이 잘못됐는지 다음에 무엇을 하라고까지 말해 줍니다.

**핵심 표현**: `an unsigned session that still looks signed`(서명이 없는데 있는 것처럼 보이는 세션 — 조용한 실패를 그리는 문장) · `appear once, at deploy, rather than never`(배포 때 한 번 드러나거나 영영 안 드러나거나 — 기동 거부를 정당화하는 교환) · `asks whether a value was chosen, not whether it is strong`(값을 골랐는지만 보고 강도는 보지 않는다 — 검사 범위를 스스로 좁혀 밝힘).

**격식 짝**: refined — *A missing key does not weaken the signature; it removes it while preserving its appearance.* / plain — *With no key set, the cookie isn't really signed — it just looks like it is.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-31-anonymous-self-identification.md — Task 9 의 `__init__.py` 주석과 `RuntimeError` 메시지를 이어 붙임</sub>

---

## 단락 3

Send a caller nobody could identify to the self-identification form. This gate is CLIENT-side on purpose. The server-side version of it would have to live in Flask's first `before_request`, where returning a response answers index.html and every bundle with it — the exact shape of the Phase 3 blank-window deploy. A Nuxt route middleware can only affect routing, so the worst it can do is send someone to the wrong page. It is therefore UX, not a security boundary: `curl` bypasses it entirely. The one rule that IS enforced server-side is that a declared identity can never be an admin.

**문법·구조**: docstring 이 동사원형 명령문으로 시작하는 것은 파이썬·JS 양쪽의 관례입니다 — `Send a caller ~ to the form`. 목적어가 `a caller nobody could identify` 로 길어졌는데, 목적격 관계대명사가 생략된 채 주어 `nobody` 가 바로 붙어 있어 읽는 속도가 떨어지지 않습니다. 세 번째 문장의 `where` 는 장소가 아니라 **상황**을 받는 관계부사이고, 그 안에서 동명사구 `returning a response` 가 주어 노릇을 합니다. 사람을 주어로 세우지 않아 누구의 잘못인지 묻지 않게 되는 것이 이 문장의 태도입니다. 대시 뒤 `the exact shape of the Phase 3 blank-window deploy` 는 동사 없이 앞 절 전체를 받는 동격 명사구인데, 과거의 사고를 이름표처럼 붙여 설명을 한 번에 끝냅니다. `so the worst it can do is send ~` 에서는 `is` 다음에 to 없는 동사원형이 오는 점을 눈여겨볼 만합니다. 마지막 문장은 `The one rule that IS enforced ~ is that ~` 형태의 분열문이고, 대문자 `IS` 가 앞 문장의 "보안 경계가 아니다"와 대비되는 유일한 예외를 짚어 줍니다.

**핵심 표현**: `client-side on purpose`(일부러 클라이언트 쪽에 뒀다 — 한계를 실수로 읽히지 않게 먼저 밝힘) · `the worst it can do is ~`(최악이라야 ~ 정도다 — 손해의 상한을 재 보이는 변호) · `UX, not a security boundary`(보안 경계가 아니라 사용성 유도 — 오해를 미리 차단하는 X, not Y 대비).

**격식 짝**: refined — *This gate is a usability affordance rather than a security boundary; `curl` bypasses it entirely.* / plain — *This just steers people to the right page — it stops nobody, and curl walks straight past it.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-31-anonymous-self-identification.md — `identify.global.ts` 모듈 docstring, 원문 그대로</sub>
