# -*- coding: utf-8 -*-
"""One canonical pipeline: extract -> merge fragments -> enrich -> aggregate reports -> HTML index.
Replaces the ad-hoc scripts (analyze_corpus2 / enrich_problems / build_index / cluster_themes)
with a single consistent dataset so every downstream number agrees.
"""
import os, io, re, json, html, itertools, collections, statistics

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
for d in (DATA, REP): os.makedirs(d, exist_ok=True)
BT = chr(96)

LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl",
       "\u2019":"'","\u2018":"'","\u201c":'"',"\u201d":'"',"\u2013":"-","\u2014":"--","\u00a0":" "}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n").replace("\x00", " "))

KW_RE   = re.compile(r"(?m)^[ \t]*(?:Problem|Question|Exercise)[ \t]*(\d{1,2})\b")
BARE_RE = re.compile(r"(?m)^[ \t]*(\d{1,2})[ \t]*[.):、]?(?=[ \t\n]|$)")
def longest_run(text, rx):
    c = [(m.start(), int(m.group(1)), m.end()) for m in rx.finditer(text)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want: run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best
def cut(text, run, limit=None):
    out = []
    for i, (st, n, en) in enumerate(run):
        stop = run[i+1][0] if i+1 < len(run) else len(text)
        out.append([n, text[en:stop].strip()])
    if limit: out = out[:limit]
    return out
def problems_of(text, limit=None):
    kw, bare = longest_run(text, KW_RE), longest_run(text, BARE_RE)
    if len(kw) >= 2 and len(kw) >= len(bare):
        return cut(text, kw, limit), "keyword"
    return cut(text, bare, limit), "bare"
def merge_fragments(probs, minlen=60):
    """A body shorter than minlen is a stray fragment (fraction/equation break): merge it forward."""
    out, carry = [], ""
    for n, b in probs:
        b = carry + "\n" + b if carry else b
        carry = ""
        if len(b.strip()) < minlen:
            carry = b
            continue
        out.append([n, b.strip()])
    if carry and out:
        out[-1][1] = (out[-1][1] + "\n" + carry).strip()
    elif carry:
        out.append([1, carry.strip()])
    return out

HEAD_RE = re.compile(r"(?m)^[ \t]*(Algebra and Number Theory|Analysis and Di.{1,3}erential Equations|"
                     r"Geometry and Topology|Probability and Statistics|"
                     r"Applied.{0,40}(Math|Statistics|Probability).{0,20}|Computational and Applied Mathematics|"
                     r"Mathematical Physics)[ \t]*(?:Problems?|Team|Section|Part)?[ \t]*$")
SUBJ_PATTERNS = [
    ("Algebra & Number Theory", r"algebra"),
    ("Analysis & PDE",          r"analysis"),
    ("Geometry & Topology",     r"geometry|geomtop|geo_topo|geotop"),
    ("Probability & Statistics", r"probab|proba|statistic"),
    ("Mathematical Physics",    r"physic"),
    ("Computational & Applied", r"applied|comput"),
]
def subj_of(name):
    low = name.lower()
    for label, pat in SUBJ_PATTERNS:
        if re.search(pat, low): return label
    return "Other/Combined"
def clean(b):
    b = re.sub(r"(?m)^[ \t]*=== page \d+ ===[ \t]*$", " ", b)
    b = re.sub(r"\n{3,}", "\n\n", b)
    return b.strip()

# ---------------- 1. extract ----------------
problems, papers = [], []
for fn in sorted(os.listdir(TXT)):
    if not fn.endswith(".txt"): continue
    name = fn[:-4]
    year, low = name[:4], name.lower()
    kind = "solution" if ("soln" in low or "solution" in low) else ("team" if "team" in low else "individual")
    text = norm(io.open(os.path.join(TXT, fn), encoding="utf-8").read())
    m = re.search(r"\((\d+)\s+problems?\)", text, re.I)
    limit = int(m.group(1)) if m else None
    if kind == "solution":
        papers.append({"file": fn, "name": name, "year": year, "kind": kind, "subject": subj_of(name),
                       "pages": text.count("=== page "), "chars": len(text), "declared": limit, "n": 0, "rule": "solution"})
        continue
    multi = kind == "team" and text.count("=== page ") >= 5
    segs = []
    if multi:
        marks = [(mm.start(), mm.group(1)) for mm in HEAD_RE.finditer(text)]
        if len(marks) >= 2:
            for i, (st, lab) in enumerate(marks):
                stop = marks[i+1][0] if i+1 < len(marks) else len(text)
                segs.append((subj_of(lab.lower()), text[st:stop], None))
        else:
            segs = [(subj_of(name), text, limit)]
    else:
        segs = [(subj_of(name), text, limit)]
    total, rules = 0, []
    for sj, seg, lim in segs:
        pr, rule = problems_of(seg, lim)
        pr = merge_fragments(pr)
        rules.append(rule)
        for n, body in pr:
            body = clean(body)
            if len(body) < 40: continue
            problems.append({"year": year, "subject": sj, "paper": name, "kind": kind, "n": n,
                             "chars": len(body), "text": body})
            total += 1
    papers.append({"file": fn, "name": name, "year": year, "kind": kind, "subject": subj_of(name),
                   "pages": text.count("=== page "), "chars": len(text), "declared": limit,
                   "n": total, "rule": "+".join(sorted(set(rules))), "multi": multi})
json.dump(problems, io.open(os.path.join(DATA, "problems_full.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(papers, io.open(os.path.join(DATA, "papers_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------- 2. enrich ----------------
TAGS = [
 ("Galois/域扩张", r"\bgalois\b|splitting field|field extension|finite field|algebraic closure"),
 ("群论", r"\bgroup\b|sylow|normal subgroup|solvable|nilpotent group|conjugat"),
 ("环与模", r"\bideal\b|\bmodule\b|noetherian|\bring\b|localization|polynomial ring|\bpid\b|\bufd\b"),
 ("线性代数/矩阵", r"matrix|matrices|eigenvalue|eigenvector|jordan|determinant|\brank\b|trace|hermitian|quadratic form"),
 ("表示论", r"representation|character table|irreducible|semisimple|tensor product|schur"),
 ("数论", r"\bprime\b|congruen|diophantine|p-adic|valuation|reciprocity|elliptic curve|quadratic residue"),
 ("范畴/同调代数", r"\bcategory\b|functor|exact sequence|homolog|projective module|injective|derived"),
 ("复分析", r"holomorphic|analytic function|meromorphic|residue|entire function|conformal|riemann mapping"),
 ("实分析/测度", r"lebesgue|measurable|radon-nikodym|absolutely continuous|bounded variation|almost everywhere"),
 ("泛函分析", r"banach|hilbert space|compact operator|spectral theorem|hahn-banach|weakly conver|reflexive|\briesz\b"),
 ("调和/位势", r"harmonic|subharmonic|maximum principle|poisson (kernel|integral)|dirichlet problem"),
 ("偏微分方程", r"\bpde\b|heat equation|wave equation|laplace equation|elliptic|parabolic|hyperbolic|sobolev|weak solution|harnack|schauder"),
 ("Fourier/变换", r"fourier|laplace transform|spectral method"),
 ("常微分方程", r"ordinary differential|\bode\b|initial value problem|sturm-liouville|wronskian|lyapunov"),
 ("微分几何", r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|gauss-bonnet|holonomy"),
 ("代数拓扑", r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
 ("微分流形/形式", r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
 ("纤维丛/示性类", r"fiber bundle|vector bundle|principal bundle|chern class|pontryagin|characteristic class"),
 ("代数几何", r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
 ("辛几何/力学", r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville|hamilton-jacobi"),
 ("概率论", r"random variable|probability space|martingale|brownian|random walk|markov chain|poisson process|central limit|law of large numbers|characteristic function|i\.i\.d"),
 ("数理统计", r"estimator|unbiased|maximum likelihood|sufficient statistic|cramer-rao|confidence interval|hypothesis test|likelihood ratio|regression|posterior"),
 ("数值分析", r"finite difference|finite element|numerical scheme|discretiz|convergence rate|condition number|truncation error|interpolation|quadrature|runge-kutta"),
 ("优化/线性规划", r"linear programming|simplex|optimization|convex (set|function)|kkt|gradient descent|subgradient"),
 ("科学计算/大规模", r"monte carlo|fast fourier|sparse|iterative (method|solver)|precondition|conjugate gradient|multigrid|\bsvd\b|singular value"),
 ("数学物理/量子", r"schrodinger|wave function|quantum|commutator|uncertainty principle|angular momentum"),
 ("经典场论/相对论", r"maxwell|electromagnetic|gauge|yang-mills|relativity|lorentz|minkowski|metric"),
 ("统计物理", r"statistical mechanics|partition function|entropy|boltzmann|gibbs|ising|phase transition"),
 ("流体/连续介质", r"navier-stokes|fluid|incompressible|elasticity|strain|stress"),
]
TAG_RX = [(n, re.compile(p, re.I)) for n, p in TAGS]
VERBS = ["prove","show that","show","compute","calculate","find","determine","construct","give an example",
         "explain","evaluate","verify","establish","derive","estimate","solve","describe","characterize"]
SUB_RE = re.compile(r"(?m)^[ \t]*\(?([a-e])\)[ \t]|\((\d)\)[ \t]")
SYM_RE = re.compile(r"[∑∫∂∇√≤≥∈⊂⊆×⊗⊕→↦⇒∀∃]")
for p in problems:
    body = p["text"]; low = body.lower()
    words = re.findall(r"[A-Za-z']+", body)
    p["words"] = len(words)
    p["tags"] = [n for n, rx in TAG_RX if rx.search(body)]
    p["subparts"] = len(SUB_RE.findall(body))
    p["symbols"] = len(SYM_RE.findall(body))
    p["verbs"] = {v: len(re.findall(r"\b" + re.escape(v) + r"\b", low)) for v in VERBS}
    p["difficulty_proxy"] = round(1.0 + min(2.0, len(words) / 160.0) + min(1.5, p["subparts"] * 0.5)
                                  + min(1.0, p["symbols"] / 40.0) + min(1.0, max(0, len(p["tags"]) - 1) * 0.25), 2)
json.dump(problems, io.open(os.path.join(DATA, "problems_enriched.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------- 3. reports ----------------
years = sorted(set(p["year"] for p in problems))
subjects = sorted(set(p["subject"] for p in problems))
by_year = collections.defaultdict(list); by_subj = collections.defaultdict(list)
for p in problems:
    by_year[p["year"]].append(p); by_subj[p["subject"]].append(p)
matrix = collections.defaultdict(collections.Counter)
tag_year = collections.defaultdict(collections.Counter)
for p in problems:
    matrix[p["subject"]][p["year"]] += 1
    for t in p["tags"]: tag_year[t][p["year"]] += 1

L = ["# Yau 初赛(笔试) 语料库统计 v3（单一流水线 rebuild_pipeline.py 生成）\n",
     "数据源：" + BT + ".tmp/yau/2010-2026历年笔试真题" + BT + "（136 个 PDF）→ PyMuPDF 抽取 → 统一解析。",
     "题量口径：**%d 道题**（已合并因公式换行产生的碎片小问；多科目团体卷先按科目标题分段再切题）。\n" % len(problems),
     "## 1. 逐年总览\n", "| 年份 | 卷数(非解答) | 解答卷 | 题数 | 抽取字符 |", "|---|---|---|---|---|"]
for y in years:
    ps = by_year[y]
    papers_y = [q for q in papers if q["year"] == y]
    L.append("| %s | %d | %d | %d | %d |" % (y, sum(1 for q in papers_y if q["kind"] != "solution"),
             sum(1 for q in papers_y if q["kind"] == "solution"), len(ps), sum(q["chars"] for q in papers_y)))
L += ["| **合计** | **%d** | **%d** | **%d** | **%d** |" % (
        sum(1 for q in papers if q["kind"] != "solution"), sum(1 for q in papers if q["kind"] == "solution"),
        len(problems), sum(q["chars"] for q in papers)), "",
      "## 2. 科目 x 年份 题量矩阵\n", "| 科目 | " + " | ".join(years) + " | 合计 |", "|" + "---|" * (len(years) + 2)]
for s in subjects:
    row = [matrix[s][y] for y in years]
    L.append("| %s | %s | %d |" % (s, " | ".join(str(v) if v else "." for v in row), sum(row)))
L.append("")
L += ["## 3. 题目级指标（按年份）\n", "| 年份 | 题数 | 平均词数 | 中位词数 | 平均小问 | 平均难度代理 |",
      "|---|---|---|---|---|---|"]
for y in years:
    ps = by_year[y]
    L.append("| %s | %d | %.0f | %.0f | %.2f | %.2f |" % (y, len(ps),
             statistics.mean([p["words"] for p in ps]), statistics.median([p["words"] for p in ps]),
             statistics.mean([p["subparts"] for p in ps]), statistics.mean([p["difficulty_proxy"] for p in ps])))
L += ["", "## 4. 题目级指标（按科目）\n", "| 科目 | 题数 | 平均词数 | 平均小问 | 平均难度代理 |",
      "|---|---|---|---|---|"]
for s in subjects:
    ps = by_subj[s]
    L.append("| %s | %d | %.0f | %.2f | %.2f |" % (s, len(ps), statistics.mean([p["words"] for p in ps]),
             statistics.mean([p["subparts"] for p in ps]), statistics.mean([p["difficulty_proxy"] for p in ps])))
L += ["", "## 5. 考点标签 x 年份（>=5 题次）\n", "| 考点 | " + " | ".join(years) + " | 合计 |",
      "|" + "---|" * (len(years) + 2)]
for t, c in sorted(tag_year.items(), key=lambda kv: -sum(kv[1].values())):
    if sum(c.values()) < 5: continue
    L.append("| %s | %s | %d |" % (t, " | ".join(str(c[y]) if c[y] else "." for y in years), sum(c.values())))
vc, vq = collections.Counter(), collections.Counter()
for p in problems:
    for k, v in p["verbs"].items():
        vq[k] += v; vc[k] += 1
L += ["", "## 6. 任务动词分布\n", "| 动词 | 涉及题数 | 出现次数 |", "|---|---|---|"]
for k, v in vq.most_common(): L.append("| %s | %d | %d |" % (k, vc[k], v))
L.append("")
io.open(os.path.join(REP, "stats_overview.md"), "w", encoding="utf-8").write("\n".join(L))

# ---------------- 4. index + html ----------------
idx = ["# Yau 初赛(笔试) 2010-2026 全题目索引\n", "共 %d 道题。" % len(problems)]
for p in sorted(problems, key=lambda x: (x["year"], x["subject"], x["n"])):
    idx.append("- **[%s | %s | %s | Q%d]** (%d chars) %s" % (p["year"], p["subject"], p["kind"], p["n"], p["chars"],
               " ".join(p["text"].split())[:240]))
io.open(os.path.join(REP, "all_problems_index.md"), "w", encoding="utf-8").write("\n".join(idx))
payload = json.dumps([{"year": p["year"], "subject": p["subject"], "paper": p["paper"], "kind": p["kind"],
                       "n": p["n"], "chars": p["chars"], "tags": p["tags"], "d": p["difficulty_proxy"],
                       "text": p["text"][:4000]} for p in problems], ensure_ascii=False)
HT = io.open(os.path.join(ROOT, "yau_index_template.html"), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, "yau_index_template.html")) else None
if HT is None:
    HT = """<!doctype html><html lang="zh"><head><meta charset="utf-8"><title>Yau 题库索引 2010-2026</title>
<style>body{font-family:system-ui,"Microsoft YaHei",sans-serif;margin:0;background:#f6f7f9;color:#1c1e21}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid #dcdfe4;padding:12px 16px}
h1{font-size:18px;margin:0 0 8px}select,input{font-size:13px;padding:5px 8px;border:1px solid #c8ccd4;border-radius:6px;margin-right:8px}
#count{color:#5b6472;font-size:13px}main{padding:12px 16px;display:grid;gap:10px}
.card{background:#fff;border:1px solid #dfe3e8;border-radius:8px;padding:10px 12px}
.meta{font-size:12px;color:#5b6472;margin-bottom:6px}.badge{display:inline-block;background:#eef2ff;color:#33418f;border-radius:4px;padding:1px 6px;margin-right:6px}
pre{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Consolas,monospace;font-size:12.5px;margin:0}</style></head><body>
<header><h1>丘成桐大学生数学竞赛 初赛题库索引 2010-2026（共 <span id="total"></span> 题）</h1>
<select id="year"><option value="">全部年份</option></select>
<select id="subject"><option value="">全部科目</option></select>
<select id="kind"><option value="">全部卷别</option></select>
<select id="tag"><option value="">全部考点</option></select>
<input id="q" placeholder="关键词搜索：Galois / Sobolev / martingale" size="32"><span id="count"></span></header>
<main id="list"></main><script>
const DATA=__DATA__;const $=s=>document.querySelector(s);
const uniq=k=>[...new Set(DATA.map(d=>d[k]))].sort();
for(const k of ['year','subject','kind']){const el=$('#'+k);for(const v of uniq(k)){const o=document.createElement('option');o.value=v;o.textContent=v;el.appendChild(o);}}
const tags=[...new Set(DATA.flatMap(d=>d.tags))].sort();for(const t of tags){const o=document.createElement('option');o.value=t;o.textContent=t;$('#tag').appendChild(o);}
$('#total').textContent=DATA.length;
function render(){const y=$('#year').value,s=$('#subject').value,k=$('#kind').value,t=$('#tag').value,q=$('#q').value.trim().toLowerCase();
const rows=DATA.filter(d=>(!y||d.year===y)&&(!s||d.subject===s)&&(!k||d.kind===k)&&(!t||d.tags.includes(t))&&(!q||d.text.toLowerCase().includes(q)));
$('#count').textContent='命中 '+rows.length+' 题';
$('#list').innerHTML=rows.slice(0,300).map(d=>'<div class="card"><div class="meta"><span class="badge">'+d.year+'</span><span class="badge">'+d.subject+'</span>'+d.kind+' · Q'+d.n+' · '+d.chars+' chars · 难度代理 '+d.d+'<br>'+d.tags.join(' / ')+'</div><pre>'+d.text.replace(/[<>&]/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;'}[c]))+'</pre></div>').join('');}
for(const id of ['#year','#subject','#kind','#tag']) $(id).addEventListener('change',render);
$('#q').addEventListener('input',render);render();</script></body></html>"""
io.open(os.path.join(ROOT, "yau_index.html"), "w", encoding="utf-8").write(HT.replace("__DATA__", payload))

print("PIPELINE_OK problems=%d papers=%d years=%d subjects=%d" % (len(problems), len(papers), len(years), len(subjects)))
print("HTML bytes", os.path.getsize(os.path.join(ROOT, "yau_index.html")))
for y in years: print(" year", y, "n", len(by_year[y]))
