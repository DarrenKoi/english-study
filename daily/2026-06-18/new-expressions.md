# 새 표현 — 2026-06-18

오늘 배치는 대부분 `wiki_for_office` 의 아키텍처 문서·ADR 와 두 개의 설계 spec 으로, **설계 결정을 글로 정당화하는** 격식 있는 영어가 풍부했습니다. 결정의 근거·대조·결과를 잇는 연결 표현 위주로 골랐습니다. (spool 노트 없음 / transcript 무내용)

---

## "If the wiki adds work for the user, it has failed."
- 레지스터: professional
- 출처: repo:wiki_for_office (overview.md)
- 맥락: 설계 원칙·목표를 한 문장으로 못 박을 때(격식, 설계문서 도입부). "X 하면 그 설계는 실패다" 라는 단정형.
- 한국어: 위키가 사용자의 일을 늘린다면, 그건 실패한 설계다.
- 설명: 조건절(`If …`) + 현재완료(`has failed`) 로 "그 시점에 이미 실패가 확정된다"는 뉘앙스. 목표를 *반대 상황으로 정의*하는 강한 수사. 회의에선 "then we've got it wrong" 으로 풀어 말함.
- 예문: If the migration makes the on-call engineer's job harder, it has failed, no matter how elegant the internals are.

## "degrade gracefully"
- 레지스터: technical
- 출처: repo:wiki_for_office (overview.md, llm-wiki-layer.md)
- 맥락: 의존 서비스가 없거나 죽었을 때 시스템이 *멈추지 않고 품질만 낮춰* 계속 동작함을 설명할 때(설계·장애 대응).
- 한국어: (기능이) 우아하게 저하되다 — 죽지 않고 성능/정확도만 떨어진 채 계속 동작하다.
- 설명: 명사형 `graceful degradation`. 반대는 hard failure(전체 중단). 외부 의존이 optional 임을 강조하는 핵심 설계 어휘.
- 예문: When the glossary service is unreachable, retrieval degrades gracefully — it just skips acronym expansion instead of failing the whole query.

## "safe by construction"
- 레지스터: professional, technical
- 출처: repo:wiki_for_office (ADR-0005, overview.md)
- 맥락: "사후 점검이 아니라 *구조 자체가* 위험을 불가능하게 만든다"고 주장할 때(설계 정당화, 격식).
- 한국어: 구조적으로(설계 자체로) 안전한 — 검사로 막는 게 아니라 애초에 위험이 불가능하도록.
- 설명: `by construction` = 수학·설계에서 "구성 방식상 자동으로". 같은 결의 표현: **made structurally impossible**.
- 예문: Keeping content in a separate repo with no public remote makes a leak structurally impossible, not just unlikely.

## "surfaced, never silently reconciled"
- 레지스터: professional, technical
- 출처: repo:wiki_for_office (ADR-0005, llm-wiki-layer.md)
- 맥락: 충돌·모순을 *숨겨 합치지 말고 드러내라*는 정책을 쓸 때(설계 결정문, 격식).
- 한국어: 충돌은 (조용히 합치지 말고) 표면에 드러낸다.
- 설명: `surface` 가 동사("드러내다") — 수동태 `is surfaced`. 부사 `silently`("티 안 나게") + `reconcile`("상충을 봉합하다")의 결합이 핵심. 회화: "flag it, don't paper over it".
- 예문: Conflicting facts are surfaced for the human to judge, never silently reconciled into one tidy answer.

## "masquerade as"
- 레지스터: professional
- 출처: repo:wiki_for_office (llm-wiki-layer.md)
- 맥락: 어떤 실패가 *다른 정상 상태인 척* 위장해 드러나지 않는 위험을 경고할 때(격식, 어휘 수준 높음).
- 한국어: ~인 척 위장하다 / ~으로 둔갑하다.
- 설명: `masquerade as X` = 가면을 쓰고 X 행세. 버그가 "정상"으로 보여 더 위험하다는 논리를 압축. 비슷: pose as, pass for.
- 예문: Reading a renamed page by path could fetch the wrong file — a bug that would masquerade as "insufficient evidence".

## "silently drift"
- 레지스터: technical
- 출처: repo:wiki_for_office (llm-wiki-layer.md)
- 맥락: 파생 데이터가 원본과 *몰래 어긋나는데도* 멀쩡해 보이는 위험을 설명할 때(데이터 정합성).
- 한국어: 소리 없이(티 안 나게) 어긋나다 / 표류하다.
- 설명: `drift` = 기준에서 서서히 벗어남(model drift, config drift 와 같은 계열). 부사 `silently` 가 "경고 없이"를 강조.
- 예문: A fact pinned to a regenerable extract can silently drift while still looking properly cited.

## "the system's own case law"
- 레지스터: professional
- 출처: repo:wiki_for_office (llm-wiki-layer.md)
- 맥락: 시스템이 자기 실수에서 만들어 축적한 규칙을 *판례*에 빗댈 때(설계 비유, 격식).
- 한국어: 시스템 스스로 쌓아온 판례(누적 규칙).
- 설명: `case law` = 판례법. 자기진화 제약(error book)을 법체계 메타포로 설명하는 고급 수사. 비유가 한 단어로 개념을 전달.
- 예문: Each approved constraint becomes part of the system's own case law — a rule learned from a past mistake and applied automatically thereafter.

## "earn its keep / stop earning its keep"
- 레지스터: professional, conversational
- 출처: repo:wiki_for_office (llm-wiki-layer.md)
- 맥락: 규칙·모듈이 *제 값어치를 못 하게 되면* 폐기한다고 판단할 때. (※ `earning its keep` 긍정형은 이미 수집됨 — 오늘은 **부정·과거형 활용**을 보강)
- 한국어: 제 밥값을 하다 / 더는 제 값어치를 못 하다.
- 설명: 상태 전이를 말할 때 `stop -ing` 형으로 자주 씀. "approved → retired" 같은 폐기 판단의 근거 문구.
- 예문: A constraint moves to "retired" when it stops earning its keep — when the failure it guarded against can no longer occur.

## "opt-in, default-OFF"
- 레지스터: technical
- 출처: repo:wiki_for_office (overview.md, ADR-0010)
- 맥락: 민감 기능을 *기본 꺼짐 + 사용자가 직접 켜야* 동작하게 한다는 정책을 한 단어로 묶을 때.
- 한국어: 옵트인(직접 켜야 함)·기본값 꺼짐.
- 설명: `opt-in`(반대 opt-out) + `default-OFF` 가 형용사처럼 토글 앞에 붙음. 프라이버시·안전 기본값을 표현하는 관용 조합.
- 예문: Auto-capture is an opt-in, default-OFF per-user toggle, so nothing is recorded unless the user turns it on.

## "shadow mode"
- 레지스터: technical
- 출처: repo:auto_recipe_creator (metric_scorer_design, vlm_roi_prior_design)
- 맥락: 새 모델·로직을 *결정에 반영하지 않고 점수만 기록*하며 먼저 검증하는 출시 단계.
- 한국어: 섀도 모드 — 실제 결정엔 영향 없이 병렬로 돌려 결과만 관찰하는 단계.
- 설명: ship 전략 어휘. "shadow first, then flip the switch" 식으로 점진 출시를 표현.
- 예문: We'll ship the scorer in shadow mode first — it logs a score on every match but doesn't change the ranking — then enable it once the A/B holds up.

## "kill switch"
- 레지스터: technical
- 출처: repo:auto_recipe_creator (metric_scorer_design §6.2)
- 맥락: 새 기능을 *즉시 끌 수 있는* 비상 차단 플래그를 둘 때(운영 안전장치).
- 한국어: 킬 스위치 — 문제가 생기면 즉시 비활성화하는 플래그.
- 설명: 보통 env 플래그 + 로드 실패 시 자동 폴백과 짝. "flag-gated with a kill switch" 형태로 자주 쓰임.
- 예문: The metric scorer is flag-gated with a kill switch: if the model fails to load, it falls back to the old reranker and logs a warning.

## "sit behind (an interface)"
- 레지스터: technical
- 출처: repo:wiki_for_office (overview.md, ADR-0004)
- 맥락: 외부·회사 서비스를 *우리가 소유한 인터페이스 뒤에 숨겨* 교체·테스트 가능하게 했다고 설명할 때.
- 한국어: (구현이) ~인터페이스 뒤에 자리하다 / 가려져 있다.
- 설명: 추상화 경계를 묘사하는 phrasal. real/fake 두 구현이 같은 인터페이스 뒤에 있어 home-testable 하다는 논리로 이어짐.
- 예문: Company services sit behind wiki-owned interfaces, each with a real and a fake implementation, so the core stays testable off the company network.

## "(the design) converged"
- 레지스터: professional
- 출처: repo:wiki_for_office (overview.md)
- 맥락: 여러 차례 검토 끝에 설계가 *더 손댈 게 없는 지점에 수렴*했다고 마무리할 때(회고, 격식).
- 한국어: (설계가) 수렴했다 — 더 다툴 거리가 남지 않은 안정점에 이르다.
- 설명: `converge` 는 반복(iteration) 끝의 안정화를 뜻하는 격식어. 보통 "after N rounds of review, the design converged" 꼴.
- 예문: After three rounds of adversarial review, the design converged where further scrutiny would need real implementation code to verify.

## "at a glance"
- 레지스터: conversational, professional
- 출처: repo:wiki_for_office (overview.md — "Architecture at a glance")
- 맥락: 요약·개요 섹션 제목이나 "한눈에 보면" 이라고 운을 뗄 때(문서·구어 공용).
- 한국어: 한눈에 / 척 보면.
- 설명: 부사구. 제목으로 쓰면 "한눈에 보는 ~", 문장에선 "you can tell at a glance that …".
- 예문: The dashboard shows, at a glance, which services are degraded and which are healthy.
