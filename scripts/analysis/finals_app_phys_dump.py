# -*- coding: utf-8 -*-
"""Dump txt content for finals records in scope (Applied | Mathematical_Physics)."""
import json, os, re, sys, io

BASE = r"."
MAN = os.path.join(BASE, "data", "finals_manifest.json")
TXT = os.path.join(BASE, "txt_finals")

def load():
    m = json.load(open(MAN, encoding="utf-8"))
    out = []
    for x in m:
        top = x["rel"].split(os.sep)[0]
        if "Applied" not in top and "Mathematical_Physics" not in top:
            continue
        p = os.path.join(TXT, x["txt"]) if x.get("txt") else None
        t = ""
        if p and os.path.exists(p):
            t = open(p, encoding="utf-8", errors="replace").read()
        out.append(dict(rel=x["rel"], top=top, txt=x.get("txt"), chars=x["chars"],
                        pages=x["pages"], text=t))
    out.sort(key=lambda r: (r["top"], r["rel"]))
    return out

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "list"
    recs = load()
    if mode == "list":
        for r in recs:
            kind = r["rel"].split(os.sep)[1] if len(r["rel"].split(os.sep)) > 2 else "-"
            print("%-46s | %-10s | chars=%-6d pg=%-3d | %s" % (
                r["rel"].split(os.sep)[-1][:46], kind, r["chars"], r["pages"], r["txt"]))
    elif mode == "dump":
        pat = sys.argv[2]
        for r in recs:
            if not re.search(pat, r["rel"], re.I):
                continue
            print("\n" + "#" * 90)
            print("### FILE:", r["rel"], "chars=", r["chars"], "pages=", r["pages"])
            print("#" * 90)
            print(r["text"])
