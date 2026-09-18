# -*- coding: utf-8 -*-
import os, fitz
OUT = r'.\data\render'
os.makedirs(OUT, exist_ok=True)
SRC = r'sources/finals\2012-2025Algebra, Number Theory and Combinatorics'
targets = [
    os.path.join(SRC, 'Individual', '2015 Algebra (Individual).pdf'),
    os.path.join(SRC, 'Team', '2015 Algebra (Team).pdf'),
    os.path.join(SRC, 'Overall', '2015 Algebra (Overall).pdf'),
]
for t in targets:
    if not os.path.exists(t):
        print('MISSING', t); continue
    doc = fitz.open(t)
    print('==', os.path.basename(t), 'pages=', doc.page_count)
    for i, pg in enumerate(doc):
        txt = pg.get_text().strip()
        print('   page', i, 'chars', len(txt), 'images', len(pg.get_images()))
        pix = pg.get_pixmap(dpi=200)
        name = os.path.splitext(os.path.basename(t))[0].replace(' ', '_').replace('(', '').replace(')', '') + '_p%d.png' % i
        pix.save(os.path.join(OUT, name))
        print('   saved', name, pix.width, pix.height)
