# 2026-07-28 — 코칭

## 한글→영어

### 카드 1 — 실측 기반으로 이미 배분해 뒀다   (내가 쓴 한글)
- 내가 쓴 한글: "나는 내가 적정 수준으로 잡들을 배분해놓은 상태야. 각자 finish 하는데 걸리는 시간을 dashboard 통해서 알고 있어서 배분해놓았어."   (출처: transcript:[user] flask-modules)
- 자연스러운 영어: "I've already spread the jobs out at a reasonable level. I know from the dashboard how long each one takes to finish, so I placed them based on that."
- 왜 이렇게: "~해놓은 상태야"는 결과 상태의 지속이므로 현재완료 "I've already spread ... out"이 정확히 맞는다. "배분하다"를 distribute로 옮기면 자원 분배처럼 들린다 — 시각을 벌려 놓는 맥락이니 spread out(또는 stagger)이 맞는 동사. "dashboard 통해서 알고 있어서"는 "~를 통해" 직역(through the dashboard) 대신 know from the dashboard가 자연스럽다.

### 카드 2 — 새로 시작해도 좋아   (내가 쓴 한글)
- 내가 쓴 한글: "lock_db 제거 하고 새로 시작해도 좋아. 문제 없어. 이동하는게 더 어려울 것 같아"   (출처: transcript:[user] flask-modules)
- 자연스러운 영어: "I'm fine with removing lock_db and starting fresh. No problem — moving the data over would probably be harder."
- 왜 이렇게: 허락의 "~해도 좋아"는 It's okay to보다 I'm fine with -ing가 화자의 결정임을 드러내 자연스럽다. "새로 시작"은 start fresh가 관용구(start newly는 없는 표현). "~것 같아"의 추측은 가정 상황이므로 would probably be — 실제로 안 할 일에 대한 판단이라 will이 아니다.

### 카드 3 — grep 결과 보고   (내가 쓴 한글)
- 내가 쓴 한글: "was missed by 검색 되지 않아" / "Running job 잘 나와." / "maximum number of 안나와"   (출처: transcript:[user] flask-modules)
- 자연스러운 영어: "'was missed by' doesn't turn up." / "'Running job' shows up fine." / "No hits for 'maximum number of'."
- 왜 이렇게: 검색 결과 보고의 3종 세트다 — 안 나오면 doesn't turn up 또는 no hits/no matches, 잘 나오면 shows up fine. "검색되지 않아"를 is not searched로 직역하면 "검색을 안 했다"는 뜻이 되어 버린다. 검색은 했고 결과가 없는 것이니 주어를 검색어로 세워 turn up을 쓴다.

### 카드 4 — 배포하고 지켜볼게   (내가 쓴 한글)
- 내가 쓴 한글: "배포하고 lock held 뜨는지 봐볼게"   (출처: transcript:[user] flask-modules)
- 자연스러운 영어: "I'll deploy it and see if 'lock held' shows up."
- 왜 이렇게: "뜨다"(화면에 나타나다)는 show up 또는 appear — pop up은 팝업창 어감이라 로그 행에는 과하다. "~는지 봐볼게"는 see if 절 하나로 끝난다. try to see는 한국어 "봐볼게"의 이중 시도를 그대로 옮긴 군더더기.

### 카드 5 — 부재의 증명   (고급 한글 · 번역)
- 한글 원문: "'안 나옴'만으로는 '안 일어남'을 증명하지 못합니다."   (출처: transcript:[assistant] flask-modules)
- 자연스러운 영어: "'Not showing up' alone doesn't prove 'not happening.'"
- 번역 포인트: 한국어가 명사화한 두 짝("안 나옴"/"안 일어남")을 영어도 동명사구 인용으로 그대로 살리면 대구가 유지된다. 격식을 올리면 "Absence from the log is not evidence of absence" — 영어 관용구 "absence of evidence is not evidence of absence"에 기대는 번역으로, 아는 사람에게는 이쪽이 더 강하게 꽂힌다.

### 카드 6 — 눈으로 안 잡히는 충돌   (고급 한글 · 번역)
- 한글 원문: "소요 시간을 다 알아도 눈으로는 안 잡히는 게 하나 있습니다 — 주기가 다른 잡들끼리의 정확한 시각 충돌입니다."   (출처: transcript:[assistant] flask-modules)
- 자연스러운 영어: "Even with every job's duration known, one thing escapes the eye: exact-time collisions between jobs on different periods."
- 번역 포인트: "~해도"의 양보를 even with + 명사구로 압축하면 even if절보다 문어답다. "눈으로는 안 잡히는"은 escapes the eye / the eye can't catch — invisible보다 "볼 수는 있는데 놓친다"는 뉘앙스가 산다. 대시로 뒤에 정체를 밝히는 구조는 영어도 콜론·대시로 그대로 가져갈 수 있다.

### 카드 7 — 균등 분할이 흉내낼 수 없는 정보   (고급 한글 · 번역)
- 한글 원문: "대시보드에서 각 잡의 실제 완료 시간을 보고 배분하셨다면 그건 균등 분할이 흉내낼 수 없는 정보로 배치하신 겁니다."   (출처: transcript:[assistant] flask-modules)
- 자연스러운 영어: "If you placed the jobs by their actual completion times from the dashboard, you scheduled them with information that even division can't imitate."
- 번역 포인트: "~하신 겁니다"의 존대 강조는 영어에 등가가 없으니 평서문으로 두고, 대신 정보 구조(그 정보 = 균등 분할이 못 가진 것)를 관계절 "that even division can't imitate"로 살린다. "보고 배분하셨다면"은 based on보다 by가 간결하다.

## 영어 다듬기

### 카드 1 — 언제 lock held가 뜨나
- 내가 쓴 영어: "In what cases, do we get the lock held in Detail in the dashboard? I have set lock_ttl shorter than cron job intervals"   (출처: transcript:[user] flask-modules)
- 정정: "In what cases," 뒤의 쉼표 삭제 — 의문사구가 문두에 와도 도치된 의문문과는 쉼표로 끊지 않는다: "In what cases do we get ..."
- 더 나은 표현: "Under what circumstances does the Detail column show 'lock held'? I've set lock_ttl shorter than the cron intervals."
- 왜: in Detail은 "자세히"라는 부사구로 읽혀 버린다 — 대시보드의 컬럼명이니 the Detail column을 주어로 세우면 오독이 사라진다. Under what circumstances는 in what cases의 격식 한 단계 위 판.

### 카드 2 — 목 잡은 mock을 실제 잡으로
- 내가 쓴 영어: "the code here task1, task2 is mock code. In my office, I have filled them with my own tasks. guide me how to fix it"   (출처: transcript:[user] flask-modules)
- 정정: "guide me how to fix it" → "guide me on how to fix it" 또는 "show me how to fix it" — guide는 「guide + 사람 + how절」을 직접 받지 못한다.
- 더 나은 표현: "task1 and task2 here are just mocks — at the office I've filled them in with my real tasks. Walk me through the fix."
- 왜: "the code here task1, task2 is"는 주어가 이중으로 겹친다 — task1 and task2를 바로 주어로 쓰면 단수/복수 문제(is→are)도 함께 풀린다. walk me through는 "단계별로 안내해 달라"는 요청의 관용구로, guide me보다 개발 대화에서 훨씬 흔하다.

### 카드 3 — lock_db가 관례인가
- 내가 쓴 영어: "the lock_db=1 not sure we can use this? I have always handle db=0 and not knowing about lock_db. in this conventionally used in anywhere? since I do not know about how redis is set in my company."   (출처: transcript:[user] flask-modules)
- 정정: ① "I have always handle" → "I have always handled" (현재완료는 과거분사). ② "and not knowing about" → "and don't know about" — 분사구는 앞 절과 병렬이 안 되니 정동사로. ③ "in this conventionally used in anywhere?" → "Is this conventionally used anywhere?" (의문문 도치 + anywhere 앞 in 불필요). ④ "how redis is set" → "how Redis is set up" (설정·구축은 set up).
- 더 나은 표현: "About lock_db=1 — I'm not sure we can use it. I've only ever worked with db=0 and hadn't heard of lock_db. Is that a common convention anywhere? I don't actually know how Redis is set up at my company."
- 왜: 화제를 먼저 던질 때는 "About X —"로 열면 조각문이 자연스러워진다. "I've only ever worked with db=0"은 "db=0밖에 몰랐다"는 경험 한정을 only ever로 압축한 것 — always handled보다 의도에 가깝다.

### 카드 4 — 참고용 케이스를 만들어 달라
- 내가 쓴 영어: "my jobs tend to be 5mins~20mins. so suggest various cases in the scheduler.py so that I can take a look at. although they are mock, it will help me a lot."   (출처: transcript:[user] flask-modules)
- 정정: ① "so that I can take a look at" → "take a look" — at은 목적어가 뒤따를 때만 붙는다(관계절로 쓰려면 "cases that I can take a look at"). ② "although they are mock, it will help" → "although they are mocks, they will help" — mock을 서술 형용사로 단독으로 쓰기 어색하고, 대명사도 복수 일치.
- 더 나은 표현: "My jobs tend to run 5–20 minutes, so add a variety of example cases to scheduler.py for me to look over. Even though they're mocks, they'll help a lot."
- 왜: 시간 범위는 "5mins~20mins"의 물결표 대신 en-dash로 "5–20 minutes"가 영어 표기 관례. tend to be보다 tend to run이 소요 시간에는 생생하다. "for me to look over"는 so that절을 부정사구로 줄인 형태로 요청문을 가볍게 만든다.
