# 2026-10-30 — 새 표현

오늘 배치의 repo 문서는 거의 다 한국어다. 아래 표현은 그 한국어 문서 속에 영어로 박혀 있던 용어·주석이고, 원문이 구 조각뿐이라 예문 대부분은 직접 지었다(작성 표시).

## "user-confirmed (2026-08-21)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 문서 속 사실 옆에 "누가·언제 확인했는지"를 꼬리표로 붙일 때(기술 문서·격식)
- 한국어: 사용자가 확인함(날짜)
- 설명: confirmed by the user 를 하이픈으로 묶어 형용사 한 단어로 만들었다. 괄호 속 날짜와 짝을 이뤄 출처 표시가 된다. 같은 문서에 user-noted 도 나오는데, 두 꼬리표는 확인의 강도가 다르다(다음 항목).
- 예문: The align image is a single `IMAP{p:04d}.jpeg`, just as on CD-SEM (user-confirmed 2026-08-21). (작성)
- 유사어: verified on site (현장 검증 강조), per the office (구어, '사무실 말로는')
- 반의어: unverified (아직 확인 안 됨), assumed (가정한 값)

## "user-noted"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 확인된 사실은 아니고 사용자가 주의만 준 내용을 표시할 때(기술 문서)
- 한국어: 사용자가 언급함(확인된 사실은 아님)
- 설명: note 는 '언급하다·짚어 두다'라서 confirmed 보다 약하다. 원문은 "이 key 이름들은 바뀔 수 있다"는 경고에 이 꼬리표를 붙였다. 사실이 아니라 경고를 들었다는 기록이다. 두 꼬리표를 나눠 쓰면 독자가 근거의 무게를 알 수 있다.
- 예문: These key names may change as the office parser reads more of the raw data (user-noted 2026-07-30). (작성)
- 유사어: flagged by the user (경고 느낌이 더 강함), per a heads-up from the user (구어)
- 반의어: user-confirmed (확인까지 된 사실)

## "targeting sub-position"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 한 측정점 안에서 다시 나뉜 세부 위치(-U/-T/-M/-L)를 가리킬 때(장비·기술 문서)
- 한국어: (측정 대상을 겨누는) 하위 위치
- 설명: sub- 는 '아래 단계의'. targeting 이 앞에서 수식해 '조준용' 하위 위치라는 뜻이 된다. split ~ into files by sub-position 처럼 by 와 같이 자주 쓴다.
- 예문: HV-SEM splits one measurement slot into several files, one per targeting sub-position. (작성)
- 유사어: sub-site (반도체 측정에서 흔함), sub-location (일반어)

## "4-digit zero padding"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 번호를 고정 자릿수로 맞춰 앞을 0으로 채우는 규칙을 설명할 때(코드·문서)
- 한국어: 네 자리 0 채우기
- 설명: pad 는 '빈 곳을 채우다'. 동사로는 zero-pad, 형용사로는 zero-padded 를 쓴다. 원문의 경고처럼 "ENAP000" + str(p) 는 p = 10 에서 자릿수가 깨진다. 패딩은 포맷 지정자(`{p:04d}`)에 맡기는 게 맞다.
- 예문: Point numbers are zero-padded to four digits, so P.No 1 becomes `ENAP0001`. (작성)
- 유사어: leading zeros (구어, 가장 흔함), fixed-width numbering (격식, 개념 설명)

## "side-by-side"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/align-crosshair/crosshair_overlay_from_cond.md
- 맥락: 두 화면·두 결과를 나란히 놓고 비교할 때(회의·문서 모두)
- 한국어: 나란히(놓고)
- 설명: 명사 앞에서는 하이픈을 넣어 a side-by-side comparison, 부사로 쓸 때는 보통 하이픈 없이 put them side by side. 원문은 배율이 다른 OM 과 SEM 을 좌표로 합치지 말고 나란히 두라고 했다.
- 예문: Place the OM and SEM images side by side and draw each with its own cond. (작성)
- 유사어: next to each other (구어), in parallel columns (문서 레이아웃), juxtaposed (격식·문어)
- 반의어: overlaid (겹쳐서), merged into one view

## "firewalled / firewall-free"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md
- 맥락: 네트워크 다이어그램에서 어느 쪽이 방화벽 안이고 어느 쪽이 밖인지 표시할 때(기술 문서)
- 한국어: 방화벽에 막힌 / 방화벽이 없는
- 설명: firewall 을 동사처럼 써서 과거분사 firewalled(방화벽에 갇힌)를 만들었다. -free 는 '~이 없는'(sugar-free 와 같은 조어)이다. 둘을 짝지으면 다이어그램 라벨이 한 단어씩으로 끝난다.
- 예문: The client PC is firewalled, so it reaches the FTP servers through a proxy on a firewall-free host. (작성)
- 유사어: behind the firewall (구어, 더 흔함), on the open side / outside the firewall (구어)

## "each doc stamped (minio_key)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md
- 맥락: 저장한 레코드마다 추적용 키·시각 등을 찍어 둔다고 말할 때(데이터 파이프라인)
- 한국어: 각 문서에 (minio_key 를) 찍어 둠
- 설명: stamp A with B 는 'A 에 B 를 도장처럼 찍다'. 원문은 다이어그램 라벨이라 is 를 뺀 분사구문이다. 색인된 문서마다 원본 바이트가 있는 MinIO 키가 붙어 있어서, 문서에서 원본으로 거슬러 갈 수 있다.
- 예문: Each OpenSearch doc is stamped with the `minio_key` of its raw source. (작성)
- 유사어: tagged with (가장 일반적), carries a reference to (설명적·격식)

## "(bytes released)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md
- 맥락: 처리가 끝난 데이터를 메모리에서 놓아준다는 걸 짧게 적을 때(코드 주석·다이어그램)
- 한국어: (처리 후) 바이트를 놓아줌
- 설명: release 는 잡고 있던 자원(메모리·락·연결)을 놓아주는 동사다. 수동 분사 한 단어로 "여기서 메모리가 풀린다"를 알린다. 최대 RAM 이 플릿 전체가 아니라 concurrency × 파일 크기에 머무는 근거가 이 한 줄이다.
- 예문: Once the doc is indexed, the bytes are released, so peak RAM stays at concurrency times file size. (작성)
- 유사어: freed (메모리에 한정, 기술 구어), dropped (구어, 더 가벼움)
- 반의어: held / retained (붙잡아 둔)

## "systemic failure"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md
- 맥락: 개별 실패가 아니라 시스템 전체가 망가졌다고 판정할 때(장애 보고·코드 메시지)
- 한국어: 구조적(전면적) 실패
- 설명: systemic 은 '체계 전체에 걸친'. 원문은 장비 몇 대가 꺼지는 건 정상으로 보고, 성공이 0이거나 실패율이 20%를 넘을 때만 이 메시지로 작업을 실패시킨다. systematic(체계적인, 계획적인)과 헷갈리기 쉽다.
- 예문: `raise RuntimeError(f"systemic failure: ok={report.ok} ng={report.ng}")`
- 유사어: a fleet-wide outage (구체적), widespread failure (일반어), a total failure (구어·과장)
- 반의어: an isolated failure (고립된 개별 실패)

## "re-export hub"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/summary.md
- 맥락: 패키지가 하위 모듈 이름을 다시 내보내 한 곳에서 import 하게 한다고 설명할 때(코드 구조 문서)
- 한국어: 재노출 허브(하위 이름을 모아 다시 내보내는 곳)
- 설명: re-export 는 받아온 이름을 다시 export 한다는 뜻이고, hub 는 바퀴 중심처럼 여러 갈래가 모이는 곳이다. 그래서 호출부는 리프 모듈 경로를 몰라도 된다.
- 예문: Each subpackage is a re-export hub, so callers import leaf names from the package itself. (작성)
- 유사어: a facade module (설계 용어, 더 넓은 뜻), a barrel file (JS/TS 진영의 같은 개념)

## "copy-out"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/summary.md
- 맥락: 파일 몇 개를 패키지 밖으로 복사해 다른 PC에서 단독으로 쓰는 방식을 말할 때(배포 문서)
- 한국어: 밖으로 복사해 단독 사용(하는 방식)
- 설명: 원문은 명사·형용사로 쓴다("copy-out proxy 번들", "copy-out: …"). 동사로는 하이픈 없이 copy the files out 이다. 표준 라이브러리만 쓰는 모듈이라 bare 이름으로 함께 따라갈 수 있다는 설명과 같이 나온다.
- 예문: For a copy-out, drop these four files flat on the client PC and import them by bare name. (작성)
- 유사어: a vendored copy (패키지째 들여온 사본), a standalone drop (구어)

## "in-process registry"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/guides/usage.md
- 맥락: 상태가 한 프로세스 메모리 안에만 있어 다른 워커와 공유되지 않는다고 경고할 때(서버 설계)
- 한국어: 프로세스 내부(메모리) 레지스트리
- 설명: in-process 는 '같은 프로세스 안에서'. 그래서 gunicorn -w N 처럼 워커가 여럿이면 상태 폴링이 그 job 을 모르는 워커에 닿을 수 있다. 대안으로 Redis 같은 out-of-process 저장소가 따라 나온다.
- 예문: The registry is in-process, so a status poll may hit a worker that never saw the job. (작성)
- 유사어: process-local (같은 뜻, 더 직설적), in-memory (저장 위치에 초점)
- 반의어: out-of-process / shared (Redis 등 외부 저장소)

## "cond sidecar"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 본 파일 옆에 붙어 다니는 부속 메타데이터 파일을 가리킬 때(파일 포맷·기술 문서)
- 한국어: 곁따르는 cond 파일(이미지 옆의 부속 파일)
- 설명: sidecar 는 오토바이 옆에 붙는 칸이다. 기술 용어로는 '본체 옆에 붙어 다니는 보조 파일·프로세스'다. 원문은 cond 가 slot 단위가 아니라 파일마다 하나씩 붙는다는 점을 강조한다.
- 예문: The cond sidecar is per file, not per slot: `.IMMS0001-U.jpeg/cond.txt`. (작성)
- 유사어: companion file (일반어), metadata file (평이)

## "covered by a tracked contract test"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/recipe_idp.txt
- 맥락: 지금 재현할 수 없는 경로도 테스트로는 지켜 두겠다고 말할 때(테스트 전략 문서)
- 한국어: 추적되는 계약 테스트로 덮는다
- 설명: cover 는 테스트 커버리지의 그 cover 다. contract test 는 내부 구현이 아니라 두 쪽이 약속한 입출력 모양만 확인한다. tracked 는 저장소에 커밋돼 계속 돌아간다는 뜻이다. 원문은 결측값을 mock 이 만들지 않는 대신 adapter 가 견디도록 짜고, 그 경로를 이 테스트로 덮는다.
- 예문: The mock does not produce NaNs, but the adapter tolerates them, and that path is covered by a tracked contract test. (작성)
- 유사어: pinned by a test (구어, '테스트로 고정'), guarded by a regression test (회귀 방지에 초점)
- 반의어: untested path (테스트 안 된 경로)
