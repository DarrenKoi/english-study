# 2026-10-11 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 UX 패턴 조사 노트 1장의 Takeaway 에 같은 장 Inferences 의 앞 두 항목을 이어 붙였다. 단락 2는 e-beam 계측 조사 노트 8장의 Takeaway 와 Inferences 세 항목이다. 단락 3은 pm-notes 세션에서 서브에이전트가 돌려준 조사 보고의 `Where the evidence is thin` 절을 목록 그대로 옮겼다. 1은 근거에서 권고를 끌어내는 글, 2는 주장의 크기와 근거의 세기를 갈라 순위를 매기는 글, 3은 자기 보고의 약한 곳을 스스로 적는 글이다.

## 단락 1

The canonical models (Shneiderman's mantra, Pirolli & Card's foraging/sense-making loops) are frameworks and expert opinion, **not measured effects**; the hard evidence that exists says (a) dashboards built for monitoring serve far narrower needs than their users actually have, and (b) linked brushing **only helps when** the highlight is conspicuous and persistent — it is routinely overlooked or misunderstood. **The safest reading for an expert tool:** support overview → filter → detail and the reverse path (start from a known lot/tool and work outward), and make every cross-view link visibly obvious. A tool-group → tool → lot → wafer → site → image hierarchy maps directly onto Grafana's "hierarchical drill-down, directed by links" advice and onto Shneiderman's mantra, but Pirolli & Card's top-down path means engineers will **just as often** *enter* at the bottom (a known lot or wafer). Every level should **therefore** be reachable directly and should link upward as well as downward. **Because** brushing is easily missed, cross-view selection in an expert tool should be persistent (a visible "selected: tool X / lot Y" chip that stays until cleared) **rather than** hover-only, and the highlight should dim non-selected marks **rather than merely** outline selected ones.

**문법·구조**: 다섯 문장이 "근거 → 해석 → 적용 → 결론 → 세부 권고" 순서로 놓였다. 첫 문장은 세미콜론 앞에서 유명한 모델들을 `not measured effects` 로 깎아 놓고 뒤에서 `the hard evidence that exists says (a) … and (b) …` 로 실제 근거 둘을 센다. `that exists` 는 "있는 것은 적지만 그나마"라는 뜻을 싣는 제한적 관계절이다. `only helps when` 은 조건부 긍정이라 "도움이 된다"와 "안 된다" 사이를 정확히 짚는다. 둘째 문장은 주어 뒤에 동사 없이 콜론을 찍고 명령문 둘(`support …`, `make …`)을 놓았다. 메모 문체에서 "해석은 이렇다:"를 줄인 꼴이다. 셋째 문장은 `maps directly onto A and onto B, but …` 로 잘 맞는 점을 먼저 인정하고 `but` 뒤에서 빠진 경로를 꺼낸다. `means` 의 주어가 사람이 아니라 `Pirolli & Card's top-down path` 인 무생물 주어 구문이고 `will` 은 예측이 아니라 "으레 그렇게 한다"는 습성을 나타낸다. 넷째 문장의 `therefore` 는 조동사 `should` 뒤에 끼어 있다. 문두에 두는 것보다 덜 딱딱하다. 권고는 전부 `should` 로 썼고 마지막 문장에서 `rather than` 이 두 번 나와 "하지 말 것"을 함께 적는다. 두 번째는 `rather than merely outline` 처럼 동사 원형끼리 맞세운 병렬이다.

**핵심 표현**: `not measured effects` — 널리 인용되는 모델이 측정된 결과는 아니라고 선을 긋는 말. / `The safest reading for an expert tool:` — 근거가 허락하는 가장 무리 없는 해석을 내놓는 머리말. / `link upward as well as downward` — `A as well as B` 에서 새 정보는 앞쪽(upward)에 온다.

**격식 짝**: (작성)
- refined: Linked brushing is beneficial only where the highlight is both conspicuous and persistent; otherwise it tends to go unnoticed.
- plain: Brushing only works if people can actually see the highlight and it stays put. If not, they just miss it.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/analytics_ux_patterns_external.md</sub>

---

## 단락 2

Quantified productivity claims are **almost all vendor-originated** and cluster around three levers: fewer manual steps in recipe creation, fewer redundant matching runs (using images or sensor data already collected), and less tool time per measurement (lower dose, smarter sampling, virtual metrology). **I found no independent study** measuring engineer time saved or excursions caught by a metrology analytics system. Ranking **by strength of evidence rather than size of claim**: (1) image-derived tool monitoring and matching from already-collected production images — peer-reviewed, found a real bad tool, and removes dedicated matching runs; (2) per-measurement recipe/health scores as FDC — **patent-level but concrete** and needs only data the tool already reports; (3) variance-term decomposition of matching (TMP/FMP) with automatic root-cause hint — **old but fully specified**; (4) unbiased roughness/LCDU on archives — strong literature, conditional on image suitability; (5) PM prediction — **plausible, but with no** metrology-specific published validation. **The common thread in the credible results is reuse:** getting matching, health and recipe-quality signals out of data the fleet produces anyway, so the saving is tool time and engineer attention rather than a new measurement. Vendor multipliers (5–20×, >30%, >50%, 6 months) **should be reported as** marketing claims with unstated baselines; **none came with** a method or a customer-attributed dataset in what I retrieved.

**문법·구조**: 시제가 둘로 갈린다. 지금도 참인 문헌의 상태는 현재(`are`, `cluster`, `is`)로, 글쓴이가 조사한 행위는 과거(`I found`, `none came with`, `what I retrieved`)로 썼다. 이 구분 덕분에 "없다"가 아니라 "내가 찾은 범위에는 없었다"로 읽힌다. 첫 문장의 콜론 뒤 세 항목은 `fewer … steps`, `fewer … runs`, `less tool time` 으로 비교급을 맞췄다. 셀 수 있는 명사에는 `fewer`, 셀 수 없는 `time` 에는 `less` 를 쓴 점을 눈여겨본다. 둘째 문장의 `measuring … saved or … caught` 는 `study` 를 꾸미는 현재분사구이고 그 안의 `saved`, `caught` 는 과거분사가 명사 뒤에서 꾸미는 꼴이다(`time saved` = 아낀 시간). 셋째 문장은 주절 없이 분사구 `Ranking by …:` 로 시작하는 목록 머리말이다. 각 항목이 대시 뒤에 `형용사 but 형용사` 로 한 줄 평을 다는 방식이 이 단락의 볼거리다. `patent-level but concrete`, `old but fully specified`, `plausible, but with no …` 모두 약점을 먼저 말하고 `but` 뒤에 쓸모를 둔다. 순서를 뒤집으면 평가가 깎이는 쪽으로 읽힌다. 넷째 문장의 `so` 는 결과절을 이끌고 `rather than` 이 얻는 것과 얻지 않는 것을 가른다. 마지막 문장의 `should be reported as` 는 보고서 작성자에게 주는 지시를 수동태로 돌려 누구에게 하는 말인지 드러내지 않는다.

**핵심 표현**: `by strength of evidence rather than size of claim` — 주장이 큰 순서가 아니라 근거가 센 순서로. / `patent-level but concrete` — 약점과 쓸모를 `but` 하나로 묶는 한 줄 평. / `none came with a method` — `come with` 는 "~이 딸려 온다". 방법도 데이터도 붙어 있지 않았다는 말이다.

**격식 짝**: (작성)
- refined: The vendor figures should be presented as marketing claims, since none was accompanied by a stated baseline or method.
- plain: Treat the vendor numbers as marketing. None of them say what they're comparing against or how they measured it.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_metrology_analytics_external.md</sub>

---

## 단락 3

- **Module mapping (section 3)** **rests on** module and domain titles plus intro paragraphs. I did not open lecture videos or notebooks, **so depth of coverage is unverified**; for example, whether Microsoft lesson 10 covers evaluation is marked unconfirmed.
- **NVIDIA domain weights** summed to 98% **as fetched**; cause unknown.
- **University courses:** CMU 11-768 is confirmed **only from** the page's description text; Stanford CS329A only from search results.
- **OWASP Top 10 for Agentic Applications:** only publication date and site licence confirmed, not the ten items.
- **Reuse table (section 7):** the copy/adapt columns are **my reading of each licence, not a legal review**. Whether internal corporate training counts as "non-commercial" under CC BY-NC **is flagged as open**.
- **Kubernetes review counts** come from an open-source project of a very different scale; they are used **as a direction, not a number to copy**.

**문법·구조**: 여섯 항목 모두 "무엇이 / 어디까지만 확인됐나 / 그래서 어떻게 읽어야 하나"로 짜였다. 첫 항목의 `rests on` 은 "~을 근거로 삼는다"이고 다음 문장이 `I did not open …, so … is unverified` 로 한 일과 그 결과를 `so` 로 잇는다. 하지 않은 일을 능동 과거로 먼저 적으니 `unverified` 가 누구 탓인지 분명하다. `whether Microsoft lesson 10 covers evaluation` 은 명사절이 통째로 주어가 된 문장이고 다섯째 항목의 `Whether … counts as … is flagged as open` 도 같은 구조다. 결론이 안 난 물음을 주어로 세우고 `is marked unconfirmed`, `is flagged as open` 같은 수동태로 닫으면 "모른다"를 깔끔하게 기록한다. 둘째 항목의 `as fetched` 는 "가져온 그대로는"이라는 뜻의 줄임(`as it was fetched`)이고 세미콜론 뒤 `cause unknown` 은 be 동사를 뺀 메모체다. 셋째·넷째 항목은 `only from A; … only from B`, `only A confirmed, not B` 로 확인 범위를 `only` 로 좁힌다. 세미콜론 뒤에서 반복되는 동사(`is confirmed`)를 생략한 것도 본다. 마지막 두 항목은 `A, not B` 로 끝난다. 독자가 넘겨짚기 쉬운 쪽을 `not` 뒤에 적어 미리 막는 방식이다. 시제는 조사 행위가 과거(`did not open`, `summed`), 보고서의 현재 상태가 현재(`rests on`, `is marked`, `are used`)다.

**핵심 표현**: `depth of coverage is unverified` — 제목만 보고 맞춘 것이라 깊이는 확인 못 했다는 고백. / `my reading of each licence, not a legal review` — 내 해석과 전문가 검토를 가르는 면책. / `as a direction, not a number to copy` — 방향만 참고하고 숫자는 베끼지 말라는 단서.

**격식 짝**: (작성)
- refined: The mapping is based on titles and introductory text alone; the depth of coverage has therefore not been verified.
- plain: I only went by the titles and intros, so I can't say how deep each course actually goes.

<sub>출처: transcript:pm-notes (서브에이전트 조사 보고)</sub>
