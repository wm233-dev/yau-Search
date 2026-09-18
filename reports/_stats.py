
import json,collections
M=json.load(open(r'E:\deepseek_exclusive\math\.tmp\burn2026\data\mother_geometry.json',encoding='utf-8'))
rows=[]
for m in M:
    ys=[int(x['year']) for x in m['members']]
    recent=sum(1 for y in ys if y>=2021)
    rows.append((m['id'],len(m['members']),min(ys),max(ys),recent,m['trend']))
rows.sort(key=lambda r:(-(r[1]*1.0+1.5*r[4]),r[2]))
for r in rows: print(r)
print('years covered by mothers:')
allrows=[]
for m in M:
    for x in m['members']: allrows.append(int(x['year']))
c=collections.Counter(allrows)
print(sorted(c.items()))
