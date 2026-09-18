# -*- coding: utf-8 -*-
"""总决赛 vs 笔试：卷面形式关键词、题长代理、题量对比。"""
import sys, os, re, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from finals_alg_ana_problems import P
ROOT = r'.'
TXT = os.path.join(ROOT, 'txt_finals')
m = json.load(open(os.path.join(ROOT, 'data', '_finals_txtmap.json'), encoding='utf-8'))
sel = [(k, v) for k, v in m.items() if ('Algebra' in v['subj']) or ('Analysis' in v['subj'])]

def rawof(subj, kind, year):
    for k, v in sel:
        tag = 'ALG' if 'Algebra' in v['subj'] else 'ANA'
        if tag == subj and v['kind'] == kind and v['year'] == str(year):
            return open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    return ''

print('### 卷面形式关键词（67 卷全文，出现卷数与次数）')
KW = ['oral', 'Oral', 'ORAL', 'Individual', 'Team', 'Overall', 'All-round', 'All around', 'around',
      'Solution', 'Solution to', 'Group Contest', 'Group Test', 'Final Contest', 'Please solve']
c1 = collections.Counter(); c2 = collections.Counter()
for k, v in sel:
    raw = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    for w in KW:
        n = raw.count(w)
        if n: c1[w] += 1; c2[w] += n
for w in KW:
    print('  %-16s 卷数=%2d 次数=%3d' % (w, c1[w], c2[w]))

print()
print('### 含官方解答的卷（出现 "Solution to Problem"）')
sol = [ (v['year'], v['kind'], 'ALG' if 'Algebra' in v['subj'] else 'ANA')
        for k, v in sel if 'Solution to Problem' in open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read() ]
for s in sorted(sol): print('  ', s)

print()
print('### 题长代理（英文词/题），剔除含官方解答的 2021 代数两卷')
tot = collections.Counter(); cnt = collections.Counter()
for (y, s, k, no, desc, tags, meth, d) in P:
    if (y, s) == (2021, 'ALG') and k in ('Individual', 'Overall'): continue
    raw = rawof(s, k, y)
    pass
for key in [('ALG', None), ('ANA', None)] + [(s, g) for s in ('ALG', 'ANA') for g in ('Individual', 'Team', 'Overall')]:
    s, g = key
    np_ = 0; wd = 0
    for (y, ss, k), _ in collections.Counter((x[0], x[1], x[2]) for x in P).items():
        if ss != s or (g and k != g): continue
        if (y, ss) == (2021, 'ALG'): continue   # 含官方解答，剔除
        raw = rawof(ss, k, y)
        np_ += len([x for x in P if x[0] == y and x[1] == ss and x[2] == k])
        wd += len(re.findall(r'[A-Za-z]+', raw))
    print('  %-4s %-11s 题数=%3d 词数=%6d 平均词/题=%.1f' % (s, g or 'ALL', np_, wd, wd / np_))

print()
print('### 与笔试语料对比（来源：reports/problem_metrics.md，2010-2026 笔试）')
print('  笔试 ALG 129 题 平均 84 词/题 平均小问 1.74 难度代理 2.64')
print('  笔试 ANA 134 题 平均 49 词/题 平均小问 0.51 难度代理 1.72')
