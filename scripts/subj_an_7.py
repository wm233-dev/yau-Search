
import os,re
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
lines=open(os.path.join(B,"yau_2013-2015_analysis.md"),encoding="utf-8",errors="replace").read().split("\n")
# print lines containing 分析 in the structural tables
for i,l in enumerate(lines,1):
    if ("分析" in l) or ("Analysis" in l):
        print(f"{i:4d}| {l}")
