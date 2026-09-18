# -*- coding: utf-8 -*-
"""总决赛 ALG/ANA 统计：逐年逐卷结构、考点频次、卷别差异、题目长度代理指标。"""
import sys, os, re, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from finals_alg_ana_problems import P

ROOT = r'.'
TXT = os.path.join(ROOT, 'txt_finals')
m = json.load(open(os.path.join(ROOT, 'data', '_finals_txtmap.json'), encoding='utf-8'))

def out(*a):
    print(*a)

# ---- 0. 语料映射（卷 -> txt） ----------------------------------------------
def find_txt(subj, kind, year):
    for k, v in m.items():
        tag = 'ALG' if 'Algebra' in v['subj'] else ('ANA' if 'Analysis' in v['subj'] else None)
        if tag == subj and v['kind'] == kind and v['year'] == str(year):
            return k
    return None

papers = collections.OrderedDict()
for (y, s, k, no, desc, tags, meth, d) in P:
    papers.setdefault((y, s, k), []).append((no, desc, tags, meth, d))

out('=' * 90)
out('表 1  逐年逐卷结构（%d 卷 / %d 题）' % (len(papers), len(P)))
out('=' * 90)
out('%-5s %-4s %-11s %5s %6s %7s %8s %7s  %s' % ('Year', 'Subj', 'Kind', 'N题', 'chars', 'words', 'w/prob', 'avgDiff', 'txt'))
tot_chars = 0
for (y, s, k), items in sorted(papers.items()):
    t = find_txt(s, k, y)
    raw = open(os.path.join(TXT, t), encoding='utf-8', errors='replace').read().strip() if t else ''
    words = len(re.findall(r'[A-Za-z]+', raw))
    tot_chars += len(raw)
    out('%-5d %-4s %-11s %5d %6d %7d %8.1f %7.2f  %s' % (
        y, s, k, len(items), len(raw), words, words / len(items), sum(i[4] for i in items) / len(items), t[:60] if t else 'NOT FOUND'))
out('总字符=%d  总英文词=%d' % (tot_chars, sum(len(re.findall(r'[A-Za-z]+', open(os.path.join(TXT, find_txt(s,k,y)), encoding='utf-8', errors='replace').read())) for (y,s,k) in papers if find_txt(s,k,y))))

# ---- 2. 考点频次 ------------------------------------------------------------
out()
out('=' * 90)
out('表 2  子领域标签频次（题次 / 覆盖卷数 / 年份）')
out('=' * 90)
tagc = collections.Counter()
tagy = collections.defaultdict(set)
tagsub = collections.defaultdict(collections.Counter)
for (y, s, k, no, desc, tags, meth, d) in P:
    for t in tags.split(','):
        t = t.strip()
        tagc[t] += 1
        tagy[t].add(y)
        tagsub[t][s] += 1
for t, c in tagc.most_common():
    yrs = sorted(tagy[t])
    out('%-14s 题次=%3d  ALG=%3d ANA=%3d  年份=%s' % (t, c, tagsub[t]['ALG'], tagsub[t]['ANA'],
        ','.join(str(x) for x in yrs) if len(yrs) <= 14 else '%d-%d(%d年)' % (min(yrs), max(yrs), len(yrs))))

out()
out('表 2b  考点 × 年份 矩阵（题次）')
years = sorted(set(y for (y, s, k, *r) in P))
out('| 标签 | ' + ' | '.join(str(y)[2:] for y in years) + ' | 合计 |')
out('|---|' + '---|' * (len(years) + 1))
for t, c in tagc.most_common():
    row = []
    for y in years:
        n = sum(1 for (yy, s, k, no, desc, tags, meth, d) in P if yy == y and t in [x.strip() for x in tags.split(',')])
        row.append(str(n) if n else '.')
    out('| %s | %s | %d |' % (t, ' | '.join(row), c))

# ---- 3. 卷别对比 ------------------------------------------------------------
out()
out('=' * 90)
out('表 3  卷别对比')
out('=' * 90)
for grp in ['Individual', 'Team', 'Overall']:
    items = [x for x in P if x[2] == grp]
    nps = [len(v) for kk, v in papers.items() if kk[2] == grp]
    ws = []
    for (y, s, k), v in papers.items():
        if k != grp: continue
        t = find_txt(s, k, y)
        raw = open(os.path.join(TXT, t), encoding='utf-8', errors='replace').read() if t else ''
        ws.append(len(re.findall(r'[A-Za-z]+', raw)) / len(v))
    dd = [x[7] for x in items]
    out('%-11s 卷数=%2d 题数=%3d 平均题/卷=%.2f 平均词/题=%.1f 难度均值=%.2f 难度≥4占比=%.0f%%' % (
        grp, len(nps), len(items), sum(nps) / len(nps), sum(ws) / len(ws), sum(dd) / len(dd),
        100.0 * sum(1 for d in dd if d >= 4) / len(dd)))

out()
out('表 3b  科目 × 卷别')
for s in ['ALG', 'ANA']:
    for grp in ['Individual', 'Team', 'Overall']:
        items = [x for x in P if x[1] == s and x[2] == grp]
        if not items: continue
        dd = [x[7] for x in items]
        outs = collections.Counter(x[3] for x in items)
        out('%-4s %-11s 题数=%3d 难度均值=%.2f 难度分布(1..5)=%s' % (
            s, grp, len(items), sum(dd) / len(dd), [sum(1 for d in dd if d == i) for i in range(1, 6)]))

# ---- 4. 按年份 --------------------------------------------------------------
out()
out('表 4  按年份（跨卷合计）')
out('| 年份 | 卷数 | 题数 | ALG题 | ANA题 | 平均难度 | 最高难度 |')
out('|---|---|---|---|---|---|---|')
for y in years:
    items = [x for x in P if x[0] == y]
    dd = [x[7] for x in items]
    npp = len(set((x[1], x[2]) for x in items))
    out('| %d | %d | %d | %d | %d | %.2f | %d |' % (y, npp, len(items),
        sum(1 for x in items if x[1] == 'ALG'), sum(1 for x in items if x[1] == 'ANA'),
        sum(dd) / len(dd), max(dd)))

# ---- 5. 题目长度/难度关联 ----------------------------------------------------
out()
out('表 5  难度分布（按卷别/科目）')
for key, items in [('ALL', P)] + [((s + '/' + g), [x for x in P if x[1] == s and x[2] == g]) for s in ('ALG', 'ANA') for g in ('Individual', 'Team', 'Overall')]:
    if not items: continue
    dd = [x[7] for x in items]
    out('%-16s n=%3d  1:%2d 2:%2d 3:%2d 4:%2d 5:%2d  均值=%.2f' % (key, len(items),
        *[sum(1 for d in dd if d == i) for i in range(1, 6)], sum(dd) / len(dd)))

# ---- 6. 年份 × 卷别 覆盖 ----------------------------------------------------
out()
out('表 6  年份 × 卷别 覆盖矩阵（题数，0=该年无此卷）')
out('| 年份 | ALG-Ind | ALG-Ov | ALG-Team | ANA-Ind | ANA-Ov | ANA-Team |')
out('|---|---|---|---|---|---|---|')
for y in years:
    row = []
    for s in ('ALG', 'ANA'):
        for g in ('Individual', 'Team', 'Overall'):
            row.append(str(len([x for x in P if x[0] == y and x[1] == s and x[2] == g])))
    out('| %d | %s |' % (y, ' | '.join(row)))

# ---- 7. 方法关键词 ----------------------------------------------------------
out()
out('表 7  方法/定理关键词频次（题次）')
mc = collections.Counter()
for x in P:
    for t in re.split(r'[/、]', x[6]):
        t = t.strip()
        if len(t) >= 2: mc[t] += 1
for t, c in mc.most_common(40):
    out('  %-34s %d' % (t, c))
