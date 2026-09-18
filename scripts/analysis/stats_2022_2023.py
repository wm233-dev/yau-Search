# -*- coding: utf-8 -*-
"""定量统计 2022/2023 丘成桐大学生数学竞赛笔试题文本。
输出: 文本表 + JSON (供报告引用)。"""
import os, re, json, glob, collections, io, sys

TXT = r".\txt"
OUT = r".\scripts"
os.makedirs(OUT, exist_ok=True)

files = sorted(glob.glob(os.path.join(TXT, "2022_*.txt")) + glob.glob(os.path.join(TXT, "2023_*.txt")))

SUBJ = {
    "algebra_and_numbertheory": "代数与数论",
    "Algebra_Number_theory": "代数与数论",
    "analysis_and_differential": "分析与微分方程",
    "Analysis_and_differential_equation": "分析与微分方程",
    "computational_and_applied": "计算与应用数学",
    "Computational_Applied": "计算与应用数学",
    "geometry_and_topology": "几何与拓扑",
    "Geometry_and_Topology": "几何与拓扑",
    "probability_and_statistics": "概率统计",
    "probability_statistics": "概率统计",
    "Mathematical_Physics": "数学物理",
}

def subject_of(fn):
    for k, v in SUBJ.items():
        if k in fn:
            return v
    return "?"

rows = []
all_text_by_year = {2022: [], 2023: []}
all_text_by_subj = collections.defaultdict(list)

for f in files:
    name = os.path.basename(f)
    raw = open(f, encoding="utf-8").read()
    year = int(name[:4])
    kind = "解答" if ("Solution" in name or "_soln" in name) else "试题"
    subj = subject_of(name)
    pages = len(re.findall(r"=== page \d+ ===", raw))
    chars = len(raw)
    nonspace = len(re.sub(r"\s", "", raw))
    # 题号: 'Problem N.' 或行首 'N.' / 'N. '  (排除小数点数字)
    probs = set()
    for m in re.finditer(r"(?m)^\s*Problem\s+(\d{1,2})\s*\.", raw):
        probs.add(int(m.group(1)))
    for m in re.finditer(r"(?m)^(\d{1,2})\.\s", raw):
        probs.add(int(m.group(1)))
    probs = {p for p in probs if 1 <= p <= 12}
    subparts = len(re.findall(r"\(([a-f])\)", raw))
    romans = len(re.findall(r"(?m)^\s*(i{1,3}v?|iv)\.\s", raw))
    pts = [int(x) for x in re.findall(r"\((\d{1,2})\s*points?\)", raw)]
    rows.append(dict(file=name, year=year, kind=kind, subject=subj, pages=pages,
                     chars=chars, nonspace=nonspace, nprob=len(probs),
                     probs=sorted(probs), subparts=subparts, romans=romans,
                     points=sum(pts), npoints=len(pts)))
    all_text_by_year[year].append(raw)
    all_text_by_subj[(year, subj)].append(raw)

print("=" * 110)
print("表 A  逐文件体量与题量")
print("=" * 110)
hdr = f"{'文件':<62}{'年':<6}{'类':<6}{'页':<5}{'字符':<8}{'非空白':<8}{'题数':<6}{'小题':<6}"
print(hdr)
for r in rows:
    print(f"{r['file']:<62}{r['year']:<6}{r['kind']:<6}{r['pages']:<5}{r['chars']:<8}{r['nonspace']:<8}{r['nprob']:<6}{r['subparts']:<6}")

print()
tot = collections.Counter()
for r in rows:
    tot[(r["year"], r["kind"])] += 1
print("文件数:", dict(tot))
print("总字符:", sum(r["chars"] for r in rows), " 总非空白:", sum(r["nonspace"] for r in rows))
print("总页(=== page ===):", sum(r["pages"] for r in rows))
print("试题文件总题数:", sum(r["nprob"] for r in rows if r["kind"] == "试题"))
print("解答文件带分值标记数:", sum(r["npoints"] for r in rows), " 分值和:", sum(r["points"] for r in rows))

print()
print("=" * 110)
print("表 B  2022 数学物理解答卷分值结构")
print("=" * 110)
mp = open(os.path.join(TXT, "2022_Solution_2022_Mathematical_Physics_solution.txt"), encoding="utf-8").read()
for m in re.finditer(r"\((\d{1,2})\s*points?\)", mp):
    print("  分值:", m.group(1))
print("  合计:", sum(int(m.group(1)) for m in re.finditer(r"\((\d{1,2})\s*points?\)", mp)))

# ---------- 关键词统计 ----------
KEYWORDS = {
 "代数/数论": ["Dedekind","projective","invertible","fractional ideal","Eisenstein","Galois","discriminant",
              "integral basis","number field","ring of integers","root of unity","p-adic","solvable",
              "commutator","free module","flat","finite presentation","profinite","finitely generated",
              "Lie algebra","representation","ideal","module","irreducible","minimal polynomial","trace","norm",
              "Chinese Remainder","uniformizer","logarithm","End"],
 "分析/方程": ["Banach","Ascoli","Arzel","Banach-Steinhaus","Gronwall","harmonic","holomorphic","Lebesgue",
              "weakly","weak convergence","entire","Laplacian","Lipschitz","positive definite","Fourier",
              "equicontinuous","compact","Cauchy","maximum principle","characteristic","resolvent","L2","ODE","PDE"],
 "几何/拓扑": ["Maurer-Cartan","Leray","Euler characteristic","homology","cohomology","Poincar","Killing",
              "Ricci","soliton","minimal surface","Gauss","Gauss-Bonnet","sectional curvature","fiber bundle",
              "flag","H-space","symmetric product","shrinker","geodesic","hypersurface","manifold","curvature",
              "diffeomorphism","normal","orient","fundamental group","homotopy","smooth","metric","Riemannian"],
 "概率统计": ["Markov chain","stationary","characteristic function","total variation","coupling","UMVUE",
              "minimax","sufficient","complete","Bayes","Dirichlet process","i.i.d","asymptotic","hypothesis",
              "power","unbiased","estimator","distribution","convergence in distribution","independen","random variable",
              "concentration","Poisson","Bernoulli","Gaussian","normal","uniform"],
 "计算/应用": ["finite difference","Runge-Kutta","Lax-Wendroff","Gaussian quadrature","orthogonal polynomial",
              "power iteration","dynamic programming","linear programming","consistency","stable","stability",
              "convergen","truncation error","Richardson","WKB","tridiagonal","eigenvalue","Gershgorin","Jacobian",
              "interpolation","Lagrange","norm","iteration","time-step","quadrature","power method","asymptotic expansion"],
 "数学物理": ["Killing","Lagrangian","Hamiltonian","Feynman","propagator","renormaliz","regulariz","one-loop",
             "gauge","Maxwell","Einstein","Schwarzschild","anti-unitary","time reversal","creation","annihilation",
             "commutation","su(2)","scale invariance","heat capacity","fermion","boson","Green's function",
             "cosmological constant","perturbation","Minkowski","Lorentz","Hilbert space","wave function",
             "spin","vacuum","dimensional regularization","propagator","Killing vector","Ricci","curvature"],
}
VERBS = ["Prove","Show","Compute","Calculate","Find","Determine","Construct","Derive","Explain","Solve",
         "Write down","Verify","Justify","Assume","State","Check","Give","Describe","List","Evaluate","Discuss"]
CN = ["证明","计算","求","构造","说明","解释","推导"]

def count_ci(text, kw):
    return len(re.findall(re.escape(kw), text, flags=re.IGNORECASE))

exam = {y: "".join(all_text_by_year[y]) for y in (2022, 2023)}
exam_only = {y: "".join(r["chars"] and open(os.path.join(TXT, r["file"]), encoding="utf-8").read()
                        for r in rows if r["year"] == y and r["kind"] == "试题") for y in (2022, 2023)}

print()
print("=" * 110)
print("表 C  关键词/定理名频次（2022 全部18个文件 vs 2023 全部文本；含试题+解答）")
print("=" * 110)
print(f"{'类别':<12}{'关键词':<26}{'2022':<8}{'2023':<8}{'合计':<8}")
kw_flat = []
for cat, kws in KEYWORDS.items():
    seen = set()
    for kw in kws:
        if kw.lower() in seen:
            continue
        seen.add(kw.lower())
        c22 = count_ci(exam[2022], kw)
        c23 = count_ci(exam[2023], kw)
        if c22 + c23 == 0:
            continue
        kw_flat.append(dict(cat=cat, kw=kw, c22=c22, c23=c23, tot=c22 + c23))
        print(f"{cat:<12}{kw:<26}{c22:<8}{c23:<8}{c22+c23:<8}")
kw_flat.sort(key=lambda d: -d["tot"])

print()
print("=" * 110)
print("表 D  疑问动词/指令词频次（2022 试题卷合并 vs 2023 试题卷合并）")
print("=" * 110)
print(f"{'动词':<16}{'2022':<8}{'2023':<8}{'合计':<8}")
verb_flat = []
for v in VERBS:
    c22 = count_ci(exam_only[2022], v)
    c23 = count_ci(exam_only[2023], v)
    verb_flat.append(dict(v=v, c22=c22, c23=c23, tot=c22 + c23))
    print(f"{v:<16}{c22:<8}{c23:<8}{c22+c23:<8}")
for v in CN:
    c22 = count_ci(exam_only[2022], v); c23 = count_ci(exam_only[2023], v)
    print(f"{v:<16}{c22:<8}{c23:<8}{c22+c23:<8}")

print()
print("=" * 110)
print("表 E  按科目汇总（试题卷）")
print("=" * 110)
print(f"{'年份':<6}{'科目':<18}{'字符':<8}{'题数':<6}{'小题(a-e)':<10}{'页':<5}")
for (y, s), texts in sorted(all_text_by_subj.items()):
    t = "".join(texts)
    rs = [r for r in rows if r["year"] == y and r["subject"] == s and r["kind"] == "试题"]
    if not rs:
        continue
    print(f"{y:<6}{s:<18}{sum(r['chars'] for r in rs):<8}{sum(r['nprob'] for r in rs):<6}"
          f"{sum(r['subparts'] for r in rs):<10}{sum(r['pages'] for r in rs):<5}")

print()
print("=" * 110)
print("表 F  年份彩蛋数字（试题卷中出现的 2022/2023 等年份数字，排除标题行）")
print("=" * 110)
for y in (2022, 2023):
    for yy in (2022, 2023):
        c = 0
        for r in rows:
            if r["year"] != y or r["kind"] != "试题":
                continue
            txt = open(os.path.join(TXT, r["file"]), encoding="utf-8").read()
            for line in txt.splitlines():
                if "Yau College" in line or "Contests 20" in line:
                    continue
                c += len(re.findall(str(yy), line))
        print(f"  {y} 年试题卷中出现 '{yy}' 次数: {c}")

json.dump(dict(rows=rows, keywords=kw_flat, verbs=verb_flat), open(os.path.join(OUT, "stats_2022_2023.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\n[JSON 已写入]", os.path.join(OUT, "stats_2022_2023.json"))
