
# -*- coding: utf-8 -*-
"""Recompute per-tag statistics from problems_enriched.json -> tag_stats.json"""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
B = r".\data"
en = json.load(open(B + r"\problems_enriched.json", encoding='utf-8'))
out = r".\scripts\tag_stats.json"

tags = collections.defaultdict(lambda: {'n':0,'years':collections.Counter(),'probs':[],'subjects':collections.Counter()})
for p in en:
    y = int(p['year'])
    for t in p.get('tags', []):
        d = tags[t]
        d['n'] += 1
        d['years'][y] += 1
        d['subjects'][p['subject']] += 1
        _f = p.get('file') or p.get('paper') or '?'
        _h = p.get('head') or p.get('text') or ''
        _h = ' '.join(_h.split())[:180]
        d['probs'].append({'year':y,'subject':p.get('subject','?'),'file':_f,'n':p.get('n','?'),'head':_h,'diff':p.get('difficulty_proxy',0)})

years_all = sorted({int(p['year']) for p in en})
recent = [y for y in years_all if y >= 2022]
prev   = [y for y in years_all if 2016 <= y <= 2021]
old    = [y for y in years_all if y <= 2015]

rows = []
for t, d in tags.items():
    rc = sum(d['years'][y] for y in recent)
    pc = sum(d['years'][y] for y in prev)
    oc = sum(d['years'][y] for y in old)
    nyr = len(d['years'])
    # trend: recent rate per year over available years vs prev
    r_rate = rc / len(recent)
    p_rate = pc / len(prev)
    if p_rate == 0:
        trend = '↑' if rc > 0 else '→'
    else:
        ratio = r_rate / p_rate
        trend = '↑' if ratio >= 1.25 else ('↓' if ratio <= 0.75 else '→')
    rows.append({'tag':t,'n':d['n'],'nyears':nyr,'years':dict(sorted(d['years'].items())),
                 'old':oc,'mid':pc,'recent':rc,'trend':trend,'subjects':dict(d['subjects']),
                 'probs':d['probs']})
rows.sort(key=lambda r: -r['n'])
json.dump({'years_all':years_all,'recent':recent,'prev':prev,'old':old,'rows':rows},
          open(out,'w',encoding='utf-8'), ensure_ascii=False, indent=1)

print(f"tags total: {len(rows)}  problems: {len(en)}  years: {years_all}")
print(f"{'rank':<5}{'tag':<22}{'n':>5}{'yrs':>5}{'<=2015':>8}{'16-21':>7}{'22-26':>7}  trend")
for i,r in enumerate(rows,1):
    print(f"{i:<5}{r['tag']:<22}{r['n']:>5}{r['nyears']:>5}{r['old']:>8}{r['mid']:>7}{r['recent']:>7}  {r['trend']}")
