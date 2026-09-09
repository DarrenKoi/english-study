# 2026-09-10 — 정독

## 단락 1

A process surviving SIGKILL isn't defying you; it's in uninterruptible sleep (D state), so the kill is queued until it comes out. For this model that's almost always one of two things: reading the ~48GiB of shards off a network mount, so a blocking read can sit in D state for a while, or CUDA teardown — the driver ioctl freeing GPU memory. Both resolve on their own, typically within seconds. The 1-second re-check is just impatient. But the PID file is deliberately kept as a flag so you don't silently start on top of it — check rather than assume. If both are clean, delete the stale file or just ignore it. If the PID *is* still alive and holding GPU memory minutes later, that's the real problem case: don't start, investigate the mount.

**문법·구조**: 첫 문장의 `A process surviving SIGKILL` 은 명사 뒤에 현재분사를 붙여 관계절 `that survives SIGKILL` 을 통째로 줄인 축약형이다. 주어가 길어지는 대신 문장이 하나로 붙어 리듬이 빨라진다. 세미콜론이 "부정 → 진짜 설명" 을 접속사 없이 잇고, 이어지는 `so` 가 결과를 단다. 중간의 콜론은 목록 예고 신호로 `one of two things:` 뒤에 두 항목이 `or` 로 걸린다 — 앞 항목이 길어 대시로 보충 설명을 밀어 넣은 자리에 주목할 것. 끝의 조건문 두 개는 `If ... , ...` 병렬로 나란히 놓여 "깨끗하면 / 아니면" 판단 트리를 만든다. `is` 를 이탤릭으로 강조한 것은 앞 조건과의 대조를 표시하는 문어적 장치다.

**핵심 표현**: `isn't defying you` — 기계를 의인화해 놓고 그 의인화를 곧바로 부정하는 방식이라, 사용자가 품기 쉬운 감정(왜 안 죽지?)을 먼저 인정하고 사실로 갈아끼운다. `Both resolve on their own` — 자동사 `resolve` 로 행위자를 지운다. `check rather than assume` — 명령형 두 동사를 `rather than` 으로 대비시킨 격언형. 조언을 짧게 못 박을 때 쓰는 틀이다.

**격식 짝**:
- refined: *The warning is retained deliberately, so that a subsequent launch cannot proceed on top of a live process.* / plain: *We keep the PID file on purpose so you don't start on top of something that's still running.* (작성)
- refined: *Both conditions are transient and typically clear within seconds.* / plain: *Both sort themselves out, usually in a few seconds.* (작성)

<sub>출처: transcript:[assistant] llm-serving — PID 파일 경고 설명</sub>

---

## 단락 2

So this deletion removes an accurate, load-bearing guard — the one that stops a future session from pasting a real `MODEL_ROOT` or an internal hostname into a public repo, and the one that stops it from "helpfully" repopulating the deliberately-empty READMEs. It's the kind of paragraph whose whole value is being in context before the mistake. This is a specific failure mode of CLAUDE.md pruning: a rule that has never fired looks like dead weight. But a preventative guard's payoff is invisible by construction — you only ever see the cost of its absence. The repo has already paid that cost once, which is exactly why the paragraph was written.

**문법·구조**: 첫 문장은 대시 뒤에 `the one that ... , and the one that ...` 을 나란히 놓아 하나의 guard 를 두 역할로 쪼갠다. 같은 틀을 반복하니 두 번째를 읽을 때 독자가 구조를 이미 알고 내용에만 집중한다. `whose whole value is being in context` 에서 소유격 관계대명사 `whose` 가 사물에 붙었고(문어에서 흔하다), 보어 자리에 동명사구가 왔다 — "가치 = 미리 놓여 있음" 이라는 등식이 문법으로 표현된 셈. `a rule that has never fired` 는 현재완료라 "지금까지 한 번도" 라는 누적 구간을 담는다. `you only ever see` 의 `only ever` 는 예외 없음을 강조하는 구어적 결합이고, 마지막 `which` 는 앞 문장 전체를 받는 비제한적 관계절이다.

**핵심 표현**: `load-bearing` — 건축의 내력벽 은유. 장식이 아니라 구조를 떠받친다는 뜻이라 "지워도 되는 문장" 판정을 뒤집을 때 쓴다. `has never fired` — 규칙·알람을 총·트리거에 빗대는 관용. `invisible by construction` — 수학·논리에서 온 `by construction`(정의상 자동으로)이 일상 논증에 들어온 자리로, "우연히 안 보이는 게 아니라 원리상 안 보인다"는 강한 주장을 짧게 만든다.

**격식 짝**:
- refined: *A preventative control yields no observable benefit; its value is only revealed when it is absent.* / plain: *You never notice a guard working — you only notice when it's gone.* (작성)
- refined: *The rule has not been invoked to date, which is not evidence that it is redundant.* / plain: *It's never come up, but that doesn't mean we don't need it.* (작성)

<sub>출처: transcript:[assistant] llm-serving — CLAUDE.md 가드 삭제 검토</sub>

---

## 단락 3

Running the launcher on a live stack fails in a way that looks like success. The readiness probe hits `127.0.0.1:8006/v1/models` and the **old** instance answers, so the script logs "ready" and moves on. Meanwhile the new duplicate process is still loading 48GiB of weights. It only discovers the port is taken *after* the load, because vLLM binds late. That load is the host-RAM peak, and two overlapping loads are exactly the OOM condition the startup ordering was written to prevent. Checking a port rather than a process is the subtle trap here: port-liveness proves that something is serving, but it cannot distinguish "my process came up" from "someone else's process is already there." That is why the fix puts the stop *before* the start instead of making the readiness check smarter — ordering beats detection.

**문법·구조**: 동명사 주어 `Running the launcher ...` 로 열어 행위 자체를 주어 자리에 앉혔다 — 조건절(`If you run ...`)보다 압축적이고 문어적이다. 두 번째 문장의 `so` 는 원인이 아니라 **결과**를 달고, 세 번째의 `Meanwhile` 은 시간 대비를 만들어 "겉으로는 성공 / 속에서는 중복 로딩" 이라는 이중 서사를 세운다. `It only discovers ... after the load, because ...` 에서 `only` 를 동사 앞에 두면 "그제서야" 라는 늦음이 살아난다. 후반부의 `cannot distinguish A from B` 는 구별 불가를 말하는 정형 패턴이고, 인용부호로 감싼 두 문장을 명사처럼 A·B 자리에 넣은 게 이 문장의 요령이다. 마지막 `ordering beats detection` 은 관사 없는 추상명사 둘을 `beats` 로 맞붙인 격언형 — 앞의 긴 설명을 세 단어로 봉인한다.

**핵심 표현**: `binds late` — 포트를 늦게 잡는다는 기술 서술이지만, 실패가 늦게 드러나는 이유를 한 단어(`late`)로 지목한다. `the subtle trap here` — 명백한 버그가 아니라 판단이 미끄러지는 지점을 가리킬 때. `ordering beats detection` — 설계 원칙을 슬로건화하는 `X beats Y` 틀. 회의에서 결론을 한 줄로 남길 때 유용하다.

**격식 짝**:
- refined: *The readiness check cannot distinguish a newly started instance from a pre-existing one.* / plain: *The check can't tell your process apart from one that was already there.* (작성)
- refined: *Sequencing the stop before the start is more reliable than refining the detection logic.* / plain: *It's easier to stop it first than to make the check clever.* (작성)

<sub>출처: transcript:[assistant] llm-serving — start_all 가드 (원문에서 한국어 로그 문구는 "ready" 로 대체)</sub>

