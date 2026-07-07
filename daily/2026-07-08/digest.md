# 2026-07-08 — 오늘의 표현

1. **a clean lift-and-shift** — 로직 변경 없이 그대로 들어 옮긴 리팩터. "The extraction is a clean lift-and-shift with no logic changes."
2. **a hard blocker** — 우회 불가능한 결정적 차단 요인. must-fix 목록의 최상단에 한 단어 문장으로.
3. **(a code path) silently goes dead** — 에러 없이 분기가 조용히 무력화되다. "a behavior change, not a crash"와 짝.
4. **correct by design** — 우연이 아니라 설계 전제 덕분에 옳은. 리뷰에서 의심을 해소하는 결론 문형.
5. **deliberately mirror the already-validated X** — 검증된 기존 것을 의도적으로 본뜨다 → 리뷰 포인트는 '어디서 갈라지는가'로 좁혀짐.
6. **safe to leave as-is** — 그대로 둬도 안전한. must-fix 의 반대편 목록 제목으로.
7. **Keep it tight.** — 보고는 군더더기 없이 짧게(구어 명령형).

### 오늘의 정독
Python 순환 import를 "파일 맨 아래 import"로 푸는 4단계 인과 설명 — 현재 단순형으로 일반 원리를 서술하고, `which in turn` / `making it patchable` 로 연쇄와 결과를 잇는 모범 단락. → [reading.md](reading.md)

### 오늘의 코칭
- 한글→영어: "가장 적은 구현 비용으로 가장 큰 recall 상승" → *the biggest recall gain for the least implementation cost* — 교환 관계는 for 하나로. / "금지: ~ 계산" → *Never reorder ... — that conflates the proposer with the reranker.*
- 영어 다듬기: "verify by reading the actual code" → 한 단계 위는 *verify every claim against the code itself* (`verify A against B`). → [coaching.md](coaching.md)

> 처리 항목 20개 / 미뤄진 항목 0개
