# -*- coding: utf-8 -*-
import io, os
import fitz

F = r"sources/prelim"
L = r"sources/prelim"
targets = [
 (os.path.join(F, "2010", "GeometryTopology-indi.pdf"), "2010 individual (Q1,Q3)"),
 (os.path.join(F, "2011", "3.GeomTop-Individual-2011.pdf"), "2011 individual (Q5)"),
 (os.path.join(F, "2013", "geometry2013(individual).pdf"), "2013 individual (Q6)"),
 (os.path.join(F, "2013", "TeamProblems2013.pdf"), "2013 team (Q1, page3)"),
 (os.path.join(F, "2016", "geometry2016-individual.pdf"), "2016 individual (Q2)"),
 (os.path.join(F, "2018", "geometry2018-individual.pdf"), "2018 individual (Q6)"),
 (os.path.join(F, "2022", "ExamPaper_2022", "geometry_and_topology_22s.pdf"), "2022 exam (Q5)"),
 (os.path.join(F, "2022", "Solution_2022", "geometry_and_topology_22s_soln.pdf"), "2022 SOLUTION (Q5)"),
 (os.path.join(L, "2026", "2026 Geo_Topology.pdf"), "2026 (Q1)"),
]
outdir = r".\work"
os.makedirs(outdir, exist_ok=True)
buf = []
for path, label in targets:
    buf.append("\n\n########## %s ##########\nFILE: %s\n" % (label, path))
    if not os.path.exists(path):
        buf.append("!!! MISSING\n"); continue
    d = fitz.open(path)
    for i in range(d.page_count):
        buf.append("\n=== page %d ===\n" % (i+1))
        buf.append(d[i].get_text() or "")
    d.close()
txt = "".join(buf)
p = os.path.join(outdir, "referee_src.txt")
io.open(p, "w", encoding="utf-8").write(txt)
print("WROTE", p, len(txt))
