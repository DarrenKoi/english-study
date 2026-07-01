# 2026-07-02 — 코칭

## 한글→영어

### 카드 1 — 오피스엔 Claude가 없다   (내가 쓴 한글)
- 내가 쓴 한글: "명심해야 할 점은 hermes agent는 office에서 사용할 예정이고, office에서는 claude model을 사용할 수 없어. claude code와 hermes agent 차이점을 알고 싶어. claude code에서 안 되는 게 hermes agent로는 구현이 되는 경우를 알고 싶어."   (출처: transcript:[user] 30ee7e8f…)
- 자연스러운 영어: "One thing to keep in mind: Hermes Agent will be used at the office, and the office has no access to Claude models. I want to understand how Claude Code and Hermes Agent differ — specifically, the cases that Claude Code can't do but Hermes can."
- 왜 이렇게: "명심해야 할 점은"은 통째로 "One thing to keep in mind:"로 콜론 처리하면 자연스럽다("The point to remember is that…"은 딱딱). "사용할 수 없어"는 "can't use"보다 "has no access to"가 제약의 성격(권한·환경 부재)을 정확히 전한다. "안 되는 게 …로는 되는 경우"는 대비를 "the cases that X can't do but Y can"으로 관계절 두 개를 하나로 묶어 압축한다.

### 카드 2 — 이거 우리가 한 거랑 같지 않아?   (내가 쓴 한글)
- 내가 쓴 한글: "이거 우리가 했던 테스트랑 다른 거야? 비슷한 것 같은데 확인해 줘."   (출처: transcript:[user] 3b7f08e4…)
- 자연스러운 영어: "Is this actually different from the test we already ran? It looks like the same thing to me — can you double-check?"
- 왜 이렇게: 의심을 담을 땐 "actually"를 넣어 "정말 다른 거 맞아?"의 뉘앙스를 살린다. "비슷한 것 같은데"는 "It looks like the same thing to me"로 *내 판단*임을 to me로 표시. "확인해 줘"는 단순 check보다 "double-check"가 "다시 한 번 대조해 봐"의 의도에 맞는다.

### 카드 3 — 하나만 남기고 나머지 정리   (내가 쓴 한글)
- 내가 쓴 한글: "edge_ncc만 남기고 cond_box 중복분 정리해 줘. 그리고 추가로 더 해볼 수 있는 방법론이 있는지 더 찾아 줘."   (출처: transcript:[user] 3b7f08e4…)
- 자연스러운 영어: "Keep only edge_ncc and strip out the duplicate cond_box work. Also, dig around for any other approaches we could still try."
- 왜 이렇게: "A만 남기고 B 정리"는 "Keep only A and strip out B"가 관용적. "중복분"은 "the duplicate work/parts". "더 찾아 줘"는 "dig around for"(탐색·발굴 뉘앙스)가 "find more"보다 능동적이고 자연스럽다. "더 해볼 수 있는"은 "we could still try"로 여지가 남았음을 still로 표현.

### 카드 4 — 커맨드 정리해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "office에서 golden 돌릴 커맨드 정리해 줘."   (출처: transcript:[user] 3b7f08e4…)
- 자연스러운 영어: "Can you write up the commands for running the golden eval at the office?"
- 왜 이렇게: "정리해 줘"는 맥락상 "깔끔하게 적어 달라"이므로 "write up"(문서로 말끔히 정리)이 가장 맞는다. 그냥 "organize"는 이미 있는 걸 재배열하는 뉘앙스라 약간 어긋난다. "golden 돌릴"은 "for running the golden eval"처럼 목적을 for + 동명사로.

### 카드 5 — env 진짜 싫어   (내가 쓴 한글)
- 내가 쓴 한글: "나는 env를 사용하는 것을 정말 싫어해."   (출처: transcript:[user] 3b7f08e4…)
- 자연스러운 영어: "I really can't stand using env vars."
- 왜 이렇게: 강한 혐오의 구어체는 "hate"도 되지만 "can't stand"가 생생하다. 격식을 조금 올리면 "I have a strong aversion to using env vars." 대상은 "env"만 쓰기보다 "env vars(environment variables)"로 명시하는 게 영어에선 자연스럽다.

### 카드 6 — 이미 해결돼 있다   (고급 한글 · 번역)
- 한글 원문: "consensus는 '현재 외형 추종'이 존재 이유라, all-time이 아니라 최근 N장이어야 드리프트를 따라감."   (출처: transcript:[assistant] 3b7f08e4…)
- 자연스러운 영어: "Consensus exists to track the current appearance, so it has to be built from the most recent N frames, not the all-time set — otherwise it can't follow the drift."
- 번역 포인트: "존재 이유라"는 "exists to (do)"로 목적을 부정사에 실으면 "the reason it exists is…"보다 간결하다. "최근 N장이어야"의 당위는 "has to be built from"으로. 한국어가 생략한 인과("따라감")를 영어에선 "otherwise it can't follow the drift"로 *반사실 조건*을 붙여 논리를 드러내는 게 자연스럽다.

### 카드 7 — 단계 최적화 말고 전체 최적화   (고급 한글 · 번역)
- 한글 원문: "개별 단계 최적화 그만하고 end-to-end 라우팅을 최적화하는 거."   (출처: transcript:[assistant] 3b7f08e4…)
- 자연스러운 영어: "Stop optimizing the individual stages and optimize the end-to-end routing instead."
- 번역 포인트: "그만하고 …하는 거"의 명사형 종결은 영어에선 명령형 "Stop A and B (instead)"로 옮기면 힘이 산다. 대비를 못 박는 "instead"를 문미에 두는 게 구어 리듬. "개별 단계"는 "the individual stages", "전체"는 하이픈 형용사 "end-to-end".

### 카드 8 — 최악의 실패도 안전   (고급 한글 · 번역)
- 한글 원문: "최악의 실패는 '브리핑이 틀리거나 안 온다'뿐이라, 사람이 원본 digest로 즉시 대조할 수 있다."   (출처: transcript:[assistant] 30ee7e8f…, 시나리오 리스크 요약)
- 자연스러운 영어: "The worst-case failure is just 'the briefing is wrong or doesn't arrive,' which a human can immediately cross-check against the original digest."
- 번역 포인트: "…뿐이라"의 한정은 "is just …"로 축소한다. "대조하다"는 "cross-check against"가 정석(compare보다 대조·검증 뉘앙스). 뒷절은 비제한 관계절 "which a human can cross-check"로 앞 상황에 안전장치를 덧붙인다.

## 영어 다듬기

### 카드 1 — 벤치 결과를 다 타이핑하기 싫다
- 내가 쓴 영어: "After run the code, we see the result in the console. I have been giving you the result by typing here. I want to give you the simple info as much as possible. it is hard to typing benchmark result all."   (출처: transcript:[user] 3b7f08e4…)
- 정정:
  - "After run the code" → "After I run the code" 또는 "After running the code". 전치사 after 뒤 동사는 동명사(-ing)이거나 절(주어+동사)이어야 한다. run 원형 단독은 비문.
  - "it is hard to typing" → "it is hard to type". 「it is + 형용사 + to부정사」구문이라 to 뒤는 원형(type).
  - "typing benchmark result all" → "type out all the benchmark results". all은 명사 앞(all the results)으로, result는 복수 results로.
  - 소문자 문두 "it" → "It" (문장 첫 글자 대문자).
- 더 나은 표현: "After I run the code, the results show up in the console, and so far I've been retyping them to you by hand. I'd like to hand them over with as little typing as possible — typing out the whole benchmark result every time is a pain."
- 왜: "we see the result"의 막연한 we보다 결과가 "show up in the console"처럼 주어가 결과 자체이면 더 자연스럽다. "by typing here"는 "retyping them by hand"로 *반복 수작업*의 불편을 드러낸다. "simple info as much as possible"는 콩글리시에 가까워 "with as little typing as possible"로 의도(입력을 최소화)를 직접 표현했다. "it is hard … all"의 투박함은 구어 관용 "is a pain"으로 자연스럽게.
