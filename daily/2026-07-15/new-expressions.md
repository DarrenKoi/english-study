# 2026-07-15 — 새 표현

---

## "non-negotiable"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md
- 맥락: 설계 문서·회의에서 "이건 협상 대상이 아니다, 예외 없다"고 못 박을 때(격식·단호)
- 한국어: 타협 불가한, 반드시 지켜야 하는
- 설명: 원래 협상(negotiation) 용어인데, 기술 문서에서 **제약 조건을 절대 원칙으로 격상**시킬 때 씁니다. `must` 보다 강하고, 반박 여지를 미리 닫아버리는 뉘앙스입니다.
- 예문: Determinism is non-negotiable — the same MSR must always open to identical data.
- 유사어: mandatory (규정상 의무 — 더 사무적), a hard requirement (요구사항 문맥), set in stone (구어·비유), inviolable (문어·매우 격식)
- 반의어: negotiable (조정 가능한), nice to have (있으면 좋은 정도)

---

## "defence in depth"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md
- 맥락: 보안·검증 설계에서 "한 겹으로 안 믿고 여러 겹으로 막는다"는 방어 전략을 설명할 때(기술 격식). 미국식은 `defense in depth`
- 한국어: 다중 방어, 심층 방어
- 설명: 군사 전략에서 온 말로, **하나의 방어선이 뚫릴 것을 전제**하고 겹겹이 검사를 두는 태도입니다. "이미 백엔드가 보장하지만 프런트에서도 또 확인한다"는 중복 검증을 정당화할 때 딱입니다.
- 예문: Defence in depth: the office backend may not honour the null contract, so we check `mp_number` as well.
- 유사어: belt and braces (영국 구어 — "허리띠에 멜빵까지", 다소 유머러스), redundant checks (중립·기술), fail-safe (실패해도 안전한 쪽으로 — 결과 중심)
- 반의어: a single point of failure (한 곳만 뚫리면 끝나는 구조)

---

## "data-hungry"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/issues/skewvoir/msr-review-detection-research.md
- 맥락: 통계·ML 기법이 "쓸 만해지려면 표본이 엄청 많이 필요하다"고 경고할 때(기술 격식)
- 한국어: 데이터를 많이 잡아먹는, 표본 요구량이 큰
- 설명: `-hungry` 는 명사에 붙여 **"~를 많이 요구한다"**는 형용사를 만드는 생산적인 접미사입니다 (power-hungry, attention-hungry). 비난이 아니라 **비용을 사실적으로 지적**하는 톤입니다.
- 예문: Distribution-free tail coverage is data-hungry: it needs 473 observations for 99% coverage.
- 유사어: sample-intensive (더 학술적), expensive in terms of data (풀어 쓴 형태), it doesn't come cheap (구어)
- 반의어: data-efficient (적은 데이터로도 되는), sample-efficient

---

## "a hard floor"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/issues/skewvoir/msr-review-detection-research.md
- 맥락: "이 수치 밑으로는 절대 못 내려간다"는 **절대 하한선**을 못 박을 때(기술·격식)
- 한국어: 절대 하한선, 최소 요건
- 설명: `floor`(바닥) 자체가 하한을 뜻하고, `hard` 가 붙어 **"예외 없는"**을 더합니다. 짝이 되는 `a hard ceiling`(절대 상한)과 세트로 익히세요. `soft floor` 는 "권장 하한(넘어도 되지만 경고)".
- 예문: Require `p < n - 1` as a hard floor, and begin validation only with substantially more observations than dimensions.
- 유사어: a strict minimum (더 평이), a bright line (넘으면 안 되는 선 — 법률·정책 뉘앙스), a non-starter below that (구어적)
- 반의어: a hard ceiling (절대 상한), a soft guideline (권고 수준)

---

## "proceed silently"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/agents/domain.md
- 맥락: 에이전트·툴에게 "없으면 없는 대로 조용히 넘어가라, 굳이 언급하지 마라"고 지시할 때(기술 명령문)
- 한국어: 조용히 진행하다, 언급 없이 넘어가다
- 설명: `silently` 는 기술 영어에서 **"로그도 경고도 남기지 않고"**라는 뜻으로 매우 자주 쓰입니다. 보통은 `silently fail`(조용히 실패 — 나쁨)처럼 부정적인데, 여기서는 드물게 **의도적으로 좋은 것**입니다. 문맥이 뒤집는 좋은 예시입니다.
- 예문: If either location does not exist, proceed silently — do not flag its absence or suggest creating it.
- 유사어: carry on without comment (풀어 쓴 회화체), skip it quietly (평이), no-op (아무 동작도 안 함 — 순수 기술어)
- 반의어: flag it / surface it (드러내어 알리다), warn loudly

---

## "last write wins"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-14-skewvoir-search-design.md
- 맥락: 두 입력구가 같은 값을 건드릴 때 **누가 이기는지** 충돌 해소 규칙을 명시할 때(기술 격식)
- 한국어: 마지막에 쓴 쪽이 이긴다 (나중 쓰기 우선)
- 설명: 분산 시스템의 충돌 해소(conflict resolution) 용어가 UI 설계로 넘어온 경우입니다. 관사 없이 **명사구 통째로 굳은 표현**이라 `the last write wins` 라고 안 씁니다. 형제 표현으로 `first one wins`, `first by number wins` 가 있습니다.
- 예문: The date token and the range dropdown write the same parameter, and last write wins.
- 유사어: the latest change takes precedence (격식·풀어씀), whichever you touched most recently sticks (회화체)
- 반의어: first write wins, immutable once set (한번 정해지면 못 바꿈)

---

## "no preamble"
- 레지스터: professional
- 출처: transcript:[user] (auto_recipe_creator 리뷰 지시문)
- 맥락: 상대에게 "서론·인사 빼고 본론부터"라고 지시할 때(격식·간결). 프롬프트·업무 지시·이메일 회신 요청에 자주
- 한국어: 서두 없이, 군말 없이 바로
- 설명: `preamble` 은 본론 앞에 붙는 도입부입니다. 명령문 끝에 `— no preamble` 을 대시로 붙여 **군더더기를 금지하는 관용 패턴**입니다. `no fluff`, `no filler` 도 같은 자리에 들어갑니다.
- 예문: Begin directly with the spec-compliance verdict — no preamble.
- 유사어: get straight to the point (회화체), cut to the chase (관용구·구어), skip the pleasantries (사교적 인사 생략에 한정), without further ado (다소 격식·구식)
- 반의어: set the scene first (배경부터 깔다), ease into it

---

## "from their respective vantage points"
- 레지스터: professional
- 출처: transcript:[assistant] (코드 리뷰 Strengths 섹션)
- 맥락: 여러 문서·역할이 **각자의 위치에서** 같은 사실을 말하고 있다고 평가할 때(격식 문어)
- 한국어: 각자의 관점(위치)에서
- 설명: `vantage point` 는 원래 "전망 좋은 높은 지점"이고, 비유적으로 **"그 자리에서만 보이는 시야"**를 뜻합니다. `respective`(각자의)와 짝을 이뤄 "서로 다른 층위에서 본다"를 압축합니다. 단순한 `viewpoint`(의견)보다 **위치·층위**를 강조합니다.
- 예문: The three files all tell the same story from their respective vantage points without contradicting each other.
- 유사어: from where each of them sits (회화체), at different levels of abstraction (기술적), through different lenses (비유·저널리즘)
- 반의어: from a single point of view, in lockstep (완전히 똑같은 시각으로)

---

## "nice to have"
- 레지스터: professional, conversational
- 출처: transcript:[user] (리뷰 출력 형식 — `#### Minor (Nice to Have)`)
- 맥락: 우선순위를 나눌 때 "필수는 아니고 있으면 좋은 것"으로 분류할 때(회의·티켓·리뷰). 명사구로도 형용사구로도 씀
- 한국어: 있으면 좋은 정도(필수 아님)
- 설명: `must-have` / `should-have` / `nice-to-have` 3단계 우선순위가 실무 표준입니다. 명사로 쓸 땐 하이픈을 넣어 `a nice-to-have`, 서술로 쓸 땐 `that's nice to have` 처럼 풉니다. **거절을 부드럽게 포장**하는 정치적 기능도 큽니다.
- 예문: Renaming the variable is a nice-to-have; it should not block the merge.
- 유사어: not a blocker (병목은 아님 — 더 단호), optional (중립·건조), icing on the cake (관용구 — "금상첨화", 더 구어)
- 반의어: a must-have, a blocker, a hard requirement

---

## "no stray staged files"
- 레지스터: technical, casual
- 출처: transcript:[assistant] (코드 리뷰 Strengths 섹션)
- 맥락: 커밋 범위를 점검하며 "딴 파일이 슬쩍 끼지 않았다"고 확인할 때(리뷰·구어적 기술 문체)
- 한국어: 엉뚱하게 끼어든 스테이징 파일이 없다
- 설명: `stray` 는 원래 "길 잃은(개·고양이)"이고, 기술 문맥에서 **"의도치 않게 흘러든"**을 뜻합니다. `a stray semicolon`, `a stray console.log`, `stray whitespace` 처럼 아주 생산적으로 씁니다. 짧고 구어적이라 리뷰 코멘트에 잘 어울립니다.
- 예문: Commit is scoped exactly to the three files; no stray staged files.
- 유사어: nothing extra slipped in (회화체), no unintended changes (격식·중립), no collateral edits (다소 과장된 비유)
- 반의어: scope creep (범위가 슬금슬금 번짐)

---

## "that test was asserting the bug"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md
- 맥락: 버그를 고쳤더니 기존 테스트가 깨질 때, "그 테스트가 틀렸다"고 판정하며(기술·단호)
- 한국어: 그 테스트는 (사양이 아니라) 버그를 보증하고 있었다
- 설명: `assert` 는 테스트가 "이게 옳다"고 **주장·보증**한다는 뜻입니다. 그래서 "버그를 assert 하고 있었다"는 말은 **"그 테스트는 잘못된 동작을 정답으로 굳혀두고 있었다"**는 통렬한 진단이 됩니다. 테스트 수정을 정당화하는 가장 깔끔한 한 줄입니다.
- 예문: If an existing test fails because it hardcoded an old mean, that test was asserting the bug — update it and say so in the commit body.
- 유사어: the test was codifying the wrong behaviour (더 격식), the test baked in the bug (구어·비유), it was testing what the code did, not what it should do (풀어 설명)
- 반의어: the test caught a real regression (테스트가 진짜 회귀를 잡아냄)

---

## "invite analysis it cannot support"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md
- 맥락: 목업·시제품이 **너무 그럴듯해 보여서** 근거 없는 해석을 유발할 위험을 경고할 때(격식 문어)
- 한국어: (근거로) 감당하지 못할 분석을 불러들이다
- 설명: `invite` 를 "초대하다"가 아니라 **"(원치 않는 것을) 자초하다·유발하다"**로 쓰는 용법입니다 (`invite criticism`, `invite trouble`). 뒤에 관계절 `it cannot support`(그것이 뒷받침 못 하는)를 붙여 **"보이는 정교함과 실제 신뢰도의 괴리"**를 한 문장에 압축했습니다. 설계 문서에서 배울 만한 고급 문장입니다.
- 예문: A mock that looks meaningful invites analysis it cannot support.
- 유사어: give a false impression of rigour (풀어 씀), overpromise (약속만 크게 — 더 평이), lull people into false confidence (비유·구어)
- 반의어: be honest about its limitations, surface its own uncertainty

---

## "you cannot half-migrate a type"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-phase-a-analytical-truth.md
- 맥락: 변경을 쪼갤 수 없는 **원자적(atomic) 작업**임을 설득할 때(기술·단호)
- 한국어: 타입 마이그레이션은 절반만 할 수 없다
- 설명: `half-` 를 동사 앞에 붙여 **"어중간하게 ~하다"**를 만드는 생산적 조어입니다 (half-finish, half-understand). 여기서는 "쪼개서 커밋하자"는 반론을 **선제적으로 차단**하는 논리로 쓰였습니다.
- 예문: This is one atomic change: you cannot half-migrate a type.
- 유사어: it's all or nothing (구어·관용), it doesn't decompose (기술·격식), there's no partial state here (중립)
- 반의어: land it incrementally (점진적으로 반영하다), ship it behind a flag

---

## "will not be actioned"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/agents/triage-labels.md (`wontfix` 의 설명)
- 맥락: 이슈·요청을 **정중하지만 확정적으로 반려**할 때(사무·격식). 영국식 비즈니스 영어에서 특히 흔함
- 한국어: (조치하지 않고) 처리되지 않을 것이다
- 설명: `action` 을 **동사로** 써서 "조치하다·실행에 옮기다"라는 뜻으로 쓰는 용법입니다 (`We will action your request.`). 수동태 `be actioned` 로 쓰면 **행위자를 감춰서** 거절이 개인적 판단이 아니라 정책처럼 들리게 만듭니다 — 거절의 완충 장치입니다.
- 예문: Issues labelled `wontfix` will not be actioned, but they remain searchable for context.
- 유사어: will not be taken forward (영국 사무체), we're not going to pick this up (회화체·솔직), declined (짧고 단호)
- 반의어: will be picked up (착수될 것이다), ready for an agent

---

## "speak in terms of"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/agents/triage-labels.md
- 맥락: 어떤 집단·문서가 **특정 어휘 체계로** 사물을 지칭한다고 설명할 때(격식 문어)
- 한국어: ~라는 용어(틀)로 말하다
- 설명: `in terms of` 는 흔히 "~의 측면에서"로 배우지만, `speak/think in terms of X` 는 **"X 라는 어휘·개념 틀을 써서 사고하거나 표현한다"**는 더 깊은 뜻입니다. 용어 매핑 문서를 여는 전형적인 첫 문장입니다.
- 예문: The skills speak in terms of five canonical triage roles; this file maps those roles to our tracker's status strings.
- 유사어: use the vocabulary of (직설적), frame it as (프레이밍 강조), be couched in (문어·다소 현학적)
- 반의어: drift to synonyms (합의된 용어를 벗어나 제멋대로 바꿔 쓰다)

---

## "the implementation is wrong, not the expectation"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-14-skewvoir-search.md
- 맥락: 검증 단계에서 결과가 예상과 다를 때 **어느 쪽을 의심해야 하는지** 미리 못 박을 때(기술·단호)
- 한국어: 틀린 건 구현이지 기대값이 아니다
- 설명: `A, not B` 대비 구문으로 **책임의 방향을 고정**합니다. 계획서에 이 한 줄을 미리 박아두면, 나중에 구현자가 "테스트가 이상한 것 같은데요" 하고 기대값을 슬쩍 낮추는 것을 막습니다. **명세를 방어하는 문장**입니다.
- 예문: Expected results are stated — if one does not hold, the implementation is wrong, not the expectation.
- 유사어: don't move the goalposts (관용구·구어 — "골대를 옮기지 마라"), the spec stands (짧고 단호), fix the code, not the test (기술 격언)
- 반의어: update the expectation to match reality (기대값을 현실에 맞추다)
