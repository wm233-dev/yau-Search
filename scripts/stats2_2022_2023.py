# -*- coding: utf-8 -*-
"""补充统计: 试题卷口径的关键词频次 + 逐卷细分 + 题号异常排查"""
import os, re, json, glob, collections

TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
OUT = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts"

FILES_2022 = {
 "代数与数论":"2022_ExamPaper_2022_algebra_and_numbertheory_22s.txt",
 "分析与微分方程":"2022_ExamPaper_2022_analysis_and_differential_22s.txt",
 "计算与应用数学":"2022_ExamPaper_2022_computational_and_applied_22s.txt",
 "几何与拓扑":"2022_ExamPaper_2022_geometry_and_topology_22s.txt",
 "数学物理":"2022_ExamPaper_2022_Mathematical_Physics_22s.txt",
 "概率统计":"2022_ExamPaper_2022_probability_and_statistics_22s.txt",
}
FILES_2023 = {
 "代数与数论":"2023_Algebra_Number_theory.txt",
 "分析与微分方程":"2023_Analysis_and_differential_equation.txt",
 "计算与应用数学":"2023_Computational_Applied.txt",
 "几何与拓扑":"2023_Geometry_and_Topology.txt",
 "数学物理":"2023_Mathematical_Physics.txt",
 "概率统计":"2023_probability_statistics.txt",
}
def rd(fn): return open(os.path.join(TXT, fn), encoding="utf-8").read()

# --- 排查 2023 数学物理多出的题号 ---
mp23 = rd(FILES_2023["数学物理"])
found = [(m.group(1), mp23[:m.start()].count("\n")+1) for m in re.finditer(r"(?m)^(\d{1,2})\.\s", mp23)]
print("2023 数学物理 行首 'N. ' 命中:", found)

# --- 罗马小题 ---
for label, F in (("2022", FILES_2022), ("2023", FILES_2023)):
    tot_r = 0
    for s, fn in F.items():
        t = rd(fn)
        n = len(re.findall(r"(?m)^\s*(i{1,3}|iv)\.\s", t))
        tot_r += n
    print(f"{label} 试题卷罗马小题 (i./ii./iii.) 合计: {tot_r}")

KEY = {
"代数/数论": ["Dedekind","projective","invertible","fractional ideal","Eisenstein","Galois","discriminant",
  "integral basis","number field","ring of integers","root of unity","p-adic","solvable","commutator",
  "free module","flat","finite presentation","profinite","Lie algebra","representation","ideal","module",
  "irreducible","minimal polynomial","trace","norm","Chinese Remainder","uniformizer","logarithm"],
"分析/方程": ["Banach","Ascoli","Banach-Steinhaus","Gronwall","harmonic","holomorphic","Lebesgue","weakly",
  "entire","Laplacian","Lipschitz","positive definite","Fourier","equicontinuous","compact","Cauchy",
  "maximum principle","characteristic","L2","ODE","PDE","periodic","convol","Banach space"],
"几何/拓扑": ["Maurer-Cartan","Leray","Euler Characteristic","Euler characteristic","homology","cohomology","Poincar",
  "Killing","Ricci","soliton","minimal surface","Gauss","Gauss-Bonnet","sectional curvature","fiber bundle",
  "flag","H-space","symmetric product","shrinker","geodesic","hypersurface","manifold","curvature",
  "diffeomorphism","orient","fundamental group","homotopy","smooth","metric","Riemannian","tensor","valued 1-form"],
"概率统计": ["Markov chain","stationary","characteristic function","total variation","coupling","UMVUE","minimax",
  "sufficient","complete","Bayes","Dirichlet process","i.i.d","asymptotic","hypothesis","power","unbiased",
  "estimator","distribution","independen","random variable","Poisson","Bernoulli","Gaussian","normal",
  "uniform","converge","limit","expect"],
"计算/应用": ["finite difference","Runge-Kutta","Lax-Wendroff","Gaussian quadrature","orthogonal polynomial",
  "power iteration","dynamic programming","linear programming","consisten","stab","convergen","truncation error",
  "Richardson","WKB","tridiagonal","eigenvalue","Gershgorin","Jacobian","interpolation","Lagrange","norm",
  "iteration","time-step","quadrature","asymptotic","order"],
"数学物理": ["Killing","Lagrangian","Hamiltonian","Feynman","propagator","renormaliz","regulariz","one-loop",
  "gauge","Maxwell","Einstein","Schwarzschild","anti-unitary","time reversal","creation","annihilation",
  "commutation","su(2)","scale invariant","scale transformation","heat capacity","fermion","boson",
  "Green's function","cosmological constant","perturbation","Minkowski","Lorentz","Hilbert space",
  "wave function","spin","vacuum","symmetry","conserved","potential","energy","field"],
}

def cnt(t, kw): return len(re.findall(re.escape(kw), t, flags=re.IGNORECASE))

print()
print("="*104)
print("表 C2  关键词频次（口径统一：仅试题卷 2022 vs 2023，不含官方解答）")
print("="*104)
print(f"{'类别':<12}{'关键词':<26}{'2022':<7}{'2023':<7}{'合计':<7}")
rowsout=[]
for cat, kws in KEY.items():
    for kw in kws:
        c22 = sum(cnt(rd(f), kw) for f in FILES_2022.values())
        c23 = sum(cnt(rd(f), kw) for f in FILES_2023.values())
        if c22 + c23 == 0: continue
        rowsout.append((cat, kw, c22, c23, c22+c23))
for cat, kw, a, b, t in sorted(rowsout, key=lambda x: -x[4]):
    print(f"{cat:<12}{kw:<26}{a:<7}{b:<7}{t:<7}")

print()
print("="*104)
print("表 G  逐卷关键词命中数（试题卷；每卷 6 题）")
print("="*104)
allkw = [kw for _, kw in [(c,k) for c,ks in KEY.items() for k in ks]]
print(f"{'年份':<6}{'科目':<16}{'字符':<7}{'命中关键词种类':<14}{'命中总次数':<10}")
for label, F in (("2022", FILES_2022), ("2023", FILES_2023)):
    for s, fn in F.items():
        t = rd(fn)
        hits = [kw for kw in allkw if cnt(t, kw) > 0]
        tot = sum(cnt(t, kw) for kw in hits)
        print(f"{label:<6}{s:<16}{len(t):<7}{len(hits):<14}{tot:<10}")

print()
print("="*104)
print("表 H  每卷小题数（(a)(b)(c)... 与 i./ii.）")
print("="*104)
print(f"{'年份':<6}{'科目':<16}{'大错数':<8}{'(a)-(e)':<9}{'i./ii.':<8}{'合计子问':<8}")
for label, F in (("2022", FILES_2022), ("2023", FILES_2023)):
    for s, fn in F.items():
        t = rd(fn)
        parts = len(re.findall(r"\(([a-f])\)", t))
        rom = len(re.findall(r"(?m)^\s*(i{1,3}|iv)\.\s", t))
        print(f"{label:<6}{s:<16}{6:<8}{parts:<9}{rom:<8}{parts+rom:<8}")
