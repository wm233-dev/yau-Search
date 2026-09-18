
import re,json,statistics as st
rows=json.load(open(r".\scripts\prob_ps_rows_body.json",encoding='utf-8'))
pats={
 "prove_or_disprove": r"prove or disprove|disprove",
 "judge_true_false": r"true or false|is it true|do you agree|does .{0,40}\?|is the .{0,40}\?|can .{0,40}\?|are they|is P\(",
 "counterexample": r"counter[- ]?example|give a counter",
 "justify/argue": r"justify|argue|reasoning|explain why",
 "hint": r"\bHint\b",
 "state/prove named thm": r"state and prove",
 "exact": r"exact|explicit",
 "asymptotic": r"asymptotic|limiting distribution|in distribution|O_p|O\(n|large sample",
 "compute/find numeric": r"\bcompute\b|\bcalculate\b|\bfind\b|\bdetermine\b",
 "construct": r"\bconstruct\b|\bprovide\b|\bgive an example\b",
 "simulation": r"simulat",
}
print("year  " + "".join(f"{k[:9]:>11s}" for k in pats))
tot={k:0 for k in pats}
for y in sorted({r['year'] for r in rows}):
    rs=[r for r in rows if r['year']==y]
    line=f"{y}  "
    for k,p in pats.items():
        c=sum(1 for r in rs if re.search(p,r['head'],re.I))
        tot[k]+=c
        line+=f"{c:>11d}"
    print(line, f"  (n={len(rs)})")
print("TOT  "+"".join(f"{tot[k]:>11d}" for k in pats))
# per-year problem counts
print()
print("problems per year:", {y: len([r for r in rows if r['year']==y]) for y in sorted({r['year'] for r in rows})})
