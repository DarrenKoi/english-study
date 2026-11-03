# 2026-11-04 — 코칭

## 한글→영어

### 카드 1 — 안 되는 이유 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "@reverse_engineering/reading.html 에서 ELF, Mach-O가 윈도우즈에서 안되는 이유는?"   (출처: transcript:[user] pm_notes 65f7b337)
- 자연스러운 영어: In reverse_engineering/reading.html, why don't ELF and Mach-O work on Windows?
- 왜 이렇게: "~에서 안 되는 이유는?"처럼 명사로 끝난 질문은 영어에서 `Why don't X work on Y?` 로 동사 질문을 만드는 편이 자연스럽습니다. `What is the reason that ...` 은 길고 딱딱합니다. 파일 위치는 `In ...` 으로 앞에 빼서 질문 본체를 짧게 둡니다. "안 되다"는 맥락상 `aren't supported` 도 됩니다.

### 카드 2 — 고치고 다시 올려 줘   (내가 쓴 한글)
- 내가 쓴 한글: "응 두 곳 고치고 재게시해줘"   (출처: transcript:[user] pm_notes 65f7b337)
- 자연스러운 영어: Yes, fix both of those and republish it.
- 왜 이렇게: "두 곳"을 `two places` 로 직역하면 어디인지 다시 묻게 됩니다. 상대가 방금 말한 두 군데이니 `both of those` 가 맞습니다. "재게시"는 `republish` 또는 `publish it again`. 회화라면 `Go ahead and fix both, then republish.` 처럼 `go ahead and` 로 허락의 느낌을 더해도 좋습니다.

### 카드 3 — 커밋하고 푸시   (내가 쓴 한글)
- 내가 쓴 한글: "커밋, 푸시"   (출처: transcript:[user] pm_notes 65f7b337)
- 자연스러운 영어: Commit and push.
- 왜 이렇게: 한국어는 쉼표로 명사 둘을 나열해도 지시가 되지만 영어는 동사 둘을 `and` 로 이어야 명령문이 됩니다. 조금 부드럽게는 `Go ahead and commit and push.`, 확인을 겸하면 `Yes, commit and push.`

### 카드 4 — 왜 이게 들어가 있지? 여긴 X 만   (내가 쓴 한글)
- 내가 쓴 한글: "reverse_engineering에서 bento 관련 내용이 왜 @reverse_engineering/reading.html 에 포함되어 있지? 여기에는 RE에 대해서만 적혀있어야 함"   (출처: transcript:[user] pm_notes 65f7b337)
- 자연스러운 영어: Why is the Bento material showing up in reverse_engineering/reading.html? That page should only cover RE.
- 왜 이렇게: "포함되어 있지?"를 `is included` 로 옮겨도 틀리진 않지만 의아함을 담으려면 `showing up` 이 낫습니다(있으면 안 될 게 보인다는 느낌). "~에 대해서만 적혀 있어야 함"은 `should only cover X` 로 짧게 끝납니다. 무생물 주어 `That page` 를 세우면 "적혀 있다"의 수동 표현을 피할 수 있습니다.

### 카드 5 — 이미 끝난 것 지우기   (내가 쓴 한글)
- 내가 쓴 한글: "@docs/office-migration/ 이미 office agent와 협업해서 구현 완료된 내용들 제거."   (출처: transcript:[user] skewnono_v3_nuxt 0028e27e)
- 자연스러운 영어: In docs/office-migration/, remove everything we've already finished implementing with the office agent.
- 왜 이렇게: "구현 완료된 내용들"은 `the contents that were completed` 로 직역하기 쉽지만 `everything we've already finished implementing` 처럼 사람을 주어로 돌리면 훨씬 자연스럽습니다. `finish + -ing` 형태를 기억해 두세요. "협업해서"는 굳이 `in collaboration with` 까지 갈 필요 없이 `with the office agent` 로 충분합니다. 명사형으로 끝난 메모체 "제거."는 영어에서 명령문 `remove` 로 시작합니다.

### 카드 6 — 잘 보고 있고 문제없음   (내가 쓴 한글)
- 내가 쓴 한글: "AFM 팁 모니터링 사무실에서 잘 보고 있고 현재까지 문제 없음"   (출처: transcript:[user] skewnono_v3_nuxt 0028e27e)
- 자연스러운 영어: We've been using AFM tip monitoring at the office, and it's working fine so far — no issues.
- 왜 이렇게: "잘 보고 있다"는 계속되는 일이라 현재완료진행 `We've been using` 이 맞습니다. 주어를 기능으로 돌려 `AFM tip monitoring has been running fine at the office` 로 써도 됩니다. "현재까지"는 `so far` 가 가장 흔하고, "문제없음"은 `no issues` 나 `no problems` 를 끝에 붙이면 보고 말투가 됩니다.

### 카드 7 — 원인을 바로잡아 말하기   (고급 한글 · 번역)
- 한글 원문: "Windows가 ELF나 Mach-O를 못 읽어서 생기는 제약이 아닙니다. REA의 Windows용 Ghidra 연동이 받는 형식을 PE와 raw 6502 이미지로 제한해 두었기 때문입니다."   (출처: transcript:[assistant] pm_notes 65f7b337)
- 자연스러운 영어: It isn't that Windows can't read ELF or Mach-O. REA's Windows Ghidra integration only accepts PE and raw 6502 images.
- 번역 포인트: "~해서 생기는 제약이 아닙니다"는 `It isn't that ...` 이라는 정형구로 상대의 짐작을 부드럽게 부정합니다. "~하기 때문입니다"를 `This is because ...` 로 옮기면 무겁습니다. 둘째 문장에서 사실만 말하면 이유라는 게 저절로 드러납니다. "제한해 두었다"는 `only accepts` 로 바꿔 행위자 없이 상태로 적었습니다.

### 카드 8 — 표현이 오해를 부른다   (고급 한글 · 번역)
- 한글 원문: "`rea-windows-pi-setup.md:28`의 "Windows는"이라는 표현은 운영체제의 한계처럼 읽힙니다."   (출처: transcript:[assistant] pm_notes 65f7b337)
- 자연스러운 영어: The phrase "Windows only accepts" in rea-windows-pi-setup.md:28 reads like a limitation of the OS itself.
- 번역 포인트: "~처럼 읽힌다"는 `reads like` 로 바로 옮겨집니다. 영어에서도 read 를 자동사로 써서 "글이 ~하게 읽힌다"를 말합니다(The sentence reads awkwardly). `is read as` 로 수동형을 만들 필요가 없습니다. "운영체제의 한계"에 `itself` 를 붙이면 "REA 가 아니라 OS 탓"이라는 대비가 살아납니다.

### 카드 9 — 오래 묵은 항목 정리 제안   (고급 한글 · 번역)
- 한글 원문: "진행 중의 07-21 recipe_tat 검증, 07-29 Recipe-open 설정 리더, 08-09 FTP 측정 스크립트는 석 달 가까이 그대로입니다. 아직 필요한지, 지울지 정해 주시면 다음 /leave-office 때 정리하겠습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 0028e27e)
- 자연스러운 영어: Three in-progress items — the recipe_tat check (07-21), the Recipe-open config reader (07-29), and the FTP measurement script (08-09) — haven't moved in nearly three months. Let me know whether you still need them or want them dropped, and I'll tidy them up at the next /leave-office.
- 번역 포인트: "그대로입니다"는 `are unchanged` 보다 `haven't moved` 가 "진척이 없다"는 뜻을 생생하게 줍니다. "정해 주시면 ~하겠습니다"는 조건문 `If you decide, I'll ...` 대신 `Let me know ..., and I'll ...` 로 요청 + 약속을 이어 붙이는 게 업무 영어의 정형입니다. "지울지"는 `drop` 이 할 일 목록에 잘 맞습니다.

### 카드 10 — 확인만으로는 확정할 수 없다   (고급 한글 · 번역)
- 한글 원문: "둘 다 mock이 지어낸 값이라 "화면이 잘 보인다"는 확인만으로는 확정할 수 없습니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 0028e27e)
- 자연스러운 영어: Both values were made up by the mock, so "the screen looks fine" isn't enough to confirm them.
- 번역 포인트: "지어낸 값"은 `made up` (회화)이나 `fabricated` (문어; 부정적 뉘앙스가 있어 주의). "~만으로는 확정할 수 없다"는 `X isn't enough to confirm Y` 로 X 를 주어로 세우면 한국어의 "~만으로는"이 깔끔하게 옮겨집니다. 따옴표 속 확인 문구를 그대로 주어로 쓰는 것도 영어에서 자연스럽습니다.

## 영어 다듬기

### 카드 1 — End Time 이 없는 경우   (사무실 회신)
- 내가 쓴 영어: "1. no End Time at all for some cases for MAP608. In that case, we do not analyze. (note that the End Time is mssing in the front-end)"   (출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 12차 회신, 사용자가 직접 쓴 답 — 문서에 원문 보존)
- 정정: `mssing` → `missing` (오타). 첫 줄은 주어·동사가 없는 조각이라 문장 첫 글자도 소문자입니다. 메모라면 괜찮지만 문장으로 쓰려면 `There is no End Time at all for some MAP608 measurements.` 처럼 주어를 세웁니다. `for some cases for MAP608` 은 for 가 겹쳐 어색합니다. `analyze` 는 타동사라 목적어가 있어야 합니다(`we do not analyze them`). `front-end` 는 명사로 쓸 때 보통 `front end`(형용사로 쓸 때만 하이픈).
- 더 나은 표현: Some MAP608 measurements have no End Time at all. We'll skip the duration analysis for those and show on the front end that the End Time is missing.
- 왜: 원문의 `note that ...` 은 "참고로 ~이다"로 읽혀 화면에 표시하라는 지시가 흐려집니다. 실제 뜻은 "화면에 밝혀라"였으니 `show on the front end that ...` 으로 동사를 분명히 했습니다. 시제는 앞으로의 방침이라 `We'll` 이 자연스럽습니다.

### 카드 2 — MAPC01 도 건너뛰기   (사무실 회신)
- 내가 쓴 영어: "MAPC01 -> skip analysis too"   (출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 12차 회신, 사용자 작성)
- 더 나은 표현: Skip the analysis for MAPC01 as well.
- 왜: 화살표 메모는 동료끼리는 통하지만 문장으로 쓰면 `the analysis` 처럼 관사를 붙여 "그 소요시간 분석"을 가리키는 편이 정확합니다. 문장 끝의 too 는 회화체이고, 글에서는 `as well` 이 조금 더 단정합니다.

### 카드 3 — 장비 설정에 달린 일, 지금은 있는 것만   (사무실 회신)
- 내가 쓴 영어: "Since this result data is based on the setting in the afm tool. I think the engineers will work on it if it is worth of doing that. We just prepare for that case and focuse on the currently available tools."   (출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 12차 회신, 사용자 작성)
- 정정: ① `Since this result data is based on ...` 는 종속절만 있는 미완성 문장입니다. 다음 문장과 쉼표로 이어야 합니다(`Since ..., I think ...`). ② `worth of doing` → `worth doing`. worth 는 바로 동명사·명사를 받습니다(worth the effort, worth trying). ③ `focuse` → `focus` (오타). ④ `the setting` → `the settings`, `afm` → `AFM`. ⑤ `We just prepare` 는 습관을 말하는 현재형이라 앞으로의 방침이면 `We'll just prepare` 가 맞습니다.
- 더 나은 표현: Whether this data gets recorded depends on how each AFM tool is configured, so I expect the engineers will change the settings if the analysis turns out to be worth it. For now, let's just handle that case and focus on the tools that already have the data.
- 왜: `be based on the setting` 보다 `depends on how ... is configured` 가 "설정에 따라 기록 여부가 갈린다"는 뜻을 정확히 줍니다. `I think ... will` 은 `I expect ... will` 로 바꾸면 추측의 근거가 있다는 느낌이 납니다. `currently available tools` 는 "지금 쓸 수 있는 장비"로 읽혀 뜻이 흐려지므로 `tools that already have the data` 로 풀었습니다.

### 카드 4 — 원본 데이터에서 확인한 것   (사무실 회신)
- 내가 쓴 영어: "What we can give Home (you) now is confirmed from raw data in skewnono-pjt-shared/AFM/"   (출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 1차 회신, 사용자 작성)
- 정정: `confirmed from raw data` → `confirmed against the raw data` (특정 폴더의 데이터라 the 가 필요하고, 대조해서 확인했다는 뜻이면 `against` 가 정확합니다).
- 더 나은 표현: Here's what we can give Home (you) for now — all of it confirmed against the raw data in skewnono-pjt-shared/AFM/.
- 왜: 긴 명사절 주어 `What we can give ...` 로 시작하면 문장 머리가 무겁습니다. `Here's what ...` 으로 열고 확인 범위는 대시 뒤로 빼면 보고 첫 줄로 가볍게 읽힙니다.

### 카드 5 — 장비 ID 와 매핑   (사무실 회신)
- 내가 쓴 영어: "D1: Equipemnt IDs are MAP608, MAPC01, 5EAP1501. Code confirms MAPC01=R3, 5EAP1501=M15, the current mocks' mapping is wrong. Fab field doesn't exist anywhere in the raw data (미정)."   (출처: repo:skewnono_v3_nuxt docs/afm/office-data-findings.md 1차 회신, 사용자 작성)
- 정정: `Equipemnt` → `Equipment` (오타). 둘째 문장은 독립절 두 개를 쉼표로만 이은 comma splice 입니다. 세미콜론이나 `so` 로 이어야 합니다. `Fab field` → `The Fab field` (특정 필드라 관사).
- 더 나은 표현: D1: The tool IDs are MAP608, MAPC01, and 5EAP1501. The code confirms MAPC01 = R3 and 5EAP1501 = M15, so the mapping in the current mocks is wrong. The Fab field doesn't appear anywhere in the raw data (TBD).
- 왜: 반도체 현장에서는 equipment 보다 `tool` 이 더 흔하게 쓰입니다. 셋 이상 나열할 때 마지막 앞에 `and` 를 넣어야 목록이 닫힙니다. `the current mocks' mapping` 처럼 복수 소유격을 앞에 두면 읽기가 걸려서 `the mapping in the current mocks` 로 풀었습니다. "미정"은 `TBD`(to be determined)가 영어 문서의 정형입니다.
