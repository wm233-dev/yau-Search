
import json, os, statistics, collections
S=json.load(open(r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\finals_app_phys_stats.json',encoding='utf-8'))
P=S["problems"]
def subj(p): return "ACM" if "Applied" in p.split(os.sep)[0] else "MP"
for key,fn in [("ALL",lambda x:True),
               ("ACM",lambda x:subj(x["paper"])=="ACM"),
               ("MP",lambda x:subj(x["paper"])=="MP")]:
    v=[x for x in P if fn(x)]
    print(key,"n=",len(v),"mean=%.1f"%statistics.mean([x["chars"] for x in v]),
          "median=%.0f"%statistics.median([x["chars"] for x in v]),
          "sub=%.2f"%statistics.mean([x["subparts"] for x in v]),
          "chars=%d"%sum(x["chars"] for x in v))
for k in ["Individual","Overall","Team"]:
    v=[x for x in P if x["kind"]==k]
    print(k,"n=",len(v),"median=%.0f"%statistics.median([x["chars"] for x in v]))
