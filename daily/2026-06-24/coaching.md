# 2026-06-24 — 코칭

오늘 배치에서 내가 직접 쓴 글은 전부 영어(transcript `[user]`)였습니다. 그래서 한글→영어
카드는 없고, **영어 다듬기**만 다룹니다.

## 영어 다듬기

### 카드 1 — align 실패 시 이미지가 안 보임
- 내가 쓴 영어: "when align fail happens I do not see the images in the align_consensus_cache folder."   (출처: transcript:[user] 052ec064)
- 정정: `align fail` 은 명사 자리에 들어갈 수 없습니다. `fail` 은 동사라 명사가 필요 → `an align failure` (가산명사라 관사 `an` 필수). 절 시작은 대문자로.
- 더 나은 표현: "When an alignment failure occurs, the images don't show up in the `align_consensus_cache` folder."
- 왜: `happen` 보다 `occur` 가 한 단계 격식 있고, `I do not see` 처럼 화자 중심으로 쓰기보다 `the images don't show up`(주어=이미지)으로 **증상 자체를 주어로** 두면 버그 리포트답게 객관적입니다. `show up`(나타나다)은 자연스러운 구동사.

### 카드 2 — 이게 정상인지 확인
- 내가 쓴 영어: "is that normal thing to see?"   (출처: transcript:[user] 052ec064)
- 정정: `normal thing` 앞에 관사 누락 → `a normal thing`. 가산 단수 명사는 관사가 필요합니다.
- 더 나은 표현: "Is that the expected behavior?" (또는 짧게 "Is that normal?")
- 왜: `a normal thing to see` 도 맞지만, 로그·동작이 의도된 것이냐를 물을 때 원어민은 `expected behavior`(예상된 동작)를 더 씁니다. 군더더기 `thing to see` 가 사라져 간결해집니다.

### 카드 3 — 다운로더 테스트 파일 요청
- 내가 쓴 영어: "I want you to make a file to test office_rcp_downloader.py and also office_success_downloader.py by applying recipe_id and eqp_id. can you make one? with prefix temp_?"   (출처: transcript:[user] 052ec064)
- 정정: `by applying recipe_id and eqp_id` 의 `apply` 는 "(규칙·패치를) 적용하다" 뉘앙스라 인자 전달엔 어색 → `using a recipe_id and eqp_id`. 문장 시작 대문자.
- 더 나은 표현: "Could you create a `temp_`-prefixed file that tests `office_rcp_downloader.py` and `office_success_downloader.py` for a given `recipe_id` and `eqp_id`?"
- 왜: 세 조각(만들어줘 / 접두사 temp_ / 인자)을 **한 문장에 통합**하면 요청이 또렷해집니다. `for a given X`(주어진 X에 대해)는 파라미터를 받는다는 뜻을 자연스럽게 전달하고, `Could you …?` 는 명령보다 정중합니다.

### 카드 4 — 경로가 잘못됨
- 내가 쓴 영어: "success fail . they download in debug_images folder without any problem but in consensus_cache folder, the path is wrong."   (출처: transcript:[user] 052ec064)
- 정정: `success fail` 은 조각 문장 → `The success path fails.` 처럼 완전한 절로. `they download`(능동)는 이미지가 스스로 내려받는 꼴이라 어색 → `they're downloaded`(수동) 또는 `they land`.
- 더 나은 표현: "The success path fails. The images download into the `debug_images` folder without any problem, but in the `consensus_cache` folder the path is wrong."
- 왜: `download into`(안으로 받아진다)에서 `into` 가 목적지를 분명히 합니다. 짧은 단정문(`The success path fails.`)을 앞세우고 세부를 잇는 구조가 진단 보고에 적합합니다.

### 카드 5 — 경로에서 eqp_id 제거
- 내가 쓴 영어: "removed the eqp_id out of the path in office_success_downloader now."   (출처: transcript:[user] 052ec064)
- 정정: `out of the path` → `from the path`. "제거하다(remove)"의 출처 전치사는 `from` 입니다(`take X out of` 는 가능하나 `remove X out of` 는 비표준). 주어 `I` 누락.
- 더 나은 표현: "I've removed the `eqp_id` from the path in `office_success_downloader` now."
- 왜: `remove A from B` 가 표준 연어입니다. 방금 끝낸 동작은 현재완료 `I've removed` 로 두면 "그 결과 지금 이렇다"는 함의가 살아 `now` 와도 잘 맞습니다.

### 카드 6 — 저장 지연 시 재시도
- 내가 쓴 영어: "also sometimes, we fail to download img_from_msr as image save is delayed inside the tool itself. In this case, can we try to check one more time after 2 seconds waiting?"   (출처: transcript:[user] 052ec064)
- 정정: `as image save is delayed` → `because the image save is delayed`(여기서 `as` 는 시간/이유가 헷갈림; 명사 `image save` 앞 관사). `after 2 seconds waiting` 어순 오류 → `after waiting 2 seconds`.
- 더 나은 표현: "Sometimes we fail to download `img_from_msr` because the tool itself is slow to save the image. In that case, could we retry once after waiting 2 seconds?"
- 왜: `retry`(재시도하다) 한 단어가 `try to check one more time` 를 대체해 간결합니다. `the tool itself is slow to save` 는 지연의 원인을 능동적으로 짚고, 이유절엔 모호한 `as` 보다 `because` 가 안전합니다.

### 카드 7 — 폴더 구조 변경·리팩터
- 내가 쓴 영어: "I changed the folder structure and refactor the codes in @poc/workflow_3/ check them and update memory and CLUADE.md"   (출처: transcript:[user] 1fc1f209)
- 정정: 시제 일치 `refactor` → `refactored`(앞의 `changed` 와 과거시제 맞춤). `the codes` → `the code`(코드는 보통 불가산). 두 명령을 마침표/접속사로 분리. 오타 `CLUADE.md` → `CLAUDE.md`.
- 더 나은 표현: "I changed the folder structure and refactored the code in `poc/workflow_3/`. Check it and update memory and `CLAUDE.md`."
- 왜: `code` 는 불가산이라 복수 `codes` 는 "암호문"으로 오해될 수 있습니다. 한 문장에 동작 보고와 지시를 섞지 말고 **마침표로 끊어** 지시를 분리하면 읽는 쪽이 할 일을 놓치지 않습니다.
