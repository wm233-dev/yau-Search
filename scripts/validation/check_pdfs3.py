# -*- coding: utf-8 -*-
import fitz, os, io
BASE = r"sources/prelim"
files = [r"2014\geometry2014(individual).pdf", r"2021\ExamPaper_21S\geometry_and_topology_21s.pdf"]
out=[]
for rel in files:
    p=os.path.join(BASE, rel)
    d=fitz.open(p)
    out.append("FILE: "+rel+" pages="+str(d.page_count))
    for i in range(d.page_count):
        out.append("--- page %d ---"%(i+1))
        out.append(d[i].get_text() or "")
    d.close()
io.open(r".\pdf_check3.txt","w",encoding="utf-8").write("\n".join(out))
print("ok")
