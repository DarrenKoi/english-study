# 2026-09-19 — 오늘의 표현

- **a guard doing its job, not a bug** — 에러를 낸 줄이 일부러 넣은 방어 코드라 고칠 대상이 아니다. ≈ working as intended.
- **so the next incident diagnoses itself** — 지금 고치는 게 아니라 다음 장애 때 원인이 바로 보이게 메시지를 보강한다.
- **a hygiene step, not a prerequisite** — 해 두면 좋지만 지금 작업을 막진 않는다. ≈ nice to have, not a blocker.
- **a letter, not an edit** — 남이 소유한 코드는 고치지 말고 요청을 보낸다. 오늘 대화 곳곳에 나온 `A, not B` 틀의 대표 예.
- **a placeholder posed as a pick** — 기본값이 사용자 선택인 척했다. `pose as` = ~로 행세하다.
- **look fine all day and take the instance down at night** — 당장은 멀쩡하다가 재시작 때만 터지는 지연형 위험.
- **To be precise for the record** — 대화를 끝내기 전에 결론을 오해 없이 한 번 더 적어 둔다.

### 오늘의 정독
uWSGI 재시작 설명 단락 — `Short answer:` 로 결론부터 주고 `cannot … / can only …` 로 범위를 그은 뒤 `Only if the backlog overflows do clients see 502s` 의 도치로 끝맺는다. OpenSearch 샤드 실패 진단(`may be` → `would confirm` → `Less likely`)과 갱신 절차 단락은 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "가려진 게 아니라 VLM이 잘못 짚었습니다" → `so the button wasn't hidden — the VLM just pointed at the wrong spot`. 관찰을 근거로 받아 `so` 로 결론을 잇는다.
- 영어 다듬기: `if there is no possibility of restarting` → `If there's no chance the restart fails` (핵심 동사가 빠져 뜻이 뒤집혔다) / `Use the first letter 'F' as the anchor` → `it uses …` (명령문이 되어 지시가 반대로 읽힌다). 17장은 `coaching.md`.

> 처리 항목 23개 / 미뤄진 항목 472개
