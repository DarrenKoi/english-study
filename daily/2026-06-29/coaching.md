# 2026-06-29 — 코칭

## 한글→영어

### 카드 1 — 보고서 한 줄 수정 요청   (내가 쓴 한글)
- 내가 쓴 한글: "minor fix: 평가 중이고 단계별 현황을 정리했습니다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Minor wording fix: it's under evaluation, and this report lays out the status phase by phase.
- 왜 이렇게: "평가 중"은 진행 중 상태이므로 `under evaluation`(또는 `still being evaluated`)이 자연스럽다. "정리했습니다"는 문서가 내용을 *제시·배열*한다는 뜻이라 영어에서는 주어를 문서로 잡아 `this report lays out / sets out the status`로 옮기면 한국어의 무주어 문장이 매끄러운 영어가 된다. "단계별"은 `phase by phase` 또는 `stage by stage`. 직역체 `organized the status by step`보다 문서를 주어로 세운 능동문이 영어답다.

### 카드 2 — 자기 지시적 보고 문장   (고급 한글 · 번역)
- 한글 원문: "평가 중이며, 본 보고는 단계별 현황을 정리한 것입니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Evaluation is ongoing; this report consolidates the current status, phase by phase.
- 번역 포인트: "본 보고는 ~한 것입니다"는 한국어 격식체의 *명사형 서술*("~한 것이다")인데, 영어로는 명사절로 끌지 말고 `this report consolidates ...`처럼 동사로 푸는 게 자연스럽다. "~이며"의 연결은 세미콜론(`;`)으로 두 독립절을 잇는 격식 문어체와 잘 맞는다. `consolidate`는 흩어진 현황을 한데 모아 정리한다는 뉘앙스로 "정리한 것"보다 정확하다.

## 영어 다듬기

### 카드 1 — 한계 돌파 방안 묻기
- 내가 쓴 영어: "we have been doing lots of test to get the right align point using ensembles of cv algorithms. We are stuck in increasing the score. what else can we do to fill the gap? ... I am okay with CV methods like we are doing but we have to append some backup solutions."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `lots of test` → `lots of tests`(가산명사 복수). `stuck in increasing the score` → `stuck trying to improve the score`(stuck 뒤에는 `on + 명사` 또는 `-ing`; "올리려다 막혔다"는 `stuck trying to ...`). `append some backup solutions` → `add some backup solutions`(append 는 데이터·리스트 뒤에 "이어 붙이다"라 해법에는 어색).
- 더 나은 표현: We've run a lot of tests to pin down the right align point with an ensemble of CV algorithms, but we've plateaued on the score. What else can we do to close the gap? I'm fine staying with CV methods, but we need to add some backup approaches.
- 왜: `plateau on the score`는 "점수가 정체됐다"를 한 단어로 깔끔히. `pin down`(콕 집어 확정), `close the gap`(격차를 메우다)은 오늘 정독·표현과도 이어지는 자연스러운 콜로케이션. `backup approaches/solutions`로 통일.

### 카드 2 — 작업 우선순위 정하기
- 내가 쓴 영어: "align_consensus_cache is not fully established yet. we need to have hardening the consensus-cache + make better decision layer first"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `we need to have hardening` → `we need to harden`(need to + 동사원형; `have + -ing` 는 비문). `make better decision layer` → `build a better decision layer`(관사 `a` 필요; 추상 계층을 "만들다"는 `build`).
- 더 나은 표현: align_consensus_cache isn't fully in place yet, so we should harden the consensus cache and build a stronger decision layer first.
- 왜: `not fully established` → `not fully in place`가 시스템·구성요소에 더 흔한 표현. 두 할 일을 `and`로 병렬(`harden ... and build ...`)해 동사원형을 맞추면 리듬이 산다. `so`로 인과를 명시해 "아직 안 됐으니 → 먼저 이걸 하자"는 논리가 또렷해진다.

### 카드 3 — 퇴근하며 작업 넘기기
- 내가 쓴 영어: "store the plan in @... I will to this job tomorrow. I leave the office now."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `I will to this job tomorrow` → `I'll do this job tomorrow`(`will` 뒤 동사 `do` 누락). `I leave the office now` → `I'm leaving the office now`(지금 막 떠나는 행동은 현재진행형).
- 더 나은 표현: Save the plan under @... — I'll pick this up tomorrow. I'm heading out now.
- 왜: `pick this up (tomorrow)`는 "내일 이어서 하겠다"는 인수인계 뉘앙스라 단순 `do`보다 자연스럽다. `head out`은 "(자리를) 뜨다·퇴근하다"의 구어. `store` 대신 `save ... under <경로>`가 파일 저장에 흔한 콜로케이션.

### 카드 4 — 용어 확인 질문
- 내가 쓴 영어: "Inference Host means a VLM model with Large Parameters?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: 문장 부호상 의문문이면 어순을 `Does ... mean ...?`로. `a VLM model`은 `VLM`에 이미 model 이 들어가 중복(`a large-parameter VLM`로 충분).
- 더 나은 표현: Does "inference host" mean a large-parameter VLM?
- 왜: `Large Parameters`(불필요한 대문자·복수)보다 형용사형 `large-parameter`가 명사 앞 수식으로 깔끔하다. 평서문에 물음표만 붙이기보다 `Does ... mean ...?` 정식 의문문이 글에서 더 또렷하고, 따옴표로 용어를 감싸면 "이 말이 ~라는 뜻이냐"는 메타 질문임이 분명해진다.
