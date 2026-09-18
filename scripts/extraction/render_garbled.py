# -*- coding: utf-8 -*-
"""Render the mojibake/empty finals PDFs to PNG so a vision model can transcribe them."""
import os, sys
sys.path.insert(0, r'sources/pylibs')
import fitz

SRC = r'sources/finals\2012-2025Probability and Statistics'
OUT = r'.\scripts\_img'
os.makedirs(OUT, exist_ok=True)
files = [
    ('2013 Probability (Individual).pdf', '2013_ind'),
    ('2014 Probability (Individual).pdf', '2014_ind'),
    ('2013 Probability (Team).pdf', '2013_team'),
    ('2014 Probability (Team).pdf', '2014_team'),
    ('2013 Probability (Overall).pdf', '2013_overall'),
]
for rel, tag in files:
    if 'Overall' in rel:
        path = os.path.join(SRC, 'Overall', rel)
    elif 'Team' in rel:
        path = os.path.join(SRC, 'Team', rel)
    else:
        path = os.path.join(SRC, 'Individual', rel)
    if not os.path.exists(path):
        print('MISSING', path); continue
    doc = fitz.open(path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=200)
        out = os.path.join(OUT, f'{tag}_p{i+1}.png')
        pix.save(out)
        print('WROTE', out, pix.width, pix.height)
    print('  pages=', doc.page_count, 'textlen=', len(''.join(p.get_text() for p in doc)))
