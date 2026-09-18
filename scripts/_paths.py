# -*- coding: utf-8 -*-
"""Shared path helpers for yau-Search scripts.

Every script should locate the repository through this module instead of
hard-coding an absolute path, so the project runs from any clone location::

    from _paths import REPO_ROOT, DATA, load_problems

Run scripts from the repository root, or add this directory to sys.path.
"""
from pathlib import Path
import json

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA = REPO_ROOT / "data"
REPORTS = REPO_ROOT / "reports"
DOCS = REPO_ROOT / "docs"
ARCHIVE = REPO_ROOT / "archive"
CORPUS = REPO_ROOT / "corpus"
CORPUS_PRELIM = CORPUS / "prelim"
CORPUS_FINALS = CORPUS / "finals"
CORPUS_FINALS_EXTRA = CORPUS / "finals_extra"
CORPUS_FINALS_RECOVERED = CORPUS / "finals_recovered"

# Optional: original contest PDFs are NOT part of this repository (copyright).
# If you have your own copy, put it here (git-ignored) to re-run the extraction.
SOURCES = REPO_ROOT / "sources"

PROBLEMS_JSON = DATA / "problems_full.json"
ENRICHED_JSON = DATA / "problems_enriched.json"
SYLLABUS_JSON = DATA / "syllabus_coverage.json"
INDEX_HTML = REPO_ROOT / "yau_index.html"


def read_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_problems():
    """Return the canonical problem list (757 problems, 2010-2026)."""
    return read_json(PROBLEMS_JSON)


def ensure_dirs(*paths):
    for item in paths:
        Path(item).mkdir(parents=True, exist_ok=True)
