#!/usr/bin/env python3
"""Render free-certifications/README.md from free-certifications/catalog.json.

Usage: python3 scripts/build_catalog.py
Edit catalog.json or config.json (never the generated README) and re-run this script.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "free-certifications" / "catalog.json"
OUT = ROOT / "free-certifications" / "README.md"

CONFIG = ROOT / "free-certifications" / "config.json"
BADGE = {"certificate": "Certificate", "badge": "Badge"}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).strip().replace(" ", "-")


def main() -> None:
    config = json.loads(CONFIG.read_text())
    role = config["role"]
    tracks = [tuple(t) for t in config["tracks"]]
    items = json.loads(DATA.read_text())
    known = {t[0] for t in tracks}
    unknown = sorted({i["track"] for i in items} - known)
    if unknown:
        raise SystemExit(f"Tracks missing from config.json: {unknown}")
    by_track: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        by_track[item["track"]].append(item)
    providers = Counter(i["provider"] for i in items)
    tracks = [t for t in tracks if by_track[t[0]]]

    lines = [
        "# Free AI Certifications Tracker",
        "",
        "> Your AI credentials, all in one place. A curated catalog of **free** AI courses from **FAANG, Big Tech and the "
        "frontier AI labs** that award a **free certificate or badge**, ordered as a study path for " + role + ".",
        "",
        f"**{len(items)} credentials** from **{len(providers)} providers**. "
        "Fork this repository and tick the boxes as you earn each credential, then add them to your LinkedIn "
        "*Licenses & certifications* section.",
        "",
        "> [!IMPORTANT]",
        "> Do the work yourself. Using bots or AI agents to complete courses, quizzes or exams on your behalf "
        "breaks most providers' terms, can get your account and credentials revoked, and defeats the purpose: "
        "interviewers test the skill, not the badge.",
        "",
        "> [!NOTE]",
        "> Generated from [`catalog.json`](catalog.json) by [`scripts/build_catalog.py`](../scripts/build_catalog.py). "
        "Free status is reported by the provider and can change; check the course page before you start. "
        "Not affiliated with or endorsed by any listed provider.",
        "",
        "## Contents",
        "",
    ]
    for name, when, _ in tracks:
        lines.append(f"- [{name}](#{slug(name)}) ({len(by_track[name])}, {when})")
    lines += ["- [Providers](#providers)", "- [How to add a credential](#how-to-add-a-credential)", ""]

    for name, when, blurb in tracks:
        lines += [f"## {name}", "", f"*{when}.* {blurb}", "", "| Done | Course | Provider | Credential | Time |", "| :-: | --- | --- | --- | --- |"]
        for i in sorted(by_track[name], key=lambda x: (x["provider"], x["title"])):
            minutes = f"{i['minutes']} min" if i.get("minutes") else "-"
            title = i["title"].replace("|", "\\|")
            lines.append(f"| <input type=\"checkbox\"> | [{title}]({i['url']}) | {i['provider']} | {BADGE.get(i['credential'], i['credential'])} | {minutes} |")
        lines.append("")

    lines += ["## Providers", "", "| Provider | Credentials |", "| --- | --: |"]
    for p, n in sorted(providers.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {p} | {n} |")
    lines += [
        "",
        "## How to add a credential",
        "",
        "1. Confirm on the official page that both the course **and** the credential are free, and that the provider is a "
        "FAANG, Big Tech or frontier AI lab platform. Small training sites and resellers are not accepted.",
        "2. Add an object to `catalog.json` with `title`, `provider`, `url`, `credential` (`certificate` or `badge`), "
        "`minutes` (or `null`) and one of the track names in `config.json`.",
        "3. Run `python3 scripts/build_catalog.py` and commit both files.",
        "",
    ]
    OUT.write_text("\n".join(lines))
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(items)} credentials.")


if __name__ == "__main__":
    main()
