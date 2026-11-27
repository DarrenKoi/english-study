# 2026-11-28 — 새 표현

오늘 배치는 computer-use 자동화 조사(arc-engine) 하루치입니다. 보고서 본문은 한국어라 영어 표현은 대부분 세션 요약(영어)에서 나왔습니다. 보고서·조사 결과를 영어로 정리할 때 바로 쓸 틀이 많아요.

## "on the healthy path"
- 레지스터: technical
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 설계 문서·리뷰에서 "아무 문제 없을 때 지나가는 기본 경로"를 가리킬 때(기술 문어)
- 한국어: 정상 경로에서는
- 설명: `healthy` 는 사람의 건강뿐 아니라 시스템이 "이상 없이 돌아가는" 상태에도 씁니다. 실패·예외 처리 경로(failure path, recovery path)와 짝을 이루죠. `happy path` 와 뜻이 거의 같지만 `healthy path` 가 조금 더 운영(ops) 냄새가 납니다.
- 예문: OpenAdapt Flow makes zero model calls on the healthy path and falls back to a grounding model only when local matching fails.
- 유사어: on the happy path (테스트·개발 쪽에서 더 흔함), in the normal case (평이), when nothing goes wrong (구어)
- 반의어: on the failure path, on the recovery path

## "false success"
- 레지스터: technical
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: agent·자동화 평가 글에서 "성공했다고 착각한 실패"를 한 단어로 묶을 때(기술 문어)
- 한국어: 성공 착각, 거짓 성공
- 설명: `false positive` 를 본뜬 조어입니다. 형용사 `false` 가 "겉보기와 실제가 다른"을 뜻해서 `false alarm`, `false start` 와 같은 결이에요. 원문은 `86% of failures are false success` 처럼 셀 수 없는 명사로 썼습니다.
- 예문: Most of the agent's failures were false success: it reported the form as submitted while the screen still showed the validation error.
- 유사어: a silent failure (드러나지 않은 실패, 더 일반적), a false completion claim (격식·구체적), the agent thought it was done (구어)
- 반의어: a verified success

## "splits the work three ways: the LLM proposes, a deterministic scoring function judges, and restricted tools execute"
- 레지스터: technical, professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 시스템 안의 역할 분담을 한 문장으로 정리할 때(설계 문서·발표)
- 한국어: 일을 셋으로 나눈다 — LLM 이 제안하고, 결정론적 채점 함수가 판정하고, 제한된 도구가 실행한다
- 설명: `split ~ three ways` 는 "셋으로 나누다"(돈을 셋이 나눠 낼 때도 `split the bill three ways`). 콜론 뒤에 "주어 + 동사" 셋을 같은 꼴로 늘어놓아 역할이 한눈에 들어옵니다. 동사(proposes / judges / execute)만 바꿔 다른 분업에도 그대로 씁니다.
- 예문: The tuning loop splits the work three ways: the LLM proposes a setting, an OCR-based score judges it, and the SAFE_MODE layer executes only values inside the allowed range.
- 유사어: divides responsibility among three parts (격식), there's a clean division of labor (설명조), three pieces, each with one job (구어)
- 반의어: one model does everything end to end

## "resolution ladder"
- 레지스터: technical
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 대상을 찾는 방법을 싼 것부터 비싼 것까지 차례로 시도하는 구조를 이름 붙일 때(설계 문서)
- 한국어: (대상) 해석 사다리, 단계별 폴백 순서
- 설명: `ladder` 는 한 칸씩 올라가는 단계를 비유합니다. 원문은 `resolution ladder local, then global, then OCR, then landmark, then grounding model` 로 `then` 을 반복해 순서를 보여 줬어요. `escalation ladder` 와 같은 쓰임입니다.
- 예문: Our resolution ladder tries UIA first, then template matching, then OCR, and calls the VLM only at the last rung.
- 유사어: fallback chain (가장 흔한 기술 용어), tiered lookup (격식), try A, then B, then C (구어)
- 반의어: a single-shot lookup

## "a closed VLM question (A/B/unknown)"
- 레지스터: technical
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 모델에 자유 답변 대신 선택지 안에서만 고르게 하는 설계를 말할 때(기술 문어)
- 한국어: 닫힌 질문(선택지가 정해진 질문)
- 설명: 설문 용어 `closed question` / `open-ended question` 을 그대로 가져왔습니다. `unknown` 을 선택지에 넣어 두는 것이 요점이고, 모르면 사람에게 넘기는 출구가 됩니다.
- 예문: At a branch point we ask the VLM a closed question — is this screen state A, B, or unknown? — and never let it generate a free-form action.
- 유사어: a multiple-choice prompt (평이), a constrained classification (기술·격식)
- 반의어: an open-ended question, free-form generation

## "with the summary block stripped"
- 레지스터: technical
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 작업 보고에서 "무엇을 뺀 상태로" 저장·전달했는지 덧붙일 때(기술 보고)
- 한국어: 요약 블록을 떼어 낸 채로
- 설명: `with + 명사 + 과거분사` 는 부대상황 구문입니다. "~가 ~된 상태로"를 절 없이 붙여요. 원문은 `saved the humanized report to docs/... with the summary block stripped`.
- 예문: I saved the report to `docs/` with the HUMANIZE-SUMMARY block stripped, so the committed file holds only the prose.
- 유사어: minus the summary block (구어), after removing the summary block (평이), excluding the summary block (격식)
- 반의어: with the summary block intact

## "standing constraints … to keep applying"
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 일회성 지시가 아니라 계속 유효한 규칙을 묶어 인계할 때(업무 문서·인계 메모)
- 한국어: 계속 지켜야 할 상시 제약
- 설명: `standing` 은 "늘 유효한"입니다. `a standing order`(상시 지시), `a standing meeting`(정기 회의)과 같아요. 뒤의 `to keep applying` 이 "앞으로도 계속 적용할"을 한 번 더 못 박습니다.
- 예문: Standing constraints from the project rules, to keep applying: no company names in committed files, and SAFE_MODE stays on at home.
- 유사어: ground rules (구어·회의), ongoing requirements (평이), persistent constraints (기술)
- 반의어: one-off instructions

## "could not be confirmed and is marked …"
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 조사 보고서에서 확인하지 못한 항목을 숨기지 않고 표시했다고 밝힐 때(격식 문어)
- 한국어: 확인하지 못해서 ~로 표시해 두었다
- 설명: 수동태 두 개(`could not be confirmed`, `is marked`)로 행위자를 빼고 결과 상태만 전합니다. 앞 문장 `TEM Agent was confirmed.` 와 나란히 써서 교차 확인 결과를 깔끔하게 대비시켰어요.
- 예문: TEM Agent was confirmed against the paper; GoldiBench could not be confirmed and is marked "unverified" in the report.
- 유사어: we couldn't verify it, so we flagged it (구어), remains unconfirmed (격식), is pending verification (업무)
- 반의어: was independently confirmed

## "Most numbers are author- or vendor-reported."
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 리서치 보고서 서두·각주에서 수치의 출처 신뢰도를 미리 밝힐 때(격식 문어)
- 한국어: 수치 대부분은 저자나 공급사가 보고한 값이다
- 설명: `author-reported` 와 `vendor-reported` 가 같은 뒷부분을 공유해서 `author- or vendor-reported` 처럼 하이픈만 남기고 줄였습니다(suspended hyphen). `short- and long-term` 도 같은 방식이에요.
- 예문: Most numbers are author- or vendor-reported, and we did not reproduce any of them independently.
- 유사어: self-reported figures (격식), these are their own numbers (구어), unaudited figures (재무·격식)
- 반의어: independently reproduced results

## "Items marked for in-company verification"
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 남은 확인 과제를 목록으로 넘길 때(인계 메모·보고서)
- 한국어: 사내에서 확인이 필요한 것으로 표시한 항목
- 설명: `mark A for B` 는 "A 를 B 대상으로 표시하다". `mark for deletion`, `mark for review` 처럼 흔합니다. 원문의 `in-company` 는 사내 맥락에서 쓴 조어고, 일반적으로는 `in-house` 가 더 자연스럽습니다.
- 예문: Items marked for in-house verification: whether the equipment apps expose UIA, and whether scores can be read from the screen.
- 유사어: flagged for follow-up (업무 구어), to be confirmed on site (평이), open questions (회의)
- 반의어: verified items, closed items

## "which belong to other work"
- 레지스터: professional, conversational
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 공유 작업 공간에서 내 것이 아닌 변경을 건드리지 않았다고 알릴 때(협업 보고)
- 한국어: 다른 작업의 것이라서
- 설명: 계속적 용법의 `, which` 로 "그건 다른 작업 소관"이라는 이유를 뒤에 덧붙였습니다. `belong to` 는 소유뿐 아니라 "~에 속한 일"에도 씁니다. 앞에는 `leave … alone`(손대지 않고 두다)이 왔어요.
- 예문: Leave the unrelated modified files in `core/` alone, which belong to other work.
- 유사어: which are from another session (구체적), which aren't ours (구어), which fall outside this task (격식)
- 반의어: which are part of this change

## "I adjusted the scope to …"
- 레지스터: conversational, professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 상대가 조건을 추가해서 조사·작업 범위를 바꿨다고 짧게 알릴 때(업무 대화·메일)
- 한국어: 범위를 ~에 맞게 조정했다
- 설명: `adjust A to B` 는 "A 를 B 에 맞추다". 바뀐 조건을 `to` 뒤에 나열하면 무엇이 달라졌는지 한 번에 전달됩니다.
- 예문: You added the vLLM-only condition, so I adjusted the scope to small open-weight models that run on our own GPUs.
- 유사어: I narrowed the scope to (좁혔을 때), I refocused on (격식), I switched gears to (구어)
- 반의어: I widened the scope

## "kept intentionally"
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 검토 결과 남은 항목이 실수가 아니라 의도적으로 둔 것임을 밝힐 때(리뷰 보고)
- 한국어: 일부러 남겨 둔
- 설명: 원문은 `remaining C-8, E-1/E-4, and A-18 kept intentionally` 로, 명사 뒤에 과거분사구를 바로 붙인 메모체입니다. 리뷰어가 "이건 왜 안 고쳤지?" 하고 되묻기 전에 막아 줍니다.
- 예문: Three remaining patterns were kept intentionally, because rewriting them would have changed the meaning of the table captions.
- 유사어: left on purpose (구어), retained by design (격식), deliberately left as is (평이)
- 반의어: missed, overlooked

## "(not requested explicitly)"
- 레지스터: professional
- 출처: transcript:arc-engine 466d352b (세션 요약)
- 맥락: 할 일 목록에서 "요청받지 않은 선택 작업"을 구분해 적을 때(작업 메모)
- 한국어: (명시적으로 요청받지는 않음)
- 설명: 괄호 속 짧은 수동태로 범위 밖 작업임을 표시합니다. 어순은 `not explicitly requested` 가 더 흔하지만 원문 어순도 틀리지 않습니다. 앞에 `Optional:` 을 달아 하지 않아도 되는 일임을 분명히 했어요.
- 예문: Optional: sync the humanized text back into the shared doc (not explicitly requested).
- 유사어: (nice to have) (구어), (out of scope) (범위 밖일 때), (only if asked) (평이)
- 반의어: (required)
