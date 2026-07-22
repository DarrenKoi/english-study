# 2026-07-23 — 정독

## 단락 1

The single fact *"this feature is wired to office"* is currently recorded three times, on two machines, in two version-control states. Three records means three chances to disagree, and the burden grows linearly with feature count — 21 features today, 21 commented lines in `.env.example`. The third record is the worst: promoting a feature requires a commit from the *home* side asserting something only the *office* side can know. `OFFICE_READY` is a cache, in git, of a fact that lives on another machine's filesystem. That is why it goes stale. Presence detection collapses all three into one: the `cp` that creates the adapter is the same act that switches it on.

**문법·구조**: 첫 문장의 뼈대는 `is recorded` 수동태 하나인데, 뒤에 부사구 셋(`three times / on two machines / in two version-control states`)을 쉼표로 나란히 답니다. 횟수 → 장소 → 상태 순으로 층이 넓어지면서 "같은 사실이 세 겹으로 흩어져 있다"는 그림이 문장 형태 자체로 그려집니다. `Three records means`는 복수 주어에 단수 동사를 붙인 것 — 세 개를 하나의 개념 덩어리로 묶어 받는 용법이라 오류가 아닙니다.

넷째 문장의 `a cache, in git, of a fact that lives on...`이 이 단락의 핵심 기교입니다. 원래 `a cache of a fact`가 한 덩어리인데 그 사이에 `in git`을 삽입해, 캐시가 **어디에** 있는지를 먼저 때려 박습니다. 삽입구를 빼면 "git 안에 캐시가 있다"는 사실이 문장 끝으로 밀려 힘을 잃습니다. 이어지는 `That is why it goes stale.`은 짧은 단문 — 긴 문장 뒤에 판결을 한 줄로 내려놓는 리듬입니다.

마지막 문장의 콜론(`:`)은 앞을 요약이 아니라 **정의**로 받습니다. 콜론 뒤 `the same act that switches it on`에서 관계절이 `act`를 한정해, 두 행동이 별개가 아니라 하나임을 못 박습니다.

**핵심 표현**: `three chances to disagree` — 기록이 셋이면 어긋날 기회도 셋이라는 계산을 명사구로 압축했습니다. `go stale`은 캐시가 낡는다는 기술 용어지만 여기서는 문서·목록이 현실과 어긋나는 상태 전반에 씁니다. `collapse A into B`는 여럿을 하나로 접어 넣는다는 뜻으로, 리팩터링 제안에서 반복해 쓸 만합니다.

**격식 짝**:

- refined: `The burden grows linearly with feature count.` / plain: `The more pages we add, the more of this bookkeeping there is.`
- refined: `Presence detection collapses all three into one.` / plain: `With presence detection you only do the one thing.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-22-provider-presence-detection-design.md</sub>

---

## 단락 2

`providers/office.py` is gitignored and only ever appears because someone deliberately ran `cp office_example.py office.py` while wiring a feature at the office. Its existence IS the migration record, so nothing else has to track readiness: no env var per feature, and no tracked set that the home side would have to commit and push about a file it cannot see. This mirrors what the app factory already does for blueprints: glob to discover, assert the hits are well-formed, fail at boot rather than at request time. Kept deliberately free of any `os.environ` access — everything env-related lives in `data_provider.py`, which imports this module. Splitting them that way is what keeps the two free of a circular import.

**문법·구조**: `only ever appears`는 부사 두 개를 겹쳐 "이것 말고 다른 경로로는 절대 생기지 않는다"까지 밀어붙입니다. `only appears`만 쓰면 "주로 그렇다"로 읽히고, `ever`가 예외 없음을 봉합니다.

둘째 문장의 `no tracked set that the home side would have to commit and push about a file it cannot see`는 관계절이 두 겹입니다. `that ... commit and push`가 `set`을 한정하고, 그 안에서 다시 `a file it cannot see`(관계대명사 that/which 생략)가 붙습니다. 조동사 `would`가 중요한데 — 이건 실제로 존재하는 부담이 아니라 **이 설계가 없앤, 가정된 부담**이라 가정법으로 씁니다. `has to`로 썼다면 지금도 그렇게 하고 있다는 뜻이 됩니다.

셋째 문장 콜론 뒤는 동사원형 셋(`glob / assert / fail`)의 병렬입니다. 주어를 지운 명령형 나열이라 절차가 규칙처럼 읽힙니다. 마지막 문장은 `Splitting them that way is what keeps...` 형태의 유사분열문(pseudo-cleft) — 동명사 주어를 세우고 `is what`으로 받아, "왜 굳이 나눴는가"라는 물음에 정면으로 답하는 자리를 만듭니다.

**핵심 표현**: `Its existence IS the record` — be 동사를 대문자로 강조해 "존재 자체가 곧 기록"이라는 등식을 세웁니다. 문서·주석에서 아껴 쓰면 효과가 큽니다. `fail at boot rather than at request time`은 실패 시점을 앞당기는 설계 원칙을 두 전치사구 대비로 표현합니다. `kept deliberately free of ~`는 "일부러 ~를 넣지 않았다"를 수동 분사로 여는 docstring 관용구.

**격식 짝**:

- refined: `Kept deliberately free of any os.environ access.` / plain: `This file never touches env vars on purpose.`
- refined: `Fail at boot rather than at request time.` / plain: `Break on startup, not when someone loads the page.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-22-provider-presence-detection.md (`office_registry.py` docstring)</sub>

---

## 단락 3

`get_hardware_service()` dispatches only the `fdc` service for `cdsem`. Requests for every other service, and FDC requests for `hvsem`, raise a clear `NotImplementedError`. This is intentional: office mode must not silently return mock or placeholder data for tabs whose real source is not connected. When `eqp_id` is `None`, the adapter does not contact OpenSearch. It returns an available-but-empty FDC payload with the existing equipment-selection hint, empty cards, and empty tables. When an equipment ID is present, the adapter queries OpenSearch and wraps the result with the existing `docs_payload()` normalizer. A selected tool with no matching documents is a valid empty result: `available` remains true, `doc_count` is zero, and `docs` is an empty list.

**문법·구조**: 처음부터 끝까지 **현재 시제 단순형**입니다(`dispatches, raise, returns, queries`). 명세서 영어의 기본값인데, 이유가 있습니다 — 과거형은 일어난 일을, `will`은 예정을 말하지만, 현재 단순형은 "언제나 그러한 규칙"을 말합니다. 계약을 기술하는 문서는 전부 이 시제로 통일합니다.

금지는 `must not`으로만 씁니다. `should not`은 권고, `cannot`은 능력의 부재고, `must not`이 규범적 금지입니다. 바로 뒤 `whose real source is not connected`에서 관계대명사 `whose`가 사람이 아닌 `tabs`를 받는 점도 눈여겨볼 만합니다 — `of which the real source`는 딱딱해서 실무 문서에서는 거의 `whose`를 씁니다.

`When A, ... When B, ...` 두 문장이 대칭으로 놓여 분기 두 개를 그대로 보여 줍니다. if 대신 when 을 쓴 이유는, 이 조건들이 "혹시 일어날 수도 있는 일"이 아니라 **반드시 둘 중 하나로 들어오는 정상 입력**이기 때문입니다. `available-but-empty`처럼 하이픈으로 묶은 임시 형용사는 명사 앞에서만 성립하고, 서술 자리에서는 `available but empty`로 풀어 씁니다.

**핵심 표현**: `This is intentional:` — 이상해 보이는 동작 뒤에 붙여 "실수 아님"을 선언하는 문장. 리뷰에서 오해를 미리 막습니다. `a valid empty result`는 "빈 결과지만 정상"이라는 판정으로, 오류와 공집합을 가르는 이 한 마디가 API 설계 논의의 절반을 정리합니다. `silently return placeholder data`는 조용한 실패를 가리키는 정형 표현.

**격식 짝**:

- refined: `Office mode must not silently return placeholder data.` / plain: `In office mode we can't just hand back fake numbers without saying so.`
- refined: `A selected tool with no matching documents is a valid empty result.` / plain: `If the tool has nothing in range, that's fine — it's empty, not broken.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-22-hardware-fdc-office-adapter-design.md</sub>
