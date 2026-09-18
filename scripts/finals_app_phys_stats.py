# -*- coding: utf-8 -*-
"""Statistics for Yau FINALS corpus, scope = Applied & Computational Math + Mathematical Physics.

Inputs : .tmp/burn2026/data/finals_manifest.json  (+ txt_finals/*.txt)
Outputs: .tmp/burn2026/scripts/finals_app_phys_stats.json
         .tmp/burn2026/scripts/finals_app_phys_tables.md
"""
import json, os, re, io, collections, statistics

BASE = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT = os.path.join(BASE, "txt_finals")
MAN = os.path.join(BASE, "data", "finals_manifest.json")
OUTJ = os.path.join(BASE, "scripts", "finals_app_phys_stats.json")
OUTM = os.path.join(BASE, "scripts", "finals_app_phys_tables.md")

SCOPE = ("Applied", "Mathematical_Physics")

def load():
    man = json.load(open(MAN, encoding="utf-8"))
    recs = []
    for x in man:
        rel = x["rel"]
        top = rel.split(os.sep)[0]
        if not any(s in top for s in SCOPE):
            continue
        parts = rel.split(os.sep)
        kind = parts[1] if len(parts) > 2 else "(root)"
        fn = parts[-1]
        ym = re.search(r"(20\d\d)", fn)
        year = ym.group(1) if ym else "n/a"
        txt = ""
        p = os.path.join(TXT, x["txt"]) if x.get("txt") else None
        if p and os.path.exists(p):
            txt = open(p, encoding="utf-8", errors="replace").read()
        body = re.sub(r"^=== page \d+ ===$", "", txt, flags=re.M)
        recs.append(dict(rel=rel, subj=top, kind=kind, year=year, file=fn,
                         chars=x["chars"], pages=x["pages"], text=body))
    # --- 2020 recovery: the three 2020 PDFs are password protected (Yau-ACM20);
    # PyMuPDF can authenticate them, so the "0 chars" in the manifest is an
    # artefact.  _finals_2020_extract.py dumps them here.
    recdir = os.path.join(BASE, "scripts", "_finals_2020")
    if os.path.isdir(recdir):
        for fn in sorted(os.listdir(recdir)):
            if not fn.endswith(".txt"):
                continue
            t = open(os.path.join(recdir, fn), encoding="utf-8", errors="replace").read()
            kind = "Overall" if "Overall" in fn else "Individual"
            tag_ = "set2" if "set2" in fn else ("set1" if "set1" in fn else "")
            recs.append(dict(rel=os.path.join("2012-2025Applied Math and Computational Math",
                                              kind, fn), subj="Applied", kind=kind,
                             year="2020", file=fn, chars=len(t), pages=t.count("=== page"),
                             text=re.sub(r"^=== page d+ ===$", "", t, flags=re.M)))
    return recs

HEAD_STOP = re.compile(r"^\s*(?:===|Figure\s*\d|Table\s*\d|Hint\b|References?\b)", re.I)
LABEL = re.compile(r"^\s*(?:Problem|Prob\.?|Question|Q)\s*[.:]?\s*(\d{1,2}|I{1,3}V?|IV|V)\b", re.I)
NUM = re.compile(r"^\s*(\d{1,2})\s*[.)]\s*(?=[A-Za-z(\[\$])")

def _label_marks(lines):
    out = []
    for i, ln in enumerate(lines):
        if HEAD_STOP.match(ln):
            continue
        m = LABEL.match(ln)
        if m:
            out.append((i, "L:" + re.sub(r"\s+", "", m.group(0))[:16]))
    return out

def _num_marks(lines):
    out, exp = [], 1
    for i, ln in enumerate(lines):
        if HEAD_STOP.match(ln):
            continue
        m = NUM.match(ln)
        if not m:
            continue
        n = int(m.group(1))
        if n == exp:
            out.append((i, "N:%d" % n))
            exp = n + 1
    return out

def segment(text):
    if not text.strip():
        return []
    lines = text.split("\n")
    lm = _label_marks(lines)
    marks = lm if len(lm) >= 2 else _num_marks(lines)
    if not marks:
        return [("(whole)", text)]
    out = []
    for k, (ln, lab) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        chunk = "\n".join(lines[ln:end])
        if len(chunk) < 20:
            continue
        out.append((lab, chunk))
    return out

SUBPART = re.compile(r"(?:^|\n|\s)\(([a-e]|[ivx]{1,4}|\d)\)")
SYM = re.compile(r"[=<>+\-*/^_{}\\]|\\int|\\sum|\\nabla|\\partial|\\frac")

TOPICS = [
    ("数值线性代数/矩阵分解", [r"LU factoriz", r"Givens", r"Cholesky", r"Householder", r"\bQR\b",
        r"condition number", r"singular value", r"tridiagonal", r"companion matrix", r"eigenvalue",
        r"eigenvector", r"power iteration", r"Arnoldi", r"Lanczos", r"Krylov", r"GMRES",
        r"Richardson", r"steepest descent", r"conjugate gradient", r"spectral radius",
        r"matrix norm", r"inverse matrix"]),
    ("迭代法收敛性(Jacobi/GS/不动点)", [r"Jacobi", r"Gauss-Seidel", r"Gauss.Seidel", r"fixed.point",
        r"fixed point", r"iterative method", r"contraction"]),
    ("非线性方程/牛顿法", [r"Newton'?s method", r"Newton iteration", r"Newton-type", r"Newton method",
        r"bisection", r"quasi-Newton", r"secant"]),
    ("插值/逼近与求积", [r"interpolat", r"trapezoidal", r"Simpson", r"spline", r"least.square",
        r"piecewise linear"]),
    ("常微分方程数值解", [r"multi-rate", r"Runge-Kutta", r"explicit Euler", r"stiff",
        r"time.marching", r"forward difference scheme", r"locally second order", r"order of accuracy",
        r"local second order"]),
    ("PDE 有限差分/CFL/von Neumann", [r"CFL", r"von Neumann", r"amplification factor",
        r"finite difference", r"stencil", r"leapfrog", r"Lax equivalence", r"upwind", r"advection",
        r"transport equation", r"heat equation", r"Burgers", r"Klein-Gordon", r"Allen-Cahn",
        r"reaction.diffusion", r"parabolic equation", r"central difference", r"stability of the scheme",
        r"stability of this scheme", r"numerical stability"]),
    ("有限元/弱解/Sobolev", [r"finite element", r"weak solution", r"weak formulation", r"Sobolev",
        r"H_?0\^?1", r"\bH1\b", r"H1\b", r"affine.equivalent", r"shape.regular", r"Galerkin",
        r"triangulation", r"a priori error", r"convergence rate", r"piecewise affine"]),
    ("能量稳定/能量守恒格式", [r"energy stable", r"energy stability", r"energy functional",
        r"Hamiltonian is conserved", r"energy conserved", r"dissipation", r"unconditional"]),
    ("变分法/Euler-Lagrange/最优化", [r"Euler-Lagrange", r"Euler.Lagrangian", r"variational problem",
        r"minimi[sz]", r"convex conjugate", r"Legendre transform", r"Fenchel", r"proximal",
        r"simplex method", r"interior method", r"penalty", r"dynamic programming", r"linear programming",
        r"optimal mass transport", r"optimal transport"]),
    ("反问题/正则化/稀疏", [r"inverse problem", r"regulariz", r"Rudin-Osher-Fatemi", r"cartoon",
        r"total variation", r"sparse", r"compressed sens", r"sparse recovery", r"Fr[eé]chet"]),
    ("渐近分析/奇异摄动/边界层", [r"asymptotic", r"boundary layer", r"singular perturbation",
        r"stationary phase", r"order of magnitude", r"uniform approximation", r"leading.order",
        r"matched", r"epsilon .{0,12}0"]),
    ("谱方法/FFT/Fourier", [r"Fourier", r"spectral (?:order|method|accuracy)", r"trigonometric",
        r"fast Fourier", r"\bFFT\b"]),
    ("离散微分几何/网格/共形", [r"triangle mesh", r"simplicial", r"Gauss-Bonnet", r"circle packing",
        r"conformal factor", r"discrete curvature", r"Voronoi", r"power diagram", r"surface .{0,12}mesh",
        r"mesh quality", r"discrete conformal", r"surface tangential"]),
    ("概率/随机过程/统计物理", [r"random walk", r"probability density", r"Brownian", r"Monte.Carlo",
        r"partition function", r"entropy", r"Ising", r"Gibbs free energy", r"canonical",
        r"heat kernel", r"path integral", r"Feynman gas", r"grand canonical", r"statistical mechanics"]),
    ("凸分析/机器学习(softmax)", [r"softmax", r"log-sum-exp", r"neural", r"convex conjugate",
        r"proximal operator", r"biconjugate"]),
    ("流体力学/连续介质", [r"Navier-Stokes", r"fluid", r"conservation of (?:mass|momentum)",
        r"Stokes equation", r"incompressible", r"velocity field", r"compressible", r"droplet",
        r"surface tension"]),
    ("经典力学/哈密顿-拉格朗日", [r"Lagrangian", r"Hamiltonian", r"Hamilton.s equation",
        r"Poisson bracket", r"canonical transformation", r"rigid body", r"Kepler", r"Noether",
        r"relativistic (?:mechanics|Hamiltonian)", r"least action", r"action is"]),
    ("电动力学/电磁学", [r"Maxwell", r"electrostatic", r"electromagnetic", r"gauge potential",
        r"Lorentz force", r"magnetic field", r"Born-Infeld", r"Coulomb", r"linking number",
        r"Faraday", r"dipole", r"electric field"]),
    ("量子力学", [r"Schr[oö]dinger", r"wave ?function", r"eigenstate", r"Hilbert space",
        r"harmonic oscillator", r"quantum", r"spin", r"angular momentum",
        r"perturbation theory", r"WKB", r"instanton", r"tunnell?ing", r"degenerac",
        r"heat kernel", r"density matrix", r"bound states", r"scattering", r"energy levels",
        r"path integral"]),
    ("量子场论/QFT", [r"quantum field", r"\bQFT\b", r"Feynman", r"Wick", r"LSZ", r"renormaliz",
        r"propagator", r"spinor.helicity", r"amplitude", r"Dirac", r"Chern-Simon",
        r"U\(1\) gauge", r"O\(N\)", r"gauge invariance", r"vacuum"]),
    ("广义相对论/引力", [r"Einstein", r"general relativity", r"\bmetric\b", r"Killing",
        r"black hole", r"horizon", r"Hawking", r"Riemann", r"geodesic", r"curvature",
        r"de Sitter", r"Schwarzschild", r"vierbein", r"tetrad", r"gravitational"]),
    ("离散数学/组合算法", [r"edge-coloring", r"claw-free", r"hyper.plane", r"rooted tree",
        r"gcd", r"Euclidean algorithm", r"pigeon hole", r"graph G\(", r"partitioned by"]),
]

def tag(chunk):
    tags = []
    for name, pats in TOPICS:
        for p in pats:
            if re.search(p, chunk, re.I):
                tags.append(name)
                break
    return tags

VERBS = ["show", "prove", "find", "compute", "derive", "determine", "construct", "solve",
         "calculate", "explain", "estimate", "discuss", "write", "verify", "analyze", "analyse",
         "state", "give", "define", "sketch", "identify", "count", "recast", "compare", "describe"]

def main():
    recs = load()
    papers, prob_rows = [], []
    for r in recs:
        if r["kind"] == "(root)":
            papers.append(dict(rel=r["rel"], kind="Syllabus", year="n/a", chars=r["chars"],
                               pages=r["pages"], nprob=0, probchars=[], tier="考纲"))
            continue
        segs = segment(r["text"])
        rows = []
        for lab, ch in segs:
            ch = ch.strip()
            if len(ch) < 40:
                continue
            rows.append(dict(paper=r["rel"], kind=r["kind"], year=r["year"], label=lab,
                             chars=len(ch), subparts=len(SUBPART.findall(ch)),
                             syms=len(SYM.findall(ch)), tags=tag(ch),
                             head=re.sub(r"\s+", " ", ch)[:160],
                             full=re.sub(r"\s+", " ", ch)))
        prob_rows.extend(rows)
        papers.append(dict(rel=r["rel"], kind=r["kind"], year=r["year"], chars=r["chars"],
                           pages=r["pages"], nprob=len(rows),
                           probchars=[x["chars"] for x in rows],
                           tier=("无文字层" if r["chars"] < 200 else
                                 ("稀疏(<800)" if r["chars"] < 800 else "正常"))))
    def by(fn, rows):
        d = collections.defaultdict(list)
        for x in rows:
            d[fn(x)].append(x)
        return d
    agg = {}
    agg["by_year"] = {y: dict(n=len(v), chars=sum(x["chars"] for x in v),
                              mean=round(statistics.mean([x["chars"] for x in v]), 1) if v else 0)
                      for y, v in sorted(by(lambda x: x["year"], prob_rows).items())}
    agg["by_kind"] = {k: dict(n=len(v), chars=sum(x["chars"] for x in v),
                              mean=round(statistics.mean([x["chars"] for x in v]), 1) if v else 0,
                              subparts=round(statistics.mean([x["subparts"] for x in v]), 2) if v else 0)
                      for k, v in sorted(by(lambda x: x["kind"], prob_rows).items())}
    agg["by_subj_kind"] = {}
    for (s, k), v in sorted(by(lambda x: (x["paper"].split(os.sep)[0], x["kind"]), prob_rows).items()):
        key = "%s | %s" % (s.split("-")[-1].strip(), k)
        agg["by_subj_kind"][key] = dict(n=len(v), mean=round(statistics.mean([x["chars"] for x in v]), 1),
                                        subparts=round(statistics.mean([x["subparts"] for x in v]), 2))
    ty = collections.defaultdict(collections.Counter)
    for x in prob_rows:
        for t in x["tags"]:
            ty[t][x["year"]] += 1
    agg["topic_by_year"] = {t: dict(sorted(c.items())) for t, c in
                            sorted(ty.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))}
    agg["topic_totals"] = {t: sum(c.values()) for t, c in
                           sorted(ty.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))}
    vt = collections.Counter()
    for x in prob_rows:
        low = x["full"].lower()
        for v in VERBS:
            if re.search(r"\b" + v + r"\b", low):
                vt[v] += 1
    agg["verbs"] = dict(vt.most_common())
    agg["totals"] = dict(files=len(recs),
                         in_scope_papers=len([p for p in papers if p["kind"] != "Syllabus"]),
                         no_text_layer=len([p for p in papers if p.get("tier") == "无文字层"]),
                         sparse=len([p for p in papers if p.get("tier") == "稀疏(<800)"]),
                         problems=len(prob_rows),
                         total_chars=sum(x["chars"] for x in prob_rows))
    json.dump(dict(papers=papers, problems=prob_rows, agg=agg),
              io.open(OUTJ, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    L = []
    A = L.append
    A("# FINALS Applied+MathPhys 统计表（脚本自动生成）\n")
    A("数据源：txt_finals 中 subj 含 Applied|Mathematical_Physics 的 %d 个 txt。" % len(recs))
    A("脚本：.tmp/burn2026/scripts/finals_app_phys_stats.py；明细 JSON：finals_app_phys_stats.json。\n")
    A("## 0. 总览\n")
    A("| 指标 | 值 |")
    A("|---|---|")
    for k, v in agg["totals"].items():
        A("| %s | %s |" % (k, v))
    A("")
    A("## 1. 逐卷（可分析/不可分析）\n")
    A("| 年份 | 卷别 | 文件 | chars | 页 | 切题数 | 文字层 |")
    A("|---|---|---|---|---|---|---|")
    for p in sorted(papers, key=lambda x: (x["kind"], x["year"], x["rel"])):
        A("| %s | %s | %s | %d | %d | %d | %s |" % (
            p["year"], p["kind"], p["rel"].split(os.sep)[-1][:52], p["chars"], p["pages"],
            p["nprob"], p.get("tier", "-")))
    A("")
    A("## 2. 按卷别\n")
    A("| 卷别 | 题次 | 总字符 | 平均字符 | 平均小问 |")
    A("|---|---|---|---|---|")
    for k, v in agg["by_kind"].items():
        A("| %s | %d | %d | %.1f | %.2f |" % (k, v["n"], v["chars"], v["mean"], v["subparts"]))
    A("")
    A("## 3. 科目 x 卷别\n")
    A("| 科目|卷别 | 题次 | 平均字符 | 平均小问 |")
    A("|---|---|---|---|")
    for k, v in agg["by_subj_kind"].items():
        A("| %s | %d | %.1f | %.2f |" % (k, v["n"], v["mean"], v["subparts"]))
    A("")
    A("## 4. 考点 x 年份\n")
    years = sorted({x["year"] for x in prob_rows})
    A("| 考点 | " + " | ".join(years) + " | 合计 |")
    A("|---" * (len(years) + 2) + "|")
    for t, c in agg["topic_totals"].items():
        row = [str(agg["topic_by_year"][t].get(y, "")) if agg["topic_by_year"][t].get(y) else "." for y in years]
        A("| %s | %s | %d |" % (t, " | ".join(row), c))
    A("")
    A("## 5. 任务动词（题面首 160 字符内）\n")
    A("| 动词 | 题次 |")
    A("|---|---|")
    for v, n in agg["verbs"].items():
        A("| %s | %d |" % (v, n))
    A("")
    io.open(OUTM, "w", encoding="utf-8").write("\n".join(L))
    print("papers", len(papers), "problems", len(prob_rows), "chars", agg["totals"]["total_chars"])
    print("WROTE", OUTJ)
    print("WROTE", OUTM)

if __name__ == "__main__":
    main()
