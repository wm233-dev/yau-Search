# -*- coding: utf-8 -*-
import json, re, collections, statistics
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
p = json.load(open(base+'problems_full.json', encoding='utf-8'))
geo = [x for x in p if x['subject']=='Geometry & Topology']
geo.append({'year':'2012','paper':'2012_Geometry2012individual','n':1,'text':'Show that pi3(S2) != 0.'})
def norm(t): return re.sub(r'[^a-z0-9]+',' ',t.lower()).split()
VERBS=['show','prove','compute','find','determine','construct','derive','verify','describe','calculate','state','does there exist','is the','decide']
def verbs(t):
    tl=t.lower(); out={}
    for v in VERBS:
        c=len(re.findall(r'\b'+re.escape(v), tl))
        if c: out[v]=c
    return out
eras=[('2010-2012',['2010','2011','2012']),('2013-2015',['2013','2014','2015']),('2016-2018',['2016','2017','2018']),('2019-2021',['2019','2020','2021']),('2022-2023',['2022','2023']),('2024-2026',['2024','2025','2026'])]
print('era\tn\tmeanChars\tmedChars\tmeanWords\tsubs/prob\tpct_with_sub\tverbs')
for name,ys in eras:
    g=[x for x in geo if x['year'] in ys]
    ch=[len(x['text']) for x in g]; w=[len(norm(x['text'])) for x in g]
    sub=[]
    for x in g:
        s=len(re.findall(r'\([a-d]\)',x['text']))+len(re.findall(r'\([1-9]\)',x['text']))
        sub.append(s)
    vc=collections.Counter()
    for x in g:
        for k,c in verbs(x['text']).items(): vc[k]+=1
    print(name, len(g), round(statistics.mean(ch)), int(statistics.median(ch)), round(statistics.mean(w),1), round(statistics.mean(sub),2), round(100*sum(1 for s in sub if s>0)/len(g)), dict(vc.most_common(8)), sep='\t')
print()
# per-year verb share
print('year\tshow\tprove\tcompute\tfind\tdetermine\tconstruct')
for y in sorted(set(x['year'] for x in geo)):
    g=[x for x in geo if x['year']==y]
    vc=collections.Counter()
    for x in g:
        for k,c in verbs(x['text']).items(): vc[k]+=1
    print(y, vc['show'], vc['prove'], vc['compute'], vc['find'], vc['determine'], vc['construct'], sep='\t')
