# -*- coding: utf-8 -*-
"""Finals (Geometry+Probability) corpus statistics.

Outputs:
  data/finals_geo_prob_stats.json   -- all numbers used in the report
  prints a markdown fragment to stdout
Reuses the SAME metric definitions as the preliminary-round report
(scripts/enrich_problems.py) so figures are comparable.
"""
import json, io, os, re, collections, statistics, itertools

BASE = r'.'
TXT, TXTR, TXTP = (os.path.join(BASE, d) for d in ('txt_finals', 'txt_finals_recovered', 'txt'))
DATA = os.path.join(BASE, 'data')

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}


def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r'[ \t]+', ' ', s.replace('\r\n', '\n'))


SUB_RE = re.compile(r'(?m)^[ \t]*\(?([a-d])\)[ \t]|\((\d)\)[ \t]')
SYM_RE = re.compile(r'[\u2211\u222b\u2202\u2207\u221a\u2264\u2265\u2208\u2282\u2286\u00d7\u2297\u2295\u2192\u21a6\u21d2\u2200\u2203|]')

TAGS = [
    ("Galois/域扩张", r"\bgalois\b|splitting field|field extension|finite field|algebraic closure"),
    ("群论", r"\bgroup\b|sylow|normal subgroup|solvable|nilpotent group|conjugat"),
    ("环与模", r"\bideal\b|\bmodule\b|noetherian|\bring\b|localization|polynomial ring|\bpid\b|\bufd\b"),
    ("线性代数/矩阵", r"matrix|matrices|eigenvalue|eigenvector|jordan|determinant|\brank\b|trace|hermitian|quadratic form"),
    ("表示论", r"representation|character|irreducible|semisimple|tensor product|schur"),
    ("数论", r"\bprime\b|congruen|diophantine|p-adic|valuation|reciprocity|elliptic curve|quadratic residue|farey|mobius"),
    ("范畴/同调代数", r"\bcategory\b|functor|exact sequence|homolog|projective module|injective|derived"),
    ("复分析", r"holomorphic|analytic function|meromorphic|residue|entire function|conformal|riemann mapping"),
    ("实分析/测度", r"lebesgue|measurable|radon-nikodym|absolutely continuous|bounded variation|almost everywhere|integration"),
    ("泛函分析", r"banach|hilbert space|compact operator|spectral theorem|hahn-banach|weak(ly)? conver|reflexive|riesz"),
    ("调和/位势", r"harmonic|subharmonic|maximum principle|poisson (kernel|integral)|dirichlet problem|green('s)? function"),
    ("偏微分方程", r"\bpde\b|heat equation|wave equation|laplace equation|elliptic|parabolic|hyperbolic|sobolev|weak solution|harnack|energy estimate"),
    ("Fourier/变换", r"fourier|laplace transform|z-transform|spectral method"),
    ("微分方程(常微)", r"ordinary differential|\bode\b|initial value problem|sturm-liouville|wronskian|lyapunov"),
    ("微分几何", r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|mean curvature|gauss-bonnet|holonomy"),
    ("代数拓扑", r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
    ("微分流形/形式", r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
    ("纤维丛/示性类", r"fiber bundle|vector bundle|principal bundle|chern class|pontryagin|characteristic class|section of"),
    ("代数几何", r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
    ("辛几何/力学", r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville|hamilton-jacobi"),
    ("概率论", r"random variable|probability space|expectation|variance|independence|conditional (probability|expectation)|martingale|brownian|random walk|markov chain|poisson process|central limit|law of large numbers|characteristic function"),
    ("数理统计", r"estimator|unbiased|maximum likelihood|sufficient statistic|cramer-rao|confidence interval|hypothesis test|likelihood ratio|regression|bayes|posterior|prior distribution|risk function"),
    ("数值分析", r"finite difference|finite element|numerical scheme|discretiz|convergence rate|condition number|truncation error|interpolation|quadrature|newton('s)? method|runge-kutta"),
    ("优化/线性规划", r"linear programming|simplex|optimization|convex (set|function|optimization)|kkt|gradient descent|duality theorem"),
    ("科学计算/大规模", r"monte carlo|fast fourier|sparse|iterative (method|solver)|precondition|conjugate gradient|multigrid|svd|singular value"),
    ("数学物理/量子", r"schrodinger|wave function|quantum|commutator|uncertainty principle|angular momentum|hydrogen atom"),
    ("经典场论/相对论", r"maxwell|electromagnetic|gauge|yang-mills|relativity|lorentz|minkowski|field equation"),
    ("统计物理", r"statistical mechanics|partition function|entropy|boltzmann|gibbs|ising|phase transition|thermodynamic"),
    ("流体/连续介质", r"navier-stokes|euler equation|fluid|incompressible|elasticity|strain|stress tensor"),
]
TAG_RX = [(n, re.compile(p, re.I)) for n, p in TAGS]

VERBS = ["prove", "show that", "show", "compute", "calculate", "find", "determine", "construct",
         "give an example", "explain", "evaluate", "verify", "establish", "derive", "estimate",
         "solve", "describe", "characterize"]
PROOF_V = ["prove", "show", "establish", "verify", "state"]
CALC_V = ["compute", "calculate", "find", "determine", "evaluate", "derive", "estimate"]

# ---------------------------------------------------------------- corpus
map74 = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))
overturned = {'2013 Probability (Overall).pdf'}          # 0-char text layer
mojibake = {'2013 Probability (Individual).pdf', '2014 Probability (Individual).pdf',
            '2013 Probability (Team).pdf', '2014 Probability (Team).pdf'}

papers = []
for x in map74:
    if x['kind'] == '(root)':
        continue
    t = io.open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
    t = t.strip()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t) < 50:
        qual = 'EMPTY'
    elif ctrl / max(1, len(t)) > 0.08:
        qual = 'MOJIBAKE'
    else:
        qual = 'OK'
    papers.append({'year': x['year'], 'kind': x['kind'], 'file': x['file'],
                   'subj': x['subj'], 'chars_idx': x['chars'], 'chars_real': len(t), 'quality': qual})

RECOVERED = [   # file, year, kind, source-note
    ('2013_prob_individual.txt', '2013', 'Individual', 'vision(200dpi render)', 'Probability and Statistics'),
    ('2014_prob_individual.txt', '2014', 'Individual', 'vision(200dpi render)', 'Probability and Statistics'),
    ('2013_prob_team.txt', '2013', 'Team', 'vision(200dpi render)', 'Probability and Statistics'),
    ('2014_prob_team.txt', '2014', 'Team', 'vision(200dpi render)', 'Probability and Statistics'),
    ('2013_prob_overall.txt', '2013', 'Overall', 'vision(handwritten scan)', 'Probability and Statistics'),
    ('2014_prob_overall.txt', '2014', 'Overall', 'vision(JPG photo)', 'Probability and Statistics'),
    ('2013_geo_overall.txt', '2013', 'Overall', 'docx(OMML)', 'Geometry and Topology'),
    ('2014_geo_individual_overall.txt', '2014', 'Individual+Team', 'legacy .doc ASCII scan', 'Geometry and Topology'),
    ('2014_geo_team_docx.txt', '2014', 'Team', 'docx(OMML)', 'Geometry and Topology'),
]

def paper_metrics(text):
    t = norm(text)
    words = re.findall(r"[A-Za-z']+", t)
    cjk = sum(1 for c in t if '\u4e00' <= c <= '\u9fff')
    subparts = len(SUB_RE.findall(t))
    syms = len(SYM_RE.findall(t))
    tags = [n for n, rx in TAG_RX if rx.search(t)]
    low = t.lower()
    verbs = {v: len(re.findall(r'\b' + re.escape(v) + r'\b', low)) for v in VERBS}
    diff = 1.0 + min(2.0, len(words) / 160.0) + min(1.5, subparts * 0.5) + min(1.0, syms / 40.0) \
        + min(1.0, max(0, len(tags) - 1) * 0.25)
    return {'chars': len(t), 'words': len(words), 'cjk': cjk, 'subparts': subparts, 'symbols': syms,
            'tags': tags, 'verbs': {k: v for k, v in verbs.items() if v}, 'diff_proxy': round(diff, 2)}

metrics, texts = {}, {}
for p in papers:
    if p['quality'] != 'OK':
        continue
    t = io.open(os.path.join(TXT, [x['txt'] for x in map74 if x['file'] == p['file']][0]),
                encoding='utf-8', errors='replace').read()
    metrics[p['file']] = paper_metrics(t)
    texts[p['file']] = norm(t)
for fn, year, kind, src, subj in RECOVERED:
    t = io.open(os.path.join(TXTR, fn), encoding='utf-8', errors='replace').read()
    metrics[fn] = paper_metrics(t)
    metrics[fn]['recovered_from'] = src
    texts[fn] = norm(t)

# ---------------------------------------------------------------- curated inventory
geo = json.load(io.open(os.path.join(DATA, 'finals_geo_problems.json'), encoding='utf-8'))
prob = json.load(io.open(os.path.join(DATA, 'finals_prob_problems.json'), encoding='utf-8'))
for r in geo:
    r['subject'] = 'Geometry & Topology'
for r in prob:
    r['subject'] = 'Probability & Statistics'
allp = geo + prob

# ---------------------------------------------------------------- aggregates
out = {}
out['n_index_records_geoprob'] = len(map74)
out['n_papers_geoprob'] = len([x for x in map74 if x['kind'] != '(root)'])
out['quality'] = collections.Counter(p['quality'] for p in papers)
out['quality_by_subject'] = {s: collections.Counter(p['quality'] for p in papers if s in p['subj'])
                             for s in ('Geometry and Topology', 'Probability and Statistics')}
out['syllabus'] = [x['file'] for x in map74 if x['kind'] == '(root)']
out['problems_total'] = len(allp)
out['problems_geo'] = len(geo)
out['problems_prob'] = len(prob)
out['problems_by_year_kind'] = {}
for r in allp:
    out['problems_by_year_kind'].setdefault(r['year'], collections.Counter())[r['kind']] += 1
out['problems_by_kind_subject'] = {}
for r in allp:
    out['problems_by_kind_subject'].setdefault(r['kind'], collections.Counter())[r['subject']] += 1

# topic frequency
tf = collections.defaultdict(collections.Counter)
tf_subj = collections.defaultdict(collections.Counter)
for r in allp:
    tf[r['topic']][r['year']] += 1
    tf_subj[r['topic']][r['subject']] += 1
out['topic_freq'] = {k: dict(v) for k, v in sorted(tf.items(), key=lambda kv: -sum(kv[1].values()))}
out['topic_freq_subject'] = {k: dict(v) for k, v in tf_subj.items()}

# self-rated difficulty
def dstat(rows):
    return {'n': len(rows), 'mean_diff': round(statistics.mean([r['diff'] for r in rows]), 2),
            'median_diff': statistics.median([r['diff'] for r in rows])}
out['kind_stats'] = {k: dstat([r for r in allp if r['kind'] == k]) for k in ('Individual', 'Team', 'Overall')}
out['subject_stats'] = {s: dstat([r for r in allp if r['subject'] == s])
                        for s in ('Geometry & Topology', 'Probability & Statistics')}
out['year_stats'] = {y: dstat([r for r in allp if r['year'] == y]) for y in sorted({r['year'] for r in allp})}
out['subj_kind_stats'] = {}
for s in ('Geometry & Topology', 'Probability & Statistics'):
    for k in ('Individual', 'Team', 'Overall'):
        rows = [r for r in allp if r['subject'] == s and r['kind'] == k]
        if rows:
            out['subj_kind_stats'][s + '|' + k] = dstat(rows)

# words / symbols per problem for readable papers
wp = {}
per_problem = {}
for p in papers:
    if p['quality'] != 'OK':
        continue
    key = (p['year'], p['kind'])
    per_problem.setdefault(key, []).append(p['file'])
for fn, year, kind, src, subj in RECOVERED:
    per_problem.setdefault((year, kind), []).append(fn)
curated_count = collections.Counter((r['year'], r['kind']) for r in allp)
rows = []
for k, files in sorted(per_problem.items()):
    tp = sum(metrics[f]['words'] for f in files if f in metrics)
    ch = sum(metrics[f]['chars'] for f in files if f in metrics)
    sp = sum(metrics[f]['subparts'] for f in files if f in metrics)
    sy = sum(metrics[f]['symbols'] for f in files if f in metrics)
    ncur = curated_count.get(k, 0)
    rows.append({'year': k[0], 'kind': k[1], 'files': len(files), 'words': tp, 'chars': ch,
                 'subparts': sp, 'symbols': sy, 'problems': ncur,
                 'words_per_problem': round(tp / ncur, 1) if ncur else None})
out['per_paper_words_per_problem'] = rows

# verb distribution (paper level, readable files)
vq, vc = collections.Counter(), collections.Counter()
for fn, m in metrics.items():
    for v, c in m['verbs'].items():
        vq[v] += c
        vc[v] += 1
out['verbs'] = {'papers_with': dict(vc), 'occurrences': dict(vq)}

# proof vs compute share at paper level
pc = {}
for fn, m in metrics.items():
    v = m['verbs']
    pr = sum(v.get(x, 0) for x in PROOF_V)
    ca = sum(v.get(x, 0) for x in CALC_V)
    pc[fn] = (pr, ca)
tot_pr = sum(a for a, b in pc.values())
tot_ca = sum(b for a, b in pc.values())
out['proof_vs_calc'] = {'proof_verbs': tot_pr, 'calc_verbs': tot_ca,
                        'ratio_proof_over_calc': round(tot_pr / max(1, tot_ca), 2)}
kind_pc = collections.Counter()
for p in papers:
    if p['file'] in pc:
        a, b = pc[p['file']]
        kind_pc[(p['kind'], 'proof')] += a
        kind_pc[(p['kind'], 'calc')] += b
for fn, year, kind, src, subj in RECOVERED:
    a, b = pc[fn]
    kind_pc[(kind, 'proof')] += a
    kind_pc[(kind, 'calc')] += b
out['proof_vs_calc_by_kind'] = {k: {'proof': kind_pc[(k, 'proof')], 'calc': kind_pc[(k, 'calc')],
                                    'ratio': round(kind_pc[(k, 'proof')] / max(1, kind_pc[(k, 'calc')]), 2)}
                                for k in ('Individual', 'Team', 'Overall')}

# keyword tags over readable papers
tagc = collections.Counter()
for fn, m in metrics.items():
    for t in m['tags']:
        tagc[t] += 1
out['paper_tag_hits'] = dict(tagc.most_common())

# ---------------------------------------------------------------- duplicates
def shingles(t, n=6):
    w = re.findall(r"[A-Za-z']+", t.lower())
    return {tuple(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}

sh = {fn: shingles(t) for fn, t in texts.items() if len(texts[fn]) > 200}
dups = []
keys = sorted(sh)
for a, b in itertools.combinations(keys, 2):
    if not sh[a] or not sh[b]:
        continue
    j = len(sh[a] & sh[b]) / len(sh[a] | sh[b])
    if j >= 0.15:
        dups.append((round(j, 3), a, b))
out['finals_duplicates'] = sorted(dups, reverse=True)

# finals vs preliminary corpus
prelim = {}
for f in os.listdir(TXTP):
    if f.endswith('.txt'):
        prelim[f[:-4]] = norm(io.open(os.path.join(TXTP, f), encoding='utf-8', errors='replace').read())
prelim_sh = {k: shingles(v) for k, v in prelim.items() if len(v) > 200}
cross = []
for fn in sh:
    for pk, ps in prelim_sh.items():
        if not ps:
            continue
        j = len(sh[fn] & ps) / len(sh[fn] | ps)
        if j >= 0.15:
            cross.append((round(j, 3), fn, pk))
out['finals_vs_prelim_duplicates'] = sorted(cross, reverse=True)

json.dump(out, io.open(os.path.join(DATA, 'finals_geo_prob_stats.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1, default=str)

# ---------------------------------------------------------------- print
P = print
P('### quality', dict(out['quality']))
P('### per subject', {k: dict(v) for k, v in out['quality_by_subject'].items()})
P('### problems', out['problems_total'], 'geo', out['problems_geo'], 'prob', out['problems_prob'])
P('### by kind', {k: dict(v) for k, v in out['problems_by_kind_subject'].items()})
P('### kind stats', json.dumps(out['kind_stats'], ensure_ascii=False))
P('### subj stats', json.dumps(out['subject_stats'], ensure_ascii=False))
P('### subj|kind', json.dumps(out['subj_kind_stats'], ensure_ascii=False))
P('### proof vs calc', out['proof_vs_calc'], json.dumps(out['proof_vs_calc_by_kind'], ensure_ascii=False))
P('### verbs', json.dumps(out['verbs'], ensure_ascii=False))
P('### topic freq (top 40)')
for k, v in list(out['topic_freq'].items())[:40]:
    P('   %-22s %3d  %s' % (k, sum(v.values()), ','.join(sorted(v))))
P('### finals duplicates', json.dumps(out['finals_duplicates'], ensure_ascii=False))
P('### finals-vs-prelim duplicates', json.dumps(out['finals_vs_prelim_duplicates'], ensure_ascii=False))
P('### paper tag hits', json.dumps(out['paper_tag_hits'], ensure_ascii=False))
