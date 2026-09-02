# 2026-09-03 — 코칭

## 한글→영어

### 카드 1 — 저장 경로를 아느냐고 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "minIO에 raw msr 파일이 저장되는 경로를 알고 있나?"   (출처: transcript:[user] skewnono_v3_nuxt 015a5b24)
- 자연스러운 영어: Do you know where the raw MSR files are stored in MinIO?
- 왜 이렇게: "경로를 알고 있나"를 `Do you know the path where...` 로 옮기면 관계절이 무거워진다. 영어는 `where` 하나로 장소 목적절을 만들어 path 라는 명사를 아예 지운다. 정말 키 구조 자체가 궁금하면 `What's the key layout for raw MSR files in MinIO?` 가 더 정확하다 — MinIO 는 경로가 아니라 key 로 말하니 어휘를 도메인에 맞추는 편이 낫다.

### 카드 2 — 빠뜨린 걸 뒤늦게 떠올리기   (내가 쓴 한글)
- 내가 쓴 한글: "raw_msr도 지워야 하는데! 잊고 있었네. 현재 scheduler에 빠져있어?"   (출처: transcript:[user] skewnono_v3_nuxt 015a5b24)
- 자연스러운 영어: We need to purge `raw_msr` too — I'd completely forgotten. Is it missing from the scheduler right now?
- 왜 이렇게: 감탄 부호를 그대로 옮겨 `We need to purge raw_msr too!` 라고 하면 영어에서는 화난 것처럼 읽힌다. 대시로 끊고 `I'd completely forgotten` 을 붙이면 "아 맞다" 하는 뉘앙스가 살아난다. 과거완료 `I'd forgotten` 은 "지금까지 잊고 있었다"는 상태를 담아 단순 과거 `I forgot` 보다 정확하다. "빠져있어?"는 `Is it missing from ~?` — `Is it excluded?` 는 누가 일부러 뺐다는 뜻이 되어 어감이 다르다.

### 카드 3 — 추천안을 그대로 받기   (내가 쓴 한글)
- 내가 쓴 한글: "추천대로 진행"   (출처: transcript:[user] skewnono_v3_nuxt f48e6b28)
- 자연스러운 영어: Go with your recommendations.
- 왜 이렇게: `Proceed as recommended.` 도 틀리지 않지만 공문 냄새가 난다. `Go with X` 는 여러 선택지 중 하나를 고른다는 구어 표현이라 Q1~Q8 같은 선택형 질문에 답할 때 딱 맞다. 더 짧게는 `Your picks, all of them.` 도 자연스럽다.

### 카드 4 — 조건부 승인   (내가 쓴 한글)
- 내가 쓴 한글: "문제 없으면 Excel로 통일"   (출처: transcript:[user] skewnono_v3_nuxt f48e6b28)
- 자연스러운 영어: If nothing depends on the CSVs, go ahead and standardise on Excel.
- 왜 이렇게: "문제 없으면"을 `If there's no problem` 으로 직역하면 무엇이 문제인지가 사라진다. 앞 문맥에서 확인해야 할 것이 "이 CSV 를 스크립트로 받아 쓰는 곳이 있는가"였으니 그 조건을 명시하는 편이 낫다. "통일"은 `unify` 보다 `standardise on X` — 여러 형식 중 하나를 표준으로 정한다는 뜻이 정확히 담긴다.

### 카드 5 — 곁가지까지 반영됐는지 확인   (내가 쓴 한글)
- 내가 쓴 한글: "button 이름들도 수정된건가?"   (출처: transcript:[user] skewnono_v3_nuxt f48e6b28)
- 자연스러운 영어: Did the button labels get updated too?
- 왜 이렇게: UI 에 보이는 글자는 name 이 아니라 label 이다. `Are the button names fixed?` 는 "고장난 걸 고쳤나"로 읽힌다. 여기서는 형식에 맞춰 문구를 갱신한 것이니 update 가 맞다. 수동태 `get updated` 는 `were updated` 보다 구어적이고, 누가 했는지를 묻지 않는 어감이 그대로 산다.

### 카드 6 — 되찾은 것이 무너뜨린 것   (고급 한글 · 번역)
- 한글 원문: "recall 을 +9.4pp 되찾자 rank-1 이 -17pp 무너졌다. 되찾은 후보들은 시스템이 순위를 못 매기는 후보였다."   (출처: repo:auto_recipe_creator 브리프 B — 원문 문체는 [assistant] 계열)
- 자연스러운 영어: Recovering 9.4 points of recall cost 17 points of rank-1. The candidates we won back were exactly the ones the system cannot rank.
- 번역 포인트: "~하자 ~했다"는 인과를 품은 시간 접속인데, 영어에서 `When we recovered ..., rank-1 collapsed` 로 풀면 두 사건이 나란히 놓여 대가라는 느낌이 약해진다. 동명사 주어 + `cost` 로 묶으면 "얻은 것이 곧 잃은 것의 값"이라는 시소가 문장 하나에 들어간다. "못 매기는"의 현재시제는 능력의 결여이므로 `cannot rank` — `could not rank` 로 옮기면 그때 한정된 실패로 좁아진다.

### 카드 7 — 드리프트가 아니라 앎의 차이   (고급 한글 · 번역)
- 한글 원문: "같은 필드가 두 provider 에서 다른 건 드리프트가 아니라 아는 것과 모르는 것의 차이입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 015a5b24)
- 자연스러운 영어: The same field differing across the two providers isn't drift — it's the difference between what we know and what we don't.
- 번역 포인트: "A 가 아니라 B"는 영어에서 `not A but B` 보다 대시로 끊는 편이 자연스럽다. 반박이 아니라 재규정이기 때문이다. "아는 것과 모르는 것"은 `knowledge and ignorance` 처럼 추상명사로 올리면 훈계조가 된다. `what we know and what we don't` 로 관계절을 그대로 두면 원문의 담백함이 남는다.

### 카드 8 — 문제의 성격을 다시 규정하기   (고급 한글 · 번역)
- 한글 원문: "이건 '둘 중 하나 고르기' 문제가 아니라 '일관성 없음' 문제입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt f48e6b28)
- 자연스러운 영어: This isn't a "which one" problem, it's an "it varies" problem.
- 번역 포인트: 인용부호로 문제 이름을 짓는 한국어 습관이 영어에도 그대로 있다. 다만 이름은 짧을수록 세다 — `choosing between two` 보다 `which one`, `lack of consistency` 보다 `it varies`. 접속에 쉼표만 쓴 comma splice 는 구어적 대비 문장에서 허용되고, 오히려 두 이름을 나란히 세워 준다.

## 영어 다듬기

### 카드 1 — 내가 직접 처리하겠다고 선을 긋기
- 내가 쓴 영어: "I will take care of it by myself with respect to purging raw_msr. Instead, I want to offer api (via the endpoint page) service to users so that they can read or download msr / pickle from minIO."   (출처: transcript:[user] skewnono_v3_nuxt 015a5b24)
- 정정: `with respect to purging raw_msr` 는 위치가 틀렸다. `with respect to` 는 주제를 앞세우는 전치사구라 문장 앞에 와야 하고, 뒤에 붙으면 `it` 이 무엇인지 밝히는 동격처럼 읽혀 어색해진다. `by myself` 도 중복이다 — `I will take care of` 가 이미 주체를 밝힌다. 관사도 빠졌다: `offer an API service`.
- 더 나은 표현: I'll handle the `raw_msr` purge myself. What I'd rather build is an API — exposed on the endpoints page — so users can read or download the MSR and pickle files straight from MinIO.
- 왜: `with respect to X, I will ...` 대신 X 를 목적어 자리로 끌어와 문장을 하나 줄였다. `Instead, I want to ...` 는 문법적으로 맞지만 밋밋하다. `What I'd rather build is ...` 라는 분열문(cleft)은 앞의 거절과 뒤의 요청을 한 축에 세워, 방향을 바꾸는 발화라는 게 문장 형태에서 드러난다. `straight from` 은 중간 단계 없이 바로라는 뜻을 더한다.

### 카드 2 — 형식을 통일하자고 제안하기
- 내가 쓴 영어: "throughout the pages, we offer either csv or excel download. why don't we unify them into a single one? excel can be better option?"   (출처: transcript:[user] skewnono_v3_nuxt f48e6b28)
- 정정: `excel can be better option` 에 관사가 빠졌다 — `a better option`. 그리고 서술문에 물음표를 붙이면 영어에서는 확신이 없어 흐려지는 느낌이 강하다. `Excel might be the better option.` 처럼 조동사로 완화하는 편이 낫다. `either csv or excel download` 는 `either a CSV or an Excel download` 로 관사를 살려야 한다.
- 더 나은 표현: Across the app, some pages export CSV and others export Excel. Should we standardise on one? Excel seems like the stronger default.
- 왜: `throughout the pages` 는 어색하다 — 페이지들을 관통한다는 뜻이 되기 때문에, 앱 전체를 가리키는 `Across the app` 이 맞다. `either A or B` 는 한 화면에서 둘 중 고른다는 뜻이라 실제 상황(화면마다 다르다)과 어긋난다. `some ... and others ...` 가 사실에 맞다. `Should we ...?` 는 `Why don't we ...?` 보다 제안을 열어 두어, 반대 근거를 들을 준비가 됐다는 신호를 준다. `the stronger default` 는 "지금 더 나은 쪽"이 아니라 "기본값으로 삼기에 더 나은 쪽"이라 논점이 정확하다.

### 카드 3 — 도구를 상황에 따라 골라 쓰라고 지시
- 내가 쓴 영어: "I see. you can use either playwright or Claude Chrome extension based on the situations."   (출처: transcript:[user] skewnono_v3_nuxt df4b4762)
- 정정: `based on the situations` 는 복수와 정관사가 둘 다 어긋난다. 관용형은 `depending on the situation` (단수, 무관사에 가까운 고정 표현). `Claude Chrome extension` 앞에도 관사가 필요하다 — `the Claude Chrome extension`.
- 더 나은 표현: Understood — use whichever fits: Playwright or the Claude Chrome extension.
- 왜: `you can use either A or B` 는 허가처럼 들려 판단 권한을 주는 뜻이 흐려진다. `use whichever fits` 는 "그때그때 네가 골라라"라는 위임을 한 단어(whichever)로 담는다. `I see.` 는 정보를 받았다는 뜻이지 승인은 아니다. 앞 결정을 뒤집는 자리이므로 `Understood` 가 더 맞다.

### 카드 4 — 브라우저 확인 방식 지시
- 내가 쓴 영어: "actively use Claude in Chrome browser extension to check/review features in the web applications. instead of playwright"   (출처: transcript:[user] skewnono_v3_nuxt df4b4762)
- 정정: `instead of playwright` 가 마침표 뒤에 조각으로 떨어져 있다. 앞 문장에 붙여야 한다. `in the web applications` 는 정관사가 특정 앱들을 가리키는데 여기서는 우리 앱 하나이므로 `in the app`. `Claude in Chrome browser extension` 은 수식이 겹쳐 있다 — `the Claude in Chrome extension` 이 실제 제품명 형태다.
- 더 나은 표현: Default to the Claude in Chrome extension, not Playwright, when you're checking a feature in the app.
- 왜: `actively use X` 는 강조처럼 보이지만 영어에서는 기준이 되지 못한다 — 얼마나 자주인지가 비어 있다. `Default to X` 는 "기본은 X, 예외는 따로"라는 규칙을 한 동사로 세운다. `not Playwright` 를 삽입구로 끼워 넣으면 대비가 규칙 안에 들어가 조각 문장이 사라진다.

### 카드 5 — 라벨링 기준을 바꾸라고 지시
- 내가 쓴 영어: "label them son to match the Mother_Para flag and mother can be highlighted in excel or csv if possible"   (출처: transcript:[user] skewnono_v3_nuxt ad54ba15)
- 정정: 문법 오류는 없다. 다만 `and` 앞에 쉼표가 없어 두 개의 별개 지시가 한 호흡으로 붙어 버렸고, `if possible` 이 문장 끝에 있어 무엇이 조건부인지 모호하다.
- 더 나은 표현: Label them `son` to match the raw Mother_Para flag. And if the writer supports it, highlight the mother rows in the Excel export — CSV can stay plain text.
- 왜: 두 지시를 문장으로 나누면 우선순위가 드러난다 — 첫째는 확정, 둘째는 조건부. `if possible` 을 앞으로 빼고 `if the writer supports it` 으로 구체화하면 상대가 무엇을 확인해야 하는지 알 수 있다. 마지막의 `CSV can stay plain text` 는 원문의 `or csv` 가 남긴 모호함을 미리 닫아 준다 — 애초에 CSV 에는 서식이 없으니, 지시하는 쪽에서 정리해 주면 되묻는 왕복이 사라진다.
