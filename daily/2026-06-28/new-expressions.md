# 2026-06-28 — 오늘 수집한 표현

배치 출처: skewnono_v3_nuxt 설계/plan/journal 문서 + auto-recipe-creator 트랜스크립트.

---

## "escalate to (a second opinion / a human)"
- 레지스터: technical, professional
- 출처: transcript:[user] auto-recipe-creator/agent-a6d2bd92...jsonl
- 맥락: 시스템·절차가 자체적으로 못 풀 때 *상위 단계·다른 주체로 넘기는* 흐름을 설명할 때(설계 문서·장애 대응).
- 한국어: (확신이 없을 때) 더 높은 권한·다른 판단 주체로 올려 보내다, 에스컬레이션하다.
- 설명: 고객지원의 "상급자에게 이관"에서 온 말로, 엔지니어링에선 "1차가 막히면 2차로 넘긴다"는 폴백 흐름을 가리킵니다. `escalate to X for Y` 꼴이 자연스럽습니다.
- 예문: When the CV matcher flags an ambiguous match, the system escalates to a VLM for a second opinion.
- 유사어: hand off to (더 중립적, 단순 인계), defer to (판단 권한을 양보 — abstain 쪽 뉘앙스), bump up to (구어)
- 반의어: handle inline (그 자리에서 자체 처리), resolve locally

## "a second opinion"
- 레지스터: conversational, professional
- 출처: transcript:[user] auto-recipe-creator/agent-a6d2bd92...jsonl
- 맥락: 1차 판단이 미덥지 않아 *다른 주체의 재확인*을 구할 때(병원에서 온 표현이라 일상·업무 모두 자연스러움).
- 한국어: 재확인 차원의 또 다른 의견·소견.
- 설명: 원래 의료 용어("다른 의사 소견")인데, 코드·설계 논의에서 "한 번 더 검증받자"는 뜻으로 폭넓게 씁니다. 권위를 넘기는 게 아니라 *참고 의견*을 받는 뉘앙스가 핵심입니다.
- 예문: The VLM gives a second opinion on the region, but OpenCV still owns the final coordinates.
- 유사어: a sanity check (가벼운 점검), cross-check (교차 확인), a sounding board (사람에게 의견을 떠보는 대상)
- 반의어: the final say / sole authority (최종 결정권)

## "X is complementary, not a replacement"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator (PixelRAG 연구)
- 맥락: 새 기법을 *기존 것을 대체*가 아니라 *보완*으로 자리매김할 때(설계 권고문·기술 비교).
- 한국어: 이건 대체재가 아니라 보완재다.
- 설명: 신기술 도입 논의에서 과잉 기대를 누르는 정석 문형입니다. `complementary`(보완적, 철자 주의: complimentary=칭찬/무료와 다름)와 `replacement`를 대비시켜 역할 경계를 한 줄로 못 박습니다.
- 예문: PixelRAG is complementary, not a replacement: it adds recall on layout-heavy pages but produces no provenance or structured fields.
- 유사어: it augments rather than replaces, it sits alongside (나란히 둔다), a layer on top of (위에 얹는 층)
- 반의어: a drop-in replacement (그대로 갈아끼우는 대체), a rip-and-replace

## "the X axis is exhausted"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator (consensus eval 결론)
- 맥락: 한 방향의 개선 여지를 *다 써버려 더 짜낼 게 없다*고 결론지을 때(실험 회고·ADR).
- 한국어: 그 축(접근 방향)은 이제 한계까지 다 소진됐다.
- 설명: `exhausted`는 "지쳤다"가 아니라 여기선 "가능성을 전부 소진했다"입니다. "이 방향으론 더 안 된다 → 레버를 바꿔라"로 이어지는 결론 문장에 잘 쓰입니다([[hit the same wall]]과 짝).
- 예문: All three fusion methods hit the same ~0.5 wall, so the matcher-fusion axis is exhausted — the lever is key distinctiveness.
- 유사어: we've hit the ceiling on X, there's no headroom left, tapped out (구어)
- 반의어: there's still headroom, room to grow

## "a recall illusion"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator (rank-1 vs in_topk)
- 맥락: 후보 풀에는 정답이 들었지만 *1순위로 못 뽑는데도* 지표가 좋아 보이는 착시를 짚을 때(평가 방법론).
- 한국어: 재현율(recall)이 높아 보이지만 실속은 없는 착시.
- 설명: in_topk(후보 안에 있나)는 천장(ceiling)일 뿐, 실전이 쓰는 건 rank-1(1순위로 뽑았나)이라는 교훈에서 나온 표현. "지표가 좋아 보이는데 실제로는 아니다"를 한 단어로 압축합니다.
- 예문: A high in_topk with a low rank-1 is a recall illusion — the true point is in the pool but never ranked first.
- 유사어: a vanity metric (보기에만 좋은 지표), a false positive signal, looks good on paper
- 반의어: a production-faithful metric (실전과 일치하는 지표)

## "downstream consumer"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator (report ↔ eval 파이프라인)
- 맥락: 데이터 파이프라인에서 *앞 단계의 출력을 받아 쓰는 뒷단 모듈*을 가리킬 때.
- 한국어: (앞 단계 산출물을 받아 쓰는) 하류 소비자.
- 설명: 강물 비유로 `upstream`(상류=생산 측)과 `downstream`(하류=소비 측)을 나눕니다. "이 모듈은 결론을 *다시 계산하지 않고* 받아서 행동으로 옮긴다"는 분업을 명확히 합니다.
- 예문: The report is the downstream consumer of the eval's conclusions — it ingests the rank-1 numbers rather than recomputing them.
- 유사어: the consuming side, the sink (데이터가 흘러드는 종착), reads from (단순 동사화)
- 반의어: upstream producer / the source (생산 측)

## "the seam (that X leaves you)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-27-anomaly-convention-phase2-handoff.md
- 맥락: 인수인계 문서에서 *이전 단계가 다음 단계에 남겨준 깔끔한 연결 지점*을 가리킬 때.
- 한국어: (앞 작업이 남긴) 이음매·접합부 — 다음 사람이 이어 붙일 자리.
- 설명: 바느질의 "솔기"에서 온 비유로, 모듈 경계나 확장 지점을 뜻합니다. handoff/journal에서 "Phase 1이 너에게 남긴 seam은 이거다"처럼 다음 작업자에게 진입점을 짚어줄 때 좋습니다.
- 예문: The seam Phase 1 leaves you is clean: scoring and rendering are stable, so Phase 2 only adds the detectors.
- 유사어: the extension point, the handoff boundary, where it plugs in
- 반의어: a tangled boundary, tight coupling (떼어내기 어려운 결합)

## "for free"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator (PixelRAG 적용)
- 맥락: *추가 비용·노력 없이 이미 얻어지는* 것을 강조할 때(구어지만 기술 글에서도 흔함).
- 한국어: 공짜로, 별도 수고 없이 거저.
- 설명: 돈이 아니라 "추가 작업 없이 부수적으로 따라온다"는 뜻. `you get X for free`는 설계 이점을 자랑할 때 자주 쓰는 관용입니다.
- 예문: Because combineVerdicts already aggregates, a point carrying three signals becomes one badge with three reason lines for free.
- 유사어: out of the box (기본 제공), at no extra cost, comes baked in
- 반의어: at a cost, you have to pay for it (별도 비용·작업 필요)

## "a coin flip"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] auto-recipe-creator (SEM rank-1 ~0.5)
- 맥락: 성공 확률이 *반반(50%)이라 사실상 운*이라고 비꼬듯 평가할 때.
- 한국어: 동전 던지기 / 반반 확률 (믿을 수 없음).
- 설명: 0.5 근처 정확도를 "예측이 아니라 운"이라고 깎아내리는 생생한 표현. 수치를 감정적으로 전달해 "이건 못 쓴다"를 각인시킵니다.
- 예문: Heatmap SEM rank-1 came in at 0.49 — a coin flip, not a usable predictor.
- 유사어: no better than chance, 50/50, hit or miss
- 반의어: a reliable signal, near-deterministic

## "gotcha (banked)"
- 레지스터: casual, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/journals/2026-06-27-anomaly-convention-phase1-build.md
- 맥락: 디버깅 중 *발에 걸린 함정*을 다음을 위해 기록해 둘 때(엔지니어 메모·journal).
- 한국어: 함정/허 찔린 포인트 (기록해 둠).
- 설명: `gotcha`는 "(허 찌르는) 함정·낚일 뻔한 지점"을 뜻하는 캐주얼 명사. `bank a gotcha`는 "이 함정을 (다음을 위해) 저장해 둔다"는 비유로, 회고 문서에서 교훈을 적립할 때 씁니다.
- 예문: Gotcha banked: binding a control to a ref that arrives through a prop trips the no-mutating-props lint.
- 유사어: a pitfall, a footgun (스스로 발등 찍는 함정, 더 캐주얼), a trap to watch for
- 반의어: (마땅한 대체 표현 없음)

## "trade away (X)"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator (PixelRAG single-vector)
- 맥락: 어떤 이점을 얻는 *대가로 다른 것을 내주는* 설계 절충을 설명할 때.
- 한국어: (~을 얻는 대신) ~을 내주다·포기하다.
- 설명: `trade-off`의 동사형. `trade away Y (for X)` = "X를 위해 Y를 희생한다". 무엇을 *잃는지*를 정직하게 밝히는 설계 서술에 좋습니다.
- 예문: A single-vector index stays light and fast, trading away the patch-level localization precision of late-interaction models.
- 유사어: give up, sacrifice, forgo (격식)
- 반의어: preserve, retain, keep intact

## "ingest (X) and turn it into (Y)"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator (report가 eval 출력 소비)
- 맥락: 한 단계가 *앞 단계의 출력을 받아들여 다른 형태로 가공*하는 역할을 설명할 때.
- 한국어: (데이터를) 받아들여 ~으로 바꾸다.
- 설명: `ingest`는 데이터 파이프라인에서 "외부/앞단 산출물을 시스템에 받아들이다"라는 전문어입니다. "재계산이 아니라 소비"라는 분업을 강조할 때 [[downstream consumer]]와 함께 자주 등장합니다.
- 예문: It doesn't re-derive the conclusions; it ingests the eval's output and turns it into an action list.
- 유사어: consume, take in, feed on
- 반의어: emit / produce (산출하다), re-derive (다시 계산하다)
