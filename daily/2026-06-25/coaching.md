# 2026-06-25 — 코칭

> 이 배치의 `[user]` 메시지는 대부분 영어로 작성되어, 코칭의 중심은 **영어 다듬기**입니다.
> 직접 쓴 한국어(코칭 (a))는 없었고, `[assistant]` 의 한국어 일부만 번역 정독(b)으로 다룹니다.

## 한글→영어

### 카드 1 — "~ 순으로 구성되어 있습니다"   (고급 한글 · 번역)
- 한글 원문: "두 문서 모두 0(문제 정의) → VLM/CV 2-pass 원리 → Sobel/gradient/projection/Laplacian 설명 → summary.json 의 모든 숫자 의미 → 개선 여지 → 용어집 순으로 구성되어 있습니다."   (출처: transcript:[assistant] 07b2cb20)
- 자연스러운 영어: "Both documents are organized in the same order: problem statement (0) → the two-pass VLM/CV principle → an explanation of Sobel/gradient/projection/Laplacian → what every number in `summary.json` means → room for improvement → a glossary."
- 번역 포인트: "~ 순으로 구성되어 있습니다"는 `be organized/structured in the following order` 또는 `follow this order`로 옮긴다. "구성되어 있다"를 `is composed`로 직역하면 어색 — 문서의 목차 흐름은 `organized`가 자연스럽다. "개선 여지"는 `room for improvement`(관용구), "숫자의 의미"는 `what each number means`처럼 명사절로 푸는 게 영어답다. 화살표 흐름은 영어에서도 그대로 `→`로 두되, 앞에 `in the same order:`로 신호를 준다.

### 카드 2 — "메모리에 ~하도록 기록했습니다"   (고급 한글 · 번역)
- 한글 원문: "두 문서 모두 한국어 존댓말로 다시 작성했습니다. 그리고 앞으로 적용되도록 메모리에 두 가지를 기록했습니다."   (출처: transcript:[assistant] 07b2cb20)
- 자연스러운 영어: "I rewrote both documents in polite Korean (존댓말), and I saved two preferences to memory so they're applied going forward."
- 번역 포인트: "앞으로 적용되도록"의 목적·결과는 `so (that) they're applied going forward`로 옮긴다 — `going forward`는 "앞으로는"의 자연스러운 비즈니스 표현(`from now on`보다 격식). "기록했습니다"는 단순 `recorded`보다 `saved ... to memory`가 맥락(설정 저장)에 맞다. "다시 작성했습니다"는 `rewrote`(한 단어)로 충분; `wrote again`은 어색하다.

## 영어 다듬기

### 카드 1 — 불가산명사 data + 문장 끊기
- 내가 쓴 영어: "Now I have collected so many data. I want to test images stored in align_images to see if the image comparison, and click points by VLM. what's the next code that I need to run?"   (출처: transcript:[user] 07b2cb20)
- 정정: ① `so many data` → `so much data` (data는 불가산명사라 many가 아니라 much). ② `to see if the image comparison, and click points by VLM` 은 동사가 빠져 비문 — `see if` 뒤에는 절(주어+동사)이 와야 한다.
- 더 나은 표현: "I've now collected a lot of data. I'd like to test the images stored in `align_images` to see whether the image comparison and the VLM click-point detection work. What's the next script I should run?"
- 왜: `a lot of data`가 가산/불가산 헷갈림을 피하는 안전한 선택. `see if`는 `see whether`로 쓰면 더 격식 있고, 그 뒤에 "X and Y **work**"처럼 동사를 넣어 비교 대상이 "동작하는지"를 명확히 한다. "next code"보다 `next script`/`next step`이 자연스럽다.

### 카드 2 — 복수형 + 단수/복수 일치
- 내가 쓴 영어: "I think there are separated test so you can do this with two different py file? right?"   (출처: transcript:[user] 07b2cb20)
- 정정: ① `separated test` → `separate tests` (형용사는 `separate`, 명사는 복수 `tests` — there are와 일치). `separated`는 "분리된(과거분사)"이라 "별개의"는 `separate`. ② `two different py file` → `two different py files` (two 뒤 복수).
- 더 나은 표현: "I think these are two separate tests, so you can do this in two different `.py` files — right?"
- 왜: `separate`(별개의)와 `separated`(분리해 놓은)는 다른 단어다. 셀 수 있는 명사가 둘 이상이면 반드시 복수형. 확인을 구하는 `right?`는 앞에 콤마+대시로 붙이면 자연스럽다.

### 카드 3 — "~할 방법이 있나요?" 어순
- 내가 쓴 영어: "However, in the targeted area, it is more precise than CV snapped. I think is there method to CV snapped to be modified again with graymask to increase precision?"   (출처: transcript:[user] 22bf3627)
- 정정: ① `I think is there method` 은 평서문 속에 의문문 어순이 섞여 비문 — `I wonder if there is a method` 또는 그냥 직접 의문문으로. ② `method to CV snapped to be modified` 은 to부정사가 꼬임.
- 더 나은 표현: "In the target area, the greymask is actually more precise than the CV-snapped box. Is there a way to refine the CV snap using the greymask to improve precision?"
- 왜: 간접의문(`I think + 의문문`)은 피하고, 묻고 싶으면 직접 의문문 `Is there a way to ...?`이 깔끔하다. `a method to do X` 또는 `a way to do X`처럼 to부정사는 **능동 동사**로 받는다(`to refine the snap`), `to be modified`(수동)로 비틀지 않는다. 명사 앞 관사 `a method/a way`도 빠뜨리지 말 것.

### 카드 4 — 빈도부사 위치
- 내가 쓴 영어: "Without knowing its characteristics, always we hinder the process when we use paddleOCR."   (출처: transcript:[user] 22bf3627)
- 정정: `always we hinder` → `we always hinder` (빈도부사 always는 주어 뒤·일반동사 앞).
- 더 나은 표현: "Until we understand how it behaves, PaddleOCR will keep getting in the way every time we use it."
- 왜: `always/often/never` 같은 빈도부사는 **주어 + (부사) + 일반동사** 순서다. 더 매끄럽게는 `keep -ing`(계속 ~하다) + `get in the way`(방해가 되다, 관용구)로 바꾸면 원어민스럽다. "its characteristics"는 사람·도구의 '특성/거동'을 말할 때 `how it behaves`가 더 구어적이고 자연스럽다.

### 카드 5 — 관사 + 가정 표현
- 내가 쓴 영어: "how do I add template? since we have different models, wait input windows look a bit different. template methods can be hard to implement"   (출처: transcript:[user] 22bf3627)
- 정정: ① `add template` → `add a template` (가산 단수엔 관사 필요). ② 문장 첫 글자 대문자·문장부호 정리.
- 더 나은 표현: "How do I add a template? Since each model's `Wait Input` window looks a bit different, a template-based approach could be hard to make robust."
- 왜: 셀 수 있는 단수명사 앞 `a/the`는 필수. "different models" 별로 창이 다르다는 뜻은 `each model's window looks different`로 소유격을 쓰면 명확하다. "template methods can be hard to implement"는 의도가 "구현이 까다롭다/견고하게 만들기 어렵다"이므로 `hard to make robust`로 구체화하면 한 단계 위의 표현이 된다.
