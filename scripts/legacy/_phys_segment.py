# -*- coding: utf-8 -*-
import re, sys, json
sys.stdout.reconfigure(encoding='utf-8')
TXT = './corpus/prelim/'
PHYS = {
 '2022': '2022_ExamPaper_2022_Mathematical_Physics_22s.txt',
 '2023': '2023_Mathematical_Physics.txt',
 '2024': '2024_2024_Math_physics.txt',
 '2025': '2025_physics.txt',
 '2026': '2026_2026_physics.txt',
}
def load(f):
    t = open(TXT+f, encoding='utf-8', errors='replace').read()
    t = re.sub(r'=== page \d+ ===', ' ', t)
    return t

def segment(y, t):
    if y in ('2025','2026'):
        marks = [m for m in re.finditer(r'Problem\s+([1-6])\.', t)]
    else:
        marks = [m for m in re.finditer(r'(?m)^\s*([1-6])\.\s+(?=[A-Z(])', t)]
    out = {}
    for i, m in enumerate(marks):
        n = int(m.group(1))
        end = marks[i+1].start() if i+1 < len(marks) else len(t)
        out[n] = t[m.end():end].strip()
    return out

VERBS = ['prove','show that','show','derive','compute','calculate','find','determine','solve',
         'explain','write down','verify','estimate','evaluate','construct','describe','check','discuss','obtain','interpret','list','state']

allsegs = {}
print('year | Q | chars | words | subpart-letters | numbered-items | verbs')
for y, f in PHYS.items():
    t = load(f)
    segs = segment(y, t)
    allsegs[y] = segs
    print('#'*70)
    print(f'### {y}: segmented {len(segs)} problems; total chars={sum(len(v) for v in segs.values())}')
    for n in sorted(segs):
        s = segs[n]
        lets = re.findall(r'\(([a-h])\)', s)
        rom = re.findall(r'(?m)^\s*(i{1,3}|iv)\.\s', s)
        items = re.findall(r'(?m)^\s*(\d)\.\s+[A-Z(]', s)
        vd = {}
        for v in VERBS:
            c = len(re.findall(r'(?i)\b' + v + r'\b', s))
            if c: vd[v] = c
        print(f'  {y} Q{n}: chars={len(s):5d} words={len(s.split()):4d} letters={len(lets)}({len(set(lets))}) roman={len(rom)} items={len(items)} verbs={vd}')
        print(f'      head: {s[:110].replace(chr(10)," ")}')

json.dump({y: {str(k): v for k, v in s.items()} for y, s in allsegs.items()},
          open('./scripts/_phys_segs.json','w',encoding='utf-8'),
          ensure_ascii=False, indent=1)
print()
print('saved segments -> ./scripts/_phys_segs.json')
