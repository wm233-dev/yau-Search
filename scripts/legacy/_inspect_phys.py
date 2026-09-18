# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = './data/'
for name in ['problems_enriched.json','papers.json','problems_index.json']:
    d = json.load(open(base + name, encoding='utf-8'))
    print('=====', name, type(d).__name__)
    if isinstance(d, dict):
        ks = list(d.keys())
        print('keys:', ks[:8], '... total', len(ks))
        print('sample:', json.dumps(d[ks[0]], ensure_ascii=False)[:1400])
    else:
        print('len:', len(d))
        print('sample[0]:', json.dumps(d[0], ensure_ascii=False)[:1400])
