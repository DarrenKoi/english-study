# 2026-11-22 — 정독

대화 본문이 한국어라서 영어 단락은 세션에 실린 지침에서 골랐습니다. 단락 1은 번호 붙은 규칙 목록, 단락 2와 3은 프로젝트 `CLAUDE.md` 의 설계 메모입니다. 셋 다 "무엇을 하라"에서 끝나지 않고 그 옆에 이유나 경계를 붙여 둡니다. 대시와 괄호, 세미콜론이 그 일을 어떻게 나눠 맡는지 봅니다.

## 단락 1

The user chose brevity over narration. You should:

1. **Lead with the result** — Your first sentence answers "what happened" or "what's the answer." No preamble ("Let me...", "Now I'll...") and no closing recap of what you already said.
2. **Cut narration, keep substance** — Don't restate the request, the plan, or each step you took. Report outcomes, decisions, and anything the user must act on.
3. **Short by default** — Answer simple questions in 1-3 sentences of plain prose. Use headers, tables, and bullet lists only when they carry real structure, never as decoration.
4. **State things plainly** — Skip hedging boilerplate. Mention a caveat only when it changes what the user should do next.
5. **Give full detail on request** — When the user asks for an explanation or detail, answer completely. Conciseness never means withholding requested information.
6. **Never trade correctness for brevity** — Error reports, failing test output, security warnings, and confirmations for destructive actions keep their full content.

Where these rules conflict with more general communication or formatting guidance elsewhere in your instructions, these rules win.

**문법·구조**: 첫 문장만 과거시제(`chose`)입니다. 선택은 이미 끝난 일이고 그 뒤 규칙은 지금부터 늘 적용되니 현재시제와 명령문으로 바뀝니다. 항목마다 굵은 명령문 제목 뒤에 대시를 긋고 풀이를 답니다. 제목은 대개 두 덩어리의 대비예요(`Cut narration, keep substance`). 접속사 없이 쉼표로만 이어서 구호처럼 들립니다. 1번의 `No preamble … and no closing recap` 은 동사가 없는 명사구 문장입니다. 규칙 목록에서는 이렇게 끊어 써도 됩니다. `what you already said` 와 `what the user should do next` 는 `what` 이 이끄는 명사절이고, `anything the user must act on` 은 전치사가 끝에 남은 관계절입니다. `only when` 이 두 번 나오는데 둘 다 "기본은 하지 않는다, 이 조건일 때만 한다"는 뜻이에요. 6번은 주어가 길게 넷 나열되고 동사 `keep` 이 뒤에 옵니다. 사람이 아니라 문서 종류를 주어로 세워서 "누가 써도 예외 없이"가 됩니다. 마지막 문장의 `Where` 는 "~하는 경우"를 여는 접속사입니다.

**핵심 표현**: `Lead with the result` 는 결과를 맨 앞에 두라는 말로, 기사 첫 문장(`lead`)에서 왔습니다. `closing recap` 은 끝에 붙이는 요약이고 `recap` 은 `recapitulation` 의 준말. `on request` 는 "요청이 있으면"으로, 관사 없이 굳은 구입니다(`available on request`).

**격식 짝** (작성):
- refined: Qualifications should be included only where they materially affect the reader's next step.
- plain: Only mention a catch if it changes what the person should do next.
- refined: In the event of a conflict, the provisions of this section shall prevail.
- plain: If these rules clash with the others, these win.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (Concise 출력 스타일 지침)</sub>

---

## 단락 2

**Local config (`workflow_3_config.py`, edit-often scratch — distinct from `config.py`):** `config.py` is the authoritative **schema/reader** (defines `Workflow3Settings` defaults + the `ALIGN_FAIL_*`/`SAFE_MODE` env names it reads); `workflow_3_config.py` is a **gitignored convenience front-end** of plain constants (copy from `workflow_3_config.example.py`) that `workflow_3_config_loader.seed_env()` bridges into env *before* `load_workflow3_settings()` runs — so you set toggles in one file instead of a long `ALIGN_FAIL_X=… uv run …` line. One-way flow: `workflow_3_config.py` constants → `seed_env()` (`os.environ`) → `config.py` reads env. **Precedence: real shell env > `workflow_3_config.py` > `config.py` defaults** (seed is setdefault; the loader prints which config values were ignored because env already set them). It can only set vars `config.py` already reads — it never adds a setting, and deleting it just falls back to `config.py` defaults (a malformed scratch file warns + falls back, doesn't crash). `seed_env()` is called in both monitors' `__main__` (`align_fail_monitor.py`, `align_fail_monitor_only_check.py`). Same pattern as workflow_2's `golden_eval_config.py`. (`ALIGN_IMAGES_DIR` is read at package import, *before* `seed_env()`, so it must come from real env or its default — not controllable here.)

**문법·구조**: 이름이 비슷한 두 파일을 가르는 단락이라서 첫 문장이 `A is X; B is Y` 를 세미콜론으로 맞세웁니다. A 에는 `authoritative`(정본), B 에는 `convenience`(편의)를 붙여 위아래를 형용사로 정해요. B 쪽 관계절이 깁니다. `constants … that seed_env() bridges into env` 에서 `that` 은 `bridges` 의 목적어이고, `before … runs` 가 시점을 못박습니다. 그 뒤 대시와 `so` 가 "그래서 얻는 이득"을 붙이는데, 여기서 주어가 `you` 로 바뀝니다. 구조를 설명하다가 읽는 사람의 손으로 내려오는 지점입니다. 수동태는 두 군데뿐이에요. `values were ignored because env already set them` 은 무시당한 값이 화제라서 수동이고, 이유절은 바로 능동으로 돌아옵니다. `is called in both monitors' __main__` 은 누가 부르느냐보다 어디서 불리느냐가 요점이라 수동입니다. `It can only set … — it never adds …` 는 할 수 있는 것과 못 하는 것을 대시로 나란히 두었고, 괄호 속 `warns + falls back, doesn't crash` 는 주어를 한 번만 쓰고 동사 셋을 이었습니다. 마지막 괄호 문장의 `so it must come from …` 은 추측이 아니라 "그럴 수밖에 없다"는 논리적 필연의 `must` 입니다.

**핵심 표현**: `edit-often scratch` 는 자주 고쳐 쓰는 임시 파일. `scratch` 는 연습장이라는 뜻에서 왔어요. `bridge A into B` 는 A 를 B 쪽으로 건네 준다는 동사 용법이고, `fall back to` 는 "없으면 ~로 물러나다"로 기본값 설명에 늘 나옵니다.

**격식 짝** (작성):
- refined: The local file serves solely as a convenience layer; it introduces no settings beyond those the reader already recognizes.
- plain: The local file is just a shortcut. It can't add anything the reader doesn't already know about.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, flask_vlm.py client config hub)</sub>

---

## 단락 3

**Production consensus cache is eqp-independent** (`ALIGN_CONSENSUS_CACHE_DIR`, distinct from the eqp-keyed `align_images` tree above): `<cache_root>/<class>/<recipe>/events/<event_id>/S*.jpeg` — **no `<eqp_id>`** (same recipe pools across tools; matches the bench `HISTORY_ROOT` keying + what `office_success_downloader` writes). `consensus_gather._events_dir_for(recipe_id, cache_root)` is the **single** path-construction point and deliberately omits `eqp_id` so it can't be re-added (re-adding splits the pool per-tool and misses the eqp-less office writer → silent permanent rcp fallback). Coupled guard: `monitor/success_gather._IN_FLIGHT` dedupe key is `recipe_id` alone (shared per-recipe staging would otherwise race across tools). The `align_images/<eqp_id>/…` tree (rcp/msr + captures/recordings) stays eqp-keyed — separate MES-contract root. Verify at office (read-only, no RCS/download): `uv run python poc/workflow_3/align/diagnostics/verify_consensus_path.py` (prints `[DIGEST]`).

**문법·구조**: 문장마다 본문에 사실을 적고 괄호에 이유를 넣었습니다. 괄호를 다 걷어내도 글이 서고, 괄호만 읽으면 "왜"가 이어져요. 둘째 문장이 뼈대입니다. `is the single … point and deliberately omits … so it can't be re-added` 에서 주어 하나에 동사 둘이 걸리고 `so (that)` 이 목적을 답니다. 괄호 안의 `re-adding splits … and misses …` 는 동명사가 주어인 현재시제 문장이에요. 실제로 일어난 일이 아니라 "그렇게 하면 늘 이렇게 된다"는 일반 사실이라서 현재시제를 썼고, 화살표 뒤에 최종 결과를 명사구로만 뒀습니다(`silent permanent rcp fallback`, 형용사 둘이 차례로 명사를 꾸밈). 셋째 문장의 괄호는 `would otherwise race` 로 가정을 씁니다. 가드가 있는 지금은 일어나지 않는 일이라 `would` 입니다. 같은 "안 하면 생기는 일"인데 앞 괄호는 현재시제, 이쪽은 가정법이라는 차이를 눈여겨볼 만합니다. 넷째 문장의 `stays eqp-keyed` 는 `stay + 형용사` 로 "그쪽은 그대로 둔다"를 말하고, 다섯째는 명령문 `Verify` 로 닫습니다.

**핵심 표현**: `eqp-keyed`, `eqp-independent`, `eqp-less` 가 한 단락에 다 나옵니다. `-keyed`(~를 키로 삼은), `-independent`(~와 무관한), `-less`(~가 없는)를 붙여 형용사를 만드는 법이에요. `pool across tools` 의 `pool` 은 동사로 "한데 모으다". `the single path-construction point` 의 `single` 은 "하나뿐인"이라서 여기만 고치면 된다는 뜻과 여기를 건드리면 전부 바뀐다는 경고를 함께 담습니다.

**격식 짝** (작성):
- refined: The equipment identifier is intentionally excluded from the path so that it cannot be reintroduced inadvertently.
- plain: We left the equipment ID out of the path on purpose, so nobody can sneak it back in.

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/e61f3271 (프로젝트 CLAUDE.md, Active Workstreams)</sub>
