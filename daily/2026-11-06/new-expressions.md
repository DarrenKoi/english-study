# 2026-11-06 — 새 표현

오늘 배치의 repo 문서(skewnono_v3_nuxt office-migration 6차 회신·datatables, ftp_handler 가이드)는 거의 한국어입니다. 그래서 표현은 skewnono 서브에이전트에게 준 작업 지시서 두 편(AFM "이상 측정 조사 묶음", 스큐보아 S7 기준·대상 비교)에서 골랐습니다. 요구사항을 빈틈없이 적어야 하는 글이라 범위를 긋고 예외를 막는 표현이 많습니다.

## "in turn"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (AFM 조사 묶음 지시서, Why)
- 맥락: 여러 대상을 하나씩 돌아가며 처리하는 수고를 묘사할 때(현황 설명·회의)
- 한국어: 차례로, 하나씩 돌아가며
- 설명: 원문은 `the engineer today opens each suspect measurement's detail page in turn and copies values by hand` 입니다. `each ... in turn` 이 붙으면 "하나 열고, 닫고, 다음 것 열고"의 반복이 그려집니다. 지금 방식이 번거롭다는 불만을 형용사 없이 전합니다. 문두의 `In turn,` 은 "그 결과 다시"라는 다른 뜻이니 구분하세요.
- 예문: Today I open each office reply in turn and copy the field names into the datatables doc by hand.
- 유사어: one by one (가장 평이), one after another (연속성 강조), sequentially (기술 문서체)
- 반의어: all at once, side by side

## "sits outside the band"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6
- 맥락: 측정값·지표가 기준 범위 바깥에 있다고 담담하게 말할 때(분석 리포트·대시보드 설명)
- 한국어: (값이) 기준 범위 밖에 있다
- 설명: `be` 대신 `sit` 를 써서 값이 그래프 위 어느 자리에 "놓여 있는" 모습을 그립니다. `fall outside` 는 떨어지는 움직임이 느껴지는 반면 `sit` 는 상태만 말합니다. "불량"이라는 판정을 피해야 하는 이 지시서의 태도와 잘 맞습니다.
- 예문: Two lots sit outside the group band, but nothing in the report calls them defective.
- 유사어: falls outside the range (가장 흔함), lies outside (문어), is out of band (기술 축약)
- 반의어: sits within the band, stays inside the range

## "the reference moves with the selection"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96 (S7 지시서, Why)
- 맥락: 비교 기준이 고정돼 있지 않고 사용자가 고른 데이터에 따라 바뀐다는 문제를 짚을 때(설계 근거)
- 한국어: 기준이 선택에 따라 같이 움직인다
- 설명: 원문은 `Every statistic ... is computed from the set the user picked, so the reference moves with the selection.` 입니다. `move with` 는 "~와 함께 움직이다", 곧 "~에 종속돼 있다"입니다. 기준점이 흔들리면 비교가 의미를 잃는다는 지적을 짧은 동사 하나로 끝냅니다. 이 문장이 바로 뒤의 해법 "fixed reference"를 끌어냅니다.
- 예문: If the band is computed from whatever the user filters, the reference moves with the selection and last week's numbers can't be compared.
- 유사어: the baseline shifts with the selection (거의 같은 뜻), the reference isn't fixed (평이), is relative to the current selection (문어)
- 반의어: a fixed reference, a pinned baseline

## "with the suspects flagged in their own column"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 1, 측정 목록)
- 맥락: 표·시트 설계에서 특정 행을 별도 열로 표시하라고 요구할 때(명세·티켓)
- 한국어: 의심 항목은 전용 열에 따로 표시해서
- 설명: `with + 명사 + 과거분사` 는 부대상황 구문입니다. 긴 열 목록을 다 나열한 뒤 대시로 이어 `— with the suspects flagged in their own column` 을 덧붙여, 문장을 새로 시작하지 않고 조건 하나를 더 얹었습니다. `in their own column` 은 "다른 값과 섞지 말고 전용 열에"라는 뜻입니다.
- 예문: Export every lot, with the mismatched fab codes flagged in their own column.
- 유사어: marked in a separate column (평이), with a dedicated flag column (명사형), highlighted (시각 강조 쪽)
- 반의어: mixed in with the rest, left unmarked

## "is omitted rather than written empty"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 1 끝)
- 맥락: 내용이 없을 때 빈 껍데기를 만들지 말고 아예 빼라고 규칙을 정할 때(출력 명세·문서 규칙)
- 한국어: 빈 채로 쓰지 말고 아예 뺀다
- 설명: 원문 `Any sheet with nothing to say is omitted rather than written empty.` 에서 시트를 의인화한 `with nothing to say`(할 말이 없는)가 재치 있습니다. `rather than` 뒤도 `written empty` 로 수동 과거분사를 맞춰 대구를 만들었습니다. `write ... empty` 는 "빈 채로 쓰다"라는 5형식 구조입니다.
- 예문: A section with nothing to say is omitted rather than written empty, so the digest never shows a bare heading.
- 유사어: is skipped instead of left blank (평이), is dropped when empty (짧은 규칙체), only appears when it has content (긍정형으로 바꿔 말하기)
- 반의어: is always included, even if empty

## "never pool recipes into one reference"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 3)
- 맥락: 성격이 다른 그룹의 데이터를 한 통에 섞어 통계를 내지 말라고 할 때(분석 설계·리뷰)
- 한국어: 여러 레시피를 하나의 기준으로 합치지 마라
- 설명: `pool` 은 동사로 "(돈·자원·데이터를) 한데 모으다"입니다. 통계에서 `pooled variance`(합동 분산)처럼 쓰이는 바로 그 단어라 기술 독자에게 정확합니다. `pool A into B` 꼴로 "A 를 모아 B 하나로 만들다"가 됩니다.
- 예문: Never pool R3 and R4 lots into one baseline; their tools sit in different locations.
- 유사어: lump together (회화, 약간 부정적), merge into a single (중립), aggregate across (문어·통계)
- 반의어: keep them separate, compute per recipe

## "the stated reason there is none"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 1, 요약)
- 맥락: 값이 없을 때 빈칸 대신 "왜 없는지"를 적으라고 요구할 때(보고서·출력 명세)
- 한국어: (값이) 없는 경우엔 그 이유를 밝힌 것
- 설명: 원문은 `per-recipe μ and band (or the stated reason there is none)` 입니다. `the reason (that) there is none` 에서 that 이 빠졌고, `stated` 가 붙어 "코드가 이미 기록해 둔 이유"를 가리킵니다. 실제로 `RecipeCentre` 에 `reason` 필드가 있어서 새 이유를 지어내지 말라는 뜻도 됩니다.
- 예문: For each tool, show the last sync time, or the stated reason there is none.
- 유사어: or why it's missing (회화), or an explanation of its absence (격식), or a note saying why (평이)
- 반의어: left blank without explanation

## "hands over state"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (기존 구현 설명)
- 맥락: 컴포넌트가 로직 없이 데이터를 넘겨주는 역할만 한다고 계층을 설명할 때(코드 리뷰·설계)
- 한국어: 상태를 넘겨주기만 한다
- 설명: 원문은 `the component only hands over state and reports a failed write` 입니다. `hand over` 는 "손에서 손으로 건네다", 곧 책임 없이 전달만 한다는 말입니다. `only` 가 동사 둘을 다 수식해 "이것 말고는 아무것도 안 한다"는 얇은 역할을 못 박습니다.
- 예문: The page only hands over the filters and shows an error if the request fails.
- 유사어: passes along (거의 같음), forwards (기술적), just wires it through (회화)
- 반의어: owns the logic, does the work itself

## "stored nowhere"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 5, 메모)
- 맥락: 입력값이 어디에도 저장되지 않는다고 개인정보·보관 범위를 분명히 할 때(명세·안내 문구)
- 한국어: 어디에도 저장되지 않는다
- 설명: 원문 `the memo is written into the file only and stored nowhere` 는 긍정(`written into the file only`)과 부정(`stored nowhere`)을 짝지어 범위를 양쪽에서 닫습니다. `nowhere` 를 동사 뒤에 두면 `not stored anywhere` 보다 짧고 단호합니다.
- 예문: The token is read from the environment at startup and stored nowhere else.
- 유사어: not saved anywhere (평이), never persisted (기술 문서), kept only in memory (긍정형)
- 반의어: saved server-side, persisted

## "as of the generation time"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Scope 4, 주의 문구)
- 맥락: 데이터가 어느 시점 기준인지 밝혀 나중의 변동에 책임을 지지 않을 때(보고서·면책 문구)
- 한국어: 생성 시점 기준으로
- 설명: `as of + 시점` 은 "~현재, ~기준"입니다. 리포트·재무 문서에서 `as of March 31` 처럼 매우 자주 씁니다. 원문은 `the values are as of the generation time` 으로 be 동사 보어 자리에 놓았습니다. "그 뒤 바뀐 건 반영 안 됐다"는 뜻이 따라옵니다.
- 예문: All counts in this reply are as of 2026-11-05 09:00, before the office reloaded the index.
- 유사어: at the time of generation (거의 같음), current as of (강조), snapshot taken at (데이터 쪽 표현)
- 반의어: live, updated in real time

## "keep it strictly additive"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a59ee0d6 (Constraints)
- 맥락: 공유 코드를 건드려야 한다면 기존 동작은 바꾸지 말고 추가만 하라고 할 때(코드 리뷰·작업 지시)
- 한국어: 순수하게 추가만 하는 변경으로 유지해라
- 설명: `additive` 는 "더하기만 하는"이라는 형용사로, 기존 API 를 지우거나 고치지 않는 변경을 가리킵니다. `strictly` 가 붙어 "조금이라도 기존 걸 바꾸면 안 된다"가 됩니다. 원문은 `If you must change shared export plumbing ..., keep it strictly additive.` 입니다.
- 예문: You can add a new op to the proxy, but keep it strictly additive so older clients still work.
- 유사어: backward-compatible (결과 쪽에 초점), add, don't change (회화), non-breaking (기술)
- 반의어: a breaking change

## "there is a known race when ..."
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96 (State of the code)
- 맥락: 이미 알려진 경합 조건을 다음 작업자에게 경고할 때(인수인계·코드 주석)
- 한국어: ~할 때 경합 문제가 있다는 게 알려져 있다
- 설명: `race` 는 race condition 의 줄임말로 개발자끼리는 명사 하나로 통합니다. 원문은 `there is a known race when two different setters write the URL in the same tick, so one user action = one patch.` 입니다. `in the same tick` 은 "같은 이벤트 루프 틱 안에서", 곧 거의 동시에입니다. 문제와 회피 규칙을 `so` 한 번으로 이었습니다.
- 예문: There is a known race when two jobs write the same progress file, so only finalize is allowed to touch it.
- 유사어: there's a race condition (정식 용어), the two can clobber each other (회화, 결과 묘사), a timing issue (뭉뚱그린 표현)
- 반의어: thread-safe, the writes are serialized

## "so the URL stays clean"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96
- 맥락: 기본값은 URL 에 남기지 않는다는 설계 이유를 한 줄로 댈 때(설계 문서·PR 설명)
- 한국어: URL 이 지저분해지지 않도록
- 설명: 원문은 `default encodes to null so the URL stays clean` 입니다. `stay + 형용사` 는 "그 상태를 유지하다". `clean` 은 불필요한 쿼리 키가 붙지 않은 상태를 말하며, 기본값이면 아무것도 쓰지 않는다는 규칙의 목적을 짧게 밝힙니다.
- 예문: Unset filters aren't written to the query string, so the URL stays clean and easy to share.
- 유사어: stays tidy (회화), avoids clutter in the URL (문어), keeps the query string minimal (기술)
- 반의어: clutters the URL

## "One requested extension beyond the plan, and only this one"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96
- 맥락: 계획에 없던 추가 요구를 딱 하나만 허락하며 범위가 더 번지지 않게 막을 때(작업 지시·요구사항)
- 한국어: 계획을 넘어서는 추가 요청 하나, 그리고 딱 그것 하나만
- 설명: 동사 없는 명사구 뒤에 콜론을 찍어 제목처럼 씁니다. `, and only this one` 을 덧붙여 "다른 확장은 하지 마라"를 반복 없이 전합니다. 앞선 "follow it, do not redesign" 원칙과 충돌하지 않게 예외를 하나로 못 박는 장치입니다.
- 예문: One change beyond the office's request, and only this one: the mock now pairs A to D by lot_cd.
- 유사어: a single exception to the plan (격식), just one extra thing (회화), one addition, nothing more (단호)
- 반의어: open-ended scope, while you're at it

## "shows as no-data, never as zero"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96
- 맥락: 값이 없는 것과 0인 것을 화면에서 구분하라고 요구할 때(시각화·데이터 명세)
- 한국어: 0이 아니라 '데이터 없음'으로 보인다
- 설명: 원문은 `a site present in only one group shows as no-data, never as zero.` 입니다. `show as` 는 "~로 표시되다"라는 자동사 용법입니다. `X, never Y` 는 `X, not Y` 보다 강해 "어떤 경우에도 Y 는 안 된다"가 됩니다. 결측을 0으로 채우면 차이 지도가 거짓말을 하게 되니 핵심 규칙입니다.
- 예문: A lot with no planstep row shows as no-data, never as zero, in the weekly trend.
- 유사어: is left blank rather than zero-filled (기술), displays as N/A (UI 문구), treated as missing (분석 용어)
- 반의어: defaults to zero, is zero-filled

## "diverging and centred on zero"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96
- 맥락: 차이값 시각화의 색 척도를 정할 때(차트 설계·디자인 리뷰)
- 한국어: (색 척도가) 0을 중심으로 양쪽으로 갈라지는
- 설명: `diverging scale` 은 가운데 중립색에서 양 끝으로 서로 다른 색이 짙어지는 척도로, 시각화 분야의 정식 용어입니다(↔ sequential). `centred on` 은 영국식 철자이고 미국식은 `centered on` 입니다. 같은 지시서 안에 `colour`, `centred` 와 코드 쪽 `centered` 가 섞여 있어 두 철자를 비교해 보기 좋습니다.
- 예문: Use a diverging scale centred on zero, so a negative delta and a positive one read as opposite colours.
- 유사어: a two-sided colour scale (평이), a zero-centred palette (명사형), red-blue scale (구체적 회화)
- 반의어: a sequential scale

## "read how far the target moved"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent afc27a96 (S7 Why)
- 맥락: 기준 대비 변화량을 사용자가 읽어 낸다는 기능의 목적을 말할 때(기능 소개·회의)
- 한국어: 대상이 얼마나 움직였는지 읽어 내다
- 설명: 원문은 `S7 lets the engineer split the curated set by hand into a baseline group and a target group and read how far the target moved.` 입니다. `read` 뒤에 의문사절 `how far ... moved` 가 목적어로 왔습니다. 판단은 사람 몫이고 도구는 거리만 보여 준다는 태도가 `read` 라는 동사에 담깁니다.
- 예문: Pin last month's lots as the baseline, and you can read how far this week's lots moved.
- 유사어: see how much X shifted (회화), measure the drift of (기술), quantify the change (격식)
