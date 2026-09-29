# 2026-09-30 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 사무실 LLM 에게 보내는 필드 점검 브리프의 머리말. 누가 읽는지, 왜 집에서는 못 하는지, 무엇을 하면 되는지를 순서대로 깐다. 단락 2는 같은 문서의 목록 항목 다섯 개를 이어 붙인 것으로, 시간대 하나가 어긋나면 데이터가 어떻게 "조용히" 사라지는지 인과를 따라간다. 단락 3은 인계 문서를 쓴 뒤 어시스턴트가 남긴 해설 두 항목에서 굵은 소제목 표시만 뗐다.

## 단락 1

This brief is written for an LLM running **at the office**, next to the real databases. Home cannot reach them, so everything below is what the code *assumes*. Your job is to compare these assumptions against the real Redis / OpenSearch / MinIO data and report every mismatch. That tells us why data is missing on the Hardware page. The schema background for each source lives in the `hardware_*.txt` files in this folder. Where this brief and those files disagree, report it.

**문법·구조**: 첫 문장은 수동태 `is written for` 로 쓴 사람보다 "누구를 위한 글인가"를 앞세웠다. `running at the office` 는 `an LLM` 을 뒤에서 꾸미는 현재분사구(= that is running). 둘째 문장은 `A, so B` 로 제약(집에서는 못 닿는다)과 그 결과(아래 내용은 전부 가정이다)를 잇는다. 기울임꼴 *assumes* 가 "확인된 사실이 아니다"를 소리 내어 강조한다. 셋째 문장 `Your job is to compare … and report …` 는 to부정사 두 개를 `and` 로 묶은 보어로, 할 일을 한 문장에 담았다. 넷째 문장의 `That` 은 앞 문장 전체(불일치 보고)를 받고 `tells us why …` 로 목적을 밝힌다. 다섯째 문장 `lives in` 은 문서가 어디 "사는지"를 말하는 기술 문서 관용이다. 마지막 문장은 `Where`(= in cases where) 조건절 + 명령문으로 짧게 닫는다. 대상 → 제약 → 임무 → 목적 → 참고 자료 → 예외 처리 순서라서 브리프 머리말의 교본으로 쓸 만하다.

**핵심 표현**: `everything below is what the code assumes` — 아래 내용 전체의 지위를 "가정"으로 한 번에 규정. / `That tells us why …` — 요청한 작업이 어떤 질문에 답하는지 연결. / `lives in` — 자료가 있는 위치를 가볍게 가리키는 기술 문서 동사.

**격식 짝**: (작성)
- refined: Since the development environment has no access to these databases, the following describes the code's assumptions rather than verified facts.
- plain: We can't reach the databases from home, so this is just what the code expects.

<sub>출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md</sub>

---

## 단락 2

The frontend sends the last 30 days as UTC ISO strings. The route converts them to a **naive KST wall clock** before the adapters see them. Every OpenSearch range filter therefore assumes the stored `timestamp` is **offset-less KST** (for example `2026-06-17T09:20:00`). A stored `Z` or `+00:00` value makes the window slide 9 hours. You would see the newest ~9h of data missing, not an error.

**문법·구조**: 다섯 문장이 전부 현재시제다. 시스템이 늘 그렇게 동작한다는 일반 사실이라서. 첫 두 문장은 주어가 `The frontend` → `The route` 로 바뀌며 데이터가 흘러가는 순서를 그대로 따른다. `before the adapters see them` 의 `before` 절이 변환 시점을 못 박는다. 셋째 문장의 `therefore` 는 문두가 아니라 동사 앞 문중에 들어가 흐름을 끊지 않고 결론을 잇는다. `assumes (that) the stored timestamp is …` 는 that 을 생략한 명사절. 넷째 문장 `makes the window slide 9 hours` 는 사역동사 `make + 목적어 + 동사원형` 이고, 원인(저장 형식)이 결과(기간 이동)를 "일으킨다"는 인과가 한 동사에 들었다. 마지막 문장은 가정법 `would` 로 "그런 값이 있다면 이렇게 보일 것이다"라고 증상을 예고한다. `see + 목적어 + missing` 은 지각동사 + 목적격 보어(형용사). 끝의 `not an error` 가 이 단락의 요점이다. 틀린 데이터는 오류를 내지 않고 조용히 빠진다.

**핵심 표현**: `naive KST wall clock` — 시간대 정보가 없는(naive) 벽시계 시각. Python datetime 용어가 문장 속으로 들어왔다. / `makes the window slide 9 hours` — 조회 기간이 통째로 밀리는 모습을 동사 `slide` 로. / `You would see X missing, not an error.` — 조용한 실패의 증상을 미리 그려 주는 틀.

**격식 짝**: (작성)
- refined: If timestamps are stored with a UTC designator, the query window is shifted by nine hours, and the most recent data is silently excluded.
- plain: If the time has a `Z` on it, everything's off by nine hours and the latest data just doesn't show up.

<sub>출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_field_usage.md</sub>

---

## 단락 3

Expect the office to redo letters 02, 03, 11, 12 and 14. I compared the letters with the last commit the office pulled (`b262fde`, 9/21), not with the latest commit. Any of those five already marked done has a new hash now, so the agent will redo it on its own. This comes from last time, when I predicted from the latest commit and was wrong. The handoff doc only summarizes. Its opening says the spec, `index.md` and `engineer-guide.md` win if they disagree with it. That keeps it from becoming a second rulebook that drifts.

**문법·구조**: 명령문 `Expect X to do` 로 결론부터 던진다. `expect + 목적어 + to부정사` 는 "~가 ~하리라 예상해 두라". 둘째 문장은 과거시제로 근거를 댄다. `the last commit the office pulled` 는 목적격 관계대명사 that 이 빠진 관계절이고 `, not with the latest commit` 으로 비교 기준을 대비한다. 셋째 문장의 `Any of those five already marked done` 은 과거분사구 `marked done` 이 주어를 뒤에서 꾸민다. `has` 가 단수인 건 `Any` 가 "어느 하나든"을 뜻해서다. `so … will redo it on its own` 으로 미래 결과를 잇는다. 넷째 문장은 `last time, when …` 계속적 관계부사절로 지난 실수를 인정한다(`was wrong`). 다섯째 문장 `The handoff doc only summarizes.` 는 다섯 단어로 화제를 바꾸는 짧은 문장. 여섯째 문장 `win if they disagree with it` 은 현재시제 조건문으로 우선순위 규칙을 말한다. 마지막 `That keeps it from becoming …` 은 앞 문장의 규칙이 어떤 위험을 막는지 설명한다. 두 화제 모두 "주장 → 근거 → 이유" 순서다.

**핵심 표현**: `Expect X to …` — 앞으로 벌어질 일을 미리 알려 놀라지 않게 하는 보고 문형. / `on its own` — 사람이 시키지 않아도 스스로. / `keeps it from becoming a second rulebook that drifts` — 요약 문서가 원본과 따로 놀지 않게 막는 장치.

**격식 짝**: (작성)
- refined: The office should anticipate rework on letters 02, 03, 11, 12 and 14, as their hashes have changed since the last refresh.
- plain: Heads up — the office is going to redo 02, 03, 11, 12 and 14, because those letters changed.

<sub>출처: transcript:[assistant] equipment-data-map</sub>
