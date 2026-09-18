
# -*- coding: utf-8 -*-
import os, re, json, collections
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
CLEAN = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean"
def rd(p): return open(p, encoding="utf-8", errors="replace").read()
def norm(s):
    for a,b in [("\ufb01","fi"),("\ufb02","fl"),("\ufb00","ff"),("\ufb03","ffi"),("\ufb04","ffl")]:
        s=s.replace(a,b)
    return s
papers = {
 2010: [("I","2010_Analysis_and_differential_equations_individual.txt"),("T","2010_Analysis_and_differential_equations_team.txt")],
 2011: [("I","2011_1_AnalysisDiffEquation_Individual_2011.txt"),("T","2011_5_AnalysisDiffEquation_Team_2011.txt")],
 2012: [("I","2012_Analysis_individual.txt"),("T","2012_Analysis_team.txt")],
 2013: [("I","2013_analysis2013_individual.txt")],
 2014: [("I","2014_analysis2014_individual.txt"),("T","2014_analysis2014_team.txt")],
 2015: [("I","2015_analysis2015_individual.txt"),("T","2015_team_analysis2015.txt")],
 2016: [("I","2016_analysis2016_individual.txt")],
 2017: [("I","2017_analysis2017_individual.txt")],
 2018: [("I","2018_analysis2018_individual.txt")],
 2019: [("I","2019_Analysis2019_individual.txt"),("T","2019_Analysis2019_team.txt")],
 2020: [("I","2020_Analysis_DifferentialEquations_analysis_and_differential_20.txt")],
 2021: [("I","2021_ExamPaper_21S_analysis_and_differential_21s.txt")],
 2022: [("I","2022_ExamPaper_2022_analysis_and_differential_22s.txt")],
 2023: [("I","2023_Analysis_and_differential_equation.txt")],
 2024: [("I","2024_2024_Analysis_and_diff_v2.txt")],
 2025: [("I","2025_analysis.txt")],
 2026: [("I","2026_2026_analysis.txt")],
}
t13 = norm(rd(os.path.join(TXT,"2013_TeamProblems2013.txt")))
team13 = [p for p in re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests 2013)", t13) if "Analysis and Di" in p[:400]][0]
team = {2013: team13}
for y,f in [(2016,"2016_2016_team.txt"),(2017,"2017_2017_team.txt"),(2018,"2018_2018_team.txt")]:
    t = norm(rd(os.path.join(CLEAN,f)))
    for p in re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests "+str(y)+")", t):
        if "Analysis and Di" in p[:400]: team[y]=p

secs={}
probs=[]   # (year, part, idx, text)
for y,lst in papers.items():
    for part,f in lst:
        t = re.sub(r"=== page \d+ ==="," ",rd(os.path.join(TXT,f)))
        t = norm(t)
        secs[(y,part)]=t
for y,t in team.items():
    secs[(y,"T")]=norm(re.sub(r"=== page \d+ ==="," ",t))

def split_problems(t, year):
    # cut off header lines
    lines=t.split("\n")
    # find start: first line that begins with "1." or "1)" or "Problem 1"
    idx=0
    for i,l in enumerate(lines):
        if re.match(r"^\s*(1\.|1\)|Problem 1\b)", l):
            idx=i; break
    body="\n".join(lines[idx:])
    pat = r"(?m)^\s*(?:Problem\s+)?(\d{1,2})\s*[\.\)]\s+"
    ms=list(re.finditer(pat, body))
    out=[]
    for j,m in enumerate(ms):
        n=int(m.group(1))
        if n!=len(out)+1:  # enforce monotone numbering
            continue
        end = ms[j+1].start() if j+1<len(ms) else len(body)
        out.append((n, body[m.start():end].strip()))
    return out

for (y,part),t in sorted(secs.items()):
    ps=split_problems(t,y)
    for n,txt in ps:
        probs.append({"year":y,"part":part,"n":n,"chars":len(txt),"text":txt})

cnt=collections.Counter((p["year"],p["part"]) for p in probs)
print("PROBLEM COUNTS:", json.dumps({f"{k[0]}{k[1]}":v for k,v in sorted(cnt.items())}, ensure_ascii=False))
print("TOTAL", len(probs))

VERBS=["prove","show","derive","compute","calculate","find","determine","construct","verify","state","solve","give","explain","justify","check","estimate","establish","list","define","write","discuss"]
print("\nYEAR  nP  chars  avgCh  subparts  verbs")
rows={}
for y in sorted(set(p["year"] for p in probs)):
    sel=[p for p in probs if p["year"]==y]
    ch=sum(p["chars"] for p in sel)
    sub=sum(len(re.findall(r"(?m)^\s*\(?[a-j]\)", p["text"])) + len(re.findall(r"(?m)^\s*[1-9]\)", p["text"])) for p in sel)
    vc=collections.Counter()
    for p in sel:
        low=p["text"].lower()
        for v in VERBS:
            c=len(re.findall(r"\b"+v+r"\w*", low))
            if c: vc[v]+=c
    rows[y]=(len(sel),ch,ch/len(sel),sub,dict(vc))
    print(f"{y}  {len(sel):2d}  {ch:5d}  {ch/len(sel):6.1f}  {sub:3d}   {dict(sorted(vc.items(), key=lambda kv:-kv[1]))}")
json.dump(probs, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_probs.json","w"), ensure_ascii=False, indent=1)
json.dump({str(k):v for k,v in rows.items()}, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_rows.json","w"), ensure_ascii=False, indent=1)
