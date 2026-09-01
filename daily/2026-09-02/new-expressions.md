# 2026-09-02 — 새 표현

## "readiness"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/back-end/provider-selection.md
- 맥락: 두 개의 독립된 조건 중 "이 기능이 준비됐는가"만 따로 떼어 판정할 때(설정·배포 설계, 격식)
- 한국어: 준비 상태, (기능이) 구현되어 있는가의 판정
- 설명: `mode`(지금 어디서 도는가)와 `readiness`(그 기능이 실제로 준비됐는가)를 별개 축으로 나눌 때 쓰는 명사다. 두 질문을 하나의 스위치로 뭉치면 "환경은 맞는데 기능이 없어서" 실패하는 경우를 설명할 수 없다.
- 예문: Provider selection is the logical AND of two independent questions — mode and readiness — judged by two separate modules.
- 유사어: whether it's implemented (풀어쓴 표현), feature availability (더 넓은 개념)
- 반의어: mode (환경이 어디인가라는 별개 축)

## "a handoff"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/README.md
- 맥락: 한쪽 팀·담당자가 다른 쪽에 작업을 넘기며 지시·근거를 문서로 남길 때(프로젝트 문서, 격식)
- 한국어: 인계, 업무 넘김
- 설명: 원래 계주에서 배턴을 넘기는 동작을 가리키던 말이 프로젝트 업무 이양 전반으로 확장됐다. `handoff letter/doc` 형태로 자주 쓰여 "무엇을 어떻게 넘기는지"를 문서화한다.
- 예문: The RAG team's handoff letter listed the public API set and told us exactly which seams to fill in.
- 유사어: a transition document (더 격식), a handover (영국식 표현, 뜻은 같음)

## "fabless"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/adr/0006-page-grouping-by-domain-and-object.md
- 맥락: 반도체 산업에서 자체 생산 공장 없이 설계만 하는 회사·조직 구조를 가리킬 때(업계 용어, 격식)
- 한국어: 팹리스(자체 생산라인이 없는)
- 설명: `fab`(fabrication plant, 반도체 생산라인)이 없다(`-less`)는 뜻의 업계 표준 용어. 이 배치에서는 실제로 라우트 이름(`hideFabSidebar`)에도 녹아 있어, 조직 구조가 코드 구조에 그대로 반영된 사례다.
- 예문: As a fabless company, they design the chips but outsource all manufacturing.
- 유사어: (마땅한 대체 표현 없음 — 업계 고유 용어)
- 반의어: an IDM (integrated device manufacturer, 설계·생산을 모두 하는 회사)

## "anchored"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/planstep_r3.txt
- 맥락: 문자열 매칭 규칙이 아무 데서나 걸리지 않고 정해진 위치(끝·시작)에만 고정돼야 한다고 설명할 때(스펙 문서, 격식)
- 한국어: (문자열 끝/시작에) 고정된
- 설명: 배가 닻(anchor)을 내려 한 자리에 고정되듯, 매칭 위치를 문자열의 특정 지점(여기서는 끝)에 못 박는다는 뜻이다. `anywhere in the string`과 정반대 개념이라 정규식·검증 로직 설명에서 자주 쓴다.
- 예문: The suffix check needs to be anchored to the end of the string, or ordinary words like "BASE" get misdetected as a match.
- 유사어: pinned to (덜 기술적), fixed at (평이)
- 반의어: matched anywhere in the string

## "a golden example"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/chat_rag_contract.txt
- 맥락: 계약·스펙 문서에 "정답이 이렇게 생겼다"를 보여주는 기준 예시를 실어 둘 때(계약·테스트 문서, 격식)
- 한국어: (검증 기준이 되는) 모범 예시
- 설명: `golden`은 소프트웨어 테스트에서 "정답으로 못 박아 둔"이라는 뜻으로 굳어진 용법이다(`golden file`, `golden test`). 실제 출력과 이 예시를 비교해 계약 위반을 자동으로 잡아낸다.
- 예문: The contract module ships a golden example so both sides can verify their output against the same known-good response.
- 유사어: a reference example (더 평이), a canonical case (더 격식)
- 반의어: an edge case (경계·예외 상황)

## "over-fetch"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/chat_rag_contract.txt
- 맥락: 권한 필터링 뒤 결과가 모자랄 수 있는 문제를, 필요한 양보다 더 많이 미리 뽑아 두는 방식으로 해결한다고 설명할 때(설계 문서, 격식)
- 한국어: (필요량보다) 더 뽑아 두기
- 설명: `fetch` 앞의 `over-`는 "지나치게"가 아니라 "여유분을 두고"라는 뜻이다. 뒤 단계에서 걸러질 것을 예상하고 미리 더 많이 가져오는, 검색·페이지네이션에서 흔한 패턴이다.
- 예문: The fix isn't smarter filtering — it's adaptive over-fetch, pulling more candidates until five survive the access check.
- 유사어: fetch with headroom (덜 표준적), pad the candidate pool (풀어쓴 표현)
- 반의어: fetch exactly what's needed

## "co-location"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt back_dev_home/chat/docs/2026-08-31-chat-reply-rag-colocation.md
- 맥락: 서로 다른 두 시스템(코드베이스)을 별도 서비스로 분리하지 않고 한 프로세스 안에 같이 두는 배치를 설명할 때(설계 편지, 격식)
- 한국어: 동거 배치, 한 프로세스에 같이 두기
- 설명: `co-`(함께) + `location`(위치)의 합성어로, 네트워크 호출 없이 같은 런타임 안에 두 시스템을 두는 배치를 가리킨다. 이 문서에서는 저자가 한국어 "동거"를 직접 만들고 괄호로 원어를 병기했다.
- 예문: Co-location means the RAG repo runs inside the chat process, so there's no network hop between the two.
- 유사어: running in-process (더 구체적), sharing a runtime (풀어쓴 표현)
- 반의어: a separate service (독립된 서비스로 분리)

## "wall-clock"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt back_dev_home/chat/docs/2026-08-28-chat-to-rag-suggestions.md
- 맥락: 프로그램 내부 시간이 아니라 사람이 시계로 재는 실제 경과 시간을 가리킬 때(타임아웃·성능 논의, 격식)
- 한국어: 실제 경과 시간(벽시계 기준)
- 설명: CPU 처리 시간이 아니라 벽에 걸린 시계가 가리키는 시간, 즉 사람이 체감하는 실제 시간을 뜻한다. 타임아웃·SLA 논의에서 "CPU time"과 대비해 정확히 무엇을 재는지 밝힐 때 필수적인 구분이다.
- 예문: The agent loop is cut off at 60 seconds wall-clock, even though the actual CPU work is much shorter.
- 유사어: real time (더 평이), elapsed time (일반적)
- 반의어: CPU time

## "self-contained"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt back_dev_home/chat/docs/2026-08-31-chat-reply-rag-colocation.md
- 맥락: 외부 설정이나 다른 모듈 없이 그 자체로 완결되어 동작하는 패키지·파일을 설명할 때(기술 문서, 격식)
- 한국어: 자체 완결된, 외부 의존 없이 그 자체로 돌아가는
- 설명: `self`(스스로) + `contained`(담긴)로, 필요한 것을 전부 안에 갖고 있어 바깥에 기대지 않는다는 뜻이다. 설정 키, 자산, 코드 어느 것에나 붙을 수 있는 범용 표현이다.
- 예문: All three gateway keys are baked into `skewnono_rag/config.py`, so the package is self-contained.
- 유사어: standalone (더 평이), bundled (자산·파일 맥락에 더 맞음)
- 반의어: dependent on external config

## "a deny-list"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt back_dev_home/chat/docs/2026-09-01-chat-to-rag-structure-changes.md
- 맥락: 특정 항목을 명시적으로 걸러 거절하는 목록을 가리킬 때(보안·필터링 설계, 격식)
- 한국어: 거부 목록
- 설명: 예전에 흔히 쓰던 `blacklist`를 대체하는 중립적 표현이다. `allow-list`(허용 목록)와 짝을 이루며, 요즘 기술 문서에서는 이 쌍이 표준이 됐다.
- 예문: Obviously off-topic queries like "movies" or "the weather" get rejected by a deny-list without ever hitting search.
- 유사어: a blocklist (동의어, 최근 더 흔함)
- 반의어: an allow-list

## "prune (a list)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt back_dev_home/chat/docs/2026-08-28-chat-to-rag-ack.md
- 맥락: 배포 패키지에 실리면 안 되는 파일을 목록에서 걸러낼 때(배포·빌드 설정, 격식)
- 한국어: (목록에서) 쳐내다, 가지치기하다
- 설명: 나무의 가지를 쳐내는 원예 동사가 배포 목록·데이터 정리 전반에 쓰인다. `prune list`(제외 목록)에 파일 패턴을 넣으면 배포 패키지를 만들 때 그 파일을 통째로 빼고 담는다.
- 예문: The deploy script was about to ship a local `chat.db` on top of the cloud copy — we added `*.db` to the prune list to stop it.
- 유사어: exclude from the bundle (풀어쓴 표현), strip out (더 구어)
- 반의어: include in the bundle

## "a cold fetch"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/msr_image_ftp.txt
- 맥락: 캐시나 연결이 준비되지 않은 상태에서 처음 하는 요청의 소요 시간을 잴 때(성능 측정, 격식)
- 한국어: (캐시·연결이 없는) 첫 요청, 콜드 페치
- 설명: `cold`(달궈지지 않은)는 캐시·커넥션 풀이 준비되지 않은 상태를 뜻하고, 반대는 `warm`(이미 준비된)이다. `cold start`(첫 실행 지연)와 같은 계열의 비유다.
- 예문: A cold fetch takes 133 ms — most of that is the login round trip, not the actual transfer.
- 유사어: a cold start (더 넓은 맥락에서 쓰임)
- 반의어: a warm fetch

## "wrong-labelled"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt 4feef4b1 (타임존 수동 변환의 위험성 설명)
- 맥락: 값 자체는 맞아 보여도 붙은 표시(라벨)가 실제와 다르다고 지적할 때(디버깅·데이터 정합성 논의, 격식)
- 한국어: 라벨이 잘못 붙은
- 설명: `wrong`(틀린) + `labelled`(라벨이 붙은)의 합성어. 값의 크기나 형식은 문제 없지만 "이게 무슨 시간대다"라는 꼬리표가 사실과 어긋난다는, 아주 구체적인 종류의 오류를 가리킨다.
- 예문: Adding nine hours by hand produces a wrong-labelled value — `10:00+00:00` for what is actually a 10:00 KST event.
- 유사어: mislabelled (동의어), tagged incorrectly (풀어쓴 표현)
- 반의어: correctly tagged

## "X is the norm"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt c872b54e (파일명 검증 정규식 수정 지시)
- 맥락: 예외적으로 보이는 값이 실은 표준적이고 흔한 경우라고 짚어줄 때(코드 리뷰·지시, 구어~격식 모두)
- 한국어: X가 당연한 경우다, X가 예사다
- 설명: `norm`은 원래 "표준·기준"을 뜻하는 명사다. `X is the norm`은 "X는 예외가 아니라 늘 있는 흔한 경우"라고 선을 그어, 그것을 예외 처리하려던 이전 가정을 뒤집는다.
- 예문: The stem is an arbitrary filename, so spaces and Korean characters are the norm — don't treat them as edge cases.
- 유사어: X is standard/expected (더 평이), X is business as usual (구어)
- 반의어: X is the exception

## "discharged"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt df3be4c6 (리뷰 아티팩트 정리)
- 맥락: 처리해야 할 의무·판정이 커밋 등으로 완전히 이행되어 더 이상 남지 않았다고 말할 때(코드 리뷰·문서 정리, 격식)
- 한국어: (의무·판정이) 이행되어 해소된
- 설명: 원래 빚이나 법적 의무를 갚아 없앤다는 뜻의 격식 있는 동사다. `REQUEST-CHANGES` 같은 리뷰 판정을 "빚"처럼 표현해, 커밋으로 갚고 나면 그 기록 자체의 가치가 사라진다는 논리를 세운다.
- 예문: Once a REQUEST-CHANGES verdict is discharged in a commit, the review file's only remaining value is historical.
- 유사어: resolved (더 평이), settled (금전 비유가 남는 표현)
- 반의어: outstanding (아직 이행되지 않은)

## "cascades across (four files)"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt 5a311ce2 (타임아웃 값 변경 추적)
- 맥락: 값 하나를 바꾸면 그 여파가 여러 파일·장소로 순차적으로 번져 나간다고 설명할 때(변경 영향 분석, 격식)
- 한국어: 여러 파일에 걸쳐 연쇄적으로 번지다
- 설명: 폭포(cascade)가 위에서 아래로 이어지듯, 한 값의 변경이 자동으로 다음 자리, 또 다음 자리로 퍼진다는 그림이다. `across`가 붙어 퍼지는 범위(파일 수)까지 한 단어로 명시된다.
- 예문: The timeout number cascades across four files with a load-bearing invariant tying them together.
- 유사어: ripple through (더 부드러운 어감), propagate to (더 기계적)
- 반의어: stays contained to one file

## "double-shifted"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt 4feef4b1 (타임존 회귀 테스트 논의)
- 맥락: 시간대 오프셋이 두 번 적용되어 값이 실제보다 더 크게 어긋나는 특정 버그 유형을 가리킬 때(디버깅·테스트 설명, 격식)
- 한국어: (시간대 등이) 이중으로 밀린
- 설명: `shift`(밀다, 옮기다) 앞에 `double-`을 붙여 "한 번이 아니라 두 번 밀렸다"는 정확한 증상을 한 단어로 표현한다. 이 배치에서는 KST 문자열이 UTC로 잘못 해석된 뒤 다시 KST로 변환되어 결과가 18시간 어긋나는 버그를 가리킨다.
- 예문: A regression test exists precisely because a naive KST-stamped document would be double-shifted by the reader's `time_zone` setting.
- 유사어: shifted twice (풀어쓴 표현)
- 반의어: correctly normalized once

## "left ... residue behind"
- 레지스터: technical, casual
- 출처: transcript:skewnono-v3-nuxt df3be4c6 (worktree 정리)
- 맥락: 정리 작업이 끝난 뒤에도 흔적처럼 남아 있는 부산물을 가리킬 때(정리·클린업 보고, 캐주얼~기술)
- 한국어: 잔여물을 남기다
- 설명: 화학·물리에서 반응 후 남는 찌꺼기를 뜻하던 `residue`를 빌려, 삭제·정리 명령이 끝난 뒤에도 남는 파일·캐시를 가리킨다. `left X behind`와 짝지어 "치웠다고 생각했는데 실은 남아 있었다"는 뉘앙스를 만든다.
- 예문: `git worktree remove` deleted the tracked files but left the untracked build residue — `.nuxt/`, `node_modules/.cache` — behind.
- 유사어: leftover artifacts (더 평이), stray files (덜 비유적)
- 반의어: a clean removal

## "it's spent"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt df3be4c6 (리뷰 파일 삭제 여부 판단)
- 맥락: 물건이 물리적으로 없어진 게 아니라 그 목적을 이미 다해 더 쓸모가 없어졌다고 말할 때(정리 판단, 구어에 가까운 격식)
- 한국어: (역할을 다해서) 다 쓴, 소진된
- 설명: 화살이나 총알이 `spent`(다 써버린) 상태이듯, 문서나 작업물이 물리적으로 존재해도 목적을 다해 더 이상 가치가 없다는 판정이다. "삭제해도 되냐"는 질문에 대한 답으로 쓰기 좋다.
- 예문: No — it's spent. Its verdict already landed on `main`, so the file's only remaining value is historical.
- 유사어: served its purpose (풀어쓴 표현), no longer needed (평이)
- 반의어: still live / still in use

## "a change with cost and no effect"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt 4feef4b1 (타임존 저장 방식 변경 검토)
- 맥락: 겉보기엔 그럴듯한 변경 제안이 실제로는 아무 결과도 바꾸지 않는다고 논리적으로 반박할 때(설계 논의, 격식)
- 한국어: 비용만 들고 효과는 없는 변경
- 설명: `cost`와 `effect`를 나란히 대구로 놓아 "든 돈은 있는데 얻는 게 없다"는 판정을 한 문장으로 압축한다. 어떤 제안을 정면으로 "나쁘다"고 하지 않으면서도 채택하지 말라는 결론을 분명히 전한다.
- 예문: The offset you write is discarded after parsing — you're choosing an encoding nothing downstream reads back, which is the definition of a change with cost and no effect.
- 유사어: it buys nothing (더 짧은 관용구), all pain, no gain (구어)
- 반의어: a change that pays for itself
