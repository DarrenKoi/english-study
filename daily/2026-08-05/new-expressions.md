# 2026-08-05 — 새 표현

## "endpoint ergonomics"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 기능이 아니라 "쓰기 편한 정도"를 고치는 작은 개선에 이름을 붙일 때(설계 문서·PR 설명)
- 한국어: (API·도구의) 사용 편의성, 손에 붙는 정도
- 설명: ergonomics 는 원래 인체공학이지만 개발 문서에서는 "기능은 같은데 쓰는 사람 손에 얼마나 잘 붙는가"를 뜻한다. API ergonomics, developer ergonomics 처럼 쓴다. 새 데이터 경로 없이 헤더 하나·필터 하나만 더한 이번 변경을 계획서가 "two small endpoint ergonomics fixes" 라고 불렀다.
- 예문: This plan adds no new data path — just documentation plus two small endpoint ergonomics fixes.
- 유사어: developer experience / DX (더 넓은 개념), usability (일반어), quality-of-life improvements (도구·게임권 구어)
- 반의어: a hostile API / clunky (쓰기 불편한)

## "on purpose"
- 레지스터: conversational, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 이상해 보이는 선택이 실수가 아니라 의도임을 짧게 못 박을 때(주석·docstring·구어)
- 한국어: 일부러, 의도적으로
- 설명: deliberately 의 평이한 회화체. "Standard library only, on purpose" 처럼 선언 뒤에 꼬리로 붙이고, 바로 다음에 이유가 따라오는 것이 관례다. 표준 라이브러리만 쓴 것이 게을러서가 아니라 pip 없는 PC 를 위해서라는 방어.
- 예문: Standard library only, on purpose — this file is meant to be copied to a user's machine that may have no pip install.
- 유사어: by design (설계상 그렇다는 격식형), deliberately (문어), intentionally (중립)
- 반의어: by accident / inadvertently (뜻하지 않게)

## "turnkey"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 받는 사람이 조립 없이 돌리기만 하면 되는 상태로 만들어 넘길 때(업무 보고)
- 한국어: 열쇠만 돌리면 되는, 즉시 가동 상태의
- 설명: 건설업에서 온 말로, 열쇠(key)를 돌리기(turn)만 하면 되는 완성품 인도를 뜻한다. "Let me make the fix turnkey" 는 "사무실에서 명령 한 줄이면 끝나게 만들어 드리겠다"는 뜻. 형용사로도(a turnkey solution) 쓴다.
- 예문: Let me make the fix turnkey — check what publish_rules needs and give you a one-command seed script.
- 유사어: plug-and-play (연결만 하면 됨), out-of-the-box (기본 설정으로 바로 됨), ready-to-run
- 반의어: some assembly required (받는 쪽이 조립해야 함)

## "tear down"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 임시로 세운 것(worktree·서버·픽스처)을 걷어낼 때. set up 의 반대짝
- 한국어: (세웠던 것을) 걷어내다, 철거하다
- 설명: 세우는 쪽이 set up / stand up 이면 걷는 쪽이 tear down 이다. 테스트 프레임워크의 setup/teardown 이 같은 짝. "worktree torn down" 처럼 수동형 보고에도 자주 나온다.
- 예문: Merge the branch and tear the worktree down.
- 유사어: dismantle (격식·문어), remove (중립), clean up (더 넓게 정리)
- 반의어: set up / stand up (세우다)

## "tell them apart (on the spot)"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 헷갈리는 두 경우를 구별한다고 말할 때. 구어에서는 distinguish 보다 이쪽
- 한국어: 둘을 (그 자리에서) 구별하다
- 설명: tell A and B apart / tell them apart 가 기본형. on the spot(그 자리에서 즉시)을 붙이면 "따로 조사하지 않아도 바로 판별된다"가 된다. 툴팁 하나가 "룰 미발행"과 "전부 gray" 라는 두 원인을 즉석에서 갈라 준다는 문맥.
- 예문: The coverage tooltip now tells the two causes apart on the spot.
- 유사어: distinguish (격식), differentiate (문어·학술), disambiguate (용어·기술)
- 반의어: conflate (뭉뚱그리다)

## "honor (a filter)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 코드가 옵션·계약·설정을 무시하지 않고 지켜 동작함을 말할 때(문서·주석)
- 한국어: (설정·계약을) 지키다, 존중해 반영하다
- 설명: honor 는 사람에게 쓰면 "예우하다"지만 기술 문서에서는 "플래그·계약을 실제로 반영해 동작하다"는 관용 동사다. honor the timeout, honor the cache header 처럼 목적어만 바꿔 쓴다. 수동형(is honored)이 특히 흔하다.
- 예문: The job is scoped to `names`, so an ext filter is honored and files already cached are not refetched.
- 유사어: respect (거의 동의), comply with (규정 준수 쪽 격식), take into account (더 약함)
- 반의어: ignore / bypass (무시하고 지나가다)

## "heavy-tailed"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 소수의 바쁜 항목과 다수의 한산한 꼬리로 치우친 분포를 말할 때(데이터·mock 설계)
- 한국어: 꼬리가 두꺼운(치우친) 분포의
- 설명: 통계 용어 heavy-tailed distribution 에서 온 형용사. 같은 문장의 "a few busy devices, a long quiet tail" 처럼 머리(head)와 꼬리(tail)의 대비로 풀어 쓰면 비전공자에게도 통한다. 측정 상위 N 필터가 의미 있으려면 mock 도 이렇게 치우쳐 있어야 한다는 문맥.
- 예문: The mock generates deterministic heavy-tailed counts per lot_cd — a few busy devices, a long quiet tail.
- 유사어: skewed (치우친, 일반어), long-tailed (비즈니스권), power-law (더 엄밀)
- 반의어: uniform / evenly distributed (고른)

## "reasoned from the spec, not observed"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 어떤 주장이 명세에서 추론한 것이지 실제로 관측한 것이 아님을 구분할 때(검증 계획)
- 한국어: 명세에서 추론했을 뿐 실측한 것은 아니다
- 설명: 근거의 등급을 나누는 `A, not B` 대구. 이 한 구절이 "그래서 브라우저 확인 단계를 넣는다"는 후속 작업을 정당화한다. 이 저장소가 `office 확인`과 `OFFICE-VERIFY` 를 가르는 습관의 영어판이다.
- 예문: The claim that inline is neutral for `<img>` was reasoned from the spec, not observed.
- 유사어: inferred rather than verified, on paper (실제로는 미확인이라는 구어)
- 반의어: empirically confirmed / observed (실측으로 확인된)

## "neutral for (both paths)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 어떤 변경이 특정 소비자에게 아무 부작용도 없음을 주장할 때(설계 근거)
- 한국어: (그 경로에는) 아무 영향이 없는, 중립인
- 설명: neutral 은 "이롭지도 해롭지도 않은, 동작을 바꾸지 않는"이라는 뜻. 헤더·플래그를 더해도 기존 소비자(갤러리의 `<img>` 와 `fetch()`)가 달라지지 않음을 for/to 로 대상을 붙여 말한다.
- 예문: The gallery reads these bytes through `<img>` and `fetch()`, and inline is neutral for both.
- 유사어: a no-op for (더 강한 기술어), transparent to (있는 줄도 모르는), harmless (약함)
- 반의어: intrusive / behavior-changing (동작을 바꾸는)

## "for no gain"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 위험·비용만 지고 얻는 것이 없는 선택을 기각할 때(대안 비교)
- 한국어: 얻는 것 하나 없이
- 설명: "add X for no gain" 꼴로 비용(risk, complexity)을 목적어에 놓고 뒤에 붙여, 트레이드오프가 한쪽으로만 기울었음을 짧게 선언한다. attachment 를 기각한 한 줄 근거.
- 예문: Attachment would add browser-behavior risk for no gain.
- 유사어: to no benefit (문어), with nothing to show for it (구어·사후 평가), needlessly (부사형)
- 반의어: a net win (합계가 이득)

## "exist to prevent (X)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md
- 맥락: 파일·테스트·규칙의 존재 이유를 "막으려는 실수 하나"로 요약할 때(커밋 메시지·문서)
- 한국어: X 를 막으려고 존재한다
- 설명: 사물 주어 + exist to + 동사로 존재 이유를 못 박는 틀. this test exists to prevent regressions, this doc exists to answer one question 처럼 응용한다. "가장 자연스러워 보이는 사용법이 곧 최악의 사용법"일 때 참조 구현을 배포하는 이유를 이 한 구가 요약한다.
- 예문: Skipping the warm turns N images into N serial FTP round trips, which is the mistake this file exists to prevent.
- 유사어: is there to stop (구어), whose whole point is to (더 구어), be designed to prevent (중립)

## "fork on"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 다음 진행이 몇 가지 사실 확인에 따라 갈라진다고 말할 때(질문의 앞머리)
- 한국어: (몇 가지 사실에 따라) 갈라지다
- 설명: fork 는 길이 두 갈래로 나뉘는 지점. "X forks on Y" 는 Y 의 값에 따라 X 의 경로가 달라진다는 뜻이다. 같은 날 다른 세션의 "This one distinction forks the whole investigation" 처럼 주어를 바꿔도 쓴다. 질문하기 전에 "왜 물어야 하는지"를 정당화하는 문형.
- 예문: The fixes fork on a few facts only you know, so let me ask before I implement.
- 유사어: hinge on (성패가 달려 있다), depend on (중립), branch on (코드 뉘앙스)
- 반의어: converge (갈라졌던 경로가 다시 합쳐지다)

## "momentum is cheapest there"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/bdade38d
- 맥락: 여러 후보 중 "이미 하던 일"부터 잡는 이유를 댈 때(하루 시작·우선순위)
- 한국어: 거기서 다시 탄력을 얻는 비용이 가장 싸다
- 설명: 추진력(momentum)을 되찾는 비용이 가장 싼 곳, 즉 관성이 남아 있는 일부터 손대라는 뜻. 우선순위 판단을 비용 은유(cheap) 하나로 정당화한다. next action 이 이미 적혀 있는 in-progress 항목을 추천하는 근거였다.
- 예문: Resume the top in-progress item first — its next action is already written and momentum is cheapest there.
- 유사어: the path of least resistance (저항이 가장 적은 길), pick up where you left off (구어)
- 반의어: a cold start (관성이 전혀 없는 시작)

## "come back empty"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 조회·검색이 오류 없이 빈 결과만 돌려줄 때(버그·위험 서술)
- 한국어: (조회가) 빈손으로 돌아오다
- 설명: 요청이 빈손으로 돌아온다는 그림. 예외가 아니라 0건이라 발견이 늦는 실패 유형 — 이 저장소가 반복해서 경계하는 "zero rows with no error" — 를 한 구로 말한다.
- 예문: Confirm R3 documents actually carry fab_id="R3" — otherwise only the R3 ranking comes back empty.
- 유사어: return zero rows (더 명시적), turn up nothing (탐색 쪽 구어), draw a blank (사람 기억 쪽 관용구)
- 반의어: return hits (결과가 잡히다)

## "age out (of the window)"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/e0858fc1
- 맥락: 시간 창(보존 기간·최근성 필터)이 흐르며 항목이 자격을 잃고 빠질 때
- 한국어: 기간이 지나 (조건 밖으로) 밀려나다
- 설명: age(나이 들다) + out(밖으로) — 시간이 지나 조건 밖으로 밀려나는 자동사구. 캐시 만료, 보존 정책, 최근 90일 창 어디에나 쓴다. TTL expiry 를 사람 냄새 나게 말하는 방법.
- 예문: A cart item that ages out of the window still renders, because the lot index stays unfiltered.
- 유사어: expire (기계적), roll off (로그·보존 쪽), fall out of the window (풀어쓴 형태)
- 반의어: stay in scope / remain fresh (아직 창 안에 있다)

## "cheapest first"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt/bdade38d
- 맥락: 진단·조사 단계를 비용 순으로 배열했음을 알릴 때(계획 제시)
- 한국어: 싼 것부터 (순서로)
- 설명: 목록의 정렬 기준을 콤마 뒤에 붙이는 압축형 — oldest first, smallest first 와 같은 꼴. "the ladder(사다리), cheapest first" 로 짝지어 "아래 칸부터 올라간다"는 그림을 만든다. DevTools 확인(2분) → 로그 grep → probe 실행 순으로 세운 조사 계획의 제목이었다.
- 예문: Here's the ladder, cheapest first — the first two steps need no Python and decide whether the rest is even needed.
- 유사어: in order of cost (풀어쓴 격식형), start with the cheap checks (동사형)
