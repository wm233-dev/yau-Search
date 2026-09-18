# -*- coding: utf-8 -*-
"""Extractor v3: bare numbering must be followed by real prose (>=12 chars), which kills
stray digits coming from fractions / equation numbers. Adds per-paper diagnostics."""
import os, io, re, json, collections

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl",
       "\u2019":"'","\u2018":"'","\u201c":'"',"\u201d":'"',"\u2013":"-","\u2014":"--","\u00a0":" "}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n").replace("\x00", " "))

KW_RE   = re.compile(r"(?m)^[ \t]*(?:Problem|Question|Exercise)[ \t]*(\d{1,2})\b")
BARE_RE = re.compile(r"(?m)^[ \t]*(\d{1,2})[ \t]*[.)][ \t]*(\S[^\n]{11,})")

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
        out.append((n, text[en:stop].strip()))
    return out[:limit] if limit else out

def problems_of(text, limit=None):
    kw, bare = longest_run(text, KW_RE), longest_run(text, BARE_RE)
    if len(kw) >= max(2, len(bare)):
        return cut(text, kw, limit), "keyword"
    return cut(text, bare, limit), "bare"

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
    b = re.sub(r"^\s*[.):、]\s*", "", b)
    b = re.sub(r"\n{3,}", "\n\n", b)
    return b.strip()

prev = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
prev_by_paper = collections.Counter(p["paper"] for p in prev)

problems, diag = [], []
for fn in sorted(os.listdir(TXT)):
    if not fn.endswith(".txt"): continue
    name = fn[:-4]
    year, low = name[:4], name.lower()
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
    total = 0
    for sj, seg, lim in segs:
        pr, rule = problems_of(seg, lim)
        frags = [n for n, b in pr if len(clean(b)) < 60]
        diag.append({"file": fn, "year": year, "subject": sj, "kind": kind, "rule": rule,
                     "declared": lim, "n": len(pr), "fragments": frags,
                     "prev_n": prev_by_paper.get(name, 0)})
        for n, body in pr:
            body = clean(body)
            if len(body) < 30: continue
            problems.append({"year": year, "subject": sj, "paper": name, "kind": kind,
                             "n": n, "chars": len(body), "text": body})
            total += 1
    if total == 0: print("WARN zero problems:", fn)

json.dump(problems, io.open(os.path.join(DATA, "problems_full.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(diag, io.open(os.path.join(DATA, "extraction_diagnostics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

newc = collections.Counter((p["year"], p["subject"], p["kind"]) for p in problems)
oldc = collections.Counter((p["year"], p["subject"], p["kind"]) for p in prev)
L = ["# 抽取规则修正 v2 -> v3（去碎片）\n",
     "v2 的裸编号规则会把分数/公式残留（单独一行的一个数字）当成新题号，v3 要求裸编号后必须跟 >=12 字符的正文。\n",
     "| 年份 | 科目 | 卷别 | v2 | v3 | 变化 |", "|---|---|---|---|---|---|"]
for k in sorted(set(oldc) | set(newc)):
    a, b = oldc.get(k, 0), newc.get(k, 0)
    if a != b: L.append("| %s | %s | %s | %d | %d | %+d |" % (k[0], k[1], k[2], a, b, b - a))
frag = [d for d in diag if d["fragments"]]
L += ["", "v2 合计 %d 题 -> v3 合计 %d 题。" % (len(prev), len(problems)),
      "仍有 <60 字符碎片小问的卷：%d 个（碎片通常来自分数/公式换行，属已知抽取噪声）。" % len(frag), ""]
for d in frag[:25]:
    L.append("- %s：题号 %s" % (d["file"], d["fragments"]))
L.append("")
io.open(os.path.join(REP, "extraction_fix_v2_v3.md"), "w", encoding="utf-8").write("\n".join(L))
print("v2", len(prev), "v3", len(problems), "papers", len(diag), "frag_papers", len(frag))
for k in sorted(set(oldc) | set(newc)):
    a, b = oldc.get(k, 0), newc.get(k, 0)
    if a != b: print("  DIFF", k, a, "->", b)
print("rule usage:", dict(collections.Counter(d["rule"] for d in diag)))
