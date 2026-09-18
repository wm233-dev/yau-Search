# -*- coding: utf-8 -*-
import os, re, glob
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
def raw(n): return open(os.path.join(TXT, n), encoding="utf-8", errors="replace").read()
def norm(t):
    t = re.sub(r"===\s*page\s*\d+\s*===", " ", t).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", t)).strip()

def lcs(a, b, minlen=60):
    # suffix-automaton-free DP is too big; use rolling set of k-grams to find longest shared run
    best = ""
    lo, hi = minlen, min(len(a), len(b))
    # exponential search on length
    def has(L):
        S = set(a[i:i+L] for i in range(0, len(a)-L+1, 1))
        for i in range(0, len(b)-L+1, 1):
            if b[i:i+L] in S: return b[i:i+L]
        return None
    L = minlen
    found = None
    while L <= hi:
        r = has(L)
        if r is None: break
        found = r; L = int(L*1.4)+8
    if found is None: return None
    # refine
    step = 1
    cur = found
    while True:
        r = has(len(cur)+step)
        if r is None:
            if step == 1: break
            step = 1
        else:
            cur = r; step = max(step*2, 2) if step>1 else 1
            if step==1: 
                r2 = has(len(cur)+1)
                if r2 is None: break
                cur = r2
                break
    return cur

pairs = [
 ("2013_applied2013_individual.txt","2013_TeamProblems2013.txt"),
 ("2014_applied2014_individual.txt","2014_applied2014_team.txt"),
 ("2015_analysis2015_individual.txt","2015_team_analysis2015.txt"),
 ("2013_probability2013_individual.txt","2015_team_probability2015.txt"),
]
for a,b in pairs:
    na, nb = norm(raw(a)), norm(raw(b))
    r = lcs(na, nb, 40)
    print("=== %s  <->  %s" % (a,b))
    print("  longest shared normalized run: %s chars" % (len(r) if r else 0))
    if r: print("  >>>", r[:400])
    print()
