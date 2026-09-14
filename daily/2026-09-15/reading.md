# 2026-09-15 — 정독

> 오늘 repo 문서는 전부 한국어라 정독 단락은 transcript 의 `[assistant]` 영어에서 골랐다. 세 단락 모두 원문 그대로다(단락 2 는 두 불릿을 이어 붙였고 굵은 글씨만 뺐다).

## 단락 1

Stable IDs should be content hash plus source path plus byte range, never an auto-increment. Units belong on the record, not in a lookup table nobody maintains. Quality is a small enum such as complete, truncated, parse-error, or sampled. Schema version is the parser version that produced the record. Lineage is a single parent-ID field pointing to the source record and the extractor version. That is enough. A full provenance graph is over-engineering at this stage.

**문법·구조**: 일곱 문장 중 여섯이 `X is / should be Y` 꼴의 정의문이다. 항목을 하나씩 "무엇이어야 하는가"로 못 박는 리뷰 문체라 접속사가 거의 없다. 첫 문장은 `should be … , never …` 로 권고 뒤에 금지를 붙였고, 둘째 문장은 `belong on … , not in …` 으로 전치사만 바꿔 위치를 대조한다. `a lookup table nobody maintains` 와 `the parser version that produced the record` 는 각각 접촉 관계절과 `that` 관계절로, 명사 뒤에 짧은 꼬리를 달아 문장을 늘리지 않고 정보를 더한다. `pointing to …` 는 현재분사 후치 수식이다. 여섯 문장을 쌓은 뒤 `That is enough.` 세 단어로 끊고, 마지막 문장에서 대안을 `over-engineering` 으로 분류한다. 긴 나열 → 짧은 단정 → 판정 순서가 리듬을 만든다.

**핵심 표현**: `never an auto-increment` — 명사구만으로 금지를 붙이는 압축형. / `a lookup table nobody maintains` — 방치될 구조를 접촉 관계절로 비꼰다. / `over-engineering at this stage` — 틀렸다가 아니라 지금은 이르다는 판정.

**격식 짝**: (작성)
- refined: A single parent-ID field suffices for lineage; a full provenance graph would be premature at this stage.
- plain: One parent-ID field is enough for now. A whole provenance graph is overkill.

<sub>출처: transcript:equipment-map-claude-review (architecture critique)</sub>

---

## 단락 2

The launcher waits for each model to answer /v1/models before starting the next one. On a timeout it stops the model, because models loading at the same time can use up the 16 GB of host RAM. That check can't tell a slow load from a model that's up but rejecting the check. A wrong VLLM_API_KEY or a SERVED_MODEL_NAME mismatch looks the same as "still loading" and keeps failing until the time limit. A longer timeout would only make that failure take 30 minutes instead of 15.

**문법·구조**: 현재 시제로 동작을 서술하는 설명문이다. 첫 문장은 `waits for A to do B before doing C` 로 순서를 한 문장에 담는다. 둘째 문장은 `On a timeout` 이라는 전치사구로 조건을 세우고 `because` 절로 이유를 뒤에 붙였다. 셋째 문장의 `can't tell A from B` 가 이 단락의 축이다. A 는 `a slow load` 두 단어, B 는 `a model that's up but rejecting the check` 라는 관계절 명사구로 길이가 다르지만 대칭이 유지된다. 넷째 문장은 주어에 `or` 로 두 원인을 묶고 `looks the same as … and keeps failing until …` 로 동사 둘을 이었다. 마지막 문장은 `would only make X take Y instead of Z` 가정법으로, 요청받은 수정이 근본 해결이 아님을 수치로 보여 준다.

**핵심 표현**: `can't tell a slow load from a model that's up` — 두 상태가 겉으로 같아 보인다는 진단. / `looks the same as "still loading"` — 인용부호로 로그 문구를 그대로 끌어와 비교 대상으로 삼는다. / `would only make that failure take 30 minutes instead of 15` — 요청의 부작용을 숫자로 대비.

**격식 짝**: (작성)
- refined: The readiness check cannot distinguish a genuinely slow load from a server that is up but rejecting the probe.
- plain: The check can't tell "still loading" apart from "up, but saying no."

<sub>출처: transcript:llm-serving (readiness timeout 설명)</sub>

---

## 단락 3

Whole-file download plus bounded deterministic extracts is fine. It means the unit of retention is the extract, not the file, and every record must say which approved file and which extractor produced it. The validated local LLM changes my "no LLM extraction" rule into "LLM writes only into inferred fields, with a citation to observed records." Unknown cadence is acceptable if it is stored as unknown rather than as zero gaps. Non-verbatim RAG is correct given the injection and sensitivity risk.

**문법·구조**: 앞선 비판을 새 제약에 맞춰 수정하는 단락이라, 문장마다 "받아들인다 + 단서" 구조가 반복된다. 첫 문장은 긴 명사구 주어를 단수 `is` 로 받는다. `A plus B` 를 한 덩어리로 보기 때문이다. 둘째 문장은 `It means (that) …` 으로 앞 문장의 함의를 풀고, `which approved file and which extractor` 처럼 의문사 `which` 를 두 번 써서 기록해야 할 두 가지를 나란히 세운다. 셋째 문장은 `changes A into B` 에서 A 와 B 자리에 인용부호로 묶은 규칙 문장을 통째로 넣었다. 규칙을 명사처럼 다루는 기법이다. 넷째 문장의 `stored as unknown rather than as zero gaps` 는 `as` 를 반복해 두 저장 방식을 대조한다. 마지막 문장은 `given + 명사구` 로 근거를 짧게 붙인다. `because of` 보다 격식이 높고 리뷰 문체에 잘 맞는다.

**핵심 표현**: `the unit of retention is the extract, not the file` — 시스템의 기본 단위를 정의로 굳힌다. / `stored as unknown rather than as zero gaps` — 모른다는 사실을 0 으로 위장하지 말라는 원칙. / `given the injection and sensitivity risk` — 근거를 명사구로 압축.

**격식 짝**: (작성)
- refined: Where cadence cannot be established, it should be recorded explicitly as unknown rather than represented as an absence of gaps.
- plain: If we don't know the cadence, say "unknown." Don't write it down as "no gaps."

<sub>출처: transcript:equipment-map-claude-review (architecture critique, follow-up)</sub>
