
import re, os, json
src=open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_twins2.py",encoding='utf-8').read()
exec(src.split("keys=list(store)")[0])
json.dump({f"{k[0]}|{k[1]}|{k[2]}":v for k,v in store.items()}, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_bodies.json","w"), ensure_ascii=False, indent=1)
print("saved", len(store), "bodies")
pats={
 "prove_or_disprove": r"prove or disprove|disprove",
 "judge/Q-form": r"true or false|is it true|do you agree|does[^.?]{0,60}\?|is the[^.?]{0,60}\?|can[^.?]{0,60}\?|which (one )?is|are they|must ",
 "counterexample": r"counter[- ]?example|give a counter",
 "justify/argue/explain": r"justify|argue|reasoning|explain why|discuss",
 "Hint": r"\bHint\b",
 "exact/explicit": r"exact|explicit",
 "asymptotic/limiting": r"asymptotic|limiting distribution|in distribution|O_p|O\(n|large sample|as n ",
 "compute/derive/determine": r"\bcompute\b|\bcalculate\b|\bderive\b|\bdetermine\b|\bevaluate\b",
 "construct/provide/give example": r"\bconstruct\b|\bprovide\b|give an example",
 "simulation": r"simulat",
 "prove/show": r"\bprove\b|\bshow\b",
 "find": r"\bfind\b",
}
yrs=sorted({k[0] for k in store})
print(f"{'yr':5s}"+"".join(f"{k[:12]:>14s}" for k in pats)+f"{'n':>5s}")
tot={k:0 for k in pats}
for y in yrs:
    keys=[k for k in store if k[0]==y]
    line=f"{y:5s}"
    for k,p in pats.items():
        c=sum(1 for kk in keys if re.search(p, store[kk], re.I))
        tot[k]+=c; line+=f"{c:>14d}"
    print(line+f"{len(keys):>5d}")
print(f"{'TOT':5s}"+"".join(f"{tot[k]:>14d}" for k in pats))
for name,ys in [("2010-2012",{"2010","2011","2012"}),("2013-2015",{"2013","2014","2015"}),("2016-2018",{"2016","2017","2018"}),("2019-2021",{"2019","2020","2021"}),("2022-2026",{"2022","2023","2024","2025","2026"})]:
    keys=[k for k in store if k[0] in ys]
    print(f"{name}: n={len(keys)} "+" ".join(f"{k}={sum(1 for kk in keys if re.search(p,store[kk],re.I))}" for k,p in pats.items()))
