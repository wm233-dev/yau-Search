
# -*- coding: utf-8 -*-
import json, sys, collections, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
rows=json.load(open(r'.tmp/burn2026/work/prob_metrics_curated.json',encoding='utf-8'))
# computational subset = my curated inventory
keep = {
 2010:['5','6'], 2011:['1','2'], 2012:None, 2013:None, 2014:None, 2015:None,
 2016:None, 2017:None, 2018:None, 2019:None, 2020:None, 2021:None, 2022:None,
 2023:None, 2024:None, 2025:None, 2026:None}
comp=[]
for r in rows:
    y=int(r['year'])
    if y in (2010,2011):
        if str(r['n']) in keep[y]: comp.append(r)
    else:
        comp.append(r)
print('computational problems measured:', len(comp))
def agg(rs):
    ch=[r['chars'] for r in rs]; su=[r['subparts'] for r in rs]
    vc=collections.Counter()
    for r in rs: vc.update(r['verbs'])
    tot=sum(vc.values())
    return dict(n=len(rs), chars_mean=round(st.mean(ch)), chars_med=round(st.median(ch)),
                chars_max=max(ch), sub_mean=round(st.mean(su),2), sub_zero=sum(1 for x in su if x==0),
                verbs={k:round(v/tot,3) for k,v in vc.most_common()}, verb_total=tot)
byyear=collections.defaultdict(list)
for r in comp: byyear[int(r['year'])].append(r)
print('\nYEAR | n | mean chars | median | max | mean subparts | #0-subpart | verb mix(top5,share)')
for y in sorted(byyear):
    a=agg(byyear[y])
    top=', '.join(f'{k}:{v}' for k,v in list(a['verbs'].items())[:5])
    print(f"{y} | {a['n']} | {a['chars_mean']} | {a['chars_med']} | {a['chars_max']} | {a['sub_mean']} | {a['sub_zero']} | {top}")
print()
eras={'2010-2014':range(2010,2015),'2015-2019':range(2015,2020),'2020-2026':range(2020,2027),'2010-2019':range(2010,2020),'2020-2026':range(2020,2027)}
for name,rng in [('2010-2014',range(2010,2015)),('2015-2019',range(2015,2020)),('2020-2026',range(2020,2027))]:
    rs=[r for r in comp if int(r['year']) in rng]
    a=agg(rs)
    print(name, 'n=',a['n'],'meanchars',a['chars_mean'],'medchars',a['chars_med'],'meansub',a['sub_mean'],'zero-sub share',round(a['sub_zero']/a['n'],3))
    print('   verbs:', a['verbs'])
# explicit 'prove/show' share vs compute-ish
for name,rng in [('2010-2014',range(2010,2015)),('2015-2019',range(2015,2020)),('2020-2026',range(2020,2027))]:
    rs=[r for r in comp if int(r['year']) in rng]
    vc=collections.Counter()
    for r in rs: vc.update(r['verbs'])
    tot=sum(vc.values())
    proof=vc['prove']+vc['show']
    compw=vc['compute']+vc['find']+vc['determine']+vc['solve']
    print(name,'proof-verbs share',round(proof/tot,3),'compute-verbs share',round(compw/tot,3),'total verb tokens',tot)
# subpart distribution over time
print()
for name,rng in [('2010-2014',range(2010,2015)),('2015-2019',range(2015,2020)),('2020-2026',range(2020,2027))]:
    rs=[r for r in comp if int(r['year']) in rng]
    c=collections.Counter(r['subparts'] for r in rs)
    print(name,'subpart hist',dict(sorted(c.items())))
