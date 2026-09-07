# 2026-09-08 — 코칭

## 한글→영어

### 카드 1 — 서비스가 바뀌었을 때 확인 목록 요청   (내가 쓴 한글)
- 내가 쓴 한글: "VLM service 변경이 좀 있었는데 우리가 확인해야 할 일은? for poc/workflow_3 to run"   (출처: transcript:auto_recipe_creator ff8357d4)
- 자연스러운 영어: The VLM services changed a fair bit. What do we need to check before `poc/workflow_3` can run?
- 왜 이렇게: "좀 있었는데"의 "좀"은 양이 적다는 뜻이 아니라 "꽤"에 가까우니 `a little` 이 아니라
  `a fair bit` 이 맞는다. 그리고 한국어는 배경과 질문을 `-는데` 로 한 문장에 붙이지만 영어는 끊는
  편이 읽기 쉽다. 끝의 목적구는 질문 안으로 넣어 `before … can run` 으로 붙여야 무엇을 위한
  점검인지가 분명해진다.

### 카드 2 — 결과를 문서로 남겨 달라   (내가 쓴 한글)
- 내가 쓴 한글: "오피스 체크리스트로 runbook 에 정리해줘"   (출처: transcript:auto_recipe_creator ff8357d4)
- 자연스러운 영어: Write this up as an office checklist in the runbooks.
- 왜 이렇게: "정리해줘"를 `organize` 로 옮기면 이미 있는 것을 재배열한다는 뜻이 되어 어긋난다.
  대화 내용을 문서 형태로 새로 쓰는 것은 `write up` 이다. 조사 "로"는 결과물의 형태를 가리키므로
  `as` — `into a checklist` 라고 하면 변환 과정 쪽에 무게가 실린다.

### 카드 3 — 구성상의 이점을 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "2개 GPU로 LLM 모델을 서빙하면 1개로 하는 것보다 어떤 장점이 있지?"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: What do we actually gain by serving the model on two GPUs instead of one?
- 왜 이렇게: `What are the advantages of A over B?` 도 맞지만 교과서 문장에 가깝다. `What do we
  gain by -ing` 은 같은 질문을 "우리 상황에서 실제로 얻는 게 뭐냐"로 좁혀서, 원론적 장단점 나열
  대신 판단을 요구하는 신호가 된다. `actually` 한 단어가 그 압박을 만든다.

### 카드 4 — 둘 중 어느 쪽이 담당하는지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "동일 모델을 두개에 각각 운영하게 되면 로드밸런싱을 flask로 할 수 있는건가? 아니면 uwsgi가 알아서 담당하는건가?"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: If I run the same model on both GPUs, do I have to do the load balancing in Flask, or does uwsgi handle it for me?
- 왜 이렇게: "알아서 담당한다"는 `handle it for me` 나 `take care of it` 이지 `handle it by
  itself` 가 아니다 — 후자는 "혼자 힘으로"라는 뜻이라 어색하다. 양자택일 질문은 `do I have to …,
  or does … ?` 처럼 두 절을 `or` 로 잇는 게 자연스럽고, 앞에 `If` 절로 전제를 깔아 두면 조건이
  분명해진다.

### 카드 5 — 모르는 걸 인정하면서 배우겠다고 말하기   (내가 쓴 한글)
- 내가 쓴 한글: "우리 회사는 private cloud에 nginx, uwsgi, flask가 돌아가고 있어. 하지만 나는 그 개념들을 잘 몰라. flask에 코딩만 해서 운용하고 있는 정도."   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: We run nginx, uwsgi and Flask on a private cloud, but I've never really learned how those pieces fit together — I just write the Flask code and keep it running.
- 왜 이렇게: `I don't know those concepts well` 은 문법은 맞아도 자신을 낮추는 쪽으로만 읽힌다.
  `I've never really learned how those pieces fit together` 는 모르는 이유를 경력의 사실로
  돌려서, 무능이 아니라 아직 안 배운 영역이라는 틀이 된다. "코딩만 해서 운용하는 정도"의 "정도"는
  영어에서 부사 `just` 로 옮기면 충분하고, 대시 뒤에 붙여 앞 문장을 구체화한다.

### 카드 6 — 개념 셋을 한 번에 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "CGI가 무엇인가? Apache의 역할은? 이제 nginx가 대체?"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: What is CGI? What was Apache's role, and has nginx simply replaced it by now?
- 왜 이렇게: 한국어는 명사만 던지고 서술어를 생략해도 통하지만(`Apache의 역할은?`) 영어는 동사가
  있어야 한다. 시제가 두 개로 갈리는 게 이 카드의 핵심 — Apache 가 한 일은 지나간 역할이라
  `was`, 대체 여부는 지금까지 이어진 일이라 현재완료 `has … replaced` 다. `simply` 는 "그냥
  갈아치운 건가"라는 뉘앙스를 담아, 예상 답이 "그렇게 단순하지 않다"임을 열어 둔다.

### 카드 7 — 예방적 수정 지시   (내가 쓴 한글)
- 내가 쓴 한글: "버그 발생 가능성이 있는 거는 고쳐주세요"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: Fix anything that could actually bite us.
- 왜 이렇게: `things that have the possibility of causing bugs` 는 직역이라 무겁다. `could bite
  (us)` 는 "지금은 안 터졌지만 언젠가 문다"를 한 동사로 담는 관용 표현이고, `anything that` 이
  범위를 상대에게 맡긴다. 격식이 필요하면 `Fix anything with a plausible failure mode.`

### 카드 8 — 겪은 일을 배경으로 깔고 질문하기   (내가 쓴 한글)
- 내가 쓴 한글: "model을 local에서 cloud로 업로드를 한 뒤에 start_all 했을 때 안되었던 경우 pod를 재실행해서 해결했음. pod가 cloud에서 어떤 역할 / 기능인지 알려줘"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: After I uploaded a model from local to the cloud, `start_all` failed, and restarting the pod fixed it. What is a pod actually doing in a cloud setup?
- 왜 이렇게: "안 되었던 경우"를 `in the case where it didn't work` 로 옮기면 관계절이 늘어져
  읽기 어렵다. 사건을 시간 순서대로 `After …, X failed, and Y fixed it` 세 마디로 늘어놓는 편이
  훨씬 영어답다. 질문에서 `is … doing` 진행형을 쓰면 정의가 아니라 실제 하는 일을 묻는 게 되어,
  "교과서 설명 말고 내 상황에서의 역할"이라는 의도가 산다.

### 카드 9 — 특정 조치를 배제한 해법 요구   (내가 쓴 한글)
- 내가 쓴 한글: "유력한 원인들을 고려하면 pod 재시작 없이 해결할 수 있는 방법들은?"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: Given those likely causes, what could I try short of restarting the pod?
- 왜 이렇게: "~없이"를 그대로 `without restarting` 해도 되지만, `short of X` 는 "X 까지 가지
  않는 선에서"라는 뜻이라 최후 수단을 배제한다는 의도가 더 정확히 실린다. `Given …` 은 앞서
  받은 답을 전제로 삼는다는 표시라 대화를 이어 붙이는 접착제 노릇을 한다.

### 카드 10 — 시도가 실패했음을 보고하기   (내가 쓴 한글)
- 내가 쓴 한글: "1-1은 불가능 (한시간 이상 기다렸으나 안됨)"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: 1-1 is a dead end — I waited over an hour and it never came back.
- 왜 이렇게: `impossible` 은 원리상 불가능을 뜻해서 과하다. 시도했는데 통하지 않은 길은
  `a dead end` 다. 괄호 안의 근거는 영어에선 대시 뒤 완전한 절로 붙이는 게 자연스럽고,
  `it never came back` 이 `it didn't work` 보다 "기다렸는데 끝내 응답이 없었다"는 상황을
  정확히 그린다. 음성 결과를 이렇게 적어 두면 다음 사람이 같은 한 시간을 안 쓴다.

### 카드 11 — 선택지 중 하나를 골라 지시하기   (내가 쓴 한글)
- 내가 쓴 한글: "A. 업로드 완료 시점에 확인을 붙인다 코드에 적용 해줘"   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: Let's go with A — add the check at upload completion. Put it in the code.
- 왜 이렇게: 제안 목록에서 하나를 고를 때의 관용구가 `Let's go with A` 다. `I choose A` 는
  시험 답안처럼 들린다. "코드에 적용해줘"는 `apply it to the code` 보다 `put it in the code`
  가 구어에 맞고, 격식이 필요하면 `implement it` 한 단어로 끝난다.

### 카드 12 — 만들고 싶은 구조를 설명하기   (내가 쓴 한글)
- 내가 쓴 한글: "letters_to_agent 폴더를 만들고 거기에 회사에 있는 LLM이 따라서 수행할 수 있도록 구조를 만들고 싶어. 각 단계 별로 완성이 되면 다음 단계로 넘어가는거야."   (출처: transcript:equipment_data_map d218c61c)
- 자연스러운 영어: I want a `letters_to_agent` folder laid out so the LLM at the office can just follow it, one stage at a time — it only moves on once the current stage is finished.
- 왜 이렇게: "따라서 수행할 수 있도록"은 `so that it can perform by following` 이 아니라
  `so … can just follow it` 이다. `just` 가 "해석하지 말고 그대로 따라가면 된다"는 설계 의도를
  담는다. "각 단계 별로 완성이 되면 넘어간다"는 `once` 절이 딱 맞는 자리 — `if` 는 넘어갈지
  말지가 불확실하다는 뜻이 되어 순차 진행 규칙과 어긋난다.

### 카드 13 — 제약을 알려주고 대응을 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "28B context window는 256K 일거야. 중간 중간 컨텍스트가 가득 찰경우 어떻게 해야하지?"   (출처: transcript:equipment_data_map d218c61c)
- 자연스러운 영어: The 28B model has a 256K context window, I think. What should it do when the window fills up partway through?
- 왜 이렇게: 추측을 담은 "~일거야"는 문장 끝에 `I think` 를 붙이는 게 가장 가볍다. `It might be
  256K` 라고 하면 확신이 더 떨어져 보인다. "중간 중간"은 반복이 아니라 "작업 도중"이라는 뜻이니
  `partway through` 가 맞고, `from time to time` 으로 옮기면 뜻이 달라진다. 주어를 `it`(모델)로
  두면 "내가 뭘 해야 하나"가 아니라 "규칙을 어떻게 정할까"라는 설계 질문이 된다.

### 카드 14 — 분업으로 수렴했다는 판정   (고급 한글 · 번역)
- 한글 원문: "nginx가 Apache를 대체한 게 아니라, Apache가 하던 일이 둘로 쪼개졌습니다. 커넥션 관리는 이벤트 모델이 압도적으로 유리하고, 앱 실행은 프로세스 모델이 필수인데, 이 둘을 한 프로그램이 다 하는 게 애초에 무리였던 거죠."   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: nginx did not replace Apache; Apache's job split in two. Connection handling strongly favours an event model, application execution needs a process model, and asking one program to do both was always a stretch.
- 번역 포인트: "~게 아니라 ~다"는 `not A but B` 로 옮기고 싶어지지만, 문장이 길면 세미콜론으로
  끊는 편이 훨씬 읽힌다. "쪼개졌습니다"는 수동으로 보이나 행위자가 없으므로 자동사 `split` 이
  맞는다 — `was split` 은 누가 쪼갰는지를 묻게 만든다. "애초에 무리였던 거죠"는 `was always a
  stretch` 가 정확한 짝으로, `always` 가 "애초에"를, `a stretch` 가 "무리"의 완곡함을 가져간다.

### 카드 15 — 성능의 출처를 뒤집어 말하기   (고급 한글 · 번역)
- 한글 원문: "nginx의 성능은 상당 부분 '안 하기로 한 것들'에서 나옵니다."   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: A good part of nginx's speed comes from what it decided not to do.
- 번역 포인트: 따옴표로 묶인 명사구 "안 하기로 한 것들"은 영어에서 선행사 없는 `what` 절로
  옮기면 따옴표 없이도 같은 무게가 산다. `the things it chose not to do` 도 되지만 `what` 쪽이
  짧고 격언에 가깝다. "상당 부분"은 `a large portion of` 보다 `a good part of` 가 구어와 문어
  사이에 잘 앉는다.

### 카드 16 — 재시작을 해결로 세지 않는다는 판정   (고급 한글 · 번역)
- 한글 원문: "'재시작하니 됐다'는 해결이 아니라 미해결의 다른 이름입니다. 원인을 안 남기니 다음에 또 나고, 그때는 재시작이 안 통할 수도 있어요."   (출처: transcript:llm_serving d5ba8a8f)
- 자연스러운 영어: "It worked after a restart" is not a fix; it is unresolved under another name. It leaves no cause behind, so it will happen again — and next time the restart may not save you.
- 번역 포인트: "~의 다른 이름"은 `another name for X` 가 사전적 짝이지만, 여기서는 `under
  another name` 이 낫다 — 같은 것이 이름만 바꿔 통과했다는 그림이 살아난다. "안 통할 수도
  있어요"의 완곡함은 조동사 `may` 로 충분하고, `might not work` 보다 `may not save you` 가
  재시작을 구원자로 세웠다가 거두는 대비를 만든다.

## 영어 다듬기

### 카드 1 — enable 은 부사 on 을 받지 않는다
- 내가 쓴 영어: "enable on for background auto-updates"   (출처: transcript:llm_serving 4a62ec10)
- 정정: `enable on` 은 성립하지 않는다. `enable` 은 목적어를 바로 받는 타동사라 `enable
  background auto-updates` 이고, 부사 `on` 을 쓰려면 동사를 `turn` 으로 바꿔 `turn on
  background auto-updates` 여야 한다. 두 표현이 머릿속에서 섞인 형태다.
- 더 나은 표현: Turn background auto-updates back on.
- 왜: 껐던 것을 다시 켜는 상황이므로 `back` 이 들어가야 "원래대로 돌린다"는 뜻이 산다. 그리고
  `turn X on` 처럼 목적어를 가운데 넣으면 무엇을 켜는지가 먼저 들려 구어에서 더 자연스럽다.

### 카드 2 — go 는 슬래시 명령의 동사가 아니다
- 내가 쓴 영어: "go /humanize-korean:humanize in the study folder"   (출처: transcript:llm_serving d5ba8a8f)
- 정정: `go` 는 뒤에 목적어를 바로 받지 못한다(`go run`, `go to X` 는 되지만 `go X` 는 안 된다).
  명령을 실행하라는 뜻이면 `run` 이 맞다.
- 더 나은 표현: Run `/humanize-korean:humanize` on the study folder.
- 왜: 전치사도 함께 바뀐다. `in the study folder` 는 "그 폴더 안에서 실행하라"(작업 디렉터리)가
  되고, `on the study folder` 는 "그 폴더를 대상으로"가 된다. 의도는 후자였다.

### 카드 3 — 목적을 나타내는 to부정사구는 매달아 두지 않는다
- 내가 쓴 영어: "for poc/workflow_3 to run"   (출처: transcript:auto_recipe_creator ff8357d4)
- 정정: 앞이 한국어 문장이라 이 구가 어디에도 걸리지 못하고 떠 있다. `for X to Y` 는 문장 안의
  술어에 붙어야 한다.
- 더 나은 표현: What needs checking before `poc/workflow_3` can run?
- 왜: 목적을 나타내는 `for … to …` 를 조건으로 바꿔 `before … can run` 으로 쓰면 "그게 돌기
  전에 끝나야 할 일"이라는 시간 순서가 드러난다. 점검 항목을 요청할 때는 이 순서가 더 유용하다.

### 카드 4 — the job 과 that job 은 다른 것을 가리킨다
- 내가 쓴 영어: "clean up worktrees if the job is done"   (출처: transcript:skewnono_v3_nuxt 23a9b296)
- 더 나은 표현: Clean up the worktrees if that work is finished.
- 왜: 문법 오류는 없다. 다만 `the job` 은 앞에서 특정한 작업을 언급했을 때만 자연스럽고, 새 세션
  첫 줄에서는 무슨 일인지 불분명하다. 지난번 작업을 가리키려면 `that work` 나 `that branch's
  work` 가 낫다. `worktrees` 도 이 저장소의 특정 워크트리들이므로 `the` 를 붙인다. `done` 은
  일상적이고 `finished` 는 "끝까지 갔다"에 조금 더 무게가 실린다.

### 카드 5 — 부사 하나를 쉼표 사이에 끼우면 무게가 흔들린다
- 내가 쓴 영어: "Correct these residual issues now, minimally, then re-sync spec.md."   (출처: transcript:equipment_data_map de6f3de9)
- 더 나은 표현: Correct these residual issues now with the smallest edits that work, then re-sync `spec.md`.
- 왜: 오류는 없고 뜻도 통한다. 다만 쉼표에 갇힌 `minimally` 는 "최소한으로 고쳐라"인지 "최소한
  이것만은 고쳐라"인지 두 갈래로 읽힌다. 지시문에서는 이런 이중성이 비싸다. 부사를 구로 풀어
  `with the smallest edits that work` 로 쓰면 범위 제한이라는 뜻 하나만 남는다.

### 카드 6 — concise 는 검사가 아니라 출력에 붙는 말이다
- 내가 쓴 영어: "Run git diff --check, a snapshot equality check ignoring the four-line preamble, and concise rg checks for those patterns."   (출처: transcript:equipment_data_map de6f3de9)
- 더 나은 표현: … and narrowly scoped `rg` checks for those patterns.
- 왜: 문장 자체는 정확하고, 세 항목을 한 목록에 얹은 구조도 좋다. `concise` 는 말·글이 짧다는
  뜻이라 검사에 붙으면 "결과를 짧게 보고하라"로 읽힐 여지가 있다. 의도는 검사 범위를 좁히라는
  것이므로 `narrowly scoped` 가 정확하고, `targeted` 도 같은 자리에 쓸 수 있다.
