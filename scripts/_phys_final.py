# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
TXT='E:/deepseek_exclusive/math/.tmp/burn2026/txt/'
files = sorted(f for f in os.listdir(TXT) if f.endswith('.txt'))
print('### files containing Chinese char 说明')
for f in files:
    t = open(TXT+f, encoding='utf-8', errors='replace').read()
    if '说明' in t: print('  ', f)
print()
print('### 2022 physics paper header (first 12 non-empty lines)')
t = open(TXT+'2022_ExamPaper_2022_Mathematical_Physics_22s.txt', encoding='utf-8', errors='replace').read()
print('\n'.join([l for l in t.splitlines() if l.strip()][:10]))
print()
print('### declared problem counts per paper 2024-2026')
for f in files:
    if f[:4] in ('2024','2025','2026'):
        t = open(TXT+f, encoding='utf-8', errors='replace').read()
        m = re.search(r'\((\d+)\s*problems?\)', t, re.I)
        print(f'  {f[:55]:55s} declared={m.group(1) if m else "-"}')
