
# -*- coding: utf-8 -*-
import json, re, itertools, collections
P=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_probs2.json",encoding="utf-8"))
def toks(t):
    t=t.lower(); t=re.sub(r"[^a-z0-9]+"," ",t); return t.split()
items=[]
for k,v in P.items():
    y=int(k[:4]); part=k[4:]
    for n,txt in v:
        items.append({"y":y,"p":part,"n":n,"t":txt,"w":toks(txt)})
def sh(ws,k=5): return set(tuple(ws[i:i+k]) for i in range(len(ws)-k+1))
for it in items: it["s"]=sh(it["w"])
pairs=[]
for a,b in itertools.combinations(items,2):
    if not a["s"] or not b["s"]: continue
    inter=len(a["s"]&b["s"])
    if inter<4: continue
    pairs.append((inter/len(a["s"]|b["s"]), inter, a, b))
pairs.sort(key=lambda x:-x[0])
print("PROBLEM-LEVEL TOP PAIRS (5-gram Jaccard, analysis only), shared>=4")
for j,inter,a,b in pairs[:25]:
    print(f"  J={j:.3f} sh={inter:2d}  {a['y']}{a['p']}Q{a['n']}  <->  {b['y']}{b['p']}Q{b['n']}")
print("\n--- detail of top 12 ---")
for j,inter,a,b in pairs[:12]:
    com=sorted(a["s"]&b["s"])
    print(f"\n=== {a['y']}{a['p']}Q{a['n']} <-> {b['y']}{b['p']}Q{b['n']}  J={j:.3f} ===")
    print("  A:", " ".join(a["w"])[:230])
    print("  B:", " ".join(b["w"])[:230])
    for s in com[:6]: print("     shared:", " ".join(s))
