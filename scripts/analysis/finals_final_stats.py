# -*- coding: utf-8 -*-
"""总决赛 ALG/ANA 最终统计（PDF 主集 + 恢复集）。输出到 _finals_final_stats.txt"""
import sys, os, re, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from finals_alg_ana_problems import P
from finals_alg_ana_extras import E
ROOT = r'.'
TXT = os.path.join(ROOT, 'txt_finals')
mL = []
def norm(rec, src):
    y, s, k, no, desc, tags, meth, d = rec[:8]
    try: d = int(d)
    except Exception: d = None
    return dict(y=y, s=s, k=k, no=no, desc=desc, tags=[t.strip() for t in tags.split(',')], meth=meth, d=d, src=src)
A = [norm(r, 'pdf') for r in P]
B = [norm(r, 'doc') for r in E]
ALL = A + B
buf = []
def o(*a):
    line = ' '.join(str(x) for x in a); buf.append(line)

# 1) 规模
o('## 1 规模')
o('PDF 主集: %d 卷 / %d 题' % (len(set((x['y'], x['s'], x['k']) for x in A)), len(A)))
o('恢复集(doc/docx): %d 卷 / %d 题' % (len(set((x['y'], x['s'], x['k']) for x in B)), len(B)))
o('合计: %d 卷 / %d 题' % (len(set((x['y'], x['s'], x['k']) for x in ALL)), len(ALL)))
o('')

# 2) 卷别
o('## 2 卷别对比（主集 -> 含恢复集）')
for g in ('Individual', 'Team', 'Overall'):
    a = [x for x in A if x['k'] == g]; b = [x for x in ALL if x['k'] == g]
    da = [x['d'] for x in a if x['d']]; db = [x['d'] for x in b if x['d']]
    na = len(set((x['y'], x['s'], x['k']) for x in a)); nb = len(set((x['y'], x['s'], x['k']) for x in b))
    o('%-11s 卷 %2d->%2d  题 %3d->%3d  平均题/卷 %.2f->%.2f  难度均值 %.2f->%.2f  难度>=4 %2d%%->%2d%%' % (
        g, na, nb, len(a), len(b), len(a)/na, len(b)/nb,
        sum(da)/len(da), sum(db)/len(db),
        100*sum(1 for d in da if d >= 4)//len(da), 100*sum(1 for d in db if d >= 4)//len(db)))
o('')

# 3) 科目 x 卷别
o('## 3 科目 x 卷别（含恢复集）')
for s in ('ALG', 'ANA'):
    for g in ('Individual', 'Team', 'Overall'):
        it = [x for x in ALL if x['s'] == s and x['k'] == g]
        if not it: continue
        dd = [x['d'] for x in it if x['d']]
        o('%-4s %-11s 题=%3d 难度均值=%.2f 分布1..5=%s' % (s, g, len(it), sum(dd)/len(dd),
            [sum(1 for d in dd if d == i) for i in range(1, 6)]))
o('')

# 4) 考点频次（主集 / 恢复 / 合计）
o('## 4 考点频次（合)')
tc = collections.Counter(); ty = collections.defaultdict(set); ts = collections.defaultdict(collections.Counter)
tA = collections.Counter(); tB = collections.Counter()
for x in ALL:
    for t in x['tags']:
        if t in ('—',): continue
        tc[t] += 1; ty[t].add(x['y']); ts[t][x['s']] += 1
        (tA if x['src'] == 'pdf' else tB)[t] += 1
o('| 考点 | 题次 | 主集 | 恢复 | ALG | ANA | 年份 |')
o('|---|---|---|---|---|---|---|')
for t, c in tc.most_common():
    yrs = sorted(ty[t])
    ys = ','.join(str(v)[2:] for v in yrs) if len(yrs) <= 20 else '%d-%d' % (min(yrs), max(yrs))
    o('| %s | %d | %d | %d | %d | %d | %s |' % (t, c, tA[t], tB[t], ts[t]['ALG'], ts[t]['ANA'], ys))
o('')

# 5) 年份 x 卷别 覆盖
o('## 5 年份 x 卷别 题数')
o('| 年份 | ALG-Ind | ALG-Team | ALG-Ov | ANA-Ind | ANA-Team | ANA-Ov | 合计 |')
o('|---|---|---|---|---|---|---|---|')
for y in sorted(set(x['y'] for x in ALL)):
    row = []
    for s in ('ALG', 'ANA'):
        for g in ('Individual', 'Team', 'Overall'):
            row.append(str(len([x for x in ALL if x['y'] == y and x['s'] == s and x['k'] == g])))
    tot = len([x for x in ALL if x['y'] == y])
    o('| %d | %s | %d |' % (y, ' | '.join(row), tot))
o('')

# 6) 难度分布
o('## 6 难度分布')
dd = [x['d'] for x in ALL if x['d']]
o('合计 n=%d  1:%d 2:%d 3:%d 4:%d 5:%d  均值=%.2f' % (len(dd), *[sum(1 for d in dd if d == i) for i in range(1,6)], sum(dd)/len(dd)))
for s in ('ALG', 'ANA'):
    d2 = [x['d'] for x in ALL if x['s'] == s and x['d']]
    o('%-4s n=%d 均值=%.2f' % (s, len(d2), sum(d2)/len(d2)))
o('')

# 7) 前十难
o('## 7 难度=5 的题')
for x in ALL:
    if x['d'] == 5:
        o('  %d %s %s #%s  %s' % (x['y'], x['s'], x['k'], x['no'], x['desc'][:70]))
open(os.path.join(ROOT, 'data', '_finals_final_stats.txt'), 'w', encoding='utf-8').write('\n'.join(buf))
print('\n'.join(buf))
