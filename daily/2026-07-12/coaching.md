# 2026-07-12 — 코칭

오늘 배치에는 내가 쓴 한국어(및 어시스턴트의 한국어 산문)가 없어 한글→영어 섹션은 생략합니다.
recording_filter 설계 대화에서 내가 직접 쓴 영어 5건을 다듬었습니다.

## 영어 다듬기

### 카드 1 — 녹화 후 필터 질문
- 내가 쓴 영어: "we record tool monitor via screenshot. after recording done, we have to filter unnecesary images. what file can I use it? in workflow_3"   (출처: transcript:[user] 686f8e5b…)
- 정정: ① unnecesary → **unnecessary** (철자). ② "after recording done" → **after the recording is done** — 접속사 뒤 절에는 주어+be동사가 필요합니다(분사구문 "after recording"도 가능). ③ "what file can I use it?" → **which file can I use for it?** — what file이 이미 use의 목적어이므로 it을 또 두면 목적어가 중복됩니다.
- 더 나은 표현: "We record the tool monitor with screenshots. Once a recording finishes, we need to filter out the unnecessary images — which file in workflow_3 should I use for that?"
- 왜: 불필요한 것을 걸러 '내는' 것이므로 구동사 **filter out**이 정확하고, 한정된 후보 중에서 고르는 질문은 what보다 **which**가 자연스럽습니다. "Once a recording finishes"는 "after ~ done"보다 한 단계 매끄러운 시간절입니다.

### 카드 2 — 필터 이동 + 새 폴더 제안
- 내가 쓴 영어: "move the two filtering method from workflow_1/workflow_2 to workflow_3. maybe we need new folder \"recording_filter\" in workflow_3 to manage this filter methods well."   (출처: transcript:[user] 686f8e5b…)
- 정정: ① "the two filtering method" → **the two filtering methods** (two 뒤 복수). ② "need new folder" → **need a new folder** (가산 단수엔 관사). ③ "this filter methods" → **these filter methods** (지시사도 수 일치).
- 더 나은 표현: "Move the two filtering methods from workflow_1/workflow_2 into workflow_3 — maybe under a new `recording_filter` folder so they're easier to manage."
- 왜: 이동의 도착점이 '안'이면 to보다 **into**가 그림이 선명하고, 폴더 '아래' 배치는 **under**가 관용적입니다. "to manage X well"은 **so they're easier to manage**로 바꾸면 목적이 아니라 효과로 읽혀 더 자연스럽습니다.

### 카드 3 — VLM으로 마우스·타이핑 추적 계획
- 내가 쓴 영어: "anyways, we need to filter images into smaller number of images, and use vlm to track down on mouse movements and key typings. those info will be used to establish the workflows for certain situation"   (출처: transcript:[user] 686f8e5b…)
- 정정: ① anyways → **anyway** (anyways는 비표준·아주 캐주얼). ② "into smaller number" → **into a smaller number** (관사). ③ "track down on" → **track** — track down은 "추적 끝에 찾아내다"(범인·파일 등)이고 전치사 on을 받지 않습니다. 지속적인 추적·기록은 그냥 track/trace. ④ "key typings" → **keystrokes** (키 입력의 표준 명사). ⑤ "those info" → **that information** (information은 불가산). ⑥ "for certain situation" → **for certain situations** (복수).
- 더 나은 표현: "Anyway, the goal is to cut the recording down to a much smaller set of frames, then use a VLM to track mouse movements and keystrokes. That information will feed into building workflows for specific situations — align-fail first, more to come."
- 왜: "filter images into smaller number of images"의 명사 반복은 **cut ~ down to a smaller set**으로 압축됩니다. "will be used to establish"은 **will feed into building**처럼 살아 있는 동사로 바꾸면 보고서 어투를 벗습니다.

### 카드 4 — 계획 보관 지시
- 내가 쓴 영어: "keep the plan in @poc/workflow_3/docs/superpowers/ I will work on it later on"   (출처: transcript:[user] 686f8e5b…)
- 더 나은 표현: "Keep the plan under poc/workflow_3/docs/superpowers/ — I'll pick it up later."
- 왜: 문법 오류는 없습니다(later on도 표준). 다만 디렉터리 '아래'는 **under**가 관용적이고, "나중에 이어서 하겠다"는 **pick it up later**가 가장 자연스러운 구어입니다. 채팅에서는 I will보다 **I'll** 축약이 온도에 맞습니다.

### 카드 5 — 섹션 승인
- 내가 쓴 영어: "looks right, show section 2"   (출처: transcript:[user] 686f8e5b…)
- 더 나은 표현: "Looks good — go ahead with Section 2."
- 왜: 오류는 없습니다. 승인 후 진행을 지시하는 표준 콜로케이션은 **Looks good — go ahead with ~**입니다. right는 "정확하다"에, good은 "이대로 진행해도 좋다"에 무게가 실려, 설계 검토의 응답으로는 good 쪽이 살짝 더 자연스럽습니다. "show me Section 2"처럼 me를 넣으면 어조가 부드러워집니다.
