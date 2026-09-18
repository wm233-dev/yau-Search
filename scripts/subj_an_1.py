
import json, re, collections, os
BASE = r"E:\deepseek_exclusive\math\.tmp\burn2026"
pe = json.load(open(os.path.join(BASE,"data","problems_enriched.json"), encoding="utf-8"))
subs = collections.Counter(p["subject"] for p in pe)
print("SUBJECTS:", json.dumps(subs, ensure_ascii=False))
an = [p for p in pe if p["subject"]=="Analysis & PDE"]
print("ANALYSIS problems:", len(an))
byyear = collections.Counter(p["year"] for p in an)
print("BY YEAR:", json.dumps(dict(sorted(byyear.items())), ensure_ascii=False))
tags = collections.Counter()
tbyyear = collections.defaultdict(set)
for p in an:
    for t in p["tags"]:
        tags[t]+=1
        tbyyear[t].add(p["year"])
print("\nTAG FREQ (count, years):")
for t,c in tags.most_common():
    print(f"  {t}\t{c}\t{','.join(sorted(tbyyear[t]))}")
