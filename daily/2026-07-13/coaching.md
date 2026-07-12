# 2026-07-13 — 코칭

## 한글→영어

### 카드 1 — 캐시는 계속 갈아끼우나?   (내가 쓴 한글)
- 내가 쓴 한글: "cache에 특정 recipe에는 이미지가 다 채워져 있어도 시간이 지나면 새로운 이미지로 계속 교체하는건가?"   (출처: transcript:[user] 68f829b0…)
- 자연스러운 영어: "Even if a recipe's cache is already fully populated, does it keep replacing the images with newer ones over time?"
- 왜 이렇게: "다 채워져 있어도"는 even if + fully populated(캐시가 채워진 상태의 표준 어휘)로. "계속 교체하다"는 keep + -ing가 정확히 "시간이 지나며 반복"을 담습니다. 주어를 recipe's cache로 세우면 한국어의 이중 주제("cache에 특정 recipe에는")가 영어 한 주어로 깔끔히 접힙니다.

### 카드 2 — 주간 보고 요청   (내가 쓴 한글)
- 내가 쓴 한글: "weekly report 작성해야해. 우리가 workflow_3에서 했던 것들, 어디까지 진행되었는지 작성해줘"   (출처: transcript:[user] 6a5dc0b9…)
- 자연스러운 영어: "I need to write my weekly report. Write up what we've done in workflow_3 and where each item stands."
- 왜 이렇게: "작성해줘"에는 write up(흩어진 내용을 정리해 문서로 만들다)이 딱 맞습니다. "어디까지 진행되었는지"는 how far it has progressed보다 where each item stands가 보고서 어휘로 자연스럽고, 진행 중 작업엔 현재완료 what we've done이 정석입니다.

### 카드 3 — 날짜 폴더에 3형식으로   (내가 쓴 한글)
- 내가 쓴 한글: "workflow_3/docs/weekly_report 폴더에 오늘 날짜로 폴더를 만들어서 거기에 다 넣어줘. md, slide, html 형식으로"   (출처: transcript:[user] 6a5dc0b9…)
- 자연스러운 영어: "Create a folder named with today's date under workflow_3/docs/weekly_report and put everything there — in md, slide, and html formats."
- 왜 이렇게: "오늘 날짜로 폴더"는 a folder named with today's date(또는 a folder for today's date). 경로 "~폴더에"는 under가 디렉터리 계층을 정확히 표현합니다. 형식 나열은 문장 끝에 대시로 붙이면 한국어 어순 그대로의 후첨 리듬이 살아납니다.

### 카드 4 — marp → pptx 확인   (내가 쓴 한글)
- 내가 쓴 한글: "mac에서 marp를 실행해서 만들고 나서 pptx를 생성하면 되는거지?"   (출처: transcript:[user] 6a5dc0b9…)
- 자연스러운 영어: "So on the Mac, I just run Marp to build it and then generate the pptx from that, right?"
- 왜 이렇게: "~하면 되는거지?"는 So I just … , right?가 정확한 상당어 — just가 "그거면 충분"을, 꼬리 right?가 확인 요청을 맡습니다. "만들고 나서"는 and then; from that을 붙이면 "그 결과물로부터"라는 파이프라인 순서가 명시됩니다.

### 카드 5 — 교체는 의도된 동작   (고급 한글 · 번역)
- 한글 원문: "이 교체(누적 아님)는 의도된 동작입니다. consensus의 가치 자체가 'stale한 rcp key 대신 현재 공정 외형을 추종'하는 것이라, 오래된 S를 계속 쌓으면 우리가 고치려던 staleness가 되돌아옵니다."   (출처: transcript:[assistant] 68f829b0…)
- 자연스러운 영어: "This replacement (not accumulation) is intentional: the whole value of consensus is that it tracks the current process appearance instead of a stale rcp key, so piling up old S images would bring back the very staleness we set out to fix."
- 번역 포인트: "가치 자체가 ~하는 것이라"는 the whole value of X is that절로 — 명사절이 이유 역할을 하고 콜론이 "즉"을 대신합니다. "우리가 고치려던 바로 그"는 the very + 관계절 we set out to fix(set out to: 작정하고 착수하다)가 정확한 강조 짝. 가정적 결과 "쌓으면 되돌아온다"는 would bring back으로 가정법 처리.

### 카드 6 — frontmatter 디버깅 회고   (고급 한글 · 번역)
- 한글 원문: "처음 PPTX는 플로우차트가 평문으로 깨졌는데, 원인은 Marp frontmatter 위에 HTML 주석이 있어 style: 디렉티브가 통째로 무시된 것이었습니다."   (출처: transcript:[assistant] 6a5dc0b9…)
- 자연스러운 영어: "In the first PPTX the flowchart collapsed into plain text; the cause was an HTML comment sitting above the Marp frontmatter, which made the whole style: directive get silently ignored."
- 번역 포인트: "평문으로 깨졌다"는 collapse into plain text — 구조가 무너져 내리는 그림이 깨짐을 정확히 옮깁니다. "~가 있어 …된 것이었다"의 인과는 분사 sitting above + 비제한 관계절 which made …로 연결하면 한국어의 긴 원인절이 자연스러운 두 층으로 나뉩니다. "통째로"는 the whole + 명사.

### 카드 7 — 생성물은 커밋 제외   (고급 한글 · 번역)
- 한글 원문: "PPTX는 생성물(재생성 가능, 1.5MB 바이너리)이라 제외하고, 작성한 소스 3개(md/slides.md/html)만 커밋하겠습니다."   (출처: transcript:[assistant] 6a5dc0b9…)
- 자연스러운 영어: "I'll leave the PPTX out — it's a build artifact (regenerable, a 1.5 MB binary) — and commit only the three source files I wrote."
- 번역 포인트: "생성물"은 a build artifact가 정확한 업계 용어. "~이라 제외하고"는 leave out + 대시 삽입 이유가 구어체 보고에 자연스럽습니다. "작성한 소스 3개만"의 '만'은 only를 동사 뒤 목적어 앞(commit only the three…)에 두어 커밋 범위를 한정합니다.

## 영어 다듬기

### 카드 1 — 다운로드가 안 보인다
- 내가 쓴 영어: "when I run @…only_check.py I do not see the images are downloaded in align_consensus_cache and align_images (only captured images are seen). there must be issue in image_* py files and the only_check.py file. can you check they are well connected?"   (출처: transcript:[user] 68f829b0…)
- 정정: "I do not see the images are downloaded" → **I don't see the images being downloaded** (지각동사 see + 목적어 뒤에는 원형/분사 — that절 축약형 "see (that) the images are…"로 쓰려면 that을 살리는 게 안전). "there must be issue" → **there must be an issue** (가산명사 issue엔 관사 필수).
- 더 나은 표현: "When I run only_check.py, nothing lands in align_consensus_cache or align_images — only the captured images show up. There must be an issue in the image_* modules or only_check.py; can you check that they're wired up correctly?"
- 왜: "nothing lands in X"는 "다운로드된 게 안 보인다"를 결과 중심으로 뒤집은 원어민 리듬이고, 연결 상태 점검은 well connected보다 **wired up correctly**가 코드 문맥의 관용어입니다.

### 카드 2 — 어디서 다운로드하나?
- 내가 쓴 영어: "but while I running @…, it fails to download. office_rich_notify is not imported? how you're downloading images align_img_from_rcp and align_img_from_msr?"   (출처: transcript:[user] 8657d569…)
- 정정: "while I running" → **while I'm running** (진행형엔 be동사 필수). "how you're downloading …?" → **how are you downloading …?** (wh-의문문은 조동사 도치).
- 더 나은 표현: "But when I run only_check.py, the download never happens. Is office_rich_notify not getting imported? How do align_img_from_rcp and align_img_from_msr actually get downloaded?"
- 왜: 반복 현상엔 while보다 when + 단순현재가 맞고, "the download never happens"가 fails to download보다 "아예 안 일어난다"는 관찰을 정확히 전합니다. 마지막 질문은 행위자(당신)가 아니라 메커니즘이 궁금한 것이므로 **get downloaded** 수동 구문이 의도에 부합합니다.

### 카드 3 — 바로 쓰도록 설정돼 있나?
- 내가 쓴 영어: "Do we set to use align_consensus right away to get the right align point when align fail happens?"   (출처: transcript:[user] 68f829b0…)
- 정정: "Do we set to use" → **Are we set (up) to use** (be set (up) to: ~하도록 설정·준비돼 있다 — 상태이므로 be동사). "when align fail happens" → **when an align fail happens** 또는 **when alignment fails** (명사엔 관사, 또는 동사문으로).
- 더 나은 표현: "Are we already set up to use align_consensus for the align point when an align fail happens?"
- 왜: set up to가 "그렇게 구성돼 있다"는 시스템 상태를 묻는 표준 형태이고, already가 "지금 그런가?"라는 질문의 초점을 살립니다.

### 카드 4 — 그래도 consensus가 낫지 않았나?
- 내가 쓴 영어: "Still Consensus gave the better result for the align point correction? can we use them? I can collect more than 3 S images if the recipe ran recently."   (출처: transcript:[user] 68f829b0…)
- 정정: 평서문 어순 의문문 "Still Consensus gave …?"는 구어에선 통하지만 글에선 **Still, didn't consensus give better results …?** 처럼 도치(또는 부가의문)가 안전합니다. "can we use them?"의 them은 consensus(단수 개념)를 받으므로 **it**.
- 더 나은 표현: "Even so, consensus did give better align-point corrections, right? Can we actually use it? I can collect more than three S images as long as the recipe has run recently."
- 왜: Even so가 "그럼에도"의 논리 연결을 명시하고, did give가 "실제로 더 좋았잖아"라는 강조를 실어 줍니다. 조건 "최근에 돌았다면"은 시점 불특정 과거+현재 관련이므로 **has run** 현재완료 + as long as(조건 충족하는 한)가 자연스럽습니다.

### 카드 5 — 콘덴스 + 플로우차트 + 흰 배경
- 내가 쓴 영어: "like we did in weekly_report in workflow_2, can you make it more conden and progress with the flow chart? and use white background."   (출처: transcript:[user] 6a5dc0b9…)
- 정정: "conden" → **condensed** (형용사형). "use white background" → **use a white background** (관사).
- 더 나은 표현: "Like the workflow_2 weekly report, can you make it more condensed, show the progress as a flowchart, and use a white background?"
- 왜: 세 요구를 병렬 동사(make / show / use)로 정렬하면 요청이 한 문장으로 깔끔해집니다. "progress with the flow chart"는 "플로우차트로 진행하라"로 오독될 수 있어 **show the progress as a flowchart**(진행 상황을 플로우차트로 보여 달라)로 의도를 고정합니다.

### 카드 6 — 함수를 빼내야 하나?
- 내가 쓴 영어: "do I need take out the download functions from office_rich_notify.py? why do you import the two functions in the temp?"   (출처: transcript:[user] 8657d569…)
- 정정: "need take out" → **need to take out** (need는 to부정사를 받음).
- 더 나은 표현: "Do I need to move the download functions out of office_rich_notify.py? And why does the template import those two functions?"
- 왜: 코드 재배치엔 take out보다 **move X out of Y**가 표준 동사이고, "the temp"는 줄임말이라 **the template**로 풀어 주면 오해가 없습니다. 두 질문 사이의 And가 화제 전환을 부드럽게 만듭니다.

### 카드 7 — 존재 확인은 어떻게?
- 내가 쓴 영어: "how can I add existing check for msr images? they are *01AP.jpeg and cond.txt in the subfolder"   (출처: transcript:[user] 8657d569…)
- 정정: "existing check" → **existence check** ("이미 있는지" 확인은 existence; existing check는 "기존의 검사"로 읽힘). 관사도 필요: **an existence check**.
- 더 나은 표현: "How should I add an already-downloaded check for the msr images? They're *01AP.jpeg files, each with a cond.txt in a hidden subfolder."
- 왜: 의도가 "이미 받아졌는지"이므로 **an already-downloaded check**(또는 a skip-if-present guard)가 도메인 의미까지 전달합니다. each with 구문은 "각 이미지마다 딸린 cond.txt"라는 1:1 구조를 정확히 그립니다.

### 카드 8 — 왜 Phase 2에서 멈췄나
- 내가 쓴 영어: "update what we have done phase 1 and phase 2 test. why we stop at phase 2 and move on to the next step"   (출처: transcript:[user] 882dd9ec…)
- 정정: "what we have done phase 1 and phase 2 test" → **what we did in the Phase 1 and Phase 2 tests** (전치사 in + 복수). "why we stop" → **why we stopped** (이미 내린 결정은 과거형).
- 더 나은 표현: "Update the report with what we did in the Phase 1 and Phase 2 tests, why we stopped at Phase 2, and why we're moving on to the next step."
- 왜: update는 **update X with Y**(X를 Y로 갱신) 구조로 목적어(the report)를 세워야 명령이 완결됩니다. 멈춘 결정은 과거(stopped), 다음 단계 전환은 현재 진행 중인 방침이므로 **we're moving on**이 시제 대비를 살립니다.
