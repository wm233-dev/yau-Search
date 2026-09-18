
import os
B = r".\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("yau_2013-2015_analysis.md", 61, 80)
show("yau_2013-2015_analysis.md", 203, 310)
show("yau_2013-2015_analysis.md", 585, 651)
