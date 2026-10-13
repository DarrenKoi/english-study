# 2026-10-14 — 코칭

## 한글→영어

### 카드 1 — 로그에서 본 오류의 원인 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "logs를 통해서 4XX, 5XX 오류들을 보면, recipe-search/recipe-detail인데 fab_name이 M16B로 되어서 발생하는 케이스들이 있어 내 생각에 fab_name이 R3 또는 R4여야 했을텐데, 왜 M16B로 선택되어서 query가 날라가고 오류가 발생할까?"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: Looking at the logs, some of the 4xx/5xx errors are recipe-search/recipe-detail calls where `fab_name` is M16B. I'd have expected R3 or R4 there. Why would M16B get selected and sent in the query?
- 왜 이렇게: "~를 통해서 보면"은 `Looking at the logs,` 분사구 하나로 끝난다. "~여야 했을텐데"는 `I'd have expected …` 가 정확한 짝이다(과거의 기대가 어긋남). "왜 M16B로 선택되어서"는 `Why would … get selected` 로, `would` 가 "그럴 리가 없는데 왜"라는 의아함을 담는다. 문장 셋으로 나누면 관찰·기대·질문이 또렷해진다.

### 카드 2 — 고치기 전에 부작용 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "지금 logging은 알 수 없지만 예상되는 경로를 너도 이미 알고 있으니 그 부분을 수정할 수 있을까? 수정하게 되면 발생하는 side effects가 있어?"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: We can't see the logs right now, but you already know the likely paths. Could you fix those? And would the fix have any side effects?
- 왜 이렇게: "알 수 없지만"의 주어는 로그가 아니라 우리라서 `We can't see the logs` 가 자연스럽다. "예상되는 경로"는 `the likely paths`. "수정하게 되면 발생하는"은 조건 전체를 `would the fix have` 가정법 하나로 받는다. 요청과 질문을 두 문장으로 나눠 상대가 둘 다 답하게 한다.

### 카드 3 — 깊이 고민해서 해법 찾자   (내가 쓴 한글)
- 내가 쓴 한글: "이 문제에 대해서 깊은 고민을 하고 해별 방안을 찾아보자. discuss with codex via herdr"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: Let's think this through properly and work out a fix. Discuss it with Codex via Herdr.
- 왜 이렇게: "깊은 고민을 하다"를 `think deeply` 로 직역하면 명상 느낌이 난다. `think this through` 가 "끝까지 따져 보다"에 가장 가깝다. "해결 방안을 찾다"는 `work out a fix` / `find a way forward`. `Let's` 로 함께 하자는 어조를 유지한다.

### 카드 4 — 확인 요청 리스트를 md 로   (내가 쓴 한글)
- 내가 쓴 한글: "그럼 내일 office agent에게 확인 요청할 것 리스트를 작성해서 md파일로 만들어줘"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: Then write up a list of things to have the office agent check tomorrow, as a markdown file.
- 왜 이렇게: "확인 요청할 것"은 `things to have the office agent check` 로 사역 `have + 사람 + 동사원형`. "리스트를 작성해서 md 파일로 만들다"는 두 동작이 아니라 `write up … as a markdown file` 한 동작이다. `write up` 은 정리해 문서로 만든다는 뜻이다.

### 카드 5 — 놓친 부분 검토 맡기기   (내가 쓴 한글)
- 내가 쓴 한글: "기존 사무실 요청서에 놓친 부분이 있는 지 codex에게 검토 맡겨줘. (herdr, vertical pane)"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: Have Codex review the office request doc for anything we missed. (Herdr, vertical pane.)
- 왜 이렇게: "검토 맡기다"는 `have Codex review`. "놓친 부분이 있는지"는 `whether there is anything missed` 보다 `for anything we missed` 가 짧고 자연스럽다(`review X for Y` = Y 가 있는지 X 를 보다). 괄호 지시는 영어도 그대로 괄호다.

### 카드 6 — 어디서 시작할까   (내가 쓴 한글)
- 내가 쓴 한글: "이제 veritysem과 provision을 구현하고 싶은데 어디에서 부터 시작하면 좋을까? office agent에게 요청할 게 있어?"   (출처: transcript:[user] skewnono-v3-nuxt/065d8f78)
- 자연스러운 영어: I'd like to start on VeritySEM and Provision now. Where should I begin, and is there anything I should ask the office agent for first?
- 왜 이렇게: "구현하고 싶은데"는 `I'd like to start on` 으로 의지를 부드럽게. "어디에서부터"는 `Where should I begin`. "요청할 게 있어?"는 `is there anything I should ask … for` 로 `ask for`(요청하다)를 끝에 둔다. `first` 를 보태면 "시작 전에"라는 숨은 뜻이 살아난다.

### 카드 7 — 현황 통보   (내가 쓴 한글)
- 내가 쓴 한글: "AMAT도 FTP로 가져올 수 있음. AMAT 장비의 경우 ALID 다름 (추후에 확인 예정). 소스는 만들어 나가야 함 for redis and opensearch. 측정 이력도 만들어야 함. 장비 명부만 확인 가능."   (출처: transcript:[user] skewnono-v3-nuxt/065d8f78)
- 자연스러운 영어: AMAT tools can also be pulled over FTP. Their ALIDs differ from Hitachi's (to be confirmed later). The Redis and OpenSearch sources still have to be built, and so does the measurement history. Only the tool roster is available today.
- 왜 이렇게: 메모체 "~함/~음"은 영어에서도 짧은 평서문이 짝이다. "만들어 나가야 함"은 `still have to be built` 로 "아직"을 `still` 이 맡는다. "측정 이력도"는 `and so does the measurement history` 로 반복을 피한다. "만 확인 가능"은 `Only … is available`.

### 카드 8 — 네 말이 맞다   (내가 쓴 한글)
- 내가 쓴 한글: "너가 맞아. v3_df_sem_list_version은 사용하지 않는 key야"   (출처: transcript:[user] skewnono-v3-nuxt/065d8f78)
- 자연스러운 영어: You're right — `v3_df_sem_list_version` isn't a key we use.
- 왜 이렇게: "사용하지 않는 key" 를 `an unused key` 로 하면 "존재하지만 안 쓰는"으로 읽힌다. `isn't a key we use` 는 "우리 쪽에선 안 쓴다"로 더 정확하다. `You're right` 뒤에 대시로 바로 사실을 붙이면 구어 리듬이 난다.

### 카드 9 — 내 처음 구상 설명   (내가 쓴 한글)
- 내가 쓴 한글: "내가 생각하는 처음 구조는, LLM 모델과 응답을 주고 받으며 내가 타겟으로 지정한 장비의 파일 구조를 함께 파악, 어떤 것을 다운받을 지 결정. 폴더 리스트를 그대로 raw 폴더에 받음."   (출처: transcript:[user] pm-notes/044c6c36)
- 자연스러운 영어: My initial idea is this: working back and forth with an LLM, we map out the file structure of a target tool together and decide what to download. Then we pull the listed folders as-is into a raw folder.
- 왜 이렇게: "주고 받으며"는 `working back and forth with` 가 대화의 왕복을 담는다. "함께 파악"은 `map out … together`. "그대로 받음"은 `pull … as-is`. 콜론으로 "구조는 이렇다" 를 열고 `Then` 으로 순서를 잇는다.

### 카드 10 — 위키에 적을 것   (내가 쓴 한글)
- 내가 쓴 한글: "wiki로 문서화 할 때는 파일에 어떤 데이터들이 있는 지 간략하게 설명하고 형태와 타입을 명시. 파일 경로는 현재 local이 저장된 path와 장비에 저장된 path 두개를 기록. 나의 생각 어때?"   (출처: transcript:[user] pm-notes/044c6c36)
- 자연스러운 영어: In the wiki, each entry briefly describes what data the file holds and spells out its format and types. For paths, we record both the local path and the path on the tool. What do you think?
- 왜 이렇게: "명시"는 `spell out`(빠짐없이 적다)이 `specify` 보다 메모에 어울린다. "두 개를 기록"은 `record both A and B`. "나의 생각 어때?"는 `What do you think?` 가 정형구다. `How about my idea?` 는 어색하다.

### 카드 11 — 낮과 밤으로 나누기   (내가 쓴 한글)
- 내가 쓴 한글: "처음에는 얕게 살펴보기로 시작해서 어떤 폴더들을 탐색하고 파일들을 다운받아 열지 리스트를 정리. 내가 퇴근할 때 일을 맡기면 이때부터 파일들을 다운받아 열어보고 그 내용들을 위키로 저장"   (출처: transcript:[user] pm-notes/044c6c36)
- 자연스러운 영어: Start with a shallow pass to draw up a list of which folders to explore and which files to download and open. When I leave for the day, I hand the job over, and from then on it downloads and opens the files and writes what it finds into the wiki.
- 왜 이렇게: "얕게 살펴보기"는 `a shallow pass`. "리스트를 정리"는 `draw up a list`. "퇴근할 때"는 `when I leave for the day`. "일을 맡기면"은 `hand the job over`. "이때부터"는 `from then on`. 사람이 하는 낮 일은 명령문, 기계가 하는 밤 일은 3인칭 현재로 주체를 가른다.

### 카드 12 — 절 추가와 기준 시각   (내가 쓴 한글)
- 내가 쓴 한글: "그래 04-phased-plan에 낮/밤 분업 절 추가해줘. 밤 일 시작 기준은 오후 8시."   (출처: transcript:[user] pm-notes/044c6c36)
- 자연스러운 영어: OK, add a day/night split section to 04-phased-plan. The night run starts at 8 p.m.
- 왜 이렇게: "분업"은 `division of labour` 가 사전 뜻이지만 여기선 `split` 이 짧고 맞다. "시작 기준은"을 `the criterion for starting is` 로 옮기면 번역투다. `starts at 8 p.m.` 한 문장이 기준을 말한다.

### 카드 13 — 이제 빼 달라   (내가 쓴 한글)
- 내가 쓴 한글: "home과 오피스 분업 내용은 이제 빼줘. office의 agent는 알 필요 없어."   (출처: transcript:[user] pm-notes/044c6c36)
- 자연스러운 영어: Take the home/office split out now. The office agent doesn't need to know about it.
- 왜 이렇게: "빼다"는 `take out` / `drop`. "알 필요 없어"는 `doesn't need to know about it` 으로 `about it` 을 붙여야 "그 내용을"이 전달된다. `has no need to know` 는 보안 문서 느낌이라 과하다.

### 카드 14 — 스키마 변경 통보   (내가 쓴 한글)
- 내가 쓴 한글: "{cdsem,hvsem}_idp_ver os 인덱스의 스키마에 약간 변화가 있어. ... 버그기간 문서와 신규 문서 공존 가능. 시간이 지나면 자동 치유. 위 opensearch index를 쓰는 코드들 반영 필요."   (출처: transcript:[user] skewnono-v3-nuxt/bcad2e37)
- 자연스러운 영어: There's a small schema change in the `{cdsem,hvsem}_idp_ver` OpenSearch indexes. Documents from the bug period can coexist with the new ones, and it heals itself over time. Every piece of code that reads these indexes needs updating.
- 왜 이렇게: "변화가 있어"는 `There's a … change in`. "공존 가능"은 `can coexist with`. "자동 치유"는 `heals itself over time` 으로 재귀 `itself` 가 "저절로"를 맡는다. "반영 필요"는 `needs updating`(동명사) 이 가장 짧다.

### 카드 15 — 배지로 표시   (내가 쓴 한글)
- 내가 쓴 한글: "unknown_eqp_id 미보유 탭에 배지로 표시해줘"   (출처: transcript:[user] skewnono-v3-nuxt/bcad2e37)
- 자연스러운 영어: Show `unknown_eqp_id` as a badge on the not-installed tab.
- 왜 이렇게: "~로 표시하다"는 `show X as a badge`. "~탭에"는 `on the … tab`(탭 위에 얹힌 UI 요소에는 `on`). 명령문 하나로 끝낸다.

### 카드 16 — 중단 기능 구현 가능?   (내가 쓴 한글)
- 내가 쓴 한글: "검색이 오래 걸리는 경우 사용자가 중단할 수 있어야 하는데 구현 가능함? 예를 들어, skewvoir에 초기화 버튼 옆에 검색 중단 (Search 시작 시 3초 이상 걸릴 시 활성화)."   (출처: transcript:[user] skewnono-v3-nuxt/cf55cb11)
- 자연스러운 영어: When a search takes a long time, the user should be able to cancel it. Is that doable? For example, a "Stop search" button next to Reset in skewvoir, enabled once a search has been running for more than three seconds.
- 왜 이렇게: "구현 가능함?"은 `Is that doable?` 가 구어 짝(`Is it implementable?` 는 어색). "3초 이상 걸릴 시 활성화"는 `enabled once … has been running for more than three seconds` 로 `once` 가 "~하면 그때부터". 현재완료진행이 "3초째 돌고 있다"를 정확히 담는다.

### 카드 17 — 데이터 미스매치 걱정   (내가 쓴 한글)
- 내가 쓴 한글: "프런트만 구현해서 중단을 누르는 경우 backend와 데이터 미스매치에 대한 문제는 없나?"   (출처: transcript:[user] skewnono-v3-nuxt/cf55cb11)
- 자연스러운 영어: If we only do this on the front end and the user hits Stop, is there any risk of the data getting out of sync with the backend?
- 왜 이렇게: "미스매치에 대한 문제"는 `risk of the data getting out of sync` 로 `out of sync` 가 기술 정형구. "~에 대한"을 `about` 으로 옮기지 않고 `risk of` 로 직결한다. "중단을 누르다"는 `hit Stop`(버튼은 `hit`/`press`).

### 카드 18 — 그럼 효과가 없네   (내가 쓴 한글)
- 내가 쓴 한글: "사실 그럼 중단 버튼을 누르는 효과가 없는거네?"   (출처: transcript:[user] skewnono-v3-nuxt/cf55cb11)
- 자연스러운 영어: So pressing Stop doesn't actually achieve anything, then?
- 왜 이렇게: "사실 그럼"은 `So … actually …, then?` 으로 앞뒤에 흩어 넣는다. "효과가 없다"는 `doesn't achieve anything` / `has no real effect`. 끝의 `then?` 이 "~인 거네?" 의 확인 어조다.

### 카드 19 — 틀린 전제 위에 쌓는 셈   (고급 한글 · 번역)
- 한글 원문: "A는 진짜 근본 원인일 가능성이 높지만 사무실 확인 없이는 틀린 전제 위에 쌓는 셈이고, C는 증상을 숨길 뿐 사용자 경험은 그대로입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/b4fc9877)
- 자연스러운 영어: A is probably the real root cause, but without confirmation from the office we'd be building on an unverified assumption; C only hides the symptom and leaves the user experience unchanged.
- 번역 포인트: "~하는 셈이다"는 `we'd be building on …` 가정법 진행으로 "그런 행동이 되어 버린다"를 담는다. "틀린 전제"는 아직 틀렸다고 확정된 게 아니라 `unverified assumption` 이 정확하다. "증상을 숨길 뿐 … 그대로"는 `only hides … and leaves … unchanged` 로 `leave + 목적어 + 형용사`.

### 카드 20 — 경계에서 갈라진다   (고급 한글 · 번역)
- 한글 원문: "사람이 판단할 일(어디를 볼지)과 기계가 반복할 일(받고 열고 적기)이 정확히 그 경계에서 갈라집니다."   (출처: transcript:[assistant] pm-notes/044c6c36)
- 자연스러운 영어: That boundary is exactly where human judgement (deciding where to look) and machine repetition (downloading, opening, writing) part ways.
- 번역 포인트: 한국어는 "A 와 B 가 경계에서 갈라진다"인데 영어는 경계를 주어로 세워 `That boundary is exactly where … part ways` 로 뒤집는 편이 힘이 있다. "판단할 일"은 `human judgement`, "반복할 일"은 `machine repetition` 으로 명사화해 대구를 맞춘다. `part ways` 는 "갈라서다".

### 카드 21 — 새벽 3시에 죽어도   (고급 한글 · 번역)
- 한글 원문: "새벽 3시에 죽어도 그때까지의 페이지는 남아 있어야 합니다."   (출처: transcript:[assistant] pm-notes/044c6c36)
- 자연스러운 영어: If the run dies at 3 a.m., every page written up to that point must still be there.
- 번역 포인트: "죽어도"는 양보 `even if` 보다 조건 `If … dies` 뒤에 `must still be there` 로 `still` 이 "그래도"를 맡는 쪽이 영어답다. "그때까지의 페이지"는 `every page written up to that point` 로 과거분사 후치 수식.

## 영어 다듬기

### 카드 1 — 초단축본 요청
- 내가 쓴 영어: "We need super-brief version (make a separate file) for the demo. in the super brief, we have the intro card -> search around (no need to show the card, play right away the video with the simple subtitle ...) and then append cube_alarm.JPG (we change the order)"   (출처: transcript:[user] auto-recipe-creator/baf56f9b)
- 정정: `a super-brief version` — 단수 가산명사에 관사가 필요하다. `play right away the video` → `play the video right away`: 부사 `right away` 는 목적어 뒤에 둔다. 문장 첫 글자 `in` 은 대문자.
- 더 나은 표현: We need a super-brief version for the demo, as a separate file. It opens with the intro card, then goes straight into the Search Around recording with a simple subtitle ("Search Around 기능 구현 with Agent") and no title card, and ends with cube_alarm.JPG — so the order changes.
- 왜: 순서를 `opens with → then goes straight into → ends with` 세 동사로 풀면 화살표 없이도 흐름이 보인다. `no need to show the card` 는 `and no title card` 로 압축된다.

### 카드 2 — 긴 lot ID 넘침
- 내가 쓴 영어: "in afm page, from the 최근 측정 / search result table, when LOT ID is longer like (XED0504TZ_TE) then, the text is overflow from the LOT component. can you fix this?"   (출처: transcript:[user] skewnono-v3-nuxt/8b037e20)
- 정정: `the text is overflow` → `the text overflows`: `overflow` 는 동사로 쓴다(`is overflowing` 도 가능). `in afm page` → `on the AFM page`(페이지는 `on`, 관사 필요). `when … then,` 에서 `then` 은 불필요.
- 더 나은 표현: On the AFM page, in the 최근 측정 / search-result table, a longer lot ID such as XED0504TZ_TE overflows its Lot tag. Can you fix this?
- 왜: 조건절 대신 `a longer lot ID such as …` 를 주어로 세우면 문장이 하나로 줄고 `such as` 가 예시를 자연스럽게 끼운다. `component` 보다 사용자가 보는 이름 `tag` 가 구체적이다.

### 카드 3 — 슬롯 정보도 빠지나
- 내가 쓴 영어: "due to the longer lot id, do we miss slot info as well? I do not see the number in the slot."   (출처: transcript:[user] skewnono-v3-nuxt/8b037e20)
- 더 나은 표현: Are we also losing the slot info because of the long lot ID? I can't see a number in the Slot tag.
- 왜: 문법 오류는 없다. `miss` 는 "놓치다/그리워하다"로 읽힐 수 있어 데이터가 사라지는 뜻에는 `lose` 가 맞다. 현재진행 `Are we losing` 이 "지금 화면에서 벌어지는 일"을 담는다. `due to` 는 문두 격식체라 질문에서는 `because of` 가 자연스럽다.

### 카드 4 — 가치 있으면 고쳐 달라
- 내가 쓴 영어: "this is unusual case that is longer lot id. so if it is worth of fixing without harming our UI/UX, go deal with it."   (출처: transcript:[user] skewnono-v3-nuxt/8b037e20)
- 정정: `an unusual case` — 관사. `worth of fixing` → `worth fixing`: `worth + -ing` 에 `of` 가 붙지 않는다(`worthy of` 와 혼동). `that is longer lot id` → `where the lot ID is longer` 또는 `: a longer lot ID`.
- 더 나은 표현: This is an edge case — lot IDs this long are rare. If it's worth fixing without hurting the UI/UX, go ahead and deal with it.
- 왜: `edge case` 가 "드문 예외 상황"의 기술 정형구. `go deal with it` 은 명령으로는 다소 거칠게 들리고, `go ahead and deal with it` 이 "그럼 진행해"의 승인 어조다. `harm` 보다 UI 에는 `hurt` 가 흔하다.

### 카드 5 — 플레이스홀더 추가
- 내가 쓴 영어: "add the – placeholder for a blank slot"   (출처: transcript:[user] skewnono-v3-nuxt/8b037e20)
- 더 나은 표현: Go ahead and add the "–" placeholder for blank slots.
- 왜: 오류는 없다. 상대가 제안한 것을 승인하는 상황이라 `Go ahead and` 가 그 맥락을 살린다. 기호는 따옴표로 감싸야 문장 속에서 읽힌다. 규칙을 말할 때는 복수 `blank slots` 가 일반 진술에 맞다.

### 카드 6 — 프롬프트 편집기 닫기
- 내가 쓴 영어: "close the temp prompt ide" / "close IDE currently opening up for the prompt if there is"   (출처: transcript:[user] skewnono-v3-nuxt/4921f2b7, c0567c9e)
- 정정: `if there is` 는 보어가 빠졌다 → `if there is one`. `currently opening up` → `currently open`: 열려 있는 상태는 형용사 `open`, `opening up` 은 열리는 동작이다.
- 더 나은 표현: Close the temporary prompt editor if one is still open.
- 왜: `IDE` 보다 실제 대상인 `prompt editor`(Ctrl+G 로 열린 임시 편집 창)가 정확하다. `if one is still open` 이 "있으면"과 "아직 열려 있으면"을 한 절로 처리한다.

### 카드 7 — 접두사로 구분 가능
- 내가 쓴 영어: "distinguishabld by eqp_model_cd prefix (VERITY* / PROVISION*)"   (출처: transcript:[user] skewnono-v3-nuxt/065d8f78)
- 정정: `distinguishable` 철자. 명사 앞 관사 `the eqp_model_cd prefix`.
- 더 나은 표현: They can be told apart by the `eqp_model_cd` prefix (VERITY* / PROVISION*).
- 왜: `distinguishable by` 도 맞지만 메모에는 `told apart by` 가 가볍다. 메모체라도 영어는 주어(`They`)를 세워 주는 쪽이 읽기 쉽다.

### 카드 8 — Codex 와 논의
- 내가 쓴 영어: "discuss with codex via herdr"   (출처: transcript:[user] skewnono-v3-nuxt/b4fc9877)
- 더 나은 표현: Talk it through with Codex via Herdr.
- 왜: 오류는 없다. `discuss` 는 타동사라 목적어가 있어야 자연스럽다(`discuss it with Codex`). `talk it through` 는 "결론이 날 때까지 주고받다"로, 앞 문장의 "깊은 고민"과 이어진다.
