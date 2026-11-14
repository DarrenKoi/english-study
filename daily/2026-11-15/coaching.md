# 2026-11-15 — 코칭

리버스 엔지니어링 입문 deck을 맡기면서 쓴 지시문이 오늘 재료다. 한글→영어 20장(내가 쓴 한글 16, 번역 정독 4), 영어 다듬기 2장.

## 한글→영어

### 카드 1 — 해야 할 일 두 가지를 한 문장에   (내가 쓴 한글)
- 내가 쓴 한글: "팀 내에서 reverse engineering 기법에 대해서 소개를 해야 하고 REA skill을 어떻게 활용하면 좋은지도 알려줘야 한다."   (출처: transcript:[user] /goal)
- 자연스러운 영어: I need to introduce reverse engineering to my team and show them how to get the most out of the REA skill.
- 왜 이렇게: "~에 대해서 소개하다"는 `introduce about` 이 아니라 `introduce X to 사람` 이다. `introduce` 는 타동사라 전치사가 필요 없다. "어떻게 활용하면 좋은지"는 `how to use it well` 도 되고, "최대한 뽑아 쓰다"는 느낌이면 `get the most out of`. "팀 내에서"는 `in my team` 보다 `to my team` 이 듣는 사람을 분명히 한다.

### 카드 2 — 환경 조건 알려 주기   (내가 쓴 한글)
- 내가 쓴 한글: "회사에서는 ghidra를 설치할 수 있고 운영체제는 Windows이다."   (출처: transcript:[user] /goal)
- 자연스러운 영어: At work we're allowed to install Ghidra, and our machines run Windows.
- 왜 이렇게: 여기서 "설치할 수 있다"는 능력이 아니라 허가라서 `can` 보다 `are allowed to` 가 정확하다. "운영체제는 Windows이다"를 `The OS is Windows` 로 옮겨도 맞지만, 영어는 `our machines run Windows` 처럼 기계를 주어로 세우는 쪽을 더 자주 쓴다.

### 카드 3 — 청중이 비전공자라는 사정   (내가 쓴 한글)
- 내가 쓴 한글: "팀 내 모든 전공자는 전기 공학, 컴퓨터 공학이 아니고 다양하기 때문에 보편적으로 이해할 수 있는 방식 (용어 설명 필요)으로 설명해야 한다."   (출처: transcript:[user] /goal)
- 자연스러운 영어: Not everyone on the team has an EE or CS background; people come from all sorts of fields. So it needs to be explained in a way anyone can follow, with the jargon spelled out.
- 왜 이렇게: 원문은 "모두가 전공자인 것은 아니다"라는 부분 부정인데 `All members are not…` 로 쓰면 "전원이 아니다"로 읽힌다. `Not everyone…` 으로 시작해야 한다. "전공"은 `major` 보다 `background` 가 직장인에게 맞는다. "보편적으로 이해할 수 있는"을 `universally understandable` 로 옮기면 딱딱하고, `in a way anyone can follow` 가 말에 가깝다. "용어 설명"은 `spell out the jargon` 또는 `define the terms`.

### 카드 4 — 분량과 파일 형식 지정   (내가 쓴 한글)
- 내가 쓴 한글: "슬라이드는 20~30장 정도로 구성되어야 함. pptx와 md 파일로 만들어줘."   (출처: transcript:[user] /goal)
- 자연스러운 영어: The deck should be around 20 to 30 slides. Please make it as both a pptx and a Markdown file.
- 왜 이렇게: "구성되어야 한다"를 `should be composed of` 로 옮길 필요가 없다. `should be around 20 to 30 slides` 면 끝난다. "~장"은 `pages` 가 아니라 `slides`. 두 형식을 다 원한다는 뜻은 `both A and B` 로 못박아 둔다. 그냥 `in pptx and md` 라고 하면 둘 중 하나로 읽힐 여지가 있다.

### 카드 5 — 필요하면 다른 도구와 같이   (내가 쓴 한글)
- 내가 쓴 한글: "필요하면, codex와 협동해서 컨텐츠를 풍성하게 만들어줘 (via herdr)."   (출처: transcript:[user])
- 자연스러운 영어: If it helps, work with Codex through herdr to flesh out the content.
- 왜 이렇게: "풍성하게 만들다"는 `make it rich` 보다 `flesh out`(뼈대에 살을 붙이다)이 딱 맞는다. `enrich the content` 는 격식체다. "협동해서"는 `cooperate` 보다 `work with` 가 자연스럽고, 격식을 올리면 `collaborate with`. "필요하면"은 `if needed` 도 좋지만 판단을 맡길 때는 `if it helps` 가 부드럽다.

### 카드 6 — 시각 자료가 이해를 돕는다   (내가 쓴 한글)
- 내가 쓴 한글: "시각적인 도표, scheme, 차트등을 활용하면 이해하는데 도움이 될거야."   (출처: transcript:[user])
- 자연스러운 영어: Diagrams, schematics, and charts would make it much easier to follow.
- 왜 이렇게: 영어 `scheme` 은 "계획, 제도"이고 영국에서는 "꿍꿍이"로도 읽힌다. 구조를 그린 그림은 `schematic` 이나 `diagram` 이다. `visual diagrams` 는 겹말이라 `visual` 을 뺀다. "~을 활용하면 도움이 될 거야"는 `If we use…, it will be helpful` 로 풀기보다 도표를 주어로 세워 `Diagrams would make it easier` 로 줄인다. 한국어의 조건절이 영어에서는 주어가 되는 경우가 많다.

### 카드 7 — 발표는 내가 한다   (내가 쓴 한글)
- 내가 쓴 한글: "발표는 한시간 이내로 내가 발표하면서 내용을 이해시켜줄거야."   (출처: transcript:[user])
- 자연스러운 영어: I'll be presenting it myself in under an hour and walking the team through the content as I go.
- 왜 이렇게: "이해시켜 주다"를 `make them understand` 로 옮기면 억지로 이해시키는 어감이 난다. `walk someone through` 는 옆에서 하나씩 짚어 주며 설명한다는 뜻이라 여기 맞는다. "한 시간 이내"는 `within one hour` 보다 `in under an hour` 가 길이를 말할 때 자연스럽다(`within` 은 기한 쪽). "발표하면서"는 `as I go`.

### 카드 8 — 나중에 내가 채워 넣을 예정   (내가 쓴 한글)
- 내가 쓴 한글: "참고사항. 회사에서 내가 REA를 돌려서 얻은 결과물들도 사이사이에 넣을 예정."   (출처: transcript:[user])
- 자연스러운 영어: One more thing to keep in mind: I'm also planning to drop in some results from running REA at work, in between the slides.
- 왜 이렇게: "참고사항"은 `FYI` 가 가장 짧고, 지시의 일부라면 `One thing to keep in mind:` 나 `Heads-up:` 이 낫다. `Reference:` 는 참고 문헌으로 읽힌다. "REA를 돌려서 얻은 결과물"은 `results I got by running REA` 를 `results from running REA` 로 줄인다. "사이사이에 넣다"는 `drop in … in between the slides`, 격식 있게는 `intersperse`. "~할 예정"은 `I'm planning to`.

### 카드 9 — 다른 LLM이 저장소를 읽고 삽입   (내가 쓴 한글)
- 내가 쓴 한글: "office에서 운영하는 LLM이 해당 repo를 탐색하고 삽입할 수 있음."   (출처: transcript:[user])
- 자연스러운 영어: The LLM we run at the office can browse the repo and insert them itself.
- 왜 이렇게: "office에서 운영하는 LLM"은 관계절로 `the LLM we run at the office`. `operate` 는 장비 조작 쪽이고 서비스 운영은 `run` 이나 `host` 다. "해당 repo"의 "해당"은 `the` 하나로 충분하니 `the corresponding repo` 까지 가지 않는다. `insert` 는 타동사라 목적어 `them` 이 꼭 있어야 한다. 한국어에서 목적어를 생략한 자리를 영어에서 채우는 연습이 된다.

### 카드 10 — 다른 방식이 더 낫지 않을까   (내가 쓴 한글)
- 내가 쓴 한글: "지금 pptx로 만들었지만 html로 만들면 좀 더 모던하고 비주얼 효과를 넣을 수 있을까? bento skill을 이용한다면 말이야."   (출처: transcript:[user])
- 자연스러운 영어: We built it as a pptx, but would an HTML version look more modern and let us add visual effects? I mean with the Bento skill.
- 왜 이렇게: 실제로 일어나지 않은 선택을 묻는 질문이라 `can` 보다 `would` 를 쓴다. "~면 ~할 수 있을까?"를 `If we make…, can we…?` 로 풀지 않고 `an HTML version` 을 주어로 세우면 한 절로 끝난다. 뒤에 덧붙인 "~한다면 말이야"는 `I mean with…` 또는 `…, using the Bento skill, that is.` 로 받는다. `HTML` 은 발음이 모음(에이치)으로 시작해 `an HTML` 이다.

### 카드 11 — 취향 밝히기   (내가 쓴 한글)
- 내가 쓴 한글: "bento에서 나는 하얀색 배경을 더 좋아한다." / "하얀색으로"   (출처: transcript:[user])
- 자연스러운 영어: For Bento decks, I prefer a white background. / Make that one white too.
- 왜 이렇게: `prefer` 에 이미 "더"가 들어 있어 `prefer more` 라고 하지 않는다. 비교 대상을 밝히려면 `prefer A to B`(`than` 이 아니다). 바꿔 달라는 요청을 겸할 때는 `I'd rather have a white background` 가 한 번에 통한다. 뒤의 "하얀색으로"는 대상이 빠진 한마디라 영어로는 `Make that one white too` 처럼 무엇을 가리키는지 `that one` 을 넣어 준다. 실제 대화에서도 어시스턴트가 "기존 deck도"라고 대상을 추측해 처리했다.

### 카드 12 — 다른 쪽 의견도 들어 봐   (내가 쓴 한글)
- 내가 쓴 한글: "bento 내용 추가/수정 할게 있는 지 codex에게도 조언을 구해봐 (via herdr)"   (출처: transcript:[user])
- 자연스러운 영어: Ask Codex too, through herdr, whether anything in the Bento deck should be added or changed.
- 왜 이렇게: "조언을 구하다"는 `ask for advice` 인데, 묻는 내용이 따로 있으면 `ask 사람 whether…` 로 바로 잇는 편이 짧다. "추가/수정할 게 있는지"는 수동으로 `whether anything should be added or changed`. 가볍게는 `Get Codex's take on it too` 도 쓴다. `advice` 는 불가산이라 `an advice`, `advices` 가 없다.

### 카드 13 — 가볍게 희망 사항 던지기   (내가 쓴 한글)
- 내가 쓴 한글: "움직이는 모션 같은거 추가하면 좋겠네."   (출처: transcript:[user])
- 자연스러운 영어: It'd be nice to add some animation or something.
- 왜 이렇게: "움직이는 모션"은 겹말이고 영어 `motion` 도 이 뜻으로는 덜 쓴다. 슬라이드에서는 `animation` 이다. "~하면 좋겠네"는 강한 요청이 아니라 `It'd be nice to…` 가 온도에 맞는다. "~ 같은 거"는 `or something` 을 뒤에 붙인다. 요청을 분명히 하려면 `Could you add some animation?`.

### 카드 14 — 이것도 같이 올려 줘   (내가 쓴 한글)
- 내가 쓴 한글: "커밋하고 push 해줘" / "my-task/arc-tf 변경건도 commit and push"   (출처: transcript:[user])
- 자연스러운 영어: Commit and push, please. / Commit and push the my-task/arc-tf changes as well.
- 왜 이렇게: "변경건"은 `change items` 가 아니라 그냥 `changes`. "~도"는 문장 끝 `as well` 이나 `too` 로 받는다. `also` 를 맨 앞에 두면 "그리고 또"라는 접속 느낌이 강해진다. 목적어가 길면 `commit and push` 뒤에 한 번만 쓴다.

### 카드 15 — 끝난 것은 정리   (내가 쓴 한글)
- 내가 쓴 한글: "작업이 끝난 worktrees는 제거"   (출처: transcript:[user])
- 자연스러운 영어: Remove the worktrees that are no longer in use.
- 왜 이렇게: "작업이 끝난"을 `finished worktrees` 로 옮기면 worktree 자체가 완성됐다는 뜻이 되어 어색하다. 끝난 것은 그 안의 작업이므로 `the worktrees whose work is done` 이나 `that are no longer in use` 로 푼다. 가볍게는 `Clean up the worktrees we're done with`. `we're done with` 는 "다 쓴"이라는 뜻의 구어 표현이다.

### 카드 16 — 합치고 지우기   (내가 쓴 한글)
- 내가 쓴 한글: "조사 문서 3개는 main에 합치고 브랜치 삭제"   (출처: transcript:[user])
- 자연스러운 영어: Merge the three research docs into main, then delete the branches.
- 왜 이렇게: "합치다"는 git에서 `merge A into B` 로 쓰고 전치사는 `into` 다(`to` 가 아니다). "조사 문서"는 `investigation documents` 보다 `research docs`. 순서가 중요한 지시라 `and` 대신 `then` 을 넣으면 "합친 다음에 지워라"가 분명해진다. 숫자는 `the three research docs` 처럼 정관사 뒤에 온다.

### 카드 17 — 없는 숫자는 만들지 않았다   (고급 한글 · 번역)
- 한글 원문: "근거 없는 수치를 만들지 않으려고 나머지는 도식과 색 구분 표로 처리했습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: To avoid inventing numbers I couldn't back up, I handled the rest with diagrams and color-coded tables.
- 번역 포인트: "근거 없는 수치"를 `groundless figures` 로 옮기면 사전 냄새가 난다. `numbers I couldn't back up`(뒷받침 못 할 숫자)처럼 관계절로 풀면 책임 주체까지 드러난다. "만들다"는 `make` 가 아니라 `invent` 또는 `make up` 이어야 "지어내다"가 된다. 목적의 "~하지 않으려고"는 `To avoid -ing` 을 문두에 둔다. "색 구분 표"는 `color-coded tables`.

### 카드 18 — 내 판단을 밝히고 선택은 넘기기   (고급 한글 · 번역)
- 한글 원문: "비밀번호나 토큰은 아니어서 저는 그대로 두어도 된다고 보지만, 컴퓨터 이름이 공개되는 것이 꺼려지시면 말씀해 주세요."   (출처: transcript:[assistant])
- 자연스러운 영어: It isn't a password or a token, so I think it's fine to leave it as is, but let me know if you're uncomfortable having your machine's name out in public.
- 번역 포인트: "~라고 보다"는 `I see that` 이 아니라 `I think` / `in my view`. "그대로 두다"는 `leave it as is`. "꺼려지다"는 `reluctant`(하기 싫다)보다 `uncomfortable`(마음이 불편하다)이 맞고, 뒤에 `having + 목적어 + 부사구` 로 상황을 붙인다. 한국어는 "~지만"으로 한 문장에 묶었고 영어도 `so …, but …` 로 한 문장에 담되 내 의견이 앞에, 상대의 선택권이 뒤에 오는 순서를 지켰다.

### 카드 19 — 장식이 아니라 뜻이 있는 곳에만   (고급 한글 · 번역)
- 한글 원문: "장식보다 '무엇이 어디로 가는가'를 보여 주는 곳에만 넣었습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: I added it only where it shows what goes where, not as decoration.
- 번역 포인트: "무엇이 어디로 가는가"는 `what goes where` 세 단어로 떨어진다. 의문사 두 개를 겹쳐 쓰는 꼴로 `who does what`, `what belongs where` 와 같은 틀이다. "장식보다"를 `rather than decoration` 으로 앞에 두면 문장이 무거워지니 `not as decoration` 을 뒤로 돌렸다. `only` 는 꾸미는 `where` 절 바로 앞에 둔다.

### 카드 20 — 부분의 일치를 전체로 넘겨짚지 않게   (고급 한글 · 번역)
- 한글 원문: "몇 건의 일치를 프로그램 전체의 동일성으로 받아들이지 않게"   (출처: transcript:[assistant], 수정 이유 칸)
- 자연스러운 영어: so that a handful of matching cases isn't mistaken for proof that the two programs are identical
- 번역 포인트: 명사가 줄지어 선 한국어("일치", "동일성")를 영어에서는 절로 푼다. "동일성"은 `identity` 보다 `that the two programs are identical`. "~으로 받아들이다"가 잘못된 수용을 뜻하므로 `be mistaken for` 를 쓴다. "몇 건"은 `a handful of` 로 적다는 어감을 살린다. 오늘 표현 `A pass is not proof of a valid file` 과 같은 논리다.

## 영어 다듬기

### 카드 21 — before 뒤의 동사 꼴
- 내가 쓴 영어: "also update bento slide skills if possible before implement"   (출처: transcript:[user])
- 정정: also update the Bento slides skill if possible before **implementing** — 전치사 `before` 뒤에는 동사 원형이 올 수 없다. 동명사(`before implementing`)나 절(`before you implement it`)로 쓴다. 스킬은 하나이므로 `skills` 가 아니라 `the … skill` 이고, 특정한 것을 가리키니 `the` 가 필요하다.
- 더 나은 표현: Before you start, update the Bento slides skill if there's a newer version.
- 왜: 순서가 핵심인 지시는 `Before you start` 를 앞에 두면 읽는 쪽이 먼저 할 일을 놓치지 않는다. `if possible` 은 "가능하면"이라 조건이 흐릿한데, 실제 뜻은 "새 버전이 있으면"이므로 `if there's a newer version` 으로 구체화했다. `implement` 는 타동사라 목적어 없이 쓰면 어색하다. 목적어가 뻔할 때는 `start` 나 `build it` 으로 바꾼다.

### 카드 22 — commit and push
- 내가 쓴 영어: "commit and push"   (출처: transcript:[user])
- 더 나은 표현: Looks good. Commit and push the reverse_engineering changes.
- 왜: 문법 오류는 없고 개발자끼리는 이대로 쓴다. 다만 이날은 작업 트리에 `my-task/arc-tf` 변경이 함께 남아 있어서 범위가 갈렸고, 바로 다음 메시지로 "그것도"를 따로 요청해야 했다. 여러 변경이 섞여 있을 때는 목적어로 범위를 밝히거나 `Commit and push everything` 이라고 쓰면 왕복이 한 번 준다. 앞에 `Looks good.` 처럼 승인 한마디를 붙이면 검토를 마쳤다는 신호도 된다.
