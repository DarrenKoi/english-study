import json
import os
from datetime import date
from pathlib import Path

from pipeline import config, gitutil, transcripts, spool, batch

def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))

def collect(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()
    cfg = config.load_config(root / "config" / "sources.json")
    state = config.load_state(root / "state" / "progress.json")

    units: list[dict] = []
    # repo 별 이번 실행에서 다룬 파일 집합과 head 를 기록 (배치 후 queue/전진 계산용)
    repo_plan: dict[str, dict] = {}

    # 1) spool 노트(사용자가 직접 적은 학습 질문) — 최우선
    for note in spool.pending_notes(root):
        rel = note.relative_to(root).as_posix()
        units.append({"kind": "spool", "id": note.name,
                      "provenance": f"spool:{rel}", "text": note.read_text(encoding="utf-8"),
                      "advance": {"note": rel}})

    # 2) repo 별 증분 마크다운 — 파일 1개 = 단위 1개 (예산이 파일 단위로 작동).
    #    부분 소비 시 남은 파일을 repo_queue 로 기억해 SHA 는 전부 소진된 뒤에만 전진한다.
    base = _expand(cfg["base_path"])
    for r in cfg["repos"]:
        name = r["name"]
        repo_path = base / name
        if not repo_path.exists():
            continue
        gitutil.pull(repo_path)
        head = gitutil.head_sha(repo_path)
        # 진행 중인 queue 가 같은 head 를 가리키면 재-diff 없이 남은 파일만 이어서 소진한다.
        q = state["repo_queue"].get(name)
        if q and q.get("target") == head:
            files = [f for f in q.get("remaining", []) if (repo_path / f).exists()]
        else:
            files = gitutil.changed_md_files(repo_path, state["repos"].get(name), r["globs"])
        repo_plan[name] = {"head": head, "files": list(files)}
        for f in files:
            units.append({"kind": "repo_file", "id": f"{name}/{f}",
                          "provenance": f"repo:{name} {f}",
                          "text": (repo_path / f).read_text(encoding="utf-8", errors="replace"),
                          "advance": {"repo": name, "file": f}})

    # 3) 트랜스크립트 — 파일 1개 = 단위 1개
    tx_dir = _expand(cfg["transcripts_dir"])
    recs, new_offsets = transcripts.new_messages(tx_dir, state["transcripts"])
    by_file: dict[str, list[str]] = {}
    for rec in recs:
        by_file.setdefault(rec["file"], []).append(f"[{rec['role']}] {rec['text']}")
    for fname, texts in by_file.items():
        units.append({"kind": "transcript", "id": fname,
                      "provenance": f"transcript:{fname}", "text": "\n\n".join(texts),
                      "advance": {"transcript": fname, "offset": new_offsets[fname]}})

    # 예산 내 조립
    batch_text, consumed = batch.build_batch(units, cfg.get("char_budget", 200000), today)

    # 매니페스트(소비 단위만 상태 전진 대상)
    manifest = {"repos": {}, "repo_queue": {}, "transcripts": {}, "spool": [],
                "deferred": len(units) - len(consumed)}
    consumed_repo_files: dict[str, set[str]] = {}
    for u in consumed:
        adv = u["advance"]
        if u["kind"] == "repo_file":
            consumed_repo_files.setdefault(adv["repo"], set()).add(adv["file"])
        elif u["kind"] == "transcript":
            manifest["transcripts"][adv["transcript"]] = adv["offset"]
        elif u["kind"] == "spool":
            manifest["spool"].append(adv["note"])

    # repo 별 소진 여부 판정: 전부 소비됐으면 SHA 전진, 일부면 남은 파일을 queue 로.
    for name, plan in repo_plan.items():
        done = consumed_repo_files.get(name, set())
        remaining = [f for f in plan["files"] if f not in done]
        if remaining:
            manifest["repo_queue"][name] = {"target": plan["head"], "remaining": remaining}
        else:
            manifest["repos"][name] = plan["head"]

    (root / "state").mkdir(parents=True, exist_ok=True)
    batch_path = root / "state" / f"batch-{today}.md"
    batch_path.write_text(batch_text, encoding="utf-8")
    (root / "state" / f"consumed-{today}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"item_count": len(consumed), "deferred": manifest["deferred"],
            "batch_path": str(batch_path), "today": today}

if __name__ == "__main__":
    print(collect())
