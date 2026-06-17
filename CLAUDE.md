# english-study — 자동 영어 학습 파이프라인

매일 밤 23:00 Mac launchd 가 `scripts/run.sh` → `python3 -m pipeline.run` 을 실행한다.

## 흐름
1. `collect` — git 공유 docs + Mac 트랜스크립트 + `requests/inbox` 에서 새 영어를
   토큰 예산 안에서 `state/batch-<날짜>.md` 로 모은다. 소비분은 `state/consumed-<날짜>.json` 에 기록.
2. `claude -p` — `prompts/process.md` 지침대로 추출·분류·코칭하여 `daily/`·`notes/` 에 쓴다.
3. `finalize` — 소비한 만큼만 `state/progress.json` 을 전진시키고, 처리한 요청을
   `requests/done/` 으로 옮기고, commit & push.

## 직접 쓰는 법
- 자기 전 `requests/inbox/<주문>.md` 에 요청을 적어두면 다음 실행이 처리한다.
- 아침에 `daily/<오늘날짜>/digest.md` 를 읽는다.
- 토큰 사용 추이는 `state/token-log.jsonl`.

## 수동 실행
`PYTHONPATH=scripts uv run python -m pipeline.run`
