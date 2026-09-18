# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = './data/'
enr = json.load(open(base + 'problems_enriched.json', encoding='utf-8'))
papers = json.load(open(base + 'papers.json', encoding='utf-8'))['papers']

print('### PHYSICS problems (subject=Mathematical Physics)')
for p in enr:
    if p['subject'] == 'Mathematical Physics':
        print(json.dumps({k: p[k] for k in ['year','file','n','chars','words','subparts','symbols','tags','verbs','difficulty_proxy']}, ensure_ascii=False))

print()
print('### Physics-tagged problems in OTHER subjects')
for p in enr:
    if p['subject'] != 'Mathematical Physics' and any(t in ('数学物理/量子','经典场论/相对论','统计物理','辛几何/力学') for t in p.get('tags', [])):
        print(p['year'], '|', p['subject'], '| Q'+str(p['n']), '|', p.get('tags'), '|', p.get('head','')[:150].replace('\n',' '))

print()
print('### Papers by year: kind counts')
from collections import defaultdict
d = defaultdict(lambda: defaultdict(int))
for pp in papers:
    d[pp['year']][pp['kind']] += 1
for y in sorted(d):
    print(y, dict(d[y]))
