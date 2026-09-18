
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"E:\deepseek_exclusive\math\book_research_clean_restart"
p = BASE + r"\raw\library_toc.json"
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
print("top type:", type(d).__name__)
if isinstance(d, dict):
    print("keys:", list(d.keys())[:20])
    for k in list(d.keys())[:5]:
        v = d[k]
        print(" ", k, type(v).__name__, (len(v) if hasattr(v,'__len__') else ''))
    recs = d.get('records') or d.get('tocs') or None
    if recs is None:
        # maybe keyed by id
        for k in list(d.keys())[:3]:
            print("---", k, "---")
            print(json.dumps(d[k], ensure_ascii=False)[:3000])
    else:
        print("recs len", len(recs))
        print(json.dumps(recs[0], ensure_ascii=False)[:3000])
elif isinstance(d, list):
    print("len", len(d))
    print(json.dumps(d[0], ensure_ascii=False)[:3000])
