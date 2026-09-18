
import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
inv=json.load(open(r'./archive/work/tagfreq.json',encoding='utf-8'))
# family era share: recompute from INV quickly by re-executing the inventory literal
src=open(r'./archive/work/_inv.py',encoding='utf-8').read()
ns={}
exec(src.split("print('TOTAL")[0], ns)
INV=ns['INV']; TAX=ns['TAX']
famshare=collections.defaultdict(lambda: collections.Counter())
for era,rng in [('10-14',range(2010,2015)),('15-19',range(2015,2020)),('20-26',range(2020,2027))]:
    n=0
    for y,k,q,ts in INV:
        if y in rng:
            n+=1
            for t in ts: famshare[t[0]][era]+=1
    famshare['_N'][era]=n
print('problems per era:',dict(famshare['_N']))
fams=[f for f in famshare if f!='_N']
print('family | 10-14 | 15-19 | 20-26 | share20-26')
for f in sorted(fams):
    c=famshare[f]; tot=sum(c.values())
    print(f, c['10-14'], c['15-19'], c['20-26'], 'total',tot, 'share20-26=%.2f'%(c['20-26']/famshare['_N']['20-26']))
# per era: how many problems are "numerical" (families A,B,C,D,E,F) vs "applied/other" (G,H,I,J)
numf=set('ABCDEF'); 
for era in ['10-14','15-19','20-26']:
    cnt=0; n=famshare['_N'][era]
    for y,k,q,ts in INV:
        ok={ '10-14':2010<=y<=2014,'15-19':2015<=y<=2019,'20-26':2020<=y<=2026}[era]
        if ok and any(t[0] in numf for t in ts): cnt+=1
    print(era,'含数值方法类考点(A-F)的题数',cnt,'/',n, '%.2f'%(cnt/n))
