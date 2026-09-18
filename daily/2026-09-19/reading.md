# 2026-09-19 — 정독

> auto_recipe_creator 설계 문서와 skewnono chat→RAG 계약 편지는 한국어 본문이라 인용할 영어 단락이 없다. 세 단락 모두 transcript 의 `[assistant]` 영어다. 원문 그대로이며 굵은 글씨·백틱과 번호 머리(`1.`)만 풀어 한 단락으로 이었다.

## 단락 1

It is the cluster, not the backend. The _shards.failed=2 number comes straight from OpenSearch's own response metadata. Two shards could not execute the aggregation, so OpenSearch returned a partial answer, and the backend deliberately refuses to serve it. Line 201 of _office_search.py is a guard doing its job, not a bug. Most likely cause, given the two-index query: a per-index mapping mismatch. When you aggregate across meas_hist_cdsem,meas_hist_hvsem, a field used in the agg (terms, date_histogram, or a sort in top_hits) may be keyword in one index and text or absent in the other. OpenSearch then fails the shards of the offending index and succeeds on the rest. Two failed shards fitting one index's shard count would confirm this. Less likely alternatives are a genuinely red/unassigned shard or a circuit-breaker trip on a large bucket count.

**문법·구조**: "DB 문제냐 백엔드 문제냐"는 양자택일 질문에 첫 문장에서 바로 답한다. `It is A, not B` 는 결론을 앞에 두는 분열문형이라 뒤따르는 문장은 모두 근거가 된다. 둘째·셋째 문장은 과거형(`could not`, `returned`)으로 실제로 일어난 일을, 넷째 문장부터는 현재형(`refuses`, `is`, `fails`)으로 코드와 시스템의 상시 동작을 말한다. `deliberately` 한 단어가 "거절이 실수가 아니라 설계"임을 못 박는다. `Most likely cause, given …:` 는 동사 없는 메모체 제목 문장이고, 콜론 뒤에 답을 둔다. `given` 은 전치사처럼 쓰여 "~를 고려하면"이다. 추측의 강도가 단계적으로 내려가는 것도 볼 만하다. `may be`(가능성) → `would confirm`(이런 증거가 나오면 확정) → `Less likely alternatives are …`(낮은 순위 후보)로, 확신의 정도를 조동사와 형용사로 조절한다. `Two failed shards fitting one index's shard count` 는 분사구가 주어를 꾸며 "한 인덱스의 샤드 수와 맞아떨어지는 실패 샤드 두 개"라는 긴 명사구를 만든다.

**핵심 표현**: `a guard doing its job, not a bug` — 에러를 낸 코드가 정상 작동한 방어선이다. / `the offending index` — 문제를 일으킨 쪽. `offending` 은 "말썽인, 문제의"라는 뜻의 형용사다. / `would confirm this` — 이런 증거가 나오면 가설이 확정된다는 조건부 표현.

**격식 짝**: (작성)
- refined: The failure originates in the cluster rather than the application; the backend is correctly declining to serve an incomplete result.
- plain: It's the database, not our code. The backend's just refusing to show you half an answer.
- refined: A shard-failure count matching a single index's shard allocation would substantially confirm this hypothesis.
- plain: If the two failed shards are exactly one index's worth, that pretty much proves it.

<sub>출처: transcript:[assistant] skewnono_v3_nuxt</sub>

---

## 단락 2

Short answer: heavy use cannot interrupt or abort the restart. It can only lose the requests that are in flight at 00:05, and there is one unrelated way the restart itself fails. How the reload actually works. restart.txt is a touch-reload trigger, which is uWSGI's SIGHUP-style graceful reload. The master keeps the listening socket open, tells all 4 workers to finish their current requests and exit, then boots 4 new ones. Nothing a client sends can cancel that sequence. New connections during the boot gap sit in the socket backlog, so a few seconds of latency is the normal cost. Only if the backlog overflows do clients see 502s at the ingress.

**문법·구조**: `Short answer:` 로 결론을 먼저 주고 `How the reload actually works.` 라는 소제목 조각으로 설명 단계에 들어간다. 대화체 기술 설명에서 흔한 "결론 → 원리" 구조다. 조동사 `cannot` 과 `can only` 가 짝을 이뤄 "막을 수는 없고, 잃을 수 있는 건 이것뿐"이라는 범위를 긋는다. `which is uWSGI's … graceful reload` 는 앞 명사를 풀어 주는 계속적 관계절이다(쉼표 뒤 `which`). 다섯째 문장은 주어 하나(`The master`)에 동사 셋(`keeps`, `tells`, `boots`)을 순서대로 걸어 절차를 그렸고, 마지막 동사 앞에는 `and` 대신 `then` 을 써 시간 순서를 강조했다. `Nothing a client sends can cancel …` 은 `Nothing (that) a client sends` 에서 관계대명사가 생략된 부정 주어 문장이다. 마지막 문장이 핵심 문법이다. `Only if …` 가 문두에 오면 주절이 도치되어 `do clients see` 가 된다. "백로그가 넘칠 때에만 비로소 502가 보인다"는 한정이 도치 덕분에 강하게 들린다.

**핵심 표현**: `in flight` — 처리 중인(요청·작업이 아직 끝나지 않은). / `sit in the (socket) backlog` — 대기열에서 기다리다. `sit` 이 "아무것도 안 하고 머무른다"는 느낌을 준다. / `the normal cost` — 정상 동작에 따라오는 예상된 비용이라 버그가 아니라는 뜻.

**격식 짝**: (작성)
- refined: Only in the event that the backlog overflows would clients encounter 502 errors at the ingress.
- plain: Clients only get 502s if the backlog fills up.
- refined: Client activity has no means of cancelling the reload sequence once it has begun.
- plain: Once it starts, nothing a user does can stop it.

<sub>출처: transcript:[assistant] skewnono_v3_nuxt</sub>

---

## 단락 3

Let the current session finish. Turn off the schedule or loop and wait until the running agent and its child processes exit. Don't copy files in while it's still working. It already has the old letter text loaded, and when it finishes a letter it hashes whatever file is on disk at that moment. If the new file is there by then, the done line gets the new hash for work that followed the old text, and the stale work is never caught.

**문법·구조**: 절차 안내라 첫 세 문장이 명령문이다. `Let … finish`, `Turn off … and wait until …`, `Don't copy …` 로 할 일과 하지 말 일을 먼저 늘어놓고, 넷째 문장부터 그 이유를 댄다. `has the old letter text loaded` 는 `have + 목적어 + 과거분사` 로 "옛 텍스트를 이미 불러온 상태"를 가리킨다. `hashes whatever file is on disk at that moment` 의 `whatever` 는 "그 순간 디스크에 있는 파일이 무엇이든"이라는 복합관계사로, 에이전트가 파일을 가리지 않는다는 점이 버그의 핵심이다. 마지막 문장은 1형 조건문(`If … is …, … gets …`)인데 주절을 현재형으로 써서 "그러면 반드시 이렇게 된다"는 인과를 규칙처럼 말한다. `by then` 은 "그때까지는", `work that followed the old text` 의 `follow` 는 "(지시를) 따르다"다. 끝의 `is never caught` 는 수동태로, 잡아낼 주체보다 "아무도 못 잡는다"는 결과에 초점을 둔다.

**핵심 표현**: `Let (something) finish` — 진행 중인 작업을 끊지 말고 끝나게 두다. / `whatever file is on disk at that moment` — 그 순간 있는 것이면 무엇이든. / `the stale work is never caught` — 낡은 기준으로 한 작업이 끝내 발견되지 않는다.

**격식 짝**: (작성)
- refined: Please allow the current session to complete before replacing any files.
- plain: Wait for it to finish before you copy anything in.
- refined: Otherwise, work performed against the superseded text would be recorded as current and would escape detection.
- plain: If you don't, the old work gets marked as up to date and nobody notices.

<sub>출처: transcript:[assistant] equipment-data-map</sub>
