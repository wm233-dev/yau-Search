# -*- coding: utf-8 -*-
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = './data/'
enr = json.load(open(base + 'problems_enriched.json', encoding='utf-8'))
# also full text
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))
print('problems_full type', type(full).__name__, len(full))
if isinstance(full, list):
    print(json.dumps(full[0], ensure_ascii=False)[:600])
