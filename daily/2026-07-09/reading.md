# 2026-07-09 — 정독

## 단락 1

The harness is a synchronous, main-thread call; the loop is an async daemon reusing a main-thread-constructed connection. "Works in the test, empty in the loop" is the classic signature of cross-thread connection reuse — the one variable the harness changes nothing about. The atomic-swap design (`.events_staging` → `events/` only on completion) means a half-finished daemon leaves the cache exactly empty, not partial — which looks like "nothing happened" when bytes were actually flowing. If that is the cause, the fix is to stop using an import-time singleton and build the downloader inside the daemon thread — per-call, so the connection is created on the thread that uses it. That single change kills both the thread-affinity bug and the import-timing bug at once.

**문법·구조**: 첫 문장은 세미콜론(;)으로 harness와 loop를 대칭 배치한 대조 구문 — 접속사 없이 두 절을 나란히 세워 "같은 코드, 다른 실행 조건"을 형태로 보여줍니다. 둘째 문장의 주어는 인용부호로 감싼 증상 자체("Works in the test, empty in the loop")인데, 증상을 명사처럼 주어 자리에 앉히는 이 기법은 진단 글에서 매우 영어다운 수입니다. 이어지는 `the one variable the harness changes nothing about`은 관계대명사 생략 + 전치사 잔류(about이 뒤에 남음) 구조. 셋째 문장 `leaves the cache exactly empty, not partial`은 목적어 + 보어 뒤에 `not + 형용사`로 반대항을 붙여 정밀도를 높였고, `when bytes were actually flowing`의 과거진행은 "그 순간 실제로 일어나고 있던 일"을 대비시킵니다. 마지막 문장의 `kills both A and B at once`는 단순현재로 수정안의 효과를 단정 — 제안을 현재형으로 쓰면 확신이 실립니다.

**핵심 표현**: `the classic signature of X`(전형적 징후 — 증상 조합으로 원인을 지목), `thread-affinity`(스레드 귀속 — 연결이 만든 스레드에 묶이는 성질), `at once`(한 번에, 동시에 — 하나의 수정으로 두 버그를 잡을 때).

**격식 짝**: refined — *This failure pattern is the classic signature of cross-thread connection reuse.* ↔ plain — *That's textbook "connection made on one thread, used on another."* (작성)

<sub>출처: transcript:auto_recipe_creator — align-fail 데몬 디버깅 세션의 진단 결론</sub>

---

## 단락 2

Only "S" (tool-self-reported success) frames are scored. Per project memory, S labels can be false-positives. More critically for this experiment: the ensemble proposer gains recall precisely on the frames where the baseline proposer fails — frames with drift or changed appearance. Such frames are more likely to carry an "E" label because drift causes align-fail. Restricting to S frames therefore measures the ensemble on easy cases that the baseline already handles, systematically under-counting the headroom where ensemble actually helps.

**문법·구조**: 짧은 수동태 단문(are scored)으로 사실을 깔고 → 콜론으로 핵심 논점을 예고(More critically for this experiment:) → 마지막 문장에서 동명사구 주어(Restricting to S frames)로 결론을 맺는 3단 구성. `precisely on the frames where ...`의 precisely는 "다른 곳이 아니라 바로 그곳"을 짚는 초점 부사로, 선택 편향 논증의 급소입니다. 마지막 문장의 `therefore`(문중 삽입)와 분사구문 `systematically under-counting ...`은 "측정한다 → 그 결과 축소집계한다"라는 인과를 쉼표 하나로 이어붙이는 격식 문어의 전형 — 문장을 새로 시작하지 않고 결과를 분사로 매다는 패턴을 눈에 익혀 두세요.
**핵심 표현**: `carry a label`(라벨을 달고 있다 — have보다 격식), `restricting to X ... measures Y on easy cases`(동명사 주어로 방법론 비판), `under-count the headroom`(개선 여지를 축소 집계하다).
**격식 짝**: refined — *This design systematically understates the true gain.* ↔ plain — *Set up like this, the numbers will make the gain look smaller than it really is.* (작성)

<sub>출처: transcript:auto_recipe_creator — A/B 평가 러너 유효성 감사(선택 편향 지적)</sub>

---

## 단락 3

Both issues are Minor and neither touches correctness or the extensibility contract. The primary plan requirement — a channel-agnostic `_collect_candidates` that later channels can call directly — is correctly implemented. All existing tests pass. M1 is worth a one-liner fix before the Task 2 PR — the comment is useful precisely because Task 2 will add a second call-site that may not have the surrounding context — but it is not a blocker.

**문법·구조**: 리뷰 승인(APPROVED) 뒤에 붙는 모범적 마무리 단락. 첫 문장 `neither touches ...`는 단수 동사와 호응하는 neither 용법(둘 다 ~하지 않는다)이고, touch는 "영향을 주다"의 축약적 은유. 둘째 문장은 주어와 동사 사이에 긴 동격 삽입(— a channel-agnostic ... —)을 두는 구조로, 요구사항의 정의를 문장 흐름 안에서 상기시킵니다. 마지막 문장은 `worth + 명사`(고칠 가치가 있다) → 이중 대시로 이유 삽입(precisely because ...) → `but it is not a blocker`로 급을 매기며 끝나는, "권고하되 막지 않는다" 리뷰 어법의 정석입니다.
**핵심 표현**: `neither touches X`(둘 다 X에 영향 없음 — 안심시키는 첫 문장), `worth a one-liner fix`(한 줄짜리 수정 가치는 있다), `not a blocker`(차단 사유는 아님).
**격식 짝**: refined — *M1 merits a small fix before the next PR, but it does not block approval.* ↔ plain — *M1's worth a quick one-liner, but don't hold the PR for it.* (작성)

<sub>출처: transcript:auto_recipe_creator — Chamfer 리팩터 코드리뷰의 Assessment 단락</sub>
