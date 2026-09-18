# -*- coding: utf-8 -*-
import json, re
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
p = json.load(open(base+'problems_full.json', encoding='utf-8'))
def g(y,paper,n):
    for x in p:
        if x['subject']=='Geometry & Topology' and x['year']==y and x['paper']==paper and x['n']==n: return x['text']
a = g('2011','2011_3_GeomTop_Individual_2011',4)
b = g('2014','2014_geometry2014_individual',3)
na=' '.join(a.split()); nb=' '.join(b.split())
print('2011I4 == 2014I3 verbatim?', na==nb)
print('len A', len(na), 'len B', len(nb))
c = g('2011','2011_3_GeomTop_Individual_2011',2)
d = g('2013','2013_geometry2013_individual',2)
nc=' '.join(c.split()); nd=' '.join(d.split())
print('2011I2 vs 2013I2:', nc==nd)
print(' A:', nc)
print(' B:', nd)
print()
# sentence-level long-sentence duplicate check across ALL geometry
def sents(t):
    t=re.sub(r'\s+',' ',t)
    return [s.strip() for s in re.split(r'(?<=[.;:])\s+', t) if len(s.split())>=12]
from collections import defaultdict
idx=defaultdict(list)
geo=[x for x in p if x['subject']=='Geometry & Topology']
for x in geo:
    for s in sents(x['text']):
        idx[s].append((x['year'],x['paper'],x['n']))
dup=[(k,v) for k,v in idx.items() if len({(a,b) for a,b,_ in v})>1]
print('geometry long-sentence duplicates (>1 distinct paper): count =', len(dup))
for k,v in dup[:40]:
    print('  ', sorted(set((a,c) for a,b,c in v)), '::', k[:150])
