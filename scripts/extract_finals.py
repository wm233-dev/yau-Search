# -*- coding: utf-8 -*-
"""Extract the Yau FINALS corpus (2012-2025, F: drive) into .tmp/burn2026/txt_finals."""
import os, io, re, json
import fitz

BASE = r"F:\丘成桐大学生数学竞赛历年总决赛真题"
OUT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt_finals"
os.makedirs(OUT, exist_ok=True)
manifest = []
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        if not fn.lower().endswith(".pdf"): continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, BASE)
        try:
            d = fitz.open(p)
            parts, total = [], 0
            for i in range(d.page_count):
                t = d[i].get_text() or ""
                total += len(t)
                parts.append("\n=== page %d ===\n" % (i + 1)); parts.append(t)
            d.close()
            safe = re.sub(r"[^0-9A-Za-z]+", "_", rel[:-4]).strip("_")
            with io.open(os.path.join(OUT, safe + ".txt"), "w", encoding="utf-8") as f:
                f.write("".join(parts))
            manifest.append({"rel": rel, "txt": safe + ".txt", "pages": len(parts) // 2, "chars": total})
        except Exception as e:
            manifest.append({"rel": rel, "txt": None, "pages": -1, "chars": -1, "err": str(e)[:120]})
json.dump(manifest, io.open(r"E:\deepseek_exclusive\math\.tmp\burn2026\data\finals_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = [m for m in manifest if m["txt"]]
print("FINALS files", len(manifest), "extracted", len(ok), "chars", sum(m["chars"] for m in ok))
import collections
c = collections.Counter(m["rel"].split(os.sep)[0] for m in manifest)
for k, v in c.items(): print("SUBJ", k, v)
thin = [m for m in ok if m["chars"] < 400]
print("THIN(<400 chars):", len(thin))
for m in thin[:10]: print("  THIN", m["rel"], m["pages"], m["chars"])
err = [m for m in manifest if m["txt"] is None]
for m in err[:10]: print("  ERR", m["rel"], m.get("err"))
