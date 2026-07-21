# 2026-07-22 — 정독

## 단락 1

The default now comes from the hostname, not from `.env` — so provider lines stay commented on both machines. Nothing that syncs through git (`.env.example`, code) or gets copied between machines can flip your home environment to office. Unknown hostnames also default to mock — a new machine can never accidentally reach for office infrastructure. The office default deliberately applies only to `OFFICE_READY` features — a blanket "office" default would 500 the 16 pages whose adapters are still stubs. When you *do* want office data from home (VPN testing), that stays a deliberate act: set the one feature's var, or `SKEWNONO_SITE=office`.

**문법·구조**: 안전 설계를 설명하는 전형적 수사 — 부정 주어(Nothing that ..., can never ...)로 "무슨 일이 있어도 안 일어난다"를 강하게 못박는다. `Nothing that syncs through git ... can flip ...`은 관계절이 주어를 길게 꾸미고 조동사 can이 뒤에 오는 구조라, 우리말 어순으로 옮기면 "git으로 동기화되는 그 무엇도 ~할 수 없다". 마지막 문장의 조동사 *do*는 강조 용법 — "정말로 원할 때는"을 이탤릭 없이도 소리로 들리게 한다. `would 500 the 16 pages`처럼 HTTP 상태코드를 동사로 쓰는 것도 개발자 영어의 특징.
**핵심 표현**: reach for(무심코 손을 뻗다 — 실수로 인프라에 접근), a blanket default(일괄 적용되는 기본값), a deliberate act(의도적 행위여야만 가능).
**격식 짝**: "that stays a deliberate act" ↔ plain: "you'd have to do it on purpose" / refined(작성): "such access requires an explicit, intentional override."

<sub>출처: transcript:skewnono_v3_nuxt 1b71ccc2 (hostname 기반 site 감지 설명)</sub>

---

## 단락 2

Good catch — the cloud absolutely needs considering, because it's the one place where an unrecognized hostname silently defaulting to `mock` would be a real incident: production showing fake data. Cloud is now handled — and it needed to be, for exactly the inverse reason as home: production must never silently fall back to mock data because a VM hostname wasn't registered. The cloud check sits *after* the explicit `SKEWNONO_SITE` override but *before* hostname matching, and it's path-based rather than hostname-based deliberately — cloud hostnames are ephemeral, the deploy path isn't. Note the cloud default still respects `OFFICE_READY`, so unwired stub features serve mock in production rather than 500ing. So at the office tomorrow: register just your office PC's hostname — the cloud takes care of itself.

**문법·구조**: 첫 문장은 동명사 수동 구문 needs considering(= needs to be considered)이 핵심 — need 뒤의 동명사는 수동 의미를 갖는다. `for exactly the inverse reason as home`은 집과 클라우드의 위험이 정반대(집=실데이터 오접속, 클라우드=가짜 데이터 서빙)임을 한 구로 압축한다. `A rather than B deliberately — X are ephemeral, the isn't`처럼 대시 뒤에 근거를 축약문으로 붙이는 리듬, 그리고 `the deploy path isn't`의 동사 생략(= isn't ephemeral)이 문장을 팽팽하게 만든다.
**핵심 표현**: a real incident(실제 장애 — 가벼운 버그와 구분), fall back to(폴백하다), ephemeral(수명이 짧은 — VM·컨테이너 문맥의 단골 형용사).
**격식 짝**: "the cloud takes care of itself" ↔ refined(작성): "no manual configuration is required for the cloud environment."

<sub>출처: transcript:skewnono_v3_nuxt 1b71ccc2 (cloud 환경 site 감지 설명)</sub>

---

## 단락 3

End-of-day ritual. Distill this session into the work that is *still open* and persist it so the next session can continue without re-reading everything. You were here for the whole session — use that memory; do not re-derive it from git. The goal is a clean list of open loops, not a record of what got done. Finished work already lives in the journals and commits — do not duplicate it here. Keep the file under 25 lines — this is a launchpad, not a diary. Specific beats complete: "next: add MAD slider min/step, AnalyzePanel.vue:120" is worth more than a paragraph. Date-stamp each job with `since` so stale work is visible at a glance.

**문법·구조**: 지침 문서의 문체 — 주어 없는 명령문의 연속(Distill ..., use ..., do not duplicate ...)이 규칙의 단호함을 만든다. 문장마다 "X, not Y" 대비가 반복된다: open loops, not a record / a launchpad, not a diary — 정의를 긍정+부정 쌍으로 주면 오해의 여지가 없다. `so (that)` 목적절(so the next session can continue, so stale work is visible)이 각 규칙에 "왜"를 붙이는 것도 좋은 글쓰기 습관.
**핵심 표현**: distill A into B(A를 B로 증류하다 — 핵심만 추려내다), re-derive(이미 아는 것을 다시 도출하다 — 낭비의 뉘앙스), at a glance(한눈에).
**격식 짝**: "Specific beats complete" ↔ refined(작성): "precision should take precedence over exhaustiveness." / plain: "better one exact pointer than a full page."

<sub>출처: transcript:skewnono_v3_nuxt 1b71ccc2 (leave-office 스킬 지침, 일부 문장 발췌)</sub>
