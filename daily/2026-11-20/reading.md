# 2026-11-20 — 정독

대화가 한국어 위주라서 영어 단락은 auto_recipe_creator 의 `CLAUDE.md` 에서 골랐습니다. 셋 다 사람과 에이전트에게 "이 시스템이 지금 어떤 상태이고 왜 그런가"를 압축해서 알려 주는 글입니다. 문장이 짧고 괄호와 대시가 많은 기술 메모체가 어떻게 정보를 쌓는지 봅니다.

## 단락 1

Development is **mixed macOS + Windows**:

- On **macOS**, Claude Code cannot see or drive the actual RCS application. Windows-only paths (RCS, pywinauto, pynput mouse/keyboard) are edited on Mac, pushed via git, pulled at the office, and run there; debugging relies on the user reporting console output and debug screenshots in `poc/workflow_3/debug_images/` (per-model subdirs).
- On **Windows** (office machine), Claude Code runs directly and can execute the automation scripts itself.

Pure-CV and synthetic-data work in `workflow_3/align` (e.g. `diagnostics/compare_align_images.py`, `matching/test_engine.py`) and the replay-source loop dry-run run and are verified on any dev machine without RCS.

**문법·구조**: 두 불릿이 `On macOS, …` / `On Windows, …` 로 같은 자리에서 시작합니다. 장소 부사구를 문두에 두면 읽는 사람이 두 환경을 바로 비교하게 됩니다. 둘째 문장은 수동태 과거분사 넷을 나란히 놓았습니다(`are edited …, pushed …, pulled …, and run there`). 누가 하는지는 중요하지 않고 코드가 거치는 경로가 중요해서 수동태를 골랐고, `are` 는 한 번만 쓰고 나머지 셋이 공유합니다. 여기서 `run` 은 과거분사입니다(run–ran–run). 세미콜론 뒤는 능동태로 바뀌어 `debugging relies on the user reporting …` 이 되는데, `the user` 가 동명사 `reporting` 의 의미상 주어입니다. 마지막 문장은 주어가 아주 깁니다. `Pure-CV and synthetic-data work … and the replay-source loop dry-run` 까지가 주어이고 동사는 `run and are verified` 입니다. `dry-run run` 처럼 명사 `dry-run` 과 동사 `run` 이 붙어 있어 한 번에 읽히지 않으니, 직접 쓸 때는 `can be run and verified` 로 풀면 편합니다.
**핵심 표현**: `cannot see or drive` 는 관찰과 조작을 한 쌍으로 묶어 한계를 말합니다. `relies on the user reporting` 은 작업이 누구 손에 달렸는지 밝히는 꼴입니다. `runs directly … itself` 의 재귀대명사는 "남의 손을 안 거치고"를 강조합니다.
**격식 짝**:
- refined (작성): Because Claude Code has no access to the RCS application on macOS, debugging depends on console output and screenshots supplied by the user.
- plain (작성): On the Mac, Claude can't see RCS at all, so I have to tell it what the console says and send screenshots.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Development Workflow")</sub>

---

## 단락 2

VLM calls route through a Flask proxy at the company server, which provides unified health discovery and per-service routing. […] **mai-ui-2b was discarded 2026-09-05** — unused; its route stub, registry entry, blueprint wiring and deploy env file are gone (workflow_3's client-side bench references remain). **ui-venus / ui-tars / got-ocr are gone as of 2026-09-03** — weights deleted from the server, so their registry entries, route stubs, deploy env files and start scripts were all removed on both server and client. A call to those slugs now fails at slug resolution (`get_service_by_slug` returns `None`), not at the proxy. Reviving one needs the checkpoint re-imported first; git history is the restore path (the route stub is a 13-line `service_template` copy).

**문법·구조**: 시제가 세 겹입니다. 구조를 말하는 첫 문장은 현재(`route through`, `provides`), 지운 사건은 과거(`was discarded`, `were all removed`), 그 결과로 지금 어떤지는 다시 현재입니다(`are gone`, `now fails`). `are gone` 은 수동태가 아니라 형용사 보어라서 "지워졌다"는 동작보다 "지금 없다"는 상태를 말하고, `as of 2026-09-03` 이 그 상태의 시작점을 찍습니다. 첫 문장의 `, which provides …` 는 쉼표가 있는 계속적 용법이어서 프록시를 한정하지 않고 설명을 덧붙입니다. 대시 뒤 `weights deleted from the server, so …` 는 `were` 가 빠진 메모체인데, `so` 로 원인과 결과를 이었습니다. `Reviving one needs the checkpoint re-imported first` 는 동명사 주어에 `need + 목적어 + 과거분사`(~가 ~되어야 한다) 구조입니다.
**핵심 표현**: `fails at slug resolution, not at the proxy` 는 실패 지점을 정확히 찍고 흔한 오해를 지웁니다. `git history is the restore path` 는 복구 방법을 명사구 하나로 이름 붙였습니다. 괄호 속 `references remain` 은 "아직 남아 있다"를 두 단어로 끝냅니다.
**격식 짝**:
- refined (작성): Requests for the removed services are now rejected during slug resolution rather than at the proxy; restoring a service requires re-importing its checkpoint.
- plain (작성): If you call one of the old models now, it dies before it even reaches the proxy. To bring one back, you'd have to re-import the weights first.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md "Flask Proxy VLM Architecture")</sub>

---

## 단락 3

Tool-row click is coarse→fine 2-VLM (coarse bbox → fine point; **both stages default to `mai-ui`** since 2026-08-07) + a **row confirm gate** (`tool_row_verify`): the two VLMs are *not* independent votes (fine only sees the crop coarse chose), so after the point is picked a **single-row strip** is cropped and OCR'd to confirm the text is the target ID. Policy via `SELECT_TOOL_ROW_CONFIRM` = `lenient` (default; reject only on reading a *different* ID) | `strict` (require confirmation) | `off`. Crop tightness needs all three of `SELECT_TOOL_ROW_VERTICAL_PAD_RATIO` (0.35) / `SELECT_TOOL_ROW_VERTICAL_PAD_MIN_PX` (10) / `SELECT_TOOL_ROW_MIN_CROP_HEIGHT` (56) — lowering only the ratio is a no-op because the two floors dominate (list rows are ~24px). A mis-click reports `failure_class="wrong_tool_opened"` (distinct from `rcs_occupied`), closes the stray tool window, and is deferred to the occupied cooldown — which never re-fires under the event-log feed (see 알람 피드 above). Model choice is benchmarked by `bench_tool_locator.py` (no alarm, no clicking).

**문법·구조**: 첫 문장이 이 단락의 논증입니다. 콜론 앞은 "무엇을 하는가", 콜론 뒤는 "왜 그렇게 하는가"이고, 뒤쪽이 `전제(not independent votes) → so → 조치(strip is cropped and OCR'd)` 순서로 흐릅니다. 괄호 속 `the crop coarse chose` 는 관계대명사를 뺀 접촉절이고(`the crop that coarse chose`), `coarse`·`fine` 이 형용사인데 단계 이름으로 명사처럼 쓰였습니다. `OCR'd` 는 약어에 `'d` 를 붙여 과거분사로 만든 꼴입니다. `after the point is picked` 는 시간 부사절이라 미래 일이어도 현재 시제를 씁니다. 넷째 문장은 주어 하나(`A mis-click`)에 동사 셋이 걸리는데 앞의 둘은 능동(`reports`, `closes`), 마지막은 수동(`is deferred`)입니다. 주어를 바꾸지 않으려고 태를 바꿨습니다. 이어지는 `— which never re-fires` 는 바로 앞 `cooldown` 을 받는 계속적 관계절이에요. `reject only on reading a different ID` 의 `on + -ing` 는 "~할 때에만"입니다.
**핵심 표현**: `are not independent votes` 는 두 번 확인해도 독립이 아니면 소용없다는 근거입니다. `is a no-op because the two floors dominate` 는 설정 하나만 건드려서는 효과가 없다는 경고입니다. `distinct from` 은 비슷해 보이는 두 분류를 갈라 놓습니다.
**격식 짝**:
- refined (작성): Because the second model evaluates only the region selected by the first, the two predictions cannot be treated as independent confirmations.
- plain (작성): The second model only looks at what the first one picked, so if the first one is wrong, the second can't catch it.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/168ab999 (프로젝트 CLAUDE.md `rcs/`)</sub>
