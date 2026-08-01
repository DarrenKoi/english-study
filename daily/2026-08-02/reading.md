# 2026-08-02 — 정독

## 단락 1

Short answer: **no changes needed** — and there's a specific reason that's fortunate. `pack.py:244` and `docs/deployment.md` §3 both confirm `wsgi.ini` is *deliberately excluded* from the deploy bundle. It lives permanently on the cloud host at `/project/workSpace/wsgi.ini` and is never overwritten by an overlay. So a design that needs a `wsgi.ini` change doesn't cost a deploy — it costs a **manual, out-of-band edit on the cloud host, coordinated by hand, with no way to verify it from home.** That's a strong reason to prefer a design that needs zero. The good news is the current file already provides everything worker-election needs, by accident of prior decisions.

**문법·구조**: 첫 문장이 결론(`no changes needed`)이고 나머지 다섯 문장이 전부 근거다. 영어 기술 산문의 기본 배열인데, 대시(`—`)로 "그런데 그게 다행인 이유가 따로 있다"를 덧붙여 근거 문단을 예고한다.

시제를 보면 판단이 갈린다. `both confirm`·`lives`·`is never overwritten`은 현재형이다. 지금도 계속 참인 사실이라서다. 반면 `doesn't cost … it costs …`는 가상의 설계를 두고 하는 말인데도 현재형을 쓴다. 영어는 조건이 문장 안에 이미 들어 있으면(`a design that needs a change`) 굳이 `would`를 얹지 않는다. 여기서 `would`를 쓰면 오히려 "실제로는 그럴 일 없다"는 뉘앙스가 생겨 경고가 약해진다.

`is deliberately excluded`와 `is never overwritten`은 둘 다 수동태다. 배포 도구가 무엇인지가 아니라 파일이 어떤 처지에 놓였는지가 논점이므로, 행위자를 지우는 편이 초점에 맞다. `deliberately` 하나가 "빠뜨린 게 아니라 뺀 것"임을 밝혀 준다.

마지막 문장의 `by accident of prior decisions`는 문미에 놓여 반전을 만든다. 앞까지 읽으면 설계가 잘 맞아떨어진 듯 보이는데, 마지막 구가 그 조건이 의도된 적 없음을 밝힌다. 정보를 문장 끝에 두는 배치(end-focus)의 전형이다.

**핵심 표현**: `out-of-band`(정규 경로 밖의 수동 처리 — 뒤의 `with no way to verify it from home`이 왜 나쁜지까지 설명한다) · `costs a deploy` vs `costs a manual edit`(같은 동사를 두 번 써서 비용의 종류가 다름을 대비) · `by accident of prior decisions`(결과는 맞지만 설계는 아니었다).

**격식 짝**:
- refined: A design requiring a `wsgi.ini` change would incur a manual, out-of-band edit on a host we cannot verify from home. (작성)
- plain: If the design needs a `wsgi.ini` change, someone has to go edit it on the server by hand — and we can't check it from here. (작성)

<sub>출처: transcript:skewnono_v3_nuxt [assistant]</sub>

---

## 단락 2

**`harakiri = 60` will not kill a 20-minute job.** uWSGI arms the harakiri timer per *request*, on entry to the request handler, and disarms on response. A job running on the scheduler's thread pool never arms it. A long job in worker 1 is safe; only a stuck HTTP request in that same worker would take the process down. **`max-requests = 1000` recycles worker 1, and that's the one real interaction.** After 1000 requests uWSGI respawns it, taking the scheduler thread with it. uWSGI reuses the worker-id slot, so the respawned process re-elects itself and rebuilds the scheduler — the outage is the length of one app boot.

**문법·구조**: 두 덩어리가 같은 틀로 짜였다. 굵게 쓴 판정 한 문장 → 메커니즘 설명 → 결론. 첫 덩어리는 걱정을 해소하고 둘째 덩어리는 진짜 상호작용을 인정한다. `and that's the one real interaction`이 두 덩어리를 잇는 경첩이다. `one real`이 "앞 것은 가짜였다"를 되돌아보며 가리킨다.

세미콜론 문장(`A long job in worker 1 is safe; only a stuck HTTP request … would take the process down`)을 눈여겨볼 만하다. 두 절이 안전과 위험으로 대칭을 이루므로 마침표로 끊으면 대비가 흩어지고, `but`을 넣으면 앞 절을 뒤집는 것처럼 읽힌다. 세미콜론은 뒤집지 않고 나란히 놓는다. 여기서 `would`는 앞 문단과 반대로 반드시 필요하다. 실제로 일어나지 않은 조건을 말하고 있어서다.

분사구 `taking the scheduler thread with it`은 결과를 덧붙이는 자리다. 시간 순서상 뒤따르는 일을 주절에 매다는 방식이라, 별도 문장으로 쪼갤 때보다 인과가 촘촘해진다.

마지막 대시 뒤 `the outage is the length of one app boot`가 이 문단의 값이다. 장애가 있다는 사실보다 얼마나 짧은지가 결론이라서, 앞의 설명을 다 읽지 않아도 판단이 서게 문미에 놓았다.

**핵심 표현**: `arms / disarms the timer`(타이머가 언제 살아 있는지를 상태 전환으로 서술) · `take the process down`(프로세스를 죽게 만들다 — 주어가 사람이 아닐 때 자연스럽다) · `the outage is the length of one app boot`(장애 시간을 다른 익숙한 작업의 길이로 환산해 감을 준다).

**격식 짝**:
- refined: The harakiri timer is armed per request and therefore never engages a job executing on the scheduler's thread pool. (작성)
- plain: Harakiri only starts counting when a request comes in, so it never sees scheduler jobs at all. (작성)

<sub>출처: transcript:skewnono_v3_nuxt [assistant]</sub>

---

## 단락 3

**Gap A — files loaded, no parameters.** If every returned file carries an empty `parameters` array, `setParams.length === 0` so the pool silently falls back to `focusParams`, while the guard sees `size !== 0` and lets the write through. The original bug, reached by a different route. Narrow, but it's the same defect. **Gap B — partial batch. This one is documented behavior.** So a 5-msr set where 2 msrs have no file yields `setFiles.size === 3`: the guard passes, the pool *looks* authoritative, and a parameter carried only by the 2 missing measurements gets rewritten out of the URL and lost for the session. That's the identical user-visible harm the fix was written to prevent. Rendering off a 3-file union is fine; using that same incomplete union as URL authority is not — which is exactly the two-masters distinction.

**문법·구조**: 병렬 구조가 문단을 떠받친다. `Gap A` / `Gap B`, 그리고 각 항목 안의 "조건 → 그래서 무슨 일이 → 그래서 왜 문제인가". 두 항목을 같은 틀로 쓰면 독자가 두 번째를 훨씬 빨리 읽는다.

`The original bug, reached by a different route.`와 `Narrow, but it's the same defect.`는 둘 다 동사가 없는 조각 문장이다. 기술 산문에서 판정을 내릴 때 의도적으로 쓰는 장치로, 앞 문장의 긴 설명을 짧게 요약해 리듬을 끊는다. 남용하면 성의 없어 보이지만 긴 설명 뒤 한 번이면 강조로 작동한다.

`while the guard sees … and lets the write through`의 `while`은 시간이 아니라 대조다. 같은 순간에 두 판단이 엇갈린다는 뜻이라서, "동시에"와 "그런데"를 한 단어가 겸한다. 콜론 뒤 세 절(`the guard passes, the pool looks authoritative, and a parameter … gets lost`)은 원인에서 피해까지 한 호흡에 이어 붙였다.

마지막 문장의 `is fine; … is not`은 생략(ellipsis)이다. `is not fine`에서 `fine`을 지워 대비를 날카롭게 만든다. 그 뒤 `which`는 앞 절 전체를 받는 관계대명사로, 앞의 구체적 사례를 이미 이름 붙여 둔 유형(`the two-masters distinction`)에 연결한다.

**핵심 표현**: `lets the write through`(막아야 할 쓰기를 통과시키다 — 게이트 비유) · `the pool looks authoritative`(권위 있어 *보인다*, 즉 아니다) · `reached by a different route`(같은 결함에 다른 경로로 도달했다).

**격식 짝**:
- refined: Using an incomplete union as the authority for URL state is not equivalent to rendering from it. (작성)
- plain: It's fine to draw the chart from three files. It's not fine to let those three decide what the URL says. (작성)

<sub>출처: transcript:skewnono_v3_nuxt [assistant]</sub>
