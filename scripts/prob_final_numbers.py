
import json, statistics as st
b=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_bodies.json",encoding='utf-8'))
import re
rows=[]
for k,v in b.items():
    y,kind,n=k.split("|")
    rows.append((y,kind,int(n),v))
print("N =",len(rows))
L=[len(v) for _,_,_,v in rows]
print("overall chars: mean=%.0f median=%.0f min=%d max=%d total=%d"%(st.mean(L),st.median(L),min(L),max(L),sum(L)))
print("overall words: mean=%.0f median=%.0f"%(st.mean(len(v.split()) for _,_,_,v in rows), st.median([len(v.split()) for _,_,_,v in rows])))
sub=[len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',v)) for _,_,_,v in rows]
print("overall subparts mean=%.2f median=%.1f total=%d"%(st.mean(sub),st.median(sub),sum(sub)))
# era
ERAS=[("2010-2012",{"2010","2011","2012"}),("2013-2015",{"2013","2014","2015"}),("2016-2018",{"2016","2017","2018"}),("2019-2021",{"2019","2020","2021"}),("2022-2026",{"2022","2023","2024","2025","2026"})]
for name,ys in ERAS:
    r=[x for x in rows if x[0] in ys]
    L=[len(x[3]) for x in r]; S=[len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',x[3])) for x in r]
    print(f"{name}: n={len(r)} chars mean={st.mean(L):.0f} med={st.median(L):.0f} sub mean={st.mean(S):.2f} totalSub={sum(S)}")
print()
for name,ys in [("团体卷时代 2010-2019",{str(y) for y in range(2010,2020)}),("单卷时代 2020-2026",{str(y) for y in range(2020,2027)})]:
    r=[x for x in rows if x[0] in ys]
    L=[len(x[3]) for x in r]; S=[len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',x[3])) for x in r]
    print(f"{name}: 题数={len(r)} chars mean={st.mean(L):.0f} med={st.median(L):.0f} sub mean={st.mean(S):.2f} 年均题数={len(r)/len(ys):.1f}")
print()
# per year table final
print(f"{'yr':5s}{'n':>4s}{'mean':>7s}{'med':>7s}{'sub':>6s}")
for y in sorted({x[0] for x in rows}):
    r=[x for x in rows if x[0]==y]
    print(f"{y:5s}{len(r):4d}{st.mean(len(x[3]) for x in r):7.0f}{st.median([len(x[3]) for x in r]):7.0f}{st.mean([len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',x[3])) for x in r]):6.2f}")
