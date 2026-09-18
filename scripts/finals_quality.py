# -*- coding: utf-8 -*-
"""Classify finals (geo/prob) txt files by text-layer quality."""
import json, os

BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
gp = json.load(open(os.path.join(BASE, 'data', 'geoprob_map.json'), encoding='utf-8'))
TXT = os.path.join(BASE, 'txt_finals')

def classify(t):
    t = t.strip()
    n = len(t)
    if n < 50:
        return 'EMPTY', n, 0, 0
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    cjk = sum(1 for c in t if '\u4e00' <= c <= '\u9fff')
    if n and ctrl / n > 0.08:
        return 'GARBLED', n, ctrl, cjk
    return 'OK', n, ctrl, cjk

if __name__ == '__main__':
    rows = []
    for x in gp:
        t = open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
        tag, n, ctrl, cjk = classify(t)
        rows.append((tag, n, ctrl, cjk, x['year'], x['kind'], x['file']))
    for tag in ('EMPTY', 'GARBLED', 'OK'):
        sel = [r for r in rows if r[0] == tag]
        print(f'== {tag}: {len(sel)}')
        for r in sel:
            print(f'   n={r[1]:5d} ctrl={r[2]:4d} cjk={r[3]:4d} {r[4]} {r[5]} {r[6]}')
