# 2026-07-07 — 새 표현

ensemble-proposer 리뷰 subagent transcript 들에서 수집. 리뷰 평결·실험 설계 어휘가 중심.

## "chasing the wrong root cause"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (cross-file impact 감사 subagent)
- 맥락: 낡은 진단 도구·지표가 엔지니어를 엉뚱한 원인으로 이끌 것이라고 경고할 때(리뷰·포스트모템, 준격식)
- 한국어: 엉뚱한 근본 원인을 쫓다
- 설명: chase(추적하다) + root cause. 진짜 원인이 아닌 것을 계속 파게 된다는 뜻. 원문: "An engineer running this tool to debug a production regression will be chasing the wrong root cause."
- 예문: If the dashboard still reports the old categories, whoever debugs the next incident will be chasing the wrong root cause.
- 유사어: bark up the wrong tree (관용·구어), chase a red herring (거짓 단서를 쫓다), go down the wrong rabbit hole (구어; 깊이 파고드는 뉘앙스)
- 반의어: zero in on the real cause (진짜 원인으로 정확히 좁혀 가다)

## "err on the side of X"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (RRF fusion Task 4 리뷰 subagent)
- 맥락: 두 오차 중 덜 위험한 쪽으로 치우치게 설계·판단했음을 정당화할 때(설계 근거·리뷰, 문어·구어 모두)
- 한국어: (어차피 틀린다면) ~쪽으로 틀리게 하다, 안전한 쪽으로 치우치다
- 설명: err = 틀리다. "오차가 불가피하면 X 쪽 오차가 낫다"는 보수적 설계 근거를 한 구로 압축한다. 원문: "it errs on the side of fewer duplicate clusters." 가장 흔한 꼴은 err on the side of caution.
- 예문: The merge radius errs on the side of fewer duplicate clusters, which is the right trade-off for a proposer.
- 유사어: lean conservative (더 간결·구어), default to the safer option (중립·기술문서), play it safe (구어; 전략 전체가 소극적)
- 반의어: cut it fine (아슬아슬한 쪽으로 가다)

## "on equal footing"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 2 Scharr 채널 구현 지시)
- 맥락: 비교 대상들을 같은 조건에서 겨루게 만들었다고 말할 때(실험 설계·보고서, 격식)
- 한국어: 동등한 조건에서, 같은 출발선에서
- 설명: footing 은 "발 디딤 자리". 원문: "its edge density is matched to C1 (Canny) so channels compare on equal footing" — 밀도를 맞춰야 채널 간 비교가 공정해진다는 문맥.
- 예문: We normalize edge density first so the three channels compare on equal footing.
- 유사어: on a level playing field (더 비유적·관용), apples-to-apples (비교의 공정함, 구어), under identical conditions (가장 중립·기술)
- 반의어: stack the deck (한쪽에 유리하게 판을 짜다)

## "a drop-in replacement"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator (통합 최종 리뷰 subagent)
- 맥락: 호출부를 한 줄도 안 고치고 그대로 갈아 끼울 수 있는 대체물을 말할 때(API 설계·마이그레이션)
- 한국어: 그대로 꽂아 넣는 대체물
- 설명: drop in = 툭 넣다. 시그니처·반환 형태가 같아 교체 비용이 0에 가깝다는 뜻. 원문: "Drop-in replacement is safe." / "confirm drop-in compatibility".
- 예문: The new entrypoint populates every field the callers read, so it works as a drop-in replacement for the old function.
- 유사어: API-compatible (형용사·명세 톤), swap in without touching callers (풀어쓴 표현)
- 반의어: a breaking change (호출부 수정을 강제하는 변경)

## "spot-check" (동사)
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator (통합 최종 리뷰 지시)
- 맥락: 전수 검사 대신 표본 몇 개만 골라 빠르게 확인하라고 할 때(리뷰 지시·QA)
- 한국어: 표본만 뽑아 점검하다
- 설명: spot(지점) + check. 원문: "Spot-check one such caller's usage to confirm drop-in compatibility." 전체를 다 보지 않아도 될 때의 실용적 검증 동사.
- 예문: I spot-checked three of the migrated files and the formatting held up.
- 유사어: sanity-check (말이 되는지 가볍게 확인), sample (통계 뉘앙스), eyeball (더 캐주얼; 눈대중으로)
- 반의어: audit exhaustively (전수 감사하다)

## "ship with caution"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (통합 최종 리뷰 subagent)
- 맥락: 배포는 허용하되 특정 이슈를 주시하라는 조건부 승인 평결(리뷰 보고서, 격식)
- 한국어: 조심해서 내보내라 (조건부 승인)
- 설명: 리뷰 평결 어휘. approve 와 block 사이의 제3의 판정. 원문: "**Ship with caution** on Issue 1."
- 예문: Assessment: ship with caution — the fix is sound, but watch the distinctiveness gate on real data.
- 유사어: approve with notes (지적사항 첨부 승인), a conditional go (출시 판정 톤)
- 반의어: block the release (출시를 막다)

## "not a blocker"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator (holistic 리뷰 subagent)
- 맥락: 결함을 인정하되 진행을 막을 급은 아니라고 심각도를 매길 때(리뷰·스탠드업)
- 한국어: 진행을 막을 문제는 아니다
- 설명: blocker = 앞길을 막는 것. 원문: "Not a blocker for the A/B; worth a comment." — 뒤에 "그래도 주석은 달아라"처럼 후속 조치를 붙이는 게 관례.
- 예문: The stale docstring is real but not a blocker — file it as a follow-up.
- 유사어: non-blocking (형용사형), advisory (권고 수준임을 명시), can ship as-is (구어)
- 반의어: a showstopper (모든 걸 멈추는 치명적 결함)

## "behavior-preserving"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (holistic 리뷰 subagent)
- 맥락: 외부 동작을 전혀 바꾸지 않는 리팩터링임을 못 박을 때(커밋 메시지·리뷰)
- 한국어: 동작을 보존하는 (리팩터링)
- 설명: 원문: "a true behavior-preserving refactor." 구조는 바꾸되 관측 가능한 출력은 동일하다는 계약을 한 단어로 선언한다.
- 예문: The extraction is behavior-preserving: the smoke test output is identical before and after.
- 유사어: no functional change (NFC; 커밋 관례어), semantics-preserving (더 이론적)
- 반의어: behavior-changing (동작이 달라지는)

## "measure the ghost of the old system"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (cross-file impact 감사 subagent)
- 맥락: 지표·도구가 이미 사라진 구현을 기준으로 값을 내고 있음을 수사적으로 강하게 지적할 때(리뷰, 문어)
- 한국어: 옛 시스템의 유령을 측정하다 — 죽은 코드 경로를 진단하다
- 설명: 원문: "its output measures the ghost of the old system." ORB 선택 로직이 제거된 뒤에도 진단 도구가 ORB 기준 분류를 내는 상황. ghost 은유 하나로 "무의미해진 계측"을 각인시킨다.
- 예문: After the selector swap, the diagnostic still measures the ghost of the old system, so its counts say nothing about production.
- 유사어: diagnose a code path that no longer exists (평서형), stale instrumentation (중립 명사구)
- 반의어: track the live behavior (현행 동작을 계측하다)

## "be proportionate"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (holistic 리뷰 지시)
- 맥락: 검토 강도를 대상의 위험도에 맞추라고 지시할 때(리뷰 가이드, 격식)
- 한국어: (수고·엄격함을) 대상에 비례시켜라
- 설명: 원문: "Be proportionate: this is a measurement-tool feature, verified on synthetic data; the real test is the office run." — 측정용 스크립트에 프로덕션급 잣대를 들이대지 말라는 뜻.
- 예문: Be proportionate: it's a throwaway measurement script, so don't demand production-grade error handling.
- 유사어: weigh effort against risk (풀어쓴 표현), keep it in proportion (구어 쪽)
- 반의어: gold-plate (필요 이상으로 공들이다)

## "bit-for-bit identical"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Tasks 3+4 리뷰 subagent)
- 맥락: 반올림·근사 차이조차 없는 완전 동일함을 주장할 때(기술 검증)
- 한국어: 비트 단위까지 동일한
- 설명: 원문: "the returned (tw, th) are bit-for-bit identical." 결정론·재현성 주장에서 "거의 같다"와 구분되는 가장 강한 등급.
- 예문: Five consecutive runs produce bit-for-bit identical results, so the pipeline is fully deterministic.
- 유사어: byte-identical (파일 비교 톤), exactly reproducible (더 일반적)
- 반의어: within float rounding (부동소수 오차 범위 안에서만 같은)

## "safe-by-default"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (holistic 리뷰 subagent)
- 맥락: 옵션 없이 쓴 기본 동작이 안전하도록 설계함을 말할 때(API 설계)
- 한국어: 기본값이 곧 안전한
- 설명: 원문: "This makes the API safe-by-default without touching the test." `X-by-default` 합성 패턴(secure-by-default, private-by-default)의 하나.
- 예문: Changing the default scale band makes the API safe-by-default for future callers.
- 유사어: secure-by-default (보안 문맥), sensible defaults (온건한 표현)
- 반의어: a footgun (잘못 쓰기 쉬운 위험한 기본 설계)

## "retract (a finding)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Tasks 3+4 리뷰 subagent)
- 맥락: 자기가 제기한 지적·주장을 검증 끝에 공식적으로 철회할 때(리뷰·논문, 격식)
- 한국어: (지적을) 철회하다
- 설명: 원문: "Verdict on C1: ... No bug here. **Retract C1.**" — 스스로 낸 Critical 지적을 추적 끝에 거둬들이는 장면. 학술 논문 철회(retraction)에도 같은 단어.
- 예문: After tracing the initialization, I retract the finding — the sentinel can never survive the first iteration.
- 유사어: withdraw (일반·격식), walk back (구어; 슬그머니 물러서는 뉘앙스), stand corrected (정정을 받아들이다)
- 반의어: stand by (one's claim) (주장을 고수하다)
