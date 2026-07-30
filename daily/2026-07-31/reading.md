# 2026-07-31 — 정독

## 단락 1

Your error message is not a database connection failure. `fetch_hits` returned an *empty result set* — a broken connection raises, it doesn't return zero hits. So OpenSearch answered fine and genuinely has no measurement document for that recipe in R3, which is the normal state for a recipe that has never been measured. The Redis recipe registry exists precisely to open those recipes without a measurement. The real question was why the registry didn't rescue it. Your deployed `office.py` is a **stale** copy from before the Redis-registry work landed. Its `_locate_idp` is a single meas_hist query with no registry path at all — grep confirms no `_locate_via_redis`, no `rcp_loc`, no `tools_in_rcp`. It went straight to meas_hist and 502'd, exactly as observed.

**문법·구조**: 시제가 이 단락의 뼈대입니다. 첫 문장은 현재형 `is not` 으로 상대의 진단을 부정하고, 근거는 과거형 `returned` 로 실제 일어난 일을 댑니다. `a broken connection raises, it doesn't return zero hits` 는 접속사 없이 쉼표로만 두 절을 이었는데, 여기서 현재형은 시점이 아니라 **일반적 성질**을 말합니다 — "끊긴 연결은 원래 예외를 던지지 값을 안 준다". 이어지는 `which is the normal state for a recipe that has never been measured` 는 앞 절 전체를 받는 계속적 관계절이고, 그 안에 다시 `that has never been measured` 관계절이 들어가 이중 구조를 이룹니다. 현재완료 `has never been measured` 는 "지금까지 한 번도"라는 누적 부정이라 과거형으로 바꾸면 뜻이 흐려집니다. 마지막 문장의 `502'd` 는 상태 코드를 동사로 쓴 개발자식 조어이고, `exactly as observed` 로 관찰 사실과 설명이 맞물렸음을 닫습니다.

**핵심 표현**: `exists precisely to ~`(바로 그것을 위해 존재한다 — 기능의 존재 이유를 못 박을 때) · `rescue it`(다른 경로가 실패를 구제하다 — 폴백을 사람처럼 표현) · `exactly as observed`(관찰된 그대로 — 가설과 증상이 일치했다고 보고할 때).

**격식 짝**: refined — *The registry exists precisely to serve recipes that carry no measurement.* / plain — *That registry is there for exactly this case: recipes nobody has measured yet.* (작성)

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (eb7129d4) — 원문 발췌를 한 단락으로 이어 붙임</sub>

---

## 단락 2

`v3_df_sem_avail` is a derived subset, not the roster. Every tool is assigned an `eqp_ip` when it is installed in the fab and is firewalled from that moment; it only enters `v3_df_sem_avail` once IT opens that IP. So `v3_df_sem_list - v3_df_sem_avail` is exactly the queue of firewall-exception requests, and "in the roster but unreachable" is the normal initial state of every tool rather than an error. This is the fleet identity source, and that has a consequence for home runs. `storage`, `lateral_recipe`, `hardware/sharpness`, `hardware/reso_center` and `hardware/mdc` all resolve `eqp_id -> eqp_ip / fab_name` through this roster, so those office adapters refuse to run while sem_list is on mock: a fabricated IP matches zero documents and is indistinguishable from "no data". Turning one of them onto office therefore means turning sem_list on too.

**문법·구조**: 두 번째 문장이 **수동태를 왜 쓰는가**의 교과서입니다. `Every tool is assigned an eqp_ip` — IP 를 부여하는 주체(IT? 설비팀?)는 이 문서의 관심사가 아니고 장비가 겪는 일만 중요하므로, 행위자를 지운 수동이 정확합니다. 이어지는 `when it is installed` 도 같은 이유로 수동이고, 세미콜론 뒤 `it only enters ~ once IT opens that IP` 에서는 반대로 능동으로 돌아옵니다. 여기서만 행위자 IT 가 중요해지기 때문입니다. `once` 는 `after` 와 달리 "그 일이 일어나야 비로소"라는 조건 색이 있어 방화벽 해제라는 관문을 잘 표현합니다. 뒤쪽 `so ~ , so ~` 는 인과의 사슬을 두 번 이어 놓은 것이고, 콜론 뒤 문장은 앞의 `refuse to run` 을 설명하는 근거로 붙습니다. `A is indistinguishable from B` 는 "구별이 불가능하다"를 형용사 하나로 처리하는 압축 표현이라 기억해 둘 만합니다.

**핵심 표현**: `a derived subset, not the roster`(파생된 부분집합이지 명부가 아니다 — 오해를 먼저 차단하는 X, not Y 대비) · `the normal initial state ~ rather than an error`(오류가 아니라 정상 초기 상태 — 결함처럼 보이는 값을 변호할 때) · `refuse to run`(조건이 안 맞으면 아예 실행을 거부하다 — 조용한 실패보다 낫다는 설계 태도).

**격식 짝**: refined — *A fabricated IP matches zero documents and is indistinguishable from an absence of data.* / plain — *A made-up IP finds nothing, and you can't tell that apart from there being no data.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md (mock.py 모듈 docstring)</sub>

---

## 단락 3

The bug had two halves, and the cache key was the smaller one. The watcher was keyed on the parameter name — moving between two rows of one parameter left that name unchanged, so `loadParamDetail` never ran at all. Fixing only the cache would have changed nothing on screen; the stale panel was a missed fetch, not just a bad cache hit. The fix makes the key derive from the request payload itself, so an entry cannot be filed under settings other than the ones fetched. It is correct whichever way the office turns out to work. If same-parameter rows always share slots, identical keys give cache hits exactly as before. If they differ, distinct keys mean each row fetches its own files. No office verification is needed for the fix to be right, which is why I did not wait on one.

**문법·구조**: 가정법이 논증을 끌고 갑니다. `Fixing only the cache would have changed nothing on screen` 은 가정법 과거완료(would have p.p.)로, 실제로는 하지 않은 선택의 결과를 되짚습니다. 주어가 동명사구 `Fixing only the cache` 라서 `If I had only fixed the cache, it would have ~` 를 절반 길이로 줄였습니다. 뒤이어 나오는 두 문장은 반대로 **직설법 조건문**(If + 현재형, 현재형)입니다 — 사무실 사정이 어느 쪽으로 밝혀지든 지금 참인 사실을 말하므로 `would` 가 들어가면 안 됩니다. 두 조건문을 같은 형태로 나란히 놓은 덕에 `whichever way ~ turns out to work` 라는 앞 문장의 주장이 형식만으로도 입증됩니다. 마지막 `which is why I did not wait on one` 은 앞 문장 전체를 받아 자기 판단의 근거로 닫는 계속적 관계절이고, `one` 은 `verification` 을 되받는 대명사입니다.

**핵심 표현**: `the bug had two halves`(버그가 두 겹이었다 — 부분 수정으로는 안 되는 이유를 도입) · `a missed fetch, not just a bad cache hit`(놓친 요청이지 캐시 오적중이 아니다 — 증상과 원인의 층위를 갈라 줌) · `whichever way it turns out to work`(어느 쪽으로 밝혀지든 — 미검증 사실에 결론을 걸지 않았음을 밝힐 때).

**격식 짝**: refined — *No office verification is required for the fix to be sound.* / plain — *We don't need the office to confirm anything for this fix to hold.* (작성)

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (a068254c) — 원문 발췌를 한 단락으로 잇고 코드 조각은 줄임</sub>
