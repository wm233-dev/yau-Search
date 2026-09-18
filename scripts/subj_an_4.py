
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("stats_2022_2023.md", 69, 80)
show("stats_2022_2023.md", 135, 146)
show("stats_2022_2023.md", 192, 340)
show("stats_2022_2023.md", 450, 579)
