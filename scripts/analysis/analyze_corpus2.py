# -*- coding: utf-8 -*-
"""Yau corpus structural analysis v2."""
import os, io, re, json, itertools, collections

ROOT = r"."
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
for d in (DATA, REP):
    os.makedirs(d, exist_ok=True)

LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl",
       "\u2019":"'","\u2018":"'","\u201c":'"',"\u201d":'"',"\u2013":"-","\u2014":"--","\u00a0":" "}
def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n"))

SUBJ_PATTERNS = [
    ("Algebra & Number Theory", r"algebra"),
    ("Analysis & PDE",          r"analysis"),
    ("Geometry & Topology",     r"geometry|geomtop|geo_topo|geotop"),
    ("Probability & Statistics", r"probab|proba|statistic"),
    ("Mathematical Physics",    r"physic"),
    ("Computational & Applied", r"applied|comput"),
]
def subject_of_filename(name):
    low = name.lower()
    for label, pat in SUBJ_PATTERNS:
        if re.search(pat, low):
            return label
    return "Mixed/Team(multi-subject)"

def year_of(name):
    m = re.match(r"(\d{4})_", name)
    return m.group(1) if m else "????"

def kind_of(name):
    low = name.lower()
    if "soln" in low or "solution" in low: return "solution"
    if "team" in low: return "team"
    return "individual"

PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):：、]?(?=[ \t\n]|$)")

def best_run(text):
    cands = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(text)]
    best = []
    for i, (st, num, en) in enumerate(cands):
        if num != 1:
            continue
        run, want = [cands[i]], 2
        for j in range(i + 1, len(cands)):
            if cands[j][1] == want:
                run.append(cands[j]); want += 1
        if len(run) > len(best):
            best = run
    return best

def cut(text, run):
    out = []
    for idx, (st, num, en) in enumerate(run):
        stop = run[idx + 1][0] if idx + 1 < len(run) else len(text)
        out.append((num, text[en:stop].strip()))
    return out

def split_problems(text, limit=None):
    p = cut(text, best_run(text))
    return p[:limit] if limit else p

HEAD_RE = re.compile(r"(?m)^[ \t]*(Algebra and Number Theory|Analysis and Di.{1,3}erential Equations|"
                     r"Geometry and Topology|Probability and Statistics|"
                     r"Applied.{0,40}(Math|Statistics|Probability).{0,20}|Computational and Applied Mathematics|"
                     r"Mathematical Physics)[ \t]*$")
def split_team(text):
    marks = [(m.start(), m.group(1)) for m in HEAD_RE.finditer(text)]
    out = []
    if len(marks) < 2:
        return [(subject_of_filename(""), n, b) for n, b in split_problems(text)]
    for i, (st, label) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        seg = text[st:stop]
        for n, b in split_problems(seg):
            out.append((subject_of_filename(label.lower()), n, b))
    return out

def shingles(s, k=6):
    w = re.findall(r"[a-z]{3,}", s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(0, len(w)-k+1)))

files = sorted(f for f in os.listdir(TXT) if f.endswith(".txt"))
records, prob_items = [], []
for fn in files:
    name = fn[:-4]
    text = norm(io.open(os.path.join(TXT, fn), encoding="utf-8").read())
    subj, kind, year = subject_of_filename(name), kind_of(name), year_of(name)
    m = re.search(r"\((\d+)\s+problems?\)", text, re.I)
    limit = int(m.group(1)) if m else None
    multi = kind == "team" and text.count("=== page ") >= 5
    src = split_team(text) if multi else [(subj, n, b) for n, b in split_problems(text, limit)]
    items = [{"subject": s, "n": n, "chars": len(b), "head": " ".join(b.split())[:400]} for s, n, b in src]
    records.append({"file": fn, "name": name, "year": year, "subject": subj, "kind": kind,
                    "pages": text.count("=== page "), "chars": len(text),
                    "declared_problems": limit, "n_problems": len(items),
                    "multi_subject": multi, "problems": items})
    if kind != "solution":
        for s, n, b in src:
            prob_items.append({"key": "%s|%s|%s|Q%d" % (year, s.split(" ")[0], name[-16:], n),
                               "year": year, "subject": s, "n": n, "sh": shingles(b)})

json.dump({"papers": records}, io.open(os.path.join(DATA, "papers.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

pairs = []
for a, b in itertools.combinations(prob_items, 2):
    if not a["sh"] or not b["sh"]:
        continue
    inter = len(a["sh"] & b["sh"])
    if inter < 4:
        continue
    j = inter / len(a["sh"] | b["sh"])
    if j >= 0.15:
        pairs.append({"a": a["key"], "b": b["key"], "jaccard": round(j, 3), "shared": inter})
pairs.sort(key=lambda x: -x["jaccard"])
json.dump(pairs[:500], io.open(os.path.join(DATA, "near_duplicates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump([{k: v for k, v in p.items() if k != "sh"} for p in prob_items],
          io.open(os.path.join(DATA, "problems_index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

by_year = collections.defaultdict(collections.Counter)
matrix = collections.defaultdict(collections.Counter)
for r in records:
    d = by_year[r["year"]]
    d["files"] += 1; d["chars"] += r["chars"]
    d["soln" if r["kind"] == "solution" else "papers"] += 1
    if r["kind"] != "solution":
        d["problems"] += r["n_problems"]
        for p in r["problems"]:
            matrix[p["subject"]][r["year"]] += 1

BT = chr(96)
L = ["# Yau 竞赛语料库结构分析 v2（脚本自动生成）\n",
     "数据源：" + BT + "sources/prelim" + BT + "（136 个 PDF）→ PyMuPDF 抽取 → 本报告统计。",
     "脚本：" + BT + "./scripts/analyze_corpus2.py" + BT + "；明细：" + BT + "./data/papers.json" + BT + "。\n",
     "## 1. 逐年总览\n", "| 年份 | 文件 | 试卷 | 解答 | 解析出的题目数 | 字符数 |", "|---|---|---|---|---|---|"]
years = sorted(by_year)
for y in years:
    d = by_year[y]
    L.append("| %s | %d | %d | %d | %d | %d |" % (y, d["files"], d["papers"], d["soln"], d["problems"], d["chars"]))
T = collections.Counter()
for d in by_year.values(): T.update(d)
L.append("| **合计** | **%d** | **%d** | **%d** | **%d** | **%d** |" % (T["files"], T["papers"], T["soln"], T["problems"], T["chars"]))
L += ["", "## 2. 科目 x 年份 题量矩阵（个人赛+团体赛合计）\n",
      "| 科目 | " + " | ".join(years) + " | 合计 |", "|" + "---|" * (len(years) + 2)]
for s in sorted(matrix):
    row = [matrix[s][y] for y in years]
    L.append("| %s | %s | %d |" % (s, " | ".join(str(v) if v else "." for v in row), sum(row)))
L.append("")
L += ["## 3. 单卷题量明细\n", "| 年份 | 文件 | 卷别 | 解析题数 | 声明题数 |", "|---|---|---|---|---|"]
for r in sorted(records, key=lambda x: (x["year"], x["file"])):
    if r["kind"] == "solution": continue
    L.append("| %s | %s | %s | %d | %s |" % (r["year"], r["name"][:46], r["kind"], r["n_problems"], r["declared_problems"] or "-"))
L += ["", "## 4. 跨年近似重复题（词元 6-gram Jaccard >= 0.15）\n",
      "共 %d 对，前 40 对：\n" % len(pairs), "| 题目A | 题目B | Jaccard | 共享 shingle |", "|---|---|---|---|"]
for p in pairs[:40]:
    L.append("| %s | %s | %.3f | %d |" % (p["a"], p["b"], p["jaccard"], p["shared"]))
L.append("")
io.open(os.path.join(REP, "stats_overview.md"), "w", encoding="utf-8").write("\n".join(L))

print("papers", len(records), "problems", T["problems"], "dup_pairs", len(pairs))
for y in years:
    print("year", y, "papers", by_year[y]["papers"], "soln", by_year[y]["soln"], "problems", by_year[y]["problems"])
