
import os,re
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
for f in ["2021_Solution_21S_analysis_and_differential_21s_soln.txt","2022_Solution_2022_analysis_and_differential_22s_soln.txt"]:
    s=open(os.path.join(TXT,f),encoding="utf-8",errors="replace").read()
    ctrl=set(ch for ch in s if ord(ch)<32 and ch not in "\n\r\t")
    print("="*70); print(f, "len",len(s), "ctrl chars:", [hex(ord(c)) for c in sorted(ctrl)])
    s2 = "".join(("[#%02X]"%ord(c)) if (ord(c)<32 and c not in "\n\r\t") else c for c in s)
    print(s2[:9000])
