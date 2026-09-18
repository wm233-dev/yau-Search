
import json, io, sys
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
d = json.load(open(p, encoding="utf-8"))
print(type(d))
if isinstance(d, dict):
    print(list(d.keys())[:20])
    recs = d.get("problems") or d.get("records") or []
else:
    recs = d
print("n =", len(recs))
print(json.dumps(recs[0], ensure_ascii=False)[:800])
