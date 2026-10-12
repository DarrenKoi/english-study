# 2026-10-13 — 코칭

> 내가 쓴 글은 세션 둘에서 나왔다. pm-notes 의 장비 데이터 매핑 Agent 기획(한국어)과 skewnono 의 개인화 페이지 제안(영어)이다. 한국어 메시지는 열세 건인데 한 메시지에 문장이 여럿이라 나눠서 카드 스물일곱이 됐다. 영어는 세 건을 문장별로 나눠 여덟 장. `커밋하고 push 해줘` 는 전에 다뤄서 뺐고 `/model`·`/clear` 명령, task-notification, 스킬 문서, 하위 에이전트 보고, 이 저장소의 배치 프롬프트도 다루지 않았다. 번역 정독은 어시스턴트 답변에서 네 문장을 골랐다.

## 한글→영어

### 카드 1 — 계획하는 안들을 작성하고 싶어   (내가 쓴 한글)
- 내가 쓴 한글: "my-task안에 equipment-data-mapping 이라는 폴더를 만들고 여기에 내가 계획하는 안들을 작성하고 싶어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'd like to create a folder called equipment-data-mapping under my-task and write up my proposals there.
- 왜 이렇게: "~이라는 폴더"는 `a folder called X` 또는 `named X`. "안에"는 폴더 경로를 말할 때 `in` 보다 `under` 가 흔하다. "내가 계획하는 안들"을 `the plans that I am planning` 으로 옮기면 겹친다. `my proposals` 나 `the plans I have in mind` 로 줄인다. "작성하다"는 `write up` 이 맞다. 흩어진 생각을 문서로 정리한다는 뜻이 `write` 보다 뚜렷하다.

### 카드 2 — 검/계측 장비를 다루고 있고   (내가 쓴 한글)
- 내가 쓴 한글: "나는 반도체 팹 중에 검/계측 (Inspection/Metorlogy, MI) 장비를 다루고 있고, 이 장비 안에 저장되어 있는 데이터들의 계층/포맷/의미/연결의 의미들을 파악해서 지도화하고 싶어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I work with metrology and inspection (MI) tools in a semiconductor fab, and I want to map the data stored on them: its hierarchy, formats, meanings, and how the pieces relate.
- 왜 이렇게: 철자는 `Metrology` 다. "다루다"는 `handle`(물건을 만지다) 대신 `work with` 나 `am responsible for`. "파악해서 지도화"는 동사 둘을 `map` 하나로 합친다. `map` 에 이미 "파악해서 그린다"가 들어 있다. 슬래시로 이은 네 항목은 콜론 뒤에 풀고, "연결의 의미"는 명사 `connections` 보다 절 `how the pieces relate` 가 자연스럽다. 장비 "안에" 저장된 데이터는 `on the tool` 이다. 디스크에 있는 것은 `on` 으로 받는다.

### 카드 3 — AI Agent 를 설계하고 배포하는 게 목적이야   (내가 쓴 한글)
- 내가 쓴 한글: "이걸 진행해 줄 수 있는 AI Agent를 설계하고 배포하는 게 나의 목적이야."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: My goal is to design and deploy an AI agent that can do this mapping.
- 왜 이렇게: "~하는 게 나의 목적이야"는 `My goal is to …` 로 곧게 받는다. `My purpose is` 는 존재 이유처럼 무겁다. "이걸 진행해 줄 수 있는"을 `that can proceed this` 로 옮기면 틀린다. `proceed` 는 목적어를 받지 않는다. `do`, `carry out`, `handle` 을 쓴다. 한 줄 요약으로는 `The aim is an agent that does this mapping for us.`

### 카드 4 — 같은 모델 안에서도 장비마다 수치가 다를 것이고   (내가 쓴 한글)
- 내가 쓴 한글: "처음에 하나의 장비 모델로 시작하지만 동일 모델 안에서도 장비마다 가지고 있는 데이터의 수치가 다를 것이고 그런 수치들을 비교 분석할 수 있다면 MI 장비들의 H/W 차이점과 개선하기 위해서 어떤 것들을 수정해야 하는 지 파악하는데 도움이 될 것 같아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We'll start with a single tool model, but even within one model the values will differ from tool to tool. If we can compare them, it should help us see where the hardware differs and what needs adjusting to close the gap.
- 왜 이렇게: 한국어 한 문장을 둘로 끊는다. "동일 모델 안에서도"는 `even within one model`, "장비마다"는 `from tool to tool` 이 딱 맞는 관용 틀이다. "비교 분석"은 `compare and analyze` 로 둘 다 쓰지 않아도 `compare` 로 충분하다. "도움이 될 것 같아"는 `I think it will be helpful to understand` 보다 `it should help us see` 가 짧다. `should` 가 "~일 것 같다"의 확신 정도를 맡는다. "개선하기 위해 수정해야 하는 것"은 `what needs adjusting`. 오늘 표현의 `need + -ing` 와 같은 꼴이다.

### 카드 5 — 의미는 유사하나 다른 이름을 쓰는 경우가 많아   (내가 쓴 한글)
- 내가 쓴 한글: "더 나아가 동일 목적의 장비이지만 생산하는 업체가 다를 경우에는 장비 내에서 사용되는 파라미터들이 의미는 유사하나 다른 이름을 쓰는 경우가 많아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Beyond that, tools built for the same purpose by different vendors often use different names for parameters that mean much the same thing.
- 왜 이렇게: "~하는 경우가 많아"는 `there are many cases where` 대신 부사 `often` 하나로 받는다. "생산하는 업체가 다를 경우"도 `if` 절로 풀지 않고 `by different vendors` 로 명사에 붙인다. 장비 제조사는 `maker` 보다 `vendor` 가 팹 용어다. "의미는 유사하나"는 `mean much the same thing`, 더 줄이면 `the same concept under different names`. "더 나아가"는 `Furthermore` 가 논문체라 대화에서는 `Beyond that` 이나 `On top of that` 이 낫다.

### 카드 6 — ontology 활용에도 도움이 될 것 같아   (내가 쓴 한글)
- 내가 쓴 한글: "이런 경우 equipment-data-mapping agent가 비슷한 데이터와 의미를 파악함으로써 ontology 활용에도 많은 도움이 될 것 같아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: If the agent can work out which parameters mean the same thing, that would feed straight into our ontology work.
- 왜 이렇게: "파악함으로써"를 `by grasping` 으로 옮기면 딱딱하다. `work out`(따져서 알아내다)이나 `identify` 를 쓴다. "~에도 많은 도움이 될 것"은 `be very helpful for` 도 맞지만 `feed into`(재료로 흘러 들어가다)가 관계를 더 정확히 말한다. 대응표가 온톨로지의 입력이 된다는 뜻이다. `ontology 활용` 은 `ontology utilization` 대신 `our ontology work` 정도로 둔다.

### 카드 7 — 논리를 탄탄하게 만들고 싶고   (내가 쓴 한글)
- 내가 쓴 한글: "나의 계획 안의 논리를 탄탄하게 만들고 싶고 (이걸 왜 해야하는 지 임원과 매니저를 설득해야함)."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I want to make the case airtight, because I have to convince executives and my manager that this is worth doing.
- 왜 이렇게: "계획안의 논리"는 `the logic of my plan` 보다 `the case` 가 영어다운 말이다. 설득하려고 세우는 논거 전체를 가리킨다(`make the case for`, `a business case`). "탄탄하게"는 `airtight`(빈틈없는), `solid`, `watertight`. "왜 해야 하는지 설득"은 `convince A that this is worth doing` 이 `persuade A why we should do this` 보다 매끄럽다. 괄호 속 이유는 `because` 로 본문에 올린다.

### 카드 8 — 단계별로 수행하고 싶어   (내가 쓴 한글)
- 내가 쓴 한글: "참고로 이를 수행하는 AI Agent를 실제로 구현하기 위해서 필요한 요소들을 마련하고 단계별로 수행하고 싶어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I also want to line up everything we need to actually build the agent, and then do it in phases.
- 왜 이렇게: "참고로"를 `For your reference` 로 옮기면 공문 같다. 덧붙이는 말이면 `also` 로 충분하고, 곁가지 정보일 때만 `FYI` 나 `For context` 를 쓴다. "필요한 요소들을 마련하다"는 `prepare the necessary elements` 대신 `line up everything we need` 또는 `get the prerequisites in place`. "단계별로"는 `step by step`(차근차근)도 되지만 과제 계획에서는 `in phases` 가 맞는 말이다.

### 카드 9 — home 에서 쓰고 office 에서 수행   (내가 쓴 한글)
- 내가 쓴 한글: "이 계획안은 home에서 작성되고 있고, 실제 수행은 office에 있는 llm (GLM-5.3)이 수행하게 될 거야."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: I'm drafting the plan at home; the actual work will be done by the LLM at the office (GLM-5.3).
- 왜 이렇게: "작성되고 있고"는 한국어에서도 피동이 굳이 필요 없는 자리다. 영어도 `I'm drafting` 능동이 낫다. 뒷절은 수행 주체(LLM)가 새 정보라 문장 끝에 두려고 수동 `will be done by` 를 쓴다. 능동과 수동을 정보 순서에 맞춰 고른 셈이다. "실제 수행은 … 수행하게"처럼 같은 말이 겹치는 것은 `the actual work` 한 번으로 줄인다. `at home`, `at the office` 는 전치사 `at`.

### 카드 10 — 전부 다운받기엔 시간이 너무 늘어날 테고   (내가 쓴 한글)
- 내가 쓴 한글: "장비에 수많은 데이터 형태(txt, csv, sh, 고유 확장자)가 있을텐데 그런 것들을 전부 다운 받아서 진행하기엔 수행 시간이 너무 늘어날 테고, walk를 통해 각 폴더의 유사한 파일 이름의 경우 샘플링을 통해 몇개만 다운받아 데이터 format, column 정보, data type, value and its range 등등, keyword 등을 추출하는게 중요한 것 같아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: The tools will hold all kinds of files (txt, csv, sh, vendor-specific extensions), and downloading every one of them would take far too long. I think the key is to walk the directory tree, sample just a few files from each group of similarly named ones, and extract the format, columns, data types, value ranges, and keywords from those.
- 왜 이렇게: 문장을 둘로 나눈다. 앞은 문제, 뒤는 해법이다. "전부 다운받아서 진행하기엔 수행 시간이 너무 늘어날 테고"는 동명사 주어 `downloading every one of them would take far too long` 로 받는다. 안 할 일이라 `would` 다. "walk를 통해", "샘플링을 통해"의 "~를 통해"는 영어에서 `through` 로 옮기지 않고 동사로 바꾼다(`walk`, `sample`). "고유 확장자"는 `vendor-specific` 또는 `proprietary`. `value and its range` 는 `value ranges` 로 합친다. "~하는 게 중요한 것 같아"는 `I think the key is to …`.

### 카드 11 — 일부만 읽는 것도 허용할 수 있어   (내가 쓴 한글)
- 내가 쓴 한글: "파일의 일부만 읽는 것도 가능하면 허용할 수 있어. 큰 파일을 전부 다 읽는 건 의미가 없을 것 같아."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Partial reads are fine if they're possible. There's no point reading a large file in full.
- 왜 이렇게: "허용할 수 있어"는 `I can allow` 보다 `X is fine` 이 승인하는 말투다. "파일의 일부만 읽는 것"은 명사로 `partial reads`. "의미가 없다"는 `it is meaningless` 가 아니다. 그건 뜻이 없다는 말이고, 해 봐야 소용없다는 뜻은 `there's no point (in) -ing` 다. "전부 다"는 `in full` 또는 `end to end`.

### 카드 12 — 파일 수는 몇만 단위   (내가 쓴 한글)
- 내가 쓴 한글: "대상 장비의 대략적인 파일 수는 몇만 단위가 될 수 있어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: A target tool could have tens of thousands of files.
- 왜 이렇게: "몇만 단위"는 `tens of thousands of`. 몇천은 `thousands of`, 몇십만은 `hundreds of thousands of` 다. `several ten thousands` 는 영어에 없는 표현이다. "대략적인"은 `tens of` 에 이미 들어 있어 `roughly` 를 덧붙이지 않는다. 자릿수로 말하려면 `The file count is on the order of 10^4.` "될 수 있어"의 `could` 는 확정이 아니라 가능한 규모라는 뜻이다.

### 카드 13 — 세 종류의 파일   (내가 쓴 한글)
- 내가 쓴 한글: "장비 H/W 설정 및 운영에 사용되는 파일들과 장비가 WAFER 측정 후 내뱉는 파일들, 그리고 장비가 condition을 파악하기 위해 몇 시간/몇 일 주기로 업데이트 되는 파일들."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: There are three kinds: files used to configure and operate the hardware, files the tool writes out after measuring a wafer, and files it refreshes every few hours or days to track its own condition.
- 왜 이렇게: 나열이 길면 `There are three kinds:` 로 개수를 먼저 세워 준다. "내뱉는"은 `spit out` 이 그대로 대응하는 구어이고 문서에는 `write out`, `emit`, `produce`. "몇 시간/몇 일 주기로"는 `every few hours or days`. `in a cycle of several hours` 는 번역투다. 세 항목을 `files used to …`, `files the tool writes …`, `files it refreshes …` 로 같은 명사에서 출발시켜 평행을 맞춘다.

### 카드 14 — xlsx 와 pdf 는 빼자   (내가 쓴 한글)
- 내가 쓴 한글: "xlsx와 pdf는 빼자"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Let's leave out xlsx and pdf.
- 왜 이렇게: "빼다"는 대상에서 제외한다는 뜻이면 `leave out`, `drop`, `exclude`. `remove` 는 이미 들어 있는 것을 지우는 느낌이고 `subtract` 는 산수다. 가장 짧게는 `Drop xlsx and pdf.` 문서에는 `xlsx and pdf are out of scope.`

### 카드 15 — 날짜 차이로 유추할 수 있어   (내가 쓴 한글)
- 내가 쓴 한글: "목록 며칠 간격으로 두 번 뽑는 것보다는 파일들간에 date difference로 유추할 수 있어. 몇달씩 차이가 있는 경우 (혹은 최근에 생선된 파일의 경우) 업데이트가 주기적으로 되거나 새로 생성된 거니까.."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Rather than pulling the listing twice a few days apart, we can infer it from the gaps between file dates. If one file is months newer than the rest, or was created recently, it's either updated periodically or newly created.
- 왜 이렇게: "~보다는"으로 대안을 내놓을 때는 `Rather than -ing, we can …` 으로 문장을 연다. "며칠 간격으로 두 번"은 `twice a few days apart`. `apart` 가 간격을 맡는다. "date difference 로 유추"는 `infer A from B` 틀에 넣고, 차이는 `difference` 보다 `gap` 이 시간 간격에 잘 맞는다. "몇 달씩 차이가 있는"은 `months newer than the rest` 처럼 기간 명사를 비교급 앞에 놓는다. "~거나 ~거니까"는 `either A or B`.

### 카드 16 — 얻을 수 있는 것을 brainstorming 하자   (내가 쓴 한글)
- 내가 쓴 한글: "이 agent를 통해서 우리가 얻을 수 있는 것들이 무엇이 있는 지 brainstorming 하자."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Let's brainstorm what we could get out of this agent.
- 왜 이렇게: `brainstorm` 은 타동사라 `brainstorm about` 없이 바로 목적어나 `what` 절을 받는다. "~를 통해서 얻을 수 있는 것"은 `what we can obtain through this agent` 보다 `what we could get out of it` 이 구어답다. `get A out of B` 는 "B 에서 A 를 뽑아내다"이다. 아직 가능성을 펼치는 단계라 `can` 보다 `could` 가 어울린다.

### 카드 17 — 7은 필요 없음, 12·13은 한 묶음   (내가 쓴 한글)
- 내가 쓴 한글: "7은 필요 없음. 대부분 측정 데이터가 많은 부분 차지. 12, 13은 한 묶음으로 볼 수 있음."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We don't need 7; measurement data takes up most of the space anyway. 12 and 13 can be treated as one item.
- 왜 이렇게: 목록 번호로 답할 때는 `Drop 7`, `We don't need 7` 처럼 번호를 그대로 명사로 쓴다. "많은 부분 차지"는 `take up most of the space`. `occupy` 는 문어다. `anyway` 를 붙이면 "어차피 뻔하니까"라는 이유가 실린다. "한 묶음으로 보다"는 `treat as one`, `lump together`(구어), `merge`(문서를 고치라는 지시일 때).

### 카드 18 — 참고 자료로 쓰거나 벤더에게 확인 요청   (내가 쓴 한글)
- 내가 쓴 한글: "동일 모델간에도 장비마다 세팅 값이 다른 경우, 참고 자료로 사용하거나 벤더에게 확인 요청 가능하니까. 너의 정리가 타당성이 있어."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: When settings differ between tools of the same model, we can use that as a reference or take it to the vendor to confirm. Your breakdown makes sense.
- 왜 이렇게: "벤더에게 확인 요청"은 `request confirmation to the vendor` 가 아니다. `request` 뒤 사람은 `from` 이고, 더 자연스럽게는 `ask the vendor to confirm` 이나 `take it to the vendor`. "타당성이 있어"를 `has validity` 로 옮기면 논문 같다. `makes sense` 또는 `holds up`. "너의 정리"는 `your summary` 도 되지만 항목별로 나눈 것이라 `your breakdown` 이 정확하다.

### 카드 19 — 담당 엔지니어도 다 알지는 못한다   (내가 쓴 한글)
- 내가 쓴 한글: "일단 특정 장비를 담당하는 엔지니어라 해도 그 장비에 있는 파일, 데이터들의 의미를 전부 추적하지 못하고 모르는 내용도 많음."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Even the engineer who owns a tool can't keep track of what every file and value on it means, and there's a lot they simply don't know.
- 왜 이렇게: "~라 해도"는 `Even` 을 주어 앞에 놓는다. "담당하는"은 `in charge of` 도 맞지만 현장에서는 `owns` 가 흔하다(`tool owner`). "전부 추적하지 못하고"는 `can't keep track of` 가 "계속 따라잡지 못한다"는 뜻에 맞다. `trace` 는 한 번 따라가 보는 것이라 다르다. 성별을 모르는 엔지니어는 `they` 로 받는다. `simply` 는 "그냥 모른다"의 "그냥"이다.

### 카드 20 — 복합적인 요소를 다 추적해 차이를 발굴   (내가 쓴 한글)
- 내가 쓴 한글: "장비의 유지 보수와 장비간의 SKEW를 판단하는데 복합적인 요소를 고려해야 하는데 그런 요소들을 궁극적으로는 다 추적을 하고 차이점을 발굴해내는게 중요함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Judging maintenance needs and tool-to-tool skew means weighing many interacting factors. What matters in the end is tracking all of them and surfacing the differences.
- 왜 이렇게: "~하는데 ~하는데"로 이어진 문장은 둘로 끊는다. "복합적인 요소를 고려"는 `consider complex factors` 보다 `weigh many interacting factors` 가 뜻에 가깝다. 요소가 어려운 게 아니라 서로 얽혀 있다는 말이기 때문이다. "장비 간"은 `tool-to-tool`. "발굴해내다"는 `dig up` 도 되지만 숨은 것을 드러낸다는 뜻의 타동사 `surface` 가 기술 글에 잘 맞는다. "~하는 게 중요함"은 `What matters is …` 로 앞에 세운다.

### 카드 21 — 노드가 줄수록 장비 간 차이도 줄어야   (내가 쓴 한글)
- 내가 쓴 한글: "반도체 노드는 갈수록 줄어들기 때문에 장비간 차이도 줄어들어야 함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: As nodes keep shrinking, tool-to-tool variation has to shrink with them.
- 왜 이렇게: "갈수록 ~하기 때문에"는 `because` 보다 `As …` 가 낫다. 원인과 동시 진행을 함께 담는다. 노드가 작아지는 것은 `shrink` 가 업계 표준 동사다(`node shrink`). `decrease` 는 수치에 쓰는 말이라 어색하다. "~도"는 `also` 대신 `with them` 으로 받으면 "같이 따라 줄어야 한다"는 뜻이 선다. 격식을 올리면 `The tolerance for tool-to-tool variation tightens as nodes shrink.`

### 카드 22 — 장비 장악력으로 지식을 자산화   (내가 쓴 한글)
- 내가 쓴 한글: "장비 장악력 (얼마나 깊게 파고 들 수 있는 지)을 가지고 지식 자산화를 해야 하고, agent가 산업 현장에서 일할 수 있는 구조를 갖춰야 함."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We need real command of our tools, meaning how deep we can dig into them, and we need to turn that into a knowledge asset. We also need the groundwork that lets agents do real work on the fab floor.
- 왜 이렇게: "장악력"은 `control`(조종)보다 `command of`(깊이 알고 부릴 줄 앎) 또는 `mastery of` 가 맞다. `have a good command of English` 와 같은 쓰임이다. 괄호 속 풀이는 `meaning …` 으로 잇는다. "지식 자산화"는 `knowledge assetization` 같은 조어 대신 동사로 풀어 `turn it into a knowledge asset` 또는 `capture it as institutional knowledge`. "산업 현장"은 반도체라면 `on the fab floor`, 일반적으로는 `on the shop floor`. "구조를 갖추다"는 `groundwork`, `foundation` 이 `structure` 보다 뜻에 가깝다.

### 카드 23 — 후보를 확인하고 조치할 수 있게   (내가 쓴 한글)
- 내가 쓴 한글: "맞아. 엔지니어가 후보를 확인하고 조치할 수 있게 도움을 줘야지."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Right. It should help engineers review the candidates and act on them.
- 왜 이렇게: "~할 수 있게 도움을 줘야지"는 `help + 사람 + 동사원형` 으로 짧게 받는다. `give help so that engineers can …` 은 길다. "조치하다"는 `take action` 도 되지만 대상이 있을 때는 `act on them` 이 한 단어 적다. "~해야지"의 가벼운 당위는 `should` 다. `must` 는 세다.

### 카드 24 — MDC 값이 장비마다 달랐고 한 대는 outlier   (내가 쓴 한글)
- 내가 쓴 한글: "과거에는 몰랐지만 CD-SEM을 측정하는데 CD 값을 미세 튜닝하는 MDC (meas. data correction)이라는 조정 수치값이 있었는데, 장비마다 전부 다 달랐고, 특정 장비는 outlier에 속해 있었고, 이 장비는 다른 장비와 skew가 항상 있어왔음. 최근에 이런 것들을 발견해서 MDC 재조정 작업 중."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We didn't know this before, but CD-SEMs have a correction value called MDC (measurement data correction) that fine-tunes the CD reading. It turned out to be different on every tool, and one tool was an outlier, the same tool that has always shown skew against the others. We found this recently and are now recalibrating MDC.
- 왜 이렇게: 이야기 순서대로 세 문장으로 나눈다. "CD-SEM 을 측정하는데"는 CD-SEM 이 측정하는 쪽이라 `CD-SEMs have …` 로 주어를 바로잡는다. "outlier 에 속해 있었고"는 `belonged to outliers` 가 아니라 `was an outlier`. "항상 있어 왔음"은 지금까지 이어지는 일이라 현재완료 `has always shown` 이다. `the same tool that …` 으로 두 사실을 한 장비에 묶으면 요점이 선다. "알고 보니 ~였다"는 `It turned out …`. "재조정 작업 중"은 `are now recalibrating`. `re-adjust` 도 통하지만 교정값에는 `recalibrate` 가 맞는 말이다.

### 카드 25 — 우연히 찾았고, 비교해 보기 전에는 알 수 없었지   (내가 쓴 한글)
- 내가 쓴 한글: "우연히 찾았고, 전체 장비의 수치를 비교해보다가 발견하게 되었어. 비교해보기 전에는 알 수 없었지."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We found it by accident, while comparing the values across all the tools. There was no way to know until we compared them.
- 왜 이렇게: "우연히"는 `by accident` 나 `by chance`. 더 구어로는 `We stumbled on it`. "~하다가"는 `while -ing` 로 받는다. "전체 장비의 수치"는 `across all the tools` 다. `across` 가 "나란히 놓고"를 맡는다. "~하기 전에는 알 수 없었지"는 `We couldn't know before comparing` 보다 `There was no way to know until …` 이 "방법이 없었다"는 뜻을 살린다. `until` 은 그 시점에야 바뀌었다는 말이다.

### 카드 26 — 관리 대상 파라미터를 추출하고 전 모델로 확장   (내가 쓴 한글)
- 내가 쓴 한글: "전부 확인하고, 우리가 관리 대상으로 삼아야 하는 파라미터들을 추출해야지. 지금은 한 모델로 시작하지만 최종적으로는 모든 모델과 장비로 확장하고 싶어. 그런 AGENT가 되도록 설계해야해. 물론 주기적으로 같은 장비도 체크하면서 달라진 점이 있으면 업데이트도 하고 해야해."   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: We should check everything and pull out the parameters we ought to be managing. We're starting with one model, but I eventually want to cover every model and every tool, so the agent has to be designed for that from the start. It should also recheck the same tools periodically and update the map whenever something has changed.
- 왜 이렇게: "관리 대상으로 삼아야 하는 파라미터"는 `parameters that should be management targets` 가 아니라 `the parameters we ought to be managing` 으로 관계절에 넣는다. 진행형이 "지금 하고 있어야 하는데 안 하는"이라는 뜻을 싣는다. "최종적으로는"은 `eventually`. `finally` 는 "드디어"여서 다르다. "그런 Agent 가 되도록 설계"는 `designed for that from the start` 로 받고, "확장"은 `extend to` 도 되고 `cover` 가 더 구어다. "달라진 점이 있으면"은 `whenever something has changed`. 점검 시점보다 앞서 바뀐 것이라 현재완료다.

### 카드 27 — 기록으로 남겨줘 / 다 같이 올려줘   (내가 쓴 한글)
- 내가 쓴 한글: "굳. 기록으로 남겨줘" / "codex (via herdr)에게 의견을 물어보고 보충/수정해야 할 부분 있으면 진행해줘" / "다 같이 올려줘~"   (출처: transcript:[user] pm-notes)
- 자연스러운 영어: Good. Put that on record. / Get Codex's take (via herdr) and make whatever additions or fixes it calls for. / Push all of it together.
- 왜 이렇게: "기록으로 남기다"는 `put it on record`, `write it down`, 문서 이름이 있으면 `log it in the decision log`. "의견을 물어보다"는 `ask for an opinion` 보다 `get someone's take` 가 동료 사이 말투다. "~할 부분 있으면 진행해줘"는 `if there are parts to supplement, proceed` 식 직역 대신 `make whatever changes it calls for` 로 줄인다. `whatever` 가 "있으면 있는 대로"를 맡는다. "올리다"는 git 맥락에서 `push` 이고 "다 같이"는 `all of it together` 또는 `the rest too`.

### 카드 28 — 볼 수 있게 하는 것까지   (고급 한글 · 번역)
- 한글 원문: "지도가 하는 일은 볼 수 있게 하는 것까지이고, 실제로 차이가 줄려면 엔지니어가 후보를 확인하고 조치해야 합니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: The map only gets you as far as visibility; for the differences to actually shrink, an engineer still has to review the candidates and act on them.
- 번역 포인트: "~까지이고"라는 한계 표시는 `only gets you as far as …` 로 옮긴다. `as far as` 가 "거기까지만"을 맡는다. "볼 수 있게 하는 것"은 절로 풀지 않고 명사 `visibility` 하나로 줄인다. "차이가 줄려면"은 `for A to B` 구문으로 조건을 세운다. `in order to reduce the differences` 로 쓰면 줄이는 주체가 엔지니어로 읽혀 원문과 달라진다. `still` 은 "그래도 여전히 사람 손이 필요하다"를 싣는다.

### 카드 29 — 어려웠던 것은 그 값을 봐야 한다는 것을 아는 일   (고급 한글 · 번역)
- 한글 원문: "원인은 장비 안에 처음부터 있었고, 찾고 나면 단순했고(값을 나란히 놓으면 한 대가 벗어남), 어려웠던 것은 "그 값을 봐야 한다"는 것을 아는 일이었습니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: The cause had been sitting in the tool all along, and once found it was simple: line the values up and one tool stands out. The hard part was knowing to look at that value in the first place.
- 번역 포인트: "처음부터 있었고"는 과거의 어느 시점까지 이어진 상태라 과거완료 진행 `had been sitting … all along` 이 맞다. `sit` 은 아무도 안 건드린 채 놓여 있었다는 느낌을 준다. 괄호 속 설명은 콜론 뒤로 꺼내고 `명령문 + and` 로 "~하면 ~한다"를 만든다. "어려웠던 것은 ~하는 일이었다"는 `The hard part was -ing`. "봐야 한다는 것을 아는"은 `knowing that we should look` 보다 `knowing to look` 이 짧고, `in the first place` 가 "애초에"를 더한다.

### 카드 30 — 우연을 절차로 바꾼다   (고급 한글 · 번역)
- 한글 원문: "우연을 절차로 바꾼다. 사람이 값 하나를 골라 비교한 일을, Agent가 장비 안의 모든 값에 대해 한다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: Turn luck into procedure. What one person did for a single value they happened to pick, the agent does for every value on the tool.
- 번역 포인트: 구호는 명령형으로 짧게 간다. "우연"은 `coincidence`(우연의 일치)보다 `luck` 이나 `chance` 가 "운 좋게 찾았다"에 맞는다. 둘째 문장은 한국어처럼 목적어를 앞에 세운 어순을 영어에서도 살릴 만하다. `What one person did for X, the agent does for Y` 로 목적절을 문두에 두면 사람과 Agent, 하나와 전부의 대구가 드러난다. `happened to pick` 이 "우연히 고른"을 받아 첫 문장의 `luck` 과 이어진다. "모든 값에 대해"는 `about` 이 아니라 `for` 다.

### 카드 31 — "더 찾아내겠다"가 아니라 "전부 확인하겠다"   (고급 한글 · 번역)
- 한글 원문: "임원에게 약속할 때는 "더 찾아내겠다"가 아니라 "전부 확인하겠다"로 말하는 편이 안전합니다."   (출처: transcript:[assistant] pm-notes)
- 자연스러운 영어: When you make the promise to executives, it's safer to say "we will check everything" than "we will find more."
- 번역 포인트: "~가 아니라 ~로 말하는 편이 안전하다"는 `it's safer to say A than B` 로 비교급에 넣는다. 영어는 권하는 쪽을 먼저 말하므로 한국어와 순서가 뒤집힌다. `not A but B` 로 옮겨도 뜻은 통하지만 "편이 낫다"는 정도의 뉘앙스가 빠진다. 약속의 내용은 결과(`find more`)가 아니라 범위(`check everything`)라는 대비가 요점이라 두 인용을 같은 `we will + 동사` 꼴로 맞췄다. 한 줄 조언으로는 `Promise coverage, not discoveries.`

## 영어 다듬기

### 카드 32 — individualized service for engineers
- 내가 쓴 영어: "I want to give individualized (Customized) service for engineers based on what they are interested in."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `give … service for engineers` → `give engineers … service` 또는 `offer … to engineers`. `give` 는 받는 사람을 `for` 로 받지 않는다. `service` 는 이 뜻에서 셀 수 있는 명사로 쓰는 편이 자연스러워 `a … service` 로 관사를 붙인다.
- 더 나은 표현: I'd like to give each engineer a personalized view based on what they care about.
- 왜: 제품 용어로는 `individualized`·`customized` 보다 `personalized` 가 표준이다. `customized` 는 사용자가 직접 고친 것, `personalized` 는 사용자에 맞춰 보여 주는 것이라는 구분도 있다. `service` 보다 `view` 나 `page` 가 실제로 만들 것에 가깝다. `what they are interested in` 은 맞는 문장이고 `what they care about` 이 조금 더 구어다.

### 카드 33 — he can see the issue right away
- 내가 쓴 영어: "For example, if an MI engineer is in charge of some group of tools in a couple of fabs, he can see the issue right away when he visit skewnono."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `when he visit` → `when he visits`(3인칭 단수 현재에는 `-s`). `some group of tools` → `a group of tools`(단수 가산명사 앞 `some` 은 "어떤 정체 모를"이라는 뜻이 된다). `the issue` → `any issues`(아직 특정되지 않은 문제라 정관사가 맞지 않는다). `he can see` → `they should see`(바라는 동작이라 `can` 보다 `should`).
- 더 나은 표현: For example, an MI engineer who owns a group of tools across a couple of fabs should see any issues on those tools the moment they open SKEWNONO.
- 왜: `if` 절을 관계절 `who owns …` 로 바꾸면 문장이 한 겹 얇아진다. 여러 팹에 걸쳐 있다는 뜻은 `in` 보다 `across` 다. `right away` 는 좋은 구어이고 `the moment they open` 은 "열자마자"를 접속사로 붙인다. 성별을 모르는 엔지니어는 `they` 로 받는다.

### 카드 34 — Another example is like if …
- 내가 쓴 영어: "Another example is like if a process engineer is interested in a some steps of CD measurements so he want to see the results of summary from some recipe's measurements."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `a some steps` → `some steps`(`a` 와 `some` 은 같이 못 쓴다). `he want` → `he wants`. `the results of summary` → `a summary of the results`(요약의 결과가 아니라 결과의 요약). `is like if … so …` 는 주절이 없는 문장이다. `Another example:` 로 끊고 완전한 절을 세운다.
- 더 나은 표현: Another example: a process engineer who follows certain CD measurement steps wants a summary of the results for the recipes that measure them.
- 왜: 말할 때의 `it's like if …` 는 글에서 콜론 하나로 바뀐다. `interested in` 은 맞지만 계속 지켜본다는 뜻이면 `follows` 나 `tracks` 가 더 정확하다. `some recipe's measurements` 는 어느 레시피인지 흐릿해서 `the recipes that measure them` 으로 앞의 step 과 이었다.

### 카드 35 — Can we make that service?
- 내가 쓴 영어: "Can we make that service?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 더 나은 표현: Could we build something like that?
- 왜: 문법은 맞다. 소프트웨어는 `make` 보다 `build` 를 쓴다. 가능한지 타진하는 물음이라 `Could we` 가 `Can we` 보다 부드럽고, `something like that` 이 `that service` 보다 아직 형태가 열려 있다는 뜻을 준다. 실현 가능성을 정면으로 물으려면 `Is that feasible with what we have?`

### 카드 36 — accessed via top nav
- 내가 쓴 영어: "I think we can make a separate page that can be accessed via top nav."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `via top nav` → `via the top nav`(화면에 하나뿐인 특정 요소라 정관사가 필요하다).
- 더 나은 표현: I think it could be a separate page, reachable from the top nav.
- 왜: `that can be accessed via` 는 맞지만 수동 관계절이 무겁다. 형용사 `reachable from` 하나로 줄어든다. 어시스턴트도 같은 내용을 `a separate page reachable from the top nav` 로 받아 적었다. `we can make` 를 `it could be` 로 바꾸면 만들 수 있느냐가 아니라 어떤 꼴이면 좋겠느냐로 초점이 옮겨 간다.

### 카드 37 — a good start position
- 내가 쓴 영어: "localStorage is a good start position."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `start position` → `starting point`. `start position` 은 경주나 게임의 출발 위치를 가리키고, 일의 첫 단계라는 뜻으로는 `starting point` 가 굳은 말이다.
- 더 나은 표현: localStorage is a good place to start.
- 왜: `a good place to start` 가 가장 흔한 구어다. 나중에 바꿀 여지를 밝히려면 `localStorage is fine for a first version.` 어시스턴트의 `I'd start with localStorage and move only if someone asks` 와 같은 취지다.

### 카드 38 — self-selected tools by engineers. let's go grilling
- 내가 쓴 영어: "self-selected tools by engineers. let's go grilling"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `self-selected tools by engineers` 는 `self-` 와 `by engineers` 가 같은 말을 두 번 한다. 하나만 남긴다. `let's go grilling` 은 `go fishing` 처럼 여가 활동에 쓰는 `go + -ing` 꼴이어서 "바비큐 하러 가자"로 읽힌다.
- 더 나은 표현: Engineers pick their own tools. Let's move on to the grilling.
- 왜: 결정 사항은 명사구보다 주어와 동사가 있는 문장이 분명하다. `pick their own` 이 `self-selected` 를 일상어로 푼다. 스킬 이름을 가리킬 때는 `Let's run the grilling skill.` 이나 `Go ahead and grill me.` 라고 하면 오해가 없다.

### 카드 39 — readme.md commit and push too
- 내가 쓴 영어: "readme.md commit and push too"   (출처: transcript:[user] pm-notes)
- 정정: 어순이 한국어식(목적어 + 동사)이다. 영어 명령문은 동사가 먼저 온다: `Commit and push readme.md too.`
- 더 나은 표현: Commit and push the README as well.
- 왜: 메모체로도 뜻은 통하지만 동사를 앞에 두는 것만으로 문장이 된다. `too` 와 `as well` 은 같은 뜻이고 `as well` 이 조금 더 단정하다. 앞서 올린 것에 덧붙인다는 뜻을 살리려면 `Include the README in the push too.`
