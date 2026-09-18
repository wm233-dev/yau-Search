# -*- coding: utf-8 -*-
import re, os
SRC = r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Analysis and Differential Equations\Individual\2012 Analysis (Individual).doc'
raw = open(SRC, 'rb').read()
WORDS = ['the', 'that', 'prove', 'show', 'function', 'let', 'all', 'for', 'and', 'solution', 'problem', 'converge', 'series']
def sc(s):
    return sum(len(re.findall(r'\b' + w + r'\b', s, re.I)) for w in WORDS)
cands = {}
for off in (0, 1):
    for enc in ('utf-16-le', 'utf-16-be'):
        s = raw[off:].decode(enc, 'ignore')
        cands['%s+%d' % (enc, off)] = s
        cands['swap_' + enc + '+%d' % off] = ''.join(
            chr(((ord(c) & 0xFF) << 8) | (ord(c) >> 8)) if ord(c) < 0x10000 else c for c in s)
for k, v in sorted(cands.items(), key=lambda kv: -sc(kv[1]))[:4]:
    print('%-18s score=%4d len=%d' % (k, sc(v), len(v)))
    print('   ', v[:300].replace('\n', ' | '))
