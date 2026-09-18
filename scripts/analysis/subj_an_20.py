
# -*- coding: utf-8 -*-
import os, re, json, collections, itertools
exec(open(r".\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])
EXP={(2010,'I'):6,(2010,'T'):6,(2011,'I'):6,(2011,'T'):6,(2012,'I'):6,(2012,'T'):6,(2013,'I'):6,(2013,'T'):6,
 (2014,'I'):6,(2014,'T'):6,(2015,'I'):6,(2015,'T'):6,(2016,'I'):6,(2016,'T'):6,(2017,'I'):6,(2017,'T'):6,
 (2018,'I'):6,(2018,'T'):5,(2019,'I'):5,(2019,'T'):5,(2020,'I'):6,(2021,'I'):6,(2022,'I'):6,(2023,'I'):6,
 (2024,'I'):5,(2025,'I'):6,(2026,'I'):5}
BOIL = re.compile(r"^(S\.-T\.? Yau College Student Mathematics Contests \d+|Analysis and Di\w* Equations|Individual|Team|\(?Please (solve|select)[^\n]*|Solve every problem\.|\(\d+ problems\)|GROUP TEST|INDIVIDUAL TEST|S\.-T YAU COLLEGE MATH CONTESTS \d+|\d+)\s*$", re.I)
def clean(t):
    lines=[l for l in t.split("\n") if not BOIL.match(l.strip())]
    return re.sub(r"=== page \d+ ===","","\n".join(lines))
probs={}
for (y,p),t in sorted(secs.items()):
    body=clean(t)
    cands=[(m.start(), int(m.group(1)), m.end()) for m in re.finditer(r"(?m)^\s*(?:Problem\s+)?(\d{1,2})\s*[\.\)]?(?=\s|$)", body)]
    # also handle "Problem 2 Recall" (number followed by space+capital)
    cands += [(m.start(), int(m.group(1)), m.end()) for m in re.finditer(r"(?m)^\s*Problem\s+(\d{1,2})\s+(?=[A-Z])", body)]
    cands=sorted(set(cands))
    accepted=[]; exp=1
    for pos,n,end in cands:
        if n==exp:
            accepted.append((pos,end,n)); exp+=1
    out=[]
    for i,(pos,end,n) in enumerate(accepted):
        e = accepted[i+1][0] if i+1<len(accepted) else len(body)
        out.append((n, body[pos:e].strip()))
    probs[(y,p)]=out
    flag = "OK " if len(out)==EXP.get((y,p),0) else "**"
    print(f"{flag} {y}{p}: got {len(out)} expect {EXP.get((y,p))}  lens={[len(x[1]) for x in out]}")
json.dump({f"{k[0]}{k[1]}":v for k,v in probs.items()}, open(r".\scripts\an_probs2.json","w"), ensure_ascii=False, indent=1)
