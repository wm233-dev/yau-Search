# -*- coding: utf-8 -*-
import os, re, sys, json
sys.stdout.reconfigure(encoding='utf-8')
TXT = 'E:/deepseek_exclusive/math/.tmp/burn2026/txt/'

PHYS = {
 '2022': '2022_ExamPaper_2022_Mathematical_Physics_22s.txt',
 '2023': '2023_Mathematical_Physics.txt',
 '2024': '2024_2024_Math_physics.txt',
 '2025': '2025_physics.txt',
 '2026': '2026_2026_physics.txt',
}
SOL = {'2022': '2022_Solution_2022_Mathematical_Physics_solution.txt'}

def strip_pages(t):
    return re.sub(r'=== page \d+ ===', ' ', t)

def body(t):
    # remove header lines up to first problem marker
    return t

for y, f in PHYS.items():
    raw = open(TXT + f, encoding='utf-8', errors='replace').read()
    t = strip_pages(raw)
    n_chars_raw = len(raw)
    print('=' * 78)
    print(f'{y}  file={f}  raw_chars={n_chars_raw}  stripped_chars={len(t)}')
    # find problem starts
    pats = [m for m in re.finditer(r'(?:^|\s)(?:Problem\s+)?(\d)\s*[\.。]\s', t)]
    print('  page markers:', len(re.findall(r'=== page', raw)))
    # count subpart letters
    lets = re.findall(r'\(([a-h])\)', t)
    print('  letter-subparts (a)-(h) count:', len(lets), 'distinct:', sorted(set(lets)))
    nums = re.findall(r'(?:^|\n)\s*(\d)\.\s', t)
    print('  numbered-item count:', len(nums), nums)
    for v in ['prove','show','derive','compute','calculate','find','determine','solve','explain','write down','obtain','verify','estimate','evaluate','construct','describe','check','discuss','argument']:
        c = len(re.findall(r'\b' + v + r'\b', t, re.I))
        if c: print(f'    verb {v:12s} {c}')
