
import fitz, os
p = r"F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Applied Math and Computational Math\Individual\2014 Applmath (Individual and Overall).pdf"
out = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_p2014"
os.makedirs(out, exist_ok=True)
d = fitz.open(p)
print("pages", d.page_count)
for i in [0,1,2,3]:
    pg = d[i]
    pix = pg.get_pixmap(dpi=70)
    f = os.path.join(out, "p%d.png" % (i+1))
    pix.save(f)
    print(f, pix.width, pix.height)
d.close()
