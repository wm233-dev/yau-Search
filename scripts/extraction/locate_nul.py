# -*- coding: utf-8 -*-
"""定位 NUL 字节位置, 供报告"存疑清单"精确引用"""
import glob, os
src = r'.\txt'
for f in sorted(glob.glob(os.path.join(src, '201[678]_*.txt'))):
    b = open(f, 'rb').read()
    if b'\x00' not in b: continue
    print('=' * 70)
    print(os.path.basename(f), 'len=', len(b))
    i = -1
    while True:
        i = b.find(b'\x00', i + 1)
        if i < 0: break
        ctx = b[max(0, i-90):i+90].replace(b'\x00', b'<NUL>')
        try: ctx = ctx.decode('utf-8')
        except Exception: ctx = repr(ctx)
        line = b[:i].count(b'\n') + 1
        print(f'  offset={i}  行号≈{line}')
        print('    上下文:', repr(ctx.replace(chr(10), ' / ')))
