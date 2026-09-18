
# -*- coding: utf-8 -*-
"""Fine-grained sub-topic recency probe: find topics absent from 2022-2026."""
import json, sys, re, collections
sys.stdout.reconfigure(encoding='utf-8')
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\data"
en = json.load(open(B + r"\problems_enriched.json", encoding='utf-8'))
docs = []
for p in en:
    t = p.get('text') or p.get('head') or ''
    docs.append((int(p['year']), ' '.join(t.split()), p.get('subject','?')))

PROBE = {
 "有限元方法": r"finite element",
 "数值积分/求积公式": r"quadrature|Simpson|trapezoid|numerical integration",
 "插值逼近": r"interpolat",
 "有限差分/差分格式": r"finite difference|difference scheme|\bscheme\b",
 "线性规划/单纯形": r"linear program|simplex method|simplex algorithm",
 "凸优化/KKT": r"\bKKT\b|convex optim|lagrangian dual|karush",
 "最优控制/变分法": r"optimal control|calculus of variations|euler-lagrange",
 "图论": r"\bgraph\b|graph theory",
 "组合计数/母函数": r"generating function|combinatorial identity|pigeonhole|inclusion-exclusion",
 "编码/密码": r"\bcode\b|coding theory|cryptograph|RSA|error-correcting",
 "数值线性代数(算法)": r"singular value decomposition|\bSVD\b|\bQR\b|condition number|power method|conjugate gradient",
 "常微分方程定性/极限环": r"limit cycle|lyapunov|poincare-bendixson|phase portrait",
 "混沌/动力系统": r"chaos|chaotic|bifurcation|strange attractor",
 "Sobolev/弱解": r"sobolev|weak solution|weak derivative|distributional",
 "调和分析/Fourier级数": r"fourier series|fourier transform|parseval|dirichlet kernel",
 "位势论/调和函数": r"harmonic function|potential theory|green's function|dirichlet problem",
 "复分析(留数/共形)": r"residue|holomorphic|conformal map|rouche|maximum modulus",
 "实分析(测度/勒贝格)": r"lebesgue|measurable|outer measure|dominated convergence",
 "泛函分析(算子/谱)": r"banach|hilbert space|compact operator|spectral theorem|hahn-banach",
 "概率论(鞅/布朗)": r"martingale|brownian|central limit|law of large numbers",
 "数理统计(估计/检验)": r"maximum likelihood|hypothesis test|confidence interval|estimator",
 "数值PDE稳定性": r"\bCFL\b|von neumann stability|\bLax-?Wendroff\b|upwind|\bADI\b|stability of the scheme",
 "PDE(椭圆/抛物)": r"elliptic|parabolic|maximum principle|green function",
 "PDE(双曲/守恒律)": r"hyperbolic|conservation law|shock|entropy solution|characteristic",
 "流体力学": r"navier|stokes equation|incompressible|euler equation|viscous|reynolds",
 "统计物理/热力学": r"partition function|ising|entropy of|bose|fermi|canonical ensemble|thermodynamic",
 "量子力学": r"schr|quantum mechan|wave function|heisenberg|hermitian operator",
 "相对论/场论": r"relativ|minkowski|schwarzschild|lagrangian density|gauge field|maxwell",
 "代数几何": r"algebraic variety|projective variety|sheaf|elliptic curve|scheme",
 "交换代数": r"noetherian|localization|integral closure|dedekind domain|valuation ring",
 "表示论": r"representation of|irreducible representation|character table|induced representation",
 "同调代数/范畴": r"category|functor|ext group|\bTor\b|derived functor|exact sequence",
 "代数拓扑(同调/同伦)": r"homology|homotopy|fundamental group|cohomology|covering space",
 "示性类/纤维丛": r"characteristic class|chern class|euler class|vector bundle|fiber bundle|pontryagin",
 "李群/李代数": r"lie group|lie algebra|exponential map of|killing form|root system",
 "微分几何(曲率)": r"sectional curvature|ricci|scalar curvature|geodesic|gauss-bonnet",
 "数论(初等)": r"quadratic residue|primitive root|fermat's little|chinese remainder|legendre symbol",
 "数论(代数/p进)": r"p-adic|cyclotomic|galois extension|local field|ramif",
 "矩阵分析(标准形)" : r"jordan canonical|characteristic polynomial|minimal polynomial|normal matrix|cayley-hamilton",
 "数值逼近/数值代数其他": r"newton's method|bisection|fixed point iteration|convergence rate",
}

rows = []
for name, pat in PROBE.items():
    rx = re.compile(pat, re.I)
    yrs = collections.Counter()
    for y, t, s in docs:
        if rx.search(t): yrs[y] += 1
    total = sum(yrs.values())
    recent = sum(v for k,v in yrs.items() if k >= 2022)
    last = max(yrs) if yrs else None
    rows.append((name, total, recent, last, dict(sorted(yrs.items()))))

rows.sort(key=lambda r: (r[2], -r[1]))
print(f"{'sub-topic':<28}{'total':>6}{'22-26':>7}{'last':>6}  years")
for name, total, recent, last, yrs in rows:
    print(f"{name:<28}{total:>6}{recent:>7}{str(last):>6}  {yrs}")
