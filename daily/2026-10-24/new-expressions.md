# 2026-10-24 — 새 표현

## "pitches the whole project"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 3df93f7f (docs 폴더 위치 제안)
- 맥락: 문서·발표가 무엇을 "홍보·소개하는 글"인지 성격을 규정할 때(설계 논의·구어와 문어 모두)
- 한국어: (그 문서는) 프로젝트 전체를 소개·설득하는 글이다
- 설명: `pitch` 는 투자자·상사 앞에서 아이디어를 "파는" 행위다. 문서를 주어로 두면 "이 글은 기능 설명서가 아니라 소개용"이라는 성격 구분이 한 단어로 된다. 탭별 기능을 거기 넣으면 너무 길어진다는 근거로 이어졌다.
- 예문: `project-overview.md` pitches the whole project, so adding a section for every tab would make it too long.
- 유사어: presents (중립·격식), sells (구어, 설득 뉘앙스 강함), makes the case for (논증 쪽)
- 반의어: documents in detail (세부를 기록하다)

## "It's just stuck inside a folder for one feature."
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 3df93f7f
- 맥락: 좋은 것이 엉뚱한 자리에 묻혀 있다고 아쉬워할 때(동료와 말로·채팅)
- 한국어: 그게 그냥 한 기능 폴더 안에 갇혀 있을 뿐이다
- 설명: `stuck` 은 "끼어서 못 나온다"는 감각이라 "자리를 잘못 잡았다"는 아쉬움이 묻어난다. 앞의 `just` 가 "내용은 좋은데 위치만 문제"라고 문제 범위를 좁힌다.
- 예문: The AFM summary already has the format you want; it's just stuck inside a folder for one feature.
- 유사어: buried in (더 강한 "묻혀 안 보인다"), tucked away in (부드러움·중립), confined to (격식)
- 반의어: front and center (눈에 잘 띄는 곳에)

## "stops matching the app without anyone noticing"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 3df93f7f (README 갱신 규칙 설명)
- 맥락: 문서·인덱스가 조용히 낡아 가는 위험을 설명할 때(설계 근거·리뷰)
- 한국어: 아무도 모르는 사이에 앱과 어긋나 버린다
- 설명: `stop -ing` 로 "원래 맞았는데 어느 순간 안 맞게 된다"는 변화를 그리고, `without anyone noticing` 이 그 변화가 경보 없이 일어난다는 점을 붙인다. 규칙(탭을 고치면 표도 고친다)을 왜 적어 두는지 설득하는 한 줄이다.
- 예문: Without that rule, an index like this stops matching the app without anyone noticing.
- 유사어: silently drifts out of sync (기술 문어), quietly goes out of date (중립)
- 반의어: stays in sync (계속 맞는다)

## "would have been extra work for nothing"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 3df93f7f
- 맥락: 하지 않은 선택을 "괜히 일만 늘었을 것"이라며 정당화할 때(보고·구어)
- 한국어: 괜히 일만 늘고 얻는 건 없었을 것이다
- 설명: `would have been` 은 하지 않은 일의 결과를 가정한다. `for nothing` 은 "보상 없이, 헛되이". 둘을 묶어 "안 한 게 맞았다"는 판단을 부드럽게 전한다.
- 예문: This was a single-file change, so a worktree would have been extra work for nothing.
- 유사어: wasted effort (명사구, 중립), overkill (구어, "과했다"), not worth the overhead (격식)
- 반의어: well worth the effort (충분히 할 가치가 있었다)

## "Do you want to pick that up, or work on something else?"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 9306a6b3 (세션 재개 인사)
- 맥락: 하다 만 일을 이어 갈지 상대에게 고르게 할 때(동료·대화형 세션)
- 한국어: 그거 이어서 하실래요, 아니면 다른 거 하실래요?
- 설명: `pick (something) up` 은 "멈췄던 데서 다시 잡다". 선택지 두 개를 `or` 로 나란히 줘서 상대가 한 단어로 답할 수 있게 한다.
- 예문: You were partway through the Provision work — do you want to pick that up, or work on something else?
- 유사어: resume that (격식), carry on with it (영국식 구어), get back to it (구어)
- 반의어: drop it (그만두다), park it (일단 보류하다)

## "read-modify-write"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 9306a6b3 (설정 파일 수정 보고)
- 맥락: 파일·레지스터를 통째로 덮어쓰지 않고 읽고-고치고-쓰는 방식을 말할 때(기술 문서·보고)
- 한국어: 읽고 → 고치고 → 다시 쓰기(기존 내용 보존)
- 설명: 동시성·하드웨어에서 온 용어다. 여기서는 "JSON 을 읽어 키 하나만 넣고 다시 썼다"는 뜻으로, `instead of rewriting the file` 과 대비되어 다른 값이 그대로 남았다는 보증이 된다.
- 예문: I added the key with a JSON read-modify-write instead of rewriting the file, so nothing else in it was changed.
- 유사어: in-place update (일반), patch (구어·API 쪽)
- 반의어: overwrite (통째로 덮어쓰기), blind write

## "Calls I made that the reviewer may push on"
- 레지스터: professional
- 출처: transcript:skewnono-s1 cf64f1f6 (구현 보고)
- 맥락: 리뷰 전에 "반박이 나올 만한 판단"을 먼저 꺼내 놓을 때(보고서·PR)
- 한국어: 리뷰어가 문제 삼을 수 있는, 제가 내린 판단들
- 설명: `call` 은 "판단·결정"(make the call). `push on` 은 "그 지점을 눌러 따지다"로 `push back on`(반대하다)보다 "캐묻다"에 가깝다. 소제목처럼 써서 리뷰어의 시선을 미리 그쪽으로 모은다.
- 예문: Calls I made that the reviewer may push on, all recorded in the report: the lot column wording and the clock source.
- 유사어: decisions open to challenge (격식), judgment calls worth a second look (중립), things you might question (구어)

## "the house rules apply"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 3df93f7f
- 맥락: 팀·저장소 고유의 규칙이 여기에도 적용된다고 짚을 때(동료 간·설계 메모)
- 한국어: 우리 쪽 규칙이 그대로 적용된다
- 설명: `house rules` 는 원래 "이 집(가게)만의 규칙". 개발 맥락에서는 그 저장소의 문체·린트 규약을 가리킨다. 바로 뒤에 콜론으로 규칙 목록을 붙이는 패턴이 자연스럽다.
- 예문: These docs are for teammates, so the house rules apply: Korean with formal endings, compact tables, and `npm run lint:md` afterwards.
- 유사어: the usual conventions apply (중립·격식), our standard rules hold (격식)
- 반의어: anything goes (규칙 없음)

## "the one sanctioned exception"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt CLAUDE.md (transcript 안 Git Workflow 절)
- 맥락: 규칙에 공식 허용된 예외가 딱 하나뿐임을 못 박을 때(규약 문서·격식)
- 한국어: 공식적으로 허용된 유일한 예외
- 설명: `sanctioned` 는 "승인된·인가된". `the one` 이 "이것 하나뿐"을 강조해, 다른 예외는 없다는 함의가 생긴다. 규칙 문서에서 예외를 소개할 때 자주 쓰는 격식 표현이다.
- 예문: A worktree branch is the one sanctioned exception to "work directly on main".
- 유사어: the only approved exception (중립), the single permitted exception (격식)
- 반의어: an unsanctioned workaround (승인 안 된 우회)

## "fail-soft"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt CLAUDE.md (transcript 안 Feature-sliced Backend Layout 절)
- 맥락: 일부가 고장 나도 전체는 계속 돌게 짜인 방식을 말할 때(아키텍처 문서)
- 한국어: 부분 실패를 허용하며 계속 동작하는(방식)
- 설명: 깨진 패키지는 건너뛰고 목록에 남긴 채 앱은 뜬다는 뜻이다. `loads fail-soft` 처럼 부사로도 쓴다. 반대편 `fail-fast` 는 문제가 있으면 바로 멈춘다.
- 예문: `backend/contrib/<slug>/` loads fail-soft: a broken package is skipped and listed in the boot log.
- 유사어: graceful degradation (더 일반적·격식), best-effort (구어·기술)
- 반의어: fail-fast (즉시 실패), fail-closed

## "per your ruling"
- 레지스터: professional
- 출처: transcript:skewnono-s1 cf64f1f6 (Round 2 보고)
- 맥락: 결정권자의 판정대로 했다고 근거를 밝힐 때(보고·리뷰 응답)
- 한국어: 판정하신 대로
- 설명: `per` 는 "~에 따라"(격식). `ruling` 은 판사의 판결처럼 "공식 판정"이라, 매니저가 리뷰 쟁점을 정리해 준 상황에 꼭 맞는다. 책임 소재를 짧게 정리하는 효과가 있다.
- 예문: I kept the original wording on the lot column, per your ruling.
- 유사어: as you decided (중립·회화), in line with your decision (격식), per the manager's call (구어 섞인 업무체)

## "counts in full ink, labels may stay muted"
- 레지스터: technical
- 출처: transcript:skewnono-s1 cf64f1f6 (매니저 지시)
- 맥락: UI 에서 무엇을 진하게, 무엇을 흐리게 둘지 지시할 때(디자인 리뷰)
- 한국어: 숫자는 진한 글자색으로, 라벨은 흐린 채로 둬도 된다
- 설명: `full ink` 는 인쇄 비유로 "기본 진한 글자색". `muted` 는 채도·명도를 낮춘 보조색이다. 위계(무엇이 먼저 읽히나)를 말할 때 짝으로 쓴다.
- 예문: The Align and 측정 counts are now in full ink; the labels stay muted.
- 유사어: primary vs. secondary text color (중립·기술), bold vs. dimmed (구어)

## "One thing the manager should look at"
- 레지스터: professional
- 출처: transcript:skewnono-s2 8142838c (구현 보고)
- 맥락: 보고 끝에 결정권자가 판단해야 할 문제 하나를 따로 꺼낼 때(보고서·메일)
- 한국어: 매니저께서 봐 주셔야 할 것이 하나 있습니다
- 설명: 헤딩처럼 문장 앞에 세워 "여기부터는 내가 정할 수 없는 일"이라고 구분한다. 뒤에 콜론으로 문제와 내가 한 조치(지시대로 따르고 열린 질문에 기록)를 이어 붙인다.
- 예문: One thing the manager should look at: the 8-character label just repeats the timestamp column.
- 유사어: One item for your review (격식), One thing worth flagging (구어·업무체)

## "Commit and push whenever you judge it necessary"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt CLAUDE.md (transcript 안 Git Workflow 절)
- 맥락: 판단을 상대에게 위임하는 지시를 쓸 때(규약·위임 메모)
- 한국어: 필요하다고 판단되면 언제든 커밋·푸시하라
- 설명: `judge it necessary` 는 `judge + 목적어 + 형용사` 5형식이다. `think it necessary` 보다 "책임 있게 판단한다"는 무게가 실린다. 뒤의 `no need to ask first` 와 짝을 이뤄 권한을 넘긴다.
- 예문: Commit and push whenever you judge it necessary — no need to ask first.
- 유사어: as you see fit (격식·관용), whenever it makes sense (구어)

## "Works as specified."
- 레지스터: professional
- 출처: transcript:skewnono-s2 8142838c
- 맥락: 검증 결과를 짧게 보고할 때(진행 보고·채팅)
- 한국어: 명세대로 동작합니다
- 설명: 주어(`It`)를 생략한 보고체 문장이다. `as specified` 가 "내 생각에 괜찮다"가 아니라 "명세와 대조해 맞다"는 기준을 밝힌다. 다음 단계(서버 정지, 커밋)를 바로 이어 쓴다.
- 예문: Works as specified. Stopping the servers, committing, and writing the report.
- 유사어: Behaves as expected (중립), Matches the spec (간결·기술), All good (구어)
- 반의어: Deviates from the spec (명세와 다르다)

## "The ban is on claims, not on disclaimers."
- 레지스터: professional
- 출처: transcript:skewnono-s1 cf64f1f6 (매니저 판정)
- 맥락: 규칙의 적용 범위를 정확히 갈라 판정할 때(리뷰·규약 해석)
- 한국어: 금지 대상은 단정이지 단서 문구가 아니다
- 설명: `The ban is on X, not on Y` 로 규칙이 겨냥하는 대상을 좁힌다. `claims`(단정하는 주장)와 `disclaimers`(아니라고 밝히는 단서)는 철자가 닮아 대비가 또렷하다. "원인" 이라는 단어를 쓰되 원인이라고 주장하지 않으면 괜찮다는 판정이었다.
- 예문: The caption with 원인 stays: the ban is on claims, not on disclaimers.
- 유사어: The rule targets X, not Y (중립·격식), It's X that's off-limits, not Y (구어)

## "the code is what gets corrected"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt CLAUDE.md (transcript 안 Visual language 절)
- 맥락: 둘이 어긋날 때 어느 쪽을 진실로 볼지 정할 때(규약 문서)
- 한국어: 고쳐지는 쪽은 코드다
- 설명: `X is what gets corrected` 는 의사분열문(pseudo-cleft)이다. `the code gets corrected` 보다 "고쳐야 할 대상은 바로 코드"라는 초점이 선다. `gets` 수동은 동작(고쳐짐)을 강조한다.
- 예문: Where the code and `DESIGN.md` disagree, the code is what gets corrected.
- 유사어: the code yields (격식), the code loses (구어), the doc wins (구어, 반대 방향 표현)

## "I haven't checked that it's active yet"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 9306a6b3 (설정 변경 보고)
- 맥락: 바꾼 것과 확인한 것을 구분해 정직하게 보고할 때(보고·구어 모두)
- 한국어: 아직 실제로 적용됐는지는 확인하지 않았습니다
- 설명: 현재완료 부정 + `yet` 으로 "아직 안 했지만 할 일"이라는 여지를 남긴다. 뒤에 `one way to check is …` 로 확인 방법을 붙이면 상대가 바로 이어 갈 수 있다.
- 예문: I haven't checked that it's active yet; one way to check is to look for a 1M context limit in the next session.
- 유사어: This is unverified so far (격식), I haven't confirmed it took effect (중립)
- 반의어: I've confirmed it's live (적용 확인함)

## "a little different from what you named"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 3df93f7f
- 맥락: 상대가 말한 목록·이름이 실제와 조금 다르다고 부드럽게 정정할 때(동료와 대화)
- 한국어: 말씀하신 것과 조금 다르다
- 설명: `a little` 로 정정을 완충하고, `what you named` 로 "당신이 든 이름들"을 하나로 묶는다. 근거(`The tabs come from FeatureTabs.vue`)를 앞에 두면 상대 탓이 아니라 출처 차이로 읽힌다.
- 예문: The tabs come from `FeatureTabs.vue`, so the list is a little different from what you named.
- 유사어: slightly off from what you listed (구어), differs somewhat from your list (격식)
- 반의어: exactly what you named (말씀하신 그대로)
