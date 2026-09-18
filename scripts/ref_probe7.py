
import json, re
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
recs = json.load(open(p, encoding="utf-8"))
ap = [r for r in recs if r["subject"] == "Analysis & PDE"]
def show(y,k=None,n=None):
    for r in ap:
        if r["year"]!=y: continue
        if k and r["kind"]!=k: continue
        if n and r["n"]!=n: continue
        print("---", r["year"], r["kind"], r["n"])
        print("   ", r["text"][:420].replace("\n"," | "))
print("### 2012 individual 1"); show("2012","individual",1)
print("### 2017 individual 6"); show("2017","individual",6)
print("### 2017 individual 2"); show("2017","individual",2)
print("### 2014 individual 3"); show("2014","individual",3)
print("### 2014 individual 5"); show("2014","individual",5)
print("### 2014 team 3"); show("2014","team",3)
print("### 2015 team 1"); show("2015","team",1)
print("### 2016 team 3"); show("2016","team",3)
print("### 2015 individual 5"); show("2015","individual",5)
print("### 2015 team 5"); show("2015","team",5)
print("### 2024 individual (all)"); show("2024","individual")
print("### 2010 individual 1"); show("2010","individual",1)
print("### 2010 individual 2"); show("2010","individual",2)
print("### 2020 individual 3"); show("2020","individual",3)
print("### 2020 individual 4"); show("2020","individual",4)
