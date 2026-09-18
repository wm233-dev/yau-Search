# -*- coding: utf-8 -*-
import json, os, re
ROOT = r'E:\deepseek_exclusive\math'
TXT = os.path.join(ROOT, '.tmp', 'burn2026', 'txt_finals')
m = json.load(open(os.path.join(ROOT, '.tmp', 'burn2026', 'data', '_finals_txtmap.json'), encoding='utf-8'))
sel = [(k, v) for k, v in m.items() if ('Algebra' in v['subj']) or ('Analysis' in v['subj'])]
sel.sort(key=lambda kv: (('ALG' if 'Algebra' in kv[1]['subj'] else 'ANA'), kv[1]['kind'], kv[1]['year']))
out = []
for i, (k, v) in enumerate(sel):
    raw = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    tag = 'ALG' if 'Algebra' in v['subj'] else 'ANA'
    out.append('\n' + '=' * 100)
    out.append('### %d %s | %s | %s | chars=%d pages=%d | %s' % (i, tag, v['kind'], v['year'], v['chars'], v['pages'], v['file']))
    out.append('=' * 100)
    out.append(raw.strip())
dump = '\n'.join(out)
open(os.path.join(ROOT, '.tmp', 'burn2026', 'data', '_finals_alg_ana_dump.txt'), 'w', encoding='utf-8').write(dump)
print('files', len(sel), 'dumpchars', len(dump))
for i, (k, v) in enumerate(sel):
    raw = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    print('%3d %s %-10s %s chars=%d' % (i, ('ALG' if 'Algebra' in v['subj'] else 'ANA'), v['kind'], v['year'], len(raw.strip())))
