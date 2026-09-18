
# -*- coding: utf-8 -*-
import json, sys, statistics as st, collections
sys.stdout.reconfigure(encoding='utf-8')
rows=json.load(open(r'./archive/work/prob_metrics_curated.json',encoding='utf-8'))
comp=[r for r in rows if not (int(r['year']) in (2010,2011) and str(r['n']) not in ('5','6') and int(r['year'])==2010)
      and not (int(r['year'])==2011 and str(r['n']) not in ('1','2'))]
print('n comp',len(comp))
def m(rs): return round(st.mean([r['chars'] for r in rs])), round(st.median([r['chars'] for r in rs]))
for y in range(2010,2027):
    for k in ['I','T','Q']:
        rs=[r for r in comp if int(r['year'])==y and r['kind']==k]
        if rs:
            a,b=m(rs); print(y,k,'n=%d'%len(rs),'mean',a,'median',b,'max',max(r['chars'] for r in rs))
print()
r3=[r for r in comp if 2016<=int(r['year'])<=2018]
for k in ['I','T']:
    rs=[r for r in r3 if r['kind']==k]; a,b=m(rs)
    print('2016-2018',k,'n',len(rs),'mean',a,'median',b,'max',max(r['chars'] for r in rs))
a,b=m(r3); print('2016-2018 all applied n',len(r3),'mean',a,'median',b,'max',max(r['chars'] for r in r3))
print()
# subpart share by era (using robust "has any labelled subpart")
def has_sub(r): return r['subparts']>0
for name,rng in [('2010-2014',range(2010,2015)),('2015-2019',range(2015,2020)),('2020-2026',range(2020,2027))]:
    rs=[r for r in comp if int(r['year']) in rng]
    print(name,'n',len(rs),'share with >=1 subpart marker',round(sum(has_sub(r) for r in rs)/len(rs),3))
# verbs per era (raw counts)
VER=['prove','show','derive','compute','find','determine','explain','describe','construct','verify','estimate','solve','design','analyze','justify']
for name,rng in [('2010-2014',range(2010,2015)),('2015-2019',range(2015,2020)),('2020-2026',range(2020,2027))]:
    rs=[r for r in comp if int(r['year']) in rng]
    c=collections.Counter()
    for r in rs: c.update(r['verbs'])
    print(name, dict(c.most_common(10)))
