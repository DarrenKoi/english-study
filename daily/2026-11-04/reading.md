# 2026-11-04 — 정독

## 단락 1

Provision and VeritySEM (AMAT tool families) are now judged by per-family Redis host keys instead of v3_df_sem_avail. Rule: Provision usable iff ip_note=="data-ip confirmed"; VeritySEM usable iff present in v3_df_verity_hosts. The tool-family registry is backend/ebeam/_tool_specs.py (and frontend/app/utils/toolType.ts); read CLAUDE.md at repo root for conventions (tool family is a providers/ axis). Check whether each change sits at the right depth or is a special case layered on shared infrastructure: e.g. the frontend ToolInventoryView branching on toolType === 'provision'/'veritysem' (should the family capabilities live in toolType.ts like hasStorageView?), tool-roster deciding columns by field presence, the office adapter hardcoding _HOST_KEY_FAMILIES instead of reading _tool_specs, `available` being overwritten with data_available. Name the more general change only if it is clearly simpler and within the diff's scope. Return file, line, summary, proposed change, cost. Under 300 words.

**문법·구조**: 리뷰어에게 주는 지시문인데 **사실 → 규칙 → 위치 → 질문 → 제한 → 산출물** 순서로 흘러갑니다. 첫 문장은 현재시제 수동태 `are now judged by` 로 바뀐 판정 기준을 사실로 깔고, 둘째 줄은 `Rule:` 뒤에 동사 없는 조각 두 개를 세미콜론으로 나란히 둡니다. 규칙은 문장보다 식처럼 읽혀야 해서 be동사를 뺐습니다(iff 는 "if and only if"). 넷째 문장이 핵심인데 `Check whether A or B` 로 판단 축을 세우고, 콜론 뒤에 `e.g.` 로 의심 사례 네 개를 늘어놓습니다. 사례가 모두 **현재분사구**(branching on, deciding, hardcoding, being overwritten)라는 점을 보세요. 명사 + -ing 꼴로 "~하고 있는 X"를 만들어 문장을 다시 시작하지 않고도 사례를 이어 붙였습니다. 마지막 `being overwritten` 만 수동형인데, `available` 이 덮어씌워지는 쪽이기 때문입니다. 끝의 `only if it is clearly simpler and within the diff's scope` 는 조건 두 개로 제안의 문턱을 높이고, `Under 300 words.` 같은 조각문으로 분량을 잘라 맺습니다.

**핵심 표현**:
- `sits at the right depth or is a special case layered on shared infrastructure` — 변경이 공통 계층에 들어갔는지, 위에 덧댄 예외인지 묻는 리뷰 축.
- `instead of reading _tool_specs` — "원천을 읽는 대신 하드코딩했다"를 instead of + 동명사로.
- `within the diff's scope` — 이번 변경 범위 안으로 제안을 묶어 두는 말.

**격식 짝**:
- refined: "Please assess whether each change is implemented at the appropriate layer or merely adds a special case on top of shared infrastructure." (작성)
- plain: "Does this change live in the right place, or is it just a special case slapped on top?" (작성)

<sub>출처: transcript:skewnono_v3_nuxt 71930ffc subagent a3c93e7c (ALTITUDE 리뷰 지시 중간~끝)</sub>

---

## 단락 2

Project facts: data fetching uses useAsyncData with shared keys; /api/* is rate-limited to 50 req / 5 s per user. useEchart(el, option, opts) rebuilds the chart with notMerge whenever the option computed changes, so a chart option depending on something volatile is a full rebuild. Users are on FHD desktops. Not hunting for correctness bugs — skip those. Do not report micro-optimisations with no measurable effect at these sizes; say what size makes it matter.

Return a list of findings, each with: file, line, one-line summary, the cheaper alternative, and the concrete cost (what repeats, how often, at what data size). Only report what you verified by reading. Rank by payoff; cap at the 8 best. Keep the report under 500 words.

**문법·구조**: 앞 단락은 **배경 사실**, 뒷 단락은 **산출물 요구**로 역할을 나눴습니다. 사실은 모두 단순현재(uses, is rate-limited, rebuilds, are)로 적어 늘 참인 조건임을 보입니다. 둘째 문장은 `whenever ...` 로 조건을 걸고 `so ...` 로 귀결을 이어 "그러니 조심하라"를 명령 없이 전합니다. 셋째·넷째 문장은 길이가 확 줄어 리듬이 바뀝니다. 특히 `Not hunting for correctness bugs — skip those.` 는 주어를 뺀 조각문 + 대시 + 명령문으로, 긴 설명 사이에 짧은 금지를 박아 눈에 띄게 합니다. 다섯째 문장은 `Do not ...; say ...` 로 금지와 대안을 세미콜론 하나로 묶었습니다. 뒷 단락의 괄호 `(what repeats, how often, at what data size)` 는 간접의문 조각 세 개로 "cost" 가 무엇인지 풀어 주고, 마지막 세 문장은 모두 명령문이라 체크리스트처럼 읽힙니다.

**핵심 표현**:
- `depending on something volatile is a full rebuild` — 자주 바뀌는 값에 기대면 매번 전체 재구성이라는 경고.
- `say what size makes it matter` — 최적화 지적에 규모 기준을 달라는 요구.
- `Only report what you verified by reading.` — 추측을 빼라는 리뷰 지시의 단골 문장.

**격식 짝**:
- refined: "Please omit micro-optimisations that would have no measurable effect at the current data volumes, and indicate the scale at which each finding becomes significant." (작성)
- plain: "Skip the tiny stuff that won't make a difference here, and tell me how big the data has to get before it actually hurts." (작성)

<sub>출처: transcript:skewnono_v3_nuxt eeafaf6d subagent aa56b14d (EFFICIENCY 리뷰 지시 끝 두 단락)</sub>

---

## 단락 3

Some MAP608 measurements have no End Time at all. We will not analyze their duration, but the front end should state that the End Time is missing so nobody mistakes the gap for a bug. MAPC01 does not record Start Time or End Time in a usable place, so we will skip its analysis as well. Whether these fields are written at all depends on how each AFM tool is configured. If the duration analysis proves worth doing, the engineers can change those settings on their side. For now, we will prepare for that case and focus on the tools that already provide the data. In code, the decision should rest on whether the values are present, not on the tool's name, so a newly configured tool is picked up without any change.

**문법·구조**: 사용자가 사무실에서 보낸 12차 회신 세 줄(영어)을 한 단락으로 다듬은 모범 단락입니다. 원문은 `Since this result data is based on ...` 처럼 종속절만 떼어 문장으로 끝낸 부분이 있었는데, 여기서는 이유를 `so` 로 뒤에 붙이거나 주어절 `Whether these fields are written at all` 로 세워 완결된 문장으로 만들었습니다. 시제는 **현재(사실)** → **will(결정)** → **can/should(권한·권고)** 로 나뉩니다. 사실은 "지금 그렇다", 결정은 "우리가 이렇게 하겠다", 권고는 "이렇게 하는 게 맞다"라서 조동사만 봐도 문장의 성격이 보입니다. `prove worth doing` 은 "해 볼 가치가 있다고 드러나다"이고, 원문의 `worth of doing` 에서 of 를 뺀 정형입니다. 마지막 문장의 `rest on whether ..., not on ...` 은 판단 근거를 대비하는 구조이고, `is picked up` 은 행위자(코드)를 지운 수동태입니다.

**핵심 표현**:
- `mistake the gap for a bug` — `mistake A for B`, A 를 B 로 잘못 알다.
- `prove worth doing` — 해 볼 가치가 있다고 판명되다.
- `rest on whether X, not on Y` — 판단을 X 에 두고 Y 에 두지 않는다.

**격식 짝**:
- refined: "The decision should rest on whether the values are present, not on the identity of the tool." (작성)
- plain: "Just check if the value's there — don't hardcode tool names." (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 12차 회신 내용 기반</sub>
