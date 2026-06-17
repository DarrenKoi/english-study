# 정독 단락 — 2026-06-17

> 오늘 배치(`repo:auto_recipe_creator`)에서 *잘 쓰인 영어 단락*을 골라 문법·맥락으로 정독.
> 이 repo 의 `docs/setup_vlms/*` 는 깔끔한 영어 기술문서라 문장 학습에 좋다.

---

## 단락 1 — 출처: `docs/setup_vlms/01-runtime-layout-and-capacity.md`

> "The server does not only load weights. It also needs the correct tokenizer,
> processor, chat template, and preprocessor configuration. … `PagedAttention`
> gives better KV-cache memory management, continuous batching keeps the GPU busy
> across incoming requests, and prefix caching reuses shared prompt prefixes. In
> this repo's workload, prefix caching is useful **because** many requests share
> long fixed prompt instructions **while** only the image and a small amount of
> context change."

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

---

## 단락 2 — 출처: `docs/setup_vlms/02-model-bringup-and-special-settings.md`

> "Always validate both `/v1/models` health and one real screenshot request through
> the same code path used by `poc/work2`. The model is not truly ready until both pass."

**문법·구조**
- `validate both A and B` — `both ... and ...` 상관접속. "둘 다" 검증하라는 *완결 요구*.
- `not ... until ~` — "~하기 전까지는 …아니다" = "~해야 비로소 …이다". 영어다운 *부정+until* 강조. 직역("둘 다 통과할 때까지 준비된 게 아니다")보다 "둘 다 통과해야 비로소 준비된 것"으로 이해.

**핵심 표현**
- **through the same code path** — "같은 코드 경로를 거쳐". 테스트가 실제 동작과 *같은 길*을 타야 한다는 실무 표현.
- **not truly ready until both pass** — "둘 다 통과해야 진짜 준비 완료". 완료 기준(definition of done)을 못 박는 문장.
