
import re, os, json, statistics as st
TXT = r".\txt"
SPEC = [
 ("2010","2010_Applied_Computational_Probability_and_Statistics_individual.txt","individual",4,0),
 ("2010","2010_Applied_Computational_Probability_and_Statistics_team.txt","team",4,0),
 ("2011","2011_2_AppliedMathProb_Individual_2011.txt","individual",4,2),
 ("2011","2011_6_AppliedMathProb_Team_2011.txt","team",4,2),
 ("2012","2012_Probability2012_individual.txt","individual",6,0),
 ("2012","2012_Probability2012_team.txt","team",6,0),
 ("2013","2013_probability2013_individual.txt","individual",6,0),
 ("2013","2013_TeamProblems2013.txt","team",6,0),
 ("2014","2014_probability2014_individual.txt","individual",5,0),
 ("2014","2014_probability2014_team.txt","team",5,0),
 ("2015","2015_probability2015_individual.txt","individual",5,0),
 ("2015","2015_team_probability2015.txt","team",5,0),
 ("2016","2016_probability2016_individual.txt","individual",5,0),
 ("2016","2016_2016_team.txt","team",5,0),
 ("2017","2017_probability2017_individual.txt","individual",5,0),
 ("2017","2017_2017_team.txt","team",5,0),
 ("2018","2018_probability2018_individual.txt","individual",5,0),
 ("2018","2018_2018_team.txt","team",5,0),
 ("2019","2019_ProbaStat2019_individual.txt","individual",4,0),
 ("2019","2019_ProbaStat2019_team.txt","team",4,0),
 ("2020","2020_Prob_Stat_probability_and_statistics_20.txt","single",6,0),
 ("2021","2021_ExamPaper_21S_probability_and_statistics_21s.txt","single",6,0),
 ("2022","2022_ExamPaper_2022_probability_and_statistics_22s.txt","single",6,0),
 ("2023","2023_probability_statistics.txt","single",6,0),
 ("2024","2024_2024_statistics.txt","single",5,0),
 ("2025","2025_statistics.txt","single",4,0),
 ("2026","2026_2026_statistics.txt","single",6,0),
]
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
SPLIT_P=re.compile(r'(?m)^\s*Problem\s+(\d+)\s*[\.\):]')
SPLIT_D=re.compile(r'(?m)^\s*(\d+)\s*\.\s')
SPLIT_R=re.compile(r'(?m)^\s*(\d+)\s*\)\s')
VERBS=["prove","show","find","compute","derive","calculate","determine","evaluate","construct","justify","disprove","describe","verify","explain","suggest","identify","compare","discuss","estimate","argue"]
rows=[]
for (y,f,kind,exp,skip) in SPEC:
    t = slice_ps(f, read(os.path.join(TXT,f)))
    best=[]
    for rx in (SPLIT_P,SPLIT_R,SPLIT_D):
        ms=[(int(m.group(1)),m.start(),m.end()) for m in rx.finditer(t)]
        if len(ms)>=exp+skip and len(ms)>len(best): best=ms
    best=sorted(best,key=lambda z:z[1])
    sel=best[skip:skip+exp]
    if len(sel)!=exp: print("!! WARN",f,len(sel),exp)
    for i,(n,s,e) in enumerate(sel):
        gi = skip+i
        nxt = best[gi+1][1] if gi+1<len(best) else len(t)
        b=norm(t[e:nxt])
        sub=len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)',b))
        v={x:len(re.findall(r'\b'+re.escape(x),b,re.I)) for x in VERBS}
        rows.append(dict(year=y,file=f,kind=kind,n=i+1,chars=len(b),words=len(b.split()),subparts=sub,verbs=v,head=b[:130]))
print("TOTAL:",len(rows))
by={}
for r in rows: by.setdefault(r['year'],[]).append(r)
print(f"{'yr':5s}{'n':>4s}{'meanCh':>8s}{'medCh':>7s}{'meanSub':>9s}{'prove':>7s}{'show':>6s}{'find':>6s}{'comp':>6s}{'der':>5s}{'det':>5s}")
for y in sorted(by):
    rs=by[y]
    print(f"{y:5s}{len(rs):4d}{st.mean(r['chars'] for r in rs):8.0f}{st.median(r['chars'] for r in rs):7.0f}{st.mean(r['subparts'] for r in rs):9.2f}"
          f"{sum(r['verbs']['prove'] for r in rs):7d}{sum(r['verbs']['show'] for r in rs):6d}{sum(r['verbs']['find'] for r in rs):6d}"
          f"{sum(r['verbs']['compute'] for r in rs):6d}{sum(r['verbs']['derive'] for r in rs):5d}{sum(r['verbs']['determine'] for r in rs):5d}")
for name,ys in [("2010-2012",{"2010","2011","2012"}),("2013-2015",{"2013","2014","2015"}),("2016-2018",{"2016","2017","2018"}),("2019-2021",{"2019","2020","2021"}),("2022-2026",{"2022","2023","2024","2025","2026"}),("2020-2026(no team)",{"2020","2021","2022","2023","2024","2025","2026"})]:
    rs=[r for r in rows if r['year'] in ys]
    print(f"{name}: n={len(rs)} mean={st.mean(r['chars'] for r in rs):.0f} med={st.median(r['chars'] for r in rs):.0f} meanSub={st.mean(r['subparts'] for r in rs):.2f} prove={sum(r['verbs']['prove'] for r in rs)} show={sum(r['verbs']['show'] for r in rs)} find={sum(r['verbs']['find'] for r in rs)}")
json.dump(rows, open(r".\scripts\prob_ps_rows3.json","w"), ensure_ascii=False, indent=1)
# print problem-level detail for the smallest/largest to sanity check
for r in sorted(rows,key=lambda r:-r['chars'])[:5]:
    print("BIG",r['year'],r['file'][:30],r['n'],r['chars'],r['subparts'],r['head'][:70])
for r in sorted(rows,key=lambda r:r['chars'])[:5]:
    print("SMALL",r['year'],r['file'][:30],r['n'],r['chars'],r['subparts'],r['head'][:70])
