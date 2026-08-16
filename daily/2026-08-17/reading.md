# 2026-08-17 — 정독

## 단락 1

**Objection 1 (worst): the "unfalsifiable fixture" argument proves too much.** The prior doc's priorities — skewvoir lens, nightly rollup, state-space filter — all run on the *same* 129-line static fixture with its three hand-written trend points per tool. A state-space filter on three authored points is exactly as unrecoverable as an MDS map. If "no ground truth ⇒ defer" is the sequencing rule, it doesn't justify the prior doc's order; it annihilates the license for *all* Phase 1 work. The argument's real force is "replace the fixture with a generative mock," which is orthogonal to whether A-2 ships first. Cost of keeping it: your position rests on a principle that, applied consistently, also condemns the alternative you're defending.

**문법·구조**: 반론 하나가 통째로 조립되는 순서를 보여주는 단락이다. 첫 줄은 판정을 먼저 준다 — `Objection 1 (worst)` 로 등급까지 매겨 놓고, 상대 논거를 따옴표에 담아 주어 자리에 앉힌다. 둘째 문장의 대시 삽입구(`— skewvoir lens, nightly rollup, state-space filter —`)는 목록을 문장 흐름에서 잠깐 들어 올려 보여주는 장치로, 괄호보다 눈에 띄고 쉼표보다 덜 헷갈린다. 그 뒤 `all run on the same … fixture` 에서 `all` 이 주어를 되받아 "예외 없이 전부"를 못 박는다.

셋째 문장의 `exactly as unrecoverable as` 는 동등비교 `as … as` 에 `exactly` 를 얹어 정도 차이의 여지를 없앤다 — 상대가 "그건 좀 다르다"로 빠져나갈 틈을 막는 자리다. 넷째 문장이 이 단락의 축이다. 조건절 `If "no ground truth ⇒ defer" is the sequencing rule` 이 **상대의 규칙을 그대로 인용해** 전제로 올린 뒤, 세미콜론으로 두 결과를 대비시킨다(`it doesn't justify …; it annihilates …`). 세미콜론은 여기서 마침표보다 두 절을 세게 붙여, 부정과 확대가 한 호흡의 반전이 되게 한다.

다섯째 문장의 `which is orthogonal to whether A-2 ships first` — 계속적 용법의 관계대명사 `which` 가 앞 절 전체를 받고, 그 뒤에 `whether` 명사절이 전치사 `to` 의 목적어로 들어간다. `if` 가 아니라 `whether` 인 이유는 전치사 뒤이기 때문이다(`orthogonal to if …` 는 비문). 마지막 문장은 콜론으로 대가를 열고, 삽입된 분사구 `applied consistently` 가 "일관 적용하면"이라는 조건을 두 단어로 줄인다. 현재시제 `condemns` 를 쓴 게 요점 — 미래형 `would condemn` 이면 가정으로 물러나지만, 현재시제가 "지금 이 원칙이 이미 그렇게 작동하고 있다"로 읽히게 한다.

**핵심 표현**: `proves too much` — 전제를 부정하지 않고 일관 적용만으로 자멸시키는 논박. `orthogonal to X` — 쟁점이 아예 다른 축이라 이 논의를 못 가른다. `Cost of keeping it: …` — 주장을 유지했을 때 치를 값을 콜론 뒤에 그대로 적는 문형.

**격식 짝**:
- refined: *Applied consistently, that principle also condemns the alternative you're defending.* (작성)
- plain: *If you follow your own rule all the way, it kills your own option too.* (작성)
- refined: *That concern is orthogonal to the sequencing question.* (작성)
- plain: *That's a separate issue — it doesn't tell us what to do first.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md</sub>

---

## 단락 2

The key reason your feared failure mode ("right align point, wrong place in the live box") is structurally prevented: **the align point is never transported as a coordinate from consensus-image space into the live SEM box.** Only image *content* travels. The coordinate is re-derived inside the live box's own pixel space by template matching, so there is no place where a consensus-image pixel coordinate gets naively pasted onto a differently-sized live frame. The size difference is absorbed by the scale sweep, not by any manual rescale that could be wrong. There is, however, one residual risk. If office images ever come at 1024 px, every consensus crop is centered at the *wrong* point — and because all crops are mis-centered **identically**, co-registration aligns them, the median comes out sharp, the blur gate passes, and you get a confident, systematically wrong click.

**문법·구조**: 사용자의 걱정을 먼저 그대로 받아 적고 그것이 왜 성립하지 않는지를 구조로 설명하는 단락이다. 첫 문장은 `The key reason … is structurally prevented:` 로 명사구 주어를 길게 세우고 콜론으로 답을 연다 — 콜론 앞은 "무엇에 답하는가", 뒤는 "답" 이라는 분업이 선명하다. 걱정의 내용을 괄호 안 따옴표로 압축해 넣은 것도 눈여겨볼 만하다. 상대의 말을 요약하지 않고 인용해 두면 반박이 딴 이야기로 새지 않는다.

수동태가 이 단락의 주력이다. `is never transported`, `is re-derived`, `is absorbed` — 행위자를 지우는 게 목적이 아니라, **좌표라는 대상에 초점을 고정하기 위해서**다. 능동으로 바꾸면(`the code never transports the point`) 주인공이 코드로 옮겨 가고, "그 값이 어디를 지나느냐"는 이 설명의 축이 흐려진다. 둘째 문장 `Only image content travels.` 는 세 단어짜리 능동문이라 앞뒤의 긴 수동문 사이에서 확 튄다 — 길이 대비가 강조 장치로 쓰인 자리다.

넷째 문장의 `not by any manual rescale that could be wrong` 은 `A, not B` 구문에 관계절을 달아 B를 그냥 부정하는 게 아니라 **왜 위험한 선택지였는지**까지 담는다. 다섯째 문장의 `There is, however, one residual risk.` 는 삽입 `however` 로 전환을 알리는 격식체 — 문두 `However,` 보다 부드럽고, 문어에서 더 흔하다. 마지막 문장은 `If …, every crop is centered at the wrong point — and because …, A, B, C, and you get …` 로 조건 → 이유 → 연쇄 결과를 한 문장에 이어 붙인다. `aligns / comes out / passes / get` 을 모두 현재시제로 두어 "이 조건에서는 이렇게 굴러간다"는 기계적 필연으로 읽히게 했고, 마지막에 `a confident, systematically wrong click` 이라는 형용사 두 개짜리 명사구로 착지한다 — 형용사 `confident`(자신만만한)와 `wrong`(틀린)의 충돌이 이 위험의 정체를 한 구로 요약한다.

**핵심 표현**: `structurally prevented` — 검사로 막는 게 아니라 구조상 일어날 수 없다. `absorbed by X, not by Y` — 차이를 흡수하는 주체를 지정하고 위험한 대안을 같은 자리에서 배제. `a confident, systematically wrong (result)` — 게이트가 못 잡는 오류의 성질을 형용사만으로 규정.

**격식 짝**:
- refined: *The coordinate is re-derived inside the live box's own pixel space.* (작성)
- plain: *The point gets worked out again inside the live box itself.* (작성)
- refined: *No existing gate can catch this failure mode.* (작성)
- plain: *Nothing we've got would notice this one.* (작성)

<sub>출처: transcript:auto-recipe-creator/03453890 — 원문 두 단락(판정부 + Risk 1)을 이어 붙였고, 잇는 문장 `There is, however, one residual risk.` 만 작성했습니다.</sub>

---

## 단락 3

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure. The opposite is horizontal slicing: writing all tests first, then all implementation. Bulk tests verify *imagined* behavior — you test the shape of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in vertical slices instead: one test → one implementation → repeat, each test a tracer bullet that responds to what the last cycle taught you.

**문법·구조**: 규범을 가르치는 산문의 표본이다. 첫 문장은 `A, not B` 한 구로 정의를 끝낸다 — 정의문에서 반대편을 같은 자리에 붙여 두면 다음 문단 전체가 그 대비 위에서 굴러간다. 둘째 문장 `Code can change entirely; tests shouldn't.` 는 세미콜론으로 두 절을 붙이고, 뒤 절에서 `change` 를 생략했다(`shouldn't` 뒤가 비어 있다). 영어는 조동사만 남기고 본동사를 지우는 생략이 자연스럽고, 그 덕에 여섯 단어짜리 대구가 만들어진다.

셋째 문장은 대시로 예시를 끼워 넣은 뒤 원래 술어로 복귀한다 — `A good test reads like a specification … and survives refactors`. 주어 하나에 동사 둘(`reads`, `survives`)이 걸려 있고, 그 사이에 대시 삽입구가 들어간 구조라 삽입구를 지워도 문장이 온전하다. 이게 대시 삽입의 조건이다. 넷째·다섯째 문장은 안티패턴 쪽으로 넘어가면서 이탤릭 `imagined` 한 단어에 판정을 싣는다. 다섯째 문장의 세 절(`you test …, the tests go …, and you commit …`)은 주어를 일부러 바꿔 가며(you → the tests → you) 병렬을 이룬다 — 같은 주어로 세 번 반복하는 것보다 리듬이 산다. `go insensitive` 는 `become` 대신 `go` 를 쓴 형태로, 나쁜 방향의 변화에 붙는 구어적 연결동사다(`go stale`, `go quiet`).

마지막 문장의 `Work in vertical slices instead:` 는 명령형 + 콜론으로 처방을 열고, 콜론 뒤는 완전한 문장이 아니라 화살표 도식과 동격 명사구(`each test a tracer bullet …`)로 채웠다. 이 동격구에는 be동사가 없다 — `each test [is] a tracer bullet` 의 생략형으로, 규범 문서에서 리듬을 끊지 않고 정의를 덧붙일 때 쓰는 절대구문이다.

**핵심 표현**: `reads like a specification` — 읽으면 그대로 명세가 되는 테스트. `survive refactors` — 리팩터링을 겪고도 살아남다(테스트 품질의 기준). `go insensitive to real changes` — 진짜 변화에 반응하지 못하게 둔해지다.

**격식 짝**:
- refined: *A good test survives refactors because it does not depend on internal structure.* (작성)
- plain: *A good test keeps working after you move the code around.* (작성)
- refined: *Tests verify behavior through public interfaces, not implementation details.* (작성)
- plain: *Test what it does, not how it does it.* (작성)

<sub>출처: transcript:auto-recipe-creator/03453890 (`tdd` 스킬 본문) — 원문의 "What a good test is" 절과 "Horizontal slicing" 불릿을 한 단락으로 이었고, 잇는 문장 `The opposite is horizontal slicing:` 만 작성했습니다.</sub>
