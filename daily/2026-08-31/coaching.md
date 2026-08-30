# 2026-08-31 — 코칭

## 한글→영어

### 카드 1 — 탭이 두 개 켜지는 버그 신고   (내가 쓴 한글)
- 내가 쓴 한글: "실험실 페이지(/tttm, /pm-planning)에서 상단 FeatureTabs 의 "장비 상태" 가 함께 활성으로 표시됨"   (출처: transcript:[user] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl)
- 자연스러운 영어: "On the lab pages (/tttm, /pm-planning), the top-level FeatureTabs bar lights 장비 상태 as active as well — two tabs are highlighted at once."
- 왜 이렇게: 개조식 "표시됨"을 그대로 수동태(`is displayed`)로 옮기면 누가 그러는지가 사라진다. 화면 요소를 주어로 세워 `the bar lights X` 로 능동으로 쓰면 짧아지고 어디를 고쳐야 하는지까지 드러난다. "~에서"로 시작하는 장소구는 영어에서도 문두에 두고 콤마로 끊는 게 자연스럽다. "함께"는 `as well` 하나로 충분하지만, 버그 신고에서는 대시 뒤에 `two tabs are highlighted at once` 처럼 증상을 한 번 더 못 박아 주면 재현 여부를 바로 확인할 수 있다.

### 카드 2 — gitignore 수정 커밋 제목   (고급 한글 · 번역)
- 한글 원문: "fix(gitignore): fab 데이터 루트 2개가 실제로 무시되게 인라인 주석 분리"   (출처: transcript:[assistant] auto-recipe-creator/a6e1b17a-2c86-4a6b-8a36-47edad1117b3.jsonl)
- 자연스러운 영어: "fix(gitignore): move inline comments to their own lines so the two fab-data roots are actually ignored"
- 번역 포인트: 한국어 커밋 제목은 "인라인 주석 분리"처럼 명사로 끝맺지만, 영어 관례는 명령형 동사로 시작한다(`move`, `split`). "~게" 목적 부사절은 `so (that)` 절로 뒤에 붙이면 순서가 그대로 뒤집힌다 — 한국어는 목적이 앞, 영어는 뒤. "실제로"는 `actually` 로 살려야 한다. 무시되는 줄 알았는데 아니었다는 이 커밋의 요점이 그 한 단어에 들어 있다.

### 카드 3 — 누락 파일 복구 커밋 제목   (고급 한글 · 번역)
- 한글 원문: "합치기 커밋 누락분 5개 파일"   (출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl)
- 자연스러운 영어: "add the five files the merge commit missed"
- 번역 포인트: "누락분"처럼 한자어 명사 하나로 압축된 개념은 영어에서 관계절로 풀어야 자연스럽다 — `the files the merge commit missed`(목적격 관계대명사 that 생략). 한국어는 수식어를 앞에 쌓아 "합치기 커밋 누락분 5개 파일"이 되지만 영어는 핵심 명사를 먼저 놓고 뒤에서 설명한다. 수량 표현도 위치가 다르다: 한국어의 "5개 파일"은 `the five files` 로 관사 뒤에 온다.

### 카드 4 — 화면 안내 문구   (고급 한글 · 번역)
- 한글 원문: "tolerance 는 TTTM 페이지의 설정을 따릅니다"   (출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl, 화면 문구 인용)
- 자연스러운 영어: "Tolerance follows whatever you set on the TTTM page."
- 번역 포인트: "~의 설정을 따릅니다"를 `follows the setting of the TTTM page` 로 직역하면 뻣뻣하다. UI 문구에서는 `whatever you set` 처럼 사용자를 주어로 끌어들이는 관계절이 훨씬 자연스럽고, 어디서 바꾸는지도 함께 알려 준다. 존댓말 종결은 영어에 대응물이 없으니 문장을 짧게 끊는 것으로 대신한다. 참고로 이 문구가 세 군데 반복된다는 사실이 그 세션에서 두 페이지를 합치자는 근거가 됐다 — 안내 문구는 종종 없어져야 할 기능의 흔적이다.

## 영어 다듬기

### 카드 1 — 다른 페이지 UX 이식 요청
- 내가 쓴 영어: "데이터 요청 button in tttm page (the way to 데이터 요청) should be applied to pm-planning to. apply the method (ui/ux) to pm-planning."   (출처: transcript:[user] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl)
- 정정: `in tttm page` → `on the tttm page`(페이지 위는 on, 관사 필요). `to` → `too`("~도"라는 뜻일 때는 o 가 둘. 전치사 to 와 철자가 갈린다). `should be applied to pm-planning` 은 문법은 맞지만 뒤 문장과 같은 말을 두 번 하고 있다.
- 더 나은 표현: "Apply the 데이터 요청 flow from the tttm page — the whole UI/UX, not just the button — to pm-planning as well."
- 왜: `apply A to B` 는 A 를 길게 늘일수록 to B 가 멀어져 읽기 어려워진다. 부연은 대시 사이에 넣고 `to pm-planning` 을 끝에 붙이면 골격이 살아난다. "the way to 데이터 요청"처럼 방식을 가리킬 때는 `the way we do X` 나 `the X flow` 가 관용적이다.

### 카드 2 — 두 페이지 통합 가능성 질문
- 내가 쓴 영어: "Is there way to combine the two pages into a single one?"   (출처: transcript:[user] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl)
- 정정: `Is there way` → `Is there a way`(way 는 가산명사라 관사가 빠질 수 없다).
- 더 나은 표현: "Could these two pages be merged into one?"
- 왜: `combine ... into a single one` 은 single 과 one 이 같은 일을 해서 늘어진다. `merge into one` 이면 충분하다. 또 `Is there a way to...` 는 가능성을 묻는 열린 질문이고 `Could ... be merged?` 는 "해도 되겠나"라는 제안에 가깝다. 실제로 그 답이 설계 권고로 돌아왔으니 후자가 의도에 더 맞았다.

### 카드 3 — 버그 신고
- 내가 쓴 영어: "in pm-planning checked, 장비 상태 is also on in the tab nav. fix the bug"   (출처: transcript:[user] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl)
- 정정: `in pm-planning checked` 는 주어와 동사가 없어 "확인했다"인지 "체크된 상태"인지 갈린다 → `I checked pm-planning and ...`. `is also on` 도 틀리진 않지만 탭에는 `lit`·`highlighted`·`active` 를 쓴다.
- 더 나은 표현: "On /pm-planning, 장비 상태 is highlighted in the tab nav too. Can you fix it?"
- 왜: 버그 신고는 [어디서] → [무엇이] → [무엇을 해 달라] 순서일 때 가장 빨리 읽힌다. `fix the bug` 는 명령형이라 동료 사이에서는 `Can you fix it?` 이나 `Please fix.` 가 무난하다.

### 카드 4 — 오피스 정보 전달
- 내가 쓴 영어: "for the chat service, update the info below to make the conditions met. Here are the info from the office agent."   (출처: transcript:[user] skewnono-v3-nuxt/d3cb6758-cf05-44b1-8363-691e01340651.jsonl)
- 정정: `Here are the info` → `Here's the info`(info 는 불가산이라 복수 취급하지 않는다). `to make the conditions met` → `so it meets the conditions below`(make + 목적어 + 과거분사는 "억지로 그렇게 만들다"로 읽혀 어색하다). `update the info below` 도 아래 정보를 고치라는 뜻이 되어 의도와 반대다.
- 더 나은 표현: "For the chat service, update the code so it satisfies the spec below. Here's what the office agent sent over."
- 왜: 실제 요청은 "아래 정보를 고쳐라"가 아니라 "아래 정보에 맞게 코드를 고쳐라"였다. 기준이 되는 문서는 `the spec below`, 맞추는 동사는 `satisfy`·`meet`·`conform to` 를 쓴다. 남이 준 자료를 옮길 때는 `Here's what X sent over` 가 출처와 전달을 한 번에 밝혀 준다.

### 카드 5 — 문제 없음 확인
- 내가 쓴 영어: "after refresh, I see them all. no issue"   (출처: transcript:[user] skewnono-v3-nuxt/bb345f7a-4139-4130-9e4c-fc2661a1845a.jsonl)
- 정정: `after refresh` → `after a refresh`(한 번의 새로고침이라는 가산 행위).
- 더 나은 표현: "After a refresh they all show up — no issue."
- 왜: `I see them all` 은 지금 보인다는 사실만 전하지만 `they all show up` 은 "나타났다"는 변화까지 담아 새로고침이 해결책이었음을 보여 준다. 마무리 `no issue` 는 그대로 두어도 좋다. 짧게 닫는 게 이 상황에 맞다.

### 카드 6 — 문서 삭제 지시
- 내가 쓴 영어: "remove ponytail audit. that's garbage"   (출처: transcript:[user] auto-recipe-creator/a6e1b17a-2c86-4a6b-8a36-47edad1117b3.jsonl)
- 정정: `remove ponytail audit` → `remove the ponytail audit`(특정 문서를 가리키므로 the 가 필요하다).
- 더 나은 표현: 구어 그대로 — "Drop the ponytail audit, it's junk." / 기록에 남길 문어 — "Remove the ponytail audit; its conclusions don't hold."
- 왜: garbage 는 판정만 있고 근거가 없어 나중에 그 문서를 다시 꺼내는 사람을 막지 못한다. 한 마디라도 이유를 붙이면 삭제가 기록으로 남는다. 참고로 그 세션의 진단은 "importer 가 없다"를 "죽은 코드"로 읽은 것이 오류였다는 것인데, 영어로는 `it treated "no importers" as "dead"` 로 옮긴다.

### 카드 7 — 내일 할 일 메모
- 내가 쓴 영어: "what to do in the office side tomorrow"   (출처: transcript:[user] auto-recipe-creator/a6e1b17a-2c86-4a6b-8a36-47edad1117b3.jsonl)
- 정정: `in the office side` → `on the office side`(A side / B side 처럼 "~쪽"을 가리킬 때는 on 을 쓴다).
- 더 나은 표현: "what to do on the office machine tomorrow"
- 왜: side 는 대비되는 두 쪽이 문맥에 있을 때 쓴다. 여기서는 집 Mac 과 오피스 PC 라는 대비가 이미 서 있으니 `on the office side` 도 성립하지만, 실제로 가리키는 건 그 장비 한 대라 `on the office machine` 이 더 구체적이다.
