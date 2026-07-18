# 2026-07-18 — 코칭

## 한글→영어

### 카드 1 — 산출물이 얇은 게 구조 탓인지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "최근 생성된 daily 자료들을 보면 내용이 적은 편인데, 구조상 어쩔 수 없는건가?"   (출처: transcript:[user] english-study/456b8bff)
- 자연스러운 영어: "The recent daily outputs look a bit thin — is that just inherent to how the pipeline works, or something we can tune?"
- 왜 이렇게: "내용이 적은 편"은 thin(얇다)이 딱 맞는 관용어이고, a bit 로 "~한 편"의 완화를 살립니다. "구조상 어쩔 수 없는가"는 inherent to X(X에 본래 내재된)가 핵심 — unavoidable 보다 원인을 구조에 귀속시키는 뉘앙스가 정확합니다. 뒤에 "or something we can tune?" 을 붙이면 진짜 묻고 싶은 것(조정 가능성)까지 한 번에 전달됩니다.

### 카드 2 — deferred 에서 코칭 재료를 끌어오자는 제안   (내가 쓴 한글)
- 내가 쓴 한글: "coaching 같은 경우는 문법적으로 개선이 필요하거나 어색한 문장을 고치는 경우가 많이 있을텐데, deferred에서 coaching 내용이 부족하거나 없으면 가져올 수 있는거 아닌가?"   (출처: transcript:[user] english-study/456b8bff)
- 자연스러운 영어: "Coaching is mostly about fixing grammar and awkward phrasing, so when the day's batch is short on coaching material, couldn't we just pull it from the deferred backlog?"
- 왜 이렇게: "~할텐데"의 추정 + "~아닌가?"의 제안형 질문은 영어에서 couldn't we just …? 로 한 번에 처리됩니다(부드러운 제안 + 당연하지 않냐는 뉘앙스). "부족하거나 없으면"은 is short on X 하나로 압축 — lacking or missing 처럼 둘 다 옮기면 번역투가 됩니다. deferred backlog 처럼 형용사를 명사에 붙여 대상을 명명하는 것도 영어식.

### 카드 3 — 스킬로 한글 다듬기 요청   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 한글 내용을 만들 때 내용이 어색하니까 skills 중에 humanize-korean:humanize 를 적용해서 한번 다듬어줘."   (출처: transcript:[user] english-study/456b8bff)
- 자연스러운 영어: "Also, the Korean output reads awkwardly — run it through the humanize-korean skill and polish it up."
- 왜 이렇게: "어색하다"를 is awkward 대신 **reads awkwardly**(읽어 보면 어색하다)로 쓰면 글 품질 얘기임이 분명해집니다. "적용해서 다듬다"는 run X through Y(Y에 X를 통과시키다)가 파이프라인 은유로 자연스럽고, polish up 이 "한번 다듬어줘"의 가벼운 완성 뉘앙스를 담습니다.

### 카드 4 — 수동 실행으로 검증 요청   (내가 쓴 한글)
- 내가 쓴 한글: "파이프라인 한번 수동으로 돌려서 coaching.md 나오는지 확인해줘"   (출처: transcript:[user] english-study/456b8bff)
- 자연스러운 영어: "Run the pipeline manually once and make sure coaching.md actually comes out."
- 왜 이렇게: "돌려서"는 run 이 정확한 동사(execute 는 과격식). "나오는지 확인"은 make sure X actually comes out — actually 가 "이번엔 진짜로 되는지"라는 검증 의도를 살립니다. verify that … is generated 로 쓰면 문어체 보고서가 되고, 채팅 지시로는 이 버전이 자연스럽습니다.

### 카드 5 — 원인 진단의 반전 구문   (고급 한글 · 번역)
- 한글 원문: "코칭 재료가 없어서 coaching.md가 빠진 게 아니라, 재료가 배치에 못 들어오고 있던 것입니다."   (출처: transcript:[assistant] english-study/456b8bff)
- 자연스러운 영어: "It's not that there was no coaching material — the material just wasn't making it into the batch."
- 번역 포인트: "~해서 …한 게 아니라"는 **It's not that A — B** 구문이 정석입니다(통념을 부정하고 진짜 원인을 제시). "못 들어오고 있던"의 진행상은 wasn't making it into 로 — make it into X(간신히 X에 들어가다)가 "경쟁에서 밀려 못 들어간다"는 함의까지 운반합니다.

### 카드 6 — 기아(starvation) 구조 설명   (고급 한글 · 번역)
- 한글 원문: "트랜스크립트는 offset 기반이라 deferred 되어도 유실되진 않지만, 매일 새 문서가 갱신되는 한 계속 우선순위에서 밀리는 기아(starvation) 구조입니다."   (출처: transcript:[assistant] english-study/456b8bff)
- 자연스러운 영어: "Transcripts are offset-based, so deferring them loses nothing — but as long as fresh documents keep arriving every day, they get starved out of the queue indefinitely."
- 번역 포인트: "~하는 한"은 **as long as** 절. "우선순위에서 밀리는 기아 구조"는 명사구를 그대로 옮기지 말고 get starved out of the queue 라는 동사구로 풀어야 영어답습니다(구조입니다 → 동사로 사건화). indefinitely 가 "계속"의 열린 지속을 담당합니다.

### 카드 7 — 변곡점 진단   (고급 한글 · 번역)
- 한글 원문: "얇아진 진짜 변곡점은 소스 구성 변화입니다."   (출처: transcript:[assistant] english-study/456b8bff)
- 자연스러운 영어: "The real inflection point was the shift in source mix."
- 번역 포인트: "변곡점"은 inflection point 가 비즈니스 영어에서도 그대로 쓰이는 차용어. "소스 구성 변화"는 change in source composition 보다 **shift in source mix** 가 훨씬 관용적입니다 — mix 는 구성 비율, shift 는 점진적이지만 방향 있는 이동을 함의합니다.

## 영어 다듬기

### 카드 1 — 유튜브 채널 감시 요청
- 내가 쓴 영어: "can you take a look at a certain youtube channel, if there's new video uploaded, can you take a look at the video and summarize, get the trascript and get the contents and make them into a md file?"   (출처: transcript:[user] english-study/1c9dfebc)
- 정정: "if there's **a** new video uploaded" — video 는 가산명사라 관사 필요. "trascript" → "transcript" (철자). 한 문장에 의문문이 두 번(can you …, can you …) 겹친 run-on 구조는 하나로 합쳐야 합니다.
- 더 나은 표현: "Could you watch a YouTube channel and, whenever a new video is uploaded, summarize it, pull the transcript, and turn the whole thing into a markdown file?"
- 왜: watch 한 단어가 "지켜보다가 새 게 올라오면"의 감시 의미를 담아 조건절 부담을 줄입니다. take a look at 이 두 번 반복되면 장황해지므로 각 동작을 서로 다른 동사(summarize, pull, turn into)로 배분 — 영어는 나열에서 동사 다양성이 세련됨을 만듭니다. get the contents 는 정보가 없어 삭제.

### 카드 2 — 트랜스크립트 문법 정제 + 스킬화 요청
- 내가 쓴 영어: "great. I want you to make this into a skill. For the transcript, make sentences gramatically correct and full sentences. make the skill and let's do the job for the link https://youtu.be/9fubhllmsBU"   (출처: transcript:[user] english-study/1c9dfebc)
- 정정: "gramatically" → "grammatically" (m 하나, l 두 개 아님 — grammar + -tically). "make sentences grammatically correct and full sentences" 는 make X correct 와 make X full sentences 두 구문이 충돌 — "rewrite them into complete, grammatical sentences" 처럼 한 동사로 통일해야 합니다.
- 더 나은 표현: "Great — let's turn this into a skill. For the transcript, rewrite it into complete, grammatical sentences. Once the skill is ready, run it on this link: https://youtu.be/9fubhllmsBU"
- 왜: turn X into Y 가 make X into Y 보다 자연스러운 변환 동사입니다. "make the skill and let's do the job" 은 명령과 청유가 섞여 어색 — Once the skill is ready, run it on … 으로 순서 관계를 명시하면 지시가 깔끔해집니다. do the job for the link 는 영어에서 의미가 모호합니다(run it on this link 가 도구를 대상에 적용하는 표준 표현).

### 카드 3 — 커밋 지시
- 내가 쓴 영어: "commit and push" / "commit all and push"   (출처: transcript:[user] english-study/1c9dfebc, skewnono/b6191cae)
- 더 나은 표현: "Commit everything and push to main." / 선별이 필요하면 "Commit just the digest files and push."
- 왜: 문법 오류는 없고 지시로 충분히 통합니다. 다만 all 은 "지금 워킹트리의 전부"라는 범위가 암묵적이라, everything 뒤에 to main 같은 목적지나 just the digest files 같은 한정을 붙이는 습관을 들이면 에이전트·동료 누구에게든 오해 여지가 줄어듭니다.
