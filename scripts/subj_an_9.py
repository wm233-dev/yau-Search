
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("2016-2018_笔试真题深度分析.md", 50, 60)
show("2016-2018_笔试真题深度分析.md", 176, 190)
show("2016-2018_笔试真题深度分析.md", 235, 250)
show("2016-2018_笔试真题深度分析.md", 293, 310)
show("2016-2018_笔试真题深度分析.md", 339, 355)
show("2016-2018_笔试真题深度分析.md", 396, 530)
show("2016-2018_笔试真题深度分析.md", 758, 790)
show("2016-2018_笔试真题深度分析.md", 807, 888)
