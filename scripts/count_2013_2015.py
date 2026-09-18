# -*- coding: utf-8 -*-
"""Robust top-level problem counting per paper (2013-2015)."""
import os, re, glob, json
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"

def raw(n): return open(os.path.join(TXT, n), encoding="utf-8", errors="replace").read()

def count_problems(text):
    # prefer explicit "Problem N."
    nums = set()
    for m in re.finditer(r"(?mi)^[ \t]*Problem\s+(\d+)\s*[\.\:]", text):
        nums.add(int(m.group(1)))
    if len(nums) >= 3:
        return sorted(nums), "Problem N."
    nums = set()
    for m in re.finditer(r"(?mi)^[ \t]*(\d+)\s*\.\s*(?:\(|\s)", text):
        n = int(m.group(1))
        if 1 <= n <= 12:
            nums.add(n)
    return sorted(nums), "N."

combo = raw("2013_TeamProblems2013.txt")
tm = list(re.finditer(r"S\.-T\. Yau College Student Mathematics Contests 2013\s*\n(.+?)\nTeam", combo, re.S))
rows = []
for i, m in enumerate(tm):
    s = m.start(); e = tm[i+1].start() if i+1 < len(tm) else len(combo)
    body = combo[s:e]
    nm = re.sub(r"\s+", " ", m.group(1)).strip()
    ns, mode = count_problems(body)
    rows.append(("2013_TeamProblems2013.txt::"+nm, len(body), ns, mode))

names = []
for y in ("2013","2014","2015"):
    names += [os.path.basename(p) for p in sorted(glob.glob(os.path.join(TXT, y+"_*.txt")))]
for n in names:
    if n == "2013_TeamProblems2013.txt": continue
    t = raw(n); ns, mode = count_problems(t)
    rows.append((n, len(t), ns, mode))

tot = 0
for nm, ln, ns, mode in rows:
    tot += len(ns)
    print("%-58s chars=%5d n=%2d %-10s %s" % (nm[:58], ln, len(ns), mode, ns))
print("\nSUM of top-level problems 2013-2015 =", tot, " over", len(rows), "papers")
