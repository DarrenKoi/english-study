# 2026-07-25 — 새 표현

## "have a shelf life"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 지금은 맞지만 언젠가 반드시 상하는 것을 경고할 때. 문서·주석·측정치의 수명을 말하는 회고조 문장에 어울립니다.
- 한국어: 유통기한이 있다, 언젠가 상한다.
- 설명: 식품 표기에서 온 말인데 기술 글에서는 "이 정보는 영원히 참이 아니다"를 부드럽게 찌릅니다. `tied to ~` 를 붙이면 무엇에 수명이 묶여 있는지까지 한 문장에 담깁니다. 틀렸다고 비난하지 않으면서 갱신 필요를 알리는 완곡함이 이 표현의 값어치.
- 예문: Empirical comments have a shelf life tied to the code they describe, so a measurement taken before the fix reads as authoritative long after it stopped being true.
- 유사어: go stale (더 짧고 구어적), date badly (시간이 지나면 흉해진다는 뉘앙스), be a point-in-time snapshot (격식·중립)
- 반의어: hold indefinitely / be evergreen

## "a false green"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 테스트가 통과했는데 그 통과가 무의미하다고 판정할 때. 코드리뷰·회고에서 씁니다.
- 한국어: 가짜 통과, 헛통과.
- 설명: CI 초록불에서 온 말입니다. 실패해야 마땅한 상황인데 초록이 떴다는 뜻이라, 단순한 flaky(들쭉날쭉)와 다릅니다. flaky 는 결과가 흔들리는 것이고 false green 은 **일관되게 틀린 답을 준다**는 점에서 더 나쁩니다.
- 예문: The plan's single-MSR round-trip was a false green at first — it passed against a mock that was demonstrably broken.
- 유사어: a vacuous pass (검증 자체가 비어 있을 때), passing for the wrong reason (풀어쓴 형태), a green that proves nothing (강조형)
- 반의어: a genuine red / an honest failure

## "draw a lucky seed"

- 레지스터: technical, casual
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 난수·샘플링 기반 테스트가 우연히 통과했다고 짚을 때. 원인 진단 문장에서 씁니다.
- 한국어: 운 좋은 시드를 뽑았다, 하필 통과하는 표본을 골랐다.
- 설명: `seed` 는 난수 생성기의 초기값이라, 뽑기(draw)라는 동사와 붙어 "운이었지 실력이 아니었다"를 정확히 말합니다. 카드 게임 어휘를 그대로 가져온 표현이라 문어보다는 진단 메모·구두 설명에 자연스럽습니다.
- 예문: The single-MSR test just drew a lucky seed, so sweeping thirty MSRs is what turned it genuinely red.
- 유사어: get lucky on that sample (평이한 회화체), happen to land inside the tolerance (기계적·정확), a happy accident (더 가볍고 긍정적)
- 반의어: exercise the whole space / sweep the parameter range

## "nothing announces it"

- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-24-deploy-packaging-design.md
- 맥락: 어떤 실패가 왜 최악인지 근거를 댈 때. 설계 문서의 위험 서술에서 결정타로 씁니다.
- 한국어: 아무것도 그 사실을 알려 주지 않는다, 경고가 전혀 없다.
- 설명: 주어를 `nothing` 으로 놓아 "어느 장치도 알려 주지 않는다"를 한 단어로 처리합니다. `no warning is printed` 같은 수동태보다 짧고 세며, 뒤에 `because` 절로 붙여 앞의 최상급 주장을 떠받치는 자리에 잘 맞습니다.
- 예문: A git-archive packer would boot cleanly and serve mock data in production — the worst available failure mode, because nothing announces it.
- 유사어: it fails silently (가장 흔한 대체), there is no signal to catch (중립·기술), it gives you no tell (구어, 포커 어휘)
- 반의어: it fails loudly / it surfaces immediately

## "what breaks the tie"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 두 후보가 팽팽할 때 결정적 근거 하나를 꺼내며. 설계 논의·리뷰 구두 설명에 알맞습니다.
- 한국어: 승부를 가르는 것은, 결정적인 근거는.
- 설명: 스포츠의 동점(tie) 깨기에서 왔습니다. `What breaks the tie is (that) ~` 이라는 유사분열문으로 쓰면 결정 근거만 문장 앞으로 끌어올려 강조됩니다. 두 선택지를 이미 늘어놓은 뒤에 써야 자연스럽고, 처음부터 답이 뻔한 상황에 쓰면 과장으로 들립니다.
- 예문: No backend test can arbitrate between the two sign conventions, so what breaks the tie is that the frontend shifts the grid independently.
- 유사어: the deciding factor is (격식·문어), what settles it is (더 단정적), the tiebreaker (명사형)
- 반의어: it's a wash / the two are indistinguishable

## "a poor diagnostic surface"

- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-24-deploy-packaging-design.md
- 맥락: 로그·에러 형태가 문제 파악에 도움이 안 된다고 지적할 때. 도구를 새로 만드는 근거로 씁니다.
- 한국어: 진단하기 나쁜 창구, 원인 파악에 쓸모없는 출력.
- 설명: `surface` 는 여기서 "관찰자가 들여다보는 면"이라, 정보가 드러나는 창구를 뜻합니다. 크래시 로그가 있긴 한데 읽어서 원인을 못 찾는 상황을 정확히 겨냥합니다 — 정보가 아예 없는 것과는 다릅니다.
- 예문: `need-app = true` turns every boot problem into a uwsgi crash log, which is a poor diagnostic surface on a host with a slow iteration loop.
- 유사어: hard to diagnose from (평이하게 풀어쓴 형태), gives you little to go on (구어), low observability (격식·업계어)
- 반의어: a clear failure signal / one line naming the remedy

## "under-powered (a test)"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 테스트가 틀린 게 아니라 검출력이 모자란다고 구분해 줄 때. 통계 어휘를 빌린 진단 문장.
- 한국어: 검출력이 부족한, 잡아낼 힘이 모자란.
- 설명: 통계학의 statistical power(검정력)에서 왔습니다. 핵심은 **전제가 틀린 것과 표본이 약한 것을 갈라놓는다**는 점 — `The test is under-powered, not the premise wrong` 처럼 `not` 대구로 쓰면 "테스트를 고쳐라, 설계를 뒤집지 말라"가 한 문장에 담깁니다.
- 예문: The test is under-powered, not the premise wrong: one seed sits inside the rounding basin while twenty-two of thirty MSRs fall outside it.
- 유사어: not sensitive enough (평이·중립), too narrow a sample (원인을 표본 크기로 특정), it can't detect the defect it was written for (풀어쓴 형태)
- 반의어: a decisive test / adequately powered

## "fixture rot"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 고정 기대값이 오래돼 틀어진 상태를 부를 때. 테스트 실패의 원인을 분류하는 자리에서 씁니다.
- 한국어: 픽스처가 삭은 것, 고정 기댓값이 낡아 어긋난 상태.
- 설명: `bit rot`(비트 부패) 계열의 조어입니다. 코드는 정상이고 비교 기준만 낡았다는 뜻이라, 실패 원인을 코드 쪽에서 테스트 쪽으로 옮겨 놓습니다. `a fixture-rot reason` 처럼 하이픈으로 묶어 형용사로 쓰는 형태가 특히 자주 나옵니다.
- 예문: Left alone, those four would fire at the office as false failures for a fixture-rot reason rather than a real shape difference.
- 유사어: a stale expectation (가장 평이한 대체), the snapshot drifted (스냅샷 테스트 맥락), the baseline is out of date (격식·중립)
- 반의어: a current baseline / a fixture that still matches

## "promote X to blocking"

- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-24-deploy-packaging-design.md
- 맥락: 경고에 그치던 검사를 실패로 격상하는 옵션을 설명할 때. 도구 설계·릴리스 정책 문서.
- 한국어: (경고를) 차단 수준으로 승격하다.
- 설명: `advisory`(권고, 통과시키되 경고)와 `blocking`(차단, 진행 불가)의 대비가 이 표현의 뼈대입니다. 이 두 단어 쌍을 알아 두면 린터·CI·배포 게이트의 심각도 설계를 영어로 그대로 말할 수 있습니다. 승격의 반대는 보통 `downgrade to a warning`.
- 예문: `--strict` promotes every advisory to blocking — the setting to use once the transition is complete and a mock-serving bundle *should* fail the build.
- 유사어: turn warnings into errors (평이·구체적), escalate the severity (격식), fail the build on (결과 중심 서술)
- 반의어: downgrade to a warning / keep it advisory

## "trace to (a source)"

- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-24-deploy-packaging-design.md
- 맥락: 오류의 출처를 특정 문서·커밋까지 거슬러 짚을 때. 원인 규명 문서에서 씁니다.
- 한국어: ~까지 거슬러 올라간다, 출처가 ~이다.
- 설명: 자동사로 `X traces to Y`(X의 유래가 Y다)라 수동태 없이 씁니다. `trace X back to Y`(타동사, 추적하는 주체가 드러남)와 짝으로 익혀 두면 좋습니다. 책임을 묻는 어감이 아니라 계보를 밝히는 중립적 어감이라 사후 분석에 안전합니다.
- 예문: The typo traces to the in-house requirements doc the code was written from, which also contains `reutrn` and smart quotes.
- 유사어: originates in (더 격식), comes from (평이·회화), be inherited from (물려받았다는 뉘앙스)
- 반의어: was introduced here / originates with this change

## "environment-coupled"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 테스트 결과가 실행 머신 상태에 좌우된다고 지적할 때. 특히 그 사실이 명시돼 있지 않을 때.
- 한국어: 실행 환경에 묶여 있는, 머신 상태에 좌우되는.
- 설명: `coupled`(결합된) 계열의 조어로, 뒤에 `without saying so`(그렇다고 밝히지도 않은 채)를 붙이면 비판의 날이 섭니다. 같은 코드가 어떤 PC 에서는 통과하고 다른 PC 에서는 실패하는 상황을 한 단어로 명명해 줍니다.
- 예문: Those tests were environment-coupled without saying so — having the office adapters locally made the suite worse, at five seconds per Redis timeout.
- 유사어: machine-dependent (평이·중립), it depends on what's installed locally (풀어쓴 회화체), not hermetic (빌드 업계어)
- 반의어: hermetic / self-contained

## "hostname-agnostic"

- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-24-deploy-packaging-design.md
- 맥락: 산출물이 어느 주소에 올라가도 그대로 동작한다고 보장할 때. 설계 문서의 소제목·주장문.
- 한국어: 호스트명을 가리지 않는, 주소와 무관한.
- 설명: `-agnostic` 은 "그것을 알 필요도, 신경 쓸 필요도 없는"을 만드는 접미사라 `platform-agnostic`·`vendor-agnostic`·`schema-agnostic` 으로 무한히 확장됩니다. 재빌드가 필요 없다는 실무 결론을 이 한 단어가 미리 요약해 줍니다.
- 예문: The bundle is hostname-agnostic: the SPA resolves its API as the relative `/api`, so the cutover needs no rebuild.
- 유사어: portable across hosts (평이), works unchanged on either URL (풀어쓴 형태), environment-independent (격식)
- 반의어: hardcoded to one host / baked in at build time

## "treat X as binary"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 자기 판단이 성급했다고 인정할 때. 회고·자기 정정 문장에서 씁니다.
- 한국어: ~를 양자택일로 봤다, 되냐 안 되냐로만 갈랐다.
- 설명: 실무에서 값진 자기비판 틀입니다. "막혔다"를 0 아니면 1 로만 보면 부분적으로 할 수 있는 일을 놓치게 되는데, 그 사고 습관 자체를 지적하는 말. 뒤에 `decomposing it found real work I could do` 같은 결과절이 따라오면 반성이 실천으로 이어집니다.
- 예문: I'd treated "blocked" as binary — decomposing the job found a slice I could finish at home after all.
- 유사어: see it as all-or-nothing (평이·회화), take it as a yes/no question (구체적), fail to decompose it (원인 지목)
- 반의어: break it into slices / decompose the job

## "bury (real signal under noise)"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 큰 변경 더미가 중요한 수정을 가려 버린다고 설명할 때. 커밋 범위를 좁힌 이유를 대는 자리.
- 한국어: (진짜 중요한 것을) 파묻다, 묻혀서 안 보이게 만들다.
- 설명: `bury` 는 물리적으로 덮는다는 뜻이라, 삭제(delete)와 달리 **거기 있는데 안 보인다**는 점이 핵심입니다. 리뷰어의 주의력을 자원으로 보는 사고가 깔려 있어, 커밋을 쪼개는 이유를 설명할 때 설득력이 큽니다.
- 예문: Committing twenty-four files of date churn would have buried the four real fixes, so I kept only the files that actually failed.
- 유사어: drown out (소리 비유, 더 구어), lose it in the noise (평이), dilute the diff (변경 밀도 강조)
- 반의어: keep the diff legible / make the real change stand out

## "it's one sitting"

- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 남은 일의 규모가 작다고 안심시킬 때. 인수인계·일정 잡기 대화에서 씁니다.
- 한국어: 한 번에 앉아서 끝낼 분량이다, 한 타임이면 된다.
- 설명: `in one sitting`(자리에서 안 일어나고 한 번에)이 기본형이고, 위처럼 술어로 쓰면 더 짧고 구어적입니다. 시간 단위(두 시간)가 아니라 **끊기지 않는 한 덩어리**라는 점을 말해서, 여러 날 나눠 할 일이 아니라는 뜻이 됩니다.
- 예문: The exact command sequence is already in the carryover, so it's one sitting once you're at the office.
- 유사어: it's a single session (더 중립적), you can knock it out in one go (구어·활기참), it's not a multi-day job (부정으로 규모 한정)
- 반의어: it'll take several passes / it's a slog

## "at your expense"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (ec501d42)
- 맥락: 상대의 비용·시간을 축내며 계속하지 않겠다고 밝힐 때. 작업을 중단하며 이유를 대는 정중한 문장.
- 한국어: 당신 부담으로, 당신 비용을 축내면서.
- 설명: 문자 그대로 "그쪽 지갑에서 나가는 돈으로"입니다. 중단 선언에 붙이면 **게을러서가 아니라 상대를 아껴서 멈춘다**는 뜻이 되어 어감이 완전히 달라집니다. 참고로 `at the expense of X` 는 "X를 희생해서"라 뜻이 갈리니 구분해 두세요.
- 예문: The condition can't be satisfied from this machine, so I'm stopping rather than looping further at your expense.
- 유사어: on your dime (더 구어, 미국식), without spending more of your budget (풀어쓴 형태), rather than burn your time (시간에 초점)
- 반의어: at no cost to you / on my own time
