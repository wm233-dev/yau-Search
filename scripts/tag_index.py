
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
F = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\tag_problems.txt"
txt = open(F, encoding='utf-8').read()
for sec in txt.split("="*90):
    lines = [l for l in sec.strip().split("\n") if l.strip()]
    if not lines or not lines[0].startswith("##"): continue
    heads = [l.strip() for l in lines if l.strip().startswith("[")]
    print(lines[0])
    print("   " + " | ".join(heads))
