
# -*- coding: utf-8 -*-
import json, re, collections
P=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_probs2.json",encoding="utf-8"))
NP = {2010:12,2011:12,2012:12,2013:12,2014:12,2015:12,2016:12,2017:12,2018:11,2019:10,2020:6,2021:6,2022:6,2023:6,2024:5,2025:6,2026:5}
rows=collections.defaultdict(lambda: {"n":0,"chars":0,"sub":0,"judge":0,"hint":0,"prove":0,"show":0,"calc":0,"subprob":0})
for k,v in P.items():
    y=int(k[:4]); part=k[4:]
    for n,txt in v:
        r=rows[y]; r["n"]+=1; r["chars"]+=len(txt)
        sa=len(re.findall(r"(?m)^\s*\(?[a-j][\)\.]", txt))
        s1=len(re.findall(r"(?m)^\s*\(?[1-9][\)\.]", txt))
        r["sub"]+=sa+s1
        if re.search(r"does there exist|is there|can you|is it true|prove or disprove|is the (above )?claim|are there|does the", txt, re.I): r["judge"]+=1
        if "Hint" in txt: r["hint"]+=1
        low=txt.lower()
        r["prove"]+=len(re.findall(r"\bprove(?:s|d)?\b", low))
        r["show"]+=len(re.findall(r"\bshow(?:s|n)?\b", low))
        r["calc"]+=len(re.findall(r"\b(compute|calculate|derive|find|determine|evaluate)\w*\b", low))
print("| 年份 | 题数 | 总字符 | 字符/题 | 小问总数 | 小问/题 | 判定型题 | Hint 题 | 含prove | 含show | 计算类动词 |")
tot=collections.Counter()
for y in sorted(rows):
    r=rows[y]
    for k in r: tot[k]+=r[k]
    print(f"| {y} | {r['n']} | {r['chars']} | {r['chars']/r['n']:.0f} | {r['sub']} | {r['sub']/r['n']:.2f} | {r['judge']} | {r['hint']} | {r['prove']} | {r['show']} | {r['calc']} |")
print("TOTAL", dict(tot), "avg chars/problem", round(tot['chars']/tot['n'],1), "sub/题", round(tot['sub']/tot['n'],2))
# period aggregates
for lo,hi in [(2010,2013),(2014,2018),(2019,2021),(2022,2026),(2010,2026)]:
    c=sum(rows[y]["chars"] for y in rows if lo<=y<=hi); n=sum(rows[y]["n"] for y in rows if lo<=y<=hi)
    s=sum(rows[y]["sub"] for y in rows if lo<=y<=hi)
    print(f"  {lo}-{hi}: n={n} chars/prob={c/n:.0f} sub/prob={s/n:.2f}")
