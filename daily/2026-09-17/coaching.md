# 2026-09-17 — 코칭

> 오늘 transcript 의 `[user]` 메시지는 전부 영어라 한글→영어 (a) 카드가 없다. `[assistant]` 도 영어로만 답해서 (b) 번역 정독 대상도 없다. 답변 안에 인용된 한국어 한 줄은 스펙 문서 원문이라 코칭 소스에서 뺐다. 영어 다듬기는 두 저장소(auto-recipe-creator, equipment-data-map)의 `[user]` 문장에서 14장을 만들었고, `push it`, `commit and push`, `pi-subagents is installed`, `now give me the prompt to run` 은 고칠 데가 없고 더 나은 표현을 제안할 여지도 적어 뺐다.

## 영어 다듬기

### 카드 1 — 로그가 너무 많다
- 내가 쓴 영어: "when I run @poc/…/manual_align_correction.py and @poc/…/align_fail_monitor.py there are too many [INFO] shows up in the console, so I think I miss lots of important information. can we trim down some RCS related info (I think we have almost done for automation for RCS part, no issues so far)"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `there are too many [INFO] shows up` → `too many [INFO] lines show up`. `there are` 구문과 동사 `shows up` 이 한 절에 겹쳤으니 하나만 남긴다(`there are too many [INFO] lines showing up` 도 된다). `I think I miss` → `I'm missing`. 지금 계속 놓치는 중이라 현재진행이 맞다. `we have almost done for automation for RCS part` → `we're almost done automating the RCS part`. "~하는 걸 거의 끝냈다"는 `be done + -ing` 이고, `have done` 은 뒤에 목적어가 와야 한다. 명사 앞 복합형용사는 `RCS-related` 로 하이픈을 넣는다.
- 더 나은 표현: When I run manual_align_correction.py and align_fail_monitor.py, the console gets flooded with [INFO] lines and I end up missing important messages. Can we trim down the RCS-related output? The RCS automation is pretty much done and hasn't caused any issues so far.
- 왜: `gets flooded with` 는 "너무 많이 뜬다"를 동사 하나로 담는다. `end up missing` 은 원치 않는데 결국 놓치게 된다는 결과를 살린다. 괄호 속 부연은 따로 한 문장으로 빼야 요청이 먼저 읽힌다.

### 카드 2 — 사무실 진행 상황 보고와 질문
- 내가 쓴 영어: "In my office, I ran a previous parser version upto 14 letters. … the office wants to write down into skills for the discovery roots for each coding harness / the office wants to write the installers and the run the full Done-when. but we have changed the parser md contents recently. Should I re-run the parser folder and discarding the previous version's results?"   (출처: transcript:[user] equipment-data-map)
- 정정: `upto` → `up to` (두 단어). 다만 `up to 14 letters` 는 "최대 14통"으로 읽히니, 14번까지 순서대로 했다는 뜻이면 `through letter 14` 가 정확하다. `write down into skills for the discovery roots` → `write the discovery roots into the skills` (write A into B 로 목적어를 앞에 세우고 `down` 은 뺀다). `and the run` → `and then run` (오타). `Should I re-run … and discarding` → `and discard`. 조동사 `should` 뒤에서 두 동사가 병렬이니 둘 다 원형이어야 한다.
- 더 나은 표현: At the office, I ran the previous parser version through letter 14, which built equipment-map-suite and the six skills. The office LLM asked me to confirm the four discovery roots, so I appended a "14 confirmed" line to progress.md. Next, it wants to write the discovery roots into the skills for each coding harness, write the installers, and run the full Done-when. But we've recently changed the parser .md files. Should I re-run the parser folder from scratch and discard the previous results?
- 왜: `In my office` 는 "내 사무실 방 안에서"처럼 들려 직장을 말할 때는 `At the office` 가 자연스럽다. 줄마다 흩어진 메모를 시간순 문장으로 이으면 상대가 상황을 한 번에 잡는다. `the office wants to …` 가 두 줄 반복됐던 것도 `Next, it wants to A, B, and C` 한 문장으로 합쳤다.

### 카드 3 — 필요한 폴더만 갱신
- 내가 쓴 영어: "no, instead, @tools/reset_model_folder.py make sure only refresh folders only needed. the outputs from the office llm learning should not be touched."   (출처: transcript:[user] equipment-data-map)
- 정정: `make sure only refresh folders only needed` → `make sure it refreshes only the folders that need it`. `make sure` 뒤에는 주어 + 동사가 갖춰진 절이 와야 하고 동사원형만 올 수는 없다. `only` 가 두 번 들어간 것도 하나로 줄인다. 문장 맨 앞의 파일 경로는 문법상 어디에도 걸리지 않아 떠 있으니 목적어 자리로 옮긴다. `llm learning` 의 `learning` 은 "학습 과정"이라 여기서 뜻한 산출물과 맞지 않는다.
- 더 나은 표현: No — instead, change @tools/reset_model_folder.py so it refreshes only the folders that need it. Anything the office LLM has produced must stay untouched.
- 왜: 파일을 고쳐 달라는 요청이니 `change X so it …` 틀이 깔끔하다. `must stay untouched` 는 `should not be touched` 보다 어길 수 없는 규칙처럼 들린다.

### 카드 4 — 기본 모드로 바꾸기
- 내가 쓴 영어: "can you make refresh mode as default? so that I do not need to type --refresh"   (출처: transcript:[user] equipment-data-map)
- 정정: `make refresh mode as default` → `make refresh mode the default`. `make + 목적어 + 명사 보어` 에는 `as` 를 넣지 않는다(`set X as the default` 는 가능). `default` 앞에는 `the` 가 필요하다. `so that …` 은 떨어진 조각이라 앞 문장에 붙인다.
- 더 나은 표현: Can you make refresh the default mode, so I don't have to type --refresh every time?
- 왜: 한국어 "~로 만들다"를 옮기다 보면 `as` 가 끼기 쉽다. `make it the default` 와 `set it as the default` 두 틀만 구분해 두면 된다. 끝에 `every time` 을 붙이면 반복되는 번거로움이 이유라는 점이 산다.

### 카드 5 — 사람이 적는 기록 줄이 왜 필요해?
- 내가 쓴 영어: "I do not understand why human record line is needed? just let the llm confirm by himself or ask me about that and fill up the contents"   (출처: transcript:[user] equipment-data-map)
- 정정: `I do not understand why … is needed?` 는 간접의문을 품은 평서문이라 마침표로 끝낸다. 물음표를 쓰려면 `Why is the human record line needed?` 로 바꾼다. `human record line` → `the human record line` (앞서 나온 그 줄이라 정관사). `by himself` → `by itself` (LLM 은 `it`). `fill up the contents` → `fill in the contents`. 빈칸이나 양식을 채우는 건 `fill in` 이고, `fill up` 은 그릇·탱크를 가득 채운다는 뜻이다.
- 더 나은 표현: I don't see why the human record line is needed. Just let the LLM confirm it on its own, or have it ask me and fill in the details.
- 왜: `I don't see why` 는 "이해가 안 된다"를 가벼운 반박조로 말하는 구어 정형이다. `have it ask me` 는 사역 have 로 LLM 에게 일을 시키는 구조를 만든다.

### 카드 6 — 속도를 올릴 방법
- 내가 쓴 영어: "any idea to expedite the running? I do test mostly with pi coding agent and you can spawn multiple pi coding (in herdr skills with multiple tabs, which are also installed in office PC). I think you can open 2~3 pi tabs to run some of jobs simultaneously."   (출처: transcript:[user] equipment-data-map)
- 정정: `any idea to expedite the running` → `any ideas for speeding up the run`. `idea` 뒤에는 to부정사보다 `for -ing` 나 `on how to` 가 자연스럽고, `the running` 은 명사로 어색하다. `I do test mostly with pi coding agent` → `I mostly test with the pi coding agent` (강조의 `do` 는 필요 없고 빈도부사는 동사 앞, 관사 추가). `spawn multiple pi coding` → `spawn multiple pi coding agents` (명사가 빠졌다). `installed in office PC` → `installed on the office PC`. `some of jobs` → `some of the jobs`. `some of` 뒤에는 `the` 같은 한정사가 있어야 한다.
- 더 나은 표현: Any ideas for speeding this up? I mostly test with the pi coding agent, and you can spawn multiple pi agents in separate tabs with the herdr skill, which is also installed on the office PC. Maybe open two or three pi tabs and run some of the jobs in parallel?
- 왜: `expedite` 는 서류 처리나 배송을 앞당길 때 쓰는 격식 어휘라 채팅에서는 `speed up` 이 맞는다. `2~3` 의 물결표는 영어에서 범위 표시로 쓰지 않는다. `2–3` 이나 `two or three` 로 적는다.

### 카드 7 — 규칙을 바꾸고 병렬로 돌리기
- 내가 쓴 영어: "we remove the rule that one model runs the whole letter sequence. Instead of using herdr skills, let pi agent spawns subagents or with one shot prompt method so that we can make it faster if the jobs are not interfere each other. We now only focus on pi aagent only. Can you add the instruction for md files in the parser folder? check if it can be run parallel."   (출처: transcript:[user] equipment-data-map)
- 정정: `we remove` → `let's remove` 또는 `we're removing`. 결정을 알리는 말이라 단순현재는 어색하다. `let pi agent spawns` → `let the pi agent spawn` (let + 목적어 + 동사원형). `or with one shot prompt method` → `or use one-shot prompts` (앞의 동사 `spawn` 과 병렬을 맞춘다). `if the jobs are not interfere each other` → `as long as the jobs don't interfere with each other`. be 동사와 일반동사가 겹쳤고, `interfere` 는 자동사라 `with` 가 필요하다. `only focus on pi aagent only` → `focus on the pi agent only` (`only` 중복, 오타). `run parallel` → `run in parallel`.
- 더 나은 표현: Let's drop the rule that one model runs the whole letter sequence. Instead of the herdr skill, have the pi agent spawn subagents or use one-shot prompts, so jobs that don't interfere with each other can run at the same time. From now on we're focusing on pi only. Can you add instructions for this to the .md files in the parser folder, and check whether the letters can actually run in parallel?
- 왜: `as long as` 나 관계절 `jobs that don't interfere` 가 "간섭하지 않는 작업이면"이라는 조건을 정확히 건다. `if` 는 "간섭하지 않는다면(그럴지 모르겠지만)"처럼 가정으로 흐른다. 마지막 두 요청은 `and` 로 묶어 한 번에 읽히게 했다.

### 카드 8 — "Keep that rule, it's fine"
- 내가 쓴 영어: "keep that rule, it's fine"   (출처: transcript:[user] equipment-data-map)
- 정정: 독립절 두 개를 쉼표 하나로만 이었다(comma splice). 채팅에서는 흔히 보지만 글에서는 세미콜론·마침표·대시로 끊는다.
- 더 나은 표현: Keep that rule — it's fine as is.
- 왜: 대시는 채팅과 문서 양쪽에서 무난하게 두 절을 잇는다. `as is` 를 붙이면 "손대지 말고 지금 그대로"라는 뜻이 분명해진다.

### 카드 9 — 짧은 요청과 질문
- 내가 쓴 영어: "give me the prompt to run for office llm" / "and how pi agents run in pararelle?"   (출처: transcript:[user] equipment-data-map)
- 정정: `for office llm` → `on the office LLM`. 모델 위에서 돌리는 것이라 `on` 이고 관사가 필요하다. `and how pi agents run in pararelle?` → `And how do pi agents run in parallel?` 직접의문문은 조동사 `do` 를 앞으로 보내 도치한다. 철자는 `parallel` 로, 가운데 `ll` 이 두 개이고 끝은 `-el` 이다.
- 더 나은 표현: Give me the prompt to run on the office LLM. / And how exactly do the pi agents run in parallel?
- 왜: 평서 어순 `how pi agents run` 은 `I wonder how pi agents run …` 처럼 다른 문장 안에 들어간 간접의문에서만 쓴다. `exactly` 를 넣으면 원리를 구체적으로 알고 싶다는 뜻이 선다.

### 카드 10 — 프록시 필수 규칙 확인
- 내가 쓴 영어: "you know it is mendatory to use proxy from ftp_handler.py in Windows. have you stated that comment in the index.md?"   (출처: transcript:[user] equipment-data-map)
- 정정: `mendatory` → `mandatory` (철자). `use proxy` → `use the proxy` (정해진 그 프록시). `in Windows` → `on Windows`. OS 위에서 돌아가는 건 `on` 이다. `have you stated that comment` → `have you stated that`. `state` 는 사실·규칙을 목적어로 받지 `comment` 와는 잘 붙지 않는다. 파일명 `index.md` 앞의 `the` 도 빼는 편이 자연스럽다.
- 더 나은 표현: As you know, going through the proxy in ftp_handler.py is mandatory on Windows. Is that stated anywhere in index.md?
- 왜: 문장 첫머리 `you know` 는 "알잖아" 정도로 가볍고 따지는 투로도 들릴 수 있다. 상기시키는 말이면 `As you know,` 가 정돈돼 보인다. `Is that stated anywhere in …?` 는 "혹시 빠졌나" 하는 확인 뉘앙스까지 담는다.

### 카드 11 — 결과물로 무엇을 받게 되나
- 내가 쓴 영어: "once the whole cycle finishes, what do I expect to get as result? skills? scripts?"   (출처: transcript:[user] equipment-data-map)
- 정정: `as result` → 관사가 빠졌는데, `as a result` 로 고쳐도 "그 결과로"라는 연결 부사로 굳어 있어 뜻이 틀어진다. `as the output` 이나 `out of it` 으로 바꾼다. `what do I expect` → `what should I expect`. 내 기대가 무엇인지 묻는 게 아니라 무엇을 기대하면 되는지 묻는 말이다.
- 더 나은 표현: Once the whole cycle finishes, what should I expect to end up with — skills, scripts, or something else?
- 왜: `end up with` 는 긴 과정 끝에 손에 쥐게 되는 것을 가리키는 구어다. 조각 질문 `skills? scripts?` 는 대시 뒤 선택지 목록으로 합쳤다.

### 카드 12 — 새 조건을 만나면 어떻게 개선하나
- 내가 쓴 영어: "20-letter sequence is a one-time bootstrap and once we have scripts and skills, how can I improve if I face with the new conditions from other tools? how can we improve the scripts and skills."   (출처: transcript:[user] equipment-data-map)
- 정정: `20-letter sequence` → `The 20-letter sequence` (특정 대상이라 정관사). `if I face with` → `if I face` 또는 `if I'm faced with`. 능동 `face` 는 타동사라 `with` 없이 목적어를 받고, `with` 는 수동 `be faced with` 에만 붙는다. `how can I improve` 에는 목적어(`them`)가 필요하다. 마지막 문장은 의문문이니 물음표로 끝낸다.
- 더 나은 표현: So the 20-letter sequence is a one-time bootstrap. Once we have the scripts and skills, how do we improve them when we run into new conditions on other equipment?
- 왜: 같은 질문이 두 번 들어가 있어 한 문장으로 합쳤다. `run into` 는 예상 못 한 상황을 "마주치다"라는 구어로 `face` 보다 가볍다. 대화 맥락에서 other tools 는 다른 장비를 가리키니 `other equipment` 라고 써야 코딩 도구와 헷갈리지 않는다.

### 카드 13 — 마우스 이동이 전부 드래그인가
- 내가 쓴 영어: "Now we all use mouse dragging when you move mouse around?"   (출처: transcript:[user] equipment-data-map)
- 정정: 평서 어순 끝에 물음표만 달았다. 말로 할 때는 억양으로 묻는 게 통하지만 글에서는 `Do we now …?` 로 도치한다. 주어가 `we` 와 `you` 로 엇갈린 것도 하나로 맞춘다. `mouse` 앞에는 `the` 가 필요하다.
- 더 나은 표현: So is every mouse movement a drag now? / Are we now dragging whenever we move the mouse?
- 왜: 평서문에 물음표만 붙이면 "설마 그렇다고?" 하는 놀람이 섞여 들린다. 중립적으로 확인하려면 도치형이 안전하다. 첫 번째 제안은 주어를 동작(`every mouse movement`)으로 바꿔 더 짧게 물었다.

### 카드 14 — Markdown 을 HTML 로
- 내가 쓴 영어: "convert the md into html so that I can read with ease."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `read with ease` → `read it with ease`. 목적어 없는 `read` 는 "책을 읽다, 독서하다"처럼 읽히니 무엇을 읽는지 `it` 을 넣는다.
- 더 나은 표현: Convert the .md to HTML so it's easier to read.
- 왜: `with ease` 는 문어적이라 짧은 지시문에서 튄다. `so it's easier to read` 처럼 문서를 주어로 세우면 더 짧고 구어답다. 원래 문장도 뜻은 충분히 통한다.
