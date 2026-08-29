# 2026-08-30 — 코칭

## 한글→영어

### 카드 1 — wayfinder 재개 요청   (내가 쓴 한글)
- 내가 쓴 한글: "wayfinder로 진행 중이였어. 마무리 안한 영역을 진행하자"   (출처: transcript:[user] auto-recipe-creator/f914191d-1bfd-46dc-ae6a-2b96a31bb08e.jsonl)
- 자연스러운 영어: "I was in the middle of working through this with wayfinder — let's pick up the parts we didn't finish."
- 왜 이렇게: "진행 중이였다"는 과거진행형이므로 "was in the middle of -ing"가 대응한다. "마무리 안한 영역"은 명사구보다 "the parts we didn't finish"처럼 절로 풀면 더 자연스럽다. "진행하자"는 청유형이라 "let's pick up"으로 시작하면 대화체 톤이 그대로 산다.

### 카드 2 — 반영 지시   (내가 쓴 한글)
- 내가 쓴 한글: "스펙에 반영해주세요"   (출처: transcript:[user] auto-recipe-creator/1e403abe-517b-4bd4-b5dd-25a03345e39c.jsonl)
- 자연스러운 영어: "Go ahead and fold these into the spec."
- 왜 이렇게: "반영하다"는 여기서 "리뷰 결과를 문서에 적용하다"이므로 fold in / incorporate 가 알맞다. "-해주세요"의 정중한 요청 뉘앙스는 "Go ahead and ..."로 담아, 이미 논의된 걸 실행에 옮기라는 승인의 느낌을 살린다.

### 카드 3 — 기본값 지시   (내가 쓴 한글)
- 내가 쓴 한글: "search_mode grid (신규)를 기본값으로 정해줘"   (출처: transcript:[user] auto-recipe-creator/d9f5b773-1425-4d4d-acd4-c00db5a3d2dc.jsonl)
- 자연스러운 영어: "Make grid the new default for search_mode."
- 왜 이렇게: "A를 B로 정하다"는 "make A B" 5형식 구문과 정확히 대응한다. "(신규)"라는 부연은 명사 앞에 형용사 new를 붙이는 것만으로 자연스럽게 흡수된다.

### 카드 4 — 짧은 승인   (내가 쓴 한글)
- 내가 쓴 한글: "배율 변경 금지 가능."   (출처: transcript:[user] auto-recipe-creator/d9f5b773-1425-4d4d-acd4-c00db5a3d2dc.jsonl)
- 자연스러운 영어: "Blocking magnification changes works for me."
- 왜 이렇게: 원문은 주어 없이 "(그렇게 하는 것이) 가능하다"는 승인만 전한다. 영어는 주어가 필요하므로 동명사구 "Blocking magnification changes"를 주어로 세우고 "works for me"로 캐주얼하게 동의를 표현하면 자연스럽다. 격식체라면 "That's acceptable" 정도가 대응한다.

### 카드 5 — 스펙 리뷰 한 줄 판정   (고급 한글 · 번역)
- 한글 원문: "한 줄 판정: map.md 의 9개 결정을 빠짐없이 옮겼고 불변식(unknown≠wildcard, terminal≠Outcome, 의존 방향, 새 dependency 0)도 지켰다. 다만 코드 seam 과 대조하면 to-tickets 전에 결정해야 할 구멍 5개와 엔진 계약 오해 2개가 있고, 8 increment 를 synthetic fixture 위에서 6개까지 쌓는 롤아웃 순서는 이 저장소가 이미 한 번 데인 방식이다."   (출처: transcript:[assistant] auto-recipe-creator/1e403abe-517b-4bd4-b5dd-25a03345e39c.jsonl)
- 자연스러운 영어: "One-line verdict: the spec carries over all nine decisions from map.md without dropping any, and it holds every invariant — unknown isn't a wildcard, terminals aren't outcomes, the dependency direction stays fixed, zero new dependencies. Set against the actual code seams, though, it leaves five gaps that need deciding before to-tickets and two places where it misreads the engine's contract, and stacking six of the eight increments on synthetic fixtures is a rollout order this repo has already been burned by once."
- 번역 포인트: "빠짐없이"는 "without dropping any"처럼 부정+명사로 풀면 자연스럽다. "불변식을 지켰다"의 목적어 나열은 영어에서 대시(—)로 늘어놓는 편이 자연스럽다. "이미 한 번 데인 방식이다"는 뼈아픈 실패를 겪었다는 관용구라 "has already been burned by X"로 옮기면 원문의 냉소적 톤이 그대로 산다.

### 카드 6 — 세 디베이트에서 반복된 순환 오류   (고급 한글 · 번역)
- 한글 원문: "세 디베이트(heavy, glm-5.3)에서 제 처음 입장이 매번 무너진 지점은 같은 종류였습니다: '실행 기록을 근거로 승격한다'는 순환 — replay 가 rule 을 만든 정규화기와 같은 편향을 재현하고, shadow 의 verify 가 엔지니어의 성공을 rule 에 귀속시키고, 분류기가 Outcome 을 kind 에 부호화해 인과를 날조하는 식이었습니다."   (출처: transcript:[assistant] auto-recipe-creator/f914191d-1bfd-46dc-ae6a-2b96a31bb08e.jsonl)
- 자연스러운 영어: "Across all three debates (heavy, glm-5.3), my opening position broke down at the same kind of point every time: the circularity of 'promoting something on the strength of its own execution record' — replay reproducing the same bias as the normalizer that built the rule, shadow's verify attributing the engineer's success to the rule, the classifier encoding outcome into the action kind and fabricating causation."
- 번역 포인트: "무너진 지점"은 "broke down at the point"처럼 동사+전치사구로 옮기면 자연스럽다. 콜론 뒤 나열된 세 사례는 병렬 분사구문(-ing)으로 이어야 원문처럼 같은 문법 구조가 반복되는 리듬이 산다. "인과를 날조하다"는 "fabricate causation"으로 직역해도 통하는 학술적 표현이다.

### 카드 7 — 3층 설정과 기본값   (고급 한글 · 번역)
- 한글 원문: "이 저장소의 설정은 3층(config.py 스키마 → env → workflow_3_config.py 파일 상수)이라 '기본값을 정한다'는 것이 코드 한 줄이 아니라 세 층이 같은 답을 하는지의 문제입니다."   (출처: transcript:[assistant] auto-recipe-creator/d9f5b773-1425-4d4d-acd4-c00db5a3d2dc.jsonl)
- 자연스러운 영어: "Configuration in this repo runs three layers deep — the config.py schema, then env, then the file constants in workflow_3_config.py — so 'setting the default' isn't a one-line code change; it's a question of whether all three layers agree."
- 번역 포인트: "3층이라 ~다"는 이유절이므로 "so"로 자연스럽게 이어진다. "코드 한 줄이 아니라"는 부정 대구이므로 "isn't X; it's Y" 구조로 영어의 대표적 대조 표현을 살렸다. 화살표(→)로 나열된 세 층은 영어에서는 "then"으로 잇는 편이 자연스럽다.

## 영어 다듬기

### 카드 1 — 리뷰 게이트 활성화 지시
- 내가 쓴 영어: "enable the review gate"   (출처: transcript:[user] skewnono-v3-nuxt/df74b5af-62cf-4b5d-93f8-ca9965748f15.jsonl)
- 정정: (문법 오류 없음)
- 더 나은 표현: "Go ahead and enable the review gate." 또는 정중히 물을 때는 "Could you enable the review gate?"
- 왜: 명령문 자체는 정확하지만 주어 없는 완전한 명령형은 다소 사무적으로 들린다. "Go ahead and ..."를 붙이면 이미 논의된 조치를 실행하라는 승인의 뉘앙스가 더해지고, 의문형으로 바꾸면 동료에게 요청하는 정중한 톤이 된다.
