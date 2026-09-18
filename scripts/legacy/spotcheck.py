# -*- coding: utf-8 -*-
"""Independent spot-check of three headline claims made by sub-reports."""
import os, io, re, json, difflib
DATA = r".\data"
P = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
def get(year, subj_kw, n):
    for p in P:
        if p["year"] == year and subj_kw.lower() in p["subject"].lower() and p["n"] == n:
            return p
    return None

print("=== claim A: 2022 analysis Q4 == 2026 analysis Q4 ? ===")
a, b = get("2022", "Analysis", 4), get("2026", "Analysis", 4)
for x in (a, b):
    print(" ", x["year"], x["subject"], "Q%d" % x["n"], x["chars"], "|", " ".join(x["text"].split())[:220])
if a and b:
    r = difflib.SequenceMatcher(None, a["text"], b["text"]).ratio()
    print("  char-level ratio = %.3f" % r)

print("\n=== claim B: 2016 team Dirichlet heat kernel vs 2026 periodic heat kernel ===")
c = get("2016", "Analysis", 6); d = get("2026", "Analysis", 5)
for x in (c, d):
    if x: print(" ", x["year"], x["subject"], "Q%d" % x["n"], x["chars"], "|", " ".join(x["text"].split())[:200])

print("\n=== claim C: 2013 individual applied Q6 == 2013 team applied Q6 ? ===")
e = [p for p in P if p["year"] == "2013" and p["n"] == 6 and "Applied" in p["subject"]]
for x in e: print(" ", x["paper"], x["kind"], x["chars"], "|", " ".join(x["text"].split())[:150])

print("\n=== claim D: does 'Cauchy' really never appear in Analysis papers? ===")
ana = [p for p in P if p["subject"].startswith("Analysis")]
for t in ["Cauchy", "Schwarz", "residue", "holomorphic", "Sobolev", "Fourier"]:
    hit = sum(1 for p in ana if re.search(t, p["text"], re.I))
    print("  %-12s appears in %d / %d analysis problems" % (t, hit, len(ana)))

print("\n=== claim E: verb 'derive' count in analysis ===")
n = sum(1 for p in ana if re.search(r"\bderive\b", p["text"], re.I))
print("  derive in %d analysis problems" % n)

print("\n=== claim F: 2025 probability lowest with 4 problems? ===")
import collections
cnt = collections.Counter((p["year"], p["subject"][:14]) for p in P)
for y in ["2023", "2024", "2025", "2026"]:
    row = {k[1]: v for k, v in cnt.items() if k[0] == y}
    print(" ", y, row)
