# 2026-09-20 — 코칭

> 오늘 `[user]` 한국어는 auto-recipe-creator 의 align 보정 요청 한 건인데 여섯 문장짜리라 (a) 카드 5장으로 나눴다. (b) 는 같은 세션의 어시스턴트 완료 보고에서 4문장을 골랐다. 영어 다듬기는 `[user]` 영어 4장이다. `apply all four` 와 `commit and push` 는 고칠 데가 없어 뺐다. equipment-data-map 세션의 `<pasted_content>` 영어는 Codex 가 herdr 로 보낸 글이라 내 영작으로 보지 않았다.

## 한글→영어

### 카드 1 — 실전에 쓸 수 있을 정도로   (내가 쓴 한글)
- 내가 쓴 한글: "지금 manual_align_correction.py 를 진행해서 실전에 활용할 수 있을 정도로 개선하고 싶음."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: I'd like to keep working on `manual_align_correction.py` and get it to the point where we can actually use it on the real tool.
- 왜 이렇게: "~할 수 있을 정도로"는 `to the point where …` 가 가장 가깝다. 더 짧게는 `good enough to use in the field` 도 된다. "실전"을 `real battle` 로 옮기면 안 된다. 소프트웨어면 `in production`, 장비 현장이면 `in the field` 나 `on the real tool` 이 맞는다. "개선하고 싶음" 같은 음슴체는 영어에 대응하는 문체가 없으니 `I'd like to` 나 `I want to` 로 주어를 세운다. "진행해서 개선"은 동사 둘을 다 살리기보다 `keep working on it and get it to …` 로 흐름을 잇는 편이 자연스럽다.

### 카드 2 — 중앙이면 잘 찾는데 모서리면 못 찾는다   (내가 쓴 한글)
- 내가 쓴 한글: "문제는 처음 접속 화면에서 live sem box에 align key (die fit target)이 중앙 부근에 있으면, agent가 align point를 잘 집어냄. 하지만 DFT가 화면 모서리 부근에 있으면 찾아내지 못함."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: On the first screen after connecting, the agent picks out the align point just fine as long as the align key (the die-fit target, DFT) is near the center of the live SEM box. The problem is when the DFT is near a corner of the screen — then it can't find it.
- 왜 이렇게: 한국어는 "문제는"을 먼저 던져 놓고 정상 케이스부터 말해도 어색하지 않다. 영어에서 `The problem is that` 바로 뒤에 "잘 찾는다"가 오면 그게 문제라는 말이 되어 버린다. 그래서 정상 → 문제 순으로 두고 `The problem is when …` 을 둘째 문장으로 옮겼다. "잘 집어냄"은 `picks out … just fine`, "~이면(그런 한)"은 `as long as` 가 어울린다. "모서리"는 `corner`, "가장자리"는 `edge` 로 구별한다. 어시스턴트 보고서가 `edge` 조각과 `corner` key 를 따로 다룬 것도 이 구별 때문이다.

### 카드 3 — 가까이 와도 못 찾고 다른 데로 간다   (내가 쓴 한글)
- 내가 쓴 한글: "이때 search around로 진입하는데, 역시 DFT가 중앙 부분에 접근해도 찾아내지 못하고 다른 영역으로 찾으러 진행함."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: At that point it falls back to search-around, but even when the DFT comes close to the center, it still doesn't recognize it and moves on to search other areas.
- 왜 이렇게: "진입하다"는 `enter` 도 되지만 1차 방법이 실패해 다음 수단으로 넘어가는 상황이라 `fall back to` 가 정확하다. "~해도"는 `even when`, "역시 (또) 못 찾고"는 `still doesn't` 로 기대가 어긋났음을 담는다. "다른 영역으로 찾으러 진행함"은 `moves on to search other areas` 또는 `goes looking elsewhere` 다. 주어를 `it` 하나로 끌고 가면 동사 셋(`falls back`, `doesn't recognize`, `moves on`)이 순서대로 읽힌다.

### 카드 4 — 근본 원인을 찾아서 해결해야 한다   (내가 쓴 한글)
- 내가 쓴 한글: "search around에서 DFT를 인식 못하고 align point를 못 찾아내는 근본적인 원인을 찾아내고 해결해야함."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: We need to get to the root cause of why search-around fails to recognize the DFT, and so never finds the align point, and fix it.
- 왜 이렇게: "근본적인 원인"은 `fundamental reason` 보다 `root cause` 가 개발 현장의 굳은 말이다. 한국어는 "~하는 원인"처럼 긴 관형절을 명사 앞에 붙이지만 영어는 `the root cause of why …` 로 뒤에 푼다. "인식 못하고 못 찾아내는"은 원인과 결과 관계라 `fails to recognize …, and so never finds …` 로 이었다. "찾아내고 해결"은 `find and fix` 로 짝지어도 좋다(`find and fix the root cause`). `get to the root cause` 는 "파고들어 닿는다"는 그림이 있어 `find` 보다 과정이 느껴진다.

### 카드 5 — Codex 와 의논해서 코드에 반영해 줘   (내가 쓴 한글)
- 내가 쓴 한글: "herdr로 codex와 의논하면서 해결 방안을 마련하고 코드에 반영해줘."   (출처: transcript:[user] auto-recipe-creator)
- 자연스러운 영어: Talk it through with Codex over herdr, work out a fix, and apply it to the code.
- 왜 이렇게: "반영하다"를 `reflect` 로 옮기는 것이 한국어 화자의 대표적인 버릇이다. `reflect it in the code` 는 뜻은 통해도 원어민은 `apply`, `implement`, `put it in` 을 쓴다. `reflect` 는 "문서가 현재 상태를 반영한다"처럼 비추어 보여 준다는 뜻일 때 어울린다. "의논하면서"는 `discuss` 보다 `talk it through with` 가 "끝까지 이야기해 결론을 낸다"는 어감이라 맞다. "해결 방안을 마련하다"는 `work out a fix` 나 `come up with a fix` 다. 도구를 거쳐서 한다는 "~로"는 `over herdr` 나 `via herdr` 로 쓴다.

### 카드 6 — 합성 장면에서만 검증했다   (고급 한글 · 번역)
- 한글 원문: "검증은 Mac 합성 장면에서만 했고, 오피스 실장비에서는 아직 돌려보지 못했습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: I've only verified this on synthetic scenes on the Mac; I haven't been able to run it on the real tool at the office yet.
- 번역 포인트: "~만 했고 … 아직 못했습니다"는 지금 시점의 검증 범위를 밝히는 말이라 두 절 모두 현재완료가 맞다. `only` 와 `yet` 이 한국어 "만"과 "아직"을 그대로 받는다. 두 절을 `and` 대신 세미콜론으로 이으면 "한 것 / 못 한 것"의 대비가 선다. "돌려보다"는 `run it` 이면 충분하다. 시도의 어감을 살리려면 `try it on` 도 된다. "실장비"는 `actual equipment` 보다 팹 현장 말투로 `the real tool` 이 짧다.

### 카드 7 — 원인이 네 가지 더 겹쳐 있었다   (고급 한글 · 번역)
- 한글 원문: "search-around가 DFT 옆을 지나가면서도 못 잡은 데에는 원인이 네 가지 더 겹쳐 있었습니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: Four more causes piled on top of that, which is why search-around missed the DFT even as it passed right by it.
- 번역 포인트: 한국어는 "~한 데에는 원인이 있었다"로 결과를 앞에, 원인을 뒤에 둔다. 영어는 원인을 주어로 세우고 결과를 `which is why …` 로 잇는 편이 읽기 쉽다. "겹쳐 있다"는 `overlap` 이 아니다. 문제가 쌓였다는 뜻이라 `pile on top of`, `stack up`, `compound` 가 맞는다. "지나가면서도"의 양보는 `even as it passed right by it` 로 옮긴다. 여기서 `right` 가 "바로 옆"의 아쉬움을 살린다.

### 카드 8 — 단서로만 쓰고 판정은 게이트가 한다   (고급 한글 · 번역)
- 한글 원문: "이동 방향을 정하는 단서로만 쓰고, key가 맞는지는 옮긴 뒤 기존 게이트가 다시 판정합니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The fragment only tells us which way to move; after the move, the existing gate still decides whether it's really the key.
- 번역 포인트: 원문 앞 절에는 주어가 없다. 영어는 주어 없이 못 쓰니 무엇을 단서로 쓰는지(`The fragment`)를 찾아 세워야 한다. 수동 `is used only as a hint for …` 도 되지만 무생물 주어에 `tells us` 를 주면 더 짧고 능동적이다. "key가 맞는지는"은 화제를 앞세운 한국어 어순인데, 영어에서는 `decides whether …` 의 목적어 자리로 보낸다. "다시 판정"은 `re-judge` 보다 `still decides` 가 낫다. 힌트가 있어도 최종 판단 권한은 그대로라는 뜻을 `still` 이 맡는다.

### 카드 9 — 데이터 없이 잡은 값   (고급 한글 · 번역)
- 한글 원문: "가장자리 조각 판정 임계는 데이터 없이 잡은 값입니다."   (출처: transcript:[assistant] auto-recipe-creator)
- 자연스러운 영어: The thresholds for judging edge fragments were picked without any real data behind them.
- 번역 포인트: "값을 잡다"의 "잡다"는 `catch` 도 `grab` 도 아니고 `pick` 이나 `set` 이다. "데이터 없이"를 `without data` 로만 쓰면 밋밋한데 `without any real data behind them` 이라고 하면 "뒷받침이 없다"는 뜻이 선다. 한 단어로는 `uncalibrated`, 구어로는 `an educated guess` 도 같은 고백이다. 임계가 `MIN_SEL`, `MIN_VISIBLE` 두 개라 복수로 옮겼다. 한국어는 단복수를 안 가리니 영어로 옮길 때마다 개수를 확인해야 한다.

## 영어 다듬기

### 카드 1 — 필요하면 개선해 줘
- 내가 쓴 영어: "improve the @DESIGN.md if needed."   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Review DESIGN.md and improve it wherever it's outdated or unclear.
- 왜: 문법 오류는 없다. 다만 `if needed` 는 무엇이 "필요"인지 기준을 상대에게 통째로 넘긴다. 이번에 어시스턴트는 새 섹션을 추가하고 죽은 참조 여섯 개를 고치는 큰 작업으로 받아들였다. 가볍게 훑기만 바랐다면 `Skim DESIGN.md and fix anything that's clearly wrong.` 처럼 범위를 말해 두는 편이 안전하다. 파일 이름 앞의 `the` 는 빼는 쪽이 보통이다(`the README` 는 보통명사처럼 굳어서 예외).

### 카드 2 — 한 번 움직이고 멈춘다
- 내가 쓴 영어: "the search around stops after one movement. something's wrong."   (출처: transcript:[user] auto-recipe-creator)
- 더 나은 표현: Search-around stops after a single move when it should keep sweeping. Something's off.
- 왜: 문법 오류는 없다. 버그 보고는 "본 것"에 "기대한 것"을 붙이면 받는 쪽이 증상을 바로 좁힌다. `when it should keep sweeping` 이 그 역할을 한다. `a single move` 는 `one movement` 보다 "딱 한 번뿐"이 강조된다. 스테이지나 커서가 한 번 이동하는 것은 `movement` 보다 `move` 가 흔하다. 기능 이름으로 쓸 때는 하이픈을 넣어 `search-around` 로 묶으면 동사구와 헷갈리지 않는다. `Something's off` 는 `something's wrong` 의 가벼운 구어 버전이다.

### 카드 3 — 다음 실행 뒤에 알려 줄게
- 내가 쓴 영어: "commit and push. I will tell you grid search result after the next running"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `after the next running` → `after the next run`. "한 번의 실행"은 셀 수 있는 명사 `run` 이다. `running` 은 동명사라 `the next` 로 셀 수 없다. `grid search result` → `the grid search result`. 서로 아는 특정 결과라 정관사가 필요하다.
- 더 나은 표현: Commit and push. I'll send you the grid search line after the next run.
- 왜: 채팅에서 `I will` 을 풀어 쓰면 다짐처럼 무겁게 들려 `I'll` 이 자연스럽다. 어시스턴트가 달라고 한 것은 콘솔의 한 줄이라 `result` 보다 `the grid search line` 이 정확하다. 실제로 어시스턴트도 `the line to grab is:` 라고 받았다. `I'll let you know what it prints` 도 좋다.

### 카드 4 — 커밋 안 된 변경을 처리해 줘
- 내가 쓴 영어: "fix the uncommited changes"   (출처: transcript:[user] auto-recipe-creator)
- 정정: `uncommited` → `uncommitted`. `commit` 은 강세가 뒤 음절에 있어 어미를 붙일 때 `t` 를 겹쳐 쓴다(`committed`, `committing`). `edit` → `edited` 처럼 강세가 앞에 있으면 겹치지 않는다.
- 더 나은 표현: Commit and push the pending changes.
- 왜: `fix` 는 "고치다"라서 "커밋 안 된 변경 속의 버그를 고쳐라"로도 읽힌다. 어시스턴트가 `Taking that as: commit and push the pending edits.` 라고 해석부터 밝히고 움직인 이유다. 원하는 동작을 동사로 그대로 말하면 해석할 여지가 사라진다. "알아서 정리해 줘"의 어감을 살리고 싶다면 `Take care of the uncommitted changes.` 가 `fix` 보다 안전하다.
