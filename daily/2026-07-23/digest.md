# 2026-07-23 — 오늘의 표현

- **a hypothesis, not a verdict** — 가설이지 판결이 아니다. 린터·지표가 내놓은 결과를 근거로만 쓰자고 할 때. `Treat the linter's dead-code report as a hypothesis, not a verdict.`
- **hinge on** — ~에 달려 있다. depend on 보다 결정적이라, 논의를 질문 하나로 좁힐 때 씁니다. `The choice between them hinges on one thing.`
- **at a resting point** — 끝난 건 아니지만 지금 멈춰도 깨지지 않는 상태. 남의 작업을 언제 건드려도 되는지 물을 때.
- **a commitment, not a preview** — 가벼워 보이는 동작(파일 하나 복사)이 실은 되돌릴 수 없는 결정이라는 경고.
- **encode a state that expires** — 오늘만 참인 사실을 테스트나 문서에 박아 넣는 실패 유형. 마이그레이션 중에 반복해서 나옵니다.
- **the dangerous kind of wrong** — 요란하게 틀리는 오류가 아니라, 권위 있게 읽혀서 그냥 믿게 되는 오류.
- **buy (someone) something** — 어떤 설계 결정이 대가로 벌어다 준 이득. `Cost: ... Buys: ...` 형태로 트레이드오프를 두 줄에 정리할 수 있습니다.

전체 16개는 [new-expressions.md](new-expressions.md).

### 오늘의 정독

단락 1은 "같은 사실이 세 군데에 기록돼 있다"는 문제를 푸는 글인데, `a cache, in git, of a fact that lives on another machine's filesystem` 한 문장이 설계 결함 전체를 은유 하나로 접습니다. 삽입구 `in git` 의 위치, 그리고 긴 문장 뒤에 `That is why it goes stale.` 를 단문으로 떨어뜨리는 리듬을 함께 보세요. → [reading.md](reading.md)

### 오늘의 코칭

- 한글→영어: "그러면 redis에 정보를 저장하고 넘겨주는게 api 요청 낭비를 방지하는 법이 아닐까?" → "Then wouldn't caching it in Redis and serving from there keep us from burning API calls?" — "~아닐까?"와 `Wouldn't ...?` 는 기능이 정확히 같습니다.
- 한글→영어: "사용자마다 각자 요청하는 개념을 너는 생각 중이야?" → "Are you assuming each viewer polls the API on their own?" — 상대의 숨은 전제를 물을 때는 `Are you assuming ...?`.
- 영어 다듬기: `I want to exempt this alarm` → exempt 는 "면제하다"라 정반대 뜻입니다. 빼내 쓴다는 뜻은 **`tap into`**.
- 영어 다듬기: `check step by step for the tabs` → `go through the tabs one at a time`. step by step 은 절차의 순서, one at a time 은 "한 번에 하나씩"으로 초점이 다릅니다.

→ [coaching.md](coaching.md)

> 처리 항목 17개 / 미뤄진 항목 0개 (문서 9건 + 트랜스크립트 8건. 이 중 트랜스크립트 4건은 `/clear` 뿐이라 추출 대상이 없었습니다.)
