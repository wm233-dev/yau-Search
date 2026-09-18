
# -*- coding: utf-8 -*-
import os, re, json, collections
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
CLEAN = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean"
def rd(p): return open(p, encoding="utf-8", errors="replace").read()
t13 = rd(os.path.join(TXT,"2013_TeamProblems2013.txt"))
parts = re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests 2013)", t13)
for p in parts:
    if "Analysis and Di" in p[:400]:
        print("### 2013 TEAM ANALYSIS SECTION, chars", len(p)); print(p[:200],"...\n...",p[-300:])
for y,f in [(2016,"2016_2016_team.txt"),(2017,"2017_2017_team.txt"),(2018,"2018_2018_team.txt")]:
    t = rd(os.path.join(CLEAN,f))
    ps = re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests "+str(y)+")", t)
    for p in ps:
        if "Analysis and Di" in p[:400]:
            print(f"\n### {y} TEAM ANALYSIS, chars {len(p)}")
            print("TAIL:", p[-350:])
