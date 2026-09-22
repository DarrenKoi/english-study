# 2026-09-23 — 코칭

> 오늘 `[user]` 한국어는 auto-recipe-creator 세션 3건과 pm-notes-orchestration 세션 2건에서 나왔다. (a) 카드는 9장. "manual_align_correction.py 하고 난 뒤 녹화를 영상으로" 메시지는 어제(09-22) 카드 1로 이미 다뤘고 "커밋하고 푸시해줘"·"commit and push" 는 고칠 데가 없어 뺐다. (b) 는 pm-notes-orchestration 과 auto-recipe-creator 의 어시스턴트 한국어에서 4문장. 영어 다듬기는 equipment-data-map 세션이 가장 많아 14장, auto-recipe-creator 2장, skewnono 2장으로 18장이다. herdr·browser-verify 스킬 본문은 `[user]` 로 찍혔어도 내가 쓴 글이 아니라 제외했다.

## 한글→영어

### 카드 1 — 루트 전체 탐색 금지가 적용돼 있나   (내가 쓴 한글)
- 내가 쓴 한글: "scout 모델 케이스 주의 루트 전체 탐색 금지가 적용되어 있나? 전체 루트 /find로 인해 타임아웃 방지가 필요해"   (출처: transcript:[user] pm-notes-orchestration)
- 자연스러운 영어: For the scout model, is the "no full-root search" rule actually in place? We need to prevent timeouts caused by running `find` on the whole root.
- 왜 이렇게: "적용되어 있나"는 규칙이 주어이므로 `is … in place` 나 `is … enforced`. "타임아웃 방지가 필요해"는 명사 "방지"를 동사 `prevent` 로 되돌리는 게 자연스럽다. "~로 인해"는 `caused by` 로 원인만 붙이면 되고 `due to` 는 문장 앞머리에서 어색하다. "케이스 주의"처럼 메모식 조각은 영어로는 `For the scout model,` 하나로 문맥을 잡는다.

### 카드 2 — 운영 안정성을 더하는 일이면 진행해   (내가 쓴 한글)
- 내가 쓴 한글: "운영에 안정성을 더하는 작업이면 진행해도 좋아"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: If it makes operations more robust, go ahead.
- 왜 이렇게: "안정성을 더하다"를 `add stability` 로 직역하면 어색하다. 형용사 비교급 `more robust` 나 `more reliable` 이 영어의 결. "진행해도 좋아"는 허락이므로 `go ahead` 두 단어면 충분하고 격식을 올리면 `feel free to proceed`.

### 카드 3 — 커밋 상태 보고 업데이트 가능하면 진행해   (내가 쓴 한글)
- 내가 쓴 한글: "git commit 상태롤 보고 업데이트 가능하면 진행해"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Check the git commit state, and if it's safe to update, go ahead.
- 왜 이렇게: "~을 보고"는 `check … and` 로 두 동작을 잇는다. "업데이트 가능하면"의 "가능"은 여기서 능력이 아니라 "해도 되는지"라 `if it's safe to` 나 `if it's clear to` 가 뜻에 맞고 `if possible` 은 다른 말이 된다. "상태롤"은 "상태를"의 오타.

### 카드 4 — SEM 에는 Dark 모드가 없다   (내가 쓴 한글)
- 내가 쓴 한글: "SEM에는 Dark 모드 없음. Image 드롭다운에 SEM 있음. recipe 등록 극성은 무슨 뜻?"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: SEM has no dark mode. SEM is an option in the Image dropdown. What do you mean by "recipe registration polarity"?
- 왜 이렇게: "~에는 X 없음"은 `X has no …` 로 주어를 바꾸면 짧다. "드롭다운에 SEM 있음"은 `is an option in` 이 "선택지로 들어 있다"를 정확히 담는다. 상대가 만든 용어의 뜻을 물을 때는 `What do you mean by "…"?` 가 정석이고 `What is the meaning of` 는 사전 찾듯 들린다.

### 카드 5 — B 가 맞고 오피스에서 확인할게   (내가 쓴 한글)
- 내가 쓴 한글: "B 맞아, cond.txt에 image mode 필드 있는지 오피스에서 확인할게. 그리고 manual_image_mode_change.py로 인식하고 변경 가능한지 테스트 하고 싶어."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: It's B. I'll check at the office whether cond.txt has an image-mode field. I'd also like to test whether `manual_image_mode_change.py` can detect the current mode and switch it.
- 왜 이렇게: "B 맞아"는 `It's B.` 나 `B is right.` "~있는지 확인할게"는 `check whether` 로 의문의 내용을 절로 넣는다. "인식하고 변경 가능한지"는 동사 둘을 `detect … and switch it` 으로 나란히 두고 `whether … can` 하나로 감싼다. "테스트 하고 싶어"는 `I'd like to test` 가 `I want to test` 보다 협업 채팅에서 부드럽다.

### 카드 6 — 실제 변경 후 테스트했음   (내가 쓴 한글)
- 내가 쓴 한글: "3 실제 변경후 테스트했음. OM-D, SEM 변경 성공. 하지만 다른 모드에서 OM으로 변경 안함. WARNING에서 클릭 안함 읽힘 ['OOM']"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Step 3: tested with real changes. Switching to OM-D and SEM worked. Switching back to OM from another mode didn't, though. The WARNING says it skipped the click and read `['OOM']`.
- 왜 이렇게: 시험 결과 보고는 과거 단순으로 짧게 끊는다. "변경 성공"은 동명사 주어 `Switching to … worked`, "변경 안 함"은 같은 틀에서 `didn't` 로 받으면 대비가 선명하다. "클릭 안함 읽힘"처럼 로그를 요약할 때는 로그를 주어로 세워 `The WARNING says …` 로 쓰고 읽힌 값은 코드 서체로 남긴다. "다른 모드에서 OM 으로"는 `back to OM from another mode`.

### 카드 7 — OM 으로 변경 성공   (내가 쓴 한글)
- 내가 쓴 한글: "OM으로 변경 성공했음"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Switching to OM worked.
- 왜 이렇게: "성공했음"을 `succeeded` 로 옮기면 딱딱하다. 채팅에서는 `worked` 가 "됐다"에 가장 가깝다. 확인 사실을 알릴 때 `Confirmed: OM works now.` 처럼 `Confirmed:` 를 앞세워도 좋다.

### 카드 8 — 제안 1 로 가되 기록만   (내가 쓴 한글)
- 내가 쓴 한글: "일단 제안 1로 가되 기록만 진행. cond.txt에서 단서가 될만한 key와 value를 찾았음"   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Let's go with proposal 1 for now, but recording only. Also, I found a key/value pair in cond.txt that looks like a useful clue.
- 왜 이렇게: "일단"은 `for now`, "~로 가되"는 `go with …, but`. "기록만 진행"은 동사 없이 `recording only` 로 붙이는 게 원문의 압축을 살린다. "단서가 될 만한"은 `that looks like a useful clue` 나 `that might be a clue`. "찾았음"은 발견 보고라 과거 단순 `found`.

### 카드 9 — pi 에서 서브에이전트를 어떻게 활용하나   (내가 쓴 한글)
- 내가 쓴 한글: "pi coding agent에서 subagents들을 어떻게 활용하면 되지?"   (출처: transcript:[user] pm-notes-orchestration)
- 자연스러운 영어: How should I use subagents in the pi coding agent?
- 왜 이렇게: "어떻게 활용하면 되지"의 "되지"는 방법을 묻는 것이라 `How should I` 나 `How do I` 가 맞고 `How can I` 는 가능성을 묻는 뉘앙스다. "subagents들"처럼 영어 복수에 "들"을 겹치지 않는다. 좀 더 여는 질문이면 `What's the best way to use subagents in pi?`

### 카드 10 — 프롬프트 수준 규칙은 강제가 아니다   (고급 한글 · 번역)
- 한글 원문: "이 규칙은 프롬프트 수준이라 강제가 아닙니다. 강제하려면 toolTimeoutMs 를 낮추거나 scout 의 tools 에서 bash 를 빼는 방법이 있는데, 후자는 rg 도 막히므로 권하지 않습니다."   (출처: transcript:[assistant] pm-notes-orchestration)
- 자연스러운 영어: This rule lives at the prompt level, so it isn't enforced. To enforce it, you could lower `toolTimeoutMs` or drop `bash` from the scout's tools, but I don't recommend the latter, since it would block `rg` as well.
- 번역 포인트: "프롬프트 수준이라"의 "~이라"는 원인이므로 `lives at the prompt level, so`. "강제가 아니다"는 명사가 아니라 수동 `isn't enforced` 로. "방법이 있는데 … 권하지 않는다"는 `you could A or B, but I don't recommend the latter` 로 선택지 제시와 판단을 한 문장에 담는다. "후자"는 `the latter` 가 그대로 대응한다.

### 카드 11 — 문자열 정렬에 기대면   (고급 한글 · 번역)
- 한글 원문: "문자열 정렬에 기대면 tag 형식이 바뀌는 순간 순서가 뒤집힙니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: If you rely on string sorting, the order flips the moment the tag format changes.
- 번역 포인트: "~에 기대다"는 `rely on`. "~하는 순간"은 `the moment (that) …` 가 `as soon as` 보다 급작스러움을 살린다. "순서가 뒤집히다"는 `the order flips` 가 `is reversed` 보다 짧고 구어적이다.

### 카드 12 — 분석이 아니라 실행 가능한 검증   (고급 한글 · 번역)
- 한글 원문: "즉 '반전이면 정답 위에서도 match 임계에 도달할 수 없다'가 분석이 아니라 실행 가능한 검증이 됐습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: In other words, "an inverted frame can't reach the match threshold even at the correct position" is no longer an analysis but a runnable check.
- 번역 포인트: 주장 자체를 따옴표로 주어 삼는 구조는 영어에서도 그대로 통한다. "분석이 아니라 검증이 됐다"는 상태 변화이므로 `is no longer A but B` 가 `became` 보다 자연스럽다. "실행 가능한"은 테스트 문맥에서 `runnable` 이 관용이고 `executable` 은 바이너리를 떠올리게 한다.

### 카드 13 — 한 번에 한 변수만   (고급 한글 · 번역)
- 한글 원문: "B 를 극성이 틀린 화면에서 시험하면 '격자가 잘못된 건지 극성이 잘못된 건지' 구분이 안 됩니다. 한 번에 한 변수만 바꾸는 쪽이 낫습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: If you test B on a screen with the wrong polarity, you can't tell whether the grid is wrong or the polarity is. Better to change one variable at a time.
- 번역 포인트: "구분이 안 된다"는 `you can't tell whether A or B`. 뒤의 `the polarity is` 처럼 반복되는 형용사를 생략하는 것이 영어식 압축이다. "~하는 쪽이 낫다"는 `It's` 를 떨어뜨린 `Better to …` 가 조언 채팅의 관용이다. "한 번에 한 변수"는 `one variable at a time`.

## 영어 다듬기

### 카드 1 — 이 설정이 꼭 필요한가
- 내가 쓴 영어: "I do not get why we have @engineer.toml.example . is this setting necessary?"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: I don't see why we need `engineer.toml.example`. Is this file actually necessary?
- 왜: 문법 오류는 없음. `I do not get why` 는 구어로는 자연스럽지만 축약 없는 `do not` 과 섞이면 어색하다. `I don't see why` 가 채팅 톤과 맞는다. `.example` 파일은 "setting" 이 아니라 "file" 이라 명사를 맞추면 답이 정확해진다.

### 카드 2 — 채울 항목이 너무 많다
- 내가 쓴 영어: "in rollout.json fields, there are too many items to be filled in. can you reduce the items?"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: `rollout.json` has too many fields to fill in. Can you cut that down?
- 왜: 오류는 아니지만 `items to be filled in` 은 수동이 불필요하다. `to fill in` 으로 충분하다. "the items 를 줄여 달라"는 `cut that down` 이나 `trim the list` 가 `reduce the items` 보다 자연스럽다. 문두 대문자와 파일명 코드 서체는 읽는 이를 위한 예의.

### 카드 3 — 너무 많아서 답답했다
- 내가 쓴 영어: "I was frustrated to many items to be filled in for schema. can you prefill some default values to there if they are low keys."   (출처: transcript:[user] equipment-data-map)
- 정정: `frustrated to many items` → `frustrated by how many items`. `frustrated` 뒤에는 원인을 `by` 나 `with` 로 잇고 `to` 는 쓰지 않는다. `prefill … to there` → `prefill them`. `prefill` 은 타동사라 `to there` 가 붙지 않는다.
- 더 나은 표현: I was frustrated by how many schema fields there are to fill in. Could you prefill the low-stakes ones with defaults?
- 왜: "중요하지 않은 키"를 `low keys` 로 쓰면 "낮은 음의 건반"으로 읽힌다. `low-stakes` 나 `minor` 가 맞다. `Could you` 가 `can you` 보다 부탁 톤이 한 단계 부드럽다.

### 카드 4 — 엔지니어 전용 단계만 관여하나
- 내가 쓴 영어: "we are on letter 16. The enginner only steps should be involed? we have engineer.toml and equipment.toml. are they all used? they seem to have some duplicated info to be filled."   (출처: transcript:[user] equipment-data-map)
- 정정: `enginner`, `involed` 는 `engineer`, `involved` 의 오타. `The engineer only steps should be involved?` 는 평서문에 물음표만 붙인 형태라 뜻이 흐리다. `Which steps are engineer-only?` 처럼 의문사로 시작한다.
- 더 나은 표현: We're at letter 16. Which steps are engineer-only here? We have both `engineer.toml` and `equipment.toml`. Are both still in use? They seem to ask for overlapping information.
- 왜: "letter 16 에 있다"는 `at`. `duplicated info to be filled` 는 `overlapping information` 이나 `the same fields` 로 쓰면 수동 부정사가 사라진다. `Are both still in use?` 가 `are they all used?` 보다 "아직도 쓰이나"라는 의심을 정확히 담는다.

### 카드 5 — budgets 와 용어의 뜻을 모르겠다
- 내가 쓴 영어: "when equipment_map init, I do not understand the meaning of budgets and terms. like realitme_candidates? allowed_roots? can be in a list like ['/HITACHI', '/public']? protocol? access_window?"   (출처: transcript:[user] equipment-data-map)
- 정정: `when equipment_map init` 은 주어·동사가 없는 절이다. `When I run equipment-map init` 으로 채운다. `realitme` 은 `realtime` 의 오타.
- 더 나은 표현: When I run `equipment-map init`, I don't understand what the budgets and some of the terms mean, such as `realtime_candidates`, `allowed_roots` (can it be a list like `['/HITACHI', '/public']`?), `protocol`, and `access_window`.
- 왜: `the meaning of X` 보다 `what X means` 가 구어에서 자연스럽다. 항목을 물음표로 나열하는 대신 `such as` 한 번으로 묶는다. 세부 질문은 괄호 안에 넣으면 읽는 쪽이 한 번에 답할 수 있다.

### 카드 6 — 최대 예산에도 기본값을
- 내가 쓴 영어: "let's also put the default for max budgets. max_download_files 200, total_bytes 500MB, and so on. also ftp concrurrent connection and download. you can use ftp_handler with 6~8 concurrent connection"   (출처: transcript:[user] equipment-data-map)
- 정정: `concrurrent` 는 `concurrent` 의 오타. `6~8 concurrent connection` → `6–8 concurrent connections`. 숫자 범위 뒤 가산명사는 복수이고 물결표(~)는 영어에서 범위 표시로 쓰지 않는다.
- 더 나은 표현: Let's also set defaults for the max budgets: `max_download_files` 200, `total_bytes` 500 MB, and so on. Same for FTP concurrency. `ftp_handler` can handle 6 to 8 concurrent connections.
- 왜: "기본값을 두다"는 `put the default` 가 아니라 `set defaults`. "동시 접속과 다운로드도"는 `Same for FTP concurrency` 로 앞 문장의 틀을 재사용하면 짧다. `you can use X with N connections` 는 도구를 주어로 `X can handle N connections` 라고 하면 능력 진술이 된다.

### 카드 7 — 재시작해서 적용하려면
- 내가 쓴 영어: "commit and push and how can I restart to apply this change?"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Commit and push. Then, how do I restart the office setup to pick up this change?
- 왜: 오류는 없지만 명령과 질문을 `and` 로 이으면 읽기 힘들다. 문장을 끊고 `Then` 으로 잇기. "적용하다"는 여기서 `pick up the change`(변경을 반영해 받다)가 `apply` 보다 상황에 맞는다. 무엇을 재시작하는지 목적어를 주면 답이 정확해진다.

### 카드 8 — 시험 끝났으니 spike.py 는 지워도
- 내가 쓴 영어: "we can get rid of spike.py as we have done the test"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: We can drop `spike.py` now that the test is done.
- 왜: 오류는 없다. `as we have done the test` 는 "우리가 그 시험을 했으므로"인데, 이유가 "시험이 끝난 상태"라면 `now that the test is done` 이 시점까지 담아 더 정확하다. `get rid of` 는 구어로 괜찮고 코드 정리 문맥에서는 `drop` 이나 `remove` 도 흔하다.

### 카드 9 — 에러가 잔뜩 난다
- 내가 쓴 영어: "from equipment-map init --rollout, I face with lots of errors "missing required value" and "missing budget". I think we are agreed to fill in most of them with default values. all I want to do is to add equipment_id, protocol (default ftp), host and port and allowed_roots. the patters for allow and deny, you have to fill in based no our discussion so far. the rest of them should be set by default"   (출처: transcript:[user] equipment-data-map)
- 정정: `I face with lots of errors` → `I'm getting lots of errors` 또는 `I run into lots of errors`. `face` 는 타동사라 `with` 가 붙지 않는다(`face lots of errors`). `we are agreed to fill in` → `we agreed to fill in`. `patters`, `based no` 는 `patterns`, `based on` 의 오타.
- 더 나은 표현: When I run `equipment-map init --rollout`, I get a flood of "missing required value" and "missing budget" errors. I thought we'd agreed to default most of these. All I want to enter is `equipment_id`, `protocol` (default ftp), `host`, `port`, and `allowed_roots`. Fill in the allow/deny patterns based on our discussion so far, and default everything else.
- 왜: "채우다"를 매번 `fill in with default values` 로 쓰지 말고 `default` 를 동사로 쓰면(`default most of these`) 짧아진다. `I thought we'd agreed` 는 "그렇게 합의한 걸로 아는데"라는 가벼운 항의를 담는다. `All I want to enter is …` 로 목록 앞에 틀을 세우면 "나머지는 기본값"이 자연스럽게 따라온다.

### 카드 10 — LLM 이 채우게 하자
- 내가 쓴 영어: "even when I try with init, let the llm fill in (or ask what to add like equipment id, ip, port)"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Even for `init`, let the LLM fill things in, or have it ask me for what it needs, like the equipment ID, IP, and port.
- 왜: 오류는 없지만 `try with init` 은 "init 으로 시도하다"라 의도(init 단계에서도)가 흐리다. `Even for init` 이 명확하다. "물어보게 하자"는 사역 `have it ask me` 가 자연스럽고 `LLM` 은 대문자 약어다.

### 카드 11 — 0 of 78 이 나온다, 왜?
- 내가 쓴 영어: "run reset_model_folder.py and see 0 of 78 files changed. why?" / "ran it twice"   (출처: transcript:[user] equipment-data-map)
- 정정: `run … and see` 는 명령문으로 읽혀 "너가 실행해서 봐라"가 된다. 내가 한 일이면 과거형 주어가 필요하다. `I ran … and it says …`
- 더 나은 표현: I ran `reset_model_folder.py` and it reported "0 of 78 files changed". Why? / I ran it twice.
- 왜: 스크립트 출력을 인용할 때는 스크립트를 주어로 `it reported …` 나 `it says …`. 후속 답 `ran it twice` 는 채팅에서 주어를 떨어뜨려도 통하지만 `I ran it twice.` 로 온전히 쓰면 앞 질문과 시제가 맞는다.

### 카드 12 — 장비 정보 파일을 init 에 넘기고 싶다
- 내가 쓴 영어: "I want to fill in engineer.toml that contains tool name, ip, id, pw and I can designate this toml file to the init so that it goes to run and the file doesn't need to be in the specific folder. (I am thinking of placing them in a folder and let the llm reads one of them and go for the mapping-out work. Anyways, we can add a step to fill in equipment.toml to help engineers instead of handwriting all of the items."   (출처: transcript:[user] equipment-data-map)
- 정정: `let the llm reads` → `let the LLM read`. `let` 뒤 동사는 원형. `designate this toml file to the init` → `point init at this TOML file`. `designate X to Y` 는 "X 를 Y 로 임명하다"라 뜻이 어긋난다.
- 더 나은 표현: I'd like to fill in an `engineer.toml` with the tool name, IP, ID, and password, then point `init` at that file so it runs from there and the file doesn't have to sit in a specific folder. I'm thinking of keeping several of these in one folder and letting the LLM pick one and start the mapping work. Either way, let's add a step that fills in `equipment.toml` for engineers instead of making them type every item by hand.
- 왜: 긴 문장은 `then` 과 `so` 로 인과를 세우면 따라가기 쉽다. "손으로 다 적다"는 `handwriting` 이 아니라 `type … by hand` 또는 `fill in by hand`. `handwriting` 은 종이에 손글씨를 쓰는 것이다. `Anyways` 는 비표준이고 `Anyway` 또는 `Either way` 가 맞다.

### 카드 13 — 왜 손으로 채워야 하나
- 내가 쓴 영어: "why do I need to fill in budget and other info by handwriting? aren't we agreed to set them with default values that can be generally used?"   (출처: transcript:[user] equipment-data-map)
- 정정: `by handwriting` → `by hand`. `aren't we agreed to` → `didn't we agree to`. 합의는 과거의 행위라 `agree` 동사의 과거형으로 묻는다.
- 더 나은 표현: Why do I still have to fill in the budgets and the rest by hand? Didn't we agree to give them sensible defaults?
- 왜: "아직도"의 항의 톤은 `still` 하나가 살린다. "일반적으로 쓸 수 있는 기본값"은 관용구 `sensible defaults` 가 정확히 그 뜻이다. `default values that can be generally used` 는 문법은 맞지만 늘어진다.

### 카드 14 — 빈 토큰이 인증을 켠다
- 내가 쓴 영어: "from letter 16, there are problems to be solved. FTP_PROXY_TOKEN, the documented empty-means-no-auto intent fails. we do not use PROXY_TOKEN for ftp. it can be used with "" empty string."   (출처: transcript:[user] equipment-data-map)
- 정정: `empty-means-no-auto` 는 `empty-means-no-auth` 의 오타로 보인다(auth = 인증). `it can be used with "" empty string` 은 주어 `it` 이 무엇인지 흐리다.
- 더 나은 표현: Letter 16 turned up a problem. `FTP_PROXY_TOKEN` doesn't behave as documented: an empty value is supposed to mean "no auth", but that fails. We don't use a proxy token for FTP, so it should work when the variable is set to an empty string.
- 왜: "문제가 있다"를 `there are problems to be solved` 로 쓰면 무엇이 문제인지 한 박자 늦는다. `X doesn't behave as documented:` 뒤에 기대와 실제를 대비시키면 버그 리포트의 틀이 된다. "빈 문자열로 쓸 수 있어야 한다"는 요구이므로 `should work when … is set to an empty string`.

### 카드 15 — Scope 는 OM 과 SEM
- 내가 쓴 영어: "Scope we have "OM" and "SEM". for "OM", in cond.txt we also do have "Magnification" as a key and the value is 104 or 210, and I assume that the key "!OM_Brightness" indicates dark mode or not. if it is below than 35000, we have to use OM-D mode from Image dropdown."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `below than 35000` → `below 35000`. `below` 는 전치사라 `than` 이 붙지 않는다(`lower than` 은 가능). `indicates dark mode or not` → `indicates whether it's dark mode`. `or not` 을 붙이려면 `whether` 가 앞에 있어야 한다.
- 더 나은 표현: For Scope we have "OM" and "SEM". For "OM", cond.txt also has a `Magnification` key whose value is 104 or 210, and I assume `!OM_Brightness` tells us whether it's dark mode: if it's below 35000, we should use OM-D from the Image dropdown.
- 왜: `we also do have` 의 `do` 는 강조인데 여기서는 강조할 이유가 없다. `whose value is` 로 키와 값을 한 절에 묶으면 `as a key and the value is` 의 나열이 사라진다. 가정과 조건을 콜론으로 이으면 "밝기 → 판정" 관계가 한눈에 보인다.

### 카드 16 — 정확히 일치하는 recipe 를 먼저
- 내가 쓴 영어: "in skewvoir search, let's say, I search with recipe:RJ1BXXX_CG6300/RJ1B_BG. The result contains lots of RJ1BXXX_CG6300/RJ1B_BGHMPOEB, and other recipe strings same as upto BG. when I search with that recipe name, can you give me more accurate result like RJ1BXXX_CG6300/RJ1B_BG exact matching show up first and than other other recipe names."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `and than other other recipe names` → `and then the other recipe names`. 순서의 `then` 과 비교의 `than` 이 바뀌었고 `other` 가 겹쳤다. `more accurate result` → `more accurate results`(가산명사 복수). `strings same as upto BG` → `strings that match up to BG`.
- 더 나은 표현: In the skewvoir search, say I search for `recipe:RJ1BXXX_CG6300/RJ1B_BG`. The results are full of `RJ1BXXX_CG6300/RJ1B_BGHMPOEB` and other recipes that match only up to "BG". Could exact matches show up first, and the rest after?
- 왜: "예를 들어 …라고 하자"는 `say I …` 나 `let's say I …` 로 문장 앞에 붙인다. "정확히 일치하는 것"은 명사 `exact matches` 가 `exact matching` 보다 자연스럽다. 요청은 `Could exact matches show up first` 처럼 결과를 주어로 세우면 짧다.

### 카드 17 — 다른 페이지처럼 스큐보아 링크 추가
- 내가 쓴 영어: "in <- Recipe 검색으로 component that is available in recipe-search/* . We do still have 열어보기, 횡전개, 측정 이력. add skewvoir link like we have done in other pages."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `in other pages` → `on other pages`. 웹 페이지 위의 요소는 `on the page`.
- 더 나은 표현: In the component with the "← Recipe 검색으로" back link under `recipe-search/*`, we still have 열어보기, 횡전개, and 측정 이력. Add a skewvoir link there, the way we did on the other pages.
- 왜: 어느 컴포넌트인지 `the component with the "…" back link` 로 특정하면 상대가 찾기 쉽다. "우리가 했던 것처럼"은 `the way we did` 나 `like we did` 가 `like we have done` 보다 채팅에 맞는다.

### 카드 18 — 버튼이 겹쳐서 OOM 으로 보인다
- 내가 쓴 영어: "I see. when you click Image dropdown box, the button Optipcs.. that is right below the button, they are overlayed so that it looks like OOM" / "considering the fac that we have Optics... and OM ABC buttons are right below the Image dropdown box, OCR or vlm might confisued."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `overlayed` → `overlaid`(overlay 의 과거분사). `Optipcs`, `fac`, `confisued` 는 `Optics`, `fact`, `confused` 의 오타. `might confisued` → `might get confused` 또는 `might be confused`. 조동사 뒤에는 동사 원형이 와야 한다.
- 더 나은 표현: I see. When you open the Image dropdown, the list overlaps the "Optics..." button right below it, so it reads as "OOM". Given that "Optics..." and "OM ABC" sit right under the Image dropdown, the OCR or the VLM could easily get confused.
- 왜: "겹쳐서 OOM 으로 보인다"는 목록을 주어로 `the list overlaps the button, so it reads as "OOM"`. `reads as` 는 "그렇게 읽힌다"는 OCR 문맥의 관용. `considering the fact that` 은 `given that` 세 단어로 준다. "혼동할지도"는 `could easily get confused` 가 가능성과 이유를 함께 담는다.
