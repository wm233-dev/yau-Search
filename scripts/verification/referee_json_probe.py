# -*- coding: utf-8 -*-
import json, io
p = r".\data\problems_full.json"
probs = json.load(io.open(p, encoding="utf-8"))
want = [("2018_geometry2018_individual",6),("2016_geometry2016_individual",2),
        ("2010_GeometryTopology_indi",1),("2010_GeometryTopology_indi",3),
        ("2013_geometry2013_individual",6),("2011_3_GeomTop_Individual_2011",5),
        ("2013_TeamProblems2013",1),("2019_Geometry2019_team",1),
        ("2022_ExamPaper_2022_geometry_and_topology_22s",5),
        ("2026_2026_Geo_Topology",1)]
print("keys of one entry:", list(probs[0].keys()))
for pid, n in want:
    hits = [x for x in probs if x.get("paper")==pid and str(x.get("n"))==str(n)]
    print("\n### %s #%s -> %d hit(s)" % (pid, n, len(hits)))
    for h in hits:
        t = h.get("text") or h.get("statement") or ""
        print("   subject:", h.get("subject"), "| len(text):", len(t))
        print("   " + " ".join(t.split())[:220])
print("\n--- 2018 individual: which n are present?")
print(sorted(str(x.get("n")) for x in probs if x.get("paper")=="2018_geometry2018_individual"))
