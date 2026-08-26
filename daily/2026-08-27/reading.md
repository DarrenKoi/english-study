# 2026-08-27 — 정독

## 단락 1

**Spec (c)1 — conceded, and it's the finding that mattered.** I checked `310128c1`: `start` did feed all three sources. With the window at 2주, a PM three weeks ago became `post_pm_at = None`, `prev_post_delta` went with it, and pm-tune's "freshest out of PM" default pick moved. Nobody asked for that; my "one span, one label" note in MIGRATION was rationalising a widening. **Fixed:** `PM_LOOKBACK_DAYS = 30` (what the old window gave PM events), decoupled exactly the way MDC epochs already are, with a test asserting the lookback at both ends of the choices. BSM stays windowed — it's a "current reading" like CD, which the spec did size.

**문법·구조**: 외부 리뷰의 지적 하나를 "수용 → 검증 → 피해 → 자백 → 수정 → 경계선" 순서로 닫는 판정문이다.
① 첫 문장은 굵은 한 단어 `conceded` 로 판정을 끝내고 `and it's the finding that mattered` 로 등급을 붙인다. 판정이 먼저, 근거가 뒤 — 리뷰 응답의 기본 순서다.
② `I checked …: start did feed all three sources.` — 조동사 `did` 가 강조 용법이다. 모델의 주장을 내가 직접 확인했더니 *정말로* 그랬다는 뜻으로, 남의 말을 옮기는 게 아니라 검증했음을 한 단어로 보인다.
③ 셋째 문장은 과거시제 세 절을 쉼표로 이어 연쇄 피해를 그린다. `became None`, `went with it`, `moved` — 세 동사가 모두 과거형이라 "고치기 전엔 실제로 이랬다"가 된다. `went with it` 은 "그것과 함께 사라졌다"는 관용구.
④ `Nobody asked for that; my note … was rationalising a widening.` — 세미콜론 앞은 스펙 위반의 확인, 뒤는 자기 문서에 대한 자백이다. 과거진행형 `was rationalising` 이 "그 문장을 쓰는 동안 내가 하고 있던 일"을 되짚는다.
⑤ `Fixed:` 뒤는 명사구만으로 수정 내용을 적는다. 괄호가 값의 출처(`what the old window gave`)를, 과거분사구 `decoupled exactly the way X already are` 가 기존 패턴과의 일관성을, `with a test asserting …` 이 회귀 방지를 각각 맡아 한 문장에 세 층이 실린다.
⑥ 마지막은 대시로 붙인 경계선이다. `BSM stays windowed` 로 고치지 *않은* 것을 밝히고, 관계절 `which the spec did size` 에서 다시 강조 `did` 가 나온다 — "이건 스펙이 실제로 정한 것"이라 되돌릴 이유가 없다는 근거.

**핵심 표현**
- `conceded, and it's the finding that mattered` — 수용하면서 그 지적의 무게까지 매긴다(새 표현 참조).
- `went with it` — 앞의 것이 사라지자 덩달아 사라졌다.
- `decoupled exactly the way X already is` — 새 예외를 만든 게 아니라 있던 패턴을 그대로 따랐다.

**격식 짝**
- refined: My note in MIGRATION was rationalising a widening nobody asked for.
- plain: My MIGRATION note was just me talking myself into a bigger change than you asked for. (작성)

<sub>출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66</sub>

---

## 단락 2

APScheduler's DEFAULT memory jobstore is used on purpose, in both phases. Jobs here are declared in code and rebuilt every boot, and all three triggers are cron — absolute wall-clock — so a fresh scheduler after a restart computes exactly the right next fire. A RedisJobStore would pickle each job, and pickling a `functools.wraps`-decorated closure follows `__qualname__` back to the BARE task, so a restored job would bypass the lock and the run log entirely. The accepted loss: a run missed while the process is down is skipped rather than detected as missed.

**문법·구조**: 네 문장짜리 docstring 이 "선택 → 왜 안전한가 → 대안은 왜 위험한가 → 감수하는 것" 의 트레이드오프 서술을 완성한다.
① 첫 문장은 수동태 `is used on purpose` 다. 주어를 jobstore 로 두어 "누가"가 아니라 "무엇이 선택됐는가"에 초점을 맞추고, `on purpose` 가 리뷰어의 "기본값 그냥 둔 거 아니냐"를 미리 막는다. 대문자 `DEFAULT` 는 코드 주석의 강조 관행.
② 둘째 문장은 `A and B, and C — so D` 구조. 세 가지 사실(코드 선언, 매 부팅 재구성, cron 트리거)을 현재형으로 쌓고 `so` 로 결론을 뽑는다. 대시 속 `absolute wall-clock` 은 `cron` 을 풀어 쓴 동격구다.
③ 셋째 문장은 가정법 `would` 가 세 번이다 — `would pickle`, `follows … back to`(현재형: 파이썬의 일반 사실), `would bypass`. "만약 Redis 를 썼다면"이라는 조건이 주어 `A RedisJobStore` 안에 숨어 있어 `if` 절 없이 가정법이 성립한다. `follows __qualname__ back to the BARE task` 는 pickle 이 데코레이터를 벗겨 원함수를 찾아간다는 동작을 `follow … back` 한 구로 그린 것.
④ `The accepted loss:` 콜론 뒤는 단점을 숨기지 않는 결말이다. `skipped rather than detected as missed` — `rather than` 이 두 과거분사를 대비시켜 "놓치는 건 같지만 *알아차리지도* 못한다"는 손실의 정확한 크기를 말한다.

**핵심 표현**
- `is used on purpose` — 기본값을 그대로 둔 게 아니라 고른 것이다.
- `follows X back to the bare task` — 겉을 벗기고 원본까지 거슬러 간다.
- `The accepted loss:` — 알고도 감수한 단점(새 표현 참조).

**격식 짝**
- refined: The accepted loss: a run missed while the process is down is skipped rather than detected as missed.
- plain: The downside we're living with: if the process is down when a job is due, it just doesn't run — and nothing tells us. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-01-scheduler-runtime.md</sub>

---

## 단락 3

The page request triggers the refresh. `providers/office.py` resolves `fab_name → fac_id` through the `sem_list` roster, calls `refresh.ensure_fresh(client, fac_id)`, then reads the accumulated ZSET and filters it to the requested fab. `ensure_fresh` returns immediately when the cache is younger than 20s; otherwise it takes a `SET NX EX` lock, and the loser serves the previous board rather than waiting. The office seam is a single lazily-imported `office_utils.live_alarm.get_live_alarms(fac_id)`.

**문법·구조**: 계획 문서의 Architecture 절 — 네 문장으로 요청 한 번의 경로를 끝까지 따라간다.
① 첫 문장은 주어 `The page request` 에 동사 `triggers` 하나뿐인 다섯 단어다. 설계의 핵심(스케줄러가 아니라 요청이 방아쇠)을 가장 짧은 문장에 두어 눈에 띄게 한다.
② 둘째 문장은 한 주어에 동사 셋 — `resolves …, calls …, then reads … and filters …`. 순서를 `then` 하나로만 표시하고 나머지는 쉼표로 이어 실행 순서가 문장 순서와 같게 했다. 화살표 `fab_name → fac_id` 를 문장 안에 그대로 넣는 것도 설계 문서의 관례.
③ 셋째 문장은 `when` / `otherwise` 로 두 갈래를 가른다. 앞 갈래는 `returns immediately`, 뒤 갈래는 `takes a lock, and the loser serves … rather than waiting`. 락에 진 요청을 `the loser` 라는 명사 하나로 부르고, `rather than waiting` 으로 하지 *않는* 행동을 밝혀 논블로킹 설계를 문법으로 보인다.
④ 마지막 문장은 `The office seam is a single …` — 사무실에서 갈아 끼울 지점(seam)이 함수 하나뿐임을 `single` 과 복합 형용사 `lazily-imported` 로 말한다. 명사문이라 동작이 없고, 그래서 "이것 말고는 손댈 데가 없다"는 경계 선언처럼 읽힌다.

**핵심 표현**
- `X triggers the refresh` — 갱신의 방아쇠는 X 다(스케줄러가 아니라 요청).
- `the loser serves the previous board rather than waiting` — 락 경쟁에서 진 쪽은 기다리지 않고 이전 결과를 낸다.
- `the office seam is a single …` — 환경별로 갈아 끼우는 지점이 하나뿐이다.

**격식 짝**
- refined: `ensure_fresh` returns immediately when the cache is younger than 20s; otherwise it takes a lock, and the loser serves the previous board rather than waiting.
- plain: If the cache is under 20 seconds old we just return it; if not, whoever grabs the lock refreshes, and everyone else shows the old board instead of waiting. (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-02-live-alarm-cached-pull.md</sub>
