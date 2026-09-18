
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 81, 107)
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 159, 172)
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 211, 224)
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 289, 315)
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 570, 587)
show("2010-2012_丘成桐竞赛笔试真题深度分析.md", 780, 845)
