
# -*- coding: utf-8 -*-
import os, re, json, collections
exec(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])
for pat in ["older","Rukowski","Riemann","Gauss","Cauchy","Green","Newton","Stokes"]:
    hits=[]
    for (y,p),t in sorted(secs.items()):
        for m in re.finditer(pat,t):
            hits.append((y,p,t[max(0,m.start()-55):m.start()+45].replace("\n"," ")))
    print(f"\n### {pat}: {len(hits)}")
    for h in hits[:12]: print("   ",h)
