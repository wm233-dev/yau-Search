# -*- coding: utf-8 -*-
"""Crude text recovery from legacy .doc by scanning 1-byte and UTF-16LE runs."""
import os, re

def runs8(data, minlen=8):
    out, cur = [], []
    for b in data:
        if 0x20 <= b <= 0x7e:
            cur.append(chr(b))
        else:
            if len(cur) >= minlen:
                out.append(''.join(cur))
            cur = []
    if len(cur) >= minlen:
        out.append(''.join(cur))
    return out

p = r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Geometry and Topology\Individual\2014 Geometry (Individual&Overall).doc'
data = open(p, 'rb').read()
print('size', len(data))
rs = runs8(data)
print('runs8:', len(rs))
for r in rs:
    if len(r) >= 12 and not re.search(r'(Microsoft|Times New|Cambria|Calibri|Symbol|Root Entry|WordDocument|SummaryInformation|ObjectPool|CompObj|Arial|SimSun|Euclid|CMBX|Normal\.|Word\.|Table)', r):
        print('  |', r)
