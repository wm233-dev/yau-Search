# -*- coding: utf-8 -*-
"""Emit the markdown tables used in reports/finals_geo_prob.md."""
import json, io, os, re, collections, statistics, itertools

BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
DATA = os.path.join(BASE, 'data')
geo = json.load(io.open(os.path.join(DATA, 'finals_geo_problems.json'), encoding='utf-8'))
prob = json.load(io.open(os.path.join(DATA, 'finals_prob_problems.json'), encoding='utf-8'))
for r in geo: r['subject'] = 'G'
for r in prob: r['subject'] = 'P'
allp = geo + prob
idx = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))

out = []
P = out.append
YEARS = [str(y) for y in range(2012, 2026)]
for subj, tag in (('Geometry and Topology', 'G'), ('Probability and Statistics', 'P')):
    P('### presence matrix %s' % tag)
    P('| 年份 | Individual | Team | Overall |')
    P('|---|---|---|---|')
    for y in YEARS:
        cells = []
        for k in ('Individual', 'Team', 'Overall'):
            hit = [x for x in idx if y == x['year'] and x['kind'] == k and subj in x['subj']]
            cells.append('有' if hit else '—')
        P('| %s | %s | %s | %s |' % (y, cells[0], cells[1], cells[2]))

P('')
P('### topic freq table')
tf = collections.defaultdict(list)
for r in allp:
    tf[r['topic']].append(r)
rows = sorted(tf.items(), key=lambda kv: (-len(kv[1]), kv[0]))
P('| 考点 | 题次 | 科目 | 出现年份 | 卷别分布 |')
P('|---|---|---|---|---|')
for t, rs in rows:
    yrs = sorted({r['year'] for r in rs})
    kd = collections.Counter(r['kind'] for r in rs)
    subj = '几何' if all(r['subject'] == 'G' for r in rs) else ('概率' if all(r['subject'] == 'P' for r in rs) else '混合')
    P('| %s | %d | %s | %s | I%d/T%d/O%d |' % (t, len(rs), subj, ','.join(yrs),
       kd.get('Individual', 0), kd.get('Team', 0), kd.get('Overall', 0)))
P('')
P('### per-year table')
P('| 年份 | 题数 | 平均自评难度 | 几何题 | 概率题 | I/T/O |')
P('|---|---|---|---|---|---|')
for y in YEARS:
    rs = [r for r in allp if r['year'] == y]
    kd = collections.Counter(r['kind'] for r in rs)
    P('| %s | %d | %.2f | %d | %d | %d/%d/%d |' % (
        y, len(rs), statistics.mean([r['diff'] for r in rs]),
        sum(1 for r in rs if r['subject'] == 'G'), sum(1 for r in rs if r['subject'] == 'P'),
        kd.get('Individual', 0), kd.get('Team', 0), kd.get('Overall', 0)))
P('')
P('### per paper table (year, kind, file, n, mean diff)')
for subj, tag in (('G', 'GEO'), ('P', 'PROB')):
    P('-- %s --' % tag)
    grp = collections.defaultdict(list)
    for r in allp:
        if r['subject'] == subj:
            grp[(r['year'], r['kind'], r['paper'])].append(r)
    for (y, k, paper), rs in sorted(grp.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2])):
        P('| %s | %s | %s | %d | %.2f | %s |' % (y, k, paper, len(rs),
          statistics.mean([r['diff'] for r in rs]), '; '.join(r['topic'] for r in rs)))
P('')
P('### duplicate / repeated content (gist 4-gram jaccard >= 0.35)')
def sh(t, n=4):
    w = re.findall(r'[\u4e00-\u9fff]|[A-Za-z]+', t.lower())
    return {tuple(w[i:i+n]) for i in range(max(0, len(w)-n+1))}
shs = [(r, sh(r['gist'])) for r in allp]
dups = []
for (a, sa), (b, sb) in itertools.combinations(shs, 2):
    if not sa or not sb: continue
    j = len(sa & sb)/len(sa | sb)
    if j >= 0.35:
        dups.append((round(j, 2), '%s %s Q%d' % (a['year'], a['kind'], a['n']), '%s %s Q%d' % (b['year'], b['kind'], b['n'])))
for d in sorted(dups, reverse=True):
    P('   %s  %s  <->  %s' % d)
io.open(os.path.join(BASE, 'scripts', '_finals_tables.md'), 'w', encoding='utf-8').write('\n'.join(out))
print('\n'.join(out))
