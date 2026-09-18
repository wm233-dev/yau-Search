# -*- coding: utf-8 -*-
"""修复版：从 .doc/.docx 提取未被 pipeline 转换的卷，侧重 ASCII 可读性。"""
import os, re, zipfile
SRC = r'sources/finals'
OUT = r'.\txt_finals_extra'
os.makedirs(OUT, exist_ok=True)
targets = [
 (r'2012-2025Algebra, Number Theory and Combinatorics\Team\2014 Algebra (Team).docx', 'ALG_2014_Team'),
 (r'2012-2025Analysis and Differential Equations\Individual\2012 Analysis (Individual).doc', 'ANA_2012_Individual'),
 (r'2012-2025Analysis and Differential Equations\Individual\2013 Analysis (Individual).docx', 'ANA_2013_Individual'),
 (r'2012-2025Analysis and Differential Equations\Individual\2014 Analysis (Individual and Overall).doc', 'ANA_2014_Individual_and_Overall'),
 (r'2012-2025Analysis and Differential Equations\Team\2013 Analysis (Team).docx', 'ANA_2013_Team'),
 (r'2012-2025Analysis and Differential Equations\Team\2014 Analysis (Team).docx', 'ANA_2014_Team'),
 (r'2012-2025Analysis and Differential Equations\Overall\2013 Analysis (Overall).docx', 'ANA_2013_Overall'),
]
def asc_score(s):
    return sum(1 for ch in s[:6000] if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'))
def docx_text(path):
    with zipfile.ZipFile(path) as z:
        data = z.read('word/document.xml').decode('utf-8', 'replace')
    paras = []
    for p in re.split(r'</w:p>', data):
        s = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))
        s += ''.join(re.findall(r'<m:t[^>]*>(.*?)</m:t>', p, re.S))
        for a, b in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&apos;', "'")):
            s = s.replace(a, b)
        paras.append(s)
    return '\n'.join(paras)
def doc_text(path):
    raw = open(path, 'rb').read()
    best, bestsc = '', -1
    for off in (0, 1):
        for enc in ('utf-16-le', 'utf-16-be', 'latin-1'):
            s = raw[off:].decode(enc, 'ignore')
            sc = asc_score(s)
            if sc > bestsc: best, bestsc = s, sc
    keep = []
    for line in best.split('\n'):
        if asc_score(line) >= 4 and len(line) < 500:
            keep.append(line)
    return '\n'.join(keep)
for rel, tag in targets:
    p = os.path.join(SRC, rel)
    if not os.path.exists(p): print('MISSING', rel); continue
    t = docx_text(p) if p.lower().endswith('.docx') else doc_text(p)
    t = re.sub(r'\n{3,}', '\n\n', t).strip()
    open(os.path.join(OUT, tag + '.txt'), 'w', encoding='utf-8').write(t)
    print('%-34s chars=%6d ascii=%5d' % (tag, len(t), asc_score(t)))
