# 정독 단락 — 2026-06-17

> 오늘 배치(`repo:auto_recipe_creator`)에서 *잘 쓰인 영어 단락*을 골라 문법·맥락으로 정독.
> 이 repo 의 `docs/setup_vlms/*` 는 깔끔한 영어 기술문서라 문장 학습에 좋다.

---

## 단락 1

"The server does not only load weights. It also needs the correct tokenizer,
processor, chat template, and preprocessor configuration. … `PagedAttention`
gives better KV-cache memory management, continuous batching keeps the GPU busy
across incoming requests, and prefix caching reuses shared prompt prefixes. In
this repo's workload, prefix caching is useful **because** many requests share
long fixed prompt instructions **while** only the image and a small amount of
context change."

**문법·구조**
- `not only ... It also ...` — "단지 ~만이 아니라, ~도". 두 문장에 걸친 강조 병렬. 글에서 핵심을 *쌓아 올릴* 때.
- 등위 접속 `A, B, and C` 의 3박자: `gives ... , keeps ... , and reuses ...` — 동사 형태(현재형 3인칭)를 *나란히* 맞춘 게 포인트(parallelism). 리스트를 산문으로 풀 때 이 평행 구조가 가독성을 만든다.
- `because ... while ...` — 한 문장에 *이유*(because)와 *대조*(while)를 동시에. `while`는 "~인 반면"의 대조 용법(시간 아님). 기술 문서에서 "왜 효과적인가 + 무엇이 고정/가변인가"를 한 번에 말하는 전형.

**핵심 표현 (맥락과 함께)**
- **keep the GPU busy** — "GPU를 놀지 않게 (계속 일하게) 유지하다". `keep + 목적어 + 형용사` 패턴: `keep the build green`, `keep the user informed`.
- **across incoming requests** — "들어오는 요청들 전반에 걸쳐". `across`가 "여러 X에 두루"를 뜻하는 격식 전치사.
- **a small amount of context** — "약간의 맥락". 불가산 명사엔 `a small amount of`, 가산이면 `a small number of`.

**격식 짝 (refined ↔ plain)**
| 뜻 | refined (문서) | plain (회화) |
|---|---|---|
| 요청이 들어와도 GPU가 안 논다 | *Continuous batching keeps the GPU busy across incoming requests.* | *It keeps the GPU working even when new requests come in.* |
| 고정 부분이 많아 캐싱이 잘 듣는다 | *Prefix caching is useful because requests share fixed instructions.* | *Caching helps a lot since most of the prompt stays the same.* |

<sub>출처: `docs/setup_vlms/01-runtime-layout-and-capacity.md`</sub>

---

## 단락 2

"Always validate both `/v1/models` health and one real screenshot request through
the same code path used by `poc/work2`. The model is not truly ready until both pass."

**문법·구조**
- `validate both A and B` — `both ... and ...` 상관접속. "둘 다" 검증하라는 *완결 요구*.
- `not ... until ~` — "~하기 전까지는 …아니다" = "~해야 비로소 …이다". 영어다운 *부정+until* 강조. 직역("둘 다 통과할 때까지 준비된 게 아니다")보다 "둘 다 통과해야 비로소 준비된 것"으로 이해.

**핵심 표현**
- **through the same code path** — "같은 코드 경로를 거쳐". 테스트가 실제 동작과 *같은 길*을 타야 한다는 실무 표현.
- **not truly ready until both pass** — "둘 다 통과해야 진짜 준비 완료". 완료 기준(definition of done)을 못 박는 문장.

<sub>출처: `docs/setup_vlms/02-model-bringup-and-special-settings.md`</sub>

---

## 단락 3

Only offer to create an ADR when all three are true:
1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR.

**문법·구조**
- `Only offer ... when all three are true` — 문두 `Only` + `when` 조건절. "세 조건이 *모두* 참일 때**만**" 이라는 강한 제한. `Only` 를 앞에 빼서 "예외적으로만 하라"는 톤을 만든다.
- 세 항목이 **명사구/형용사구 병렬**: `Hard to reverse` / `Surprising without context` / `The result of a real trade-off`. 주어·동사를 생략한 *헤드라인 문체* — 체크리스트에서 자주 보는 압축 형태.
- `the cost of changing your mind later is meaningful` — 동명사구 주어(`changing your mind`)를 `the cost of ...` 가 감싼 명사구. "마음을 바꾸는 비용이 (무시 못 할 만큼) 크다"를 `meaningful` 한 단어로.
- `a future reader will wonder "why ...?"` — 미래시제 `will` 로 *가상의 독자*를 세워 판단 기준을 의인화. 직접 인용부호로 그 독자의 속마음을 그대로 옮겼다.
- `If any of the three is missing, skip the ADR` — `any ... is`(단수 일치) + 명령형 귀결. "하나라도 빠지면 → 하지 마라"는 단호한 if-then.

**핵심 표현**
- **hard to reverse** — "되돌리기 어려운". 의사결정의 *비가역성*을 한마디로. (앞서 본 `before an irreversible action` 과 짝)
- **the result of a real trade-off** — "진짜 맞바꿈의 결과". 선택지가 실제로 있었고 무언가를 *포기하고* 골랐다는 뜻. `trade-off` 가 없으면 기록할 가치도 없다는 논리.

**격식 짝**
- refined(문어): *Only document a decision when reversing it would be costly, the rationale is non-obvious, and a genuine alternative was rejected.* (작성)
- plain(회화): *Only write it down if it'd be a pain to undo, isn't obvious, and you actually gave something up to choose it.* (작성)

<sub>출처: repo:auto_recipe_creator grill-with-docs/SKILL.md ("Offer ADRs sparingly")</sub>

## 단락 4

When the user uses a term that conflicts with the existing language in CONTEXT.md, call it out immediately. When the user uses vague or overloaded terms, propose a precise canonical term. When domain relationships are being discussed, stress-test them with specific scenarios. When the user states how something works, check whether the code agrees. If you find a contradiction, surface it.

**문법·구조**
- 네 문장이 모두 `When ... , [명령형]` 의 **같은 골격**으로 반복된다. 동일 구조를 일부러 되풀이해(parallelism) "상황 → 즉각 행동" 규칙집의 리듬을 만든다. 영어 지침서의 전형적 문체.
- `terms that conflict with ...`, `how something works` — 관계절·간접의문문이 목적어 자리에 들어가 한 문장에 조건을 촘촘히 싣는다.
- `When domain relationships are being discussed` — **현재진행 수동태**(`are being discussed`). 행위자(누가 논의하는지)를 지우고 "논의가 벌어지는 동안"이라는 *상황 자체*에 초점.
- `check whether the code agrees` — `whether` 명사절. agree 의 주어를 `the code` 로 의인화해 "코드가 동의하느냐(= 코드와 들어맞느냐)"로.

**핵심 표현**
- **overloaded term** — "한 단어에 뜻이 여러 개 얹힌" 과적재 용어. 프로그래밍 `overload` 비유.
- **propose a precise canonical term** — "정확한 표준 용어를 제안하다". `canonical` = 정본의·표준의.
- **surface it** — "(모순을) 표면으로 끌어올려 드러내다". `call it out` 보다 한 단계 점잖은 동의어.

**격식 짝**
- refined(문어): *When a stated behaviour contradicts the implementation, surface the discrepancy at once.* (작성)
- plain(회화): *If what they say doesn't match the code, just call it out right away.* (작성)

<sub>출처: repo:auto_recipe_creator grill-with-docs/SKILL.md ("During the session")</sub>
