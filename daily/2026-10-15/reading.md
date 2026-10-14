# 2026-10-15 — 정독

## 단락 1

Evidence level is tagged on every finding. **[read]** = I opened the page or document and read it. **[snippet]** = the claim comes from a search-result summary of that page; the page itself was not opened, so wording and numbers should be treated as unverified. Anything I know from background but could not source in this session is placed under **Gaps**, labelled "unverified background", never under Cited Findings. Coverage is uneven. Strongest: tip wear and tip characterisation (NIST), hybrid-bonding AFM, Park NX-Wafer and Bruker InSight AFP feature lists, Gwyddion file-format support. Weakest: throughput and utilisation analytics, tool-to-tool matching practice, IRDS, SEMI standards. Those are stated as gaps, not filled in.

**문법·구조**: 규칙을 세우는 문장(`is tagged`, `is placed`, `are stated`)은 전부 현재 수동태다. 누가 하든 변하지 않는 체계라서 행위자를 지웠다. 반대로 근거를 직접 다룬 행동은 `I opened … and read it` 처럼 1인칭 과거 능동이라, "규칙"과 "내가 실제로 한 일"이 태로 갈린다. `could not source` 의 `source` 는 동사로 "출처를 대다". `Strongest: … Weakest: …` 는 동사 없이 콜론 뒤에 목록만 둔 표 같은 문장인데, 앞의 `Coverage is uneven.` 을 짧게 끊고 바로 증거를 대는 리듬이다. 마지막 `stated as gaps, not filled in` 은 `A, not B` 대조로 "비워 둔 것도 일부러다"를 못 박는다.

**핵심 표현**:
- `should be treated as unverified` — 자기 근거의 한계를 독자에게 넘기는 규칙형 수동태.
- `never under Cited Findings` — 앞 절의 동사(`is placed`)를 생략하고 `never` 로 금지 위치만 덧붙였다. 반복을 줄이는 생략 구문.
- `Coverage is uneven.` — 세 단어로 보고서 전체의 신뢰 지도를 깐다.

**격식 짝**:
- refined (작성): Findings drawn solely from search summaries should be treated as unverified.
- plain (작성): If I only saw it in a search snippet, don't take the numbers as solid.
- refined (작성): Coverage across the sections is uneven.
- plain (작성): I dug deeper on some parts than others.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md (Reading guide, 일부 생략)</sub>

---

## 단락 2

Data needed to track tip life, derived from the NIST method: per-tip identity and type or material; cumulative sites or images; periodic qualifier results; and results on a fixed monitor site. Wear rate is then the slope of qualifier width against the usage counter, fitted as two segments (run-in and steady state). Because product linewidth statistics did not reveal wear in the NIST study, product results alone are a weak tip-wear detector; a dedicated qualifier or monitor-site series is required. Probe-to-probe offset is a distinct quantity from within-tip wear. A step in a result series aligned with a tip-exchange event indicates tip-to-tip offset; a slope inside one tip's life indicates wear. Direction of bias for implementation rules: blunter tip gives lower Rq, shallower apparent depth in narrow trenches, wider apparent lines and narrower apparent trenches.

**문법·구조**: 첫 문장은 주동사가 없다. `Data needed …, derived from …:` 라는 명사구 제목 뒤에 세미콜론으로 항목을 늘어놓는 목록 문장이다. 항목 안에 이미 `and`·`or` 가 있어서 쉼표 대신 세미콜론으로 큰 구분을 지었다. `Wear rate is then …` 의 `then` 은 시간이 아니라 "그러면, 그렇게 모으면"이라는 논리 연결이다. `Because … , … ; …` 문장은 원인 → 결론 → 처방을 한 호흡에 담고, 세미콜론이 "그러니 이것이 필요하다"의 전환 역할을 한다. 다섯째 문장은 `A … indicates X; B … indicates Y` 로 구조를 똑같이 맞춘 병렬이라 두 신호(계단 vs 기울기)의 대비가 저절로 선다. `aligned with` 는 앞 명사를 꾸미는 과거분사구다(`which is aligned with` 의 축약).

**핵심 표현**:
- `the slope of X against Y` — 세로축·가로축을 말로 정의한다.
- `a weak tip-wear detector` — 지표를 탐지기로 의인화한 평가.
- `a distinct quantity from` — 섞기 쉬운 두 값을 갈라 두는 선언.

**격식 짝**:
- refined (작성): A step change coinciding with a tip exchange indicates probe-to-probe offset rather than wear.
- plain (작성): If the numbers jump right when the tip is swapped, that's the new tip, not wear.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md (§2 Inferences, 첫 항목 일부 생략)</sub>

---

## 단락 3

Both major inline vendors advertise the same core loop — host-delivered recipe, automatic tip selection and exchange, pattern-recognition site alignment, automatic analysis and report — and differ mainly in tip strategy. Neither publishes detail on cross-tool or tip-population analytics, which is where an in-house tool is least likely to duplicate vendor software. Features vendors do advertise on-tool (per-measurement analysis, per-recipe reports, tip exchange on threshold) are low-value to rebuild. Features absent from every vendor page I read — cross-tool comparison, tip-population statistics across a tool group, long-horizon trends joined with tip and tool events, correlation to other metrology — are the candidate gaps for an in-house application. No vendor documentation found describing group-level (multi-tool) dashboards or tip-population management software, so "vendors do not offer it" is an absence of evidence in public pages, not a confirmed absence.

**문법·구조**: 첫 문장은 주어 하나(`Both major inline vendors`)에 동사 둘(`advertise … and differ`)을 걸었고, 그 사이를 대시 삽입구로 길게 벌렸다. 대시 안의 목록을 지우면 뼈대가 "둘 다 같은 루프를 광고하고, 팁 전략에서만 다르다"로 바로 보인다. `which is where …` 는 앞 절 전체를 받는 계속적 관계절로, "바로 그 지점이 ~하는 곳"이다. 셋째·넷째 문장은 `Features vendors do advertise` 와 `Features absent from every vendor page` 로 주어를 대칭으로 세웠다. 첫째에서 강조 조동사 `do` 가 "실제로 광고하는 것은"을 세게 만든다. 마지막 문장(원문 Gaps 항목)은 `No vendor documentation found describing …` 이 동사 없는 명사구라 문법상 미완결이다. 메모체에서 흔한 생략인데, 문장으로 쓰려면 `No vendor documentation was found that describes …` 가 된다. 결론은 `an absence of evidence …, not a confirmed absence` 로 닫아 앞의 판단에 스스로 단서를 단다.

**핵심 표현**:
- `low-value to rebuild` — build vs buy 판단을 형용사 하나로.
- `least likely to duplicate` — 사내 개발이 중복 투자가 될 가능성이 가장 낮은 곳.
- `an absence of evidence …, not a confirmed absence` — "못 찾았다"와 "없다"를 구별하는 조사 보고의 정석.

**격식 짝**:
- refined (작성): Capabilities already offered on-tool provide little return if rebuilt in-house.
- plain (작성): The vendors already do that part, so building it ourselves isn't worth it.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/afm_metrology_analytics_external.md (§6 Takeaway·Inferences·Gaps 발췌, 괄호 일부 생략)</sub>
