# 2026-08-05 — 정독

## 단락 1

Images rendering is a load-bearing negative result. `get_param_detail` fetches AMP/AF-PR/cond files from the same raw folder (`data/{idw}/{idp}/`) that the image files live in. Since images render on the cloud, FTP reachability, path derivation, and the `office_utils` import are all proven fine — which eliminates the entire transport half of the search space. What's left is only: the slot values (the `img_meas2` / `img_add2` column values naming the setting files) or the readers themselves.

Parser version skew is the trap here. All five readers were confirmed 2026-07-30 — on the office Windows PC. The cloud runs a different `office_utils` copy, which is exactly what the tuple-wrap 502 proved. Any probe you run must run **on the cloud host**, or it will re-confirm the environment that was never broken.

**문법·구조**: 두 단락 모두 굵은 주제문이 먼저 오고 근거가 뒤따르는 두괄식이다. `Since images render …, X, Y, and Z are all proven fine` 은 관측 사실(종속절)에서 논리적 귀결(주절·수동태)을 끌어내고, 이어지는 계속적 용법 `— which eliminates …` 가 앞 절 전체를 받아 수사적 결론까지 민다. `What's left is only:` 는 의사분열문(pseudo-cleft)으로 남은 용의자를 콜론 뒤에 몰아넣는다. 마지막 문장의 `must …, or it will …` 은 명령 + 경고(안 그러면 ~된다) 구문이고, `the environment that was never broken` 은 관계절 속 수동태 + never 로 "멀쩡한 쪽만 다시 확인하는" 헛수고를 비꼰다.

**핵심 표현**: a load-bearing negative result (아무 일도 안 일어났다는 사실이 오히려 하중을 받치는 증거다), version skew (같아야 할 두 사본의 판 어긋남), re-confirm the environment that was never broken (원래 멀쩡했던 환경만 재확인하기 — 헛짚은 진단의 전형).

**격식 짝** (작성): refined — "which eliminates the entire transport half of the search space." ↔ plain — "so we can stop worrying about anything transport-related." / refined — "Any probe you run must run on the cloud host." ↔ plain — "Run it on the cloud box, or you're testing the wrong machine."

<sub>출처: transcript:skewnono-v3-nuxt/bdade38d</sub>

---

## 단락 2

Copy-one-file client for users pulling images to their PC from Python. No third-party imports, because a controlled in-house PC may have no pip install.

The call order is list -> scoped warm -> fetch, not warm -> list -> fetch. Office-side both the listing endpoint and the warm job do an FTP listing, so warming first costs two; and passing names to the POST scopes the warm to what the ext filter kept, so asking for JPEGs does not make the tool serve TIFFs. Skipping the warm entirely turns N images into N serial FTP round trips, which is the mistake this file exists to prevent.

Files are written via .part and renamed, so an interrupted run cannot leave a truncated file that the resume check would later skip.

**문법·구조**: 커밋 메시지 문체의 표본이다. 첫 줄은 동사 없는 명사구 헤드라인이고, 본문부터 완결문이 시작된다. 규칙 선언은 `A, not B` 대구(list → warm → fetch, **not** warm → list → fetch)로 하고, 근거 두 개를 세미콜론 + and 로 한 문장에 병렬시킨다. 눈여겨볼 것은 동명사 주어의 연쇄 — `passing names …`, `asking for JPEGs …`, `skipping the warm …` — 행위 자체를 주어로 세워 "행위 → 결과"의 인과를 문장 구조로 만든다. `does not make the tool serve TIFFs` 는 사역동사 make + 원형부정사. 마지막 문장의 `cannot leave a truncated file that the resume check would later skip` 은 관계절 안에 would 를 넣어 "나중에 일어났을 가상의 2차 사고"까지 한 문장에 눌러 담는다.

**핵심 표현**: scoped (범위가 딱 필요한 만큼으로 좁혀진 — unscoped 와 대비), turns N images into N serial round trips (실수의 비용을 "변환"으로 표현), the mistake this file exists to prevent (파일의 존재 이유를 막을 실수 하나로 요약).

**격식 짝** (작성): refined — "which is the mistake this file exists to prevent." ↔ plain — "that's exactly the mistake this script is here to stop." / refined — "a controlled in-house PC may have no pip install." ↔ plain — "office PCs often can't pip install anything."

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-04-msr-image-download-api.md</sub>

---

## 단락 3

`comparison.vue`'s `formatBarTooltip` rendered the device description as hardcoded 10px `#888`. Every chart theme paints its tooltip on a contrasting panel, so mid-gray landed at roughly 2.5:1 contrast — effectively invisible. The line now inherits the theme's tooltip text color at 0.85 opacity, and wraps inside a 320px column instead of stretching the tooltip into one long unwrappable strip. Verified in both modes — the description line inherits whatever ink each theme pairs with its tooltip panel, so it reads correctly on the dark panel and the white panel alike. In tooltip/overlay HTML, never hardcode a text color — inherit the container's ink and de-emphasize with opacity, and it survives every theme/mode combination automatically.

**문법·구조**: 접속사 없이 시제만으로 전/후를 가르는 것이 뼈대다 — 과거형(rendered, landed)이 "고치기 전", 현재형(inherits, wraps, reads)이 "고친 후"다. `landed at roughly 2.5:1 contrast — effectively invisible` 은 대시 뒤 평가 부사구로 수치의 의미를 즉석에서 번역해 준다. `instead of + 동명사` 는 채택안과 기각안을 한 문장에 대비시키는 표준 틀. `whatever ink each theme pairs with its tooltip panel` 은 whatever 관계절로 "테마마다 다른 그 값이 무엇이든"을 담고, `on the dark panel and the white panel alike` 의 alike 는 "둘 모두에 똑같이"를 문미 한 단어로 처리한다. 마지막 문장은 명령문 + and 결과절(never hardcode …, and it survives …)로 규칙과 보상을 함께 준다.

**핵심 표현**: effectively invisible (물리적으로는 있지만 사실상 안 보이는 — effectively 가 "실질적으로는"), ink (글자색을 가리키는 디자인권 은어; the container's ink = 부모 요소의 글자색), A and B alike (양쪽 모두에 똑같이).

**격식 짝** (작성): refined — "it survives every theme/mode combination automatically." ↔ plain — "it just works in every theme." / refined — "de-emphasize with opacity" ↔ plain — "just fade it a bit instead of picking a gray."

<sub>출처: transcript:skewnono-v3-nuxt/3043a732</sub>
