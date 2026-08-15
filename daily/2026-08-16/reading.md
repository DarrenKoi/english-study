# 2026-08-16 — 정독

## 단락 1

"Set in exactly one place — `toOutlierDrill` line 85" only shows no adapter *assigns* `exempt`. It says nothing about passthrough. If `toViolationDrill` spreads raw records, any `exempt` key in office cap-violation payloads still fires `v-if="recipe.exempt"`. Your own constraints make this unfalsifiable from home: office DBs are unreachable. Cost of being wrong: the branch records "dead branch," a later cleanup deletes it, and a live badge silently disappears from the measurement-rules page — a page with no harness, so regression surfaces only when a human stares at it.

**문법·구조**: 반론 한 단락이 어떻게 조립되는지가 그대로 보인다. 첫 문장은 상대의 근거를 따옴표로 통째 옮겨 주어 자리에 앉히고(`"Set in exactly one place" only shows …`), 동사를 `only shows` 로 눌러 "이 근거는 여기까지"라는 선을 긋는다. 이탤릭 `assigns` 는 대비되는 짝 `passthrough` 를 예고하는 장치다. 셋째 문장의 `If …, any … still fires …` 는 조건절 + `still` 로 "그 근거를 인정해도 남는 경로"를 그린다 — `still` 이 빠지면 단순 가정이 되고, 반박의 힘이 사라진다. 마지막 문장은 콜론으로 시나리오를 열어 `records → deletes → disappears` 세 동사를 현재시제로 이어 붙였다. 미래시제(`will disappear`)를 쓰지 않은 게 요점이다 — 현재시제가 "언젠가 벌어질 일"이 아니라 "이 구조에서는 이렇게 굴러간다"로 읽히게 만든다. 끝의 `so regression surfaces only when a human stares at it` 은 `so` 로 결과를 달고 `only when` 으로 조건을 좁혀, 위험이 늦게 드러난다는 사실 하나를 마지막 자리에 남긴다.

**핵심 표현**: `says nothing about X` — 근거는 인정하되 사정거리를 자를 때. `unfalsifiable from home` — 반증 자체가 불가능하다고 못 박고, 뒤의 `from home` 이 그 범위를 정확히 한정한다. `Cost of being wrong:` — 확률 다툼을 결과 크기 다툼으로 바꾸는 콜론 구문.

**격식 짝**:
- refined: *Your own constraints make this unfalsifiable from home.* (작성)
- plain: *We just can't check that from here.* (작성)
- refined: *Regression surfaces only when a human stares at it.* (작성)
- plain: *Nobody finds out until someone happens to look.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md</sub>

---

## 단락 2

Short answer: in-memory is safe here, and it is not inherently riskier than disk. The fear that "async mixes one host's data into another host's buffer" comes from *shared mutable state*, not from memory itself. Cross-host contamination happens only if concurrent units share a destination or a stateful resource. Note that disk has the exact same risk: if two hosts write to a path keyed by filename only, they clobber each other — that is cross-host mixing, just on disk. Correctness comes from isolating the destination per host and not sharing a connection — not from the storage medium. asyncio never moves data between coroutines on its own; each task has its own stack.

**문법·구조**: 오해 하나를 해체하는 설명문의 표준 순서다. `Short answer:` 로 결론을 먼저 던지고, 두 번째 문장이 그 오해에 이름을 붙인다 — `The fear that "…" comes from A, not from B`. 여기서 `that` 은 관계대명사가 아니라 동격절을 여는 접속사라 `fear` 의 내용을 그대로 문장으로 담을 수 있고, 그래서 남의 걱정을 인용부호 안에 넣어 공정하게 옮길 수 있다. 셋째 문장의 `happens only if` 는 필요조건을 못 박는 형태다(충분조건 `if` 와 다르다). 넷째 문장 `Note that disk has the exact same risk` 는 명령형 `Note that` 으로 독자의 주의를 끌어당기고, 대시 뒤 `that is cross-host mixing, just on disk` 가 앞에서 만든 개념을 새 상황에 재적용한다 — 새 용어를 만들지 않고 있던 용어를 옮겨 쓰는 게 이 문단의 경제성이다. 다섯째 문장은 `Correctness comes from A and B — not from C` 로 원인을 재지정하며 끝을 맺고, 마지막 문장은 세미콜론으로 두 절을 붙여 근거를 한 호흡에 덧댄다.

**핵심 표현**: `not inherently riskier than X` — "본질적으로 더 위험한 건 아니다"로 과장된 우려를 낮출 때. `clobber each other` — 두 주체가 서로의 결과를 덮어써 망가뜨리다(구어에 가까운 기술 어휘). `on its own` — 누가 시키지 않는 한 스스로는 그러지 않는다.

**격식 짝**:
- refined: *The risk stems from shared mutable state, not from the storage medium.* (작성)
- plain: *It's not about memory versus disk — it's about who writes where.* (작성)

<sub>출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md</sub>
