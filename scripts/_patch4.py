# -*- coding: utf-8 -*-
import io, os
p = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_report_tpl_tail.md'
t = io.open(p, encoding='utf-8').read()
old = '20. \u8bed\u8a00\uff1a\u51b3\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 5 \u4efd\uff082013/2014/2015 \u7684\u6982\u7387\u5377\uff09\uff1b2020 \u5e74\u4e4b\u540e\u5168\u90e8\u4e3a\u82f1\u6587\u3002'
new = '20. \u8bed\u8a00\uff1a\u51b3\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 7 \u4efd\uff082013/2014/2015 \u5e74\u7684\u6982\u7387\u4e2a\u4eba\u5377\u3001\u56e2\u4f53\u5377\uff0c\u4ee5\u53ca 2015 \u5168\u80fd\u5377\uff09\uff1b2020 \u5e74\u4e4b\u540e\u5168\u90e8\u4e3a\u82f1\u6587\u3002'
assert old in t, 'not found'
t = t.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(t)
print('tail fixed')
