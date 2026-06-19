# 2026-06-20 — 수집한 표현

## "blast radius"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§12)
- 맥락: 변경이 *어디까지 영향을 미치는지(파장 범위)* 를 설계 문서·PR 에서 한 섹션으로 정리할 때(격식).
- 한국어: (코드) 변경의 영향 범위 / 파장.
- 설명: 원래 폭발 반경을 뜻하는 군사 용어인데, 소프트웨어에서는 "이 변경이 건드리는 파일·모듈·시스템의 범위"를 가리킵니다. "작다(small/contained)"가 좋은 것.
- 예문: The blast radius is contained: only the hardware route changes, and pm_planning is left untouched.
- 유사어: scope of impact (더 평이·격식), surface area of the change (변경이 노출하는 면), ripple effect (파급 효과, 더 일상어)
- 반의어: contained change / localized change (영향이 한곳에 갇힌 변경)

## "in scope / out of scope"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§11)
- 맥락: 기획·설계에서 "이번에 *할 일*과 *안 할 일*"의 경계를 못 박을 때(회의·문서, 격식).
- 한국어: 범위 안 / 범위 밖.
- 설명: 무엇을 이번 라운드에 포함하고 무엇을 미루는지를 가르는 표준 표현. `in this round`, `this time` 와 자주 붙습니다.
- 예문: The skewvoir button is out of scope this round; the hardware page only needs to read the deep-link params.
- 유사어: within/beyond the remit (더 격식, 영국식), part of this round vs deferred (풀어 쓴 버전)
- 반의어: in scope ↔ out of scope (둘이 서로 반의 쌍)

## "faithful (to the source)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§2, §6)
- 맥락: mock·복제·번역이 원본을 *한 글자도 바꾸지 않고 그대로* 재현했음을 강조할 때(격식 문서).
- 한국어: 원본에 충실한 / 원형 그대로의.
- 설명: 모든 필드·오타·메타데이터까지 원본과 동일하게 보존했다는 뜻. `faithful raw docs`, `faithful reproduction` 처럼 명사 앞에. 동사로는 `stay faithful to`.
- 예문: These are faithful raw docs — every field is preserved, including the source misspellings like "Ellipicity".
- 유사어: true to the original (더 일상어), verbatim (글자 단위로 똑같이; 텍스트 한정), high-fidelity (충실도 높은; 더 기술적)
- 반의어: simplified / lossy (정보를 덜어낸·손실 있는)

## "as-of (date / snapshot)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§3, §6.4)
- 맥락: 데이터·재무·이력에서 "특정 *시점 기준*의 값"을 가리킬 때(데이터·회계·엔지니어링, 격식).
- 한국어: ~시점 기준의 / 기준일.
- 설명: `as-of date` = 그 값이 유효한 기준 시점. 하이픈으로 묶어 형용사로 자주 씁니다(`as-of snapshot`). 회계의 "as of June 1" 도 같은 뿌리.
- 예문: The mdc service returns a single as-of snapshot — the settings effective at or just before `end`.
- 유사어: point-in-time (값) (더 일반적·격식), effective as of (date) (풀어 쓴 동사구)
- 반의어: time-series / over time (시점 하나가 아니라 구간 전체)

## "deep-link-ready"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§4)
- 맥락: 외부에서 URL 파라미터로 *특정 상태를 바로 열 수 있게* 페이지를 준비해 둘 때(프론트엔드, 기술 문서).
- 한국어: 딥링크 대응이 된 / 특정 화면·상태로 바로 연결 가능한.
- 설명: deep link = 첫 화면이 아니라 *앱 안쪽의 특정 지점*으로 바로 들어가는 링크. `-ready` 를 붙이면 "그걸 받을 준비가 됐다". 동사로는 `deep-link into X`.
- 예문: The hardware page reads `eqp_id`, `start`, and `end` off the query so it is deep-link-ready.
- 유사어: bookmarkable (북마크 가능한; 사용자 관점), addressable state (상태에 URL 주소가 있는; 더 기술적)
- 반의어: lands on the default view only (파라미터를 못 받고 기본 화면만 여는)

## "coexist by design"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-19-hardware-raw-doc-mocks-design.md (§8)
- 맥락: 두 구현·표현이 나란히 있는 게 *실수가 아니라 의도된 결정*임을 방어할 때(설계 문서, 격식).
- 한국어: 의도적으로 (둘이) 공존하게 둔.
- 설명: `by design` 은 "우연이 아니라 일부러 그렇게 설계했다"를 뜻하는 강한 방어 표현. 중복·기술부채로 오해받기 쉬운 결정에 붙입니다.
- 예문: The two BSM representations coexist by design; reconciling them is deferred to a future round.
- 유사어: intentional duplication (의도된 중복), kept separate on purpose (일부러 분리해 둔)
- 반의어: accidental duplication / drifted apart (우연히 생긴 중복·따로 표류)

## "orthogonal"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/superpowers/specs/2026-06-19-om-sem-modality-split-eval-design.md (§5)
- 맥락: 두 변경·요인이 *서로 간섭하지 않고 독립적*임을 강조할 때(엔지니어링·수학, 기술).
- 한국어: 직교하는 / 서로 독립적인.
- 설명: 수학의 직교에서 온 말로, "A 를 바꿔도 B 에 영향이 없다"는 뜻. 흔히 `orthogonal to X`, `cheap and orthogonal` 처럼 "안전하게 따로 적용 가능"을 함의.
- 예문: L1 is orthogonal and unconditional — it improves classification without touching the localization path.
- 유사어: independent (더 평이), decoupled (의존이 끊긴; 설계 맥락), non-interacting (간섭 없는)
- 반의어: entangled / coupled (서로 얽혀 한쪽을 건드리면 다른 쪽도 영향받는)

## "thread (a value) through"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-19-hardware-raw-doc-mocks-plan1-backend.md (File Structure: data.py)
- 맥락: 값(파라미터)을 *여러 함수 호출 계층을 거쳐 끝까지 전달*하는 작업을 말할 때(코드 작업, 기술).
- 한국어: (값을) 호출 사슬을 통해 죽 꿰어 전달하다.
- 설명: 바늘에 실을 꿰듯 한 인자를 여러 단계에 차례로 넘기는 그림. `thread start/end through get_hardware_service` 처럼 `through + 경유 지점`.
- 예문: We thread `start` and `end` through `get_hardware_service` so the provider receives the time window.
- 유사어: pass X down (through the call chain) (더 평이), propagate X (값을 전파; 더 격식·추상)
- 반의어: read it directly at the call site (계층 전달 없이 그 자리에서 바로 읽다)

## "honour (a constraint / rule)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-19-hardware-raw-doc-mocks-plan1-backend.md (Global Constraints)
- 맥락: 규칙·제약·계약을 *지키고 따르라*고 할 때(설계 문서·정책, 격식). 미국식은 `honor`.
- 한국어: (제약·규칙을) 준수하다 / 지키다.
- 설명: "respect/obey"보다 약간 더 격식 있고 문어적. 규약·약속·SLA 에 잘 어울립니다(`honour the contract`).
- 예문: These are project-wide rules; every task must honour all of them.
- 유사어: respect (a rule) (더 일상어), abide by / adhere to (둘 다 격식, 규정 준수), comply with (규정·법규)
- 반의어: violate / break (a rule) (어기다)

## "a wrinkle worth flagging"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (15a1d642 세션, assistant)
- 맥락: 작업 중 발견한 *작지만 짚고 넘어가야 할 걸림돌*을 동료에게 부드럽게 알릴 때(구어·반격식).
- 한국어: 짚어둘 만한 (사소한) 걸림돌/변수.
- 설명: `wrinkle` = 매끈한 계획에 생긴 작은 주름(=예상 못한 복잡함). `worth -ing` = "~할 가치가 있다". 합치면 "큰일은 아니지만 알려둘 만한 점".
- 예문: I read both sides of the contract before changing anything — there's a wrinkle worth flagging.
- 유사어: a small catch (걸리는 점), a caveat (단서·주의점; 더 격식), something worth calling out (짚을 만한 것)
- 반의어: a clean/straightforward change (걸림돌 없는 깔끔한 변경)

## "just say the word"
- 레지스터: conversational, casual
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (15a1d642 세션, assistant)
- 맥락: "원하시면 *말씀만 하세요, 바로 하겠습니다*"라고 협조 의사를 가볍게 밝힐 때(구어).
- 한국어: 말씀만 하세요 / 한마디만 하시면 바로 합니다.
- 설명: 상대가 신호만 주면 즉시 실행하겠다는 정중하면서 편한 표현. `Say the word and I'll …` 형태로도.
- 예문: I won't amend the commit message unless you want it — just say the word.
- 유사어: let me know (더 무난·중립), just give me the go-ahead (실행 허락만 주세요)
- 반의어: (마땅한 대체 표현 없음)

## "exercise (a code path)"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (15a1d642 세션, assistant)
- 맥락: 특정 코드 경로를 *실제로 실행시켜 동작을 확인*했는지(혹은 못 했는지) 말할 때(테스트·디버깅, 기술).
- 한국어: (코드 경로를) 실제로 태워보다 / 실행시켜 검증하다.
- 설명: "운동시키다"의 비유로, 그 경로를 한 번 돌려 동작·예외를 끌어내 본다는 뜻. 테스트 커버리지 얘기에서 `exercise this branch`.
- 예문: This runs on the office Windows machine, so I couldn't exercise the actual capture path here.
- 유사어: run / trigger (the path) (더 평이), hit this branch (그 분기를 타다)
- 반의어: leave it untested / never executed (한 번도 안 돌려본)
