
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\data"
en = json.load(open(B + r"\problems_enriched.json", encoding='utf-8'))
full = json.load(open(B + r"\problems_full.json", encoding='utf-8'))
print("enriched type", type(en).__name__, (list(en.keys())[:10] if isinstance(en,dict) else len(en)))
print("full type", type(full).__name__, (list(full.keys())[:10] if isinstance(full,dict) else len(full)))
def sample(d, name):
    if isinstance(d, dict):
        for k in list(d.keys())[:5]:
            print(" ", name, k, type(d[k]).__name__, (len(d[k]) if hasattr(d[k],'__len__') else d[k] if not isinstance(d[k],(list,dict)) else ''))
        # find list
        for k in d:
            if isinstance(d[k], list) and d[k] and isinstance(d[k][0], dict):
                print("### ", name, k, len(d[k]))
                print(json.dumps(d[k][0], ensure_ascii=False, indent=1)[:2500])
                return d[k]
    elif isinstance(d, list):
        print("###", name, len(d))
        print(json.dumps(d[0], ensure_ascii=False, indent=1)[:2500])
        return d
    return None
a = sample(en, "enriched")
b = sample(full, "full")
