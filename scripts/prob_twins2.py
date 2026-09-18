
import re, os, json, itertools, difflib
TXT=r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
exec(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\subject_prob_final2.py").read().split("print(\"TOTAL")[0])
json.dump(rows, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_rows_body.json","w"), ensure_ascii=False)
def sh(s,k=6):
    w=re.findall(r"[A-Za-z0-9]+", s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(1,len(w)-k+1)))
S={(r['year'],r['kind'],r['n']):(sh(r['head']) if False else sh(r['head']), r) for r in rows}
# rebuild with full body: head was truncated at 150; re-extract bodies properly
def read(p): return open(p,'rb').read().replace(b'\x00',b' ').decode('utf-8','replace')
def norm(t):
    t=re.sub(r'-\s*\n\s*','',t); t=re.sub(r'\s+',' ',t); return t.strip()
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
store={}
for (y,f,kind,exp,skip,style) in SPEC:
    t=slice_ps(f,read(os.path.join(TXT,f)))
    raw=[(int(m.group(1)),m.start(),m.end()) for m in RX[style].finditer(t)]
    kept=[]; want=1
    for (n,s,e) in raw:
        if n==want: kept.append((n,s,e)); want+=1
    for i,(n,s,e) in enumerate(kept[skip:skip+exp]):
        gi=skip+i
        nxt=kept[gi+1][1] if gi+1<len(kept) else len(t)
        store[(y,kind,i+1)]=norm(t[e:nxt])
keys=list(store)
def lcs(a,b):
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    m=sm.find_longest_match(0,len(a),0,len(b))
    return m.size, a[m.a:m.a+m.size]
res=[]
for a,b in itertools.combinations(keys,2):
    A,B=store[a],store[b]
    sa,sb=sh(A),sh(B)
    if not sa or not sb: continue
    j=len(sa&sb)/len(sa|sb)
    if j>=0.05 or (a[0]!=b[0]):
        # only report cross-year or same-year strong
        pass
    if j>=0.05:
        L,txt=lcs(A,B)
        res.append((round(j,3),L,a,b,txt[:90]))
res.sort(reverse=True)
for j,L,a,b,txt in res[:25]:
    print(f"J={j:.3f} LCS={L:3d} {a} <-> {b}\n     shared: {txt!r}")
print()
print("=== cross-year pairs with LCS>=60 chars ===")
for j,L,a,b,txt in res:
    if a[0]!=b[0] and L>=60:
        print(f"J={j:.3f} LCS={L} {a} <-> {b} :: {txt[:100]!r}")
