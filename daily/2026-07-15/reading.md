# 2026-07-15 — 정독

---

## 단락 1

This is one atomic change: you cannot half-migrate a type. Flipping `cd_value` to `number | null` makes `npm run typecheck` enumerate *every* consumer that was silently reading fabricated values — the compiler produces the worklist. The gate is what makes it green again. Do not "fix" the type errors with `?? 0` or `!`. A zero is not a missing measurement; it is a measurement of zero, and it would poison exactly the averages this whole plan exists to clean. Every site must either drop the row or explicitly handle null.

**문법·구조**:
- **콜론(`:`)의 논증 기능** — `This is one atomic change: you cannot half-migrate a type.` 콜론 앞은 **주장**, 뒤는 **근거**입니다. 영어 기술 문서에서 콜론은 "즉, 왜냐하면"을 대신하는 가장 경제적인 연결 장치입니다. `because` 를 쓰면 문장이 늘어지는데, 콜론은 두 절을 대등하게 붙여 힘이 실립니다.
- **사역동사 `make` + 원형부정사** — `makes ... enumerate`. `make A do B` = "A가 B하게 만들다". 여기서 주어가 사람이 아니라 **행위(Flipping)** 라는 점이 핵심입니다. 무생물 주어가 사람/도구를 움직이게 만드는 이 구조는 영어 논증문의 뼈대입니다. 한국어로 직역하면 어색하니("타입을 뒤집는 것이 컴파일러를 열거하게 만든다"), **"타입만 바꾸면 컴파일러가 알아서 훑는다"** 로 이해하세요.
- **대시(`—`)의 결론 제시** — 앞 절을 다 말한 뒤 대시로 **한 줄 요약**을 던집니다. `the compiler produces the worklist.` 긴 설명을 짧은 명제로 착지시키는 리듬입니다.
- **세미콜론(`;`)의 대조** — `A zero is not a missing measurement; it is a measurement of zero`. 세미콜론은 **"아니라 ~다"** 의 정정 대비를 접속사 없이 잇습니다. `but` 을 쓰는 것보다 차갑고 단정적입니다.
- **관계절의 시제 선택** — `every consumer that was silently reading fabricated values` 에서 과거진행(`was reading`)을 쓴 이유: 그 소비자들이 **지금까지 계속·습관적으로** 그러고 있었다는 지속성을 담기 위함입니다. 단순과거 `read` 였다면 일회성 사건처럼 들립니다.
- **명령문 + 조동사 must** — 마지막 문장 `Every site must either drop the row or explicitly handle null.` `either A or B` 로 **선택지를 둘로 닫아버립니다**. "세 번째 길은 없다"는 뜻이죠. 설계 문서가 구현자의 재량을 통제하는 전형적 문형입니다.

**핵심 표현**:
- `you cannot half-migrate a type` — 쪼갤 수 없는 원자적 변경임을 못 박는 말. `half-` + 동사 조어법.
- `the compiler produces the worklist` — "할 일 목록을 컴파일러가 만들어 준다". 타입 시스템을 **작업 발견 도구**로 쓰는 사고방식이 이 한 구절에 압축돼 있습니다.
- `it would poison exactly the averages this whole plan exists to clean` — `poison`(오염시키다)이라는 강한 동사 + `this whole plan exists to clean`(이 계획이 존재하는 이유인 바로 그 평균) 이라는 관계절. **"고치려는 그것을 도리어 망친다"** 는 아이러니를 한 문장에 담았습니다.

**격식 짝**:

| refined (문어·설계 문서) | plain (회화·구두 설명) |
| --- | --- |
| This is one atomic change: you cannot half-migrate a type. | We have to do this in one go — there's no half-way version. |
| A zero is not a missing measurement; it is a measurement of zero. | Zero isn't "no data." Zero means we actually measured zero. |

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md</sub>

---

## 단락 2

A 50% breakdown point protects the center and scale only while contamination remains below the estimator's tolerance. If most compatible peers move together, median/MAD will describe the shifted regime as typical. That is why frozen-baseline temporal evidence is a separate detector rather than another peer score. Median/MAD is also not automatically probability-calibrated for skewed, multimodal, or mixed-regime cohorts. Positive skewed measures may use a declared log transform, followed by the same transparent calculation; NIST recommends transformation when an approximately lognormal model is appropriate. A transform must be part of the versioned detector configuration and shown in the explanation. Do not rely on empirical outer quantiles as a small-cohort escape hatch. Distribution-free tail coverage is data-hungry: NIST's min/max tolerance example needs 46 observations to cover 90% of an unknown distribution with 95% confidence, and 473 for 99% coverage at the same confidence.

**문법·구조**:
- **`only while` — 조건의 범위를 좁히는 부사절** — `protects ... only while contamination remains below ...`. `only` 를 `while` 앞에 놓아 **"오직 ~하는 동안에만"** 이라는 한계를 문장 한가운데에 심습니다. 학술 영어의 전형적 **hedging(단정 회피)** 기법입니다. `protects the center` 만 썼다면 과잉 주장이 되지만, `only while ~` 이 붙는 순간 정직한 명제가 됩니다.
- **`That is why ~` — 앞 문장 전체를 받는 지시** — `That` 이 가리키는 것은 명사 하나가 아니라 **앞 두 문장의 상황 전체**입니다. 영어 논증문에서 문단의 허리를 접는 장치로, "그래서 ~인 것이다" 하고 **설계 결정을 정당화**합니다.
- **과거분사구의 후치 수식** — `followed by the same transparent calculation`. 앞의 `a declared log transform` 을 뒤에서 수식합니다. 관계절(`which is followed by ~`)로 풀 수도 있지만, 분사구가 **더 짧고 격식** 있습니다.
- **수동태의 의도적 사용** — `A transform must be part of ... and shown in the explanation.` 행위자(누가 보여주는가)를 **일부러 감춥니다**. 규범(norm)을 서술할 때 수동태는 "누가 하든 반드시 그래야 한다"는 **비인칭적 강제력**을 만듭니다. 능동태 `You must show the transform` 이었다면 특정 구현자에게만 하는 말처럼 좁아집니다.
- **콜론 + 숫자 = 증거 제시** — `is data-hungry: NIST's ... example needs 46 observations ...`. 형용사(`data-hungry`)로 주장하고, 콜론 뒤에 **구체적 수치**를 던져 반박 불가능하게 만듭니다. `46` 과 `473` 의 대비가 논증의 펀치라인입니다.
- **명령문의 등장** — 학술적 서술문이 이어지다가 `Do not rely on ...` 로 갑자기 명령문이 나옵니다. **분석에서 정책으로 넘어가는 전환점**을 문형 자체로 표시한 것입니다.

**핵심 표현**:
- `contamination remains below the estimator's tolerance` — "오염이 추정기의 허용치 아래에 머무는 동안". `tolerance` 는 "관용"이 아니라 **"견딜 수 있는 한계치"** 입니다.
- `an escape hatch` — 원래 "비상 탈출구". 비유적으로 **"곤란할 때 빠져나가는 편법"**. `as a small-cohort escape hatch` = "표본이 적을 때 대충 둘러대는 수단으로".
- `data-hungry` — `-hungry` 접미사로 "~를 많이 요구하는"을 만드는 조어법.

**격식 짝**:

| refined (문어·연구 노트) | plain (회화·동료에게 설명) |
| --- | --- |
| Do not rely on empirical outer quantiles as a small-cohort escape hatch. | Don't reach for tail quantiles just because the sample is small — that's a cop-out. |
| Distribution-free tail coverage is data-hungry. | You'd need a mountain of data before that number means anything. |

<sub>출처: repo:skewnono_v3_nuxt docs/issues/skewvoir/msr-review-detection-research.md</sub>

---

## 단락 3

The three-way consistency is tight: `config.py`, `__init__.py`, and `CLAUDE.md` all tell the same story from their respective vantage points — field-level comment, module-level constant comment, human-facing architecture doc — without contradicting each other. The `config.py` rewrite preserves the full rationale while cleanly adding the msr-offline distinction; no information is accidentally dropped from the old comment. The insertion point in `CLAUDE.md` is well-chosen: immediately after the directory-tree code block, it contextualizes what the three subdirs mean at runtime before the reader moves on to the operational notes. The commit is scoped exactly to the three files; no stray staged files. The one minor phrasing nit does not affect correctness.

**문법·구조**:
- **평가문의 기본형: `X is 형용사: 근거`** — `The three-way consistency is tight: ...`. 리뷰·평가 글은 **판정을 먼저, 근거를 나중에** 놓습니다. 한국어 글쓰기 습관(근거 → 결론)과 정반대라 의식적으로 연습해야 하는 순서입니다.
- **대시 삽입구(`— ... —`)로 목록 끼워넣기** — `from their respective vantage points — field-level comment, module-level constant comment, human-facing architecture doc — without contradicting each other`. 괄호보다 **눈에 띄게**, 콤마보다 **경계가 분명하게** 세 항목을 문장 중간에 삽입했습니다. 삽입구를 걷어내도 `from their respective vantage points without contradicting each other` 로 문장이 온전히 남는지 확인하는 것이 대시 사용의 검증법입니다.
- **부사의 위치가 뉘앙스를 바꾼다** — `while cleanly adding the msr-offline distinction`. `cleanly` 를 동명사 앞에 놓아 **"깔끔하게 추가했다"**는 방식(manner)을 강조합니다. `adding the distinction cleanly` 로 뒤에 놓으면 강조가 약해집니다.
- **`no + 명사` 무동사 문장** — `no stray staged files.` / `no information is accidentally dropped`. 앞 절을 세미콜론으로 잇고 **동사 없이 명사구만** 던지는 압축 문형입니다. 체크리스트를 훑는 듯한 리듬을 만들어, 리뷰 문서 특유의 **건조한 확신**을 줍니다.
- **완곡한 부정: `does not affect correctness`** — 지적을 하되 즉시 그 무게를 깎아줍니다. `The one minor phrasing nit does not affect correctness.` 리뷰에서 **"고치면 좋지만 막을 일은 아니다"**를 표현하는 표준 문장입니다.

**핵심 표현**:
- `from their respective vantage points` — "각자의 위치·층위에서". 세 파일이 **서로 다른 추상 레벨**에서 같은 사실을 말한다는 칭찬.
- `is well-chosen` — "(위치·표현이) 잘 골라졌다". 사람이 아니라 **선택 자체**를 칭찬하는 수동태라 담백하고 프로답습니다.
- `a nit` — "사소한 트집". `nitpick`(하찮은 것까지 따지다)에서 온 말로, 리뷰에서 **"이건 진짜 별거 아닌데요"** 하고 미리 방어막을 치는 단어입니다. `Nit:` 로 코멘트를 시작하는 관습이 널리 쓰입니다.

**격식 짝**:

| refined (문어·공식 리뷰) | plain (회화·구두 리뷰) |
| --- | --- |
| The one minor phrasing nit does not affect correctness. | It reads a bit awkwardly, but it's not wrong — I wouldn't block on it. |
| The commit is scoped exactly to the three files. | Only the three files got touched — nothing else snuck in. |

<sub>출처: transcript:[assistant] auto_recipe_creator 코드 리뷰 (원문을 정독용으로 일부 압축·연결)</sub>

---
