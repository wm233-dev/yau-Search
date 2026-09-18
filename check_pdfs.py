# -*- coding: utf-8 -*-
import fitz, os, io
BASE = r"E:\deepseek_exclusive\math\.tmp\yau\2010-2026历年笔试真题"
files = [
 r"2010\GeometryTopology-indi.pdf",
 r"2011\3.GeomTop-Individual-2011.pdf",
 r"2013\geometry2013(individual).pdf",
 r"2016\geometry2016-individual.pdf",
 r"2018\geometry2018-individual.pdf",
 r"2022\ExamPaper_2022\geometry_and_topology_22s.pdf",
 r"2026\2026 Geo_Topology.pdf",
]
out=[]
for rel in files:
    p=os.path.join(BASE, rel)
    d=fitz.open(p)
    out.append("#"*80); out.append("FILE: "+rel+" pages="+str(d.page_count))
    for i in range(d.page_count):
        out.append("--- page %d ---"%(i+1))
        out.append(d[i].get_text() or "")
    d.close()
io.open(r"E:\deepseek_exclusive\math\.tmp\burn2026\pdf_check1.txt","w",encoding="utf-8").write("\n".join(out))
print("ok")
