# 2026-08-06 — 새 표현

## "Independent of X and ships on its own"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 계획서에서 한 작업이 나머지에 매이지 않아 따로 배포해도 된다고 밝힐 때(문어·격식)
- 한국어: 나머지와 무관하며 단독으로 배포된다
- 설명: `ship`은 "만들었다"가 아니라 "사용자에게 도달했다"를 뜻한다. `on its own`이 붙으면 앞뒤 작업의 완료를 기다리지 않아도 된다는 뜻이 되어, 리뷰어에게 "이건 먼저 머지해도 된다"를 알린다.
- 예문: Independent of the beacon and ships on its own — the banner fires once per page load and measures sessions, not interest in a page.
- 유사어: can land separately (더 평이), is not blocked on the rest (의존 없음을 직접 말함), stands alone (범위가 독립적임에 방점)
- 반의어: blocked on Task 2 / rides the same commit

## "longest match wins"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 규칙 표·라우팅 테이블의 우선순위 관례를 한 구로 못박을 때(주석·문서)
- 한국어: 가장 길게 일치하는 규칙이 이긴다
- 설명: 접두사 규칙을 늘어놓는 자료구조에서 순서가 왜 그렇게 짜였는지를 설명하는 관용구다. 뒤에 "so the nested children are listed first" 같은 결과절을 붙이면 표의 배열 근거까지 한 문장에 담긴다.
- 예문: Page segment → slug; longest match wins, so the nested recipe-search children are listed before their parent.
- 유사어: most specific rule wins (규칙 특이도로 표현), first match wins (전혀 다른 정책이니 혼동 금지)
- 반의어: first match wins

## "stand in for"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 시드 데이터·목업에서 어떤 값이 실제 값을 대신 맡고 있다고 밝힐 때(주석·격식)
- 한국어: ~를 대신하다, ~의 자리를 대표하다
- 설명: 배우의 대역(stand-in)에서 온 표현이라 "임시로 그 역할을 맡았을 뿐 그것 자체는 아니다"라는 뉘앙스가 남는다. 시드 값이나 더미 계정처럼 진짜가 아닌 데이터를 설명할 때 `represent`보다 정직하다.
- 예문: `sem_list` stands in for entry traffic — see `_seed_feature`.
- 유사어: serve as a proxy for (지표·대리 측정에 가까움), act as (중립적), double as (원래 용도가 따로 있을 때)
- 반의어: is the real thing / is measured directly

## "console noise"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 오류가 아닌 상황에 에러 응답을 주지 않기로 한 이유를 댈 때(코드 주석·리뷰)
- 한국어: 콘솔을 어지럽히는 잡음
- 설명: 브라우저 콘솔에 빨간 줄이 늘어나면 진짜 오류가 묻힌다는 비용을 한 단어로 압축한다. `a 400 would be console noise for something that is not an error` 형태로 "규격상 실패가 아닌 것"을 가려내는 논거로 쓰인다.
- 예문: A 400 here would make the browser console noisy for a case that is not an error.
- 유사어: log spam (서버 로그 쪽), red herring in the logs (오해까지 유발할 때), chatter (더 구어)
- 반의어: an actionable error

## "not worth a line the user cannot act on"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 예외를 삼키기로 한 결정을 변호할 때(코드 주석·설계 문서)
- 한국어: 사용자가 손쓸 수 없는 메시지는 남길 값어치가 없다
- 설명: 로그·경고의 가치를 "읽는 사람이 그걸로 무엇을 할 수 있는가"로 재는 기준이다. 무조건 다 로깅하자는 반사 반응을 막는 데 잘 듣는다.
- 예문: The expected 429 under fast tab-flipping is not worth a console line the user cannot act on.
- 유사어: nothing the reader can do with it (풀어쓴 회화체), non-actionable (형용사 한 단어)
- 반의어: an error the operator must see

## "Known consequence, accepted"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 설계 문서에서 부작용을 숨기지 않고 "알고 받아들였다"고 라벨을 다는 자리(격식·문어)
- 한국어: 알려진 결과이며 감수하기로 함
- 설명: 두 낱말짜리 헤딩이 문단 전체의 성격을 바꾼다 — 뒤에 오는 서술이 결함 보고가 아니라 의사결정 기록이 된다. 뒤에 "Do not 'fix' this by …"를 붙여 미래의 선의의 수정까지 막는 것이 이 문서의 수법.
- 예문: Known consequence, accepted: a user who only opens zero-API pages appears in the page ranking but not in `dau`.
- 유사어: accepted trade-off (좀 더 중립), by design (더 짧고 방어적), we are knowingly living with this (회화체)
- 반의어: an open defect / to be fixed

## "silently redefine what X means"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 숫자의 단위나 지표 정의가 예고 없이 바뀌는 위험을 경고할 때(리뷰·설계)
- 한국어: 어떤 지표의 의미를 아무도 모르게 바꿔버리다
- 설명: 버그가 아니라 "고장 없이 뜻만 달라지는" 변화를 가리킨다. 화면은 멀쩡하고 테스트도 통과하는데 해석이 틀려지므로 발견이 가장 늦다.
- 예문: Mixing them would silently redefine `this_month.requests`.
- 유사어: change the unit out from under the reader (더 그림 같음), quietly shift the definition (완화)
- 반의어: keep the contract intact

## "stay in agreement about"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 두 모듈이 같은 규칙을 각자 들고 있을 때 어긋나지 않게 맞춰둔 근거를 댈 때
- 한국어: ~에 대해 서로 같은 인식을 유지하다
- 설명: 주어를 사람이 아니라 코드 두 조각으로 잡는 것이 요령이다. 정규식·상수를 복사하면서도 "왜 같은 모양을 썼는가"를 한 줄로 밝힌다.
- 예문: Same shape the frontend uses in `plugins/persist-fab.client.ts`, so the two stay in agreement about what a fab looks like.
- 유사어: stay in lockstep (더 강하게 동기), remain consistent with (격식·건조)
- 반의어: drift apart / get out of sync

## "a shell over (two genuinely different features)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 하나의 라우트·컴포넌트가 껍데기일 뿐 내용이 둘 이상임을 설명할 때
- 한국어: 서로 다른 두 기능을 감싼 껍데기
- 설명: `shell`은 알맹이가 없다는 함의를 준다. 그래서 "URL 은 하나지만 사용자에게는 다른 화면"이라는 상황을 짧게 표현하고, 뒤이어 `?tab=` 같은 실제 정체성을 지목하는 문장으로 이어진다.
- 예문: `tab` on recipe-status is the exception: that route is a shell over two genuinely different features.
- 유사어: a wrapper around (중립), a container route (라우팅 용어), one route carrying two features (풀어쓴 설명)
- 반의어: a page in its own right

## "have no counterpart on the X side"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 두 체계를 대조하면서 한쪽에만 있는 사례를 짚어, 코드를 합치지 않은 이유로 삼을 때
- 한국어: 반대편에는 대응물이 없다
- 설명: 함수를 하나로 합치자는 자연스러운 반론을 미리 막는 논거다. "형태가 정말 다르다"를 주장으로 세우고, 대응물의 부재를 증거로 댄다.
- 예문: `recipe-status` is ONE route carrying TWO features, which has no counterpart on the API side.
- 유사어: has no analogue in (더 격식), there is nothing like it on the other side (회화체)
- 반의어: maps one-to-one

## "beat the redirect"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 경합 조건을 설명하며 "리다이렉트보다 먼저 도착한 요청"을 가리킬 때
- 한국어: 리다이렉트보다 먼저 도착하다
- 설명: 경주 은유의 `beat`가 시간 순서를 그대로 옮긴다. 확률이 낮아도 있을 수 있는 순서를 방어했다는 뜻이라, 뒤에 `defensively`가 자주 따라온다.
- 예문: Legacy routes are mapped defensively so a beacon that beats the redirect is not misfiled.
- 유사어: arrive before the redirect lands (풀어쓴 회화체), race ahead of (경합임을 강조)
- 반의어: follow the redirect

## "teach a relationship the data does not have"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 시드·목 데이터를 실제에서 유도하지 않기로 한 근거를 밝힐 때(설계·리뷰)
- 한국어: 데이터에 없는 상관관계를 가르치다
- 설명: 목 데이터의 위험을 "거짓말"이 아니라 "학습"으로 표현한다. 화면과 프런트엔드가 그 가짜 비율을 사실로 받아들여 이후 판단이 오염된다는 그림이 한 구에 담긴다.
- 예문: A derived number would teach a relationship the office data does not have.
- 유사어: bake in a false correlation (더 기계적), train the reader on a fiction (더 문학적)
- 반의어: reflect what production actually looks like

## "read as X rather than Y"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: UI·문구가 사용자에게 어떻게 오해되는지를 설명해 안내 문구의 필요를 논증할 때
- 한국어: ~가 아니라 ~로 읽힌다
- 설명: 주어를 화면으로 두고 `read`를 자동사로 쓴다. 사실이 아니라 인상을 다루는 문장이라, 기능은 정상인데 오해가 생기는 상황을 정확히 집는다.
- 예문: Without a caption, an almost-empty 인기 기능 Top 10 reads as a broken page rather than a young one.
- 유사어: comes across as (더 구어), looks like a bug when it is not (풀어쓴 회화)
- 반의어: reads exactly as intended

## "reachable at all"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-activity-page-view-beacon.md
- 맥락: 필터·쿼리를 넓히는 변경에서 "그 전에는 아예 닿지도 않았다"를 강조할 때
- 한국어: 애초에 닿기라도 하도록
- 설명: `at all`이 붙으면 "부족했다"가 아니라 "0이었다"가 된다. 상위 필터가 하위 집계 전체를 가리는 구조를 설명할 때 이 강도가 필요하다.
- 예문: Widen the base query so page-view rows are reachable at all.
- 유사어: visible to the query in the first place (풀어씀), included at the top level (건조)
- 반의어: filtered out upstream

## "the only symptom is (uptime that keeps climbing)"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 조용히 실패하는 방식을 설명하며, 관찰 가능한 흔적이 딱 하나뿐임을 밝힐 때
- 한국어: 유일한 증상은 ~뿐이다
- 설명: 실패가 예외도 로그도 남기지 않을 때, 무엇을 봐야 알아챌 수 있는지를 지정하는 문장이다. 운영자에게 감시 지표를 알려주는 실용적 효과까지 있다.
- 예문: Touching a file uWSGI isn't watching succeeds every night and reloads nothing — the only symptom is uptime that keeps climbing.
- 유사어: the one tell is (더 구어·탐정 은유), you would only notice it by (동사절로 풀기)
- 반의어: it fails loudly

## "say so instead of pretending"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 설정이 빠졌을 때 작업이 성공한 척하지 않고 사실을 보고하도록 만들었다고 밝힐 때
- 한국어: 성공한 척하지 않고 그 사실을 말한다
- 설명: 프로그램을 사람처럼 주어로 세우는 의인화가 관용으로 굳은 표현이다. `pretend`가 있어서 "조용한 성공"이 왜 나쁜지까지 한 낱말로 전달된다.
- 예문: Change the path in `wsgi.ini` and the job follows with no code change; delete the line and the job says so instead of pretending.
- 유사어: report the gap rather than paper over it (더 격식), fail loudly (결과 쪽에 방점)
- 반의어: silently succeed

## "the durable record"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 여러 로그 중 어느 것이 재시작·장애를 견디는 정본인지 지정할 때
- 한국어: 끝까지 남는 기록, 정본
- 설명: `durable`은 저장소 논의에서 "프로세스가 죽어도 살아남는"을 뜻한다. 어느 로그를 믿을지 정해두면 사후 조사에서 헤매지 않는다.
- 예문: The INFO line is emitted before the touch — the uWSGI log is the durable record.
- 유사어: the source of truth (권위 쪽 강조), what survives the restart (풀어쓴 회화체)
- 반의어: best-effort logging

## "be silently loosened"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 기존 불변식을 깨야 할 때 테스트를 슬쩍 완화하지 말고 예외를 명시하라고 말할 때
- 한국어: 아무 설명 없이 조건이 헐거워지다
- 설명: 수동태가 행위자를 지워, 사람을 탓하지 않고 관행을 문제 삼는다. `rather than` 구문과 짝으로 써서 올바른 대안을 같은 문장에 넣는 것이 정석이다.
- 예문: The test has to grow an explicit, documented carve-out rather than be silently loosened.
- 유사어: get quietly relaxed (평이), have its teeth pulled (관용·비유)
- 반의어: be tightened / be documented explicitly

## "can't outlive"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 락·캐시·임시 자원의 수명 상한을 그 원인 사건에 묶어 설명할 때
- 한국어: ~보다 오래 살아남을 수 없다
- 설명: TTL 을 숫자로만 말하지 않고 "무엇보다 짧아야 하는가"로 말한다. 수명 관계를 한 문장에 넣으면 그 숫자를 왜 그렇게 골랐는지가 같이 설명된다.
- 예문: `lock_ttl` is 120s so the orphaned lock can't outlive the reload that caused it.
- 유사어: expires before (건조·중립), is bounded by the restart (경계 강조)
- 반의어: leaks / lingers indefinitely

## "deliberately narrow"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a14518c0 (scheduler 로그 정리·리로드 작업)
- 맥락: 파괴적인 동작(삭제·덮어쓰기)의 범위를 일부러 좁혔다고 밝힐 때
- 한국어: 일부러 좁게 잡았다
- 설명: `deliberately`가 없으면 "기능이 빈약하다"로 읽힐 서술이, 붙는 순간 안전 설계의 선언이 된다. 뒤에 `since it unlinks` 처럼 이유절을 달아 좁힘의 대가를 정당화한다.
- 예문: The sweep is deliberately narrow since it unlinks: one directory, glob-matched names only, symlinks skipped rather than followed.
- 유사어: intentionally conservative (더 격식), scoped as tightly as it can be (풀어씀)
- 반의어: recursive by default / broad by design
