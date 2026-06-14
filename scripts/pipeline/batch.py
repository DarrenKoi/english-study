def build_batch(units: list[dict], char_budget: int, today: str) -> tuple[str, list[dict]]:
    header = f"# 수집 배치 — {today}\n\n"
    parts = [header]
    consumed: list[dict] = []
    used = 0
    for u in units:
        block = f"\n## [{u['provenance']}]\n\n{u['text']}\n"
        # 최소 한 단위는 무조건 포함, 이후엔 예산을 지킨다
        if consumed and used + len(block) > char_budget:
            continue
        parts.append(block)
        consumed.append(u)
        used += len(block)
    return "".join(parts), consumed
