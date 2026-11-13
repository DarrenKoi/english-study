# 2026-11-14 — 코칭

오늘은 내가 쓴 영어 문장이 없어서 "영어 다듬기"는 건너뛴다. 한글→영어만 24장(내가 쓴 한글 20, 번역 정독 4).

## 한글→영어

### 카드 1 — 공통점을 묶어 소개하기   (내가 쓴 한글)
- 내가 쓴 한글: "skewnono_v3_nuxt, auto_recipe_creation, flask_modules와 같은 repo들은 공통적으로 회사에서 서비스하기 위한 어플리케이션들이고, skewnono_v3_nuxt는 특히 규모가 상당히 커진 상태."   (출처: transcript:[user])
- 자연스러운 영어: Repos like skewnono_v3_nuxt, auto_recipe_creation, and flask_modules are all applications we run in production at work, and skewnono_v3_nuxt in particular has grown quite large.
- 왜 이렇게: "공통적으로"는 `commonly` 보다 `are all` 이 자연스럽다. `commonly` 는 "흔히"로 읽힌다. "서비스하기 위한"을 `for servicing` 으로 옮기면 "정비용"이 되니 `run in production` 이나 `serve internally` 를 쓴다. "커진 상태"는 상태 명사를 찾지 말고 현재완료 `has grown` 으로 처리한다.

### 카드 2 — 두 에이전트가 협업해야 하는 경우   (내가 쓴 한글)
- 내가 쓴 한글: "이런 repo들 처럼 home agent (you)와 office agent (회사에서 내부적으로 제공하는 LLM으로 GLM-5.3이나 그에 상응하는 모델 성능)이 서로 협동해서 작업을 해야 하는 케이스가 많아지고 있음."   (출처: transcript:[user])
- 자연스러운 영어: With repos like these, there are more and more cases where the home agent (you) and the office agent (the LLM my company provides internally, GLM-5.3 or something comparable) have to work together.
- 왜 이렇게: "케이스가 많아지고 있다"는 `there are more and more cases where…` 가 기본형이다. `cases are increasing` 도 통하지만 딱딱하다. "그에 상응하는 성능"은 `or something comparable`, 격식을 올리면 `or a model of comparable capability`. "서로 협동해서"의 "서로"는 `work together` 에 이미 들어 있어 `each other` 를 덧붙이지 않는다.

### 카드 3 — 이유를 덧붙이기   (내가 쓴 한글)
- 내가 쓴 한글: "office agent만 접근 가능한 실제 회사의 데이터들이 많아지기 때문."   (출처: transcript:[user])
- 자연스러운 영어: That's because more and more of the real company data is accessible only to the office agent.
- 왜 이렇게: 영어는 `Because …` 만으로 문장을 끝내면 조각 문장이 된다. 글에서는 `That's because …` 로 받는다. `only` 는 꾸미는 말 바로 앞에 둔다(`only to the office agent`). `data` 는 불가산으로 써서 "데이터들"의 복수 표시는 사라진다.

### 카드 4 — 유지할지 궁금하다   (내가 쓴 한글)
- 내가 쓴 한글: "앞으로 이런 구조를 유지하는게 좋을 지 (회사의 일부 정보를 home agent에게 알려주기 위해서는 내가 일일히 핸드 타이핑 해야 하는 어려움이 있음) 궁금하다."   (출처: transcript:[user])
- 자연스러운 영어: I'm wondering whether I should keep this setup going forward. The pain point is that I have to type everything out by hand whenever I want to pass company information to the home agent.
- 왜 이렇게: "~하는 게 좋을지 궁금하다"는 `I'm wondering whether I should…`. 괄호 안 사정은 영어에서 문장을 따로 떼는 편이 읽기 쉽다. "일일이 손으로 타이핑"은 `type everything out by hand` 로, `out` 이 "하나하나 다"를 맡는다. `hand typing` 은 콩글리시에 가깝다. "어려움이 있음"은 `there is a difficulty` 보다 `the pain point is that…` 이 개발자 말투다.

### 카드 5 — 대안을 물음표로 던지기   (내가 쓴 한글)
- 내가 쓴 한글: "아니면 회사에서 대부분 작업을 진행하고 필요에 따라 주요 알고리즘을 home agent가 프로토타입으로 제공하는 방식?"   (출처: transcript:[user])
- 자연스러운 영어: Or should I do most of the work at the office and have the home agent prototype the key algorithms as needed?
- 왜 이렇게: 명사로 끝나는 질문("~하는 방식?")은 `Or should I…?` 처럼 주어와 동사를 세운다. 가볍게 가려면 `Or how about doing most of the work at the office…?` 도 된다. "프로토타입으로 제공하다"는 `prototype` 을 동사로 쓰면 한 단어다. "필요에 따라"는 `as needed`.

### 카드 6 — 한발 물러선 단서   (내가 쓴 한글)
- 내가 쓴 한글: "작업 난이도에 따라 달라질 것 같기는 함."   (출처: transcript:[user])
- 자연스러운 영어: I suppose it depends on how hard the task is, though.
- 왜 이렇게: "~것 같기는 함"의 양보 느낌은 문장 끝 `though` 가 맡는다. "작업 난이도"는 `task difficulty` 보다 `how hard the task is` 처럼 절로 푸는 쪽이 회화답다. `I suppose` 는 `I think` 보다 확신이 약해서 "~같기는"과 잘 맞는다.

### 카드 7 — 그렇다면 기준이 필요하겠다   (내가 쓴 한글)
- 내가 쓴 한글: "분담을 repo나 작업별로 다르게 가져간다고 하면, 그걸 판정하는 기준이 필요하겠다."   (출처: transcript:[user])
- 자연스러운 영어: If we split the work differently per repo or per task, then we'll need criteria for making that call.
- 왜 이렇게: "~다고 하면"은 `If we…, then we'll need…`. "분담을 가져가다"의 "가져가다"는 옮기지 않고 `split the work` 로 끝낸다. "판정하다"는 `make that call` 이 구어에서 딱 맞는다(`call` = 판단). 문서에는 `criteria for deciding who leads`.

### 카드 8 — PoC 지만 home 기반으로 해왔다   (내가 쓴 한글)
- 내가 쓴 한글: "auto_recipe_creation도 지금까지 poc지만 home을 기반으로 개발을 해왔다."   (출처: transcript:[user])
- 자연스러운 영어: auto_recipe_creation is still a PoC, but so far I've been developing it mostly at home, too.
- 왜 이렇게: "지금까지 ~해왔다"는 현재완료진행 `I've been developing`. "home을 기반으로"를 `based on home` 으로 옮기면 "집을 근거로 한"처럼 어색해서 `at home`, `on the home side` 가 낫다. "~도"는 문장 끝 `too` 로.

### 카드 9 — 긴 고민을 두 문장으로 나누기   (내가 쓴 한글)
- 내가 쓴 한글: "앞으로 더 발전된 서비스인 공통 플랫폼을 만들고 여기에서 auto recipe creation 작업을 하는 기반을 갖추려고 하는데, office agent를 통해 정보를 가져와야 할 지 아니면 독자적으로 office agent가 다 작업하게 해야할 지 고민이 된다."   (출처: transcript:[user])
- 자연스러운 영어: Next, I want to build a shared platform, a more mature service, and make it the foundation for the auto recipe creation work. What I can't decide is whether to pull information through the office agent or to let the office agent handle everything on its own.
- 왜 이렇게: 한국어는 "~는데"로 계획과 고민을 한 문장에 담지만 영어는 둘로 끊어야 읽힌다. "고민이 된다"는 `I'm worried` 가 아니다(그건 걱정). 선택을 못 정한 상태는 `I can't decide whether A or B`, `I'm torn between A and B`. "독자적으로"는 `on its own`. "기반을 갖추다"는 `make it the foundation for`.

### 카드 10 — 추천대로 간다   (내가 쓴 한글)
- 내가 쓴 한글: "Q5~Q8은 추천대로 따름." / "모두 추천대로 따름"   (출처: transcript:[user])
- 자연스러운 영어: For Q5 through Q8, I'll go with your recommendations. / I'll go with your recommendation on all of them.
- 왜 이렇게: "따르다"를 `follow` 로 해도 되지만 선택지 중 하나를 고를 때는 `go with` 가 가장 흔하다. 범위 "~"는 말로 `Q5 through Q8`. 아주 짧게는 `Go with your picks for all.` 처럼 써도 채팅에서 통한다.

### 카드 11 — 내가 원하는 건 이런 스킬이다   (내가 쓴 한글)
- 내가 쓴 한글: "1. 인데, 나는 auto_recipe_creation 플랫폼 개발을 포함해서, 앞으로 진행하게 될 개발 건에 대해서 home / office 협업 구조를 만들고 진행할 수 있도록 적절한 업무 분담과 파일 구조를 판정하고 시작할 수 있게 도와주는 스킬 또는 프롬프트를 만드는거야."   (출처: transcript:[user])
- 자연스러운 영어: Option 1. But what I actually want is a skill or prompt that, for any future development work, including the auto_recipe_creation platform, helps me decide the right division of work and file structure so I can set up the home/office collaboration and get started.
- 왜 이렇게: "내가 원하는 건 ~이다"는 `What I actually want is…` 로 문장 머리에 초점을 세운다. 꾸미는 말이 긴 한국어 명사구는 `a skill that helps me decide A and B so I can C` 처럼 관계절과 목적절로 풀어야 한다. "업무 분담"은 `division of work`(또는 `who does what`), "개발 건"은 `development work` 나 `project`.

### 카드 12 — 이런 스킬이면 좋겠다   (내가 쓴 한글)
- 내가 쓴 한글: "분할을 하되 어떤식으로 파일 구조와 작업 방식을 가져갈 지 가이드를 알려주고 AGENTS.md가 있으면 업데이트 해주는 스킬이 좋음."   (출처: transcript:[user])
- 자연스러운 영어: I'd prefer a skill that still does the split but also gives guidance on how to lay out the files and how to work, and updates AGENTS.md if there is one.
- 왜 이렇게: "~이 좋음"은 선호를 밝히는 말이라 `I'd prefer…`. "~하되"는 "그건 그대로 하고, 거기에 더해"라는 뜻이라 `still does A but also B` 로 옮긴다. "AGENTS.md가 있으면"은 `if there is one` 으로, 대명사 `one` 이 반복을 피한다. "파일 구조를 가져가다"는 `lay out the files`.

### 카드 13 — 더 나은 방법이 있는지 조사 부탁   (내가 쓴 한글)
- 내가 쓴 한글: "지금까지 skewnono 방식으로 해왔는데, 그거보다 좋은 방법론이 있을지 스터디도 해줘."   (출처: transcript:[user])
- 자연스러운 영어: I've been doing it the skewnono way so far. Could you also look into whether there's a better approach?
- 왜 이렇게: "스터디하다"를 `study` 로 옮기면 "공부하다"에 가깝다. 조사 부탁은 `look into`, `research`. "~방식으로"는 `the skewnono way` 처럼 `the ~ way` 를 부사처럼 쓴다. "방법론"은 `methodology` 보다 `approach` 가 일상 업무에서 덜 거창하다.

### 카드 14 — 제3자에게도 물어봐 달라   (내가 쓴 한글)
- 내가 쓴 한글: "skill 구성에 있어서 재검토 해야할 게 있는 지 codex (via herdr)에게도 물어봐줘."   (출처: transcript:[user])
- 자연스러운 영어: Could you also ask Codex (via herdr) whether anything in the skill's structure needs a second look?
- 왜 이렇게: "~에 있어서"는 번역하지 않고 `in the skill's structure` 로 끝낸다. "재검토해야 할 게 있는지"는 `whether anything needs a second look` 이 구어, `needs to be reconsidered` 가 격식. "~에게도"의 `also` 는 동사 앞에 둔다.

### 카드 15 — 어떤 파일을 고쳐야 하나   (내가 쓴 한글)
- 내가 쓴 한글: "두 파일은 어떤 파일을 손봐야 하는거야?"   (출처: transcript:[user])
- 자연스러운 영어: Which two files are the ones that need touching up?
- 왜 이렇게: "손보다"는 크게 고치는 게 아니라 다듬는다는 느낌이라 `touch up`, `tweak` 이 맞다. 더 단순하게 `Which two files need to be changed?` 도 좋다. `need + -ing` 는 수동 의미(`need touching up` = `need to be touched up`)라는 점을 기억해 둔다.

### 카드 16 — 반영하고 재검토 맡기기   (내가 쓴 한글)
- 내가 쓴 한글: "응, 반영하고 codex에게 재검토 맡겨줘"   (출처: transcript:[user])
- 자연스러운 영어: Yes, apply those and have Codex review it again.
- 왜 이렇게: 피드백을 "반영하다"는 `reflect` 가 아니라 `apply`, `incorporate`, `address`. `reflect` 는 "비추다, 나타내다"라서 `apply the feedback` 이 자연스럽다. "~에게 맡기다"는 사역 `have Codex review` 가 가장 짧다. `ask Codex to re-review` 도 가능.

### 카드 17 — 항상 세로 분할로   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 herdr pane은 항상 vertical mode로" / "vertical은 양옆으로 좌우로 pane을 만드는거야"   (출처: transcript:[user])
- 자연스러운 영어: Also, always open herdr panes as a vertical split. / By vertical, I mean side by side, with the panes left and right.
- 왜 이렇게: 용어를 정의할 때는 `By X, I mean Y` 가 표준 틀이다. "양옆으로 좌우로"는 `side by side` 한 표현이면 된다. 터미널에서 vertical split 은 도구마다 뜻이 달라(구분선이 세로 vs 배치가 세로) 실제로 오해가 잦으니, 이렇게 한 줄로 풀어 주는 습관이 유용하다.

### 카드 18 — 닫고 새로 열어서 확인 맡기기   (내가 쓴 한글)
- 내가 쓴 한글: "닫고 오른쪽에 새로 열어서 확인 맡겨줘" / "pane 닫아줘"   (출처: transcript:[user])
- 자연스러운 영어: Close it, open a new one on the right, and have it verify the fix. / Close the pane, please.
- 왜 이렇게: 동작 셋을 `A, B, and C` 명령형으로 나열한다. "새로 열다"는 `open a new one` 으로, `newly open` 은 어색하다. "확인 맡기다"는 다시 `have it verify`. 무엇을 확인하는지(`the fix`, `the last change`) 목적어를 채워야 영어 문장이 선다.

### 카드 19 — 내 이해가 맞는지 확인하기   (내가 쓴 한글)
- 내가 쓴 한글: "home office split skill 소개에 새 개발건을 시작할 때라고 써있는데, 이는 현재 repo에서 큰 변화를 주는 것도 포함하는 것이지?"   (출처: transcript:[user])
- 자연스러운 영어: The description of the home-office-split skill says "when starting new development work." That also covers making major changes to an existing repo, right?
- 왜 이렇게: "~라고 써 있다"는 `The description says…` 로, 문서가 주어다(`It is written that` 은 고어투). "포함하는 것이지?"처럼 확인을 구하는 말끝은 `…, right?` 가 가장 가볍고, `doesn't it?` 부가의문문도 된다. "포함하다"는 범위를 말하니 `include` 보다 `cover`. "현재 repo"는 `current` 보다 `an existing repo` 가 "새 건"과 대비된다.

### 카드 20 — 그렇게 바꿔 줘   (내가 쓴 한글)
- 내가 쓴 한글: "응, 그렇게 바꿔줘"   (출처: transcript:[user])
- 자연스러운 영어: Yes, go ahead and change it.
- 왜 이렇게: 제안에 동의하며 실행을 맡길 때는 `go ahead and ~` 가 관용이다. "그렇게"를 살리려면 `Yes, change it to that.` 더 짧게는 `Yes, do that.` 세 가지 모두 채팅에서 자연스럽다.

### 카드 21 — 유일한 증거는 스스로를 증명해야 한다   (고급 한글 · 번역)
- 한글 원문: "손으로 옮기는 한 줄이 유일한 증거이니, 그 줄이 스스로를 증명해야 합니다."   (출처: transcript:[assistant])
- 자연스러운 영어: The one hand-typed line is the only evidence we get, so that line has to be self-verifying.
- 번역 포인트: "손으로 옮기는"은 관계절(`that is carried over by hand`)보다 복합형용사 `hand-typed` 가 짧다. "스스로를 증명하다"를 `prove itself` 로 옮기면 "실력을 입증하다"로 읽히기 쉬워서 `be self-verifying`, `carry its own proof` 를 고른다. "~이니"는 `so` 로 가볍게 잇는다.

### 카드 22 — 만들수록 어긋난다   (고급 한글 · 번역)
- 한글 원문: "시뮬레이터는 만들수록 실제 장비와 어긋나 유지 비용만 쌓입니다."   (출처: transcript:[assistant])
- 자연스러운 영어: The more of a simulator you build, the further it drifts from the real equipment, and all you accumulate is maintenance cost.
- 번역 포인트: "~할수록 ~하다"는 `The more…, the further…` 비교급 구문 그대로다. "어긋나다"는 시간이 가며 벌어지는 것이라 `drift from` 이 맞고, `differ from` 은 정적인 차이만 말한다. "~만 쌓인다"의 "만"은 `all you accumulate is…` 로 주어 자리에 올려 강조한다.

### 카드 23 — 두 가지가 섞여 버린다   (고급 한글 · 번역)
- 한글 원문: "아직 확인되지 않은 능력으로 시작하면 판정 기준을 시험하는 건지 장비 미지수를 푸는 건지 섞여 버립니다."   (출처: transcript:[assistant])
- 자연스러운 영어: If we start with an unconfirmed capability, we won't be able to tell whether we're testing the decision criteria or working out unknowns in the equipment.
- 번역 포인트: "섞여 버린다"를 `get mixed` 로 직역하면 무엇이 섞이는지 흐려진다. 영어는 "구별할 수 없게 된다"로 뒤집어 `we won't be able to tell whether A or B` 로 쓴다. 통계 용어를 빌려 `the two get confounded` 도 가능하다. "미지수를 풀다"는 `work out unknowns`.

### 카드 24 — 버그가 아니라 정보다   (고급 한글 · 번역)
- 한글 원문: "`H2=FAIL`은 버그가 아니라 정보이고, 그 정보를 어떤 구현이 처리했는지가 합격 여부를 가릅니다."   (출처: transcript:[assistant])
- 자연스러운 영어: `H2=FAIL` is information, not a bug; what decides pass or fail is which implementation handled that information.
- 번역 포인트: "A가 아니라 B"는 영어에서 긍정을 먼저 두는 `B, not A` 순서가 힘이 있다. 뒷절은 한국어처럼 긴 주어(`which implementation handled…`)를 앞세우면 머리가 무거워지니 `what decides X is Y` 로 뒤집었다. "가르다"는 `decide`, `determine`. "합격 여부"는 `pass or fail`.
