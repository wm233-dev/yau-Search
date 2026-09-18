# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))
for p in full:
    if p['subject']=='Mathematical Physics' and p['year'] in ('2025','2026'):
        print('='*60)
        print(p['year'], 'Q'+str(p['n']), 'chars=', p['chars'])
        print(p['text'][:260].replace('\n',' '))
