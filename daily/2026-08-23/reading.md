# 2026-08-23 — 정독

## 단락 1

Positives first: the mock/office formula-drift smell is *avoided* — both providers route through one `rawfiles.align_reference_images(listing)`; the fabricated 1-in-4 OM-only ratio is marked `OFFICE-VERIFY`; `docs/datatables/recipe_idp.txt` and `mock.py` changed together; no vendor path, no inline hex, `usePersistedState` untouched. `back_dev_home/ebeam/recipe_search/MIGRATION.md` not updated. Its endpoint table still reads "resolution only, no FTP", and its narrative says "No FTP happens in this endpoint. Align image names are computable … so the tool is only dialed when `/recipe-image` is asked for the bytes." The change makes `/align-images` perform an NLST round trip via `_list_raw_dirs`. CLAUDE.md defers per-feature specifics to MIGRATION.md; it now states the opposite of the code. `recipe_idp.txt` was rewritten but this doc was left contradicting it.

**문법·구조**: 이 단락은 칭찬과 지적을 **문장 형태로 갈라 놓는다**. 앞쪽 `Positives first:` 뒤는 완전한 절 하나에 세미콜론으로 네 항목을 매단 긴 문장이고, 지적으로 넘어가는 순간 `MIGRATION.md not updated.` 라는 **동사 없는 조각**으로 뚝 끊긴다. 리듬이 바뀌는 자리가 곧 태도가 바뀌는 자리다.

세미콜론이 왜 쉼표가 아닌지도 볼 만하다. 항목 안에 이미 괄호와 백틱, 쉼표(`no vendor path, no inline hex, …`)가 들어 있어서, 쉼표로 항목을 나누면 어디까지가 한 항목인지 끊어 읽을 수 없다. 항목 내부에 구두점이 있을 때 항목 사이를 세미콜론으로 올리는 것은 영어 나열의 표준 처리다.

시제는 두 층으로 나뉜다. `still reads`, `says`, `defers`, `states` 는 **문서가 지금 이 순간 무엇을 말하고 있는가**라서 현재시제다. 반면 `was rewritten`, `was left` 는 사람이 한 행위라 과거 수동태로 간다. 수동을 고른 덕에 "누가 안 고쳤냐" 를 묻지 않고도 누락 사실만 남는다. 특히 `this doc was left contradicting it` 은 `leave + 목적어 + 현재분사`(~한 채로 방치되다) 구조로, "안 고쳤다" 를 "모순된 상태로 남겨졌다" 라는 **지속 상태**로 바꿔 놓는다.

`The change makes `/align-images` perform an NLST round trip` 은 사역동사 `make + 목적어 + 원형부정사`다. 여기서 주어를 the change 로 둔 것이 논점인데, 사람이 아니라 변경 자체가 행위자가 되니 "네가 문서를 안 고쳤다" 가 아니라 "이 변경이 문서를 거짓으로 만들었다" 가 된다. `to perform` 이 아니라 `perform` 인 점도 놓치기 쉽다 — make·let·have 뒤에는 to 가 붙지 않는다.

**핵심 표현**: `route through one function` — 여러 경로가 한 함수를 거쳐 가게 만들다. 중복 구현을 막았다는 뜻을 동사 하나로 말한다. / `changed together` — 두 파일이 **같은 커밋에서** 함께 바뀌었다. 문서와 mock 이 따로 노는 흔한 결함의 반대말이라, 리뷰에서 칭찬으로 쓰인다. / `defers per-feature specifics to X` — 세부는 X 문서에 위임한다. 문서 사이의 권한 관계를 한 동사로 정리하는 표현이며, 그래서 X 가 틀리면 상위 문서까지 틀린 게 된다.

**격식 짝**:
- refined: It now states the opposite of the code. / plain: The doc says the exact opposite of what the code does now.
- refined: `recipe_idp.txt` was rewritten but this doc was left contradicting it. / plain: They updated the other doc and just forgot this one, so now the two don't match.

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md</sub>

---

## 단락 2

The altitude review found the same defect at two sites I deliberately left alone, both written up in `.scratch/align-image-404/spec.md`. `slot_sources`' listing-failure fallback derives `{stem}.jpeg`, which on HV-SEM doesn't exist (`IMMS0001-U.jpeg` does). Fixing it properly needs `tool_type` threaded through `get_param_detail`, and dropping the fallback would cost CD-SEM users images that currently load. I want evidence before making that trade. `get_align_detail` still derives names — so if a tool splits align files, `align-images` finds them and `align-detail` 404s. To tell whether #1 is live: in `/admin-logs`, filter `status: 404` and `path` containing `recipe-image`, then read `query_string`. A `name=IMMS####.jpeg` with no `-U`/`-T` suffix means the listing is degrading and #1 is your real volume problem — I'd want to know that before deciding.

**문법·구조**: 안 고친 것을 보고하는 단락이라, 문장 순서 자체가 논증이다. ①무엇을 남겼는가 → ②왜 위험한가 → ③고치면 무엇을 잃는가 → ④그래서 지금은 안 한다 → ⑤그럼 어떻게 판단하는가. 마지막에 확인 절차를 주는 덕분에, 보류가 회피가 아니라 다음 단계로 읽힌다.

`both written up in the spec` 은 `both of which are written up in the spec` 에서 관계대명사와 be 동사를 지운 **분사구 후치 수식**이다. 콤마 뒤에 이렇게 붙이면 문장을 하나 더 만들지 않고도 부가 정보를 얹을 수 있어, 기술 보고문에서 대단히 자주 쓰인다.

`which on HV-SEM doesn't exist (`IMMS0001-U.jpeg` does)` 의 괄호 안 `does` 는 `IMMS0001-U.jpeg does exist` 의 반복을 피한 **대동사**다. 앞 절이 부정이고 뒤가 긍정이라 대비가 선명해지는데, `does` 한 단어에 "없는 건 그거고 있는 건 이거" 가 다 들어간다.

`needs `tool_type` threaded through …` 는 `need + 목적어 + 과거분사` 로, "~가 …되어야 한다" 를 뜻하는 사역 수동이다(`needs to be threaded` 의 축약형). 뒤이어 `would cost CD-SEM users images that currently load` 는 cost 의 4형식 — `cost + 사람 + 잃는 것`. "사용자에게서 지금 뜨는 이미지를 빼앗는다" 를 전치사 없이 명사 둘로 붙였다.

가정법과 현재시제가 역할을 나눠 쓴다. 아직 하지 않은 선택은 `would cost`, `I'd want to know` 로 가정법이고, 지금 코드가 하는 일(`still derives`, `finds`, `404s`)과 진단 규칙(`means`)은 현재시제다. 마지막 `To tell whether #1 is live:` 는 목적을 나타내는 to 부정사를 문두로 빼고 콜론으로 절차를 여는 형태라, 명령문 나열(`filter … then read …`)이 자연스럽게 이어진다.

**핵심 표현**: `threaded through` — 값이 여러 함수 층을 거쳐 전달되게 하다. 실 꿰기 은유라, 인자를 하나 추가하는 일이 왜 번거로운지까지 함께 전한다. / `is live` — (버그·문제가) 실제로 발생 중인. `To tell whether #1 is live` 처럼 "이론상 가능" 과 "지금 벌어지는 중" 을 가르는 자리에 쓴다. / `your real volume problem` — 진짜로 양을 만들어내는 원인. volume 이 "건수" 를 뜻해서, 심각도가 아니라 발생량 기준으로 우선순위를 매긴다는 뜻이 된다.

**격식 짝**:
- refined: I want evidence before making that trade. / plain: I'd rather see it actually happening before we pay that price.
- refined: A `name` with no suffix means the listing is degrading. / plain: If the name comes through with no suffix, the listing is quietly failing.

<sub>출처: transcript:[assistant] (skewnono-v3-nuxt, align-404 마무리 보고)</sub>

