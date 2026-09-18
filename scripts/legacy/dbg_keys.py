
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
B = r".\data"
en = json.load(open(B + r"\problems_enriched.json", encoding='utf-8'))
c = collections.Counter()
for p in en:
    c[tuple(sorted(p.keys()))] += 1
for k,v in c.most_common():
    print(v, k)
