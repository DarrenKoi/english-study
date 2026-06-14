# English Study Pipeline — 설계 문서

- 작성일: 2026-06-14
- 상태: 승인 대기 (브레인스토밍 산출물)
- 위치: `C:\Code\english-study` (Mac: `~/Codes/english-study`)

## 1. 목적

다른 프로젝트 폴더에 흩어진 영어 문장(docs, journals, README, ADR 등)과 Claude Code
대화 로그에서 **의미 있는 표현을 자동 수집·해설**하고, 매일 아침 읽을 **학습 다이제스트**로
만든다. 매일 밤 자동 실행해 평소 안 쓰고 남는 토큰을 학습에 활용한다.

### 학습 결과물 형태
- **해설형 노트** (1): 문장 + 한국어 해석 + 표현/숙어 설명이 쌓이는 영구 아카이브
- **일일 다이제스트** (3): 매일 "오늘의 표현 N개" 요약 한 편
- 표현은 **레지스터(말투/격식)별로 분류**: professional / conversational / casual / technical
- **한글 → 영어 코칭**: 영어로 프롬프트 쓰기 힘들어 한글로 쓴 경우, "내가 썼어야 할
  자연스러운 영어"를 생성해 학습 카드로 만든다

## 2. 핵심 결정사항

| 항목 | 결정 |
|---|---|
| 실행 위치 | **Mac 로컬** (항상 켜져 있음). Windows는 git push로 기여만 함 |
| 트리거 | **launchd, 매일 23:00** |
| 증분 방식 | **git 커밋 SHA 기준** (기기 무관, 정확). 트랜스크립트는 오프셋 기준 |
| 결과 공유 | `english-study`를 **git repo**로 운영 → commit/push, Windows는 pull |
| 역할 분리 | git·파일수집·중복필터 = **코드**, 추출·분류·번역 = **Claude** |
| 출처 (docs) | 프로젝트 repo의 `*.md` (git 공유라 Windows-off 무관, Mac이 pull) |
| 출처 (대화) | **Mac 트랜스크립트만** 우선. Windows 대화는 미래 확장 |
| OS 경로 | **Mac 경로 단일** (`~/Codes/`). OS별 매핑 불필요 |

### 왜 Mac 로컬인가 (클라우드 `/schedule` 대신)
출처 repo들은 모두 GitHub(`DarrenKoi/...`)에 있어 클라우드도 가능하나,
샌드박스에서 여러 private repo를 clone할 수 있는지 불확실하다. Mac이 항상 켜져 있어
로컬 실행이 더 확실하고 단순하며("기기 안 켜도 됨"이라는 클라우드 장점은 무의미),
로컬 파일 + `git pull`로 최신본 접근이 보장된다.

### Windows-off 처리
- **docs/journals**: git repo 안에 있으므로 Mac이 각 repo를 `git pull`하면 Windows
  기여분이 자동 포함. 처리 시점만 "다음 Mac 실행"으로 미뤄질 뿐 누락 없음.
- **Claude Code 대화 로그**: `~/.claude/projects/`에 기기 로컬 저장 → git에 없음.
  Windows 대화는 Mac이 못 봄. **초기에는 Mac 대화만** 처리. 추후 필요 시 Windows에
  `Stop`/`SessionEnd` 훅을 달아 영어 추출분을 git에 commit/push → Mac이 pull.

## 3. 디렉터리 구조

```
english-study/
├─ config/
│   └─ sources.json          # 출처 repo 목록 (Mac 경로) + 일일 처리 상한
├─ state/
│   └─ progress.json         # repo별 마지막 처리 SHA, 트랜스크립트 오프셋, last-run
│   └─ batch-<date>.md       # (실행 중 생성) 수집된 원문 + provenance
├─ requests/                 # 자기 전 "주문서"
│   ├─ inbox/                #   내가 떨궈두는 요청 .md (자유 형식)
│   └─ done/                 #   처리 완료 보관 (멱등성)
├─ daily/                    # 날짜별 "오늘 학습할 것"
│   └─ YYYY-MM-DD/
│       ├─ digest.md         #   오늘의 표현 다이제스트
│       ├─ new-expressions.md#   그날 수집·해설 표현 전체
│       └─ requests/         #   내 주문 결과
├─ notes/                    # 영구 아카이브 (브라우즈 + 중복제거 기준)
│   ├─ by-register/          #   professional / conversational / casual / technical .md
│   └─ index.md              #   전체 표현 색인
├─ scripts/
│   ├─ run.sh                #   launchd가 호출 → collect + claude -p + finalize
│   └─ com.daeyoung.english-study.plist
├─ docs/superpowers/specs/   # 이 설계 문서
└─ CLAUDE.md                 # 헤드리스 실행 지침(작업 절차 명문화)
```

### daily vs notes 역할 분리
- `daily/<date>/` = **그날 공부할 것** (시간순). 날짜로 학습 진도 관리.
- `notes/` = **영구 자산** (레지스터·주제별). 길게 쌓이고, 중복제거의 기준점.

## 4. 데이터 모델 — 학습 아이템 1개

```yaml
표현: "circle back"
레지스터: [conversational, professional]
원문_출처: skewnono_v3_nuxt/docs/journals/2026-06-10.md   # 또는 conversation:<id>
한국어: 나중에 다시 논의하다
설명: 회의에서 "이건 나중에 다시 보자"는 뉘앙스로 자주 씀
예문: "Let's circle back to this after lunch."
# 한글→영어 코칭인 경우 추가 필드:
내가_쓴_한글: "이 부분은 나중에 다시 얘기하자"
자연스러운_영어: "Let's circle back to this later."
왜: "talk about later"보다 비즈니스 맥락에서 관용적
```

## 5. 데이터 흐름 (하이브리드: 코드 수집 + LLM 가공)

```
launchd (매일 23:00) → scripts/run.sh

1) cd english-study && git pull                    # 결과물 repo 최신화

2) collect (코드, 토큰 0):
   - config/sources.json 읽기
   - 각 source repo: git pull
   - git diff <progress.SHA>..HEAD -- '*.md' → 새 마크다운
   - Mac 트랜스크립트 JSONL: 마지막 오프셋 이후 메시지
   - requests/inbox/*.md 읽기
   → state/batch-<date>.md 에 "원문 + provenance" 적재
     (일일 상한 초과분은 다음 날로 큐잉 + 로그)

3) claude -p (LLM 가공, 토큰 사용):
   - batch 읽고 의미있는 표현 추출 + 레지스터 분류
   - 한글 프롬프트 → 영어 코칭 카드
   - notes/ 기존 항목과 중복 제거
   - requests 주문 수행 (단어 확장·시적 표현 등)
   - daily/<date>/ 에 digest.md, new-expressions.md, requests/ 작성
   - notes/by-register/, index.md 갱신

4) finalize (코드):
   - 처리한 requests → requests/done/ 이동 (멱등성)
   - state/progress.json 갱신 (SHA·오프셋·last-run)
   - git add && commit && push
```

## 6. 토큰 통제 & 사용량 트래킹

- collect 단계는 **결정적(LLM 미사용)** → 토큰 0
- 일일 처리 상한을 `sources.json`에 설정 (예: 파일 N개 / 문자 M개 / 토큰 예산)
- 상한 초과분은 **다음 날로 큐잉**하고 로그에 명시 ("조용히 잘림" 금지)

### 토큰 사용량 트래킹
- `claude -p --output-format json` 실행 결과의 `usage`(input/output/cache 토큰)와
  `total_cost_usd`를 `run.sh`가 파싱
- `state/token-log.jsonl`에 실행별 1줄 적재:
  `{date, input_tokens, output_tokens, cache_read, cost_usd, items_processed}`
- 활용:
  1. 일일 상한을 **토큰 예산 기준**으로도 설정 가능
  2. `daily/<date>/digest.md` 푸터에 "오늘 사용 토큰 / 누적" 표시
  3. 주간 사용량 추이 파악 (남는 토큰 적극 활용 여부 확인)

## 7. 출력 포맷

- `daily/<date>/digest.md` — "오늘의 표현 N개". 표현당 1~2줄 + notes 링크. 아침에 빠르게 읽기
- `daily/<date>/new-expressions.md` — 그날 수집분 전체 해설(데이터 모델대로)
- `daily/<date>/requests/*.md` — 주문 결과
- `notes/by-register/*.md` — 레지스터별 영구 누적, 중복제거 기준
- `notes/index.md` — 전체 표현 색인

## 8. 요청(주문서) 메커니즘

- 자기 전 `requests/inbox/`에 자유 형식 마크다운을 떨군다
  (예: "'resilient' 들어간 문장 더 만들어줘", "이 표현 시적으로 바꿔줘")
- 새벽 작업이 읽어 `daily/<date>/requests/`에 결과 생성
- 처리 후 `requests/done/<date>-<name>.md`로 이동 → 다음 날 재실행 방지(멱등성)

## 9. 확정된 파라미터

- 다이제스트 표현 개수 N: **하루 5~7개**
- 일일 처리 상한: **약 50k 토큰/밤** (토큰 예산 기준)
- 중복제거 판정: **표현 텍스트 정확 일치** 우선 (의미 유사 매칭은 추후)
- GitHub remote: **`DarrenKoi/english-study` private repo** 신규 생성

### 추후 확장 (이번 범위 밖)
- Windows 대화 훅 (`Stop`/`SessionEnd` → git push → Mac pull)
- 의미 유사 기반 중복제거
- git SHA 증분의 rebase/force-push 대응(현재는 단순 선형 히스토리 가정)
```
