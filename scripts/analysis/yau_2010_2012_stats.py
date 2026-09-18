# -*- coding: utf-8 -*-
r"""
丘成桐大学生数学竞赛 2010-2012 笔试真题 —— 定量统计脚本 (v2)
输入: ./corpus/prelim/ 下 2010_/2011_/2012_ 开头的 txt
输出: 控制台 markdown 表格 + scripts/stats_2010_2012.json
"""
import os, re, json, collections, glob

TXT = r".\txt"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stats_2010_2012.json")

files = []
for pat in ("2010_*.txt", "2011_*.txt", "2012_*.txt"):
    files += glob.glob(os.path.join(TXT, pat))
files = sorted(set(files))

SUBJ = {"algebranumbertheory": "代数与数论", "algebra": "代数与数论",
        "analysisdiffequation": "分析与微分方程", "analysis": "分析与微分方程",
        "appliedcomputational": "应用/计算/概率统计", "appliedmathprob": "应用/计算/概率统计",
        "applied": "应用/计算/概率统计", "geometrytopology": "几何与拓扑",
        "geomtop": "几何与拓扑", "geometry": "几何与拓扑",
        "probability": "概率统计"}

def subject_of(name):
    low = name.lower()
    for k in ("algebranumbertheory", "algebra", "analysisdiffequation", "analysis",
              "appliedcomputational", "appliedmathprob", "applied",
              "geometrytopology", "geomtop", "geometry", "probability"):
        if k in low:
            return SUBJ[k]
    return "未知"

def exam_kind(name):
    low = name.lower()
    if "individual" in low or "_indi" in low:
        return "个人"
    if "team" in low:
        return "团体"
    return "?"

KW = {
 # ---- 代数与数论 ----
 "Galois 理论/分裂域": r"galois|splitting field",
 "不可约性(irreducible)": r"irreducib",
 "Sylow 定理": r"sylow",
 "单群/群阶整除": r"not simple|group of order",
 "群表示论": r"representation|direct sum of two one-dimensional",
 "张量积/对称幂": r"tensor product|symmetric power|⊗",
 "共轭类": r"conjugacy class",
 "正交群/反射": r"orthogonal group|reflection|\bo\(v\)|\bo\(n\)",
 "PID/模/自由模": r"\bpid\b|free module|submodule|module",
 "数域/域扩张": r"number field|field extension|quadratic field|rational number",
 "p 进数/p-adic": r"\bp-adic|z_p\b|q_p\b|projective limit",
 "行列式/矩阵": r"determinant|matri(x|ces)|det\(",
 "环/理想/商环": r"\bring\b|ideal|quotient ring|z\[x, ?y\]/",
 "四元数": r"quaternion",
 "结式/互素多项式": r"g\.c\.d\.|finitely many \(a, b\)",
 "特征多项式/极小多项式": r"characteristic polynomial|minimal polynomial",
 "D-模/微分算子": r"d-module|differential operator",
 "对角化/不变子空间": r"diagonalizable|invariant subspace|common eigenvector",
 # ---- 分析与微分方程 ----
 "全纯/共形映射": r"holomorphic|analytic function|conformal",
 "调和函数/Laplace 方程": r"harmonic|laplace|∆u|\\delta u",
 "Fourier 级数/系数": r"fourier|\\hat f|e\^{-inx}",
 "Lp/L2 空间": r"\bl\^?2\b|\bl\^?p\b|\bl1\(|\bl1\[|l\^1\b",
 "Hilbert/Banach 空间": r"hilbert space|banach space|inner product space",
 "紧算子/紧性": r"compact operator|pre-?compact|compactness|\bcompact\b",
 "测度/可测函数": r"measurable|lebesgue|\bmeasures?\b",
 "最大模/最大原理": r"maximum principle|schwarz|maximum modulus",
 "Borel 测度/Cauchy 型积分": r"borel measure|cauchy|poisson",
 "常微分方程/初值问题": r"\\ddot|d2u/dx2|d\^2u|solution approaches zero|ode\b|has a unique solution of period",
 "Lyapunov 稳定性": r"lyapunov|stable|stability",
 "一致收敛/逼近": r"uniform (convergence|norm|bounded)|uniformly convergent|approximat|weierstrass",
 "导数不等式/插值估计": r"sup \|f|interpolat|\\leq 2\\sqrt",
 "椭圆型 PDE(∆u)": r"∆u|elliptic|boussinesq|mean curvature",
 # ---- 几何与拓扑 ----
 "覆盖空间/基本群": r"covering (space|map|projection)|fundamental group|π1|simply connected",
 "同调/上同调": r"homology|cohomology|de rham",
 "微分形式/Stokes/Poincaré": r"differential form|stokes|poincar|exact sequence",
 "Gauss-Bonnet/示性类": r"gauss-bonnet|gauss–bonnet|euler characteristic",
 "曲率(Ricci/高斯/平均)": r"curvature|ricci|einstein",
 "子流形/第二基本形式": r"hypersurface|submanifold|second fundamental form",
 "测地线/联络": r"geodesic|connection|levi-civita",
 "Riemann 度量/等距": r"riemannian|metric|isometr",
 "同伦/映射度": r"homotop|\bdeg\b|degree of f|essential",
 "射影空间 RP^n/CP^2": r"projective space|rp\s?\^?n|cp\s?\^?2",
 "辛形式": r"symplectic",
 "临界点": r"critical point",
 "嵌入/光滑流形": r"embed|smooth manifold|differentiable manifold",
 # ---- 概率统计 ----
 "i.i.d./独立同分布": r"i\.i\.d|independent and identically|independent random sample",
 "正态分布": r"normal distribution|n\(0, ?1\)|gaussian|bivariate normal",
 "指数/泊松/二项": r"exponential distribution|poisson|binomial|bernoulli",
 "极大似然 MLE": r"maximum likelihood|\blikelihood\b|\bmle\b",
 "无偏/UMVU/Cramer-Rao": r"unbiased|umvu|cramer-rao|fisher information",
 "渐近分布/CLT": r"asymptotic|central limit|converges? in (law|probability|distribution)",
 "条件期望/辅助统计量": r"conditional expectation|martingale|ancillary",
 "顺序统计量": r"order statistic",
 "假设检验/检验功效": r"\btests?\b|power of the test|wilcoxon|mann-whitney|p-value|critical region",
 "密度/分布函数": r"density|distribution function|\bcdf\b|p\.d\.f",
 "Bayes/后验分布": r"posterior|prior\b|bayes",
 "收敛性(依概率/几乎必然)": r"in probability|infinitely often|i\.o\.|lim sup",
 # ---- 应用与计算数学 ----
 "有限差分/CFL/von Neumann": r"finite difference|von neumann|\bcfl\b|scheme",
 "格式稳定性": r"\bstability\b|\bstable\b|well-posed",
 "有限元": r"finite element|piecewise linear",
 "迭代法/SOR/共轭梯度": r"conjugate gradient|\bsor\b|iterative scheme|spectral radius|diagonally dominant",
 "SVD/奇异值/最小二乘": r"singular value|\bsvd\b|least square|rank\(b\)=k",
 "算法复杂度": r"complexity|o\(n\^?2\)|o\(pn\^?2\)",
 "整数分解/RSA/素数": r"factori|\brsa\b|twin prime|\bprimes?\b",
 "正交多项式/数值积分": r"orthogonal sequence|legendre|chebyshev|quadrature|numerical integration",
 "PDE 数值格式": r"\bpde\b|ut \+ ux|second order accurate|convergence order",
}

# ---- 具名定理/经典对象 ----
NAMES = {
 "Sylow 定理": r"sylow", "Schur 引理": r"schur", "Schwarz 引理": r"schwarz",
 "Stokes 定理": r"stokes", "Gauss-Bonnet": r"gauss-bonnet|gauss–bonnet",
 "Cramer-Rao 下界": r"cramer-rao", "von Neumann 稳定性": r"von neumann",
 "Chebyshev 多项式": r"chebyshev", "Bertrand 曲线": r"bertrand",
 "Poincaré 对偶": r"poincar", "de Rham 上同调": r"de rham",
 "Boussinesq 方程": r"boussinesq", "RSA 密码": r"\brsa\b",
 "Wilcoxon 秩和": r"wilcoxon", "Mann-Whitney U": r"mann-whitney",
 "最大模原理": r"maximum principle", "Green 公式/散度定理": r"div\(x\)|divergence",
 "Fubini/控制收敛": r"dominated convergence|fubini",
 "最小二乘/正交投影": r"least square", "共轭梯度法": r"conjugate gradient",
 "SOR 迭代": r"\bsor\b", "对称群 S_n": r"s_4|s3\b|symmetric group",
 "正交群 O(n)": r"\bo\(n\)|orthogonal group", "SL_2(Z)": r"sl2\(z\)",
 "四元数群 Q8": r"quaternion", "Jacobi/椭圆函数": r"jacobi|elliptic function",
 "Borel 测度/Riesz 表示": r"borel measure",
}

rows, texts = [], []
for f in files:
    base = os.path.basename(f)
    txt = open(f, encoding="utf-8").read()
    texts.append(txt)
    lines = txt.split("\n")
    nums = []
    for i, ln in enumerate(lines):
        m = re.match(r"^\s*(\d{1,2})\.\s*(.*)$", ln)
        if m and int(m.group(1)) == len(nums) + 1:
            nums.append(i)
    rows.append(dict(file=base, year=base[:4], kind=exam_kind(base), subject=subject_of(base),
                     nprob=len(nums), chars=len(txt), lines=len(lines),
                     pages=txt.count("=== page ")))

def count_kw(table):
    res = {}
    for name, pat in table.items():
        rx = re.compile(pat, re.I)
        pf, tot = {}, 0
        for f, t in zip(files, texts):
            c = len(rx.findall(t))
            if c:
                pf[os.path.basename(f)] = c; tot += c
        res[name] = dict(total=tot, nfiles=len(pf), per_file=pf)
    return res

kw = count_kw(KW)
nm = count_kw(NAMES)

print("=== TAB1 逐卷结构 ===")
print("| 文件 | 年 | 卷别 | 科目 | 题数 | 页数 | 字符数 |")
print("| --- | --- | --- | --- | --- | --- | --- |")
for r in rows:
    print("| %s | %s | %s | %s | %d | %d | %d |" % (r["file"], r["year"], r["kind"], r["subject"], r["nprob"], r["pages"], r["chars"]))
tot_p = sum(r["nprob"] for r in rows)
print("\nTOTAL problems=%d files=%d chars=%d" % (tot_p, len(rows), sum(len(t) for t in texts)))
print("by year:", dict(collections.Counter({r["year"]: 0 for r in rows}) | {}))
byyr = collections.Counter(); byk = collections.Counter()
for r in rows:
    byyr[r["year"]] += r["nprob"]; byk[(r["year"], r["kind"])] += r["nprob"]
print("probs by year:", dict(sorted(byyr.items())))
print("probs by year+kind:", dict(sorted(byk.items())))

print("\n=== TAB2 关键词频次(降序) ===")
print("| 考点关键词 | 总命中 | 覆盖卷数 | 命中前二的卷 |")
print("| --- | --- | --- | --- |")
for name, d in sorted(kw.items(), key=lambda kv: (-kv[1]["total"], kv[0])):
    top = sorted(d["per_file"].items(), key=lambda kv: -kv[1])[:2]
    print("| %s | %d | %d | %s |" % (name, d["total"], d["nfiles"],
          "; ".join("%s(%d)" % (a.replace(".txt",""), b) for a, b in top) or "-"))

print("\n=== TAB3 具名定理/对象(降序) ===")
print("| 名称 | 总命中 | 覆盖卷数 |")
print("| --- | --- | --- |")
for name, d in sorted(nm.items(), key=lambda kv: (-kv[1]["total"], kv[0])):
    print("| %s | %d | %d |" % (name, d["total"], d["nfiles"]))

# 分期对比: 2010/2011 与 2012
print("\n=== TAB4 分期关键词对比 (2010+2011 vs 2012) ===")
print("| 考点 | 2010-2011 命中 | 2012 命中 |")
print("| --- | --- | --- |")
for name, pat in KW.items():
    rx = re.compile(pat, re.I)
    a = sum(len(rx.findall(t)) for f, t in zip(files, texts) if f[-4:].startswith("2012") is False and os.path.basename(f)[:4] in ("2010","2011"))
    b = sum(len(rx.findall(t)) for f, t in zip(files, texts) if os.path.basename(f)[:4] == "2012")
    if a + b:
        print("| %s | %d | %d |" % (name, a, b))

# 跨年重复题检测
print("\n=== TAB5 跨卷/跨年重复题检测 ===")
DUP = {
 "阶 150 群不单": r"group of order 150",
 "GL_3(F_7) 的 Sylow 子群": r"gl3\(f7\)",
 "两样本 Bernoulli 检验临界域 |√n(p̂1−p̂2)|": r"z_?1.?α|z1−α|2ˆpˆq|2\\hat p",
 "对流方程 ut+ux=0 差分格式稳定性": r"ut \+ ux|u_t \+ u_x",
 "Riemann 度量/联络唯一性": r"riemannian connection",
 "the degree of f : S^n → S^n": r"degree of f",
 "Wishart/正交投影 SVD 截断": r"min\s+rank\(b\)=k",
 "Gauss-Bonnet / 曲面整体几何": r"gauss-bonnet|gauss–bonnet",
}
for name, pat in DUP.items():
    rx = re.compile(pat, re.I)
    hit = [os.path.basename(f) for f, t in zip(files, texts) if rx.search(t)]
    print("- %s: %d 卷 -> %s" % (name, len(hit), ", ".join(hit) if hit else "无"))

json.dump(dict(rows=rows, kw=kw, names=nm), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nwrote", OUT)
