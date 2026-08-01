# 2026-08-02 — 오늘의 표현

1. **out-of-band** — 정규 배포 경로 밖에서 손으로 처리해야 하는 일.
   "It costs a manual, out-of-band edit on the cloud host, with no way to verify it from home."
2. **serve two masters** — 하나가 성격 다른 두 소비자를 동시에 떠맡아 둘 다 못 만족시키는 구조.
   해결되면 `both masters served` 로 닫는다. 버그를 *유형*으로 부르는 이름표.
3. **a proxy (variable) for X** — 진짜 조건 대신 상관관계만 있는 값을 조건으로 쓴 것.
   따라오는 명제가 핵심이다 — "Every proxy eventually drifts from what it proxies."
4. **the instance is fixed, the class is still open** — 그 사례는 막았지만 유형은 열려 있다.
   "고쳤냐"는 질문에 절반만 예라고 답하는 문형.
5. **by accident of prior decisions** — 지금 필요한 조건이 이미 있는데, 그게 의도가 아니라 과거 결정의 부산물일 때.
6. **carry no weight** — 관행처럼 들어와 있지만 실제로는 아무 일도 하지 않는다.
   `load-bearing` 과 짝으로 쓰면 글이 정돈된다.
7. **costs nothing and saves a week** — 비용과 이득의 비대칭을 한 줄로 보여 주는 설득 틀.

### 오늘의 정독

단락 2가 오늘의 축이다 — uWSGI 의 `harakiri` 와 `max-requests` 가 스케줄러를 건드리는지를
두 번 판정하는데, 앞은 걱정을 해소하고 뒤는 진짜 상호작용을 인정한다.
현재형과 `would` 를 어떻게 갈라 쓰는지, 세미콜론이 왜 `but` 보다 나은지를 함께 본다.
→ `reading.md`

### 오늘의 코칭

- **한글→영어**: "스냅샷이 없는 과거 주차는 키 자체를 응답에서 뺍니다" → API 규격은 능동이 아니라
  수동(`are omitted from the response`)이 자연스럽다. `exclude` 가 아니라 `omit` 인 이유도 함께.
- **영어 다듬기**: "The time between 1 and 8 am is quite time" → `quiet window`. 철자 하나가 뜻을
  뒤집고, `without worrying about the resources` 는 `without competing for resources` 로 초점이 잡힌다.
- **영어 다듬기**: "The main purpose of having scheduler is to …" → `The scheduler exists to …`.
  같은 뜻이 절반 길이가 된다.

→ `coaching.md`

> 처리 항목 8개 / 미뤄진 항목 1113개
