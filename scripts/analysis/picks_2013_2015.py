# -*- coding: utf-8 -*-
"""Extract verbatim problem blocks chosen as representative (2013-2015)."""
import os, re
TXT = r".\txt"
def raw(n): return open(os.path.join(TXT, n), encoding="utf-8", errors="replace").read()

def block(fn, start_marker, end_marker=None, occurrence=0):
    t = raw(fn)
    idxs = [m.start() for m in re.finditer(start_marker, t)]
    if not idxs:
        return "<<NOT FOUND: %s in %s>>" % (start_marker, fn)
    s = idxs[occurrence]
    if end_marker:
        m = re.search(end_marker, t[s+5:])
        e = s+5+m.start() if m else min(len(t), s+2600)
    else:
        e = min(len(t), s+2600)
    return t[s:e].rstrip()

picks = [
 ("A1", "2013_algebra2013_individual.txt", r"5\. \(60 pt\)", r"=== page \d+ ==="),
 ("A2", "2015_algebra2015_individual.txt", r"Problem 3\. \(40pt\)", r"Problem 4\. \(40pt\)"),
 ("A3", "2015_algebra2015_individual.txt", r"Problem 5 \(20pt\)", None),
 ("B1", "2014_analysis2014_individual.txt", r"5\. Let f ∈L2\(R\)", r"\n6\. Let"),
 ("B2", "2013_TeamProblems2013.txt", r"1\. Scaling behavior", r"\n2\. The following three operators"),
 ("C1", "2015_geometry2015_individual.txt", r"5\. Let M be an n-dimensional", None),
 ("C2", "2013_TeamProblems2013.txt", r"6\. Let C be a regular closed curve", None),
 ("D1", "2015_team_probability2015.txt", r"Problem 1\. One hundred passengers", r"Problem 2\."),
 ("E1", "2014_algebra2014_team.txt", r"Problem 6\. Let c be a non-zero", None),
 ("E2", "2015_team_applied2015.txt", r"Problem 1\. Consider the elliptic", r"Problem 2\."),
 ("E3", "2013_probability2013_individual.txt", r"Problem 5\. Let X1, X2 be iid uniform", r"Problem 6\."),
]
out = []
for tag, fn, s, e in picks:
    out.append("@@@ %s | %s" % (tag, fn))
    out.append(block(fn, s, e))
    out.append("")
open(r".\scripts\picks_2013_2015.txt","w",encoding="utf-8").write("\n".join(out))
print("\n".join(out))
