# 2026-07-14 — 코칭

## 한글→영어

### 카드 1 — "잘 모르니 설명 자료를 만들어줘"   (내가 쓴 한글)
- 내가 쓴 한글: "우리가 진행했던 평가 중, heatmap, rrf, baseline digest, template bank등의 개념을 내가 잘 모르니 그런 것들을 설명하는 자료를 만들어줘."   (출처: transcript:[user] auto_recipe_creator 8908e3ed…)
- 자연스러운 영어: "I'm not too familiar with some of the concepts from the evaluations we ran — heatmap, RRF, baseline digest, template bank — so put together a doc that explains them."
- 왜 이렇게: ① "내가 잘 모르니"는 I don't know well 보다 **I'm not (too) familiar with** 가 자연스럽습니다 — '지식이 얕다'는 상태 표현. ② 이유를 앞세우는 한국어 어순은 영어에서 진술 + **so** 명령으로 잇는 편이 매끄럽습니다(Since I'm not familiar…, could you…도 가능). ③ 열거는 문장 중간에 **대시(—)로 삽입**하면 "등의 개념"의 예시 나열이 깔끔하게 처리됩니다. ④ "자료"는 여기선 학습용 문서이므로 a doc / a write-up / an explainer — make material 은 어색합니다.

### 카드 2 — "통합하고 지워도 돼"   (내가 쓴 한글)
- 내가 쓴 한글: "24와 25를 통합하고 24는 지워도 돼"   (출처: transcript:[user] auto_recipe_creator 8908e3ed…)
- 자연스러운 영어: "Merge 24 into 25 — and feel free to delete 24 afterwards."
- 왜 이렇게: ① "통합하다"는 문서 두 개를 합치는 상황이니 **merge** (consolidate 는 더 격식·거창). 방향이 있으면 **merge A into B** 로 못 박는 게 영어답습니다. ② "~해도 돼"(허락·양보)는 **feel free to** 또는 you can go ahead and — it's okay to delete 보다 지시문 안에서 자연스럽습니다. ③ 순서 관계는 afterwards 한 단어로 충분합니다.

### 카드 3 — 커밋 보류 보고   (고급 한글 · 번역)
- 한글 원문: "커밋은 따로 요청하지 않으셔서 working tree에만 반영해 뒀습니다. 커밋·푸시 원하시면 진행하겠습니다."   (출처: transcript:[assistant] auto_recipe_creator 8908e3ed…)
- 자연스러운 영어: "Since you didn't ask for a commit, I've left the changes in the working tree only. Happy to commit and push whenever you'd like."
- 번역 포인트: "-아/어 뒀습니다"(조치 후 상태 유지)는 **현재완료 I've left…** 가 정확히 대응합니다 — 과거에 해 두었고 그 상태가 지금도 유효. "원하시면 진행하겠습니다"는 If you want, I will… 보다 **Happy to … whenever you'd like** 가 공손하면서 능동적인 관용 제안입니다.

### 카드 4 — "독립적으로 같은 결론에 도달한 게 핵심 서사"   (고급 한글 · 번역)
- 한글 원문: "리포트의 두 갈래(재등록 Phase 2 + template-bank)가 독립적으로 같은 결론에 도달한 게 핵심 서사입니다."   (출처: transcript:[assistant] auto_recipe_creator 8908e3ed…)
- 자연스러운 영어: "The heart of the story is that the report's two threads — re-registration Phase 2 and the template bank — independently arrived at the same conclusion."
- 번역 포인트: 한국어의 "~한 **게** …입니다" 구조는 영어에서 **The heart/point of X is that-절**로 뒤집는 게 자연스럽습니다. "갈래"는 **thread**(또는 strand) — 서사가 여러 줄기로 갈라진다는 비유가 양쪽 언어에서 통합니다. "독립적으로"는 동사 앞 **independently** 로 붙여 '따로따로 검증했다'는 증거 가치를 살립니다.

### 카드 5 — "가장 비싸게 배운 규율"   (고급 한글 · 번역)
- 한글 원문: "in_topk vs rank-1 구분이 이번 주 가장 비싸게 배운 규율이라, 교육 자료·md·html·슬라이드 네 곳에 모두 강조해 넣었습니다."   (출처: transcript:[assistant] auto_recipe_creator 8908e3ed…)
- 자연스러운 영어: "The in_topk-versus-rank-1 distinction was this week's most expensive lesson, so I called it out in all four artifacts — the explainer, the markdown, the HTML, and the slides."
- 번역 포인트: "비싸게 배운 규율"은 **an expensive lesson** 또는 **a hard-won lesson** — 영어도 교훈을 비용 은유로 말합니다. "강조해 넣었다"는 highlight 도 되지만 **call it out**(짚어 드러내다)이 문서 여러 곳에 명시했다는 행위에 더 밀착합니다. "네 곳"은 in all four **artifacts/places** 로 받고 대시 뒤에 열거합니다.

## 영어 다듬기

### 카드 1 — "commit and push to the main"
- 내가 쓴 영어: "commit and push to the main"   (출처: transcript:[user] auto_recipe_creator 8908e3ed…)
- 정정: **the main → main.** 브랜치 이름(main, develop 등)은 고유명사처럼 관사 없이 씁니다. the 를 쓰려면 명사를 붙여 **the main branch** 로.
- 더 나은 표현: "Commit the changes and push to main."
- 왜: push to main / merge into main 이 굳은 관용 형태입니다. commit 에 목적어(the changes)를 넣으면 명령이 더 완결되고, 급할 땐 "Commit and push."만으로도 충분합니다.

### 카드 2 — "what do we have next thing to do?"
- 내가 쓴 영어: "based on workflow_2 or workflow_3, what do we have next thing to do? based on plans, specs and journals"   (출처: transcript:[user] auto_recipe_creator 8909999c…)
- 정정: "what do we have next thing to do"는 **what do we have to do next** 와 **what's the next thing to do** 두 구문이 섞인 비문입니다 — 둘 중 하나로 골라야 합니다.
- 더 나은 표현: "Looking at the plans, specs, and journals for workflow_2 and workflow_3 — what should we tackle next?"
- 왜: ① based on 이 문장 앞뒤로 두 번 흩어졌는데, **Looking at / Going by** 분사구 하나로 근거를 모아 주면 한 문장이 됩니다. ② "다음에 착수할 일"은 **tackle next** 가 가장 자연스러운 동사 선택이고, 더 짧게는 **"What's next for workflow_2 and workflow_3?"** 도 관용적입니다.
