# 2026-06-20 — 코칭

## 영어 다듬기

### 카드 1 — 폴더 이름에 timestamp 추가 제안
- 내가 쓴 영어: "I have found that @poc/workflow_1/align_fail_alarm_record.py I think we should use timestamp in the folder name as we have multiple images stackup in the same folder path when there are more than one align fail for the same tool and recipe. can we add timestamp as a suffix to the eqp_id in the folder? so that we have like 20260530_133020_{eqp_id}"   (출처: transcript:[user] 15a1d642 세션)
- 정정:
  - **"I have found that @… I think we should"** — 두 개의 주절이 접속사 없이 붙은 run-on(달리는 문장). `I have found that` 뒤에는 명사절이 와야 하는데 곧장 `I think` 가 또 시작됩니다. → 앞을 분사구로 줄여 `Looking at @poc/workflow_1/align_fail_alarm_record.py, I think we should …` 로.
  - **"multiple images stackup"** — `stackup` 은 명사(또는 잘못 붙인 두 단어)입니다. 동사가 필요하니 `stack up` 또는 `get stacked`. → `multiple images stack up in the same folder` / `multiple images get stacked into one folder`.
  - **"when there are more than one align fail"** — `more than one` 은 단수 취급(`more than one … occurs`)이고, `align fail` 은 명사로 `align failure` 가 자연스럽습니다. → `when more than one align failure occurs` 또는 복수로 `when there are multiple align failures`.
  - **"use timestamp" / "add timestamp"** — 가산명사라 관사가 필요: `use a timestamp`, `add a timestamp`.
  - 소문자 문장 시작(`can we …`, `so that …`)은 대문자로.
- 더 나은 표현:
  - 자연스러운 회화체: *"Looking at `align_fail_alarm_record.py`, I think we should put a timestamp in the folder name. Right now, when more than one align failure happens for the same tool and recipe, all the images stack up in the same folder. Could we add a timestamp prefix to the `eqp_id` folder — e.g. `20260530_133020_{eqp_id}`?"*
  - 더 격식 있는 문어체: *"In `align_fail_alarm_record.py`, multiple align failures for the same tool and recipe currently write into a single folder, so their images stack up. I propose prefixing the `eqp_id` folder with a timestamp (e.g. `20260530_133020_{eqp_id}`) to keep each event separate."*
- 왜: 원문은 뜻이 다 통하지만 (1) 문장 경계가 흐려 한 호흡에 두 생각이 엉켰고, (2) `stackup`·`align fail`·무관사 명사 같은 작은 형태 오류가 있습니다. 핵심 개선은 **"현상(images stack up) → 원인(more than one failure) → 제안(add a timestamp prefix)"** 으로 정보를 끊어 배열하는 것 — 동료가 한 번에 이해하고 바로 "네/아니오"로 답할 수 있게 됩니다. 제안은 `I think we should` / `I propose` / `Could we …?` 중 격식에 맞춰 고르세요.
