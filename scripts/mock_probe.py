# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
d = json.load(open(p, encoding="utf-8"))
years = ["2020","2021","2022","2023","2024","2025","2026"]
out = []
for subj in ["Algebra & Number Theory", "Analysis & PDE"]:
    out.append("=" * 90)
    out.append("SUBJECT: " + subj)
    for x in d:
        if x["year"] in years and x["subject"] == subj:
            out.append("### %s | %s | n=%s" % (x["year"], x["paper"], x["n"]))
            out.append(x["text"].strip())
            out.append("")
open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\modern_dump.txt", "w", encoding="utf-8").write("\n".join(out))
print("written", sum(len(o) for o in out))
