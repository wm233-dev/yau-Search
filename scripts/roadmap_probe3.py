
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"E:\deepseek_exclusive\math\book_research_clean_restart"
p = BASE + r"\raw\library_toc_full.json"
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
print("top type:", type(d).__name__)
if isinstance(d, dict):
    print("keys:", list(d.keys())[:20])
    for k in list(d.keys()):
        v = d[k]
        print(" ", k, type(v).__name__, (len(v) if hasattr(v,'__len__') else v if not isinstance(v,(dict,list)) else ''))
    files = d.get('files')
    if files:
        print("n files", len(files))
        cnt=0
        for it in files:
            if it.get('n_toc',0) > 5:
                print(json.dumps(it, ensure_ascii=False)[:3000])
                cnt+=1
                if cnt>=3: break
