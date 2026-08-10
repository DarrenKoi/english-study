# 2026-08-11 — 정독

## 단락 1

The measuring tool's FTP server caps concurrent sessions and engineers use their own tools against the same equipment, so a session is a shared, scarce resource. Two things make us open more of them than we need: the browser re-requests a slow image at 2.5s and 5s, and two people can open the same MSR at once. Both arrive as concurrent requests for the SAME cache key, and each used to open its own session. This module only provides the mutual exclusion. The dedup comes from the caller re-reading the cache while holding the gate. Deliberately per-process and lock-free of any store: with one worker it is exact, and with several the duplication drops from unbounded to the worker count, which the shared MinIO cache already absorbs. A Redis lease would add TTLs, polling and failure modes to buy that last factor. There is no timeout. A waiter blocking IS the intent — the alternative is giving up and going to the tool, which is the load this exists to prevent — and the fetch it waits on is already bounded by ftp_timeout / host_timeout.

**문법·구조**: 시제가 세 층으로 갈린다. 상시 사실은 현재형(`caps`, `use`, `comes`), 고쳐지기 전의 과거 습관은 `used to open`, 채택하지 않은 대안은 가정법 `would add` 다. 세 시제가 "지금 이렇다 / 예전엔 이랬다 / 만약 이랬다면"을 문법만으로 갈라 준다.
`so a session is a shared, scarce resource` 의 `so` 는 앞 두 사실에서 결론을 뽑는 접속사이고, 뒤이어 나오는 `which the shared MinIO cache already absorbs` 는 앞 절 **전체**를 받는 비제한 관계절이다(선행사가 단어 하나가 아니라 "중복이 워커 수로 줄어든다"는 사실 전체).
마지막 문장의 `A waiter blocking IS the intent` 에서 주어는 동명사구 `A waiter blocking`("대기자가 막히는 것")이다. 동명사에 의미상 주어를 앞에 붙이는 형태이고, `IS` 를 대문자로 세워 "그게 부작용이 아니라 의도"라고 강세를 준다. 그 뒤 em-dash 두 개로 감싼 삽입절은 "왜 의도인가"를 끼워 넣고, 문장은 끊긴 자리에서 `and the fetch it waits on...` 으로 다시 이어진다. `the fetch it waits on` 은 관계대명사를 생략한 목적격 관계절이다.
`Deliberately per-process and lock-free of any store:` 는 주어·동사가 없는 조각 문장이다. 앞 문단의 주어(this module)를 이어받는 설계 노트 특유의 압축이고, 콜론 뒤에 그 판단의 근거가 온다.

**핵심 표현**:
- `a shared, scarce resource` — 공용이면서 희소한 자원. 두 형용사를 쉼표로 나란히 놓아 각각 독립적으로 명사를 꾸민다(`shared scarce resource` 처럼 붙이면 "희소자원 중 공유되는 것"으로 읽혀 뜻이 좁아진다).
- `to buy that last factor` — 그 마지막 한 배수를 사자고. 복잡도를 지불해 성능을 산다는 은유.
- `the load this exists to prevent` — 이것이 막으려고 존재하는 바로 그 부하. 관계절 안에 `exist to + 동사` 를 넣어 모듈의 존재 이유를 명사구 하나로 접었다.

**격식 짝**:
| refined (문어·설계 문서) | plain (구어·동료에게) |
| --- | --- |
| A waiter blocking is the intent, not a side effect. | Yeah, it's *supposed* to block there. |
| A Redis lease would add TTLs, polling and failure modes to buy that last factor. | Redis would get us the rest, but it's a lot of moving parts for not much. |

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md (`single_flight.py` docstring)</sub>

---

## 단락 2

The export contract already existed in this repo. `FailIssueRankingTable` emits `download`/`copy` carrying its sorted, filtered rows, and the parent composes headers + filename. That split matters: the table is the only thing that knows what you're looking at, while the parent is the only thing that knows the scope that belongs in the filename. Reusing it kept both new tables at zero new abstractions. The signal badges forced a judgment call. `peerGroupComparable` is false when the query spans multiple fabs, and the UI deliberately blanks the column then. The CSV honors that same gate — recomputing signals unconditionally would have produced a file that asserts more than the screen does, and a file outlives the caveat text next to it. Line vs bar isn't cosmetic here. Align-fail days are mostly 0, so the line hugs the axis and you can't count the zero days.

**문법·구조**: 단락이 **세 주장 × (선언 → 근거)** 리듬으로 짜여 있다. 각 덩어리가 짧은 단정문으로 열리고(`That split matters.` / `The signal badges forced a judgment call.` / `Line vs bar isn't cosmetic here.`), 그 뒤에 긴 설명문이 붙는다. 짧은 문장이 제목 역할을 하니 소제목 없이도 구조가 보인다.
`the only thing that knows what you're looking at, while the parent is the only thing that knows the scope` — 같은 틀(`the only thing that knows X`)을 두 번 반복하고 `while` 로 맞세워 **책임 분리**를 문장 모양 자체로 보여 준다. 대조의 `while` 은 시간이 아니라 "반면에"다.
가정법 과거완료 `would have produced` 가 "그렇게 했더라면 이런 파일이 나왔을 것"이라는 **하지 않은 선택의 결과**를 그린다. 실제 코드는 그렇게 하지 않았으므로 직설법으로 쓰면 거짓이 된다.
`Line vs bar isn't cosmetic here` 의 주어는 명사 두 개를 `vs` 로 묶은 덩어리이고 단수 취급이다("선이냐 막대냐 하는 문제"). 뒤 문장의 `so ... and you can't count` 는 원인 → 결과 → 그 결과의 실제 불편을 한 호흡에 잇는다.

**핵심 표현**:
- `That split matters.` — 그 분리가 중요합니다. 앞 문장을 `That + 명사` 로 되받아 논점을 한 단어에 고정하는 자리(`That distinction matters` / `That ordering matters` 로도 확장된다).
- `the UI deliberately blanks the column` — 화면이 일부러 그 칸을 비운다. `blank` 를 타동사로 쓰면 "빈 채로 만든다"는 능동적 결정이 되고, `deliberately` 가 버그가 아님을 못박는다.
- `honors that same gate` — 같은 판정 조건을 (내보내기도) 지킨다. `honor` 는 계약·설정을 "존중해 따른다"는 기술 문서 상용어다.

**격식 짝**:
| refined (문어·설계 근거) | plain (구어·리뷰 코멘트) |
| --- | --- |
| Recomputing the signals unconditionally would have produced a file that asserts more than the screen does. | If we just recomputed them, the CSV would say more than the UI does. |
| Reusing it kept both new tables at zero new abstractions. | We reused it, so nothing new had to be invented. |

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)</sub>

---

## 단락 3

The directory survives, but it is not a worktree anymore — `.git` is gone, so any git command inside it fails. What's left is 27 files, all gitignored build output. No source files, no commits, nothing unmerged. Safe to delete. This is the standard tail of `git worktree remove`: it deletes tracked files and the `.git` pointer, but refuses to touch untracked or ignored files it didn't create. Nuxt regenerates `.nuxt/` on every `npm run dev`, so a worktree where you ran the frontend always leaves this shell behind. The registry being clean while the directory persists is why `git worktree prune` reports nothing — prune only garbage-collects metadata whose checkout vanished, which is the opposite of this case.

**문법·구조**: `What's left is 27 files` 는 의문사 `what` 이 이끄는 명사절을 주어로 세운 **what-분열문**이다. "남아 있는 것은 ~다"처럼 결론을 뒤로 미뤄 강조하는 구조이며, 이때 동사는 뒤의 복수(`27 files`)가 아니라 명사절에 맞춰 `is` 를 쓴다.
`No source files, no commits, nothing unmerged. Safe to delete.` 는 동사 없는 조각 문장 넷을 연달아 놓았다. 점검 항목을 하나씩 지워 나가는 리듬이라, 완전한 문장으로 풀면 오히려 늘어진다. 기술 보고에서 허용되는 생략이다.
`refuses to touch untracked or ignored files it didn't create` — 도구를 의인화한 `refuses` 가 "못 지운다"가 아니라 "일부러 안 지운다"는 설계 의도를 담는다. 뒤의 `it didn't create` 는 관계대명사를 생략한 목적격 관계절.
마지막 문장의 주어는 동명사구 `The registry being clean`("레지스트리가 깨끗하다는 사실")이고, 그 뒤 `while the directory persists` 가 대조 부사절, `is why ...` 가 술부다. 즉 **[사실] is why [현상]** 이라는 인과 틀에 동명사 주어를 얹었다. 끝의 `which is the opposite of this case` 는 앞 절 전체를 받는 비제한 관계절이다.

**핵심 표현**:
- `the standard tail of X` — X 의 흔한 뒤끝. `tail` 을 "작업이 끝난 뒤 남는 꼬리"로 써서, 이상 현상이 아니라 예상된 잔여물임을 알린다.
- `leaves this shell behind` — 껍데기만 남긴다. `leave behind` 는 떠나면서 뒤에 두고 간다는 뜻이고, `shell` 은 알맹이(소스·git 메타데이터)가 빠진 빈 껍질이다.
- `nothing unmerged` — 병합 안 된 것은 없다. `nothing + 과거분사` 로 "그런 상태인 것이 하나도 없다"를 두 단어에 담는 압축형(`nothing broken`, `nothing pending`).

**격식 짝**:
| refined (문어·보고서) | plain (구어·슬랙) |
| --- | --- |
| The registry being clean while the directory persists is why `prune` reports nothing. | `prune` says nothing's there because git already forgot about it — the folder just stuck around. |
| No source files, no commits, nothing unmerged. | There's nothing in it worth keeping. |

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/2ca1e865 (assistant)</sub>
