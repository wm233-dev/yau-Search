# -*- coding: utf-8 -*-
"""
Yau College Student Mathematics Competition -- 2024/2025/2026 笔试真题统计脚本 (v3, 最终版)
输出: .tmp/burn2026/reports/stats_2024_2026.md
"""
import os, re, collections

TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
OUT = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports\stats_2024_2026.md"

FILES = {
 2024: ["2024_2024_Algebra.txt","2024_2024_Analysis_and_diff_v2.txt","2024_2024_Computational_Math.txt",
        "2024_2024_GeometryTopology.txt","2024_2024_Math_physics.txt","2024_2024_statistics.txt"],
 2025: ["2025_algebra.txt","2025_analysis.txt","2025_computational_and_applied_math.txt",
        "2025_Geometry_and_Topology.txt","2025_physics.txt","2025_statistics.txt"],
 2026: ["2026_2026_Algebra_and_Number_Theory.txt","2026_2026_analysis.txt","2026_2026_Computation.txt",
        "2026_2026_Geo_Topology.txt","2026_2026_physics.txt","2026_2026_statistics.txt"],
}
SUBJ = {
 "2024_2024_Algebra.txt":"Algebra & Number Theory","2024_2024_Analysis_and_diff_v2.txt":"Analysis & PDE",
 "2024_2024_Computational_Math.txt":"Computational & Applied","2024_2024_GeometryTopology.txt":"Geometry & Topology",
 "2024_2024_Math_physics.txt":"Mathematical Physics","2024_2024_statistics.txt":"Probability & Statistics",
 "2025_algebra.txt":"Algebra & Number Theory","2025_analysis.txt":"Analysis & PDE",
 "2025_computational_and_applied_math.txt":"Computational & Applied","2025_Geometry_and_Topology.txt":"Geometry & Topology",
 "2025_physics.txt":"Mathematical Physics","2025_statistics.txt":"Probability & Statistics",
 "2026_2026_Algebra_and_Number_Theory.txt":"Algebra & Number Theory","2026_2026_analysis.txt":"Analysis & PDE",
 "2026_2026_Computation.txt":"Computational & Applied","2026_2026_Geo_Topology.txt":"Geometry & Topology",
 "2026_2026_physics.txt":"Mathematical Physics","2026_2026_statistics.txt":"Probability & Statistics",
}
MANGLE = {"p":"(","q":")","\u00d1":"->","\u0105":">","\u201c":"=","\u00b4":"-","\u02c6":"INT","\u0159":"SUM"}

def load(fn, demangle=False):
    raw = open(os.path.join(TXT, fn), "rb").read()
    t = raw.decode("utf-8-sig")
    t = "".join(ch for ch in t if ch in "\n\t" or ord(ch) >= 32)
    for a,b in [("\ufb00","ff"),("\ufb01","fi"),("\ufb02","fl"),("\ufb03","ffi"),("\ufb04","ffl")]:
        t = t.replace(a,b)
    t = re.sub(r"-\n(?=[a-z])", "", t).replace("\u00ad","")
    t = re.sub(r"[ \t]+", " ", t)
    if demangle:
        t = "".join(MANGLE.get(ch, ch) for ch in t)
    return t

pm  = re.compile(r"^[ \t]*(?:Problem|Question)[ \t]*(\d{1,2})\b", re.M)
nm  = re.compile(r"^[ \t]*(\d{1,2})[\.\)][ \t]*(?:\S|$)", re.M)
pg  = re.compile(r"^=== page (\d+) ===", re.M)
sub = re.compile(r"\((?:[a-j]|\d{1,2}|i{1,3}v?|iv|v|vi{0,3}|ix|x)\)")

def contiguous(nums):
    s=set(nums); n=0
    for i in range(1,40):
        if i in s: n=i
        else: break
    return n

rows=[]
for yr, fs in FILES.items():
    for fn in fs:
        dm = "Analysis_and_diff" in fn          # 该卷为 Cambria-Math 抽取, 需反混淆
        t  = load(fn, demangle=dm)
        raw= load(fn, demangle=False)
        nums=[int(x) for x in pm.findall(t)]
        probs = contiguous(nums) if nums else 0
        if probs==0:
            probs = contiguous([int(x) for x in nm.findall(raw)])
        rows.append(dict(year=yr, fn=fn, subj=SUBJ[fn], pages=len(pg.findall(raw)),
                         chars=len(raw), probs=probs, sub=len(sub.findall(t)),
                         sub_per=round(len(sub.findall(t))/probs,2) if probs else 0,
                         kb=round(len(raw.encode())/1024,1), demangle=dm))

KEYS = {
"代数与数论": ["Galois","irreducible","polynomial","finite group","representation","ideal","prime",
  "unramified","ramified","discriminant","valuation","p-adic","cyclotomic","character","module",
  "field extension","ring of integers","Frobenius","localization","inertia","splitting field",
  "cubic","residue","norm","tensor","category","equivalence of categories","semi-linear","coset","SL2"],
"几何与拓扑": ["metric","curvature","Euler characteristic","homotopy","homology","cohomology",
  "fundamental group","vector bundle","tangent bundle","Chern","Euler class","geodesic","minimal surface",
  "Ricci","scalar curvature","Killing","CP","sphere","manifold","immersion","embedding",
  "index","loop space","Poincar","characteristic class","Gauss map","Lie group","sectional curvature",
  "compact","aspherical","universal cover","Betti","conformal","Gaussian curvature",
  "geodesic curvature","Hessian","critical point","energy functional","isometric","disk"],
"分析与微分方程": ["heat equation","Fourier","Laplacian","harmonic","subharmonic","Sobolev","L2","BMO",
  "Plancherel","eigenvalue","self-adjoint","Banach","norm","maximum principle","boundary","Dirichlet",
  "convergence","compact support","integral","measure","holomorphic","fundamental solution",
  "Poisson summation","estimate","inequality","irrational","periodic","orthonormal basis","smooth"],
"计算与应用数学": ["finite element","finite difference","stability","convergence","quadrature",
  "Gaussian quadrature","Chebyshev","Legendre","Newton","BFGS","QR","singular value","subgradient",
  "convex","A-stable","spectral radius","trapezoid","iteration","tridiagonal","Crank-Nicolson","Euler",
  "mesh","discretiz","truncation error","eigenvalue","order of accuracy","flop","rank","perturbation",
  "norm","interpolation","orthogonal","least squares","variational","exact solution","stiff"],
"数学物理": ["Lagrangian","Hamiltonian","Ising","partition function","magnetization","susceptibility",
  "Maxwell","gauge","renormaliz","propagator","scalar field","black hole","gravitational wave",
  "de Sitter","Killing vector","harmonic oscillator","oscillation","angular momentum","energy","entropy",
  "specific heat","critical exponent","mean field","conformal","Klein","Riemann tensor","Christoffel",
  "quantum","spectrum","vacuum","Dirac","Yukawa","wave","photon","curvature"],
"概率统计": ["distribution","probability","normal","independent","random variable","copula","OLS",
  "covariate","density","expectation","estimator","regression","CDF","asymptotic","confidence interval",
  "i.i.d","median","ANOVA","Brownian","Poisson","characteristic function","log-likelihood","variance",
  "maximum likelihood","exponential family","convergence in distribution","unbiased","martingale"],
"通用/竞赛": ["show that","prove","assume","determine","compute","suppose","derive","construct","hint",
  "if and only if","justify","example","disprove","classify","counterexample"],
}

def count(keys, texts):
    out=[]
    for k in keys:
        kk=k.lower(); tot=0; files=0; by=collections.Counter()
        for fn,t in texts.items():
            c=t.lower().count(kk)
            if c: files+=1
            tot+=c; by[int(fn[:4])]+=c
        out.append((k,tot,files,by[2024],by[2025],by[2026]))
    out.sort(key=lambda r:(-r[1], r[0]))
    return out

alltext={}
for yr,fs in FILES.items():
    for fn in fs:
        alltext[fn]=load(fn, demangle=("Analysis_and_diff" in fn))

L=[]
L.append("# 丘成桐大学生数学竞赛 2024-2026 笔试真题 -- 自动统计结果")
L.append("")
L.append("生成脚本: .tmp/burn2026/scripts/yau_2024_2026_stats.py ; 语料目录: .tmp/burn2026/txt/")
L.append("说明: 2024 Analysis 卷为 Cambria-Math 抽取(字符错乱), 统计前做了反混淆映射 p->( q->) N-tilde->-> 等。")
L.append("")
L.append("## 1. 每卷结构统计")
L.append("")
L.append("| 年份 | 卷别 | 学科 | 页数 | 字符数 | KB | 题量 | 小问标记数 | 小问/题 | 抽取异常 |")
L.append("|---|---|---|---|---|---|---|---|---|---|")
for s in sorted(rows, key=lambda x:(x["year"], x["fn"])):
    L.append("| %d | 个人 | %s | %d | %d | %s | %d | %d | %s | %s |" % (
        s["year"], s["subj"], s["pages"], s["chars"], s["kb"], s["probs"], s["sub"],
        s["sub_per"], "Cambria-Math 错乱" if s["demangle"] else "-"))
L.append("")
L.append("## 2. 逐年汇总")
L.append("")
L.append("| 年份 | 卷数 | 总题量 | 总字符 | 平均题量/卷 | 平均小问/题 |")
L.append("|---|---|---|---|---|---|")
for yr in (2024,2025,2026):
    ss=[s for s in rows if s["year"]==yr]
    tp=sum(x["probs"] for x in ss); ts=sum(x["sub"] for x in ss)
    L.append("| %d | %d | %d | %d | %s | %s |" % (yr,len(ss),tp,sum(x["chars"] for x in ss),
             round(tp/len(ss),2), round(ts/tp,2)))
L.append("")
L.append("三年合计: **%d 题**, %d 字符。" % (sum(x["probs"] for x in rows), sum(x["chars"] for x in rows)))
L.append("")
L.append("## 3. 关键词 / 定理名频次 (全三年 18 卷合并)")
for grp, keys in KEYS.items():
    L.append("")
    L.append("### 3.x " + grp)
    L.append("")
    L.append("| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |")
    L.append("|---|---|---|---|---|---|")
    for k,tot,fs,a,b,c in count(keys, alltext):
        if tot: L.append("| %s | %d | %d | %d | %d | %d |" % (k,tot,fs,a,b,c))

TREND = {
 "proof-demanding: prove / show": r"\b(?:prove|show that)\b",
 "computation-demanding: compute/derive/determine/find/calculate": r"\b(?:compute|derive|determine|calculate|find)\b",
 "decision form: Does there exist / Is the / Can ...": r"\b(?:Does there exist|Is the|Is it|Is there|Are there|Can we|Can the|Can a|Does the)\b",
 "construct / counterexample / disprove": r"\b(?:construct|counterexample|disprove)\b",
 "sub-question marker (a)-(j)": r"\([a-j]\)",
 "sub-question marker (1)-(9)": r"\([1-9]\)",
 "'if and only if'": r"if and only if",
 "'Hint'": r"\bHint\b",
 "linear algebra words (matrix/eigenvalue/rank/orthogonal)": r"\b(?:matrix|matrices|eigenvalue|eigenvector|singular value|orthogonal|rank)\b",
 "curvature words": r"\b(?:curvature|Ricci|Riemann tensor|geodesic)\b",
 "p-adic / local field words": r"\b(?:p-adic|Qp|Zp|local field|unramified|ramified)\b",
 "numerical scheme words (finite element/difference/stability/scheme)": r"\b(?:finite element|finite difference|stabilit|scheme|discretiz)\b",
 "QFT words (renormaliz/propagator/counterterm/loop)": r"\b(?:renormaliz|propagator|counterterm|loop|Yukawa)\b",
 "GR words (black hole/gravitational wave/de Sitter)": r"\b(?:black hole|gravitational wave|de Sitter|general relativity)\b",
 "stochastic words (Brownian/martingale/stopping time)": r"\b(?:Brownian|martingale|stopping time)\b",
 "topology words (homotopy/homology/cohomology/bundle)": r"\b(?:homotopy|homology|cohomology|bundle|fundamental group)\b",
}
L.append("")
L.append("## 4. 命题风格趋势指标 (逐年出现次数)")
L.append("")
L.append("| 指标 | 2024 | 2025 | 2026 | 三年合计 |")
L.append("|---|---|---|---|---|")
for name, pat in TREND.items():
    rx=re.compile(pat, re.I); c=collections.Counter()
    for yr,fs in FILES.items():
        for fn in fs:
            c[yr]+=len(rx.findall(load(fn, demangle=("Analysis_and_diff" in fn))))
    L.append("| %s | %d | %d | %d | %d |" % (name, c[2024],c[2025],c[2026], c[2024]+c[2025]+c[2026]))

open(OUT,"w",encoding="utf-8").write("\n".join(L))
print("WROTE", OUT)
print()
for s in sorted(rows, key=lambda x:(x["year"], x["fn"])):
    print("%d %-28s pages=%d chars=%5d probs=%d sub=%3d sub/p=%s" % (
        s["year"], s["subj"], s["pages"], s["chars"], s["probs"], s["sub"], s["sub_per"]))
print()
for yr in (2024,2025,2026):
    ss=[s for s in rows if s["year"]==yr]
    print("%d: probs=%d chars=%d" % (yr, sum(x["probs"] for x in ss), sum(x["chars"] for x in ss)))
print("TOTAL probs:", sum(x["probs"] for x in rows), "chars:", sum(x["chars"] for x in rows))
print()
print("=== TREND ===")
for name, pat in TREND.items():
    rx=re.compile(pat, re.I); c=collections.Counter()
    for yr,fs in FILES.items():
        for fn in fs:
            c[yr]+=len(rx.findall(load(fn, demangle=("Analysis_and_diff" in fn))))
    print("%-62s %4d %4d %4d" % (name, c[2024],c[2025],c[2026]))
print()
print("=== KEYWORDS TOP ===")
for grp,keys in KEYS.items():
    print("--",grp); print("   ", ", ".join("%s:%d"%(k,t) for k,t,f,a,b,c in count(keys,alltext)[:20] if t))
