# 2026-09-28 — 정독

> 세 단락 모두 transcript 영어 원문 그대로다. 단락 1은 Insight 불릿 두 개를 이어 붙였고 단락 2는 번호 목록 한 항목에서 번호와 굵은 소제목을 뗐다. 단락 1은 git 이 무엇을 옮기고 무엇을 남기는지 원리로 풀어 주는 설명이고 단락 2는 "새로고침하면 가끔 된다"는 증상의 인과를 끝까지 추적한다. 단락 3은 writing-for-agents 스킬 본문에서 금지문이 왜 역효과를 내는지 비유로 설득하는 글.

## 단락 1

A rename in git is really "delete here, add there" for tracked files. Git never touches ignored files, so after the pull `.env` and `office.py` are still sitting in the old folder. The app runs, it just can't see them. That's why the error is a connection error and not a missing-config error. With no `.env`, the client still starts and tries to connect to a default address.

**문법·구조**: 첫 문장은 정의문. `really` 가 "겉보기와 달리 실제로는"을 담고 따옴표 속 `"delete here, add there"` 는 명사구처럼 보어 자리에 들어갔다. 둘째 문장은 `never` 로 예외 없는 규칙을 세운 다음 `so` 로 결과를 잇는데, 결과절은 현재진행형 `are still sitting` 이다. 지금 이 순간에도 옛 폴더에 그대로 놓여 있다는 그림. 셋째 문장 `The app runs, it just can't see them.` 은 접속사 없이 쉼표로 두 절을 붙인 comma splice 로, 격식 글에서는 틀린 문장이지만 말하듯 쓰는 설명에서는 리듬을 만든다. 범위를 좁히는 건 `just` 로, "돌아가긴 하는데 딱 그것만 못 한다"는 뉘앙스. 넷째 문장 `That's why …` 는 앞 내용을 원인으로 받아 증상을 설명하는 틀이고 `A and not B` 로 사용자가 예상했을 법한 오류와 대비시켰다. 마지막 문장은 `With no .env` 전치사구로 조건을 앞에 두고 `still` 로 "설정이 없는데도 멈추지 않는다"는 의외성을 짚는다.

**핵심 표현**: `is really "X" for Y` — 복잡한 동작을 따옴표 속 짧은 말로 다시 정의한다. / `are still sitting in the old folder` — `stay behind` 와 같은 상황을 진행형으로 그린다. / `That's why the error is A and not B.` — 증상의 모양이 왜 그런지를 원인에 연결한다.

**격식 짝**: (작성)
- refined: Git records a rename as the deletion of tracked files at one path and their addition at another; untracked files are never moved.
- plain: Git only moves the files it tracks. Anything it ignores just stays where it was.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>

---

## 단락 2

`WARM_CEILING_MS` is 15 s in `utils/imageWarm.ts`. Measured throughput is 0.2 s per image at concurrency 6, so the ceiling covers roughly 75 images. An HV-SEM parameter is points × up to 8 files (U/T/M/L, sometimes JPEG+TIF twins), which easily exceeds that. Past the ceiling the state flips to `gaveup`, the panel releases every `<img>` into cold GETs while the server job is still holding the tool's FTP sessions, each cold GET opens its own FTP login, and some fail. The `gaveup` state is then stored in the module-level `warmStore` for the whole session, so switching back to that parameter never re-warms. A page refresh clears the store, POSTs a new job, and by then the old daemon-thread job has filled the cache. That is why refreshing "sometimes" fixes it.

**문법·구조**: 앞 세 문장은 숫자로 논증을 쌓는다. 15초 상한 → 이미지당 0.2초 → 약 75장, 그런데 HV-SEM 은 그보다 많다는 흐름. 셋째 문장의 `, which easily exceeds that` 는 계속적 관계절이고 `that` 이 앞 문장의 "75장"을 받는다. 넷째 문장은 어떨까? `Past the ceiling` 으로 시점을 먼저 놓은 뒤 네 개의 절을 쉼표로 늘어놓고 마지막에만 `and` 를 붙였다. 사건이 연쇄로 터지는 속도감이 이 구조에서 나온다. 그 안의 `while the server job is still holding …` 은 진행형으로 동시에 벌어지는 배경을 깐다. 다섯째 문장의 수동태 `is stored` 는 저장 주체보다 상태가 어디에 남는지에 초점을 두고 `then` 과 `so` 가 순서와 결과를 잇는 연결어. 여섯째 문장에서는 현재완료 `has filled` 가 핵심이다. 새로고침할 즈음이면 옛 작업이 캐시를 이미 채워 놓았으니 그제야 이미지가 뜬다. 마지막 문장은 사용자가 보고한 증상의 `"sometimes"` 를 따옴표로 되받아 설명을 닫는다.

**핵심 표현**: `which easily exceeds that` — 수치 비교를 관계절 하나로 끝낸다. / `by then … has filled the cache` — "그 시점엔 이미 끝나 있다"를 현재완료로. / `That is why X "sometimes" fixes it.` — 상대가 쓴 단어를 인용해 관찰과 원인을 이어 준다.

**격식 짝**: (작성)
- refined: Once the ceiling is exceeded, the client abandons the warm-up and every tile issues an uncached request concurrently, several of which fail under FTP contention.
- plain: After 15 seconds it gives up, and then all the images hit the server at once and some of them fail.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>

---

## 단락 3

**Negation** is the failure mode beside this lever: steering by prohibition drags the forbidden behaviour into context and makes it _more_ available, not less. _Don't think of an elephant_, and the elephant is all there is; the negation is a weak modifier the strongly-activated concept overruns, so the ban half-reads as an instruction to do the thing. Prompt the **positive** — state the target behaviour ("write one-line comments") so the banned one is never spoken. A prohibition earns its place only as a hard guardrail you cannot phrase positively; even then, pair it with the positive target so attention lands on what to do.

**문법·구조**: 네 문장이지만 세미콜론과 대시로 절이 여섯 개쯤 이어진 밀도 높은 단락이다. 첫 문장은 콜론 앞에서 `Negation` 을 이름 붙이고 콜론 뒤에서 동명사 주어 `steering by prohibition` 에 동사 둘(`drags`, `makes`)을 붙인다. 끝의 `more available, not less` 는 `A, not B` 대비. 둘째 문장 `Don't think of an elephant, and the elephant is all there is` 는 "명령문 + and + 결과" 구문으로 "~하면 …된다"라는 조건을 담는다(`Push it, and it opens.` 와 같은 틀). 세미콜론 뒤 `a weak modifier the strongly-activated concept overruns` 는 목적격 관계대명사 `that` 이 빠진 관계절이다. `half-reads as` 는 "반쯤 ~로 읽힌다"는 조어. 셋째 문장은 명령문 `Prompt the positive` 뒤에 대시로 구체 지침을 붙이고 `so` 뒤는 "그러면 금지된 쪽은 입에 오르지도 않게"라는 목적의 절이다. 마지막 문장은 `only as` 로 예외를 좁게 허용하고 세미콜론 뒤 `even then` 으로 그 예외에도 조건을 하나 더 건다. 허용 → 제한 → 추가 조건 순서가 규칙 글의 전형이다.

**핵심 표현**: `Don't think of an elephant` — 금지하면 오히려 그 생각을 떠올리게 된다는 유명한 비유. / `earn its place only as …` — 존재 조건을 좁게 거는 틀. / `so attention lands on what to do` — 주의가 "할 일"에 내려앉게 한다는 목적절.

**격식 짝**: (작성)
- refined: Instructions phrased as prohibitions tend to prime the very behaviour they forbid; a positive statement of the desired behaviour is more reliable.
- plain: If you tell it what not to do, you're basically putting the idea in its head. Just tell it what to do instead.

<sub>출처: transcript:[user] auto-recipe-creator (writing-for-agents 스킬 본문)</sub>
