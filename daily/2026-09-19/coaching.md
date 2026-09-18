# 2026-09-19 — 코칭

> 오늘 `[user]` 한국어 문장은 auto-recipe-creator 의 File Manager 테스트 보고 하나뿐이라 (a) 카드는 1장이다. (b) 는 어시스턴트가 인용한 skewnono 화면 문구 두 줄로 만들었다. 어시스턴트는 오늘 영어로만 답해서 다른 한국어 원문은 없다. 영어 다듬기는 세 저장소의 `[user]` 문장에서 14장을 골랐다. `commit and push`, `close the codex pane`, `apply the failures message change`, `bump opensearch-py to 3.x`, `update CLAUDE.md with …` 는 고칠 데가 없어 뺐다.

## 한글→영어

### 카드 1 — 가려진 게 아니라 잘못 짚었다   (내가 쓴 한글)
- 내가 쓴 한글: "라벨 확인 실패. 예상 역ㅕㄱ에 file manager button 라벨이 보입니다. 가려진 게 아니라 VLM이 잘못 짚었습니다."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Label check failed. The File Manager label is visible in the expected area, so the button wasn't hidden — the VLM just pointed at the wrong spot.
- 왜 이렇게: "보입니다"는 `can be seen` 보다 `is visible` 이 짧고 자연스럽다. "가려진 게 아니라 잘못 짚었다"는 `It wasn't A; it was B` 로 옮겨도 되지만, 앞 문장을 근거로 받아 `so … wasn't hidden` 으로 이으면 관찰 → 결론이 한 문장에 선다. "잘못 짚다"는 `mislocated it` 도 되고, 구어로는 `pointed at the wrong spot` 이 그림이 선명하다. 어시스턴트도 같은 상황을 `the VLM mislocated it` 과 `the VLM just pointed at the wrong button` 두 가지로 말했다. (`역ㅕㄱ` 은 "영역"의 오타.)

### 카드 2 — 그룹이 없다는 안내   (고급 한글 · 번역)
- 한글 원문: "현재 허용 오차를 모든 비교 셀에서 만족하는 장비 그룹이 없습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt, 1차 추천 카드 문구 인용)
- 자연스러운 영어: No tool group meets the current tolerance in every compared cell.
- 번역 포인트: 한국어는 "~하는 그룹이 없습니다"로 관계절이 명사 앞에 길게 붙는다. 영어는 `There is no group that satisfies …` 로 옮기기 쉽지만, UI 문구라면 `No + 명사 + 동사` 로 부정을 주어에 얹는 편이 짧다. "만족하다"는 기준·조건에는 `satisfy` 보다 `meet` 이 흔하다(`meet the tolerance`, `meet the requirement`). "모든 비교 셀에서"는 `in all compared cells` 도 되지만 `in every` 가 "하나도 빠짐없이"를 더 분명히 한다.

### 카드 3 — 대체 기준을 알리는 안내   (고급 한글 · 번역)
- 한글 원문: "현재 허용 오차로는 N배화 그룹이 없어, 비교 중인 다른 장비의 항목별 중앙값을 기준으로 계산했습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt, 폴백 카드 문구 인용)
- 자연스러운 영어: The current tolerance leaves no N-fold group, so the targets are based on the per-parameter median of the other tools being compared.
- 번역 포인트: "허용 오차로는 그룹이 없어"를 `With the current tolerance, there is no group` 으로 옮기면 한국어 어순이 그대로 남는다. 허용 오차를 주어로 세워 `The current tolerance leaves no group` 이라고 하면 원인이 주어가 되는 영어다운 무생물 주어 문장이 된다. "~을 기준으로 계산했습니다"는 주어(누가)가 없는 한국어라 영어에서는 `the targets are based on …` 처럼 결과물을 주어로 둔 수동이 매끄럽다. "항목별"은 `per-parameter`, "비교 중인"은 `being compared` 로 진행 수동 분사를 쓴다.

## 영어 다듬기

### 카드 1 — 알림이 사라졌나 묻기
- 내가 쓴 영어: "now we have no more notification in the landing page?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `notification` → `notifications`. 여러 공지를 말하니 복수다. `in the landing page` → `on the landing page`. 웹 페이지는 표면으로 보아 `on` 을 쓴다.
- 더 나은 표현: Are the notifications gone from the landing page now?
- 왜: 평서문 끝에 물음표만 붙이는 것도 구어에선 통하지만, "없어졌어?"라는 놀람은 `Are … gone?` 이 바로 전한다. `no more` 는 "더 이상 없다(앞으로도)"라서 일시적 현상을 묻는 데는 조금 무겁다.

### 카드 2 — DB 문제냐 백엔드 문제냐
- 내가 쓴 영어: "Is this the problem happening in the opensearch DB? or the issue in the backend?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 두 선택지를 한 질문으로 묻는 것이니 물음표를 중간에 끊지 않는다. `the problem happening in` 은 "그 DB 에서 일어나는 바로 그 문제"로 읽혀 어색하다.
- 더 나은 표현: Is this a problem on the OpenSearch side, or in our backend?
- 왜: 양자택일 질문은 `Is it A or B?` 한 문장으로 묻는다. "~쪽 문제"는 `on the X side` 가 딱 맞는 연어다. 어시스턴트 답의 첫 줄 `It is the cluster, not the backend.` 과 짝을 지어 외워 두면 묻고 답하는 틀이 함께 익는다.

### 카드 3 — 버전을 올려도 되는지
- 내가 쓴 영어: "can I change the opensearch version from 3.4 to 3.7? no issue based on the current usage at all?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Can I upgrade OpenSearch from 3.4 to 3.7? Would that break anything we're currently using?
- 왜: 문법 오류는 없다. 버전을 올리는 건 `change` 보다 `upgrade` 가 정확하다. 둘째 질문은 명사구 조각이라 무엇을 묻는지 상대가 채워야 한다. `Would that break anything …?` 처럼 동사를 세우면 "하위 호환 확인"이라는 의도가 분명해진다. 확신을 구하는 뉘앙스는 `Is it safe given how we use it?` 도 좋다.

### 카드 4 — 챗에 OpenSearch 연결 제안
- 내가 쓴 영어: "What do you think of connect the opensearch case? … can we do that? but what if the opensearch give the data that is supposed to be displayed in charts, how can we do it?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `think of connect` → `think of connecting`. 전치사 `of` 뒤에는 동명사가 온다. `the opensearch give` → `OpenSearch gives`. 3인칭 단수 현재형이고 고유명사라 관사가 필요 없다.
- 더 나은 표현: What do you think about connecting OpenSearch the same way? And if OpenSearch returns data that's better shown as a chart, how would we handle that?
- 왜: `the opensearch case` 는 "매뉴얼 경우처럼"을 말하려던 것이라 `the same way` 가 짧다. `is supposed to be displayed` 는 "그렇게 보여야 한다고 정해져 있다"라서 "차트가 어울리는 데이터"라는 뜻이면 `better shown as a chart` 가 맞는다. `how can we do it` 보다 가정 질문에 맞춰 `how would we handle that` 이 자연스럽다.

### 카드 5 — 계약을 만들 수 있나
- 내가 쓴 영어: "So can we make a contract to communicate between you and office LLM? like we have done for manual case?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `office LLM` → `the office LLM`, `manual case` → `the manual case`. 특정한 하나를 가리키니 정관사가 필요하다. `like we have done` → `like we did`. 과거의 특정 작업을 떠올리는 것이라 단순 과거가 자연스럽다.
- 더 나은 표현: So can we set up a contract between you and the office LLM, like we did for the manuals?
- 왜: `make a contract to communicate between` 은 성분이 많아 흐리다. `set up a contract between A and B` 로 줄이면 뜻이 같다. 두 번째 조각을 쉼표로 붙이면 한 문장이 된다.

### 카드 6 — 파일 이름 바로잡기
- 내가 쓴 영어: "the file name hidden_button.. it must be manual_click_button.py hidden is a just kind of fallback method when the button is not seen when supposed to be there."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `a just kind of` → `just a kind of`. `just` 는 관사 앞에 온다. `when supposed to be there` → `when it's supposed to be there`. 이 경우 주어와 be 동사를 생략하면 어색하다. 문장 경계도 없어 마침표가 필요하다.
- 더 나은 표현: The file name should be manual_click_button.py, not hidden_button. "Hidden" is just the fallback for when the button isn't visible where it should be.
- 왜: `must be` 는 강한 추측("~임에 틀림없다")으로도 읽혀 지시로는 `should be` 가 안전하다. `A, not B` 로 옳은 이름과 틀린 이름을 한 번에 대비시켰다. `not seen when supposed to be there` 는 `isn't visible where it should be` 가 흔한 문형이다.

### 카드 7 — 무엇을 앵커로 썼는지
- 내가 쓴 영어: "your prompt is wrong. Use the first letter 'F' as the anchor. there are so many buttons and text starts with "F". you mislocated."   (출처: transcript:[user] auto-recipe-creator)
- 정정: 둘째 문장이 명령문이라 "F 를 앵커로 써라"로 읽힌다. 하려던 말은 "네가 F 를 앵커로 썼다"이므로 `You used …` 여야 한다. `text starts with` → `labels that start with`. `mislocated` 는 타동사라 목적어가 필요하다(`mislocated it`).
- 더 나은 표현: Your prompt is wrong — it uses the first letter 'F' as the anchor. There are lots of buttons whose labels start with "F", so you picked the wrong one.
- 왜: 명령문과 서술문의 차이가 지시를 뒤집을 수 있다. 어시스턴트는 문맥으로 맞게 읽었지만 반대로 구현했어도 이상하지 않았다. `so many` 는 감탄조라 사실 설명에는 `lots of` 가 가볍다. 관계절 `whose labels start with "F"` 로 "F 로 시작하는 라벨을 가진 버튼"을 한 명사구로 묶었다.

### 카드 8 — OCR 로 확대해서 확인 안 하나
- 내가 쓴 영어: "don't Alt+click when the label is just mislocated. you do not use OCR to zoom in screen shot to check?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `you do not use OCR …?` → `Don't you use OCR …?`. 의문문은 조동사가 주어 앞으로 온다. 평서문에 물음표만 붙이면 구어에선 통하지만, `do not` 을 풀어 쓴 채로는 딱딱한 서술로 읽힌다. `zoom in screen shot` → `zoom in on the screenshot`. `zoom in` 은 대상을 `on` 으로 받는다. `screenshot` 은 한 단어다.
- 더 나은 표현: Don't Alt+click when the label is just in the wrong place. Aren't you using OCR on a zoomed-in crop to check it?
- 왜: 부정 의문문 `Aren't you …?` 는 "당연히 하고 있지 않아?"라는 기대를 담아 확인하는 어조다. `mislocated` 는 기술 문서 말투라 구어에선 `in the wrong place` 가 편하다.

### 카드 9 — 창 두 개가 겹칠 때
- 내가 쓴 영어: "the latest test, it detects the windows but fail to locate the mouse on the window, a bit located higher than the window and no ALT + click effect."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `the latest test, it detects` → `In the latest test, it detected`. 시간 부사구에는 전치사가 필요하고, 지난 테스트를 말하니 과거형이다. `fail` → `failed`. 주어가 `it` 이라 주어-동사 일치도 필요하다.
- 더 나은 표현: In the latest test, it found the windows but put the cursor a bit above them, so the Alt+click had no effect.
- 왜: `locate the mouse on the window` 는 "창 위에서 마우스를 찾다"로 읽힌다. 마우스를 어디에 두는 건 `put`/`place the cursor` 다. 증상 두 개(`a bit higher`, `no effect`)를 `so` 로 이어 원인 → 결과 관계를 드러냈다.

### 카드 10 — 커서가 원인이었다
- 내가 쓴 영어: "I think you had failed because mouse cursor is on the button File Manager. anyways now it works."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `you had failed` → `it failed`. 과거완료는 다른 과거 시점보다 앞선 일을 말할 때만 쓴다. 여기선 단순 과거면 된다. `mouse cursor is` → `the mouse cursor was`. 관사가 필요하고 시제를 과거로 맞춘다. `the button File Manager` → `the File Manager button`. 영어는 이름이 명사 앞에 온다. `anyways` 는 구어체라 글에서는 `anyway`.
- 더 나은 표현: I think it failed because the mouse cursor was sitting on the File Manager button. Anyway, it works now.
- 왜: `was sitting on` 은 커서가 거기 머물러 있었다는 상태를 진행형으로 그린다. 어시스턴트는 같은 사실을 `left the equipment's cursor on top of the File Manager button` 으로 받았다. `now it works` 도 틀리진 않지만 `it works now` 가 더 자연스러운 어순이다.

### 카드 11 — 커서 동기화 설명
- 내가 쓴 영어: "If it is not synced. the mouse movement from the local PC and the mouse cursor in the tool monitor located separately. (drifted). … if they are two with the certain disctance, then it is out of sync."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `If it is not synced.` 뒤 마침표는 쉼표여야 한다. 조건절만으로는 문장이 끝나지 않는다. `located separately` 에는 동사가 없다(`are located` 또는 `end up in different places`). `with the certain disctance` → `a certain distance apart`. 불특정 거리라 부정관사, `disctance` 는 오타.
- 더 나은 표현: If it's out of sync, the local mouse and the cursor on the tool monitor end up in different places (drift). So if you see two cursors a certain distance apart, it's out of sync.
- 왜: 조건 + 결과를 한 문장으로 닫고, 괄호 속 `(drift)` 로 용어를 달았다. `a certain distance apart` 는 두 물체 사이 간격을 말하는 고정 틀이다(`two meters apart`).

### 카드 12 — 몇 번이 5번인지
- 내가 쓴 영어: "no need to try 5 times. just 3 times enough I think"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `just 3 times enough` 에는 동사가 없다 → `3 times is enough`.
- 더 나은 표현: We don't need 5 probe points — 3 should be enough.
- 왜: 문법보다 모호함이 문제였다. 어시스턴트는 "5 times"가 측정 지점 5곳인지 재판독 횟수인지 몰라 `"5 times" probably means the 5 probe points` 라고 추측한 뒤 확인을 붙였다. 무엇을 세는지(`probe points`, `retries`)를 명사로 적으면 이런 추측이 필요 없다. `should be enough` 는 `I think` 없이도 판단을 부드럽게 낸다.

### 카드 13 — 재시작이 실패할 수 있나
- 내가 쓴 영어: "we touch the file to restart at late night. is there any possibility of failing restart based on the current code? like while rebooting, if someone uses haveavily, it might interrupt the restarting?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `at late night` → `late at night`. 고정된 어순이다. `failing restart` → `the restart failing`. 의미상 주어를 앞에 둔 동명사구다. `haveavily` → `heavily` (오타). `interrupt the restarting` → `interrupt the restart`.
- 더 나은 표현: We touch a file late at night to trigger a restart. Could the restart fail with the current code — for example, if someone is using the app heavily while it reboots?
- 왜: `is there any possibility of …` 는 뜻은 맞지만 길다. `Could X fail …?` 가 같은 질문을 동사 하나로 묻는다. 예시는 대시로 붙이고 `for example` 로 연다. `like` 로 여는 예시는 구어에서는 괜찮지만 질문 본문과 섞이면 흐려진다.

### 카드 14 — 뜻이 뒤집힌 마무리
- 내가 쓴 영어: "if there is no possibility of restarting, I stop talking here"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 하려던 말은 "재시작이 실패할 가능성이 없으면"인데 쓴 문장은 "재시작할 가능성이 없으면"이라 뜻이 반대다. `of restarting` → `of the restart failing`. `I stop talking here` 는 현재형이라 습관처럼 들린다. 결정은 `I'll stop here` 로 말한다.
- 더 나은 표현: If there's no chance the restart fails, I'll stop here.
- 왜: 어시스턴트가 `To be precise for the record: load cannot stop the reload …` 로 답한 것도 이 문장이 모호해서다. 부정어가 겹치는 조건문(`no possibility` + `failing`)은 핵심 동사(`fails`)를 빠뜨리기 쉬우니 쓰고 나서 한 번 더 읽는다. 대화를 끝낼 때는 `That's all I needed, thanks.` 도 자연스럽다.
