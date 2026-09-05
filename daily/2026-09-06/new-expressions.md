# 2026-09-06 — 새 표현

## "it does not get a fresh one"
- 레지스터: technical, professional
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 새로 붙는 컴포넌트가 자기 몫의 자원을 따로 받는 게 아니라 기존 예산을 나눠 쓴다고 못박을 때(설계 문서·격식)
- 한국어: 별도로 하나 더 받는 게 아니다.
- 설명: 앞 문장에서 "borrows from that same budget" 이라 해 놓고 대시 뒤에 이 말을 붙이면, 독자가 흔히 하는 오해("어차피 프로세스가 늘면 메모리도 늘겠지")를 한 문장으로 닫는다. `fresh` 가 "새것 · 아직 안 쓴" 을 동시에 담아 `separate` 보다 예산 뉘앙스가 산다.
- 예문: The proxy borrows from that same per-worker budget — it does not get a fresh one.
- 유사어: it shares the existing budget (중립·설명적), there is no separate allocation for it (더 격식·회계 어투), it rides on the same envelope (구어에 가깝고 인프라 문맥 전용)
- 반의어: it runs on its own worker (자기 몫의 자원을 따로 받는다)

## "briefly co-resident"
- 레지스터: technical
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 메모리 피크를 설명할 때, 두세 벌의 사본이 "짧은 순간 동시에" 떠 있어서 순간 사용량이 튄다고 짚는 자리(격식)
- 한국어: 잠깐 동시에 메모리에 떠 있는.
- 설명: `co-` 가 "함께", `resident` 가 "상주" 라서 메모리 용어로 굳었다. 앞에 `briefly` 를 붙이는 게 핵심 — 총량이 아니라 **겹치는 순간**이 문제라는 뜻이 되어, 왜 평균이 아니라 피크를 봐야 하는지가 설명된다.
- 예문: The response is JSON with base64'd bytes — roughly a 3x transient over the batch's raw bytes (raw buffer + base64 string + serialized JSON copy, briefly co-resident).
- 유사어: alive at the same time (평이·회화), held simultaneously (중립·격식), overlapping in memory (덜 굳은 표현이라 설명이 붙어야 한다)
- 반의어: freed before the next allocation (다음 할당 전에 해제되어 겹치지 않는다)

## "at the ... cliff"
- 레지스터: technical
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 임계값을 조금만 넘으면 성능이 완만히 나빠지는 게 아니라 뚝 떨어진다고 경고할 때(설계 리뷰·격식)
- 한국어: (수치) 임계선 바로 앞까지 간다 / 절벽에 걸린다.
- 설명: `limit` 이나 `threshold` 는 넘으면 어떤 일이 나는지 말해 주지 않는데, `cliff` 는 "넘는 순간 급락" 을 그림으로 준다. 워커 재활용, OOM kill 처럼 **점진적이지 않은** 실패를 가리킬 때 정확한 단어다.
- 예문: A batch landing several large hosts reaches ~1.4 GB transient — at the `reload-on-rss=1500` cliff — and can recycle the worker mid-request.
- 유사어: right at the limit (평이·중립), within the margin of the cap (더 격식·완곡), one bad batch from an OOM (구어체·극적)
- 반의어: with comfortable headroom (여유가 넉넉하다)

## "mid-request"
- 레지스터: technical
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 장애가 "요청을 처리하는 도중" 터져서 그 요청이 통째로 날아간다는 걸 한 단어로 표현할 때
- 한국어: 요청 처리 도중에.
- 설명: `mid-` 접두사는 하이픈 하나로 부사구를 만든다(`mid-flight`, `mid-migration`, `mid-review`). "in the middle of a request" 보다 짧고, 무엇보다 뒤에 오는 피해("failing the whole batch")와 인과가 붙어 읽힌다.
- 예문: It can recycle the worker mid-request, failing the whole batch and potentially disrupting an in-flight pandas task in that worker.
- 유사어: in the middle of a request (평이·회화), while a request is still in flight (더 길지만 그림이 선명), before the response is returned (결과 기준 서술)
- 반의어: between requests (요청과 요청 사이, 즉 안전한 시점)

## "if X changes materially"
- 레지스터: professional, technical
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 지금 내린 결정이 언제 무효가 되는지 조건을 걸어 둘 때. ADR·계약서·정책 문서의 정형구(격식)
- 한국어: 사정이 실질적으로 달라지면.
- 설명: `materially` 가 "결과를 바꿀 만큼" 을 담아, 사소한 변동으로 결정을 다시 뒤집지 말라는 방어선을 같이 친다. `if it changes` 라고만 쓰면 아무 변화에나 재검토를 요구하는 문장이 된다.
- 예문: If the file profile changes materially — many hosts each dumping several 10MB+ files — small batches stop being enough.
- 유사어: if the picture shifts (구어·비유), should the assumptions no longer hold (아주 격식·문어), if this stops being true (평이하고 직설적)
- 반의어: for minor fluctuations, leave it alone (사소한 변동에는 손대지 않는다)

## "do not 'optimize' X back up"
- 레지스터: technical, professional
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 미래의 누군가가 "이건 너무 보수적인데" 하며 되돌릴 게 뻔한 설정에 미리 못을 박을 때(코드 주석·ADR)
- 한국어: 이 값을 '최적화' 한답시고 도로 올리지 마라.
- 설명: 따옴표가 문장의 무게중심이다 — optimize 를 인용부호로 감싸 "본인은 최적화라 믿겠지만 아니다" 를 비꼬지 않고 전달한다. 영어 기술 문서에서 scare quotes 가 정확히 이 용도로 쓰인다.
- 예문: Do not "optimize" `request_batch` back up without re-checking the `reload-on-rss` / pandas-stacking math above.
- 유사어: resist the urge to raise this (부드럽고 격식 있음), leave this number alone (짧고 단호한 구어), this is not a tuning knob (규칙 선언조)
- 반의어: tune this freely for your workload (마음껏 조정해도 되는 값)

## "not left to the call site"
- 레지스터: technical
- 출처: repo:equipment-data-map ftp_handler/docs/adr/0001-proxy-batch-sizing.md
- 맥락: 기본값을 라이브러리 안에 박아 둔 이유를 밝힐 때. 호출자에게 판단을 떠넘기지 않겠다는 설계 선언(격식)
- 한국어: 호출부의 판단에 맡기지 않는다.
- 설명: `leave it to X` 는 "X 가 알아서 하게 두다" 인데, 부정형으로 쓰면 그게 무책임이라는 뜻이 된다. 뒤에 붙는 `because the defaults exist to give a caller who hasn't done this math a safe result` 가 이유를 대는 정석 구조다.
- 예문: These are baked in as defaults in `ftp_flask_downloader.py`, not left to the call site.
- 유사어: the library decides, not the caller (대비를 앞세운 평이한 버전), safe by default (짧은 슬로건), the caller shouldn't have to know this (호출자 입장에서 서술)
- 반의어: configurable per call (호출마다 지정하게 열어 둔다)

## "extra dependency surface"
- 레지스터: technical, professional
- 출처: repo:llm_serving docs/03-ocr-and-parser-services.md
- 맥락: 도구 하나를 더 들이는 비용을 "코드가 는다" 가 아니라 "관리해야 할 면적이 는다" 로 표현할 때(도입 검토·격식)
- 한국어: 추가로 떠안는 의존성 부담.
- 설명: `surface` 는 attack surface 에서 온 비유로, 세로로 세는 개수가 아니라 **노출된 면적**을 가리킨다. 버전 충돌·보안 패치·빌드 실패까지 한 단어로 묶여서 리스크 절에 잘 어울린다.
- 예문: Main concerns: extra dependency surface compared with plain `vLLM`, a separate deployment contract, and AGPL-3.0 implications.
- 유사어: more moving parts (구어·비유적), an additional maintenance burden (격식·중립), one more thing to keep patched (아주 구체적·회화)
- 반의어: no new dependencies (의존성이 늘지 않는다)

## "should not be treated as another X"
- 레지스터: professional, technical
- 출처: repo:llm_serving docs/03-ocr-and-parser-services.md
- 맥락: 겉모습이 비슷해서 같은 범주로 오해받는 도구의 자리를 바로잡을 때(문서·격식)
- 한국어: 또 하나의 X 취급을 하면 안 된다.
- 설명: `another` 한 단어가 "이미 여럿 있는 그 부류" 를 불러와, 오해를 굳이 서술하지 않고도 부정한다. `is not an X` 보다 부드러우면서 경계는 더 분명하다.
- 예문: It should not be treated as another general-purpose chat VLM.
- 유사어: don't file it under X (구어·분류 비유), it plays a narrower role than X (완곡·설명적), it is purpose-built for Y (긍정형으로 뒤집은 버전)
- 반의어: it can be swapped in wherever X is used (X 자리에 그대로 넣어 써도 된다)

## "best treated as X, not a mandatory part of Y"
- 레지스터: professional
- 출처: repo:llm_serving docs/03-ocr-and-parser-services.md
- 맥락: 도입은 하되 필수 구성에서는 빼자고 권고할 때. 결론 절의 마무리 문장(격식)
- 한국어: 필수 구성이 아니라 선택 요소로 두는 게 낫다.
- 설명: `best treated as` 는 `we recommend` 없이 권고를 담는 수동태 관용구다. 뒤에 `not ...` 대비를 붙여 "쓰지 말자" 와 "무조건 넣자" 양쪽을 한 번에 배제하는 게 이 문형의 쓸모다.
- 예문: Because of that, OmniParser is best treated as an optional parser service, not a mandatory part of the base serving stack.
- 유사어: keep it optional (짧은 구어), it belongs in the nice-to-have tier (덜 격식·비유), adopt it case by case (조건부 도입 뉘앙스)
- 반의어: it belongs in the base stack (기본 구성에 넣어야 한다)

## "field report"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/runbooks/mai_ui_2b_vs_8b_bench.md
- 맥락: 논문 수치나 벤치마크가 아니라 **실제로 굴려 본 사람의 후기**를 찾는다고 말할 때
- 한국어: 실사용 후기 / 현장 보고.
- 설명: `field` 가 연구실 밖 실전을 가리켜서, benchmark 와의 대비가 단어 하나로 선다. "후기가 없다" 를 근거로 "그래서 직접 재야 한다" 로 넘어가는 논증에서 이 단어가 축이 된다.
- 예문: I could not find a single field report comparing the 2B and the 8B on real desktop automation.
- 유사어: real-world write-up (평이·회화), production experience (격식·이력 강조), war story (아주 구어적이고 실패담 뉘앙스)
- 반의어: published benchmark numbers (저자 발표 벤치 수치)

## "typical warning signs"
- 레지스터: technical, professional
- 출처: repo:llm_serving docs/01-runtime-layout-and-capacity.md
- 맥락: 런북에서 증상 목록을 열기 직전에 쓰는 머리말. "이게 보이면 이걸 의심하라" 를 여는 자리
- 한국어: 흔히 나타나는 경고 신호.
- 설명: `symptoms` 는 이미 병이 난 뒤지만 `warning signs` 는 아직 원인이 확정되지 않은 단계라서, 진단으로 넘어가는 목록의 머리말로 정확하다. `typical` 이 "이게 전부는 아니다" 를 미리 깔아 준다.
- 예문: Typical warning signs: `EngineCore ... died unexpectedly`, API server exits before first successful request, kernel OOM entries in `dmesg`.
- 유사어: things to watch for (평이·회화), common failure modes (더 기술적·분류 지향), the usual tells (구어·탐지 뉘앙스)
- 반의어: confirmed root cause (원인이 확정된 상태)

## "keeps the GPU busy across incoming requests"
- 레지스터: technical
- 출처: repo:llm_serving docs/01-runtime-layout-and-capacity.md
- 맥락: 최적화 기능을 설명할 때, 내부 구현이 아니라 "그래서 자원이 놀지 않는다" 는 효과로 요약하는 자리
- 한국어: 들어오는 요청들을 가로질러 GPU 를 계속 일하게 한다.
- 설명: `keep + 목적어 + 형용사` 는 상태를 유지시킨다는 사역 구문이다. 여기서 진짜 일하는 단어는 `across` — 요청 하나 안이 아니라 **요청들 사이의 빈틈**을 메운다는 continuous batching 의 요점을 전치사가 담는다.
- 예문: Continuous batching keeps the GPU busy across incoming requests.
- 유사어: avoids idle gaps between requests (부정형으로 같은 뜻), maximizes utilization (격식·지표 어투), no dead time on the card (아주 구어적)
- 반의어: the GPU sits idle between requests (요청 사이에 GPU 가 논다)

## "must stay client-side independent"
- 레지스터: technical, professional
- 출처: repo:llm_serving docs/04-operations-integration-and-benchmarking.md
- 맥락: 모듈 경계를 규칙으로 못박을 때. 리뷰에서 "이 import 는 안 된다" 의 근거가 되는 한 줄
- 한국어: 클라이언트 쪽 독립성을 유지해야 한다.
- 설명: `stay` 가 `be` 대신 쓰인 게 핵심 — 지금은 지켜지고 있고 **앞으로도 그래야 한다**는 시간 축이 들어간다. 뒤에 금지 사항(`should not import ...`)을 붙이면 규칙이 검증 가능해진다.
- 예문: `poc/work2` must stay client-side independent; it should not import server-side `flask_api` code or depend on server env files.
- 유사어: keep the two sides decoupled (평이·설계 어투), no server imports on the client path (규칙을 그대로 적은 버전), the boundary is one-way (경계의 성질로 서술)
- 반의어: the client may reach into server internals (클라이언트가 서버 내부를 참조해도 된다)
