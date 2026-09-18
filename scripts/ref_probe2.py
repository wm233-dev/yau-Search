
import json
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
recs = json.load(open(p, encoding="utf-8"))
ap = [r for r in recs if r["subject"] == "Analysis & PDE"]
print("Analysis & PDE count:", len(ap))
from collections import Counter
print(Counter(r["year"] for r in ap))

want = [("2011","individual",2),("2014","team",2),("2015","individual",2),("2010","individual",6),
        ("2013","individual",2),("2017","team",5),("2020","individual",5),("2018","individual",6),
        ("2025","individual",2),("2026","individual",1)]
for y,k,n in want:
    hits = [r for r in ap if r["year"]==y and r["kind"]==k and r["n"]==n]
    print("="*80)
    print(y,k,n,"hits:",len(hits))
    for h in hits:
        print("  paper:",h["paper"],"chars:",h["chars"])
        print("  TEXT:",repr(h["text"]))
