---
description: Run the English-study pipeline interactively (collect → process with web search → finalize)
argument-hint: "[optional topic for the web reading passage]"
allowed-tools: Bash, Read, Write, Edit, Glob, WebSearch, WebFetch
---

당신은 이 세션에서 영어 학습 파이프라인을 **대화형으로** 실행합니다.
야간 `claude -p` 대신, 사용자가 지켜보는 동안 직접 돌립니다 — 그래서 **웹 검색을 써도 안전**합니다.

결정적 단계(collect/finalize)는 Python 이 그대로 담당하고, 당신은 가운데 LLM 가공만 맡습니다.

## 1) 배치 수집
```bash
PYTHONPATH=scripts uv run python -m pipeline.collect
```
출력의 `batch_path` 와 `item_count` 를 확인합니다.
- `item_count == 0` 이면: "처리할 새 항목이 없습니다" 라고 알리고 여기서 멈춥니다.

## 2) 지침과 배치 읽기
- `prompts/process.md` 를 읽어 작업 규칙(표현 추출·맥락·정독 단락·격식 짝·코칭)을 따릅니다.
- 1)에서 받은 `batch_path` (`state/batch-<오늘>.md`) 를 Read 로 읽습니다.

## 3) 가공 (web search 활성)
`prompts/process.md` 의 출력 규칙대로 `daily/<오늘>/` 와 `notes/` 에 씁니다.
추가로, 대화형이라 가능한 **웹 정독**을 더합니다:
- `$ARGUMENTS` 에 토픽이 있으면 그 주제로, 없으면 개발자에게 유용한 일반 주제로
  **WebSearch/WebFetch** 를 써서 *고품질 영어 원문* 1개와 *자연스러운 회화체* 1개를 찾습니다.
- 찾은 원문에서 5~10문장 단락을 인용하고(출처 URL 명기), 문법·맥락·격식 짝을 해설해
  `daily/<오늘>/reading-web.md` 에 씁니다. 저작권상 과도한 전체 인용은 피하고 학습에 필요한 만큼만.
- 지어낸(모범) 단락에는 반드시 "(작성)", 웹 인용에는 출처 URL 을 달아 구분합니다.

## 4) 검토 후 확정 (commit/push)
쓴 결과(특히 `daily/<오늘>/digest.md`)를 사용자에게 1~2줄로 요약해 보여줍니다.
**커밋·푸시는 사용자 승인 후에만** 실행합니다:
```bash
PYTHONPATH=scripts uv run python -m pipeline.finalize
```
finalize 는 consumed 매니페스트만큼 `state/progress.json` 을 전진시키고,
처리된 spool 노트를 `spool/done/<날짜>-<이름>` 으로 아카이브하고, commit & push 합니다.
사용자가 "아직 커밋하지 마" 라고 하면 finalize 를 건너뛰고 파일만 남겨둡니다.
