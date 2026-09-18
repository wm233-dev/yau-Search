# -*- coding: utf-8 -*-
"""统计 2019-2021 年丘成桐大学生数学竞赛笔试题（含官方解答）的结构与关键词频。
用法: python stats_2019_2021.py
说明: 计数为「正则全文匹配次数」，不是「题目数量」；ligature(ﬁ/ﬀ) 已归一化。
"""
import os, re, json

TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
OUT_MD = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\kw_2019_2021.md"
OUT_JSON = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\stats_2019_2021.json"

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi",
       "\ufb04": "ffl", "\u02dc": "~", "\u00a8": "", "\u02dd": ""}

def load(p):
    s = open(p, "rb").read().decode("utf-8", errors="replace")
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = "".join(ch if (ord(ch) >= 32 or ch in "\n\t") else " " for ch in s)
    return s

files = sorted(f for f in os.listdir(TXT)
               if f.endswith(".txt") and re.match(r"^(2019|2020|2021)_", f))

SUBJ = [("algebra", "Algebra & Number Theory"), ("numbertheory", "Algebra & Number Theory"),
        ("analysis", "Analysis & Differential Eq."), ("differential", "Analysis & Differential Eq."),
        ("applied", "Computational & Applied"), ("computational", "Computational & Applied"),
        ("geometry", "Geometry & Topology"), ("topology", "Geometry & Topology"),
        ("proba", "Probability & Statistics"), ("stat", "Probability & Statistics")]

def subject(f):
    low = f.lower()
    for k, v in SUBJ:
        if k in low:
            return v
    return "?"

def kind(f):
    low = f.lower()
    if "soln" in low or "solution" in low:
        return "官方解答"
    if "team" in low:
        return "团体卷"
    return "试卷"

rows, corpus_exam, corpus_soln = [], [], []
for f in files:
    s = load(os.path.join(TXT, f))
    year, k = f[:4], kind(f)
    pages = len(re.findall(r"=== page \d+ ===", s))
    if year == "2019":
        nprob = len(re.findall(r"(?m)^\s*\d+\)\s", s))
    else:
        nprob = len(re.findall(r"(?m)^\s*Problem\s+\d+\s*[\.\:]", s))
    rows.append(dict(file=f, year=year, subject=subject(f), kind=k,
                     pages=pages, chars=len(s), probs=nprob))
    (corpus_exam if k == "试卷" else corpus_soln).append(s)

KEYWORDS = [
 ("Galois 理论", r"Galois"),
 ("有限域 Fp/Fq", r"finite field|\bFp\b|\bFq\b|\bF p\b"),
 ("分圆域/分圆多项式", r"cyclotomic"),
 ("p 进数 Zp/Qp", r"p-adic|\bZp\b|\bQp\b|Z p\b|Q p\b"),
 ("素理想/极大理想", r"prime ideal|maximal ideal"),
 ("Noether 环", r"Noetherian"),
 ("整扩张/整闭（normalization）", r"integral extension|integral closure|integrally closed|integral over|normalization"),
 ("Dedekind 环/类数", r"Dedekind|class number"),
 ("理想 ideal", r"\bideals?\b"),
 ("不可约/Eisenstein", r"irreducible|Eisenstein"),
 ("分裂域/自同构群", r"splitting field|automorphism group"),
 ("幂零/特征多项式", r"nilpotent|characteristic polynomial"),
 ("迹/Newton 恒等式", r"\btrace\b|Newton.?s identit"),
 ("有限群/置换群/中心化子", r"finite group|permutation|centralis|centraliz"),
 ("表示论/特征标", r"representation|character "),
 ("Hensel/分歧", r"Hensel|ramified|unramified|ramification"),
 ("Witt 向量", r"Witt"),
 ("Gauss 和/二次剩余", r"Gauss sum|Legendre|quadratic resid"),
 ("范映射 norm", r"norm map|\bnorm\b"),
 ("全纯/整函数", r"holomorphic|entire function|meromorphic"),
 ("Liouville/Picard 定理", r"Liouville|Picard"),
 ("极值原理", r"maximum principle"),
 ("调和函数", r"harmonic"),
 ("Poisson/Laplace 方程", r"Poisson|Laplace|Laplacian|\u25b3"),
 ("Fourier（变换/系数）", r"Fourier"),
 ("卷积", r"convolution"),
 ("Lebesgue 测度/可测", r"Lebesgue|measurable|measure"),
 ("Sobolev 空间/H^1_0", r"Sobolev|H1\s*0|W1,2|W\^"),
 ("Schauder/Holder 估计", r"Schauder|H.{0,2}older"),
 ("a priori 估计", r"a priori"),
 ("变分/能量泛函/极小化", r"variational|energy functional|minimiz|minimis"),
 ("Bochner 公式", r"Bochner"),
 ("Jacobi 场/测地线/指数映射", r"Jacobi|geodesic|exponential map"),
 ("曲率（Ricci/截面/Riemann）", r"Ricci|sectional curvature|curvature tensor|Riemannian curvature|curvature"),
 ("Killing 向量场", r"Killing"),
 ("Bishop-Gromov/分裂定理", r"Bishop|Gromov|splitting theorem"),
 ("平均曲率", r"mean curvature"),
 ("等距 isometry", r"isometr"),
 ("Stiefel-Whitney/可定向", r"Stiefel-Whitney|orientab"),
 ("Euler 示性数/signature/Mayer-Vietoris", r"Euler characteristic|signature|Mayer-Vietoris"),
 ("上同调/De Rham", r"cohomology|de Rham"),
 ("基本群/同伦群", r"fundamental group|homotopy"),
 ("覆叠空间", r"covering"),
 ("向量丛/切丛", r"vector bundle|tangent bundle|normal bundle|disk bundle"),
 ("Lie 群 SO(n)/SU(n)", r"Lie group|SO\(|SU\(|U\(n\)|O\(n\)"),
 ("自由群", r"free group"),
 ("环面/球面", r"torus|T 2|\bS2\b|\bS4\b|\bS6\b|\bS11\b|sphere"),
 ("配边/boundary of compact", r"boundary of a compact|cobord"),
 ("VC 维", r"VC dimension|VC\(H\)"),
 ("特征值/奇异值/SVD", r"eigenvalue|eigenvector|singular value|SVD"),
 ("矩阵范数/非奇异", r"\bnorm|nonsingular|full-rank"),
 ("幂法 power method", r"power method"),
 ("迭代/不动点/Newton 法", r"iteration|fixed point|Newton"),
 ("截断误差/精度阶", r"truncation error|order of accuracy|order of the"),
 ("稳定性多项式/稳定域/von Neumann", r"stability polynomial|stability region|von Neumann|unconditionally stable|\bstable\b|\bstability\b"),
 ("Runge-Kutta/Stoermer/多步法", r"Runge-Kutta|St.{0,2}rmer|two-step|multi-step|multistep|semi-implicit"),
 ("差分格式", r"difference scheme|difference|scheme"),
 ("有限元/Galerkin", r"finite element|Galerkin|FEM|CG\("),
 ("先验误差估计 (FEM)", r"a priori error"),
 ("Chebyshev/插值/Lagrange", r"Chebyshev|interpolat|Lagrange"),
 ("样条 spline", r"spline"),
 ("求积公式 quadrature", r"quadrature"),
 ("凸优化/投影/Lipschitz", r"convex|projection|Lipschitz"),
 ("Markov 链/常返", r"Markov chain|recurrent|transition"),
 ("鞅/停时", r"martingale|stopping"),
 ("Borel-Cantelli/大数律", r"Borel-Cantelli|law of large numbers|almost surely"),
 ("中心极限/Lindeberg/正态", r"central limit|Lindeberg|gaussian|normal random|normal distribution"),
 ("特征函数", r"characteristic function"),
 ("Poisson 分布", r"Poisson"),
 ("独立同分布 i.i.d.", r"i\.i\.d|independent"),
 ("Erdos-Renyi 随机图", r"random graph|Erd.{0,2}s-R.{0,2}nyi|Erdos"),
 ("随机游走", r"random walk"),
 ("因果效应/潜在结果", r"causal|potential outcome|treatment effect|treatment e"),
 ("无偏估计/SUTVA/estimand", r"unbiased|SUTVA|estimand"),
 ("随机化/再随机化/allocation", r"randomiz|re-randomization|allocation"),
 ("Mahalanobis/协变量平衡", r"Mahalanobis|covariate"),
 ("置换的轮换数", r"number of cycles"),
]

def count(pat, text):
    return len(re.findall(pat, text, flags=re.I))

exam_text = "\n".join(corpus_exam)
soln_text = "\n".join(corpus_soln)

L = []
L.append("# 2019-2021 丘赛笔试语料统计（stats_2019_2021.py 自动生成）\n")
L.append("口径：正则全文匹配次数（非题目数）；ligature(ﬁ/ﬀ) 已归一化；含解答文件单独成列。\n")
L.append("## 1. 文件级结构\n")
L.append("| 年份 | 文件 | 类型 | 学科 | 页数 | 字符数 | 抽取题数 |")
L.append("|---|---|---|---|---|---|---|")
for r in rows:
    L.append("| {} | {} | {} | {} | {} | {} | {} |".format(
        r["year"], r["file"], r["kind"], r["subject"], r["pages"], r["chars"], r["probs"]))
L.append("\n## 2. 关键词频（试卷正文 / 官方解答 / 合计）\n")
L.append("| 关键词/考点 | 试卷 | 解答 | 合计 |")
L.append("|---|---|---|---|")
kws = []
for name, pat in KEYWORDS:
    a, b = count(pat, exam_text), count(pat, soln_text)
    kws.append(dict(name=name, exam=a, soln=b, total=a + b))
    L.append("| {} | {} | {} | {} |".format(name, a, b, a + b))
L.append("\n## 3. 汇总\n")
L.append("- 试卷正文合计字符：{}".format(len(exam_text)))
L.append("- 官方解答合计字符：{}".format(len(soln_text)))
L.append("- 试卷页数合计：{}".format(sum(r["pages"] for r in rows if r["kind"] == "试卷")))
L.append("- 解答页数合计：{}".format(sum(r["pages"] for r in rows if r["kind"] == "官方解答")))
L.append("- 试卷抽取题数合计：{}".format(sum(r["probs"] for r in rows if r["kind"] != "官方解答")))

md = "\n".join(L)
open(OUT_MD, "w", encoding="utf-8").write(md)
json.dump(dict(rows=rows, kw=kws,
               totals=dict(exam_chars=len(exam_text), soln_chars=len(soln_text))),
          open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(md)
