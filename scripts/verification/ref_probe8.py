
import json, re
p = r".\data\problems_full.json"
recs = json.load(open(p, encoding="utf-8"))
ap = [r for r in recs if r["subject"] == "Analysis & PDE"]
for r in ap:
    if r["year"]=="2020" and r["n"] in (3,4):
        print("###", r["year"], r["kind"], r["n"], "len", len(r["text"]))
        print(r["text"])
        print()
for r in ap:
    if r["year"]=="2012" and r["kind"]=="team":
        print("###2012 team", r["n"], "len",len(r["text"]))
        print(r["text"][:800]); print()
