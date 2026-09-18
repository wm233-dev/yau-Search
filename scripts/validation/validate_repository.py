#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_repository.py — lightweight self-check for the yau-Search repository.

Checks (no third-party dependencies):
  1. required files exist
  2. every *.json parses
  3. data/problems_full.json has the expected size, fields and value ranges
  4. every relative link used in README.md resolves
  5. corpus directories are non-empty and their file counts are reported
  6. no machine-specific absolute paths leaked back into tracked text files

Exit code 0 = all hard checks passed, 1 = at least one failure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "NOTICE.md",
    "requirements.txt",
    ".gitignore",
    "yau_index.html",
    "data/problems_full.json",
    "data/problems_enriched.json",
    "data/papers_manifest.json",
    "data/syllabus_coverage.json",
    "docs/HOW_TO_USE.md",
    "docs/FINAL_REPORT.md",
    "scripts/_paths.py",
    "scripts/extraction/rebuild_pipeline.py",
    "scripts/validation/validate_repository.py",
]

EXPECTED_SUBJECTS = {
    "Algebra & Number Theory",
    "Analysis & PDE",
    "Geometry & Topology",
    "Probability & Statistics",
    "Computational & Applied",
    "Mathematical Physics",
}
EXPECTED_PROBLEM_COUNT = 757
PROBLEM_FIELDS = {"year", "subject", "paper", "kind", "n", "chars", "text"}

# paths that must never appear again in tracked text files
# Markers that must never appear again in tracked text files.
# Assembled from fragments so that this checker does not match itself.
_AUTHOR_DIR = "deepseek" + "_" + "exclusive"
_WORK_DIR = "burn" + "2026"
FORBIDDEN = re.compile("|".join([
    _AUTHOR_DIR,
    _WORK_DIR,
    r"[A-Za-z]:[\\/]+" + _AUTHOR_DIR,
    r"[A-Za-z]:[\\/]+" + _WORK_DIR,
    r"[A-Za-z]:[\\/]+Python31[0-9]",
]))

# historical record of the reorganisation: the old paths are the point of the file
SKIP_FILES = {"archive/MOVES.tsv"}
TEXT_EXT = {".py", ".md", ".json", ".txt", ".mjs", ".html", ".tsv", ".yml", ".toml"}
SKIP_DIRS = {".git", "__pycache__", "corpus"}

failures: list[str] = []
notes: list[str] = []


def check(ok: bool, message: str) -> None:
    print(("  PASS  " if ok else "  FAIL  ") + message)
    if not ok:
        failures.append(message)


def main() -> int:
    print("yau-Search repository self-check")
    print("root:", REPO_ROOT)
    print()

    # 1 -- required files
    print("[1] required files")
    for rel in REQUIRED_FILES:
        check((REPO_ROOT / rel).is_file(), rel)

    # 2 -- all JSON parses
    print()
    print("[2] JSON files")
    json_files = [p for p in REPO_ROOT.rglob("*.json")
                  if not any(part in SKIP_DIRS for part in p.parts)]
    broken = []
    for path in json_files:
        try:
            with path.open(encoding="utf-8") as fh:
                json.load(fh)
        except Exception as exc:                      # noqa: BLE001
            broken.append("%s (%s)" % (path.relative_to(REPO_ROOT), exc))
    check(not broken, "parsed %d JSON files" % len(json_files))
    for item in broken:
        print("        broken:", item)

    # 3 -- canonical problem data
    print()
    print("[3] data/problems_full.json")
    problems_path = REPO_ROOT / "data" / "problems_full.json"
    if problems_path.is_file():
        with problems_path.open(encoding="utf-8") as fh:
            problems = json.load(fh)
        check(len(problems) == EXPECTED_PROBLEM_COUNT,
              "problem count == %d (found %d)" % (EXPECTED_PROBLEM_COUNT, len(problems)))
        missing = [i for i, p in enumerate(problems) if not PROBLEM_FIELDS.issubset(p)]
        check(not missing, "all records carry the required fields %s" % sorted(PROBLEM_FIELDS))
        subjects = {p["subject"] for p in problems}
        check(subjects == EXPECTED_SUBJECTS,
              "subject set matches (%d subjects)" % len(subjects))
        years = sorted({p["year"] for p in problems})
        check(years and years[0] == "2010" and years[-1] == "2026",
              "year range 2010-2026 (found %s..%s)" % (years[0] if years else "?", years[-1] if years else "?"))
        empty = [p for p in problems if not str(p.get("text", "")).strip()]
        check(not empty, "no empty problem texts")
        notes.append("problems: %d | subjects: %s" % (len(problems), ", ".join(sorted(subjects))))

    # 4 -- relative links in README
    print()
    print("[4] README relative links")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)#\s]+)\)", readme)
    bad_links = []
    for link in links:
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        target = (REPO_ROOT / link).resolve()
        if not target.exists():
            bad_links.append(link)
    check(not bad_links, "all %d relative links resolve" % len(links))
    for link in bad_links:
        print("        missing:", link)

    # 5 -- corpus directories
    print()
    print("[5] corpus directories")
    for rel in ("corpus/prelim", "corpus/finals", "corpus/finals_extra", "corpus/finals_recovered"):
        folder = REPO_ROOT / rel
        count = len(list(folder.glob("*"))) if folder.is_dir() else 0
        check(count > 0, "%s (%d files)" % (rel, count))
        notes.append("%s: %d files" % (rel, count))

    # 6 -- no machine paths
    print()
    print("[6] machine-specific absolute paths")
    offenders = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXT:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if str(path.relative_to(REPO_ROOT)).replace("\\", "/") in SKIP_FILES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if FORBIDDEN.search(text):
            offenders.append(str(path.relative_to(REPO_ROOT)))
    check(not offenders, "no hard-coded machine paths in tracked text files")
    for item in offenders[:10]:
        print("        offender:", item)

    # summary
    print()
    print("-" * 62)
    for line in notes:
        print("  info:", line)
    if failures:
        print("RESULT: FAIL (%d check(s) failed)" % len(failures))
        return 1
    print("RESULT: OK — all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
