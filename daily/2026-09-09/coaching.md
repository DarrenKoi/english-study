# 2026-09-09 — 코칭

## 한글→영어

### 카드 1 — 파일을 건드리지 않는 리뷰 지시   (내가 쓴 한글)
- 내가 쓴 한글: "docs/architecture/equipment-data-map.md 전체를 처음부터 끝까지 읽고 독립적으로 전체 리뷰해 주세요. 파일을 수정하지 마세요."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: Read `docs/architecture/equipment-data-map.md` end to end and review it independently. Do not edit any file.
- 왜 이렇게: "처음부터 끝까지"를 `from the beginning to the end` 로 옮기면 길고 어색하다. 영어는 `end to end` 라는 굳은 짝을 쓴다(관사 없이). "독립적으로"는 `independently` 한 단어면 되는데, 뒤에 놓아야 "누구 의견에도 기대지 말고"라는 뜻이 산다 — `independently review` 처럼 앞에 붙이면 "따로따로 검토하라"로도 읽힌다. 마지막 문장은 짧게 끊는 게 낫다. 금지 조항을 앞 문장에 `without editing` 으로 붙이면 부수 조건처럼 보이고, 떼어 놓아야 규칙으로 읽힌다.

### 카드 2 — 두 개의 "단계"를 분리하기   (내가 쓴 한글)
- 내가 쓴 한글: "현재 의도는 §3의 6개 런타임 파이프라인과 §8의 5개 rollout/운영자 승인 단계를 분리하고, 통합 스킬 1개와 단계별 스킬 5개는 로직 없이 단일 equipment-map CLI의 고정 subcommand만 호출하는 것입니다."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: The current intent is to keep §3's six runtime pipeline stages separate from §8's five rollout and operator-approval stages, and to have the one umbrella skill and the five per-stage skills carry no logic at all — each calls only fixed subcommands of a single `equipment-map` CLI.
- 왜 이렇게: "A와 B를 분리하다"를 `separate A and B` 로 쓰면 "둘을 갈라 놓다"까지만 간다. 여기서 말하려는 건 **섞이지 않게 유지하는 것**이라 `keep A separate from B` 가 정확하다. "로직 없이 ~만 호출한다"는 한국어에서 부사구 하나지만 영어로는 부정(`carry no logic`)과 한정(`only fixed subcommands`)이 다른 층위라, 대시로 끊어 두 주장으로 나누는 편이 읽힌다. 한 문장에 밀어 넣으면 `no` 와 `only` 가 서로 간섭한다.

### 카드 3 — 검증 → 확산 → 인수인계   (내가 쓴 한글)
- 내가 쓴 한글: "초기에는 한 PC에서 검증하고 이후 각 운영자 PC에서 수행하며 rollout 작업 디렉터리를 승인된 회사 내부 저장소로 인수인계합니다."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: We validate on one PC first, then run it on each operator's PC, handing the rollout working directory over to an approved internal company repository.
- 왜 이렇게: "인수인계"는 영어에 딱 맞는 명사가 없다. `handover` 가 있긴 하지만 동사로 풀어 `hand X over to Y` 로 쓰는 쪽이 훨씬 자연스럽다. 세 동작을 "-고 -하며"로 이은 한국어를 영어에서 `and` 세 번으로 옮기면 평면적이라, **앞 둘은 `first … then` 으로 시간 순서를 세우고 마지막은 분사구문(`handing`)으로 낮춰** 주된 흐름과 부수 동작을 구분한다. "승인된 회사 내부 저장소"는 형용사가 셋 겹쳐 무거우니 영어 어순 관행을 지킨다 — 판단(approved) → 위치(internal) → 소속(company).

### 카드 4 — 출력 형식을 못 박기   (내가 쓴 한글)
- 내가 쓴 한글: "결과는 actionable finding만 `파일:라인 | severity | 한 문장 설명` 형식으로 쓰고, 필요하면 바로 아래 최소 수정안을 덧붙이세요."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: Report actionable findings only, one per line as `file:line | severity | one-sentence description`, and where it helps, add the minimal fix directly underneath.
- 왜 이렇게: "~만"을 `only actionable findings` 로 앞에 두면 "다른 것 말고 이것"이라는 대조가 되고, `actionable findings only` 로 뒤에 두면 **필터 조건**이 된다. 지시문에서는 후자가 맞다. "필요하면"은 `if necessary` 가 기본이지만 여기서는 상대에게 판단을 맡기는 자리라 `where it helps` 가 부드럽고 더 자연스럽다. "바로 아래"는 `right below` 도 되지만 문서 레이아웃을 말할 때는 `directly underneath` 가 관용에 가깝다.

### 카드 5 — 마지막 줄을 지정하기   (내가 쓴 한글)
- 내가 쓴 한글: "마지막 줄은 정확히 APPROVE 또는 REQUEST-CHANGES로 끝내 주세요."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: End with a final line that reads exactly `APPROVE` or `REQUEST-CHANGES`, and nothing else.
- 왜 이렇게: `End the last line with X` 라고 쓰면 "마지막 줄의 *끝부분*이 X"가 되어, 앞에 다른 말이 붙어도 규칙을 지킨 셈이 된다. 실제 의도는 그 줄이 X 하나뿐이라는 것이므로 `a final line that reads exactly X` 로 내용을 지정하고 `and nothing else` 로 잠근다. 지시문에서 모호함이 새는 자리는 대개 이런 전치사 하나다.

### 카드 6 — 재분석 없이 다시 출력   (내가 쓴 한글)
- 내가 쓴 한글: "방금 완료한 재리뷰의 finding 전체를 재분석 없이 다시 출력해 주세요. 누락 없이 번호를 붙이고 각 항목을 한 줄로 압축하세요."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: Print the full set of findings from the re-review you just finished, without re-analyzing anything. Number them all, leaving none out, and compress each to a single line.
- 왜 이렇게: "재분석 없이"를 `without reanalysis` 로 명사화하면 딱딱하고, 무엇을 재분석하지 말라는 건지 흐려진다. `without re-analyzing anything` 처럼 동명사에 목적어를 붙이면 범위가 분명해진다. "누락 없이"는 대응 부사가 없어서 `leaving none out` 이라는 분사구로 푼다 — `without omission` 은 법률투다. `compress X to Y` 에서 전치사는 `into` 가 아니라 `to` 다. 도달한 결과를 가리키기 때문이다.

### 카드 7 — 비협상 조건 선언   (내가 쓴 한글)
- 내가 쓴 한글: "다음 사용자 요구는 비협상 조건입니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: The following requirement is non-negotiable.
- 왜 이렇게: 짧아서 오히려 배울 게 있다. "사용자 요구"를 그대로 `the user's requirement` 로 옮기면 내가 나를 3인칭으로 부르는 어색함이 생긴다. 내가 곧 사용자이므로 소유격을 통째로 버리는 게 맞다. `non-negotiable` 은 하이픈이 필수이고 조건에만 붙는다 — 사람에게 쓰면 무례하게 들린다. 앞 리뷰가 전제를 잘못 읽었을 때 한 줄로 다시 세우는 문장이다.

### 카드 8 — 반복되는 축임을 정정하기   (내가 쓴 한글)
- 내가 쓴 한글: "이 5단계는 조직 전체에서 한 번 쓰고 폐기되는 것이 아니라 장비/현장/버전별 rollout마다 반복됩니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: These five stages are not run once org-wide and then retired — they repeat for every rollout, per tool, per site, and per version.
- 왜 이렇게: "한 번 쓰고 폐기되다"를 `used once and discarded` 로 옮겨도 되지만, 스킬이나 프로세스에는 `retired` 가 관용이다. `discard` 는 물건을 내다 버리는 그림이라 결이 다르다. "장비/현장/버전별"의 슬래시는 영어에서 그대로 두면 읽히지 않는다. `per X, per Y, per Z` 로 풀어 반복 축을 셋 다 세우면 원문의 정보가 살고, 이 문장의 요지가 바로 "축이 여럿"이라는 점이라 풀어 쓸 값어치가 있다.

### 카드 9 — 별도 축임을 밝히기   (내가 쓴 한글)
- 내가 쓴 한글: "§3의 6개 런타임 처리 단계와는 별도 축입니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: This is a separate axis from §3's six runtime processing stages.
- 왜 이렇게: `axis` 는 수학·데이터에서 온 말이지만 영어 설계 논의에서 "서로 독립적인 분류 기준"이라는 뜻으로 그대로 쓴다. 놓치기 쉬운 건 전치사다 — `different from`, `separate from` 이지 `separate with` 가 아니다. 한국어 "~와는"의 "와" 때문에 `with` 로 끌리는 게 전형적인 간섭이다.

### 카드 10 — 조건은 유지한 채 최소안 요청   (내가 쓴 한글)
- 내가 쓴 한글: "이 조건을 유지하면서 1차 지적을 반영한 최소 구조를 제안해 주세요."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: Keeping that constraint, propose the smallest structure that still addresses your first-round findings.
- 왜 이렇게: "지적을 반영하다"에 `reflect` 를 쓰면 안 된다. `reflect` 는 "비추다·드러내다"라서 "그 지적이 겉으로 보인다" 정도가 된다. 의견이나 지적에는 `address`, 즉 다루어 해소한다는 동사가 정확하다. "최소 구조"는 `minimum structure` 보다 관계절로 조건을 달아야 무엇에 대해 최소인지가 분명해진다. `still` 한 단어가 "줄이되 이건 놓치지 마라"는 긴장을 만든다.

### 카드 11 — 공유 승인 명시   (내가 쓴 한글)
- 내가 쓴 한글: "사용자가 이 문서와 아래 설계 요약을 검토 목적으로 Claude에 전달하는 것을 명시적으로 승인했습니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: Sharing this document and the design summary below with Claude for review has been explicitly authorized.
- 왜 이렇게: 원문은 "사용자가 승인했다"는 능동문인데 그 사용자가 지금 말하는 나 자신이라, 영어로 옮기면 이상해진다. **수동태로 돌려 행위자를 지우는 게 오히려 자연스러운 드문 경우다.** 승인이나 허가 문맥에서 `has been authorized` 는 관료적이라기보다 표준이다. `approve` 는 안건에 찬성한다는 뜻이라, 권한을 부여하는 이 자리에는 `authorize` 가 맞다.

### 카드 12 — 역할 분담 규정   (내가 쓴 한글)
- 내가 쓴 한글: "LLM은 의미 해석/예외 설명/요약만 담당하고 예산, JSON 유효성, 단계 진입 판단은 코드가 강제합니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: The LLM handles only interpretation, exception narration, and summarization; budgets, JSON validity, and stage-entry decisions are enforced in code.
- 왜 이렇게: 두 절이 대조라서 마침표보다 세미콜론이 낫다. 각각 독립된 문장이면서 한 규칙의 두 반쪽이다. "코드가 강제한다"는 능동으로 `code enforces` 도 되지만, 대조의 초점이 *무엇이* 강제되는가에 있으므로 그 명사들을 주어 자리로 올리는 수동태가 문장의 무게중심을 맞춘다. "예외 설명"은 `exception explanation` 이 아니라 `exception narration` — 기계가 뱉은 예외를 사람 말로 풀어 준다는 뜻에 더 가깝다.

### 카드 13 — 범위 제외 선언   (내가 쓴 한글)
- 내가 쓴 한글: "전자결재 연동은 현 범위에서 제외합니다."   (출처: transcript:[user] equipment-data-map ddf9d4ae)
- 자연스러운 영어: Electronic-approval integration is out of scope for now.
- 왜 이렇게: `excluded from the current scope` 라고 길게 쓸 필요가 없다. `out of scope` 가 그대로 굳은 구다. "현"은 `current` 로 형용사를 하나 더 얹기보다 `for now` 로 뒤에 붙이는 편이 가볍고, "나중에는 할 수도 있다"는 여지까지 남긴다. 원문의 "현 범위"가 딱 그 뜻이다.

### 카드 14 — 저장 뒤 경로만 답하라   (내가 쓴 한글)
- 내가 쓴 한글: "저장소 파일은 수정하지 마세요. 완료 후 임시 파일 경로만 답하세요."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: Leave the repository files untouched. When you are done, reply with the temp file path and nothing more.
- 왜 이렇게: "수정하지 마세요"를 매번 `Do not edit` 으로 쓰면 지시문이 금지 목록처럼 무거워진다. `Leave X untouched` 는 같은 내용을 **긍정문**으로 말해 읽기가 가볍고, 지켜야 할 상태를 그림으로 준다. "~만 답하세요"는 `reply only with X` 도 되지만, 카드 5와 같은 이유로 `and nothing more` 를 뒤에 붙이는 쪽이 빠져나갈 틈이 없다.

### 카드 15 — 파일 복사 요청   (내가 쓴 한글)
- 내가 쓴 한글: "참고 py file과 md 파일을 @../skewnono_v3_nuxt/docs/ 로 copy 해줘"   (출처: transcript:[user] auto-recipe-creator f4dfd099)
- 자연스러운 영어: Copy the reference `.py` and `.md` files over to `../skewnono_v3_nuxt/docs/`.
- 왜 이렇게: "참고"는 `reference` 가 그대로 형용사로 붙는다(`a reference implementation`, `reference files`). 확장자를 말할 때는 `py file` 보다 `.py` 처럼 점을 찍는 게 표준이고, 두 확장자를 나열할 때 `files` 는 뒤에 한 번만 쓴다. `copy A to B` 도 맞지만 `copy A over to B` 의 `over` 가 이쪽에서 저쪽으로 옮겨 놓는 방향감을 더해 준다.

### 카드 16 — 저성능 모델까지 견디는 것이 목표   (내가 쓴 한글)
- 내가 쓴 한글: "최소 Qwen3.8 28B급 모델에서도 안정적으로 수행하는 것입니다."   (출처: transcript:[user] equipment-data-map 8d7cb2ac)
- 자연스러운 영어: It has to run reliably even on models as small as Qwen3.8 28B.
- 왜 이렇게: "최소 ~급"이 까다롭다. `at minimum` 을 쓰면 최소 요구사항 목록처럼 들리는데, 실제 뜻은 "그 정도로 작은 모델에서도"이므로 `as small as` 가 맞다. "수행하다"의 주어가 한국어에서는 생략됐지만 영어는 주어가 있어야 하니 설계를 가리키는 `It` 을 세운다. `perform stably` 는 문법상 틀리지 않아도 기계 번역 냄새가 나고, 소프트웨어에는 `run reliably` 가 관용이다.

### 카드 17 — 한 번 쓰고 죽는 스킬   (고급 한글 · 번역)
- 한글 원문: "이걸 실행 스킬 5개로 만들면 1·2·3번은 한 번 쓰고 죽는 스킬입니다. Skill Market에 배포된 뒤 영구히 존재하면서 아무도 호출하지 않고, 저성능 모델의 라우팅 후보로만 남아 오답률을 올립니다."   (출처: transcript:[assistant] equipment-data-map ddf9d4ae)
- 자연스러운 영어: Turn these into five executable skills and the first three are single-use skills. Once published to the Skill Market they live there forever, called by no one, surviving only as routing candidates that raise the miss rate for weaker models.
- 번역 포인트: "한 번 쓰고 죽는"을 `die after one use` 로 직역하면 영어에서는 과하게 극적이다. `single-use` 라는 굳은 형용사가 있고, 일회용 도구를 가리키는 그 그림이 원문의 냉소와 정확히 겹친다. "~하면 ~이다"는 조건절 `If you turn these into …` 로 가도 되지만 **명령형 + `and`** 구문이 훨씬 간결하고 구어적 힘이 있다. 뒤 문장의 "존재하면서 / 호출하지 않고 / 남아"라는 세 겹을 영어로 전부 절로 만들면 무너진다. 주절 하나(`they live there forever`)를 세우고 나머지 둘을 분사구로 내려 계층을 만든다.

### 카드 18 — 스킬 경계가 아니라 문서 섹션 경계   (고급 한글 · 번역)
- 한글 원문: "그건 스킬 경계가 아니라 문서 섹션 경계입니다."   (출처: transcript:[assistant] equipment-data-map ddf9d4ae)
- 자연스러운 영어: That is not a skill boundary; that is a section heading.
- 번역 포인트: "A가 아니라 B"는 보통 `not A but B` 로 배우지만, 실제 영어 논증문에서 `but` 은 무겁다. 세미콜론으로 두 문장을 나란히 놓고 `that is` 를 반복하면 대구가 더 또렷해진다. 두 번째 항의 "문서 섹션 경계"를 `document section boundary` 로 직역하면 첫 항과 대칭은 맞아도 실제로 쓰지 않는 말이 된다. `a section heading` 으로 바꾸면 "그건 코드 구조가 아니라 목차일 뿐"이라는 폄하가 살아난다. 대칭을 조금 깨는 대신 뜻을 살리는 쪽을 골랐다.

### 카드 19 — 확인창이 잦을수록   (고급 한글 · 번역)
- 한글 원문: "운영자 피로(무지성 y 연타)도 실제 위험입니다 — 확인창이 잦을수록 확인의 의미가 사라집니다."   (출처: transcript:[assistant] equipment-data-map ddf9d4ae)
- 자연스러운 영어: Operator fatigue — mashing `y` without reading — is a real risk too: the more often you prompt for confirmation, the less any confirmation means.
- 번역 포인트: "무지성 연타"는 대응 명사가 없어서 동작으로 푼다. `mash` 는 키를 마구 두드리는 소리까지 담은 구어 동사이고, `without reading` 이 "무지성"의 실질을 짚는다. 뒷절은 `the 비교급, the 비교급` 구문이 정확히 맞아떨어지는 자리다. 주목할 건 두 번째 `any` 다. `the less confirmation means` 라고 하면 그 확인창 하나만 가리키는데, `any` 를 넣으면 **모든 확인 절차의 값어치가 함께 떨어진다**는 원문의 뜻이 산다.

### 카드 20 — 좌표 이식이 불가능하다   (고급 한글 · 번역)
- 한글 원문: "OM/SEM 은 FOV 가 달라 좌표 이식이 불가능 — 'combined' 는 좌표 합성이 아니라 side-by-side 배치가 유일하게 맞는 해석이다."   (출처: transcript:[assistant] auto-recipe-creator f4dfd099)
- 자연스러운 영어: OM and SEM have different fields of view, so coordinates cannot be carried across — which means "combined" can only mean a side-by-side layout, not a merged coordinate space.
- 번역 포인트: "이식"은 장기 이식의 `transplant` 가 아니라 좌표를 옮겨 적용한다는 뜻이라 `carry across` 가 맞다. 원문은 명사 위주("이식이 불가능")인데 영어는 동사로 풀어야 읽힌다. 이게 한→영에서 가장 자주 필요한 변환이다. 마지막 "유일하게 맞는 해석"을 `the only correct interpretation` 으로 옮기면 무겁고 학술적이다. `can only mean` 이라는 조동사 하나로 같은 배타성을 담고, `not a merged coordinate space` 를 뒤에 달아 배제 대상을 명시하는 편이 훨씬 영어답다.

## 영어 다듬기

### 카드 1 — GPU 배치를 물을 때
- 내가 쓴 영어: "it seems we are settled down to run the qwen model and the other two models without problem. is there any issues if I run the qwen with the two H200 GPUs like having half and half from the both sides and the other two model in each GPU."   (출처: transcript:[user] llm-serving 842f4019)
- 정정: 네 군데다. ① `we are settled down` — `settle down` 은 "(사람이) 자리를 잡다·진정하다"라서 여기 뜻이 아니다. 결론에 도달했다는 뜻은 `we've settled on`, 지금처럼 "잘 돌아가는 상태"를 말하려면 `we're set up to` 가 맞다. ② `is there any issues` — 주어가 복수 `issues` 이므로 `are there any issues`. ③ `the both sides` — `both` 앞에는 정관사를 붙이지 않는다. ④ `the other two model` — `two` 뒤는 복수 `models`.
- 더 나은 표현: "It looks like we're set up to run qwen and the other two models without problems. Any issue with giving qwen both H200s, split across the two, and putting the other two models one per GPU?"
- 왜: `it seems` 도 맞지만 눈으로 본 상태를 말할 때는 `it looks like` 가 더 자연스럽다. "half and half from the both sides"는 무엇이 반반인지 흐린데, GPU 두 장에 모델 하나를 나눠 얹는 구성이므로 `split across the two` 가 정확하다. 마지막의 `in each GPU` 는 "각 GPU에 두 모델을 다"로도 읽히므로 `one per GPU` 로 배분을 명시한다.

### 카드 2 — 좌표를 문서화해 달라는 요청
- 내가 쓴 영어: "write down in the docs folder that the methodology of displaying the crosshair extracting from the cond.txt and combined with the align images of OM and SEM. Give me the detail where cond.txt files are located, and what to extract for the coordination too."   (출처: transcript:[user] auto-recipe-creator f4dfd099)
- 정정: ① `write down … that the methodology` — `that` 절이 시작됐는데 동사가 오지 않아 문장이 끝나지 않는다. `that` 을 빼고 `document the methodology` 로 목적어를 바로 받는다. ② `extracting from` — 십자선은 뽑는 주체가 아니라 뽑히는 대상이므로 과거분사 `extracted from`. ③ `the detail` — 여러 항목이므로 `the details`. ④ 명사 뒤에 절을 바로 붙일 수 없어 `details of where …` 처럼 전치사가 필요하다. ⑤ **`coordination` → `coordinates`.** 오늘 가장 값비싼 오류다. `coordination` 은 "협조·조율"이고, 좌표는 늘 복수 `coordinates` 다.
- 더 나은 표현: "In the docs folder, document how the crosshair is extracted from `cond.txt` and overlaid on the aligned OM and SEM images. Include where the `cond.txt` files live and which values to read for the coordinates."
- 왜: "methodology of displaying"처럼 명사를 겹쳐 쌓는 대신 `how the crosshair is extracted …` 라는 의문사절로 풀면 문장이 스스로 정리된다. `combined with` 는 두 대상을 대등하게 섞는 그림이라 실제 작업(이미지 *위에* 겹쳐 그리기)과 어긋나고, `overlaid on` 이 정확하다. `align images` 는 명령형으로 읽히므로 `aligned images` 로 분사를 써야 "정렬된 이미지"가 된다.

### 카드 3 — 고칠 값어치가 있는지
- 내가 쓴 영어: "worth of fixing?"   (출처: transcript:[user] llm-serving b0fb3a9d)
- 정정: `worth` 뒤에는 전치사 없이 동명사가 바로 온다 — `worth fixing?`. `worth of` 는 `a week's worth of work`(일주일치 분량)처럼 **양**을 셀 때만 쓰는 다른 구문이다.
- 더 나은 표현: "Worth fixing?" 한 단계 위로는 "Any of these worth acting on?"
- 왜: 리뷰 결과 여러 건을 받고 던지는 질문이라 `these` 로 대상을 지정해 주면 상대가 무엇에 답할지 안다. `act on` 은 `fix` 보다 넓어서 고치는 것 말고 기록·보류 같은 선택지도 열어 둔다.

### 카드 4 — 설정 방법을 물을 때
- 내가 쓴 영어: "I thought that the qwen model is able to read images. how can we set?"   (출처: transcript:[user] llm-serving 842f4019)
- 정정: `set` 은 타동사라 목적어가 있어야 한다. `how can we set?` 만으로는 문장이 끝나지 않는다 — `how do we set that up?` 처럼 목적어와 부사를 붙인다.
- 더 나은 표현: "I thought qwen could read images. How do we turn that on?"
- 왜: 두 가지가 올라간다. 첫째, `I thought that … is` 는 시제가 어긋난다. `I thought` 가 과거이므로 종속절도 과거로 당겨 `could` 가 되는 게 표준이다. 둘째, `the qwen model` 은 이 대화에서 이미 아는 대상이라 `qwen` 만으로 충분하다. 관사와 동격 명사를 걷어내면 문장이 빨라진다. 설정을 켜는 맥락에서는 `set up` 보다 `turn on` 이 짧고 정확하다.

### 카드 5 — 가상환경과 상관있는지
- 내가 쓴 영어: "does it has anything to do with .venv?"   (출처: transcript:[user] llm-serving b0fb3a9d)
- 정정: 조동사 `does` 가 이미 3인칭 단수를 표시했으므로 본동사는 원형이다 — `does it have`. `has` 는 조동사 없이 쓸 때만 나온다(`it has nothing to do with …`).
- 더 나은 표현: "Could the venv have anything to do with this?"
- 왜: `have anything to do with` 자체는 아주 좋은 관용구다. 다만 `does` 로 물으면 사실 확인이고 `could` 로 물으면 **가설 제기**가 된다. 원인을 함께 좁혀 가는 대화에서는 후자가 맞고, 상대가 "아니다"라고 답하기도 편하다. 구어에서 `.venv` 는 점을 떼고 `the venv` 라고 부른다.

### 카드 6 — 버전 다운그레이드 문의
- 내가 쓴 영어: "can I downgrade vllm to lower version for the compatiblity?"   (출처: transcript:[user] llm-serving b0fb3a9d)
- 정정: ① `to lower version` — 셀 수 있는 단수 명사라 관사가 필요하다(`to a lower version`). ② `for the compatibility` — 추상명사를 일반적 의미로 쓸 때는 무관사다(`for compatibility`). ③ `compatiblity` 는 철자 오타로, `compatibility` 다.
- 더 나은 표현: "Can I drop vllm to an older version to get compatibility back?"
- 왜: `downgrade` 도 맞지만 `drop X to Y` 가 더 구어적이고 버전을 낮춘다는 동작이 직접적이다. `for compatibility` 는 목적을 명사로만 던지는데, `to get compatibility back` 은 **잃었던 걸 되찾는다**는 상황까지 담는다. 드라이버 때문에 깨진 상태를 복구하려던 이 맥락에 정확히 맞다.
