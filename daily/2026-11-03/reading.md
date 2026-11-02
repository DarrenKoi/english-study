# 2026-11-03 — 정독

## 단락 1

Implement one feature in the SKEWNONO repo: surface, as DISPLAY-ONLY axes in the skewvoir analysis workspace, the measurement-quality and execution signals that already arrive in the API responses but are thrown away. Skewvoir's stated purpose is to connect measurement results, tool state, and measurement execution / data-quality information, but its views lean on CD values and FDC. Meanwhile every measurement row already carries the tool's own quality scores and alignment offsets, and every history row carries start/end/measurement time — and almost nothing reads them. When a CD value moves, the first question is "did the measurement itself degrade (pattern recognition, alignment, timing) or did the wafer change?". Putting these signals beside CD lets the engineer look; it must not decide for them.

**문법·구조**: 작업 지시의 "왜" 부분인데 순서가 잘 짜여 있습니다. 첫 문장은 명령문으로 할 일을 던지고, 동사 surface 와 목적어 사이에 `as DISPLAY-ONLY axes ...` 를 끼워 넣어 조건을 먼저 박아 둡니다. 목적어가 길어서 뒤로 미룬 배치입니다. 둘째 문장은 `stated purpose ..., but ...` 로 "원래 하겠다던 것"과 "실제 모습"을 맞세웁니다. 셋째 문장은 **Meanwhile** 로 시선을 데이터 쪽으로 옮기고, 대시(—) 뒤에 `and almost nothing reads them` 을 붙여 펀치라인을 따로 떼어 냅니다. 현재시제 carries/reads 는 지금도 늘 그렇다는 사실을 말합니다. 넷째 문장의 `When ... moves` 는 습관적 조건절이고, 질문을 직접 인용해 독자를 현장에 세웁니다. 마지막 문장은 동명사 주어(Putting these signals beside CD)로 시작해 세미콜론으로 허용과 금지를 대구로 맞춥니다. 첫 문장의 `are thrown away` 수동태도 볼 만합니다. 누가 버리는지보다 값이 버려지는 처지에 초점이 갑니다.

**핵심 표현**:
- `lean on` — 다른 데 기대어 서 있다. 비판조로 쓰면 "치우쳐 있다"에 가깝습니다.
- `almost nothing reads them` — 무생물(코드)을 주어로 해 "아무도 안 쓴다"를 건조하게 말합니다.
- `lets the engineer look; it must not decide for them` — 도구의 역할 한정. them 은 성별을 정하지 않는 단수 대명사입니다.

**격식 짝**:
- refined: "These signals are presented alongside CD to inform the engineer's judgement, not to replace it." (작성)
- plain: "We just put them next to CD so people can look. The tool shouldn't make the call." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent 작업 지시 (첫 문장 + "Why" 절)</sub>

---

## 단락 2

`wafer-analysis-method-research.md` (around lines 74-81 and 521) excluded vendor scores from the JUDGEMENT path. So these axes are display-only: they must not feed `anomaly` verdicts, the 확인 필요 badge, `overviewSites`, `measurementVerdict`, the Time-Series anomaly roll-up, or any colour that means 주의/이상. No thresholds on them. Check that nothing you add flows into `utils/anomaly/*` or `utils/skewvoirAnalysis/verdict.ts`. The home mock derives FDC drift, CD movement and the quality scores from one per-MSR `health` seed, so any score↔CD relation seen at home is manufactured by the generator. Skewvoir already has a `DemoDataNote` component used for FDC pairings — find how it is triggered and show it wherever one of the new axes is plotted against CD. The score scale and the alignment offset unit are not confirmed with the office: mark them `OFFICE-VERIFY` in code comments where you rely on an assumption, and do not write a unit on screen that the docs do not state.

**문법·구조**: 제약 조건 세 개를 이어 붙인 단락입니다(원문은 글머리표 세 개이고 경로 일부는 줄였습니다). 패턴이 반복됩니다. 먼저 과거시제로 **사실**을 놓고(excluded, 이미 내려진 결정), `So` 나 `so` 로 **귀결**을 잇고, 명령문으로 **행동**을 지시합니다. 콜론(:)이 두 번 나오는데 둘 다 "앞 문장을 풀면 이렇다"는 뜻입니다. `No thresholds on them.` 은 동사가 없는 조각문인데, 규칙 목록에서는 이렇게 짧게 끊어야 금지가 단호하게 들립니다. `any score↔CD relation seen at home` 은 과거분사 seen 이 뒤에서 명사를 꾸미는 구조로, which is seen 이 줄어든 꼴입니다. 마지막 문장의 `where you rely on an assumption` 과 `that the docs do not state` 는 둘 다 범위를 좁히는 절입니다. 앞은 "그런 곳에서만", 뒤는 "문서에 없는 단위만"이라는 조건을 붙입니다.

**핵심 표현**:
- `must not feed X` — 값이 X 의 입력으로 흘러 들어가면 안 된다. feed 를 데이터 흐름 동사로 씁니다.
- `flows into` — 코드·값이 어디로 흘러가는지. 의존 경로를 물을 때 씁니다.
- `manufactured by the generator` — 실재가 아니라 생성기가 지어낸 상관관계.

**격식 짝**:
- refined: "Any correlation observed in the home environment is an artefact of the data generator and should not be interpreted." (작성)
- plain: "Whatever link you see at home, the mock made it up. Don't read anything into it." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 466cd9af subagent 작업 지시 ("Hard constraints" 글머리표 1~3 이어 붙임)</sub>

---

## 단락 3

B cannot distinguish empty from failed. Both produce zero rows and enter `missing`, contradicting spec:71. Add a per-recipe status manifest. Recipe identity/selection is underspecified. Join at least by family plus recipe; confirm fab/device scope. Q10B needs a variant-selection policy. IDP currently selects highest version, then newest modified. Result-derived parameters need one coherent recipe/run identity, avoiding mixed observations.

**문법·구조**: 리뷰 보고의 전형적인 압축체입니다. 각 항목이 **진단 → 근거 → 처방** 순서로 갑니다. 첫 문장은 현재시제 진단(cannot distinguish), 둘째 문장이 근거이고, `contradicting spec:71` 처럼 분사구문으로 "그 결과 명세와 어긋난다"를 덧붙입니다. 접속사 없이 붙인 분사가 결과를 나타내는 용법입니다. 셋째 문장은 명령문 처방입니다. 둘째 항목도 진단(is underspecified) 다음에 세미콜론으로 처방 두 개(Join ...; confirm ...)를 묶습니다. `highest version, then newest modified` 는 정렬 우선순위를 then 하나로 표현합니다. 마지막 문장의 `avoiding mixed observations` 도 분사구문인데 여기서는 "그렇게 해서 ~을 피하다"라는 목적·효과를 나타냅니다. 관사가 거의 빠진 것도 보고서 압축체의 특징입니다.

**핵심 표현**:
- `cannot distinguish A from B` — 구조가 두 상태를 구별하지 못한다는 무생물 주어 지적.
- `underspecified` — 틀렸다가 아니라 "덜 정해졌다"는 부드러운 지적.
- `X, then Y` — 1순위 X, 동률이면 Y. 정렬 규칙을 말할 때 씁니다.

**격식 짝**:
- refined: "The current design conflates two distinct states, an empty recipe and a failed extraction, and therefore contradicts the specification." (작성)
- plain: "Right now you can't tell 'zero params' from 'it broke' — both just show nothing." (작성)

<sub>출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고 "WRONG / AMBIGUOUS" 글머리표 1~2, 링크 생략)</sub>
