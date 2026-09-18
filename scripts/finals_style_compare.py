# -*- coding: utf-8 -*-
"""Finals vs preliminary: named-theorem citation rate, task-verb mix, lexical overlap."""
import json, io, os, re, statistics, itertools, collections

BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
DATA = os.path.join(BASE, 'data')
TXT, TXTR, TXTP = (os.path.join(BASE, d) for d in ('txt_finals', 'txt_finals_recovered', 'txt'))

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}
def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r'[ \t]+', ' ', s.replace('\r\n', '\n'))

PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):\uff1a\u3001]?(?=[ \t\n]|$)")
def best_run(t):
    c = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(t)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want:
                run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best
def cutp(t):
    r = best_run(t)
    return [(n, t[(r[i+1][0] if i+1 < len(r) else len(t)) and 0:0] or t[r[i][2]:(r[i+1][0] if i+1 < len(r) else len(t))].strip()) for i, (st, n, en) in enumerate(r)]

THEOREMS = ['bonnet', 'myers', 'synge', 'cartan', 'hadamard', 'hopf', 'poincar', 'crofton', 'brouwer',
            'lefschetz', 'hilbert', 'gauss-bonnet', 'gauss\u2013bonnet', 'stokes', 'mayer-vietoris',
            'kunneth', 'k\u00fcnneth', 'sard', 'whitney', 'nash', 'stone-weierstrass', 'cauchy',
            'radon-nikodym', 'perron-frobenius', 'cayley-hamilton', 'sylow', 'burnside', 'mordell',
            'fermat', 'dirichlet', 'chebyshev', 'chebychev', 'cram\u00e9r-rao', 'cramer-rao',
            'neyman-pearson', 'neyman\u2013pearson', 'kolmogorov', 'l\u00e9vy', 'levy', 'wald', 'fatou',
            'jensen', 'h\u00f6lder', 'holder', 'minkowski', 'doob', 'birkhoff', 'alexander',
            'riemann-roch', 'noether', 'schur', 'jordan', 'spectral theorem', 'borsuk', 'tietze',
            'urysohn', 'banach', 'hahn-banach', 'bessel', 'parseval', 'abel', 'jacobi', 'liouville',
            'maximum principle', 'reilly', 'simons', 'alexandrov', 'gung', 'chen', 'willmore',
            '\u5b9a\u7406']
THEO_RX = re.compile('|'.join(re.escape(t) for t in THEOREMS), re.I)

VERBS = ["prove", "show", "compute", "calculate", "find", "determine", "construct", "derive",
         "estimate", "evaluate", "verify", "establish", "state", "describe", "explain", "solve"]
PROOF_V = ["prove", "show", "establish", "verify"]
CALC_V = ["compute", "calculate", "find", "determine", "evaluate", "derive", "estimate"]

# ---- finals problem bodies
cur = collections.Counter()
for fn in ('finals_geo_problems.json', 'finals_prob_problems.json'):
    for r in json.load(io.open(os.path.join(DATA, fn), encoding='utf-8')):
        cur[r['paper']] += 1
finals_bodies, finals_gists = [], []
for fn in ('finals_geo_problems.json', 'finals_prob_problems.json'):
    for r in json.load(io.open(os.path.join(DATA, fn), encoding='utf-8')):
        finals_gists.append(r['gist'])
map74 = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))
seen = set()
for x in map74:
    if x['kind'] == '(root)' or x['file'] in seen: continue
    seen.add(x['file'])
    t = io.open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t.strip()) < 50 or ctrl / max(1, len(t)) > 0.08: continue
    if len(cutp(norm(t))) != cur.get(x['file'], -1):   # keep only clean segmentations
        continue
    for n, b in cutp(norm(t)):
        finals_bodies.append(b)
for fn in ('2013_prob_individual.txt', '2014_prob_individual.txt', '2013_prob_team.txt', '2014_prob_team.txt',
           '2013_prob_overall.txt', '2014_prob_overall.txt', '2013_geo_overall.txt', '2014_geo_team_docx.txt',
           '2014_geo_individual_overall.txt'):
    finals_bodies.append(io.open(os.path.join(TXTR, fn), encoding='utf-8', errors='replace').read())

prelim = json.load(io.open(os.path.join(DATA, 'problems_full.json'), encoding='utf-8'))
prelim_bodies = [p['text'] for p in prelim]
prelim_gp = [p['text'] for p in prelim if p['subject'] in ('Geometry & Topology', 'Probability & Statistics')]

def verbstat(bodies, label):
    vq = collections.Counter()
    withproof = withcalc = 0
    for b in bodies:
        low = b.lower()
        pr = sum(low.count(v) for v in PROOF_V)
        ca = sum(low.count(v) for v in CALC_V)
        if pr: withproof += 1
        if ca: withcalc += 1
        for v in VERBS:
            vq[v] += len(re.findall(r'\b' + v + r'\b', low))
    return {'label': label, 'n': len(bodies), 'prove_show_problems': withproof, 'compute_style_problems': withcalc,
            'ratio': round(withproof / max(1, withcalc), 2), 'verbs': dict(vq.most_common(8))}

P = print
P('=== named-theorem citation (regex on problem text / curated gist)')
P('   finals gist   : %d/%d = %.1f%%' % (sum(1 for g in finals_gists if THEO_RX.search(g)), len(finals_gists),
                                         100 * sum(1 for g in finals_gists if THEO_RX.search(g)) / len(finals_gists)))
P('   finals bodies : %d/%d = %.1f%%' % (sum(1 for b in finals_bodies if THEO_RX.search(b)), len(finals_bodies),
                                         100 * sum(1 for b in finals_bodies if THEO_RX.search(b)) / max(1, len(finals_bodies))))
P('   prelim bodies : %d/%d = %.1f%%' % (sum(1 for b in prelim_bodies if THEO_RX.search(b)), len(prelim_bodies),
                                         100 * sum(1 for b in prelim_bodies if THEO_RX.search(b)) / len(prelim_bodies)))
P('   prelim geo/prob: %d/%d = %.1f%%' % (sum(1 for b in prelim_gp if THEO_RX.search(b)), len(prelim_gp),
                                          100 * sum(1 for b in prelim_gp if THEO_RX.search(b)) / len(prelim_gp)))
P('=== State-and-prove phrasing')
for pat, lab in ((r'state and prove', 'state and prove'), (r'state and sketch', 'state and sketch'),
                 (r'\u53d9\u8ff0\u5e76\u8bc1\u660e', '叙述并证明'), (r'define|definition of', 'define')):
    P('   finals gist  %-16s %d ; prelim %d' % (lab,
      sum(1 for g in finals_gists if re.search(pat, g, re.I)), sum(1 for b in prelim_bodies if re.search(pat, b, re.I))))
P('=== verb mix')
P('   finals  %s' % json.dumps(verbstat(finals_bodies, 'finals'), ensure_ascii=False))
P('   prelim  %s' % json.dumps(verbstat(prelim_bodies, 'prelim'), ensure_ascii=False))
P('   prelimGP %s' % json.dumps(verbstat(prelim_gp, 'prelimGP'), ensure_ascii=False))

# ---- lexical overlap
def shingles(t, n=6):
    w = re.findall(r"[A-Za-z']+", t.lower())
    return {tuple(w[i:i+n]) for i in range(max(0, len(w)-n+1))}
fin_sh = {}
for x in map74:
    if x['kind'] == '(root)': continue
    t = io.open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t.strip()) < 50 or ctrl / max(1, len(t)) > 0.08: continue
    fin_sh[x['file']] = shingles(norm(t))
for fn in os.listdir(TXTR):
    fin_sh['REC:' + fn] = shingles(norm(io.open(os.path.join(TXTR, fn), encoding='utf-8', errors='replace').read()))
pre_sh = {}
for f in os.listdir(TXTP):
    if f.endswith('.txt'):
        pre_sh[f[:-4]] = shingles(norm(io.open(os.path.join(TXTP, f), encoding='utf-8', errors='replace').read()))
best, hist = [], collections.Counter()
for k, s in fin_sh.items():
    if not s: continue
    mx = 0.0; arg = None
    for pk, ps in pre_sh.items():
        if not ps: continue
        j = len(s & ps) / len(s | ps)
        if j > mx: mx, arg = j, pk
    best.append((round(mx, 3), k, arg))
    hist[round(mx * 10) / 10] += 1
best.sort(reverse=True)
P('=== finals paper -> most similar PRELIM paper (6-gram Jaccard), top 10')
for j, k, arg in best[:10]:
    P('   %.3f  %-52s ~ %s' % (j, k[:52], arg))
P('   similarity histogram (0.1 bins): %s' % json.dumps(dict(sorted(hist.items())), ensure_ascii=False))
P('   pairs >= 0.15: %d / %d' % (sum(1 for j, k, a in best if j >= 0.15), len(best)))
