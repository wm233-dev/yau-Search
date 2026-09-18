# -*- coding: utf-8 -*-
import re, sys, json
sys.stdout.reconfigure(encoding='utf-8')
TXT = './corpus/prelim/'
t = open(TXT+'2022_Solution_2022_Mathematical_Physics_solution.txt', encoding='utf-8', errors='replace').read()
t = re.sub(r'=== page \d+ ===', ' ', t)
# split by problem
marks = [m for m in re.finditer(r'(?m)^\s*([1-6])\.\s*\n?', t)]
print('problem marks:', [m.group(1) for m in marks])
tot = 0; npts = 0
for i, m in enumerate(marks):
    end = marks[i+1].start() if i+1 < len(marks) else len(t)
    seg = t[m.end():end]
    pts = [int(x) for x in re.findall(r'\((\d+)\s*points?\)', seg)]
    print(f'Problem {m.group(1)}: points={pts} sum={sum(pts)} n={len(pts)}')
    tot += sum(pts); npts += len(pts)
print('TOTAL points =', tot, ' total graded subparts =', npts)
print('5-point items:', sum(1 for m in re.finditer(r'\(5 points\)', t)), ' 10-point items:', sum(1 for m in re.finditer(r'\(10 points\)', t)))
print('chars of solution file:', len(t))
print('pages:', len(re.findall(r'=== page', open(TXT+'2022_Solution_2022_Mathematical_Physics_solution.txt',encoding='utf-8',errors='replace').read())))
