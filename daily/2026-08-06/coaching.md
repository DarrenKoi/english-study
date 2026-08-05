# 2026-08-06 — 코칭

## 한글→영어

### 카드 1 — 편의 래퍼를 걷어내고 직접 조합하기   (내가 쓴 한글)
- 내가 쓴 한글: "combined_idp_info는 위에 function들을 하나로 합친 거였어. 그래서 return 값이. result[parameter] 안에는 "addr1_beam_condition", "addr2_beam_condition", "amp" 등이 파라미터 별로 담겨 있었어."   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `combined_idp_info was just those functions bundled into one, so its return value was keyed by parameter — result[parameter] held addr1_beam_condition, addr2_beam_condition, amp and so on.`
- 왜 이렇게: "하나로 합친 거였어"는 `bundled into one` 이 정확하다. `combined` 를 다시 쓰면 이름과 겹쳐 설명이 안 된다. "파라미터 별로 담겨 있었어"는 영어에서 `keyed by parameter` 라는 한 구로 굳어 있어서, 자료구조 얘기를 할 때 이만큼 짧게 옮기기 어렵다. 원문에서 "그래서 return 값이."로 끊긴 자리는 영어로는 문장을 끊지 말고 `so its return value was keyed by parameter` 로 이어 붙이는 편이 읽힌다.

### 카드 2 — 없애고 네가 직접 만들어 달라   (내가 쓴 한글)
- 내가 쓴 한글: "idp_amp_reader를 바꾸면서 combined_idp_info는 없애고 너가 직접 조합해서 만들도록 하는게 좋겠어. 가능할까?"   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `Now that idp_amp_reader has changed, I'd rather drop combined_idp_info and have you assemble the result yourself. Is that doable?`
- 왜 이렇게: "~하는 게 좋겠어"는 `it would be good to` 로 직역하면 남 얘기처럼 들린다. `I'd rather …` 가 선호를 밝히면서도 지시가 되지 않아 이 자리에 맞다. "너가 직접 만들도록 하다"의 사역은 `have you assemble` — `make you` 는 강제, `let you` 는 허가라서 둘 다 어긋난다. 끝의 "가능할까?"는 `Is it possible?` 보다 `Is that doable?` 이 자연스럽다. 실현 가능성이 아니라 "품이 감당되냐"를 묻는 말이기 때문이다.

### 카드 3 — 무엇이 달라졌는지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "sem list 어떤 변경 점이 있지?"   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `What's changed in sem_list since that copy was made?`
- 왜 이렇게: "변경 점"을 `change points` 로 옮기면 통하지 않는다. 영어는 명사가 아니라 현재완료 `What's changed` 로 묻는다 — 과거에 일어나 지금까지 이어지는 차이를 묻는 자리라 시제가 곧 의미다. 맥락상 "그 사본 이후"가 핵심이므로 `since that copy was made` 를 붙여야 질문이 겨냥한 범위가 살아난다. 더 짧게는 `What did I miss in sem_list?`
- 격식 짝: refined `What has changed in sem_list since that snapshot?` / plain `So what's new in sem_list?`

### 카드 4 — 짧은 승인   (내가 쓴 한글)
- 내가 쓴 한글: "수정해줘"   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `Go ahead and fix it.`
- 왜 이렇게: `Fix it.` 만 쓰면 명령이 날것으로 남는다. `Go ahead and …` 가 앞에 붙으면 "내가 승인하니 진행하라"가 되어, 상대가 이미 제안한 일을 재가하는 이 맥락에 딱 맞는다. 앞선 "둘 다 처리할까요?"에 답하는 자리라면 `Yes, please — both.` 도 자주 쓴다.

### 카드 5 — 늑대를 외치는 진단 도구   (고급 한글 · 번역)
- 한글 원문: "리허설할 때마다 실패를 보고하는 도구는 정작 맞는 날 아무도 안 믿기 때문에, 대역 모듈에 IS_HOME_STANDIN을 달아서 진단이 진짜 발견과 잡음을 구분하게 했습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `A tool that reports failure at every rehearsal is one nobody believes on the day it is right, so the stand-in module now carries IS_HOME_STANDIN and the diagnostic can tell a real finding from noise.`
- 번역 포인트: "정작 맞는 날"이 이 문장의 무게중심이다. `on the day it is right` 로 옮기면 관계절이 `the day` 를 수식하며 "그 하루"의 특별함을 살린다. "아무도 안 믿는다"는 부정 주어 `nobody` 를 그대로 쓰되 `is one nobody believes` 처럼 대명사 `one` 을 세워야 앞의 긴 주어를 다시 받을 수 있다. "구분하게 했습니다"의 사역은 영어에서 굳이 `make … distinguish` 로 갈 필요가 없다 — `and the diagnostic can tell A from B` 로 결과를 그냥 서술하는 편이 자연스럽다. `tell A from B` 가 "A와 B를 구별하다"의 관용이다.

### 카드 6 — 잘못을 흉내내는 mock   (고급 한글 · 번역)
- 한글 원문: "잘못된 사무실 응답을 흉내내는 mock은 프런트엔드에 그 잘못된 형태를 가르칩니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 3dcdb4a 세션)
- 자연스러운 영어: `A mock that imitates a broken office response teaches the frontend that broken shape.`
- 번역 포인트: "가르치다"를 은유 그대로 `teach` 로 두는 것이 요령이다. 영어에서도 `teach the frontend X` 처럼 사람이 아닌 것을 간접목적어로 세우는 쓰임이 살아 있어, 의인화가 어색하지 않다. "형태"는 `format` 이 아니라 `shape` — 데이터의 구조를 말할 때 영어는 `shape` 를 쓴다. "잘못된"이 두 번 나오는데 앞은 `broken`(고장 난 응답), 뒤는 같은 낱말을 반복해 그 고장이 그대로 전수된다는 점을 드러냈다.

### 카드 7 — 다른 시대의 사본   (고급 한글 · 번역)
- 한글 원문: "코드는 정상 200을 돌려주는데 실행되는 사본이 다른 시대의 것이라 기능 일부가 없거나 값이 틀립니다."   (출처: transcript:[assistant] skewnono-v3-nuxt 0bec48c7)
- 자연스러운 영어: `The code returns a healthy 200, but the copy actually running is from another era, so a feature is missing or the values are wrong.`
- 번역 포인트: "정상 200"은 `a normal 200` 보다 `a healthy 200` 이 관용이다 — 헬스체크 어휘가 상태 코드에 그대로 붙는다. "실행되는 사본"의 수동 표현은 `the copy actually running` 처럼 능동 분사로 뒤에서 수식하는 편이 짧고, `actually` 가 "우리가 읽는 코드가 아니라"라는 대조까지 실어 준다. "다른 시대의 것"은 직역 `from another era` 가 그대로 통하고, 과장이 살아 있어 원문의 어감도 남는다.

## 영어 다듬기

### 카드 1 — 스케줄러 작업 두 개 요청
- 내가 쓴 영어: "add a task in scheduler job to maintain the logs stored in the flask server. … I want to keep it remove if the dates are older than a week. Only keep the log files in 7 days. … I want to reboot the server at 00:05 am every night by touching it in order to keep the server fresh."   (출처: transcript:[user] skewnono-v3-nuxt a14518c0)
- 정정: `I want to keep it remove if …` → `I want them removed if …`. `keep + 목적어 + 원형동사`는 성립하지 않는다. 유지의 `keep` 뒤에는 분사가 오고(`keep it running`), 여기서 필요한 뜻은 유지가 아니라 지시라서 `want + 목적어 + 과거분사`가 맞다. `Only keep the log files in 7 days` 의 `in` 은 기간 안이 아니라 시점 이후를 뜻하므로 `for 7 days` 또는 `from the last 7 days`.
- 더 나은 표현: `Add a scheduled job that prunes the Flask server's logs — keep only the last 7 days and delete anything older. We've enabled touch-reload in wsgi.ini, so add a second job that touches that file at 00:05 every night to recycle the workers.`
- 왜: 로그 정리는 `maintain` 보다 `prune` 이나 `sweep` 이 그 일을 정확히 가리킨다. 보관 기준은 `keep only the last 7 days` 한 구면 충분해서 "지우고 남기고"를 두 문장으로 나눌 필요가 없다. `reboot the server` 는 호스트 재부팅으로 읽히니, uWSGI 워커만 되살리는 상황에서는 `recycle the workers` 또는 `gracefully reload` 가 맞다. `keep the server fresh` 는 뜻이 통하지만 구어라, 문서에 남길 문장이면 `so long-running workers don't accumulate state` 처럼 이유를 밝히는 편이 낫다.

### 카드 2 — 트리거 파일 지정
- 내가 쓴 영어: "the file to restart for me is restart.txt in the root."   (출처: transcript:[user] skewnono-v3-nuxt a14518c0)
- 정정: 문법 오류 없음.
- 더 나은 표현: `The file I touch to trigger a restart is restart.txt at the repo root.`
- 왜: `the file to restart` 는 "재시작될 파일"로도 읽혀 주체가 흐려진다. `the file I touch to trigger a restart` 가 동작(touch)과 결과(restart)를 분리해 준다. `for me` 는 "나를 위해"로 들리므로 빼고, 위치는 `in the root` 보다 `at the repo root` 가 관용이다 — 루트는 지점이라 `at` 을 쓴다.

### 카드 3 — 백엔드가 함수들을 알고 있는지 확인 요청
- 내가 쓴 영어: "you know that we use multiple functions in this py file. … check the backend know these functions and use them."   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 정정: `check the backend know these functions` → `check that the backend knows these functions`. `check` 뒤 명사절에는 접속사 `that` 이 필요하고, 3인칭 단수 주어에는 `knows`.
- 더 나은 표현: `Confirm the backend is aware of these five readers and actually calls them.`
- 왜: `check` 는 훑어보라는 뉘앙스라, 사실 확인을 요구하는 자리에서는 `confirm` 이 한 단계 위다. `know` 는 사람에게 쓰는 낱말이라 코드가 주어일 땐 `is aware of` 나 `references` 가 자연스럽다. "쓰고 있는지"는 `use` 보다 `actually calls` 가 정확하다 — import 만 해 두고 호출하지 않는 경우와 구분되고, 이번 대화에서 실제로 문제가 된 지점이 바로 그 차이였다.

### 카드 4 — 모달 버그 신고
- 내가 쓴 영어: "in recipe-search/open, I click Align 정보 button to see the align images of OM and SEM. I do not see the info table about Chip.X, Chip.Y, Coordinate.X … and the popup windows freezed and cannot close it."   (출처: transcript:[user] skewnono-v3-nuxt 0bec48c7)
- 정정: `the popup windows freezed and cannot close it` → `the popup window freezes and I can't close it`. `freeze` 의 과거형은 `froze`(과거분사 `frozen`)이며 `freezed` 는 없는 형태다. 창이 하나이므로 단수 `window`, 그리고 `cannot close it` 은 주어가 창이 되어 "창이 스스로를 못 닫는다"가 되니 주어를 `I` 로 바꿔야 한다.
- 더 나은 표현: `On recipe-search/open, clicking the "Align 정보" button opens the OM/SEM align images, but the info table (Chip.X, Chip.Y, Coordinate.X, P.No) never renders and the modal locks up — the ✕ does nothing.`
- 왜: 버그 신고는 시제를 현재로 통일하면 재현 절차로 읽힌다. `I click … I do not see …` 를 `clicking … opens …, but … never renders` 로 묶으면 원인과 증상의 관계가 드러난다. UI 용어로는 `popup window` 보다 `modal`, "안 보인다"는 `never renders` 가 프런트엔드 어휘다. 마지막의 `the ✕ does nothing` 처럼 시도한 행동과 그 결과를 붙여 주면 개발자가 재현 경로를 바로 잡는다.
