# 2026-07-22 — 코칭

## 한글→영어

### 카드 1 — 한글 문서 매끄러움 점검 요청   (내가 쓴 한글)
- 내가 쓴 한글: "전체적으로 한글이 매끄럽게 적용되고 있는지 확인해서 수정해줘"   (출처: transcript:[user] skewnono_v3_nuxt e65e5c9a)
- 자연스러운 영어: "Go through the docs and check whether the Korean reads smoothly overall — fix anything that doesn't."
- 왜 이렇게: "매끄럽다"는 문장에 대해 쓰면 read smoothly / flow naturally가 정확하다(be applied smoothly는 코드 적용처럼 들림). "확인해서 수정해줘"는 check and fix로 직결하되, fix anything that doesn't(매끄럽지 않은 곳은 고쳐라)처럼 관계절 생략 구문을 쓰면 한 문장으로 깔끔하게 닫힌다.

### 카드 2 — 과윤문 회피 보고   (고급 한글 · 번역)
- 한글 원문: "이 문서들은 이미 짧고 리듬 있는 개발자 문체라 번역투·기계적 병렬이 거의 없어서, '억지 제거 금지' 지침대로 과윤문을 피했습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt e65e5c9a)
- 자연스러운 영어: "These docs are already written in a terse, rhythmic developer voice with almost no translationese or mechanical parallelism, so — per the no-forced-fixes guideline — I steered clear of over-editing."
- 번역 포인트: "문체라"의 이유 연결은 so 하나로 충분하고, "~ 지침대로"는 per(=~에 따라)가 문어에서 가장 간결하다. "과윤문을 피했다"는 avoided도 되지만 steered clear of가 "일부러 거리를 뒀다"는 의지까지 담는다. "개발자 문체"는 developer voice — style보다 voice가 글쓴이 개성의 뉘앙스.

### 카드 3 — 덤으로 잡은 버그   (고급 한글 · 번역)
- 한글 원문: "덤으로, 제가 처음 작성할 때 챕터 11에 12/13 폴더 번호를 뒤바꿔 링크한 버그도 찾아 고쳤습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt e65e5c9a)
- 자연스러운 영어: "As a bonus, I also caught and fixed a bug from my original draft — chapter 11 had folders 12 and 13 linked the wrong way around."
- 번역 포인트: "덤으로"는 as a bonus가 딱 맞는 관용 대응. "뒤바꿔 링크한"은 linked the wrong way around(순서가 서로 뒤바뀐)로 — swapped도 좋다. "찾아 고쳤다"는 caught and fixed — catch가 "버그를 잡다"의 표준 동사라 found보다 자연스럽다.

### 카드 4 — 하루 마무리 인사   (고급 한글 · 번역)
- 한글 원문: "잘 마무리하셨습니다 — 내일 사무실에서 뵙겠습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 1b71ccc2)
- 자연스러운 영어: "Nicely wrapped up — see you at the office tomorrow."
- 번역 포인트: "마무리하다"는 wrap up이 회화의 표준. 상대의 마무리를 칭찬하는 "잘 ~하셨습니다"는 영어에서 주어를 빼고 Nicely wrapped up / Good work wrapping up처럼 결과를 평가하는 형태가 자연스럽다(You finished well은 어색).

## 영어 다듬기

### 카드 1 — office 연결 완료 보고
- 내가 쓴 영어: "now we have made up the connection the pages via env setting (health, sem_list, recipe_tat, storage) are now office (un-commented). For me they seems work find as they call the data from officd DBs without problem."   (출처: transcript:[user] skewnono_v3_nuxt 1b71ccc2)
- 정정: ① "they seems work find" → "they seem to work fine" — 주어 they에 -s 불필요, seem 뒤에는 to부정사, find는 fine의 오타. ② "made up the connection" → "wired up the pages" — make up은 "지어내다/화해하다"라서 연결의 뜻이 없다.
- 더 나은 표현: "We've now wired the pages (health, sem_list, recipe_tat, storage) to office via the env settings, and they seem to work fine — they're pulling from the office DBs without any problems."
- 왜: 연결 작업은 wire up / hook up이 개발 영어의 관용 동사. "call the data"는 영어에서 어색하고 pull/fetch data가 표준이다. 문장을 and로 잇고 대시 뒤에 근거를 붙이면 보고 리듬이 산다.

### 카드 2 — limit=1000 우려 제기
- 내가 쓴 영어: "one of things I am worried is that you use limit=1000 for calling url in the page. limit 1000 will lead to missing data as we have so many tools and lots of measurements across the fabs. you have to call all the data (entire rows with the date range)."   (출처: transcript:[user] skewnono_v3_nuxt 1b71ccc2)
- 정정: ① "one of things" → "one of the things" — one of 뒤 복수명사에는 정관사 필요. ② "I am worried is that" → "I'm worried about is that" — worry는 about과 결합("the thing I'm worried about").
- 더 나은 표현: "One thing that worries me is the limit=1000 on that request — with this many tools and measurements across the fabs, a 1,000-row cap is bound to drop data. Please fetch every row in the date range instead."
- 왜: "One thing that worries me is ..."가 우려 제기의 표준 오프닝. "lead to missing data"보다 drop data(데이터가 잘려 나간다)가 구체적이고, is bound to(필연적으로 ~하게 된다)가 will보다 위험 경고의 어감을 살린다. "call the data" → fetch.

### 카드 3 — hostname 감지 제안
- 내가 쓴 영어: "Although we make step-by-step transition, can we make overide method? I wonder if it is possible to detect where I am via host name? since we are working in mac-mini, I think it is possible."   (출처: transcript:[user] skewnono_v3_nuxt 1b71ccc2)
- 정정: ① "make step-by-step transition" → "we're making the transition step by step" — transition에 관사 필요, step by step은 부사구로 뒤에. ② "overide" → "override". ③ "working in mac-mini" → "working on a Mac mini" — 기기는 on.
- 더 나은 표현: "Even though we're migrating step by step, could we add an override? I'm wondering if we could detect where I am from the hostname — since I work on a Mac mini, that should be doable."
- 왜: 기능을 새로 넣는 것은 make보다 add가 자연스럽다("add an override"). "I wonder if it is possible"은 문법상 맞지만 I'm wondering if we could가 제안의 어감으로 더 부드럽고, "that should be doable"(가능할 것 같다)이 I think it is possible보다 회화답다.

### 카드 4 — cloud 고려 여부 질문
- 내가 쓴 영어: "At the office, we have two hostnames (my pc in the office) and cloud (for production mode). No need to consider about the cloud?"   (출처: transcript:[user] skewnono_v3_nuxt 1b71ccc2)
- 정정: "consider about" → "consider" — consider는 타동사라 전치사가 붙지 않는다(think about과 혼동하기 쉬운 지점).
- 더 나은 표현: "At the office there are actually two environments — my office PC and the cloud (production). Don't we need to account for the cloud too?"
- 왜: "No need to ...?"는 통하지만, 부정 의문 Don't we need to ...?가 "고려해야 하는 것 아닌가요?"라는 확인 질문의 표준형. account for(계산에 넣다)는 설계 논의에서 consider보다 한 단계 정확한 동사다.

### 카드 5 — PC 접두사 규칙 제안
- 내가 쓴 영어: "To make it simpler, just my PC hostname starts with \"PC\" so it can easily be detected as my PC in the office."   (출처: transcript:[user] skewnono_v3_nuxt 1b71ccc2)
- 정정: 문법 오류는 없지만 "just my PC hostname starts with"의 just 위치가 모호하다(내 PC만? 그냥?).
- 더 나은 표현: "To keep it simple: my PC's hostname starts with \"PC\", so that prefix alone is enough to identify my office machine."
- 왜: "To keep it simple:"이 단순화 제안의 관용 오프닝. "that prefix alone is enough to ..."(그 접두사만으로 충분하다)가 "it can easily be detected"의 수동태보다 의도를 능동적으로 전달한다.

### 카드 6 — 자는 동안 작업 위임
- 내가 쓴 영어: "let's update the @docs/study/ the contents based on what we have done upto now. I let you freely fill in all the folders in study (if new one needed? make ones). Also you can make more md files if you want. Since I am going to sleep now, you continue to do the job."   (출처: transcript:[user] skewnono_v3_nuxt e65e5c9a)
- 정정: ① "upto" → "up to" — 두 단어. ② "I let you freely fill in" → "Feel free to fill in" — 허락은 let이 아니라 feel free to로 표현. ③ "make ones" → "create new ones" — ones 앞에는 수식어가 필요하다.
- 더 나은 표현: "Let's update docs/study/ to reflect what we've done so far. Feel free to restructure any folder — create new ones if needed, and add more md files as you see fit. I'm heading to bed, so keep going without me."
- 왜: "based on what we have done"보다 to reflect what we've done(한 일이 반영되도록)이 목적을 정확히 담는다. as you see fit(알아서 판단해서)이 if you want의 격식 위 버전. "you continue to do the job"은 명령처럼 굳어 있어 keep going without me가 훨씬 자연스럽다.

### 카드 7 — fac_id/fab_name 불일치 보고
- 내가 쓴 영어: "from api, I found that you use fac_id for storage. But we are using fab_name from the left side bar selection. can you fix this mismatch?"   (출처: transcript:[user] skewnono_v3_nuxt 92aad678)
- 정정: 문법 오류 없음. "side bar"는 한 단어 sidebar가 표준 표기.
- 더 나은 표현: "Looking at the API, I noticed storage filters by fac_id, while the left-sidebar selection sends fab_name. Can you fix this mismatch?"
- 왜: found도 맞지만 noticed(눈에 띄었다)가 관찰 보고의 어감에 더 맞다. 두 문장을 while로 이으면 "한쪽은 A, 다른 쪽은 B"라는 대비가 mismatch라는 결론과 구조적으로 연결된다. 이 문장은 원문도 이미 훌륭하다 — 문제·대비·요청이 세 문장에 다 있다.
