# 2026-11-21 — 코칭

오늘 내가 쓴 한국어는 짧은 지시가 대부분입니다. "수정 적용", "추가해줘", "local에만 보존"처럼 명사로 끊거나 목적어를 뺀 말이에요. 한국어는 이렇게 줄여도 통하지만 영어는 동사와 목적어를 채워야 문장이 섭니다. 무엇을 넣어야 하는지가 오늘의 요점입니다. 영어로 쓴 문장도 하나 있어서 영어 다듬기 카드를 만들었습니다.

## 한글→영어

### 카드 1 — 수정 적용   (내가 쓴 한글)
- 내가 쓴 한글: "수정 적용"   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Go ahead and apply the changes.
- 왜 이렇게: 명사 두 개로 끝낸 지시라서 영어로는 동사를 세워야 합니다. `Apply the changes.` 만으로도 되고, 제안을 받아들이는 상황이라 `Go ahead and …` 를 앞에 두면 "제안한 대로 진행해"가 됩니다. 여기서 "수정"은 diff 로 제안된 변경이니 `fixes` 보다 `changes` 나 `edits` 가 맞아요. 버그를 고친 게 아니라 문서를 다듬은 것이니까요. 더 짧게는 `Apply them.`, 전부라는 뜻을 살리면 `Apply all of them.`

### 카드 2 — off 로 전환   (내가 쓴 한글)
- 내가 쓴 한글: "explanatory output style off로 전환."   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Turn off the explanatory output style.
- 왜 이렇게: "off 로 전환"을 `switch to off` 로 옮기면 어색합니다. 켜고 끄는 것은 `turn off` / `turn on` 이 기본이고, 설정 화면의 토글이라면 `switch it off`, 플러그인이면 `disable` 을 씁니다. 목적어가 길 때는 `turn off + 목적어` 순서가 읽기 편하고 대명사일 때는 반드시 가운데에 넣습니다(`turn it off`).

### 카드 3 — ~할 때는 무시할 수 있어?   (내가 쓴 한글)
- 내가 쓴 한글: "poteto mode 실행할 때는 ponytail 무시할 수 있어?"   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Can you ignore ponytail while poteto mode is running?
- 왜 이렇게: "실행할 때"는 실행되는 동안 내내라는 뜻이라 `when` 보다 `while … is running` 이 정확합니다. "무시할 수 있어?"는 가능한지 묻는 동시에 그렇게 해 달라는 부탁이어서 `Can you …?` 가 둘을 다 받습니다. 규칙 사이의 우선순위를 묻는 말투로는 `Can poteto mode take precedence over ponytail?` 이 있고, 설정으로 고정하고 싶다는 뜻이면 `Can we make poteto mode override ponytail?`

### 카드 4 — 추가해줘   (내가 쓴 한글)
- 내가 쓴 한글: "추가해줘"   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Yes, add it.
- 왜 이렇게: `add` 는 목적어 없이 못 씁니다. 한국어는 "추가해줘"만으로 통하지만 영어는 `it` 이라도 넣어야 해요. 어시스턴트가 "말씀해 주시면 추가하겠습니다"라고 했으니 그 제안에 답하는 `Yes, please add it.` 이나 `Go ahead.` 가 자연스럽습니다. 어디에 넣는지까지 말하면 `Add it to the global CLAUDE.md.`

### 카드 5 — 모델들도 업데이트   (내가 쓴 한글)
- 내가 쓴 한글: "그리고 poteto mode에 사용되는 모델들도 업데이트 해줘."   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Also, update the models that poteto mode uses.
- 왜 이렇게: "~에 사용되는 모델"을 직역하면 수동 관계절 `the models that are used in poteto mode` 인데, 영어는 능동 `the models poteto mode uses` 가 더 짧고 자연스럽습니다. "그리고 ~도"는 문두 `Also,` 하나로 충분하고 `And also … too` 처럼 겹치지 않습니다. 문장 끝에 붙여 `Update the models poteto mode uses as well.` 도 좋아요. "모델들"의 복수는 `models` 가 이미 맡습니다.

### 카드 6 — 올라가 있으면 남기지 않아도 됨   (내가 쓴 한글)
- 내가 쓴 한글: "정리되어 올라가 있으면 남기지 않아도 됌."   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: If the cleaned-up version is already committed, there's no need to keep the originals.
- 왜 이렇게: 한국어 문장에는 주어도 목적어도 없습니다. 영어로는 무엇이 올라가 있고 무엇을 남기지 않는지 채워야 해요. "정리되어 올라가 있다"는 정리한 판이 이미 커밋돼 있다는 뜻이라 `the cleaned-up version is already committed` 로 풀었습니다. 푸시까지 됐다는 뜻이면 `already pushed` 나 `already in the repo`. "~하지 않아도 된다"는 `don't have to`, `no need to`, `needn't` 가 있고 지시문에서는 `there's no need to` 가 부드럽습니다. 더 짧게는 `If it's already in the repo in cleaned-up form, you can drop the originals.` (참고로 한국어 맞춤법은 "됌"이 아니라 "됨"입니다.)

### 카드 7 — local 에만 보존   (내가 쓴 한글)
- 내가 쓴 한글: ".scratch는 local에만 보존."   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Keep `.scratch` local only.
- 왜 이렇게: "보존"을 `preserve` 로 옮기면 박물관 유물 같은 느낌이 납니다. 파일을 그냥 두는 것은 `keep` 이에요. `local` 은 형용사라서 `keep X local` 의 5형식에 그대로 들어가고, "에만"은 뒤에 `only` 를 붙입니다. git 맥락을 분명히 하려면 `Keep .scratch on my machine and out of the repo.` 나 `Don't commit .scratch; keep it local.`

### 카드 8 — 정상을 고장으로 판정   (고급 한글 · 번역)
- 한글 원문: "스킬을 그대로 따르면 정상 템플릿을 고장으로 판정합니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: Followed as written, the skill would flag a working template as broken.
- 번역 포인트: "그대로 따르면"은 `If you follow the skill as written` 이 기본입니다. 분사구문 `Followed as written,` 으로 줄이면 주어가 `the skill` 로 맞춰져 문장이 짧아져요. `as written` 은 "적힌 그대로"라는 굳은 표현입니다. "A 를 B 로 판정하다"는 `flag A as B` 가 깔끔하고 `misjudge` 나 `misdiagnose A as B` 도 됩니다. 아직 일어나지 않은 일이라 `would` 를 넣었습니다.

### 카드 9 — 어느 쪽이 더 최근이냐에 달림   (고급 한글 · 번역)
- 한글 원문: "모델이 매번 조정해야 하고 결과는 어느 쪽이 더 최근에 로드됐느냐에 달립니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: The model has to reconcile them every time, and the outcome depends on which one happened to load last.
- 번역 포인트: 여기 "조정"은 값을 맞추는 `adjust` 가 아니라 충돌하는 지시를 절충한다는 뜻이라 `reconcile` 이 맞습니다. "~느냐에 달리다"는 `depend on + 의문사절` 로 받고, 의문사절 안은 평서문 어순입니다(`which one loaded last`). "더 최근에"는 셋 중 하나라서 비교급 `more recently` 보다 `last` 가 정확해요. `happened to` 를 넣으면 순서가 우연이라는 원문의 불만이 살아납니다.

### 카드 10 — 독자가 본 적 없는 이전 상태   (고급 한글 · 번역)
- 한글 원문: "독자가 본 적 없는 이전 상태를 기준으로 한 문장입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: These sentences are written relative to an earlier state the reader has never seen.
- 번역 포인트: "~를 기준으로"는 `based on` 보다 `relative to` 가 맞습니다. 근거가 아니라 비교의 기준점이니까요. "본 적 없는"은 현재완료 `has never seen` 이고, 관계대명사를 뺀 `a state the reader has never seen` 이 자연스럽습니다. 풀어서 쓰면 `They describe the present by contrast with a past the reader never saw.`

### 카드 11 — 완전히 지운 것이 아니라서   (고급 한글 · 번역)
- 한글 원문: "완전히 지운 것이 아니라서 필요하면 되돌릴 수 있습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 444fbcbd)
- 자연스러운 영어: They aren't permanently deleted, so you can restore them if you need to.
- 번역 포인트: "완전히 지우다"는 `completely delete` 보다 `permanently delete` 가 관용입니다. 휴지통으로 옮긴 것과 대비되는 말이에요. "되돌리다"는 파일이면 `restore`, 변경이면 `revert`, 방금 한 동작이면 `undo` 로 갈립니다. `if you need to` 는 뒤의 `restore them` 을 생략한 꼴이라 `to` 를 남겨야 합니다.

## 영어 다듬기

### 카드 12 — if anything to push
- 내가 쓴 영어: "commit and push if anything to push in this repo"   (출처: transcript:[user] skewnono_v3_nuxt 444fbcbd)
- 정정: commit and push if **there's** anything to push in this repo — `if` 절에도 주어와 동사가 있어야 합니다. `if anything to push` 는 `there is` 가 빠졌어요. 주어와 be 동사를 함께 지울 수 있는 것은 `if necessary`, `if possible`, `if any` 같은 굳은 꼴뿐입니다.
- 더 나은 표현: Commit and push anything that's outstanding in this repo. / If there's anything left to push in this repo, commit and push it.
- 왜: `outstanding` 은 "아직 처리 안 된"이라는 형용사로, 커밋 안 된 변경과 푸시 안 된 커밋을 한 단어로 묶습니다. 둘째 안은 조건을 앞에 두고 `it` 으로 받아서 무엇을 푸시하는지 분명해져요. 아주 짧게 쓰고 싶으면 굳은 꼴을 빌려 `Commit and push, if there's anything.` 도 됩니다.
