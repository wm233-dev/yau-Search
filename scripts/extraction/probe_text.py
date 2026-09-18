# -*- coding: utf-8 -*-
"""Probe text-layer quality of every Yau past-paper PDF."""
import os, sys, json, io
import fitz

BASE = r"sources/prelim"
OUT = r".\yau_probe.tsv"

rows = []
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        if not fn.lower().endswith(".pdf") or fn.startswith("._"):
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, BASE)
        try:
            d = fitz.open(p)
            pages = d.page_count
            total = 0
            per_page = []
            sample = ""
            for i in range(pages):
                t = d[i].get_text() or ""
                per_page.append(len(t))
                total += len(t)
                if not sample and len(t.strip()) > 40:
                    sample = " ".join(t.split())[:90]
            d.close()
            rows.append({
                "rel": rel, "pages": pages, "chars": total,
                "avg": round(total / max(pages, 1), 1),
                "sample": sample,
            })
        except Exception as e:
            rows.append({"rel": rel, "pages": -1, "chars": -1, "avg": -1, "sample": "ERR " + str(e)[:80]})

with io.open(OUT, "w", encoding="utf-8") as f:
    f.write("rel\tpages\tchars\tavg_per_page\tsample\n")
    for r in rows:
        f.write("%s\t%d\t%d\t%s\t%s\n" % (r["rel"], r["pages"], r["chars"], r["avg"], r["sample"]))

n_text = sum(1 for r in rows if r["avg"] >= 200)
n_thin = sum(1 for r in rows if 0 <= r["avg"] < 200)
n_err = sum(1 for r in rows if r["avg"] < 0)
print("FILES", len(rows), "TEXT_LAYER_OK", n_text, "THIN_OR_SCANNED", n_thin, "ERRORS", n_err)
print("--- thin/scanned list (first 40) ---")
for r in rows:
    if 0 <= r["avg"] < 200:
        print("THIN", r["rel"], r["pages"], r["chars"])
print("--- errors ---")
for r in rows:
    if r["avg"] < 0:
        print("ERR", r["rel"], r["sample"])
print("WROTE", OUT)
