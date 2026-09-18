
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("yau_2024_2026_deep_analysis.md", 51, 60)
show("yau_2024_2026_deep_analysis.md", 118, 130)
show("yau_2024_2026_deep_analysis.md", 187, 258)
show("yau_2024_2026_deep_analysis.md", 500, 545)
