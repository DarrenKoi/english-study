# 2026-08-09 — 정독

## 단락 1

`promoteRecipeSelectionsToRedis` currently matches catalog rows by bare recipe name and adopts the first matching row's fab, overwriting the entry's own fab. With the cross-fab recipe-name overlap documented in the multi-fab Phase B spec (R3 ∩ M16B ≈ 20%), a promoted OpenSearch selection can be silently rerouted: the compare body and `&fab_name=` owner-fab routing then hit the wrong fab's registry. Selection identity is the (recipe_name, fab_name) pair per spec §5, so promotion must require a pair-exact catalog hit. Only entries whose fab is unknown (`''`) may use a name-only lookup — and a non-unique name must not guess; keep the entry's own fab instead. §5 defines selection identity as the (recipe_name, fab_name) pair, and this function rewrites that identity by name-only matching. First-row-wins adoption is a silent correctness defect — no error, no log, the user just sees the wrong fab's detail/compare data. The ~20% cross-fab name overlap documented in the Phase B spec makes this a live risk, not a corner case.

**문법·구조**: 첫 문장의 주어는 함수 이름이고 술어가 `matches … and adopts …` 로 병렬입니다. 그 뒤 `overwriting the entry's own fab` 은 분사구문인데, 앞 동작의 **결과**를 덧붙이는 자리라 "그래서 덮어쓴다"로 읽힙니다 — 원인이 아니라 귀결을 붙일 때 영어가 즐겨 쓰는 꼬리입니다. 둘째 문장은 `With + 명사구` 로 조건을 얹고, 콜론 뒤에 그 조건이 만드는 구체적 경로를 놓았습니다. `can be silently rerouted` 는 수동태에 부사를 끼운 형태이며, 행위자를 지우는 것이 여기서는 정확합니다 — 경로를 바꾸는 주체가 사람이 아니라 코드니까요. 셋째 문장의 `so` 는 규범을 끌어내는 접속사이고, `must require` 의 조동사가 권고가 아니라 요구임을 못 박습니다. 넷째 문장의 대시와 세미콜론은 서로 다른 일을 합니다: 대시는 예외 규정에 단서를 덧붙이고, 세미콜론은 "추측 금지" 다음에 그 대신 할 일을 나란히 세웁니다. 마지막 문장은 `The overlap … makes this a live risk` 로 5형식을 써서, 수치가 판정을 내리는 주체가 되게 했습니다.

**핵심 표현**: `bare recipe name` — `bare` 가 "다른 식별자 없이 이름만"이라는 결함을 형용사 하나로 표시합니다. `first-row-wins` — 정책을 하이픈으로 묶어 이름 붙이는 방식이라 비판이 짧아집니다(`last-write-wins` 와 같은 계열). `no error, no log` — 동사 없는 두 명사구를 나란히 놓아 "조용한 실패"의 정의를 리듬으로 전달합니다.

**격식 짝** (작성):
- refined: Promotion must not rewrite an entry's fab on the basis of a name-only match.
- plain: Don't let the lookup swap someone's fab just because the name matched.

<sub>출처: repo:skewnono_v3_nuxt docs/tickets/multi-fab/01-promote-redis-pair-exact-fab.md (What to build 와 Why 를 문서 순서대로 이어 붙이고, `**Spec axis:**` 같은 라벨만 뗐습니다)</sub>

---

## 단락 2

`components/sk/Chip.vue`'s `.dark` override hardcodes `rgba(21, 17, 13, 0.18)` / `rgba(21, 17, 13, 0.9)` — the resolved dark value of `--sk-ink-fg` written out by hand, which the DESIGN.md token rule bans ("colors come from `--sk-*` tokens only, never inline hex"). Replace the literals with `color-mix` on `--sk-ink-fg` so future retones track the token. The identical pair is already byte-for-byte in `NavPill.vue`: extract one shared dark-chip/pill rule (a role class in `main.css`'s components layer) and make both components consume it. CLAUDE.md makes DESIGN.md the visual source of truth — "colors come from `--sk-*` tokens only, never inline hex". A hand-resolved literal of a token's current value is worse than an arbitrary hex: it looks deliberate, but freezes today's value, so the next dark-mode retone silently leaves the chip stale. The byte-identical pair in `NavPill.vue` means that retone already shotguns across two design-system components.

**문법·구조**: 첫 문장은 대시 뒤에 동격 명사구(`the resolved dark value …`)를 붙여 값이 무엇인지 설명하고, 다시 `which` 로 그 명사구 전체를 받아 금지 규정으로 잇습니다 — 대시·관계절·괄호 인용이 한 문장에 3층으로 쌓인 구조라, 각 층이 앞의 무엇을 받는지 확인하며 읽어야 합니다. 둘째·셋째 문장은 주어 없는 명령형이라 티켓의 지시부임을 형태로 알립니다. `so future retones track the token` 은 `so that` 의 that 이 생략된 목적절이고, 현재시제 `track` 이 미래 사건을 규칙처럼 서술합니다. 다섯째 문장이 이 단락의 중심인데, `A … literal is worse than an arbitrary hex` 로 비교급 판정을 먼저 내리고 콜론 뒤에서 근거를 셋으로 펼칩니다: `it looks deliberate, but freezes today's value, so … leaves the chip stale`. 대조(`but`)와 귀결(`so`)이 한 줄에 이어져, 주장에서 결론까지가 문장 하나로 닫힙니다.

**핵심 표현**: `hand-resolved` — 토큰을 손으로 계산해 박아 넣었다는 사실을 한 단어로 압축합니다(`hand-maintained`, `hand-rolled` 와 같은 조어 계열). `freezes today's value` — "지금은 맞지만 앞으로 틀린다"는 결함의 성격을 시간으로 설명합니다. `worse than an arbitrary hex` — 더 나쁜 이유가 겉보기의 의도성이라는 반직관적 논지를 비교급으로 세웁니다.

**격식 짝** (작성):
- refined: A literal that duplicates a token's present value forecloses every future retone.
- plain: Writing the token's value out by hand just means it goes stale the next time we retint.

<sub>출처: repo:skewnono_v3_nuxt docs/tickets/design-tokens/01-chip-dark-override-uses-token.md (What to build 와 Why 를 이어 붙이고 리뷰 축 라벨을 뗐습니다)</sub>

---

## 단락 3

`M16` isn't a `fab_name` — that fab exists as `M16A`/`M16B`/`M16C`. It was a **fac_id** leaking in from device-statistics. `device-statistics/index.vue` selects at fac_id grain (legitimately — `device_desc` has no `fab_name` column), but its `onMounted` did `setFab(selectedFab.value)`, pushing `'M16'` into the navigation store, which is `fab_name`-grained. `persist-fab.client.ts` then wrote it to localStorage — and its validator `^[RM]\d{1,2}[A-C]?$` accepts `M16`, since the suffix is optional. So one visit to device-statistics poisoned the app-wide fab selection permanently, surfacing as a pre-selected `M16` on the landing page. The page sets `hideFabSidebar: true` and keeps its own fab in `useDeviceStatisticsPreferences`, so that global write bought nothing.

**문법·구조**: 앞 두 문장은 현재시제(`isn't`, `exists`)로 변하지 않는 사실을 말하고, 세 번째 문장부터 과거시제(`did`, `wrote`)로 사건 서술로 넘어갑니다 — 사후 보고문에서 "규칙"과 "그날 일어난 일"을 시제로 갈라 놓는 관례입니다. 세 번째 문장이 인과 사슬의 몸통인데, 주절 뒤에 `pushing …` 분사구문으로 결과를 잇고 다시 `which is fab_name-grained` 로 그 저장소의 성질을 붙여, 원인·행위·모순을 한 문장에 담았습니다. 네 번째 문장의 `since the suffix is optional` 은 `because` 보다 가벼운 근거 표시로, 이미 아는 사실을 상기시킬 때 씁니다. 다섯째 문장은 `So` 로 시작해 사슬을 결론으로 닫고, `surfacing as …` 분사구문이 내부 원인을 사용자가 본 증상에 연결합니다. 마지막 문장의 `so that global write bought nothing` 은 "위험은 있었고 이득은 없었다"는 판정이라, 그 코드를 지워도 되는 근거가 됩니다.

**핵심 표현**: `leaking in from X` — 값이 경계를 넘어 흘러들었다는 그림이라, 누구의 잘못인지 지목하지 않고 경로만 짚습니다. `at fac_id grain` / `fab_name-grained` — 같은 개념을 명사(`grain`)와 형용사(`-grained`)로 번갈아 써서, 두 층의 단위가 다르다는 것이 문장마다 드러납니다. `poisoned … permanently` — 한 번의 방문이 남긴 상태가 계속 살아 있다는 점을 부사로 못 박습니다.

**격식 짝** (작성):
- refined: A single visit to that page committed an out-of-grain identifier to persistent storage.
- plain: One trip to that page was enough to stick the wrong fab in your browser for good.

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (M16 pre-selected 버그의 원인 보고 — "The bug" 와 "How it got there" 두 문단. 문서 경로를 인용한 한 문장만 뺐습니다)</sub>
