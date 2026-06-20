# 2026-06-20 — 정독

## 단락 1
Feature-sliced Flask backend under `back_dev_home/ebeam/hitachi/hardware/`. The route layer (`routes.py`) parses the URL + query params and validates; the swap surface (`data.py`) selects mock vs. office provider; `providers/mock.py` dispatches per-service to faithful deterministic generators; `normalizers.py` wraps generated data into the canonical `HardwarePayload` envelope; `contracts.py` is the TypedDict source of truth; `metrics.py` is the beam_shape metric registry that the bsm generator fabricates from. Per the cross-phase principle, the home↔office swap stays isolated to `providers/`; `routes.py`/`normalizers.py`/`contracts.py` do not branch on phase.

**문법·구조**:
- **시제 — 현재 단순형(present simple)으로 시스템을 묘사**: `parses`, `selects`, `dispatches`, `wraps`, `stays isolated`, `do not branch`. 아키텍처·동작 설명은 "지금 한 번"이 아니라 "*항상 그렇게 동작한다*"는 일반 진리이므로 현재 단순형을 씁니다. 한국어 "~한다"에 해당. 절대 과거형(parsed)이나 미래형을 쓰지 않습니다.
- **세미콜론(;)으로 병렬 절을 잇기**: 각 모듈의 역할을 `A does X; B does Y; C does Z` 로 세미콜론으로 줄줄이 엮었습니다. 콤마보다 강하고 마침표보다 약한 연결로, *대등하고 밀접한 항목들*을 한 문장에 모을 때 격식 있게 쓰입니다.
- **관계절 `that the bsm generator fabricates from`**: "the metric registry **that** the bsm generator fabricates **from**" — 목적격 관계대명사 that 절이고, 전치사 from 이 절 끝에 남는(stranded) 구어·현대 영어식 배치. 격식 최상으로 쓰면 `from which the bsm generator fabricates` 가 되지만, 기술 문서에서는 끝에 두는 편이 자연스럽습니다.
- **`do not branch on phase`** — "phase 에 따라 분기하지 않는다". `branch on X` = X 값에 따라 코드 경로를 가르다. 부정문 현재형으로 *설계 원칙(불변식)* 을 못 박습니다.

**핵심 표현**:
- **the swap surface** — 구현을 바꿔 끼우는 *한 군데의 경계면*. "여기만 갈면 mock↔office 가 바뀐다"는 격리 지점.
- **source of truth** — 다른 모든 것이 참조하는 단 하나의 정본(여기선 타입 정의가 그 기준).
- **stays isolated to `providers/`** — 변경 영향이 한 폴더 안에 *갇혀 있다*. 위 표현 `blast radius` 와 짝.

**격식 짝**:
- refined: *The home/office swap stays isolated to `providers/`; the upper layers never branch on phase.* (작성)
- plain: *Only `providers/` knows about home-vs-office — nothing above it cares which one is running.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-06-19-hardware-raw-doc-mocks-plan1-backend.md</sub>

---

## 단락 2
If I prefix the timestamp onto the eqp_id folder (`20260530_133020_MCD916/...`), the captures get separated from the MES-downloaded recipe/measurement images for that same tool+recipe — they'd no longer sit side-by-side, and that tree wouldn't match workflow_2's expected layout. A cleaner way to get the same separation is a timestamped subfolder inside `captured_img_from_rcs/`, which keeps the eqp/class/recipe leaf intact and colocated.

**문법·구조**:
- **조건문 — 1형식 가정에서 2형식 결과로 이어짐**: `If I prefix … , the captures get separated …` 는 현재형 조건절 + 현재형 결과(실제·반복 사실의 1형식). 이어서 같은 결과를 `they'd no longer sit side-by-side` (= they **would** not), `that tree **wouldn't** match` 로 **would** 를 써서 *가정된 결과의 함의* 를 부드럽게 풉니다. 같은 if 의 결과를 현재형(사실)→would(가정 함의)로 옮겨 단정 톤을 누그러뜨리는 자연스러운 구어 흐름입니다.
- **em-dash(—)로 결과를 덧붙이기**: 앞 절의 귀결을 대시 뒤에서 풀어 설명. 콜론보다 가볍고 구어적입니다.
- **관계절 `which keeps … intact and colocated`**: 콤마 뒤 비제한적(non-restrictive) 관계절. 앞 명사(subfolder)에 대한 *부가 설명* 으로, "그리고 그것은 ~한다"로 자연스럽게 이어집니다. 제한적 관계절(that)과 달리 콤마+which 를 씁니다.
- **`get separated` (get-수동)**: be separated 대신 `get separated`. 구어에서 *변화·결과* 를 강조하는 수동태로, "분리되어 버린다"는 뉘앙스.

**핵심 표현**:
- **sit side-by-side** — (파일·항목이) 나란히 같은 위치에 놓여 있다. 물리적 인접·비교 가능성을 함의.
- **a cleaner way to …** — "더 깔끔한 방법은 …" — 대안을 제안하는 부드러운 도입. 단정 대신 비교급으로 권합니다.
- **keep X intact** — X 를 손대지 않고 그대로 보존하다.

**격식 짝**:
- refined: *Nesting the captures in a timestamped subfolder keeps the existing leaf intact while still separating each event.* (작성)
- plain: *Putting them in a per-event timestamp subfolder does the same thing without messing up the existing folders.* (작성)

<sub>출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (15a1d642 세션, assistant)</sub>
