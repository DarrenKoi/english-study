# 2026-09-13 — 오늘의 표현

- **is bounded at** — "최대 얼마를 넘지 않는다"를 숫자로 약속하는 말. 뒤에 `regardless of …` 를 붙이면 불변식 선언이 된다. *Office API load is bounded at three calls per minute per facility.*
- **collapse into one upstream call** — 동시 요청 여럿이 상위 호출 하나로 합쳐지다. 캐시·락 설계를 한 줄로 요약하는 동사구.
- **point at the same replacement** — 서로 다른 두 문제가 같은 해법을 가리키다. 결론을 취향이 아니라 증거의 수렴으로 읽히게 한다.
- **the catalog just doesn't show it well** — "없는 게 아니라 안 보일 뿐". `just` 가 잔여 과제를 축소해, 요청을 거절하지 않고 재조준한다.
- **don't fail the rest** — 일부 실패가 나머지까지 실패시키지 않는다. 부분 실패 정책의 정형구.
- **that only holds for …** — 자기 주장의 적용 범위를 사과 없이 스스로 좁히는 말. `hold` = 명제가 참으로 유지되다.
- **not worth a diff** — 지적은 맞지만 고칠 값어치는 없다. 비용 단위를 시간이 아니라 diff 로 잡는 환유.

### 오늘의 정독
`live_alarm` 캐시 설계의 ZSET 단락 — 가정법 `would`/`could never` 로 기각 사유를 그리고, 마지막에 분열문 `Idempotence is what allows …` 으로 성질 하나를 집어 올린다. 다른 두 단락(파라미터 API 의 함정, 엔드포인트 확장 답변)과 함께 `reading.md`.

### 오늘의 코칭
- 한글→영어: "~보다는 ~이 나을까?" → `Rather than X, would it be better to Y?` / "학습 용도 포함되어 있고" → `It doubles as a learning exercise.`
- 영어 다듬기: `fill up the mock data` → `seed enough mock data` (빈칸을 메우는 건 `fill in`, 목 데이터를 만드는 건 `seed`) / `replace with echarts library` → `rebuild it on ECharts` (목적어 + 정관사, 그리고 의도에 맞는 동사).
- 전체는 `coaching.md`.

> 처리 항목 18개 / 미뤄진 항목 0개
