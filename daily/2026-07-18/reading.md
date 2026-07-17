# 2026-07-18 — 정독

## 단락 1

The long-term primary knowledge source is an immutable local FAISS index built from equipment manuals. Manuals contain many pages, diagrams, graphs, and charts, so retrieved evidence must retain document, page, and visual-region provenance. OpenSearch and approved company systems provide secondary, current operational context through read-only tools. The first implementation is a compatibility foundation. It installs and exercises Deep Agents with deterministic fake manual evidence, preserves the current direct chat runtime, and creates explicit office hookup points. It does not invent company interfaces, OpenSearch mappings, or a production manual indexing pipeline.

**문법·구조**: 설계 문서의 전형인 **일반 현재 시제**가 전체를 지배합니다 — "미래에 이렇게 할 것"이 아니라 이미 확정된 사실처럼 서술해 권위를 만듭니다. 두 번째 문장은 `..., so retrieved evidence must retain ...` 으로 **원인(so) + 의무(must)** 를 연결해 "매뉴얼이 시각 자료 위주 → 그러므로 출처가 시각 영역까지 보존돼야 한다"는 논리를 한 문장에 담습니다. 마지막 두 문장은 **It ... / It does not ...** 의 긍정-부정 대구로 범위(in-scope)와 비범위(out-of-scope)를 선명하게 가릅니다. `installs and exercises ... , preserves ... , and creates ...` 처럼 3연속 동사 병렬도 눈여겨보세요.
**핵심 표현**: *retain provenance* (출처 정보를 보존하다), *exercise* (기능을 실제로 돌려 검증하다 — test 보다 "작동시켜 본다" 뉘앙스), *hookup points* (나중에 연결할 접점).
**격식 짝**: refined — "It does not invent company interfaces." ↔ plain — "We're not making up company APIs here." (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md</sub>

---

## 단락 2

Clean, minimal cut. The change does exactly what the spec asked: a single `include_msr` flag threaded through the Protocol, with opposite defaults at the two layers so production inherits rcp-only without touching either call site. Backward compatibility holds. The only other caller calls `download_rcp_msr` without `include_msr`; because the impl default is `True`, that office smoke test still fetches rcp+msr — its intended behavior — and does not break on the new keyword-only param. Silenced warning hides nothing. Both offline consumers guard `current_sem` with explicit `is not None` checks, so removing the load-time warning removes only noise.

**문법·구조**: 시니어 리뷰어의 문체 교본입니다. 각 논점을 **두세 단어짜리 무동사 헤드라인**("Clean, minimal cut." / "Backward compatibility holds." / "Silenced warning hides nothing.")으로 먼저 선언하고, 뒤 문장이 증거를 댑니다 — 결론 먼저, 근거는 나중(front-loading). `threaded through the Protocol` 은 **과거분사 축약 관계절**(which is threaded ...)이고, `because the impl default is True, ... and does not break` 는 근거→결과 순서의 종속절 배치입니다. 대시로 끼워 넣은 `— its intended behavior —` 는 판단(의도된 동작임)을 사실 서술 중간에 삽입하는 리뷰 특유의 기법.
**핵심 표현**: *threaded through* (여러 층을 관통해 전달된), *holds* (성질·불변식이 "성립한다" — Backward compatibility holds), *call site* (호출 지점).
**격식 짝**: refined — "Silencing the warning hides nothing." ↔ plain — "Turning that warning off doesn't bury anything real." (작성)

<sub>출처: transcript:auto-recipe-creator (whole-branch code review)</sub>

---

## 단락 3

FAISS stores vectors and stable chunk identifiers, not original manuals. Text extraction, OCR, chart descriptions, and page rendering occur in a separate offline ingestion workflow. The running Flask application never mutates or incrementally updates the index. Index deployment uses a versioned directory and an atomic active-version switch. This prevents Flask workers from observing a partially rebuilt index. Models without vision support can still answer from extracted text and visual descriptions. They do not receive image-only references they cannot inspect.

**문법·구조**: 짧은 **단문 연쇄**가 만드는 리듬을 보세요 — 접속사 없이 문장을 끊어 각 문장이 하나의 설계 결정을 못 박습니다. 첫 문장의 `X, not Y` 구조는 오해를 선제 차단하는 부정 대비. `prevents Flask workers from observing ...` 은 **prevent + 목적어 + from + 동명사** 패턴이고, `references they cannot inspect` 는 **관계대명사 생략** 접촉절(references *that* they cannot inspect)입니다. `never mutates or incrementally updates` 처럼 부사(never)가 병렬 동사 둘을 한꺼번에 부정하는 것도 압축 포인트.
**핵심 표현**: *ingestion workflow* (데이터 수집·가공 파이프라인), *an atomic switch* (중간 상태가 노출되지 않는 원자적 전환), *image-only references* (이미지로만 존재하는 참조 — X-only 합성 형용사).
**격식 짝**: refined — "This prevents workers from observing a partially rebuilt index." ↔ plain — "This way a worker never sees a half-built index." (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md</sub>
