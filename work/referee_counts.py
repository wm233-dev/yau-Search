# -*- coding: utf-8 -*-
import json, collections, io
p = r"E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json"
d = json.load(io.open(p, encoding="utf-8"))
print("type:", type(d).__name__, "len:", len(d))
if isinstance(d, dict):
    print("keys:", list(d.keys())[:10])
    probs = d.get("problems", d)
else:
    probs = d
print("n problems:", len(probs))
subj = collections.Counter(x.get("subject") for x in probs)
print("subjects:", dict(subj))
paper = collections.Counter(x.get("paper") for x in probs)
print("n papers:", len(paper))
# the 10 papers used by the handout
for pid in ["2010_GeometryTopology_indi","2016_geometry2016_individual","2026_2026_Geo_Topology",
            "2019_Geometry2019_team","2022_ExamPaper_2022_geometry_and_topology_22s",
            "2013_geometry2013_individual","2011_3_GeomTop_Individual_2011","2013_TeamProblems2013",
            "2018_geometry2018_individual"]:
    print("  ", pid, "->", paper.get(pid))
