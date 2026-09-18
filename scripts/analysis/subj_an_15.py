
# -*- coding: utf-8 -*-
import os, re, json, collections
exec(open(r".\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])
NP = {2010:12,2011:12,2012:12,2013:12,2014:12,2015:12,2016:12,2017:12,2018:11,2019:10,2020:6,2021:6,2022:6,2023:6,2024:5,2025:6,2026:5}
VERBS=["prove","show","derive","compute","calculate","find","determine","construct","verify","state","solve","give","explain","justify","check","estimate","establish","describe"]
rows={}
for y in sorted(NP):
    txt = "\n".join(t for (yy,p),t in sorted(secs.items()) if yy==y)
    txt = re.sub(r"S\.-T\.? Yau College Student Mathematics Contests \d+\s*","",txt)
    txt = re.sub(r"Analysis and Di\w* Equations\s*","",txt)
    txt = re.sub(r"(Individual|Team)\s*","",txt)
    txt = re.sub(r"(Please solve[^\n]*|\((?:Please )?select[^\n]*|Solve every problem\.|\(\d+ problems\))","",txt)
    sa=len(re.findall(r"(?m)^\s*\(?[a-j]\)", txt)); s1=len(re.findall(r"(?m)^\s*\(?[1-9]\)", txt))
    low=txt.lower(); vc={v:len(re.findall(r"\b"+v+r"(?:s|d|ed|ing)?\b",low)) for v in VERBS}
    rows[y]={"n":NP[y],"chars":len(txt),"avg":round(len(txt)/NP[y],1),"sub_a":sa,"sub_1":s1,"verbs":{k:v for k,v in vc.items() if v}}
    print(f"| {y} | {NP[y]} | {len(txt)} | {len(txt)/NP[y]:.1f} | {sa} | {s1} | " + " | ".join(str(vc.get(v,0)) for v in VERBS) + " |")
print()
print("| 年份 | "+" | ".join(VERBS)+" |")
tv=collections.Counter()
for y in sorted(NP):
    for k,v in rows[y]["verbs"].items(): tv[k]+=v
print("TOTALS", dict(tv.most_common()))
json.dump(rows, open(r".\scripts\an_rows2.json","w"), ensure_ascii=False, indent=1)
