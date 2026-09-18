
import json
d=json.load(open(r'.\data\problems_full.json',encoding='utf-8'))
gt=[x for x in d if x.get('subject')=='Geometry & Topology']
have=set((x['year'],x['kind'],x['n']) for x in gt)
M=json.load(open(r'.\data\mother_geometry.json',encoding='utf-8'))
entries=[]; bad=[]
for m in M:
    for x in m['members']:
        t=(x['year'],x['kind'],int(x['n']))
        if t not in have: bad.append((m['id'],t))
        entries.append((m['id'],t))
print('bad members:',bad)
orph=[('2012','individual',4),('2013','team',2),('2013','team',3),('2014','individual',4),('2017','team',4),('2018','individual',4),('2019','individual',4),('2022','individual',3),('2023','individual',3),('2023','individual',4),('2024','individual',6)]
covered=set(t for _,t in entries)
dup=[t for t in covered if sum(1 for _,u in entries if u==t)>1]
print('entries',len(entries),'distinct covered',len(covered),'dup',dup)
missing = have - covered - set(orph)
print('rows not accounted for:',sorted(missing))
print('orphans not in gt:',[o for o in orph if o not in have])
print('coverage',len(covered),'/',len(have), round(100*len(covered)/len(have),1))
