# -*- coding: utf-8 -*-
"""Cross-validate the six mother-problem JSON files against problems_full.json and aggregate."""
import os, io, json, collections

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
DATA, REP = os.path.join(ROOT, "data"), os.path.join(ROOT, "reports")
P = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
index = collections.defaultdict(list)
for p in P:
    index[(p["year"], p["kind"], str(p["n"]))].append(p)
print("problems_full:", len(P), "unique keys:", len(index))

SUBJ = {"algebra": "Algebra & Number Theory", "analysis": "Analysis & PDE", "geometry": "Geometry & Topology",
        "probability": "Probability & Statistics", "computational": "Computational & Applied",
        "physics": "Mathematical Physics"}
tot_mothers = tot_members = tot_unique = tot_bad = 0
rows = []
for key, subj in SUBJ.items():
    fp = os.path.join(DATA, "mother_%s.json" % key)
    if not os.path.exists(fp):
        print("MISSING", fp); continue
    raw = json.load(io.open(fp, encoding="utf-8"))
    mothers = raw["mothers"] if isinstance(raw, dict) and "mothers" in raw else raw
    if isinstance(raw, dict) and "mothers" in raw:
        orphans = raw.get("orphans", [])
    else:
        orphans = []
    members, bad, uniq = 0, [], set()
    for m in mothers:
        for mem in m.get("members", []):
            y, k, n = str(mem.get("year")), mem.get("kind", "individual"), str(mem.get("n"))
            members += 1
            if (y, k, n) not in index:
                bad.append((m.get("id"), y, k, n))
            else:
                uniq.add((y, k, n))
    n_subj = sum(1 for p in P if p["subject"] == subj)
    cov = len(uniq) / max(n_subj, 1)
    tot_mothers += len(mothers); tot_members += members; tot_unique += len(uniq); tot_bad += len(bad)
    rows.append((key, subj, len(mothers), len(orphans), members, len(uniq), n_subj, cov, len(bad)))
    print("%-14s mothers=%-3d orphans=%-3d member_slots=%-4d unique_members=%-4d subject_problems=%-4d coverage=%.1f%% bad_refs=%d"
          % (key, len(mothers), len(orphans), members, len(uniq), n_subj, cov * 100, len(bad)))
    for b in bad[:5]:
        print("    BAD REF:", b)

print("---")
print("TOTAL mother problems = %d, member slots = %d, uniquely covered problems = %d / %d (%.1f%%), invalid refs = %d"
      % (tot_mothers, tot_members, tot_unique, len(P), tot_unique / len(P) * 100, tot_bad))

# deliverables check
want = ["referee_algebra.md", "referee_analysis.md", "referee_geometry.md",
        "mock_exam_A.md", "mock_exam_B.md", "mock_exam_C.md",
        "mother_algebra.md", "mother_analysis.md", "mother_geometry.md",
        "mother_probability.md", "mother_computational.md", "mother_physics.md"]
print("--- deliverable files ---")
for w in want:
    fp = os.path.join(REP, w)
    print("%-26s %s  %s bytes" % (w, os.path.exists(fp), os.path.getsize(fp) if os.path.exists(fp) else "-"))
