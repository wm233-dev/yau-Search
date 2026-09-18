
import re, os, sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
rows=json.load(open(r'./archive/work/prob_metrics_curated.json',encoding='utf-8'))
comp=[r for r in rows if not (int(r['year'])==2010 and str(r['n']) not in ('5','6')) and not (int(r['year'])==2011 and str(r['n']) not in ('1','2'))]
BASE=r'./txt'
# recount marker styles from the stored file+n: need bodies again -> re-segment quickly
import importlib.util
exec(open(r'./archive/work/_metrics.py',encoding='utf-8').read().split('rows=[]')[0])
cnt=collections.Counter()
style=collections.defaultdict(collections.Counter)
for year,kind,f,pat,want in FILES:
    t=load(f)
    if f in SEC:
        sp,ep=SEC[f]; m=re.search(sp,t); s=m.start()
        if ep:
            m2=re.search(ep,t[s+10:]); t=t[s:s+10+m2.start()]
        else: t=t[s:]
    for n,body in segment(t,pat,want):
        key=(year,kind,str(n))
        if year==2010 and str(n) not in ('5','6'): continue
        if year==2011 and str(n) not in ('1','2'): continue
        b=re.sub(r'\s+',' ',body)
        a=len(re.findall(r'\(([a-j])\)',b))
        r=len(re.findall(r'\(((?:i|ii|iii|iv|v|vi))\)',b))
        d=len(re.findall(r'\((\d)\)',b))
        style[year][('letters(a-j)','roman(i,ii)','digits(1-9)')[max(range(3),key=lambda i:(a,r,d)[i])]]+=1
        cnt['letters']+=a>0
for y in sorted(style): print(y, dict(style[y]))
