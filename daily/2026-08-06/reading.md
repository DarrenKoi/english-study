# 2026-08-06 — 정독

## 단락 1

Page identity for usage beaconing. Identity answers ONE question: "is this the same page as a moment ago?" It is not a feature slug. Slug vocabulary lives on the backend (`_logging/feature_map.py`) so the two can never drift apart. Almost every query param is state within a page (fab, ppid, filters) and must not re-fire the beacon. `tab` on recipe-status is the exception: that route is a shell over two genuinely different features.

**문법·구조**: 전부 현재 시제다. 코드가 "지금 무엇인가"를 규정하는 글이라 과거·미래가 낄 자리가 없고, 시제가 흔들리지 않는 덕에 문장이 규칙처럼 읽힌다. 둘째 문장의 콜론 뒤 큰따옴표 질문은 정의를 질문 형태로 박아 넣는 수법이다 — "정체성이란 X이다"보다 "정체성은 이 질문에 답한다"가 범위를 훨씬 좁게 못박는다. 셋째 문장 `It is not a feature slug.`는 **부정으로 정의하는** 문장이다. 흔한 오해를 먼저 죽여야 뒤가 안전해진다. 넷째 문장의 `so`는 인과 접속사인데, 앞이 원인(백엔드에만 산다)이고 뒤가 결과(어긋날 수 없다)다. `can never`가 `will not`이 아니라는 점이 중요하다 — 약속이 아니라 구조상 불가능하다는 주장이다. 다섯째 문장은 `and must not` 으로 두 술어를 이어 사실(is state)과 규칙(must not re-fire)을 한 문장에 겹쳐 놓았다. 마지막 문장의 콜론은 예외를 선언한 뒤 그 예외의 근거를 곧바로 대는 자리다.

**핵심 표현**: `drift apart`는 두 벌의 규칙이 시간이 지나며 서로 어긋나는 상태를 가리킨다. `a shell over`는 껍데기 하나에 알맹이가 둘이라는 그림. `state within a page`는 "페이지 안의 상태일 뿐 페이지 자체는 아니다"를 세 낱말로 눌러 담아, 왜 beacon 을 다시 쏘면 안 되는지를 설명 없이 납득시킨다.

**격식 짝**: (작성)
- refined: `Slug vocabulary lives on the backend, so the two cannot drift apart.`
- plain: `The backend owns the slug names, so they can't get out of sync.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md (`app/utils/pageIdentity.ts` 헤더 주석)</sub>

---

## 단락 2

**The reload path is parsed out of `wsgi.ini`, not configured twice.** This was the one place the job could fail invisibly: touching a file uWSGI isn't watching succeeds every night, logs "removed 0 / touched 1", and reloads nothing — the only symptom is uptime that keeps climbing. So `parse_touch_reload()` reads the deploy's own `touch-reload` lines. Change the path in `wsgi.ini` and the job follows with no code change; delete the line and the job says so instead of pretending.

**Log age is mtime, not the date in the filename.** A day-stamped file stops being written when its day ends, so its mtime already *is* its date — and mtime keeps working for rotated `*.log.1` files that carry no date. The sweep is deliberately narrow since it unlinks: one directory (never recursive), glob-matched names only, symlinks skipped rather than followed, per-file `OSError` logged and skipped. A retention of `0` disables the job rather than deleting the file uWSGI has open.

**문법·구조**: 두 문단 다 굵은 글씨 한 문장으로 열고, 나머지가 그 주장을 떠받친다. 둘 다 `X, not Y` 대조 구조라는 것도 눈여겨볼 것 — 결정을 말하면서 기각한 대안을 같은 문장에 넣는다. 첫 문단 둘째 문장은 콜론 뒤에 동사 세 개(`succeeds`, `logs`, `reloads nothing`)를 병렬로 세워 실패가 어떻게 성공처럼 보이는지를 연속 동작으로 그린다. 주어가 `touching a file uWSGI isn't watching`이라는 동명사구인 것도 요령이다 — 행위 자체를 주어로 세워야 "그 행위가 성공한다"는 모순이 드러난다. 대시 뒤 `the only symptom is …`가 결론이다. 넷째 문장은 **명령형 + and**(`Change the path … and the job follows`) 조건문으로, `If you change …, the job will follow`보다 짧고 규칙처럼 들린다. 세미콜론이 같은 형태의 두 조건절을 대칭으로 붙인다. 둘째 문단의 `so its mtime already *is* its date`에서 이탤릭이 강세를 be 동사에 얹는데, 한국어로는 "이미 그 자체로 날짜다" 정도의 힘이다. 마지막 문장의 `rather than -ing`는 선택하지 않은 동작을 밝히는 자리로, 여기서는 그 대안이 곧 사고(운영 중인 파일 삭제)라 안전 설계의 선언이 된다.

**핵심 표현**: `fail invisibly`(예외도 로그도 없이 실패하다), `says so instead of pretending`(성공한 척하지 않고 사실을 알리다), `deliberately narrow`(파괴적 동작이라 일부러 좁게 잡았다).

**격식 짝**: (작성)
- refined: `A retention of 0 disables the job rather than deleting the file uWSGI has open.`
- plain: `Set retention to 0 and the job just doesn't run — it won't go and delete the log uWSGI is still writing to.`

<sub>출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)</sub>
