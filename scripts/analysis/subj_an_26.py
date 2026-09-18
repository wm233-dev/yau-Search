
import json, collections
P=json.load(open(r".\data\problems_enriched.json",encoding="utf-8"))
M=[p for p in P if p["subject"]=="Mixed/Team(multi-subject)"]
print(len(M))
for p in sorted(M, key=lambda x:(x["year"],x["n"])):
    print(f"  {p['year']} {p['file'][:34]:34s} n={p['n']} chars={p['chars']:5d} tags={p['tags']} | {p['head'][:80]}")
