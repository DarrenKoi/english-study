# 2026-08-06 — 오늘의 표현

1. **Known consequence, accepted** — 부작용을 결함이 아니라 의사결정 기록으로 남기는 두 낱말 라벨.
   "Known consequence, accepted: a zero-API user appears in the page ranking but not in `dau`."
2. **silently redefine what X means** — 고장 없이 숫자의 뜻만 바뀌는, 가장 늦게 발견되는 변화.
   "Mixing them would silently redefine `this_month.requests`."
3. **the only symptom is …** — 예외도 로그도 없이 실패할 때 무엇을 봐야 알아채는지 지정하는 문장.
   "It reloads nothing — the only symptom is uptime that keeps climbing."
4. **say so instead of pretending** — 설정이 빠졌을 때 성공한 척하지 않고 사실을 보고한다.
   "Delete the line and the job says so instead of pretending."
5. **teach a relationship the data does not have** — 유도한 목 데이터가 가짜 상관을 가르친다는 경고.
   "A derived number would teach a relationship the office data does not have."
6. **read as X rather than Y** — 기능은 멀쩡한데 인상이 틀어지는 상황을 집는 자동사 read.
   "An almost-empty Top 10 reads as a broken page rather than a young one."
7. **deliberately narrow** — 삭제처럼 되돌릴 수 없는 동작의 범위를 일부러 좁혔다는 선언.
   "The sweep is deliberately narrow since it unlinks."

### 오늘의 정독

단락 1은 `pageIdentity.ts` 헤더 주석이다. 정의를 큰따옴표 질문 하나로 못박고(`answers ONE question`),
바로 다음 문장을 부정형(`It is not a feature slug.`)으로 세워 흔한 오해를 먼저 죽인다. 단락 2는
운영 결정 두 개를 각각 `X, not Y` 대조로 열고 명령형+and 조건문으로 규칙을 짧게 만든다. → `reading.md`

### 오늘의 코칭

- **한글→영어**: "너가 직접 조합해서 만들도록 하는 게 좋겠어" → `I'd rather have you assemble the result yourself.`
  사역은 make(강제)도 let(허가)도 아닌 have 가 맞다.
- **한글→영어**: "sem list 어떤 변경 점이 있지?" → `What's changed in sem_list since that copy was made?`
  "변경 점"은 명사가 아니라 현재완료로 묻는다.
- **영어 다듬기**: "I want to keep it remove if the dates are older than a week" → `keep only the last 7 days and delete anything older.`
  keep + 원형동사는 없는 형태이고, 보관 기준은 한 구로 끝난다.
- **영어 다듬기**: "the popup windows freezed and cannot close it" → `the modal locks up — the ✕ does nothing.`
  freezed 는 없는 과거형이고, 못 닫는 주체는 창이 아니라 나다.

→ `coaching.md`

> 처리 항목 11개 / 미뤄진 항목 1243개
