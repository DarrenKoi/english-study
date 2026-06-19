# 코칭 카드 강화 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `prompts/process.md` 를 고쳐 한글→영어 코칭과 영어 다듬기 카드를 전용 `coaching.md` 로 모으고 `digest.md` 에서 보이게 한다.

**Architecture:** 순수 프롬프트(LLM 지침) 변경. 파이썬 코드·테스트 변경 없음. 입력 배치의 `[user]`/`[assistant]`/`repo:` 태그를 근거로 "내가 쓴 글"만 코칭 소스로 삼는다. 새 출력 파일은 `finalize` 의 `git add -A` 가 자동 커밋한다.

**Tech Stack:** Markdown 프롬프트, Python 3.11 파이프라인(`pipeline.run`), `claude -p`.

## Global Constraints

- 코칭 소스는 transcript 의 `[user]` + `spool:` 만. `[assistant]`·`repo:` 는 코칭에서 제외.
- 추출 충실: "내가 쓴 한글/영어" 는 배치에 실제 등장한 사용자 텍스트만 인용. 없는 오류를 지어내지 않는다.
- `정정` 은 실제 오류가 있을 때만 출력. `더 나은 표현` 은 오류 유무와 무관하게 항상 출력.
- 카드가 하나도 없는 섹션은 생략, 두 종류 다 없으면 `coaching.md` 와 digest 코칭 섹션 모두 생략.
- 파이썬 코드(`scripts/pipeline/*`) 는 건드리지 않는다.

---

### Task 1: `## 작업` 섹션 — 7번 정제 + 새 8번 추가 + 재번호

**Files:**
- Modify: `prompts/process.md:29-34`

**Interfaces:**
- Produces: 작업 목록에 새 8번(영어 다듬기) 도입, 기존 8·9번을 9·10번으로 이동. Task 2 의 출력 섹션이 이 카드들을 `coaching.md` 로 보낸다.

- [ ] **Step 1: 7~9번을 아래로 교체**

`old_string` (현재 `prompts/process.md` 29-34줄):
```
7. **한글→영어 코칭**: 원문이 한국어인 경우(특히 transcript 의 사용자 프롬프트),
   "내가 쓴 한글 / 자연스러운 영어 / 왜 이렇게" 3단으로 코칭 카드를 만듭니다.
8. **중복 제거**: `notes/by-register/*.md` 의 기존 표현과 텍스트가 정확히 일치하면 건너뜁니다.
9. **spool 노트 답변**: `spool:` 항목은 사용자가 자기 전·생각날 때 `spool/` 폴더에 직접 적은
   학습 질문/궁금증(예: "affect vs effect 차이", "'resilient' 들어간 문장 10개", "왜 a historic 인가")
   입니다. 각 노트를 실제로 답합니다 — **원 질문을 맨 위에 그대로 인용**한 뒤 친절히 해설합니다.
```

`new_string`:
```
7. **한글→영어 코칭**: 내가 직접 쓴 한국어(transcript 의 `[user]` 메시지 + `spool:` 노트)
   중 학습 가치가 있는 것을 "내가 쓴 한글 / 자연스러운 영어 / 왜 이렇게" 3단 카드로 만듭니다.
   `[assistant]` 와 `repo:` 문서는 코칭 소스가 아닙니다. 출력은 `coaching.md` 로 갑니다(아래 출력 참조).
8. **영어 다듬기**: 내가 직접 쓴 영어(transcript 의 `[user]` 메시지 + `spool:` 노트)를 다듬습니다.
   문법 오류가 있으면 정정하고, **오류가 없어도 한 단계 위의 더 나은 표현을 항상 제안**합니다.
   카드는 "내가 쓴 영어 / 정정(오류 있을 때만) / 더 나은 표현(항상) / 왜" 구조. 배치에 내가 쓴
   영어가 없으면 이 단계는 생략합니다. 없는 오류를 지어내지 않습니다. 출력은 `coaching.md` 로 갑니다.
9. **중복 제거**: `notes/by-register/*.md` 의 기존 표현과 텍스트가 정확히 일치하면 건너뜁니다.
10. **spool 노트 답변**: `spool:` 항목은 사용자가 자기 전·생각날 때 `spool/` 폴더에 직접 적은
   학습 질문/궁금증(예: "affect vs effect 차이", "'resilient' 들어간 문장 10개", "왜 a historic 인가")
   입니다. 각 노트를 실제로 답합니다 — **원 질문을 맨 위에 그대로 인용**한 뒤 친절히 해설합니다.
```

- [ ] **Step 2: 번호 정합성 확인**

Run: `grep -nE '^[0-9]+\.' prompts/process.md`
Expected: 작업 목록이 1~10 으로 중복·누락 없이 이어짐(8=영어 다듬기, 9=중복 제거, 10=spool 답변).

- [ ] **Step 3: Commit**

```bash
git add prompts/process.md
git commit -m "feat(prompt): add English-polishing step, scope coaching to user-written text"
```

---

### Task 2: `## 출력` 섹션 — coaching.md 신설 + new-expressions 경계 명시 + digest 코칭

**Files:**
- Modify: `prompts/process.md` 출력 섹션 (new-expressions 블록, reading 블록 직후, digest 블록)

**Interfaces:**
- Consumes: Task 1 의 7·8번 카드 정의.
- Produces: `daily/<날짜>/coaching.md` 출력 스펙과 digest 의 `### 오늘의 코칭` 요약 위치.

- [ ] **Step 1: new-expressions.md 블록 끝에 코칭 제외 한 줄 추가**

`old_string` (현재 new-expressions 항목 끝 — 유사어/반의어 코드펜스 닫힘 줄. `prompts/process.md` 39-50 블록의 마지막 ``` 부분):
```
  - 반의어: 표현 (반대 뜻; 있을 때만, 없으면 이 줄 생략)
  ```
```

`new_string`:
```
  - 반의어: 표현 (반대 뜻; 있을 때만, 없으면 이 줄 생략)
  ```
  한글→영어·영어 다듬기 코칭 카드는 여기 넣지 않습니다(`coaching.md` 로 갑니다).
```

- [ ] **Step 2: reading.md 블록 직후에 coaching.md 항목 삽입**

`old_string` (reading 블록의 닫는 안내 줄):
```
  배치에 양질의 영어 단락이 없으면 모범 단락(작성)으로 채웁니다.
```

`new_string`:
```
  배치에 양질의 영어 단락이 없으면 모범 단락(작성)으로 채웁니다.
- `daily/<날짜>/coaching.md` — **내가 쓴 글 코칭**. 두 섹션을 둡니다(해당 카드가 있을 때만):
  ```
  # <날짜> — 코칭

  ## 한글→영어
  ### 카드 N — <짧은 제목>
  - 내가 쓴 한글: "..."   (출처: transcript:... 또는 spool:...)
  - 자연스러운 영어: ...
  - 왜 이렇게: ...

  ## 영어 다듬기
  ### 카드 N — <짧은 제목>
  - 내가 쓴 영어: "..."   (출처: transcript:[user] ... 또는 spool:...)
  - 정정: ...            (문법 오류가 있을 때만; 틀린 부분 + 규칙 한 줄)
  - 더 나은 표현: ...     (항상; 자연스러움/격식 한 단계 위)
  - 왜: ...
  ```
  한쪽 카드가 없으면 그 `##` 섹션을 통째로 생략하고, 두 종류 다 없으면 `coaching.md` 를 만들지 않습니다.
```

- [ ] **Step 3: digest.md 블록에 오늘의 코칭 추가**

`old_string` (현재 digest 항목):
```
- `daily/<날짜>/digest.md` — 그중 핵심 5~7개만 1~2줄로 요약한 "오늘의 표현".
  끝에 `### 오늘의 정독` 으로 `reading.md` 의 단락 1개를 1~2줄로 가리키고,
  맨 끝에 `> 처리 항목 N개 / 미뤄진 항목 M개` 푸터.
```

`new_string`:
```
- `daily/<날짜>/digest.md` — 그중 핵심 5~7개만 1~2줄로 요약한 "오늘의 표현".
  `### 오늘의 정독` 으로 `reading.md` 의 단락 1개를 1~2줄로 가리키고,
  코칭 카드가 있으면 `### 오늘의 코칭` 으로 한글→영어·영어 다듬기에서 각 1~2개를 1줄씩
  요약하고 `coaching.md` 를 가리킵니다(코칭이 없으면 이 섹션 생략).
  맨 끝에 `> 처리 항목 N개 / 미뤄진 항목 M개` 푸터.
```

- [ ] **Step 4: 코드펜스 짝 확인**

Run: `grep -c '```' prompts/process.md`
Expected: 짝수(모든 코드펜스가 열림/닫힘 쌍). 홀수면 어딘가 펜스가 깨진 것이니 수정.

- [ ] **Step 5: Commit**

```bash
git add prompts/process.md
git commit -m "feat(prompt): add coaching.md output and digest coaching section"
```

---

### Task 3: `## 원칙` 보강 + 실행 검증

**Files:**
- Modify: `prompts/process.md` 원칙 섹션
- Verify: `daily/<오늘날짜>/` 산출물

**Interfaces:**
- Consumes: Task 1·2 의 카드 정의와 출력 스펙.

- [ ] **Step 1: 원칙에 코칭 규칙 한 줄 추가**

`old_string`:
```
- 한국어 해설로 친절하게, 그러나 간결하게.
```

`new_string`:
```
- 코칭(한글→영어·영어 다듬기)은 내가 직접 쓴 글(`[user]`·spool)만 대상으로 합니다. 문법 오류는
  지어내지 않되, 영어 다듬기의 "더 나은 표현"은 오류가 없어도 항상 제안합니다.
- 한국어 해설로 친절하게, 그러나 간결하게.
```

- [ ] **Step 2: 파이프라인 1회 실행(대화형/수동)**

Run: `cd /Users/daeyoung/Codes/english-study && PYTHONPATH=scripts uv run python -m pipeline.run`
Expected: 에러 없이 완료. (또는 다음 야간 자동 실행으로 검증)

- [ ] **Step 3: 산출물 육안 검증**

확인 항목:
- `daily/<오늘날짜>/coaching.md` 가 생성되고 `## 한글→영어` / `## 영어 다듬기` 형식이 맞는지.
- 한글→영어 카드가 `new-expressions.md` 에 더 이상 없는지 (`grep -L "한글→영어" daily/<날짜>/new-expressions.md` 식 확인).
- `digest.md` 에 `### 오늘의 코칭` 이 있고 `coaching.md` 를 가리키는지.
- 배치에 내가 쓴 영어가 없던 날엔 `## 영어 다듬기` 섹션이 깔끔히 생략됐는지.

- [ ] **Step 4: Commit**

```bash
git add prompts/process.md
git commit -m "docs(prompt): note coaching source/over-correction rules in principles"
```

(산출물 `daily/`·`state/` 는 finalize 가 별도 커밋하므로 여기서는 prompt 변경만 커밋.)

---

## Self-Review

- **Spec coverage:** 한글→영어(Task1 §7, Task2 §2) ✓, 영어 다듬기(Task1 §8) ✓, coaching.md 신설(Task2 §2) ✓, digest 코칭(Task2 §3) ✓, 소스 제한·정정/더나은표현 규칙(Global Constraints, Task3 §1) ✓, 코드 변경 없음 ✓, 검증(Task3 §2-3) ✓.
- **Placeholder scan:** TBD/TODO 없음. 모든 edit 에 exact old/new 문자열 포함.
- **Type consistency:** 파일명 `coaching.md`, 섹션명 `## 한글→영어`/`## 영어 다듬기`, digest 헤더 `### 오늘의 코칭` 을 전 태스크에서 일관 사용.
