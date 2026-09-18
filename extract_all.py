# -*- coding: utf-8 -*-
"""Dump every Yau past paper to plain text under .tmp/burn2026/txt/, plus a manifest."""
import os, io, json, re
import fitz

BASE = r"E:\deepseek_exclusive\math\.tmp\yau\2010-2026历年笔试真题"
OUTDIR = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
os.makedirs(OUTDIR, exist_ok=True)

manifest = []
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        if not fn.lower().endswith(".pdf") or fn.startswith("._"):
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, BASE)
        year_dir = rel.split(os.sep)[0]
        safe = re.sub(r"[^0-9A-Za-z]+", "_", rel[:-4]).strip("_")
        out = os.path.join(OUTDIR, safe + ".txt")
        d = fitz.open(p)
        parts = []
        for i in range(d.page_count):
            parts.append("\n=== page %d ===\n" % (i + 1))
            parts.append(d[i].get_text() or "")
        meta = d.metadata or {}
        d.close()
        txt = "".join(parts)
        with io.open(out, "w", encoding="utf-8") as f:
            f.write(txt)
        manifest.append({
            "rel": rel, "year_dir": year_dir, "txt": os.path.basename(out),
            "pages": txt.count("=== page "), "chars": len(txt),
            "title": (meta.get("title") or "").strip()[:120],
        })

with io.open(r"E:\deepseek_exclusive\math\.tmp\burn2026\manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

print("EXTRACTED", len(manifest), "files ->", OUTDIR)
print("TOTAL_CHARS", sum(m["chars"] for m in manifest))
by_year = {}
for m in manifest:
    by_year.setdefault(m["year_dir"], [0, 0])
    by_year[m["year_dir"]][0] += 1
    by_year[m["year_dir"]][1] += m["chars"]
for k in sorted(by_year):
    print("YEAR", k, "files", by_year[k][0], "chars", by_year[k][1])
