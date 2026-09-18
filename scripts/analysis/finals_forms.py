# -*- coding: utf-8 -*-
import os, re, json
ROOT = r'.'
TXT = os.path.join(ROOT, 'txt_finals')
m = json.load(open(os.path.join(ROOT, 'data', '_finals_txtmap.json'), encoding='utf-8'))
sel = [(k, v) for k, v in m.items() if ('Algebra' in v['subj']) or ('Analysis' in v['subj'])]
PATS = {
 '选做/任选(out of)': r'(?:solve|Solve|prove)\s+\w*\s*(?:out of|of the following)|out of the following',
 'optional': r'optional',
 'Choose (1) or (2)': r'Choose \(1\) or \(2\)',
 'at least N of': r'at least \w+ out of',
 'Please solve': r'Please solve',
 'Oral': r'\b[Oo]ral\b|\bORAL\b',
 'Overall/All-round': r'Overall|All-round',
}
for name, pat in PATS.items():
    hits = []
    for k, v in sel:
        t = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
        if re.search(pat, t):
            hits.append('%s-%s-%s' % (v['year'], ('ALG' if 'Algebra' in v['subj'] else 'ANA'), v['kind']))
    print('%-20s 卷数=%2d  %s' % (name, len(hits), ', '.join(sorted(hits))))
