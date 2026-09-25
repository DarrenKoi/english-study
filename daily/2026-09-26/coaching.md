# 2026-09-26 — 코칭

> 오늘 `[user]` 한국어는 equipment-data-map 세션의 지시 세 개와 skewnono 세션의 안내 문구 하나였고 이 넷으로 (a) 카드를 만들었다. (b) 는 ftp_handler 포팅 보고에 나온 어시스턴트의 한국어에서 네 문장을 골랐다. 영어 다듬기는 27장. "commit and push", "close the codex tab" 처럼 고칠 게 없는 짧은 명령은 뺐다. english-study 파이프라인 프롬프트와 herdr·writing-for-agents·grilling 스킬 본문은 `[user]` 로 찍혔어도 내가 쓴 글이 아니라서 제외했다.

## 한글→영어

### 카드 1 — 필요할 때 추가하자   (내가 쓴 한글)
- 내가 쓴 한글: "spike 스크립트 써줘. 그리고 SMB는 아직 사용 안하니 제거하자. (필요할 때 추가)."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Write the spike script. And since we don't use SMB yet, let's drop it — we can add it back when we need it.
- 왜 이렇게: "아직 사용 안 하니"는 이유라서 `since` 로 앞에 세운다. "제거하자"는 코드·문서에서 빼는 일이라 `remove` 도 되지만 기능 범위를 덜어 낼 땐 `drop` 이 더 자연스럽다. 괄호 속 "(필요할 때 추가)"는 한국어에선 메모처럼 통해도 영어에선 `we can add it back when we need it` 으로 문장을 살려야 의도가 분명해진다. `back` 을 넣으면 "지웠다가 되살린다"는 뜻까지 살고.

### 카드 2 — 윈도우가 필수, 체크포인트는 완화   (내가 쓴 한글)
- 내가 쓴 한글: "윈도우가 필수. 먼저 윈도우 (must: ftp_handler proxy 사용) 그리고 SMB는 아직 사용 안하니 제거하자. (필요할 때 추가). blocked 제거. keystore waiting 풀기. 세세한 체크포인트도 완화."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Windows is a must, so do Windows first, and it has to go through the ftp_handler proxy. Drop SMB for now since we don't use it yet; we can add it back later. Also remove the `blocked` state, lift the keystore wait, and relax the fine-grained checkpoints.
- 왜 이렇게: 명사형으로 끊어 쓴 지시를 영어로 옮길 땐 동사를 하나씩 붙여 나열한다(`remove`, `lift`, `relax`). "waiting 풀기"의 "풀다"는 보류를 해제하는 뜻이라 `lift` 가 맞는다(`lift a ban`, `lift a restriction`). "완화"는 `relax` 가 규칙·조건을 느슨하게 할 때 쓰는 말이다. "세세한"은 `fine-grained` 가 개발 문서에서 흔한 표현이다.

### 카드 3 — 변경분을 포팅하자   (내가 쓴 한글)
- 내가 쓴 한글: "ftp_handler 변경분을 skewnono_v3_nuxt, flask_modules에 포팅하자"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Let's port the ftp_handler changes to skewnono_v3_nuxt and flask_modules.
- 왜 이렇게: "변경분"은 `the changes` 한 단어면 된다. `the changed part` 로 옮기면 어색하다. `port A to B` 가 정해진 짝이라 전치사는 `to` 다(`port into` 는 드묾). 한국어의 쉼표 나열은 영어에선 둘일 때 `and` 로 잇는다.

### 카드 4 — 모든 페이지에 적용됩니다   (내가 쓴 한글)
- 내가 쓴 한글: "여기에서 설정된 장비군은 모든 페이지 영역에 적용됩니다."   (출처: transcript:[user] skewnono-v3-nuxt, 즐겨찾기 안내 문구)
- 자연스러운 영어: Tools you select here apply across all pages.
- 왜 이렇게: 화면 안내문은 짧을수록 좋다. "설정된"을 수동 `that are set here` 로 옮기면 길어지니 사용자를 주어로 한 `you select here` 로 바꿨다. "모든 페이지 영역에"의 "영역"은 영어에서 덧말이라 빼고 `across all pages` 로 "전체에 걸쳐"를 살렸다. "장비군"은 문맥상 고른 장비 목록이니 `tools` 면 충분하고.

### 카드 5 — 블로커의 실체   (고급 한글 · 번역)
- 한글 원문: "블로커의 실체는 "vendor에 mtime이 없다"가 아니라 "listing에 없다"였다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: The real blocker wasn't that the vendor code had no mtime; it was that the listing didn't carry it.
- 번역 포인트: "~의 실체는"을 `the substance of` 로 직역하면 무겁다. `The real blocker` 처럼 형용사 `real` 하나로 "겉보기와 다른 진짜"를 담는다. "A가 아니라 B였다"는 `It wasn't A; it was B` 로 두 절을 세미콜론으로 대비시키면 리듬이 원문과 같아진다. 따옴표 속 인용은 `that` 절로 풀어야 영어 문장에 자연스럽게 들어가고.

### 카드 6 — 우회로가 원래 길보다 나은 드문 경우   (고급 한글 · 번역)
- 한글 원문: "우회로가 원래 길보다 나은 드문 경우."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: A rare case where the workaround beats the intended path.
- 번역 포인트: "우회로"는 개발 맥락에서 `workaround`, "원래 길"은 `the intended path` 나 `the original route` 다. "~보다 낫다"를 `is better than` 대신 `beats` 로 쓰면 짧고 구어 맛이 살아 원문의 가벼운 결말 톤과 맞는다. 명사구로 끝나는 한국어 문장은 영어에서도 `A rare case where …` 조각문으로 두면 된다.

### 카드 7 — 계약이 best-effort면 catch도 total이어야   (고급 한글 · 번역)
- 한글 원문: "계약이 best-effort면 catch도 total이어야 한다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: If the contract is best-effort, the catch has to be total too.
- 번역 포인트: 한국어가 이미 영어 용어를 섞어 쓴 문장이라 구조만 맞추면 된다. "~도"는 문장 끝 `too` 로, "~이어야 한다"는 규칙에서 나오는 필연이라 `should` 보다 `has to` 가 세다. 원칙을 선언하는 짧은 조건문이라 `If A, B` 한 줄로 두는 편이 힘이 있다.

### 카드 8 — 검사지 배포가 아니다   (고급 한글 · 번역)
- 한글 원문: "다만 그건 검사지 배포가 아니다. proxy 배포는 사람이 해야 한다."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: But that's a check, not a deployment. Someone still has to deploy the proxy by hand.
- 번역 포인트: "A지 B가 아니다"는 영어의 `A, not B` 대비와 딱 맞는다. "사람이 해야 한다"를 `a human must do` 로 옮기면 딱딱하니 `Someone still has to … by hand` 로 풀었다. `still` 이 "검사가 있어도 여전히"라는 앞 문장과의 연결을 맡는다.

## 영어 다듬기

### 카드 9 — 탭 2 보고서를 검토하고 고쳐 줘
- 내가 쓴 영어: "with herder skill, check the tab 2, which is the report on possible issues when I deploy the workflow_3 in real work place, give your thought and if it is agreeable, go fix"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `herder` → `herdr`(도구 이름). `the tab 2` → `tab 2`(번호가 붙은 이름엔 관사 없음). `in real work place` → `in the real workplace`(`workplace` 는 한 단어, 관사 필요). `give your thought` → `give me your thoughts`(의견은 보통 복수).
- 더 나은 표현: Using the herdr skill, check tab 2. It's a report on possible issues with deploying workflow_3 at the actual workplace. Tell me what you think, and if you agree with it, go ahead and fix them.
- 왜: 한 문장에 지시 셋을 쉼표로 이어 붙이면 읽는 쪽이 끊을 곳을 찾기 어렵다. 문장을 나누고 `if it is agreeable` 은 `if you agree with it` 으로 바꿨다. `agreeable` 은 "상냥한, 받아들일 만한"이라 사람의 동의를 묻는 자리엔 어색하다.

### 카드 10 — 수정 끝났어?
- 내가 쓴 영어: "fix is done?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `fix is done?` → `Is the fix done?` (관사 `the` + 의문문 어순)
- 더 나은 표현: Are the fixes done?
- 왜: 채팅에선 평서문에 물음표만 붙여도 통하지만 관사는 빼지 않는다. 고친 항목이 여럿이면 `fixes` 가 정확하다.

### 카드 11 — 30회분만 보관
- 내가 쓴 영어: "for the #8b, we can store data for 30 runs only"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: For #8b, let's keep data for only the last 30 runs.
- 왜: 번호로 가리키는 항목엔 `the` 를 붙이지 않는다(`for #8b`). `can store` 는 "저장할 수 있다"는 능력이라 결정을 내리는 말로는 약하다. `let's keep` 이 보관 정책을 정하는 말에 맞는다. `the last 30` 을 넣으면 오래된 것부터 지운다는 뜻까지 전해진다.

### 카드 12 — 왜 해시 이름 폴더를 만들어?
- 내가 쓴 영어: "Why the agent creates the folders named with hashes in the rollout folder?"   (출처: transcript:[user] equipment-data-map)
- 정정: `Why the agent creates …?` → `Why does the agent create …?` (의문사 의문문은 `do/does` + 주어 + 동사원형)
- 더 나은 표현: Why does the agent create hash-named folders in the rollout folder?
- 왜: 한국어 화자가 자주 놓치는 의문문 어순이다. `folders named with hashes` 는 틀리진 않지만 `hash-named folders` 가 짧고 개발 글에서 흔하다.

### 카드 13 — 위키만 보면 되나?
- 내가 쓴 영어: "so I can read the data in wiki? i do not need to care about the result in hashes?"   (출처: transcript:[user] equipment-data-map)
- 정정: `in wiki` → `in the wiki`. 문장 첫 `i` → `I`.
- 더 나은 표현: So I can just read the data in the wiki? I don't need to worry about the hash-named results?
- 왜: 특정 위키를 가리키니 `the` 가 필요하다. `care about` 은 "관심을 두다"에 가깝고 "신경 써야 하나"라는 부담을 말할 땐 `worry about` 이 자연스럽다. `just` 를 넣으면 "그것만 보면 되냐"는 뜻이 산다.

### 카드 14 — 수만 개 파일이 해시되면
- 내가 쓴 영어: "for the Catch 2, there will be tens of thousands of files will be hashed. no problem with the performace of the agent?"   (출처: transcript:[user] equipment-data-map)
- 정정: `there will be … files will be hashed` → `there will be … files to hash` 또는 `tens of thousands of files will be hashed`(`there will be` 와 `will be hashed` 를 한 문장에 겹치면 동사가 둘이 된다). `performace` → `performance`. `the Catch 2` → `Catch 2`.
- 더 나은 표현: For Catch 2, tens of thousands of files will get hashed. Won't that hurt the agent's performance?
- 왜: `there will be` 구문을 쓰려면 뒤는 `to hash` 나 관계절(`that will be hashed`)로 이어야 한다. 걱정을 묻는 말은 `Won't that …?` 부정 의문문이 영어에서 자연스럽다.

### 카드 15 — OKF 고려해 봤어?
- 내가 쓴 영어: "have we considered to use googles wiki style like OKF?"   (출처: transcript:[user] equipment-data-map)
- 정정: `considered to use` → `considered using` (`consider` 뒤는 동명사). `googles` → `Google's` (소유격 아포스트로피, 고유명사 대문자).
- 더 나은 표현: Have we considered using a Google-style wiki format like OKF?
- 왜: `consider`, `avoid`, `suggest`, `finish` 는 to부정사가 아니라 `-ing` 를 받는 동사다. 자주 틀리는 묶음이라 한 번에 외워 두자.

### 카드 16 — 옵시디언에서 잘 읽히는지만
- 내가 쓴 영어: "skip OKF. just focus on if the wiki can be well read in obsidian"   (출처: transcript:[user] equipment-data-map)
- 정정: `focus on if` → `focus on whether` (전치사 뒤엔 `if` 절이 올 수 없음). `obsidian` → `Obsidian`.
- 더 나은 표현: Skip OKF. Just focus on whether the wiki reads well in Obsidian.
- 왜: `on`, `about` 같은 전치사 뒤의 "~인지"는 `whether` 만 된다. `can be well read` 는 수동이라 무겁다. `read well` 은 자동사로 "(글이) 잘 읽힌다"는 뜻이라 간결하다.

### 카드 17 — 예시 값을 살짝 보여 주기
- 내가 쓴 영어: "I thought it would be okay to add some values as examples in the wiki. so that users glimps on it"   (출처: transcript:[user] equipment-data-map)
- 정정: `glimps on it` → `get a glimpse of the data` (`glimpse` 철자, 명사로 쓸 땐 `get a glimpse of`). `so that` 절은 앞 문장에 붙인다.
- 더 나은 표현: I thought it'd be fine to show a few example values in the wiki, so users can get a quick feel for the data.
- 왜: `so that` 은 목적절이라 마침표로 떼면 조각문이 된다. `get a feel for` 는 "감을 잡다"로 이 맥락에 딱 맞는다.

### 카드 18 — JSON 이 한 줄이라 읽기 어렵다
- 내가 쓴 영어: "and from the result, the json files are way too long (no new lines). hard to read"   (출처: transcript:[user] equipment-data-map)
- 더 나은 표현: Also, the JSON files in the output are all on one line, with no line breaks, so they're hard to read.
- 왜: 문제는 파일이 "길다"가 아니라 "한 줄로 붙어 있다"여서 `are all on one line` 이 정확하다. "줄바꿈"은 `new lines` 보다 `line breaks` 가 자연스럽다. `from the result` 는 `in the output` 이 맞는 전치사다.

### 카드 19 — 옵시디언 CLI 를 깔았으니
- 내가 쓴 영어: "since I install obsidian cli packages, the llm can easily work on the jobs. go update for the changes"   (출처: transcript:[user] equipment-data-map)
- 정정: `since I install` → `since I've installed` (이미 끝난 일은 현재완료). `go update for the changes` → `go ahead and apply the changes` (`update for` 는 목적어 짝이 틀림).
- 더 나은 표현: Since I've installed the Obsidian CLI packages, the LLM can handle this easily. Go ahead and apply the changes.
- 왜: "~했으니"의 근거는 지금 영향이 남은 완료라 현재완료가 맞다. `go update` 는 구어에서 쓰이지만 `for` 가 붙으면 틀린다. 변경을 반영하라는 지시는 `apply the changes` 가 정형이다.

### 카드 20 — Codex 에게 리뷰 요청 (반복 실수)
- 내가 쓴 영어: "ask for the review to the codex (herdr open a tab)"   (출처: transcript:[user] equipment-data-map)
- 정정: `ask for the review to the codex` → `ask Codex for a review` (`ask + 사람 + for + 물건`). `herdr open a tab` → `open a herdr tab`.
- 더 나은 표현: Ask Codex for a review in a new herdr tab.
- 왜: 어제 카드에도 나온 실수다. `ask for X to Y` 는 영어에 없는 짝이다. 요청 받는 사람을 바로 `ask` 뒤에 둔다. Codex 는 고유명사라 `the` 가 필요 없고.

### 카드 21 — 일부러 엉뚱한 곳에 두었더니
- 내가 쓴 영어: "working on @poc/workflow_3/monitor/manual_align_correction.py, intentionally place in the wrong place for the align OM so, it forces the agent get into the search around but it fails. it stuck in [INFO] … and no search around. and just wait for 60s and stop working. fix the search around trigger"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `intentionally place` → `I intentionally placed the stage` (주어·시제·목적어 필요). `forces the agent get into` → `forces the agent to go into` (`force + 목적어 + to부정사`). `it stuck in` → `it got stuck at` (`stuck` 은 형용사/과거분사라 `get stuck`). `just wait … and stop` → `just waits … and stops`.
- 더 나은 표현: While testing manual_align_correction.py, I deliberately put the align OM in the wrong spot to force the agent into search-around, but it never gets there. It gets stuck at `[INFO] engineer-done ROI 캐시 …`, never searches, waits 60 s and then stops. Please fix the search-around trigger.
- 왜: 상황 설명에 주어가 빠지면 누가 무엇을 했는지 흐려진다. `force A to do` 와 `get stuck` 은 자주 쓰는 짝이라 통째로 익혀 두자. 반복되는 `and … and …` 는 동사 셋을 쉼표로 나열하면 깔끔해진다.

### 카드 22 — 한 번만 시도한다
- 내가 쓴 영어: "the align point correction algo is not precise. I think this is somewhat related to search around (no try at all). and align point correction is only tried once (the pointed location is a bit drifted)."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `no try at all` → `it never tries it at all` (`try` 를 명사로 쓰면 `no attempt at all` 이 자연스럽다). `is a bit drifted` → `has drifted a bit` (`drift` 는 자동사라 수동태 불가).
- 더 나은 표현: The align point correction isn't precise. I suspect it's related to search-around, which never runs at all. The correction is also attempted only once, and the clicked point ends up slightly off.
- 왜: `drift` 처럼 목적어를 받지 않는 자동사는 `be + 과거분사` 로 쓸 수 없다. 괄호로 덧붙인 메모는 관계절(`which never runs`)이나 `and` 절로 문장에 넣으면 흐름이 이어진다.

### 카드 23 — align point 와 박스 중심을 구분해
- 내가 쓴 영어: "I realize that the OM works good but the agent locates the correct point in the center of the box from the recipe. I think you have to manage well what is the align point and what is the center of the box. … We recently documented about this … the cond.txt is obsolutly needed for the align fail correction."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `works good` → `works well` (동사 수식은 부사). `what is the align point` → `what the align point is` (간접의문문은 평서 어순). `documented about this` → `documented this` (`document` 는 타동사). `obsolutly` → `absolutely`.
- 더 나은 표현: I noticed the OM works well, but the agent puts the target at the center of the recipe box. You need to keep the align point and the box center clearly separate. We documented this recently, and cond.txt is essential for align-fail correction.
- 왜: `document`, `discuss`, `mention` 은 `about` 없이 바로 목적어를 받는다. `manage well what is …` 는 뜻이 흐리다. 원하는 건 두 개념을 섞지 말라는 것이니 `keep A and B separate` 가 정확하다.

### 카드 24 — 늘 차이가 있다
- 내가 쓴 영어: "crosshair and center, there is always delta (as human cannot set the very center of the box). I will tell you the good and bad one in the next test. currently not sure what is good or bad due to overloaded [INFO]"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `there is always delta` → `there is always a delta`. `as human cannot` → `since a human can't` (가산명사 단수엔 관사).
- 더 나은 표현: There's always some offset between the crosshair and the center, since no one can set the exact center of the box by hand. I'll tell you which runs were good and bad after the next test; right now I can't tell because of all the `[INFO]` noise.
- 왜: `human` 은 가산명사라 `a human` 이나 `no one` 으로 쓴다. `overloaded [INFO]` 는 뜻은 통하지만 로그가 너무 많아 신호가 묻힌다는 말은 `noise` 가 영어 개발자들이 쓰는 단어다.

### 카드 25 — 일부러 드래그해?
- 내가 쓴 영어: "In workflow_3, do you intentionally use mouse dragging when move around like clicking buttons?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `when move around` → `when moving around` 또는 `when you move around` (접속사 `when` 뒤엔 주어+동사나 분사).
- 더 나은 표현: In workflow_3, do you deliberately drag the mouse when moving between buttons?
- 왜: `use mouse dragging` 은 명사화가 겹쳐 무겁다. 동사 `drag` 하나로 줄인다. `like clicking buttons` 는 "버튼 클릭처럼"으로 읽혀 뜻이 흐려서 `between buttons` 로 바꿨다.

### 카드 26 — glide 를 빼면 더 빨라지나?
- 내가 쓴 영어: "I see. glide method is applied to track mouse down? how about remove the glide and jiggle a bit right before clicking buttons. In that case, the automation can be faster?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `how about remove` → `how about removing` (`how about` 뒤는 동명사). `glide method is applied` → `Is the glide there …?` (의문문 어순).
- 더 나은 표현: I see. So is the glide there to track the mouse-down? What if we drop the glide and just jiggle right before each click? Would that make the automation faster?
- 왜: `How about + -ing`, `What if + 절` 은 제안의 두 틀이다. 가능성을 묻는 말은 `can be faster?` 보다 가정 `Would that make … faster?` 가 자연스럽다.

### 카드 27 — 코드가 비대해지나?
- 내가 쓴 영어: "if we add the distance-proportional variant, code gets bloated?"   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Would adding the distance-proportional variant bloat the code much?
- 왜: 평서문에 물음표만 붙인 형태는 구어로 통한다. 다만 가정 질문은 `Would …?` 로 시작하면 더 매끄럽다. 동명사 주어(`adding …`)로 조건절을 접으면 문장이 짧아지고 `bloat` 는 타동사로 바로 쓸 수 있다.

### 카드 28 — 먼저 지연 시간부터
- 내가 쓴 영어: "I see. let's go first with glide delay reduction."   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Got it. Let's start with reducing the glide delay.
- 왜: `go first with` 는 뜻은 통하지만 `start with` 가 순서를 정하는 정형구다. `glide delay reduction` 같은 명사 세 개 연쇄는 동명사 `reducing the glide delay` 로 풀면 말로 할 때 자연스럽다.

### 카드 29 — 엔지니어에게 넘길 때 녹화?
- 내가 쓴 영어: "for the screen recording, right now, have we set to record when the agents hand off to an engineers?"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `an engineers` → `an engineer` 또는 `engineers` (`an` 은 단수에만). `have we set to record` → `have we set it to record` (`set` 뒤에 목적어 필요).
- 더 나은 표현: For screen recording, is it currently set to record when the agent hands off to an engineer?
- 왜: 어제도 나온 `a/an` + 복수 실수다. 관사를 붙였으면 명사는 단수로 맞춘다. 현재 설정을 묻는 말은 `is it currently set to …` 가 간결하다.

### 카드 30 — 들어가자마자 녹화, 최대 5분
- 내가 쓴 영어: "I just like to record as soon as the agent enters the tool monitor. and recording max seconds to be 5 minutes (300s). Of couse, we can stop recording after the engineer finish the hand-off job from the agent."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `I just like to` → `I'd just like to` (희망은 `would like`; `like to` 는 "평소 좋아한다"). `Of couse` → `Of course`. `the engineer finish` → `the engineer finishes` (3인칭 단수).
- 더 나은 표현: I'd like recording to start as soon as the agent enters the tool monitor, capped at 5 minutes (300 s). Of course, it can stop early once the engineer finishes the handoff.
- 왜: `I like to` 와 `I'd like to` 는 뜻이 다르다. 요청할 땐 반드시 `'d` 를 붙인다. 두 번째 문장은 동사 없는 조각이라 `capped at` 분사구로 앞 문장에 붙였다.

### 카드 31 — 500초, 엔지니어 대기 60초
- 내가 쓴 영어: "I see. recording_max_sec should be then 500 seconds (including the tool window opens), and wait for the engineers 60 seconds."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `should be then 500` → `should then be 500` (`then` 은 조동사와 본동사 사이). `including the tool window opens` → `including the time the tool window is opening` 또는 `counting from when the tool window opens`.
- 더 나은 표현: Got it. Then recording_max_sec should be 500 seconds, counted from when the tool window opens, and the engineer wait should be 60 seconds.
- 왜: `including` 은 전치사라 뒤에 절(`the tool window opens`)을 바로 받지 못한다. 병렬 구조도 맞춘다: 앞이 설정값이면 뒤도 `the engineer wait should be …` 로 설정값을 말한다.

### 카드 32 — 재미있는 건
- 내가 쓴 영어: "I wonder if it is possible to monitor consistently the rcs list tab while the agent is working on the tool monitor. … Funnything is even if you do not click one of the buttons, engineers can enter the tool monitor as the information windows disappear in 3 seconds."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `monitor consistently the rcs list tab` → `continuously monitor the RCS List tab` (부사는 동사와 목적어 사이에 두지 않는다). `Funnything is` → `The funny thing is (that)`. `the information windows disappear` → `the Information window disappears`.
- 더 나은 표현: I wonder if we could keep watching the RCS List tab while the agent works in the tool monitor. The funny thing is, even if nobody clicks either button, the engineer still gets in, because the Information popup disappears after 3 seconds.
- 왜: 영어는 동사와 목적어를 떼지 않는다(`monitor X consistently` 또는 `continuously monitor X`). "지속적으로 감시"는 `consistently`(한결같이)보다 `continuously`(끊임없이)가 맞다. `in 3 seconds` 는 "3초 뒤에"로도 읽혀 괜찮지만 `after 3 seconds` 가 더 분명하다.

### 카드 33 — 제가 걱정하는 건
- 내가 쓴 영어: "I see. Understanding that Information window is not the priority. What I am concern is that, when the agent is working on the correction, if someone is entering the tool monitor, the tool monitor is hidden for 3s from the agent side … which might screw up the agent's working on correction."   (출처: transcript:[user] auto-recipe-creator)
- 정정: `What I am concern is` → `What I'm concerned about is` (`be concerned about`). `Understanding that …` 단독 분사구 → `I understand that …`. `the agent's working on correction` → `the agent's correction work`.
- 더 나은 표현: Got it — the Information window isn't the priority. My concern is this: if someone connects to the tool while the agent is mid-correction, the tool monitor is hidden from the agent for about 3 seconds, and that could throw off the correction.
- 왜: 어제 카드의 `What I am worried` 와 같은 유형이다. `concern` 을 동사로 쓰면 뜻이 달라지니(`concern` = 관련되다) 명사 `My concern is` 로 가는 편이 안전하다. `screw up` 은 속어라 동료에겐 괜찮지만 `throw off` 가 한 단계 점잖다.

### 카드 34 — 사무실에서 확인하게
- 내가 쓴 영어: "add a console line so I can confirm at office"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `at office` → `at the office` (특정 장소는 관사 필요; `in office` 는 "재임 중"이라 뜻이 다름).
- 더 나은 표현: Add a console line so I can confirm it at the office.
- 왜: `at home`, `at work` 는 관사 없이 쓰지만 `office` 는 `at the office` 가 표준이다. `confirm` 은 타동사라 `it` 을 받쳐 주면 자연스럽다.

### 카드 35 — Q1~Q4 답변
- 내가 쓴 영어: "Q1, it is (a) and (c). Q2, apply everywhere (like parent setting), should be able to on/off with toggle. Q3, (a) Q4. favorites stub in the landing page can be usable with the name of "favorite tools"."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `should be able to on/off` → `should be able to turn it on and off` (`on/off` 는 동사가 아님). `can be usable` → `can be used` (`can` + `usable` 중복).
- 더 나은 표현: Q1: (a) and (c). Q2: one set applied everywhere, like a parent setting, with a toggle to turn it on and off. Q3: (a). Q4: the favorites stub on the landing page can be reused as "Favorite tools".
- 왜: 번호 답변은 콜론으로 맞추면 한눈에 읽힌다. `with the name of` 는 `as "…"` 로 줄인다. 이미 있는 스텁을 다시 쓰는 거라 `reused` 가 뜻을 정확히 전한다.
