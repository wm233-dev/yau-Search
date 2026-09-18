# -*- coding: utf-8 -*-
"""Enrich every parsed problem: length, sub-parts, task verbs, LaTeX-ish symbol load,
rule-based topic tagging, and a difficulty proxy. Writes data/problems_enriched.json
and reports/problem_metrics.md."""
import os, io, re, json, collections, statistics

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl"}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n"))
PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):：、]?(?=[ \t\n]|$)")
def best_run(t):
    c = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(t)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want: run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best
def cutp(t):
    r = best_run(t); out = []
    for i, (st, n, en) in enumerate(r):
        stop = r[i+1][0] if i+1 < len(r) else len(t)
        out.append((n, t[en:stop].strip()))
    return out

TAGS = [
 ("Galois/域扩张",      r"\bgalois\b|splitting field|field extension|finite field|algebraic closure"),
 ("群论",              r"\bgroup\b|sylow|normal subgroup|solvable|nilpotent group|conjugat"),
 ("环与模",            r"\bideal\b|\bmodule\b|noetherian|\bring\b|localization|polynomial ring|\bpid\b|\bufd\b"),
 ("线性代数/矩阵",      r"matrix|matrices|eigenvalue|eigenvector|jordan|determinant|\brank\b|trace|hermitian|quadratic form"),
 ("表示论",            r"representation|character|irreducible|semisimple|tensor product|schur"),
 ("数论",              r"\bprime\b|congruen|diophantine|p-adic|valuation|reciprocity|elliptic curve|quadratic residue|farey|mobius"),
 ("范畴/同调代数",      r"\bcategory\b|functor|exact sequence|homolog|projective module|injective|derived"),
 ("复分析",            r"holomorphic|analytic function|meromorphic|residue|entire function|conformal|riemann mapping|cauchy('s)? (integral|theorem)"),
 ("实分析/测度",        r"lebesgue|measurable|radon-nikodym|absolutely continuous|bounded variation|almost everywhere|integration"),
 ("泛函分析",          r"banach|hilbert space|compact operator|spectral theorem|hahn-banach|weak(ly)? conver|reflexive|riesz"),
 ("调和/位势",          r"harmonic|subharmonic|maximum principle|poisson (kernel|integral)|dirichlet problem|green('s)? function"),
 ("偏微分方程",         r"\bpde\b|heat equation|wave equation|laplace equation|elliptic|parabolic|hyperbolic|sobolev|weak solution|a priori|harnack|schauder|energy estimate"),
 ("Fourier/变换",       r"fourier|laplace transform|z-transform|spectral method"),
 ("微分方程(常微)",      r"ordinary differential|\bode\b|initial value problem|sturm-liouville|wronskian|lyapunov"),
 ("微分几何",           r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|mean curvature|gauss-bonnet|holonomy"),
 ("代数拓扑",           r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
 ("微分流形/形式",       r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
 ("纤维丛/示性类",       r"fiber bundle|vector bundle|principal bundle|chern class|pontryagin|characteristic class|section of"),
 ("代数几何",           r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
 ("辛几何/力学",         r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville|hamilton-jacobi"),
 ("概率论",            r"random variable|probability space|expectation|variance|independence|conditional (probability|expectation)|martingale|brownian|random walk|markov chain|poisson process|central limit|law of large numbers|characteristic function"),
 ("数理统计",           r"estimator|unbiased|maximum likelihood|sufficient statistic|cramer-rao|confidence interval|hypothesis test|likelihood ratio|regression|bayes|posterior|prior distribution|risk function"),
 ("数值分析",           r"finite difference|finite element|numerical scheme|discretiz|convergence rate|condition number|truncation error|interpolation|quadrature|newton('s)? method|runge-kutta|stability of the scheme"),
 ("优化/线性规划",       r"linear programming|simplex|optimization|convex (set|function|optimization)|kkt|gradient descent|duality theorem"),
 ("科学计算/大规模",      r"monte carlo|fast fourier|sparse|iterative (method|solver)|precondition|conjugate gradient|multigrid|svd|singular value"),
 ("数学物理/量子",       r"schrodinger|wave function|quantum|commutator|uncertainty principle|angular momentum|hydrogen atom"),
 ("经典场论/相对论",      r"maxwell|electromagnetic|gauge|yang-mills|relativity|lorentz|minkowski|field equation"),
 ("统计物理",           r"statistical mechanics|partition function|entropy|boltzmann|gibbs|ising|phase transition|thermodynamic"),
 ("流体/连续介质",       r"navier-stokes|euler equation|fluid|incompressible|elasticity|strain|stress tensor"),
]
TAG_RX = [(name, re.compile(pat, re.I)) for name, pat in TAGS]
VERBS = ["prove","show that","show","compute","calculate","find","determine","construct","give an example",
         "explain","evaluate","verify","establish","derive","estimate","solve","describe","characterize"]
SUB_RE = re.compile(r"(?m)^[ \t]*\(?([a-d])\)[ \t]|\((\d)\)[ \t]")
SYM_RE = re.compile(r"[∑∫∂∇√≤≥∈⊂⊆×⊗⊕→↦⇒∀∃|]")

papers = json.load(io.open(os.path.join(DATA, "papers.json"), encoding="utf-8"))["papers"]
enriched = []
for rec in papers:
    if rec["kind"] == "solution": continue
    txt = norm(io.open(os.path.join(TXT, rec["file"]), encoding="utf-8").read())
    multi = rec.get("multi_subject")
    if multi:
        # reuse simple per-file split (subject segmentation handled in v2 report)
        items = cutp(txt)
        items = [(rec["subject"], n, b) for n, b in items]
    else:
        items = [(rec["subject"], n, b) for n, b in cutp(txt)]
    for subj, n, body in items:
        low = body.lower()
        words = re.findall(r"[A-Za-z']+", body)
        tags = [name for name, rx in TAG_RX if rx.search(body)]
        verbs = {v: len(re.findall(r"\b" + re.escape(v) + r"\b", low)) for v in VERBS}
        subparts = len(SUB_RE.findall(body))
        syms = len(SYM_RE.findall(body))
        # difficulty proxy: length + subparts + symbol density + #tags
        diff = 1.0 + min(2.0, len(words) / 160.0) + min(1.5, subparts * 0.5) + min(1.0, syms / 40.0) + min(1.0, max(0, len(tags) - 1) * 0.25)
        enriched.append({
            "year": rec["year"], "file": rec["file"], "subject": subj, "n": n,
            "chars": len(body), "words": len(words), "subparts": subparts, "symbols": syms,
            "tags": tags, "verbs": {k: v for k, v in verbs.items() if v},
            "difficulty_proxy": round(diff, 2),
            "head": " ".join(body.split())[:300],
        })
json.dump(enriched, io.open(os.path.join(DATA, "problems_enriched.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- aggregate ----
by_subj = collections.defaultdict(list)
for e in enriched: by_subj[e["subject"]].append(e)
by_year = collections.defaultdict(list)
for e in enriched: by_year[e["year"]].append(e)
tag_year = collections.defaultdict(collections.Counter)
for e in enriched:
    for t in e["tags"]: tag_year[t][e["year"]] += 1
years = sorted(by_year)

L = ["# 题目级量化指标（自动生成）\n",
     "共 %d 道题（已剔除官方解答卷）。指标含义：chars/words 为抽取文本长度；subparts 为 (a)(b)(1)(2) 型小问个数；" % len(enriched),
     "symbols 为数学符号出现数；difficulty_proxy 为长度+小问数+符号密度+考点跨度的启发式难度（1–6，非官方难度）。\n",
     "## 1. 按年份\n", "| 年份 | 题数 | 平均词数 | 中位词数 | 平均小问 | 平均符号 | 平均难度代理 |",
     "|---|---|---|---|---|---|---|"]
for y in years:
    ws = [e["words"] for e in by_year[y]]
    L.append("| %s | %d | %.0f | %.0f | %.2f | %.1f | %.2f |" % (
        y, len(ws), statistics.mean(ws), statistics.median(ws),
        statistics.mean([e["subparts"] for e in by_year[y]]),
        statistics.mean([e["symbols"] for e in by_year[y]]),
        statistics.mean([e["difficulty_proxy"] for e in by_year[y]])))
L += ["", "## 2. 按科目\n", "| 科目 | 题数 | 平均词数 | 平均小问 | 平均难度代理 | 最难 5 题（年份/Q号/难度） |", "|---|---|---|---|---|---|"]
for s in sorted(by_subj):
    es = by_subj[s]
    top = sorted(es, key=lambda e: -e["difficulty_proxy"])[:5]
    L.append("| %s | %d | %.0f | %.2f | %.2f | %s |" % (
        s, len(es), statistics.mean([e["words"] for e in es]),
        statistics.mean([e["subparts"] for e in es]),
        statistics.mean([e["difficulty_proxy"] for e in es]),
        "; ".join("%s/Q%d(%.1f)" % (e["year"], e["n"], e["difficulty_proxy"]) for e in top)))
L += ["", "## 3. 考点标签 × 年份（跨全部科目）\n",
      "| 考点 | " + " | ".join(years) + " | 合计 |", "|" + "---|" * (len(years) + 2)]
for t, c in sorted(tag_year.items(), key=lambda kv: -sum(kv[1].values())):
    if sum(c.values()) < 4: continue
    L.append("| %s | %s | %d |" % (t, " | ".join(str(c[y]) if c[y] else "." for y in years), sum(c.values())))
L += ["", "## 4. 任务动词分布（全部题目）\n", "| 动词 | 出现题数 | 出现次数 |", "|---|---|---|"]
vc = collections.Counter(); vq = collections.Counter()
for e in enriched:
    for k, v in e["verbs"].items():
        vq[k] += v; vc[k] += 1
for k, v in vq.most_common():
    L.append("| %s | %d | %d |" % (k, vc[k], v))
L.append("")
io.open(os.path.join(REP, "problem_metrics.md"), "w", encoding="utf-8").write("\n".join(L))
print("enriched", len(enriched), "tags", len(tag_year), "->", os.path.join(REP, "problem_metrics.md"))
print("top tags:", ", ".join("%s=%d" % (t, sum(c.values())) for t, c in sorted(tag_year.items(), key=lambda kv: -sum(kv[1].values()))[:15]))
