# 2026-11-10 — 코칭

출처는 모두 `transcript:[user]`/`[assistant]` pm-notes-my-task 2825a965 (ARC TF 제안서 수정 세션)입니다.

## 한글→영어

### 카드 1 — 명사형 종결 선호   (내가 쓴 한글)
- 내가 쓴 한글: "~듦, ~핢 보다는 명사형으로 끝나면 좋다."
- 자연스러운 영어: I'd rather the bullets end in nouns than in "-함"/"-듦" verb forms.
- 왜 이렇게: 취향을 말할 때 `I'd rather A than B` 가 가장 자연스럽습니다. "명사형으로 끝나다"는 `end in nouns`. 영어 개조식에서도 같은 개념을 `noun phrases instead of clauses` 라고 부릅니다.

### 카드 2 — 기반 확보   (내가 쓴 한글)
- 내가 쓴 한글: "API 없는 장비를 사내 AI로 읽고 조작하는 기반 확보."
- 자연스러운 영어: We now have a foundation for reading and operating equipment that has no API, using our in-house AI.
- 왜 이렇게: "확보"를 `secure` 로 직역하면 보안 뜻과 헷갈립니다. 결과를 말하는 `We now have a foundation for …` 가 깔끔합니다. 장표 제목이면 `A foundation for operating API-less equipment with in-house AI` 처럼 명사구로 둡니다.

### 카드 3 — 큰 허들, headless 불가   (내가 쓴 한글)
- 내가 쓴 한글: "SecureVDI는 스크린샷 기반으로 입력 가능 (큰 허들, headless 불가)"
- 자연스러운 영어: SecureVDI only accepts input through screenshots. That's a major hurdle, and it can't run headless.
- 왜 이렇게: "가능"이지만 실제로는 제약이라 `only` 를 넣어야 뜻이 맞습니다. `hurdle` 은 그대로 영어에서도 씁니다. `run headless` 가 동사구 정석입니다.

### 카드 4 — 혼자 두 역할   (내가 쓴 한글)
- 내가 쓴 한글: "PoC는 두 역할을 혼자 맡아서 진행했음"
- 자연스러운 영어: I ran the PoC alone, covering both roles.
- 왜 이렇게: "두 역할을 맡다"는 `cover both roles` 또는 `wear both hats`(구어). 주어를 `I` 로 세워야 영어답습니다.

### 카드 5 — 확보 자체가 지연   (내가 쓴 한글)
- 내가 쓴 한글: "녹화분 확보 경로가 없어 확보 자체에 시간 지연."
- 자연스러운 영어: With no established way to get recordings, just getting them took a long time.
- 왜 이렇게: "~자체"는 `just getting them` 이나 `getting them in the first place` 로 살립니다. `With no …` 로 이유를 앞에 짧게 둡니다.

### 카드 6 — 라벨링은 현업 몫   (내가 쓴 한글)
- 내가 쓴 한글: "녹화분에서 Recipe 작업 내용 추출 -> AI가 이해할 수 있도록 라벨링하는 작업은 현업 엔지니어가 진행 필요함"
- 자연스러운 영어: Extracting the recipe steps from recordings and labeling them so the AI can understand them has to be done by the field engineers.
- 왜 이렇게: "진행 필요함"은 `has to be done by` 수동태가 자연스럽습니다. 동명사 주어 두 개(Extracting … and labeling …)를 하나의 작업으로 보고 단수 동사 `has` 를 씁니다. 현업 엔지니어는 `field engineers` 또는 `process engineers`.

### 카드 7 — Human on Command   (내가 쓴 한글)
- 내가 쓴 한글: "엔지니어가 원할 때 Agent 실행. 작업에 대한 책임 (Human on Command)"
- 자연스러운 영어: The agent runs only when an engineer starts it, and the engineer stays accountable for the work.
- 왜 이렇게: "원할 때"는 `on demand` 나 `only when … starts it` 으로 주도권이 사람에게 있음을 드러냅니다. 결과에 대한 책임은 `responsible` 보다 `accountable` 이 정확합니다.

### 카드 8 — 기술 부채 적재   (내가 쓴 한글)
- 내가 쓴 한글: "기술부채가 적재됨 (혼자서 진행하니 원리를 확인하지 못하고 진행한 사항들이 대부분)"
- 자연스러운 영어: Tech debt piled up. Working alone, I pushed most things through without checking why they worked.
- 왜 이렇게: "적재"는 `piled up` / `accumulated`. "원리를 확인하지 못하고"는 `without understanding why they worked` 가 살아 있는 표현입니다. 분사구문 `Working alone,` 으로 이유를 붙였습니다.

### 카드 9 — 의미 불분명   (내가 쓴 한글)
- 내가 쓴 한글: "9 페이지 돌파구 추천 채택률 의미가 다소 불분명. -> 삭제"
- 자연스러운 영어: On page 9, "breakthrough suggestion adoption rate" is a bit unclear. Let's drop it.
- 왜 이렇게: "다소"는 `a bit`(구어)/`somewhat`(격식). 삭제 지시는 `drop it` / `remove it` 이 자연스럽고, `delete` 는 파일·데이터에 더 어울립니다.

### 카드 10 — 비율로 표기   (내가 쓴 한글)
- 내가 쓴 한글: "자동화 측정 기준 -> recipe setup에 얼마나 Agent가 개입을 해서 진행했는 지 Recipe 별로 비율로 표기."
- 자연스러운 영어: For the automation metric, show per recipe what percentage of the setup the agent handled.
- 왜 이렇게: "얼마나 개입해서 진행했는지"는 `what share/percentage … the agent handled` 로 짧아집니다. "Recipe 별로"는 `per recipe`.

### 카드 11 — 명확한 표현   (내가 쓴 한글)
- 내가 쓴 한글: "\"WIP에 영향을 주는 Wafer Align 문제부터 자동화 시도\" 명확한 표현 사용."
- 자연스러운 영어: Use clear wording: "We start by automating the wafer-align issues that affect WIP."
- 왜 이렇게: "~부터 시도"는 `start by + -ing`. `affect` 는 동사, `effect` 는 명사라는 구분도 여기서 확인해 두세요.

### 카드 12 — 동시 시작 불가   (내가 쓴 한글)
- 내가 쓴 한글: "C는 제거. (전체를 동시에 시작하기 불가능)"
- 자연스러운 영어: Remove option C. We can't realistically start everything at once.
- 왜 이렇게: "불가능"을 `impossible` 로 쓰면 너무 단정적입니다. 기획 문서에서는 `can't realistically` / `isn't feasible` 이 설득력이 있습니다.

### 카드 13 — 무슨 말이지?   (내가 쓴 한글)
- 내가 쓴 한글: "페이지 7 베타 기준 내용이 뭔가 불명확한데, 무슨 말이지?"
- 자연스러운 영어: The beta criteria on page 7 feel a bit vague. What are they actually saying?
- 왜 이렇게: "뭔가 불명확한데"의 모호한 느낌은 `feel a bit vague`. `What does this mean?` 보다 `What are they actually saying?` 이 "의도가 뭐냐"에 가깝습니다.

### 카드 14 — 구체화 필요   (내가 쓴 한글)
- 내가 쓴 한글: "생성형 AI모델에게 Recipe 작업 방식을 어떻게 학습시킬 것인지 구체화 필요"
- 자연스러운 영어: We need a concrete plan for how to teach generative models the way recipe work is done.
- 왜 이렇게: "구체화 필요"는 `need to pin down` 이나 `need a concrete plan for` 로 씁니다. `concretize` 는 영어권에서 잘 안 씁니다.

### 카드 15 — 함께 쓰이는 구조 필수   (내가 쓴 한글)
- 내가 쓴 한글: "Rule 기반 자동화, 이미지 처리(CV), ML/DL를 생성형 AI모델과 함께 쓰이는 구조 필수"
- 자연스러운 영어: The architecture must let rule-based automation, CV, and ML/DL work alongside the generative model.
- 왜 이렇게: "함께 쓰이는"은 `work alongside`. "구조 필수"는 `The architecture must …` 로 주어를 세우면 개조식 명사 나열보다 분명해집니다.

### 카드 16 — 인원 범위   (내가 쓴 한글)
- 내가 쓴 한글: "공통 플랫폼 팀도 최소 3명, 최대 5명으로 필요할 것 같아. 1차 MI팀에 속한 현업 엔지니어들이 개발일 같이 진행해도 좋음."
- 자연스러운 영어: I think the platform team needs three to five people. Field engineers from the first MI group could also pitch in on development.
- 왜 이렇게: "최소 3명, 최대 5명"은 `three to five people` 이면 충분합니다. "같이 진행해도 좋음"은 `could pitch in on` 이 부드러운 허용 표현입니다.

### 카드 17 — 고정하자   (내가 쓴 한글)
- 내가 쓴 한글: "그냥 개발 5명으로 고정하자. 리드 1명. backend 2명, frontend 2명."
- 자연스러운 영어: Let's just lock it at five developers: one lead, two backend, two frontend.
- 왜 이렇게: "고정하자"는 `lock it at` / `settle on`. 콜론 뒤에 내역을 나열하면 한 문장에 정리됩니다.

### 카드 18 — 너무 길게 느껴짐   (내가 쓴 한글)
- 내가 쓴 한글: "8주 합류 교육이 너무 길게 느껴지는데, 4주 합류 교육이 어떨까"
- 자연스러운 영어: Eight weeks of onboarding feels too long. How about four?
- 왜 이렇게: 제안은 `How about …?` / `What if we made it four weeks?`. 반복되는 "합류 교육"은 영어에서 두 번째부터 생략합니다.

### 카드 19 — 유지하고 두자   (내가 쓴 한글)
- 내가 쓴 한글: "응, 주 5시간 유지하고 기준선은 2월로 둬"
- 자연스러운 영어: Yes, keep it at five hours a week and leave the baseline in February.
- 왜 이렇게: "유지"는 `keep it at`, "그대로 두다"는 `leave … in`. 둘 다 짧은 구동사라 대화체에 맞습니다.

### 카드 20 — 있을 필요가 없어   (내가 쓴 한글)
- 내가 쓴 한글: "PoC에서 얻은 것 중에 화살표가 컬럼 사이에 있는데, 있을 필요가 없어."
- 자연스러운 영어: On the "What we got from the PoC" slide, the arrows between the columns don't need to be there.
- 왜 이렇게: "있을 필요가 없다"는 `don't need to be there` 가 그대로 통합니다. 더 짧게는 `We can lose the arrows.`(구어)

### 카드 21 — 같은 내용 반영   (내가 쓴 한글)
- 내가 쓴 한글: "상반기 월별 계획도 새 목표 기준으로 고쳐줘. 전체적으로 다른 문서들에 변경된 proposal 기획안과 동일한 내용 반영"
- 자연스러운 영어: Update the first-half monthly plan to match the new goals too, and bring the other documents in line with the revised proposal.
- 왜 이렇게: "~기준으로 고치다"는 `update … to match`. "동일한 내용 반영"은 `bring … in line with` 가 정확한 관용구입니다.

### 카드 22 — 결정 직전 구분   (고급 한글 · 번역)
- 한글 원문: "B가 기존 C와 겹쳐서, C는 \"전체 동시 개발\"로 바꿔 구분했습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: Since B now overlapped with the old C, I redefined C as "full parallel development" to keep them distinct.
- 번역 포인트: "구분했다"는 결과를 목적으로 바꿔 `to keep them distinct` 로 옮깁니다. "겹치다"는 `overlap with`.

### 카드 23 — 근거도 된다   (고급 한글 · 번역)
- 한글 원문: "이 내용은 시사점 1(개발자와 현업 엔지니어 두 역할이 동시에 필요)의 근거도 됩니다."   (출처: transcript:[assistant])
- 자연스러운 영어: This also backs up lesson 1, that you need both a developer and a field engineer at the same time.
- 번역 포인트: "~의 근거가 되다"를 `be the basis of` 로 옮기면 딱딱합니다. 동사 `back up` 이 자연스럽고, 괄호 내용은 동격 `that` 절로 풀었습니다.

### 카드 24 — 기록이라서   (고급 한글 · 번역)
- 한글 원문: "보고용 문서가 아니고, 숫자의 출처를 남긴 기록이라서입니다."   (출처: transcript:[assistant])
- 자연스러운 영어: They aren't reporting documents; they're records of where the numbers came from.
- 번역 포인트: "~가 아니고 ~라서"는 `A, not B` 혹은 세미콜론 대비로 옮깁니다. "숫자의 출처"는 명사구 대신 `where the numbers came from` 간접의문절이 영어답습니다.

## 영어 다듬기

### 카드 1 — this contents
- 내가 쓴 영어: "update other files based on this newly updated contents."   (출처: transcript:[user])
- 정정: update the other files based on **this newly updated content** (또는 these updated contents). `this` 는 단수, `contents` 는 복수라 수가 맞지 않습니다. 추상적인 "내용"은 불가산 `content` 가 기본입니다.
- 더 나은 표현: Update the other files to match these changes.
- 왜: `based on` 보다 `to match` 가 "똑같이 맞춰라"는 의도를 바로 드러냅니다. `newly updated` 는 `updated` 와 겹쳐서 하나만 씁니다.

### 카드 2 — commit and push
- 내가 쓴 영어: "commit and push"   (출처: transcript:[user])
- 더 나은 표현: Commit and push when you're done.
- 왜: 문법은 맞습니다. `when you're done` 을 붙이면 순서가 분명해져 작업 도중에 끼어드는 지시로 오해받지 않습니다.

### 카드 3 — 한영 섞인 지시
- 내가 쓴 영어: "완성 후 republish and commit and push"   (출처: transcript:[user])
- 더 나은 표현: Once it's done, republish, then commit and push.
- 왜: 문법 오류는 없습니다. 다만 `and … and` 가 이어지면 단계가 흐려집니다. `Once it's done,` 으로 "완성 후"를 옮기고 `then` 으로 republish 와 커밋의 순서를 나눴습니다.
