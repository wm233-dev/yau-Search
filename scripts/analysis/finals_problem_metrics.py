# -*- coding: utf-8 -*-
"""Problem-level metrics for the finals corpus (same formulas as enrich_problems.py),
segmented with the same cutp() heuristic, then compared with the preliminary corpus.
"""
import json, io, os, re, statistics, collections

BASE = r'.'
DATA = os.path.join(BASE, 'data')
TXT = os.path.join(BASE, 'txt_finals')
TXTR = os.path.join(BASE, 'txt_finals_recovered')

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}


def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r'[ \t]+', ' ', s.replace('\r\n', '\n'))


PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):\uff1a\u3001]?(?=[ \t\n]|$)")
SUB_RE = re.compile(r"(?m)^[ \t]*\(?([a-d])\)[ \t]|\((\d)\)[ \t]")
SYM_RE = re.compile(r'[\u2211\u222b\u2202\u2207\u221a\u2264\u2265\u2208\u2282\u2286\u00d7\u2297\u2295\u2192\u21a6\u21d2\u2200\u2203|]')


def best_run(t):
    c = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(t)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1:
            continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want:
                run.append(c[j]); want += 1
        if len(run) > len(best):
            best = run
    return best


def cutp(t):
    r = best_run(t)
    out = []
    for i, (st, n, en) in enumerate(r):
        stop = r[i + 1][0] if i + 1 < len(r) else len(t)
        out.append((n, t[en:stop].strip()))
    return out


def enriched(body):
    words = re.findall(r"[A-Za-z']+", body)
    subparts = len(SUB_RE.findall(body))
    syms = len(SYM_RE.findall(body))
    diff = 1.0 + min(2.0, len(words) / 160.0) + min(1.5, subparts * 0.5) + min(1.0, syms / 40.0)
    return {'words': len(words), 'chars': len(body), 'subparts': subparts, 'symbols': syms, 'diff_len_only': round(diff, 2)}


# curated counts per (paper-file, subject) -- for reporting extraction coverage
cur = collections.Counter()
for r in json.load(io.open(os.path.join(DATA, 'finals_geo_problems.json'), encoding='utf-8')):
    cur[r['paper']] += 1
for r in json.load(io.open(os.path.join(DATA, 'finals_prob_problems.json'), encoding='utf-8')):
    cur[r['paper']] += 1

fin = json.load(io.open(os.path.join(DATA, 'geoprob_map.json'), encoding='utf-8'))
rows = []
seen = set()
for x in fin:
    if x['kind'] == '(root)' or x['file'] in seen:
        continue
    seen.add(x['file'])
    t = io.open(os.path.join(TXT, x['txt']), encoding='utf-8', errors='replace').read()
    ctrl = sum(1 for c in t if ord(c) < 32 and ord(c) not in (9, 10, 13))
    if len(t.strip()) < 50 or ctrl / max(1, len(t)) > 0.08:
        continue
    items = cutp(norm(t))
    subj = 'Geometry & Topology' if 'Geometry' in x['subj'] else 'Probability & Statistics'
    rows.append({'file': x['file'], 'subj': subj, 'year': x['year'], 'kind': x['kind'],
                 'curated': cur.get(x['file'], 0), 'auto': len(items),
                 'probs': [enriched(b) for n, b in items]})

P = print
P('=== finals auto-segmentation coverage')
tot_cur = tot_auto = 0
for r in sorted(rows, key=lambda r: -r['curated']):
    tot_cur += r['curated']; tot_auto += r['auto']
    flag = '' if r['auto'] == r['curated'] else '  <-- mismatch'
    P('  %-6s %-11s auto=%2d curated=%2d  %s%s' % (r['year'], r['kind'], r['auto'], r['curated'], r['file'][:46], flag))
P('  TOTAL auto=%d curated=%d' % (tot_auto, tot_cur))

matched = [r for r in rows if r['auto'] == r['curated'] and r['curated'] > 0]
P('=== papers where auto == curated: %d/%d' % (len(matched), len([r for r in rows if r['curated'] > 0])))


def agg(rs):
    ps = [p for r in rs for p in r['probs']]
    if not ps:
        return None
    return {'problems': len(ps), 'mean_words': round(statistics.mean([p['words'] for p in ps]), 1),
            'median_words': statistics.median([p['words'] for p in ps]),
            'mean_subparts': round(statistics.mean([p['subparts'] for p in ps]), 2),
            'mean_symbols': round(statistics.mean([p['symbols'] for p in ps]), 1),
            'mean_diff_len': round(statistics.mean([p['diff_len_only'] for p in ps]), 2)}


P('=== finals per-problem (auto-segmented, all readable papers)')
for s in ('Geometry & Topology', 'Probability & Statistics', None):
    rs = [r for r in rows if s is None or r['subj'] == s]
    P('   %-24s %s' % (s or 'ALL', json.dumps(agg(rs), ensure_ascii=False)))
P('=== finals per-problem (only papers where auto == curated -> higher confidence)')
for s in ('Geometry & Topology', 'Probability & Statistics', None):
    rs = [r for r in matched if s is None or r['subj'] == s]
    P('   %-24s %s' % (s or 'ALL', json.dumps(agg(rs), ensure_ascii=False)))
P('=== finals per-problem by kind (auto == curated subset)')
for k in ('Individual', 'Team', 'Overall'):
    rs = [r for r in matched if r['kind'] == k]
    P('   %-12s %s' % (k, json.dumps(agg(rs), ensure_ascii=False)))

# ---------------- preliminary
enr = json.load(io.open(os.path.join(DATA, 'problems_enriched.json'), encoding='utf-8'))
P('=== preliminary per-problem (problems_enriched.json)')
for s in ('Geometry & Topology', 'Probability & Statistics', None):
    es = [e for e in enr if s is None or e['subject'] == s]
    P('   %-24s n=%d mean_words=%.1f median=%.0f subparts=%.2f symbols=%.1f diff=%.2f' % (
        s or 'ALL', len(es), statistics.mean([e['words'] for e in es]), statistics.median([e['words'] for e in es]),
        statistics.mean([e['subparts'] for e in es]), statistics.mean([e['symbols'] for e in es]),
        statistics.mean([e['difficulty_proxy'] for e in es])))
json.dump({'finals_rows': rows}, io.open(os.path.join(DATA, 'finals_problem_metrics.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
