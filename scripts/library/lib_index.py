
# -*- coding: utf-8 -*-
"""Build a merged library index: master_catalog + library_toc + subject_classification."""
import json, sys, os, collections
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"sources/book_research"
OUT  = r".\scripts\lib_index.json"

mc = json.load(open(BASE + r"data\master_catalog.json", encoding='utf-8'))['records']
toc = json.load(open(BASE + r"\raw\library_toc.json", encoding='utf-8'))['files']
sub = json.load(open(BASE + r"data\subject_classification.json", encoding='utf-8'))['records']

toc_by_path = {t['path']: t for t in toc}
sub_by_id = {s['id']: s for s in sub}

out = []
for r in mc:
    p = r['file_path']
    t = toc_by_path.get(p, {})
    s = sub_by_id.get(r['canonical_id'], {})
    out.append({
        'id': r['canonical_id'],
        'title': r['canonical_title'],
        'fn': r['original_filename'],
        'author': r['author'],
        'series': r['series'],
        'publisher': r['publisher'],
        'year': r['publication_year'],
        'edition': r['edition'],
        'vol': r['volume'],
        'path': p,
        'subject': s.get('subject'),
        'sub_conf': s.get('confidence'),
        'text_layer': r['text_layer'],
        'bookmark': r['bookmark_available'],
        'bookmark_count': r['bookmark_count'],
        'pages': r['pages'],
        'toc': t.get('toc', []),
        'n_toc': t.get('n_toc', 0),
    })

json.dump(out, open(OUT,'w',encoding='utf-8'), ensure_ascii=False)
print("wrote", OUT, len(out))

# stats
n_use = sum(1 for o in out if o['n_toc'] >= 8)
print("books with n_toc>=8:", n_use)
print("books with n_toc>=3:", sum(1 for o in out if o['n_toc']>=3))
print("books with toc empty:", sum(1 for o in out if o['n_toc']==0))
c = collections.Counter(o['subject'] for o in out)
print("\nsubject distribution:")
for k,v in c.most_common(40):
    print(f"  {k}: {v}")
