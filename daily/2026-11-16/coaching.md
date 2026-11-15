# 2026-11-16 — 코칭

오늘은 내가 쓴 메시지가 전부 영어였다. 그래서 내가 쓴 한글 카드는 없고 영어 다듬기 5장이 중심이다. 한글→영어에는 번역 정독 4장만 넣었는데, 대화 속 `[assistant]` 본문도 영어뿐이라 한국어 시험 실행에서 서브에이전트(카운슬 조언자·검토자·의장)가 쓴 한국어 답변에서 골랐다.

## 한글→영어

### 카드 1 — 잡는 것 없이 초록불만   (고급 한글 · 번역)
- 한글 원문: "지금 정의대로면 잡는 것 없이 초록불만 켜집니다."   (출처: transcript: 서브에이전트 답변 — 조언자 '반대론자')
- 자연스러운 영어: As currently defined, the check catches nothing and still goes green.
- 번역 포인트: "지금 정의대로면"은 `If we follow the current definition` 으로 풀지 않고 `As currently defined` 분사구로 줄인다. "초록불이 켜지다"는 테스트 맥락에서 `go green` 이 굳은 말이다. "~없이 ~만"의 비꼼은 `and still` 이 살린다. 더 세게 쓰려면 `a green light that proves nothing`.

### 카드 2 — 결함은 도구가 아니라 강제력   (고급 한글 · 번역)
- 한글 원문: "'가'의 결함은 도구가 아니라 강제력입니다. "에이전트가 확인한다"에는 누락을 막는 장치가 없고, 깨진 화면이 배포되는 이유가 바로 그것입니다."   (출처: transcript: 서브에이전트 답변 — 조언자 '반대론자')
- 자연스러운 영어: What option A lacks is enforcement, not tooling. "The agent checks" has nothing in it to stop a skipped check, and that is exactly why broken screens get shipped.
- 번역 포인트: "A가 아니라 B"를 영어는 흔히 B부터 말한다(`enforcement, not tooling`). "강제력"은 `force` 가 아니라 `enforcement` 다. "누락을 막는 장치"를 `a device` 로 옮기면 기계처럼 들리므로 `nothing in it to stop a skipped check` 로 풀었다. "바로 그것"의 강조는 `that is exactly why`. "배포되다"는 `get shipped` 가 `be deployed` 보다 "어쩌다 나가 버렸다"는 어감에 가깝다.

### 카드 3 — 관문이 자기 승인이 된다   (고급 한글 · 번역)
- 한글 원문: "여러 에이전트가 UI를 계속 바꾸므로 기준 이미지는 매번 깨지고, 갱신도 에이전트가 하므로 관문이 자기 승인이 됩니다."   (출처: transcript: 서브에이전트 답변 — 검토자 1)
- 자연스러운 영어: With several agents constantly changing the UI, the baseline images break every time, and since the agents also update them, the gate turns into self-approval.
- 번역 포인트: "~하므로"가 두 번 나온다. `because` 를 반복하지 않고 첫째는 `With + 명사 + -ing`, 둘째는 `since` 로 갈랐다. "기준 이미지"는 스크린샷 비교에서 `baseline images`(또는 `golden images`). "관문"은 `gate` 이고 "~이 되다"는 `become` 보다 `turn into` 가 변질의 느낌을 준다. 오늘 정독의 `grading your own homework` 로 받아도 뜻이 통한다.

### 카드 4 — 결론 전체가 걸려 있다   (고급 한글 · 번역)
- 한글 원문: "양쪽 모두 실행해 보지 않은 주장이며, 이 대립에 결론 전체가 걸려 있습니다."   (출처: transcript: 서브에이전트 답변 — 의장 판결문)
- 자연스러운 영어: Neither side has actually run it, and the whole conclusion hinges on this disagreement.
- 번역 포인트: "양쪽 모두 ~하지 않은"은 `Both sides did not` 이 아니라 `Neither side has` 다(`Both … not` 은 부분 부정으로 읽힐 수 있다). "실행해 보지 않은 주장"을 명사구(`untested claims`)로 옮길 수도 있지만 동사로 푼 쪽이 말에 가깝다. "~에 걸려 있다"는 `hinge on`, 경첩 하나에 문 전체가 달린 그림이다. `depend on` 보다 "이것 하나"가 강조된다.

## 영어 다듬기

### 카드 5 — 설치 요청
- 내가 쓴 영어: "install this skill in this computer git clone https://github.com/tenfoldmarc/llm-council-skill ~/.claude/skills/llm-council"   (출처: transcript:[user])
- 정정: `in this computer` → `on this computer`. 컴퓨터·서버·기기에 설치할 때 전치사는 `on` 이다(`in` 은 물리적으로 그 안에 넣는다는 뜻이 된다).
- 더 나은 표현: Install this skill on this machine by running: `git clone https://github.com/tenfoldmarc/llm-council-skill ~/.claude/skills/llm-council`
- 왜: 요청과 명령어가 한 줄에 붙어 있어 어디까지가 문장인지 흐리다. `by running:` 뒤에 명령을 두면 경계가 선다. `this` 가 두 번 나오니 하나는 `machine` 으로 바꿔 반복을 피했다. 개발자끼리는 `computer` 보다 `machine` 을 더 자주 쓴다.

### 카드 6 — 가능하면 개선해 달라
- 내가 쓴 영어: "upgrade llm-council skill if you can"   (출처: transcript:[user] /skill-creator 인자)
- 정정: `llm-council skill` → `the llm-council skill`. 이미 설치해 둔 특정 스킬이라 정관사가 필요하다.
- 더 나은 표현: See if you can improve the llm-council skill.
- 왜: `upgrade` 는 버전을 올린다는 느낌이 강하다. 내용을 더 좋게 고치는 일은 `improve` 가 맞다. `if you can` 을 끝에 붙이면 "할 수 있으면 해"로 들리는데, `See if you can …` 으로 시작하면 "개선할 여지가 있는지 살펴봐 달라"는 원래 의도가 그대로 실린다.

### 카드 7 — 시험 실행 지시
- 내가 쓴 영어: "try test-run to get the best result"   (출처: transcript:[user])
- 정정: `try test-run` → `try a test run`. `test run` 은 셀 수 있는 명사라 관사가 필요하고, 명사로 쓸 때는 하이픈 없이 띄운다(하이픈은 `a test-run script` 처럼 앞에서 꾸밀 때).
- 더 나은 표현: Do a test run and keep refining it until the output is as good as you can get it.
- 왜: `to get the best result` 는 시험 실행 한 번이 최고 결과를 낸다는 말처럼 읽힌다. 실제 의도는 "돌려 보고 고쳐 가며 다듬어라"였으니 `and keep refining it until …` 으로 과정을 말해 준다. `try` 뒤에 명사를 놓는 것보다 `do a test run`, `give it a test run` 이 자연스럽다.

### 카드 8 — 한국어로도 쓸 수 있게
- 내가 쓴 영어: "the llm-council skill can be also usable in Korean language too."   (출처: transcript:[user])
- 정정: 세 군데다. ① `also … too` 는 같은 뜻이 겹치니 하나만 쓴다. ② `can be usable` 은 가능이 두 번 들어갔다(`can` + `-able`). `should work` 나 `should be usable` 로 쓴다. ③ `in Korean language` → `in Korean`. 언어 이름에는 `language` 를 붙이지 않고, 붙인다면 `in the Korean language` 다.
- 더 나은 표현: The llm-council skill should work in Korean too.
- 왜: 원문은 "쓸 수 있다"는 사실 진술로도, "쓸 수 있어야 한다"는 요청으로도 읽힌다. 요청이었으니 `should` 로 못박는다. 더 분명히 하려면 `Please make the llm-council skill work in Korean as well.` `also` 를 쓴다면 자리는 조동사 뒤, be동사 앞이다(`should also be usable`).

### 카드 9 — Codex 를 카운슬 멤버로
- 내가 쓴 영어: "yes test them all. To include the codex as council member, you can use herdr skill"   (출처: transcript:[user])
- 정정: 관사가 세 곳 어긋났다. `the codex` → `Codex`(제품 이름은 고유명사라 관사 없음), `as council member` → `as a council member`(셀 수 있는 단수 명사), `herdr skill` → `the Herdr skill`(특정한 그 스킬). `yes` 뒤에는 쉼표를 찍는다.
- 더 나은 표현: Yes, test them all. You can bring Codex in as a council member through the Herdr skill.
- 왜: 고유명사에는 관사를 빼고 보통명사에는 넣는다는 구분이 한 문장 안에서 세 번 시험됐다. `To include …, you can use …` 도 틀리지 않지만 목적을 앞세우면 문장이 무거워진다. `bring X in as Y`(X를 Y로 합류시키다)와 수단을 나타내는 `through` 로 한 호흡에 말하는 쪽이 대화에 가깝다. 어시스턴트의 최종 보고도 같은 전치사를 썼다. `can include Codex as a council member through Herdr.`
