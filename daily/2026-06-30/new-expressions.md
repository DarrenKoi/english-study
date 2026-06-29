# 2026-06-30 — 수집한 표현

오늘 배치는 거의 전부 `auto_recipe_creator` CV 프로젝트의 **코드 리뷰·구현 트랜스크립트**(영어)였다.
그래서 추출 표현도 *코드 리뷰 영어*에 집중했다 — 개발자에게 실전 가치가 큰 격식 영어다.

---

## "make the comparison apples-to-apples"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator (code review, Task 7)
- 맥락: 두 방식/지표를 **공정하게 같은 조건에서** 비교한다고 강조할 때(설계·리뷰·회의, 격식~중립).
- 한국어: 같은 잣대로(동일 조건에서) 비교하는, 사과 대 사과의 비교.
- 설명: 비교 대상의 조건을 똑같이 맞춰 "공정한 비교"임을 뜻하는 관용구. `apples-to-apples comparison` 처럼 형용사로도 쓴다. 반대는 `apples-to-oranges`(조건이 달라 비교 불가).
- 예문: Change the gate to match exactly so the `min_s="3"` bin comparison is apples-to-apples.
- 유사어: like-for-like (영국식, 거의 동의), on equal footing (대등한 조건에서; 더 격식), a fair comparison (가장 평이)
- 반의어: apples-to-oranges (조건이 달라 비교가 성립하지 않는)

---

## "bit-parity / byte-for-byte identical"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Task 4, bit-parity requirement)
- 맥락: 두 코드 경로가 **완전히 똑같이 동작**해야 함을 못 박을 때(엔지니어링, 격식).
- 한국어: 비트 단위로 동일한 / 바이트 하나까지 똑같은.
- 설명: 결과가 "대충 같다"가 아니라 *완전히 동일*함을 강조하는 기술 표현. `bit-parity`(명사), `byte-for-byte`/`byte-identical`(형용사)로 쓴다. 재현성·회귀 방지 맥락에서 자주 등장.
- 예문: The E proposer call must stay bit-parity with the existing matcher, so a precomputed input yields byte-identical behavior.
- 유사어: identical down to the byte (강조형), behaviorally equivalent (관찰 동작이 같음; 더 느슨), a faithful match (덜 기술적)
- 반의어: subtly divergent (미묘하게 어긋나는), drifted (기준에서 표류한)

---

## "kept in lock-step"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (simplification finding)
- 맥락: 두 곳을 **항상 함께·동시에** 바꿔야 한다고 경고할 때(리뷰·설계, 격식).
- 한국어: 보조를 맞춰 / 한 치의 어긋남 없이 같이 움직이는.
- 설명: 두 상태가 서로 동기화되어 *늘 같이* 갱신돼야 함을 뜻한다. 흔히 유지보수 위험을 지적할 때 "lock-step 으로 관리해야 하니 위험" 식으로 쓴다.
- 예문: Any new modality key must update both dicts in lock-step, or the two will silently diverge.
- 유사어: in sync (평이·구어 가까움), in tandem (둘이 짝지어 함께), hand in hand (비유적)
- 반의어: out of sync (어긋난), independently (각자 따로)

---

## "short-circuit (the None case)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Task 4 review, "None short-circuits")
- 맥락: 조건을 만족하면 **나머지 계산을 건너뛰고 바로 반환**하는 흐름을 말할 때(코드 설명, 격식).
- 한국어: 조기 반환하다 / 중간에 끊고 곧장 빠져나가다.
- 설명: 전기 회로의 "단락"에서 온 말. 함수가 이른 조건에서 즉시 결과를 내고 이후 로직을 타지 않는 것을 가리킨다. `&&`/`or` 의 단축 평가도 같은 단어.
- 예문: `_free_search_best_score` returns `None` only on empty candidates, so the aggregator short-circuits before taking a median.
- 유사어: bail out early (구어), return early (가장 평이), guard clause 로 빠지다 (구문 명칭)
- 반의어: fall through (끝까지 흘러 내려가다), run to completion (끝까지 수행하다)

---

## "a None-sentinel guard"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Task 2 review, GT_TOL_NORM sentinel)
- 맥락: 특정 값(보통 `None`)을 **"없음/미설정"의 표시값**으로 두고 분기할 때(코드 설계, 격식).
- 한국어: 센티넬(보초)값 가드 — `None` 을 "값 없음" 신호로 쓰는 방어 코드.
- 설명: `sentinel` 은 정상 데이터와 구분되는 특수 표시값(주로 `None`/`-1`). `sentinel guard` 는 그 값을 만나면 따로 처리하는 방어 분기를 뜻한다.
- 예문: The four new knobs have non-None defaults, so unconditional `setdefault` can never stringify a sentinel.
- 유사어: a null check (가장 평이), a missing-value guard (서술적), an absence flag (덜 표준적)
- 반의어: (마땅한 대체 표현 없음)

---

## "inert in practice"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 6 review, "inert at runtime")
- 맥락: 결함이 **이론상 존재하지만 실제로는 아무 영향이 없다**고 평가할 때(리뷰 판정, 격식).
- 한국어: 실제로는 무해한 / 작동상 아무 효과가 없는.
- 설명: `inert`(화학적으로 비활성)에서 온 비유. 코드 리뷰에서 "엣지 케이스이긴 하나 현실 입력에선 결코 발생 안 함"을 점잖게 표현. `harmless`/`negligible` 보다 한 단계 격식.
- 예문: A label literally equal to `"total"` would double-count, but `classify_winner` never emits it, so the bug is inert in practice.
- 유사어: harmless in practice (평이), has no real-world effect (서술적), a non-issue (단정적·구어)
- 반의어: actively harmful (실질적 해를 끼치는), a live defect (실제로 터지는 결함)

---

## "a merge blocker"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (whole-branch review)
- 맥락: 어떤 이슈가 **병합을 막을 만큼 중대한지** 판정할 때(코드 리뷰, 격식~중립).
- 한국어: 병합을 막는(머지 차단) 사안.
- 설명: PR 을 main 에 합치기 전에 *반드시* 고쳐야 하는 심각도. 보통 "이건 merge blocker 아니다 → 사소한 개선"으로 강도를 낮춰 말할 때 쓴다.
- 예문: It is a real but minor coverage gap, not a merge blocker.
- 유사어: a release blocker (배포 차단; 더 무거움), a showstopper (치명적·구어), a hard gate (통과 필수 관문)
- 반의어: a nice-to-have (있으면 좋은 정도), a follow-up (나중에 처리할 후속)

---

## "matches the file's house style"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 6, Korean `[WARNING]` prints)
- 맥락: 코드/문서가 **그 저장소 고유의 관행**을 따르는지 따질 때(리뷰·온보딩, 중립).
- 한국어: (그 팀·파일의) 집안 스타일 / 고유 관행.
- 설명: 공식 규칙은 아니지만 그 코드베이스가 *실제로 일관되게 지켜온* 방식. "house style 을 깨면 안 되니 WONTFIX" 처럼 결정을 정당화할 때 자주 등장.
- 예문: The new print matches the seven pre-existing Korean warnings — changing it to English would break the file's house style.
- 유사어: the established convention (격식·서술적), the local idiom (그 코드 특유의 방식), how the rest of the file does it (평이·구어)
- 반의어: an outlier (혼자 튀는 예외), a one-off (관행을 벗어난 일회성)

---

## "confirm or overrule"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (whole-branch review, triage of minors)
- 맥락: 상위 검토자가 하위 판단을 **그대로 인정하거나 뒤집으라**고 지시·수행할 때(리뷰·승인, 격식).
- 한국어: 확정하거나 번복하다 / 인정 또는 기각하다.
- 설명: `overrule`(판정을 뒤집다)은 법정·심판 용어가 일상 업무로 넘어온 것. 리뷰에서 "선임이 이 minor 를 confirm 할지 overrule 할지" 식으로 결정 권한을 가리킨다.
- 예문: The controller's tentative call is WONTFIX; the senior reviewer can confirm or overrule it.
- 유사어: uphold or reverse (더 격식·법률조), sign off on or reject (승인/반려), back or veto (구어·강함)
- 반의어: defer (판단을 미루다), leave undecided (미결로 두다)

---

## "upgrade-only (it must never downgrade)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (Phase 2 E-confirm post-pass)
- 맥락: 어떤 변경이 **한 방향으로만** 작동하도록 불변식을 못 박을 때(설계·리뷰, 격식).
- 한국어: 등급을 올리기만 하는(절대 내리지 않는) 단방향 처리.
- 설명: 후처리(post-pass)가 상태를 *상향*만 하고 절대 *하향*하지 않는다는 안전 불변식. `X-only`(예: append-only, read-only)는 "오직 X 만 한다"는 일반 패턴.
- 예문: This is upgrade-only: the post-pass may bump a row to `E_CONFIRMED` but must never downgrade a tier.
- 유사어: one-directional (방향 한정), monotonic (값이 한쪽으로만 변하는; 수학적), non-destructive (기존 것을 망가뜨리지 않는)
- 반의어: bidirectional (양방향), destructive (덮어써 망가뜨리는)

---

## "a faithful transcription of the spec"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (Task 2 review verdict)
- 맥락: 구현이 명세를 **글자 그대로 충실히 옮겼다**고 호평할 때(리뷰 판정, 격식).
- 한국어: 명세를 충실히(글자 그대로) 옮긴 것.
- 설명: `transcription`(받아쓰기·필사)에 `faithful`(원본에 충실한)을 붙여, 자의적 해석 없이 명세를 정확히 코드로 옮겼음을 칭찬. `spec-faithful`(형용사), `verbatim`(토씨 하나 안 틀리게)과 짝.
- 예문: The implementation is a faithful, minimal transcription of the spec — every requirement met, nothing extra.
- 유사어: spec-faithful (형용사형), a verbatim match (토씨까지 동일), true to the design (덜 기술적)
- 반의어: a loose interpretation (느슨한 해석), a divergence (어긋남)

---

## "dead code (a branch that can't be reached)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (simplification findings)
- 맥락: **실행될 수 없거나 읽히지 않는** 코드를 지적할 때(리뷰·정리, 중립~격식).
- 한국어: 죽은 코드 — 도달 불가능하거나 결코 쓰이지 않는 부분.
- 설명: 닿을 수 없는 분기(unreachable branch), 할당했지만 읽지 않는 변수(assigned but never read) 등을 묶어 부른다. 보통 "이 가드는 위에서 이미 `continue` 했으니 dead code"처럼 무용함을 들어 삭제를 권한다.
- 예문: The `if bank else None` guard is dead code — the earlier `continue` already proved `bank` is truthy.
- 유사어: an unreachable branch (도달 불가 분기; 구체적), a redundant guard (불필요한 방어), a no-op (아무 일도 안 하는 코드)
- 반의어: a live path (실제로 타는 경로), load-bearing code (없으면 깨지는 핵심 코드)

---

## "give the spec a read"
- 레지스터: conversational, casual
- 출처: transcript:[user] "give the spec a read to confirm the fix-type and distinct_floor default"
- 맥락: 동료에게 **문서를 한번 훑어봐 달라**고 가볍게 부탁할 때(구어·채팅, 비격식).
- 한국어: 명세 좀 읽어봐 / 한번 훑어봐 줘.
- 설명: `give X a read` 는 `read X` 를 부드럽고 캐주얼하게 만든 관용 구문. 같은 패턴: `give it a look`, `give it a try`, `give it a go`. 명령형이라도 정중함보다 친근함이 느껴진다.
- 예문: Give the spec a read and confirm the default value before we lock the design.
- 유사어: take a look at (가장 무난), look it over (대충 검토), skim through (빠르게 훑다; 더 가벼움)
- 반의어: study it closely (꼼꼼히 정독하다), pore over (파고들어 정독하다)
