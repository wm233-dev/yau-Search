# -*- coding: utf-8 -*-
"""Canonical problem extractor v2: prefer keyword-anchored numbering (Problem/Question/Exercise N)
over bare numbering, so that in-problem sub-numbering (1. 2. 3.) is not mistaken for new problems.
Emits data/problems_full.json (overwrites) + a diff report vs the previous version.
"""
import os, io, re, json, collections, shutil

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl",
       "\u2019":"'","\u2018":"'","\u201c":'"',"\u201d":'"',"\u2013":"-","\u2014":"--","\u00a0":" "}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n").replace("\x00", " "))

KW_RE = re.compile(r"(?m)^[ \t]*(?:Problem|Question|Exercise)[ \t]*(\d{1,2})\b")
BARE_RE = re.compile(r"(?m)^[ \t]*(\d{1,2})[ \t]*[.):、]?(?=[ \t\n]|$)")

def longest_run(text, rx):
    c = [(m.start(), int(m.group(1)), m.end()) for m in rx.finditer(text)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want: run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best

def cut(text, run, limit=None):
    out = []
    for i, (st, n, en) in enumerate(run):
        stop = run[i+1][0] if i+1 < len(run) else len(text)
        out.append((n, text[en:stop].strip(), run[i][0]))
    if limit: out = out[:limit]
    return out

HEAD_RE = re.compile(r"(?m)^[ \t]*(Algebra and Number Theory|Analysis and Di.{1,3}erential Equations|"
                     r"Geometry and Topology|Probability and Statistics|"
                     r"Applied.{0,40}(Math|Statistics|Probability).{0,20}|Computational and Applied Mathematics|"
                     r"Mathematical Physics)[ \t]*$")
SUBJ_PATTERNS = [
    ("Algebra & Number Theory", r"algebra"),
    ("Analysis & PDE",          r"analysis"),
    ("Geometry & Topology",     r"geometry|geomtop|geo_topo|geotop"),
    ("Probability & Statistics", r"probab|proba|statistic"),
    ("Mathematical Physics",    r"physic"),
    ("Computational & Applied", r"applied|comput"),
]
def subj_of(name):
    low = name.lower()
    for label, pat in SUBJ_PATTERNS:
        if re.search(pat, low): return label
    return "Other/Combined"

def clean(b):
    b = re.sub(r"(?m)^[ \t]*=== page \d+ ===[ \t]*$", " ", b)
    b = re.sub(r"\n{3,}", "\n\n", b)
    return b.strip()

def problems_of(text, limit=None):
    """Prefer keyword-anchored runs; fall back to bare numbering; also report which rule won."""
    kw = longest_run(text, KW_RE)
    bare = longest_run(text, BARE_RE)
    if len(kw) >= 2:
        rule = "keyword"
        chosen = kw
    else:
        rule = "bare"
        chosen = bare
    if limit and len(chosen) > limit and len(kw) >= limit:
        chosen, rule = kw[:limit], "keyword+limit"
    return cut(text, chosen, limit), rule

prev = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
prev_count = collections.Counter((p["year"], p["subject"], p["kind"]) for p in prev)

problems, rules = [], collections.Counter()
for fn in sorted(os.listdir(TXT)):
    if not fn.endswith(".txt"): continue
    name = fn[:-4]
    year = name[:4]
    low = name.lower()
    kind = "solution" if ("soln" in low or "solution" in low) else ("team" if "team" in low else "individual")
    if kind == "solution": continue
    text = norm(io.open(os.path.join(TXT, fn), encoding="utf-8").read())
    m = re.search(r"\((\d+)\s+problems?\)", text, re.I)
    limit = int(m.group(1)) if m else None
    multi = kind == "team" and text.count("=== page ") >= 5
    segs = []
    if multi:
        marks = [(mm.start(), mm.group(1)) for mm in HEAD_RE.finditer(text)]
        if len(marks) >= 2:
            for i, (st, lab) in enumerate(marks):
                stop = marks[i+1][0] if i+1 < len(marks) else len(text)
                segs.append((subj_of(lab.lower()), text[st:stop], None))
        else:
            segs = [(subj_of(name), text, limit)]
    else:
        segs = [(subj_of(name), text, limit)]
    for sj, seg, lim in segs:
        pr, rule = problems_of(seg, lim)
        rules[rule] += 1
        for n, body, _ in pr:
            body = clean(body)
            if len(body) < 30: continue
            problems.append({"year": year, "subject": sj, "paper": name, "kind": kind,
                             "n": n, "chars": len(body), "text": body})

json.dump(problems, io.open(os.path.join(DATA, "problems_full.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
new_count = collections.Counter((p["year"], p["subject"], p["kind"]) for p in problems)

L = ["# 抽取规则修正（v1 -> v2）\n",
     "v1 用单一正则同时接受「Problem N.」与裸编号，遇到卷内自带 1. 2. 3. 小问编号的卷会把小问误切成题目。",
     "v2 改为**优先使用 Problem/Question/Exercise 锚定的编号**，只有在锚定编号不足 2 个时才退回裸编号。\n",
     "规则命中统计：" + ", ".join("%s=%d" % kv for kv in rules.items()) + "\n",
     "| 年份 | 科目 | 卷别 | v1 题数 | v2 题数 | 变化 |", "|---|---|---|---|---|---|"]
keys = sorted(set(prev_count) | set(new_count))
changed = 0
for k in keys:
    a, b = prev_count.get(k, 0), new_count.get(k, 0)
    if a == b: continue
    changed += 1
    L.append("| %s | %s | %s | %d | %d | %+d |" % (k[0], k[1], k[2], a, b, b - a))
L += ["", "**总计 v1 = %d 题，v2 = %d 题；受影响(年,科目,卷别)组合 %d 个。**" % (len(prev), len(problems), changed), ""]
io.open(os.path.join(REP, "extraction_fix_v1_v2.md"), "w", encoding="utf-8").write("\n".join(L))
print("v1", len(prev), "v2", len(problems), "rules", dict(rules), "changed_combos", changed)
for k in keys:
    a, b = prev_count.get(k, 0), new_count.get(k, 0)
    if a != b: print("  DIFF", k, a, "->", b)
