# 2026-09-15 — 새 표현

> 오늘 배치의 repo 문서 4건은 모두 한국어라 표현 추출 대상이 아니었다. 아래 표현은 전부 transcript 의 `[assistant]` 영어에서 골랐다.

## "fall out for free"
- 레지스터: technical, conversational
- 출처: transcript:equipment-map-claude-review (architecture critique, follow-up)
- 맥락: 설계를 이렇게 잡으면 다른 기능이 따로 구현 없이 저절로 얻어진다고 설득할 때(리뷰·설계 논의)
- 한국어: 추가 작업 없이 부수적으로 떨어져 나온다
- 설명: `fall out (of)` 는 "어떤 구조의 결과로 자연히 나온다"는 뜻이고 `for free` 가 "공짜로"를 덧붙여 강조한다. 원문은 `Two passes over an unchanged file share the hash, so dedup and change detection fall out for free.` 로, 앞에 원인(해시 공유)을 두고 `so` 뒤에 공짜로 얻는 결과 둘을 나열한다. 노트에 이미 있는 `come for free` 와 뜻은 같고, `fall out` 쪽이 "구조에서 굴러떨어진다"는 그림이 더 선명하다.
- 예문: Because the ID is content-addressed, dedup and change detection fall out for free.
- 유사어: come for free (같은 뜻, 조금 더 흔함), follow naturally from (격식·문어), you get X for nothing (구어)
- 반의어: has to be built separately / comes at a cost

## "One thing to watch:"
- 레지스터: conversational, professional
- 출처: transcript:equipment-data-map (hub-and-copies layout 보고)
- 맥락: 작업 보고를 마무리하며 부작용·주의점 하나를 덧붙일 때(채팅·PR 설명)
- 한국어: 한 가지 주의할 점은
- 설명: `One thing to + 동사` 는 "~할 것 하나"라는 명사구를 문두에 세워 콜론으로 본문을 연다. `watch` 는 여기서 "지켜보다·조심하다"다. 원문 `One thing to watch: each copy is a full clone including .git, so …` 처럼 뒤에 사실 + `so` + 결과 순으로 쓰면 경고가 훈계로 들리지 않는다. 같은 틀로 `One thing to note:`, `One thing to flag:` 도 자주 쓴다.
- 예문: One thing to watch: each copy is a full clone, so a merge must be run in every folder separately.
- 유사어: one caveat (격식·짧음), heads-up (구어), worth noting (문어)
- 반의어: nothing to worry about

## "sufficient until proven otherwise"
- 레지스터: professional
- 출처: transcript:equipment-map-claude-review (architecture critique)
- 맥락: 지금 방식으로 충분하니 더 복잡한 대안은 필요가 증명될 때까지 미루자고 할 때(설계 리뷰·문어)
- 한국어: 반대가 입증되기 전까지는 충분하다
- 설명: `until proven otherwise` 는 법률 표현 `innocent until proven guilty` 를 빌린 꼴이다. `proven` 뒤에 `to be insufficient` 를 다 쓰지 않고 `otherwise` 한 단어로 받아 짧다. 원문은 `Streaming ingestion. Batch on file change is sufficient until proven otherwise.` 로, 과잉 설계 목록에서 "지금은 배치로 충분"이라는 판단을 단정하되 뒤집힐 여지를 남긴다.
- 예문: Batch processing on file change is sufficient until proven otherwise.
- 유사어: good enough for now (구어), adequate for the current scale (격식), YAGNI (개발 은어)
- 반의어: already shown to be insufficient

## "A and B are different things."
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt (npm deprecation 질문 답변)
- 맥락: 상대가 두 개념을 섞어 걱정할 때 그 둘이 별개임을 한 문장으로 못 박을 때(구어·설명)
- 한국어: A 와 B 는 다른 문제다
- 설명: 원문 `"Deprecated" and "vulnerable" are different things.` 는 두 단어를 인용부호로 묶어 주어로 세우고 `are different things` 로 닫는다. `different` 만 쓰면 "다르다"에 그치지만 `things` 를 붙이면 "아예 다른 종류의 문제"라는 어감이 된다. 이 문장 뒤에 각 개념의 정의를 한 문장씩 붙이는 것이 정형이다.
- 예문: "Deprecated" and "vulnerable" are different things, and only the second one needs action.
- 유사어: not the same thing (부정형·구어), two separate concerns (격식), conflating A with B (섞는 쪽을 지적하는 표현)
- 반의어: one and the same

## "just to hide a warning"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt (npm deprecation 질문 답변)
- 맥락: 사소한 이득을 위해 큰 위험을 지는 선택을 말릴 때(구어·코드 리뷰)
- 한국어: 고작 경고 하나 없애자고
- 설명: `just to + 동사` 는 목적이 하찮음을 깎아내리는 말투다. 원문 `forcing them risks breaking Excel export at runtime just to hide a warning` 은 앞에 위험(`risks breaking`)을 무겁게 놓고 뒤에 목적을 `just to` 로 가볍게 놓아 불균형을 드러낸다. `hide` 를 고른 것도 의도적이다. 경고를 "고치는" 게 아니라 "숨기는" 것뿐이라는 뜻이 실린다.
- 예문: Forcing a major-version override risks breaking the Excel export just to hide a warning.
- 유사어: only to silence a warning (같은 어감), for cosmetic reasons (격식), to make the log look clean (풀어쓴 구어)
- 반의어: to fix a real vulnerability

## "at the schema level, not by convention"
- 레지스터: technical, professional
- 출처: transcript:equipment-map-claude-review (architecture critique, follow-up)
- 맥락: 규칙을 "약속"이 아니라 "구조적 강제"로 만들라고 요구할 때(설계 리뷰)
- 한국어: 관례가 아니라 스키마 차원에서
- 설명: `at the X level` 은 규칙이 걸리는 층을 지정하고, `not by convention` 이 대조로 "사람들이 지키기로 한 약속"을 배제한다. 원문 `the LLM must be blocked from writing to observed fields at the schema level, not by convention` 처럼 `must be + 과거분사` 수동태 뒤에 붙으면 요구 사항의 강제력이 명확해진다. `by convention` 은 "관례상"이라는 부사구로 단독으로도 자주 쓴다.
- 예문: Enforce the rule at the schema level, not by convention, so a careless caller cannot break it.
- 유사어: enforced by the type system (구체적 변형), structurally guaranteed (격식), baked into the schema (구어)
- 반의어: by convention / on the honour system

## "a courtesy for the reader, not the ground truth"
- 레지스터: professional
- 출처: transcript:equipment-map-claude-review (architecture critique, follow-up)
- 맥락: 어떤 데이터가 참고용일 뿐 판단 근거가 아님을 선 긋을 때(설계 문서·격식)
- 한국어: 읽는 사람을 위한 편의일 뿐 진실의 원천은 아니다
- 설명: `a courtesy` 는 "호의·배려"라는 뜻으로, 있으면 좋지만 없어도 되는 것을 가리킨다. 원문 `The excerpt is a courtesy for the reader, not the ground truth.` 는 `A, not B` 대조로 발췌문의 지위를 낮춘다. `ground truth` 는 기계학습·측정에서 "기준이 되는 참값"이라는 관용어라, 이 문장은 "인용문을 근거로 삼지 말라"는 경고가 된다.
- 예문: The bounded excerpt is a courtesy for the reader, not the ground truth; the citation ID is what gets verified.
- 유사어: for convenience only (격식·짧음), a nicety (구어·가벼움), informational, not authoritative (문서체)
- 반의어: the source of truth / the authoritative record

## "It's worth doing when …, not only …"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt (npm deprecation 질문 답변)
- 맥락: 어떤 조치의 적용 조건을 좁혀 줄 때(구어 조언)
- 한국어: ~할 때는 할 만하지만 ~만으로는 아니다
- 설명: `worth doing` 은 `worth + 동명사` 꼴로 "할 가치가 있다"이며, 뒤에 `when` 절로 조건을 단다. 원문 `It's worth doing when a package is actually vulnerable, not only deprecated.` 는 `not only` 를 뒤에 붙여 "단순 deprecated 만으로는 안 한다"를 덧붙인다. `actually` 가 "진짜로"라는 강조로 앞 문장의 오해를 걷어낸다.
- 예문: An override is worth doing when a package is actually vulnerable, not only deprecated.
- 유사어: makes sense when (구어), is justified when (격식), pays off when (효과 강조)
- 반의어: not worth the trouble

## "The only ways out would be …"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt (npm deprecation 질문 답변)
- 맥락: 지금 상황에서 벗어날 선택지가 몇 개 없고 다 부담스럽다고 알려 줄 때(구어·설명)
- 한국어: 벗어날 길은 ~뿐일 것이다
- 설명: `a way out` 은 "탈출구"이며, `the only ways out` 로 복수를 쓰면 "그나마 있는 몇 가지"라는 뜻이 된다. `would be` 는 가정법으로 "굳이 하자면"이라는 거리감을 준다. 원문은 `The only ways out would be switching Excel libraries or adding overrides that force newer major versions` 로 동명사 둘을 `or` 로 잇고, 곧이어 둘 다 위험하다는 설명이 따른다.
- 예문: The only ways out would be switching libraries or forcing newer major versions under exceljs.
- 유사어: the alternatives are (중립·격식), your options are (구어), short of X, there's no fix (더 강한 어감)
- 반의어: there's an easy fix

## "over-engineering at this stage"
- 레지스터: professional
- 출처: transcript:equipment-map-claude-review (architecture critique)
- 맥락: 제안이 틀리진 않지만 지금 시점에는 과하다고 말할 때(설계 리뷰·문어)
- 한국어: 지금 단계에서는 과잉 설계다
- 설명: `over-engineering` 은 명사로 쓰여 판정 자체가 된다. `at this stage` 가 붙어 "영원히 틀렸다"가 아니라 "지금은 이르다"로 톤을 낮춘다. 원문 `A full provenance graph is over-engineering at this stage.` 는 `That is enough.` 라는 세 단어 문장 바로 뒤에 온다. 짧은 단정 뒤에 대안을 과잉으로 분류하는 흐름이다.
- 예문: A separate lineage service is over-engineering at this stage; one parent-ID field covers it.
- 유사어: premature (한 단어·격식), more than we need right now (구어), gold-plating (은어)
- 반의어: the minimum that works / under-engineered

## "structural, not a bug"
- 레지스터: professional, technical
- 출처: transcript:equipment-data-map (모델별 폴더 분리 보고)
- 맥락: 문제의 원인이 코드 실수가 아니라 구조 자체임을 진단할 때(작업 보고·리뷰)
- 한국어: 구조 문제이지 버그가 아니다
- 설명: 원문 `The interference was structural, not a bug in the letters:` 는 형용사 `structural` 과 명사구 `a bug` 를 `not` 으로 대조한다. 품사가 달라도 대조는 성립한다. 이 한 줄이 "letter 를 고쳐도 소용없다"는 결론을 미리 정당화하고, 콜론 뒤에서 세 파일이 왜 충돌했는지 근거를 푼다.
- 예문: The interference was structural, not a bug in the letters: every model wrote the same files on one branch.
- 유사어: a design problem, not an implementation error (풀어쓴 격식), by construction (수학·기술), baked into the layout (구어)
- 반의어: a one-off bug / a typo-level fix

## "a lookup table nobody maintains"
- 레지스터: conversational, professional
- 출처: transcript:equipment-map-claude-review (architecture critique)
- 맥락: 나중에 방치될 것이 뻔한 구조를 비꼬듯 지적할 때(리뷰·구어)
- 한국어: 아무도 관리 안 하는 조회 테이블
- 설명: 관계대명사 없이 `nobody maintains` 가 명사를 바로 꾸미는 접촉 관계절이다. `that nobody maintains` 보다 짧고 말맛이 산다. 원문 `Units belong on the record, not in a lookup table nobody maintains.` 는 `belong on … , not in …` 으로 위치를 대조하면서 뒤쪽 선택지에 이 꼬리를 달아 가치를 깎는다.
- 예문: Units belong on the record itself, not in a lookup table nobody maintains.
- 유사어: an orphaned table (기술 은어), a table that will rot (구어), a separately maintained mapping (중립·격식)
- 반의어: a table with a clear owner

## "a later exercise"
- 레지스터: professional
- 출처: transcript:equipment-data-map (단일 LLM 규칙 변경 보고)
- 맥락: 지금은 하지 않되 나중에 할 일임을 짧게 분류할 때(계획·보고)
- 한국어: 나중에 할 일
- 설명: `exercise` 는 여기서 "연습"이 아니라 "수행할 과제·작업"이다. 원문 `Model comparison is a later exercise on a finished process.` 는 `on a finished process` 를 붙여 "끝난 프로세스 위에서" 라는 전제 조건까지 한 문장에 담는다. `later` 가 형용사로 명사 앞에 오는 점도 눈여겨볼 만하다.
- 예문: Model comparison is a later exercise on a finished process.
- 유사어: a follow-up (구어·짧음), out of scope for now (격식), deferred (한 단어)
- 반의어: a prerequisite / first order of business

## "One assumption to flag:"
- 레지스터: professional
- 출처: transcript:equipment-data-map (문서 작성 보고)
- 맥락: 요청을 해석해 작업한 뒤, 그 해석이 틀렸을 수 있다고 미리 알릴 때(작업 보고·문어)
- 한국어: 짚어 둘 가정 하나
- 설명: `flag` 는 "표시해 두다·주의를 끌다"라는 동사다. `One thing to watch:` 와 같은 `One X to + 동사:` 틀이다. 원문은 `One assumption to flag: I read "with md files and html" as …. If you meant something else, … say so and I will extend the doc.` 로, 가정 → 해석 → 정정 요청 순서다. 보고 끝에 이 한 줄을 두면 오해가 있어도 되돌리기 쉽다.
- 예문: One assumption to flag: I read "one llm takes all" as covering both roles.
- 유사어: to be clear about what I assumed (풀어쓴 구어), caveat (한 단어), for the record (구어)
- 반의어: (마땅한 대체 표현 없음)

## "conditional on two points"
- 레지스터: professional
- 출처: transcript:equipment-map-claude-review (architecture critique, follow-up)
- 맥락: 승인하되 조건을 붙일 때(리뷰 판정·문어)
- 한국어: 두 가지를 조건으로
- 설명: `conditional on` 은 "~를 조건으로 하는"이라는 형용사구다. 원문 `Verdict: APPROVE, conditional on two points. First, …. Second, ….` 처럼 판정 뒤에 쉼표로 붙이고 다음 문장에서 `First / Second` 로 조건을 푼다. `approved with conditions` 보다 조건 개수를 먼저 말해 주어 독자가 얼마나 남았는지 안다.
- 예문: Verdict: APPROVE, conditional on two points.
- 유사어: subject to (법률·격식), with two caveats (문어·가벼움), provided that (조건절 형태)
- 반의어: unconditionally

## "X is off until Y finishes"
- 레지스터: conversational, technical
- 출처: transcript:equipment-data-map (단일 LLM 규칙 변경 보고)
- 맥락: 어떤 기능·방식을 일시 중지하고 재개 조건을 붙일 때(구어·작업 보고)
- 한국어: Y 가 끝날 때까지 X 는 꺼 둔다
- 설명: 형용사 `off` 하나로 "중단 상태"를 만든다. 원문 `parallel model folders are off until that finishes` 는 `until + 절` 로 재개 시점을 건다. `disabled` 보다 가볍고, 스위치를 껐다는 그림이라 "다시 켤 수 있다"는 뜻이 함께 실린다.
- 예문: Parallel model folders are off until the single-model run finishes.
- 유사어: on hold until (구어·격식 모두), paused (한 단어), disabled for now (기술)
- 반의어: back on / re-enabled

## "required, not optional"
- 레지스터: conversational, technical
- 출처: transcript:ghostty 설정 (Korean font 추가)
- 맥락: 상대가 "있으면 좋은 것"으로 볼 만한 것을 "없으면 안 된다"로 바로잡을 때(구어·설명)
- 한국어: 선택이 아니라 필수다
- 설명: 원문 `JetBrains Mono ships no Hangul at all, so a second font is required, not optional.` 는 근거(`ships no Hangul at all`) 뒤에 `so` 로 결론을 잇고, 끝에 `not optional` 을 덧붙여 반대 해석을 차단한다. `ship` 이 "포함해 출시하다"라는 뜻의 동사로 쓰인 점도 함께 익힐 만하다.
- 예문: A second font is required, not optional, because JetBrains Mono ships no Hangul at all.
- 유사어: a hard requirement (격식), non-negotiable (강한 구어), mandatory (한 단어·격식)
- 반의어: nice to have / optional

## "the unit of X is A, not B"
- 레지스터: professional, technical
- 출처: transcript:equipment-map-claude-review (architecture critique, follow-up)
- 맥락: 시스템이 무엇을 기본 단위로 다루는지 정의를 바로잡을 때(설계 문서·리뷰)
- 한국어: X 의 단위는 B 가 아니라 A 다
- 설명: `the unit of retention` 처럼 `the unit of + 명사` 는 "무엇을 하나로 세는가"를 묻는 틀이다. 원문 `It means the unit of retention is the extract, not the file` 은 앞 문장의 제약(파일 통째로만 내려받을 수 있음)을 받아 그 결과를 정의로 굳힌다. `not the file` 이 붙어 오해의 여지를 지운다.
- 예문: The unit of retention is the extract, not the file, so every record must name the extractor that produced it.
- 유사어: the atomic unit is (기술), we count by (구어), granularity (한 단어·격식)
- 반의어: (마땅한 대체 표현 없음)
