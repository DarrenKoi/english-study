# 2026-08-08 — 새 표현

## "coincide by construction"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (device-statistics 정렬 검증)
- 맥락: 두 결과가 우연히 같은 게 아니라 데이터를 만든 방식 때문에 필연적으로 같을 때. 설계 메모·디버깅 보고(격식).
- 한국어: 만들어진 구조상 어쩔 수 없이 일치한다
- 설명: `by construction` 은 수학에서 온 어투로 "구성 방식 자체에서 따라 나온다"는 뜻. 여기 붙으면 "우연의 일치가 아니라 애초에 그렇게 만들어서 같다"가 되어, 그 자리에서 하는 검증이 왜 무의미한지를 한 마디로 끝낸다.
- 예문: The mock builds `recipe_id` from the same index it uses for `oper_seq`, so the two orderings coincide by construction and a browser check proves nothing.
- 유사어: follow trivially (논증에서 더 격식), be the same by definition (정의상 같다는 더 강한 주장), fall out of the way it's generated (평이한 회화체)
- 반의어: agree by coincidence

## "axis furniture"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md
- 맥락: 차트에서 데이터가 아닌 부속(축선·눈금·라벨)을 한 단어로 묶어 부를 때. 코드 주석·설계 문서.
- 한국어: 축 부속물, 축 장식
- 설명: `furniture` 를 "본체가 아니라 주변에 놓인 것들"이라는 비유로 쓴다. UI 쪽 `chrome`(브라우저 테두리·툴바)도 같은 계열이라, 둘 다 "지울 수 있는 주변부"라는 판단을 이름에 이미 담고 있다.
- 예문: No axis furniture here: the host is 64px tall, so every pixel belongs to the bars.
- 유사어: chart chrome (UI 테두리 쪽에 더 자주), axis decorations (평이하지만 덜 관용적)
- 반의어: the data ink

## "violate the letter of X / the spirit of X"
- 레지스터: professional
- 출처: transcript:[user] systematic-debugging 스킬 문서
- 맥락: 규칙을 형식만 지키고 취지를 어겼다고 지적할 때. 규범·정책 문서(격식).
- 한국어: 조문(문자)을 어기다 / 취지를 어기다
- 설명: 법률 관용구 `the letter of the law` ↔ `the spirit of the law` 에서 왔다. 원문은 순서를 뒤집어 "형식을 어기는 것이 곧 취지를 어기는 것"이라고 못 박아, "절차는 건너뛰었지만 정신은 지켰다"는 흔한 변명을 미리 막는다.
- 예문: Violating the letter of this process is violating the spirit of debugging.
- 유사어: pay lip service to (말로만 따르다; 비판 어조가 더 셈), tick the box (회화체, 형식만 채우다)
- 반의어: honour the intent

## "X doesn't stick"
- 레지스터: conversational, professional
- 출처: transcript:[user] systematic-debugging 스킬 문서
- 맥락: 조치가 오래 못 가고 되돌아온다고 짧게 못 박을 때. 회의 발언·리뷰 코멘트.
- 한국어: 붙어 있지 않는다, 오래 못 간다
- 설명: `stick` 은 "달라붙어 남다". 회귀를 예언하는 말이라 근거를 길게 붙이지 않아도 경고로 읽힌다. 주어를 사람이 아니라 조치로 두는 게 핵심이다.
- 예문: Untested fixes don't stick — the next refactor quietly puts the bug back.
- 유사어: regress (격식·중립), come undone (회화, 서서히 풀린다는 뉘앙스), not hold (더 담백)
- 반의어: hold up

## "there's no room for X"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (mother_para 조사)
- 맥락: 스키마·자료구조에 값을 담을 자리가 아예 없다고 말할 때. 물리적 공간이 아니라 표현력 부족을 가리킨다.
- 한국어: ~를 담을 자리가 없다
- 설명: 데이터 스키마에 쓰면 "필드가 없어서 표현 자체가 불가능하다"가 되어, 값이 비어 있는 상태와 명확히 갈린다. 원인이 우리 코드가 아니라 상류 계약에 있다는 신호이기도 하다.
- 예문: `cdsem_idp_ver.parameters` is `{name: point_count}` — there's no room for a `Mother_Para` flag.
- 유사어: the schema can't express it (더 명시적·격식), there's nowhere to put it (회화체)
- 반의어: the field is there, just empty

## "hunt it (down)"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 아직 위치를 모르는 원인을 끝까지 추적하겠다고 약속할 때. 짧은 상태 보고의 끝맺음.
- 한국어: 끝까지 쫓아 잡겠다
- 설명: `fix it` 이 결과를 약속한다면 `hunt it` 은 찾는 과정을 약속한다. 어디 있는지 모를 때 이쪽이 정직하고, 조건절 뒤에 붙이면 "이 경우엔 내가 맡는다"는 분담 선언이 된다.
- 예문: R3 fine, M zero → that's a real join bug and I'll hunt it.
- 유사어: track it down (거의 동의, 조금 더 중립), chase it (덜 집요한 어감)
- 반의어: let it lie

## "whichever way that goes"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 아직 결론 안 난 조사와 무관하게 따로 할 일이 있다고 분리할 때.
- 한국어: 그게 어느 쪽으로 결론 나든
- 설명: 두 갈래 조건절을 다 쓰지 않고 한 번에 접는다. 미해결 항목 옆에 확정 항목을 나란히 놓을 때 특히 유용해서, 보고가 "기다려야 함"으로만 끝나지 않게 해준다.
- 예문: Separately, there's a defect I can fix from home whichever way that goes.
- 유사어: either way (더 짧고 캐주얼), regardless of the outcome (격식·문어)
- 반의어: depending on which way it goes

## "aim the fix"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 정보가 모자라 수정을 어디에 넣을지 못 정했다고 상대에게 관측을 요청할 때.
- 한국어: 수정을 어디에 겨눌지 정하다
- 설명: `aim` 이 들어가면 "고칠 능력은 있는데 표적이 없다"가 되어, 못 하겠다는 보고가 아니라 협조 요청으로 읽힌다. 상대가 무엇을 주면 되는지도 함께 지정된다.
- 예문: I can't reproduce it here, so I need your observation to aim the fix.
- 유사어: narrow it down (범위 좁히기 쪽), know where to cut (회화, 비유적)
- 반의어: fix blind

## "all green"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: CI·테스트·린트가 모두 통과했다고 한마디로 보고할 때. 팀 채팅·커밋 코멘트.
- 한국어: 전부 초록불, 다 통과
- 설명: 대시보드 색에서 온 관용구. 뒤에 대시를 찍고 숫자를 붙이는 게 관용적 리듬이다. 격식 있는 문서에는 `all checks pass` 를 쓴다.
- 예문: All green — 1,227 tests, typecheck and lint clean.
- 유사어: all checks pass (격식), green across the board (강조), clean (린트·타입에 한정)
- 반의어: red / failing

## "pass X through (unchanged)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md
- 맥락: 처리할 수 없는 입력을 변환하지 않고 그대로 내보내는 동작을 계약으로 적을 때.
- 한국어: 손대지 않고 그대로 흘려보내다
- 설명: 실패 처리 방식을 한 단어로 요약한다. 예외를 던지지도, 기본값으로 바꾸지도 않는다는 약속이라 호출자가 무엇을 보게 될지 예측할 수 있다.
- 예문: The formatter passes an unparseable date through instead of throwing.
- 유사어: return it as-is (평이), fall through to the raw value (구현 관점)
- 반의어: coerce it / substitute a default

## "survive X"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md
- 맥락: 빈 입력·경계값에서 죽지 않는지만 확인하는 테스트의 이름.
- 한국어: ~에서도 살아남다, 터지지 않다
- 설명: `handle` 보다 기대치를 일부러 낮춘 말이다 — "잘 처리한다"가 아니라 "터지지 않는다". 테스트 이름에 쓰면 그 테스트가 무엇을 보증하지 *않는지*까지 전달된다.
- 예문: The builder survives an empty series and returns an empty `data` array.
- 유사어: handle gracefully (기대치가 더 높음), not blow up on (회화체)
- 반의어: choke on

## "the X it was handed"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md
- 맥락: 함수가 값을 스스로 정하지 않고 받은 것을 그대로 쓴다는 설계를 강조할 때.
- 한국어: 넘겨받은 바로 그 값
- 설명: 수동태 `was handed` 가 "이 함수에는 결정권이 없다"를 드러낸다. 색을 누가 정하는지가 이 리팩터링의 요점이라, 테스트 이름 한 줄이 책임 소재까지 문서화하는 셈이다.
- 예문: It paints the bars with the colour it was handed, never one of its own.
- 유사어: whatever it's given (더 캐주얼), the caller-supplied value (격식·문어)
- 반의어: a colour of its own choosing

## "can spare it"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-activity-sparkline-echarts.md
- 맥락: 공간·시간·예산을 내줄 여유가 어느 쪽에 있는지 비교할 때.
- 한국어: 그만큼 내줄 여유가 있다
- 설명: `spare` 는 "빼줘도 괜찮다". 목적어가 픽셀이면 레이아웃 얘기, 시간이면 일정 얘기가 된다. 같은 기능을 한 곳에만 켜는 이유를 설명할 때 딱 맞는다.
- 예문: The slider needs 20px and only the standalone card can spare it.
- 유사어: has the headroom for it (수치 여유 강조), can afford it (비용 비유)
- 반의어: can't give up the space

## "question the fundamentals"
- 레지스터: professional
- 출처: transcript:[user] systematic-debugging 스킬 문서
- 맥락: 개별 수정을 멈추고 전제를 다시 봐야 할 때를 선언하는 말. 설계 회의(격식).
- 한국어: 전제를 다시 묻다
- 설명: 여기서 `question` 은 "의심하고 따져 묻다"라는 타동사. `doubt` 이 감정을 가리키는 것과 달리 이쪽은 절차를 가리켜서, 남의 설계를 문제 삼을 때도 인신공격으로 들리지 않는다.
- 예문: Three failed fixes is the signal to stop patching and question the fundamentals.
- 유사어: revisit the premise (더 부드러움), go back to first principles (더 야심찬 어감)
- 반의어: keep patching

## "one variable at a time"
- 레지스터: professional, conversational
- 출처: transcript:[user] systematic-debugging 스킬 문서
- 맥락: 여러 수정을 한꺼번에 넣지 말라고 할 때. 디버깅·리뷰 지침.
- 한국어: 한 번에 하나씩만 바꿔라
- 설명: 실험 설계 용어가 그대로 개발 규범으로 넘어왔다. 이유(원인 분리)가 표현 안에 이미 들어 있어서 뒤에 설명을 덧붙일 필요가 없다.
- 예문: Make the smallest possible change to test the hypothesis — one variable at a time.
- 유사어: change one thing and re-run (평이·구어), isolate the change (격식)
- 반의어: bundle the fixes

## "make guessing tempting"
- 레지스터: conversational, professional
- 출처: transcript:[user] systematic-debugging 스킬 문서
- 맥락: 규율이 무너지는 상황을 사람 탓 없이 설명할 때.
- 한국어: (상황이) 찍고 싶게 만든다
- 설명: `make + 동명사 + 형용사` 구조가 유혹의 주체를 사람에서 상황으로 옮긴다. "너는 성급하다"가 아니라 "그 상황이면 누구나"가 되어 지적이 훨씬 덜 아프게 꽂힌다.
- 예문: Use it especially under time pressure — emergencies make guessing tempting.
- 유사어: invite shortcuts (격식·문어), is where people start cutting corners (회화체)
- 반의어: forces you to slow down

## "it's the only place X is observable"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt
- 맥락: 실환경에서는 차이를 볼 수 없어 단위 테스트가 유일한 관측 지점이라고 말할 때.
- 한국어: 차이가 드러나는 유일한 자리
- 설명: `observable` 이 물리 실험 어투를 끌고 와서, "테스트가 있으면 좋다"는 권고를 "여기 말고는 볼 방법이 없다"는 필연으로 바꾼다. 테스트를 왜 그 층에 뒀는지 변호할 때 강하다.
- 예문: I pulled the comparators into a unit test — it's the only place the difference is observable until this hits real recipe names.
- 유사어: the only place it shows up (평이), the sole point of visibility (지나치게 격식)
- 반의어: visible anywhere you look
