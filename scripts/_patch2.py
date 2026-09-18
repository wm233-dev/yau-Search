# -*- coding: utf-8 -*-
import io, os
SCR = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts'
# builder: move 3.4 after TAGREAD, escape pipes in dup table
b = os.path.join(SCR, 'build_finals_geo_prob_report.py')
src = io.open(b, encoding='utf-8').read()
src = src.replace("doc.replace('@@TAG_COMPARE@@', '@@TAG_COMPARE@@\\n\\n### 3.4",
                  "doc.replace('@@TAGREAD@@', '@@TAGREAD@@\\n\\n### 3.4")
src = src.replace("rows += ['| %s | %s |' % r for r in dups]",
                  "rows += ['| %s | %s |' % (r[0], r[1].replace('|', chr(92) + '|')) for r in dups]")
io.open(b, 'w', encoding='utf-8').write(src)
# head template: fix the one-line conclusion number
h = os.path.join(SCR, '_report_tpl_head.md')
t = io.open(h, encoding='utf-8').read()
t = t.replace('点名定理率 12.1% vs', '点名定理率 12.8% vs')
io.open(h, 'w', encoding='utf-8').write(t)
print('patched')
