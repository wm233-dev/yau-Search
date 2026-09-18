# -*- coding: utf-8 -*-
import io, os
SCR = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts'
for name in ('_report_tpl_body.md', '_report_tpl_tail.md'):
    p = os.path.join(SCR, name)
    t = io.open(p, encoding='utf-8').read()
    t = t.replace('\u8bed\u8a00\u4e0a\uff0c\u51b3\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 5 \u4efd\uff082013/2014/2015 \u7684\u6982\u7387\u5377\uff09',
                  '\u8bed\u8a00\u4e0a\uff0c\u51b3\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 **7 \u4efd**\uff082013 \u6982\u7387\u4e2a\u4eba+\u56e2\u4f53\u30012014 \u6982\u7387\u4e2a\u4eba+\u56e2\u4f53\u30012015 \u6982\u7387\u4e2a\u4eba+\u56e2\u4f53+\u5168\u80fd\uff0c\u5171 7 \u4efd\uff09')
    t = t.replace('\u521d\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 5 \u4efd', '\u521d\u8d5b\u4fdd\u7559\u4e2d\u6587\u5377 5 \u4efd')
    t = t.replace('stats_overview \u5355\u5377\u660e\u7ec6\u4e2d 2020 \u5e74\u4e4b\u540e 71 \u6761\u8bb0\u5f55 kind \u5168\u4e3a individual',
                  'stats_overview \u5355\u5377\u660e\u7ec6\u4e2d 2020\u20132026 \u5e74\u7684 40 \u6761\u8bb0\u5f55 kind \u5168\u4e3a individual')
    io.open(p, 'w', encoding='utf-8').write(t)
    print(name, 'ok')
