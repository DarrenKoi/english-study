# 2026-07-27 — 새 표현

## "punt to (something)"

- 레지스터: technical, casual
- 출처: transcript:[assistant] skewnono_v3_nuxt (99399c55)
- 맥락: 여기서 끝냈어야 할 판단을 다음 계층에 떠넘겼다고 지적할 때. 코드리뷰·회고의 구어.
- 한국어: (판단·처리를) 떠넘기다, 미루다.
- 설명: 미식축구에서 4다운째 공을 차 넘기는 punt 입니다. "틀렸다"가 아니라 **책임 소재가 뒤로 밀렸다**는 진단이라, 결과는 맞는데 경로가 이상한 코드에 딱 맞습니다. 전치사를 구분하세요 — `punt to`(떠넘긴 대상) / `punt on`(보류한 사안). `punt on the naming` 은 이름 짓기를 미뤘다는 뜻.
- 예문: Two of the six call sites punted to the index page instead of resolving the fab themselves, so the href they published hid the real destination.
- 유사어: kick the can down the road (더 부정적·구어), defer to (격식·중립), leave it to the next layer (풀어쓴 형태)
- 반의어: resolve it at the source / own the decision

## "blow past (a limit)"

- 레지스터: technical, conversational
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 한도를 아슬아슬 넘는 게 아니라 훌쩍 지나쳐 버린다고 경고할 때. 용량 산정·성능 논의.
- 한국어: (한도를) 가볍게 넘겨 버리다.
- 설명: exceed 가 중립적으로 "넘는다"라면 blow past 는 속도감이 붙어 "브레이크 없이 지나쳐 버린다"에 가깝습니다. 그래서 여유가 없다는 걸 강조할 때만 어울리고, 5% 초과 같은 상황엔 안 씁니다. 기한에도 그대로 옮겨 갑니다 — `we blew past the deadline`.
- 예문: Two hundred simultaneous connections blow past the worker's open-file limit, and some downloads then silently fail.
- 유사어: exceed (격식·중립), overrun (기한·예산), bust through (더 구어)
- 반의어: stay within / sit comfortably under

## "black-holed (host)"

- 레지스터: technical
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 죽었다는 응답조차 없이 요청을 삼켜 버리는 상대를 가리킬 때. 타임아웃 설계 문서.
- 한국어: (요청을) 그냥 삼켜 버리는, 응답도 거절도 없는.
- 설명: 방화벽이 `DROP` 으로 조용히 버릴 때 요청이 블랙홀에 빨려 들어간 것처럼 보인다는 데서 왔습니다. 원문이 `dead/black-holed` 로 나란히 쓴 게 핵심 — 죽은 호스트는 거절이라도 즉시 돌려주지만 black-holed 호스트는 아무것도 안 줘서 타임아웃까지 슬롯을 물고 있습니다. 그래서 이 단어 뒤에는 늘 timeout 이야기가 따라붙습니다.
- 예문: A tight `connect_timeout` is what makes hundreds of black-holed tools fail fast instead of each holding a worker slot for minutes.
- 유사어: silently dropped (풀어쓴 표현), unresponsive (더 넓고 중립적), hanging (증상 쪽에서 본 말)
- 반의어: actively refusing the connection

## "(a guard) actually bites"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (99399c55)
- 맥락: 검사를 넣은 뒤 일부러 규칙을 어겨 빨간불을 확인했다고 보고할 때.
- 한국어: (방어장치가) 진짜로 물어 준다, 실제로 걸러 낸다.
- 설명: 개가 짖기만 하는지 무는지에 빗댄 말(`its bark is worse than its bite`). "테스트가 통과했다"보다 한 단계 높은 주장이라, 뒤에 **깨뜨려 봤다는 절차**가 따라와야 정직한 문장이 됩니다. 원문의 괄호가 이유를 한 줄로 못 박습니다 — a guard that can't fail is worthless.
- 예문: I removed `/chat` from the list to check the guard actually bites — three tests went red, naming the missing path in the failure message.
- 유사어: has teeth (거의 같은 뜻이고 규칙·계약에도 씀), is enforced (격식·중립), fails when it should (풀어쓴 형태)
- 반의어: a rubber stamp / a test that can never fail

## "works on my machine, breaks on the server"

- 레지스터: casual, technical
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 환경 차이로만 터지는 부류의 버그를 한 마디로 분류할 때. 인용부호로 묶어 명사처럼 씁니다.
- 한국어: "내 컴퓨터에선 되는데요" 부류의 문제.
- 설명: 원형은 개발자 변명의 대명사인 `it works on my machine`. 여기서는 통째로 인용부호에 넣어 `a classic ~ cause` 의 수식어 자리에 밀어 넣었습니다. 관용구를 인용부호나 하이픈으로 묶어 형용사로 굳히는 이 압축법은 영어 기술 글에서 아주 흔하니, 한 번 익혀 두면 계속 씁니다.
- 예문: An unpinned dependency installed at task runtime is a classic "works on my machine, breaks on the server" cause.
- 유사어: an environment-specific failure (격식), it only reproduces in CI (증상 중심), a snowflake environment (환경 쪽에 책임을 둘 때)
- 반의어: reproducible everywhere / hermetic

## "a rule surviving on discipline"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (99399c55)
- 맥락: 규칙이 코드가 아니라 사람의 주의력으로만 지켜지고 있다고 진단할 때. 리팩터링 제안의 도입부.
- 한국어: 규율(주의력)에 기대어 겨우 버티는 규칙.
- 설명: `survive on ~` 은 "~만 먹고 연명하다"라 이미 위태롭다는 뜻을 품고 들어옵니다. 여섯 군데 복사된 규칙을 지금껏 사람이 전부 기억해서 맞춰 왔다는 사실을, 누구도 탓하지 않으면서 짚는 표현이에요. 그래서 바로 뒤에 자동화 제안을 붙이기 좋습니다.
- 예문: Six copies of the same fallback all remembered to check the sentinel — that's a rule surviving on discipline, and one lapse gives you a URL that quietly returns nothing.
- 유사어: enforced by convention only (격식), held together by memory (구어), tribal knowledge (사람 머릿속에만 있는 지식)
- 반의어: structurally impossible to get wrong / caught mechanically

## "slip past (a check)"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (99399c55)
- 맥락: 검사가 잡아야 할 것을 놓친다고 지적할 때. 테스트 설계 비평.
- 한국어: (검사망을) 빠져나가다.
- 설명: `slip through` 와 뜻은 겹치지만 그림이 다릅니다. `past` 는 **관문 하나를 지나쳐 갔다**라서 검사 대상을 목적어로 바로 받고(`slip past the guard`), `slip through` 는 `the cracks` 같은 "틈"을 데려오는 경향이 있습니다.
- 예문: The regex scrape only matches a static `to="/…"`, so any dynamic binding slips past it while the test still reports green.
- 유사어: slip through the cracks (놓친 쪽을 강조), go undetected (격식·중립), evade the check (의도적일 때)
- 반의어: get caught by / trip the guard

## "spend most of its travel on"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)
- 맥락: 슬라이더·다이얼의 범위가 잘못 잡혔다고 UI 리뷰에서 짚을 때.
- 한국어: (조작 범위의) 대부분을 ~에 써 버리다.
- 설명: 여기서 `travel` 은 여행이 아니라 **가동 행정** — 손잡이가 끝에서 끝까지 움직이는 물리적 거리입니다. 기계 용어를 UI 비평에 그대로 가져와, "범위가 넓다"가 아니라 넓은 만큼 쓸모없는 구간이 많다는 구체적인 불만을 말합니다.
- 예문: The 2–30 range spent most of its travel on values nobody sets, so 4–20 puts the usual 6–10 band under your thumb.
- 유사어: wastes half the range on (직설적), is poorly scaled (격식·중립), most of the slider does nothing (풀어쓴 구어)
- 반의어: every step earns its place

## "want (something) on the record"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (99399c55)
- 맥락: 승인받을 정도는 아니지만 나중에 문제 되면 곤란한 변경을 스스로 밝혀 둘 때. 보고서 말미.
- 한국어: 기록으로 남겨 두고 싶다, 명시해 둔다.
- 설명: 법정·회의록의 `on the record`(공식 기록에 남는)에서 왔습니다. 허락을 구하는 게 아니라 일방적으로 공표해 두는 자리라, 승인을 청하는 `worth your call` 과 섞이면 상대가 무엇을 해야 하는지 흐려집니다. 자기 변경의 부작용을 자진 신고하는 문장에 특히 잘 맞습니다.
- 예문: One behavior change I introduced and want on the record: rows with an empty `fab_name` are now dropped instead of surfacing a blank picker option.
- 유사어: for the record (문두 부사구로), flagging this explicitly (중립), noting it so it isn't a surprise later (풀어쓴 형태)
- 반의어: slip it in quietly / leave it undocumented

## "in situ"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)
- 맥락: 따로 떼어 본 게 아니라 실제 놓일 자리에 얹어 확인했다고 말할 때. 검증 보고.
- 한국어: 제자리에서, 실제 맥락 안에서.
- 설명: 라틴어를 그대로 쓰는 말이라 이탤릭 없이 두 단어로 둡니다. 아이콘·컴포넌트를 격리 화면에서 본 것과 실제 헤더에 얹어 본 것을 가르는 데 유용해요. 발음은 [인 사이투]에 가깝습니다.
- 예문: The icon read fine on its own, but in situ it competed with the search glass two slots to the left.
- 유사어: in place (평이한 말), in context (가장 무난), in the real header (아예 구체적으로 풀기)
- 반의어: in isolation / on a swatch sheet

## "dead space"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)
- 맥락: 레이아웃에서 아무 일도 하지 않는 빈자리를 문제로 지목할 때.
- 한국어: 죽은 여백, 아무 일도 안 하는 빈 공간.
- 설명: 같은 픽셀이라도 의도된 여백은 `whitespace`(긍정), 의도 없이 생긴 구멍은 `dead space`(부정)로 갈립니다. 어느 쪽 단어를 고르는지가 곧 판정이라, 여백을 지적할 때 이 선택 자체가 메시지입니다.
- 예문: The card shrank from 700px to 380px once the note spanned the full width — about 300px of dead space reclaimed.
- 유사어: wasted vertical space (구체적), a gap that does no work (풀어쓴 형태)
- 반의어: breathing room / intentional whitespace

## "stranded"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)
- 맥락: 요소가 주변과 끊긴 채 홀로 떠 있다고 묘사할 때. 레이아웃 진단.
- 한국어: (혼자) 붕 뜬, 고립된.
- 설명: 배가 좌초하고 사람이 발이 묶이는 그 stranded 입니다. 위치가 틀렸다는 말이 아니라 **주변이 사라져서 혼자 남았다**는 인과를 담고 있어서, 고칠 곳이 그 요소가 아니라 옆 칸이라는 뜻까지 은근히 전달합니다.
- 예문: With the left column ending 400px early, the stats block sat stranded top-right with nothing below it.
- 유사어: orphaned (더 셈; 부모가 사라진 그림), floating on its own (구어), visually detached (격식)
- 반의어: anchored to / grouped with

## "X comes from A, not from B itself"

- 레지스터: professional
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 상대의 걱정을 부정하지 않고 원인만 옮겨 놓아 오해를 푸는 자리. 설계 방어 문서.
- 한국어: 그건 A 탓이지 B 자체 탓이 아니다.
- 설명: "괜찮습니다"로 시작하면 방어적으로 들립니다. 걱정을 명사구로 받아 `comes from` 으로 원인을 재배치하면, 상대의 관찰은 인정하면서 결론만 뒤집을 수 있어요. 끝의 `itself` 가 일합니다 — B 를 통째로 무죄로 만드는 게 아니라 **B 라는 성질 자체는 원인이 아니라고** 범위를 좁혀 줍니다.
- 예문: The fear that async mixes one host's data into another host's buffer comes from shared mutable state, not from memory itself.
- 유사어: the risk is X, not Y (더 짧음), that's a property of A rather than B (격식), it's not B that does it — it's A (구어 강조형)

## "vendor (a package)"

- 레지스터: technical
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 의존성을 설치하는 대신 저장소 안에 복사해 넣으라고 지시할 때. 폐쇄망·오프라인 배포.
- 한국어: (외부 패키지를) 저장소 안에 복사해 넣다.
- 설명: 명사 vendor(공급업체)를 그대로 동사로 쓴 개발 은어. `pip install` 이 막힌 환경의 표준 해법이라, 이 단어 하나로 "설치가 아니라 동봉"이라는 방식까지 지정됩니다. 실제로는 과거분사 `vendored` 형태를 더 자주 봅니다.
- 예문: Only `minio_handler` is vendored under `airflow_mgmt/`, so the index step fails on the worker until `ops_store` travels the same way.
- 유사어: bundle (더 일반적), inline the dependency (풀어쓴 형태), check it into the repo (직설적)
- 반의어: pull it from the package index / declare it in requirements.txt

## "bloat"

- 레지스터: technical
- 출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 인코딩·의존성 때문에 불어난 군살을 수치와 함께 지적할 때.
- 한국어: 군살, 불어난 양.
- 설명: 배가 더부룩한 그 bloat 입니다. 앞에 퍼센트가 붙으면(`~33% bloat`) 정확한 오버헤드를 가리키고, 명사 앞에 붙으면(`dependency bloat`) 막연한 비대함을 가리킵니다. 같은 단어인데 수치 유무로 정밀도가 갈리니 앞뒤를 보고 읽으세요.
- 예문: JSON + base64 is simple and fine for small files, but a streaming transport would beat base64's ~33% bloat on large payloads.
- 유사어: overhead (중립·정량적), padding (부풀린 부분), fat (구어)
- 반의어: a lean wire format

## "worth your eye"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)
- 맥락: 결정은 이미 내렸지만 상대가 한 번 봐 줬으면 하는 대목을 표시할 때. 보고서 소제목.
- 한국어: 한 번 봐 둘 만한, 눈여겨볼.
- 설명: `worth your time`(시간을 쓸 값어치) 과 달리 **보는 것**만 요구해서 부담이 훨씬 가볍습니다. 이미 진행했다는 전제가 깔리므로, 판단을 넘기는 `worth your call` 과는 요구 수준이 다릅니다. 둘을 섞어 쓰면 상대가 승인해야 하는지 확인만 하면 되는지 알 수 없게 됩니다.
- 예문: Two judgment calls worth your eye: the dark field stays dark in light mode, and the margin hatching went terracotta rather than indigo.
- 유사어: worth flagging (더 중립), one to keep an eye on (앞으로 지켜볼 것), FYI (가장 가벼움)
- 반의어: settled, no action needed
