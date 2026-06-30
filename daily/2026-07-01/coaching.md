# 2026-07-01 — 코칭

오늘 배치에서 내가 직접 쓴 한국어는 workflow_2 align-point 매칭 정확도 개선을 요청한 한 단락이었습니다.
기술 배경 설명을 자연스러운 영어로 옮기는 데 집중했습니다. (어시스턴트 고급 한국어·내가 쓴 영어 원문은 없어 해당 섹션은 생략)

## 한글→영어

### 카드 1 — "제대로 못 잡고 있다"   (내가 쓴 한글)
- 내가 쓴 한글: "live SEM box 이미지에서 align point를 잡는 테스트를 해봤는데, align point를 제대로 못 잡고 있다."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: I tested locating the align point on live SEM box images, but it isn't reliably locking onto the point.
- 왜 이렇게: "(좌표를) 잡다"는 맥락에 따라 동사가 갈립니다. 탐지/위치추정이면 **locate**·**pinpoint**, 추적해 고정하면 **lock onto**가 자연스럽습니다. "제대로 못 ~"은 **isn't reliably -ing**(신뢰성 부족) 또는 **fails to ~**로 옮깁니다. "테스트를 해봤는데"의 '~해봤다'는 시도의 뉘앙스라 단순 과거 **I tested / I tried** 로 충분하고, 굳이 "tried to test"처럼 겹치지 않습니다.

### 카드 2 — "포팅했는데 정확도가 부족하다"   (내가 쓴 한글)
- 내가 쓴 한글: "workflow_2에서 이미 했던 매칭/ensemble/threshold/consensus 개선을 workflow_3/align 으로 포팅한 상태인데, 정확도가 부족하다."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: I've already ported the matching, ensemble, threshold, and consensus improvements from workflow_2 into workflow_3/align, but the accuracy still falls short.
- 왜 이렇게: "~한 상태인데"는 **현재완료 + but**으로 옮기면 "이미 해놨지만 (여전히) 문제가 남았다"는 결과 상태가 잘 살아납니다(I've ported … but …). "정확도가 부족하다"를 직역한 *the accuracy is lacking*보다 **falls short**(기준에 못 미친다) 또는 **isn't good enough**가 더 관용적입니다. 나열은 영어에서 마지막 항목 앞에 **and**를 넣는 게 표준입니다(A, B, C, and D).

### 카드 3 — "검증된 변경만 포팅한다"   (내가 쓴 한글)
- 내가 쓴 한글: "검증된 변경만 나중에 workflow_3로 포팅한다."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Only validated changes get ported back to workflow_3 later.
- 왜 이렇게: "검증된 변경만"의 **Only + 명사구**를 문두에 두면 영어에서 자연스럽게 강조됩니다. 한국어 "~한다"(규칙·방침 진술)는 행위자를 드러내지 않는 **수동태 현재시제**(get/are ported)가 잘 맞습니다 — 누가 하느냐보다 "그렇게 한다"는 원칙이 핵심이니까요. "나중에"는 문장 끝 **later**가 가장 가볍고, "다시 들여보낸다"는 회귀 뉘앙스를 **port back**의 *back*이 담아 줍니다.

### 카드 4 — "구체적이고 시도 가능한 방법"   (내가 쓴 한글)
- 내가 쓴 한글: "정확도를 더 높일 수 있는 구체적이고 시도 가능한 방법들을 연구해서 제안하고, 가능하면 벤치에서 실험을 셋업/실행까지 해줘."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Research and propose concrete, actionable ways to push the accuracy higher, and if feasible, set up and run the experiments on the bench yourself.
- 왜 이렇게: "시도 가능한"은 *tryable*(어색) 대신 **actionable**(바로 실행에 옮길 수 있는)이 비즈니스·엔지니어링에서 표준 어휘입니다. "정확도를 더 높이다"는 **push the accuracy higher** 또는 **improve accuracy further**. "가능하면"은 **if feasible**(실현 가능하면)이 *if possible*보다 한 단계 격식 있고, 자원·여건상 가능하냐는 뉘앙스를 줍니다. "셋업/실행까지 해줘"의 '~까지'는 **set up and run … yourself**에서 *yourself*로 "제안에 그치지 말고 직접 끝까지"라는 함의를 살립니다.
