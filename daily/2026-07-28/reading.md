# 2026-07-28 — 정독

## 단락 1

Setting `ttl < runtime` creates a worse failure than a skip: the key expires mid-run, the next fire acquires it cleanly, and you get two genuinely concurrent executions with no warning anywhere. The owner-token CAS release correctly stops run #1 from deleting run #2's lock — but by then mutual exclusion is already gone. So the target isn't `ttl < interval`; it's `ttl ≥ worst-case runtime + margin`. TTL trades "how long the lock is guaranteed to protect a live run" against "how long a stale lock lingers after a hard kill" — and only the first is a correctness property.

**문법·구조**: 첫 문장은 콜론 뒤에 결과를 세 개의 절로 병렬 나열한다(expires / acquires / you get) — 콜론이 "구체적으로 말하면"의 역할을 해서 접속사 없이도 흐름이 잡힌다. 둘째 문장의 "by then ... is already gone"은 현재형이지만 논리적 시간 순서를 나타내는 관용 구조. 셋째 문장 "the target isn't X; it's Y"는 세미콜론으로 대조를 압축한 전형적 교정 문형. 마지막 문장은 trade A against B(A를 B와 맞바꾸다) 구문에 인용부호로 감싼 명사절 두 개를 목적어로 넣었다 — 긴 개념을 따옴표로 묶어 한 단어처럼 다루는 기술 문서 특유의 수법이다.
**핵심 표현**: *mid-run* (실행 도중에 — mid-X 조어 패턴), *linger* (없어져야 할 것이 남아 맴돌다), *a correctness property* (성능이 아니라 정합성 차원의 속성).
**격식 짝**: refined — "Only the first constitutes a correctness property." / plain — "Only the first one actually matters for correctness." (작성)

<sub>출처: transcript: flask-modules — lock TTL 튜닝 해설</sub>

---

## 단락 2

This was not a drop-in, and the reason is worth knowing because both defaults fail silently. redis-py stores the acquisition token in `threading.local()` by default. Our watchdog renews from its own thread, where that storage is empty, so every `extend()` would fail and the lock would quietly expire mid-run. That's exactly the "TTL is a bet on runtime" failure the renewal was built to eliminate — reintroduced by a default. And `extend(30)` by default *adds* 30s to whatever remains: each tick would push the expiry further out, so a killed process would strand an orphan far beyond `lock_ttl`, growing with every renewal that ran. Neither raises at the call site.

**문법·구조**: 전체가 가정법 would의 연쇄다(would fail / would quietly expire / would push / would strand) — 실제로 일어난 일이 아니라 "기본값을 그대로 썼다면 벌어졌을 일"을 서술하기 때문. "the failure the renewal was built to eliminate"는 목적격 관계절 두 겹(the failure [that] the renewal was built to eliminate)이고, 뒤의 과거분사구 "reintroduced by a default"가 대시로 붙어 반전을 만든다. 마지막 "Neither raises at the call site"는 다섯 단어로 앞 문단 전체를 닫는 요약문 — 짧은 문장을 결구로 쓰는 리듬을 눈여겨볼 것.
**핵심 표현**: *not a drop-in* (그대로 갈아 끼울 수 있는 교체가 아님), *strand an orphan* (고아 키를 오도 가도 못하게 남겨 두다 — strand는 "좌초시키다"), *at the call site* (호출 지점에서).
**격식 짝**: refined — "Neither failure mode produces an error at the call site." / plain — "Neither one ever throws — you just never find out." (작성)

<sub>출처: transcript: flask-modules — redis-py `Lock` 교체 해설</sub>

---

## 단락 3

A one-time script under `ops_index_mgmt/` provisions local and production aliases on the same company cluster. Flask resolves one logging target, classifies every request once, and asynchronously writes one idempotent canonical document through `OSDoc`; the activity and admin-log office adapters read that same alias through `OSSearch`. Mock adapters remain network-free for automated tests. (…) The application must not infer logging behavior from `is_cloud()`. Request processing must never wait for or fail because of OpenSearch logging. No request or response body, authentication header, cookie, password, token, or unredacted secret may be stored.

**문법·구조**: 앞 세 문장은 설계 요약의 정석 — 주어가 전부 시스템 구성 요소(script / Flask / adapters)이고 동사는 현재형 단언(provisions / resolves / writes / read)이다. 계획서의 현재형은 "그렇게 될 것"이 아니라 "이 설계에서는 그렇다"는 규범 서술. 뒤 세 문장은 제약 조항으로, must not / must never / may (not) be stored 조동사가 금지의 강도를 단계별로 나른다. 마지막 문장은 7개 명사를 or로 병렬한 뒤 수동태(may be stored)로 닫아 행위자를 지운다 — "누구든, 어떤 경로로든 안 된다"는 효과.
**핵심 표현**: *one-time* (일회성의), *idempotent* (몇 번 실행해도 결과가 같은), *infer X from Y* (Y에서 X를 추론하다 — 금지 대상으로 쓰인 게 포인트).
**격식 짝**: refined — "Request processing must never wait for or fail because of OpenSearch logging." / plain — "Requests should never get stuck or die just because logging is down." (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md</sub>
