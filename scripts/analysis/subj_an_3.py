
import os
B = r".\reports"
def show(f, a, b):
    lines=open(os.path.join(B,f),encoding="utf-8",errors="replace").read().split("\n")
    print(f"----- {f} lines {a}-{b} -----")
    for i in range(a-1, min(b,len(lines))):
        print(f"{i+1:4d}| {lines[i]}")
show("report_2019_2021.md", 52, 70)
show("report_2019_2021.md", 237, 290)
show("report_2019_2021.md", 352, 412)
show("report_2019_2021.md", 412, 501)
