
# -*- coding: utf-8 -*-
"""Search the merged library index.
Usage:
  python lib_search.py --book KW1 KW2 ...        # match metadata (title/fn/author/series), all KWs must appear
  python lib_search.py --toc  KW1 KW2 ...        # match TOC lines, print matching lines per book
  python lib_search.py --both KW1 KW2 ...
Options: --limit N (default 25), --min-toc N (default 0), --pathonly
"""
import json, sys, re, argparse
sys.stdout.reconfigure(encoding='utf-8')
IDX = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\lib_index.json"
recs = json.load(open(IDX, encoding='utf-8'))

ap = argparse.ArgumentParser()
ap.add_argument('--book', nargs='*', default=None)
ap.add_argument('--toc', nargs='*', default=None)
ap.add_argument('--both', nargs='*', default=None)
ap.add_argument('--limit', type=int, default=25)
ap.add_argument('--min-toc', type=int, default=0)
ap.add_argument('--maxlines', type=int, default=30)
a = ap.parse_args()

def meta_blob(r):
    return " | ".join(str(r.get(k) or '') for k in ('title','fn','author','series','publisher'))

def ok(blob, kws):
    return all(re.search(k, blob, re.I) for k in kws)

hits = []
if a.book is not None:
    for r in recs:
        if r['n_toc'] < a.min_toc: continue
        if ok(meta_blob(r), a.book): hits.append((r, []))
elif a.toc is not None:
    for r in recs:
        if r['n_toc'] < max(a.min_toc,1): continue
        m = [l for l in r['toc'] if all(re.search(k, l, re.I) for k in a.toc)]
        if m: hits.append((r, m))
elif a.both is not None:
    for r in recs:
        if r['n_toc'] < a.min_toc: continue
        mm = ok(meta_blob(r), a.both)
        m = [l for l in r['toc'] if all(re.search(k, l, re.I) for k in a.both)]
        if mm or m: hits.append((r, m))

hits.sort(key=lambda x: (-len(x[1]), -x[0]['n_toc']))
print(f"### {len(hits)} matches")
for r, m in hits[:a.limit]:
    print(f"\n[{r['id']}] {r['title']}  | subj={r['subject']} | n_toc={r['n_toc']} | tl={r['text_layer']} | bm={r['bookmark']}")
    print(f"    author={r['author']} | series={r['series']} | pub={r['publisher']} | year={r['year']} | ed={r['edition']} | vol={r['vol']} | pages={r['pages']}")
    print(f"    fn={r['fn']}")
    if m:
        for l in m[:a.maxlines]:
            print(f"      - {l}")
