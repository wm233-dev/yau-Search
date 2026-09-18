
import json, collections
P=json.load(open(r".\data\problems_enriched.json",encoding="utf-8"))
c=collections.Counter((p["year"],p["subject"]) for p in P)
for y in sorted(set(int(k[0]) for k in c)):
    tot=sum(v for k,v in c.items() if int(k[0])==y)
    print(y, tot, {k[1]:v for k,v in sorted(c.items()) if int(k[0])==y})
print("\nFILES for 2016 team:")
print(sorted(set(p["file"] for p in P if "2016_2016_team" in p["file"])))
for p in P:
    if "2016_2016_team" in p["file"]:
        print("  ", p["subject"], p["n"], p["chars"], "|", p["head"][:70])
