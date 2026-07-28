# 2026-07-29 — 코칭

오늘 배치의 `[user]` 발화는 모두 영어였습니다. 한국어로 쓴 문장이 없어 한글→영어 카드는 만들지 않고,
영어 다듬기만 3장 정리합니다.

## 영어 다듬기

### 카드 1 — exist 는 수동태가 없다

- 내가 쓴 영어: "office_utils/read_idp_info.py is existed in my office, so when I pull git, it will be an issue right?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정:
  - `is existed` → `exists`. exist 는 목적어를 갖지 않는 자동사라 수동태 자체가 없습니다. 같은 실수가 잘 나는 자동사로 `happen`, `occur`, `appear`, `belong` 이 있습니다 — `it was happened` 도 늘 틀립니다.
  - `when I pull git` → `when I pull` 또는 `when I run git pull`. pull 의 목적어는 git 이 아니라 브랜치·리모트입니다(`pull from origin`). 도구 이름을 목적어 자리에 두면 어색해집니다.
  - `it will be an issue right?` → `it'll be an issue, right?` 부가 의문 앞에는 쉼표를 찍습니다.
- 더 나은 표현: "`office_utils/read_idp_info.py` already exists on my office machine — wouldn't a `git pull` overwrite it?"
- 왜: 파일이 있는 곳은 사무실이라는 공간이 아니라 사무실 PC 라서 `on my office machine` 이 정확합니다. 걱정을 평서문으로 말한 뒤 `right?` 를 붙이는 것보다 `wouldn't ~?` 부정 의문으로 던지면 "내 생각엔 이런데 맞나요"가 한 문장에 담기고, 상대가 아니라고 답하기도 쉬워집니다.

### 카드 2 — had better 는 경고에 가깝다

- 내가 쓴 영어: "you'd better to use different name in order to avoid conflicts at home?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정:
  - `you'd better to use` → `you'd better use`. had better 뒤에는 to 없는 동사원형이 옵니다.
  - `different name` → `a different name`. 셀 수 있는 명사의 단수에는 관사가 필요합니다.
- 더 나은 표현: "Would it be safer to give the home stand-in a different name, so it can't clash with the real one at the office?"
- 왜: `you'd better` 는 "그렇게 안 하면 곤란해진다"는 경고 쪽에 가깝습니다. 동료나 조수에게 안을 내밀 때는 세게 들리니 `Would it be safer to ...?` / `Should we ...?` 로 낮춥니다. `in order to` 는 문어체라 짧은 대화에서는 `to` 하나로 충분하고요. 하나 더 — 이름이 부딪히는 곳은 집이 아니라 사무실이라, 원문의 `at home` 은 자리를 옮겨야 뜻이 맞습니다.

### 카드 3 — 지시문 첫머리의 무주어 분사구

- 내가 쓴 영어: "Correcting three idp_image_info columns to the types the real office parser returns, confirmed 2026-07-28: Addressing and Mother_Para are bool (not "Yes"/"No" strings and not a parameter name), dnumber_removed is bool (not int64)."   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: "This change corrects three `idp_image_info` columns to the types the real office parser returns (confirmed at the office on 2026-07-28)."
- 왜: 주어 없이 `-ing` 로 여는 형태는 커밋 메시지나 릴리스 노트에서는 자연스럽지만, 작업 지시문 첫머리에 오면 고치는 주체가 흐려집니다. `This change corrects ...` 로 주어를 세우면 뒤에 붙는 콜론 목록이 무엇의 근거인지 바로 읽힙니다. 날짜만 툭 던진 `confirmed 2026-07-28` 도 `confirmed at the office on 2026-07-28` 처럼 전치사를 채워 괄호로 내리면 걸리는 데가 없어집니다. 참고로 뒤 문장 "The recipe-open table already shows the right eight columns — only the types and their rendering are wrong." 은 손댈 데가 없습니다. 대시로 범위를 좁히고 `only` 로 남은 문제를 한정하는 방식이 그대로 좋은 본보기입니다.
