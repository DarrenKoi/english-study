# 2026-09-07 — 정독

## 단락 1

Review of the diff (efficiency only). The diff is almost entirely deletion — the auto-tune engine (weight-shard `stat`s over every safetensors file plus a blocking `nvidia-smi` subprocess at launch), the JSON re-encode of every `/v1/chat/completions` body in the proxy, the `ps aux` fallback, and the duplicate `home` view functions are all gone. Nothing new was added to a request hot path or to launcher startup. One residual item in a changed region: `print_gpu_plan` calls `read_env_value(env_path, ...)` four times per model, and each call re-opens and re-scans the same `.env` file from the top. Cost: 4 opens × 3 models = 12 file reads to print one banner. It is a one-shot startup print, so this is microseconds, not a real cost. Cheaper alternative if touched again: parse each file once into a dict and index it, which also removes the `is_file()` stat per call.

**문법·구조**: 첫 문장에 동사가 없다. `Review of the diff (efficiency only).` 는 제목 겸 범위 선언이라 완전한 절이 필요 없다. 리뷰·감사 보고에서 흔한 압축이고, 괄호 안 `efficiency only` 가 "다른 축은 안 봤다"는 면책까지 겸한다. 둘째 문장은 주어가 길다 — 대시 뒤로 삭제된 것 넷을 나열하고 마지막에야 `are all gone` 이 온다. 영어에서 목록이 길면 이렇게 술어를 뒤로 미루는 편이 읽기 쉽다. `Nothing new was added` 는 수동태인데, 행위자가 궁금하지 않고 "추가된 것이 없다"는 상태만 중요해서다. 능동으로 바꾸면 누가 안 넣었는지를 묻게 되어 초점이 흐려진다. `One residual item in a changed region:` 역시 동사 없는 표제구이고, 콜론이 그 뒤 설명 전체를 끌어온다. 마지막 문장의 `which also removes...` 는 앞 절 전체를 받는 비제한 관계절이다 — 앞의 명사 하나가 아니라 "한 번만 파싱해 인덱싱한다"는 행위 전체가 선행사다.

**핵심 표현**: `residual` — 큰 정리가 끝난 뒤 남은 자잘한 것. `remaining` 보다 "털어낸 뒤 남은"이라는 순서가 담긴다. / `microseconds, not a real cost` — 문제를 인정한 뒤 크기로 기각한다. / `if touched again` — "지금 고치라는 게 아니라 다음에 이 파일을 열게 되면"이라는 조건. 지적을 남기되 작업 지시로 읽히지 않게 하는 안전장치다.

**격식 짝**: (작성)
- refined: The overhead is negligible, as the routine executes once during startup.
- plain: It only runs once at boot, so it's microseconds — not a real cost.

<sub>출처: transcript:llm_serving (`/simplify` efficiency 리뷰 에이전트 결과)</sub>

---

## 단락 2

The diff deletes `_prepare_upstream_body` and the `force_stream` field. In `auto_recipe_creator` this was added specifically because UI-TARS' vLLM upstream returned broken or empty assistant content on non-streaming requests, and `service_template.py` had to force `stream=true` and reassemble the response as a workaround. That is exactly "a fix for a documented past incident." However, it is safe to remove here. `force_stream=True` was only ever set on `ui_tars.py`, and UI-TARS' weights and code were already deleted from this server on 2026-09-03. None of the three live services ever set it. Residual risk, not a blocker: if a future model exhibits the same "no content unless streamed" upstream bug, the escape hatch is now gone and someone will have to rediscover this workaround from scratch. Consider a one-line comment pointing at this history so it is not relitigated blind.

**문법·구조**: 시제가 세 층으로 갈린다. 현재 `The diff deletes` 는 지금 눈앞의 변경, 과거 `was added` 는 그 코드가 들어온 시점, 과거완료 `were already deleted` 는 그보다 더 앞선 사건이다. 한국어는 "~했다"로 뭉갤 자리를 영어는 층을 나눠 인과 순서를 보여 준다. `had to force ... and reassemble` 은 조동사 하나에 동사 둘이 걸린 형태로, `had to` 를 반복하지 않는 게 자연스럽다. `was only ever set on` — `only ever` 는 "지금껏 통틀어 그것 하나뿐"이라는 완전 열거를 만든다. `only` 만 쓰면 현재만 말하는 것으로 읽힐 여지가 남는다. 부정 주어 `None of the three live services ever set it` 은 not 을 문장 앞으로 끌어와 단정을 세게 만든다. 마지막 문장의 `so it is not relitigated blind` 는 목적의 that 절 대신 수동태를 써서 "누가 다시 논쟁할지"를 굳이 지목하지 않는다.

**핵심 표현**: `Residual risk, not a blocker` — 위험을 인정하되 진행을 막지 않는다는 두 판정을 콤마 하나로 붙인다. 리뷰 결론의 표준 틀. / `from scratch` — 남은 기록 없이 맨바닥에서 다시. / `relitigate` — 이미 끝난 논쟁을 다시 벌이다. 법정 은유라 "쓸데없이 또" 라는 피로감이 함께 실린다.

**격식 짝**: (작성)
- refined: The removal is safe, though it forecloses a workaround that a future model may require.
- plain: Safe to drop — but if some model hits the same bug later, we'll have to figure it out all over again.

<sub>출처: transcript:llm_serving (git 이력 리뷰 에이전트 결과)</sub>

---

## 단락 3

The audit turned up sixteen items, and most of them were left over from models this server no longer runs. The `--port` flag is one example: it is two spellings of one action, so I dropped it, and it is six lines to restore if you want it back. One finding I did not act on — a startup banner that re-reads the same `.env` four times per model — is tolerable but real, but it runs once at launch, so this is microseconds, not a real cost. The docs still describe the removed knobs; that prose is history and can stay, since only the code claims to be current. What I did fix, I tried to cut at the right depth: the mechanism is gone, not just its callers. One reviewer objected that a deletion could bite in principle, and it could — but no live service ever set that flag, so the objection does not stand up to light scrutiny once you grep the three `.env` files. Everything else: lean already.

**문법·구조**: 오늘 표현들을 한 흐름에 녹인 모범 단락이다. 셋째 문장의 대시 삽입구는 주어와 술어 사이를 갈라 놓는데, 무엇에 대한 판정인지 먼저 이름 붙이고 판정은 뒤로 미루는 리뷰 문체다. `What I did fix, I tried to cut at the right depth` 는 목적어를 문두로 뺀 도치로, 앞 문장의 "안 고친 것"과 대비를 세운다. 강조하고 싶은 대비가 있을 때만 쓰고 남발하면 어색하다. `and it could` 는 앞의 `could bite` 를 되풀이하지 않고 조동사만 남긴 생략이다. 인정과 반박을 한 문장에 담을 때 이 형태가 가장 짧다. 세미콜론은 마침표를 찍기엔 두 절이 너무 붙어 있을 때 쓴다 — 여기서는 "문서는 낡았다"와 "그래도 둬도 된다"가 한 판단의 앞뒤라 세미콜론이 맞다.

**핵심 표현**: `turn up` — 찾아 나서서가 아니라 훑다 보니 나왔다는 뉘앙스. `find` 보다 우연성이 있다. / `bite` — 잠재 결함이 실제로 문제를 일으키다. `a guard that never bites` 처럼 부정형으로도 자주 쓴다. / `claims to be current` — 문서·코드를 의인화해 "현행이라고 주장한다"로 쓴다. 무엇을 고쳐야 하는지 가르는 기준이 된다.

**격식 짝**: (작성)
- refined: The remaining items were retained deliberately; each is documented rather than deferred.
- plain: I left the rest alone on purpose, and wrote down why instead of just skipping them.

<sub>출처: 모범 단락(작성) — 오늘의 표현으로 구성</sub>
