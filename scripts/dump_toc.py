
# -*- coding: utf-8 -*-
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
recs = {r['id']: r for r in json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\lib_index.json", encoding='utf-8'))}
IDS = sys.argv[1].split(",")
def good(l):
    l = l.strip()
    if re.fullmatch(r'[0-9]{3,}', l): return False
    if re.fullmatch(r'0?[0-9]{4,}', l): return False
    if len(l) <= 2: return False
    if re.fullmatch(r'(cov|bok|fow|leg|ind|att)\d+', l, re.I): return False
    if 'www.' in l or 'freekaoyan' in l: return False
    return True
for i in IDS:
    r = recs.get(i)
    if not r: print(f"!! {i} NOT FOUND"); continue
    toc = [l for l in r['toc'] if good(l)]
    print("\n" + "#"*90)
    print(f"[{r['id']}] {r['title']} | {r['author']} | {r['publisher']} {r['year']} | n_toc={r['n_toc']} | tl={r['text_layer']} | pages={r['pages']}")
    print(f"    fn={r['fn']}")
    for l in toc[:70]:
        print("   ", l)
