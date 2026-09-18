
# -*- coding: utf-8 -*-
import os, re, json, collections
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
CLEAN = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean"

def rd(p):
    return open(p, encoding="utf-8", errors="replace").read()

# analysis paper files (problems)
papers = {
 2010: ["2010_Analysis_and_differential_equations_individual.txt","2010_Analysis_and_differential_equations_team.txt"],
 2011: ["2011_1_AnalysisDiffEquation_Individual_2011.txt","2011_5_AnalysisDiffEquation_Team_2011.txt"],
 2012: ["2012_Analysis_individual.txt","2012_Analysis_team.txt"],
 2013: ["2013_analysis2013_individual.txt"],   # + team from TeamProblems2013
 2014: ["2014_analysis2014_individual.txt","2014_analysis2014_team.txt"],
 2015: ["2015_analysis2015_individual.txt","2015_team_analysis2015.txt"],
 2016: ["2016_analysis2016_individual.txt"],   # + team clean
 2017: ["2017_analysis2017_individual.txt"],
 2018: ["2018_analysis2018_individual.txt"],
 2019: ["2019_Analysis2019_individual.txt","2019_Analysis2019_team.txt"],
 2020: ["2020_Analysis_DifferentialEquations_analysis_and_differential_20.txt"],
 2021: ["2021_ExamPaper_21S_analysis_and_differential_21s.txt"],
 2022: ["2022_ExamPaper_2022_analysis_and_differential_22s.txt"],
 2023: ["2023_Analysis_and_differential_equation.txt"],
 2024: ["2024_2024_Analysis_and_diff_v2.txt"],
 2025: ["2025_analysis.txt"],
 2026: ["2026_2026_analysis.txt"],
}
sols = {
 2020: "2020_Analysis_DifferentialEquations_analysis_and_differential_soln_20.txt",
 2021: "2021_Solution_21S_analysis_and_differential_21s_soln.txt",
 2022: "2022_Solution_2022_analysis_and_differential_22s_soln.txt",
}

# extract 2013 team analysis section
t13 = rd(os.path.join(TXT,"2013_TeamProblems2013.txt"))
parts = re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests 2013)", t13)
team_parts = {}
for p in parts:
    if "Analysis and Di" in p[:400]:
        team_parts[2013]=p
    if "Geometry and Topology" in p[:400]:
        pass
# 2016-2018 team analysis sections
team_clean = {}
for y,f in [(2016,"2016_2016_team.txt"),(2017,"2017_2017_team.txt"),(2018,"2018_2018_team.txt")]:
    t = rd(os.path.join(CLEAN,f))
    ps = re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests "+str(y)+")", t)
    for p in ps:
        if "Analysis and Di" in p[:400]:
            team_clean[y]=p

def strip_pages(s):
    return re.sub(r"=== page \d+ ===", " ", s)

records = []   # (year, part, text)
for y, fs in papers.items():
    for f in fs:
        records.append((y, "I" if ("individual" in f.lower() or "_1_" in f or "_ExamPaper" in f or f.startswith(str(y)+"_") and "team" not in f.lower()) else "T", strip_pages(rd(os.path.join(TXT,f))), f))
# fix part labels properly
records = []
for y, fs in papers.items():
    for f in fs:
        low=f.lower()
        part = "T" if ("team" in low) else "I"
        records.append((y, part, strip_pages(rd(os.path.join(TXT,f))), f))
if 2013 in team_parts:
    records.append((2013,"T",strip_pages(team_parts[2013]),"2013_TeamProblems2013.txt[analysis]"))
for y,t in team_clean.items():
    records.append((y,"T",strip_pages(t),"2016_2018_team[analysis]"))

tot=0
print("YEAR PART CHARS  FILE")
for y,part,s,f in sorted(records):
    tot+=len(s)
    print(f"{y} {part} {len(s):6d}  {f}")
print("TOTAL chars", tot, "files", len(records))

# per year aggregate
agg=collections.defaultdict(lambda: [0,0])
for y,part,s,f in records:
    agg[y][0]+=len(s); agg[y][1]+=1
json.dump({str(k):v for k,v in agg.items()}, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_agg.json","w"), ensure_ascii=False, indent=1)
