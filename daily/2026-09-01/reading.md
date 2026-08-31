# 2026-09-01 — 정독

## 단락 1

**This is the skill.** Everything else is mechanical. If you have a **tight** pass/fail signal for the bug — one that goes red on _this_ bug — you will find the cause; bisection, hypothesis-testing, and instrumentation all just consume it. If you don't have one, no amount of staring at code will save you. Spend disproportionate effort here. **Be aggressive. Be creative. Refuse to give up.**

**문법·구조**: 전체가 현재시제로 굴러간다. 절차를 설명하는 글이 아니라 **언제나 참인 규칙**을 선언하는 글이어서다 — 과거시제를 한 번이라도 섞으면 "그때 그랬다"는 사례담으로 내려앉는다. 세 번째 문장이 이 단락의 뼈대다. `If you have ...` 조건절 뒤에 결과절 `you will find the cause` 가 오고, 세미콜론 뒤에 근거 절이 하나 더 붙는 3단 구조. 세미콜론을 쓴 이유가 있다 — `because` 로 이었으면 종속절이 되어 힘이 빠지고, 마침표로 끊었으면 앞 문장과의 연결이 끊긴다. 세미콜론은 두 절을 대등하게 붙여 둔다. `all just consume it` 의 `all` 은 앞의 세 명사를 되받는 동격 대명사고, `just` 가 "그것들은 도구일 뿐 주인공이 아니다"를 한 단어로 처리한다. 그다음 `If you don't have one` 은 앞 조건의 정확한 뒤집기라 두 문장이 짝을 이룬다. 마지막 세 개의 명령문은 모두 두 단어 — 앞 문장들이 길었기 때문에 짧은 리듬이 종결부로 기능한다.

**핵심 표현**:
- `goes red on this bug` — 신호가 이 버그에 반응해 실패로 바뀐다. `is red` 가 상태라면 `goes red` 는 전이라, "지금 통과 중인데 이 버그가 있으면 실패로 돌아설 수 있는가"라는 검증 조건이 된다.
- `no amount of X will save you` — 양으로는 안 된다는 강한 부정. 노력 부족이 아니라 접근법이 틀렸다고 말하는 자리.
- `Spend disproportionate effort here.` — 균형 있게 나누지 말라는 지시. `disproportionate` 의 부정적 어감을 일부러 뒤집어 썼다.

**격식 짝**:
- refined: *Resources allocated to this phase should be deliberately out of proportion to its share of the overall work.* (작성)
- plain: *Blow way more time on this bit than feels reasonable.* (작성)
- refined: *In the absence of such a signal, further code inspection is unlikely to yield the cause.* (작성)
- plain: *Without that, you can stare at the code all day and get nowhere.* (작성)

<sub>출처: transcript:auto-recipe-creator aeec243f — `diagnosing-bugs` 스킬 본문</sub>

---

## 단락 2

Short answer: **I'd leave them as they are.** The `_` prefix already *is* the grouping — moving them under one folder buys a shorter `ls` and costs a repo-wide rename plus an office boot break. […] The prefix is load-bearing in two places: `back_dev_home/__init__.py:284` (blueprint auto-discovery skips any `_` path part) and `_runtime/office_registry.py:42` (feature slug registry does the same). A single `_infra/` folder would still need that underscore, so the rule doesn't get simpler — you'd just have one more nesting level. The real cost is at the office: every gitignored `providers/office.py` copy imports `back_dev_home._runtime.office_redis` etc. After the rename, each one fails at import and the whole app factory refuses to boot until every adapter is re-`cp`'d — the "stale office.py breaks boot" failure mode, but for all features at once.

**문법·구조**: 반대 의견을 쓸 때의 모범적인 순서다. 결론(`I'd leave them as they are`)이 맨 앞에 오고 근거가 뒤따른다. 조동사 `would` 가 핵심이다 — `I leave them` 은 사실 보고, `I'd leave them` 은 "내가 결정권자라면"이라는 가정을 깔아 권고로 만든다. 상대의 결정권을 뺏지 않고 의견을 내는 자리에서 이 `'d` 하나가 온도를 정한다. 두 번째 문장의 이탤릭 `*is*` 는 강조 조동사 `does` 를 쓸 수 없는 be동사 자리에서 같은 일을 한다("이미 그것이 바로 그루핑이다"). `buys A and costs B` 는 한 주어에 동사 둘을 걸어 득실을 나란히 놓는 대구고, 이득 쪽을 `a shorter ls` 처럼 사소하게 잡아 두면 판정이 문장 안에서 저절로 난다. 뒷부분은 시제가 움직인다 — 현재형(`still need`, `imports`)으로 지금의 사실을 말하다가, `After the rename` 뒤에서 `fails`·`refuses` 로 **가상의 미래를 현재형으로** 그린다. `would fail` 대신 현재형을 쓰면 그 일이 이미 일어난 것처럼 생생해진다. 마지막 대시 뒤 `but for all features at once` 는 동사 없는 조각인데, 앞 절을 통째로 받아 규모만 갱신하는 자리라 문장으로 늘리면 오히려 늘어진다.

**핵심 표현**:
- `load-bearing in two places` — 빼면 무너지는 자리가 둘. 건축의 내력벽 비유를 쓰면 "중요하다"보다 훨씬 구체적인 주장이 된다.
- `the rule doesn't get simpler — you'd just have one more nesting level` — 제안의 목적(단순화)이 실제로 달성되지 않는다는 반박. 상대의 목표를 그대로 인용해 안에서 무너뜨린다.
- `the real cost is at the office` — 진짜 비용은 다른 곳에 있다. `the real X` 는 앞서 나온 비용 계산이 불완전했음을 예고하는 신호어다.

**격식 짝**:
- refined: *My recommendation is to leave the current layout in place.* (작성)
- plain: *I'd just leave them where they are.* (작성)
- refined: *The consolidation would deliver marginal benefit at substantial migration cost.* (작성)
- plain: *You'd get a tidier folder list and pay for it with a rename across the whole repo.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt f2d1927f — `[…]` 는 중간 항목 두 개를 생략한 자리</sub>

---

## 단락 3

The two PIDs on 5050 weren't a leak — that's the normal Werkzeug reloader shape: the parent watches files and re-execs a child that actually serves. Killing the parent alone can orphan the child still holding the socket, so both need the signal. Note the child had *two* FDs on the same socket (3u and 4u) — that's the inherited listener plus its own dup, not a second bind. This project's scheduler runs in that reloader **child** specifically (per CLAUDE.md, "the Werkzeug reloader's app child at home"), so killing 5050 also stops periodic jobs — worth knowing if you later wonder why `/api/health/jobs` shows a gap. `lsof` exiting 1 when it finds nothing is why the compound command uses `|| echo` rather than trusting exit status — the "error" on the first call was just port 3000 being empty.

**문법·구조**: 다섯 문장이 전부 `X, not Y` 또는 `X — that's actually Z` 구조로 짜여 있다. 오해를 먼저 세우고 그 자리에 사실을 갈아 끼우는 틀이다. 첫 문장은 부정(`weren't a leak`)으로 열고 대시 뒤에서 정정하며, 콜론이 그 정정을 다시 한 단계 풀어 준다 — 부정 · 정정 · 설명이 한 문장 안에 층으로 쌓인다. `a child that actually serves` 의 관계절에서 `actually` 는 앞의 부모 프로세스와 대조하는 자리라 빼면 문장이 밋밋해진다. 두 번째 문장의 `the child still holding the socket` 은 관계절을 줄인 현재분사 수식이고, `which is still holding` 보다 짧아 기술 설명에서 선호된다. 네 번째 문장은 삽입 괄호로 근거 문서를 인용한 뒤 `so` 로 결과를 잇고 다시 대시로 조언을 얹는 3단 확장이다. 마지막 문장은 특이한 배치를 쓴다 — 동명사구 `lsof exiting 1 when it finds nothing` 이 통째로 주어 자리에 앉고 `is why ...` 가 이어져서, 원인을 주어로 세우고 결과를 술어로 놓는다. 원인 · 결과 순서가 문장 순서와 그대로 겹쳐 읽기 쉽다.

**핵심 표현**:
- `orphan the child` — 부모를 죽여 자식 프로세스를 고아로 만들다. 표준 용어라 설명 없이 통한다.
- `not a second bind` — 두 번 bind 한 게 아니다. 독자가 떠올릴 법한 오해를 마지막에 한 조각으로 못 박는 마무리.
- `rather than trusting exit status` — 종료 코드를 믿는 대신. `rather than -ing` 은 버린 선택지를 명시해 결정을 방어하는 표준 틀이다.

**격식 짝**:
- refined: *Terminating the parent in isolation may leave the child orphaned while it continues to hold the listening socket.* (작성)
- plain: *Kill just the parent and you can end up with a stray child still sitting on the port.* (작성)
- refined: *This is worth noting should you later observe a gap in the scheduled-job history.* (작성)
- plain: *Handy to know if you later wonder why the jobs page has a hole in it.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt 81fe0f54</sub>

