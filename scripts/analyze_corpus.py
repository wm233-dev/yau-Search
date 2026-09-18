# -*- coding: utf-8 -*-
"""Yau corpus structural analysis (ligature normalisation, problem splitting,
subject/year tables, keyword taxonomy, cross-year near-duplicate detection)."""
import os, io, re, json, itertools, collections

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT  = os.path.join(ROOT, "txt")
DATA = os.path.join(ROOT, "data")
REP  = os.path.join(ROOT, "reports")
os.makedirs(DATA, exist_ok=True)
os.makedirs(REP, exist_ok=True)

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi",
       "\ufb04": "ffl", "\u2019": "'", "\u2018": "'", "\u201c": '"',
       "\u201d": '"', "\u2013": "-", "\u2014": "--", "\u00a0": " "}

def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = s.replace("\r\n", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    return s

SUBJECTS = [
    ("Algebra & Number Theory", r"algebra|numbertheory|number_theory"),
    ("Analysis & PDE",          r"analysis"),
    ("Geometry & Topology",     r"geometry|geomtop|geo_topo|topology"),
    ("Probability & Statistics", r"probab|statistic|proba|stat"),
    ("Computational & Applied", r"applied|comput|computation"),
    ("Mathematical Physics",    r"physic"),
]

def subject_of(name):
    low = name.lower()
    for label, pat in SUBJECTS:
        if re.search(pat, low):
            return label
    return "Mixed/Team(multi-subject)"

def year_of(name):
    m = re.match(r"(\d{4})_", name)
    return m.group(1) if m else "????"

def kind_of(name):
    low = name.lower()
    if "soln" in low or "solution" in low:
        return "solution"
    if "team" in low:
        return "team"
    return "individual"

PROB_RE = re.compile(r"(?m)^[ \t]*(?:Problem[ \t]*)?(\d{1,2})[.、][ \t]")

def split_problems(text, limit=None):
    cands = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(text)]
    best = []
    n = len(cands)
    for i in range(n):
        if cands[i][1] != 1:
            continue
        run = [cands[i]]
        want = 2
        for j in range(i + 1, n):
            if cands[j][1] == want:
                run.append(cands[j]); want += 1
        if len(run) > len(best):
            best = run
    probs = []
    for idx, (start, num, end) in enumerate(best):
        stop = best[idx + 1][0] if idx + 1 < len(best) else len(text)
        probs.append((num, text[end:stop].strip()))
    if limit:
        probs = probs[:limit]
    return probs

KEYWORDS = {
 "Algebra & Number Theory": [
   "Galois","field extension","finite field","splitting field","irreducible polynomial","characteristic",
   "group action","Sylow","normal subgroup","solvable","nilpotent","semisimple","Jordan form","eigenvalue",
   "determinant","rank","module","ideal","localization","Noetherian","PID","UFD","tensor product","exact sequence",
   "representation","character","quadratic form","bilinear","Hermitian","orthogonal","unitary",
   "prime","Diophantine","congruence","reciprocity","p-adic","valuation","algebraic integer","elliptic curve",
   "zeta function","Mobius","continued fraction","transcendental","resultant","discriminant","ramification",
   "category","functor","homological","projective","injective","Nakayama","Hilbert basis"],
 "Analysis & PDE": [
   "holomorphic","analytic","Cauchy","maximum principle","harmonic","subharmonic","Poisson kernel",
   "Schwarz","Montel","normal family","Riemann mapping","entire","meromorphic","residue",
   "Lebesgue","measurable","Radon-Nikodym","absolutely continuous","bounded variation","weak derivative",
   "distribution","Sobolev","compactness","Banach","Hilbert space","fixed point","contraction",
   "Fourier","Laplace","heat equation","wave equation","elliptic","parabolic","hyperbolic",
   "Green function","Dirichlet problem","Neumann","Harnack","Schauder","energy estimate",
   "eigenfunction","spectrum","Sturm-Liouville","variational","Euler-Lagrange","Riesz","Hahn-Banach",
   "uniform convergence","equicontinuous","Arzela","Holder","Lipschitz"],
 "Geometry & Topology": [
   "manifold","smooth","diffeomorphism","immersion","submersion","tangent","vector field",
   "fundamental group","covering space","homotopy","homology","cohomology","Euler characteristic",
   "CW complex","simplicial","singular","Mayer-Vietoris","Kunneth","cup product","Poincare duality",
   "de Rham","differential form","Stokes","exterior derivative","closed form","exact form",
   "Riemannian","metric","curvature","geodesic","connection","parallel transport","holonomy",
   "fiber bundle","vector bundle","principal bundle","Chern class","Pontryagin","characteristic class",
   "Morse","critical point","index","symplectic","Kahler","complex structure","almost complex",
   "embedding","Whitney","tubular neighborhood","transversality","degree","winding number","Borsuk"],
 "Probability & Statistics": [
   "random variable","distribution","expectation","variance","covariance","independence",
   "conditional","Bayes","prior","posterior","martingale","stopping time","optional stopping",
   "Brownian motion","random walk","Markov chain","Poisson process","renewal","ergodic",
   "central limit","law of large numbers","characteristic function","moment generating","large deviation",
   "estimator","unbiased","efficiency","maximum likelihood","sufficient statistic","Cramer-Rao",
   "confidence interval","hypothesis test","likelihood ratio","decision rule","risk function",
   "regression","linear model","nonparametric","bootstrap","order statistic","quantile",
   "Poisson","Gaussian","exponential","binomial","chi-square","Fisher information"],
 "Computational & Applied": [
   "finite difference","finite element","numerical","discretization","iteration","convergence rate",
   "condition number","stability","truncation error","round-off","interpolation","quadrature",
   "Newton method","gradient descent","conjugate gradient","Krylov","multigrid","preconditioner",
   "linear programming","simplex","duality","optimization","KKT","Lagrange multiplier","convex",
   "Monte Carlo","importance sampling","fast Fourier","spectral method","stiff","Runge-Kutta",
   "matrix factorization","LU","QR","SVD","eigenvalue problem","sparse","graph algorithm",
   "machine learning","neural network","least squares","regularization","singular value"],
 "Mathematical Physics": [
   "Hamiltonian","Lagrangian","action","variational principle","Noether","conservation law",
   "Poisson bracket","symplectic form","canonical transformation","Hamilton-Jacobi","Liouville",
   "Schrodinger","wave function","quantum","operator","commutator","uncertainty","spectral theorem",
   "Maxwell","electromagnetic","gauge","Yang-Mills","relativity","Lorentz","Minkowski",
   "statistical mechanics","partition function","entropy","Boltzmann","Gibbs","Ising","phase transition",
   "fluid","Navier-Stokes","Euler equation","elasticity","scattering","dispersion",
   "momentum","angular momentum","field theory"],
}

def count_keywords(text, terms):
    low = text.lower()
    out = {}
    for t in terms:
        pat = r"\b" + re.escape(t.lower()).replace(r"\ ", r"[\s\-]+") + r"\b"
        out[t] = len(re.findall(pat, low))
    return out

files = sorted(f for f in os.listdir(TXT) if f.endswith(".txt"))
records = []
for fn in files:
    name = fn[:-4]
    text = norm(io.open(os.path.join(TXT, fn), encoding="utf-8").read())
    limit = None
    m = re.search(r"\((\d+)\s+problems?\)", text, re.I)
    if m:
        limit = int(m.group(1))
    probs = split_problems(text, limit)
    subj = subject_of(name)
    rec = {"file": fn, "name": name, "year": year_of(name), "subject": subj, "kind": kind_of(name),
           "pages": text.count("=== page "), "chars": len(text),
           "declared_problems": limit, "n_problems": len(probs),
           "problems": [{"n": n, "chars": len(b), "head": " ".join(b.split())[:400]} for n, b in probs]}
    rec["keywords"] = count_keywords(text, KEYWORDS.get(subj, []))
    records.append(rec)

json.dump(records, io.open(os.path.join(DATA, "papers.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

def shingles(s, k=6):
    w = re.findall(r"[a-z]{3,}", s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(0, len(w)-k+1)))

prob_items = []
for rec in records:
    if rec["kind"] == "solution":
        continue
    raw = norm(io.open(os.path.join(TXT, rec["file"]), encoding="utf-8").read())
    for n, body in split_problems(raw, rec["declared_problems"]):
        prob_items.append({"key": "%s/%s/Q%d" % (rec["year"], rec["subject"], n),
                           "year": rec["year"], "subject": rec["subject"], "n": n,
                           "sh": shingles(body)})
pairs = []
for a, b in itertools.combinations(prob_items, 2):
    if not a["sh"] or not b["sh"]:
        continue
    inter = len(a["sh"] & b["sh"])
    if inter < 4:
        continue
    j = inter / len(a["sh"] | b["sh"])
    if j >= 0.15:
        pairs.append({"a": a["key"], "b": b["key"], "jaccard": round(j, 3), "shared": inter})
pairs.sort(key=lambda x: -x["jaccard"])
json.dump(pairs[:500], io.open(os.path.join(DATA, "near_duplicates.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

lines = []
lines.append("# Yau 竞赛语料库结构分析（analyze_corpus.py 自动生成）\n")
lines.append("来源目录：.tmp/yau/2010-2026历年笔试真题 -> PyMuPDF 抽取为纯文本 -> 本报告统计。\n")
lines.append("## 1. 语料总览\n")
lines.append("| 年份 | 文件数 | 试卷(非解答) | 解答 | 抽取题数 | 字符数 |")
lines.append("|---|---|---|---|---|---|")
by_year = collections.defaultdict(lambda: {"f":0,"p":0,"s":0,"q":0,"c":0})
for r in records:
    d = by_year[r["year"]]
    d["f"] += 1; d["c"] += r["chars"]
    if r["kind"] == "solution": d["s"] += 1
    else:
        d["p"] += 1; d["q"] += r["n_problems"]
for y in sorted(by_year):
    d = by_year[y]
    lines.append("| %s | %d | %d | %d | %d | %d |" % (y, d["f"], d["p"], d["s"], d["q"], d["c"]))
tot = {k: sum(d[k] for d in by_year.values()) for k in ("f","p","s","q","c")}
lines.append("| **合计** | **%d** | **%d** | **%d** | **%d** | **%d** |" % (tot["f"],tot["p"],tot["s"],tot["q"],tot["c"]))
lines.append("")
lines.append("## 2. 科目 x 年份 题量矩阵\n")
years = sorted(by_year)
matrix = collections.defaultdict(lambda: collections.defaultdict(int))
for r in records:
    if r["kind"] == "solution": continue
    matrix[r["subject"]][r["year"]] += r["n_problems"]
lines.append("| 科目 | " + " | ".join(years) + " | 合计 |")
lines.append("|" + "---|" * (len(years) + 2))
for s in sorted(matrix):
    row = [matrix[s][y] for y in years]
    lines.append("| %s | %s | %d |" % (s, " | ".join(str(v) for v in row), sum(row)))
lines.append("")
lines.append("## 3. 高频考点词频（跨全部年份合计，仅列 >=3 次）\n")
agg = collections.defaultdict(collections.Counter)
for r in records:
    if r["kind"] == "solution": continue
    for k, v in r["keywords"].items():
        agg[r["subject"]][k] += v
for s in sorted(agg):
    items = [(k, v) for k, v in agg[s].most_common() if v >= 3]
    if not items: continue
    lines.append("### " + s + "\n")
    lines.append("| 考点 | 次数 |")
    lines.append("|---|---|")
    for k, v in items:
        lines.append("| %s | %d |" % (k, v))
    lines.append("")
lines.append("## 4. 跨年近似重复题（词元 6-gram Jaccard >= 0.15）\n")
lines.append("共发现 %d 对，前 40 对：\n" % len(pairs))
lines.append("| 题目A | 题目B | Jaccard | 共享 shingle |")
lines.append("|---|---|---|---|")
for p in pairs[:40]:
    lines.append("| %s | %s | %.3f | %d |" % (p["a"], p["b"], p["jaccard"], p["shared"]))
lines.append("")
io.open(os.path.join(REP, "stats_overview.md"), "w", encoding="utf-8").write("\n".join(lines))

print("papers:", len(records), "problems:", tot["q"], "dup_pairs:", len(pairs), "prob_items:", len(prob_items))
for y in sorted(by_year):
    d = by_year[y]
    print("year", y, "papers", d["p"], "soln", d["s"], "problems", d["q"])
print("REPORT", os.path.join(REP, "stats_overview.md"))
