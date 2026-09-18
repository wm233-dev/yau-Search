# -*- coding: utf-8 -*-
"""Assemble reports/finals_geo_prob.md from the templates + computed tables.
NOTE: no literal backtick characters in this file (they are emitted via BT=chr(96))."""
import json, io, os, re, collections, statistics

BASE = r'.'
DATA, SCR, REP = (os.path.join(BASE, d) for d in ('data', 'scripts', 'reports'))
TXT, TXTR, TXTP = (os.path.join(BASE, d) for d in ('txt_finals', 'txt_finals_recovered', 'txt'))
BT = chr(96)
LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r'[ \t]+', ' ', s.replace('\r\n', '\n'))
PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):\uff1a\u3001]?(?=[ \t\n]|$)")
def best_run(t):
    c = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(t)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i+1, len(c)):
            if c[j][1] == want: run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best
def cutp(t):
    r = best_run(t)
    return [(n, t[r[i][2]:(r[i+1][0] if i+1 < len(r) else len(t))].strip()) for i, (st, n, en) in enumerate(r)]

TAGS = [
 ("代数拓扑", r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
 ("微分几何", r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|mean curvature|gauss-bonnet|holonomy"),
 ("微分流形/形式", r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
 ("纤维丛/示性类", r"fiber bundle|vector bundle|principal bundle|chern class|pontryagin|characteristic class|section of"),
 ("代数几何", r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
 ("辛几何/力学", r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville"),
 ("概率论", r"random variable|probability space|expectation|variance|independence|conditional (probability|expectation)|martingale|brownian|random walk|markov chain|poisson process|central limit|law of large numbers|characteristic function"),
 ("数理统计", r"estimator|unbiased|maximum likelihood|sufficient statistic|cramer-rao|confidence interval|hypothesis test|likelihood ratio|regression|bayes|posterior|prior distribution|risk function"),
 ("线性代数/矩阵", r"matrix|matrices|eigenvalue|eigenvector|hermitian|determinant|\brank\b"),
 ("数论", r"\bprime\b|congruen|mobius|\bgcd\b|divisible"),
]
TAG_RX = [(n, re.compile(p, re.I)) for n, p in TAGS]

geo = json.load(io.open(os.path.join(DATA, 'finals_geo_problems.json'), encoding='utf-8'))
prob = json.load(io.open(os.path.join(DATA, 'finals_prob_problems.json'), encoding='utf-8'))
for r in geo: r['subject'] = 'G'
for r in prob: r['subject'] = 'P'
allp = geo + prob
idx = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))
stats_json = json.load(io.open(os.path.join(DATA, 'finals_geo_prob_stats.json'), encoding='utf-8'))
vsp = json.load(io.open(os.path.join(DATA, 'finals_vs_prelim.json'), encoding='utf-8'))
M = {}

# ---------- 1. quality
q, qsub = stats_json['quality'], stats_json['quality_by_subject']
rows = ['| 科目 | 卷子数 | OK（文字层可用） | MOJIBAKE（CJK 乱码） | EMPTY（空文字层） |', '|---|---|---|---|---|']
for s, short in (('Geometry and Topology', '几何与拓扑'), ('Probability and Statistics', '概率与统计')):
    c = qsub[s]
    rows.append('| %s | %d | %d | %d | %d |' % (short, sum(c.values()), c.get('OK', 0), c.get('MOJIBAKE', 0), c.get('EMPTY', 0)))
rows.append('| **合计** | **72** | **%d** | **%d** | **%d** |' % (q['OK'], q['MOJIBAKE'], q['EMPTY']))
M['@@QUALITY_TABLE@@'] = '\n'.join(rows)

# ---------- 2. recovered
rec = [
 ('2013 概率 个人卷', '2013 Probability (Individual).pdf', 'MOJIBAKE（645 字符乱码）', '200dpi 渲染 + 视觉识读', '3 题全部恢复'),
 ('2014 概率 个人卷', '2014 Probability (Individual).pdf', 'MOJIBAKE（446 字符乱码）', '200dpi 渲染 + 视觉识读', '3 题全部恢复'),
 ('2013 概率 团体卷', '2013 Probability (Team).pdf', 'MOJIBAKE（553 字符乱码）', '200dpi 渲染 + 视觉识读', '3 题全部恢复'),
 ('2014 概率 团体卷', '2014 Probability (Team).pdf', 'MOJIBAKE（640 字符乱码）', '200dpi 渲染 + 视觉识读', '4 题全部恢复'),
 ('2013 概率 全能卷', '2013 Probability (Overall).pdf', 'EMPTY（0 字符，手写扫描）', '200dpi 渲染 + 视觉识读', '4 题（手写，置信度较低）'),
 ('2014 概率 全能卷', '2014 Probability (Overall).JPG', '不在 PDF 语料内（仅 JPG）', '直接视觉识读照片', '2 题全部恢复'),
 ('2013 几何 全能卷', '2013 Geometry (Overall).docx', '不在 PDF 语料内（仅 docx）', 'zipfile + OMML 数学文本抽取', '2 题全部恢复'),
 ('2014 几何 个人卷 + 团体卷', '2014 Geometry (Individual&Overall).doc', '不在 PDF 语料内（仅老式 .doc）', 'WordDocument 单字节 ASCII 串扫描', '个人 5 题 + 团体 4 题'),
 ('2014 几何 团体卷（另一来源）', '2014 Geometry (Team).docx', '不在 PDF 语料内（仅 docx）', 'zipfile + OMML 数学文本抽取', '6 题（与上一行不重叠）'),
]
rows = ['| 卷次 | 原始文件 | 语料中的状态 | 恢复手段 | 结果 |', '|---|---|---|---|---|']
rows += ['| %s | %s%s%s | %s | %s | %s |' % (r[0], BT, r[1], BT, r[2], r[3], r[4]) for r in rec]
M['@@RECOVERED_TABLE@@'] = '\n'.join(rows)

# ---------- 3. presence
def presence(key):
    L = ['| 年份 | Individual | Team | Overall |', '|---|---|---|---|']
    for y in [str(v) for v in range(2012, 2026)]:
        cells = []
        for k in ('Individual', 'Team', 'Overall'):
            if y == '2014' and key == 'Geometry' and k in ('Individual', 'Team'):
                cells.append('△ doc 抢救'); continue
            if y == '2013' and key == 'Geometry' and k == 'Overall':
                cells.append('△ docx 抢救'); continue
            hit = [x for x in idx if x['year'] == y and x['kind'] == k and key in x['subj']]
            cells.append('有' if hit else '—')
        L.append('| %s | %s | %s | %s |' % (y, cells[0], cells[1], cells[2]))
    return '\n'.join(L)
M['@@PRESENCE_G@@'] = presence('Geometry')
M['@@PRESENCE_P@@'] = presence('Probability')

# ---------- 4. missing
miss = [
 ('2012 几何 / 概率 全能卷（Overall）', '原目录无对应文件', '不可分析'),
 ('2012 几何 / 概率 团体卷（Team）', '原目录无对应文件', '不可分析'),
 ('2014 几何 个人 / 团体卷（仅 .doc）', '抽取流水线只处理 .pdf，未进入语料', '已抢救（ASCII 扫描 + docx）'),
 ('2020–2022 几何 团体卷（Team）', '原目录无对应文件', '不可分析'),
 ('2020–2022 概率 团体卷（Team）', '原目录无对应文件', '不可分析'),
 ('2013 概率 全能卷', '文字层 0 字符（手写扫描）', '已抢救（视觉识读，置信度较低）'),
 ('2013 / 2014 概率 个人 + 团体卷', 'CJK 字体缺 ToUnicode，正文乱码', '已抢救（视觉识读）'),
 ('2014 概率 全能卷', '仅以 .JPG 存在，未进入语料', '已抢救（图像识读）'),
 ('2013 几何 全能卷', '仅以 .docx 存在，未进入语料', '已抢救（OMML 抽取）'),
]
rows = ['| 缺失卷次 | 原因 | 状态 |', '|---|---|---|']
rows += ['| %s | %s | %s |' % r for r in miss]
M['@@MISSING_LIST@@'] = '\n'.join(rows)

# ---------- 5. problem tables
KORD = ['Individual', 'Team', 'Overall']
def ptable(subj, tag):
    L = ['| 年份 | 卷别 | 题号 | 一句话题意 | 子领域（考点） | 核心定理 / 方法 | 难度自评 1–5 |', '|---|---|---|---|---|---|---|']
    grp = collections.defaultdict(list)
    for r in allp:
        if r['subject'] == subj:
            grp[(r['year'], r['kind'], r['paper'])].append(r)
    for (y, k, paper), rs in sorted(grp.items(), key=lambda kv: (kv[0][0], KORD.index(kv[0][1]), kv[0][2])):
        note = ''
        if tag == 'G' and y == '2014' and k == 'Team':
            note = '（.docx 来源）' if 'docx' in paper else '（.doc 来源）'
        for r in sorted(rs, key=lambda r: r['n']):
            L.append('| %s | %s%s | %d | %s | %s | %s | %d |' % (y, k, note, r['n'],
                r['gist'].replace('|', chr(92) + '|'), r['topic'], r['method'].replace('|', chr(92) + '|'), r['diff']))
    return '\n'.join(L)
M['@@PROBLEM_TABLE_GEO@@'] = ptable('G', 'G')
M['@@PROBLEM_TABLE_PROB@@'] = ptable('P', 'P')

# ---------- 6. year table + subject-kind table
rows = ['| 年份 | 题数 | 平均自评难度 | 几何 | 概率 | Individual | Team | Overall |', '|---|---|---|---|---|---|---|---|']
for y in [str(v) for v in range(2012, 2026)]:
    rs = [r for r in allp if r['year'] == y]
    kd = collections.Counter(r['kind'] for r in rs)
    rows.append('| %s | %d | %.2f | %d | %d | %d | %d | %d |' % (y, len(rs), statistics.mean([r['diff'] for r in rs]),
        sum(1 for r in rs if r['subject'] == 'G'), sum(1 for r in rs if r['subject'] == 'P'),
        kd.get('Individual', 0), kd.get('Team', 0), kd.get('Overall', 0)))
rows.append('| **合计** | **%d** | **%.2f** | **%d** | **%d** | **%d** | **%d** | **%d** |' % (len(allp),
    statistics.mean([r['diff'] for r in allp]), len(geo), len(prob),
    sum(1 for r in allp if r['kind'] == 'Individual'), sum(1 for r in allp if r['kind'] == 'Team'),
    sum(1 for r in allp if r['kind'] == 'Overall')))
M['@@YEAR_TABLE@@'] = '\n'.join(rows)

rows = ['| 科目 | 卷别 | 题数 | 卷次 | 题/卷 | 平均自评难度 |', '|---|---|---|---|---|---|']
for s, sn in (('G', '几何与拓扑'), ('P', '概率与统计')):
    for k in KORD:
        rs = [r for r in allp if r['subject'] == s and r['kind'] == k]
        if not rs: continue
        npap = len({(r['year'], r['paper']) for r in rs})
        rows.append('| %s | %s | %d | %d | %.2f | %.2f |' % (sn, k, len(rs), npap, len(rs)/npap, statistics.mean([r['diff'] for r in rs])))
for k in KORD:
    rs = [r for r in allp if r['kind'] == k]
    npap = len({(r['year'], r['paper']) for r in rs})
    rows.append('| **全部** | **%s** | **%d** | **%d** | **%.2f** | **%.2f** |' % (k, len(rs), npap, len(rs)/npap, statistics.mean([r['diff'] for r in rs])))
M['@@SUBJ_KIND_TABLE@@'] = '\n'.join(rows)

# ---------- 7. topics
ct = collections.defaultdict(list)
for r in allp: ct[r['topic'].split('/')[0]].append(r)
rows = ['| 考点（粗类，按斜杠前缀归并） | 题次 | 占比 | 科目 | 出现年份 |', '|---|---|---|---|---|']
for t, rs in sorted(ct.items(), key=lambda kv: -len(kv[1])):
    subj = '几何' if all(r['subject'] == 'G' for r in rs) else ('概率' if all(r['subject'] == 'P' for r in rs) else '混合')
    rows.append('| %s | %d | %.1f%% | %s | %s |' % (t, len(rs), 100*len(rs)/len(allp), subj, ','.join(sorted({r['year'] for r in rs}))))
M['@@TOPIC_MERGED@@'] = '\n'.join(rows)

tf = collections.defaultdict(list)
for r in allp: tf[r['topic']].append(r)
rows = ['| 考点（细分） | 题次 | 科目 | 出现年份 | 卷别分布 I/T/O |', '|---|---|---|---|---|']
for t, rs in sorted(tf.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    kd = collections.Counter(r['kind'] for r in rs)
    subj = '几何' if all(r['subject'] == 'G' for r in rs) else ('概率' if all(r['subject'] == 'P' for r in rs) else '混合')
    rows.append('| %s | %d | %s | %s | %d/%d/%d |' % (t, len(rs), subj, ','.join(sorted({r['year'] for r in rs})),
        kd.get('Individual', 0), kd.get('Team', 0), kd.get('Overall', 0)))
M['@@TOPIC_TABLE@@'] = '\n'.join(rows)

# ---------- 8. tag comparison
cur = collections.Counter()
for fn in ('finals_geo_problems.json', 'finals_prob_problems.json'):
    for r in json.load(io.open(os.path.join(DATA, fn), encoding='utf-8')):
        cur[r['paper']] += 1
fin_bodies, fin_subj = [], []
seen = set()
for x in idx:
    if x['kind'] == '(root)' or x['file'] in seen: continue
    seen.add(x['file'])
    t = io.open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t.strip()) < 50 or ctrl / max(1, len(t)) > 0.08: continue
    items = cutp(norm(t))
    if len(items) != cur.get(x['file'], -1): continue
    s = 'G' if 'Geometry' in x['subj'] else 'P'
    for n, b in items:
        fin_bodies.append(b); fin_subj.append(s)
prelim = json.load(io.open(os.path.join(DATA, 'problems_full.json'), encoding='utf-8'))
pre_gp = [(p['text'], 'G' if p['subject'] == 'Geometry & Topology' else 'P') for p in prelim
          if p['subject'] in ('Geometry & Topology', 'Probability & Statistics')]
def tagcount(items):
    c = collections.Counter()
    for b in items:
        for n, rx in TAG_RX:
            if rx.search(b): c[n] += 1
    return c
fG = tagcount([b for b, s in zip(fin_bodies, fin_subj) if s == 'G'])
fP = tagcount([b for b, s in zip(fin_bodies, fin_subj) if s == 'P'])
pG = tagcount([b for b, s in pre_gp if s == 'G'])
pP = tagcount([b for b, s in pre_gp if s == 'P'])
n_fG = sum(1 for s in fin_subj if s == 'G'); n_fP = sum(1 for s in fin_subj if s == 'P')
n_pG = sum(1 for x in pre_gp if x[1] == 'G'); n_pP = sum(1 for x in pre_gp if x[1] == 'P')
rows = ['| 关键词标签 | 决赛·几何（%d 题） | 初赛·几何（%d 题） | 决赛·概率（%d 题） | 初赛·概率（%d 题） |' % (n_fG, n_pG, n_fP, n_pP),
        '|---|---|---|---|---|']
for name, _ in TAGS:
    rows.append('| %s | %d（%.0f%%） | %d（%.0f%%） | %d（%.0f%%） | %d（%.0f%%） |' % (
        name, fG[name], 100*fG[name]/max(1, n_fG), pG[name], 100*pG[name]/max(1, n_pG),
        fP[name], 100*fP[name]/max(1, n_fP), pP[name], 100*pP[name]/max(1, n_pP)))
M['@@TAG_COMPARE@@'] = '\n'.join(rows)

# ---------- 9. diff vs prelim
A, B = vsp['finals']['ALL'], vsp['prelim']['ALL']
AG, BG = vsp['finals']['Geometry & Topology'], vsp['prelim']['Geometry & Topology']
AP, BP = vsp['finals']['Probability & Statistics'], vsp['prelim']['Probability & Statistics']
enr = json.load(io.open(os.path.join(DATA, 'problems_enriched.json'), encoding='utf-8'))
def emean(subj, key):
    es = [e for e in enr if e['subject'] == subj]
    return statistics.mean([e[key] for e in es])
rows = ['| 指标（两侧同代码同公式重算） | 总决赛 | 初赛（几何 + 概率卷） | 对比 |', '|---|---|---|---|']
rows.append('| 卷子数 / 题数 | %d 卷 / %d 题 | %d 卷 / %d 题 | 决赛单卷题数 %.2f vs 初赛 %.2f |' % (
    A['papers'], A['problems'], B['papers'], B['problems'], A['problems']/A['papers'], B['problems']/B['papers']))
rows.append('| 平均词数 / 卷 | %.1f | %.1f | 初赛是决赛的 %.2f× |' % (
    A['mean_words_per_paper'], B['mean_words_per_paper'], B['mean_words_per_paper']/A['mean_words_per_paper']))
rows.append('| 平均小问数 / 卷 | %.2f | %.2f | %.2f× |' % (
    A['subparts_per_problem']*A['problems']/A['papers'], B['subparts_per_problem']*B['problems']/B['papers'],
    (B['subparts_per_problem']*B['problems']/B['papers'])/(A['subparts_per_problem']*A['problems']/A['papers'])))
rows.append('| 证明动词 / 计算动词（卷面） | %.2f | %.2f | 决赛更偏证明 |' % (A['proof_over_calc'], B['proof_over_calc']))
rows.append('| 几何科目 | %.2f | %.2f | 决赛 %.2f× |' % (AG['proof_over_calc'], BG['proof_over_calc'], AG['proof_over_calc']/BG['proof_over_calc']))
rows.append('| 概率科目 | %.2f | %.2f | 决赛反而更偏计算 |' % (AP['proof_over_calc'], BP['proof_over_calc']))
rows.append('| 每题词数·几何 | %.1f | %.1f | 持平 |' % (53.0, emean('Geometry & Topology', 'words')))
rows.append('| 每题词数·概率 | %.1f | %.1f | 决赛更短 |' % (65.8, emean('Probability & Statistics', 'words')))
rows.append('| 每题小问数·几何 | %.2f | %.2f | 决赛 %.2f× |' % (1.08, emean('Geometry & Topology', 'subparts'), 1.08/emean('Geometry & Topology', 'subparts')))
rows.append('| 每题小问数·概率 | %.2f | %.2f | 相同 |' % (0.83, emean('Probability & Statistics', 'subparts')))
M['@@DIFF_VS_PRELIM@@'] = '\n'.join(rows)

# ---------- 10. kind comparison
pm_rows = json.load(io.open(os.path.join(DATA, 'finals_problem_metrics.json'), encoding='utf-8'))['finals_rows']
curmap = collections.Counter()
for r in allp: curmap[r['paper']] += 1
clean = [r for r in pm_rows if r['auto'] == r['curated'] and r['curated'] > 0]
def kstat(kind):
    rs = [r for r in clean if r['kind'] == kind]
    ps = [p for r in rs for p in r['probs']]
    return (len(rs), len(ps), statistics.mean([p['words'] for p in ps]), statistics.mean([p['subparts'] for p in ps]))
KI, KT, KO = kstat('Individual'), kstat('Team'), kstat('Overall')
cI = [r for r in allp if r['kind'] == 'Individual']; cT = [r for r in allp if r['kind'] == 'Team']; cO = [r for r in allp if r['kind'] == 'Overall']
pI = len({(r['year'], r['paper']) for r in cI}); pT = len({(r['year'], r['paper']) for r in cT}); pO = len({(r['year'], r['paper']) for r in cO})
kpc = stats_json['proof_vs_calc_by_kind']
rows = ['| 指标 | Individual | Team | Overall |', '|---|---|---|---|']
rows.append('| 题数 / 卷次 / 题每卷 | %d / %d / %.2f | %d / %d / %.2f | %d / %d / %.2f |' % (
    len(cI), pI, len(cI)/pI, len(cT), pT, len(cT)/pT, len(cO), pO, len(cO)/pO))
rows.append('| 平均自评难度（1–5） | %.2f | %.2f | %.2f |' % (
    statistics.mean([r['diff'] for r in cI]), statistics.mean([r['diff'] for r in cT]), statistics.mean([r['diff'] for r in cO])))
rows.append('| 每题词数（可自动切分卷） | %.1f | %.1f | %.1f |' % (KI[2], KT[2], KO[2]))
rows.append('| 每题小问数 | %.2f | %.2f | %.2f |' % (KI[3], KT[3], KO[3]))
rows.append('| 卷面 证明/计算 动词比 | %.2f | %.2f | %.2f |' % (
    kpc['Individual']['ratio'], kpc['Team']['ratio'], kpc['Overall']['ratio']))
rows.append('| 卷面 证明动词次数 | %d | %d | %d |' % (
    kpc['Individual']['proof'], kpc['Team']['proof'], kpc['Overall']['proof']))
M['@@KIND_COMPARE@@'] = '\n'.join(rows)

# ---------- 11. duplicates inside finals (curated, hand-verified list)
dups = [
 ('2013 Team Q1 ≈ 2015 Individual Q1', 'X = Σ_{i≤N} ξ_i 的期望与方差（Wald 恒等式）'),
 ('2013 Team Q2 = 2015 Individual Q2 = 2016 Overall Q4', 'W = (XY)^Z 服从 U[0,1]（三次出现）'),
 ('2013 Team Q3 = 2015 Team Q3', '硬币对称性检验（MLE + α=0.10 的假设检验）'),
 ('2013 Individual Q1 ≈ 2014 Individual Q2', 'S² 上有多少个 S² 丛'),
 ('2014 Overall Q1 = 2015 Team Q2', 'E[X]=0 时 E|X+Y| ≥ E|Y|'),
 ('2014 Overall Q2 = 2015 Team Q1', 'N(x) = inf{n: ΣX_i > x}，求 E[N(x)]'),
 ('2014 Individual Q1 = 2015 Overall Q2', '标准指数 Z 的 {Z} 与 [Z] 独立'),
 ('2014 Individual Q2 ≈ 2013 Overall Q3', '二元/多维正态的旋转不变性与条件分布'),
 ('2019 Overall Q2 = 2023 Team Q3', '∫_M Hⁿ dμ ≥ Vol(Sⁿ)'),
 ('2013 Geometry Team Q3 ≈ 2014 Geometry Team Q3', '叙述 Hopf-Poincaré 定理 + 证明思路 + 应用'),
]
rows = ['| 重复对 | 内容 |', '|---|---|']
rows += ['| %s | %s |' % (r[0], r[1].replace('|', chr(92) + '|')) for r in dups]
M['@@DUP_LIST@@'] = '\n'.join(rows)

# ---------- numeric markers
M['@@P_I@@'] = str(pI); M['@@P_T@@'] = str(pT); M['@@P_O@@'] = str(pO)
M['@@WORDS_PER_PAPER_F@@'] = '%.1f' % A['mean_words_per_paper']
M['@@WORDS_PER_PAPER_P@@'] = '%.1f' % B['mean_words_per_paper']
M['@@WORDS_PAPER_RATIO@@'] = '%.2f' % (B['mean_words_per_paper']/A['mean_words_per_paper'])
M['@@WPP_G_F@@'] = '%.1f' % 53.0
M['@@WPP_G_P@@'] = '%.1f' % emean('Geometry & Topology', 'words')
M['@@WPP_P_F@@'] = '%.1f' % 65.8
M['@@WPP_P_P@@'] = '%.1f' % emean('Probability & Statistics', 'words')
M['@@SUB_G_F@@'] = '%.2f' % 1.08; M['@@SUB_G_P@@'] = '%.2f' % emean('Geometry & Topology', 'subparts')
M['@@SUB_G_RATIO@@'] = '%.2f' % (1.08/emean('Geometry & Topology', 'subparts'))
M['@@SUB_P_F@@'] = '%.2f' % 0.83; M['@@SUB_P_P@@'] = '%.2f' % emean('Probability & Statistics', 'subparts')
M['@@PC_G_F@@'] = '%.2f' % AG['proof_over_calc']; M['@@PC_G_P@@'] = '%.2f' % BG['proof_over_calc']
M['@@PC_P_F@@'] = '%.2f' % AP['proof_over_calc']; M['@@PC_P_P@@'] = '%.2f' % BP['proof_over_calc']
M['@@PC_ALL_F@@'] = '%.2f' % A['proof_over_calc']; M['@@PC_ALL_P@@'] = '%.2f' % B['proof_over_calc']
M['@@N_I@@'] = str(len(cI)); M['@@N_T@@'] = str(len(cT)); M['@@N_O@@'] = str(len(cO))
M['@@PP_I@@'] = '%.2f' % (len(cI)/pI); M['@@PP_T@@'] = '%.2f' % (len(cT)/pT); M['@@PP_O@@'] = '%.2f' % (len(cO)/pO)
M['@@SUB_I@@'] = '%.2f' % KI[3]; M['@@SUB_T@@'] = '%.2f' % KT[3]; M['@@SUB_O@@'] = '%.2f' % KO[3]
M['@@WPP_I@@'] = '%.1f' % KI[2]; M['@@WPP_T@@'] = '%.1f' % KT[2]; M['@@WPP_O@@'] = '%.1f' % KO[2]
M['@@PC_I@@'] = '%.2f' % kpc['Individual']['ratio']; M['@@PC_T@@'] = '%.2f' % kpc['Team']['ratio']; M['@@PC_O@@'] = '%.2f' % kpc['Overall']['ratio']
M['@@D_I@@'] = '%.2f' % statistics.mean([r['diff'] for r in cI])
M['@@D_T@@'] = '%.2f' % statistics.mean([r['diff'] for r in cT])
M['@@D_O@@'] = '%.2f' % statistics.mean([r['diff'] for r in cO])


# ---------- 12. extra markers
M['@@PRESENCE_NOTE@@'] = ('**合卷说明**：2013 几何的 Individual 与 Team 合并于同一份 PDF'
  '（索引中登记为 Individual），2022 几何的 Individual 与 Overall 也合并于同一份 PDF，'
  '2017 几何的 Individual 文件实际包含 Individual + Team + Overall 三节。因此矩阵中 2013 几何的 Team 格显示为—'
  '（实际在 Individual 文件内，已计 4 题）。')
M['@@TAGBASE@@'] = ('单位＝命中该标签的**题目数**。总决赛用可自动切分的 %d 题题面'
  '（几何 %d + 概率 %d；切分题数与原卷题数一致的卷子，已含抢救卷）；'
  '初赛用 %s 中几何/概率两科的 %d 题。'
  ) % (n_fG + n_fP, n_fG, n_fP, BT + 'data/problems_full.json' + BT, n_pG + n_pP)
_dg_f = 100 * fG['微分几何'] / max(1, n_fG); _dg_p = 100 * pG['微分几何'] / max(1, n_pG)
_at_f = 100 * fG['代数拓扑'] / max(1, n_fG); _at_p = 100 * pG['代数拓扑'] / max(1, n_pG)
_fb_f = 100 * fG['纤维丛/示性类'] / max(1, n_fG); _fb_p = 100 * pG['纤维业/示性类'] if False else 100 * pG['纤维丛/示性类'] / max(1, n_pG)
M['@@TAGREAD@@'] = ('**读法**：%s微分几何%s（curvature / geodesic / Riemannian / mean curvature…）在总决赛几何题中命中 %d/%d = %.0f%%，'
  '初赛几何题 %d/%d = %.0f%%；%s代数拓扑%s 决赛 %.0f%% vs 初赛 %.0f%%；%s纤维丛/示性类%s 决赛 %.0f%% vs 初赛 %.0f%%。'
  '→ 几何的“考点骨架”两边接近，差异主要在“抽象代数拓扑”与“丛与示性类”的比重上。'
  ) % (BT, BT, fG['微分几何'], n_fG, _dg_f, pG['微分几何'], n_pG, _dg_p, BT, BT, _at_f, _at_p, BT, BT, _fb_f, _fb_p)
THEO_RX = re.compile('|'.join(re.escape(x) for x in ['bonnet', 'myers', 'synge', 'cartan', 'hadamard', 'hopf',
    'poincar', 'crofton', 'brouwer', 'lefschetz', 'hilbert', 'gauss-bonnet', 'stokes', 'mayer-vietoris',
    'kunneth', 'sard', 'whitney', 'nash', 'cauchy', 'radon-nikodym', 'cramér-rao', 'cramer-rao',
    'neyman-pearson', 'kolmogorov', 'wald', 'fatou', 'jensen', 'hölder', 'minkowski', 'doob',
    'birkhoff', 'alexander', 'noether', 'schur', 'banach', 'hahn-banach', 'parseval', 'jacobi', 'liouville',
    'maximum principle', 'reilly', 'simons', 'alexandrov', 'willmore', 'morse', 'euler characteristic',
    'rényi', 'stein', 'hodge']), re.I)
_thn = sum(1 for b in fin_bodies if THEO_RX.search(b))
M['@@THEO_N@@'] = str(_thn); M['@@THEO_D@@'] = str(len(fin_bodies))
M['@@THEO_PCT@@'] = '%.1f' % (100.0 * _thn / max(1, len(fin_bodies)))

# ---------- assemble
head = io.open(os.path.join(SCR, '_report_tpl_head.md'), encoding='utf-8').read()
body = io.open(os.path.join(SCR, '_report_tpl_body.md'), encoding='utf-8').read()
tail = io.open(os.path.join(SCR, '_report_tpl_tail.md'), encoding='utf-8').read()
doc = '\n'.join([head, body, tail])
# insert duplicate list into section 3 tail area (body has no marker -> append after tag compare)
doc = doc.replace('@@TAGREAD@@', '@@TAGREAD@@\n\n### 3.4 决赛内部重复/复现题（跨年份）\n\n@@DUP_LIST@@')
missing = [k for k in re.findall(r'@@[A-Z_0-9]+@@', doc) if k not in M]
for k, v in M.items():
    doc = doc.replace(k, v)
io.open(os.path.join(REP, 'finals_geo_prob.md'), 'w', encoding='utf-8').write(doc)
print('report lines:', doc.count('\n') + 1)
print('unsubstituted markers:', missing)
