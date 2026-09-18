
# -*- coding: utf-8 -*-
"""Representative problems per tag: prefer 2022-2026, then highest difficulty."""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\data"
en = json.load(open(B + r"\problems_enriched.json", encoding='utf-8'))
OUT = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\tag_problems.txt"

# map file -> readable paper label
bytag = collections.defaultdict(list)
for p in en:
    y = int(p['year'])
    for t in p.get('tags', []):
        _h = p.get('head') or p.get('text') or ''
        _h = ' '.join(_h.split())
        bytag[t].append({'year':y,'subject':p.get('subject','?'),
                         'file':p.get('file') or p.get('paper') or '?','n':p.get('n','?'),
                         'head':_h,'diff':p.get('difficulty_proxy',0)})

buf = []
for t, ps in sorted(bytag.items(), key=lambda kv: -len(kv[1])):
    recent = [p for p in ps if p['year'] >= 2022]
    older  = [p for p in ps if p['year'] < 2022]
    recent.sort(key=lambda p: (-p['year'], -p['diff']))
    older.sort(key=lambda p: (-p['year'], -p['diff']))
    sel = recent[:6] + older[:4]
    buf.append("\n" + "="*90)
    buf.append(f"## {t}  (n={len(ps)})")
    for p in sel:
        buf.append(f"  [{p['year']} {p['subject']} Q{p['n']}] diff={p['diff']} file={p['file']}")
        buf.append(f"      {p['head'][:260]}")
open(OUT,'w',encoding='utf-8').write("\n".join(buf))
print("wrote", OUT, len(buf))
