# english-study — 자동 영어 학습 파이프라인

매일 00:01 Mac launchd 가 `scripts/run.sh` → `python3 -m pipeline.run` 을 실행한다.

## 흐름
1. `collect` — `spool/` 노트(최우선) + `~/Codes` 전 프로젝트의 문서 폴더 + Mac 트랜스크립트에서
   영어를 토큰 예산 안에서 `state/batch-<날짜>.md` 로 모은다. 소비분은 `state/consumed-<날짜>.json` 에 기록.
   - 문서 폴더: 각 프로젝트 아래 깊이 무관하게 `doc`/`docs`/`shared_docs` 폴더를 찾아(설정 `doc_dirs`),
     그 안의 `.md`/`.txt`(`doc_exts`) 중 **최근 `recent_days`(기본 7일) 안에 수정된** 파일만, 최신순으로.
     `node_modules`·hidden·빌드 산출물은 건너뛰고, `exclude_projects`(기본 `english-study`)는 제외.
     상태 추적 없이 매 실행마다 다시 훑으므로, 예산에 밀린 파일은 다음 실행에서 자연히 재시도된다.
   - **빈 날 폴백**: 새 항목이 0개면 ① `backlog_days`(기본 14일) 윈도로 7일 너머
     미처리 문서를 따라잡고, 그래도 없으면 ② `notes/` 누적 표현 중 아직 복습 안 한
     것을 골라 복습본을 생성한다(`state/reviewed.json` 추적). 둘 다 없으면 중단한다.
2. `claude -p` — `prompts/process.md` 지침대로 추출·분류·코칭하여 `daily/`·`notes/` 에 쓴다.
3. `finalize` — 소비한 만큼만 `state/progress.json` 을 전진시키고, 처리한 spool 노트를
   `spool/done/<날짜>-<이름>` 으로 아카이브하고, commit & push.

## 직접 쓰는 법
- 궁금한 것·공부하고 싶은 것을 `spool/` 에 `.txt`/`.md` 파일로 적어두면 다음 실행이 **최우선**으로 답한다.
  (답: `daily/<날짜>/spool/<이름>.md`, 원본: `spool/done/` 으로 보관)
- 아침에 `daily/<오늘날짜>/digest.md` 를 읽는다.
- 토큰 사용 추이는 `state/token-log.jsonl`.

## 실행 방법
- **야간 무인** (자리 비움): launchd → `pipeline.run` → `claude -p` (파일 도구만, 네트워크 차단).
- **대화형** (자리에 있을 때): Claude Code 세션에서 `/study [토픽]` 입력.
  같은 collect/finalize 골격을 쓰되 가운데 가공을 대화형 LLM 이 맡고, **웹 검색으로
  고품질 영어·회화 원문을 정독 자료로 추가**합니다(감독 하에 실행되므로 안전).
- **순수 수동**: `PYTHONPATH=scripts uv run python -m pipeline.run`
