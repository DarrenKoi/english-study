# Professional register

격식 있는 업무/문서 영어. 보고서, ADR, 설계 결정문에서 쓰기 좋은 표현.

## 2026-06-17
- **single source of truth** — 모두가 참조하는 단 하나의 정본 기준. [→ daily](../../daily/2026-06-17/new-expressions.md)
- **the bridge between X and Y** — 분리된 두 세계를 잇는 다리.
- **document what it actually returns, not what feels canonical** — 이상이 아니라 실제 동작을 문서화하라.
- **conservative default** — 안전한 쪽을 기본값으로 두는 전략.
- **first-class** — 시스템이 정식으로 동등하게 대우하는 대상.
- **must implement these contracts identically** — 스펙을 한 치도 다르지 않게 구현하라.
- **easier to grant later than to take away** — 권한은 주는 게 뺏는 것보다 쉽다.

### auto_recipe_creator 배치
- **anchor on (the first idea)** — 처음 가설에 고착되다.
- **stress-test a plan** — 계획을 까다로운 시나리오로 두드려 약점을 찾다.
- **be opinionated** — 소신 있게 하나로 정하라.
- **measure first, fix second** — 추측으로 손대기 전에 먼저 재라.
- **As-Is / To-Be** — 현재 모습 / 목표 모습 (기획 보고서 단골).
- **load-bearing** — 빠지면 전체가 무너지는 핵심 요소.

### auto_recipe_creator 배치 (추가 발굴)
- **earning its keep** — (모듈·코드가) 제 값어치를 하다.
- **a strong read, not a menu** — 메뉴 나열 말고 소신 있는 추천 하나.
- **re-litigate (a decision)** — 끝난 결정을 다시 끄집어내 따지다.
- **would take a quarter to swap out** — 갈아치우는 데 한 분기는 걸릴 만큼 무거운.
- **the explicit no's are as valuable as the yes's** — "안 한다"는 결정도 그만큼 값지다.
- **reads like a specification** — (테스트·코드가) 명세서처럼 읽힌다.
- **backstop** — 모든 게 실패해도 받쳐주는 최후방 안전장치.
- **before an irreversible action** — 되돌릴 수 없는 작업을 하기 전에 (확인 게이트).

### auto_recipe_creator 배치 (4회차: grill-with-docs)
- **sharpen fuzzy language** — 두루뭉술한 말을 표준 용어로 또렷이 다듬다.
- **call it out** — 모순·문제를 그 자리에서 짚어 말하다 (격식: flag / point out).
- **don't batch these up — capture them as they happen** — 모아뒀다 말고 생기는 즉시 기록하라.
- **offer (something) sparingly** — 아껴서·드물게만 하라 (반대: liberally).
- **as decisions crystallise** — 결정이 또렷이 굳어가는 대로 (문어).

## 2026-06-18 — wiki_for_office 아키텍처/ADR 배치
- **If X, it has failed.** — 목표를 *반대 상황으로* 정의하는 단정형(조건절+현재완료).
  - 예: If the migration makes the on-call engineer's job harder, it has failed, no matter how elegant the internals are.
- **made structurally impossible** — 검사가 아니라 *구조 자체가* 불가능하게 만들다 (≈ safe by construction).
  - 예: Keeping content in a separate repo with no public remote makes a leak structurally impossible, not just unlikely.
- **surfaced, never silently reconciled** — 충돌을 숨겨 봉합하지 말고 *드러내다*.
  - 예: Conflicting facts are surfaced for the human to judge, never silently reconciled into one tidy answer.
- **masquerade as** — ~인 척 위장하다 / ~으로 둔갑하다 (버그가 정상처럼 보일 때).
  - 예: Reading a renamed page by path could fetch the wrong file — a bug that would masquerade as "insufficient evidence".
- **the system's own case law** — 자기 실수에서 쌓은 누적 규칙을 *판례*에 빗댄 비유.
  - 예: Each approved constraint becomes part of the system's own case law — a rule learned from a past mistake and applied automatically thereafter.
- **(the design) converged** — 반복 검토 끝에 더 다툴 게 없는 안정점에 *수렴*하다.
  - 예: After three rounds of adversarial review, the design converged where further scrutiny would need real implementation code to verify.
- **stop earning its keep** — (규칙·모듈이) 더는 제 값어치를 못 하다 → 폐기 판단의 근거.
  - 예: A constraint moves to "retired" when it stops earning its keep — when the failure it guarded against can no longer occur.
