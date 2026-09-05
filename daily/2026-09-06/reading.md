# 2026-09-06 — 정독

## 단락 1

The Flask proxy (`ftp_handler/ftp_flask_proxy.py`) mounts as a blueprint on the existing company API uWSGI app. That app's envelope (`api/wsgi.ini`): `processes=4`, `reload-on-rss=1500` (MB), `harakiri=60` (s), on an **8 GiB** host, and it already runs memory-heavy pandas/Arrow tasks (600–800 MB per request per the wsgi comments). The proxy borrows from that same per-worker budget — it does not get a fresh one. At the original defaults (`request_batch=20`, `host_timeout=60`, `client_workers=8`) a batch landing several large hosts reaches ~1.4 GB transient — at the `reload-on-rss=1500` cliff — and can recycle the worker mid-request, failing the whole batch and potentially disrupting an in-flight pandas task in that worker. Separately, `host_timeout=60 ≥ harakiri=60` lets one stalled host consume the entire request budget so uWSGI kills the request before the downloader's own graceful backstop fires.

**문법·구조**: 다섯 문장이 전부 **현재시제**다. 과거에 벌어진 사건을 보고하는 글이 아니라 "지금 이 시스템이 이렇게 생겼다" 는 상태 서술이라서, ADR 의 Context 절은 관례적으로 현재로 쓴다. 시제가 바뀌는 자리는 딱 하나 — `it already runs` 의 `already` 로, 이건 시제가 아니라 부사가 "우리가 오기 전부터" 를 담당한다.

두 번째 문장은 동사가 없다. `That app's envelope (...): processes=4, ...` 는 콜론 뒤에 설정값을 나열한 명사 조각인데, 기술 문서에서 스펙을 던질 때 허용되는 생략형이다. 다만 뒤에 `and it already runs ...` 를 접속사로 붙여 다시 완전한 절로 돌아온다 — 조각으로 시작해 절로 착지하는 이 리듬이 스펙 나열을 문장으로 흡수한다.

네 번째 문장의 무게중심은 **분사구문**이다. `can recycle the worker mid-request, failing the whole batch and potentially disrupting an in-flight pandas task`. `-ing` 두 개가 앞 절의 **결과**를 이어 붙인다(`so that it fails ...` 를 줄인 것). 결과를 새 문장으로 끊지 않고 분사로 매달면 "워커 재활용 → 배치 실패 → 남의 작업까지 피해" 가 한 번의 사건으로 읽힌다. 인과 사슬을 보여줄 때 쓰는 정석이다.

마지막 문장의 `so` 는 목적이 아니라 **결과**다(`so that ... may` 가 아니라 `and as a result`). 그리고 `before ... fires` 의 `fires` 는 자동사 — 타이머·핸들러가 "발동한다" 는 뜻으로, 주어가 사람이 아닐 때 `trigger` 대신 흔히 쓴다.

**핵심 표현**:
- **envelope** — 한 앱이 움직일 수 있는 자원 한계선 전체. `budget` 이 총액이라면 `envelope` 은 그 총액을 규정하는 설정 묶음(프로세스 수·RSS 상한·타임아웃)까지 포함한다.
- **borrows from that same budget — it does not get a fresh one** — 새 컴포넌트가 자기 몫을 따로 받는 게 아니라 남의 예산을 나눠 쓴다는 경고. 오해를 직접 서술하지 않고 부정문 하나로 닫는다.
- **at the cliff** — 임계값을 넘으면 완만히 나빠지는 게 아니라 뚝 떨어진다는 그림. 이 단어를 고른 순간 "여유가 없다" 가 아니라 "한 번 넘으면 끝난다" 가 된다.

**격식 짝**:
- refined: *The proxy borrows from that same per-worker budget; it does not receive an allocation of its own.*
- plain: *The proxy has to share whatever memory that worker already has — it doesn't get its own.* (작성)
- refined: *One stalled host may consume the entire request budget.*
- plain: *One host that hangs can eat the whole request.* (작성)

<sub>출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md</sub>

---

## 단락 2

Roughly 4× more HTTP round trips for the same fleet (60 batches vs 15 at 300 hosts). Acceptable — the proxy path is the firewalled fallback, not the hot path, and the trips run `client_workers=4` concurrent. If the file profile changes materially — many hosts each dumping several 10MB+ files — small batches stop being enough and the proxy should move to a **streaming transport** (chunked / multipart per file, dropping base64's 33% bloat). That is the rewrite this ADR deliberately defers. Do **not** "optimize" `request_batch` back up without re-checking the `reload-on-rss` / pandas-stacking math above; the small value is load-bearing.

**문법·구조**: 단락 1이 현재시제로 사실을 깔았다면 여기는 **조동사가 문장을 끌고 간다**. `should move`(권고), `stop being`(예측), `Do not`(금지). 같은 문서 안에서 절이 바뀌면 서법도 바뀌는 게 ADR 의 문법적 뼈대다 — Context 는 직설법, Consequences 는 조건법·명령법.

첫 두 문장은 또 동사가 없다. `Roughly 4× more HTTP round trips ...` 그리고 `Acceptable — ...`. 비용을 던지고 곧바로 판정을 던지는 순서라, "비용이 있다 / 그런데 받아들일 만하다" 사이에 `This is` 를 넣을 자리가 없어야 대비가 산다. 판정어를 문장 맨 앞 단독으로 놓는 이 배치는 리뷰 코멘트에서도 그대로 쓸 수 있다.

세 번째 문장의 대시 삽입구를 눈여겨본다. `If the file profile changes materially — many hosts each dumping several 10MB+ files — small batches stop being enough`. 조건절과 주절 사이에 **조건이 무슨 뜻인지 예시**를 대시로 끼워 넣었다. 괄호였다면 곁가지로 읽혔을 텐데, 대시라서 조건의 정의로 읽힌다. `each dumping` 은 `many hosts` 를 받는 분사구다(`each of which dumps`).

마지막 문장의 세미콜론이 이 단락에서 제일 배울 만하다. 앞은 금지, 뒤는 그 **근거**다. `because` 로 이었으면 근거가 종속절로 내려가 힘이 빠지는데, 세미콜론은 두 절을 동급으로 세워 "하지 마라" 와 "이 값이 떠받치고 있다" 를 나란히 남긴다.

**핵심 표현**:
- **the firewalled fallback, not the hot path** — 느려도 되는 이유를 경로의 성격으로 설명한다. `X, not Y` 대비 하나로 성능 논쟁을 미리 닫는 방식.
- **changes materially** — "실질적으로 달라지면". 사소한 변동으로 결정을 다시 뒤집지 말라는 방어선이 부사 하나에 들어 있다.
- **deliberately defers** — 빠뜨린 게 아니라 일부러 미뤘다. 미래의 리뷰어가 "이건 왜 안 했나" 로 되돌아올 자리를 문서가 먼저 점찍어 둔다.

**격식 짝**:
- refined: *That is the rewrite this ADR deliberately defers.*
- plain: *We know that rewrite is coming — we're just not doing it now.* (작성)
- refined: *Do not raise `request_batch` without re-checking the arithmetic above; the small value is load-bearing.*
- plain: *Don't bump that number back up. It's small on purpose.* (작성)

<sub>출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md</sub>

---

## 단락 3

The parser sidecar should not be treated as another general-purpose model. It answers a narrow question — where are the interactable boxes — once another service has already narrowed the target area. Adopting it costs more than the install line suggests: extra dependency surface, a separate deployment contract, and a licence term that has to be read before it ships. None of that is fatal, and none of it belongs in the base stack either. Keep it optional, stage its weights and cache artifacts before office deployment, and run a small smoke test before wiring it into Flask. If the workload changes materially — say the primary model starts missing custom-rendered panels — revisit that call, but revisit it with a field report rather than a benchmark table.

**문법·구조**: 오늘 표현들을 한 흐름에 녹인 모범 단락이다. 첫 문장이 **부정으로 자리를 잡고**(`should not be treated as another ...`), 둘째 문장이 곧바로 긍정형 정의를 준다(`It answers a narrow question`). "아니다 → 이다" 순서는 오해가 예상될 때 쓰는 배열로, 독자의 기존 분류를 먼저 지우고 새 칸을 판다.

셋째 문장의 콜론은 단락 1의 콜론과 용법이 같다 — 추상적 주장(`costs more than the install line suggests`) 뒤에 그 내역을 나열한다. 나열은 명사구 셋으로 통일했다(`surface`, `contract`, `term`). 병렬을 지키면 항목 수를 늘려도 문장이 무너지지 않는다.

넷째 문장의 `None of that ... and none of it ...` 반복은 의도된 것이다. 같은 구조를 두 번 써서 양쪽 극단(과대평가·과소평가)을 대칭으로 쳐낸다. 다섯째 문장은 명령형 셋을 `and` 로 묶었는데(`Keep`, `stage`, `run`), 런북 문체에서 지시를 한 줄로 압축하는 방식이다.

마지막 문장의 `but revisit it with ...` 이 이 단락의 마무리 장치다. 앞에서 `revisit that call` 이라 해 놓고 같은 동사를 다시 꺼내 조건을 덧붙였다 — 동사를 반복하면 "재검토는 하되 아무렇게나 하지 마라" 가 두 문장으로 갈라지지 않고 한 호흡에 붙는다.

**핵심 표현**:
- **stage (the weights) before deployment** — 반출·설치 전에 필요한 자산을 미리 모아 두다. 오프라인 배포 런북의 전용 동사.
- **more than the install line suggests** — `pip install` 한 줄로 끝날 것처럼 보이지만 아니다. 도입 비용을 반박할 때의 정형구.
- **revisit that call** — 내렸던 판단을 다시 열다. `decision` 보다 가볍고, 되돌릴 수 있음을 전제한다.

**격식 짝**:
- refined: *Adopting it costs more than the install line suggests.* (작성)
- plain: *It's not just a pip install.* (작성)
- refined: *Revisit that call with a field report rather than a benchmark table.* (작성)
- plain: *Before you switch, find someone who's actually run it.* (작성)

<sub>출처: 모범 단락(작성) — repo:llm_serving docs/03-ocr-and-parser-services.md 의 내용을 재료로 삼음</sub>
