
# -*- coding: utf-8 -*-
import json, re, itertools, collections
P=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_probs2.json",encoding="utf-8"))
def toks(t):
    t=t.lower()
    t=re.sub(r"[\U0001D400-\U0001D7FF]","",t)
    t=re.sub(r"[^a-z0-9]+"," ",t); return t.split()
items=[]
for k,v in P.items():
    y=int(k[:4]); part=k[4:]
    for n,txt in v:
        items.append({"y":y,"p":part,"n":n,"t":txt,"w":toks(txt)})
def sh(ws,k=4): return set(tuple(ws[i:i+k]) for i in range(len(ws)-k+1))
for it in items: it["s"]=sh(it["w"])
pairs=[]
for a,b in itertools.combinations(items,2):
    if not a["s"] or not b["s"]: continue
    inter=len(a["s"]&b["s"])
    if inter<3: continue
    pairs.append((inter/len(a["s"]|b["s"]), inter, a, b))
pairs.sort(key=lambda x:-x[0])
print("TOP PAIRS (4-gram Jaccard, inter>=3)")
for j,inter,a,b in pairs[:30]:
    print(f"  J={j:.3f} sh={inter:2d}  {a['y']}{a['p']}Q{a['n']}  <->  {b['y']}{b['p']}Q{b['n']}")
# explicit checks
def find(y,p,n):
    for it in items:
        if it["y"]==y and it["p"]==p and it["n"]==n: return it
for (y1,p1,n1,y2,p2,n2) in [(2022,"I",4,2026,"I",4),(2016,"T",6,2026,"I",5),(2015,"I",3,2017,"I",3),
                            (2015,"I",1,2018,"I",1),(2016,"T",2,2018,"T",1),(2014,"T",6,2016,"I",2),
                            (2011,"T",6,2015,"I",6),(2013,"I",4,2018,"I",6),(2012,"T",6,2016,"T",5),
                            (2013,"I",2,2013,"T",3),(2012,"I",4,2013,"I",1),(2010,"I",5,2013,"I",5)]:
    a=find(y1,p1,n1); b=find(y2,p2,n2)
    if not a or not b: print("MISSING", y1,p1,n1,y2,p2,n2); continue
    com=sorted(a["s"]&b["s"])
    print(f"\n### {y1}{p1}Q{n1} <-> {y2}{p2}Q{n2}: J={len(com)/max(1,len(a['s']|b['s'])):.3f} shared={len(com)}")
    print("  A:", " ".join(a["w"])[:200])
    print("  B:", " ".join(b["w"])[:200])
    for s in com[:8]: print("     shared:", " ".join(s))
