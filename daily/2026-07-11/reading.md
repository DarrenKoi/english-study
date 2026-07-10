# 2026-07-11 — 정독

## 단락 1

New Korean design doc: `docs/rag_chart_heavy_architecture.md`, backed by a fresh web-research pass. The short answer to your question: **hybrid, not pure image-RAG** — but with an important nuance. Verified evidence shows vision-native retrieval crushes text-over-extracted-charts (ColPali: nDCG@5 79.1 vs 40.1 even against high-quality VLM captions), yet CLIP-style embeddings score **0%** on cross-modal chart queries, and image-only RAG can't give you provenance/confidence/Marp roundtrip. So the doc proposes storing **3+1 representations per chart**, a 3-arm RRF retrieval (BM25 + bge-m3 + vision kNN) with rerank, and a reader contract of crop + low-res page + labeled machine-extracted table — since readers show a text-over-visual bias that a wrong table can poison. Phase 1 works with your current stack; Phase 2's single highest-ROI deployment is **Qwen3-VL-Embedding** (single-vector), which drops straight into OpenSearch kNN — late-interaction ColQwen only buys ~2–6 nDCG points and OpenSearch multi-vector support is still an RFC.

**문법·구조**: 첫 문장은 동사 없는 명사구 + 분사구(backed by ~)로 배경을 압축 — 보고서 헤드라인의 전형입니다. 둘째 문장 "The short answer to your question: hybrid" 는 콜론으로 결론을 먼저 던지고 대시로 단서(but with an important nuance)를 답니다. 셋째 문장은 shows A, **yet** B, **and** C 의 3중 병렬로 "이겼다 / 그러나 함정 / 게다가 결손"을 한 문장에 쌓았고, 마지막 문장은 세미콜론이 Phase 1과 Phase 2를 대구로 묶은 뒤 비제한 관계절(which drops straight into ~)과 대시 부연으로 근거를 답니다.
**핵심 표현**: "crushes"(압도한다 — 수치 근거가 있을 때만 쓸 강한 동사), "a wrong table can poison"(틀린 입력이 답을 오염시킨다), "only buys ~2–6 points"(그 비용으로 사는 이득이 고작 ~).
**격식 짝(작성)**: refined — "This yields only a marginal improvement of two to six points." ↔ plain — "It only buys you 2–6 points." / refined — "The model integrates directly into the existing index with no additional infrastructure." ↔ plain — "It drops straight into OpenSearch kNN."

<sub>출처: transcript:auto_recipe_creator 62687dfa… (문서추출·Marp 세션 최종 보고 §4)</sub>

---

## 단락 2

PPT was already DRM-safe (slideshow screen capture), but DRM PDFs failed in PyMuPDF and DRM Word docs failed at COM export — both were silently skipped. New `util/viewer_capture.py` generalizes the PPT trick: open the file in its authorized viewer (DRM decrypts for display), go fullscreen, capture → PageDown → capture, and **stop when the frame stops changing** (page count is unknowable). PDF and Word handlers auto-fall-back to it; Excel gets a clear DRM warning instead (scrollable sheets make generic capture unreliable). The frame-diff decision logic is pure and tested on Mac; the keystroke constants (`^l` for Acrobat, `%wf` for Word Read Mode) are top-of-file tunables for office calibration.

**문법·구조**: 첫 문장의 과거시제 대비(was already DRM-safe, but ... failed)와 수동태 "were silently skipped" — 행위자보다 "조용히 누락됐다"는 결과가 중요할 때 수동태가 옳은 선택입니다. 둘째 문장은 콜론 뒤에 명령형 동사 나열(open, go, capture, stop)로 절차를 압축 — 영어 기술 문서에서 절차는 명령형이 표준입니다. 셋째·넷째 문장은 세미콜론으로 "PDF/Word는 이렇게; Excel은 저렇게", "로직은 검증됨; 상수는 튜닝 대상"의 대구를 만들었습니다. "unknowable", "tunables"처럼 형용사·명사화 조어도 눈여겨보세요.
**핵심 표현**: "generalizes the PPT trick"(한 사례의 요령을 일반해로 확장하다), "auto-fall-back to it"(자동 폴백하다), "top-of-file tunables"(파일 상단에 모아 둔 조정 상수).
**격식 짝(작성)**: refined — "Both failure modes were previously omitted without any notification." ↔ plain — "Both were silently skipped." / refined — "Capture terminates once consecutive frames become identical." ↔ plain — "Stop when the frame stops changing."

<sub>출처: transcript:auto_recipe_creator 62687dfa… (문서추출·Marp 세션 최종 보고 §2)</sub>

---

## 단락 3

No. Tests-after answer "What does this do?" Tests-first answer "What should this do?" Tests-after are biased by your implementation. You test what you built, not what's required. You verify remembered edge cases, not discovered ones. Tests-first force edge case discovery before implementing. Tests-after verify you remembered everything (you didn't). 30 minutes of tests after ≠ TDD. You get coverage, lose proof tests work.

**문법·구조**: 설득하는 영어의 교과서 같은 단락입니다. 한 단어 문장 "No."로 반론을 시작하고, does/should의 조동사 대비 한 쌍으로 논지 전체를 요약합니다. 이어지는 "You test what you built, not what's required" — **A, not B** 대비 구문이 세 번 반복되며 리듬을 만듭니다. 괄호 삽입 "(you didn't)"는 앞 문장의 전제를 즉시 뒤집는 촌철살인 — 구어적이지만 글에서도 강력합니다. 마지막 문장은 접속사 없이 동사구 두 개를 쉼표로 병치(get coverage, lose proof)해 트레이드오프를 최소 단어로 전달합니다.
**핵심 표현**: "biased by your implementation"(구현에 물들어 편향된), "A, not B"(~이지 ~이 아니다 — 대비로 정의하기), "(you didn't)"(괄호 반전).
**격식 짝(작성)**: refined — "Retrospective tests tend to reflect the implementation rather than the requirements." ↔ plain — "You test what you built, not what's required."

<sub>출처: transcript:auto_recipe_creator 66c408dd… (TDD 스킬 본문 인용)</sub>
