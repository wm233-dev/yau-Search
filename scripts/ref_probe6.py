
import json, re
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
recs = json.load(open(p, encoding="utf-8"))
ap = [r for r in recs if r["subject"] == "Analysis & PDE"]
def show(y,k=None,n=None,pat=None):
    for r in ap:
        if r["year"]!=y: continue
        if k and r["kind"]!=k: continue
        if n and r["n"]!=n: continue
        if pat and not re.search(pat, r["text"], re.I): continue
        print("---", r["year"], r["kind"], r["n"], r["paper"])
        print(r["text"][:600].replace("\n"," | "))
print("### 2021 individual")
show("2021","individual")
print()
print("### 2022 individual")
show("2022","individual")
print()
print("### 2026 individual")
show("2026","individual")
print()
print("### 2019 individual")
show("2019","individual")
print()
print("### 2011 team")
show("2011","team")
print()
print("### 2016 individual 4")
show("2016","individual",4)
print()
print("### 2013 team (Gauss-Lucas?)")
show("2013","team")
