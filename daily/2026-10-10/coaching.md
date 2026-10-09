# 2026-10-10 — 코칭

> 내가 쓴 글은 skewnono 세션 둘과 pm-notes 세션 하나에서 나왔다. 한국어는 열 건이고 두 가지를 한꺼번에 물은 긴 메시지는 문장 단위로 나눠 카드 열두 장이 됐다. 영어는 한 건. 세션에 딸려 온 스킬 문서(Artifact 지침, Herdr, browser-verify)와 `/clear` 기록은 `[user]` 로 찍혔어도 내가 쓴 글이 아니어서 다루지 않았다. 번역 정독은 어시스턴트 보고에서 네 문장을 골랐다.

## 한글→영어

### 카드 1 — 사용자별로 나뉘어 컴파일되는지 확인   (내가 쓴 한글)
- 내가 쓴 한글: "npm run build를 했을 때 ebeam 사용자와 afm 사용자가 구분되어 각자 원하는 파일만을 브라우져에서 사용할 수 있게 compile이 되고 있는 건지 확인해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Can you check whether `npm run build` splits the output so that e-beam users and AFM users each download only the files they need?
- 왜 이렇게: "~인 건지 확인해줘"는 `check whether …` 로 받는다. `check if` 도 되지만 둘 중 하나를 가리는 물음에는 `whether` 가 또렷하다. "구분되어 … compile 이 되고 있는"은 수동으로 옮기지 않고 빌드를 주어로 세워 `splits the output` 이라 하면 짧다. 번들러 용어로는 `code-split per route`. "각자"는 `each` 를 주어 뒤에 둔다(`users each download`). "브라우저에서 사용할 수 있게"는 결국 내려받는 파일 이야기여서 `download` 가 정확하다.

### 카드 2 — 어떤 식으로 쓰이는지 궁금하다, 가르쳐줘   (내가 쓴 한글)
- 내가 쓴 한글: "나는 트랜스포머, attention이 LLM을 만드는데 어떤 식으로 사용되는 지 궁금하다. 그것에 대해서 나를 가르켜줘."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'm curious how transformers and attention are actually used to build an LLM. Can you walk me through it?
- 왜 이렇게: "궁금하다"는 `I'm curious how …` 또는 `I wonder how …`. 뒤는 간접의문문이라 평서문 어순(`how A are used`)이다. "그것에 대해서 나를 가르쳐줘"를 `teach me about it` 으로 옮겨도 되지만 차근차근 설명해 달라는 부탁에는 `walk me through it` 이 자연스럽다. "만드는데"는 목적이어서 `to build`. 종류 전체를 말하므로 `transformers` 는 복수, `attention` 은 셀 수 없는 명사로 둔다.

### 카드 3 — 문서와 시각화로 이해를 도와줘   (내가 쓴 한글)
- 내가 쓴 한글: "md 파일을 만들고 html로 시각화를 해서 내가 잘 이해할 수 있게 도와줘."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Write it up as a Markdown file and add an HTML visualization so it's easier for me to follow.
- 왜 이렇게: "내가 잘 이해할 수 있게 도와줘"를 `help me understand well` 로 옮기면 `well` 이 어색하다. 영어는 `so it's easier to follow` 나 `to help it sink in` 처럼 쉬워진다는 쪽으로 말한다. "md 파일을 만들고"는 `write it up as …`. `write up` 은 정리해서 문서로 쓴다는 뜻이다. "html 로 시각화"는 `an HTML visualization` 이고 손으로 눌러 보는 페이지를 원하면 `an interactive HTML page`.

### 카드 4 — 서비스될 때 prefill·cache·양자화   (내가 쓴 한글)
- 내가 쓴 한글: "추가로 LLM이 서비스 될 때 prefill, cache가 어떻게 활용되고, 양자화는 어떤 방식으로 진행되어 서비스 되는 건지, 궁금해."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'd also like to know how prefill and caching come into play when an LLM is served, and how quantization is done before a model goes into production.
- 왜 이렇게: "추가로 … 궁금해"는 `I'd also like to know` 또는 `One more thing —`. "LLM 이 서비스될 때"는 `when an LLM is served` 이고 그 일 전체는 명사로 `serving` 또는 `inference` 라 부른다. `serviced` 는 정비받는다는 뜻이어서 쓰지 않는다. "활용되고"는 `are used` 도 맞지만 "어디서 등장해 무슨 구실을 하는가"를 묻는 것이면 `come into play` 가 어울린다. `cache` 는 물건, `caching` 은 기법. "양자화가 진행되어 서비스되는"은 순서가 중요하므로 `before a model goes into production` 으로 풀었다.

### 카드 5 — 데이터셋을 어떻게 준비해야 하는지   (내가 쓴 한글)
- 내가 쓴 한글: "또 LLM을 만들 때 data set을 어떻게 준비해야 하는 지 궁금해"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'm also wondering how you go about preparing a dataset when you're building an LLM.
- 왜 이렇게: "어떻게 ~해야 하는지"는 `how to prepare` 로 줄여도 되고 절차를 묻는 느낌을 살리려면 `how you go about -ing` 를 쓴다. 여기서 `you` 는 상대가 아니라 일반 사람을 가리킨다. `dataset` 은 요즘 한 단어로 붙여 쓴다. "또"는 `also` 를 be 동사 뒤에 둔다(`I'm also wondering`).

### 카드 6 — 상의해서 확장에 문제없는 구조인지 확인   (내가 쓴 한글)
- 내가 쓴 한글: "codex (via herdr)와 상의해서 afm의 codebase가 scale up 하기 문제 없는 구조로 되어 있는지 확인해줘."   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Talk it over with Codex (via Herdr) and check whether the AFM codebase is structured in a way that will scale.
- 왜 이렇게: "상의해서"는 `consult with` 가 격식이고 `talk it over with` 가 구어다. 토론을 붙이라는 뜻이면 `get a second opinion from Codex`. "scale up 하기 문제 없는 구조"는 영어에서 `scale` 을 자동사로 써서 `will scale` 한마디면 된다(`Does it scale?`). `scale up` 은 서버 사양을 올린다는 좁은 뜻으로 읽히기 쉽다. "~로 되어 있는지"는 `is structured in a way that …`. 약어는 대문자 `AFM`.

### 카드 7 — ~로 추가하자 / 안 바꿔도 되는 거지?   (내가 쓴 한글)
- 내가 쓴 한글: "compact를 opt-in으로 추가하자. redis와 scheduler를 통해서 저장되는 데이터는 변경 안해도 되는거지?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Let's add compact as an opt-in. We don't need to change the data that's stored via Redis and the scheduler, right?
- 왜 이렇게: "~로 추가하자"는 `Let's add A as B`. `opt-in` 은 명사로도 형용사로도 쓴다(`an opt-in flag`). "~해도 되는 거지?"처럼 그렇다고 믿으면서 확인만 받는 물음은 평서문 끝에 `, right?` 를 붙이는 것이 구어에서 가장 흔하고 격식을 올리면 부가의문문 `do we?`. "안 해도 된다"는 `don't need to` 또는 `don't have to` 이고 `must not` 은 금지여서 뜻이 달라진다. "~를 통해서 저장되는"은 `stored via` 나 `written by`.

### 카드 8 — ~도 진행해줘   (내가 쓴 한글)
- 내가 쓴 한글: "캐시 수정도 진행해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Go ahead with the cache fix as well.
- 왜 이렇게: 미뤄 둔 일을 이제 하라는 "진행해줘"는 `go ahead with …` 가 꼭 맞는다. `proceed with` 는 격식이고 `do … too` 는 가장 평이하다. "캐시 수정"은 명사 둘을 붙여 `the cache fix`. 앞에서 합의한 그 수정이므로 `the` 를 쓴다. "도"는 문장 끝에 `as well` 이나 `too`.

### 카드 9 — 숫자는 이 문구로 바꿔줘   (내가 쓴 한글)
- 내가 쓴 한글: "숫자는 "크게 줄었습니다"로 바꿔줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Replace the number with "크게 줄었습니다" instead.
- 왜 이렇게: "A 를 B 로 바꾸다"는 `replace A with B` 또는 `change A to B`. 전치사가 동사마다 다르다. `replace A to B` 는 틀린 조합이다. `swap A for B` 도 구어에서 쓴다. 문두의 "숫자는"은 화제를 꺼내는 말이라 영어에서는 그냥 목적어 자리에 둔다. 영어 문구로 바꾸는 상황이었다면 `Just say "significantly reduced" instead of giving the number.`

### 카드 10 — 접근이 가능하면 상태 표시에도 넣어줘   (내가 쓴 한글)
- 내가 쓴 한글: "landing page에 AFM 3대 데이터 접근이 가능하면 system status 에도 afm 장비 표시해줘"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: If data from the three AFM tools is accessible, show the AFM tools in the System Status section on the landing page too.
- 왜 이렇게: "접근이 가능하면"은 `If … is accessible` 또는 `If we can reach …`. `data` 는 요즘 단수 취급이 보통이라 `is`. "AFM 3대"는 `the three AFM tools`. 한국어 "대"는 영어에서 `tools`·`machines`·`units` 같은 명사로 바뀐다. 페이지 위에 있는 것은 `on the landing page`, 그 안의 구역은 `in the System Status section` 으로 전치사가 갈린다. "표시해줘"는 `show` 가 무난하고 목록에 넣는다는 뜻이면 `list`.

### 카드 11 — 그렇게 해줘, 이 표기로   (내가 쓴 한글)
- 내가 쓴 한글: "그렇게 해줘 조회가능으로"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Yes, do that — label it "조회 가능".
- 왜 이렇게: 상대 제안을 받아들이는 "그렇게 해줘"는 `Yes, do that.` `Go with that.` `Let's do it that way.` 가운데 고른다. `Do like that` 은 영어에 없는 말이다. "~으로"는 표기를 정하는 것이므로 `label it "…"` 또는 `use "…" as the label`. 여러 안 가운데 하나를 고르는 말투면 `Go with "조회 가능".`

### 카드 12 — 서버 띄웠어   (내가 쓴 한글)
- 내가 쓴 한글: "flask 5050 실행했어"   (출처: transcript:[user] skewnono-v3-nuxt)
- 자연스러운 영어: Flask is back up on port 5050.
- 왜 이렇게: 직역 `I ran Flask 5050` 도 통하지만 상대가 알고 싶은 것은 지금 서버가 떠 있느냐여서 상태로 말하는 편이 낫다. `is up` 은 "떠 있다", `back` 을 넣으면 내려갔다가 다시 떴다는 뜻이 된다. 내가 한 일을 말하려면 `I've started Flask on 5050.` 방금 끝낸 일이 지금 상태로 이어지므로 현재완료다. 포트는 `on port 5050`.

### 카드 13 — 한 토큰이라도 다르면   (고급 한글 · 번역)
- 한글 원문: "중간에 한 토큰이라도 다르면 그 뒤는 전부 다시 계산합니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: If even a single token differs partway through, everything after it has to be recomputed.
- 번역 포인트: "한 ~이라도"는 `even a single …` 으로 옮기면 최소량을 강조하는 맛이 산다. "중간에"는 `in the middle` 보다 `partway through` 가 "앞에서부터 읽어 가다 어느 지점에서"라는 뜻에 가깝다. "그 뒤는 전부"는 `everything after it` 을 주어로 세우고 수동 `has to be recomputed` 로 받았다. 한국어는 주어 없이 "계산합니다"로 끝나는데 영어는 주어를 세워야 하므로 계산 대상을 주어로 올린 것이다.

### 카드 14 — 학습은 돌아가지만 조용히 나빠진다   (고급 한글 · 번역)
- 한글 원문: "손으로 조립해 어긋나면 학습은 돌아가지만 결과가 조용히 나빠집니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: If you assemble the prompt by hand and get the format slightly wrong, training still runs, but the results quietly get worse.
- 번역 포인트: "어긋나면"에는 주어도 목적어도 없어서 영어로는 무엇이 어긋나는지 채워야 한다. 문맥이 chat template 이므로 `get the format slightly wrong` 으로 풀었다. "학습은 돌아가지만"의 "은"은 대조 표시이고 영어에서는 `still` 이 그 일을 맡는다. "조용히 나빠진다"는 `quietly get worse` 또는 `silently degrade`. 오류 메시지 없이 품질만 떨어진다는 뜻으로 엔지니어링 글에서 `silently` 를 자주 쓴다.

### 카드 15 — 무엇을 아는가보다 어떻게 행동하는가   (고급 한글 · 번역)
- 한글 원문: "미세조정은 "무엇을 아는가"보다 "어떻게 행동하는가"를 바꾸는 데 맞습니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Fine-tuning is better suited to changing how a model behaves than what it knows.
- 번역 포인트: "A 보다 B 를 바꾸는 데 맞다"는 `is better suited to changing B than A` 로 비교급 하나에 담는다. 한국어 순서(아는가 → 행동하는가)와 달리 영어는 긍정하는 쪽 `how it behaves` 를 먼저 둔다. 따옴표로 묶인 두 물음은 간접의문문 `how a model behaves`, `what it knows` 가 되어 따옴표가 필요 없다. `be suited to` 뒤는 전치사 `to` 여서 동명사 `changing` 이 온다.

### 카드 16 — 확신하시면 이쪽이 낫습니다   (고급 한글 · 번역)
- 한글 원문: "외부에서 이 목록을 토큰으로 호출하는 사람이 없다고 확신하시면 slim 기본값이 낫습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt)
- 자연스러운 영어: If you're confident that no one outside is calling this list endpoint with a token, making slim the default is the better option.
- 번역 포인트: "~하는 사람이 없다"는 `no one is -ing` 로 부정을 주어에 싣는다. `there is nobody who calls` 는 길다. "확신하시면"의 높임은 영어에 대응이 없으니 `If you're confident that …` 로 충분하다. "slim 기본값"은 명사구 그대로 두면 뜻이 흐려서 `making slim the default` 라는 동명사구로 풀었다. `make A B` 5형식. "낫습니다"는 둘 중 하나를 고르는 자리라 `the better option`.

## 영어 다듬기

### 카드 17 — 공지사항에 오늘 한 일 반영
- 내가 쓴 영어: "Good. update what we have done in the 공지사항."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `update what we have done in the 공지사항` → `update the 공지사항 with what we have done`. `update` 의 목적어는 고쳐지는 대상(공지사항)이고 새로 넣을 내용은 `with` 로 붙인다. 원문대로면 "공지사항에서 우리가 한 일을 수정하라"로 읽힌다. 문장 첫 글자는 대문자 `Update`.
- 더 나은 표현: Good. Add today's changes to the notices page.
- 왜: 새 항목을 올리라는 뜻이면 `update` 보다 `add A to B` 가 정확하다. `what we have done` 은 `today's changes` 나 `what we shipped today` 로 줄이면 무엇을 적을지가 또렷해진다. 공지 글을 새로 쓰라는 부탁이면 `Post a notice about today's changes.` 도 된다.
