# 2026-07-30 — 새 표현

## "lying around"

- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 정리 안 된 채 방치된 것을 가볍게 가리킬 때(구어, 동료 사이). 보고서에는 잘 안 씀.
- 한국어: 남아서 굴러다니는, 치우지 않고 방치된
- 설명: 물건이든 브랜치든 "쓰이지도 않고 자리만 차지하는" 상태. `What *is* lying around is …` 처럼 강조 도치와 붙어 "정작 남은 건 이것"이라는 뜻이 된다.
- 예문: What is lying around is ten stale local branches, none of them merged into main.
- 유사어: left over (중립·사실 서술), sitting there unused (더 풀어쓴 구어), dormant (격식, 죽은 게 아니라 잠든 뉘앙스)
- 반의어: cleaned up, tracked and in use

## "carry something forward on faith"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 이전 기록을 검증 없이 그대로 옮겨 적는 태도를 비판하거나, 그러지 않았음을 밝힐 때(문서·회고, 격식 중간).
- 한국어: 확인 없이 믿고 그대로 이어 적다
- 설명: `carry forward` 는 이월하다, `on faith` 는 근거 없이 믿고. 둘을 붙이면 "검증 대신 신뢰로 넘긴다"는 결이 생긴다. 보통 `rather than` 과 짝지어 자기 검증 절차를 강조한다.
- 예문: Every item was checked against the code rather than carried forward on faith.
- 유사어: take at face value (액면 그대로 받아들이다, 구어에 가까움), rubber-stamp (형식적으로 승인, 더 비판적), assume it still holds (평이·중립)
- 반의어: verify against the source, re-derive from scratch

## "drift from reality"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 문서·백로그·주석이 코드와 어긋난 걸 지적할 때(리뷰·회고, 중립 격식).
- 한국어: 실제와 어긋나다, 현실에서 멀어지다
- 설명: 한 번에 틀린 게 아니라 시간이 지나며 서서히 벌어졌다는 뉘앙스가 `drift` 에 들어 있다. 그래서 비난보다 관리 실패를 가리킨다.
- 예문: Two backlog items had drifted from reality, so I corrected both rather than copying them forward.
- 유사어: go stale (짧고 구어적), fall out of sync (기술 문맥에서 가장 흔함), no longer reflect the code (풀어쓴 격식)
- 반의어: stay in sync, reflect the current state

## "the real tiebreaker"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 여러 판단 근거가 엇갈릴 때 결론을 낸 결정적 근거를 지목하며(설명·리뷰, 중립).
- 한국어: 승부를 가른 결정적 근거
- 설명: 원래 스포츠의 동점 결승. 기술 문맥에서는 "A 도 B 도 애매했는데 이것이 결론을 냈다"는 자리에 쓴다. 앞에 애매했던 근거를 먼저 깔아야 자연스럽다.
- 예문: `git cherry` still reports a false miss when context lines shift, which is why the blob comparison was the real tiebreaker.
- 유사어: the deciding factor (가장 무난·격식), what settled it (구어), the clincher (구어, 다소 극적)
- 반의어: inconclusive evidence, a wash

## "half right"

- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt c3d8d75e
- 맥락: 상대의 보고·추측을 정면으로 부정하지 않고 절반만 정정할 때(구어~중립). 상대 체면을 지키면서 사실을 바로잡는 표현.
- 한국어: 절반은 맞다
- 설명: `half right` 뒤에 "틀린 절반이 오히려 원인을 가리킨다"를 붙이면 정정이 공격이 아니라 단서가 된다. 대화형 코드 리뷰에서 아주 쓸모 있는 문형.
- 예문: Your report was half right, and the half that was wrong points at the real cause.
- 유사어: partly true (더 밋밋·중립), right about X, not about Y (구조를 드러내는 대구), not quite (완곡한 부정)
- 반의어: spot on, exactly right

## "replace something wholesale"

- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt c3d8d75e
- 맥락: 부분 교체가 아니라 통째 교체임을 경고할 때(설계 설명·문서, 중립 격식).
- 한국어: 통째로 갈아치우다
- 설명: 부사 `wholesale` 은 "선별 없이 전부". slot override 처럼 "일부만 바꾸려 했는데 딸린 것까지 사라진다"를 설명하는 데 잘 맞는다.
- 예문: Supplying your own header slot replaces that fallback wholesale — title, description, and the close button.
- 유사어: swap out entirely (평이·구어), override in full (기술 문맥), supersede (격식, 공식 대체)
- 반의어: patch selectively, override just one field

## "orders of magnitude below"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0ff1832b
- 맥락: 성능 걱정을 수치 감각으로 잠재울 때(코드 리뷰·설계 논의, 중립).
- 한국어: 자릿수가 몇 단계 낮은, 비교 자체가 안 되는 수준으로 작은
- 설명: `4–5 orders of magnitude` 처럼 자릿수를 세어 붙이면 "무시해도 된다"가 주관이 아니라 계산이 된다. `below` 대신 `smaller than` 도 되지만 비용 비교에는 `below` 가 더 흔하다.
- 예문: Both are four to five orders of magnitude below the FTP round-trip that fetched the file, so neither can slow the server measurably.
- 유사어: negligible next to (짧고 단정적), dwarfed by (수동, 다소 문어적), in the noise (구어, 측정 오차 수준이라는 뜻)
- 반의어: on the same order as, the dominant cost

## "move under someone"

- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 0ff1832b
- 맥락: 내가 작업하는 사이 다른 사람·세션이 기반을 바꿔 놨을 때(팀 채팅·작업 로그, 구어).
- 한국어: 내가 딛고 선 바닥이 바뀌었다
- 설명: `under me` 는 "내 발밑에서". 잘못을 따지기보다 상황 변화를 알리는 말이라 비난 톤이 아니다. main, 스키마, 설정처럼 전제로 삼던 것에 붙인다.
- 예문: Main moved under me — another session committed at 15:25, so I landed the finished work first and branched from there.
- 유사어: shifted beneath me (더 문어적), changed out from under me (구어, 불평 뉘앙스가 더 셈), was updated concurrently (격식·중립)
- 반의어: stayed put, was untouched

## "husk"

- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 내용은 빠지고 껍데기만 남은 디렉터리·구조를 가리킬 때(비유, 구어에 가까운 서술).
- 한국어: 껍데기, 알맹이 빠진 잔해
- 설명: 원뜻은 곡물 겉껍질. 파일 시스템 문맥에서 `empty husks` 는 "지웠는데 빌드 산출물만 남은 폴더"를 정확히 짚는다. 비유라 정식 문서보다 설명 글에 어울린다.
- 예문: Both directories are empty husks — 184 KB of build artifacts, no source files and no repo metadata.
- 유사어: leftovers (평이), a shell of a directory (같은 비유, 더 흔함), residue (격식·중립)
- 반의어: a working checkout, a live worktree

## "smoke-test"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0ff1832b
- 맥락: 정밀 검증 전에 "일단 굴러가는지" 훑는 확인을 가리킬 때(개발 대화, 중립).
- 한국어: 최소한만 돌려 보다, 굵직한 고장만 걸러 보다
- 설명: 명사 `smoke test` 를 그대로 동사로 쓴다. 전수 검증이 아님을 스스로 밝히는 말이라, 한계를 인정하며 진행할 때 유용하다.
- 예문: You can't smoke-test the naming at home until the stand-in is fixed.
- 유사어: sanity-check (더 가벼움, 논리 점검 쪽), do a first pass (범위를 말함), exercise the happy path (경로를 특정)
- 반의어: verify exhaustively, run the full suite

## "worth your judgment"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 내가 결론 내리지 않고 결정권을 상대에게 넘길 때(보고 말미, 정중한 격식).
- 한국어: 이건 당신이 판단할 몫이다
- 설명: `One thing worth your judgment:` 로 문단을 열면 "여기까지가 사실, 여기부터가 당신 결정"이라는 경계가 선다. 상대를 재촉하지 않으면서 책임 소재를 분명히 한다.
- 예문: One thing worth your judgment: those branch-only test names may or may not be covered by the rewrite on main.
- 유사어: your call (짧은 구어), I'd defer to you on this (정중·격식), a decision for you to make (평이한 문어)
- 반의어: I've settled this, no action needed

## "written as settled"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 0ff1832b
- 맥락: 확정으로 적어 둔 내용이 새 정보로 뒤집힐 때(설계 문서 수정, 중립 격식).
- 한국어: 확정으로 적어 둔
- 설명: `settled` 는 "더 논의할 것 없이 정해진". 새 사실을 받았을 때 `That changes two things I'd written as settled` 라고 열면, 문서를 고치는 이유가 변덕이 아니라 근거 갱신임을 드러낸다.
- 예문: That changes two things I'd written as settled, so let me look at what calls those readers before I touch anything.
- 유사어: treated as fixed (평이), taken as given (전제로 삼았다는 쪽), locked in (구어·기술)
- 반의어: still open, an open question

## "the irreversible half"

- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 위험한 작업을 되돌릴 수 있는 부분과 없는 부분으로 갈라 확인을 요청할 때(운영·배포 대화, 중립 격식).
- 한국어: 되돌릴 수 없는 쪽
- 설명: 작업을 통째로 승인받는 대신 `half` 로 쪼개면, 안전한 절반은 진행하고 위험한 절반만 확인받을 수 있다. 확인 요청을 최소화하는 실무 화법.
- 예문: Deleting the remote branches is a separate command, and I'd want you to confirm, since it's the irreversible half.
- 유사어: the destructive part (더 직설적), the one-way door (구어 비유, 의사결정 문맥), the point of no return (극적)
- 반의어: the recoverable half, a reversible change

## "bookkeeping lag"

- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 일은 끝났는데 체크박스·이슈만 안 닫힌 상태를 설명할 때(진행 보고, 중립).
- 한국어: 기록만 안 따라온 것
- 설명: 문제 없음을 한 마디로 정리하는 표현. `Bookkeeping lag only.` 처럼 짧게 끊으면 "실제 결함 아님"이 분명해져 상대가 다시 확인하러 가지 않는다.
- 예문: The plan's checkboxes are all unticked, but every function is on main with tests — bookkeeping lag only.
- 유사어: a paperwork gap (더 일상적), stale tracking (원인을 지목), out-of-date bookkeeping (평이한 문어)
- 반의어: genuinely unfinished, still open in code

## "the documented normal case"

- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0ff1832b
- 맥락: 예외처럼 보이는 동작이 사실은 정상 시나리오임을 못박을 때(설계 설명·PR 본문, 중립 격식).
- 한국어: 문서에 적힌 정상 동작
- 설명: `not failures — that's the documented normal case` 처럼 부정 뒤에 붙이면, 왜 오류로 처리하지 않았는지가 설계 근거로 읽힌다. `documented` 가 근거의 출처까지 함께 주장한다.
- 예문: Missing files are logged and skipped, not treated as failures — that's the documented normal case.
- 유사어: expected behaviour (가장 흔함), by design (짧고 단정적), a supported state (계약 뉘앙스)
- 반의어: an error path, an unhandled edge case

## "has never met real data"

- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 134c9baf
- 맥락: 테스트는 통과했지만 실제 환경 데이터로는 한 번도 돌려 본 적 없음을 정직하게 밝힐 때(인수·검증 논의, 중립).
- 한국어: 실제 데이터를 아직 한 번도 못 만나 봤다
- 설명: `meet` 를 써서 코드와 데이터의 첫 대면을 사건처럼 만든다. "green 하지만 검증된 건 아니다"를 한 문장으로 구분해 주는 말.
- 예문: It is written and green against home stand-ins, but no part of it has met real office data.
- 유사어: unproven in production (가장 격식), never exercised against live data (풀어쓴 기술 문어), untested in the wild (구어)
- 반의어: proven against production data, office-verified
