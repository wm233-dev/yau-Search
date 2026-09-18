# -*- coding: utf-8 -*-
import json, re, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')
segs = json.load(open('E:/deepseek_exclusive/math/.tmp/burn2026/scripts/_phys_segs.json', encoding='utf-8'))
VERBS = ['prove','proof','show that','show','derive','compute','calculate','find','determine','solve',
         'explain','write down','verify','estimate','evaluate','construct','describe','check','discuss','obtain','interpret','list','state']
tab = {}
for y in sorted(segs):
    text = ' '.join(segs[y][n] for n in segs[y])
    d = {}
    for v in VERBS:
        # avoid double counting 'show' inside 'show that': count separately
        c = len(re.findall(r'(?i)\b' + v + r'\b', text))
        if c: d[v] = c
    tab[y] = d
    print(y, d, ' total verbs =', sum(d.values()))
print()
print('verb | ' + ' | '.join(sorted(tab)))
for v in VERBS:
    row = [str(tab[y].get(v,0)) for y in sorted(tab)]
    if sum(int(x) for x in row):
        print(f'{v:12s} | ' + ' | '.join(row) + '  | sum=' + str(sum(int(x) for x in row)))
