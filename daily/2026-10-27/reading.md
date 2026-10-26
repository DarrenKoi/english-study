# 2026-10-27 — 정독

## 단락 1

Each host is one short FTP session that is almost all socket I/O, and Python releases the GIL during socket I/O — so blocking `ftplib` in a bounded `ThreadPoolExecutor` fans out hundreds of hosts concurrently with **zero extra packages**. No `aioftp` to install into an Airflow venv, no version drift between a laptop and the worker (unpinned `aioftp` installed at task runtime was the original "works locally, fails on the server" bug).

There is no asyncio anywhere: every fleet operation is a plain synchronous call, safe from a script, an Airflow task, a Flask handler, or code already running its own event loop.

One dead host never aborts its siblings, and inside a host one bad file (or directory, for `mkdir`) never aborts the rest. Failures are collected into the report, never raised. Callers gate on `failure_ratio` (e.g. `> 0.2`, or zero successes) — tools go offline routinely.

**문법·구조**: 설계 근거 문서답게 거의 모두 **현재 시제**로 쓴 일반 사실이다. 과거형은 괄호 속 `was the original … bug` 하나뿐이고, 이 선택을 하게 만든 과거 사건이라 시제가 바뀐다. 첫 문장은 '사실 A, and 사실 B — so 결론' 구조다. 대시 뒤 so 가 앞의 두 사실(대부분 소켓 I/O, 그동안 GIL 이 풀림)을 묶어서 '스레드만으로 충분하다'는 결론을 낸다. 둘째 문장은 동사가 없다. `No X …, no Y …` 처럼 명사구만 나열한 **생략문**인데, 설계 문서에서 '없어서 좋은 것'을 빠르게 늘어놓을 때 쓴다. 콜론은 '선언 → 풀이' 신호다(`There is no asyncio anywhere:` 뒤에 그 결과를 푼다). 마지막 단락에서는 `never` 가 세 번 나와 실패 격리가 예외 없는 규칙임을 박는다. 수동태 `are collected …, never raised` 는 누가 모으는지보다 실패가 어떻게 처리되는지에 초점을 둔다. 대시 뒤 짧은 절 `tools go offline routinely` 가 이 규칙이 필요한 현장 이유로 단락을 닫는다.

**핵심 표현**:
- `fans out (hundreds of hosts) concurrently` — 작업을 여러 대상에 한꺼번에 퍼뜨린다. fan out 은 부채처럼 펼친다는 그림.
- `safe from (a script, a task, a handler …)` — 어디서 불러도 안전하다. from 뒤에 호출하는 곳을 나열한다.
- `never aborts its siblings` — 형제(같은 실행 단위의 다른 호스트)를 멈추지 않는다. 트리 구조 용어 sibling 을 빌렸다.

**격식 짝**:
- refined (작성): A failure on any single host is contained and recorded; it does not interrupt processing of the remaining hosts.
- plain (작성): If one machine is down, the rest keep going, and we just note the failure.

<sub>출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md ("Threads + ftplib" · "Failure isolation" 두 절을 이어 인용)</sub>

---

## 단락 2

`mkdir` exists so an `upload` to a new path has a destination — STOR cannot create folders. Each entry of `MkdirSpec.dirs` creates its missing parents, and an existing directory counts as success, so callers run it before an upload without looking first. FTP answers MKD with the same 550 for "already exists" and for "permission denied", so a refused MKD is settled by CWD into that path (enter it → it exists; then CWD back to the login PWD so relative paths keep resolving there). If that CWD back fails, the session sits in an unknown directory, so the host's remaining dirs are all reported failed rather than created in the wrong place.

**문법·구조**: 네 문장 모두 **'사실 → so → 결과'** 사슬이다. 첫 문장의 `exists so …` 는 목적의 so(that)로 '~하도록 존재한다', 나머지 세 문장의 so 는 결과의 so 로 '그래서'다. 같은 단어가 두 뜻으로 쓰였으니 구분해서 읽는다. 첫 문장 대시 뒤 `STOR cannot create folders` 는 기능이 왜 필요한지 근거를 짧게 붙인다. 셋째 문장의 괄호는 화살표(→)로 판정 절차를 압축한 메모체다. 본문 흐름을 끊지 않고 '어떻게'를 끼워 넣는 방법이다. 마지막 문장은 `If` 조건절로 최악의 경우를 가정하고, 수동태 `are … reported failed` 에 `rather than created in the wrong place` 를 붙여 두 결과 중 무엇을 골랐는지 밝힌다. `reported failed` 는 report + 목적어 + 형용사 보어가 수동태로 바뀐 꼴이다.

**핵심 표현**:
- `counts as success` — 이미 있는 폴더를 성공으로 친다. 멱등 설계의 핵심 규칙.
- `is settled by (CWD into that path)` — 같은 550 응답이라는 모호함을 다른 수단으로 판가름한다.
- `reported failed rather than created in the wrong place` — 틀린 성공보다 정직한 실패를 고른다.

**격식 짝**:
- refined (작성): Where the server's response is ambiguous, the outcome is resolved by attempting to enter the directory.
- plain (작성): The server says the same thing either way, so we just try to cd into it and see.

<sub>출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md ("mkdir is mkdir -p and idempotent")</sub>

---

## 단락 3

Today the AFM trend chart computes its centre and band (μ ± 3σ, MAD-based σ) from the very group of measurements the user selected, so the reference moves with the selection, and it labels that band "UCL/LCL" (frontend/app/utils/afmTrend.ts, around lines 91-99). The owner earlier withdrew "AFM control limits" because the data cannot support that claim. The goal: let the engineer pin earlier measurements as a fixed baseline, so later measurements are judged against a reference that does not move, and stop calling a self-computed band UCL/LCL.

The design exists — do not redesign it. (…) It names the seam: the `centres` used by `trendRows`. Follow that design. One of its stated preconditions ("deferred until the AFM office adapter exists") no longer holds — the adapter ran at the office on 2026-10-07 (backend/afm/MIGRATION.md:12) — so the feature is unblocked.

**문법·구조**: 작업 지시문의 전형인 **'현재 문제 → 목표 → 이미 있는 것 → 막힌 게 풀렸다'** 흐름이다. 첫 문장은 현재형(computes, moves, labels)으로 지금의 동작을 묘사하고, 둘째 문장만 과거형(withdrew)이다. 이전에 내린 결정이라 그렇다. `the very group … the user selected` 의 very 는 '바로 그'라는 강조로, 기준을 평가 대상 자신에게서 뽑는 순환을 꼬집는다. 관계대명사 that 은 생략됐다. `The goal:` 은 콜론 뒤에 원형 동사(let, stop)가 오는 **목표 선언형**이다. 두 동사를 and 로 이어 할 일 두 가지를 한 문장에 담았다. 둘째 단락은 짧은 명령문(do not redesign it, Follow that design)과 긴 설명문을 번갈아 써서 리듬을 만든다. 마지막 문장은 대시 한 쌍으로 근거를 삽입하고 so 로 결론을 낸다. 주장(no longer holds) → 증거(어댑터가 돌았다) → 귀결(unblocked) 순서다.

**핵심 표현**:
- `be judged against a reference that does not move` — 고정된 기준에 비추어 판단하다. 앞 문장의 `moves with the selection` 을 정반대로 뒤집었다.
- `The design exists — do not redesign it.` — 위임할 때 설계 범위를 닫는 문장.
- `(a stated precondition) no longer holds` — 걸어 둔 전제가 이제 성립하지 않는다.

**격식 짝**:
- refined (작성): The precondition originally attached to this feature has since been satisfied, and implementation may proceed.
- plain (작성): The thing we were waiting on is done, so you can go ahead.

<sub>출처: transcript:skewnono-v3-nuxt (AFM 고정 기준선 작업 지시, "Why" · "What is already designed" 절. (…) 는 문서 경로를 나열한 문장 하나를 줄인 자리)</sub>
