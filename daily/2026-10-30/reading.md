# 2026-10-30 — 정독

오늘 배치에는 인용할 만한 영어 단락이 없다(repo 문서 8개가 모두 한국어). 그래서 문서 내용을 바탕으로 모범 단락 세 개를 영어로 지었다.

## 단락 1
Since September, our parser had divided every `!Cursor_info` coordinate by `Pixel × 10`. The office has now confirmed that the frame is a fixed 5120, regardless of image size. The mistake went unnoticed because every sample we had seen happened to be a 512-px align image, where the two values coincide. On a 1024-px image, the crosshair and box would have been drawn at half size and pulled toward the top-left corner. Because align, live-alarm and parameter images share this one parser, all three screens were affected. We added a 1024-px test first, watched it fail, and only then fixed the divisor.

**문법·구조**: 시제 배치가 핵심이다. 첫 문장은 과거완료 `had divided` 로 "확인을 받기 전까지 계속 그렇게 해 왔다"는 기간을 깔고, 둘째 문장의 현재완료 `has now confirmed` 가 지금 시점의 새 사실을 세운다. 넷째 문장의 `would have been drawn` 은 실제로 확인하진 못했지만 그랬을 것이라는 과거 추정(가정법 과거완료)이다. 원문의 "그려졌을 것입니다"를 옮긴 모양이고, 수동태라서 누가 그렸는지보다 화면이 어떻게 됐는지에 초점이 간다. 마지막 문장은 `first … and only then` 으로 순서를 못 박아 TDD 절차를 보여 준다.
**핵심 표현**: `went unnoticed`(눈에 띄지 않고 지나갔다, 수동 의미의 자동사 구문), `happened to be`(우연히 ~였다; 설계가 아니라 우연), `regardless of`(~와 무관하게).
**격식 짝**:
- refined: The error remained latent because all available samples happened to share the same resolution. (작성)
- plain: Nobody caught it because every sample we had was 512 px. (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt docs/measurement-box/office-replies.md 1차 회신 "틀렸던 가정" 내용 바탕</sub>

---

## 단락 2
`put` never writes to the real file name directly. It first stores the data as `<target>.<random>.part` in the same folder, then renames it to the target. If the transfer is cut off halfway, what remains is a stray temp file, not a half-written file under the real name. By default it refuses to overwrite; an existing target raises `TargetExists`. With `overwrite=True`, it deletes the old target before the rename, because some servers reject a rename onto an existing file. For a brief moment the target does not exist, and if the rename then fails, the temp file is the only copy of the new content, so it is kept and reported in the exception's `temp_path`.

**문법·구조**: 동작 설명이라 전부 현재 시제다(습관·규칙의 현재). 둘째 문장의 `first …, then …` 이 두 단계를 한 문장에 담고, 셋째 문장의 `what remains is …, not …` 은 명사절 주어(what remains)로 결과를 앞세운 뒤 `A, not B` 대비로 마무리한다. 넷째 문장은 세미콜론으로 규칙과 그 결과를 붙였다. 마지막 문장은 `and if …, … so …` 로 조건 → 사실 → 결론을 한 호흡에 이었다. 길지만 연결어 하나하나가 논리 단계를 표시해서 읽힌다. `it is kept and reported` 는 수동태 두 개를 and 로 묶어 주어(temp file)를 한 번만 쓴다.
**핵심 표현**: `cut off halfway`(중간에 끊기다), `a rename onto an existing file`(기존 파일 위로 덮는 rename; onto 가 '위로 올라탐'을 그린다), `the only copy of`(유일한 사본).
**격식 짝**:
- refined: Should the rename fail at that point, the temporary file is retained, as it holds the sole copy of the new content. (작성)
- plain: If the rename fails there, we keep the temp file, because that's the only copy of the new data. (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md 케이스 1 `put` 설명 바탕</sub>

---

## 단락 3
In a fleet run, individual failures are normal: tools go offline, and a few hosts will always time out. So do not fail the job on any single failure. Gate on `failure_ratio` instead, and raise only when nothing succeeded or more than a fifth of the fleet failed. That is what the "systemic failure" error is for. Note also that in streaming mode the report's `data` is empty, because the bytes were already archived and then released. Check the counts and `failures`, not the bytes; the bytes now live in MinIO and OpenSearch.

**문법·구조**: 규칙을 알려 주는 안내문이라 명령문(`do not fail`, `Gate on`, `Note`, `Check`)이 중심이다. 첫 문장은 콜론 뒤에 이유를 풀어놓는 구조로, 명령을 내리기 전에 근거부터 깐다. `will always time out` 의 will 은 미래가 아니라 '늘 그러기 마련'이라는 경향의 will 이다. `raise only when A or B` 는 only 를 when 앞에 붙여 조건을 좁혔다. `That is what … is for` 는 "그게 바로 ~의 용도다"라는 분열문으로, 앞 규칙과 에러 메시지를 잇는다. 마지막 문장은 `A, not B` 대비 + 세미콜론 + 이유로 끝난다.
**핵심 표현**: `gate on (X)`(X 를 통과 기준으로 삼다), `more than a fifth of`(5분의 1 이상; 0.2 를 말로), `systemic failure`(전면 장애).
**격식 짝**:
- refined: The job should be failed only when the failure rate indicates a systemic problem rather than isolated outages. (작성)
- plain: Don't kill the job just because a couple of tools are down; only bail when it's clearly broken across the board. (작성)

<sub>출처: 모범 단락(작성) — repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md 케이스 5 "결과 읽기 & 알림" 바탕</sub>
