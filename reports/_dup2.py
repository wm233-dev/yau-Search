
import json,re,itertools
d=json.load(open(r'.\data\problems_full.json',encoding='utf-8'))
gt=[x for x in d if x.get('subject')=='Geometry & Topology']
idx={(x['year'],x['kind'],x['n']):x for x in gt}
def norm(t):
    t=t.lower(); t=re.sub(r'[^a-z0-9 ]',' ',t); return re.sub(r'\s+',' ',t).strip()
def grams(t,n=6):
    w=norm(t).split(); return set(tuple(w[i:i+n]) for i in range(len(w)-n+1))
def J(a,b):
    ga,gb=grams(a),grams(b); return round(len(ga&gb)/len(ga|gb),3)
for x in [[('2011','team',5),('2024','individual',4)],[('2014','team',4),('2026','individual',3)],[('2015','team',2),('2016','team',2)],[('2010','team',3),('2016','individual',4)],[('2011','individual',5),('2013','team',6)]]:
    a,b=idx[x[0]],idx[x[1]]
    print(x, J(a['text'],b['text']))
