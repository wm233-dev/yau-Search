
import json,re,itertools
d=json.load(open(r'E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json',encoding='utf-8'))
gt=[x for x in d if x.get('subject')=='Geometry & Topology']
def norm(t):
    t=t.lower(); t=re.sub(r'[^a-z0-9 ]',' ',t); return re.sub(r'\s+',' ',t).strip()
def grams(t,n=6):
    w=norm(t).split()
    return set(tuple(w[i:i+n]) for i in range(len(w)-n+1))
pairs=[]
for a,b in itertools.combinations(gt,2):
    ga,gb=grams(a['text']),grams(b['text'])
    if not ga or not gb: continue
    j=len(ga&gb)/len(ga|gb)
    if j>0.35: pairs.append((round(j,3),a['year'],a['kind'],a['n'],b['year'],b['kind'],b['n']))
pairs.sort(reverse=True)
for p in pairs[:12]: print(p)
print('pairs>0.35:',len(pairs))
