
# -*- coding: utf-8 -*-
import os, re, json, collections, itertools
exec(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])
def toks(t):
    t=t.lower()
    t=re.sub(r"[^a-z0-9]+"," ",t)
    return t.split()
docs={}
for (y,p),t in secs.items():
    w=toks(t)
    docs[(y,p)]=w
def shingles(ws,k=7):
    return set(tuple(ws[i:i+k]) for i in range(len(ws)-k+1))
S={k:shingles(v) for k,v in docs.items()}
pairs=[]
ks=list(S)
for a,b in itertools.combinations(ks,2):
    if not S[a] or not S[b]: continue
    inter=len(S[a]&S[b])
    if inter==0: continue
    j=inter/len(S[a]|S[b])
    pairs.append((j,inter,a,b))
pairs.sort(reverse=True)
print("TOP ANALYSIS-SECTION PAIRS by 7-gram Jaccard")
for j,inter,a,b in pairs[:18]:
    print(f"  J={j:.3f} shared={inter}  {a}  <->  {b}")
print()
print("shared shingles for top pairs:")
for j,inter,a,b in pairs[:6]:
    sh=sorted(S[a]&S[b])
    print(f"\n--- {a} <-> {b} (J={j:.3f}) ---")
    for s in sh[:8]:
        print("     ", " ".join(s))
