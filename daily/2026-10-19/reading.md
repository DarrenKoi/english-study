# 2026-10-19 — 정독

## 단락 1

Note that disk has the exact same risk: if two hosts write to a path keyed by *filename only*, they clobber each other — that *is* cross-host mixing, just on disk. The repo's `recipe_log_collector` avoids it with a `uuid4` folder + per-IP subdir. Correctness comes from isolating the destination per host (unique buffer *or* unique path) and not sharing a connection — not from the storage medium. asyncio never moves data between coroutines on its own; each task has its own stack. When disk genuinely wins: memory pressure, not correctness. Large files × high concurrency can exceed worker RAM; streaming to disk keeps RAM flat.

**문법·구조**: 첫 문장은 `Note that …` 으로 시작해 독자의 시선을 반대쪽으로 돌린다. 콜론 뒤 `if` 조건절이 위험이 생기는 조건을 대고, 대시 뒤 `that *is* cross-host mixing, just on disk` 가 재판정을 내린다. 여기서 `is` 를 기울인 것은 강조의 `is` 로, "그것이야말로 바로 섞임이다"라는 반박 억양을 글로 옮긴 것이다. 셋째 문장이 단락의 결론이다. `comes from A and B — not from C` 로 동명사구 두 개(`isolating …`, `not sharing …`)를 원인으로 세우고 대시 뒤에서 오해된 원인을 지운다. 넷째 문장은 `never … on its own` 으로 asyncio 에 대한 막연한 의심을 끊고, 세미콜론 뒤에 근거(`each task has its own stack`)를 붙인다. 다섯째는 동사 없는 소제목형 문장으로 양보를 시작하고, 마지막 문장이 그 조건을 수치 느낌의 `×` 기호로 압축한다. 시제는 끝까지 단순현재다. 특정 사건이 아니라 늘 성립하는 성질을 말하기 때문이다.

**핵심 표현**:
- `that *is* X, just on Y` — "모양만 다를 뿐 똑같은 X 다"라고 재분류하는 반박 틀.
- `Correctness comes from A — not from B` — 올바름의 출처를 옮겨 주는 결론 문장.
- `keeps RAM flat` — 입력이 늘어도 메모리 그래프가 평평하게 유지된다는 그림.

**격식 짝**:
- refined (작성): Correctness depends on per-host isolation of the destination, not on the choice of storage medium.
- plain (작성): It's not about memory versus disk — it's about each host writing to its own place.

<sub>출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md ("In-memory vs. disk")</sub>

---

## 단락 2

The Flask proxy mounts as a blueprint on the existing company API uWSGI app. That app's envelope (`api/wsgi.ini`): `processes=4`, `reload-on-rss=1500` (MB), `harakiri=60` (s), on an **8 GiB** host, and it already runs memory-heavy pandas/Arrow tasks (600–800 MB per request per the wsgi comments). The proxy borrows from that same per-worker budget — it does not get a fresh one. At the original defaults a batch landing several large hosts reaches ~1.4 GB transient — at the `reload-on-rss=1500` cliff — and can recycle the worker **mid-request**, failing the whole batch and potentially disrupting an in-flight pandas task in that worker. Separately, `host_timeout=60 ≥ harakiri=60` lets one stalled host consume the entire request budget so uWSGI kills the request before the downloader's own graceful backstop fires.

**문법·구조**: ADR 의 Context 절이라 판단 없이 사실만 현재시제로 늘어놓는다. 둘째 문장은 `envelope` 라는 명사 하나 뒤에 콜론을 찍고 설정값을 나열한다. 동사 없이 목록부터 보여 주다가 `and it already runs …` 에서야 동사가 나오는데, `already` 가 "이미 무거운 일을 하고 있는 곳에 얹힌다"는 압박을 만든다. 셋째 문장은 같은 내용을 긍정(`borrows`)과 부정(`does not get a fresh one`)으로 두 번 말해 오해를 막는다. 넷째 문장이 길다. 주어 `a batch landing several large hosts` 에서 `landing` 은 현재분사 후치 수식으로 "큰 호스트 여럿이 걸린 배치"다. 동사는 `reaches` 와 `can recycle` 두 개고, 그 뒤 분사구문 `failing …` 과 `potentially disrupting …` 이 결과를 이어 붙인다. 대시로 낀 `at the … cliff` 는 그 수치가 어떤 의미인지 알려 주는 삽입이다. 마지막 문장은 `Separately` 로 별개의 두 번째 위험을 연다. `lets A do B so C` 꼴로 허용 → 결과를 잇고, `before` 절로 순서가 뒤집히는 문제를 짚는다. 사람 주어가 하나도 없다. 시스템 구성요소(`proxy`, `batch`, `uWSGI`)가 주어가 되어 능동태로 움직이는 것이 장애 서술의 전형이다.

**핵심 표현**:
- `borrows from that same budget — it does not get a fresh one` — 공유 자원임을 두 번 못 박는다.
- `can recycle the worker mid-request` — 요청 처리 도중 워커가 재시작될 수 있다. `mid-` 접두사로 시점을 압축한다.
- `before the … backstop fires` — 안전장치가 작동하기도 전에. `fire` 는 타이머·알람이 "터지다, 작동하다".

**격식 짝**:
- refined (작성): A single unresponsive host may exhaust the request's time allowance, causing uWSGI to terminate it prematurely.
- plain (작성): One stuck host can eat the whole time limit, and then uWSGI just kills the request.

<sub>출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md (Context 중 일부, 문장 사이 일부 생략)</sub>

---

## 단락 3

These are baked in as defaults, not left to the call site, because the defaults exist to give a caller who hasn't done this math a safe result on the shared host. Roughly 4× more HTTP round trips for the same fleet. Acceptable — the proxy path is the firewalled fallback, not the hot path, and the trips run concurrent. If the file profile changes materially — many hosts each dumping several 10MB+ files — small batches stop being enough and the proxy should move to a **streaming transport**. That is the rewrite this ADR deliberately defers. Do **not** "optimize" `request_batch` back up without re-checking the `reload-on-rss` / pandas-stacking math above; the small value is load-bearing.

**문법·구조**: 결정과 그 대가를 적는 Consequences 단락이다. 첫 문장은 수동태 `are baked in` 과 `(are) not left to` 를 `X, not Y` 로 맞세운다. 누가 박았는지는 중요하지 않아 수동태를 썼고, `because` 절이 기본값의 존재 이유를 설명한다. 둘째 문장은 동사가 없는 명사구다. 비용을 먼저 툭 던지고, 셋째 문장 `Acceptable —` 한 단어로 판정한 뒤 대시 뒤에 근거를 댄다. "비용 → 판정 → 근거" 순서가 ADR 다운 리듬이다. 넷째 문장은 `If … changes materially` 조건절 안에 대시로 구체적 상황을 끼우고, 주절에서 `stop being enough` 와 `should move to` 로 결과와 권고를 나눈다. 다섯째 문장의 `That` 이 앞 문장의 streaming transport 전체를 받아 "의도적 보류"로 못 박는다. 마지막은 명령문 금지(`Do not`)에 세미콜론으로 이유를 붙여 닫는다.

**핵심 표현**:
- `baked in as defaults, not left to the call site` — 호출하는 쪽에 맡기지 않고 기본값으로 박아 넣었다.
- `Acceptable —` — 비용을 인정하고 감수하겠다는 한 단어 판정.
- `stop being enough` — 지금은 충분하지만 어느 시점부터 모자라게 된다는 변화의 동사구.

**격식 짝**:
- refined (작성): This overhead is acceptable, given that the proxy serves only as a fallback for firewalled clients.
- plain (작성): It's more round trips, but that's fine — the proxy is just the backup route.

<sub>출처: repo:bulk_recipe_copy ftp_handler/docs/adr/0001-proxy-batch-sizing.md (Decision 끝 문장 + Consequences, 괄호·수치 일부 생략)</sub>
