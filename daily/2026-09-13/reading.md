# 2026-09-13 — 정독

## 단락 1

The events key remains an accumulating sorted set, pruned at `WRITER_PRUNE_SEC` (900s) and displayed at `BOARD_WINDOW_SEC` (600s). It is **not** replaced by a plain "cache the last response" value, for one reason: `get_live_alarms(fac_id)` takes no window argument, so how far back it reaches is the office API's choice, not ours. If it reports only currently active alarms, a last-response cache would drop each alarm the moment it cleared, and a 10-minute board could never be assembled. Accumulating successive snapshots into a ZSET reconstructs the board from whatever the upstream happens to report. This is safe precisely because ZSET members are canonical JSON: re-adding an event already present is a no-op. Idempotence is what allows the refresh cadence to be irregular and viewer-driven rather than a fixed schedule.

**문법·구조**: 다섯 문장이 "현상 → 반대 선택지 기각 → 그 근거 → 채택안 → 안전성 → 일반 원리" 순으로 좁혀진다. 세 번째 문장의 `If it reports …, a last-response cache **would** drop …, and a 10-minute board **could never be** assembled` 는 가정법 현재/would 조합이다. 실제로 그렇다고 단정하지 않으면서(업스트림이 뭘 주는지 모르니까) 그 경우의 결과만 확정적으로 그린다 — 설계 문서에서 기각 사유를 쓸 때 가장 자주 쓰는 시제 조합이다. 네 번째 문장은 동명사구 `Accumulating successive snapshots into a ZSET` 이 통째로 주어라서 "행위 자체"가 주인공이 된다. 마지막 문장의 `Idempotence is what allows X to be A rather than B` 는 분열문(cleft)으로, 성질 하나를 집어 올려 "이것 때문에 저게 가능하다"를 강조한다.

**핵심 표현**: `for one reason:` — 근거를 여러 개 늘어놓지 않고 하나로 못 박는 도입. 콜론 뒤에 곧바로 그 이유가 온다. / `the office API's choice, not ours` — 소유격 대조로 통제권의 소재를 한 줄에 정리한다. / `is a no-op` — "해도 아무 일도 안 일어난다", 멱등성을 설명하는 표준 어휘.

**격식 짝**: (작성)
- refined: `Idempotence is what allows the refresh cadence to be viewer-driven rather than scheduled.`
- plain: `Because adding the same event twice does nothing, we can refresh whenever someone shows up.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-live-alarm-cached-pull-design.md</sub>

---

## 단락 2

`POST param-detail` already returns the deep data, but its body requires the `locator` **and** the five `img_*` slot values. A browser has both because `recipe-detail` returned them; a script starting from a recipe name has neither. It must call `recipe-detail`, dig `locator` out of the payload, find the matching `idp_image_info` row, extract five columns, and post them back. None of that is documented. There is a third trap under both of them. A row of `idp_image_info` is one image definition, and `Para_13` legitimately appears twice in one recipe, at SEQ 4/6 and SEQ 11/15. This has already caused one silent wrong-answer bug — a cache keyed on the parameter name alone served the first row's images under the second row's heading. Any new API that returns "the parameter's detail" as a single object reproduces that bug for every caller.

**문법·구조**: 두 번째 문장의 `A browser has both …; a script … has neither.` 는 세미콜론을 축으로 삼은 대칭 구문이다. `both` / `neither` 한 쌍이 앞 문장의 두 요소를 그대로 받아, 같은 말을 반복하지 않고 대비만 남긴다. 세 번째 문장은 `call → dig → find → extract → post` 다섯 동사를 한 줄에 늘어놓아 절차의 번거로움을 형식으로 보여 준다 — 내용이 "귀찮다"이므로 문장도 길게 끌리게 둔 것. 마지막 문장의 주어는 관계절을 품은 명사구 `Any new API that returns … as a single object` 이고, 술어는 현재시제 `reproduces` 다. 미래(`will reproduce`)가 아니라 현재를 쓰면 개별 사건이 아니라 규칙으로 읽힌다.

**핵심 표현**: `has both … has neither` — 보유 여부를 한 쌍의 대명사로 정리. / `dig X out of the payload` — 중첩된 응답에서 값을 캐낸다(구어에 가까운 기술 어휘). / `a silent wrong-answer bug` — 에러도 안 나고 답만 틀리는 버그. 명사 앞에 하이픈 수식어를 겹쳐 쓰는 기술 문서 특유의 조어법.

**격식 짝**: (작성)
- refined: `Any endpoint that models a parameter as a single object reproduces the defect for every caller.`
- plain: `If a new endpoint hands back one object per parameter, everyone hits the same bug again.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-08-02-recipe-param-export-and-api-design.md</sub>

---

## 단락 3

Yes, and most of it is already built. The catalog just doesn't show it well, and one of its examples is broken. `GET /api/msr-file/download?msr=…&kind=raw|pkl` returns the original MinIO file unchanged. API tokens work on every `/api/*` path, so a notebook can call it today. Missing measurements get 404 and files past retention get 410, so a script can tell "no such MSR" apart from "pickle already deleted". My recommendation: do 1 and 2 now. That's frontend only, two files. Hold off on 3 until someone actually needs to pull a large batch.

**문법·구조**: 첫 문장 `Yes, and …` 이 이 단락의 성격을 정한다. `Yes, but` 이었다면 요청을 깎는 답이 되지만 `and` 라서 승인 위에 정보를 얹는 답이 된다 — 한 글자가 톤을 통째로 바꾼다. 가운데 세 문장은 모두 `so` 로 사실과 결과를 잇는 같은 틀을 쓴다(`tokens work …, so a notebook can call it`). 병렬을 일부러 유지해 "이미 되는 것들" 목록임을 형식으로 알린다. 끝의 `My recommendation:` 이하는 문장을 짧게 끊어 앞의 설명부와 리듬을 갈라놓았다. 명령형(`do 1 and 2`, `Hold off on 3`)으로 바뀌는 것도 같은 신호다.

**핵심 표현**: `tell A apart from B` — 둘을 구별하다. 목적어가 짧으면 `tell A from B` 로도 쓴다. / `hold off on X until …` — 신호가 올 때까지 보류하다("안 한다"가 아니라 "기다린다"). / `until someone actually needs to` — `actually` 가 가정된 수요와 실제 수요를 가른다.

**격식 짝**: (작성)
- refined: `We recommend deferring the bulk endpoint until a concrete need arises.`
- plain: `Let's hold off on the bulk one until someone actually asks for it.`

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/1b339d73</sub>
