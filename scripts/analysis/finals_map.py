# -*- coding: utf-8 -*-
"""Build txt<->original PDF mapping for Yau finals corpus; dump scope files."""
import json, os, re

ROOT = r'.'
IDX = os.path.join(ROOT, 'data', 'finals_index.json')
TXT = os.path.join(ROOT, 'txt_finals')

def norm(s):
    s = re.sub(r'[^A-Za-z0-9]+', '_', s)
    return s.strip('_')

def txtname(a):
    return '_'.join([norm(a['subj']), norm(a['kind']), norm(os.path.splitext(a['file'])[0])]) + '.txt'

def main():
    d = json.load(open(IDX, encoding='utf-8'))
    files = set(os.listdir(TXT))
    ok = miss = 0
    m = {}
    for a in d:
        t = txtname(a)
        if t in files:
            ok += 1
            m[t] = a
        else:
            miss += 1
            print('MISS:', t)
    print('mapped ok=%d miss=%d total=%d' % (ok, miss, len(d)))
    json.dump({k: v for k, v in m.items()}, open(os.path.join(ROOT, 'data', '_finals_txtmap.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

main()
