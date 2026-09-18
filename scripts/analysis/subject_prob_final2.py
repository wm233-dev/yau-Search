
import re, os, json, statistics as st
TXT = r".\txt"
P,R,D="P","R","D"
SPEC=[("2010","2010_Applied_Computational_Probability_and_Statistics_individual.txt","individual",4,0,D),
("2010","2010_Applied_Computational_Probability_and_Statistics_team.txt","team",4,0,D),
("2011","2011_2_AppliedMathProb_Individual_2011.txt","individual",4,2,D),
("2011","2011_6_AppliedMathProb_Team_2011.txt","team",4,2,D),
("2012","2012_Probability2012_individual.txt","individual",6,0,D),
("2012","2012_Probability2012_team.txt","team",6,0,D),
("2013","2013_probability2013_individual.txt","individual",6,0,P),
("2013","2013_TeamProblems2013.txt","team",6,0,P),
("2014","2014_probability2014_individual.txt","individual",5,0,P),
("2014","2014_probability2014_team.txt","team",5,0,P),
("2015","2015_probability2015_individual.txt","individual",5,0,P),
("2015","2015_team_probability2015.txt","team",5,0,P),
("2016","2016_probability2016_individual.txt","individual",5,0,P),
("2016","2016_2016_team.txt","team",5,0,P),
("2017","2017_probability2017_individual.txt","individual",5,0,P),
("2017","2017_2017_team.txt","team",5,0,P),
("2018","2018_probability2018_individual.txt","individual",5,0,P),
("2018","2018_2018_team.txt","team",5,0,P),
("2019","2019_ProbaStat2019_individual.txt","individual",4,0,R),
("2019","2019_ProbaStat2019_team.txt","team",4,0,R),
("2020","2020_Prob_Stat_probability_and_statistics_20.txt","single",6,0,P),
("2021","2021_ExamPaper_21S_probability_and_statistics_21s.txt","single",6,0,P),
("2022","2022_ExamPaper_2022_probability_and_statistics_22s.txt","single",6,0,P),
("2023","2023_probability_statistics.txt","single",6,0,D),
("2024","2024_2024_statistics.txt","single",5,0,D),
("2025","2025_statistics.txt","single",4,0,P),
("2026","2026_2026_statistics.txt","single",6,0,P)]
def read(p): return open(p,'rb').read().replace(b'\x00',b' ').decode('utf-8','replace')
def norm(t):
    t=re.sub(r'-\s*\n\s*','',t); t=re.sub(r'\s+',' ',t); return t.strip()
def slice_ps(f,t):
    if f=="2013_TeamProblems2013.txt":
        i=t.find("Probability and Statistics Problems"); return t[i:] if i>=0 else ""
    if f in ("2016_2016_team.txt","2017_2017_team.txt","2018_2018_team.txt"):
        for m in re.finditer(r"Probability and Statistics", t):
            i=m.start()
            if "Team" in t[i:i+80]:
                nx=re.search(r"S\.-T\. Yau College Student Mathematics Contests", t[i+50:])
                return t[i:(i+50+nx.start()) if nx else len(t)]
        return ""
    return t
RX={P:re.compile(r'(?m)^\s*Problem\s+(\d+)\s*[\.\):]'),R:re.compile(r'(?m)^\s*(\d+)\s*\)\s'),D:re.compile(r'(?m)^\s*(\d+)\s*\.\s')}
VERBS=["prove","show","find","compute","derive","calculate","determine","evaluate","construct","justify","disprove","describe","verify","explain","suggest","identify","compare","discuss","estimate","argue","give","solve","prove or disprove"]
rows=[]
for (y,f,kind,exp,skip,style) in SPEC:
    t=slice_ps(f,read(os.path.join(TXT,f)))
    raw=[(int(m.group(1)),m.start(),m.end()) for m in RX[style].finditer(t)]
    # greedy sequential filter starting at 1
    kept=[]; want=1
    for (n,s,e) in raw:
        if n==want:
            kept.append((n,s,e)); want+=1
    ms=kept
    if len(ms)<exp+skip: print("!! WARN",f,"seq marks",len(ms),"want",exp+skip)
    sel=ms[skip:skip+exp]
    for i,(n,s,e) in enumerate(sel):
        gi=skip+i
        nxt=ms[gi+1][1] if gi+1<len(ms) else len(t)
        b=norm(t[e:nxt])
        sub=len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',b))
        v={x:len(re.findall(r'(?i)\b'+re.escape(x),b)) for x in VERBS}
        v['prove_or_disprove']=len(re.findall(r'(?i)prove or disprove',b))
        rows.append(dict(year=y,file=f,kind=kind,n=i+1,chars=len(b),words=len(b.split()),subparts=sub,verbs=v,head=b[:150]))
print("TOTAL:",len(rows))
by={}
for r in rows: by.setdefault(r['year'],[]).append(r)
for y in sorted(by):
    rs=by[y]
    print(f"{y} n={len(rs):3d} meanCh={st.mean(r['chars'] for r in rs):6.0f} medCh={st.median(r['chars'] for r in rs):6.0f} maxCh={max(r['chars'] for r in rs):5d} meanSub={st.mean(r['subparts'] for r in rs):5.2f} prove={sum(r['verbs']['prove'] for r in rs):3d} show={sum(r['verbs']['show'] for r in rs):3d} find={sum(r['verbs']['find'] for r in rs):3d} compute={sum(r['verbs']['compute'] for r in rs):2d} derive={sum(r['verbs']['derive'] for r in rs):2d} det={sum(r['verbs']['determine'] for r in rs):2d} calc={sum(r['verbs']['calculate'] for r in rs):2d} disprove={sum(r['verbs']['prove_or_disprove'] for r in rs):2d}")
for name,ys in [("2010-2012",{"2010","2011","2012"}),("2013-2015",{"2013","2014","2015"}),("2016-2018",{"2016","2017","2018"}),("2019-2021",{"2019","2020","2021"}),("2022-2026",{"2022","2023","2024","2025","2026"}),("TEAM-era 2010-2019",{"2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"}),("SINGLE-era 2020-2026",{"2020","2021","2022","2023","2024","2025","2026"})]:
    rs=[r for r in rows if r['year'] in ys]
    print(f"{name}: n={len(rs)} meanCh={st.mean(r['chars'] for r in rs):.0f} medCh={st.median(r['chars'] for r in rs):.0f} meanSub={st.mean(r['subparts'] for r in rs):.2f} prove={sum(r['verbs']['prove'] for r in rs)} show={sum(r['verbs']['show'] for r in rs)} find={sum(r['verbs']['find'] for r in rs)} compute={sum(r['verbs']['compute'] for r in rs)} derive={sum(r['verbs']['derive'] for r in rs)} determine={sum(r['verbs']['determine'] for r in rs)} calculate={sum(r['verbs']['calculate'] for r in rs)}")
json.dump(rows, open(r".\scripts\prob_ps_rows_v2.json","w"), ensure_ascii=False, indent=1)
