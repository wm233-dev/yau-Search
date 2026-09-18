
import os,re
B = r".\reports"
for f in ["2010-2012_丘成桐竞赛笔试真题深度分析.md","yau_2013-2015_analysis.md","2016-2018_笔试真题深度分析.md","report_2019_2021.md","stats_2022_2023.md","yau_2024_2026_deep_analysis.md","stats_2024_2026.md","problem_metrics.md","theme_clusters.md"]:
    p=os.path.join(B,f)
    lines=open(p,encoding="utf-8",errors="replace").read().split("\n")
    print("="*80)
    print(f, len(lines),"lines")
    for i,l in enumerate(lines,1):
        if re.match(r"^#{1,3} ", l):
            print(f"  {i:5d}  {l[:110]}")
