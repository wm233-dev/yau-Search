# -*- coding: utf-8 -*-
import os
D = r'.\txt_finals_extra'
for fn in ['ANA_2012_Individual.txt', 'ANA_2014_Individual_and_Overall.txt']:
    b = open(os.path.join(D, fn), 'rb').read()
    print('==', fn, 'bytes', len(b), 'head', b[:16])
    for enc in ('utf-8', 'utf-16-le', 'utf-16-be', 'latin-1'):
        try:
            s = b.decode(enc)
        except Exception as e:
            print('  ', enc, 'FAIL', e); continue
        print('  %-10s %r' % (enc, s[:120]))
