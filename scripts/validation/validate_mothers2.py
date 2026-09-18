# -*- coding: utf-8 -*-
"""Stronger validation: member refs must match (year, subject, kind, n); also report each JSON schema."""
import os, io, json, collections

ROOT = r"."
DATA = os.path.join(ROOT, "data")
P = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
key4 = collections.defaultdict(int)
for p in P:
    key4[(p["year"], p["subject"], p["kind"], str(p["n"]))] += 1

SUBJ = {"algebra": "Algebra & Number Theory", "analysis": "Analysis & PDE", "geometry": "Geometry & Topology",
        "probability": "Probability & Statistics", "computational": "Computational & Applied",
        "physics": "Mathematical Physics"}
tot_m, tot_bad, tot_uniq = 0, 0, 0
for k, subj in SUBJ.items():
    raw = json.load(io.open(os.path.join(DATA, "mother_%s.json" % k), encoding="utf-8"))
    print("== %s  schema=%s" % (k, "dict{mothers,orphans}" if isinstance(raw, dict) else "list"))
    mothers = raw["mothers"] if isinstance(raw, dict) and "mothers" in raw else raw
    orphans = raw.get("orphans", []) if isinstance(raw, dict) else []
    bad, uniq, slots = [], set(), 0
    for m in mothers:
        for mem in m.get("members", []) or []:
            slots += 1
            t = (str(mem.get("year")), subj, mem.get("kind") or "individual", str(mem.get("n")))
            if key4.get(t, 0) == 0:
                bad.append((m.get("id"), t))
            else:
                uniq.add(t)
    n_subj = sum(1 for p in P if p["subject"] == subj)
    print("   mothers=%d orphans=%d slots=%d uniq=%d / subject_problems=%d  bad=%d"
          % (len(mothers), len(orphans), slots, len(uniq), n_subj, len(bad)))
    for b in bad[:8]:
        print("      BAD", b)
    tot_m += len(mothers); tot_bad += len(bad); tot_uniq += len(uniq)
print("---")
print("sum(mothers as listed)=%d  invalid refs=%d  uniquely covered=%d/%d (%.1f%%)" % (tot_m, tot_bad, tot_uniq, len(P), tot_uniq / len(P) * 100))
print("NOTE: 'mothers' lists include orphan entries for some subjects (schemas differ) -> use per-subject numbers, not the sum, as the mother count.")
