# -*- coding: utf-8 -*-
"""2013-2015 Yau CSMC text statistics.
Reads .tmp/burn2026/txt/{2013,2014,2015}_*.txt and emits a keyword-frequency
table + per-file structural table as markdown/TSV.
No third-party deps beyond stdlib.
"""
import os, re, json, sys, glob
from collections import Counter, OrderedDict

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT  = os.path.join(ROOT, "txt")
OUT  = os.path.join(ROOT, "scripts")
os.makedirs(OUT, exist_ok=True)

files = []
for y in ("2013", "2014", "2015"):
    files += sorted(glob.glob(os.path.join(TXT, y + "_*.txt")))
files = sorted(files)

def load(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()

# ---------------- keyword dictionary ----------------
KEYS = OrderedDict()
def add(group, name, pat):
    KEYS.setdefault(group, []).append((name, pat))

# 代数 / 数论
add("代数/数论", "Galois", r"galois")
add("代数/数论", "Galois group / Gal(", r"gal\s*\(")
add("代数/数论", "splitting field", r"splitting\s+field")
add("代数/数论", "Sylow", r"sylow")
add("代数/数论", "irreducible", r"irreducibl")
add("代数/数论", "Eisenstein", r"eisenstein")
add("代数/数论", "UFD / unique factorization", r"unique\s+factorization|ufd")
add("代数/数论", "character table", r"character\s+table")
add("代数/数论", "irreducible representation", r"irreducible\s+representation")
add("代数/数论", "SL2 / SL_2", r"\bsl2\b|\bsl\(2|\bsl_2")
add("代数/数论", "orthogonal group O(V)/O_n", r"orthogonal\s+group|\bo\s*\(\s*v\s*\)|o\s*n\s*\(\s*c")
add("代数/数论", "symmetric group S_n", r"s4\b|s5\b|symmetric\s+group")
add("代数/数论", "field extension", r"field\s+extension")
add("代数/数论", "finite field F_p / F_q", r"finite\s+field|\bf\s*p\b|f\s*5\b|f2\b|fq\b|f\s*q\b")
add("代数/数论", "Euclidean / Euclidean space", r"euclidean")
add("代数/数论", "positive (semi)definite", r"positive\s+(semi-?)?definite")
add("代数/数论", "commuting matrices", r"commut")
add("代数/数论", "p-adic", r"p-adic")
add("代数/数论", "reflection", r"reflection")
add("代数/数论", "valuation/order", r"ring of integers|prime ideal")

# 分析 / 微分方程
add("分析/方程", "harmonic", r"harmonic")
add("分析/方程", "holomorphic / analytic", r"holomorph|analytic\s+function")
add("分析/方程", "Laplacian / Laplace", r"laplac")
add("分析/方程", "Fourier", r"fourier")
add("分析/方程", "L^p / L2 space", r"\bl\s*2\b|\blp\b|l\s*p\s*\(|l2\s*\(")
add("分析/方程", "Lebesgue", r"lebesgue")
add("分析/方程", "compact operator", r"compact\s+operator|\bcompact\b")
add("分析/方程", "Hilbert space", r"hilbert")
add("分析/方程", "self-adjoint / hermitian", r"self-adjoint|hermitian")
add("分析/方程", "eigenvalue/eigenvector", r"eigen")
add("分析/方程", "Sobolev", r"sobolev")
add("分析/方程", "convex function", r"convex")
add("分析/方程", "subharmonic", r"subharmonic")
add("分析/方程", "maximum principle", r"maximum\s+principle|achieves?\s+(its\s+)?maximum")
add("分析/方程", "bounded variation", r"bounded\s+variation")
add("分析/方程", "weak derivative", r"weak\s+derivative")
add("分析/方程", "heat/wave equation", r"heat\s+equation|wave\s+equation")
add("分析/方程", "Dirichlet/Neumann 条件", r"dirichlet|neumann")
add("分析/方程", "uncertainty principle", r"uncertainty\s+principle")
add("分析/方程", "convolution", r"convolution|\bf\s*\*\s*")
add("分析/方程", "Euler-Lagrange", r"euler-lagrange")
add("分析/方程", "entire function", r"entire\s+function")
add("分析/方程", "conformal", r"conformal")
add("分析/方程", "Banach/closed range", r"coker|closed\s+in\s+h|finite\s+dimensional")

# 几何 / 拓扑
add("几何/拓扑", "manifold", r"manifold")
add("几何/拓扑", "Riemannian metric", r"riemannian")
add("几何/拓扑", "curvature", r"curvature")
add("几何/拓扑", "sectional curvature", r"sectional\s+curvature")
add("几何/拓扑", "Ricci", r"ricci")
add("几何/拓扑", "mean curvature", r"mean\s+curvature")
add("几何/拓扑", "Gauss curvature", r"gauss\s+curvature|gaussian\s+curvature")
add("几何/拓扑", "geodesic", r"geodesic")
add("几何/拓扑", "minimal surface", r"minimal\s+surface")
add("几何/拓扑", "homology", r"homology")
add("几何/拓扑", "fundamental group", r"fundamental\s+group|π1|p1\s*\(")
add("几何/拓扑", "covering / double cover", r"cover")
add("几何/拓扑", "orientable", r"orientab")
add("几何/拓扑", "diffeomorphism", r"diﬀeomorph|diffeomorph")
add("几何/拓扑", "homeomorphic", r"homeomorph")
add("几何/拓扑", "vector field / Lie bracket", r"vector\s+field|lie\s+bracket")
add("几何/拓扑", "Bianchi identity", r"bianchi")
add("几何/拓扑", "Myers / Bonnet-Myers", r"myers")
add("几何/拓扑", "submersion / immersion", r"submersion|immersion")
add("几何/拓扑", "projective space RP^n", r"\brp\s*n|real\s+projective")
add("几何/拓扑", "torus / sphere", r"\btorus\b|\bt\s*2\b|\bsphere\b|\bs\s*n\b")
add("几何/拓扑", "normal coordinates", r"normal\s+coordinates")
add("几何/拓扑", "Einstein manifold", r"einstein")

# 概率 / 统计
add("概率/统计", "random variable", r"random\s+variable")
add("概率/统计", "iid / independent", r"\biid\b|i\.i\.d|independent")
add("概率/统计", "converge in distribution/probability", r"converge.{0,12}in\s+distribution|converge.{0,12}in\s+probability|converges?\s+in\s+distribution")
add("概率/统计", "almost surely", r"almost\s+surely|a\.s\.")
add("概率/统计", "conditional expectation", r"conditional\s+expectation|\be\s*\[")
add("概率/统计", "σ-algebra / measurable", r"σ-algebra|sigma-algebra|measurable")
add("概率/统计", "Radon-Nikodym", r"radon-nikodym")
add("概率/统计", "normal / Gaussian", r"normal\s+distribution|gaussian|\bn\s*\(\s*0")
add("概率/统计", "exponential distribution", r"exponential\s+distribution|exponential\s+density|shifted\s+exponential")
add("概率/统计", "uniform distribution", r"uniform\s+distribution|uniform\s+on")
add("概率/统计", "characteristic function", r"characteristic\s+function")
add("概率/统计", "variance/covariance", r"variance|covariance|\bcov\b")
add("概率/统计", "estimator / MLE", r"estimator|maximum\s+likelihood|\bmle\b|estimate")
add("概率/统计", "unbiased / consistent / efficient", r"unbiased|consistent\s+estimator|eﬃcient\s+estimator|efficient\s+estimator")
add("概率/统计", "confidence interval", r"confidence\s+interval")
add("概率/统计", "hypothesis test / p-value", r"hypothesis|p-value|likelihood\s+ratio")
add("概率/统计", "Bayesian / posterior", r"bayesian|posterior")
add("概率/统计", "lasso / penalized", r"lasso|penal")
add("概率/统计", "martingale/record", r"record|martingale")

# 应用 / 计算数学
add("应用/计算", "finite difference scheme", r"finite\s+diﬀerence|finite\s+difference|scheme")
add("应用/计算", "stability", r"stabilit")
add("应用/计算", "upwind", r"upwind")
add("应用/计算", "discontinuous Galerkin", r"galerkin")
add("应用/计算", "SVD / singular value", r"singular\s+value|\bsvd\b")
add("应用/计算", "condition number", r"condition\s+number")
add("应用/计算", "Krylov / GMRES / Arnoldi", r"krylov|gmres|arnoldi")
add("应用/计算", "Hessenberg", r"hessenberg")
add("应用/计算", "Richardson iteration", r"richardson")
add("应用/计算", "Euler / backward Euler", r"euler")
add("应用/计算", "Catalan number", r"catalan")
add("应用/计算", "Fibonacci", r"fibonacci")
add("应用/计算", "graph / Hamiltonian / cycle", r"hamiltonian|\bgraph\b|\bcycle\b")
add("应用/计算", "variational / isoperimetric", r"isoperimetric|variational|iso-perimetric")
add("应用/计算", "energy estimate", r"energy")
add("应用/计算", "Minkowski / convex polyhedron", r"minkowski|polyhedron")
add("应用/计算", "interpolation / projection error", r"projection|l2\s+projection")
add("应用/计算", "N=100 组合/球盒", r"passenger|seat|balls|tanks")

def count(text, pat):
    return len(re.findall(pat, text, flags=re.IGNORECASE))

alltext = {}
for p in files:
    alltext[os.path.basename(p)] = load(p)
ALL = "\n".join(alltext.values())

# ------------- per-file structure -------------
TOP = re.compile(r"(?m)^[ \t]*(?:Problem\s+(\d+)|(\d+))[\.\s]\s*(?:\(|pt|points|\s)", re.IGNORECASE)
SUB = re.compile(r"(?m)^[ \t]*(\d+)\.(\d+)\b")
PTS = re.compile(r"(\d+)\s*(?:pt\b|pts\b|points\b|%)", re.IGNORECASE)
PAGES = re.compile(r"===\s*page\s*\d+\s*===")

rows = []
for name in sorted(alltext):
    t = alltext[name]
    tops = set()
    for m in re.finditer(r"(?mi)^[ \t]*(?:Problem\s+(\d+)|(\d+))\s*[\.\s]\s*", t):
        n = m.group(1) or m.group(2)
        tops.add(int(n))
    subs = set(SUB.findall(t))
    pts = [int(x) for x in PTS.findall(t)]
    rows.append({
        "file": name,
        "chars": len(t),
        "pages": len(PAGES.findall(t)),
        "top_problems": len(tops),
        "top_list": sorted(tops),
        "subparts": len({(int(a), int(b)) for a, b in subs}),
        "pts_mentions": len(pts),
        "pts_max": max(pts) if pts else 0,
        "pts_sum": sum(pts) if pts else 0,
    })

# ------------- keyword table -------------
kw_rows = []
for grp, lst in KEYS.items():
    for nm, pat in lst:
        c = count(ALL, pat)
        if c == 0:
            continue
        per_year = {y: count("\n".join(v for k, v in alltext.items() if k.startswith(y)), pat)
                    for y in ("2013", "2014", "2015")}
        kw_rows.append((grp, nm, c, per_year["2013"], per_year["2014"], per_year["2015"]))
kw_rows.sort(key=lambda r: (-r[2], r[0]))

# ------------- outputs -------------
def w(path, s):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)

lines = []
lines.append("# 2013-2015 Yau CSMC keyword frequency (auto-generated)\n")
lines.append("corpus: 26 txt files, %d chars\n" % len(ALL))
lines.append("| 领域 | 关键词/定理 | 合计 | 2013 | 2014 | 2015 |")
lines.append("|---|---|---:|---:|---:|---:|")
for grp, nm, c, a, b, cc in kw_rows:
    lines.append("| %s | %s | %d | %d | %d | %d |" % (grp, nm, c, a, b, cc))
w(os.path.join(OUT, "kw_2013_2015.md"), "\n".join(lines) + "\n")

lines2 = []
lines2.append("# 2013-2015 per-file structure (auto-generated)\n")
lines2.append("| 文件 | 字符 | 页 | 顶层题号数 | 题号列表 | 子题数 | 分值标记数 | 最大分值 |")
lines2.append("|---|---:|---:|---:|---|---:|---:|---:|")
for r in rows:
    lines2.append("| %s | %d | %d | %d | %s | %d | %d | %d |" % (
        r["file"], r["chars"], r["pages"], r["top_problems"],
        ",".join(str(x) for x in r["top_list"]), r["subparts"], r["pts_mentions"], r["pts_max"]))
w(os.path.join(OUT, "struct_2013_2015.md"), "\n".join(lines2) + "\n")

json.dump({"files": rows, "keywords": kw_rows}, open(os.path.join(OUT, "stats_2013_2015.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print("TOTAL FILES", len(rows), "TOTAL CHARS", len(ALL))
print("\n--- per-file ---")
for r in rows:
    print("%-40s chars=%5d pages=%2d tops=%2d subs=%2d ptsmax=%3d" % (
        r["file"], r["chars"], r["pages"], r["top_problems"], r["subparts"], r["pts_max"]))
print("\n--- top keywords ---")
for grp, nm, c, a, b, cc in kw_rows[:70]:
    print("%-8s %-34s %4d  (%d/%d/%d)" % (grp, nm, c, a, b, cc))
