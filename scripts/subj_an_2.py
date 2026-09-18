
import os,glob
BASE = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
files = sorted(os.listdir(BASE))
import re
def is_an(f):
    l=f.lower()
    return ("analysis" in l) or ("differential" in l)
sel=[f for f in files if is_an(f)]
tot=0
for f in sel:
    p=os.path.join(BASE,f)
    s=open(p,encoding="utf-8",errors="replace").read()
    tot+=len(s)
    print(f"{len(s):7d}  {f}")
print("TOTAL", tot, "files", len(sel))
