
import json, io, sys, collections
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"E:\deepseek_exclusive\math\book_research_clean_restart"

def peek(path, n=2):
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("="*70)
    print(path)
    print("top type:", type(d).__name__)
    if isinstance(d, dict):
        print("top keys:", list(d.keys())[:20])
        for k in list(d.keys())[:3]:
            v = d[k]
            print("  key", k, "->", type(v).__name__, (len(v) if hasattr(v,'__len__') else ''))
    if isinstance(d, list):
        print("len:", len(d))
        for i in range(min(n, len(d))):
            print("--- item", i, "---")
            print(json.dumps(d[i], ensure_ascii=False)[:2000])
    return d

mc = peek(BASE + r"\data\master_catalog.json")
if isinstance(mc, dict):
    for k in list(mc.keys()):
        v = mc[k]
        if isinstance(v, list) and v and isinstance(v[0], dict):
            print("\n### LIST", k, len(v))
            print(json.dumps(v[0], ensure_ascii=False, indent=1)[:2500])
