# -*- coding: utf-8 -*-
"""Yau 竞赛 2016-2018 笔试真题定量统计 (最终版 v4)
输入: .tmp/burn2026/scripts/_clean/201[678]_*.txt (txt/ 原文件的去 NUL 副本, 文本内容一致)
输出: scripts/stats_out/stats_2016_2018.txt 与 problems_2016_2018.json
"""
import glob, os, re, json, collections

CLEAN = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean'
OUT   = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\stats_out'
os.makedirs(OUT, exist_ok=True)
files = sorted(glob.glob(os.path.join(CLEAN, '201[678]_*.txt')))
assert len(files) == 18, len(files)
YEAR_RE = re.compile(r'S\.-T\. Yau College Student Mathematics Contests\s+(\d{4})')

def norm(t):
    for a, b in [('\ufb01','fi'),('\ufb02','fl'),('\ufb00','ff'),('\ufb03','ffi'),
                 ('\ufb04','ffl'),('\u2019',"'"),('\u201c','"'),('\u201d','"')]:
        t = t.replace(a, b)
    return t

def subject_of(b):
    for k, v in [('Analysis and Di','Analysis'),('Probability and Statistics','Probability'),
                 ('Geometry and Topology','Geometry'),('Algebra and Number Theory','Algebra'),
                 ('Applied Math','Applied')]:
        if k in b: return v
    return 'UNKNOWN'

def kind_of(b):
    head = '\n'.join(b.split('\n')[:8])
    if re.search(r'\bIndividual\b', head): return 'Individual'
    if re.search(r'\bTeam\b', head): return 'Team'
    return 'UNKNOWN'

PROB_RE = re.compile(r'(?m)^\s*(?:Problem\s+)?(\d{1,2})\s*(?:\([^)]*points\)\s*)?[\.\)]')
records = []
for f in files:
    txt = norm(open(f, encoding='utf-8').read())
    base = os.path.basename(f)
    idx = [m.start() for m in YEAR_RE.finditer(txt)] + [len(txt)]
    for a, b in zip(idx[:-1], idx[1:]):
        blk = txt[a:b]
        kind = kind_of(blk); subj = subject_of(blk)
        fl = base.replace('.txt', '')
        ms = list(PROB_RE.finditer(blk)); keep = []; expect = 1
        for m in ms:
            if int(m.group(1)) == expect and expect <= 12:
                keep.append(m); expect += 1
        for i, m in enumerate(keep):
            end = keep[i+1].start() if i+1 < len(keep) else len(blk)
            records.append(dict(file=fl, year=base[:4], kind=kind, subject=subj,
                                num=int(m.group(1)), body=blk[m.start():end].strip()))

subs = ['Analysis','Probability','Geometry','Algebra','Applied']
L = []; P = L.append
P('#' * 100)
P('# 附表 1  逐卷结构 (自动解析结果, 与报告正文表 1 对应)')
P('#' * 100)
P(f'{"年份":<6}{"卷别":<11}{"科目":<12}{"题号":<22}{"大题":>5}{"平均字符":>9}{"最长题面":>9}')
for r in sorted(records, key=lambda x: (x['year'], 0 if x['kind']=='Individual' else 1, subs.index(x['subject']), x['num'])):
    pass
g = collections.defaultdict(list)
for r in records: g[(r['year'], r['kind'], r['subject'])].append(r)
order = [('2016','Individual'),('2016','Team'),('2017','Individual'),('2017','Team'),('2018','Individual'),('2018','Team')]
tot = 0
for y, k in order:
    for s in subs:
        rs = g.get((y,k,s), [])
        if not rs: continue
        tot += len(rs)
        nums = ','.join(str(r['num']) for r in rs)
        P(f'{y:<6}{k:<11}{s:<12}{nums:<22}{len(rs):>5}{sum(len(x["body"]) for x in rs)//len(rs):>9}{max(len(x["body"]) for x in rs):>9}')
P('-' * 100)
P(f'三年合计大题数: {tot}')
P('')
P('题量矩阵:')
P(f'{"年份":<7}{"卷别":<12}' + ''.join(f'{s:>11}' for s in subs) + f'{"合计":>8}')
for y, k in order:
    cells = [len(g.get((y,k,s), [])) for s in subs]
    P(f'{y:<7}{k:<12}' + ''.join(f'{c:>11}' for c in cells) + f'{sum(cells):>8}')
for y in ['2016','2017','2018']:
    P(f'{y} 年合计 = {sum(len(g.get((y,k,s),[])) for k in ["Individual","Team"] for s in subs)}')

KW = {
# ---------- Analysis ----------
'A. Riemann 可积 / 达布和':            r'Riemann integrable|Riemann integral',
'A. 绝对连续 / 牛顿-莱布尼茨':           r'absolutely continuous',
'A. Lebesgue 测度 / 几乎处处':          r'Lebesgue|measure zero|almost everywhere|a\.e\.|m\(B\)',
'A. 一致收敛 / 紧集上收敛':              r'uniformly on compact|converges uniformly|uniform convergence',
'A. 全纯 / 亚纯函数':                   r'holomorphic|meromorphic|entire',
'A. 共形映射':                         r'conformal',
'A. 调和函数':                         r'harmonic function|harmonic on|positive harmonic',
'A. Fourier 变换 / 级数':               r'Fourier|e−inx|e−ixξ|\^f\(n\)|ˆf\(n\)|einx',
'A. Laplace 方程 / Δ':                 r'Laplace equation|Delta f|u11 \+ u22',
'A. Hilbert 空间 / 算子':               r'Hilbert space|self-adjoint|compact operator|bounded .{0,12}operator',
'A. 弱收敛':                           r'weakly|weak convergence',
'A. 卷积 / 逼近恒等':                   r'convolution|Kδ|δ−n',
'A. Dirichlet 问题 / Green 函数':       r'Dirichlet|G\(z, z0\)|g\(z, z0\)',
'A. Sobolev / H^1_0 / Poincaré':       r'H1 0|H1\(|Sobolev|Poincare|smallest constant C',
'A. 留数 / 围道积分 / 椭圆函数':          r'residue|Rukowski|doubly periodic|log x',
'A. Newton 位势 / 基本解':              r'n\(n −1\)α\(n\)|∆f = g|−∆f',
'A. 最大模 / Schwarz 引理':             r'maximum modulus|Schwarz',
# ---------- Algebra ----------
'B. Galois 群 / 扩张':                 r'Galois',
'B. 分裂域':                           r'splitting field',
'B. 分圆多项式':                        r'cyclotomic',
'B. Sylow 定理':                       r'Sylow',
'B. 共轭类 / 类方程':                    r'conjugacy class|centralizer|#Cent',
'B. Fitting 引理 / 局部环':              r'Fitting|local ring|EndR',
'B. Chevalley–Warning 定理':           r'Chevalley',
'B. Chebyshev 素数界':                  r'Chebyshev',
'B. Goldbach / Fermat 数':             r'Goldbach|2k −1 is a prime|2k \+ 1 is a prime|22i \+ 1',
'B. p-adic 数 / Zp / Qp / 赋值':        r'p-adic|Qp|Zp|vp\(',
'B. 素理想分解 / 分歧 / 惯性次数':         r'rami|splits in|inertia degree|cubic residue|decomposition law',
'B. 二项式系数':                        r'binomial',
'B. Lie 代数':                         r'Lie algebra|adx|rank\(g\)',
'B. 表示论 / 特征标':                    r'representation|character χ|χ\(g\)|irreducible',
'B. 双线性型 / 正交与辛结构':             r'bilinear form|symplectic|positive definite symmetric',
'B. 不可分解模 / 有限长度':               r'indecomposable|finite length',
'B. 有限域 F_q 上线性代数':              r'Fq|Fp|F q|F p|algebraic closure Fp',
'B. 有限群结构 / 群阶':                  r'finite group|group of order|order 99|order 2nm',
'B. Z^d 子群 / 指数':                   r'subgroup of Zd|index n|fd\(n\)|gd\(n\)',
'B. Euclidean 平面 / 反射生成':          r'reflection|Iso\(E\)',
'B. 可除群 / 挠群 / 自同态环':            r'Qp/Zp|Q/Z|p−kZp|endomorphism ring',
# ---------- Geometry ----------
'C. de Rham 上同调':                   r'de Rham',
'C. 同调群':                           r'homology group',
'C. 基本群 / 覆盖空间':                  r'fundamental group|π1',
'C. Euler 示性数':                     r'Euler characteristic',
'C. 向量丛分类':                        r'vector bundle',
'C. 映射环面 / 约化双角锥':               r'mapping torus|suspension|ΣX',
'C. 连通和 / 粘贴胞腔':                  r'connect sum|M#N|∪S2 D3|∪ D3|crush|attaching',
'C. 极小子流形 / 极小超曲面':             r'minimal submanifold|minimal hypersurface|minimal sub',
'C. 平均曲率 / 第二基本形式':             r'mean curvature|second fundamental form|\bHr\b|HndV',
'C. 截面曲率':                         r'sectional curvature',
'C. Ricci 曲率':                       r'Ricci',
'C. Gauss 曲率 / Gauss–Bonnet':        r'Gaussian curvature|\|K\|dσ|Gauss',
'C. 测地线 / 测地挠率':                  r'geodesic',
'C. 大圆 / 超球面':                     r'great circle|hypersphere|great sphere',
'C. Crofton 公式 / Gauss 映射':         r'Crofton|Gauss map|n\(W\)dW',
'C. 球面定理 / 单连通性':                 r'homeomorphic to S|simply conn',
'C. Frobenius 定理':                   r'Frobenius',
'C. 截断函数 / 单位分解':                 r'cut-off|partition of unity',
'C. Lie 导数 / 向量场':                 r'Lie derivative|vector field|nowhere vanishing vector',
'C. 闭形式 / 恰当形式':                  r'exact\?|not closed|is not closed|dy −ydx',
# ---------- Probability ----------
'D. i.i.d. 样本':                      r'i\.i\.d\.|iid|independent and identically|independently',
'D. 极限分布 / 渐近正态':                r'limiting distribution|asymptotic|N\(0|t distribution|tn−1|tn−2',
'D. 集中不等式 / 矩母函数':               r'concentration|moment generating|Chernoff|Hoeffding|4p\(1 −p\)',
'D. 随机游走':                         r'random walk|random walker',
'D. 几乎必然 / a.s.':                   r'almost surely|a\.s\.',
'D. 期望 / 方差计算':                    r'variance|Var\(|expectation|expected|E\(sX',
'D. 估计量 / 无偏 / MLE':                r'estimator|unbiased|maximum likelihood|efficiency',
'D. Bayes / 先验':                     r'prior|Bayes',
'D. 直方图 / 密度估计':                  r'histogram|bandwidth|mean-squared error',
'D. Poisson / Bernoulli / 几何分布':    r'Poisson|Bernoulli|geometric',
'D. 随机矩阵 / 算子范数':                 r'random matrix|operator norm',
'D. 二叉树 / 分支':                     r'binary tree|branching',
'D. 随机图 / 超立方体':                  r'random graph|G\(n, p\)|hypercube|bipartite|Hamilton',
'D. 条件分布 / 条件独立':                 r'conditionally independent|conditional',
'D. Markov 过程 / 生灭过程':             r'Markov process|Markov chain|X\(t\)',
# ---------- Applied ----------
'E. CFL 条件 / 稳定性':                 r'CFL|stable|stability',
'E. von Neumann 分析 / 特征多项式':      r'von Neumann|characteristic polynomial|root condition',
'E. 有限差分格式':                      r'finite difference|scheme|mesh|truncation|grid',
'E. 精度阶数':                         r'order .{0,8}accurate|order \(2, 4\)|second order accurate',
'E. 迎风格式 / 守恒律':                  r'upwind|conservation law|f\(u\)x',
'E. Taylor 展开 / 待定系数法':            r'Taylor|undetermined coefficients',
'E. 插值':                             r'interpolat',
'E. Chebyshev / Hermite / Legendre':   r'Chebyshev|Hermite|Legendre',
'E. 凸优化 / 次梯度 / 梯度下降':           r'subgradient|strongly convex|convex function|gradient descent',
'E. 迭代法 / 谱半径 / 收敛性':             r'iterative scheme|spectral radius|residual|converges in n iterations',
'E. 特征值 / 反迭代 / 奇异值':             r'eigenvalue|eigenvector|singular value|inverse iteration',
'E. 核范数 / 低秩逼近':                  r'nuclear norm|low-rank',
'E. 辛格式 / Hamilton 系统':            r'symplectic|Hamiltonian|Verlet',
'E. 量纲分析 / 奇异摄动':                 r'nondimensional|scaling|leading order|scaled|dimensionless',
'E. Michaelis–Menten / 反应动力学':      r'Michaelis|enzyme|reaction rate',
'E. 格 / 数论算法':                     r'multiplicatively dependent|integer non-zero vector',
'E. 固定点迭代 / Steffensen':            r'fixed point|Steffensen',
'E. 匹配 / Hall 定理':                  r'matching|Hall',
'E. 正交投影 / 子空间迭代':               r'orthogonal projection|PX\(0\)|X\(m\+1\)',
}

rows = []
for name, pat in KW.items():
    rx = re.compile(pat)
    hs = [r for r in records if rx.search(r['body'])]
    c = collections.Counter(r['year'] for r in hs)
    sub = collections.Counter(r['subject'] for r in hs)
    rows.append((name, c['2016'], c['2017'], c['2018'], len(hs), sub.most_common(1)[0][0] if sub else '-', sub))

P('')
P('#' * 100)
P('# 附表 2  高频考点 (口径 = 命中的题目数; 161 题; 同题多次出现只计 1 次)')
P('#' * 100)
P(f'{"考点 / 定理 / 方法":<40}{"2016":>6}{"2017":>6}{"2018":>6}{"合计":>7}{"占比":>8}{"主科目":>10}')
for name, a, b, c, t, top, sub in sorted(rows, key=lambda x: (-x[4], x[0])):
    P(f'{name:<40}{a:>6}{b:>6}{c:>6}{t:>7}{100.0*t/len(records):>7.1f}%{top:>10}')

P('')
P('#' * 100)
P('# 附表 3  设问方式 (口径 = 命中的题目数)')
P('#' * 100)
VERB = {
 'Show that':                    r'Show that',
 'Prove that':                   r'Prove that',
 'Prove (无 that)':               r'Prove\b(?! that)',
 'Compute / Calculate':         r'Compute|Calculate',
 'Find / Determine':            r'Find\b|Determine',
 '设定型开头 Let':                 r'^\s*(?:Problem\s+\d+[^\n]{0,30})?\s*Let\b',
 '设定型开头 Suppose':             r'^\s*(?:Problem\s+\d+[^\n]{0,30})?\s*Suppose\b',
 '设定型开头 Consider':            r'^\s*(?:Problem\s+\d+[^\n]{0,30})?\s*Consider\b',
 'State and prove':             r'State and prove',
 'Prove or disprove':           r'Prove or disprove',
 '要求给反例':                    r'counter ?example',
 '题面自带 Hint':                 r'Hint',
 'if and only if':              r'if and only if|is equivalent to',
 'necessary and sufficient':    r'necessary and su\ufb03cient|necessary and sufficient',
 '带分值 (points)':               r'\(\d+\s*points\)',
 '多小问 (a)(b)(c)':             r'\(a\)\s*\(\d+\s*points\)',
 '(1)(2)(3) 编号小问':            r'(?m:^\(1\))|(?m:^1\)\s)',
}
P(f'{"设问方式":<30}{"2016":>7}{"2017":>7}{"2018":>7}{"合计":>7}{"占161题":>10}')
for name, pat in VERB.items():
    rx = re.compile(pat)
    hs = [r for r in records if rx.search(r['body'])]
    c = collections.Counter(r['year'] for r in hs)
    P(f'{name:<30}{c["2016"]:>7}{c["2017"]:>7}{c["2018"]:>7}{len(hs):>7}{100.0*len(hs)/len(records):>9.1f}%')

P('')
P('#' * 100)
P('# 附表 4  科目画像')
P('#' * 100)
P(f'{"科目":<14}{"题数":>6}{"占比":>8}{"平均字符":>10}{"最长":>7}{"带points":>10}{"带Hint":>8}')
for s in subs:
    rs = [r for r in records if r['subject'] == s]
    P(f'{s:<14}{len(rs):>6}{100.0*len(rs)/len(records):>7.1f}%'
      f'{sum(len(r["body"]) for r in rs)//len(rs):>10}{max(len(r["body"]) for r in rs):>7}'
      f'{sum(1 for r in rs if re.search(r"\(\d+\s*points\)", r["body"])):>10}'
      f'{sum(1 for r in rs if "Hint" in r["body"]):>8}')

out = '\n'.join(L)
open(os.path.join(OUT, 'stats_2016_2018.txt'), 'w', encoding='utf-8').write(out)
json.dump(records, open(os.path.join(OUT, 'problems_2016_2018.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print(out)
