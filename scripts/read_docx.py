# -*- coding: utf-8 -*-
"""Extract docx (incl. OMML math runs) and crude legacy .doc text from F: originals."""
import os, re, zipfile

def docx_text(p):
    z = zipfile.ZipFile(p)
    xml = z.read('word/document.xml').decode('utf-8', 'replace')
    paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
    out = []
    for para in paras:
        toks = re.findall(r'<(w|m):t[^>]*>(.*?)</\1:t>', para, re.S)
        txt = ''.join(t[1] for t in toks)
        txt = re.sub(r'<[^>]+>', '', txt)
        txt = txt.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        if txt.strip():
            out.append(txt.strip())
    return out

def crude_doc_text(p):
    data = open(p, 'rb').read()
    # scan for UTF-16LE runs of printable/CJK chars
    runs = []
    cur = []
    for i in range(0, len(data) - 1, 2):
        ch = data[i] | (data[i + 1] << 8)
        ok = (0x20 <= ch <= 0x7e) or (0x4e00 <= ch <= 0x9fff) or ch in (0x2018, 0x2019, 0x201c, 0x201d, 0x2013, 0x2014, 0x3002, 0xff0c, 0xff1f, 0xff1a, 0xff08, 0xff09)
        if ok:
            cur.append(chr(ch))
        else:
            if len(cur) >= 6:
                runs.append(''.join(cur))
            cur = []
    if len(cur) >= 6:
        runs.append(''.join(cur))
    return runs

if __name__ == '__main__':
    for p in [r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Geometry and Topology\Overall\2013 Geometry (Overall).docx',
              r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Geometry and Topology\Team\2014 Geometry (Team).docx']:
        print('=====', os.path.basename(p))
        for line in docx_text(p):
            print('  |', line)
    p = r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Geometry and Topology\Individual\2014 Geometry (Individual&Overall).doc'
    print('===== crude .doc scan', os.path.basename(p))
    for line in crude_doc_text(p)[:80]:
        print('  |', line)
