# 2026-06-23 — 오늘의 표현

## "course-correction(s)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-14-recipe-comparison-build.md
- 맥락: 진행 중 방향을 바로잡은 결정을 회고·리뷰 문서에 묶어 정리할 때(격식·문어)
- 한국어: (진행 중의) 방향 수정, 궤도 수정
- 설명: 계획대로 가다가 중간에 잘못을 깨닫고 경로를 바꾼 것. 항해·로켓 은유라 "왜 바꿨나"를 회고할 때 잘 어울립니다. 보통 복수형 course-corrections.
- 예문: This section lists the key decisions and course-corrections we made mid-build.
- 유사어: pivot (더 큰 전략 전환·스타트업 구어), adjustment (중립적·작은 수정), mid-flight correction (은유를 살린 격식)
- 반의어: staying the course (방향을 그대로 유지)

## "swap surface"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-05-31-tool-skew-mgmt.md
- 맥락: 지금은 mock 이지만 나중에 통째로 갈아끼울 의도로 격리해 둔 코드 경계를 가리킬 때(설계 문서·기술)
- 한국어: (나중에) 갈아끼울 지점, 교체 경계
- 설명: 자체 로직은 최소화하고 "여기만 바꾸면 실제 구현으로 교체된다"는 한 파일/모듈. surface = 교체가 일어나는 접점. office 가 `data.py` 만 swap 한다는 식.
- 예문: The office team swaps `data.py` later, so we keep it as the single swap surface.
- 유사어: seam (테스트·교체가 일어나는 이음새·기술), extension point (확장 지점·격식), pluggable boundary (끼움 경계)

## "thin wrapper"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-05-31-tool-skew-mgmt.md
- 맥락: 자체 로직 없이 위임만 하는 얇은 계층을 설명할 때(기술)
- 한국어: 얇은 래퍼, 포장만 하는 계층
- 설명: 거의 아무 일도 안 하고 인자를 추출해 다른 것에 그대로 넘기는 층. "thin" 은 로직 두께가 거의 없다는 뜻.
- 예문: The page is a thin wrapper that extracts the route param and delegates to the view component.
- 유사어: passthrough (그대로 통과·기술), shim (호환용 얇은 끼움층·기술), facade (단순화한 앞면·격식)
- 반의어: fat layer / heavy abstraction (로직이 두꺼운 층)

## "baked into (a plan/decision)"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-13-device-statistics-d22-plan2-descriptive-view.md
- 맥락: 어떤 가정·결정이 설계에 이미 박혀 떼어내기 어려울 때(회의·계획 문서)
- 한국어: (설계·계획에) 이미 박혀 있는, 전제로 깔린
- 설명: 빵을 구울 때 재료가 반죽에 녹아들 듯, 결정이 구조에 통합돼 나중에 분리하기 어렵다는 은유. "이건 협의 끝난 전제"라는 뉘앙스.
- 예문: These three assumptions are baked into the plan, so confirm them before executing.
- 유사어: built into (중립·기술), hardwired (바꾸기 더 어려움 강조), embedded (격식)
- 반의어: configurable / pluggable (밖에서 바꿀 수 있는)

## "redirect here first"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-13-device-statistics-d22-plan2-descriptive-view.md
- 맥락: 다른 접근을 원하면 *작업 시작 전에* 나에게 먼저 알려 방향을 돌려 달라고 할 때(협업·구어와 격식 중간)
- 한국어: (다른 길을 원하면) 먼저 이쪽으로 방향을 돌려 달라 / 먼저 말해 달라
- 설명: 계획서에서 "이대로 진행하기 전에 이견이 있으면 먼저 보내라"는 협업 신호. redirect = 경로를 되돌리다. 명령형이지만 무례하지 않은 실무 어조.
- 예문: If you'd rather the counts live on the main table, redirect here first.
- 유사어: loop me in first (나를 먼저 끼워 달라·구어), flag it first (먼저 알려 달라), check with me first (격식)

## "drift (from)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-14-recipe-comparison-build.md
- 맥락: 원래 같아야 할 두 사본이 시간이 지나며 조금씩 어긋나는 위험을 짚을 때(코드리뷰·기술)
- 한국어: (점점) 어긋남, 표류 (명사·동사 둘 다)
- 설명: config drift, schema drift 처럼 한쪽만 바뀌어 일치가 깨지는 상태. "can drift from X" 형태로 위험을 경고.
- 예문: Review risk: the inlined block can drift from `recipeView.ts` if its field lists change.
- 유사어: diverge (갈라지다·격식), get out of sync (구어), skew (한쪽으로 치우침)
- 반의어: stay in sync / in lockstep (보조를 맞춰 유지)

## "keep ... in sync"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-14-recipe-comparison-build.md
- 맥락: 두 사본이 함께 갱신되도록 유지하라고 지시·경고할 때(기술·구어)
- 한국어: ~을 (서로) 동기 상태로 유지하다
- 설명: 한쪽을 바꾸면 다른 쪽도 같이 고쳐 일치를 유지. 코드 주석 `KEEP IN SYNC` 처럼 경고 라벨로도 자주 씀. [[drift-from]] 의 반대 동작.
- 예문: The inlined metadata carries a "KEEP IN SYNC" comment so it tracks the source file.
- 유사어: keep aligned (격식), mirror (한쪽을 그대로 비추다), reconcile (불일치를 맞추다·격식)
- 반의어: let it drift / fall out of sync (방치해 어긋나게 두다)

## "a clean surface"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-13-device-statistics-d22-plan2-descriptive-view.md
- 맥락: 새 기능을 기존 코드와 안 얽히게 독립된 자리에 둘 때(설계·격식)
- 한국어: 깔끔한 (작업·표시) 면, 군더더기 없는 자리
- 설명: 레거시를 안 건드리고 새 기능에 정돈된 독립 공간을 준다는 뜻. surface = 코드·사용자가 마주하는 면.
- 예문: A new sibling page keeps the legacy view untouched and gives the descriptive view a clean surface.
- 유사어: a clean slate (백지에서 다시 시작·구어), a fresh canvas (은유), greenfield (제약 없는 새 영역·기술)
- 반의어: a cluttered / legacy surface (얽히고 지저분한 면)

## "byte-identical"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/plans/2026-06-22-sem-whitebox-consensus-plan.md
- 맥락: 변경 전후 출력이 한 바이트도 다르지 않음을 회귀 테스트로 보증할 때(기술)
- 한국어: 바이트 단위로 동일한
- 설명: 결과가 비트·바이트까지 완전히 같다 — "사실상 같다(equivalent)"보다 강한 보증. 무변경(zero-offset) 경로를 회귀 가드로 못 박을 때.
- 예문: With a zero offset the behavior is byte-identical to the current code, pinned by a regression test.
- 유사어: bit-for-bit identical (더 강조), bit-parity (명사형·기술), pixel-perfect (이미지에 한정)
- 반의어: approximately equal / lossy (근사·손실 있는)

## "survivorship (bias)"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/specs/2026-06-22-oracle-roi-ceiling-design.md
- 맥락: 실패한 사례가 분모에서 빠져 지표가 거짓으로 좋아 보이는 함정을 경고할 때(분석·격식)
- 한국어: 생존 편향
- 설명: "살아남은 것만" 세고 탈락분을 빼면 평균·recall 이 부풀려지는 통계 함정. 여기선 후보 0개 프레임을 skip 하면 분모가 줄어 recall 이 거짓 상승. 막는 법은 그것을 miss 로 세는 고정 분모.
- 예문: To avoid survivorship, a no-candidate frame counts as a miss instead of being dropped from the denominator.
- 유사어: selection bias (상위 개념·격식), cherry-picking (유리한 것만 고름·부정적 구어)

## "generous (for the ~100 target)"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-14-recipe-comparison-build.md
- 맥락: 설정한 상한이 실제 필요보다 넉넉함을 리뷰에서 짚을 때(구어와 격식 중간)
- 한국어: (수치가) 넉넉한, 여유 있는
- 설명: 한도(cap=200)가 실제 목표(~100)보다 충분히 크다는 뜻. generous 가 사람의 "너그러움"뿐 아니라 수치의 "여유"에도 쓰인다는 점이 학습 포인트.
- 예문: The 200-recipe cap is generous for the ~100 target; revisit it only if the office reuses the handler.
- 유사어: ample (충분한·격식), a comfortable margin (여유 마진), more than enough (구어)
- 반의어: tight / conservative (빠듯하게 잡은)

## "content-addressed (storage)"
- 레지스터: technical
- 출처: repo:flask_modules minio_handler/docs/data_management.md
- 맥락: 파일 이름·위치가 아니라 내용 해시를 키로 쓰는 저장 방식을 가리킬 때(스토리지 설계·기술)
- 한국어: 내용 주소화 (저장)
- 설명: 같은 내용이면 같은 키(SHA-256) → 자동 중복 제거, 키 자체가 무결성 검증이 됩니다. 단, 이름이 무의미해 별도 metadata DB 가 필요.
- 예문: Using the SHA-256 hash as the key makes the store content-addressed, so identical uploads dedupe automatically.
- 유사어: hash-based key (평이·기술), CAS (약어), content fingerprinting (내용 지문)
- 반의어: location-addressed / path-based (경로·이름 기반)
