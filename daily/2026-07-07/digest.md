# 2026-07-07 — 오늘의 표현

ensemble-proposer 리뷰 transcript 배치. 리뷰 평결·실험 설계 영어가 수확의 중심.

- **chasing the wrong root cause** — 낡은 진단 지표가 엔지니어를 엉뚱한 원인으로 이끈다. "whoever debugs the next incident will be chasing the wrong root cause."
- **err on the side of X** — 어차피 틀린다면 안전한 쪽으로. "it errs on the side of fewer duplicate clusters."
- **a drop-in replacement** — 호출부 수정 없이 그대로 갈아 끼우는 대체물. ↔ a breaking change.
- **ship with caution** — 조건부 승인 평결: 내보내되 이 이슈는 주시하라.
- **on equal footing** — 밀도를 맞춰야 채널 비교가 공정해진다: "so channels compare on equal footing."
- **bit-for-bit identical** — 반올림 차이조차 없는 완전 동일 — 결정론 주장의 최상급.
- **retract (a finding)** — 스스로 낸 지적을 검증 끝에 공식 철회. "No bug here. Retract C1."

### 오늘의 정독
"orb_flip 진단이 이제는 옛 시스템의 유령을 측정한다" — 사라진 코드 경로를 계속 진단하는 도구의 위험을 Now that / 분사 후치수식으로 쌓아 올린 리뷰 단락. → [reading.md](reading.md) 단락 1

### 오늘의 코칭
- 한글→영어: "spec 에 박을 구체 파라미터를 정해줘. 코드 변경 금지, 값+근거만." → "Pin down the parameters to bake into the spec. No code changes — just values, each with a one-line rationale."
- 한글→영어(번역): "평가 완화가 섞여 A/B 신호가 오염됨" → "would mix genuine improvement with a looser yardstick, contaminating the A/B signal."
- 영어 다듬기: "Sane?" 한 단어 질문 → "Does X look sane as Y?" 완전 의문문으로 판정 대상을 고정. → [coaching.md](coaching.md)

> 처리 항목 28개 (표현 13 + 정독 3 + 코칭 12) / 미뤄진 항목 1176개 (토큰 예산으로 이월된 transcript 행 — 다음 실행에서 재시도)
