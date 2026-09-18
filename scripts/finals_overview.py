# -*- coding: utf-8 -*-
"""Structure overview of the Yau FINALS corpus (from filenames) + text-layer quality."""
import os, io, re, json, collections
ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
man = json.load(io.open(os.path.join(ROOT, "data", "finals_manifest.json"), encoding="utf-8"))
rows = []
for m in man:
    rel = m["rel"]
    parts = rel.split(os.sep)
    subj = parts[0]
    kind = parts[1] if len(parts) > 2 else "(root)"
    fn = parts[-1]
    ym = re.search(r"(20\d\d)", fn)
    rows.append({"subj": subj, "kind": kind, "year": ym.group(1) if ym else "n/a",
                 "chars": m["chars"], "pages": m["pages"], "file": fn})
print("BY KIND:", dict(collections.Counter(r["kind"] for r in rows)))
print("BY SUBJ:", dict(collections.Counter(r["subj"][:12] for r in rows)))
tab = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    tab[r["subj"][:10]][r["kind"]] += 1
for k in sorted(tab): print("  ", k, dict(tab[k]))
yrs = collections.Counter(r["year"] for r in rows if r["kind"] != "(root)")
print("BY YEAR:", dict(sorted(yrs.items())))
real = [r for r in rows if r["chars"] >= 800 and r["kind"] != "(root)"]
print("REAL_TEXT_FILES(>=800 chars, excl Overall):", len(real), "chars", sum(r["chars"] for r in real))
scanned = [r["file"] for r in rows if r["chars"] < 800 and r["kind"] != "(root)"]
print("LOW_TEXT_FILES:", len(scanned))
for s in scanned[:25]: print("   low:", s)
# per year-subject matrix for individual papers
mat = collections.defaultdict(set)
for r in real:
    if r["kind"].lower().startswith("individual"):
        mat[r["subj"][:10]].add(r["year"])
for k in sorted(mat): print("INDIV YEARS", k, sorted(mat[k]))
json.dump(rows, io.open(os.path.join(ROOT, "data", "finals_index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
