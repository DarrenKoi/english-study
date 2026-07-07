# 2026-07-08 — 정독

## 단락 1

The key challenge is the circular import. My solution: place `from poc.workflow_2.ensemble_proposer import compute_ensemble_candidates` at the BOTTOM of `align_key_matcher.py`, after all function definitions. This works because: 1. When Python starts loading `align_key_matcher`, it registers the partial module in `sys.modules`. 2. The function `compute_align_key_score_ensemble` is defined (referencing `compute_ensemble_candidates` as a global name to be resolved at call time). 3. At the bottom, Python imports `ensemble_proposer` — which in turn imports from `align_key_matcher`, but since `align_key_matcher` is already in `sys.modules` (with all needed names already defined), it succeeds. 4. `compute_ensemble_candidates` is bound in `align_key_matcher`'s namespace, making it patchable via `akm.compute_ensemble_candidates`.

**문법·구조**: 기술 설명의 정석 구조 — 문제 한 문장(The key challenge is X) → 해법 한 문장(My solution: ...) → "This works because:" 뒤에 번호 매긴 인과 사슬. 시제는 전부 **현재 단순형**(registers, is defined, imports, succeeds)인데, 이는 "지금 일어난 일"이 아니라 "Python이 언제나 이렇게 동작한다"는 일반 원리를 서술하기 때문입니다. 3번 문장의 `which in turn imports ...`는 관계절에 in turn(연쇄적으로, 이번엔 그쪽이)을 끼워 A→B→다시 A의 순환을 한 절로 처리하고, `but since ... , it succeeds`로 양보-이유-결과를 압축합니다. 마지막 문장의 `making it patchable`은 분사구문으로 "그 결과 ~하게 된다"를 접속사 없이 잇는, 결과 서술의 대표 패턴입니다. `to be resolved at call time`은 수동 부정사로 "나중에 해석되도록 남겨 둔다"는 지연 의미를 담습니다.

**핵심 표현**:
- **resolved at call time** — (이름이) 정의 시점이 아니라 호출 시점에 해석되는. 지연 바인딩 설명의 핵심 콜로케이션.
- **which in turn imports ...** — "그러면 그쪽이 다시 ~한다". 연쇄·순환 의존을 한 절로 잇는 연결 장치.
- **making it patchable via X** — "그 덕분에 X로 패치 가능해진다". 결과를 붙이는 분사구문.

**격식 짝** (작성):
- refined: "The import is deferred to the end of the module so that the name is resolved only at call time." ↔ plain: "We just import it at the bottom, so Python looks the name up later."
- refined: "This arrangement renders the symbol patchable at module level." ↔ plain: "This way the tests can monkeypatch it."

<sub>출처: transcript:auto_recipe_creator subagent (circular import 해결 보고)</sub>

---

## 단락 2

If compute_align_key_score succeeds but compute_align_key_score_ensemble raises (e.g. OOM in the ORB pool-rerank on a large frame), the exception exits the try block, drop['match_failed'] += 1, and the frame is skipped for both arms. The A/B hit counts remain fair (equal frame set), but match_failed silently merges baseline-caused and ensemble-caused failures. If the ensemble arm is systematically more fragile on a subset of frames (those where its proposer generates more candidates, triggering heavier ORB cost), the drop inflates without exposing which arm is responsible. Splitting into two try/except blocks with per-arm counters (match_failed_base, match_failed_ens) would surface this; alternately, if one arm fails the frame should still be counted for the other arm and the failure recorded against only the failing arm.

**문법·구조**: 버그 리포트의 failure scenario 를 쓰는 법을 보여주는 단락. 1~3문장은 **현재 단순형 조건문**(If X succeeds but Y raises..., the exception exits...)으로 "이 입력이면 반드시 이렇게 된다"는 결정론적 인과를 서술합니다 — 가정법이 아니라 현재형을 쓰는 것이 포인트(코드의 동작은 확정적이므로). 반면 마지막 문장의 `Splitting ... would surface this`는 **동명사 주어 + would**로 "아직 안 한 수정"의 가상 효과를 말하므로 조동사가 would로 바뀝니다 — 현상(현재형)과 제안(would)의 시제 대비가 이 장르의 핵심 문법입니다. `those where its proposer generates more candidates`는 선행사를 those로 받는 관계절, `triggering heavier ORB cost`는 결과 분사구문. `the failure (should be) recorded against only the failing arm`은 반복되는 should be를 생략한 병렬 구조입니다.

**핵심 표현**:
- **silently merges X-caused and Y-caused failures** — 원인이 다른 실패들을 구분 없이 합산해 버리다. `X-caused` 합성 패턴.
- **without exposing which arm is responsible** — 어느 쪽 책임인지 드러내지 못한 채. without + -ing + 간접의문문.
- **would surface this** — (그렇게 하면) 이 문제가 드러날 것이다. surface 를 타동사로.

**격식 짝** (작성):
- refined: "The counter does not distinguish which arm was responsible for the failure." ↔ plain: "You can't tell which side actually broke."
- refined: "Recording the failure against only the failing arm would preserve the other arm's sample." ↔ plain: "Just count the failure on the side that failed and keep the other one's number."

<sub>출처: transcript:auto_recipe_creator subagent (eval 러너 버그 헌트, finding 3)</sub>
