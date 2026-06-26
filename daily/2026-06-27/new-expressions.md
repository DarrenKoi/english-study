# 2026-06-27 — 새 표현

오늘 배치는 거의 전부 `repo:` 설계·계획 문서라, 엔지니어링 격식 영어에서
표현을 골랐습니다.

## "fall back to (X) / fallback"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-26-skewvoir-cd-outlier-detection-design.md
- 맥락: 기본 경로가 막혔을 때 *대체 경로로 떨어진다*고 설계를 설명할 때(문어·기술 격식).
- 한국어: (대안으로) 물러나다, 폴백하다 / (명사) 대체 수단.
- 설명: 원래 의도한 방법이 불가능·위험할 때 더 안전하거나 단순한 방법으로 *내려앉는* 동작.
  동사는 `fall back to`, 명사·형용사는 한 단어 `fallback`.
- 예문: When MAD is zero, the function falls back to a mean-absolute-deviation rule instead of dividing by zero.
- 유사어: default to (기본값으로 가다, 더 중립적), revert to (이전 상태로 되돌아가다), drop back to (구어적).
- 반의어: the primary path / the happy path (정상 경로).

## "mask itself (masking)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-26-skewvoir-cd-outlier-detection.md
- 맥락: 통계에서 *극단값 하나가 지표를 부풀려 자기 자신을 못 잡게 만든다*고 설명할 때.
- 한국어: (값이) 자기 존재를 가리다 / 마스킹.
- 설명: 한 극단값이 평균·표준편차를 끌어올려, 정작 그 값이 임계 안으로 숨어버리는 현상.
  robust 통계(median+MAD)를 쓰는 이유를 댈 때 단골로 나온다.
- 예문: A single extreme value can mask itself when classic mean±std inflates the threshold past it.
- 유사어: hide itself, slip under the threshold (임계 밑으로 빠져나가다).
- 반의어: stand out / get flagged (눈에 띄어 잡히다).

## "resistant to / robust to (X)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-26-skewvoir-cd-outlier-detection.md
- 맥락: 어떤 방법이 *교란 요인에 흔들리지 않는다*고 강점을 말할 때(설계 근거·격식).
- 한국어: ~에 견고한 / ~에 영향을 덜 받는.
- 설명: 노이즈·이상치·입력 변동에도 결과가 크게 망가지지 않는 성질. `robust to noise`,
  `resistant to outliers` 형태로 굳어 쓴다.
- 예문: Median and MAD are resistant to a few extreme values the way mean and std are not.
- 유사어: robust against, insensitive to (둔감한), tolerant of (허용하는).
- 반의어: fragile / sensitive to / brittle (작은 교란에도 깨지는).

## "inflate (a statistic / threshold)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-06-26-skewvoir-cd-outlier-detection-design.md
- 맥락: *소수의 큰 값이 통계량을 비정상적으로 키운다*고 부작용을 지적할 때.
- 한국어: (수치를) 부풀리다 / 과도하게 키우다.
- 설명: 한두 극단값이 분산·임계치를 실제보다 크게 만들어 판정이 무뎌지는 것. 부정적 뉘앙스.
- 예문: A couple of outliers inflate the threshold, so genuine anomalies no longer cross it.
- 유사어: blow up (구어), skew (왜곡하다), drive up (끌어올리다).
- 반의어: deflate / shrink / pull down (낮추다).

## "surgical (역할·개입)"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator side_projects/document_extraction/docs/phase1_rag_build_design.md
- 맥락: 도구·모델이 *전부 하지 않고 꼭 필요한 한 점만 정밀하게* 개입한다고 역할을 좁힐 때.
- 한국어: 외과수술처럼 정밀한 / 최소·국소 개입의.
- 설명: "VLM 역할 = surgical" 처럼, 광범위하게 휘젓지 않고 모호한 곳만 콕 집어 처리하는
  절제된 개입을 가리킨다. `a surgical change`(영향 최소 변경)로도 흔히 쓴다.
- 예문: The VLM's role is surgical: it only captions figures and reconciles ambiguous tables, nothing else.
- 유사어: targeted (표적화된), minimal-touch, precise.
- 반의어: sweeping / wholesale (전면적인), broad-brush (뭉뚱그린).

## "sanity check"
- 레지스터: conversational, technical
- 출처: repo:auto_recipe_creator side_projects/document_extraction/docs/runbook.md
- 맥락: 본격 검증 전에 *대충이라도 말이 되는지 빠르게 확인*하자고 할 때(구어·실무).
- 한국어: (정밀 검증 전) 상식선 점검 / 빠른 확인.
- 설명: 정확도를 재는 게 아니라 "크게 어긋난 데 없나"를 싸게 보는 1차 점검. 동사로도
  `sanity-check the output` 처럼 쓴다.
- 예문: If Chromium won't run, render to HTML first as a quick sanity check before debugging further.
- 유사어: smoke test (코드가 죽지 않나 보는 최소 실행), gut check (직관적 점검), quick pass.
- 반의어: full validation / rigorous evaluation (엄밀한 정식 검증).

## "round-trip (roundtrip)"
- 레지스터: technical
- 출처: repo:auto_recipe_creator side_projects/document_extraction/docs/marp_roundtrip_design.md
- 맥락: *원본 → 변환 → 다시 원본 형태로 복원*하는 왕복 변환 파이프라인을 가리킬 때.
- 한국어: 왕복(변환) / 라운드트립.
- 설명: 슬라이드→이미지→구조추출→Marp→재렌더처럼 끝에서 다시 출발점으로 돌아오는 변환.
  복원 충실도(원본과 얼마나 같나)를 평가하는 맥락에서 자주 등장한다.
- 예문: The round-trip is lossy: shapes and SmartArt can't survive the Markdown stage, so we re-insert them as cropped images.
- 유사어: round-tripping, re-render loop (재렌더 루프).
- 반의어: one-way conversion (단방향 변환).

## "self-hosted"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator side_projects/document_extraction/docs/marp_roundtrip_design.md
- 맥락: 외부 클라우드가 아니라 *자체 인프라에서 직접 띄워 돌리는* 모델·서비스라고 못 박을 때.
- 한국어: 자체 호스팅한 / 사내에서 직접 띄운.
- 설명: 데이터 반출 금지 같은 제약 때문에 vendor API 대신 우리가 운영하는 서버에 올린 모델.
  보안·컴플라이언스 문장에서 단골.
- 예문: External cloud VLMs are off-limits, so the pipeline runs only on self-hosted models inside the company network.
- 유사어: on-premises / on-prem (구내의), in-house (사내의), locally hosted.
- 반의어: cloud-hosted / managed / vendor-hosted (외부 위탁).

## "X is what ships"
- 레지스터: professional, conversational
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/plans/2026-06-26-reregister-phase3-rank1-worklist-plan.md
- 맥락: 여러 지표 중 *실제 제품에 반영되는 진짜 기준이 무엇인지* 못 박을 때(우선순위 정리).
- 한국어: 결국 출시되는(실전에 쓰이는) 건 X다.
- 설명: "in_topk is a ceiling; rank-1 is what ships" 처럼, 이론상 상한과 실제 반영값을
  대비해 *무엇을 기준으로 의사결정할지*를 한 줄로 정한다. `ship`(출시·배포)의 비유적 용법.
- 예문: Compare rank-1, not in_topk — the top guess is what ships to the engineer.
- 유사어: what actually matters, what goes to production, the bottom line (결국 중요한 것).
- 반의어: a theoretical ceiling / a nice-to-have (실전엔 안 쓰이는 상한).

## "framework-free pure util"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-26-skewvoir-cd-outlier-detection.md
- 맥락: 프레임워크 의존 없이 *입출력만 있는 순수 함수 모듈*임을 강조해 테스트 용이성을 말할 때.
- 한국어: 프레임워크에 안 묶인 순수 유틸(함수).
- 설명: Vue/React 같은 런타임 의존이 0이라 어디서든(노드, Mac) 단위 테스트 가능한 로직.
  "pure"(부수효과 없음) + "framework-free"(의존 없음)가 함께 쓰여 *옮겨 심기 쉬움*을 뜻한다.
- 예문: The detector is a framework-free pure util, so it can be unit-tested with node --test off the app entirely.
- 유사어: dependency-free, standalone helper, pure function.
- 반의어: framework-coupled / runtime-bound (런타임에 묶인).
