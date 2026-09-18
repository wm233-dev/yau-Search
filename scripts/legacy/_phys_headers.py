# -*- coding: utf-8 -*-
"""Physics-corpus focused quantitative analysis (author: subject report agent)."""
import json, os, re, sys, glob
sys.stdout.reconfigure(encoding='utf-8')
TXT = './corpus/prelim/'

files = sorted(os.listdir(TXT))
print('TOTAL TXT:', len(files))
print()
# 1) headers / instruction lines of every paper file
print('### First-6-nonempty-lines of every paper file, by year')
for f in files:
    y = f[:4]
    if not y.isdigit():
        continue
    txt = open(TXT + f, encoding='utf-8', errors='replace').read()
    lines = [l.strip() for l in txt.splitlines() if l.strip() and not l.strip().startswith('=== page')]
    head = ' || '.join(lines[:5])
    flags = []
    if re.search(r'solve every problem', txt, re.I): flags.append('SOLVE-EVERY')
    if re.search(r'point', txt, re.I): flags.append('points?')
    if re.search(r'\bsoln\b|Solution', txt): flags.append('sol-word')
    print(f'{y} | {f[:60]:60s} | {" ".join(flags):28s} | {head[:150]}')
