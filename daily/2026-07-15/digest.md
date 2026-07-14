# 2026-07-15 — 오늘의 표현

1. **non-negotiable** — 타협 불가한. 설계 제약을 절대 원칙으로 격상시킬 때. `must` 보다 강하고 반박 여지를 미리 닫습니다.
   → *Determinism is non-negotiable.*
2. **that test was asserting the bug** — 그 테스트는 버그를 정답으로 굳혀두고 있었다. 버그를 고쳤더니 기존 테스트가 깨질 때, **테스트 수정을 정당화**하는 가장 깔끔한 한 줄.
3. **the compiler produces the worklist** — 할 일 목록은 컴파일러가 만들어 준다. 타입을 바꿔서 **고쳐야 할 곳을 전부 자동으로 드러내는** 사고방식.
4. **a hard floor** — 절대 하한선. 짝인 `a hard ceiling`(절대 상한), `a soft guideline`(권고)과 세트로.
5. **defence in depth** — 다중 방어. "백엔드가 이미 보장하지만 프런트에서도 또 검사한다"는 **중복 검증을 정당화**하는 말.
6. **nice to have** — 있으면 좋은 정도. `must-have` / `should-have` / `nice-to-have` 3단계 우선순위. **거절을 부드럽게 포장**하는 정치적 기능도 큽니다.
7. **no preamble** — 서두 없이 바로 본론. 지시문 끝에 대시로 붙이는 관용 패턴.
8. **will not be actioned** — 처리되지 않을 것이다. `action` 을 **동사로** 쓰는 사무 영어. 수동태로 행위자를 감춰 **거절을 정책처럼** 들리게 합니다.

### 오늘의 정독

**단락 1** (설계 문서) — *"A zero is not a missing measurement; it is a measurement of zero, and it would poison exactly the averages this whole plan exists to clean."*
콜론으로 주장→근거를 잇고, 세미콜론으로 "아니라 ~다"를 대비시키며, 무생물 주어 + 사역동사(`makes ... enumerate`)로 논증을 굴리는 법. → `reading.md`

**단락 2** (연구 노트) — `only while ~` 로 주장의 범위를 스스로 좁히는 **학술적 hedging**, 그리고 콜론 뒤에 수치를 던져 반박을 봉쇄하는 법.
**단락 3** (코드 리뷰) — **판정을 먼저, 근거를 나중에** 놓는 평가문의 어순.

### 오늘의 코칭

- **한글→영어**: "규칙을 자세히 알고 싶어" 는 `know in detail` 이 아니라 **`understand`** 한 단어로 흡수됩니다. 그리고 "붙이는 규칙"은 명사(`the rules for attaching`)가 아니라 **`when to use`**(의문사 + to부정사)로 묻는 것이 영어다운 어순입니다.
- **영어 다듬기**: `Primary risk for a docs task is INACCURACY` → **`The primary risk in a docs-only task is inaccuracy`**. `primary` 같은 **유일성 형용사가 붙으면 무조건 `the`**, 그리고 산문에서 전부 대문자는 소리 지르는 것처럼 읽힙니다.

→ `coaching.md`

### 오늘의 spool 답변

**영어 관사 완전 정리** — a / an / the / 무관사. 결정 트리, `the` 를 쓰는 5가지 이유, **철자가 아니라 소리**로 갈리는 `a`/`an`(왜 *a* universal 인데 *an* hour 인지, 왜 *an* EWMA 인데 *a* CUSUM 인지), 그리고 한국인이 실제로 틀리는 함정 7가지 — 특히 **불가산 명사에 `a` 붙이기**(~~an information~~, ~~a software~~, ~~an equipment~~)와 **커밋 제목의 관사 생략은 예외가 아니라 다른 문체**라는 점.
예문은 전부 오늘 배치의 당신 프로젝트 문서에서 뽑았습니다. → `spool/궁금한점.md`

> 처리 항목 11개 / 미뤄진 항목 0개
