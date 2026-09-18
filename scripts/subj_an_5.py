
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("yau_2024_2026_deep_analysis.md", 285, 500)
show("stats_2024_2026.md", 112, 142)
