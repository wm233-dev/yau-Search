# -*- coding: utf-8 -*-
"""v2: 2013-2015 Yau CSMC keyword named-theorem + theme frequency, cleaned labels."""
import os, re, glob, json
from collections import OrderedDict
ROOT = r"."
TXT = os.path.join(ROOT, "txt"); OUT = os.path.join(ROOT, "scripts")
files = sorted(sum([glob.glob(os.path.join(TXT, y+"_*.txt")) for y in ("2013","2014","2015")], []))
texts = {os.path.basename(p): open(p, encoding="utf-8", errors="replace").read() for p in files}
ALL = "\n".join(texts.values())

THEOREMS = [
 ("Schwarz lemma / Pick", r"schwarz|pick"),
 ("Gauss-Lucas", r"gauss\s*[-–]\s*lucas|lucas"),
 ("Bernstein theorem", r"bernstein"),
 ("Chevalley-Warning", r"chevalley|warning"),
 ("Mayer-Vietoris", r"mayer|vietoris"),
 ("van Kampen", r"van\s+kampen"),
 ("Poincare duality", r"poincar"),
 ("Gauss-Bonnet / Stokes", r"gauss\s*[-–]\s*bonnet|stokes"),
 ("Myers theorem", r"myers"),
 ("Synge / second variation", r"synge|second\s+variation"),
 ("Hopf (max principle / CMC)", r"\bhopf\b"),
 ("Weyl equidistribution", r"weyl"),
 ("Borel-Cantelli", r"borel|canelli|cantelli"),
 ("Kolmogorov three-series", r"kolmogorov"),
 ("Slutsky / converging together", r"slutsky"),
 ("Stein identity", r"\bstein\b"),
 ("Wilks / likelihood ratio", r"likelihood\s+ratio|wilks"),
 ("Cramer-Rao / Fisher info", r"cramer|fisher\s+information|information\s+inequality"),
 ("Renyi representation", r"renyi|r´enyi"),
 ("Rao-Blackwell / sufficiency", r"sufficient\s+statistic|rao|blackwell"),
 ("Minkowski (problem / thm)", r"minkowski"),
 ("Willmore / H^2 >= 4pi", r"willmore|4\s*π|4π"),
 ("Eckart-Young / low rank", r"eckart|rank\(b\)|low\s+rank"),
 ("Arnoldi / Krylov / GMRES", r"arnoldi|krylov|gmres"),
 ("Cartan-Dieudonne (reflections)", r"refl\'?ection"),
 ("Molien series", r"molien|homogeneous\s+polynomial\s+functions"),
 ("Catalan numbers", r"catalan"),
 ("Fibonacci / fast powering", r"fibonacci"),
 ("Euler-Lagrange", r"euler\s*[-–]\s*lagrange|euler-lagrange"),
 ("Isoperimetric inequality", r"isoperimetric|iso-perimetric"),
 ("Uncertainty principle", r"uncertainty"),
 ("Radon-Nikodym", r"radon"),
 ("Fredholm / compact perturbation", r"fredholm|coker|compact\s+operator"),
 ("Sobolev embedding / H^1", r"sobolev"),
 ("Laplace / Poisson kernel", r"poisson"),
 ("Heat / wave / Laplace eq", r"heat\s+equation|wave\s+equation|laplace\s+equation"),
 ("CFL / von Neumann / upwind", r"upwind|von\s+neumann|cfl"),
 ("Discontinuous Galerkin", r"galerkin"),
 ("SVD / singular values", r"singular\s+value|\bsvd\b"),
 ("Condition number", r"condition\s+number"),
 ("Eisenstein criterion", r"eisenstein"),
 ("Galois correspondence", r"galois"),
 ("Dedekind splitting / discriminant", r"discriminant|prime\s+ideal|splitting\s+field"),
 ("Sylow theory", r"sylow"),
 ("Semidirect product", r"⋉|semidirect|semi-direct"),
 ("UFD / PID", r"unique\s+factorization|\bufd\b|factorial\s+ring"),
 ("Modular group Gamma(2)", r"gamma\(2\)|Γ\(2\)|modular\s+group"),
 ("Upper half plane", r"upper\s+half\s*[- ]?plane"),
 ("Unit tangent bundle", r"unit\s+tangent\s+bundle|tangent\s+bundle"),
 ("Riemannian submersion", r"submersion"),
 ("Bernoulli / Galton-Watson", r"galton|branching\s+process|extinction"),
 ("Record values", r"record"),
 ("Confidence interval", r"confidence\s+interval"),
 ("Hypothesis test / p-value", r"p-value|hypothesis"),
 ("Bayesian / posterior", r"bayes|posterior"),
 ("Lasso / soft-thresholding", r"lasso|soft\s+threshold|penal"),
 ("Filatova", r"zzz_never"),
]

THEMES = [
 ("Lp / L2 / function spaces", r"\bl\s*2\b|\bl2\b|\bl\s*p\s*\b|\blp\b|\bl∞\b|lp\s+space"),
 ("估计量 / estimate / MLE", r"estimator|\bmle\b|maximum\s+likelihood|\bestimate\b"),
 ("有限域 F_p / F_q", r"finite\s+field|\bf\s*p\b|\bf2\b|\bf\s*5\b|\bfq\b|\bf\s*q\b"),
 ("球面 / 环面 S^n, T^2", r"\bsphere\b|\btorus\b|\bs\s*n\b|\bt\s*2\b"),
 ("流形 manifold", r"manifold"),
 ("iid / 独立同分布", r"\biid\b|i\.i\.d|independent\s+and\s+identically"),
 ("独立 independent", r"independent"),
 ("特征值/特征向量", r"eigen"),
 ("不可约 irreducible", r"irreducibl"),
 ("紧性/紧算子 compact", r"compact"),
 ("图论 graph/cycle", r"\bgraph\b|\bcycle\b|hamiltonian"),
 ("正态 Gaussian/normal", r"gaussian|normal\s+distribution|\bn\s*\(\s*0"),
 ("曲率 curvature", r"curvature"),
 ("凸函数凸集 convex", r"convex"),
 ("条件期望/期望", r"conditional\s+expectation|\be\s*\[|\bexpectation\b"),
 ("收敛 (依分布/依概率/a.s.)", r"converge|convergen"),
 ("可测/σ-代数", r"measurable|σ-algebra|sigma-algebra|borel\s+set"),
 ("方差/协方差", r"variance|covariance|\bcov\b"),
 ("指数分布", r"exponential\s+distribution|exponential\s+density|shifted\s+exponential|standard\s+exponential"),
 ("均匀分布 U(a,b)", r"uniform\s+distribution|uniform\s+on|uniformly\s+distributed"),
 ("特征函数 characteristic fn", r"characteristic\s+function|characteristic\s+fn"),
 ("全纯/解析 holomorphic", r"holomorph|analytic\s+function|entire\s+function"),
 ("调和 harmonic", r"harmonic"),
 ("Fourier 变换/级数", r"fourier"),
 ("数值格式 scheme/差分", r"scheme|finite\s+diﬀerence|finite\s+difference"),
 ("稳定性 stability", r"stabilit"),
 ("能量法 energy", r"\benergy\b"),
 ("Sobolev 空间", r"sobolev"),
 ("座位/乘客/球/坦克(经典模型)", r"passengers?\b|\bseats?\b|colored\s+balls|enemy\s+tanks|tank\s+serial"),
 ("Hilbert space", r"hilbert"),
]

def cnt(t, p): return len(re.findall(p, t, flags=re.IGNORECASE))

def table(items, title):
    rows = []
    for nm, pat in items:
        c = cnt(ALL, pat)
        if c == 0: continue
        py = [cnt("\n".join(v for k,v in texts.items() if k.startswith(y)), pat) for y in ("2013","2014","2015")]
        rows.append((nm, c, py[0], py[1], py[2]))
    rows.sort(key=lambda r: (-r[1], r[0]))
    return rows

thm = table(THEOREMS, "theorem")
thm = [r for r in thm if not r[0].startswith("Filatova")]
tms = table(THEMES, "theme")

def emit(rows, head, path):
    L = ["| " + head + " | 合计 | 2013 | 2014 | 2015 |", "|---|---:|---:|---:|---:|"]
    for nm, c, a, b, d in rows:
        L.append("| %s | %d | %d | %d | %d |" % (nm, c, a, b, d))
    s = "\n".join(L) + "\n"
    open(path, "w", encoding="utf-8").write(s)
    return s

s1 = emit(thm, "定理 / 方法名", os.path.join(OUT, "named_theorems_2013_2015.md"))
s2 = emit(tms, "主题关键词", os.path.join(OUT, "themes_2013_2015.md"))
print("=== NAMED THEOREMS / METHODS ===");  print(s1)
print("=== THEMES ===");  print(s2)
