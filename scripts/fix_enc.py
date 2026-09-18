# -*- coding: utf-8 -*-
import os, re
D = r'E:\deepseek_exclusive\math\.tmp\burn2026\txt_finals_extra'
for fn in ['ANA_2012_Individual.txt', 'ANA_2014_Individual_and_Overall.txt']:
    p = os.path.join(D, fn)
    b = open(p, 'rb').read()
    s = b.decode('gbk', 'replace')
    s = s.replace('\r\n', '\n')
    s = re.sub(r'[\x00-\x08\x0b-\x1f]', '', s)
    s = re.sub(r'\n{3,}', '\n\n', s).strip()
    open(p, 'w', encoding='utf-8').write(s)
    print('=====', fn, 'chars', len(s))
    print(s[:3000])
    print()
