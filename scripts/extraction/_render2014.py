
import fitz, os
p = r"sources/finals\2012-2025Applied Math and Computational Math\Individual\2014 Applmath (Individual and Overall).pdf"
out = r".\scripts\_p2014"
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
