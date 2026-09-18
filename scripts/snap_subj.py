
import json, sys, collections, os, datetime
sys.stdout.reconfigure(encoding='utf-8')
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\data"
for fn in ["problems_full.json","problems_enriched.json"]:
    p = os.path.join(B, fn)
    st = os.stat(p)
    d = json.load(open(p, encoding='utf-8'))
    print(fn, "n=", len(d), "mtime=", datetime.datetime.fromtimestamp(st.st_mtime).isoformat())
    c = collections.Counter(x.get('subject','?') for x in d)
    for k,v in c.most_common(): print("   ", k, v)
