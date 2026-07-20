# 2026-07-21 — 코칭

## 한글→영어

### 카드 1 — 코드 검토 후 개선까지 위임하기   (내가 쓴 한글)
- 내가 쓴 한글: "그 코드를 살펴보고 개선해야 할 게 있으면 진행해 주고, 추가로 더 진행해 보면 좋을 방법이 있으면 코드에 반영해 줘."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Look over the code, and if anything needs improving, go ahead and do it. If you see other approaches worth trying, work them into the code too.
- 왜 이렇게: "살펴보다"는 `look over`(훑어보다)나 `review`가 자연스럽다. "진행해 줘"는 `go ahead and do it`으로, 허락·위임의 뉘앙스를 살린다. "코드에 반영하다"를 직역해 `reflect in the code`라 하면 어색하고, `work them into the code`(끼워 넣다)나 `fold them in`이 원어민 표현이다.

### 카드 2 — 설정 없이 바로 실행   (내가 쓴 한글)
- 내가 쓴 한글: "golden_registration_eval_cond에 반영해 줄 수 있어? env 설정 없이 바로 실행하고 싶어."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Could you bake this into `golden_registration_eval_cond`? I want it to run out of the box, with no env setup.
- 왜 이렇게: "반영하다"가 카드 1과 달리 여기선 "기본값으로 넣어 두다"는 뜻이라 `bake this in`(굽듯이 붙박이로 넣다)이 딱 맞는다. "설정 없이 바로 실행"은 `run out of the box`(별도 설정 없이 곧장 동작)라는 관용구가 정확하다.

### 카드 3 — 개선 가능 여부와 우선순위 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "아무 알고리즘도 GT에 도달하지 못한 케이스들은 개선할 수 없는 거라고 봐야 하나? prod_mind가 제일 우선이야, 현재는?"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Should we treat the cases that no algorithm reaches as unfixable? And is `prod_mind` the top priority right now?
- 왜 이렇게: "~라고 봐야 하나?"는 `Should we treat X as …?`(X를 …로 간주해야 하나)가 자연스럽다. "개선할 수 없는"은 형용사 한 단어 `unfixable`로 압축된다. "제일 우선이야?"는 `the top priority`, 문미의 "현재는?"은 `right now`로 가볍게 붙인다.

### 카드 4 — 표기가 부정확하니 더 분명하게   (내가 쓴 한글)
- 내가 쓴 한글: "overlay notation이 정확하지 않은 것 같아. 색과 글씨를 좀 더 분명하게 확인할 수 있게 정해 주는 게 좋겠어."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: The overlay notation doesn't look quite right. It'd be better to make the colors and labels easier to tell apart.
- 왜 이렇게: "~인 것 같아"의 완곡함은 `doesn't look quite right`으로 산다 — 단정(`is wrong`)보다 부드럽다. "분명하게 확인할 수 있게"는 색·라벨을 "서로 구별하다"는 뜻이므로 `easier to tell apart`가 핵심을 짚는다. "정해 주는 게 좋겠어"는 제안의 `It'd be better to …`.

### 카드 5 — 이 도구를 계속 쓸 가치가 있나   (내가 쓴 한글)
- 내가 쓴 한글: "openwiki로 폴더 구조들을 만들었는데, 네가 코드를 관리하는 데 효과적인 툴이야? openwiki를 계속 유지하는 게 좋아?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: I set up the folder structure with openwiki — is it actually a useful tool for you when you work with the code? Is it worth keeping around?
- 왜 이렇게: "효과적인 툴이야?"를 `effective tool`이라 해도 되지만 구어에선 `useful`이 더 자연스럽고, `actually`를 넣으면 "정말로 도움이 되냐"는 의구심이 산다. "계속 유지하는 게 좋아?"는 `Is it worth keeping around?`(계속 둘 값어치가 있나)라는 관용 표현이 깔끔하다.

### 카드 6 — 어디를 봐야 하는지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "SEM arm 행 3개, 어디를 봐야 해?"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: For the three SEM arm rows, which numbers should I be looking at?
- 왜 이렇게: "어디를 봐야 해?"를 그대로 `where should I look?`이라 하면 위치를 묻는 느낌이라, 표에서 "어떤 값"을 봐야 하는지 물을 땐 `which numbers should I be looking at?`이 뜻을 정확히 전한다. 진행형 `be looking at`이 "지금 주목할 대상"을 부드럽게 가리킨다.

### 카드 7 — 개선 여지는 재등록 몫이다   (고급 한글 · 번역)
- 한글 원문: "rerank·verifier는 '있는 후보들의 순서를 다시 매기는' 도구라, 목록에 없는 답을 위로 끌어올릴 수단이 없습니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: Rerankers and verifiers only reorder the candidates you already have, so there is simply no way for them to promote an answer that isn't on the list.
- 번역 포인트: "~라서 ~할 수단이 없다"는 인과 구조를 `so there is no way to …`로 옮기면 명료하다. "위로 끌어올리다"는 순위 맥락에서 동사 `promote`(순위를 올리다) 하나로 압축된다. "목록에 없는"은 관계절 `that isn't on the list`. `simply`를 끼워 "원리상 방도가 없다"는 단호함을 더한다.

### 카드 8 — 우선순위가 아니라 합의다   (고급 한글 · 번역)
- 한글 원문: "prod_mind는 'NCC와 mind가 동등한 투표권으로 합의한 결과'이지, mind가 NCC를 이기는 구조가 아닙니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: `prod_mind` is a consensus in which NCC and mind get an equal vote — not a scheme where mind overrides NCC.
- 번역 포인트: "동등한 투표권으로 합의한 결과"는 `a consensus in which … get an equal vote`처럼 전치사+관계대명사(`in which`)로 매끄럽게 묶는다. "A이지 B가 아니다" 대조는 대시 뒤 `not …`로 받아 리듬을 살린다. "이기는 구조"의 "이기다"는 투표 맥락이라 `override`(무효화하고 앞서다)가 `win`보다 정확하다.

### 카드 9 — ROI가 안 맞는다   (고급 한글 · 번역)
- 한글 원문: "새 verifier arm을 6점(그것도 SEM 하드 케이스)을 위해 개발·A/B·포팅하는 것은 ROI가 안 맞습니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: Building, A/B-testing, and porting a new verifier arm just to recover six points — SEM hard cases at that — isn't worth the effort.
- 번역 포인트: "ROI가 안 맞는다"를 직역해 `the ROI doesn't fit`이라 하면 어색하다. `isn't worth the effort`(들인 노력만큼의 값어치가 없다)가 자연스러운 대응이다. "그것도 ~"라는 삽입 강조는 `— … at that —` 구문으로 옮기면 원문의 냉소적 부연을 그대로 살린다.

## 영어 다듬기

### 카드 1 — 다른 경로 방식을 써 달라
- 내가 쓴 영어: "load_dotenv (__file__) is not the right way for me. use different path method."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `use different path method` → `use a different path method` — 셀 수 있는 단수명사(`method`) 앞에는 관사가 필요하다.
- 더 나은 표현: `load_dotenv(__file__)` isn't the right approach for my setup — could you use a different way to resolve the path?
- 왜: "the right way for me"는 통하지만 `the right approach for my setup`(내 환경에는)이 의도를 더 분명히 한다. 명령형 `use …`보다 `could you …?` 요청형이 협업 톤에 맞고, "path method"는 `a different way to resolve the path`로 풀면 "경로를 어떻게 찾을지"라는 뜻이 산다.

### 카드 2 — 분리 규칙이 뭐야
- 내가 쓴 영어: "question. from sem_list, you seperate the datatable between cd-sem and hv-sem. what is the rule?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `seperate` → `separate`(철자), `the datatable` → `the data table`(두 단어). 또한 "분리한다"는 사실 서술이므로 현재시제 `you separate`는 맞지만, 규칙을 묻는 맥락엔 `you split`이 더 흔하다.
- 더 나은 표현: Quick question: in `sem_list`, you split the data table into cd-sem and hv-sem — what's the rule behind that?
- 왜: `separate A between B and C`는 어색하고, "둘로 나누다"는 `split A into B and C`가 정확하다. 서두 "question."은 `Quick question:`으로 다듬으면 자연스럽고, "what is the rule?"에 `behind that`을 붙이면 "무슨 기준으로 그렇게 나누냐"는 진짜 의도가 드러난다.

### 카드 3 — 한글 입력이 마지막 타건을 놓친다
- 내가 쓴 영어: "Korean Language typing has some issue. fail to type the last keystrokes. why is it so?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `fail to type` 앞에 주어가 없다 → `it fails to register the last keystrokes`. `why is it so?`는 문법은 되지만 부자연 → `why does this happen?`.
- 더 나은 표현: Korean input has a problem — it drops the last keystroke of a syllable. Why does this happen?
- 왜: "some issue"는 `a problem`으로 충분하다. "마지막 타건을 놓친다"는 `drop the last keystroke`(입력을 흘리다)가 증상을 정확히 그린다. 원인을 묻는 자연스러운 관용구는 `Why does this happen?`이다.

### 카드 4 — 어떤 작업에 이득이냐
- 내가 쓴 영어: "what kinds of jobs are beneficiary if I use pinia? I want to know the pinia concept"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `beneficiary`(수혜자, 명사)는 여기서 오용 → 동사 `benefit`으로. `what kinds of jobs are beneficiary` → `what kinds of tasks benefit`.
- 더 나은 표현: What kinds of tasks actually benefit from Pinia? I'd like to understand the core concept.
- 왜: `beneficiary`는 "혜택을 받는 사람"이라 문장이 성립하지 않는다. "이득을 본다"는 자동사 `benefit from`이 정답. "job"은 프로그래밍에선 배치 작업을 연상시키니 `tasks`/`use cases`가 안전하고, "개념을 알고 싶다"는 `understand the core concept`가 매끄럽다.

### 카드 5 — Nuxt가 Pinia를 대신할 수 있나
- 내가 쓴 영어: "Nuxt can take over pinia features? just curiosity"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 의문문 어순 누락 → `Can Nuxt take over Pinia's features?`. `just curiosity`(명사) → `just curious`(형용사).
- 더 나은 표현: Can Nuxt cover what Pinia does on its own? Just curious.
- 왜: 조동사 의문은 `Can Nuxt …?`로 도치해야 한다. `take over`도 되지만 "그 역할을 대신 감당하다"는 `cover what Pinia does`가 더 또렷하다. 상투구는 `Just curious.`(그냥 궁금해서)로 굳어져 있다.

### 카드 6 — future annotations의 이점
- 내가 쓴 영어: "what's the benefits of having future annotations in py files?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 주어가 복수(`benefits`)이므로 `what's`(= what is) → `what are the benefits`.
- 더 나은 표현: What are the benefits of using `from __future__ import annotations` in Python files?
- 왜: 복수 주어엔 복수 동사(`are`). "having … in py files"보다 실제로 무엇을 하는지 `using from __future__ import annotations`로 명시하면 질문이 구체적이 된다. "py files"는 문서에선 `Python files`로 풀어 쓰는 편이 낫다.
