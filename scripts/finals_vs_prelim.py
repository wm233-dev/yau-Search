# -*- coding: utf-8 -*-
"""Finals vs preliminary (written) round: same-metric comparison for Geometry and Probability.

Both sides use identical metric code on whole-paper extracted text, plus the
problem counts declared in the respective manifests.
"""
import json, io, os, re, collections, statistics

BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
TXT, TXTP, DATA = (os.path.join(BASE, d) for d in ('txt_finals', 'txt', 'data'))

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}


def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r'[ \t]+', ' ', s.replace('\r\n', '\n'))


SUB_RE = re.compile(r'(?m)^[ \t]*\(?([a-d])\)[ \t]|\((\d)\)[ \t]')
SYM_RE = re.compile(r'[\u2211\u222b\u2202\u2207\u221a\u2264\u2265\u2208\u2282\u2286\u00d7\u2297\u2295\u2192\u21a6\u21d2\u2200\u2203|]')
TAGS = [
    ("代数拓扑", r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
    ("微分几何", r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|mean curvature|gauss-bonnet|holonomy"),
    ("微分流形/形式", r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
    ("纤维丛/示性类", r"fiber bundle|vector bundle|principal bundle|chern class|pontryagin|characteristic class|section of"),
    ("代数几何", r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
    ("辛几何/力学", r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville"),
    ("概率论", r"random variable|probability space|expectation|variance|independence|conditional (probability|expectation)|martingale|brownian|random walk|markov chain|poisson process|central limit|law of large numbers|characteristic function"),
    ("数理统计", r"estimator|unbiased|maximum likelihood|sufficient statistic|cramer-rao|confidence interval|hypothesis test|likelihood ratio|regression|bayes|posterior|prior distribution|risk function"),
    ("线性代数/矩阵", r"matrix|matrices|eigenvalue|eigenvector|hermitian|determinant|\brank\b"),
]
TAG_RX = [(n, re.compile(p, re.I)) for n, p in TAGS]
VERBS = ["prove", "show that", "show", "compute", "calculate", "find", "determine", "construct",
         "explain", "evaluate", "verify", "establish", "derive", "estimate", "solve", "describe"]
PROOF_V = ["prove", "show", "establish", "verify", "state"]
CALC_V = ["compute", "calculate", "find", "determine", "evaluate", "derive", "estimate"]


def paper_metrics(text):
    t = norm(text)
    words = re.findall(r"[A-Za-z']+", t)
    subparts = len(SUB_RE.findall(t))
    syms = len(SYM_RE.findall(t))
    tags = [n for n, rx in TAG_RX if rx.search(t)]
    low = t.lower()
    verbs = {v: len(re.findall(r'\b' + re.escape(v) + r'\b', low)) for v in VERBS}
    diff = 1.0 + min(2.0, len(words) / 160.0) + min(1.5, subparts * 0.5) + min(1.0, syms / 40.0) \
        + min(1.0, max(0, len(tags) - 1) * 0.25)
    return {'chars': len(t), 'words': len(words), 'subparts': subparts, 'symbols': syms,
            'tags': tags, 'verbs': {k: v for k, v in verbs.items() if v}, 'diff': round(diff, 2)}


def agg(rows):
    if not rows:
        return None
    nprob = sum(r['problems'] for r in rows)
    proof = sum(sum(r['m']['verbs'].get(v, 0) for v in PROOF_V) for r in rows)
    calc = sum(sum(r['m']['verbs'].get(v, 0) for v in CALC_V) for r in rows)
    return {
        'papers': len(rows), 'problems': nprob,
        'mean_words_per_paper': round(statistics.mean([r['m']['words'] for r in rows]), 1),
        'words_per_problem': round(sum(r['m']['words'] for r in rows) / nprob, 1) if nprob else None,
        'chars_per_problem': round(sum(r['m']['chars'] for r in rows) / nprob, 1) if nprob else None,
        'subparts_per_problem': round(sum(r['m']['subparts'] for r in rows) / nprob, 2) if nprob else None,
        'symbols_per_problem': round(sum(r['m']['symbols'] for r in rows) / nprob, 2) if nprob else None,
        'mean_diff_proxy_per_paper': round(statistics.mean([r['m']['diff'] for r in rows]), 2),
        'proof_verbs': proof, 'calc_verbs': calc,
        'proof_over_calc': round(proof / max(1, calc), 2),
    }


# ---------------- finals
finals_rows = []
fin = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))
cur = collections.Counter()
for r in json.load(io.open(os.path.join(DATA, 'finals_geo_problems.json'), encoding='utf-8')):
    cur[('Geometry & Topology', r['year'], r['kind'])] += 1
for r in json.load(io.open(os.path.join(DATA, 'finals_prob_problems.json'), encoding='utf-8')):
    cur[('Probability & Statistics', r['year'], r['kind'])] += 1
for x in fin:
    if x['kind'] == '(root)':
        continue
    t = io.open(os.path.join(BASE, 'txt_finals', x['txt']), encoding='utf-8', errors='replace').read()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t.strip()) < 50 or ctrl / max(1, len(t)) > 0.08:
        continue
    subj = 'Geometry & Topology' if 'Geometry' in x['subj'] else 'Probability & Statistics'
    nprob = cur.get((subj, x['year'], x['kind']), 0)
    finals_rows.append({'subject': subj, 'year': x['year'], 'kind': x['kind'],
                        'problems': nprob, 'm': paper_metrics(t)})
# add recovered papers (2013/2014 prob ind/team; geo docx kept out to avoid double counting 2014 Team)
rec = [('2013_prob_individual.txt', 'Probability & Statistics', '2013', 'Individual', 3),
       ('2014_prob_individual.txt', 'Probability & Statistics', '2014', 'Individual', 3),
       ('2013_prob_team.txt', 'Probability & Statistics', '2013', 'Team', 3),
       ('2014_prob_team.txt', 'Probability & Statistics', '2014', 'Team', 4),
       ('2013_prob_overall.txt', 'Probability & Statistics', '2013', 'Overall', 4),
       ('2014_prob_overall.txt', 'Probability & Statistics', '2014', 'Overall', 2)]
for fn, subj, y, k, npb in rec:
    t = io.open(os.path.join(BASE, 'txt_finals_recovered', fn), encoding='utf-8', errors='replace').read()
    finals_rows.append({'subject': subj, 'year': y, 'kind': k, 'problems': npb, 'm': paper_metrics(t)})

# ---------------- preliminary
papers = json.load(io.open(os.path.join(DATA, 'papers.json'), encoding='utf-8'))['papers']
pre_rows = []
for p in papers:
    if p['subject'] not in ('Geometry & Topology', 'Probability & Statistics'):
        continue
    path = os.path.join(TXTP, p['file'])
    if not os.path.exists(path):
        continue
    t = io.open(path, encoding='utf-8', errors='replace').read()
    pre_rows.append({'subject': p['subject'], 'year': p['year'], 'kind': p['kind'],
                     'problems': p['n_problems'] or 0, 'm': paper_metrics(t)})

res = {'finals': {}, 'prelim': {}}
for name, rows in (('finals', finals_rows), ('prelim', pre_rows)):
    res[name]['ALL'] = agg(rows)
    for s in ('Geometry & Topology', 'Probability & Statistics'):
        res[name][s] = agg([r for r in rows if r['subject'] == s])
    for k in ('individual', 'team', 'Individual', 'Team', 'Overall'):
        sub = [r for r in rows if r['kind'] == k]
        if sub:
            res[name]['kind=' + k] = agg(sub)
    for y in sorted({r['year'] for r in rows}):
        res[name]['year=' + y] = agg([r for r in rows if r['year'] == y])

json.dump(res, io.open(os.path.join(DATA, 'finals_vs_prelim.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

P = print
for scope in ('ALL', 'Geometry & Topology', 'Probability & Statistics',
              'kind=individual', 'kind=team', 'kind=Individual', 'kind=Team', 'kind=Overall'):
    f, p = res['finals'].get(scope), res['prelim'].get(scope)
    P('== %s' % scope)
    P('   finals: %s' % json.dumps(f, ensure_ascii=False))
    P('   prelim: %s' % json.dumps(p, ensure_ascii=False))
P('== by year (finals / prelim: words per problem, diff proxy)')
for y in sorted({k[5:] for k in res['finals'] if k.startswith('year=')}):
    f = res['finals'].get('year=' + y)
    p = res['prelim'].get('year=' + y)
    P('   %s  F: n=%s w/p=%s diff=%s | P: n=%s w/p=%s diff=%s' % (
        y, f and f['problems'], f and f['words_per_problem'], f and f['mean_diff_proxy_per_paper'],
        p and p['problems'], p and p['words_per_problem'], p and p['mean_diff_proxy_per_paper']))
