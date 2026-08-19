# 2026-08-20 — 정독

## 단락 1

**1. HARD — `back_dev_home/health/MIGRATION.md` not updated (stale endpoint table).** The MIGRATION.md opens "This feature has three endpoints, and only one of them swaps" and lists `/health/services`, `/health/providers`, `/health/logging`. The diff adds a fourth endpoint, `GET /api/health/deployment`, open-auth and reading `_runtime` directly — i.e., a second runtime carve-out in this very feature — without touching the doc. AGENTS.md points readers to `<feature>/MIGRATION.md` as the per-feature authority; it now misstates the feature.

**문법·구조**: 지적 한 건이 세 문장으로 완결되는 리뷰의 표준 골격이다. ①현재형 `opens`/`lists` 로 문서의 현재 상태를 사실로 깔고 ②`The diff adds ...` 로 변경이 무엇을 했는지 대비시키고 ③세미콜론 뒤 `it now misstates` 로 결론을 낸다. 세 번째 문장의 세미콜론이 중요하다 — because 를 쓰면 인과 주장이 되지만, 세미콜론은 근거와 결론을 나란히 놓아 독자가 스스로 잇게 한다. 부정 분사구 `without touching the doc` 이 문장 끝에 온 것도 계산된 배치다. 영어는 문장 끝에 무게가 실리므로, 빠뜨린 행위가 마지막에 남는다. `open-auth and reading _runtime directly` 는 명사 뒤에 형용사구를 뒤로 뺀 후치 수식이고, 대시 안의 `i.e.,` 는 방금 말한 사실을 다른 이름으로 다시 부르는 자리다.

**핵심 표현**: `stale endpoint table` — 낡아서 사실과 어긋난 표. 제목 자리에 명사구로 두면 지적을 한눈에 분류할 수 있다. `a second carve-out in this very feature` — very 가 여기서 "바로 그" 라는 강조사로 쓰였다. `misstate` — 거짓말(lie)도 오류(error)도 아니고 "사실과 다르게 서술한다" 는 중립적 비난이라, 문서 지적에 딱 맞는 온도다.

**격식 짝**: refined — "The doc of record now misstates the feature." / plain — "The doc just doesn't say what the code does anymore."
또 하나 — refined — "The diff adds a fourth endpoint without touching the doc." / plain — "They added a fourth endpoint and never went back to the doc."

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-19-lab-cloud-hide-review.md</sub>

---

## 단락 2

**Hidden positional coupling** (`test_rcs_recovery.py`, `_ensure_step`): `build_cycle_steps("MCD916")[0]` assumes the ensure-RCS step is index 0. A step reorder silently retargets all three wiring tests to the wrong step. Asserting `step.name`/kind would make the failure loud. Duplicated config representation: `RECOVERY_WINDOW_TIMEOUT_SEC` is read at module import, outside `Workflow3Settings` where the sibling tunable lives. Consequence beyond symmetry: `cycle.py` imports this module at load time, before the monitors' `__main__` calls `seed_env()`, so the config file can never tune it. Moving it into `Workflow3Settings` fixes both.

**문법·구조**: 가정법 `would make the failure loud` 가 이 단락의 심장이다. 실제로 그렇게 하지 않았음을 전제로 대안을 그리는 형태라, 명령("assert the name")보다 부드럽고 서술("it is better to assert")보다 구체적이다. 리뷰에서 제안을 낼 때 기본으로 잡아 둘 문형이다. `Consequence beyond symmetry:` 는 명사 하나로 앞 문단의 반론을 미리 막는다 — "대칭성 때문에 트집 잡는 거 아니냐"에 대한 답을 콜론 앞에 세워 둔 셈이다. 시간 관계를 나타내는 `before ... calls seed_env()` 절이 결과절 `so ... can never tune it` 앞에 오면서, 원인→결과의 순서가 문장 순서와 그대로 맞는다. 부사 `silently` 의 위치도 눈여겨볼 만하다. 동사 앞에 붙어 "재조준한다"는 동작 자체가 소리 없이 일어남을 수식한다.

**핵심 표현**: `positional coupling` — 인덱스 같은 위치에 의존해 생긴 결합. 앞에 hidden 을 붙이면 "코드만 봐서는 안 보인다"까지 담긴다. `the sibling tunable` — 형제 격으로 나란히 있어야 할 설정값. 한쪽만 떨어져 나온 비대칭을 한 단어로 지적한다. `fixes both` — 두 지적을 한 조치로 닫는 마무리. 리뷰어가 작업량을 줄여 주는 신호라 수용률이 올라간다.

**격식 짝**: refined — "A step reorder silently retargets the wiring tests." / plain — "Move one step and those tests quietly start checking the wrong thing."
또 하나 — refined — "Asserting the step name would make the failure loud." / plain — "Check the name instead, and it'll blow up properly when it breaks."

<sub>출처: repo:auto_recipe_creator docs/opencode/2026-08-19-rcs-recovery-review.md</sub>
