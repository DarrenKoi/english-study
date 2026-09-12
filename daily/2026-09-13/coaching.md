# 2026-09-13 — 코칭

## 한글→영어

### 카드 1 — 문서를 하나씩 돌릴까, 하네스를 키울까   (내가 쓴 한글)
- 내가 쓴 한글: "@equipment-data-parser/ 에 있는 md file을 하나씩 다 수행하라고 하는 것보다는 office에서 llm을 연결하고 한단계씩 진행하면서 harness를 다지고 agent로 만드는 방법이 나을까?"   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Rather than having you work through the markdown files in `equipment-data-parser/` one by one, would it be better to wire up the LLM at the office, go one step at a time, harden the harness, and grow it into an agent?
- 왜 이렇게: 한국어의 "~보다는 ~이 나을까?" 는 비교 대상을 앞에 통째로 얹는데, 영어는 `Rather than X, would it be better to Y?` 로 같은 구조를 그대로 쓴다. "하나씩 다 수행하다" 를 `execute all of them` 으로 옮기면 기계가 도는 느낌이라, 사람이 순서대로 훑는 `work through … one by one` 이 낫다. "다지다" 는 `harden`(무르지 않게 굳히다) 이 이 맥락의 정착 표현이고, "agent 로 만들다" 는 `turn it into` 보다 `grow it into` 가 단계적 성장을 함의해 질문 취지와 맞는다.

### 카드 2 — 실습용 커리큘럼 요청   (내가 쓴 한글)
- 내가 쓴 한글: "어떤식으로 agent = coding + harness를 만들어서 보편적으로 이 equipment-data-map이 활용될 수 있게 진행하면 좋을 지 프로세스 플로우와 방법론을 ./agent_build_steps 폴더를 만들어서 작성해줘. 학습 용도 포함되어있고 실습하면서 agent로 만들고 싶어."   (출처: transcript:[user] equipment-data-map)
- 자연스러운 영어: Create an `./agent_build_steps/` folder and write up the process flow and methodology for building the agent — coding plus harness — so that `equipment-data-map` ends up generally reusable. It doubles as a learning exercise: I want to build the agent hands-on as I follow the steps.
- 왜 이렇게: 원문은 한 문장에 요청·목적·동기가 다 들어 있어 영어로는 두 문장으로 끊는 편이 읽힌다. "보편적으로 활용될 수 있게" 는 `can be universally used` 보다 `ends up generally reusable` 이 자연스럽다 — `universal` 은 영어에서 "예외 없이 전부"라는 강한 뜻이라 과하게 들린다. "학습 용도 포함되어 있고" 는 `it doubles as …`(한 가지가 두 역할을 겸한다)가 딱 맞는 관용구. "실습하면서" 는 부사 `hands-on` 으로 처리한다.

### 카드 3 — 프록시 경유 knob 조절 가능 여부   (내가 쓴 한글)
- 내가 쓴 한글: "vlm을 사용할 때 flask proxy를 이용해도 여전히 effort / variant / thinking 정도를 조절할 수 있나? 가능하도록 코드 변경 필요해. 각 model에 따라 설정 방법이 약간씩 다를거라.. web search 필요함."   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: When I go through the Flask proxy for VLM calls, can I still control effort, variant and thinking depth? Change the code so that I can. The knobs probably differ a little from model to model, so this needs a web search.
- 왜 이렇게: "~를 이용해도 여전히" 의 핵심은 `still` 이고, 위치는 조동사 뒤(`can I still control`)다. "조절하다" 는 대상이 설정값이면 `control`/`tune` 이고 `adjust` 는 이미 있는 값을 미세하게 옮길 때 쓴다. "가능하도록 코드 변경 필요해" 처럼 주어 없는 한국어 지시문은 영어에서 명령문 `Change the code so that I can.` 으로 옮기는 게 가장 짧다. 마지막 `so this needs a web search` 는 원문의 "..필요함" 이 가진 메모 같은 간결함을 살린 것.

### 카드 4 — 사용 예제 요청   (내가 쓴 한글)
- 내가 쓴 한글: "사용법 example을 같이 만들어서 제공해줘."   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: Add a runnable usage example alongside it.
- 왜 이렇게: "같이 만들어서 제공해줘" 를 `make and provide it together` 로 직역하면 동사가 둘 다 떠 버린다. 영어는 `add` 하나로 "만들어 붙인다"를 처리하고, "같이" 는 전치사 `alongside it` 이 맡는다. `runnable` 한 단어가 "돌려 볼 수 있는 예제"라는 기대치를 미리 못 박아 준다.

### 카드 5 — 논스트림이 느려 보이는 문제   (내가 쓴 한글)
- 내가 쓴 한글: "flask proxy를 통할 때 stream이 아닌 결과 전체를 전달받기 때문에 속도가 느리게 느껴질 수 있고, harness에서 timeout으로 오해할 수 도 있는데 이를 해결할 수 있는 방안은?"   (출처: transcript:[user] llm-serving)
- 자연스러운 영어: Going through the Flask proxy, the response comes back as one whole body rather than a stream, so it can feel slow and a harness may read it as a timeout. What are our options for fixing that?
- 왜 이렇게: "느리게 느껴질 수 있고" 의 주어는 사람이 아니라 경험이므로 `it can feel slow` 가 맞다(`we can feel slow` 는 비문에 가깝다). "오해하다" 는 `misunderstand` 보다 `read X as Y`(X 를 Y 로 읽다)가 기계 주어에 자연스럽다. "방안은?" 은 `What is the solution?` 보다 `What are our options?` 가 낫다 — 답이 여럿일 것을 이미 전제해, 실제로 돌아온 다섯 가지 답과 어긋나지 않는다.

### 카드 6 — 예측해서 쓴 글의 수명   (고급 한글 · 번역)
- 한글 원문: "letter가 예측해서 쓴 내용은 office에 닿는 순간 절반이 틀립니다 — 그래서 problems/ 폴더를 만들어 둔 거고요."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: Half of what those letters predict will be wrong the moment they meet the office — which is exactly why the `problems/` folder is there.
- 번역 포인트: "~하는 순간" 은 `the moment (that) …` 이 정확한 짝이고, 접속사처럼 절을 이끈다. "절반이 틀립니다" 를 `half is wrong` 으로 두면 무엇의 절반인지가 비므로 `Half of what those letters predict` 로 명사절을 세운다. 대시 뒤 "그래서 ~해 둔 거고요" 의 사후 설명 어조는 `which is exactly why …` 가 옮긴다 — `exactly` 가 "바로 그 때문"의 강세를 담당한다.

### 카드 7 — 하네스와 프롬프트의 경계   (고급 한글 · 번역)
- 한글 원문: "모델이 바뀌어도 참이어야 하는 것은 전부 harness 로, 나머지만 프롬프트로."   (출처: transcript:[assistant] equipment-data-map)
- 자연스러운 영어: Whatever must stay true when the model changes belongs in the harness; only the rest goes in the prompt.
- 번역 포인트: 동사 없이 조사로 끝내는 한국어 원문(`~로.`)의 압축은 영어로 그대로 못 옮긴다. 대신 `belongs in` / `goes in` 이라는 짧은 동사 둘로 대칭을 만들고 세미콜론으로 두 축을 붙인다. "~해도" 는 양보의 `even if` 보다 시간의 `when` 이 낫다 — 모델 교체는 가정이 아니라 예정된 사건이기 때문이다. "참이어야 하는 것" 은 `the things that` 보다 `whatever` 가 범위를 열어 둬 원문의 "전부"를 자연히 흡수한다.

### 카드 8 — 같은 숫자, 두 가지 의미   (고급 한글 · 번역)
- 한글 원문: "같은 숫자가 두 개의 다른 의미를 갖는 게 이 문제의 전부다."   (출처: transcript:[assistant] llm-serving)
- 자연스러운 영어: The whole problem is that one number carries two different meanings.
- 번역 포인트: "~게 이 문제의 전부다" 는 한국어에서 주어를 뒤에 두는 구조인데, 영어는 `The whole problem is that …` 으로 앞에 두는 편이 훨씬 읽힌다. "갖는다" 를 `has` 로 옮기면 밋밋하고, 의미를 실어 나른다는 뜻의 `carries` 가 이 맥락(같은 300 초가 두 가지로 해석됨)을 정확히 짚는다.

## 영어 다듬기

### 카드 9 — 엔드포인트 확장 요청
- 내가 쓴 영어: "for the endpoints page, we have to offer more api service. can we offer some endpoints service in skewvoir? like offer msr data (either download or in-memory) via raw_msr / pickle from minIO."   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `more api service` → `more API services` (`service` 는 셀 수 있는 명사라 `more` 뒤에서 복수). `some endpoints service` → `some endpoints`(명사 둘을 겹쳐 쓸 이유가 없다).
- 더 나은 표현: For the endpoints page, we should expose more of our API surface. Could we offer Skewvoir endpoints too — MSR data from MinIO as `raw_msr` or a pickle, either downloaded or loaded straight into memory?
- 왜: 같은 문단에서 `offer` 가 세 번 나와 초점이 흐려진다. 첫 번째를 `expose`(밖에서 쓸 수 있게 열어 둔다 — API 문맥의 표준 동사)로 바꾸면 반복이 풀린다. `we have to` 는 외부 강제처럼 들리니 제안에는 `we should` 가 맞고, 질문도 `can we` 보다 `could we` 가 한 단계 정중하다. `like` 로 예시를 여는 건 구어라 문서에는 대시가 낫고, `in-memory` 는 형용사라 `loaded straight into memory` 로 풀어야 `downloaded` 와 병렬이 맞는다.

### 카드 10 — ECharts 로 교체 요청
- 내가 쓴 영어: "replace with echarts library so that we keep the unified UI/UX"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `replace with echarts library` → `replace it with the ECharts library` (타동사 `replace` 에는 목적어가 필요하고, 특정 라이브러리이므로 정관사 `the`).
- 더 나은 표현: Rebuild it on ECharts so the page keeps a consistent look and feel with the other charts.
- 왜: `replace A with B` 는 버리고 갈아 끼우는 그림인데, 실제로 원한 건 같은 기능을 다른 토대 위에 다시 세우는 것이라 `rebuild it on B` 가 의도에 가깝다. `so that` 은 구어에서 `so` 로 줄여도 된다. `unified UI/UX` 는 사내 약어 느낌이라, 영어 사용자에게 통하는 `a consistent look and feel` 로 바꾸고 비교 대상(`with the other charts`)을 명시하면 요구가 검증 가능해진다.

### 카드 11 — 목 데이터 채우기 요청
- 내가 쓴 영어: "for the activity page, can we fill up the mock data to display the calander heatmap?"   (출처: transcript:[user] skewnono-v3-nuxt)
- 정정: `calander` → `calendar` (철자). `fill up` → `fill in`. `fill up` 은 그릇을 가득 채우는 것이고, 비어 있는 칸을 메우는 건 `fill in` 이다.
- 더 나은 표현: On the activity page, could we seed enough mock data for the calendar heatmap to actually render?
- 왜: 목 데이터를 만드는 행위의 전문 동사는 `seed` 다 — 코드베이스의 `seed_demo_users` 와도 어휘가 맞는다. `to display` 는 주어가 불분명한데(누가 표시하나), `for the calendar heatmap to render` 로 의미상 주어를 붙이면 명확해진다. `actually` 한 단어가 "지금은 비어 있다"는 배경을 짧게 전달한다.
