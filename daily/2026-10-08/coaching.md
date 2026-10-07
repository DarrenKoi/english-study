# 2026-10-08 — 코칭

> 내가 쓴 글은 skewnono 세션 넷, auto-recipe-creator 세션 둘, pm-notes 세션 하나에서 나왔다. 한국어는 서른 건 남짓이고 긴 메시지는 문장 단위로 나눴다. 영어는 아홉 건. 사무실 agent 의 회신을 붙여 넣은 메시지(Q43~Q53 답, 8차 답변, 번호별 A/B 답안, 실패 목록, 스크립트 네 줄)는 내가 쓴 글로 보지 않고 뺐다. 다만 그 끝에 내가 덧붙인 한 문장("우리가 주고 받은 답변 회신들은…")은 카드 7로 만들었다. "응 커밋하고 push 해줘", "CRF 12로 바꿔서 push 해줘", "좋아. push" 는 앞선 카드와 겹쳐 뺐다.

## 한글→영어

### 카드 1 — ~에게 보낼 메시지로 정리해줘   (내가 쓴 한글)
- 내가 쓴 한글: "Q54~Q56을 office agent에게 보낼 메시지로 정리해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Write up Q54–Q56 as a message I can send to the office agent.
- 왜 이렇게: "정리해줘"는 `organize` 보다 `write up` 이 맞다. 흩어진 것을 보낼 만한 글로 만든다는 뜻이 `up` 에 실린다. "~에게 보낼 메시지로"는 `as a message I can send to …` 로 풀면 "내가 그대로 보낸다"는 용도가 드러난다. 번호 범위는 `Q54–Q56` 이나 `Q54 through Q56`.

### 카드 2 — ~도 같이 넣어서, 그냥   (내가 쓴 한글)
- 내가 쓴 한글: "Q35, Q46, Q53도 같이 넣어서 md파일로 작성해줘 그냥."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Just put Q35, Q46 and Q53 in as well and make it an md file.
- 왜 이렇게: 문장 끝의 "그냥"은 "묻지 말고 해 달라"는 뜻이라 영어에서는 `Just` 를 문두에 둔다. "~도 같이 넣어서"는 `put … in as well` 이나 `include … too`. "md파일로 작성해줘"는 `make it an md file` 이 가볍고 `write it up as a Markdown file` 은 조금 더 문서답다.

### 카드 3 — 빼주고, 왜 옳은지 설명 추가   (내가 쓴 한글)
- 내가 쓴 한글: "office.py 재복사 빼주고, mileage를 빼는 것이 왜 옳은 지 설명 추가해야함."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Take out the part about re-copying office.py, and add an explanation of why leaving Mileage out is the right call.
- 왜 이렇게: "빼다"가 두 번 나오는데 영어로는 동사를 갈라 쓴다. 문서에서 항목을 빼는 것은 `take out`, 판정에서 Mileage 를 제외하는 것은 `leave out`. "왜 옳은지"는 `why … is the right call` 이 판단의 옳음을 말하고 `why it's correct` 는 사실의 맞음에 가깝다. "~해야함"은 메모체라 명령문으로 옮겼다.

### 카드 4 — ~이기 때문에 없어도 됨   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 md 파일의 내용을 copy and paste to other repo이기 때문에 file path 같은거는 없어도 됌"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Also, I'm going to copy and paste the contents into another repo, so you can leave out things like file paths.
- 왜 이렇게: 영어는 이유를 `because` 로 앞세우기보다 `…, so …` 로 뒤에 결과를 붙이는 쪽이 말하기에 자연스럽다. "없어도 됨"은 `don't need` 도 되지만 상대에게 시키는 말이니 `you can leave out`. "~같은 거"는 `things like …`. 영어로 쓴 부분(`copy and paste to other repo`)은 아래 영어 다듬기 카드 6에서 따로 다뤘다.

### 카드 5 — 있으면 정리해서 알려줘   (내가 쓴 한글)
- 내가 쓴 한글: "추가 질문이 있으면 정리해서 알려줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: If you have any follow-up questions, put them together and send them over.
- 왜 이렇게: "추가 질문"은 `additional questions` 보다 `follow-up questions` 가 "앞의 답에서 이어지는 질문"이라는 뜻을 살린다. "정리해서"는 `put them together` 나 `list them out`. 한 문장으로 줄이면 `List any follow-up questions you have.` 이고 `any` 가 "있으면"을 품는다.

### 카드 6 — 짧게 답할 수 있는 구조로, 손으로 옮기니까   (내가 쓴 한글)
- 내가 쓴 한글: "최대한 office agent가 짧게 대답할 수 있는 구조로 질문을 던져야 함 (내가 핸드라이팅 해서 너에게 답을 주기 때문에)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Phrase the questions so the office agent can answer as briefly as possible, since I'll be copying the answers by hand and typing them in for you.
- 왜 이렇게: "~할 수 있는 구조로 질문을 던지다"는 `structure` 를 명사로 끌고 오지 않고 `phrase the questions so (that) …` 으로 푼다. "최대한 짧게"는 `as briefly as possible`. "핸드라이팅"은 한국식 영어다. `handwriting` 은 필체나 손글씨 자체를 가리키는 명사라 동작으로는 `copy … by hand` 나 `write … down by hand` 로 쓴다. 이유를 괄호에 넣는 대신 `since` 절로 붙였다.

### 카드 7 — 기록이 잘 되어 있어야 함   (내가 쓴 한글)
- 내가 쓴 한글: "우리가 주고 받은 답변 회신들은 기록이 잘 되어 있어야 함!"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Make sure every reply we've exchanged is properly recorded!
- 왜 이렇게: "~되어 있어야 함"은 상태를 요구하는 말이라 `Make sure … is recorded` 가 맞다. `should be recorded` 는 권고로 들린다. "주고받은"은 `we've exchanged` 나 `that went back and forth`. "잘"은 `well` 보다 `properly` 가 "빠짐없이, 제대로"의 뜻. 명사로 받으면 `Keep a proper record of everything we've sent back and forth.`

### 카드 8 — ~라고 추정하고 진행   (내가 쓴 한글)
- 내가 쓴 한글: "KST라고 추정하고 진행. 세 장비의 fab은 MAP608은 PKG, MAPC01은 R3, 5EAP1501은 M15"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Go ahead on the assumption that it's KST. As for the fabs: MAP608 is PKG, MAPC01 is R3, and 5EAP1501 is M15.
- 왜 이렇게: "~라고 추정하고 진행"은 `go ahead on the assumption that …` 이나 더 짧게 `Assume KST and go ahead.` `estimate` 는 수치를 어림할 때 쓰는 말이라 여기에는 맞지 않는다. 주제를 먼저 세우는 "세 장비의 fab은"은 `As for the fabs:` 로 받고, 나열 끝에는 `and` 를 넣는다.

### 카드 9 — ~처럼 제한을 없애야 함   (내가 쓴 한글)
- 내가 쓴 한글: "msr_image 처럼 afm도 이미지 다수에 대한 제한을 없애야함. 원본 다운로드 기능 구현해야함. 1회차 2회차 가능하면 표"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: AFM needs to be exempt from the rate limit too, like msr_image, since it loads a lot of images. Also implement the original-file download, and show first run / second run in the table if you can.
- 왜 이렇게: "제한을 없애다"를 `remove the limit` 으로 옮기면 제한 자체를 지운다는 뜻이 된다. 한 대상만 빼 주는 것이니 `exempt A from the limit`. "이미지 다수에 대한"은 이유로 돌려 `since it loads a lot of images`. "가능하면"은 문장 끝의 `if you can`. "1회차/2회차"는 `first run / second run` 이나 `pass 1 / pass 2`.

### 카드 10 — 문제 있는 게 있는지 리뷰 요청   (내가 쓴 한글)
- 내가 쓴 한글: "오늘 수정한 것들 중 문제 있는게 있는 지 herdr 통해 codex에게 리뷰 요청해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Have Codex review today's changes through herdr and see if anything's wrong.
- 왜 이렇게: "~에게 리뷰 요청해줘"는 `ask Codex to review` 도 되고 사역동사 `have Codex review` 가 더 짧다(`have + 사람 + 동사원형`). "오늘 수정한 것들"은 `today's changes`. "문제 있는 게 있는지"는 `see if anything's wrong` 이 구어, `check for any issues` 가 문어.

### 카드 11 — 확인할 것들 정리해서   (내가 쓴 한글)
- 내가 쓴 한글: "office에서 확인할 것들 정리해서 md 파일로 만들어줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Put together a checklist of what needs verifying at the office and save it as an md file.
- 왜 이렇게: "확인할 것들 정리"는 영어에 `checklist` 라는 낱말이 따로 있다. `need + -ing` 는 "~되어야 한다"는 수동의 뜻(`needs verifying` = `needs to be verified`). "office에서"는 장소라 `at the office`. `in the office` 는 건물 안이라는 뜻이 더 짙다.

### 카드 12 — 꽉 차 있어서 너무 빽빽하고   (내가 쓴 한글)
- 내가 쓴 한글: "afm page 팁 모니터링에서 측정별 상태 지표에서 5개 차트가 하나의 row에 꽉 차있어서 너무 뺵빽하고 정보를 제대로 전달하고 있지 못해."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: On the AFM tip monitoring page, the per-measurement status section crams five charts into one row. It's too dense, and none of them reads well.
- 왜 이렇게: "꽉 차 있어서 빽빽하다"는 `cram A into B` 한 동사가 다 맡는다(`are crammed into one row` 도 좋다). "~에서 ~에서"로 겹친 위치는 앞쪽을 `On … page` 로, 뒤쪽을 주어로 올려 풀었다. "정보를 제대로 전달하지 못한다"는 `fails to convey information` 보다 `none of them reads well` 이 화면을 본 사람의 말투. "측정별"은 `per-measurement`.

### 카드 13 — ~든지 하고, 의미 없음   (내가 쓴 한글)
- 내가 쓴 한글: "측정별 상태 지표 안에서 2 by 2 차트로 나누든지 하고. Valude = False 포인트는 삭제. (Data 포인트 의미 없음)"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Split them into a 2-by-2 grid or something along those lines, and drop the Valid = FALSE chart — those data points don't tell us anything.
- 왜 이렇게: "~든지 하고"는 한 가지 안을 예로 드는 말투라 `or something along those lines` 나 `or something like that` 을 붙인다. "2 by 2 차트"는 차트 하나가 아니라 배치이니 `a 2-by-2 grid`. "의미 없음"은 `meaningless` 도 되지만 `don't tell us anything` 이 "봐도 얻는 게 없다"는 뜻으로 더 구체적이다.

### 카드 14 — ~순으로 중요하니 그렇게   (내가 쓴 한글)
- 내가 쓴 한글: "Tip Width, Mileage 평균, Approach Count 평균, FAILED+STOPPED포인트 순으로 중요하니 그렇게 2 BY 2로 표현해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: In order of importance it's Tip Width, average Mileage, average Approach Count, then FAILED + STOPPED points, so lay out the 2-by-2 in that order.
- 왜 이렇게: "~순으로 중요하니"는 `in order of importance` 를 문두에 놓고 나열한다. 마지막 항목 앞의 `then` 이 순서임을 다시 알린다. "그렇게"는 `in that order` 로 구체화해야 무엇을 따르라는지 분명하다. "표현해줘"는 `express` 가 아니라 배치하는 일이라 `lay out`.

### 카드 15 — ~은 유지   (내가 쓴 한글)
- 내가 쓴 한글: "가동 현황은 유지."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Leave the usage page as it is.
- 왜 이렇게: "유지"를 `maintain` 으로 옮기면 "관리·보수하다"로 읽힌다. 건드리지 말라는 뜻은 `leave … as it is` 나 `keep … as is`. 더 짧게는 `The usage page stays.` 이고 오늘 표현의 `The Orca app itself stays` 와 같은 틀이다.

### 카드 16 — 자막 입히는 작업, 어떤 식으로   (내가 쓴 한글)
- 내가 쓴 한글: "video폴더에 새로운 mp4 파일이 있어. … 자막 입히는 작업을 해야해. … 시간 대 별로 위 내용을 입히고 싶어. 어떤식으로 진행하는게 좋을까"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: There's a new mp4 in the video folder, and I need to add subtitles to it. I want each caption shown during its time range. What's the best way to go about this?
- 왜 이렇게: "자막을 입히다"는 `add subtitles to` 가 일반적이고, 화면에 구워 넣는 방식이면 `burn in subtitles` 라는 전문어가 있다. "시간대별로"는 `by time slot` 보다 `each caption shown during its time range` 가 정확하다. "어떤 식으로 진행하는 게 좋을까"는 `What's the best way to go about this?` 이고 `go about` 는 "일에 착수하다".

### 카드 17 — 관찰하고, 판단해서 End-point 합니다   (내가 쓴 한글)
- 내가 쓴 한글: "왼쪽은 SEM 화면, 오른쪽은 FI면화면으로 FIB 진행하면서 계속 SEM 이미지를 관찰하고 딥러닝 기반으로 판단해서 End-point합니다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The SEM view is on the left and the FIB view on the right. As milling proceeds, the system keeps watching the SEM image and uses a deep-learning model to decide when to stop.
- 왜 이렇게: 한국어는 주어 없이 이어지지만 영어는 누가 관찰하고 판단하는지를 세워야 해서 `the system` 을 넣었다. "~하면서"는 `As milling proceeds`. FIB 로 깎는 일은 `mill`. "End-point 합니다"는 명사를 동사로 쓴 현장 말이라 `decide when to stop` 으로 풀거나 `call the endpoint` 로 쓴다. "딥러닝 기반으로"는 `uses a deep-learning model to …`.

### 카드 18 — 저배율에서 고배율로 관찰해 가며   (내가 쓴 한글)
- 내가 쓴 한글: "시편을 저배율에서 고배율로 관찰해가며 학습된 패턴을 찾아 고배율 파노라마로 관찰하고 이미지를 저장합니다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The system scans the specimen from low to high magnification, locates the learned pattern, then captures and saves a high-magnification panorama.
- 왜 이렇게: 동사 넷(관찰, 찾아, 관찰, 저장)을 영어에서는 `scans, locates, captures and saves` 로 저마다 다른 동사를 쓴다. "관찰하다"를 두 번 다 `observe` 로 옮기면 밋밋해진다. "저배율에서 고배율로"는 `from low to high magnification`. "시편"은 `specimen`(TEM 에서는 `sample` 보다 흔하다). 자막이라면 주어를 빼고 `Scanning from low to high magnification …` 처럼 `-ing` 로 시작해도 된다.

### 카드 19 — 추천대로, 전용으로 하나 따로   (내가 쓴 한글)
- 내가 쓴 한글: "FIB 화면 으로 수정. 오디오 필요 없음. 자막 모양 너의 추천대로 진행. python script는 이거 전용으로 하나 따로 만들어줘"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Change it to "FIB 화면". No audio needed. Go with your recommendation for the subtitle layout, and write a separate Python script just for this.
- 왜 이렇게: "너의 추천대로 진행"은 `go with your recommendation`. `go with` 는 여러 안 가운데 하나를 고른다는 뜻이다. "이거 전용으로 하나 따로"는 `a separate script just for this` 이고, 형용사로는 `a dedicated script`. "필요 없음"은 `No audio needed.` 처럼 명사 뒤에 `needed` 를 붙이는 메모체가 그대로 통한다.

### 카드 20 — ~에만 있어서 거기서 확인할 예정   (내가 쓴 한글)
- 내가 쓴 한글: "영상은 office에만 있어서 거기에서 확인할 예정."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The video only exists at the office, so I'll check it there.
- 왜 이렇게: "~에만 있다"는 `only exists at …` 나 `is only on my office machine`. "확인할 예정"은 방금 정한 일이라 `I'll`. 이미 세워 둔 계획으로 말하려면 `I'm going to check it there`. `only` 는 꾸미는 말 바로 앞에 두는 것이 원칙이지만 구어에서는 동사 앞에 두는 일이 흔하다.

### 카드 21 — 왜 화질 열화가 발생하는 거지   (내가 쓴 한글)
- 내가 쓴 한글: "왜 화질 열화가 발생하는거지? 용량도 줄어들음."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Why did the quality drop? The file got smaller, too.
- 왜 이렇게: "화질 열화가 발생하다"를 `quality degradation occurs` 로 옮기면 논문 투가 된다. 말로는 `the quality dropped` 나 `it looks worse`. 이미 일어난 일이니 과거형. "용량"은 `capacity`(담을 수 있는 양)가 아니라 `file size` 이고, "줄어들다"는 `got smaller`.

### 카드 22 — 보통 안 넣지? 줄 바꿈이 어색   (내가 쓴 한글)
- 내가 쓴 한글: "자막에 보통 마침표 안넣지? 마침표 . 제거. 그리고 줄 바꿈이 어색하게 되는데, 예를 들어 (영상은 모의 제작된..)에서 ( )빼고, 다음 줄에서 영상은 모의 제작된 FIB 장비의 Loadlock 모형으로 수정)"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Subtitles don't usually end with a period, do they? Take the periods out. The line breaks are awkward, too — for example, drop the parentheses around "영상은 모의 제작된…" and put that part on its own line.
- 왜 이렇게: "안 넣지?"는 동의를 구하는 말이라 부가의문문 `…, do they?` 가 맞다. 앞이 부정(`don't`)이면 꼬리는 긍정. "줄 바꿈"은 `line breaks`. "어색하다"는 `awkward` 이고 `strange` 보다 "읽기 불편하다"는 뜻이 정확하다. "다음 줄에서"는 `on its own line`. 마침표는 미국식 `period`, 영국식 `full stop`.

### 카드 23 — ~만 아래 줄에 있어서 이상해   (내가 쓴 한글)
- 내가 쓴 한글: "제작된 시편을 TEM 홀더에 조립하여 로봇이 TEM 장비에 로딩합니다. 에서도 로딩합니다만 아래 줄에 있어서 자막 보이는게 이상해."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Same problem in the TEM-holder line: only "로딩합니다" wraps to the second line, so the subtitle looks off.
- 왜 이렇게: "~만 아래 줄에 있다"는 `only X wraps to the second line`. `wrap` 은 줄이 넘어간다는 동사다. 낱말 하나만 덩그러니 남는 것을 조판에서는 `an orphan`/`a widow` 라고 한다. "이상해"는 `looks off` 가 "뭔가 어긋나 보인다"는 구어. "~에서도"는 `Same problem in …:` 으로 앞세우면 무엇의 반복인지 바로 읽힌다.

### 카드 24 — 폴더를 만들고, 브레인스토밍이 필요함   (내가 쓴 한글)
- 내가 쓴 한글: "my-task에 폴더 하나를 만들고 여기에 AI/DT 교육 커리큘럼 설계안에 대한 브레인 스토밍이 필요함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Create a folder under my-task. I need to brainstorm a design for an AI/DT training curriculum there.
- 왜 이렇게: "브레인스토밍이 필요함"은 명사로 굳힌 말이라 영어에서는 사람을 주어로 세워 `I need to brainstorm …`. `brainstorm` 은 타동사로 바로 목적어를 받는다(`brainstorm ideas`). "~에 대한"을 `about` 으로 따라가지 않아도 된다. "my-task에"는 하위 폴더이니 `under my-task`. 사내 "교육"은 `education` 보다 `training`.

### 카드 25 — 목적은 ~ 도출을 위한 ~ 방향 논의   (내가 쓴 한글)
- 내가 쓴 한글: "목적은 제조 회사에서 1인 1Agent 개발 (운영) 실행 방안 도출을 위한 교육 과정 신설과 인증 체계 정리 방향 논의."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: The goal is to work out how a manufacturing company can get every employee building and running their own agent. To get there, we need to discuss which new training courses to set up and how to structure the certification system.
- 왜 이렇게: 한국어 원문은 명사 일곱 개가 조사 없이 이어진다. 영어로 그대로 쌓으면 읽을 수 없어서 문장을 둘로 가르고 명사마다 동사를 돌려줬다. "방안 도출"은 `work out how …`, "과정 신설"은 `set up new courses`, "체계 정리"는 `structure the certification system`. "1인 1Agent"는 `one agent per person` 이 직역이고 풀어서 `every employee … their own agent`.

### 카드 26 — 분과를 운영하고, 발표 자료를 만들어야 함   (내가 쓴 한글)
- 내가 쓴 한글: "여러 분과를 운영하고 각 분과는 커리큘럼을 정리하고 발표 자료를 만들어야 함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: There will be several working groups, and each one has to draw up its curriculum and prepare a presentation.
- 왜 이렇게: "분과"는 `subcommittee` 나 `working group`, 교육 과정의 갈래라는 뜻이면 `track`. "여러 분과를 운영하고"는 주어가 없으니 `There will be several working groups` 로 연다. "커리큘럼을 정리하다"는 `draw up`(초안을 짜다)이 맞고 "발표 자료"는 `a presentation` 이나 `a slide deck`. `each one` 뒤에는 단수 동사와 `its`.

### 카드 27 — 말 그대로 ~한 사람들을 길러내는   (내가 쓴 한글)
- 내가 쓴 한글: "Expert는 말그대로 AI Agent 전문적인 지식을 갖추고 개발을 하고, S/W에 대한 지식도 해박한 사람들을 길러니는 커리큘럼에 해당된다."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: As the name suggests, the Expert track is a curriculum for developing people who build AI agents with real expertise and who also know software inside out.
- 왜 이렇게: "말 그대로"는 `literally` 보다 `As the name suggests` 가 "이름이 뜻하는 대로"에 맞다. "길러내다"는 `develop people` 이나 `train people to …`. `raise` 는 아이를 키울 때 쓴다. "해박하다"는 `know … inside out` 이 구어, `have deep knowledge of` 가 문어. "~에 해당된다"는 `is` 한 낱말로 충분하다. 관계절 둘을 `who … and who also …` 로 나란히 세웠다.

### 카드 28 — 잘 준비해줬네, ~도 들어갈 수 있다고 생각해   (내가 쓴 한글)
- 내가 쓴 한글: "너가 가설을 잘 준비해줬네. 실제로 Agent를 가장 잘 만드는 개인 그리고, expert로서 지식을 가지고 Agent를 만들 수 있게 다른 사람들을 가이드 해주는 사람도 expert에 들어갈 수 있다고 생각해. grilling으로 6장 질민부터 진행"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Nice work on the hypotheses. I think "Expert" should cover both: the people who are best at building agents, and the people who use that expertise to guide others in building theirs. Let's start grilling from the questions in section 6.
- 왜 이렇게: "잘 준비해줬네"는 `Nice work on …` 이 칭찬의 가장 가벼운 틀. "~도 들어갈 수 있다고 생각해"는 `I think X should cover both:` 로 먼저 "둘 다"를 선언하고 콜론 뒤에 나열하면 긴 수식이 정리된다. "가이드해 주다"는 `guide others in building theirs` 이고 `theirs` 가 `their agents` 를 받는다. "~부터 진행"은 `Let's start … from …`.

### 카드 29 — 일단 ~하는 커리큘럼, ~로 가도 좋을 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "Fast Track은 일단 end to end로 빠르게 개발 과정을 교육 시키고 완성시킬 수 있도록 가이드 하는 커리큘럼. 분과마다 독립된 인증으로 가도 좋을 것 같아. Expert는 회사 내에서 일반적인 cloud 개발 환경 사용."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: For now, Fast Track is a curriculum that walks people through development end to end, quickly, and gets them to a finished agent. I think separate certification for each track would be fine. Expert will use the company's standard cloud dev environment.
- 왜 이렇게: "교육시키고 … 가이드하는"은 `walk people through` 한 동사구가 "단계를 따라 데리고 간다"는 뜻으로 둘을 겸한다. "완성시킬 수 있도록"은 `get them to a finished agent`. "~로 가도 좋을 것 같아"는 `I think … would be fine` 이고 `would` 가 "그래도 괜찮겠다"는 누그러진 승인을 맡는다. "일반적인"은 `general` 이 아니라 `standard`. "일단"은 `For now`.

### 카드 30 — ~로 가자   (내가 쓴 한글)
- 내가 쓴 한글: "Q1은 (c) 단계형으로 가자"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: For Q1, let's go with (c), the staged model.
- 왜 이렇게: 선택지를 고를 때의 "~로 가자"는 `let's go with …`. `let's go to` 는 장소로 간다는 뜻이다. "Q1은"은 `For Q1,` 으로 주제를 앞세운다. "단계형"은 `staged`, `tiered`(등급이 있는), `two-step` 가운데 Builder 다음에 Guide 가 오는 구조라 `staged` 나 `tiered` 가 맞다.

### 카드 31 — 나중에 이어가기 위해 남겨줘   (내가 쓴 한글)
- 내가 쓴 한글: "나중에 이어가기 위해 폴더에 내용 남겨줘."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Save where we are in the folder so we can pick this up later.
- 왜 이렇게: "이어가다"는 `pick this up later` 나 `pick up where we left off`. "내용 남겨줘"는 `leave the contents` 보다 `save where we are`(지금 어디까지 왔는지)가 뜻에 가깝다. "~하기 위해"는 `in order to` 대신 `so we can …` 이 말하기에 자연스럽다.

### 카드 32 — ~해 달라는 요청이 왔다, 가능하면   (내가 쓴 한글)
- 내가 쓴 한글: "brief demo 비디오에서 시간을 더 줄여달라는 요청이 왔다. 맨 처음 엔지니어 갱ㅂ 없는 AI 기반 자동화 card 삭제. 가능하면 00:20~00:23"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I've been asked to make the brief demo video even shorter. Delete the very first card ("엔지니어 개입 없는 AI 기반 자동화"), and cut 00:20–00:23 too if possible.
- 왜 이렇게: "요청이 왔다"는 `A request came` 보다 사람을 주어로 한 수동 `I've been asked to …` 가 자연스럽다. 누가 요청했는지 말하지 않아도 된다는 점도 원문과 같다. "더 줄이다"는 `even shorter`. "맨 처음"은 `the very first`. 원문의 "가능하면 00:20~00:23"에는 동사가 없어 어시스턴트도 뜻을 되물었다. 영어로는 `cut` 을 밝혀 적는다.

### 카드 33 — 그대로 있는데?   (내가 쓴 한글)
- 내가 쓴 한글: "첫카드 그대로 있는데?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: The first card's still there, though?
- 왜 이렇게: "~는데?"는 기대와 다르다는 것을 알리는 말끝이라 문장 끝의 `though` 가 가장 가깝다. 평서문 어순에 물음표만 붙여 "이상한데?"를 전한다. `Why is the first card still there?` 는 원인을 따지는 말이라 조금 더 세다. "그대로 있다"는 `is still there`.

### 카드 34 — 너무 많으면 문제이니, ~든가 아니면   (내가 쓴 한글)
- 내가 쓴 한글: "팁 모니터링 from afm tips, Recipe 전체 리스트 너무 많으면 문제이니, 3줄 이상이면 스크롤 방식으로 내려가며 볼 수 있던가 아니면 팝업 윈도우에서 선택할 수 있게 진행"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: On the AFM tips page, the full recipe list will be a problem once it gets long. If it runs past three rows, either make it scrollable or let me pick from a popup.
- 왜 이렇게: "~든가 아니면"은 `either A or B`. "너무 많으면 문제이니"는 `will be a problem once it gets long` 이고 `once` 가 "그렇게 되는 순간"을 맡는다. "3줄 이상이면"은 `if it runs past three rows` 에서 `run past` 가 "넘어가다". "스크롤 방식으로 내려가며 볼 수 있게"는 형용사 `scrollable` 하나로 줄어든다.

### 카드 35 — 당연히 넘게 되어 있어   (내가 쓴 한글)
- 내가 쓴 한글: "수십종은 당연히 넘게 되어있어. 선택 팝업과 recipe 검색도 가능하게 해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: It's bound to go well past a few dozen. Make it a selection popup, and make the recipes searchable too.
- 왜 이렇게: "당연히 ~하게 되어 있다"는 `be bound to` 가 꼭 맞는다. 피할 수 없이 그렇게 된다는 뜻이다. `will definitely` 도 되지만 "구조상 그럴 수밖에 없다"는 느낌은 `bound to` 쪽이 짙다. "수십 종"은 `a few dozen` 이나 `dozens`. "넘다"는 `go well past`(`well` 은 "훌쩍"). "검색도 가능하게"는 형용사 `searchable`.

### 카드 36 — 조용히 틀리는 화면   (고급 한글 · 번역)
- 한글 원문: "가정이 틀리면 화면이 오류 없이 틀린 자리에 측정이나 세로선을 놓습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: If the assumption is wrong, the page won't throw an error; it will quietly put a measurement or a vertical line in the wrong place.
- 번역 포인트: "오류 없이 틀린 자리에"는 한국어에서 부사구 하나지만 영어로는 "오류는 안 난다"와 "틀리게 놓는다"를 세미콜론으로 갈라야 뜻이 산다. `quietly` 나 `silently` 가 "티 나지 않게"를 맡는다. 같은 글의 "화면이 조용히 틀릴 수 있는 것"은 `things the page could get silently wrong`. 조건절은 현재형, 주절은 `will`.

### 카드 37 — "밖"의 뜻이 바뀐다   (고급 한글 · 번역)
- 한글 원문: "그래서 '밖'은 팁이 이상하다는 뜻이 아니라 새것이거나 오래 썼다는 뜻이 되고, 교체 직후마다 뜨는 경고에 실제 이상(Tip Width, Approach Count)이 묻힙니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: So "out of limits" ends up meaning the tip is new or well used rather than faulty, and the real anomalies (Tip Width, Approach Count) get buried under warnings that fire after every tip change.
- 번역 포인트: "~라는 뜻이 아니라 ~라는 뜻이 되고"는 `ends up meaning A rather than B` 로 접는다. `end up` 이 "결과적으로 그렇게 되어 버린다"를 맡는다. "묻힌다"는 `get buried under` 그대로 통한다. "교체 직후마다 뜨는 경고"는 관계절 `warnings that fire after every tip change` 이고 경고가 뜬다는 동사로 `fire` 를 쓴다. 관리도에서 "밖"은 `out of limits` 나 `out of control`.

### 카드 38 — 손실이 한 번 더 쌓인다   (고급 한글 · 번역)
- 한글 원문: "원본도 이미 한 번 압축된 영상이라, 다시 압축하면 손실이 한 번 더 쌓입니다. 자막을 화면에 박아 넣는 방식에서는 피할 수 없고, 비트레이트를 높여 줄일 수만 있습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The source has already been compressed once, so re-encoding it stacks a second round of loss on top. With burned-in subtitles that's unavoidable; all you can do is raise the bitrate to keep it small.
- 번역 포인트: "손실이 쌓인다"는 `stacks … on top` 이나 `compounds the loss`. 이런 누적 손실을 `generation loss` 라고 부른다. "화면에 박아 넣는"은 `burned-in`(`hardcoded`) subtitles 라는 굳은 말이 있다. "줄일 수만 있습니다"의 "~만"은 `all you can do is …` 로 옮긴다. 이때 `is` 뒤에는 to 없는 동사원형이 온다.

### 카드 39 — 가이드의 신뢰, 줄어드는 인원   (고급 한글 · 번역)
- 한글 원문: "직접 만들어 운영해 보지 않은 사람의 가이드는 신뢰를 얻기 어렵고, 잘 만드는 사람에게 가이드까지 강제하면 인원이 너무 줄어듭니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Guidance from someone who has never built and run an agent themselves is hard to trust, and if you also require every strong builder to guide, the pool shrinks too far.
- 번역 포인트: "~해 보지 않은 사람의 가이드"는 `guidance from someone who has never …` 로 관계절에 현재완료를 쓴다(경험). "신뢰를 얻기 어렵다"는 주어를 그대로 두고 `is hard to trust`. "가이드까지 강제하면"의 "까지"는 `also`. "인원이 줄어든다"는 `the pool shrinks` 이고 `pool` 은 뽑을 수 있는 사람의 모집단을 가리킨다. `too far` 가 "너무"를 맡는다.

## 영어 다듬기

### 카드 1 — Here is the reply from … about …
- 내가 쓴 영어: "Here is the reply from the office agent about the afm questions."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Here's the office agent's reply to the AFM questions.
- 왜: 문법은 맞다. `reply` 는 `to` 와 짝을 이루는 명사라 `the reply … to the questions` 가 `about` 보다 정확하다. `the reply from the office agent` 는 소유격 `the office agent's reply` 로 줄이면 한 호흡에 읽힌다. 약어 `AFM` 은 대문자로.

### 카드 2 — the simplified answer
- 내가 쓴 영어: "here is the simplified answer from the office agent."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Here's the office agent's answer in short form — just a letter per item.
- 왜: 오류는 아니다. 다만 `simplified` 는 "쉽게 풀어 쓴"으로 읽혀서, 글자 하나씩으로 줄인 답이라는 뜻과 어긋난다. 줄였다는 뜻은 `condensed`, `abbreviated`, `in short form`. 뒤에 `just a letter per item` 을 붙이면 받는 쪽이 세부가 없다는 것을 미리 안다.

### 카드 3 — reply from the office agent. / Here is the answer.
- 내가 쓴 영어: "reply from the office agent." / "Here is the answer."   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Here's the office agent's reply to the follow-up. / Here are the answers to the 31 questions.
- 왜: 둘 다 틀린 데는 없고 라벨로는 충분하다. 무엇에 대한 답인지를 붙이면 회신이 여러 차례 오갈 때 헷갈리지 않는다. 답이 여러 개이면 `the answer` 보다 복수 `the answers` 가 맞다.

### 카드 4 — go verify the web
- 내가 쓴 영어: "go verify the web via agent-browser"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `the web` → `the web app`(또는 `the pages`). `the web` 은 인터넷 전체를 가리키는 말이라 우리 화면이라는 뜻으로는 쓰지 않는다.
- 더 나은 표현: Go check the AFM pages in the browser with agent-browser.
- 왜: `go + 동사원형`(`go verify`)은 미국 구어에서 자연스러운 꼴이라 그대로 둬도 된다. `via` 는 경로·수단에 쓰는 조금 딱딱한 전치사이고 도구에는 `with` 가 가볍다. `verify` 는 "기대한 대로인지 검증"이라는 뜻이 뚜렷해서 무엇을 확인할지 붙이면 더 좋다(`verify that today's changes render correctly`).

### 카드 5 — close the codex pane
- 내가 쓴 영어: "close the codex pane"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: You can close the Codex pane now.
- 왜: 명령문으로 완전하다. `You can … now` 를 쓰면 "이제 필요 없으니"라는 이유가 함께 실리고 말투도 부드러워진다. 제품 이름 `Codex` 는 대문자.

### 카드 6 — copy and paste to other repo
- 내가 쓴 영어: "… md 파일의 내용을 copy and paste to other repo이기 때문에 …"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `copy and paste to other repo` → `copy and paste it into another repo`. 단수 가산명사 앞에는 `other` 가 아니라 `another`(an + other)를 쓰고, `copy and paste` 는 타동사라 목적어가 있어야 하며, 붙여 넣는 곳은 `into`.
- 더 나은 표현: I'll be pasting this into another repo, so drop the file paths.
- 왜: `other` 는 복수(`other repos`)나 `the other repo` 처럼 한정사가 있을 때 쓴다. `I'll be -ing` 는 "그렇게 될 예정"을 담담하게 알리는 미래진행형이라 이유를 댈 때 잘 맞는다.

### 카드 7 — commit and push
- 내가 쓴 영어: "commit and push"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Commit this and push it to main.
- 왜: 개발자끼리는 두 낱말로 충분하고 틀린 데도 없다. 목적어(`this`)와 목적지(`to main`)를 붙이면 무엇을 어디로 보낼지가 분명해진다. 이날은 이미 다 푸시된 상태여서 어시스턴트가 "남은 것이 없다"고 답했는데, `Is everything pushed?` 라고 물었다면 한 번에 끝났다.

### 카드 8 — remove orca skills and plugins
- 내가 쓴 영어: "remove orca skills and plugins"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Remove the Orca skill and any Orca plugins.
- 왜: 오류는 없다. `any` 를 넣으면 "있는지 모르지만 있다면 전부"가 되어, 실제로 플러그인이 설치돼 있지 않았던 이 경우에 딱 맞는다. 범위를 더 분명히 하려면 `Remove everything Orca-related from my Claude Code setup, but keep the app.`

### 카드 9 — 팁 모니터링 from afm tips
- 내가 쓴 영어: "팁 모니터링 from afm tips, …"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `from afm tips` → `on the AFM tips page`. 화면이나 페이지 위에 있는 것은 `on`.
- 더 나은 표현: On the AFM tips page (tip monitoring), …
- 왜: `from` 은 출처나 출발점을 말한다(`data from the AFM tips API`). 위치를 먼저 세우는 말은 `On the … page,` 로 문두에 두면 뒤의 요청이 어디에 관한 것인지 바로 잡힌다.
