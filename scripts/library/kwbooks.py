
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
recs = json.load(open(r".\scripts\lib_index.json", encoding='utf-8'))
def blob(r): return " | ".join(str(r.get(k) or '') for k in ('title','fn','author','series'))
def sc(r): return (1 if r['text_layer'] else 0)*10000 + r['n_toc']
KW = sys.argv[1]
seen = {}
for r in recs:
    if re.search(KW, blob(r), re.I):
        t = re.sub(r'\s+','', r['title'])
        if t not in seen or sc(r) > sc(seen[t]): seen[t] = r
lst = sorted(seen.values(), key=lambda r: -sc(r))
print(f"### {KW}  -> {len(lst)}")
for r in lst[:30]:
    print(f"  [{r['id']}] {r['title']} | {r['author']} | {r['series']} | {r['publisher']} {r['year']} | toc={r['n_toc']} tl={r['text_layer']} pg={r['pages']}")
    print(f"      fn={r['fn']}")
