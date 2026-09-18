import sys, os
sys.path.insert(0, r'E:\deepseek_exclusive\math\pylibs')
try:
    import fitz
except Exception as e:
    print('fitz import failed:', e); raise SystemExit(1)
p = r'F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Geometry and Topology\SyllabusonGeometryandTopology.pdf'
d = fitz.open(p)
print('pages:', d.page_count)
for i in range(d.page_count):
    print('=== page', i+1, '===')
    print(d[i].get_text())
