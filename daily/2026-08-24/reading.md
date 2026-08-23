# 2026-08-24 — 정독

## 단락 1

The events key remains an accumulating sorted set, pruned at `WRITER_PRUNE_SEC` (900s) and displayed at `BOARD_WINDOW_SEC` (600s). It is **not** replaced by a plain "cache the last response" value, for one reason: `get_live_alarms(fac_id)` takes no window argument, so how far back it reaches is the office API's choice, not ours. If it reports only *currently active* alarms, a last-response cache would drop each alarm the moment it cleared, and a 10-minute board could never be assembled. Accumulating successive snapshots into a ZSET reconstructs the board from whatever the upstream happens to report. This is safe precisely because ZSET members are canonical JSON: re-adding an event already present is a no-op. Idempotence is what allows the refresh cadence to be irregular and viewer-driven rather than a fixed schedule.

**문법·구조**: 여섯 문장이 "현재형 규칙 → 가정법 반례 → 현재형 결론" 순으로 층을 이룬다.
① 첫 문장의 `pruned at ... and displayed at ...` 는 관계절(`which is pruned`)을 줄인 과거분사 후치수식이다. 주어 `The events key` 뒤에 쉼표로 붙여 두면 본동사 `remains` 가 흐려지지 않는다.
② 둘째 문장은 수동태 `is not replaced by` 로 시작한다. 누가 안 바꿨는지가 아니라 "무엇이 무엇으로 바뀌지 않았는지"가 논점이라 행위자를 지웠다. 뒤의 `for one reason:` 은 이유가 딱 하나임을 예고하는 콜론 장치로, 근거가 여럿인 척하지 않겠다는 선언이기도 하다.
③ 셋째 문장만 가정법(`If it reports ... would drop ... could never be assembled`)이다. 아직 확인 안 된 사무실 API 동작을 다루는 자리라 사실 서술과 시제로 구분했다. 문서 뒷부분에 이 항목이 `OFFICE-VERIFY` 로 남아 있는 것과 정확히 맞물린다.
④ 다섯째 문장의 `precisely because` 는 `because` 보다 좁게 한 가지 조건만 지목한다. "안전하긴 한데 이런저런 이유로"가 아니라 "오직 이 성질 덕분에"라는 뜻.
⑤ 마지막 문장은 `Idempotence is what allows ...` 라는 what-분열문. 평범하게 쓰면 `Idempotence allows ...` 인데, `is what` 을 끼워 넣어 "허용하는 것이 바로 멱등성"이라고 초점을 옮겼다. 단락 전체가 여기로 수렴한다.

**핵심 표현**
- `for one reason:` — 반박을 예상하고 근거를 하나만 대겠다고 못 박는 전환부. 설계 문서에서 대안을 기각할 때 쓴다.
- `takes no window argument, so how far back it reaches is the office API's choice, not ours` — 인터페이스의 한계가 곧 통제권의 소재라는 논증. `not ours` 로 닫아 책임 범위를 분명히 한다.
- `is a no-op` — 실행되지만 아무 일도 일어나지 않는 동작. 중복 입력이 안전하다는 걸 한 단어로 말한다.

**격식 짝**
- refined: Idempotence is what allows the refresh cadence to be irregular rather than a fixed schedule.
- plain: Because re-adding does nothing, we can refresh whenever someone shows up instead of on a timer. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md</sub>

---

## 단락 2

The budget is `application_limits`, not per-route: one 50 req/5 s window shared across *every* `/api` route for a user. `/recipe-status` blows through it because each tab fires ~5 analytics calls per filter change (`FailIssueView.vue:365` — summary, daily-trend, align-ranking, meas-ranking, plus a separate devices fetch), and a fab multi-select refires them across the mounted tabs. Three quick clicks inside 5 s exhausted the budget, and because it's app-wide, the user pill and the page-view beacon 429'd along with the page. `fail-issue/devices` is just the request people noticed. The existing `msr_image.` exemption loop became a named constant with a comment stating the admission rule ("one page view legitimately exceeds the budget", not "this feature matters"), so the next addition has to argue for itself. `tests/test_rate_limit.py` gains a test that interleaves both blueprints for 52 requests, then probes `/api/me` — that probe is what catches an `exempt()` that covers the route but still drains the shared counter. It asserts `set(statuses) == {200}` rather than `429 not in statuses`, since a typo'd path would 404 fifty-two times and pass the weaker form.

**문법·구조**: 장애 보고의 전형적인 시제 분업이 그대로 보인다.
① 구조를 말하는 문장은 현재형(`The budget is`, `blows through`, `is just the request`), 그날 실제로 벌어진 일만 과거형(`exhausted`, `429'd`)이다. 영어 사고 보고서는 이 둘을 섞지 않는다 — 현재형은 지금도 참인 성질, 과거형은 한 번 일어난 사건.
② `429'd` 는 숫자를 동사로 만든 뒤 과거형 어미를 아포스트로피로 붙인 형태다. 구어체 기술 영어에서만 통하는 조어로, 격식 문서라면 `returned 429` 로 쓴다.
③ 셋째 문장의 `and because it's app-wide, ...` 는 등위접속사 뒤에 이유 부사절을 끼워 넣은 구조. 결과를 먼저 말하고 원인을 삽입해, 놀라운 사실(관련 없는 요청까지 같이 죽었다)이 문장 끝에 오게 배치했다.
④ 다섯째 문장의 `so the next addition has to argue for itself` 는 결과절. 코드에 주석 한 줄을 남긴 행위가 미래의 심사 기준이 된다는 걸 `so` 하나로 잇는다.
⑤ 마지막 문장의 `rather than` + `since` 조합은 테스트 단언을 고른 이유를 대는 정석이다. 무엇을 골랐는지(`asserts A`), 무엇을 안 골랐는지(`rather than B`), 왜인지(`since ...`) — 세 부분이 한 문장 안에 다 있다.
⑥ `a typo'd path would 404 fifty-two times and pass the weaker form` 에서 `would` 는 가정법. 실제로 일어난 일이 아니라 약한 단언을 썼다면 벌어졌을 일이다.

**핵심 표현**
- `blows through it` — 한도를 순식간에 소진한다. `exceed` 보다 속도와 무신경이 묻어난다.
- `is just the request people noticed` — 신고된 증상이 원인이 아니라 표본일 뿐이라는 지적. 사용자를 부정하지 않고 초점만 옮긴다.
- `that probe is what catches ...` — 단락 1의 `is what` 분열문이 여기서도 쓰였다. 테스트의 여러 줄 중 어느 줄이 실제로 결함을 잡는지를 콕 집는다.

**격식 짝**
- refined: The exemption mechanism already exists, so this is a data change, not a design change.
- plain: The switch is already there — we just need to add two names to the list. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt df011192</sub>

---

## 단락 3

"I was wrong" being empty is a claim, not a default. If it is empty, say why the objections did not land. An empty section every time means the debate is not doing its job. Disputed is a real outcome. Do not resolve a genuine disagreement by splitting the difference. Name what evidence would settle it — often a probe script, a benchmark, or a run in the environment neither side can reach from here.

**문법·구조**: 절차 문서의 명령문 문체가 압축돼 있다.
① 첫 문장의 주어는 동명사구 `"I was wrong" being empty` 다. 인용부호로 감싼 섹션 제목을 그대로 주어 자리에 넣고 `being` 으로 상태를 만들었다 — "그 칸이 비어 있다는 사실 자체"가 주어다. 뒤의 `a claim, not a default` 는 이 문서가 반복해 쓰는 A-not-B 판정형.
② 둘째·다섯째·여섯째 문장이 명령문(`say`, `Do not resolve`, `Name`)이고 첫째·셋째·넷째가 평서문이다. 규칙을 선언한 뒤 곧바로 그 규칙의 실행을 명령하는 교대 리듬으로, 읽는 사람이 "그래서 뭘 하라는 거지"를 되묻지 않게 된다.
③ `say why the objections did not land` 의 간접의문문에는 도치가 없다. `why did the objections not land` 로 쓰면 틀린다 — 명사절 안의 어순은 평서문 어순.
④ 셋째 문장 `An empty section every time means ...` 에서 `every time` 은 주어 뒤에 끼어든 빈도 부사구다. "한 번 비는 건 괜찮지만 매번 빈다면"이라는 조건을 부사구 하나로 처리했다.
⑤ 마지막 문장의 `neither side can reach from here` 는 관계사가 생략된 관계절(`(that) neither side can reach`)로 `the environment` 를 수식한다. `from here` 가 붙어 "지금 이 자리에서는"이라는 물리적 제약까지 담긴다.

**핵심 표현**
- `the objections did not land` — 지적이 유효하지 않았다. 권투 비유라 "말해졌다"와 "맞았다"를 구분한다.
- `Disputed is a real outcome.` — 합의 실패도 정당한 결론이라는 선언. 억지 봉합을 막는 한 문장.
- `Name what evidence would settle it` — 판정을 미루되 아무 데나 미루지 말라는 요구. `settle` 이 "결론을 내려 준다"를 맡는다.

**격식 짝**
- refined: An empty section every time means the debate is not doing its job.
- plain: If you never end up wrong, the review isn't really reviewing anything. (작성)

<sub>출처: transcript:[skill] .claude/skills/oc-discuss</sub>
