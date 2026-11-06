# 2026-11-07 — 코칭

## 한글→영어

### 카드 1 — 2단계라서 최적은 아니다   (내가 쓴 한글)
- 내가 쓴 한글: "왜냐하면 지금 mai-ui는 coarse, fine 두번에 걸쳐서 진행하기 때문에 최적이라고 볼 순 없음."   (출처: transcript:[user] auto-recipe-creator 59bde568)
- 자연스러운 영어: "But MAI-UI runs in two passes, coarse then fine, so I wouldn't call it optimal."
- 왜 이렇게: 앞선 결론("100%라 교체해도 동점")에 반론을 다는 말이라 `Because` 보다 `But` 으로 여는 편이 영어답습니다. `Because ...` 로 문장을 시작하고 주절 없이 끝내면 영어에서는 미완성 문장이 됩니다. "두 번에 걸쳐서 진행"은 `runs in two passes` 가 가장 짧습니다. `pass` 는 데이터를 한 번 훑는 단위라 개발자 어휘로 딱 맞습니다. "~라고 볼 순 없음"은 단정을 피하는 말투라 `I wouldn't call it ...` 로 옮기면 어감이 살아납니다. 더 격식 있게는 "Since MAI-UI requires a coarse pass followed by a fine pass, it is hard to regard as optimal."

### 카드 2 — 어떤 면에서 좋은가   (내가 쓴 한글)
- 내가 쓴 한글: "duvo-eye-2는 어떤 면에서 성능이 좋은가?"   (출처: transcript:[user] auto-recipe-creator 59bde568)
- 자연스러운 영어: "What exactly makes duvo-eye-2 perform better?" / "In what ways is duvo-eye-2 better?"
- 왜 이렇게: "어떤 면에서"를 직역한 `in which aspect` 는 어색하고 `In what ways` 나 `Where does it shine?` 이 자연스럽습니다. "성능이 좋다"는 `has good performance` 보다 `perform better` 처럼 동사로 쓰는 쪽이 영어답습니다. 비교 대상(MAI-UI)이 대화에 깔려 있으니 비교급 `better` 로 받아도 됩니다. 구어로는 "So what's duvo-eye-2 actually good at?"

### 카드 3 — 비교 축을 바꿔야 한다   (고급 한글 · 번역)
- 한글 원문: "벤치가 100% 라는 건 2회 호출(coarse→fine) 기준이라, 비교 축을 정확도가 아니라 "한 번 호출로 같은 정확도가 나오는가" 로 바꿔야 합니다."   (출처: transcript:[assistant] auto-recipe-creator 59bde568)
- 자연스러운 영어: "That 100% is measured with two calls, coarse then fine. So the question isn't accuracy; it's whether a single call can reach the same accuracy."
- 번역 포인트: "비교 축"을 `comparison axis` 로 직역하면 딱딱합니다. 영어에서는 `the question is whether ...` 로 "무엇을 따져야 하는가"를 바로 말하는 편이 자연스럽습니다. "~라는 건 ~기준이라"는 한 문장에 담기 무거우니 둘로 나눴습니다. `isn't X; it's Y` 는 한국어 "X가 아니라 Y"의 정석 대응입니다.

### 카드 4 — 정확도는 그대로, 부하는 절반   (고급 한글 · 번역)
- 한글 원문: "1회 호출로 같은 정확도가 나오면 정확도는 그대로 두고 클릭당 지연과 서버 부하가 절반이 됩니다."   (출처: transcript:[assistant] auto-recipe-creator 59bde568)
- 자연스러운 영어: "If one call gets the same accuracy, we keep the accuracy and halve both per-click latency and server load."
- 번역 포인트: "절반이 됩니다"는 `become half` 보다 동사 `halve` 하나가 깔끔합니다. 한국어는 주어가 "지연과 부하"로 바뀌지만 영어에서는 주어를 `we` 로 통일해 `keep ... and halve ...` 병렬로 묶으면 리듬이 좋아집니다. "그대로 두고"는 `keep` 이나 `with no loss in accuracy` 로 처리합니다.

### 카드 5 — 엉뚱한 곳을 짚지 않는 것   (고급 한글 · 번역)
- 한글 원문: "이때 엉뚱한 곳을 짚지 않는 것이 정확도보다 중요합니다."   (출처: transcript:[assistant] auto-recipe-creator 59bde568)
- 자연스러운 영어: "Here, not clicking the wrong place matters more than raw accuracy."
- 번역 포인트: "엉뚱한 곳"은 `a random spot` 이나 `the wrong place` 로 충분합니다. 동명사 부정 `not clicking` 을 주어로 세우고 동사 `matters more than` 을 쓰면 `is more important than` 보다 짧고 구어적입니다. 정확도 앞에 `raw` 를 붙이면 "겉보기 수치로서의 정확도"라는 대비가 또렷해집니다.

### 카드 6 — 추정이라는 단서   (고급 한글 · 번역)
- 한글 원문: "학습 분포가 가깝다는 데서 끌어낸 추정입니다."   (출처: transcript:[assistant] auto-recipe-creator 59bde568)
- 자연스러운 영어: "That's an inference from the training data being closer, not a measured result."
- 번역 포인트: "~에서 끌어낸 추정"은 `an inference from ...` 가 정확합니다. `from the training data being closer` 는 동명사 앞에 의미상 주어(`the training data`)를 둔 구조입니다. 원문에는 없지만 `not a measured result` 를 덧붙이면 "추정"이라는 단서의 의도가 영어 독자에게 분명해집니다. 짧게는 "This is inferred, not measured."

## 영어 다듬기

### 카드 7 — research 의 목적어
- 내가 쓴 영어: "I want you to research about the SOTA model that might replace mai-ui that is the main vlm currently used for ARC."   (출처: transcript:[user] auto-recipe-creator 59bde568)
- 정정: `research about` → `research` (타동사라 전치사 없이 목적어를 바로 받습니다. 명사로 쓸 때만 `do research on`). `the SOTA model` → `SOTA models` (아직 어떤 모델인지 모르니 복수·무관사). `mai-ui that is the main vlm` → `MAI-UI, the main VLM` (고유명사 뒤에는 제한적 that 절이 아니라 쉼표 동격을 씁니다).
- 더 나은 표현: "Please research the current SOTA models that could replace MAI-UI, our main VLM for ARC."
- 왜: 관계절 두 개(`that might replace`, `that is the main`)가 연달아 붙어 문장이 늘어졌습니다. 두 번째를 동격 `, our main VLM for ARC` 로 줄이면 한 호흡에 읽힙니다. `currently used` 는 `current` 를 모델 쪽에 붙이면 생략해도 뜻이 유지됩니다.

### 카드 8 — 병렬 조사 지시
- 내가 쓴 영어: "go parellel research with codex (via herdr) you can ask the codex to research on the models in huggingface."   (출처: transcript:[user] auto-recipe-creator 59bde568)
- 정정: `parellel` → `parallel` (철자). `go parallel research` → `run the research in parallel` (`go` 는 목적어를 받지 못합니다). 두 문장이 쉼표·마침표 없이 붙은 run-on 이라 마침표로 끊습니다. `the codex` → `Codex` (도구 이름이라 관사 없음). `research on the models` → `research the models` (카드 7과 같은 규칙). `in huggingface` → `on Hugging Face` (플랫폼·사이트는 `on`).
- 더 나은 표현: "Run it in parallel with Codex via herdr. You can have Codex cover the models on Hugging Face."
- 왜: `have + 사람 + 동사원형` 은 "~에게 ~를 맡기다"라는 사역 표현이라 작업 분담을 지시할 때 `ask ... to` 보다 자연스럽습니다. `cover` 는 "조사 범위로 맡다"라는 뜻으로 research 반복을 피해 줍니다.
