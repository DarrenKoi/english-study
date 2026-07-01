# Technical register

엔지니어링·통계·API 맥락의 전문 용어와 표현.

## 2026-06-17
- **single source of truth** — 단일 진실 공급원(SSOT). [→ daily](../../daily/2026-06-17/new-expressions.md)
- **a row count separate from the row payload** — 데이터(payload) 와 별도의 행 개수(총계).
- **first-class** — 일급 객체 / 정식 지원 대상.
- **worst-case** — 최악값 기준.
- **overfit / rank-deficient** — 과적합 / 행렬 계수 부족.
- **borrow strength** — 유사 그룹의 정보를 빌려 추정을 안정화.
- **human-readable** — 사람이 읽을 수 있는 (vs machine-readable).
- **must implement these contracts identically** — 계약을 동일하게 구현.

### auto_recipe_creator 배치
- **anchor on (the first idea)** — 처음 가설에 고착되다 (anchoring 편향).
- **carry lock-in** — (기술 선택이) 종속을 수반하다.
- **load-bearing** — 빠지면 전체가 무너지는 핵심. 반대 `lean`.
- **fail-safe** — 불확실하면 안전한 거부로 떨어지는 설계.
- **create X lazily — only when needed** — 최초 필요 시점까지 생성을 미루다.
- **measure first, fix second** — (성능) 측정이 먼저, 수정은 그 다음.

### auto_recipe_creator 배치 (추가 발굴)
- **deep module / shallow module** — 작은 인터페이스+큰 구현(깊음) vs 껍데기(얕음).
- **the interface is the test surface** — 공개 인터페이스를 통해 테스트하라.
- **tracer bullet (vertical slice)** — 끝에서 끝까지 관통하는 가장 얇은 한 줄기 구현.
- **never refactor while RED; get to GREEN first** — 실패 중엔 리팩터 금지, 통과부터.
- **progressive disclosure** — 핵심만 먼저, 상세는 단계적으로 드러내는 설계.
- **hot path** — 가장 자주/성능에 민감하게 도는 핵심 실행 경로.

### auto_recipe_creator 배치 (4회차: grill-with-docs)
- **stress-test (a plan/scenario)** — 극단 시나리오로 두드려 약점을 찾다.
- **don't couple X to Y** — 두 관심사를 서로 얽매지 마라 (loose coupling).
- **pin down (a faint box)** — 흐릿한 것을 정확히 짚어내다.
- **benchmark against (real data)** — 실데이터를 기준으로 성능을 재다.

## 2026-06-18 — wiki_for_office 아키텍처 + ML 설계 spec 배치
- **degrade gracefully / graceful degradation** — 의존 서비스가 없어도 죽지 않고 품질만 낮춰 계속 동작.
  - 예: When the glossary service is unreachable, retrieval degrades gracefully — it just skips acronym expansion instead of failing the whole query.
- **safe by construction** — 검사가 아니라 구성 방식 자체로 안전(≈ made structurally impossible).
  - 예: The two-repo split is safe by construction: there is simply no public remote for the content to leak through.
- **silently drift** — 기준에서 소리 없이(경고 없이) 어긋나다 / 표류하다.
  - 예: A fact pinned to a regenerable extract can silently drift while still looking properly cited.
- **opt-in, default-OFF** — 직접 켜야 동작하고 기본값은 꺼짐 (안전 기본값).
  - 예: Auto-capture is an opt-in, default-OFF per-user toggle, so nothing is recorded unless the user turns it on.
- **shadow mode** — 결정에 반영하지 않고 점수/결과만 기록하며 검증하는 출시 단계.
  - 예: We'll ship the scorer in shadow mode first — it logs a score on every match but doesn't change the ranking.
- **kill switch** — 문제 시 즉시 비활성화하는 비상 플래그 (보통 로드 실패 시 자동 폴백과 짝).
  - 예: The metric scorer is flag-gated with a kill switch: if the model fails to load, it falls back to the old reranker and logs a warning.
- **sit behind (an interface)** — 구현이 우리가 소유한 인터페이스 뒤에 가려져 교체·테스트 가능.
  - 예: Company services sit behind wiki-owned interfaces, each with a real and a fake implementation, so the core stays testable off the company network.
- **train/serve skew** — 학습 때와 추론 때 입력 처리가 달라 생기는 성능 괴리.
  - 예: We extract candidate patches with the same function at train and serve time to keep train/serve skew to a minimum.

## 2026-06-19 — wiki 아키텍처 + 장기실행 리소스 진단 배치
- **derived and disposable** — 원본에서 파생된 것이라 버려도(지웠다 다시 만들어도) 되는 (↔ canonical). 흔히 `rebuildable`이 따라옴.
  - 예: Canonical knowledge is human-curated Markdown; all search structures are derived and disposable.
- **a thin client (thin capture client)** — 로직을 최소화해 캡처·전송만 하는 가벼운 단말 (↔ thick/fat client).
  - 예: Each user runs a thin capture client that grabs the screen and ships images over an authenticated channel.
- **X is metadata only** — 그 필드는 *기록만* 하고 강제(enforcement)는 안 한다고 범위를 좁히는 표현.
  - 예: `visibility` is metadata only; there is no ACL enforcement in v1.
- **edge-triggered** — 매 주기가 아니라 *상태가 바뀌는 순간*에만 발동 (↔ level-triggered / polled every cycle).
  - 예: The expensive work is edge-triggered: it only runs when a new align-fail appears, not on every poll.
- **grow without bound** — 상한 없이 한없이 커지다 (자원 누수 진단어; ↔ bounded/capped). 동의어 `grow indefinitely`.
  - 예: The only thing that grows without bound is the filesystem, since nothing ever deletes the capture folders.

## 2026-06-20 — skewnono 하드웨어 mock spec/plan + auto_recipe modality 배치
- **blast radius** — (코드) 변경이 건드리는 영향 범위/파장. "작다(contained)"가 좋다. ↔ contained/localized change.
  - 예: The blast radius is contained: only the hardware route changes, and pm_planning is left untouched.
- **faithful (to the source)** — 오타·메타데이터까지 원본 그대로 충실한. ↔ simplified/lossy.
  - 예: These are faithful raw docs — every field is preserved, including the source misspelling "Ellipicity".
- **as-of (date / snapshot)** — 특정 *시점 기준*의 값(회계·데이터의 "as of June 1"). ↔ time-series.
  - 예: The mdc service returns a single as-of snapshot — the settings effective at or just before `end`.
- **deep-link-ready** — URL 파라미터로 특정 화면·상태를 바로 열 수 있게 준비된. ↔ lands on the default view only.
  - 예: The hardware page reads `eqp_id`/`start`/`end` off the query so it is deep-link-ready.
- **orthogonal** — 서로 간섭하지 않고 독립적인. ↔ coupled/entangled.
  - 예: L1 is orthogonal and unconditional — it improves classification without touching the localization path.
- **thread (a value) through** — 인자를 여러 호출 계층에 죽 꿰어 전달하다.
  - 예: We thread `start` and `end` through `get_hardware_service` so the provider receives the time window.
- **exercise (a code path)** — 특정 코드 경로를 실제로 실행시켜 동작을 검증하다. ↔ leave it untested.
  - 예: This runs on the office Windows machine, so I couldn't exercise the actual capture path here.
- **best-effort** — 되면 좋고 실패해도 전체를 막지 않는 비보장 작업(형용사). ↔ guaranteed/blocking.
  - 예: Gathering the consensus images is a best-effort step — if it fails, the loop keeps the existing cache and moves on.
- **trade-off curve** — 단일 평균값이 아니라, 한 축을 올리면 다른 축이 깎이는 맞교환 관계 곡선 전체. ↔ free lunch/win-win.
  - 예: The digest must report the act/abstain trade-off curve, not just a single in_topk number.
- **ground truth** — 모델 출력과 비교하는 검증된 실제 정답값(참값·정답 레이블). ↔ prediction/estimate.
  - 예: Even when the template is placed exactly at the ground-truth location, the best chamfer peak still drifts 67% of the time.
- **fast-follow** — 출시 직후 곧바로 이어 할 후속 작업. ↔ out of scope.
  - 예: The set composable is built switcher-ready, so the switcher itself is a clean fast-follow.
- **well-established** — 이미 표준으로 정립·검증된 기법. ↔ ad hoc / experimental.
  - 예: The overall pattern is well-established and sound.
- **hand-tuned** — 원리 유도가 아니라 사람이 손으로 맞춘. ↔ derived / calibrated.
  - 예: The individual score components are reasonable but hand-tuned rather than derived from a published metric.
- **cold-start values** — 실데이터 보정 전 초기 가동 기본값. ↔ calibrated values.
  - 예: The 0.50 accept threshold and scorer weights are cold-start constants, not calibrated decision boundaries.
- **ad hoc** — 그 경우만을 위한 임시변통의. ↔ principled / systematic.
  - 예: The best-3-plus-worst weighting is explicitly ad hoc tolerance for one broken side.
- **the main fragility is X** — "가장 큰 취약점은 ~다" 결론 문형.
  - 예: The main fragility is the area-first pruning, which can discard a valid box before scoring.
- **ordered by severity** — (목록을) 심각도 순으로 정렬함.
  - 예: The concerns below are ordered by severity, with the most damaging one first.
- **quarantined** — 위험·플랫폼 종속 코드를 한곳에 격리해 전파를 막다. ↔ entangled.
  - 예: The Windows-only `rcs/` package is quarantined, so nothing in `vision` drags in a Windows dependency.
- **transitively pull in** — 의존성을 간접적으로 줄줄이 끌어오다.
  - 예: Importing the CV matcher would transitively pull in `pywinauto`, and nothing would run on your Mac.
- **drill into / drill down** — 요약 뷰에서 세부로 파고들다. ↔ zoom out / roll up.
  - 예: Show the overlap grid first, then drill into a parameter's attribute matrix.
- **seeded from** — 초기 상태를 다른 출처의 값으로 미리 채워 시작한. ↔ empty by default.
  - 예: It is a persistent multi-select working set, seeded from the search page.
- **swap surface** — 나중에 통째로 갈아끼울 의도로 격리해 둔 코드 경계. ↔ frozen/internal core.
  - 예: The office team swaps `data.py` later, so we keep it as the single swap surface.
- **thin wrapper** — 자체 로직 없이 인자만 넘기는 얇은 위임 계층. ↔ fat layer.
  - 예: The page is a thin wrapper that extracts the route param and delegates to the view component.
- **drift (from)** — 같아야 할 두 사본이 시간이 지나며 조금씩 어긋남. ↔ stay in sync / in lockstep.
  - 예: Review risk: the inlined block can drift from `recipeView.ts` if its field lists change.
- **keep ... in sync** — 한쪽을 바꾸면 다른 쪽도 같이 고쳐 일치를 유지하다. ↔ let it drift.
  - 예: The inlined metadata carries a "KEEP IN SYNC" comment so it tracks the source file.
- **byte-identical** — 비트·바이트까지 완전히 같은(무변경 회귀 보증). ↔ approximately equal / lossy.
  - 예: With a zero offset the behavior is byte-identical to the current code, pinned by a regression test.
- **content-addressed (storage)** — 내용 해시를 키로 쓰는 저장(자동 dedup·무결성 검증). ↔ location/path-based.
  - 예: Using the SHA-256 hash as the key makes the store content-addressed, so identical uploads dedupe automatically.
- **degrade silently, never crash the loop** — (오류로) 죽지 않고 조용히 기능을 낮춰 견디다. ↔ crash hard / blow up.
  - 예: The glue follows a "module absent → degrade silently, never crash the loop" philosophy, so a missing downloader looks identical to a working-but-empty one.
- **the last leaf in a chain** — 이미 존재하는 호출 사슬의 맨 끝 말단 노드. ↔ the entry point / the root.
  - 예: Your two functions are the last leaf in a chain that already exists — the loop never imports them directly.
- **burn the (full) retry budget** — 재시도 횟수·시간 예산을 (성과 없이) 다 써버리다. ↔ bail out early.
  - 예: A genuinely-empty msr burns the full retry budget waiting for nothing.
- **gathering ≠ using** — 모으는 것과 (실제로) 쓰는 것은 별개다. (게이트가 끼었을 때)
  - 예: So gathering ≠ using — you need at least three valid S images per modality past the build gate.
- **manufacture lift** — 자유 파라미터를 만져 성능 개선을 인위적으로 지어내다(경계 표현). ↔ a genuine gain.
  - 예: Fewer free parameters means less room to manufacture lift, so a gain is more likely real.
- **X proposes, Y disposes** — 한쪽이 후보를 제안하고 다른 쪽이 최종 결정한다(역할 분담 관용 패턴).
  - 예: The two stages follow one rule: the VLM proposes the region, and the CV disposes by locking onto the exact border pixels.

## 2026-06-26 — auto_recipe_creator re-registration 스펙 배치
- **calibration-fragile ↔ calibration-light** — 임계값·설정에 *민감해 깨지기 쉬운* ↔ *튜닝이 거의 필요 없는* 지표. (`X-fragile`/`X-light` 합성 패턴)
  - 예: Its tier floors are calibration-fragile, so a cleaner, calibration-light signal is preferred.
- **the payload for (X rows)** — 어느 케이스에서 *정작 쓸모 있는 알맹이*가 무엇인지 지정(네트워크 payload 비유). ↔ boilerplate / filler.
  - 예: The whitebox suggestion is the payload for NEW_REGION rows; FRESH_SNAPSHOT rows don't need one.
- **ambiguous by construction** — 우연이 아니라 *구조상 필연적으로* 모호한 (cf. safe by construction). ↔ distinctive / unambiguous.
  - 예: If the matcher can't rank the true point #1 even on a clean frame, the key is ambiguous by construction.

## 2026-06-27 — skewnono outlier 설계/plan + auto_recipe document_extraction 배치
- **fall back to (X) / fallback** — 기본 경로가 막히면 더 안전·단순한 방법으로 내려앉다. 명사·형용사는 한 단어 `fallback`. ↔ the primary/happy path.
  - 예: When MAD is zero, the function falls back to a mean-absolute-deviation rule instead of dividing by zero.
- **mask itself (masking)** — 극단값 하나가 평균·표준편차를 부풀려 자기 자신을 임계 밖에 못 잡게 숨기다. ↔ get flagged / stand out.
  - 예: A single extreme value can mask itself when classic mean±std inflates the threshold past it.
- **resistant to / robust to (X)** — 노이즈·이상치·입력 변동에도 결과가 망가지지 않는. ↔ fragile / sensitive to / brittle.
  - 예: Median and MAD are resistant to a few extreme values the way mean and std are not.
- **inflate (a statistic / threshold)** — 소수의 큰 값이 분산·임계치를 실제보다 키우다(부정적). ↔ deflate / pull down.
  - 예: A couple of outliers inflate the threshold, so genuine anomalies no longer cross it.
- **surgical (개입·변경)** — 전부 휘젓지 않고 모호한 한 점만 정밀하게 손대는 절제된 개입. ↔ sweeping / wholesale.
  - 예: The VLM's role is surgical: it only captions figures and reconciles ambiguous tables, nothing else.
- **sanity check** — 정밀 검증 전, 크게 어긋난 데 없나 싸게 보는 1차 점검. cf. smoke test. ↔ full validation.
  - 예: If Chromium won't run, render to HTML first as a quick sanity check before debugging further.
- **round-trip (roundtrip)** — 원본→변환→재복원의 왕복 변환(복원 충실도 평가 맥락). ↔ one-way conversion.
  - 예: The round-trip is lossy: shapes and SmartArt can't survive the Markdown stage, so we re-insert them as cropped images.
- **self-hosted** — 외부 클라우드가 아니라 자체 인프라에서 직접 띄운 모델·서비스. ↔ cloud-hosted / vendor-hosted.
  - 예: External cloud VLMs are off-limits, so the pipeline runs only on self-hosted models inside the company network.
- **framework-free pure util** — 런타임 의존 0이라 어디서든 단위 테스트 가능한 순수 함수 모듈. ↔ framework-coupled / runtime-bound.
  - 예: The detector is a framework-free pure util, so it can be unit-tested with node --test off the app entirely.

## 2026-06-28 — auto_recipe_creator 트랜스크립트 + skewnono journal 배치
- **a recall illusion** — 후보엔 정답이 있지만 1순위로 못 뽑는데도 지표(in_topk)가 좋아 보이는 착시. ↔ a production-faithful metric.
  - 예: A high in_topk with a low rank-1 is a recall illusion — the true point is in the pool but never ranked first.
- **downstream consumer** — 파이프라인에서 앞 단계 출력을 받아 쓰는 뒷단 모듈(상류 생산↔하류 소비). ↔ upstream producer / source.
  - 예: The report is the downstream consumer of the eval's conclusions — it ingests the rank-1 numbers rather than recomputing them.
- **ingest (X) and turn it into (Y)** — 앞 단계 산출물을 받아들여 다른 형태로 가공하다(재계산 아님, 소비). ↔ emit / re-derive.
  - 예: It doesn't re-derive the conclusions; it ingests the eval's output and turns it into an action list.
- **gotcha (banked)** — 디버깅 중 발에 걸린 함정을 다음을 위해 기록해 둠(엔지니어 메모). cf. footgun.
  - 예: Gotcha banked: binding a control to a ref that arrives through a prop trips the no-mutating-props lint.
- **a gated cascade** — 통과 조건(gate)을 만족할 때만 다음 단계로 넘기는 단계형 구조. ↔ a flat single-pass pipeline.
  - 예: The answer isn't "DL or VLM" — it's a gated cascade where the peak-isolation predictor is the trigger.
- **a negative-control arm** — 효과가 없어야 정상인 대조 팔; "향상"이 보이면 측정이 허상임을 드러냄. ↔ the treatment arm.
  - 예: Run soft-voting heatmap accumulation as a negative-control arm before crediting the bank for the lift.
- **circular (by construction)** — 전제가 곧 결론이라 아무것도 입증 못 하는 순환 논리. ↔ an independent check.
  - 예: Reporting support on the selected winner is circular: the mechanism selects supported clusters, then observes support.
- **the operating point** — 실제로 행동을 결정하는 동작점·임계점(평균 성능이 아니라). ↔ aggregate / average performance.
  - 예: The gap is trustworthiness at the operating point, not the average matching score.
- **bit-parity / byte-for-byte identical** — "대충 같다"가 아니라 비트 단위로 완전히 동일한 동작. ↔ subtly divergent / drifted.
  - 예: The E proposer call must stay bit-parity with the existing matcher, so a precomputed input yields byte-identical behavior.
- **short-circuit (the None case)** — 이른 조건에서 나머지 계산을 건너뛰고 곧장 반환하다. ↔ fall through / run to completion.
  - 예: `_free_search_best_score` returns None only on empty candidates, so the aggregator short-circuits before taking a median.
- **a None-sentinel guard** — None 을 "값 없음" 표시값으로 두고 분기하는 방어 코드. (유사어: a null check)
  - 예: The four new knobs have non-None defaults, so unconditional `setdefault` can never stringify a sentinel.
- **upgrade-only (it must never downgrade)** — 상태를 상향만 하고 절대 하향하지 않는 단방향 처리. ↔ bidirectional / destructive.
  - 예: This is upgrade-only: the post-pass may bump a row to `E_CONFIRMED` but must never downgrade a tier.
- **dead code (a branch that can't be reached)** — 도달 불가능하거나 결코 읽히지 않는 코드. ↔ a live path / load-bearing code.
  - 예: The `if bank else None` guard is dead code — the earlier `continue` already proved `bank` is truthy.
- **phantom (zeros / a phantom default)** — 실체 없이 기본값으로 만들어진 가짜 값이 통계를 왜곡함.
  - 예: The `0.0` default fabricates a rate for recipes that have none, so the means diverge — phantom zeros.
- **swallow an exception / a swallowed exception** — 예외를 잡고도 처리·전파 없이 묻어버려 오류가 숨다(안티패턴). ↔ propagate / re-raise.
  - 예: This ValueError is not even swallowed — it propagates and aborts the whole run.
- **a forward reference (resolved at call time)** — 나중에 정의되는 이름을 함수 본문에서 먼저 참조해도 호출 시점에 해석돼 안전함.
  - 예: A forward reference inside a function body is safe because name lookup happens at call time, not at def time.
- **off-by-one (error)** — 경계 인덱스를 1 차이로 빗나간 고전적 버그(`<` vs `<=`). ≈ a fencepost error.
  - 예: Look for inverted conditions, off-by-one errors, and None dereferences.
- **a latent bug** — 평소엔 안 터지지만 특정 조건에서만 드러나는 잠복 결함.
  - 예: The example uses 1/0, so this is low risk — but it is a latent bug if a user writes `False` instead.
- **a testbed** — 특정 레버(변경)의 효과를 격리해 측정하는 부분·환경. ≈ a proving ground. ↔ production.
  - 예: The rcp-only arm becomes the natural testbed for the edge_ncc lever, since consensus can't help there.
- **a no-op** — 실행돼도 순 효과가 0인 공회전 동작(no-operation).
  - 예: If the cursor already sits on the center, the glide is a no-op — 24 identical writes with zero net motion.
- **a (documented) wart** — 치명적이진 않지만 알고도 감수하는, 문서에 남겨두는 자잘한 설계 흠.
  - 예: One documented wart: the two arms use different templates, so the lift is only comparable within an arm.
