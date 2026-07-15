# 2026-07-16 — 오늘의 표현

## "thin glue"
- 레지스터: technical, casual
- 출처: transcript:auto-recipe-creator agent task-4 brief
- 맥락: 자체 로직 없이 두 모듈을 이어 붙이기만 하는 얇은 코드를 설명할 때(개발 구어·PR)
- 한국어: (알맹이 로직 없이) 그저 이어 붙이는 얇은 연결 코드
- 설명: "glue code"(접착제 코드)에 thin 을 붙여, 스스로는 거의 아무 일도 안 하고 다른 것을 호출·연결만 하는 코드를 가리킵니다. 겸손하게 "별 거 아닌 이음새 코드"라고 말하는 뉘앙스.
- 예문: It is thin glue: it reads two IDs from the environment, calls the gather function, prints the log lines, and returns an exit code.
- 유사어: glue code (더 중립적), a thin wrapper (감싸기만 하는 층), plumbing (배관처럼 데이터만 흘려보내는 코드; 구어)
- 반의어: business logic / the meat of the code (실제 알맹이 로직)

## "kick off (a background job)"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-15-msr-image-tool-fetch-design.md
- 맥락: 회의·작업·백그라운드 프로세스를 격의 없이 "시작하다"라고 말할 때(회의·구어·기술)
- 한국어: (일·프로세스를) 개시하다, 발동시키다
- 설명: 축구 킥오프에서 온 표현으로, 프로젝트·회의·비동기 작업의 시작에 두루 쓰입니다. 명사형은 "kickoff / kick-off".
- 예문: The POST endpoint kicks off a fleet download in the background and immediately returns a job ID.
- 유사어: start, initiate (격식), trigger (자동 발동), set in motion (문어)
- 반의어: wrap up / wind down (마무리하다)

## "kick off a fleet download"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-15-msr-image-tool-fetch-design.md
- 맥락: 여러 대상을 한 번에 처리하는 대량 작업을 비동기로 시작한다고 말할 때(기술)
- 한국어: (여러 대상을 한꺼번에 받는) 무리 다운로드를 시작하다
- 설명: fleet 은 원래 "함대·차량 무리"인데, 여기선 "여러 host/파일을 하나의 묶음으로 처리하는 대량 작업"을 뜻합니다. fleet download, fleet downloader 처럼 씀.
- 예문: The office provider uses a fleet downloader to log in once per host and pull all images with connection reuse.
- 유사어: batch download (묶음 처리), bulk fetch (대량 수집)
- 반의어: a single-file fetch (한 건 수집)

## "circuit breaker"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/research/llm-rag-chatbot-feasibility.md
- 맥락: 반복 실패하는 원격 호출을 잠시 끊어 장애 확산을 막는 안정성 패턴을 말할 때(설계·기술)
- 한국어: (장애 확산을 막는) 회로 차단기 패턴
- 설명: 두꺼비집(전기 차단기)에서 온 비유입니다. 원격 서비스가 계속 실패하면 회로를 "열어(open)" 호출을 빠르게 실패시키고, 주기적으로 회복을 확인해 다시 "닫습니다(close)".
- 예문: When the circuit breaker opens, the system fails RAG calls fast while a health check periodically probes for recovery.
- 유사어: fail-fast guard, backpressure (부하 되밀기; 인접 개념), bulkhead (격벽; 인접 개념)

## "relay (X to the frontend)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-15-msr-image-tool-fetch-design.md
- 맥락: 받은 데이터를 저장이 아니라 곧바로 다른 쪽으로 중계·전달할 때(기술)
- 한국어: (받아서 그대로) 중계하다, 릴레이하다
- 설명: 중간에서 받아 즉시 넘겨주는 것으로, 보관이 목적이 아니라 "통과시켜 전달"하는 뉘앙스입니다.
- 예문: The goal is to relay hundreds of images to the frontend quickly rather than store them in permanent storage.
- 유사어: forward (전달), proxy (대리 중계), pass through / stream through (흘려보내다)
- 반의어: persist / store (보관하다)

## "self-describing"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-msr-image-tool-fetch.md
- 맥락: 파일·데이터가 부가 조회 없이 스스로 형식·의미를 드러내도록 설계했다고 말할 때(기술)
- 한국어: 스스로를 설명하는, (부가 정보 없이) 자기 기술적인
- 설명: 이름·확장자·헤더만 봐도 형식을 알 수 있어 별도 메타데이터 조회가 필요 없다는 뜻입니다.
- 예문: The .svg suffix makes the cached file self-describing, so the mimetype is guessable from the path on a cache hit.
- 유사어: self-documenting (코드가 주석 없이 읽힘), self-contained (자기완결적; 인접 개념)
- 반의어: opaque (내부를 알 수 없는)

## "answer-first (layout)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-skewvoir-phase-b1-measurement-overview.md
- 맥락: UI·보고서·글을 "결론부터 먼저" 보여주는 구성 원칙을 말할 때(설계·글쓰기)
- 한국어: 결론(답)부터 제시하는
- 설명: 세부·근거를 쌓기 전에 핵심 답을 맨 앞에 두는 방식입니다. 대시보드, 이메일, 보고서에 두루 쓰는 원칙.
- 예문: The team rebuilt the view as an answer-first layout that leads with a verdict strip before the supporting charts.
- 유사어: BLUF (bottom line up front; 군·비즈니스 약어), conclusion-first, top-line-first
- 반의어: bottom-up / buildup-first (근거를 쌓아 결론에 이르는)

## "match on the text, not the line number"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator agent task-5 brief
- 맥락: 위치가 바뀔 수 있으니 무엇을 기준으로 찾을지 지정할 때(코드 수정 지시·기술)
- 한국어: 줄 번호가 아니라 (그) 텍스트를 기준으로 찾아라
- 설명: 편집 지점을 고정 좌표(줄 번호)가 아니라 내용(앵커 텍스트)으로 식별하라는 지침입니다. "match on X" = X 를 매칭 기준으로 삼다.
- 예문: These are real line numbers, but a concurrent session may have shifted lines, so match on the text, not the line number.
- 유사어: anchor on the content (내용에 앵커를 걸다), key off the text (한 값을 기준 삼다)
- 반의어: rely on the line number / hard-code the position (고정 위치에 의존하다)

## "surface as (a JSON error)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-msr-image-tool-fetch.md
- 맥락: 내부 실패가 밖으로 어떤 형태로 드러나는지 규정할 때(설계·기술)
- 한국어: (내부 상태가) ~의 형태로 겉으로 드러나다
- 설명: 자동사 surface 는 "수면 위로 떠오르다 → 표면화되다"입니다. "surfaces as JSON"처럼 무엇으로 드러나는지 as 로 연결합니다. 타동사 "surface X"(드러내다)도 함께 익혀 두세요.
- 예문: Office source failure surfaces as JSON — 500 for config, 503 for unavailable, 404 for a missing image — never a fabricated image.
- 유사어: manifest as (격식), show up as, be exposed as
- 반의어: be swallowed / be hidden (조용히 묻히다)

## "invent data"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-15-skewvoir-analysis-compact-dashboard-design.md
- 맥락: 측정하지 않은 값을 보간·추정으로 만들어내는 행위를 경계할 때(데이터·계측·기술)
- 한국어: (없는) 데이터를 지어내다
- 설명: 실측하지 않은 값을 추정·보간으로 채우는 것을 "데이터를 발명한다"고 비판적으로 표현합니다. 계측 도구에서는 금기.
- 예문: Interpolating values between measured points would invent data in a metrology tool and is therefore rejected.
- 유사어: fabricate data, make up numbers (구어), synthesize values (중립·기술)
- 반의어: show only measured/real values (실측값만 보여주다)

## "on demand"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator agent task-4 brief
- 맥락: 미리가 아니라 "필요할 때 그때그때" 처리한다고 말할 때(기술·업무)
- 한국어: 요청 시에, 필요할 때 즉석에서
- 설명: 미리 준비(prefetch)해 두지 않고 요청이 올 때 계산·수집하는 방식입니다. 형용사형은 붙임표를 써서 on-demand.
- 예문: This task adds a standalone script that fetches the recipe and measurement data on demand for the offline benchmark.
- 유사어: as needed, just-in-time (적기 공급; 인접), lazily (지연 평가; 기술)
- 반의어: ahead of time / prefetched / eagerly (미리·선반영)

## "a nightly purge / purge (old cache)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-msr-image-tool-fetch.md
- 맥락: 오래된 데이터를 주기적으로 싹 비우는 운영 작업을 말할 때(운영·기술)
- 한국어: (오래된 것을) 일괄 정리·삭제하다; 그 정리 작업
- 설명: delete 보다 "쌓인 것을 주기적으로 쓸어내는" 뉘앙스입니다. 명사·동사가 같은 형태이고, cache purge / log purge 처럼 씀.
- 예문: A scheduled cron job runs a nightly purge that deletes cache files older than the retention window.
- 유사어: evict (개별 항목 축출; 기술), sweep, clear out, prune (가지치듯 일부만 정리)
- 반의어: retain / keep (보존하다)

## "honesty-gated"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-skewvoir-phase-b1-measurement-overview.md
- 맥락: 근거가 충분할 때만 정보를 노출하도록 조건을 건 설계를 말할 때(설계)
- 한국어: 정직성 조건을 건 (근거가 충분할 때만 노출되는)
- 설명: "X-gated" 는 "X 를 통과 조건으로 삼는"이라는 조어 패턴입니다(feature-gated, permission-gated 등). honesty-gated 는 데이터가 정직하게 뒷받침할 때만 표시하고 아니면 감추는 설계.
- 예문: The overview shows honesty-gated failure evidence: outlier flags appear only when the data actually supports them.
- 유사어: guarded by (조건으로 보호되는), conditional on, gated behind (뒤에 조건을 둔)
- 반의어: always-on / unconditional (무조건 노출)

## "verbatim"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator agent task-4 brief; repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-15-msr-image-tool-fetch.md
- 맥락: 한 글자도 바꾸지 말고 원문 그대로 옮기거나 인용하라고 할 때(지시·격식)
- 한국어: (한 자도 안 바꾸고) 그대로, 축자적으로
- 설명: 부사·형용사로 "원문 그대로"라는 뜻입니다. 코드·인용을 손대지 말라는 지시에 자주 등장합니다.
- 예문: The SVG body is moved verbatim from the old module, minus the caching decorator.
- 유사어: word for word, to the letter, as-is (있는 그대로)
- 반의어: paraphrased (바꿔 말한), loosely / with edits (손봐서)
