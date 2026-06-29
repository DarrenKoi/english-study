# 2026-06-30 — 코칭

> 이 배치에는 내가 직접 한국어로 쓴 문장이 없었다(트랜스크립트의 `[user]` 는 거의 다
> 영어 오케스트레이션 지시문). 그래서 **한글→영어** 섹션은 생략하고, 내가 채팅으로 직접 친
> 영어 한 줄만 다듬는다. 나머지 긴 지시문은 이미 원어민 수준이라 억지 교정을 만들지 않는다.

## 영어 다듬기

### 카드 1 — 명세 검토 부탁
- 내가 쓴 영어: "give the spec a read to confirm the fix-type and distinct_floor default value"   (출처: transcript:[user])
- 정정: (문법 오류 없음 — 자연스럽고 관용적인 캐주얼 영어다.)
- 더 나은 표현:
  - 같은 톤(캐주얼) 유지, 약간 더 매끄럽게: *Give the spec a quick read and confirm the fix-type semantics and the `distinct_floor` default.*
  - 한 단계 격식 올려(문서/이슈에 적을 때): *Please review the spec to verify the fix-type classifier semantics and the default value of `distinct_floor`.*
- 왜:
  - 원문은 `confirm A and B` 에서 A(`the fix-type`)와 B(`distinct_floor default value`)의 **구조가 비대칭**이다. A 에 `semantics`(또는 `classifier`) 같은 핵심명사를 붙이면 "무엇을 확인하는지"가 또렷해지고 B 와 균형이 맞는다.
  - `give ... a read` 는 구어에서 훌륭하다. 다만 이슈·PR 처럼 **글로 남기는** 맥락이면 `review`/`verify` 가 더 격식 있고 검색·인용에도 적합하다 — 같은 뜻을 *말로 할 때 give a read / 글로 쓸 때 review* 로 나눠 쓰면 좋다.
  - `the default value of X` 가 `X default value` 보다 명사 연쇄(noun pile-up)를 풀어 줘 읽기 쉽다.
