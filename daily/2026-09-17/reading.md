# 2026-09-17 — 정독

> repo 문서 2건은 한국어 본문에 코드가 섞여 있어 영어 단락이 없다. 세 단락 모두 equipment-data-map 세션의 `[assistant]` 영어에서 골랐다. 원문 그대로이며 표·Insight 상자 표시·굵은 글씨만 풀어 한 단락으로 이었다.

## 단락 1

The letter sequence isn't the critical path to letter 18. Your site gates are, and they're the pile that's been sitting still. Parallelizing the office LLM speeds up the pile that was never the bottleneck. The keystore backend decision alone can stop letter 18 dead — your readiness sheet flags Linux as unsupported until a reviewed backend exists — and no number of pi tabs moves it. This is the usual shape of a pipeline with a human gate in it: the automatable stage looks like the bottleneck because it's the one you can watch, while the actual constraint is a approval or a credential sitting in someone's queue. The design already encodes this — every operate letter stops at `waiting` for a human — so the schedule is set by how fast those `confirmed` lines arrive, not by how fast the agent builds.

**문법·구조**: "탭을 여러 개 띄우면 빨라지지 않느냐"는 질문에 반박하는 단락이다. 둘째 문장 `Your site gates are,` 는 `are (the critical path)` 에서 보어를 지우고 be 동사만 남긴 대동사 구조라서 앞 문장과 대구가 선다. 같은 `pile` 을 두 번 쓰면서 시제를 갈랐다. `that's been sitting still` 은 현재완료진행으로 "예전부터 지금까지 줄곧 방치됐다"이고, `that was never the bottleneck` 은 과거형 + never 로 "처음부터 한 번도 병목이 아니었다"다. 넷째 문장의 `alone` 은 명사 뒤에서 "그것 하나만으로도"를 만들고, 대시 두 개 사이에 근거를 끼워 넣었다. 그 뒤 `no number of pi tabs moves it` 은 부정어를 주어 자리에 세워 "탭을 아무리 늘려도 꿈쩍 않는다"를 만든다. 다섯째 문장은 콜론 앞에서 일반 법칙을 선언하고 뒤에서 풀어 준다. `because it's the one you can watch` 에는 관계대명사가 빠진 접촉절이 들어 있고 `while` 이 겉보기와 실제를 맞세운다. 원문의 `a approval` 은 오타로 `an approval` 이 맞다(모음 소리 앞). 마지막 문장은 수동태 `is set by` 로 "누가 일정을 정하나"가 아니라 "무엇이 정하나"를 주어로 올렸다. 뒤에 `how fast …` 간접의문 명사절 두 개를 `not by` 로 맞붙였다.

**핵심 표현**: `isn't the critical path to X` — 눈에 보이는 작업이 실제 병목이 아니라고 짚는다. / `no number of X moves it` — 자원을 아무리 늘려도 안 풀린다는 강한 부정. / `the schedule is set by A, not by B` — 일정의 결정 요인을 바로잡는 틀.

**격식 짝**: (작성)
- refined: Additional parallel sessions would accelerate a stage that was never the constraint; the timeline is governed by pending approvals.
- plain: More tabs won't help. We're waiting on approvals, not on the agent.
- refined: No amount of additional compute will resolve this dependency.
- plain: Throwing more tabs at it won't fix that.

<sub>출처: transcript:equipment-data-map (병렬 pi 탭 제안에 대한 답변)</sub>

---

## 단락 2

The discipline that makes this work is refusing to blur them. Letter 20 says it outright: "Any new extractor goes through a separate CLI release, not this rollout," and the spec adds "한 장비의 예외를 공통 로직에 억지로 넣지 않는다." The pressure during a rollout is always to just make this one equipment work — that's exactly what the profile/extractor split is defending against. `workbench` is the piece most people would have skipped, and it's the one that makes improvement safe. It operates on a copy outside `rollouts/`, refuses a path under `rollouts/`, appends to `attempts.jsonl` without ever overwriting, and appears in no skill allowlist. So the risky, exploratory work — "can I parse this weird binary?" — happens where it cannot contaminate an approved map, and a method only becomes real by being rewritten as a tested module in a reviewed release. Exploration and production are physically separated, not separated by care.

**문법·구조**: 새 장비에서 막혔을 때의 대응을 세 갈래로 나눈 표 바로 뒤에 온 단락이다. 첫 문장은 주어가 길다(`The discipline that makes this work`). 관계절 안의 `make this work` 는 사역 make + 동사원형이고, be 동사 뒤에는 동명사 보어 `refusing to blur them` 이 왔다. 둘째 문장은 콜론 뒤에 인용문 두 개를 `and` 로 이어 근거를 댄다. 셋째 문장의 `is always to just make` 는 to부정사를 보어로 썼고, `to` 와 동사 사이에 `just` 를 끼운 분리부정사다. 구어에서 자연스럽다. 대시 뒤 `what the split is defending against` 는 what 명사절 끝에 전치사가 남은 형태다. 현재진행 `is defending` 이 "지금도 계속 막아 내는 중"을 더한다. 넷째 문장 `the piece most people would have skipped` 는 접촉절 안에 `would have p.p.` 를 넣어 "보통 사람이었다면 건너뛰었을" 가정을 담았다. 다섯째 문장은 동사 네 개(`operates`, `refuses`, `appends`, `appears`)를 한 주어에 병렬로 달았다. 여섯째 문장의 `where it cannot contaminate …` 는 장소 부사절이고, `by being rewritten` 은 by + 수동 동명사로 "다시 쓰여야만"이라는 조건을 만든다. 마지막 문장은 과거분사 `separated` 를 되풀이해 `physically` 와 `by care` 를 대비시켰다. 사람의 조심성이 아니라 물리적 구조가 격리를 맡는다는 결론이다.

**핵심 표현**: `The discipline that makes this work is refusing to X` — 원칙이 지켜지는 비결을 "무엇을 거부하느냐"로 정의한다. / `the piece most people would have skipped` — 남들이 생략했을 부분의 가치를 강조. / `physically separated, not separated by care` — 안전을 주의력이 아니라 구조로 확보했다는 설계 요약.

**격식 짝**: (작성)
- refined: Experimental work is isolated by design rather than by operator diligence.
- plain: Even if you're careless in the workbench, you can't mess up the real map.

<sub>출처: transcript:equipment-data-map (스크립트·스킬 개선 사이클 설명)</sub>

---

## 단락 3

And #3 has a constraint that shapes the whole design: nothing comes back by git. The hub pulls, never pushes; the office relays sanitized summaries by hand. So the corpus can't be real fixtures shipped home. It has to be: the office reports the shape (path pattern, naming rule, format, what failed and why, counts — never addresses, real paths or contents), and the maintainer writes a synthetic fake tree from that description into `tests/`. The corpus grows in the hub without a single real byte leaving the FAB — which is also exactly what the existing invariant already demands: test fixtures never contain real equipment addresses, paths, or credentials. Two rules make it a ratchet rather than a treadmill: a new condition becomes a fixture before it becomes code, and every release runs the entire accumulated corpus, so equipment #7's lesson is permanent.

**문법·구조**: "회귀 테스트 모음이 왜 없고, 어떻게 만들어야 하나"를 설명하는 단락이다(마지막 문장은 원문에서 사이클 도식 뒤에 온다). 첫 문장은 콜론 뒤 짧은 절 하나로 설계 전체를 묶는 제약을 선언한다. 둘째 문장 `The hub pulls, never pushes;` 는 동사 두 개를 쉼표로 맞세운 뒤 세미콜론으로 다음 독립절을 붙였다. 둘 다 "왜 git 으로 돌아오지 않나"의 근거라 마침표보다 세미콜론이 가깝다. 셋째 문장 `real fixtures shipped home` 은 과거분사구가 명사를 뒤에서 꾸민다. 넷째 문장 `It has to be:` 는 앞 문장의 `can't be` 를 받아 보어를 생략하고, 콜론 뒤에서 대안을 펼친다. 괄호 속 목록에는 명사들 사이에 간접의문 `what failed and why` 가 명사처럼 끼어 있다. 다섯째 문장 `without a single real byte leaving the FAB` 는 전치사 without 뒤에 동명사가 오고 그 앞에 의미상 주어 `a single real byte` 가 붙은 구조다. 대시 뒤 `which` 는 앞 절 전체를 받는 계속적 용법이다. 마지막 문장은 `make + 목적어 + 명사 보어` 로 시작한다. 규칙 첫째 `becomes a fixture before it becomes code` 는 일반 규칙이라 시간절도 현재형으로 썼고, `so` 로 결과를 닫았다.

**핵심 표현**: `a constraint that shapes the whole design` — 모든 세부 결정을 좌우하는 전제를 먼저 세울 때. / `without a single real byte leaving X` — 데이터 반출이 전혀 없다는 강한 보장. / `a new condition becomes a fixture before it becomes code` — "테스트가 먼저"를 사건 순서로 표현한 규칙문.

**격식 짝**: (작성)
- refined: Every newly observed condition is captured as a regression fixture before any corresponding code change is made.
- plain: Turn every new problem into a test first, then fix it.

<sub>출처: transcript:equipment-data-map (개선 사이클의 빠진 조각)</sub>

