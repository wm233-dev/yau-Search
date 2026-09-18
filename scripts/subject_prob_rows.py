
import re, os, json, statistics as st
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
PS = {
 "2010": ["2010_Applied_Computational_Probability_and_Statistics_individual.txt","2010_Applied_Computational_Probability_and_Statistics_team.txt"],
 "2011": ["2011_2_AppliedMathProb_Individual_2011.txt","2011_6_AppliedMathProb_Team_2011.txt"],
 "2012": ["2012_Probability2012_individual.txt","2012_Probability2012_team.txt"],
 "2013": ["2013_probability2013_individual.txt","2013_TeamProblems2013.txt"],
 "2014": ["2014_probability2014_individual.txt","2014_probability2014_team.txt"],
 "2015": ["2015_probability2015_individual.txt","2015_team_probability2015.txt"],
 "2016": ["2016_probability2016_individual.txt","2016_2016_team.txt"],
 "2017": ["2017_probability2017_individual.txt","2017_2017_team.txt"],
 "2018": ["2018_probability2018_individual.txt","2018_2018_team.txt"],
 "2019": ["2019_ProbaStat2019_individual.txt","2019_ProbaStat2019_team.txt"],
 "2020": ["2020_Prob_Stat_probability_and_statistics_20.txt"],
 "2021": ["2021_ExamPaper_21S_probability_and_statistics_21s.txt"],
 "2022": ["2022_ExamPaper_2022_probability_and_statistics_22s.txt"],
 "2023": ["2023_probability_statistics.txt"],
 "2024": ["2024_2024_statistics.txt"],
 "2025": ["2025_statistics.txt"],
 "2026": ["2026_2026_statistics.txt"],
}
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
                end=i+50+nx.start() if nx else len(t)
                return t[i:end]
        return ""
    return t

# 2011 & 2010: combined papers -> keep only P&S problems by index
KEEP = {
 "2010_Applied_Computational_Probability_and_Statistics_individual.txt": [1,2,3,4],
 "2010_Applied_Computational_Probability_and_Statistics_team.txt": [1,2,3,4],
 "2011_2_AppliedMathProb_Individual_2011.txt": [3,4,5,6],
 "2011_6_AppliedMathProb_Team_2011.txt": [3,4,5,6],
}

SPLIT = re.compile(r'(?m)^\s*(?:Problem\s+(\d+)\s*[\.\):]|(\d+)\s*[\.\)]\s)')
def split_problems(t):
    marks=[]
    for m in SPLIT.finditer(t):
        n = int(m.group(1) or m.group(2))
        marks.append((n, m.start(), m.end()))
    out=[]
    for i,(n,s,e) in enumerate(marks):
        nxt = marks[i+1][1] if i+1<len(marks) else len(t)
        out.append((n, t[e:nxt]))
    return out

VERBS = ["prove","show","find","compute","derive","calculate","determine","evaluate","construct","justify","disprove","describe","verify","explain","give","suggest","write down","identify","compare","discuss","estimate"]
rows=[]
for y,fs in sorted(PS.items()):
    for f in fs:
        t = slice_ps(f, read(os.path.join(TXT,f)))
        probs = split_problems(t)
        keep = KEEP.get(f)
        if keep: probs=[p for p in probs if p[0] in keep]
        for n,body in probs:
            b = norm(body)
            b = re.sub(r'^[\s\.\)]*','',b)
            sub = len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|[1-9])\)', b))
            v = {x: len(re.findall(r'\b'+re.escape(x), b, re.I)) for x in VERBS}
            rows.append(dict(year=y,file=f,n=n,chars=len(b),words=len(b.split()),subparts=sub,verbs=v,head=b[:110]))
print("n problems =", len(rows))
by = {}
for r in rows: by.setdefault(r['year'],[]).append(r)
print(f"{'yr':5s}{'n':>4s}{'meanCh':>8s}{'medCh':>7s}{'meanSub':>9s}{'prove':>7s}{'show':>6s}{'find':>6s}{'compute':>8s}{'derive':>7s}{'calc':>6s}")
tot=0
for y in sorted(by):
    rs=by[y]; tot+=len(rs)
    print(f"{y:5s}{len(rs):4d}{st.mean(r['chars'] for r in rs):8.0f}{st.median(r['chars'] for r in rs):7.0f}{st.mean(r['subparts'] for r in rs):9.2f}"
          f"{sum(r['verbs']['prove'] for r in rs):7d}{sum(r['verbs']['show'] for r in rs):6d}{sum(r['verbs']['find'] for r in rs):6d}"
          f"{sum(r['verbs']['compute'] for r in rs):8d}{sum(r['verbs']['derive'] for r in rs):7d}{sum(r['verbs']['calculate'] for r in rs):6d}")
print("total problems:", tot)
json.dump(rows, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_rows.json","w"), ensure_ascii=False, indent=1)
